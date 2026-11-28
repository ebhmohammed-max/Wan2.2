"""List GOT003 shots that hold too long (default > 9 s), with the sentences they cover (section-level index, as
used by tools/plans/got003_plan.py rows), so gap-fill stills can be planned where they are needed most.
    python3 tools/plans/got003_gaps.py [min_s] [limit]
Needs 22_edit/GOT003/GOT003_timeline.json (EP=GOT003 tools/v2_timeline.py)."""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
tl = json.load(open(ROOT / '22_edit/GOT003/GOT003_timeline.json'))
VP = json.load(open(ROOT / '20_voiceover/GOT003/GOT003_vo_plan.json'))
mn = float(sys.argv[1]) if len(sys.argv) > 1 else 9.0
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 40
# sentence start times: rebuild from words (sid, li) order
sent = []   # (t0, sec, gidx, text)
idx = {}
for sub, v in VP['subsections'].items():
    sec = sub[:-1]
    for s in (v if isinstance(v, list) else v['sentences']):
        idx.setdefault(sec, []).append(s)
words = tl['words']
wi = 0
for sec in VP['order']:
    for gi, s in enumerate(idx[sec]):
        sent.append((words[wi][1], sec, gi, s))
        wi += len(s.split())
assert wi == len(words), (wi, len(words))
sh = sorted(tl['shots'], key=lambda s: s['t0'] - s['t1'])
tot = 0
for s in sh[:lim]:
    L = s['t1'] - s['t0']
    if L < mn:
        break
    inside = [x for x in sent if s['t0'] - 0.1 <= x[0] < s['t1'] - 0.3]
    print(f"{L:5.1f}s  {s['key']}  {s['sid']}  @{s['t0']:.0f}s")
    for t0, sec, gi, txt in inside:
        print(f"     {sec}{gi:<3} +{t0 - s['t0']:5.1f}  {txt[:120]}")
    tot += 1
