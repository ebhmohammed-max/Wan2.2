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
NO_TEXT = ('Book-accurate original design, NOT the HBO TV design. Every face is an invented unknown person who must NOT resemble any actor or celebrity, especially the cast of Game of Thrones or House of the Dragon. '
           'No text, letters, runes, logos or symbols anywhere in the image.')
NEGATIVE = ('text, letters, runes, words, watermark, logo, caption, actor likeness, celebrity, TV still, cartoon, anime, '
            'illustration, oversaturated, neon, gore, blood, plate armour in Age of Heroes scenes, horned helmets, '
            'Night King make-up, extra fingers, deformed hands')
CAMERA = {'EW': 'epic wide shot, low horizon, 24mm lens', 'EST': 'establishing shot, 35mm lens',
          'MS': 'medium shot, 50mm lens', 'CU': 'portrait close-up, 85mm lens, shallow depth of field',
          'INS': 'macro insert, 100mm lens', 'OH': 'high overhead view'}

CAST = {
    'NIGHTS_KING': ("the Night's King, thirteenth Lord Commander of the Night's Watch, a First Men warrior of about forty, a gaunt hard weathered face with hollow cheeks, high cheekbones and a long straight nose, pale grey eyes, iron-grey streaked dark hair pulled back tight into a single warrior's braid, a close-cropped grey-shot beard, a thin hard mouth, frost-reddened skin, an old pale scar through one eyebrow, utterly fearless expression, all in black: roughspun wool, black boiled leather, a heavy black bearskin cloak, a bronze-hilted bronze longsword"),
    'CORPSE_QUEEN': ('the corpse queen, an ageless otherworldly woman who looks barely twenty, skin white as the moon with a '
                     'faint blue chill and a dusting of tiny frost crystals across her cheekbones, a narrow heart-shaped face with a '
                     'small sharp chin, very large wide-set luminous eyes like blue stars, faint silver brows, long silver-white hair '
                     'falling straight with a few fine frosted braids, high-necked flowing robes of frost-pale grey with white fur at '
                     'the collar, fully covered, no jewellery, serene, inhuman and unsettling'),
    'OLD_NAN': ('Old Nan, an extremely old woman, tiny and bent, deeply wrinkled face, pale filmy eyes, a few wisps of white '
                'hair under a plain linen cap, grey wool shawl, knitting needles in her hands'),
    'BRAN': ('Bran Stark as in the books, a slight boy of nine with thick AUBURN-RED Tully hair and deep blue Tully eyes, a thoughtful freckled face, grey wool and a brown fur cloak; his legs are crippled, so he rides in a wicker basket'),
    'SAM': ("Samwell Tarly as in the books, a YOUNG MAN of seventeen with fully adult proportions, enormously fat, a round soft PINK moon face with several chins, clean-shaven smooth skin, fine fair sandy-blond hair, small pale eyes, soft plump hands, kind and frightened, Night's Watch blacks of worn wool straining over his belly and a black cloak, NOT a child"),
    'COLDHANDS': ('Coldhands, a rider in the black of the Night\'s Watch, face hidden behind a black wool scarf so only shadowed '
                  'eyes show, hands black and bloodless, riding a huge grey elk with broad antlers'),
    'JORAMUN': ('Joramun, King-beyond-the-Wall in the Age of Heroes, a huge wildling chieftain with a wild grey-streaked beard, '
                'weathered face, furs and hides with bronze fittings, carrying a gigantic black war horn banded with old '
                'gold, eight feet along the curve'),
    'KING_OF_WINTER': ('the Stark King of Winter in the Age of Heroes, a tall stern man with a long solemn face, dark hair, grey '
                       'eyes and a short dark beard, a grey direwolf pelt over his shoulders, bronze scale and furs, wearing '
                       'an open circlet of bronze surmounted by nine black iron spikes shaped like longswords'),
    'HODOR': ('Hodor, a gentle simple-minded GIANT of a stableman nearly seven feet tall, towering head and shoulders over everyone, huge and broad, a slack amiable face with a bushy brown beard and shaggy brown hair, plain brown wool'),
    'MEERA': 'Meera Reed, a lean young woman of sixteen, brown hair, green eyes, worn green-brown leathers, a three-pronged frog spear and a net',
    'JOJEN': 'Jojen Reed, a small solemn boy of thirteen, green eyes, green-brown clothes',
    'SUMMER': 'Summer, a huge silver-grey direwolf with golden eyes',
    'CHILD_FOREST': ('a child of the forest: a small slender being the size of a child, dark brown skin dappled with paler spots '
                     'like a fawn, large ears, huge golden eyes with slit pupils like a cat, hands with three fingers and a thumb '
                     'and small black claws, clothing of bark and leaves'),
    'OTHER': ('an Other, as described in the books: tall, gaunt and hard as old bones, flesh pale as milk, eyes deep burning '
              'blue, thin armour that ripples and changes colour with every movement like moonlight on water, a slender '
              'sword of pale translucent crystal glowing faint blue; elegant and inhuman, NOT a corpse'),
    'SHOW_NK': ('a tall gaunt figure seen ONLY as a dark silhouette, a ring of small icy horns forming a crown on his bald '
                'head, no face visible'),
    'GIANT': 'a giant as in the books: ten to twelve feet tall, covered in thick shaggy hair, massive shoulders, broad flat face',
    'YGRITTE': ("Ygritte as in the books, a wildling spearwife of about eighteen with thick wild red hair 'kissed by fire', a round peasant face, a pug nose, slightly crooked teeth, freckles and pale blue eyes, furs and a horn-and-weirwood bow"),
    'YOUNG_BRAN': 'Bran Stark aged seven, thick auburn hair, blue eyes, small and eager',
    'UNCLE_BRANDON': 'Brandon Stark, a handsome wild young northern lord of twenty, long face, dark hair, grey eyes, fierce grin',
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


# ------------------------------------------------------------------ shots 11-150 (script order)
# n, slug, chapter, type, cast, recipe, body, refs (scene numbers of earlier stills used as references)
SHOTS = [
 # H: hook (show king in silhouette only)
 (11, 'SHOW_KING_ARMY', 'H', 'EW', ['SHOW_NK'], 'PULL_OUT', 'seen from behind on a snowy ridge at night, overlooking a vast host of the dead standing motionless in the snow below, their eyes faint blue points, cold blue haze', []),
 (12, 'ICE_CROWN_MACRO', 'H', 'INS', ['SHOW_NK'], 'PUSH_IN', 'extreme close-up of the back of the head against a pale moon, the icy horn crown glittering with frost, snow falling', []),
 (13, 'ARMS_RAISED_DEAD_RISE', 'H', 'EW', ['SHOW_NK'], 'TILT_UP', 'seen from behind with both arms slowly raised, across a frozen field shapes stir and rise out of the snow, blue glints of eyes, wind-driven snow, no gore', []),
 (14, 'DEAD_FALL_DAWN', 'H', 'EW', [], 'PULL_OUT', 'a vast snowy battlefield at grey dawn where countless still dark shapes lie collapsed into the snow and drifting ice crystals, silence, distant castle walls, no gore, no bodies visible in detail', []),
 (15, 'BOOKS_CANDLE', 'H', 'MS', [], 'PUSH_IN', 'an old wooden writing desk at night with a stack of closed thick leather-bound books, a guttering candle, a raven feather quill and an iron inkwell, warm candlelight, no visible writing', []),
 (16, 'NK_SEES_HER_WIDE', 'H', 'EW', ['NIGHTS_KING'], 'PUSH_IN', 'a tiny figure in black standing on the top edge of the colossal Wall of ice at night, far below in the moonlit snow at the edge of a black forest stands a single pale figure looking up', [1]),
 (17, 'EFFIGY_DEFACED', 'H', 'MS', [], 'PUSH_IN', 'in a cold candlelit stone crypt, an ancient stone effigy of a warrior lying on a tomb whose face has been deliberately chiselled away, chisel marks and stone dust, a cloak carved in stone', []),
 (18, 'NK_INTO_BLIZZARD', 'H', 'MS', ['NIGHTS_KING'], 'DRIFT', 'seen from behind walking away into a howling blizzard beyond the Wall, black fur cloak streaming, his shape fading into white', [1]),
 # P: prologue, the Nightfort
 (19, 'NIGHTFORT_GATEHOUSE', 'P', 'EST', [], 'PUSH_IN', 'the ruined gatehouse of the Nightfort, a massive arch of dark grey stone half buried in snow, iron portcullis rusted open, the Wall of ice towering behind, dusk', [9]),
 (20, 'BROKEN_TOWER', 'P', 'EST', [], 'TILT_UP', 'a tall broken stone tower of the Nightfort with its top fallen away, snow drifting through empty window holes, crows circling, grey sky', [9]),
 (21, 'HALL_RATS_DUST', 'P', 'MS', [], 'PAN_LR', 'a vast abandoned feasting hall of the Nightfort, long rotted tables, dust and cobwebs, snow blown in through a collapsed roof, rats scurrying in a shaft of pale light', []),
 (22, 'COURTYARD_WEIRWOOD', 'P', 'EST', [], 'PULL_OUT', 'an empty snow-covered courtyard inside the ruined Nightfort, a single skinny weirwood with bone-white bark and blood-red leaves growing up through broken flagstones toward the moon', []),
 (23, 'BRAN_PARTY_ARRIVES', 'P', 'EST', ['HODOR', 'BRAN', 'MEERA', 'JOJEN', 'SUMMER'], 'PAN_LR', 'the small party entering the ruined Nightfort at dusk through deep snow, Hodor carrying Bran in a wicker basket on his back, Summer padding ahead', [4]),
 (24, 'RAT_COOK_KITCHEN', 'P', 'MS', [], 'PUSH_IN', 'a shadowy ancient castle kitchen with huge cold hearths and hanging copper pots, an enormous pale white rat the size of a dog crouched on a chopping table, glinting eyes, eerie ghost-story atmosphere, no gore', []),
 (25, 'SENTINELS_IN_ICE', 'P', 'MS', [], 'TILT_UP', 'the frozen top of the Wall at night, inside the clear blue ice a row of ghostly sealed figures in black cloaks holding spears and horns, all facing north, preserved like insects in amber, eerie and still', []),
 (26, 'NK_HALL_PAST', 'P', 'MS', ['NIGHTS_KING'], 'PUSH_IN', 'seated on a high carved wooden seat in the great hall of the Nightfort in its days of glory, hall lit by cold blue light and few torches, sworn brothers standing in shadow, menace', [1]),
 (27, 'EMPTY_SEAT_NOW', 'P', 'MS', [], 'PULL_OUT', 'the same great hall of the Nightfort in ruin today, the high wooden seat rotted and empty, snow on the dais, a single shaft of moonlight', []),
 # I: the thirteenth Lord Commander
 (28, 'LONG_NIGHT', 'I', 'EW', [], 'PAN_LR', 'the Long Night: a frozen dark world under a starless sky, a bronze-age village of round stone huts buried in snow, a single tiny fire glowing, endless darkness', []),
 (29, 'WALL_RISING_DAWN', 'I', 'EW', [], 'PULL_OUT', 'the first dawn after the Long Night, golden light on a half-built colossal wall of ice blocks stretching across the land, thousands of tiny workers, smoke from camps', []),
 (30, 'BRANDON_BUILDER', 'I', 'MS', ['KING_OF_WINTER', 'GIANT'], 'PAN_RL', 'the first Stark king of the bronze age, the builder, directing work at the foot of the rising Wall while giants haul enormous blocks of ice with ropes', [8]),
 (31, 'CHILDREN_WEIRWOODS', 'I', 'MS', ['CHILD_FOREST'], 'PUSH_IN', 'three children of the forest standing among bone-white weirwood trees with red leaves, solemn, watching, dappled light', []),
 (32, 'FIRST_OATH', 'I', 'EST', [], 'PULL_OUT', 'at grey dawn a group of bronze-age men in plain black furs kneeling before a grove of white weirwoods with carved faces, taking a solemn vow, breath fog', []),
 (33, 'BROTHERS_PATROL', 'I', 'EW', [], 'PAN_LR', 'a line of black-cloaked brothers of the Night\'s Watch walking along the top of the Wall of ice in wind and snow, the haunted forest dark far below to the north', []),
 (34, 'NK_LORD_COMMANDER', 'I', 'MS', ['NIGHTS_KING'], 'PUSH_IN', 'standing before rows of brothers in black in the snowy courtyard of the Nightfort, newly chosen leader, proud, bronze sword at his hip, torches', [1]),
 (35, 'NK_EYES', 'I', 'INS', ['NIGHTS_KING'], 'PUSH_IN', 'extreme close-up of his fearless grey eyes, frost on his eyelashes and beard, reflected moonlight', [1]),
 (36, 'LONE_SENTRY', 'I', 'MS', [], 'DRIFT', 'a lone young brother of the Night\'s Watch on top of the Wall at night holding a torch, peering nervously north into the black forest below, wind tearing at his cloak', []),
 (37, 'NK_AT_EDGE', 'I', 'MS', ['NIGHTS_KING'], 'TILT_UP', 'standing at the very edge of the Wall at night, looking down into the dark forest far below with calm fascination, not afraid', [1]),
 # II: the corpse queen
 (38, 'NK_OVERSHOULDER_HER', 'II', 'MS', ['NIGHTS_KING'], 'PUSH_IN', 'over-the-shoulder view from behind him on the Wall, far below a pale woman with long silver-white hair stands alone in the moonlit snow at the forest edge, looking up', [1, 2]),
 (39, 'QUEEN_FULL_FIGURE', 'II', 'EST', ['CORPSE_QUEEN'], 'PUSH_IN', 'standing alone in deep snow at the edge of the haunted forest at night, full figure, frost-pale robes flowing, the Wall a pale glow in the far distance', [2]),
 (40, 'NK_RIDES_FOREST', 'II', 'EST', ['NIGHTS_KING'], 'PAN_LR', 'riding hard on a dark horse through the snowbound haunted forest at night, snow flying, black trees, a pale shape glimpsed ahead between the trunks', [1]),
 (41, 'HANDS_TOUCH', 'II', 'INS', [], 'PUSH_IN', 'close-up of a man\'s rough hand in a black leather glove reaching to touch a slender moon-white hand, frost blooming outward from the point of contact, moonlight, tender and eerie', []),
 (42, 'NK_FROST_FACE', 'II', 'CU', ['NIGHTS_KING'], 'PUSH_IN', 'close-up as frost creeps across his beard and cheek, his grey eyes beginning to pale toward a faint icy blue, a look of rapture', [1]),
 (43, 'QUEEN_WALKS_MIST', 'II', 'MS', ['CORPSE_QUEEN'], 'DRIFT', 'seen from behind walking slowly away into freezing mist between black trees, silver-white hair trailing, mysterious', [2]),
 (44, 'OTHERS_IN_TREES', 'II', 'EST', ['OTHER'], 'PAN_RL', 'three of them standing silently among snow-laden black trees at night, their armour shifting from white to shadow-black to forest grey-green, blue eyes burning', []),
 (45, 'QUEEN_PROFILE', 'II', 'CU', ['CORPSE_QUEEN'], 'PUSH_IN', 'profile close-up by cold moonlight, frost on her lashes, beautiful and unsettling, faint blue glow of her eyes', [2]),
 (46, 'THROUGH_THE_WALL', 'II', 'MS', ['NIGHTS_KING', 'CORPSE_QUEEN'], 'PUSH_IN', 'he leads her on horseback through the long dark ice tunnel of a gate beneath the Wall, torches on the walls, icicles, she rides a pale horse', [1, 2]),
 (47, 'PROCLAIMED_KING', 'II', 'EST', ['NIGHTS_KING', 'CORPSE_QUEEN'], 'PULL_OUT', 'standing together on the dais of the Nightfort\'s great hall, rows of brothers in black kneeling before them, cold blue light and torch smoke', [1, 2]),
 (48, 'BROTHERS_ENTHRALLED', 'II', 'MS', [], 'DRIFT', 'rows of sworn brothers in black standing utterly still in a dark hall, eyes glazed with a faint icy sheen, frost on their cloaks and beards, enthralled, eerie', []),
 (49, 'NIGHTFORT_COLD_LIGHT', 'II', 'EW', [], 'PUSH_IN', 'the Nightfort in its prime at night, intact towers, a pale cold blue light glowing from its windows, freezing mist rolling over the walls, the Wall above it', [9]),
 (50, 'THIRTEEN_WINTERS', 'II', 'EW', [], 'PULL_OUT', 'the Nightfort buried deeper in snow and ice, icicles hanging from every tower, an endless winter, time passing', [9]),
 # CA
 (51, 'WALL_SUNRISE_PANORAMA', 'CA', 'EW', [], 'PAN_LR', 'the Wall of ice stretching away to the horizon across the North at sunrise, pink and gold light on the ice, forest below, majestic', []),
 # III: two kings against one
 (52, 'TWO_HOSTS_MEET', 'III', 'EW', [], 'PULL_OUT', 'in a snowy valley two bronze-age armies face each other: northmen under grey direwolf-on-white banners and a wild host of wildlings in furs, tension, breath steam', []),
 (53, 'HANDS_CLASP', 'III', 'INS', [], 'PUSH_IN', 'close-up of two large hands clasping in alliance, one with a bronze arm-ring and a wolf-pelt sleeve, the other weathered and fur-wrapped, snow falling', []),
 (54, 'GIANTS_WAKING', 'III', 'EW', ['GIANT'], 'TILT_UP', 'on snow-covered hills under a storm sky, several giants rising up out of the earth and snow as if waking, mammoths in the distance', []),
 (55, 'TWO_KINGS', 'III', 'MS', ['KING_OF_WINTER', 'JORAMUN'], 'PUSH_IN', 'the two kings standing side by side, the stern Stark king and the huge wildling king with his great horn, looking toward the Wall', [7, 8]),
 (56, 'HOST_MARCHES_ON_WALL', 'III', 'EW', [], 'PAN_RL', 'a combined host of northmen and wildlings marching through snow toward the Nightfort at the foot of the Wall at dawn, banners and spears', []),
 (57, 'NIGHTFORT_STORMED', 'III', 'EST', ['KING_OF_WINTER'], 'PUSH_IN', 'the gates of the Nightfort thrown open, warriors pouring into the courtyard, brothers in black kneeling dazed as if waking from a dream, no bloodshed shown', [8]),
 (58, 'STONE_RING_OFFERINGS', 'III', 'EST', [], 'PUSH_IN', 'beyond the Wall, a ring of ancient standing stones in the snow around a dark altar of ice, frost patterns radiating outward, scattered offerings of furs and bronze, ominous', []),
 (59, 'OTHERS_WATCH_RING', 'III', 'EST', ['OTHER'], 'DRIFT', 'two of them watching from the black treeline beyond the ring of standing stones at night, blue eyes burning', []),
 (60, 'RECORDS_BURN', 'III', 'MS', [], 'PUSH_IN', 'rolled parchment scrolls and leather-bound ledgers burning in an iron brazier in a stone room, embers rising, the pages blank and scorched, no writing visible', []),
 (61, 'RELIEF_CHISELLED', 'III', 'INS', [], 'PUSH_IN', 'a mason\'s hammer and chisel scraping away a carved stone relief of a cloaked warrior on a castle wall, stone chips flying', []),
 (62, 'NIGHTFORT_RUIN_TODAY', 'III', 'EW', [], 'PULL_OUT', 'the Nightfort today, a vast silent ruin at the foot of the Wall under heavy grey skies, eight thousand years of snow', [9]),
 # IV: a Stark of Winterfell
 (63, 'OLD_NAN_CU', 'IV', 'CU', ['OLD_NAN'], 'PUSH_IN', 'close-up by firelight, her filmy eyes glinting with mischief, needles paused', [3]),
 (64, 'YOUNG_BRAN_BED', 'IV', 'MS', ['YOUNG_BRAN'], 'PUSH_IN', 'tucked under heavy furs in a small stone bedchamber of Winterfell, listening wide-eyed to a story, candlelight', []),
 (65, 'BANNERS_HALL', 'IV', 'EST', [], 'PAN_LR', 'the great hall of Winterfell hung with many banners of northern houses: a grey direwolf on white, a black bull, a giant breaking chains, a bear, a stag-like moose, no lettering', []),
 (66, 'SKAGOS', 'IV', 'EW', [], 'PAN_RL', 'a wild dark mountainous island rising from a grey stormy northern sea, sea mist, no buildings', []),
 (67, 'BEAR_ISLAND', 'IV', 'EW', [], 'PAN_LR', 'a forested rocky island in a cold grey sea, a black bear on the pebble shore, pines', []),
 (68, 'NAN_LEANS_IN', 'IV', 'CU', ['OLD_NAN'], 'PUSH_IN', 'leaning in close, voice lowered, firelight from below making her face mysterious, a knowing smile', [3]),
 (69, 'TWO_BROTHERS', 'IV', 'MS', ['KING_OF_WINTER', 'NIGHTS_KING'], 'PUSH_IN', 'two brothers of the bronze age face to face in falling snow, one crowned and wolf-pelted, the other in the black of the Watch, the same long face, grief and defiance', [8, 1]),
 (70, 'NAN_PINCHES_NOSE', 'IV', 'MS', ['OLD_NAN', 'YOUNG_BRAN'], 'PUSH_IN', 'the old woman playfully pinching the little boy\'s nose by the fire, he giggles, warm and tender', [3]),
 (71, 'WINTERFELL_DUSK', 'IV', 'EW', [], 'PULL_OUT', 'Winterfell at dusk in snow: massive grey granite walls and towers, steam rising from hot springs, glass gardens glowing, a dark godswood inside the walls', []),
 (72, 'CRYPT_STATUE', 'IV', 'MS', [], 'PUSH_IN', 'the crypts beneath Winterfell, a stone statue of an ancient king seated on a throne with a rusted iron longsword across his knees and a stone direwolf at his feet, candlelight', []),
 (73, 'YOUNG_BRAN_EYES', 'IV', 'CU', ['YOUNG_BRAN'], 'PUSH_IN', 'close-up of his wide blue eyes reflecting candlelight, spellbound', []),
 (74, 'NK_BY_DAY', 'IV', 'MS', ['NIGHTS_KING'], 'DRIFT', 'on the top of the Wall in pale grey daylight, ordinary, a man among men, brothers working around him', [1]),
 (75, 'NK_BY_NIGHT', 'IV', 'MS', ['NIGHTS_KING', 'CORPSE_QUEEN'], 'PUSH_IN', 'at night in the dark hall, his face half in shadow and lit by icy blue light, the pale queen a shape behind his shoulder', [1, 2]),
 (76, 'CRYPT_ROW', 'IV', 'EW', [], 'PUSH_IN', 'a long row of stone kings on thrones receding into darkness in the crypts of Winterfell, each with a stone direwolf, a single torch', []),
 (77, 'SHIPWRIGHT_SAILS_WEST', 'IV', 'EW', [], 'PULL_OUT', 'a lone ancient longship with a square sail sailing west into a blazing sunset over an empty ocean, no land in sight', []),
 (78, 'BURNER_FLEET', 'IV', 'EW', [], 'PAN_LR', 'a fleet of ancient wooden ships burning in a harbour at night, flames reflected in black water, a lone figure watching from the shore', []),
 (79, 'UNCLE_BRANDON', 'IV', 'MS', ['UNCLE_BRANDON'], 'PUSH_IN', 'riding a horse through the snowy gates of Winterfell, laughing, cloak flying', []),
 (80, 'BROTHERS_SWORDS_CROSS', 'IV', 'MS', [], 'PUSH_IN', 'two dark silhouettes with crossed bronze swords against the pale glow of the Wall at night, snow, no blood', []),
 (81, 'DIREWOLF_BANNER_STORM', 'IV', 'MS', [], 'TILT_UP', 'a grey direwolf on white banner snapping in a snowstorm above the battlements of Winterfell, no lettering', []),
 # V: the Black Gate
 (82, 'NIGHTFORT_KITCHEN_WELL', 'V', 'EST', [], 'PUSH_IN', 'the ruined kitchen of the Nightfort at night, a wide round stone well in the middle of the floor, a skinny weirwood growing through the broken roof toward the moon', []),
 (83, 'WELL_DOWN_STEPS', 'V', 'OH', [], 'PUSH_IN', 'looking straight down a deep circular stone well with narrow steps spiralling down its wall into blackness, torchlight on wet frosted stone', []),
 (84, 'BLACK_GATE_WIDE', 'V', 'EST', [], 'PULL_OUT', 'the bottom of the deep well, the pale white weirwood door glowing softly like milk and moonlight in the darkness, steps and frost', [10]),
 (85, 'GATE_WOOD_GLOW', 'V', 'INS', [], 'DRIFT', 'macro of pale white weirwood grain glowing softly from within like milk and moonlight, frost crystals', [10]),
 (86, 'GATE_FACE_SLEEPING', 'V', 'CU', [], 'PUSH_IN', 'close-up of the old wrinkled face grown into the white weirwood door, eyes closed, as if sleeping', [10]),
 (87, 'PARTY_AT_GATE', 'V', 'EST', ['HODOR', 'BRAN', 'MEERA', 'JOJEN', 'SAM'], 'PUSH_IN', 'the small group gathered with torches at the bottom of the well before the glowing white door, Hodor carrying Bran in his basket', [4, 10, 5]),
 (88, 'GATE_EYES_OPEN', 'V', 'CU', [], 'PUSH_IN', 'extreme close-up of the face in the white weirwood door, its eyes opened, white and blind, looking straight at the viewer', [10]),
 (89, 'GATE_SPEAKS', 'V', 'CU', [], 'PUSH_IN', 'the wrinkled weirwood face with its lips parted as if speaking, faint glow, frost', [10]),
 (90, 'SAM_HAND_ON_GATE', 'V', 'MS', ['SAM'], 'PUSH_IN', 'standing before the glowing white door, one hand raised toward it, reciting solemnly, torch in the other hand', [5, 10]),
 (91, 'SWORD_IN_DARKNESS', 'V', 'INS', [], 'TILT_UP', 'a plain steel sword held upright in darkness, a thin line of torchlight along its edge', []),
 (92, 'WATCHER_ON_WALLS', 'V', 'MS', [], 'DRIFT', 'a lone brother in black standing watch on top of the Wall at dawn, silhouetted against the pale sky', []),
 (93, 'REALMS_OF_MEN', 'V', 'EW', [], 'PULL_OUT', 'seen from the south, the Wall glowing in the last light above a valley of small villages with warm lit windows and chimney smoke', []),
 (94, 'GATE_MOUTH_OPENS', 'V', 'CU', [], 'PUSH_IN', 'the face in the white weirwood door opening its mouth wider and wider into a great dark round opening ringed by wrinkles, glowing pale', [10]),
 (95, 'TUNNEL_INTO_NORTH', 'V', 'EST', ['HODOR', 'BRAN'], 'PUSH_IN', 'emerging from a dark tunnel through the ice into a snowy moonlit forest north of the Wall, Hodor carrying Bran in his basket, torches', [4]),
 (96, 'NK_AT_GATE_PAST', 'V', 'MS', ['NIGHTS_KING', 'CORPSE_QUEEN'], 'DRIFT', 'a dim dreamlike vision of the past: a man in black and a pale woman standing before the glowing white weirwood door at the bottom of the well, faces in shadow', [1, 2, 10]),
 (97, 'GATE_CLOSED', 'V', 'MS', [], 'HOLD', 'the white weirwood door at the bottom of the well, face closed and still, the torchlight fading', [10]),
 (98, 'NIGHTFORT_MOON_MIST', 'V', 'EW', [], 'PULL_OUT', 'the ruined Nightfort under a full moon, freezing mist creeping between its towers, utterly silent', [9]),
 # VI: the king of the dead (show version, silhouettes only)
 (99, 'SCREEN_GLOW_ROOM', 'VI', 'MS', [], 'PUSH_IN', 'a dark modern living room at night lit only by the cold blue glow of a large screen showing an abstract snowstorm, the silhouette of a viewer on a sofa, no logos', []),
 (100, 'RIDER_WITH_BUNDLE', 'VI', 'EW', ['SHOW_NK'], 'PAN_LR', 'riding a dead pale horse across a vast frozen plain at night carrying a small swaddled bundle, seen in silhouette from a distance', []),
 (101, 'ICE_ALTAR_RING', 'VI', 'EST', [], 'PUSH_IN', 'a ring of tall jagged ice spires on a frozen plain under a black sky, a flat altar of ice at the centre with a small swaddled bundle, blue glow', []),
 (102, 'BUNDLE_BLUE_GLOW', 'VI', 'INS', [], 'PUSH_IN', 'a small swaddled cloth bundle resting on an altar of ice, a faint icy blue light rising from within the cloth, frost spreading, no face visible', []),
 (103, 'CANDLE_SNUFFED', 'VI', 'INS', [], 'HOLD', 'a single candle flame being snuffed out in darkness, a thin curl of smoke', []),
 (104, 'HARDHOME_RISE', 'VI', 'EW', ['SHOW_NK'], 'TILT_UP', 'on a cliff above a burning wooden wildling village by a dark sea, seen from behind with arms raised, below shapes rising from the snow, no gore', []),
 (105, 'UNDEAD_DRAGON_SILHOUETTE', 'VI', 'EW', [], 'PAN_RL', 'a huge pale dragon with tattered wings and glowing blue eyes flying low over a frozen lake under a white sky, ice crystals trailing, two legs and two wings', []),
 (106, 'STONE_SPIRAL_WEIRWOOD', 'VI', 'EST', [], 'PULL_OUT', 'a lone weirwood tree on a grassy hill ringed by standing stones laid in a spiral, green summer land, ancient', []),
 (107, 'CHILDREN_RITUAL', 'VI', 'MS', ['CHILD_FOREST'], 'PUSH_IN', 'a bronze-age man bound with roots against the white trunk of a weirwood tree, a child of the forest stands before him holding a black obsidian blade, the moment before, solemn, no blood', [31]),
 (108, 'FIRST_WALKER_EYES', 'VI', 'CU', [], 'PUSH_IN', 'extreme close-up of a bronze-age man\'s eyes turning from brown to burning icy blue, frost spreading across his skin', []),
 (109, 'GODSWOOD_LEAP', 'VI', 'EST', ['SHOW_NK'], 'PUSH_IN', 'a snowy godswood at night before a weirwood tree, a small agile cloaked figure leaping toward the tall crowned silhouette with a short dagger raised, frozen in mid-air, dramatic, no blood', []),
 (110, 'ARMY_SHATTERS', 'VI', 'EW', [], 'PULL_OUT', 'across a dawn battlefield beneath castle walls, countless dark figures crumbling into glittering ice shards and snow at once, no gore', []),
 (111, 'CLOSED_BOOK_SNOW', 'VI', 'INS', [], 'HOLD', 'a closed thick leather-bound book lying in fresh snow, snowflakes settling on its cover, no lettering', []),
 # VII: The legend in the books
 (112, 'WRITERS_DESK', 'VII', 'MS', [], 'PUSH_IN', 'a cluttered writer\'s study at night with no person present: an old desktop computer glowing, stacks of manuscript pages, small painted knight figurines and a toy castle on the shelves, lamp light, nothing legible', []),
 (113, 'LEGEND_TAPESTRY', 'VII', 'MS', [], 'PAN_LR', 'an ancient faded woven tapestry on a stone wall depicting heroes of legend: a crowned king, a wall of ice and a fox-like trickster, no lettering', []),
 (114, 'LANN_THE_CLEVER', 'VII', 'MS', [], 'PUSH_IN', 'a golden-haired grinning young trickster in a dark cloak slipping through a narrow sea cave beneath an enormous cliff, torch in hand, mischievous', []),
 (115, 'CAIRN_DUSK', 'VII', 'EST', [], 'DRIFT', 'an ancient stone cairn alone on a windswept snowy moor at dusk', []),
 (116, 'CASTERLY_ROCK', 'VII', 'EW', [], 'PULL_OUT', 'a colossal rock rising from the sea like a crouching lion, a fortress carved into it, sunset light on the ocean', []),
 (117, 'FIGURE_FADES_FOG', 'VII', 'MS', ['NIGHTS_KING'], 'DRIFT', 'a man in black fading into thick fog until he is barely a shadow, like a half-forgotten legend', [1]),
 (118, 'RAVEN_SCROLL', 'VII', 'INS', [], 'PUSH_IN', 'a black raven perched on a stone ledge with a small sealed parchment tied to its leg, candlelight, no writing', []),
 (119, 'OTHERS_RING', 'VII', 'EST', ['OTHER'], 'PULL_OUT', 'several of them standing in a loose circle in a frozen forest at night with no leader among them, armour rippling in shifting colours', []),
 (120, 'OTHER_CU', 'VII', 'CU', ['OTHER'], 'PUSH_IN', 'close-up portrait, gaunt milk-pale face, deep burning blue eyes, frost in the air, the crystal blade a faint line of light', []),
 (121, 'LAND_OF_ALWAYS_WINTER', 'VII', 'EW', [], 'PAN_LR', 'the far north beyond everything: endless white ice wastes under a green and blue aurora, jagged ice mountains, no life', []),
 (122, 'CHILDREN_ROOT_CAVE', 'VII', 'EST', ['CHILD_FOREST'], 'PUSH_IN', 'children of the forest in a vast cave woven through with pale weirwood roots, small fires, bones and roots, watching silently', [31]),
 # VIII: the ranger with cold hands
 (123, 'DRAGON_EGGS', 'VIII', 'INS', [], 'PUSH_IN', 'three dragon eggs resting in glowing embers: one black with scarlet ripples, one deep green flecked with bronze, one pale cream streaked with gold, scales like stone', []),
 (124, 'COLDHANDS_LEADS', 'VIII', 'EST', ['COLDHANDS', 'HODOR', 'BRAN', 'MEERA', 'JOJEN', 'SUMMER'], 'PAN_LR', 'the hooded rider on the great elk leading the small party through deep snow among huge trees, Hodor carrying Bran in his basket', [6, 4]),
 (125, 'COLDHANDS_HANDS', 'VIII', 'INS', ['COLDHANDS'], 'PUSH_IN', 'close-up of black bloodless hands gripping leather reins, frost on the knuckles, the elk\'s fur', [6]),
 (126, 'COLDHANDS_AT_WALL', 'VIII', 'EST', ['COLDHANDS'], 'TILT_UP', 'the rider on the elk halted before the colossal Wall at night, a tiny figure against the ice, unable to go further', [6]),
 (127, 'WALL_DEEP_LIGHT', 'VIII', 'INS', [], 'DRIFT', 'deep inside the ancient ice of the Wall, a faint pale-blue light glowing like veins, old and mysterious, no symbols', []),
 (128, 'LEAF_CU', 'VIII', 'CU', ['CHILD_FOREST'], 'PUSH_IN', 'close-up of a female child of the forest with a cloak of leaves and hair of brown and gold, large golden cat-slit eyes, solemn, firelight in a root cave', [31]),
 (129, 'COLDHANDS_SCARF_EYES', 'VIII', 'CU', ['COLDHANDS'], 'PUSH_IN', 'close-up of the black scarf and hood, only the shadowed eyes visible, frost on the wool', [6]),
 (130, 'GHOST_RANGER', 'VIII', 'MS', [], 'DRIFT', 'a hooded black-cloaked ranger of the Night\'s Watch standing among white weirwoods in mist, face unseen, timeless', []),
 (131, 'RIDER_SILHOUETTE_MOON', 'VIII', 'EST', ['COLDHANDS'], 'PULL_OUT', 'the rider on the great elk silhouetted on a snowy ridge against a huge pale moon', [6]),
 (132, 'WILDLINGS_DIG_GLACIER', 'VIII', 'EST', [], 'PAN_RL', 'wildlings in furs digging with torches and picks into a blue glacier high in the mountains, snow blowing', []),
 (133, 'OPENED_CAIRNS', 'VIII', 'EST', [], 'PULL_OUT', 'dozens of ancient stone cairns broken open across a snowy mountainside, stones scattered, no bodies visible', []),
 (134, 'YGRITTE', 'VIII', 'MS', ['YGRITTE'], 'PUSH_IN', 'on top of the Wall in the wind, frustrated tears on her cheeks, looking north', []),
 (135, 'MANUSCRIPT_STACK', 'VIII', 'INS', [], 'PUSH_IN', 'a towering stack of blank manuscript pages beside a guttering candle, nothing legible', []),
 (136, 'STORM_TOWARD_WALL', 'VIII', 'EW', [], 'PUSH_IN', 'a colossal dark blizzard sweeping south toward the Wall from the frozen north, the forest disappearing into white', []),
 (137, 'NAN_DOZING_EMBERS', 'VIII', 'MS', ['OLD_NAN'], 'DRIFT', 'dozing by a dying fire in her chair, knitting in her lap, embers glowing', [3]),
 (138, 'NK_LEGEND_SKY', 'VIII', 'EW', ['NIGHTS_KING'], 'TILT_UP', 'a lone silhouette standing on the top of the Wall beneath a sky full of stars and a pale aurora', [1]),
 (139, 'WEIRWOOD_FACE_SNOW', 'VIII', 'CU', [], 'PUSH_IN', 'the carved face of a weirwood heart tree weeping red sap, fresh snow on its white bark, red leaves', []),
 # CB / ident
 (140, 'NK_QUEEN_ON_WALL', 'CB', 'EST', ['NIGHTS_KING', 'CORPSE_QUEEN'], 'PUSH_IN', 'together on the top of the Wall at night looking north, he in black furs, she in frost-pale robes, moonlight', [1, 2]),
 (141, 'WALL_NIGHT_AERIAL', 'H', 'EW', [], 'PUSH_IN', 'aerial view at night of the Wall of ice cutting across a snowy continent from coast to coast, starlight, the Nightfort a dark speck', []),
 # extras (cutaways)
 (142, 'WIGHT_HANDS', 'VI', 'INS', [], 'PUSH_IN', 'close-up of a dead man\'s black frostbitten hand rising from the snow, faint blue light, no gore', []),
 (143, 'SUMMER_GOLDEN_EYES', 'P', 'CU', ['SUMMER'], 'PUSH_IN', 'close-up in the ruined Nightfort, golden eyes reflecting firelight, hackles raised at something unseen', []),
 (144, 'HODOR_CARRIES_BRAN', 'V', 'MS', ['HODOR', 'BRAN'], 'TILT_UP', 'Hodor carrying Bran in a wicker basket on his back down a narrow spiral of stone steps, torchlight', [4]),
 (145, 'ICE_SPIRES_SHOW', 'VI', 'EW', [], 'PAN_LR', 'a frozen wasteland of jagged ice spires under a dark sky, blue light, utterly alien', []),
 (146, 'NIGHTS_WATCH_OATH_GROVE', 'V', 'EST', [], 'PULL_OUT', 'a ring of nine white weirwoods with carved faces just north of the Wall in snow, young men in black kneeling', []),
 (147, 'QUEEN_EYES_MACRO', 'II', 'INS', ['CORPSE_QUEEN'], 'PUSH_IN', 'macro of her eye, a blue like a burning star, frost on the lashes', [2]),
 (148, 'MAMMOTHS', 'III', 'EW', ['GIANT'], 'PAN_RL', 'giants riding shaggy mammoths through a snowy pass, wildlings marching alongside', []),
 (149, 'WINTERFELL_HEART_TREE', 'IV', 'EST', [], 'PUSH_IN', 'the godswood of Winterfell, a huge ancient weirwood heart tree with a long sad carved face beside a black pool, steam rising', []),
 (150, 'ARCHIVE_VAULT', 'CB', 'EST', [], 'PULL_OUT', 'an ancient candlelit archive vault of stone shelves full of scrolls and leather-bound books, dust motes, warm light, nothing legible', []),
]


def all_rows():
    rows = [(n, sl, ch, ty, ca, rc, bd, []) for n, sl, ch, ty, ca, rc, bd in B1] + SHOTS
    assert [r[0] for r in rows] == list(range(1, 151)), 'numbering'
    return rows


def write_all():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = all_rows()
    for b in range(1, 16):
        p = OUT / f'GOT001_BATCH{b:03d}.json'
        if p.exists():
            continue
        chunk = [r for r in rows if (r[0] - 1) // 10 + 1 == b]
        d = batch_json(b, [r[:7] for r in chunk])  # batch 1 already exists
        for it, r in zip(d['images'], chunk):
            it['refs'] = [key(x) for x in r[7]]
        p.write_text(json.dumps(d, indent=1, ensure_ascii=False))
    print('batches 1-15 present')


if __name__ == '__main__':
    write_all()
