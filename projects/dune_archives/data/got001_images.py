"""GOT001 (The Night King: Who Was He Really?) image plan: look-book + batches of 10.

Book-first visuals: see worlds/westeros/WESTEROS_BOOK_LOOKS.md and WESTEROS_CANON_POLICY.md.
Prompt = STYLE + subject (+ cast anchors) + palette + camera + NO_TEXT.
Batch 1 holds the character reference portraits and the two key locations. Later batches pass them as refs.
Age of Heroes (~8,000 years before the books) = First Men bronze age: bronze blades and fittings, furs,
roughspun, no plate armour. Book-era scenes (Bran, Sam, Coldhands) = medieval iron/steel.
The show's Night King appears only as a silhouette (no HBO make-up, no actor likeness).
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / '19_batches/GOT001'

STYLE = ('ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, fine film grain, '
         'full-bleed wide 16:9 cinematic frame, important action in the central band.')
PALETTE = ('Far North palette: glacier blue, charcoal black, bone white and torch amber; breath fog, drifting snow, '
           'moonlight on ice.')
NO_TEXT = ('Book-accurate original design, NOT the HBO TV design, original faces not resembling any actor. '
           'No text, letters, runes, logos or symbols anywhere in the image.')
NEGATIVE = ('text, letters, runes, words, watermark, logo, caption, actor likeness, celebrity, TV still, cartoon, anime, '
            'illustration, oversaturated, neon, gore, blood, plate armour in Age of Heroes scenes, horned helmets, '
            'Night King make-up, extra fingers, deformed hands')
CAMERA = {'EW': 'epic wide shot, low horizon, 24mm lens', 'EST': 'establishing shot, 35mm lens',
          'MS': 'medium shot, 50mm lens', 'CU': 'portrait close-up, 85mm lens, shallow depth of field',
          'INS': 'macro insert, 100mm lens', 'OH': 'high overhead view'}

CAST = {
    'NIGHTS_KING': ('the Night\'s King, thirteenth Lord Commander of the Night\'s Watch, a First Men warrior of about '
                    'thirty-five, long solemn northern face, dark brown hair to the shoulders, short dark beard, grey eyes, '
                    'proud and utterly fearless expression, all in black: roughspun wool, black boiled leather, heavy black '
                    'fur cloak, a bronze-hilted bronze longsword'),
    'CORPSE_QUEEN': ('the corpse queen, an ageless woman of unearthly beauty, skin white as the moon with a faint blue chill, '
                     'luminous eyes like blue stars, long straight silver-white hair, high-necked flowing robes of frost-pale '
                     'grey with white fur at the collar, fully covered, no jewellery, serene and unsettling'),
    'OLD_NAN': ('Old Nan, an extremely old woman, tiny and bent, deeply wrinkled face, pale filmy eyes, a few wisps of white '
                'hair under a plain linen cap, grey wool shawl, knitting needles in her hands'),
    'BRAN': ('Bran Stark, a boy of about ten, thick auburn hair, blue eyes, thoughtful face, grey wool and a brown fur cloak; '
             'his legs are crippled, so he rides in a wicker basket'),
    'SAM': ('Samwell Tarly, a very heavy young man of about sixteen, round soft pink face, beardless, kind frightened eyes, '
            'Night\'s Watch blacks of worn wool and a black cloak'),
    'COLDHANDS': ('Coldhands, a rider in the black of the Night\'s Watch, face hidden behind a black wool scarf so only shadowed '
                  'eyes show, hands black and bloodless, riding a huge grey elk with broad antlers'),
    'JORAMUN': ('Joramun, King-beyond-the-Wall in the Age of Heroes, a huge wildling chieftain with a wild grey-streaked beard, '
                'weathered face, furs and hides with bronze fittings, carrying a gigantic black war horn banded with old '
                'gold, eight feet along the curve'),
    'KING_OF_WINTER': ('the Stark King of Winter in the Age of Heroes, a tall stern man with a long solemn face, dark hair, grey '
                       'eyes and a short dark beard, a grey direwolf pelt over his shoulders, bronze scale and furs, wearing '
                       'an open circlet of bronze surmounted by nine black iron spikes shaped like longswords'),
}

B1 = [
    # n, slug, chapter, type, cast, recipe, body
    (1, 'NIGHTS_KING_PORTRAIT', 'II', 'CU', ['NIGHTS_KING'], 'PUSH_IN',
     'standing on top of the colossal ice Wall at night, torchlight on one side of his face and cold moonlight on the other, '
     'looking out north into the dark, snow drifting past'),
    (2, 'CORPSE_QUEEN_PORTRAIT', 'II', 'CU', ['CORPSE_QUEEN'], 'PUSH_IN',
     'among black snow-laden trees of the haunted forest at night, faint blue glow in her eyes, breath does not fog, '
     'snowflakes resting on her hair without melting'),
    (3, 'OLD_NAN_TELLING', 'IV', 'MS', ['OLD_NAN'], 'PUSH_IN',
     'seated by a hearth in a stone chamber of Winterfell, knitting, leaning forward as she tells a frightening tale, '
     'firelight carving the wrinkles of her face, a small fur-blanketed bed in the soft background'),
    (4, 'BRAN_NIGHTFORT_FIRE', 'P', 'CU', ['BRAN'], 'PUSH_IN',
     'sitting by a small fire inside a vast ruined stone kitchen, looking up into the darkness with wide eyes, '
     'cobwebs and broken rafters above'),
    (5, 'SAM_PORTRAIT', 'V', 'MS', ['SAM'], 'DRIFT',
     'holding a torch in a dark stone stairwell, frightened but determined, frost on the stones'),
    (6, 'COLDHANDS_ELK', 'VIII', 'EST', ['COLDHANDS'], 'PAN_LR',
     'emerging between enormous snow-laden sentinel pines and pale weirwoods in deep snow at twilight, ravens on the '
     'branches above, a faint mist at ground level'),
    (7, 'JORAMUN_HORN', 'III', 'MS', ['JORAMUN'], 'TILT_UP',
     'standing on a windswept glacier ridge under a storm sky, raising the great horn toward his lips, snow streaming '
     'past, distant mountains of the Frostfangs'),
    (8, 'KING_OF_WINTER', 'III', 'MS', ['KING_OF_WINTER'], 'PUSH_IN',
     'standing in a misty godswood before a bone-white weirwood tree with blood-red leaves and a carved weeping face, '
     'grim and resolute, a host of bronze-armed northmen half-seen in the mist behind him'),
    (9, 'NIGHTFORT_ESTABLISHING', 'P', 'EW', [], 'PULL_OUT',
     'the Nightfort: a vast, ancient, half-ruined castle of dark grey stone sprawling at the foot of the colossal Wall of '
     'ice, seven hundred feet of glittering pale-blue ice rising behind it into a dusk sky, broken towers, collapsed roofs '
     'heavy with snow, no lights anywhere, utterly abandoned'),
    (10, 'BLACK_GATE_FACE', 'V', 'MS', [], 'PUSH_IN',
     'at the bottom of a deep circular stone well, a door of pale white weirwood glowing softly like milk and moonlight, '
     'with an old wrinkled human face grown into the wood, its eyes just opening, torchlight from above, frost on the '
     'surrounding stones, eerie and beautiful'),
]


def key(n):
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


def prompt(typ, cast, body):
    who = '; '.join(CAST[c] for c in cast)
    subj = f'{who}, {body}' if who else body
    return f'{STYLE} {subj}. {PALETTE} Camera: {CAMERA[typ]}. Texture: fine film grain, atmospheric haze, tactile materials. {NO_TEXT}'


def batch_json(n_batch, rows):
    imgs = []
    for n, slug, ch, typ, cast, rec, body in rows:
        imgs.append({'scene_id': f'GOT001_SCENE{n:03d}', 'key': key(n),
                     'file': f'GOT001_BATCH{n_batch:03d}_SCENE{n:03d}_{slug}.png', 'chapter': ch, 'shot_type': typ,
                     'cast': cast, 'motion_recipe': rec, 'prompt': prompt(typ, cast, body), 'negative': NEGATIVE,
                     'refs': [], 'qc': 'PENDING'})
    return {'episode': 'GOT001', 'batch': f'BATCH{n_batch:03d}', 'max_batch_size': 10, 'status': 'PLANNED',
            'style': STYLE, 'palette': PALETTE, 'images': imgs}


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / 'GOT001_BATCH001.json'
    if not p.exists():
        p.write_text(json.dumps(batch_json(1, B1), indent=1, ensure_ascii=False))
    print('wrote', p)
