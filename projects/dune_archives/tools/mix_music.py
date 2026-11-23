#!/usr/bin/env python3
"""Build the DUN003 programme mix: VO + music cues + synthesised SFX, ducked and loudness-normalised.

usage: mix_music.py EDL.json VO.mp3 OUT.wav [--tracks DIR] [--duck 8] [--dur 731.42]

* every cue is cut from its source track (offset, start/end), high-passed, normalised to the EDL
  `bed_lufs` (+ per-cue gain_db) and faded;
* SFX (wind / tinnitus / heartbeat) are synthesised here, so there is nothing to license;
* music + SFX are ducked under the VO with a smoothed side-chain envelope (default 8 dB);
* the result is normalised to -14 LUFS integrated / -1 dBTP (two-pass loudnorm) and written as
  48 kHz stereo WAV, plus a music-only stem (OUT_stem_music.wav) for re-edits.
"""
import argparse, json, os, re, subprocess, sys
import numpy as np
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
SR = 48000


def movavg(x, k):
    c = np.cumsum(np.concatenate([[0.0], x.astype(np.float64)]))
    y = (c[k:] - c[:-k]) / k
    pad = len(x) - len(y)
    return np.concatenate([np.full(pad // 2, y[0]), y, np.full(pad - pad // 2, y[-1])]).astype(np.float32)


def decode(path, ss=None, t=None, ch=2, af=None):
    cmd = [FF, '-v', 'error']
    if ss is not None:
        cmd += ['-ss', f'{ss:.3f}']
    if t is not None:
        cmd += ['-t', f'{t:.3f}']
    cmd += ['-i', path]
    if af:
        cmd += ['-af', af]
    cmd += ['-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-']
    x = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32)
    return x.reshape(-1, ch).copy()


def lufs(x):
    p = subprocess.run([FF, '-v', 'info', '-f', 'f32le', '-ac', str(x.shape[1]), '-ar', str(SR), '-i', '-',
                        '-af', 'ebur128', '-f', 'null', '-'], input=x.astype(np.float32).tobytes(),
                       capture_output=True)
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', p.stderr.decode())
    return float(m[-1]) if m else -70.0


def fade(x, fi, fo):
    n = len(x)
    if fi > 0:
        k = min(n, int(fi * SR)); x[:k] *= np.linspace(0, 1, k, dtype=np.float32)[:, None] ** 2
    if fo > 0:
        k = min(n, int(fo * SR)); x[-k:] *= np.linspace(1, 0, k, dtype=np.float32)[:, None] ** 2
    return x


def sfx(kind, dur, rng):
    n = int(dur * SR)
    t = np.arange(n, dtype=np.float32) / SR
    if kind == 'wind':
        w = rng.standard_normal((n, 2)).astype(np.float32)
        # brown-ish noise: integrate + leak, then slow gusts
        for c in range(2):
            w[:, c] = np.cumsum(w[:, c]); w[:, c] -= movavg(w[:, c], 4801)
        w /= np.abs(w).max() + 1e-9
        gust = 0.6 + 0.4 * np.sin(2 * np.pi * t * 0.07 + 1.3) * np.sin(2 * np.pi * t * 0.031)
        return w * gust[:, None]
    if kind == 'tinnitus':
        env = np.minimum(1, t / 0.02) * np.exp(-t / (dur * 0.55))
        s = (np.sin(2 * np.pi * 7400 * t) + 0.3 * np.sin(2 * np.pi * 7417 * t)) * env
        return np.stack([s, s], 1).astype(np.float32)
    if kind == 'heartbeat':
        out = np.zeros(n, np.float32)
        beat = 60 / 62.0
        for b0 in np.arange(0.2, dur - 0.5, beat):
            for off, amp in ((0.0, 1.0), (0.24, 0.7)):
                i0 = int((b0 + off) * SR); m = int(0.18 * SR)
                if i0 + m >= n:
                    continue
                tt = np.arange(m) / SR
                out[i0:i0 + m] += amp * np.sin(2 * np.pi * (52 - 60 * tt) * tt) * np.exp(-tt / 0.045)
        out /= np.abs(out).max() + 1e-9
        return np.stack([out, out], 1)
    raise ValueError(kind)


def envelope(v, attack=0.03, release=0.45):
    """VO side-chain: 20 ms RMS, attack/release smoothed, 0..1."""
    win = int(0.02 * SR)
    p = movavg(v ** 2, win)
    db = 10 * np.log10(p + 1e-10)
    act = np.clip((db + 50) / 12, 0, 1)        # ~-50 dBFS = silence, ~-38 dBFS and up = speech
    # hold small gaps between words so the bed doesn't pump
    hop = int(0.01 * SR); a = act[::hop]
    hold = int(0.35 / 0.01); out = np.zeros_like(a); last = -10 ** 9
    for i, v_ in enumerate(a):
        if v_ > 0.5:
            last = i
        out[i] = 1.0 if i - last <= hold else v_
    ka, kr = 1 - np.exp(-0.01 / attack), 1 - np.exp(-0.01 / release)
    sm = np.zeros_like(out); g = 0.0
    for i, v_ in enumerate(out):
        g += (ka if v_ > g else kr) * (v_ - g); sm[i] = g
    return np.repeat(sm, hop)[:len(v)]


def loudnorm(inp, out, I=-14.0, TP=-1.0, LRA=11.0):
    p = subprocess.run([FF, '-v', 'info', '-i', inp, '-af', f'loudnorm=I={I}:TP={TP}:LRA={LRA}:print_format=json',
                        '-f', 'null', '-'], capture_output=True, text=True)
    js = json.loads(p.stderr[p.stderr.rindex('{'):p.stderr.rindex('}') + 1])
    af = (f"loudnorm=I={I}:TP={TP}:LRA={LRA}:measured_I={js['input_i']}:measured_TP={js['input_tp']}:"
          f"measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
    subprocess.run([FF, '-y', '-v', 'error', '-i', inp, '-af', af, '-ar', str(SR), '-c:a', 'pcm_s16le', out], check=True)
    return js


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('edl'); ap.add_argument('vo'); ap.add_argument('out')
    ap.add_argument('--tracks', default=None)
    ap.add_argument('--duck', type=float, default=8.0)
    ap.add_argument('--dur', type=float, default=None)
    a = ap.parse_args()
    E = json.load(open(a.edl))
    tracks = a.tracks or os.path.join(os.path.dirname(a.edl), 'tracks')
    vo = decode(a.vo, ch=1)[:, 0]
    dur = a.dur or max(len(vo) / SR, max(c['end'] for c in E['cues']))
    N = int(round(dur * SR))
    vo = np.pad(vo, (0, max(0, N - len(vo))))[:N]
    bed = np.zeros((N, 2), np.float32)
    report = []
    for c in E['cues']:
        d = c['end'] - c['start']
        hp = c.get('hp', 40)
        x = decode(os.path.join(tracks, c['track'] + '.mp3'), ss=c['offset'], t=d, af=f'highpass=f={hp}')
        L = lufs(x)
        g = 10 ** ((E['bed_lufs'] - L + c.get('gain_db', 0)) / 20)
        x = fade(x * g, c['fade_in'], c['fade_out'])
        i0 = int(round(c['start'] * SR)); i1 = min(N, i0 + len(x))
        bed[i0:i1] += x[:i1 - i0]
        report.append(f"{c['cue']:5} {c['track']:20} {c['start']:7.2f}-{c['end']:7.2f} src@{c['offset']:6.1f}s  "
                      f"measured {L:6.1f} LUFS -> gain {20*np.log10(g):+5.1f} dB")
    rng = np.random.default_rng(10191)
    for s in E.get('sfx', []):
        x = sfx(s['type'], s['end'] - s['start'], rng)
        x = fade(x * 10 ** (s['level_db'] / 20), 0.05 if s['type'] != 'wind' else 2.0, 1.5)
        i0 = int(round(s['start'] * SR)); i1 = min(N, i0 + len(x))
        bed[i0:i1] += x[:i1 - i0]
    env = envelope(vo)
    gain = 10 ** (-a.duck * env / 20)
    ducked = bed * gain[:, None].astype(np.float32)
    mix = ducked + vo[:, None]
    tmp = a.out + '.pre.wav'
    for arr, path in ((mix, tmp), (ducked, a.out.replace('.wav', '_stem_music.wav'))):
        subprocess.run([FF, '-y', '-v', 'error', '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-i', '-',
                        '-c:a', 'pcm_s16le' if path != tmp else 'pcm_f32le', path],
                       input=arr.astype(np.float32).tobytes(), check=True)
    js = loudnorm(tmp, a.out)
    os.remove(tmp)
    print('\n'.join(report))
    print(f"pre-norm: I={js['input_i']} LUFS TP={js['input_tp']} LRA={js['input_lra']}  -> -14 LUFS / -1 dBTP")
    print('wrote', a.out, f'{dur:.2f}s')


if __name__ == '__main__':
    main()
