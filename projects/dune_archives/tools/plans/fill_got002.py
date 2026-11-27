"""Fill data/got002.py SECTIONS shots (from tools/plans/got002_plan.py) and graphics (GFX below).
Run once after all 150 stills PASS:  python3 tools/plans/fill_got002.py
Anchors: None in the plan = first two words of the sentence. Graphics anchored a few words into a chapter's
first sentence so they do not collide with the CHAPTER card.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'data'), str(ROOT / 'tools/plans')]
import got002 as D  # noqa: E402
import got002_images as I  # noqa: E402
import got002_plan as P  # noqa: E402

N, PL, YR, NOTE, STAT, TTL, END = 'N', 'PL', 'YR', 'NOTE', 'STAT', 'TTL', 'END'

GFX = {
    ('H', 8): [("So who", TTL, {"kicker": "THE MYTHIC ARCHIVES PRESENTS", "title": "BEFORE THE FIRST MEN",
                                "sub": "The Ancient World of Westeros"}, 0)],
    ('P', 0): [("Bran Stark", PL, {"place": "WINTERFELL", "sub": "A Game of Thrones · the first book"}, 4.0)],
    ('P', 2): [("Maester Luwin", N, {"name": "MAESTER LUWIN", "role": "Maester of Winterfell"}, 3.2)],
    ('P', 4): [("the maester", NOTE, {"head": "IN THE BOOKS", "body": "A Game of Thrones: Bran's lessons with Maester Luwin."}, 4.4)],
    ('P', 11): [("Osha,", N, {"name": "OSHA", "role": "Wildling · prisoner at Winterfell"}, 3.2)],
    ('I', 5): [("only three", STAT, {"value": 3, "label": "FINGERS AND A THUMB", "sub": "Black claws instead of nails"}, 3.4)],
    ('I', 9): [("Obsidian.", N, {"name": "OBSIDIAN", "role": "Volcanic glass · dragonglass"}, 2.8)],
    ('I', 14): [("The greenseers.", N, {"name": "THE GREENSEERS", "role": "Eyes green as moss, or red as blood"}, 3.2)],
    ('I', 17): [("ten to", N, {"name": "THE GIANTS", "role": "Ten to fourteen feet tall · mammoth riders"}, 3.4)],
    ('I', 19): [("a giant's", NOTE, {"head": "THE MAESTERS' HISTORIES", "body": "A giant's grave in the North, obsidian arrowheads still lodged in its ribs."}, 4.6)],
    ('II', 0): [("the Arm", PL, {"place": "THE ARM OF DORNE", "sub": "The land bridge to the east"}, 3.2)],
    ('II', 5): [("bronze swords", N, {"name": "THE FIRST MEN", "role": "Bronze, horses, and their own gods"}, 3.2)],
    ('II', 3): [("twelve thousand", YR, {"year": "12,000 YEARS AGO", "sub": "Or eight, say others · the First Men cross"}, 3.6)],
    ('III', 3): [("Brandon of", N, {"name": "BRANDON OF THE BLOODY BLADE", "role": "Legendary hero of the First Men"}, 3.6)],
    ('III', 6): [("called down", NOTE, {"head": "LEGEND", "body": "The Hammer of the Waters: the greenseers break the Arm of Dorne."}, 4.2)],
    ('III', 10): [("the Stepstones.", PL, {"place": "THE STEPSTONES", "sub": "What remains of the Arm of Dorne"}, 4.0)],
    ('III', 14): [("Moat Cailin,", PL, {"place": "MOAT CAILIN", "sub": "The Children's Tower · the Neck"}, 4.0)],
    ('IV', 1): [("called the", PL, {"place": "THE GODS EYE", "sub": "The Isle of Faces · the riverlands"}, 4.0)],
    ('IV', 8): [("the green", N, {"name": "THE GREEN MEN", "role": "Guardians of the Isle of Faces"}, 3.2)],
    ('IV', 10): [("four thousand", STAT, {"value": 4000, "label": "YEARS OF FRIENDSHIP", "sub": "The Pact · the Age of Heroes"}, 3.4)],
    ('IV', 14): [("a hundred", STAT, {"value": 100, "label": "OBSIDIAN DAGGERS", "sub": "Every year, says the Night's Watch"}, 3.1)],
    ('V', 1): [("The Andals.", N, {"name": "THE ANDALS", "role": "Iron, steel, and the Seven"}, 3.0)],
    ('V', 6): [("called High", PL, {"place": "HIGH HEART", "sub": "The riverlands"}, 2.8)],
    ('V', 7): [("thirty-one", STAT, {"value": 31, "label": "WEIRWOOD STUMPS", "sub": "High Heart"}, 3.0)],
    ('V', 8): [("The songs", NOTE, {"head": "THE SONGS", "body": "Told in the songs. Not every history in the books agrees."}, 4.4)],
    ('VI', 0): [("have skin", NOTE, {"head": "THE SHOW", "body": "Game of Thrones on HBO, season 6. Not in the books."}, 5.0)],
    ('VI', 4): [("None of", NOTE, {"head": "IN THE BOOKS", "body": "The children never create the Others. Where the Others came from is never said."}, 5.0)],
    ('VII', 1): [("They save", NOTE, {"head": "IN THE BOOKS", "body": "A Dance with Dragons: Bran's chapters beyond the Wall."}, 4.4)],
    ('VII', 2): [("called Leaf.", N, {"name": "LEAF", "role": "One of those who sing the song of earth"}, 3.2)],
    ('VII', 7): [("the last", N, {"name": "THE LAST GREENSEER", "role": "Half swallowed by a weirwood"}, 3.4)],
    ('VII', 19): [("On a", PL, {"place": "THE FIST OF THE FIRST MEN", "sub": "Beyond the Wall · above the Milkwater"}, 4.0)],
    ('VII', 20): [("Samwell Tarly", N, {"name": "SAMWELL TARLY", "role": "Brother of the Night's Watch"}, 3.2)],
    ('VII', 21): [("eight thousand", STAT, {"value": 8000, "label": "YEARS IN THE GROUND", "sub": "The children's glass"}, 3.2)],
    ('CB', 0): [("So, who", END, {"kicker": "WATCH NEXT", "title": "THE OTHERS", "brand": "A MYTHIC ARCHIVES PRODUCTION",
                                  "sub": "What the books really say  ·  coming to the archive",
                                  "q": "INVADERS — OR GUARDIANS?", "q_at": "Were the", "comment_at": "comments",
                                  "like_at": "Like", "sub_at": "subscribe"}, 0)],
}
KIND = {'N': 'N', 'PL': 'PL', 'YR': 'YR', 'NOTE': 'NOTE', 'STAT': 'STAT', 'TTL': 'TTL', 'END': 'END'}


def first2(s):
    return ' '.join(s.split()[:2])


def main():
    num = dict(I.NUM)
    for n, slug, *_ in P.B1:
        num[slug] = n
    shots = {}
    for sid, si, anc, shot, rec in P.PLAN:
        if isinstance(shot, tuple):
            n = num[shot[0]]
        elif isinstance(shot, str):
            n = num[shot]
        else:
            n = shot
        shots.setdefault((sid, si), []).append((anc, n, rec))
    used, out = set(), []
    for sid, name, ch, lines in D.SECTIONS:
        rows = []
        for i, (txt, _, _) in enumerate(lines):
            sh = []
            for anc, n, rec in shots.get((sid, i), []):
                a = anc or first2(txt)
                assert a in txt, (sid, i, a)
                sh.append((a, n, rec)); used.add(n)
            gf = GFX.get((sid, i), [])
            for g in gf:
                assert g[0] in txt, (sid, i, g[0])
                for kk in ('q_at', 'comment_at', 'like_at', 'sub_at'):
                    if kk in g[2]:
                        assert any(g[2][kk] in l[0] for l in lines), (kk, g[2][kk])
            rows.append((txt, sh, gf))
        assert rows[0][1], f'section {sid} has no opening shot'
        out.append((sid, name, ch, rows))
    missing = sorted(set(range(1, 150)) - used)
    print('stills never used in the timeline:', missing)

    def r(x):
        return repr(x).replace("'", '"') if False else repr(x)
    L = ['SECTIONS = [']
    for sid, name, ch, rows in out:
        L.append(f' ({sid!r}, {name!r}, {ch!r}, [')
        for txt, sh, gf in rows:
            ss = ', '.join(f'({a!r}, k({n}), {rec!r})' for a, n, rec in sh)
            gg = ', '.join(f'({g[0]!r}, {KIND[g[1]]}, {g[2]!r}, {g[3]})' for g in gf)
            L.append(f'  ({txt!r}, [{ss}], [{gg}]),')
        L.append(' ]),')
        L.append('')
    L.append(']')
    p = ROOT / 'data/got002.py'
    src = p.read_text()
    a = src.index('SECTIONS = [')
    b = src.index('# one take')
    src = src[:a] + '\n'.join(L) + '\n\n' + src[b:]
    if 'IDENT_SHOT' not in src:
        src = src.replace('END_HOLD = 6.0', 'IDENT_SHOT = (k(150), "PUSH_IN", {"title": "THE MYTHIC ARCHIVES", "tag": "WESTEROS  •  ARRAKIS  •  MIDDLE-EARTH",\n'
                          '                                   "sub": "A MYTHIC ARCHIVES PRODUCTION  ·  WESTEROS  ·  RECORD 002"})\nEND_HOLD = 6.0', 1)
    p.write_text(src)
    print('written', sum(len(r[3]) for r in out), 'lines;', sum(len(x[1]) for r in out for x in r[3]), 'cuts;',
          sum(len(x[2]) for r in out for x in r[3]), 'graphics')


if __name__ == '__main__':
    main()
