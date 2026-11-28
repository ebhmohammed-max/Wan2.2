"""GOT003 shot plan -> data/got003_images.py rows + (later) data/got003.py shot anchors.
Entry: (sid, sentence_idx, anchor|None, shot, recipe); sid = script section (H, P, I..X, CA, CB), sentence_idx counts
sentences within the whole section as in 20_voiceover/GOT003/GOT003_vo_plan.json subsections joined in order.
shot = int (existing still), str (earlier slug) or ('SLUG', type, [cast], body, [refs]) -> new still numbered in order.
Maps and mockups are code-animated assets (see the script production plan); they are listed in MAPS / MOCKUPS, not here.
"""
B1 = [  # n, slug, chapter, type, cast, recipe, body, refs
 (1, 'AEGON_PORTRAIT', 'I', 'CU', ['AEGON'], 'PUSH_IN', 'portrait in a dark hall of black fused stone lit by braziers, the only figure in the image, looking slightly past the viewer', []),
 (2, 'VISENYA_PORTRAIT', 'I', 'CU', ['VISENYA'], 'PUSH_IN', 'portrait on a windswept black-stone battlement above a grey sea, the only figure in the image, a hard level gaze', []),
 (3, 'RHAENYS_PORTRAIT', 'I', 'CU', ['RHAENYS'], 'PUSH_IN', 'portrait in a warm firelit chamber with a lute and candles blurred behind her, the only figure in the image, amused bright eyes', []),
 (4, 'DAENYS_PORTRAIT', 'P', 'CU', ['DAENYS'], 'PUSH_IN', 'portrait sitting up in a canopied bed at night, a faint orange glow on her face as if from a distant fire, restrained, subtle, mouth NOT gaping, the only figure in the image', []),
 (5, 'AENAR_PORTRAIT', 'P', 'CU', ['AENAR'], 'PUSH_IN', 'portrait on a terrace of a pale Valyrian palace at dusk, a red volcanic glow on the horizon behind him, the only figure in the image', []),
 (6, 'GYLDAYN_DESK', 'P', 'MS', ['GYLDAYN'], 'PUSH_IN', 'seen from behind over his shoulder at a cluttered desk in a stone tower of the Citadel at night, stacks of old books and scrolls, one candle, writing in a large blank book, NO readable writing anywhere', []),
 (7, 'BALERION_REF', 'I', 'EW', ['BALERION'], 'PUSH_IN', 'flying low over a dark stormy sea at dusk with a black-stone island castle far below for scale, the castle tiny beneath his wings', []),
 (8, 'VHAGAR_REF', 'I', 'EST', ['VHAGAR'], 'PUSH_IN', 'perched on a black rock spire above crashing surf, wings half spread, smoke from her nostrils, overcast light', []),
 (9, 'MERAXES_REF', 'I', 'EST', ['MERAXES'], 'PUSH_IN', 'gliding over sunlit clouds at golden hour, wings fully spread, graceful', []),
 (10, 'IRON_THRONE_BOOK', 'II', 'EST', [], 'PUSH_IN', 'the Iron Throne as described in the books: an enormous asymmetric monstrosity of hundreds of half-melted fused sword blades, jagged spikes and twisted metal, far taller than a man, on a high stone platform reached by steep narrow iron steps, alone in a vast dim stone throne hall lit by shafts of light, huge black dragon skulls on the walls, EMPTY, NO people, NOT a neat chair', []),
]
N = lambda slug, typ, cast, body, refs=(): (slug, typ, cast, body, list(refs))
PLAN = [
 # ---------------- H (hook)
 ('H', 0, None, 4, 'PUSH_IN'),
 ('H', 1, None, N('VALYRIA_BURNING', 'EW', [], 'a vast ancient city of pale fused stone towers, bridges and domes on a peninsula at night, engulfed in fire, glowing red ash clouds above, seen from a distant hill, NO people visible'), 'PUSH_IN'),
 ('H', 2, None, N('MOUNTAIN_SPLITS', 'EW', [], 'a huge volcano splitting open in a cataclysmic eruption, a fountain of lava a thousand feet high, lightning in the ash plume, a chain of other erupting peaks behind it'), 'PUSH_IN'),
 ('H', 3, None, N('SEA_OF_FIRE', 'OH', [], 'high aerial view of a whole land drowning in a sea of fire and lava under a black sky, rivers of molten rock pouring into a boiling sea, the ruins of a city sinking'), 'PULL_OUT'),
 ('H', 4, None, 5, 'PUSH_IN'),
 ('H', 5, None, N('EXODUS_SHIPS', 'EW', [], 'a small fleet of dark ships with black sails crossing a grey open sea at dawn, five dragons of different colours flying above them in a loose line, a lonely smoking volcanic island on the far horizon'), 'DRIFT'),
 ('H', 6, None, 'MOUNTAIN_SPLITS', 'PULL_OUT'),
 ('H', 7, None, N('CONQUEST_TEASER', 'EW', [], 'three dragons, one colossal black, one bronze, one silver, flying low over a small army of soldiers with black banners marching inland from a beach with ships behind them, golden evening light, the soldiers tiny', [7, 8, 9]), 'PAN_LR'),
 ('H', 8, None, 10, 'PUSH_IN'),
 ('H', 9, None, N('KINGS_LANDING_DUSK', 'EW', [], 'a great medieval walled city on three hills beside a wide river mouth at dusk, a red stone castle on the highest hill, a huge domed stone dragonpit on another hill, smoke from thousands of chimneys, ships in the harbour, NO arches in the foreground'), 'PULL_OUT'),
 ('H', 10, None, N('DRAGONS_CLASH', 'EW', [], 'two huge dragons, one red and serpentine, one vast and bronze, locked together in a storm sky above a dark lake, wings tangled, lightning, seen from far below, no gore'), 'PUSH_IN'),
 ('H', 11, None, N('QUEEN_ACROSS_SEA', 'EST', [], 'a slender young woman with long pale silver-gold hair seen FROM BEHIND standing on a terrace of an eastern pyramid city at sunset, face NOT visible, three small young dragons, black, green and cream, perched and circling around her, a hazy sea beyond, the only person in the image'), 'PUSH_IN'),
 ('H', 13, None, N('TARGARYEN_BANNER', 'MS', [], 'a huge black silk banner with a red three-headed dragon rippling in the wind from a black stone tower, embers and smoke drifting past, dark sky'), 'PUSH_IN'),
 # ---------------- P (prologue)
 ('P', 0, None, 6, 'PUSH_IN'),
 ('P', 1, None, N('CITADEL_OLDTOWN', 'EW', [], 'an ancient grey stone city of the maesters on a river at night: many old stone towers, halls and bridges, a single immense stepped lighthouse tower rising above all of it with a fire burning at its summit, river mist, lamplight in windows, NO arches in the foreground'), 'PUSH_IN'),
 ('P', 4, None, N('SEPTON_WRITING', 'MS', [], 'a plump old septon in a white robe with a crystal on a cord seen in three-quarter view from behind, writing in a book by candlelight in a small stone sept chamber, his face hidden, a seven-sided crystal glinting, the only figure in the image, NO readable writing'), 'PUSH_IN'),
]
