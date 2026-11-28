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

STILLS = ROOT / '19_batches/GOT003/stills_jpg'
PENDING = []
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
    # ---- lower-thirds and cards (turn 142): names, places, years, notes, stats - book-first
    ('P', 1): [('In the books', NOTE, {'head': 'IN THE BOOKS', 'body': 'Fire & Blood: a history written inside the story by an archmaester of the Citadel.'}, 4.6)],
    ('P', 6): [('named Mushroom', N, {'name': 'MUSHROOM', 'role': 'Court fool · self-declared eyewitness'}, 3.2)],
    ('P', 10): [('the Freehold', PL, {'place': 'VALYRIA', 'sub': 'The Valyrian Freehold · Essos'}, 3.4)],
    ('P', 18): [('Daenys the', N, {'name': 'DAENYS THE DREAMER', 'role': 'Daughter of Lord Aenar Targaryen'}, 3.2)],
    ('P', 22): [('westernmost outpost', PL, {'place': 'DRAGONSTONE', 'sub': 'Westernmost outpost of Valyria'}, 3.4)],
    ('P', 35): [('the Doom', YR, {'year': '114 BC', 'sub': 'The Doom of Valyria · before the Conquest'}, 3.4)],
    ('P', 42): [('Century of', NOTE, {'head': 'THE CENTURY OF BLOOD', 'body': 'A hundred years of war between the Free Cities after the Doom.'}, 4.2)],
    ('I', 8): [('Visenya, the', N, {'name': 'VISENYA TARGARYEN', 'role': 'The elder sister · rider of Vhagar'}, 3.2)],
    ('I', 11): [('Rhaenys, the', N, {'name': 'RHAENYS TARGARYEN', 'role': 'The younger sister · rider of Meraxes'}, 3.2)],
    ('I', 15): [('Aegon himself', N, {'name': 'AEGON TARGARYEN', 'role': 'Later: Aegon the Conqueror'}, 3.2)],
    ('I', 22): [('Balerion, the', N, {'name': 'BALERION', 'role': 'The Black Dread · last to have seen Valyria'}, 3.4)],
    ('I', 27): [('In the first', NOTE, {'head': 'IN THE BOOKS', 'body': "A Game of Thrones: Arya among the dragon skulls beneath the Red Keep."}, 4.6)],
    ('I', 50): [('Argilac the', N, {'name': 'ARGILAC THE ARROGANT', 'role': 'The last Storm King'}, 3.2)],
    ('I', 53): [('In the show', NOTE, {'head': 'THE SHOW', 'body': "House of the Dragon: Aegon's dream of the coming winter. Not in the books."}, 5.0)],
    ('II', 5): [('Westeros still', YR, {'year': '1 AC', 'sub': 'Years are counted After the Conquest'}, 3.6)],
    ('II', 9): [('Harren the Black had', N, {'name': 'HARREN THE BLACK', 'role': 'King of the Isles and the Rivers'}, 3.2)],
    ('II', 24): [('Harrenhal still', PL, {'place': 'HARRENHAL', 'sub': 'Five towers · melted by dragonfire'}, 3.6)],
    ('II', 27): [('Orys Baratheon', N, {'name': 'ORYS BARATHEON', 'role': "Aegon's half-brother · first of House Baratheon"}, 3.4)],
    ('II', 34): [('fifty-five thousand', STAT, {'value': 55000, 'label': 'MEN AGAINST THE DRAGONS', 'sub': 'Lannister and Gardener'}, 3.4)],
    ('II', 43): [('four thousand', STAT, {'value': 4000, 'label': 'MEN BURNED', 'sub': 'The Field of Fire'}, 3.2)],
    ('II', 55): [('Torrhen Stark', N, {'name': 'TORRHEN STARK', 'role': 'King in the North · the King Who Knelt'}, 3.4)],
    ('II', 92): [('thirty-seven', STAT, {'value': 37, 'label': 'YEARS ON THE IRON THRONE', 'sub': 'Aegon I · died in his bed'}, 3.2)],
    ('III', 2): [('Aenys, the son', N, {'name': 'AENYS I', 'role': 'Son of Aegon and Rhaenys'}, 3.2)],
    ('III', 3): [('Maegor, the son', N, {'name': 'MAEGOR', 'role': 'Son of Aegon and Visenya'}, 3.0)],
    ('III', 10): [('holy orders', N, {'name': 'THE FAITH MILITANT', 'role': "The Warrior's Sons · the Poor Fellows"}, 3.4)],
    ('III', 24): [('Black Brides', NOTE, {'head': 'THE BLACK BRIDES', 'body': 'Three of Maegor\'s six wives, wed on a single day.'}, 4.0)],
    ('IV', 1): [('His name was', N, {'name': 'JAEHAERYS I', 'role': 'The Conciliator · reigned 55 years'}, 3.4)],
    ('IV', 5): [('his sister Alysanne', N, {'name': 'QUEEN ALYSANNE', 'role': 'The Good Queen · rider of Silverwing'}, 3.4)],
    ('IV', 10): [('named Barth', N, {'name': 'SEPTON BARTH', 'role': 'Hand of the King'}, 3.0)],
    ('IV', 21): [('the New Gift', PL, {'place': 'THE NEW GIFT', 'sub': "Alysanne's lands for the Night's Watch"}, 3.4)],
    ('IV', 31): [('Great Council', YR, {'year': '101 AC', 'sub': 'The Great Council at Harrenhal'}, 3.4)],
    ('V', 2): [('He also', N, {'name': 'VISERYS I', 'role': 'Grandson of Jaehaerys'}, 3.0)],
    ('V', 6): [("Realm's Delight", N, {'name': 'RHAENYRA TARGARYEN', 'role': "The Realm's Delight"}, 3.2)],
    ('V', 11): [('Alicent Hightower', N, {'name': 'QUEEN ALICENT', 'role': 'Of House Hightower'}, 3.2)],
    ('V', 27): [('called Caraxes', N, {'name': 'PRINCE DAEMON', 'role': 'The Rogue Prince · rider of Caraxes'}, 3.4)],
    ('V', 36): [('a sapphire', N, {'name': 'PRINCE AEMOND', 'role': 'One eye · rider of Vhagar'}, 3.2)],
    ('V', 38): [('hundred and twenty-ninth', YR, {'year': '129 AC', 'sub': 'Death of Viserys I'}, 3.2)],
    ('V', 63): [('named Nettles', N, {'name': 'NETTLES', 'role': 'Dragonseed · rider of Sheepstealer'}, 3.2)],
    ('V', 65): [('In the show', NOTE, {'head': 'THE SHOW', 'body': 'House of the Dragon season 3 ended at Tumbleton, August 2026.'}, 4.6)],
    ('VI', 5): [('The realm called', N, {'name': 'AEGON III', 'role': 'The Broken King · the Dragonbane'}, 3.2)],
    ('VI', 16): [('King Daeron the First', N, {'name': 'DAERON I', 'role': 'The Young Dragon'}, 3.0)],
    ('VI', 25): [('Baelor the Blessed', N, {'name': 'BAELOR I', 'role': 'Baelor the Blessed · septon and king'}, 3.2)],
    ('VI', 36): [('In the show', NOTE, {'head': 'THE SHOW', 'body': 'Cersei destroys the Great Sept. In the books it still stands.'}, 4.4)],
    ('VI', 40): [('His name was', N, {'name': 'AEGON IV', 'role': 'Aegon the Unworthy'}, 3.0)],
    ('VII', 2): [('He was called', N, {'name': 'DAERON II', 'role': 'Daeron the Good'}, 3.0)],
    ('VII', 17): [('He took a new', N, {'name': 'DAEMON BLACKFYRE', 'role': 'The Black Dragon'}, 3.2)],
    ('VII', 21): [('Redgrass Field', YR, {'year': '196 AC', 'sub': 'Battle of the Redgrass Field'}, 3.2)],
    ('VII', 26): [('Brynden Rivers', N, {'name': 'BRYNDEN RIVERS', 'role': 'Bloodraven'}, 3.2)],
    ('VII', 33): [('The Golden Company', N, {'name': 'THE GOLDEN COMPANY', 'role': 'Founded by Bittersteel'}, 3.0)],
    ('VII', 35): [('Five rebellions', STAT, {'value': 5, 'label': 'BLACKFYRE REBELLIONS', 'sub': '196 AC to 260 AC'}, 3.2)],
    ('VII', 49): [('In the books', NOTE, {'head': 'IN THE BOOKS', 'body': 'A Dance with Dragons: the last greenseer beneath the hill.'}, 4.4)],
    ('VIII', 4): [('three short tales', NOTE, {'head': 'IN THE BOOKS', 'body': 'Tales of Dunk and Egg: The Hedge Knight, The Sworn Sword, The Mystery Knight.'}, 4.8)],
    ('VIII', 14): [('King Aegon the Fifth', N, {'name': 'AEGON V', 'role': 'Aegon the Unlikely · "Egg"'}, 3.2)],
    ('VIII', 24): [('Ser Duncan', N, {'name': 'SER DUNCAN THE TALL', 'role': 'Lord Commander of the Kingsguard'}, 3.2)],
    ('VIII', 27): [('Summerhall', PL, {'place': 'SUMMERHALL', 'sub': '259 AC · the tragedy'}, 3.4)],
    ('VIII', 46): [('His name was', N, {'name': 'RHAEGAR TARGARYEN', 'role': 'Born in grief and smoke'}, 3.2)],
    ('IX', 0): [('at eighteen', N, {'name': 'AERYS II', 'role': 'Later: the Mad King'}, 3.2)],
    ('IX', 1): [('Tywin Lannister', N, {'name': 'TYWIN LANNISTER', 'role': 'Hand of the King · 20 years'}, 3.2)],
    ('IX', 8): [('A minor lord', PL, {'place': 'DUSKENDALE', 'sub': 'Six months a captive king'}, 3.4)],
    ('IX', 20): [('two hundred and eighty-first', YR, {'year': '281 AC', 'sub': 'The tourney at Harrenhal'}, 3.2)],
    ('IX', 35): [('Ruby Ford', PL, {'place': 'THE RUBY FORD', 'sub': 'The Trident · 283 AC'}, 3.2)],
    ('IX', 45): [('In the books', NOTE, {'head': 'IN THE BOOKS', 'body': 'A Storm of Swords: Jaime tells Brienne the truth.'}, 4.4)],
    ('X', 6): [('Daenerys Stormborn', N, {'name': 'DAENERYS STORMBORN', 'role': 'Born on Dragonstone in a storm'}, 3.2)],
    ('X', 11): [('beggar king', N, {'name': 'VISERYS', 'role': 'The beggar king'}, 3.0)],
    ('X', 26): [('The first dragons', STAT, {'value': 150, 'label': 'YEARS WITHOUT DRAGONS', 'sub': 'Nearly a century and a half'}, 3.4)],
    ('X', 32): [('Old Maester Aemon', N, {'name': 'MAESTER AEMON', 'role': "Egg's brother · the last Targaryen at the Wall"}, 3.4)],
    ('X', 36): [('called Griff', N, {'name': 'YOUNG GRIFF', 'role': "Claims to be Rhaegar's son · A Dance with Dragons"}, 3.4)],
    ('X', 45): [('In the show', NOTE, {'head': 'THE SHOW', 'body': 'Jon is confirmed as the son of Rhaegar and Lyanna. In the books it is a theory.'}, 5.0)],
    ('X', 52): [('The Winds', NOTE, {'head': 'STATUS · NOV 2026', 'body': 'The Winds of Winter and Fire & Blood volume 2 are unpublished.'}, 4.6)],
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
    slugs = [r[0] for r in [x[3] for x in P.PLAN if isinstance(x[3], tuple)]]
    dup = sorted({x for x in slugs if slugs.count(x) > 1})
    assert not dup, f'duplicate still slugs in the plan (string refs would resolve to the wrong still): {dup}'
    shots = {}
    for sid, si, anc, shot, rec in list(P.PLAN) + list(getattr(P, 'CODE_SHOTS', [])) + list(getattr(P, 'RECAP_SHOTS', [])):
        if isinstance(shot, str) and shot.startswith('MAP:'):
            n = shot                       # code-animated map / mockup (data/got003.py MAPS)
        else:
            n = num[shot[0]] if isinstance(shot, tuple) else (num[shot] if isinstance(shot, str) else shot)
            if not list(STILLS.glob(f'GOT003_BATCH*_SCENE{n:03d}_*.jpg')):
                PENDING.append(n)          # not generated / not PASS yet: leave it out so renders never break
                continue
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
    missing = sorted(set(range(1, total + 1)) - {u for u in used if isinstance(u, int)} - set(PENDING))
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
          f'{sum(len(x[2]) for r in out for x in r[3])} graphics; stills never used: {missing}; '
          f'pending (skipped): {sorted(PENDING)}')


if __name__ == '__main__':
    main()
