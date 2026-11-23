"""Re-time an episode storyboard to the paced VO master.

Usage: python retime_storyboard.py <EP> <master.mp3> [--write]
Needs the ffmpeg binary from pip `imageio-ffmpeg` (see 20_voiceover/DUN003/DUN003_VO_LOG.md).

Method:
  * find silences in the master (silencedetect -38 dB, 0.2 s or longer); speech = the complement
  * chapter windows come from the VO section files, in order, separated by 2.5 s gaps
    (the vo_build.py layout). Combined files (00-01, 09-10) are split by text
    proportion and snapped to the nearest long pause
  * inside a chapter, the character position of each shot's vo_line in the chapter's VO text
    maps to speech-only time, so pauses don't skew it
  * each cut snaps to the middle of the nearest pause (within 1.2 s for sentence starts, 0.6 s otherwise)
  * placeholder shots, "(VO continues / music breath)", split the time between their anchored neighbours evenly
  * the first shot of a chapter starts in the gap before the chapter; the final shot holds 2 s past the VO
Never run build_episode.py afterwards: it regenerates the storyboard with uniform timings.
"""
import csv, io, re, sys, glob, subprocess, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FF = glob.glob('/tmp/mv/lib/python3*/site-packages/imageio_ffmpeg/binaries/ffmpeg-*')[0]
EP, MASTER = sys.argv[1], sys.argv[2]
WRITE = '--write' in sys.argv
GAP, EXTRA, TH = 2.5, 0.4, 0.42  # must match vo_build.py


def silences(f, d=0.2):
    err = subprocess.run([FF, '-hide_banner', '-i', f, '-af', f'silencedetect=noise=-38dB:d={d}', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', err)]
    en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', err)]
    dur = float(re.search(r'Duration: (\d+):(\d+):([\d.]+)', err).groups()[2]) + \
        60 * int(re.search(r'Duration: (\d+):(\d+)', err).group(2)) + 3600 * int(re.search(r'Duration: (\d+)', err).group(1))
    if len(en) < len(st):
        en.append(dur)
    return list(zip(st, en)), dur


def stretched_len(f):
    """Length of a section after vo_build stretching (same rule as vo_build.py)."""
    sil, dur = silences(f, 0.25)
    n = sum(1 for s, e in sil if e - s >= TH and (s + e) / 2 < dur - 0.8)
    return dur + n * EXTRA


def fmt(t):
    t = int(t)
    return f'{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}'


# ---------- script chapters ----------
script = (ROOT / f'17_scripts/{EP}_SCRIPT_v1.0.md').read_text()
chap_text, order = {}, []
for s in re.split(r'\n## ', script)[1:]:
    title = s.split('\n')[0]
    name = re.sub(r'^\d+\. ', '', title.split(' (')[0])
    chap_text[name] = ' '.join(l[4:].strip() for l in s.split('\n') if l.startswith('VO: '))
    order.append(name)

# ---------- section files -> chapter windows ----------
vo_dir = ROOT / f'20_voiceover/{EP}'
files = sorted(vo_dir.glob(f'{EP}_VO_[0-9]*.mp3'))
msil, mdur = silences(MASTER)
speech = []
last = 0.0
for s, e in msil:
    if s > last:
        speech.append((last, s))
    last = e
if last < mdur:
    speech.append((last, mdur))


def speech_bounds(a, b):
    segs = [(max(s, a), min(e, b)) for s, e in speech if e > a and s < b]
    segs = [x for x in segs if x[1] - x[0] > 0.05]
    return segs


windows = {}
off = 0.0
ci = 0
for f in files:
    L = stretched_len(str(f))
    tag = re.match(rf'{EP}_VO_([\d-]+)_', f.name).group(1)
    nums = [int(x) for x in tag.split('-')]
    names = [order[n] for n in range(nums[0], nums[-1] + 1)]
    segs = speech_bounds(off, off + L)
    a, b = segs[0][0], segs[-1][1]
    if len(names) == 1:
        windows[names[0]] = (a, b)
    else:  # split by text proportion over speech time, snap to longest nearby pause
        tot = sum(len(chap_text[n]) for n in names)
        S = sum(e - s for s, e in segs)
        acc, cuts = 0, []
        for n in names[:-1]:
            acc += len(chap_text[n]) + 1
            target, rem = acc / tot * S, acc / tot * S
            for s, e in segs:
                if rem <= e - s:
                    t = s + rem
                    break
                rem -= e - s
            cand = [(s2, e2) for s2, e2 in msil if abs((s2 + e2) / 2 - t) < 4 and e2 - s2 >= 0.6 and a < s2 < b]
            if cand:
                s2, e2 = max(cand, key=lambda x: (x[1] - x[0]) - abs((x[0] + x[1]) / 2 - t) * 0.2)
                cuts.append((s2, e2))
            else:
                cuts.append((t, t))
        prev = a
        for n, (s2, e2) in zip(names, cuts + [(b, b)]):
            windows[n] = (prev, s2)
            prev = e2
    off += L + GAP


def char_to_time(name, pos):
    a, b = windows[name]
    segs = speech_bounds(a, b)
    S = sum(e - s for s, e in segs)
    rem = pos / max(1, len(chap_text[name])) * S
    for s, e in segs:
        if rem <= e - s:
            return s + rem
        rem -= e - s
    return b


def snap(t, lo, hi, radius, minlen):
    best = None
    for s, e in msil:
        if e - s < minlen:
            continue
        m = (s + e) / 2
        if lo < m < hi and abs(m - t) <= radius and (best is None or abs(m - t) < abs(best - t)):
            best = m
    return best if best is not None else t


# ---------- storyboard ----------
sb = ROOT / f'18_storyboards/{EP}_STORYBOARD.csv'
rows = list(csv.reader(io.StringIO(open(sb, newline='').read())))
h = rows[0]
if 'tc_in_s' not in h:
    h.append('tc_in_s')
    for r in rows[1:]:
        r.append('')
I = {k: h.index(k) for k in ('chapter', 'vo_line', 'timecode_in', 'duration_s', 'tc_in_s', 'shot_no')}
body = rows[1:]

starts = [None] * len(body)
prev_end = 0.0
for name in order:
    idx = [i for i, r in enumerate(body) if r[I['chapter']] == name]
    a, b = windows[name]
    T = chap_text[name]
    cursor = 0
    for k, i in enumerate(idx):
        v = body[i][I['vo_line']].strip()
        if k == 0:
            starts[i] = 0.0 if name == order[0] else (prev_end + a) / 2
            if not v.startswith('('):
                cursor = T.find(v) + len(v)
            continue
        if v.startswith('('):
            continue
        p = T.find(v, max(0, cursor - 5))
        if p < 0:
            p = T.find(v)
        t = char_to_time(name, p)
        sentence_start = p == 0 or T[p - 2:p] in ('. ', '? ', '! ')
        starts[i] = snap(t, a - 0.5, b, 1.2 if sentence_start else 0.6, 0.3 if sentence_start else 0.2)
        cursor = p + len(v)
    # placeholders: split evenly between anchored neighbours
    k = 0
    while k < len(idx):
        if starts[idx[k]] is None:
            j = k
            while j < len(idx) and starts[idx[j]] is None:
                j += 1
            lo = starts[idx[k - 1]]
            hi = starts[idx[j]] if j < len(idx) else b
            n = j - k + 1
            for m in range(k, j):
                starts[idx[m]] = lo + (hi - lo) * (m - k + 1) / n
            k = j
        k += 1
    prev_end = b

end = windows[order[-1]][1] + 2.0
# minimum shot length 1.5 s: push later cuts forward (cascade), log the sync shift
MIN = 1.5
synced = list(starts)
for i in range(1, len(starts)):
    if starts[i] - starts[i - 1] < MIN:
        starts[i] = starts[i - 1] + MIN
shifts = [(body[i][I['shot_no']], round(starts[i] - synced[i], 2)) for i in range(len(starts)) if starts[i] - synced[i] > 0.05]
print('cuts pushed later for min length:', shifts)
report = []
for i, r in enumerate(body):
    nxt = starts[i + 1] if i + 1 < len(body) else end
    d = nxt - starts[i]
    if d < 1.5 or d > 10:
        report.append((r[I['shot_no']], r[I['chapter']], round(starts[i], 2), round(d, 2), r[I['vo_line']][:60]))
    r[I['timecode_in']] = fmt(starts[i])
    r[I['duration_s']] = f'{d:.1f}'
    r[I['tc_in_s']] = f'{starts[i]:.2f}'

print('master', round(mdur, 2), 'programme end', round(end, 2))
for n in order:
    print(f'{n:35s} {windows[n][0]:7.2f} - {windows[n][1]:7.2f}')
print('shots outside 1.5-10 s:', len(report))
for x in report:
    print('  ', x)
durs = [float(r[I['duration_s']]) for r in body]
print('min/max/mean', min(durs), max(durs), round(sum(durs) / len(durs), 2))
if WRITE:
    out = io.StringIO()
    csv.writer(out, lineterminator='\r\n').writerows(rows)
    open(sb, 'w', newline='').write(out.getvalue())
    print('written', sb)
