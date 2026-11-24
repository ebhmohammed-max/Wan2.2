#!/usr/bin/env python3
"""DUN003 v2 timeline builder: word timestamps -> programme VO, shots, graphics, music EDL, SRT, chapters.

  python tools/v2_timeline.py [--wav OUT.wav]

Inputs : data/dun003_v2.py (script, shots, graphics), 20_voiceover/DUN003/v2/raw14/*.mp3 (voice-14 takes),
         20_voiceover/DUN003/v2/DUN003_v2_words.json (faster-whisper word times, tools/ci_align.py)
Outputs: 22_edit/DUN003/v2/DUN003_v2_timeline.json   shots + graphics + sections + words (programme seconds)
         21_music/DUN003/DUN003_MUSIC_EDL_v2.json     v1 cues and levels, re-timed to the v2 structure
         22_edit/DUN003/v2/DUN003_v2.srt              subtitles (script spelling, spoken timing)
         22_edit/DUN003/v2/DUN003_v2_chapters.txt     YouTube chapter list
         --wav: the programme VO (48 kHz mono) with the edit pauses inserted (CI regenerates it; not committed)

Every cut and graphic is anchored to the first word of its anchor phrase (cut 0.06 s before the word).
The script is the reference for spelling and punctuation. Whisper tokens are matched to script tokens with
difflib; unmatched script words are interpolated between their matched neighbours by character length.
"""
import argparse, difflib, json, pathlib, re, subprocess, sys

import numpy as np
import imageio_ffmpeg

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'data'))
import dun003_v2 as D  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
SR = 48000
VO = ROOT / '20_voiceover/DUN003/v2'
OUT = ROOT / '22_edit/DUN003/v2'
CLIPS = [('H_I', ['H', 'I']), ('II', ['II']), ('CTA_A', ['CA']), ('III', ['III']), ('IV', ['IV']), ('V', ['V']),
         ('VI', ['VI']), ('VII', ['VII']), ('VIII', ['VIII']), ('IX', ['IX']), ('X', ['X']), ('CTA_B', ['CB'])]
LEAD = 0.45          # music before the first word
CH_GAP = 2.4         # silence before a chapter's first word (chapter card)
CH_CARD = 3.3        # chapter card on screen
IDENT_DELAY, IDENT_DUR = 1.4, 4.6
CUT_LEAD = 0.06
MIN_SHOT = 0.6
SENT_PAUSE = 0.55    # minimum pause after a sentence (documentary pace)
SPECIAL_PAUSE = {    # sentence ending -> pause after it (s)
    'he can see the future.': 0.95, 'the galaxy burns.': 0.95, 'it is a gift.': 0.7, 'brought back to life.': 0.6,
    'walk into it anyway.': 0.75, 'won everything.': 0.6, 'he could not.': 0.6, 'utterly demoralized.': 0.75,
    'light.': 1.7, 'paul survives.': 0.95, 'and chani dies.': 3.3, 'the man is gone.': 2.6,
    'scytale falls.': 0.9, 'twins.': 0.6, 'they will break the man.': 0.8, 'is already waiting.': 0.8,
}


def norm(w):
    return re.sub(r'[^a-z0-9]', '', w.lower())


def decode(path):
    pcm = subprocess.run([FF, '-v', 'error', '-i', str(path), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(pcm, np.float32).copy()


def quietest(x, a, b, win=0.02):
    """Clip time of the quietest 20 ms window in [a, b]."""
    i0, i1 = int(a * SR), int(b * SR)
    if i1 - i0 < int(win * SR) * 2:
        return (a + b) / 2
    seg = x[i0:i1] ** 2
    k = int(win * SR)
    c = np.convolve(seg, np.ones(k, np.float32), 'valid') if len(seg) < 400000 else None
    if c is None:
        return (a + b) / 2
    return (i0 + int(np.argmin(c)) + k // 2) / SR


def match(script_tokens, wtoks):
    """script_tokens: [str]; wtoks: [[word, s, e, p]] -> [(s, e)] per script token."""
    merged = []
    for w in wtoks:  # whisper splits Muad'Dib into Muad + 'Dib: glue apostrophe-led pieces back on
        if merged and (w[0].startswith("'") or w[0].startswith('-')):
            merged[-1] = [merged[-1][0] + w[0], merged[-1][1], w[2], w[3]]
        else:
            merged.append(list(w))
    a = [norm(t) for t in script_tokens]
    b = [norm(w[0]) for w in merged]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    times = [None] * len(a)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            times[blk.a + k] = (merged[blk.b + k][1], merged[blk.b + k][2])
    for tag, i1, i2, j1, j2 in sm.get_opcodes():  # same-length replacements (Sital ~ Scytale) map 1:1
        if tag == 'replace' and (i2 - i1) == (j2 - j1):
            for k in range(i2 - i1):
                times[i1 + k] = (merged[j1 + k][1], merged[j1 + k][2])
        elif tag == 'replace' and j2 > j1:     # n:m replacement: spread the span over the script words
            s0, e0 = merged[j1][1], merged[j2 - 1][2]
            L = sum(len(script_tokens[k]) for k in range(i1, i2))
            acc = 0
            for k in range(i1, i2):
                ln = len(script_tokens[k])
                times[k] = (s0 + (e0 - s0) * acc / L, s0 + (e0 - s0) * (acc + ln) / L)
                acc += ln
    matched = sum(t is not None for t in times)
    # interpolate the rest
    n = len(times)
    i = 0
    while i < n:
        if times[i] is not None:
            i += 1
            continue
        j = i
        while j < n and times[j] is None:
            j += 1
        t0 = times[i - 1][1] if i > 0 else (times[j][0] - 0.3 * (j - i) if j < n else 0.0)
        t1 = times[j][0] if j < n else t0 + 0.3 * (j - i)
        L = sum(len(script_tokens[k]) for k in range(i, j))
        acc = 0
        for k in range(i, j):
            ln = len(script_tokens[k])
            times[k] = (t0 + (t1 - t0) * acc / L, t0 + (t1 - t0) * (acc + ln) / L)
            acc += ln
        i = j
    return times, matched


def find_anchor(tokens, anchor):
    at = anchor.split()
    na = [norm(t) for t in at]
    for i in range(len(tokens) - len(at) + 1):
        ok = all(norm(tokens[i + k]) == na[k] for k in range(len(at) - 1)) and \
            norm(tokens[i + len(at) - 1]).startswith(na[-1])
        if ok:
            return i
    raise ValueError(f'anchor {anchor!r} not in {" ".join(tokens)!r}')


def build(wav_out=None):
    words = json.load(open(VO / 'DUN003_v2_words.json'))
    secs = {s[0]: s for s in D.SECTIONS}
    report = []
    seg_audio = {}   # section id -> (np audio, [token dicts with local times])
    for clip, sids in CLIPS:
        x = decode(VO / 'raw14' / f'{clip}.mp3')
        toks = []  # (sid, line_idx, tok_idx, token)
        for sid in sids:
            for li, line in enumerate(secs[sid][3]):
                for ti, tk in enumerate(line[0].split()):
                    toks.append((sid, li, ti, tk))
        times, matched = match([t[3] for t in toks], words[clip])
        report.append(f'{clip:6} script {len(toks):4} words, matched {matched:4} ({100 * matched / len(toks):.0f}%)')
        # section boundaries in this clip
        bounds = []
        for k, sid in enumerate(sids):
            idx = [i for i, t in enumerate(toks) if t[0] == sid]
            s0, e0 = times[idx[0]][0], times[idx[-1]][1]
            bounds.append([max(0.0, s0 - 0.12), min(len(x) / SR, e0 + 0.35), idx])
        for k in range(len(bounds) - 1):
            cut = quietest(x, bounds[k][1] - 0.3, bounds[k + 1][0] + 0.1)
            bounds[k][1] = min(bounds[k][1], cut)
            bounds[k + 1][0] = max(bounds[k + 1][0], cut)
        for (a, b, idx), sid in zip(bounds, sids):
            # pause insertion at sentence ends
            ins = []  # (clip time, extra s)
            for n, i in enumerate(idx[:-1]):
                tk = toks[i][3]
                if not re.search(r'[.?!]["”]?$', tk):
                    continue
                j = idx[n + 1]
                gap = times[j][0] - times[i][1]
                # sentence text (back to previous sentence end) for special pauses
                back = []
                for m in range(n, -1, -1):
                    t = toks[idx[m]][3]
                    if m != n and re.search(r'[.?!]$', t):
                        break
                    back.insert(0, t)
                sent = ' '.join(back).lower()
                target = SENT_PAUSE
                for key, v in SPECIAL_PAUSE.items():
                    if sent.endswith(key):
                        target = v
                extra = max(0.0, target - max(gap, 0.0))
                if extra > 0.005:
                    p = quietest(x, times[i][1] - 0.03, times[j][0] + 0.03)
                    ins.append((p, extra))
            pieces, last = [], a
            for p, e in ins:
                pieces.append(x[int(last * SR):int(p * SR)])
                pieces.append(np.zeros(int(e * SR), np.float32))
                last = p
            pieces.append(x[int(last * SR):int(b * SR)])
            audio = np.concatenate(pieces)

            def local(t, a=a, ins=ins):
                return (t - a) + sum(e for p, e in ins if p < t)
            tl = [dict(sid=toks[i][0], li=toks[i][1], ti=toks[i][2], w=toks[i][3],
                       s=local(times[i][0]), e=local(times[i][1])) for i in idx]
            seg_audio[sid] = (audio, tl)

    # ---- programme layout
    order = [s[0] for s in D.SECTIONS]
    t = LEAD
    sec_info, prog_words, chunks = {}, [], []
    ident = None
    for sid in order:
        sec = secs[sid]
        gap_start = t
        if sec[2]:
            t += CH_GAP
        elif sid == 'CA':
            t += 1.0
        elif sid == 'CB':
            t += 1.2
        audio, tl = seg_audio[sid]
        chunks.append((t, audio))
        for w in tl:
            prog_words.append(dict(w, s=round(w['s'] + t, 3), e=round(w['e'] + t, 3)))
        start = t
        t += len(audio) / SR
        last_word_end = prog_words[-1]['e']
        sec_info[sid] = dict(gap_start=round(gap_start, 3), start=round(start, 3), end=round(t, 3),
                             last_word_end=round(last_word_end, 3), num=sec[2], name=sec[1])
        if sid == 'H':
            ident = (round(last_word_end + IDENT_DELAY, 3), round(last_word_end + IDENT_DELAY + IDENT_DUR, 3))
            t = ident[1]
        if sid == 'CA':
            t += 0.6
    total = round(prog_words[-1]['e'] + D.END_HOLD, 3)

    def wt(sid, li, ti):
        for w in prog_words:
            if w['sid'] == sid and w['li'] == li and w['ti'] == ti:
                return w
        raise KeyError((sid, li, ti))

    def phrase_after(phrase, t0):
        ps = [norm(p) for p in phrase.split()]
        for k in range(len(prog_words) - len(ps) + 1):
            if prog_words[k]['s'] < t0 - 0.01:
                continue
            if all(norm(prog_words[k + m]['w']) == ps[m] for m in range(len(ps) - 1)) and \
                    norm(prog_words[k + len(ps) - 1]['w']).startswith(ps[-1]):
                return prog_words[k]['s']
        raise ValueError(f'phrase {phrase!r} not found after {t0}')

    def phrase_end(phrase):
        ps = [norm(p) for p in phrase.split()]
        for k in range(len(prog_words) - len(ps) + 1):
            if all(norm(prog_words[k + m]['w']) == ps[m] for m in range(len(ps))):
                return prog_words[k + len(ps) - 1]['e']
        raise ValueError(phrase)

    # ---- shots
    shots = []
    for sid in order:
        sec, si = secs[sid], sec_info[sid]
        first = True
        for li, (text, sh, gx) in enumerate(sec[3]):
            toks = text.split()
            for s in sh:
                anchor, key, recipe = s[0], s[1], s[2]
                focus = s[3] if len(s) > 3 else [0.5, 0.5]
                tt = wt(sid, li, find_anchor(toks, anchor))['s'] - CUT_LEAD
                if first:
                    tt = 0.0 if sid == 'H' else si['gap_start']
                    first = False
                shots.append(dict(t0=round(tt, 3), key=key, recipe=recipe, focus=focus, sid=sid, anchor=anchor))
    shots.append(dict(t0=ident[0], key=D.IDENT_SHOT[0], recipe=D.IDENT_SHOT[1], focus=[0.5, 0.5], sid='IDENT',
                      anchor='(ident)'))
    shots.sort(key=lambda s: s['t0'])
    for k, s in enumerate(shots):
        s['t1'] = shots[k + 1]['t0'] if k + 1 < len(shots) else total
    dropped = [s for s in shots if s['t1'] - s['t0'] < MIN_SHOT]
    shots = [s for s in shots if s['t1'] - s['t0'] >= MIN_SHOT]
    for k, s in enumerate(shots):
        s['t1'] = shots[k + 1]['t0'] if k + 1 < len(shots) else total
    # ---- graphics
    gfx = []
    for sid in order:
        sec, si = secs[sid], sec_info[sid]
        if sec[2]:
            gfx.append(dict(kind='CHAPTER', t0=si['gap_start'], t1=round(si['gap_start'] + CH_CARD, 3),
                            p={'num': sec[2], 'title': sec[1]}))
        for li, (text, sh, gx) in enumerate(sec[3]):
            toks = text.split()
            for anchor, kind, params, dur in gx:
                t0 = wt(sid, li, find_anchor(toks, anchor))['s'] - 0.05
                if kind == 'TITLE':
                    t1 = ident[0] + 0.35
                elif kind == 'END':
                    t1 = total
                elif dur == 0:
                    t1 = si['last_word_end'] + 0.5
                else:
                    t1 = t0 + dur
                p = dict(params)
                for k2, v in params.items():
                    if k2.endswith('_at'):
                        p[k2] = round(phrase_after(v, t0) - t0, 3)  # seconds after the event start
                gfx.append(dict(kind=kind, t0=round(t0, 3), t1=round(t1, 3), p=p))
    gfx.append(dict(kind='IDENT', t0=ident[0], t1=ident[1], p=D.IDENT_SHOT[2]))
    gfx.sort(key=lambda g: g['t0'])
    # same-kind graphics never overlap: trim the earlier one
    for k, g in enumerate(gfx):
        for h in gfx[k + 1:]:
            if h['kind'] == g['kind'] and h['t0'] < g['t1']:
                g['t1'] = round(h['t0'] - 0.05, 3)
                break
    # no lower-thirds / notes over map shots (maps carry their own labels)
    maps = [(s['t0'], s['t1']) for s in shots if s['key'].startswith('MAP')]
    for g in gfx:
        for a, b in maps:
            if g['kind'] in ('NAME', 'PLACE', 'NOTE') and a <= g['t0'] < b:
                g['t0'] = round(b, 3)
    gfx = [g for g in gfx if g['t1'] - g['t0'] > 0.8]

    # ---- music EDL v2 (v1 cues, levels and offsets; new times)
    S = sec_info
    light = phrase_after('Light.', S['V']['start'])
    chani = phrase_end('And Chani dies.')
    gone = phrase_end('The man is gone.')
    behind = phrase_after('Behind him', S['IX']['start'])
    E1 = json.load(open(ROOT / '21_music/DUN003/DUN003_MUSIC_EDL.json'))
    v1 = {c['cue']: c for c in E1['cues']}

    def cue(cid, name, start, end, src=None, **over):
        c = dict(v1[src or cid])
        c.update(cue=cid, name=name, start=round(start, 2), end=round(end, 2), **over)
        return c
    cues = [
        cue('M1', 'Throne of Ash (hook)', 0.0, ident[0] + 1.2),
        cue('M2', 'Ident', ident[0] - 1.2, S['I']['gap_start'] + 1.4),
        cue('M3', 'The God on the Throne', S['I']['gap_start'] - 0.4, S['II']['gap_start'] + 0.6),
        cue('M4', 'Arithmetic', S['II']['gap_start'] - 0.6, S['CA']['gap_start'] + 1.0),
        cue('M2b', 'Subscribe (archive theme)', S['CA']['gap_start'] - 0.2, S['III']['gap_start'] + 0.8, src='M2',
            fade_in=1.0, fade_out=2.0),
        cue('M5', 'Four Powers', S['III']['gap_start'] - 0.4, S['IV']['gap_start'] + 0.6),
        cue('M6', 'Ghola', S['IV']['gap_start'] - 0.4, S['V']['gap_start'] + 0.6),
        cue('M7', 'Stone Burner (hard cut on "Light.")', S['V']['gap_start'] - 0.4, light),
        cue('M8', 'Borrowed Sight', S['VI']['gap_start'] - 3.0, S['VII']['gap_start'] + 0.4),
        cue('M9', 'Twins (grief)', chani + 3.0, S['IX']['gap_start'] + 0.8),
        cue('M10', 'Shai-Hulud', S['IX']['gap_start'] - 0.2, gone + 4.0),
        cue('M11', 'The empire goes on', behind - 0.9, S['X']['gap_start'] + 0.6, fade_in=1.2),
        cue('M12', 'Beware of Heroes', S['X']['gap_start'] - 0.6, S['CB']['gap_start'] + 1.6),
        cue('M12b', 'Outro (archive theme)', S['CB']['gap_start'] - 0.6, total, fade_in=2.0, fade_out=3.0),
    ]
    edl = dict(episode='DUN003', timeline=f'v2 storytelling cut, voice-14 VO, programme {total} s',
               bed_lufs=E1['bed_lufs'], notes=E1['notes'] + '. v2: same tracks, offsets, gains and fades as v1, re-timed.',
               cues=cues,
               sfx=[dict(type='wind', start=0.0, end=21.0, level_db=-36, note='low wind in a vast hall (hook)'),
                    dict(type='tinnitus', start=round(light, 2), end=round(light + 16.0, 2), level_db=-30,
                         note='stone burner blindness, hard cut from M7'),
                    dict(type='heartbeat', start=S['VII']['gap_start'], end=round(chani + 0.2, 2), level_db=-24,
                         note="pulse up to 'And Chani dies.', then silence"),
                    dict(type='wind', start=S['IX']['gap_start'], end=round(gone + 4.0, 2), level_db=-34,
                         note='open desert wind under Shai-Hulud')],
               silences=[f'{light:.1f} hard cut to tinnitus', f'{chani:.1f}-{chani + 3.0:.1f} after "And Chani dies."',
                         f'{gone:.1f}-{gone + 4.0:.1f} final chord rings out on "The man is gone."'])
    (ROOT / '21_music/DUN003/DUN003_MUSIC_EDL_v2.json').write_text(json.dumps(edl, indent=1))

    # ---- SRT
    def ts(x):
        h, r = divmod(x, 3600); m, s = divmod(r, 60)
        return f'{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)) % 1000:03d}'
    cues_srt, cur = [], []
    for w in prog_words:
        cur.append(w)
        txt = ' '.join(c['w'] for c in cur)
        if re.search(r'[.?!]$', w['w']) or len(txt) > 70 or (re.search(r',$', w['w']) and len(txt) > 38):
            cues_srt.append(cur); cur = []
    if cur:
        cues_srt.append(cur)
    lines = []
    for n, c in enumerate(cues_srt, 1):
        txt = ' '.join(x['w'] for x in c)
        if len(txt) > 42:
            words_ = txt.split(); half = len(txt) / 2; acc = 0
            for k, ww in enumerate(words_):
                acc += len(ww) + 1
                if acc >= half:
                    txt = ' '.join(words_[:k + 1]) + '\n' + ' '.join(words_[k + 1:]); break
        lines.append(f"{n}\n{ts(c[0]['s'])} --> {ts(c[-1]['e'] + 0.15)}\n{txt}\n")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'DUN003_v2.srt').write_text('\n'.join(lines))
    # ---- chapters
    def mmss(x):
        return f'{int(x // 60)}:{int(x % 60):02d}'
    ch = ['0:00 Prologue: He Can See the Future']
    for sid in order:
        if secs[sid][2]:
            ch.append(f"{mmss(S[sid]['gap_start'])} {secs[sid][2]}. {secs[sid][1]}")
    (OUT / 'DUN003_v2_chapters.txt').write_text('\n'.join(ch) + '\n')

    tl = dict(episode='DUN003', version='v2', duration=total, fps=24, ident=ident, sections=sec_info,
              shots=shots, graphics=gfx, words=[[w['w'], w['s'], w['e']] for w in prog_words])
    (OUT / 'DUN003_v2_timeline.json').write_text(json.dumps(tl, indent=0))

    if wav_out:
        N = int(round(total * SR))
        prog = np.zeros(N, np.float32)
        for t0, a in chunks:
            i0 = int(round(t0 * SR)); prog[i0:i0 + len(a)] += a[:max(0, N - i0)]
        subprocess.run([FF, '-y', '-v', 'error', '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-i', '-',
                        '-c:a', 'pcm_s16le', str(wav_out)], input=prog.tobytes(), check=True)
    print('\n'.join(report))
    print(f'programme {total:.2f} s ({mmss(total)}), shots {len(shots)} (dropped short: '
          f'{[(d["key"], round(d["t1"] - d["t0"], 2)) for d in dropped]}), graphics {len(gfx)}')
    print('\n'.join(ch))
    return tl


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--wav')
    build(ap.parse_args().wav)
