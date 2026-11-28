"""Build data/got003.py SECTIONS from the approved VO plan + the shot plan (tools/plans/got003_plan.py) + GFX below.

    python3 tools/plans/fill_got003.py          (re-runnable: it rewrites only the SECTIONS block)

GOT003 is recorded in 27 takes (c01-c27) that cut across sections, so the timeline sections are the VO-plan
SUBSECTIONS ('Pa', 'Pb', 'Ia', ...). Single-subsection sections keep their plain id ('H', 'CA', 'CB') so the
shared builder (tools/v2_timeline.py) still treats them specially. The chapter number sits only on a chapter's
first subsection, so the CHAPTER card and the YouTube chapter list fire once per chapter.

Plan rows address (section, sentence index within the whole section); they are mapped here to
(subsection, local index). Anchors None = first two words of the sentence.
A subsection whose first sentence has no new shot carries the running shot on (no forced cut).
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'data'), str(ROOT / 'tools/plans')]
import got003_images as I  # noqa: E402
import got003_plan as P  # noqa: E402

VP = json.load(open(ROOT / '20_voiceover/GOT003/GOT003_vo_plan.json'))
NAMES = {'H': 'Hook', 'P': 'Prologue: The Dreamer', 'I': 'Three Dragons', 'II': 'The Field of Fire', 'CA': 'Subscribe',
         'III': 'The Sons of the Dragon', 'IV': 'The Old King and the Good Queen', 'V': 'The Dance of the Dragons',
         'VI': 'The Last Dragon', 'VII': 'The Black Dragon', 'VIII': 'Egg and Summerhall', 'IX': 'The Mad King',
         'X': 'The Last Dragons', 'CB': 'Outro'}
CHAPTERS = {'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'}

N, PL, YR, NOTE, STAT, TTL, END = 'N', 'PL', 'YR', 'NOTE', 'STAT', 'TTL', 'END'
# graphics: (section, sentence idx in the whole section) -> [(anchor, KIND, params, dur)]
GFX = {
    ('H', 13): [('This is', TTL, {'kicker': 'THE MYTHIC ARCHIVES PRESENTS', 'title': 'THE COMPLETE HISTORY OF HOUSE TARGARYEN',
                                  'sub': 'Fire and Blood, from the Doom to the Last Dragon'}, 0)],
    ('CB', 0): [('So who', END, {'kicker': 'WATCH NEXT', 'title': 'THE OTHERS', 'brand': 'A MYTHIC ARCHIVES PRODUCTION',
                                 'sub': 'What the books really say  ·  coming to the archive',
                                 'q': 'WHO WAS THE GREATEST TARGARYEN?', 'q_at': 'Aegon the', 'comment_at': 'comments',
                                 'like_at': 'like', 'sub_at': 'subscribe'}, 0)],
}


def sentences(sec):
    out = []   # [(subsection key, local idx, text)]
    for k, v in VP['subsections'].items():
        if k[:-1] == sec:
            ss = v if isinstance(v, list) else v['sentences']
            out += [(k, i, s) for i, s in enumerate(ss)]
    return out


def sid_of(sub):
    sec = sub[:-1]
    n = sum(1 for k in VP['subsections'] if k[:-1] == sec)
    return sec if n == 1 else sub


def first2(s):
    return ' '.join(s.split()[:2])


def build():
    num = dict(I.NUM)
    shots = {}
    for sid, si, anc, shot, rec in list(P.PLAN) + list(getattr(P, 'CODE_SHOTS', [])):
        if isinstance(shot, str) and shot.startswith('MAP:'):
            n = shot                       # code-animated map / mockup (data/got003.py MAPS)
        else:
            n = num[shot[0]] if isinstance(shot, tuple) else (num[shot] if isinstance(shot, str) else shot)
        shots.setdefault((sid, si), []).append((anc, n, rec))
    out, used, seen_ch = [], set(), set()
    for sec in VP['order']:
        sl = sentences(sec)
        assert sl, sec
        subs = []
        for sub in dict.fromkeys(k for k, _, _ in sl):
            rows = []
            for gi, (k, li, txt) in enumerate(sl):
                if k != sub:
                    continue
                sh = []
                for anc, n, rec in shots.get((sec, gi), []):
                    a = anc or first2(txt)
                    assert a in txt, (sec, gi, a, txt)
                    sh.append((a, n, rec)); used.add(n)
                gf = GFX.get((sec, gi), [])
                for g in gf:
                    assert g[0] in txt, (sec, gi, g[0])
                rows.append((txt, sh, gf))
            ch = sec if (sec in CHAPTERS and sec not in seen_ch) else None
            seen_ch.add(sec)
            subs.append((sid_of(sub), NAMES[sec], ch, rows))
        assert subs[0][3][0][1] or sec != 'H', 'hook needs an opening shot'
        out += subs
    for (sec, gi) in shots:
        assert gi < len(sentences(sec)), ('plan row past section end', sec, gi)
    total = len(I.ROWS)
    missing = sorted(set(range(1, total + 1)) - {u for u in used if isinstance(u, int)})
    return out, missing


def main():
    out, missing = build()
    L = ['SECTIONS = [']
    for sid, name, ch, rows in out:
        L.append(f' ({sid!r}, {name!r}, {ch!r}, [')
        for txt, sh, gf in rows:
            ss = ', '.join(f'({a!r}, {n!r}, {rec!r})' if isinstance(n, str) else f'({a!r}, k({n}), {rec!r})'
                           for a, n, rec in sh)
            gg = ', '.join(f'({g[0]!r}, {g[1]}, {g[2]!r}, {g[3]})' for g in gf)
            L.append(f'  ({txt!r}, [{ss}], [{gg}]),')
        L.append(' ]),')
    L.append(']')
    p = ROOT / 'data/got003.py'
    src = p.read_text()
    a, b = src.index('SECTIONS = ['), src.index('# ---- end SECTIONS')
    p.write_text(src[:a] + '\n'.join(L) + '\n' + src[b:])
    nl = sum(len(r[3]) for r in out)
    print(f'written {len(out)} timeline sections, {nl} lines, {sum(len(x[1]) for r in out for x in r[3])} cuts, '
          f'{sum(len(x[2]) for r in out for x in r[3])} graphics; stills never used: {missing}')


if __name__ == '__main__':
    main()
