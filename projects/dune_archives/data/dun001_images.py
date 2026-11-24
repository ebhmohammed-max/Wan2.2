"""DUN001 (The Butlerian Jihad) image plan: 150 stills in 15 batches of 10, plus the character look-book.

Run `python data/dun001_images.py` to write 19_batches/DUN001/DUN001_BATCH###.json and DUN001_BATCH_INDEX.md.
Prompt = STYLE + subject (+ cast anchors) + era palette + camera + NO_TEXT. Continuity: Legends of Dune, told as history.
Batch 1 holds the character reference portraits; later batches pass them as `images=[...]` for face continuity.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / '19_batches/DUN001'

STYLE = ('ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, fine film grain, '
         'full-bleed wide 16:9 cinematic frame, important action in the central band.')
PALETTE = ('Butlerian Jihad era palette: cold steel, ash grey and ember orange; firelight against cold machine light; '
           'smoke and cracked chrome.')
NO_TEXT = 'Original character design, not based on any real person. No text, letters, logos or symbols anywhere in the image.'
NEGATIVE = ('text, letters, words, watermark, logo, signature, caption, actor likeness, celebrity, film still, cartoon, '
            'anime, illustration, oversaturated, neon, cyberpunk, extra fingers, deformed hands, blurry face, gore, blood, '
            'classical columns, arches, Roman, Greek, Gothic, medieval architecture, Terminator, chrome skeleton robot, '
            'religious symbols, crosses')
CAMERA = {'EW': 'epic wide shot, low horizon, 24mm lens', 'EST': 'establishing shot, 35mm lens',
          'MS': 'medium shot, 50mm lens', 'CU': 'portrait close-up, 85mm lens, shallow depth of field',
          'INS': 'macro insert, 100mm lens', 'OH': 'high overhead view'}

# ------------------------------------------------------------------ look-book (continuity sheets)
CAST = {
    'SERENA': 'Serena Butler, a woman in her early twenties, oval face, high cheekbones, long amber-brown hair, '
              'striking grey-violet eyes, fierce and intelligent expression',
    'SERENA_OLD': 'Serena Butler in her late fifties, silver streaks in long amber-brown hair, the same grey-violet eyes, '
                  'calm and resolute, white priestess robes with ember-orange trim',
    'XAVIER': 'Xavier Harkonnen, a man in his early twenties, close-cropped dark brown hair, square jaw, serious grey eyes, '
              'League officer uniform of slate grey with silver piping',
    'XAVIER_OLD': 'Xavier Harkonnen in his late fifties, grey temples, lined square face, serious grey eyes, '
                  'slate-grey Jihad general\'s uniform with silver piping',
    'VORIAN': 'Vorian Atreides, a lean man who looks about thirty, black hair, sharp aquiline features, watchful dark grey eyes',
    'VORIAN_TRUSTEE': 'black machine-trustee uniform with fine silver trim',
    'VORIAN_CMDR': 'dark green and black Jihad commander\'s coat',
    'IBLIS': 'Iblis Ginjo, a broad-shouldered charismatic man in his thirties, thick black hair, dark persuasive eyes, '
             'coarse grey overseer\'s tunic',
    'IBLIS_GP': 'Iblis Ginjo as Grand Patriarch, heavier and older, thick black hair greying, heavy crimson-and-black robes '
                'with a chain of office',
    'ERASMUS': 'Erasmus, a tall elegant humanoid robot with a smooth oval face of liquid mirror-like flowmetal and no '
               'features except a faint rippling expression, platinum-silver body, wearing ornate deep crimson and gold '
               'brocade robes',
    'CYMEK': 'a towering cymek war machine: a transparent canister of glowing blue fluid holding a living human brain, '
             'mounted in the armoured core of a massive multi-legged walking machine of black and bronze steel',
    'OMNIUS': 'the evermind Omnius, shown as a vast glowing core of liquid silver light deep inside a machine city, '
              'surrounded by thousands of floating silver sphere-shaped watcheyes',
    'ROBOTS': 'angular silver-grey combat robots with mirrored sensor faces',
    'ABULURD': 'Abulurd Harkonnen, a man in his early thirties, sandy-blond hair, earnest pale blue eyes, '
               'dark green officer uniform with silver trim',
    'FAYKAN': 'Faykan Butler, a tall regal man in his forties, dark-blond hair swept back, proud bearing, '
              'scarlet and gold viceroy robes',
    'SERAPH': 'a Seraph bodyguard, a tall female warrior in white and gold ceremonial armour, hair tightly braided',
    'XERXES': 'Xerxes, a small stooped nobleman with a narrow sallow face and heavy jewelled robes, lounging',
    'AGAMEMNON_H': 'Agamemnon as a human general, a hard-faced man in his forties, cropped grey-black hair, '
                   'dark military greatcoat',
    'BABY': 'a swaddled infant a few months old wrapped in a plain cream blanket',
}

# ------------------------------------------------------------------ shots
# (short name, chapter, shot type, cast keys, motion recipe, subject/action/location)
S = [
    # ---- BATCH 1: hook keys + reference portraits
    ('BALCONY_ERASMUS_INFANT', 'H', 'MS', ['ERASMUS', 'BABY'], 'PUSH_IN',
     'seen from behind, the robot stands at a stone balustrade high above a lush walled garden, cradling the infant, '
     'a pale white sky beyond, eerie stillness'),
    ('SERENA_ANGUISH', 'H', 'CU', ['SERENA'], 'PUSH_IN',
     'her face contorted in anguish and fury, reaching forward, silver robot hands gripping her shoulders from behind, '
     'tears, plain grey slave shift, villa interior behind'),
    ('OMNIUS_CORE', 'H', 'EW', ['OMNIUS'], 'PULL_OUT',
     'a cathedral-scale machine chamber without arches or columns, tiny human slaves on a walkway for scale'),
    ('CYMEK_WAR', 'H', 'EW', ['CYMEK'], 'TILT_UP',
     'striding through a burning human city at night, low angle, embers and smoke, fleeing people tiny at its feet'),
    ('REF_ERASMUS', 'II', 'CU', ['ERASMUS'], 'DRIFT',
     'portrait in a luxurious villa interior with paintings and sculptures, cold window light, the flowmetal face '
     'reflecting the room, unsettling curiosity'),
    ('REF_SERENA', 'II', 'CU', ['SERENA'], 'DRIFT',
     'portrait on Salusa Secundus, elegant deep blue and white League noble dress, soft daylight, hopeful defiance'),
    ('REF_VORIAN', 'III', 'CU', ['VORIAN', 'VORIAN_TRUSTEE'], 'DRIFT',
     'portrait aboard a sleek starship bridge, cold instrument light, conflicted expression'),
    ('REF_XAVIER', 'II', 'CU', ['XAVIER'], 'DRIFT',
     'portrait on a military landing field at dawn, wind, smoke in the distance, steadfast expression'),
    ('REF_IBLIS', 'III', 'CU', ['IBLIS'], 'DRIFT',
     'portrait in a dim slave work yard, torchlight on his face, a knowing half-smile, calculating eyes'),
    ('EARTH_ATOMIC_ORBIT', 'H', 'EW', [], 'PULL_OUT',
     'planet Earth seen from orbit as multiple white atomic flashes bloom across its night side, a fleet of dark '
     'angular warships silhouetted in the foreground'),
    # ---- BATCH 2: hook rest + chapter I start
    ('CHILD_SAINT_STATUE', 'H', 'EW', [], 'TILT_UP',
     'a colossal stone statue of a mother holding an infant, braziers of fire at its base, a vast crowd of pilgrims, dusk'),
    ('COMMANDMENT_STONE', 'H', 'INS', [], 'PUSH_IN',
     'a hand chiselling deep grooves into a slab of black stone by candlelight, stone dust, the carving blurred and illegible'),
    ('LIE_SCREENS', 'H', 'MS', [], 'PUSH_IN',
     'a crowd in a dark plaza staring up at giant floating holographic projections of flames and a blurred figure, '
     'faces lit orange, horror'),
    ('JIHAD_TITLE_BG', 'H', 'EW', [], 'PUSH_IN',
     'a lone burning robot head half buried in ash on a battlefield at dusk, smoke columns, ember-orange sky, empty space above'),
    ('OLD_EMPIRE_COMFORT', 'I', 'EW', [], 'PAN_LR',
     'a gleaming serene city of the Old Empire, white towers and gardens, people lounging idly while sleek robots serve them'),
    ('MACHINE_FIELDS', 'I', 'EW', [], 'PAN_RL',
     'endless golden fields harvested by autonomous machines under a soft sky, no humans in sight'),
    ('IDLE_NOBLES', 'I', 'MS', [], 'DRIFT',
     'bored pale nobles reclining on cushions while a robot attendant pours wine, soft decadent light'),
    ('TITANS_GATHER', 'I', 'EST', [], 'PUSH_IN',
     'twenty conspirators in dark cloaks gathered around a table of glowing schematics in a dim room, faces half lit'),
    ('REF_AGAMEMNON_HUMAN', 'I', 'CU', ['AGAMEMNON_H'], 'DRIFT',
     'portrait, cold command-room light, ruthless ambition'),
    ('NETWORK_SEIZURE', 'I', 'EST', [], 'PUSH_IN',
     'a vast control hall where screens and machine lights turn blood-red at once, operators fleeing'),
    # ---- BATCH 3: chapter I
    ('BLOODLESS_CONQUEST', 'I', 'EW', ['ROBOTS'], 'PULL_OUT',
     'ranks of robots marching unopposed through a city square while citizens kneel, banners falling'),
    ('BRAIN_SURGERY', 'I', 'MS', [], 'PUSH_IN',
     'a sterile surgical theatre, robotic arms lowering a glowing transparent brain canister, the patient hidden '
     'under sheets, clinical blue light, no gore'),
    ('BRAIN_CANISTER', 'I', 'INS', [], 'PUSH_IN',
     'a transparent cylinder of glowing blue fluid containing a living human brain, fine electrodes, reflections'),
    ('CYMEK_RISE', 'I', 'EW', ['CYMEK'], 'TILT_UP',
     'the first cymek rising from a cradle of scaffolding in a vast hangar, sparks, tiny technicians below'),
    ('XERXES_PALACE', 'I', 'MS', ['XERXES'], 'DRIFT',
     'in a decadent palace of silk and gold, robot servants and glowing consoles all around him'),
    ('NETWORK_AWAKENS', 'I', 'INS', [], 'PUSH_IN',
     'a single machine eye of silver light blinking open inside a dark tangle of cables, the first spark of a mind'),
    ('OMNIUS_SPREAD', 'I', 'OH', [], 'PULL_OUT',
     'a field of planets in deep space linked by threads of silver light spreading outward like frost'),
    ('TITANS_SUBJUGATED', 'I', 'EW', ['CYMEK'], 'PULL_OUT',
     'several cymek machines standing motionless before a towering wall of silver watcheyes, diminished, cold light'),
    ('TITAN_MONUMENT', 'I', 'EW', [], 'TILT_UP',
     'a colossal monument of a cymek machine carved from dark stone on a machine world, human slaves hauling blocks below'),
    ('SYNCHRONIZED_WORLD', 'I', 'EW', [], 'PAN_LR',
     'a machine world city of black geometric towers and silver light, no vegetation, cold perfect order'),
    # ---- BATCH 4: chapter II
    ('LEAGUE_WORLDS', 'II', 'OH', [], 'PULL_OUT',
     'a scatter of warm blue-green planets at the dark edge of a galaxy, a few faint ships between them'),
    ('ZIMIA_SALUSA', 'II', 'EW', [], 'PAN_RL',
     'the city of Zimia on Salusa Secundus, terraced white stone government buildings, green hills, warm sun, human crowds'),
    ('LEAGUE_PARLIAMENT_EXT', 'II', 'EST', [], 'PUSH_IN',
     'a grand modern parliament building of white stone and glass on a hill, banners in deep blue, citizens on the steps'),
    ('SERENA_XAVIER_GARDEN', 'II', 'MS', ['SERENA', 'XAVIER'], 'DRIFT',
     'the couple walking close together through a sunlit garden, her hand on his arm, tender'),
    ('SERENA_PREGNANT', 'II', 'MS', ['SERENA'], 'PUSH_IN',
     'standing at a window, one hand resting on her slightly rounded belly, determined gaze toward the sky'),
    ('GIEDI_PRIME_FALLS', 'II', 'EW', ['ROBOTS'], 'PULL_OUT',
     'an industrial human world under attack, robot dropships descending through orange smog, refineries burning'),
    ('SERENA_MISSION', 'II', 'MS', ['SERENA'], 'PUSH_IN',
     'in a dark flight suit at the head of a small band of volunteers boarding a ship at night, resolute'),
    ('SERENA_CAPTURED', 'II', 'MS', ['SERENA', 'ROBOTS'], 'PUSH_IN',
     'kneeling in smoking rubble, surrounded by robots, her face streaked with ash, defiant'),
    ('EARTH_MACHINE_WORLD', 'II', 'EW', [], 'PULL_OUT',
     'old Earth under machine rule, blue oceans but cities replaced by black geometric machine structures, from low orbit'),
    ('ERASMUS_VILLA', 'II', 'EW', [], 'PAN_LR',
     'a vast luxurious villa on Earth, terraced gardens, fountains and greenhouses, human slaves tending it, '
     'a high balcony on the main house'),
    # ---- BATCH 5: chapter II end + III start
    ('ERASMUS_STUDY', 'II', 'MS', ['ERASMUS'], 'PUSH_IN',
     'examining a terrified human slave held still by robots in a white laboratory, head tilted with curiosity, no gore'),
    ('ERASMUS_PAINTING', 'II', 'MS', ['ERASMUS'], 'DRIFT',
     'painting at an easel in a sunlit studio, copying a masterpiece, uncanny calm'),
    ('SERENA_SLAVE', 'II', 'MS', ['SERENA'], 'PUSH_IN',
     'in a plain grey slave shift scrubbing a marble floor in the villa, glancing up with hatred'),
    ('ARCHIVE_VILLA_DOOR', 'CA', 'EST', [], 'PUSH_IN',
     'tall bronze doors of the villa slowly opening onto darkness, a single shaft of light'),
    ('SERENA_BIRTH', 'III', 'MS', ['SERENA', 'BABY'], 'DRIFT',
     'exhausted, holding her newborn son in a bare slave quarters room, soft window light, fierce love'),
    ('SERENA_MANION', 'III', 'CU', ['SERENA', 'BABY'], 'DRIFT',
     'cradling the infant close and whispering to him, tears of joy'),
    ('ERASMUS_WATCHES', 'III', 'MS', ['ERASMUS'], 'PUSH_IN',
     'watching from a shadowed doorway, his flowmetal face reflecting a mother and child across the room'),
    ('SLAVES_GATHERED', 'III', 'EW', [], 'PULL_OUT',
     'a courtyard of the villa filled with silent human slaves in grey, ordered to watch, robots at the edges'),
    ('ERASMUS_TAKES_BOY', 'III', 'MS', ['ERASMUS', 'SERENA', 'BABY'], 'PUSH_IN',
     'the robot lifting the swaddled infant from the mother\'s arms as robot hands hold her back, terrible calm'),
    ('BALCONY_EMPTY', 'III', 'EST', [], 'HOLD',
     'an empty high stone balcony in white light, a cream blanket caught on the balustrade lifting in the wind'),
    # ---- BATCH 6: chapter III
    ('SERENA_ATTACK', 'III', 'MS', ['SERENA', 'ROBOTS'], 'PUSH_IN',
     'hurling herself at a silver sentinel robot with bare hands, motion blur, raw fury'),
    ('ROBOT_DESTROYED', 'III', 'INS', ['ROBOTS'], 'HOLD',
     'a toppled silver sentinel robot, its mirrored face cracked, sparks on the marble floor'),
    ('SLAVES_ERUPT', 'III', 'EW', [], 'PULL_OUT',
     'a crowd of slaves surging forward with tools and torches, robots overwhelmed, fire spreading'),
    ('IBLIS_LEADS', 'III', 'MS', ['IBLIS'], 'PUSH_IN',
     'standing on a crate shouting orders to rising slaves, torch held high'),
    ('EARTH_REVOLT', 'III', 'EW', [], 'PAN_LR',
     'a machine city on Earth at night with fires breaking out across it, smoke columns, explosions'),
    ('VORIAN_WITNESS', 'III', 'CU', ['VORIAN', 'VORIAN_TRUSTEE'], 'PUSH_IN',
     'watching the revolt from a balcony, the realisation dawning on his face, firelight'),
    ('DREAM_VOYAGER', 'III', 'EW', [], 'PULL_OUT',
     'a sleek silver starship lifting off from a burning city at night, engines blazing'),
    ('ESCAPE_COCKPIT', 'III', 'MS', ['VORIAN', 'SERENA', 'IBLIS'], 'DRIFT',
     'three fugitives in a starship cockpit, stars streaking, exhausted and grim'),
    ('VORIAN_SIDE', 'III', 'CU', ['VORIAN'], 'DRIFT',
     'tearing a silver trustee insignia from his black uniform, resolve'),
    ('TITANS_HUNT', 'IV', 'EW', ['CYMEK', 'ROBOTS'], 'PULL_OUT',
     'cymeks and robots sweeping through an empty ruined city on Earth, searchlights, ash falling, no people left'),
    # ---- BATCH 7: chapter IV
    ('EARTH_SILENT', 'IV', 'EW', [], 'HOLD',
     'a deserted square on Earth, scattered belongings in the ash, a single robot standing guard, grey light'),
    ('PARLIAMENT_HALL', 'IV', 'EW', [], 'PULL_OUT',
     'the vast circular League parliament chamber packed with delegates in tiers, tense, warm stone and glass, no columns'),
    ('SERENA_SPEECH', 'IV', 'MS', ['SERENA'], 'PUSH_IN',
     'at a speaker\'s podium in the parliament, grieving and furious, fist raised, delegates behind'),
    ('XAVIER_PROPOSES', 'IV', 'MS', ['XAVIER'], 'PUSH_IN',
     'standing to address the parliament, grim and certain, delegates turning to look'),
    ('ATOMICS_VAULT', 'IV', 'INS', [], 'PUSH_IN',
     'sealed atomic warheads in a dark armoury vault, red warning lights, frost on the casings'),
    ('VOTE_SILENT', 'IV', 'EW', [], 'HOLD',
     'the parliament chamber in total silence, every delegate seated, not a single hand raised'),
    ('LEAGUE_FLEET', 'IV', 'EW', [], 'PULL_OUT',
     'a great fleet of dark angular human warships forming up in orbit above a blue world'),
    ('ATOMIC_FLASH_EARTH', 'IV', 'EW', [], 'PUSH_IN',
     'a blinding white atomic flash rising over a machine city on Earth, shockwave rolling across the land'),
    ('DEAD_EARTH', 'IV', 'EW', [], 'PULL_OUT',
     'Earth from orbit transformed into a dead scorched grey sphere with faint glowing scars, no oceans of light'),
    ('JIHAD_BANNERS', 'IV', 'EW', [], 'TILT_UP',
     'huge ember-orange banners unfurling over a cheering crowd in a plaza on Salusa, smoke and torchlight, blurred illegible designs'),
    # ---- BATCH 8: chapter V
    ('IBLIS_PATRIARCH', 'V', 'MS', ['IBLIS_GP'], 'PUSH_IN',
     'addressing a vast crowd from a high stage, arms spread, torches, triumphant'),
    ('SERENA_PRIESTESS', 'V', 'MS', ['SERENA'], 'DRIFT',
     'in white priestess robes with ember-orange trim, standing beneath giant banners, solemn, now in her thirties'),
    ('GENERALS', 'V', 'MS', ['XAVIER', 'VORIAN', 'VORIAN_CMDR'], 'DRIFT',
     'two generals side by side over a glowing tactical table on a warship bridge'),
    ('BATTLE_SPACE', 'V', 'EW', [], 'PAN_LR',
     'human warships and machine ships clashing above a burning planet, beams and explosions'),
    ('GROUND_BATTLE', 'V', 'EW', ['ROBOTS'], 'PULL_OUT',
     'human soldiers in grey armour advancing through smoke against robot lines, ember light'),
    ('SHIELD_SHIMMER', 'V', 'MS', [], 'PUSH_IN',
     'a soldier standing inside a faint blue shimmering personal energy shield as projectiles slow and stop against it'),
    ('FOLDSPACE_SHIP', 'V', 'EW', [], 'PUSH_IN',
     'a strange new ship vanishing in a ripple of folded space, stars bending around it'),
    ('JIPOL', 'V', 'MS', [], 'PUSH_IN',
     'black-uniformed secret police dragging a man from his home at night, neighbours watching from windows'),
    ('JIHAD_COUNCIL', 'V', 'EST', ['IBLIS_GP'], 'PUSH_IN',
     'a closed council chamber of hard-faced officials, Iblis at the head of the table, shadows'),
    ('WAR_WEARY', 'V', 'MS', [], 'DRIFT',
     'exhausted civilians and wounded veterans in a grey street, memorial candles, weariness'),
    # ---- BATCH 9: chapter V end + VI
    ('TRUCE_HALL', 'V', 'EST', [], 'PUSH_IN',
     'hooded robed sages seated around a single glowing light in a quiet chamber, brokering peace'),
    ('SERENA_IBLIS_PLAN', 'V', 'MS', ['SERENA_OLD', 'IBLIS_GP'], 'PUSH_IN',
     'speaking in low voices in a dim candlelit room, grave expressions'),
    ('CORRIN_PLANET', 'VI', 'EW', [], 'PULL_OUT',
     'the machine capital world Corrin under a vast red giant sun, black machine cities glinting'),
    ('SERENA_ARRIVES', 'VI', 'EW', ['SERENA_OLD', 'SERAPH'], 'PUSH_IN',
     'walking down a ramp onto a black machine landing platform, five white-armoured guards behind her, robots in ranks'),
    ('OMNIUS_HALL', 'VI', 'EW', ['OMNIUS', 'SERENA_OLD'], 'PULL_OUT',
     'a tiny woman in white standing alone before the immense silver core of the evermind'),
    ('SERENA_SMILE', 'VI', 'CU', ['SERENA_OLD'], 'PUSH_IN',
     'a faint knowing smile, eyes calm, cold silver light on her face'),
    ('ERASMUS_NOTICES', 'VI', 'CU', ['ERASMUS'], 'PUSH_IN',
     'the robot raising one hand to halt, its flowmetal face rippling into recognition'),
    ('SERAPH_GRIEF', 'VI', 'CU', ['SERAPH'], 'PUSH_IN',
     'her face wet with tears, steeling herself, cold light'),
    ('SERENA_FALLEN', 'VI', 'EST', ['SERAPH'], 'HOLD',
     'a white priestess robe spread on a black machine floor, seen from high above, guards kneeling around it, no blood'),
    ('SALUSA_SCREENS', 'VI', 'EW', [], 'PUSH_IN',
     'a huge crowd in Zimia at night watching giant blurred projections of flames, faces in horror'),
    # ---- BATCH 10: chapter VI end + VII
    ('CLONE_TANK', 'VI', 'MS', [], 'PUSH_IN',
     'a woman with amber-brown hair floating unconscious in a green-lit growth tank in a hidden laboratory'),
    ('CELL_MATCH', 'VI', 'INS', [], 'PUSH_IN',
     'a lab technician\'s gloved hand placing a sample into a glowing analyser, a match signal of green light'),
    ('MOB_RAGE', 'VI', 'EW', [], 'PULL_OUT',
     'a furious torchlit mob surging through the streets of Zimia, banners, fire'),
    ('JIHAD_REBORN', 'VI', 'EW', [], 'TILT_UP',
     'columns of soldiers boarding warships under giant ember banners at dawn, renewed fervour'),
    ('TLULAXA_LAB', 'VII', 'EW', [], 'PAN_LR',
     'rows of sealed tanks holding sleeping captives in a sickly green underground facility, technicians in hoods, no gore'),
    ('CAPTIVE_TANK', 'VII', 'CU', [], 'PUSH_IN',
     'a captive man\'s face pressed to the glass of a tank, pleading eyes, green light'),
    ('XAVIER_DISCOVERS', 'VII', 'MS', ['XAVIER_OLD'], 'PUSH_IN',
     'standing frozen in the doorway of the tank hall, horror turning to cold resolve'),
    ('XAVIER_IBLIS_SHIP', 'VII', 'MS', ['XAVIER_OLD', 'IBLIS_GP'], 'PUSH_IN',
     'in a small ship cabin, Xavier at the controls, Iblis behind him realising, a bright star filling the window'),
    ('SHIP_INTO_STAR', 'VII', 'EW', [], 'PUSH_IN',
     'a tiny ship silhouetted against the blazing surface of a white star, about to be swallowed'),
    ('THREE_MARTYRS', 'VII', 'EW', [], 'TILT_UP',
     'three colossal statues, a man, a woman and a child, under braziers of eternal flame, pilgrims below'),
    # ---- BATCH 11: chapter VII end + VIII
    ('XAVIER_DEFACED', 'VII', 'INS', [], 'PUSH_IN',
     'a framed portrait of a dignified grey-haired officer smeared and cracked, lying in debris'),
    ('FAMILY_SHAME', 'VII', 'MS', [], 'DRIFT',
     'a mother with two young children leaving a grand house at dusk, heads down, servants watching'),
    ('VORIAN_KNOWS', 'VII', 'CU', ['VORIAN', 'VORIAN_CMDR'], 'PUSH_IN',
     'alone in a dark office, reading a message, jaw clenched, grief and anger'),
    ('PLAGUE_CAPSULE', 'VIII', 'INS', [], 'PUSH_IN',
     'a small machine capsule splitting open on a city rooftop, releasing a pale mist'),
    ('PLAGUE_WARD', 'VIII', 'EW', [], 'PULL_OUT',
     'an overwhelmed hospital hall filled with sick people on cots, masked healers, grey light, no gore'),
    ('MACHINE_FLEET', 'VIII', 'EW', [], 'PAN_RL',
     'an immense fleet of black angular machine ships moving through space in perfect formation'),
    ('VORIAN_PLAN', 'VIII', 'MS', ['VORIAN', 'VORIAN_CMDR'], 'PUSH_IN',
     'leaning over a holographic star chart marked with dozens of targets, war council around him'),
    ('FOLD_STRIKE', 'VIII', 'EW', [], 'PUSH_IN',
     'dozens of human warships emerging from ripples of folded space above a machine world'),
    ('PURGE_FLASH', 'VIII', 'EW', [], 'PULL_OUT',
     'a machine world engulfed in chains of white atomic flashes, seen from orbit'),
    ('SLAG_WORLD', 'VIII', 'EW', [], 'PAN_LR',
     'the surface of a burned machine world, molten black slag and twisted towers, glowing cracks'),
    # ---- BATCH 12: chapter VIII end + IX
    ('CORRIN_SURVIVES', 'VIII', 'EW', [], 'PULL_OUT',
     'the machine world Corrin alone and intact under its red sun, a ring of human warships surrounding it at a distance'),
    ('BLOCKADE', 'VIII', 'EW', [], 'PAN_LR',
     'a long line of human picket ships holding position in the dark, years of vigil, frost on hulls'),
    ('VENGEANCE_FLEET', 'IX', 'EW', [], 'PUSH_IN',
     'a vast human fleet advancing on Corrin, the red giant sun behind the planet'),
    ('VORIAN_OLDER', 'IX', 'CU', ['VORIAN', 'VORIAN_CMDR'], 'DRIFT',
     'on a warship bridge, a few grey hairs, harder and colder than before, red sunlight'),
    ('CYMEK_FALLEN', 'IX', 'EST', ['CYMEK'], 'HOLD',
     'a wrecked cymek lying in ice and smoke, its brain canister dark and cracked, a lone figure walking away'),
    ('ABULURD_PORTRAIT', 'IX', 'CU', ['ABULURD'], 'DRIFT',
     'on a warship bridge, earnest and troubled, red light'),
    ('BRIDGE_PODS', 'IX', 'EW', [], 'PULL_OUT',
     'an enormous ring of thousands of small cargo pods strung in orbit around Corrin, glinting in red light'),
    ('POD_CAPTIVES', 'IX', 'MS', [], 'PUSH_IN',
     'inside a cramped cargo pod, frightened human captives pressed together, a small window showing the fleet'),
    ('ERASMUS_CORRIN', 'IX', 'MS', ['ERASMUS'], 'PUSH_IN',
     'watching the approaching fleet on screens in a dark machine tower, red light on his flowmetal face'),
    ('ORDER_ARGUMENT', 'IX', 'MS', ['VORIAN', 'VORIAN_CMDR', 'ABULURD'], 'PUSH_IN',
     'confronting each other on the warship bridge, Abulurd pleading, Vorian unmoved'),
    # ---- BATCH 13: chapter IX end + X
    ('ABULURD_SABOTAGE', 'IX', 'MS', ['ABULURD'], 'PUSH_IN',
     'alone in a weapons control room, pulling a lever, panels going dark around him'),
    ('WEAPONS_DARK', 'IX', 'EW', [], 'PULL_OUT',
     'the human fleet\'s gun batteries powering down one by one, consoles dark'),
    ('ATOMICS_CORRIN', 'IX', 'EW', [], 'PULL_OUT',
     'atomic flashes blossoming across the surface of Corrin under the red sun'),
    ('GROUND_ASSAULT', 'IX', 'EW', ['ROBOTS'], 'PUSH_IN',
     'mercenary soldiers storming the black machine citadel of Corrin through fire and smoke'),
    ('OMNIUS_DIES', 'IX', 'EW', ['OMNIUS'], 'PULL_OUT',
     'the silver core of the evermind shattering, watcheyes falling dark like dead stars'),
    ('TRIAL', 'X', 'EW', ['ABULURD'], 'PUSH_IN',
     'standing alone in chains before a tribunal in a high stone hall, faces cold'),
    ('VORIAN_TURNS', 'X', 'MS', ['VORIAN', 'VORIAN_CMDR'], 'HOLD',
     'turning his back and refusing to look at the prisoner, cold fury'),
    ('LANKIVEIL', 'X', 'EW', [], 'PAN_LR',
     'a frozen grey world of ice fjords and a small whaling village, snow, bleak exile'),
    ('ABULURD_EXILE', 'X', 'MS', ['ABULURD'], 'DRIFT',
     'older, in rough furs, staring out over a frozen sea, broken'),
    ('ARRAKIS_FIRE', 'X', 'EW', [], 'PUSH_IN',
     'a desert city on Arrakis burning at night under two moons, sandstorm on the horizon'),
    # ---- BATCH 14: chapter X
    ('FAYKAN_CORRINO', 'X', 'MS', ['FAYKAN'], 'PUSH_IN',
     'standing before the crowd, raising his hand, proud, golden light'),
    ('GOLDEN_THRONE', 'X', 'EW', [], 'TILT_UP',
     'a monumental golden throne with a lion motif in a vast hall of scarlet and gold, light from above, empty'),
    ('COMMANDMENT_CARVED', 'X', 'EW', [], 'TILT_UP',
     'a towering black stone monolith carved with blurred illegible script, pilgrims below, ember light'),
    ('MACHINES_SMASHED', 'X', 'EW', [], 'PULL_OUT',
     'citizens throwing machines and robots onto a vast bonfire in a plaza at night, sparks rising'),
    ('MENTAT', 'X', 'CU', [], 'PUSH_IN',
     'a man with eyes rolled slightly upward in deep calculation, faint glow of data reflected in his eyes, dark room'),
    ('SISTERS', 'X', 'MS', [], 'DRIFT',
     'hooded women in black robes walking in a line through a stone cloister without arches, candlelight'),
    ('NAVIGATOR', 'X', 'MS', [], 'PUSH_IN',
     'a figure floating in a tank of orange spice gas, eyes deep blue, stars swirling outside a window'),
    ('IMPERIUM_RISE', 'X', 'EW', [], 'PULL_OUT',
     'a new imperial capital rising in gold and white, starships overhead, dawn light over ruins of machines'),
    ('MOTHER_CHILD_STATUE', 'X', 'CU', [], 'PUSH_IN',
     'close on the stone face of a mother holding an infant on a giant statue, rain, eternal flame reflected'),
    ('BALCONY_DUSK', 'X', 'EST', [], 'PULL_OUT',
     'an empty ruined stone balcony at dusk, ivy, ember sky, a sense of ancient memory'),
    # ---- BATCH 15: pickups / alternates / outro
    ('SERENA_PRIESTESS_CU', 'V', 'CU', ['SERENA_OLD'], 'DRIFT',
     'portrait under ember banners, solemn and weary'),
    ('IBLIS_GP_CU', 'V', 'CU', ['IBLIS_GP'], 'PUSH_IN',
     'portrait, a knowing ruthless smile, candlelight'),
    ('XAVIER_OLD_CU', 'VII', 'CU', ['XAVIER_OLD'], 'DRIFT',
     'portrait, weary, honourable, cold starlight'),
    ('WATCHEYES', 'I', 'INS', [], 'PUSH_IN',
     'a single floating silver sphere watcheye with a glowing lens, close, reflections of a human face'),
    ('ROBOT_RANKS', 'III', 'EW', ['ROBOTS'], 'PULL_OUT',
     'endless ranks of identical robots standing in a machine hall, cold light'),
    ('SALUSA_NIGHT', 'V', 'EW', [], 'PAN_RL',
     'Zimia at night, warm lights, warships passing overhead, uneasy calm'),
    ('VORIAN_CORRIN_CU', 'IX', 'CU', ['VORIAN', 'VORIAN_CMDR'], 'PUSH_IN',
     'giving the order, cold and certain, red light'),
    ('POD_GILBERTUS', 'IX', 'MS', [], 'PUSH_IN',
     'a young man in a cargo pod holding the hand of a woman with amber-brown hair, both looking out at the fleet'),
    ('OUTRO_DUEL', 'CB', 'EW', ['VORIAN', 'ABULURD'], 'PUSH_IN',
     'two silhouetted men facing each other across a bridge at sunset, red sky, distance between them'),
    ('ENDCARD_STARS', 'CB', 'EW', [], 'PUSH_IN',
     'a calm starfield over a dark desert horizon with a thin ember glow, empty left half'),
]
assert len(S) == 150, len(S)


def prompt(sh):
    short, ch, typ, cast, recipe, subj = sh
    who = ', '.join(CAST[c] for c in cast)
    body = f'{who}. {subj}' if who else subj
    return f'{STYLE} {body}. {PALETTE} Camera: {CAMERA[typ]}. Texture: fine film grain, atmospheric haze, tactile materials. {NO_TEXT}'


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    idx = ['# DUN001 batch index (The Butlerian Jihad)', '', '| Batch | Scene | File | Ch | Type | Cast | Recipe |',
           '|---|---|---|---|---|---|---|']
    for b in range(15):
        bp = OUT / f'DUN001_BATCH{b + 1:03d}.json'
        prev = {i['key']: i for i in json.load(open(bp))['images']} if bp.exists() else {}
        prev_status = json.load(open(bp)).get('status', 'PLANNED') if bp.exists() else 'PLANNED'
        imgs = []
        for j in range(10):
            n = b * 10 + j + 1
            sh = S[n - 1]
            fname = f'DUN001_BATCH{b + 1:03d}_SCENE{n:03d}_{sh[0]}.png'
            imgs.append({'scene_id': f'DUN001_SCENE{n:03d}', 'key': f'B{b + 1:03d}S{n:03d}', 'file': fname,
                         'chapter': sh[1], 'shot_type': sh[2], 'cast': sh[3], 'motion_recipe': sh[4],
                         'prompt': prompt(sh), 'negative': NEGATIVE, 'refs': [], 'qc': 'PENDING'})
            old = prev.get(imgs[-1]['key'], {})
            for k in ('qc', 'refs', 'drive_file_id', 'notes'):
                if k in old:
                    imgs[-1][k] = old[k]
            idx.append(f'| {b + 1:03d} | {n:03d} | {fname} | {sh[1]} | {sh[2]} | {", ".join(sh[3])} | {sh[4]} |')
        json.dump({'episode': 'DUN001', 'batch': f'BATCH{b + 1:03d}', 'max_batch_size': 10, 'status': prev_status,
                   'style': STYLE, 'palette': PALETTE, 'images': imgs},
                  open(OUT / f'DUN001_BATCH{b + 1:03d}.json', 'w'), indent=1, ensure_ascii=False)
    (OUT / 'DUN001_BATCH_INDEX.md').write_text('\n'.join(idx) + '\n')
    lb = ['# DUN001 look-book (continuity sheets)', '', 'Text anchors used in every prompt; batch 1 portraits become '
          'the image references (`19_batches/DUN001/anchors/`).', '']
    lb += [f'- **{k}**: {v}' for k, v in CAST.items()]
    (OUT / 'DUN001_LOOKBOOK.md').write_text('\n'.join(lb) + '\n')
    print('wrote 15 batches,', len(S), 'shots')


if __name__ == '__main__':
    build()
