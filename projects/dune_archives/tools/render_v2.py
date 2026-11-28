#!/usr/bin/env python3
"""v2 renderer (any episode; EP env var, default DUN003): timeline + stills + maps + motion graphics -> master MP4.

  python tools/render_v2.py --audio MIX.m4a --out OUT.mp4 [--res 1920x1080] [--jobs 4] [--crf 19]
                            [--workdir /tmp/r2] [--abr 320k] [--range 0-60]
  python tools/render_v2.py --stills 12.3,45.6 [--res 1920x1080] [--outdir .cache/qc]     # QC frames

* Shots come from 22_edit/DUN003/v2/DUN003_v2_timeline.json (tools/v2_timeline.py). Cuts are frame-exact.
* Camera: Ken Burns moves whose amount scales with shot length (no fast zooms on short shots).
* Maps: the rendered map clips (last frame held if the slot is longer).
* Graphics: tools/gfx_v2.py layers, composited on the global timeline so they run across cuts.
* Look: vignette (numpy) before the graphics; film grain in the encode. 0.5 s fade-in, 1 s fade-out.
* No disclaimers or labels are burned in. Captions (tools/captions_v2.py) only when D.BURN_CAPTIONS is set.
"""
import argparse, json, math, os, pathlib, subprocess, sys
from concurrent.futures import ProcessPoolExecutor

import cv2
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import gfx_v2 as G  # noqa: E402
import captions_v2 as CAP  # noqa: E402
import imageio_ffmpeg  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 24
OVER = 1.22
E = G.E
TL = json.load(open(E.TIMELINE))
MAPS = E.MAPS
S = {}  # per-process state


def init(W, H, crf, workdir):
    S.update(W=W, H=H, k=H / 1080, crf=crf, wd=pathlib.Path(workdir))
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / math.sqrt(2)
    m = 1 - 0.42 * np.clip(r, 0, 1) ** 2.3
    S['vig'] = np.repeat((m * 255).astype(np.uint8)[..., None], 3, 2)
    S['events'] = [dict(g) for g in TL['graphics']]
    S['cap'] = CAP.Captions(TL, W, H) if getattr(E.D, 'BURN_CAPTIONS', False) else None


def load_plate(path, W, H):
    im = cv2.cvtColor(cv2.imread(str(path), cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
    h, w = im.shape[:2]
    if w / h > W / H:
        nw = int(round(h * W / H)); x0 = (w - nw) // 2; im = im[:, x0:x0 + nw]
    else:
        nh = int(round(w * H / W)); y0 = (h - nh) // 2; im = im[y0:y0 + nh]
    return cv2.resize(im, (int(W * OVER), int(H * OVER)), interpolation=cv2.INTER_LANCZOS4)


def warp(plate, s, cx, cy, W, H):
    h, w = plate.shape[:2]
    vw, vh = (w / OVER) / s, (h / OVER) / s
    left = min(max(cx - vw / 2, 0), w - vw)
    top = min(max(cy - vh / 2, 0), h - vh)
    k = W / vw
    M = np.float32([[k, 0, -left * k], [0, k, -top * k]])
    return cv2.warpAffine(plate, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def cam(recipe, t, dur, pw, ph, focus):
    e = 0.65 * t + 0.35 * (t * t * (3 - 2 * t))
    amt = min(0.13, max(0.035, 0.03 * dur))
    p = min(0.09, max(0.03, 0.016 * dur))
    cx, cy = pw / 2, ph / 2
    fx, fy = focus[0] * pw, focus[1] * ph
    if recipe == 'PUSH_IN':
        return 1 + amt * e, cx + (fx - cx) * e, cy + (fy - cy) * e
    if recipe == 'PULL_OUT':
        return 1 + amt * (1 - e), fx + (cx - fx) * e, fy + (cy - fy) * e
    if recipe == 'PAN_LR':
        return 1.10, pw * (0.5 - p + 2 * p * e), fy
    if recipe == 'PAN_RL':
        return 1.10, pw * (0.5 + p - 2 * p * e), fy
    if recipe == 'TILT_UP':
        return 1.10, fx, ph * (0.5 + p - 2 * p * e)
    if recipe == 'TILT_DN':
        return 1.10, fx, ph * (0.5 - p + 2 * p * e)
    if recipe == 'DRIFT':
        return 1.03 + 0.015 * e, cx + 0.004 * pw * math.sin(math.pi * t) + (fx - cx) * 0.3, cy + (fy - cy) * 0.3
    return 1.02, cx + (fx - cx) * 0.3, cy + (fy - cy) * 0.3  # HOLD


def finish(frame, tg):
    W, H, k = S['W'], S['H'], S['k']
    frame = cv2.multiply(frame, S['vig'], scale=1 / 255.0)
    L, kinds = [], set()
    for ev in S['events']:
        if ev['t0'] <= tg < ev['t1']:
            L += G.layers(ev, tg - ev['t0'], k, W, H)
            kinds.add(ev['kind'])
    if L:
        frame = G.composite(np.ascontiguousarray(frame), L)
    if S.get('cap'):
        frame = S['cap'].apply(np.ascontiguousarray(frame), tg, kinds)
    dur = TL['duration']
    f = min(1.0, tg / 0.5, (dur - tg) / 1.0)
    if f < 1:
        frame = (frame.astype(np.float32) * max(0.0, f)).astype(np.uint8)
    return frame


def frames_for(shot, n):
    W, H = S['W'], S['H']
    if shot['key'].startswith('MAP'):
        p = subprocess.Popen([FF, '-v', 'error', '-i', str(E.MAPDIR / MAPS[shot['key']]),
                              '-vf', f'scale={W}:{H}:flags=lanczos', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             stdout=subprocess.PIPE)
        last = None
        for i in range(n):
            buf = p.stdout.read(W * H * 3)
            if len(buf) == W * H * 3:
                last = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
            yield last
        p.stdout.close(); p.kill(); p.wait()
        return
    plate = load_plate(G.still_path(shot['key']), W, H)
    ph, pw = plate.shape[:2]
    dur = n / FPS
    for i in range(n):
        t = i / max(1, n - 1)
        s, cx, cy = cam(shot['recipe'], t, dur, pw, ph, shot.get('focus', [0.5, 0.5]))
        yield warp(plate, s, cx, cy, W, H)


def render_seg(i):
    shot = TL['shots'][i]
    W, H = S['W'], S['H']
    f0, f1 = round(shot['t0'] * FPS), round(shot['t1'] * FPS)
    out = S['wd'] / f'seg_{i:03d}.mp4'
    if out.exists() and out.stat().st_size > 1000:
        return str(out)
    cmd = [FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-vf', 'format=yuv420p,noise=c0s=3:c0f=t', '-c:v', 'libx264', '-preset', 'medium', '-tune', 'grain', '-x264-params', 'vbv-maxrate=16000:vbv-bufsize=24000', '-crf', str(S['crf']),
           '-pix_fmt', 'yuv420p', '-an', '-video_track_timescale', '12288', str(out) + '.tmp.mp4']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for j, fr in enumerate(frames_for(shot, f1 - f0)):
        p.stdin.write(finish(fr, (f0 + j) / FPS).tobytes())
    p.stdin.close()
    if p.wait():
        raise RuntimeError(f'encode failed: shot {i}')
    os.replace(str(out) + '.tmp.mp4', out)
    return str(out)


def still(t, outdir):
    shot = next(s for s in TL['shots'] if s['t0'] <= t < s['t1'])
    W, H = S['W'], S['H']
    f0, f1 = round(shot['t0'] * FPS), round(shot['t1'] * FPS)
    j = round(t * FPS) - f0
    if shot['key'].startswith('MAP'):
        buf = subprocess.run([FF, '-v', 'error', '-ss', f'{j / FPS:.3f}', '-i',
                              str(E.MAPDIR / MAPS[shot['key']]), '-frames:v', '1', '-vf',
                              f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy() if len(buf) == W * H * 3 else np.zeros((H, W, 3), np.uint8)
    else:
        plate = load_plate(G.still_path(shot['key']), W, H)
        ph, pw = plate.shape[:2]
        n = f1 - f0
        s, cx, cy = cam(shot['recipe'], j / max(1, n - 1), n / FPS, pw, ph, shot.get('focus', [0.5, 0.5]))
        fr = warp(plate, s, cx, cy, W, H)
    fr = finish(fr, t)
    path = pathlib.Path(outdir) / f'qc_{t:07.2f}.jpg'
    cv2.imwrite(str(path), cv2.cvtColor(fr, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 88])
    return str(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--audio'); ap.add_argument('--out')
    ap.add_argument('--res', default='1920x1080'); ap.add_argument('--jobs', type=int, default=2)
    ap.add_argument('--crf', type=int, default=19); ap.add_argument('--workdir', default='/tmp/r2')
    ap.add_argument('--abr', default='320k'); ap.add_argument('--range')
    ap.add_argument('--stills'); ap.add_argument('--outdir', default=str(ROOT / '.cache/qc'))
    a = ap.parse_args()
    W, H = map(int, a.res.split('x'))
    if a.stills:
        pathlib.Path(a.outdir).mkdir(parents=True, exist_ok=True)
        init(W, H, a.crf, a.workdir)
        for t in a.stills.split(','):
            print(still(float(t), a.outdir))
        return
    pathlib.Path(a.workdir).mkdir(parents=True, exist_ok=True)
    idx = list(range(len(TL['shots'])))
    t_lo, t_hi = 0, TL['duration']
    if a.range:
        t_lo, t_hi = map(float, a.range.split('-'))
        idx = [i for i in idx if TL['shots'][i]['t1'] > t_lo and TL['shots'][i]['t0'] < t_hi]
    with ProcessPoolExecutor(a.jobs, initializer=init, initargs=(W, H, a.crf, a.workdir)) as ex:
        segs = list(ex.map(render_seg, idx, chunksize=1))
    lst = pathlib.Path(a.workdir) / 'concat.txt'
    lst.write_text(''.join(f"file '{s}'\n" for s in segs))
    vid = pathlib.Path(a.workdir) / 'video.mp4'
    subprocess.run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(vid)], check=True)
    v0 = round(TL['shots'][idx[0]]['t0'] * FPS) / FPS
    v1 = round(TL['shots'][idx[-1]]['t1'] * FPS) / FPS
    cmd = [FF, '-y', '-v', 'error', '-i', str(vid)]
    if a.audio:
        cmd += ['-ss', f'{v0:.3f}', '-i', a.audio, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', a.abr,
                '-ar', '48000']
    cmd += ['-c:v', 'copy', '-t', f'{v1 - v0:.3f}', '-movflags', '+faststart', a.out]
    subprocess.run(cmd, check=True)
    print('wrote', a.out, 'shots', len(idx), 'duration', round(v1 - v0, 2))


if __name__ == '__main__':
    main()
