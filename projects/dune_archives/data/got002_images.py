"""GOT002 (Before the First Men: The Ancient World of Westeros) image plan: look-book + batches of 10.

Book-first visuals: worlds/westeros/WESTEROS_BOOK_LOOKS.md + WESTEROS_CANON_POLICY.md (+ GOT002 script visual rules).
Prompt = STYLE + subject (+ cast anchors) + palette + camera + NO_TEXT.
Batch 1 = character reference portraits + the heart tree (later batches pass them as refs).
Children of the forest = the BOOK look (dappled nut-brown skin, cat eyes, 3 fingers + thumb, black claws),
NOT the HBO bark-and-leaf design. No actor likeness. Refs 'GOT001:<n>' point at approved GOT001 stills.
SHOTS are generated from tools/plans/got002_plan.py (shot order = script order).
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / '19_batches/GOT002'
sys.path.insert(0, str(ROOT / 'tools/plans'))

STYLE = ('ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, fine film grain, '
         'full-bleed wide 16:9 cinematic frame, important action in the central band.')
PALETTE = ('Ancient Westeros palette: weirwood bone-white and blood-red leaves, deep moss green and forest gold, '
           'bronze and firelight, storm grey sea; volumetric light, mist or drifting leaves.')
NO_TEXT = ('Book-accurate original design, NOT the HBO TV design (no bark-skinned leafy children, no Night King make-up). Every face is an '
           'invented unknown person who must NOT resemble any actor or celebrity, especially the cast of Game of Thrones or House of '
           'the Dragon. No text, letters, runes, logos or symbols anywhere in the image.')
NEGATIVE = ('text, letters, runes, words, watermark, logo, caption, actor likeness, celebrity, TV still, cartoon, anime, '
            'illustration, oversaturated, neon, gore, blood, bark skin, leaves growing from skin, plant creature, '
            'plate armour in Dawn Age or First Men scenes, horned helmets, extra fingers, deformed hands')
CAMERA = {'EW': 'epic wide shot, low horizon, 24mm lens', 'EST': 'establishing shot, 35mm lens',
          'MS': 'medium shot, 50mm lens', 'CU': 'portrait close-up, 85mm lens, shallow depth of field',
          'INS': 'macro insert, 100mm lens', 'OH': 'high overhead view'}

CAST = {
    'CHILD': ('a child of the forest as described in the books, an adult of a small ancient non-human people: as small and slender as a '
              'ten-year-old human but NOT childlike, a narrow adult face with an old guarded expression, smooth nut-brown skin dappled '
              'with paler spots like a fawn, large pointed ears, big gold-and-green eyes with vertical slit pupils like a cat, hands with '
              'EXACTLY three fingers and a thumb tipped with small sharp black claws, dark hair with leaves, vines and small flowers woven '
              'in, a cloak of stitched leaves, bark bindings on the legs; NOT a plant, NOT bark skin, NOT an elf'),
    'LEAF': ('Leaf, a child of the forest as described in the books, a small slender female of an ancient non-human people, as small '
             'as a ten-year-old but with an ancient sorrowful adult face, smooth nut-brown skin dappled with paler spots like a fawn, large '
             'ears, big gold-and-green cat-slit eyes, a cloak of living green and russet leaves, hair woven with leaves and tiny pale '
             'flowers, hands with EXACTLY three fingers and a thumb and small black claws; NOT a plant, NOT bark skin'),
    'GREENSEER': ('a greenseer of the children of the forest: a small slender ancient being with nut-brown fawn-dappled skin, large ears, '
                  'cat-slit eyes of BLOOD-RED, hair woven with red weirwood leaves, a cloak of leaves, hands with EXACTLY three fingers '
                  'and a thumb and black claws, a crown-like circle of thin white twigs; NOT a plant, NOT bark skin'),
    'GIANT': ('a giant as described in the books, 12 feet tall: NOT a tall bearded man but a massive shaggy hominid covered in coarse '
              'grey-brown fur, thicker below the waist, the lower body half again as wide as the upper, a heavy head thrust forward '
              'with a squashed flat face, tiny deep-set eyes, square heavy teeth, arms longer than his legs, splayed horny feet, '
              'no clothing but a crude fur hide'),
    'FIRST_MAN': ('a bronze-age chieftain of the First Men with an invented face: a broad weathered face, deep-set grey eyes, a heavy '
                  'brow, a thick braided brown beard, long hair tied back with bronze rings, furs and roughspun wool, a bronze torc, '
                  'a great round leather shield and a leaf-shaped bronze sword; NOT plate armour, NOT steel'),
    'BRANDON_BB': ('Brandon of the Bloody Blade, a legendary bronze-age warrior of the First Men with an invented face: tall and '
                   'raw-boned, a hard scarred face, wild dark hair and beard, wolf-fur cloak over leather, a long bronze sword, a round '
                   'leather shield'),
    'LUWIN': ('Maester Luwin as in the books, an invented face: a small, slight grey man in his sixties, thinning grey hair, a soft '
              'grey beard, mild tired grey eyes, a long plain grey robe with deep sleeves, a heavy chain collar of many linked metals '
              '(iron, bronze, silver, gold, copper) at his throat; NOT resembling any TV actor'),
    'BRAN': ('Bran Stark as in the books, a slight boy of nine with thick AUBURN-RED Tully hair, grey wool and a brown fur cloak, '
             'his legs crippled'),
    'OSHA': ('Osha as in the books, an invented face: a tall, rangy wildling woman of about thirty, a lean hard leathery face, short '
             'lank brown hair, sharp brown eyes, a crooked half-smile, rough wool and hide, an iron fetter on her wrist; NOT resembling '
             'any TV actor'),
    'ANDAL': ('an Andal warrior of the Seven with an invented face: tall and fair-haired, a long blond beard, pale blue eyes, a hard zealous '
              'face, a conical steel helm, a long coat of iron ring mail, a steel longsword and kite shield; an old healed scar shaped like '
              'a seven-pointed star on his chest where the mail is open'),
    'BLOODRAVEN': ('the last greenseer as described in the books: a pale corpse-like old man, so thin he is almost a skeleton, skin white '
                   'as bone, long white hair, a single glowing red eye, the other socket dark with a fine pale weirwood root growing '
                   'from it, seated deep in a tangle of white weirwood roots that grow into and through his body and ragged black '
                   'clothing, mushrooms and moss on him, seen mostly in shadow; NOT resembling any TV actor'),
    'SAM': ("Samwell Tarly as in the books, a YOUNG MAN of seventeen, enormously fat, a round soft PINK face with several chins, clean-shaven, fine "
            "sandy-blond hair, small pale eyes, kind and frightened, Night's Watch blacks of worn wool and a black cloak"),
    'OTHER': ('an Other, as described in the books: tall, gaunt and hard as old bones, flesh pale as milk, eyes deep burning blue, thin '
              'armour that ripples and changes colour like moonlight on water, a slender sword of pale translucent crystal; elegant and '
              'inhuman, NOT a corpse'),
    'GREEN_MAN': ('a green man of the Isle of Faces as in legend: a tall robed guardian in mossy green, a headdress of antlers, face '
                  'hidden in deep shadow under the antlers, faintly green-tinged hands, holding a staff of white weirwood'),
}


def key(n):
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


def prompt(typ, cast, body):
    who = '; '.join(CAST[c] for c in cast)
    subj = f'{who}, {body}' if who else body
    return f'{STYLE} {subj}. {PALETTE} Camera: {CAMERA[typ]}. Texture: fine film grain, atmospheric haze, tactile materials. {NO_TEXT}'


def _rows():
    import got002_plan as P
    rows = [(n, sl, ch, ty, ca, rc, bd, []) for n, sl, ch, ty, ca, rc, bd in P.B1]
    num = {}
    n = 10
    for sid, si, anc, shot, rec in P.PLAN:
        if isinstance(shot, tuple):
            n += 1
            slug, typ, cast, body, refs = shot
            num[slug] = n
            rows.append((n, slug, sid, typ, cast, rec, body, [r if isinstance(r, int) or ':' in str(r) else num[r] for r in refs]))
    slug, typ, cast, body, refs = P.IDENT
    n += 1
    num[slug] = n
    rows.append((n, slug, 'H', typ, cast, 'PUSH_IN', body, []))
    return rows, num


ROWS, NUM = _rows()
SHOTS = ROWS[10:]


def all_rows():
    assert [r[0] for r in ROWS] == list(range(1, 151)), 'numbering'
    return ROWS


def batch_json(n_batch, rows):
    imgs = []
    for n, slug, ch, typ, cast, rec, body, refs in rows:
        imgs.append({'scene_id': f'GOT002_SCENE{n:03d}', 'key': key(n),
                     'file': f'GOT002_BATCH{n_batch:03d}_SCENE{n:03d}_{slug}.png', 'chapter': ch, 'shot_type': typ,
                     'cast': cast, 'motion_recipe': rec, 'prompt': prompt(typ, cast, body), 'negative': NEGATIVE,
                     'refs': [x if isinstance(x, str) else key(x) for x in refs], 'qc': 'PENDING'})
    return {'episode': 'GOT002', 'batch': f'BATCH{n_batch:03d}', 'max_batch_size': 10, 'status': 'PLANNED',
            'style': STYLE, 'palette': PALETTE, 'images': imgs}


def write_all():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = all_rows()
    for b in range(1, 16):
        p = OUT / f'GOT002_BATCH{b:03d}.json'
        if p.exists():
            continue
        p.write_text(json.dumps(batch_json(b, [r for r in rows if (r[0] - 1) // 10 + 1 == b]), indent=1, ensure_ascii=False))
    print('batches 1-15 present')


if __name__ == '__main__':
    write_all()
