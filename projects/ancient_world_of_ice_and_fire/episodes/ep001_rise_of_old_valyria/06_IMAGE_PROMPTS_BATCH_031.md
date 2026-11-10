# PART 6Y — IMAGE PROMPT BATCH 031 (`VAL-EP001-IMG0301` – `VAL-EP001-IMG0310`)

**Series:** *The Ancient World of Ice and Fire*
**Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
**Batch:** 031 of 105 · `10:00–10:20` · 10 frames · 2 seconds/frame

**Visual standard:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.

**Continuity:** **Chapter III opens here.** *Above six thousand feet on the slopes of the Fourteen Flames, the world of grass and olive trees died abruptly. In its place stretched a cathedral of shattered black glass, hexagonal basalt pillars, and steaming yellow sulfur fissures. Here, where the mountain air tasted of iron and ash…* The pasture is gone; every frame in this batch is above the tree line at `LOC-VAL-003`, and the palette shifts from emerald to obsidian, sulphur and cold grey.

**Director's decision — a cathedral that nobody built.** The narration calls it a *cathedral*, and the temptation is to render architecture. The whole point is that it **isn't** architecture: it is a collapse chamber of natural basalt columns, chaotic, of wildly uneven height, leaning and fallen, with broken shards underfoot. No nave, no symmetry, no altar, no floor plan, no cut stone, no forge or mine timber. The awe comes from scale and disorder, not from design. Every frame carries the negation *no forged or carved stone, no masonry, no temple, no mine structure*.

**Director's decision — two things are withheld.**
1. **No dragons.** `DRG-VAL-001` is introduced at `IMG0316`; nothing in this batch may hint at a dragon — no silhouette on a ledge, no wing-shadow, no tail, no claw marks. One glimpse here would spend the reveal twice.
2. **No bones.** The *"bones, blackened and half-melted into the rock"* line lands at `IMG0311`–`IMG0315`, in Batch 032. This batch is the place the flocks were taken **to**, not the answer. The black rock must read as **vitrified stone, not charred remains** — the negations carry *no bones, no skull, no corpses*.

**Standing rules carried in from Batches 028–030:**
- **Hair value is now explicit and single:** `#EFE8D8`, a cool luminous pale silver-gold that reads almost white in cold light. Hair tone drifted frame to frame across three batches; this batch fixes one value in every prompt.
- **The elder is never hooded and never long-coated.** Two batches lost frames to an ankle-length flared coat with a hood up, so the positive knee-length description and the hood/cowl/long-coat negations both appear every time he is in frame.
- **Wide-shot eye rule:** nothing wider than a 50mm MCU exposes iris colour. `IMG0305` is the one 50mm and its subject is looking up and away; `IMG0307` at 65mm is seen from behind.
- **Plaiting negated explicitly**, not just omitted: no braided crown, no fishtail plait, no shaved sides.

**Render/QC status:** Batch complete — all ten frames visually approved, `1376x768` sRGB PNGs, uploaded to Drive folder `https://drive.google.com/drive/folders/1XqRVZAcPjVjPK7EjcQaYLWCxE4yvfYTF` and MD5-verified. Eight passed first time. `IMG0303` and `IMG0309` were held because the elder drifted bald-crowned and long-coated for the third consecutive batch. `IMG0309` then took four attempts: a bald crown, then a corrected head with a long cloak plus a floating pale blade artifact and near-black garments, then a version whose pale ash crust read as snow, then a version that turned the whole group into a row of identical hooded silhouettes. The approved frame scatters five figures at different distances and heights, each in a different posture, and keeps the ground pure matte black. **Lessons now written into the prompts: pale ash crust on black ground must never be rendered light enough to read as snow; a crowd prompt must specify different distances, heights and postures or it collapses into a line-up; and the elder's hair must be described as covering the crown, not merely as long.**

## PROMPT 301 — `VAL-EP001-IMG0301`

1. **Scene ID:** `VAL-EP001-IMG0301`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:00–10:02`
4. **Narration reference:** “Above six thousand feet”
5. **Main subject:** Low-angle monumental geological framing, camera close to the ground on a shelf of black rock: above and beyond, a wall of shattered black volcanic glass and leaning hexagonal basalt columns rises out of the top of frame, one column much taller than the rest, all of them chaotic and uneven. In the lower third, small and low, the young herdsman has just come up over the lip of the shelf on hands and knees and stopped dead, head lifted, staring up at the columns. He is seen from behind and slightly to the side.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. Rear three-quarter view, face not visible.
7. **Environment:** `LOC-VAL-003` — the basal shelf of a caldera collapse chamber above the tree line: black vitreous rock, broken shards underfoot, thin yellow sulphur staining, wisps of steam; no vegetation beyond a few dead grass tufts.
8. **Camera:** Low-angle monumental geological framing — Panavision Primo 28mm, camera at ground level, slight off-axis.
9. **Lighting/materials:** Cold grey light from a high overcast, hard specular glints off the glassy rock, sulphur yellow picking out the cracks.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:00–10:02`; physically plausible period detail; raw natural rock only.
11. **Mood:** The moment a shepherd realises the world above the grass is not for him.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 302 — `VAL-EP001-IMG0302`

1. **Scene ID:** `VAL-EP001-IMG0302`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:02–10:04`
4. **Narration reference:** “on the slopes of the”
5. **Main subject:** Over-the-shoulder depth perspective: the elder's shoulder, sheepskin mantle and the head of his crook soft and large in the near foreground at the left; beyond him in sharp focus a field of leaning basalt columns and cracked black glass receding into steam, with the young herdsman a small isolated figure standing at the base of the tallest column, looking up. Neither man faces camera.
6. **Character continuity:** `CHAR-VAL-001`: 48-year-old elder flock-master — gaunt high-cheekboned weathered face, cool ash-white hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey long past the shoulders and half-bound at the nape, full head of hair with no balding, BARE HEAD with no hood or cowl, broad square male shoulders, rough KNEE-LENGTH grey felted wool cloak stopping above the boot tops so trousers and boots show, ragged undyed raw sheepskin mantle, bronze-shod ash crook; crude handmade garments only, never a long flared coat. foreground shoulder only, cropped at the neck. `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. in focus at distance, rear view.
7. **Environment:** `LOC-VAL-003` — a broad shelf of black glass and basalt running back into steam, sulphur vents low on the ground, no sky visible in the middle of frame.
8. **Camera:** Over-the-shoulder depth perspective — Panavision Primo 40mm, shallow focus on the far figure.
9. **Lighting/materials:** Cold backlight through steam, warm iron-orange reflection low on the wet stone.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:02–10:04`; physically plausible period detail.
11. **Mood:** The old man letting the boy go first, because he remembers what is up here.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 303 — `VAL-EP001-IMG0303`

1. **Scene ID:** `VAL-EP001-IMG0303`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:04–10:06`
4. **Narration reference:** “Fourteen Flames, the world”
5. **Main subject:** Deep-focus wide atmospheric composition: a vast interior basin of black volcanic glass and hexagonal columns, the far wall lost in steam, the floor cracked into plates that catch a hard metallic sheen. Two tiny figures stand on the near lip, dwarfed, both seen from behind. The scale is geological and indifferent: no symmetry, no axis, no path.
6. **Character continuity:** `CHAR-VAL-001`: 48-year-old elder flock-master — gaunt high-cheekboned weathered face, cool ash-white hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey long past the shoulders and half-bound at the nape, full head of hair with no balding, BARE HEAD with no hood or cowl, broad square male shoulders, rough KNEE-LENGTH grey felted wool cloak stopping above the boot tops so trousers and boots show, ragged undyed raw sheepskin mantle, bronze-shod ash crook; crude handmade garments only, never a long flared coat. and `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. as two small rear-view figures on the lip; no facial detail.
7. **Environment:** `LOC-VAL-003` — a collapsed caldera chamber open to the sky, black vitrified floor, columns leaning inward, yellow sulphur crust and steam in the middle distance.
8. **Camera:** Deep-focus wide atmospheric composition — Panavision Primo 28mm, slightly elevated, deep stop.
9. **Lighting/materials:** Grey overcast light falling into the chamber, steam diffusing it, cold blue-grey shadows.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:04–10:06`; physically plausible period detail; no architecture of any kind.
11. **Mood:** Enormous, and entirely unarranged — which is what makes it feel sacred.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 304 — `VAL-EP001-IMG0304`

1. **Scene ID:** `VAL-EP001-IMG0304`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:06–10:08`
4. **Narration reference:** “of grass and olive trees”
5. **Main subject:** Ultra-wide establishing vista from the chamber rim looking back and down: the black rock shelf in the foreground, and far below it the green world they came from — pasture terraces, the silver line of a river, a haze of olive scrub, the sea beyond. The transition from black to green runs across the frame as a hard irregular boundary, not a gradient.
6. **Character continuity:** None in frame. Pure landscape: the two worlds in one image.
7. **Environment:** `LOC-VAL-003` rim above `LOC-VAL-002` — black vitreous shelf in the near foreground giving way to green pasture far below, river, olive scrub, sea haze at the horizon.
8. **Camera:** Ultra-wide establishing vista — Panavision Primo 24mm, from the rim, looking down and back.
9. **Lighting/materials:** Cold grey light on the black rock, warmer haze over the green lowlands, deep atmospheric recession.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:06–10:08`; physically plausible period detail.
11. **Mood:** The exact line where the world they know stops.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 305 — `VAL-EP001-IMG0305`

1. **Scene ID:** `VAL-EP001-IMG0305`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:08–10:10`
4. **Narration reference:** “died abruptly. In its”
5. **Main subject:** Medium close-up, the human threshold of the chapter: the young herdsman's head and shoulders, turned away and angled up so only the line of his jaw, cheek and the edge of his brow are visible; soot smudged across his cheekbone, hair lifted and blown across his face by hot air, eyes narrowed against it (not visible to camera). Behind his shoulder, out of focus, black glass and drifting steam.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. Head turned away and lifted, sighting up the columns: no eye and no face to camera.
7. **Environment:** `LOC-VAL-003` — soft out-of-focus black rock and steam immediately behind him.
8. **Camera:** Medium close-up atmospheric focal beat — Panavision Primo 50mm, near, shallow focus.
9. **Lighting/materials:** Cold key from the left, faint warm orange bounce low from the rock, soot and damp on skin.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:08–10:10`; physically plausible period detail.
11. **Mood:** Air that tastes of iron, and a boy deciding he will keep going anyway.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 306 — `VAL-EP001-IMG0306`

1. **Scene ID:** `VAL-EP001-IMG0306`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:10–10:12`
4. **Narration reference:** “place stretched a cathedral”
5. **Main subject:** Dynamic medium lateral tracking angle: the two men walk left to right along the base of the column wall, small under it, the elder's crook clicking rock, the boy half a step behind and looking up. The columns rise out of frame above them; the ground is a chaos of broken glassy shards. The camera moves with them so the near columns streak slightly.
6. **Character continuity:** `CHAR-VAL-001`: 48-year-old elder flock-master — gaunt high-cheekboned weathered face, cool ash-white hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey long past the shoulders and half-bound at the nape, full head of hair with no balding, BARE HEAD with no hood or cowl, broad square male shoulders, rough KNEE-LENGTH grey felted wool cloak stopping above the boot tops so trousers and boots show, ragged undyed raw sheepskin mantle, bronze-shod ash crook; crude handmade garments only, never a long flared coat. leading, `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. half a step behind, both seen from behind at three-quarter.
7. **Environment:** `LOC-VAL-003` — a corridor of fallen basalt between leaning columns, shard-strewn floor, sulphur seams glowing dull yellow in the joints.
8. **Camera:** Dynamic medium lateral tracking angle — Panavision Primo 35mm, moving with the subjects, slight near-edge blur.
9. **Lighting/materials:** Hard cold side light, warm yellow seam glow, deep black shadow between columns.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:10–10:12`; physically plausible period detail; no built corridor, no paving, no cut steps.
11. **Mood:** It has the proportions of a nave by accident, and that accident is the point.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 307 — `VAL-EP001-IMG0307`

1. **Scene ID:** `VAL-EP001-IMG0307`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:12–10:14`
4. **Narration reference:** “of shattered black glass, hexagonal”
5. **Main subject:** Compressed telephoto detail with a figure for scale: the young herdsman stands facing away at the foot of a cluster of perfect hexagonal basalt columns, his shoulders and the back of his pale head just inside the bottom of frame, the columns filling the rest — faceted, wet, glassy, some with sheared tops, one split by a bright yellow sulphur seam. Compression flattens the depth so the columns stack against each other.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. rear view, cropped at the shoulders: no face.
7. **Environment:** `LOC-VAL-003` — a tight cluster of natural hexagonal columns, black glassy surfaces, yellow sulphur in the fractures, thin steam.
8. **Camera:** Compressed telephoto dramatic subject framing — Panavision Primo 65mm, long and flat.
9. **Lighting/materials:** Cold flat light, high specular sheen on the glassy facets, one warm yellow seam.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:12–10:14`; physically plausible period detail.
11. **Mood:** Geometry that looks designed and is not.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 308 — `VAL-EP001-IMG0308`

1. **Scene ID:** `VAL-EP001-IMG0308`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:14–10:16`
4. **Narration reference:** “basalt pillars, and steaming”
5. **Main subject:** Medium cinematic subject focus, low: a steaming yellow sulphur fissure runs diagonally across black glass in the foreground, its yellow crust cracked and bright, thin steam curling off it. Beyond, the young herdsman crouches at the edge with one hand held out toward the heat, not touching, face turned down and away. His spear lies on the rock beside him.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. Crouched, in profile away from camera, head bent over the fissure: no eye visible.
7. **Environment:** `LOC-VAL-003` — a sulphur fissure venting steam through black vitreous rock, yellow crystalline crust, heat shimmer.
8. **Camera:** Medium cinematic subject focus — Panavision Primo 50mm, low, near the fissure.
9. **Lighting/materials:** Cold ambient with warm glow rising from the fissure onto his hand and jaw, steam lit from beneath.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:14–10:16`; physically plausible period detail; steam and sulphur only, never magma or flame.
11. **Mood:** Reaching toward something that could kill him, the way the curious always do.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 309 — `VAL-EP001-IMG0309`

1. **Scene ID:** `VAL-EP001-IMG0309`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:16–10:18`
4. **Narration reference:** “yellow sulfur fissures. Here, where”
5. **Main subject:** Wide environmental storytelling tableau of the whole party arriving: five or six clansfolk strung out along the rim in ones and twos, some crouched, some standing with crooks, one holding a torchless staff, all small against the chamber. None of them is posed or facing the camera. The black glass floor and leaning columns fill the middle distance; steam hangs in layers.
6. **Character continuity:** Clan: Valyrian clansfolk, one locked people — alabaster-pale skin smudged with soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade to mid-back length, loose or half-bound at the nape with rawhide, uniform on every head, cream-and-charcoal homespun wool, felted grey cloaks, rawhide wraps, copper pins; no black dyes, no braided crowns, no shaved heads. `CHAR-VAL-001`: 48-year-old elder flock-master — gaunt high-cheekboned weathered face, cool ash-white hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey long past the shoulders and half-bound at the nape, full head of hair with no balding, BARE HEAD with no hood or cowl, broad square male shoulders, rough KNEE-LENGTH grey felted wool cloak stopping above the boot tops so trousers and boots show, ragged undyed raw sheepskin mantle, bronze-shod ash crook; crude handmade garments only, never a long flared coat. and `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. among them at distance.
7. **Environment:** `LOC-VAL-003` — the chamber floor and rim, black glass plates, stacked columns, sulphur seams, layered steam.
8. **Camera:** Wide environmental storytelling tableau — Panavision Primo 35mm, from slightly above, deep stop.
9. **Lighting/materials:** Cold grey key, warm sulphurous accents, long soft shadows in the column shadows.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:16–10:18`; physically plausible period detail; no paths, no cairns, no built structure.
11. **Mood:** A whole people standing at the edge of what they have been warned about for generations.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 310 — `VAL-EP001-IMG0310`

1. **Scene ID:** `VAL-EP001-IMG0310`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:18–10:20`
4. **Narration reference:** “the mountain air tasted”
5. **Main subject:** High-elevation geographic scale reveal from far above and outside: the caldera chamber as a black irregular scar in a green-grey mountain flank, columns like broken teeth along its rim, steam drifting out of it in a long plume, the pasture falling away below and the sea a bright band beyond. Two figures are visible only as specks on the near rim.
6. **Character continuity:** Two distant specks: `CHAR-VAL-001`: 48-year-old elder flock-master — gaunt high-cheekboned weathered face, cool ash-white hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey long past the shoulders and half-bound at the nape, full head of hair with no balding, BARE HEAD with no hood or cowl, broad square male shoulders, rough KNEE-LENGTH grey felted wool cloak stopping above the boot tops so trousers and boots show, ragged undyed raw sheepskin mantle, bronze-shod ash crook; crude handmade garments only, never a long flared coat. and `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, straight narrow nose, firm chin, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, never grey, shoulder-blade length, worn loose with two thin narrow temple braids only — no braided crown, no fishtail plait, no shaved sides, no undercut; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, dark brown wool trousers, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear, no armour, no ornament. at extreme distance, no detail whatever.
7. **Environment:** `LOC-VAL-003` seen from outside and above, set in the flank of a volcano above a green peninsula, sea at the horizon.
8. **Camera:** High-elevation geographic scale reveal — Panavision Primo 24mm, high, distant, looking in and down.
9. **Lighting/materials:** Cold silver light, deep atmospheric layers, the black scar reading almost matte against the green.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:18–10:20`; physically plausible period detail; no roads, no buildings, no smoke other than volcanic steam.
11. **Mood:** From up here the whole chapter is one small dark hole in a green country.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no dragon, no dragon silhouette, no dragon wing, no reptile, no lizard, no fossil, no skeleton, no animal bones, no bones of any kind, no skull, no corpses, no blood, no glowing magma lake, no lava flow, no fire, no molten glow, no forged or carved stone, no masonry, no temple, no mine structure, no wooden beams or props, no chains, no writing or runes, no hood, no cowl, no ankle-length coat, no full-length coat, no braided crown, no fishtail braid, no shaved scalp, no undercut, no blonde or honey hair, no soft feminine face, no actress likeness, no snow or ice, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage
