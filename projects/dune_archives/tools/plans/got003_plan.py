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
]
