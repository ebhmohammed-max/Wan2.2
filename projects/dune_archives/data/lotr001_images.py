"""LOTR001 (Who Was Sauron Before He Was Evil?) image plan: look-book + batches of 10.

Book-first visuals: worlds/middle_earth/MIDDLE_EARTH_BOOK_LOOKS.md + MIDDLE_EARTH_CANON_POLICY.md.
Prompt = STYLE + subject (+ cast anchors) + palette + camera + NO_TEXT.
Batch 1 = character reference portraits (later batches pass them as refs).
No actor likeness (Jackson films, The Rings of Power); no film Eye-on-the-tower, no RoP designs.
SHOTS are generated from tools/plans/lotr001_plan.py (shot order = script order).
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / '19_batches/LOTR001'
sys.path.insert(0, str(ROOT / 'tools/plans'))

STYLE = ('ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, fine film grain, '
         'full-bleed wide 16:9 cinematic frame, important action in the central band.')
PALETTE = ('Mythic Middle-earth palette: forge gold and ember orange, moonlit silver and deep blue, Mordor red and ash '
           'black; volumetric light, drifting embers or mist.')
NO_TEXT = ('Book-accurate original design, NOT the Peter Jackson film design and NOT the Rings of Power TV design. Every face is an '
           'invented unknown person who must NOT resemble any actor or celebrity, especially the casts of The Lord of the Rings, '
           'The Hobbit or The Rings of Power. No text, letters, runes, logos or symbols anywhere in the image.')
NEGATIVE = ('text, letters, runes, words, watermark, logo, caption, actor likeness, celebrity, film still, cartoon, anime, '
            'illustration, oversaturated, neon, gore, blood, flaming eye on top of a tower, film Sauron armour, extra fingers, '
            'deformed hands')
CAMERA = {'EW': 'epic wide shot, low horizon, 24mm lens', 'EST': 'establishing shot, 35mm lens',
          'MS': 'medium shot, 50mm lens', 'CU': 'portrait close-up, 85mm lens, shallow depth of field',
          'INS': 'macro insert, 100mm lens', 'OH': 'high overhead view'}

CAST = {
    'MAIRON': ('Mairon, a Maia spirit in bodily form as a smith of Aule: a tall, graceful, ageless man who looks about thirty, a fine-boned '
               'oval face with a straight narrow nose, high calm brow and a precise, thoughtful mouth, clean-shaven, warm amber-gold eyes '
               'with a faint inner light, long dark copper-red hair tied back neatly at the nape, pale linen robes under a dark leather '
               "smith's apron, a faint golden glow on his skin"),
    'AULE': ('Aule the Smith, a Vala: an immense broad-shouldered smith with a great braided brown beard and forearms like oak, '
             'a leather apron, seen mostly from behind or in three-quarter view by forge-light, face never clearly shown'),
    'MELKOR': ('Melkor, the mightiest Vala turned dark: a colossal majestic figure wreathed in shadow and cold fire, eyes like burning '
               'coals, face hidden in darkness'),
    'MORGOTH': ('Morgoth, the Dark Lord: a towering king in black armour on an iron throne, wearing an iron crown set with three '
                'brilliant white jewels blazing with light, face in deep shadow'),
    'SAURON_FA': ('Sauron in the First Age, the same man as Mairon grown cold: tall and lean, the same fine-boned oval face with a straight '
                  'narrow nose, now pale and severe, clean-shaven, eyes burning red-gold, long dark copper-red hair worn loose, '
                  'black and deep crimson robes, an iron circlet on his brow, beautiful and terrible'),
    'ANNATAR': ('Annatar, the Lord of Gifts: a noble, regal, ageless man who looks about forty, a fine-boned oval face with a straight narrow '
                'nose and faint lines at the eyes, clean-shaven, warm amber eyes, long dark copper-red hair with two thin braids at the '
                'temples, a slender golden circlet, rich robes of gold and ivory, an open, generous gesture; NOT blond'),
    'SAURON_DARK': ('the Dark Lord in the Third Age: a man of more than human stature (but not a giant) in black iron armour, '
                    'face never visible, wrapped in shadow and heat haze, a black hand with ONLY FOUR FINGERS'),
    'LUTHIEN': ('Luthien, an elf-maiden of unearthly beauty: a gentle oval face, luminous grey eyes like the starlit evening, very long '
                'hair dark as the shadows of twilight, a gown blue as the unclouded heaven, a dark mantle sewn with small golden flowers, '
                'fully covered, ethereal, never sexualised'),
    'FINROD': ('Finrod Felagund, King of Nargothrond: a tall elf-king with long golden hair, a noble kind face, grey eyes, a fine gold '
               'crown, a grey cloak over silver mail'),
    'BEREN': 'Beren, a mortal man of about twenty-five: lean and rugged, dark hair, grey eyes, a short beard, worn leather and a grey cloak',
    'HUAN': 'Huan, the great wolfhound of Valinor: a huge pale-grey hound the size of a pony, a long noble head, deep intelligent eyes',
    'SAURON_WOLF': 'Sauron in the form of a werewolf: a colossal grey-black wolf, the greatest ever seen, eyes like red embers',
    'CELEBRIMBOR': ('Celebrimbor, lord of the elven-smiths of Eregion: a young-looking elf lord with long straight black hair, sharp '
                    'clever features, bright grey eyes, a thin silver circlet, a dark blue tunic, soot on his hands'),
    'ELROND': ('Elrond, an elf-lord whose face is ageless, neither old nor young: long dark hair, deep grey eyes, a smooth calm face, a '
               'silver circlet, robes of grey and deep green; NOT resembling any film actor'),
    'FRODO': ('Frodo Baggins as in the books: a hobbit about three and a half feet tall who looks thirty, a cleft chin, thick curly dark '
              'brown hair, hazel-brown eyes, a fair-skinned clever face, a green waistcoat, large bare feet with curly brown hair'),
    'SAM': ('Sam Gamgee as in the books: a sturdy hobbit with a round brown face, curly brown hair, brown eyes, plain brown clothes, '
            'large bare hairy feet'),
    'BOROMIR': ('Boromir of Gondor: a tall man with a fair and noble face, dark hair, grey eyes, proud and stern, a dark green cloak and '
                'mail, a great horn tipped with silver'),
    'GORLIM': 'Gorlim, a gaunt hollow-eyed outlaw of about forty in ragged furs, unkempt dark hair and beard',
    'EONWE': 'Eonwe, herald of Manwe: a shining warrior in white-gold armour holding a great trumpet, seen from behind',
    'AR_PHARAZON': ('Ar-Pharazon the Golden, King of Numenor: a tall proud king in gleaming golden armour and a golden helm that hides '
                    'most of his face, a black-and-gold cloak'),
    'GIL_GALAD': 'Gil-galad, High King of the Elves: a tall elf-king with long dark hair, silver mail, a blue cloak, a long spear',
    'ISILDUR': 'Isildur, a tall Numenorean prince with dark hair, grey eyes, a battle-worn face, dented armour',
    'GOLLUM': ('Gollum as in the books: a small, very thin creature with long thin hands and feet, a few lank hairs, huge pale luminous '
               'eyes, almost entirely in shadow'),
    'HALBRAND': 'a man seen ONLY as a dark silhouette from behind, ragged cloak, no face visible',
}


def key(n):
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


def prompt(typ, cast, body):
    who = '; '.join(CAST[c] for c in cast)
    subj = f'{who}, {body}' if who else body
    return f'{STYLE} {subj}. {PALETTE} Camera: {CAMERA[typ]}. Texture: fine film grain, atmospheric haze, tactile materials. {NO_TEXT}'


def _rows():
    import lotr001_plan as P
    rows = [(n, sl, ch, ty, ca, rc, bd, []) for n, sl, ch, ty, ca, rc, bd in P.B1]
    num = {}
    n = 10
    for sid, si, anc, shot, rec in P.PLAN:
        if isinstance(shot, tuple):
            n += 1
            slug, typ, cast, body, refs = shot
            num[slug] = n
            rows.append((n, slug, sid, typ, cast, rec, body, [r if isinstance(r, int) else num[r] for r in refs]))
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
        imgs.append({'scene_id': f'LOTR001_SCENE{n:03d}', 'key': key(n),
                     'file': f'LOTR001_BATCH{n_batch:03d}_SCENE{n:03d}_{slug}.png', 'chapter': ch, 'shot_type': typ,
                     'cast': cast, 'motion_recipe': rec, 'prompt': prompt(typ, cast, body), 'negative': NEGATIVE,
                     'refs': [key(x) for x in refs], 'qc': 'PENDING'})
    return {'episode': 'LOTR001', 'batch': f'BATCH{n_batch:03d}', 'max_batch_size': 10, 'status': 'PLANNED',
            'style': STYLE, 'palette': PALETTE, 'images': imgs}


def write_all():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = all_rows()
    for b in range(1, 16):
        p = OUT / f'LOTR001_BATCH{b:03d}.json'
        if p.exists():
            continue
        p.write_text(json.dumps(batch_json(b, [r for r in rows if (r[0] - 1) // 10 + 1 == b]), indent=1, ensure_ascii=False))
    print('batches 1-15 present')


if __name__ == '__main__':
    write_all()
