# PART 6Z — IMAGE PROMPT BATCH 032 (`VAL-EP001-IMG0311` – `VAL-EP001-IMG0320`)

**Series:** *The Ancient World of Ice and Fire*
**Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
**Batch:** 032 of 105 · `10:20–10:40` · 10 frames · 2 seconds/frame

**Visual standard:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.

**Continuity:** The answer to the vanished flocks arrives, and then the masters of the mountain. *…the mountain air tasted of iron and ash, early Valyrian climbers found the grim answer to their vanished flocks: bones, blackened and half-melted into the rock. No mountain wolf or shadowcat left stone vitrified into shining glass. Drawn by dread and wonder alike, the first witnesses crept to the thresholds of the great volcanic caverns opening beneath the caldera rims…*

**Structure — two movements, one hinge.** `IMG0311`–`IMG0315` are the evidence: bones fused into black glass, no animal that could have done it. `IMG0316`–`IMG0320` are the thresholds: the clan creeping to the cavern rims, and **`DRG-VAL-001` seen for the first time**. The batch hinges exactly at `IMG0316`.

**Director's decision — the dragon is revealed in fragments, not in a hero shot.** This is a first sighting by frightened shepherds, not a poster. So: `IMG0316` gives a shape at extreme scale, mostly negative space and a wing-shoulder out of frame; `IMG0317` gives it through a gap between columns, half-occluded; `IMG0318` gives an eye and a horn, close and unreadable; `IMG0319` gives an ultra-wide silhouette in a magma-lit chamber at the limit of legibility; and only `IMG0320` gives a fuller read, and even then the animal is coiled, distant and turned away. **It is never centred, never posed, never facing camera, and never breathing fire in this batch.**

**Anatomy lock — the one thing that cannot be got wrong.** `DRG-VAL-001` is **strictly four-limbed**: two hind legs and two wings, the wings acting as forelimbs when grounded. Six-limbed dragons (four legs plus a separate pair of wings) are forbidden by the book-canon rule in the location bible and are the single most likely failure here. Every prompt states the limb count in the subject text *and* negates extras. Scale ~150 ft, basalt-black `#1A1B1E`, twin swept-back obsidian horns, brass-gold slit eyes, ember glow only deep in the throat.

**Bones are evidence, not gore.** `IMG0311`–`IMG0315` show ribs and a horned sheep skull **fused and half-dissolved into vitrified black glass** — melted *into* the rock, not lying on it. No blood, no flesh, no carcass, no predator, no tooth marks: the horror is that the stone itself has been altered.

**Standing rules carried in from Batches 028–031:**
- **The elder is checked at 300% every time.** Three batches of bald-crown and long-coat drift; his hair is described as covering the crown and his cloak as knee-length, with baldness, hoods and long coats negated.
- **Pale ground must stay black.** A Batch 031 pass read as snow from ash crust alone; every prompt negates pale white ground crust.
- **Crowds must be scattered.** Different distances, heights and postures, or the render becomes a line-up.
- **Wide-shot eye rule:** nothing wider than a 50mm MCU exposes human iris colour.

**Render/QC status:** **8 of 10 approved and MD5-verified on Drive; 2 pending.** All ten frames are native `1376x768` sRGB PNGs.

| Frame | Status | Note |
| :--- | :--- | :--- |
| `IMG0311` | ✅ Approved, uploaded | Vitrified wall, ribs + horned skull fused into glass, herdsman tiny at base, no face. |
| `IMG0312` | ✅ Approved, uploaded | Macro ribs in black glass, meniscus bright on one edge, no gore. |
| `IMG0313` | ✅ Approved, uploaded | Passed after letterbox reframe (rows 12–755). Strict profile, no eye. |
| `IMG0314` | ✅ Approved, uploaded | Macro horned skull half-dissolved into melt, no people. |
| `IMG0315` | ✅ Approved, uploaded | **Pass 3.** Bones genuinely embedded under a hard glass casing; black ground edge to edge; elder mid-thigh cloak, full crown. Reframed rows 12–755, Drive copy replaced. |
| `IMG0316` | ❌ 4th pass queued | **Bird anatomy.** Limbs now correct (two hind legs, two wings) and the elder is fixed, but the folded wing wrist renders as a pointed **golden beak** with the snout suppressed. |
| `IMG0317` | ✅ Approved, uploaded | **Pass 3.** Fully interior, raw fractured ledge, no flame, correct crocodilian skull. |
| `IMG0318` | ✅ Approved, uploaded | Passed after letterbox reframe (rows 44–675). Silhouette only, four limbs, no humans. |
| `IMG0319` | ✅ Approved, uploaded | **Pass 2.** Crowd genuinely scattered, dull ember cracks only, dragon on a shattered tilted slab. Reframed rows 12–755. |
| `IMG0320` | ❌ Regenerate | Approved on pass 1, but the file was lost in a sandbox reset before its upload landed and `assets/` is gitignored. Composition preserved below. |

**Rerender briefs, both queued behind the 10-images-per-turn cap:**

1. **`IMG0316` — the wing wrist is reading as a beak.** The fix is not more "no beak" in the negative list; it is making the joint a *blunt, rounded, scaled knuckle* described positively ("overlapping scale rings, no hook, no point, no protrusion") and rotating the pose back to a wing-shoulder that runs out of frame, rather than a near-side-on animal whose wrist points into open space. State "reptile, not bird — long low crocodilian skull with a blunt squared snout" in the subject text itself.
2. **`IMG0320` — regenerate.** No local copy and no Drive copy survive. Rebuild to the recorded composition: 50mm MCU, head and shoulders behind a black rock lip, head turned away with no eye to camera, soot, two narrow temple braids, warm ember rim from off-frame right.

**Pass-one-through-three lessons to carry into Batch 033:**

1. **Stating the limb count is not enough** — the *ground contact* has to be described (two taloned feet plus two wing-knuckles, nothing else), or the wing-shoulder framing leaves room for a phantom third leg.
2. **"Embedded, not resting on" needs a material model.** "Bones fused into glass" rendered bones lying on a slab three times running; "thick glass has flowed over the bones and set hard, each bone locked under the surface with only its upper face exposed, no contact shadow beneath it" finally worked. Value matters as much as geometry: bright white bone also read as clean and new, so the bone had to be described as dirty tan-grey, close in value to the slab.
3. **A folded wing wrist will grow a beak.** Any pointed or hooked protrusion at the end of a wing membrane reads as a bird bill at cinema scale. The joint must be written as a blunt scaled knuckle.
4. **"Magma-lit" produces fire.** Even with "no fire" negated, a warm wall behind the animal rendered as a literal column of flame; the acceptable language is dull ember-red heat *inside the rock*, evenly diffuse, with the throat unlit.
5. **Columnar basalt drifts to masonry from any level ledge.** Angled slabs, snapped plates and irregular shattered blocks survive; horizontal flat-topped ledges do not.
6. **Pale mineral crust still reads as snow** under cold grey key (ninth occurrence); ground must be described as pure matte black wet basalt with black glass shards.

## PROMPT 311 — `VAL-EP001-IMG0311`

1. **Scene ID:** `VAL-EP001-IMG0311`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:20–10:22`
4. **Narration reference:** “of iron and ash,”
5. **Main subject:** Towering low-angle composition inside the chamber: a wall of black vitreous rock rises out of the top of frame, and low across its face runs a fused seam of half-melted bone — ribs and a horned sheep skull locked into the glassy black stone as though poured into it, pale against the black, partly submerged. The young herdsman stands at the bottom of frame, small, back to camera, one hand not quite touching the seam.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, shoulder-blade length, worn loose with two thin narrow temple braids only; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear. Rear view, very small against the wall: no face.
7. **Environment:** `LOC-VAL-003` — a vitrified wall face inside the caldera chamber, black glass with bone fused into it, thin steam in the seams.
8. **Camera:** Towering vertical low-angle framing — Panavision Primo 24mm, camera low and close to the wall.
9. **Lighting/materials:** Cold grey key, the fused bone catching a pale flat light, black glass holding a wet specular sheen.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:20–10:22`; physically plausible period detail.
11. **Mood:** Something was here, and the stone took it in.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 312 — `VAL-EP001-IMG0312`

1. **Scene ID:** `VAL-EP001-IMG0312`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:22–10:24`
4. **Narration reference:** “early Valyrian climbers found the”
5. **Main subject:** Macro material insert, no people: extreme close detail of sheep ribs fused into black volcanic glass, the bone surface pale and calcined where it meets the melt, the glass flowing over and between the rib ends with a smooth meniscus. A little thin ash dust in the hollows. No flesh, no blood, no tooth marks.
6. **Character continuity:** None in frame. The fused bone is the subject.
7. **Environment:** `LOC-VAL-003` — a shelf of vitrified black glass with bone locked into it.
8. **Camera:** Macro environmental and material texture insert — Panavision Primo 85mm, very shallow focus, raking side light.
9. **Lighting/materials:** Cold raking light so the glass meniscus reads bright along one edge, bone matte, deep black shadow.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:22–10:24`; physically plausible period detail.
11. **Mood:** The stone has a texture now that no weather makes.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 313 — `VAL-EP001-IMG0313`

1. **Scene ID:** `VAL-EP001-IMG0313`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:24–10:26`
4. **Narration reference:** “grim answer to their”
5. **Main subject:** Intimate close-up: the young herdsman crouched low, seen in strict profile and from slightly behind so his face is almost entirely turned away; his jaw is set, and his hand is braced on the black glass beside the fused bone seam. Soot on his cheekbone, pale hair fallen forward across the side of his face. Behind him out of focus the chamber wall.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, shoulder-blade length, worn loose with two thin narrow temple braids only; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear. Strict profile, face turned away from camera: no eye visible.
7. **Environment:** `LOC-VAL-003` — vitrified wall and broken black floor immediately around him.
8. **Camera:** Intimate close-up detail and expression beat — Panavision Primo 85mm, wide open, low.
9. **Lighting/materials:** Cold flat light, warm faint orange bounce from a distant vent low on his jaw, soot and damp.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:24–10:26`; physically plausible period detail.
11. **Mood:** Grief arriving late, at the speed the evidence allows.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 314 — `VAL-EP001-IMG0314`

1. **Scene ID:** `VAL-EP001-IMG0314`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:26–10:28`
4. **Narration reference:** “vanished flocks: bones, blackened and”
5. **Main subject:** Extreme close-up tactile study: a horned sheep skull half-submerged in black vitrified glass, one horn intact and ridged, the eye socket filled and smoothed over by the melt, the bone surface blackened to charcoal-brown where the heat took it. Nothing else in frame but black glass and a dusting of grey ash.
6. **Character continuity:** None in frame.
7. **Environment:** `LOC-VAL-003` — melted black glass surface with a skull set into it.
8. **Camera:** Extreme close-up tactile and light study — Panavision Primo 100mm macro, very shallow focus, top light.
9. **Lighting/materials:** Cold top light, bone reading dull charcoal rather than white, glass glossy black, fine ash dust.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:26–10:28`; physically plausible period detail.
11. **Mood:** Not a kill. A melting. The difference is the whole chapter.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 315 — `VAL-EP001-IMG0315`

1. **Scene ID:** `VAL-EP001-IMG0315`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:28–10:30`
4. **Narration reference:** “half-melted into the rock.”
5. **Main subject:** Transitional wide framing, closing the evidence movement: the chamber floor seen across, with a long low ridge of vitrified black glass in the middle distance into which a scatter of pale bone shapes are fused — ribs, a spine, horned skulls, all merged and part-dissolved. Two small figures stand at the near edge of it, both seen from behind, both still. Steam drifts across.
6. **Character continuity:** `CHAR-VAL-001`: 48-year-old elder — gaunt weathered face, FULL HEAD of cool ash-white hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown covering the crown with no balding and no visible scalp, long past the shoulders and half-bound at the nape, BARE HEAD with no hood, broad square male shoulders, rough KNEE-LENGTH grey felted wool cloak stopping above the boot tops so trousers and boots show, ragged undyed raw sheepskin mantle, bronze-shod ash crook. and `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, shoulder-blade length, worn loose with two thin narrow temple braids only; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear. as two small rear-view figures at the edge; no facial detail.
7. **Environment:** `LOC-VAL-003` — the vitrified floor ridge, black glass plates, grey ash, sulphur seams beyond and layered steam.
8. **Camera:** Transitional wide framing — Panavision Primo 40mm, eye level, deep stop.
9. **Lighting/materials:** Cold grey light, the vitrified ridge catching a hard sheen, bones matte and pale.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:28–10:30`; physically plausible period detail.
11. **Mood:** A whole flock, reduced to a texture in the rock.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 316 — `VAL-EP001-IMG0316`

1. **Scene ID:** `VAL-EP001-IMG0316`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:30–10:32`
4. **Narration reference:** “No mountain wolf or”
5. **Main subject:** Low-angle monumental geological framing, and the first sight of the animal. The frame is mostly black rock and steam: a vast wing-shoulder and the base of one folded wing fill the upper right and run out of frame, basalt-black and charcoal plated, the leathery membrane veined, a single curved obsidian horn tip just catching light. The creature is strictly four-limbed — two hind legs and two wings, the wing being a forelimb. It is enormous, out of scale with everything, NOT centred and NOT facing the viewer. In the lower left, tiny, the elder and the young herdsman stand frozen at the threshold, seen from behind.
6. **Character continuity:** `CHAR-VAL-001`: 48-year-old elder — gaunt weathered face, FULL HEAD of cool ash-white hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown covering the crown with no balding and no visible scalp, long past the shoulders and half-bound at the nape, BARE HEAD with no hood, broad square male shoulders, rough KNEE-LENGTH grey felted wool cloak stopping above the boot tops so trousers and boots show, ragged undyed raw sheepskin mantle, bronze-shod ash crook. and `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, shoulder-blade length, worn loose with two thin narrow temple braids only; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear. as two tiny rear-view figures at the lower left; no facial detail.
7. **Environment:** `LOC-VAL-003` — a cavern threshold beneath the caldera rim, black vitrified rock, thin steam, deeper black beyond.
8. **Camera:** Low-angle monumental framing — Panavision Primo 28mm, camera low, subject filling the upper right corner.
9. **Lighting/materials:** Cold grey key from the chamber mouth, warm ember-orange rim light along the wing edge from somewhere deeper in.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:30–10:32`; physically plausible period detail.
11. **Mood:** The frame where the episode stops being about shepherds.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 317 — `VAL-EP001-IMG0317`

1. **Scene ID:** `VAL-EP001-IMG0317`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:32–10:34`
4. **Narration reference:** “shadowcat left stone vitrified into”
5. **Main subject:** Over-the-shoulder depth perspective through a gap between two leaning basalt columns: in the sharp distance, half-occluded by the columns, the dragon lies coiled on a ledge — its long crocodilian skull turned away and down, one horn silhouetted, one folded wing rising like a ridge of black rock. The creature is strictly four-limbed: two hind legs and two wings only, no extra legs. The near foreground is the blurred shoulder and pale hair of the young herdsman, cropped at the neck.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, shoulder-blade length, worn loose with two thin narrow temple braids only; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear. foreground shoulder and hair only, cropped. `DRG-VAL-001` (first appearance, the reveal): an enormous wild caldera dragon, strictly FOUR limbs in total — two muscular taloned hind legs and two vast bat-like forelimb wings, walking on calloused wing-knuckles when grounded, absolutely never six limbs and never four legs plus wings. Volcanic basalt-black scales the colour of #1A1B1E with oxidised charcoal plating, a long crocodilian skull, twin swept-back curved obsidian horns, sulfur-crusted nostrils, and molten brass-gold vertical-slit eyes that catch light from below. ~150 ft of body. Ember-orange incandescent glow only deep in the throat and along the throat fissures when breathing, never a fireball. in the distance, partially hidden.
7. **Environment:** `LOC-VAL-003` — a column gap framing a deeper ledge, black rock, steam, faint ember glow low behind the animal.
8. **Camera:** Over-the-shoulder depth perspective — Panavision Primo 40mm, shallow focus on the far ledge.
9. **Lighting/materials:** Cold foreground, warm ember light deep in the recess, strong silhouette separation.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:32–10:34`; physically plausible period detail.
11. **Mood:** Seen through rock, the way a frightened person actually sees it.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 318 — `VAL-EP001-IMG0318`

1. **Scene ID:** `VAL-EP001-IMG0318`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:34–10:36`
4. **Narration reference:** “shining glass. Drawn by”
5. **Main subject:** Deep-focus wide atmospheric composition of the cavern interior: a magma-lit chamber with a low ember glow along the far wall, and against it, distant and enormous, a coiled dragon silhouette with two folded wings rising above its back like black sails. Two curved horns break the profile. The creature is strictly four-limbed — two hind legs and two wings, no extra legs. Human figures are absent. Everything is dark and the animal is at the limit of legibility.
6. **Character continuity:** `DRG-VAL-001` (first appearance, the reveal): an enormous wild caldera dragon, strictly FOUR limbs in total — two muscular taloned hind legs and two vast bat-like forelimb wings, walking on calloused wing-knuckles when grounded, absolutely never six limbs and never four legs plus wings. Volcanic basalt-black scales the colour of #1A1B1E with oxidised charcoal plating, a long crocodilian skull, twin swept-back curved obsidian horns, sulfur-crusted nostrils, and molten brass-gold vertical-slit eyes that catch light from below. ~150 ft of body. Ember-orange incandescent glow only deep in the throat and along the throat fissures when breathing, never a fireball. at distance, in silhouette, coiled: the whole animal reads but no fine detail.
7. **Environment:** `LOC-VAL-003` — a deep chamber with a faint ember-lit far wall, layered steam, black glass floor.
8. **Camera:** Deep-focus wide atmospheric composition — Panavision Primo 28mm, deep stop, from the threshold.
9. **Lighting/materials:** Low ember glow from the far wall, cold grey from the chamber mouth, extreme tonal separation.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:34–10:36`; physically plausible period detail.
11. **Mood:** Scale you have to read twice before you believe it.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 319 — `VAL-EP001-IMG0319`

1. **Scene ID:** `VAL-EP001-IMG0319`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:36–10:38`
4. **Narration reference:** “dread and wonder alike,”
5. **Main subject:** Ultra-wide establishing vista of the whole chamber: the immense black space, columns leaning in from both sides, a river of dull ember light along the floor far below, and coiled on a ledge above it the dragon, dwarfing everything, two folded wings, head laid down. The creature is strictly four-limbed — two hind legs and two wings. At the bottom edge, absurdly small, five or six clansfolk stand at the threshold, all seen from behind, none distinguishable.
6. **Character continuity:** Clan: Valyrian clansfolk at extreme distance, rear views only, all with long pale ash-white hair, cream, oatmeal and mid-grey wool, knee-length or shorter garments. `DRG-VAL-001` (first appearance, the reveal): an enormous wild caldera dragon, strictly FOUR limbs in total — two muscular taloned hind legs and two vast bat-like forelimb wings, walking on calloused wing-knuckles when grounded, absolutely never six limbs and never four legs plus wings. Volcanic basalt-black scales the colour of #1A1B1E with oxidised charcoal plating, a long crocodilian skull, twin swept-back curved obsidian horns, sulfur-crusted nostrils, and molten brass-gold vertical-slit eyes that catch light from below. ~150 ft of body. Ember-orange incandescent glow only deep in the throat and along the throat fissures when breathing, never a fireball. coiled above them, enormous.
7. **Environment:** `LOC-VAL-003` — the full cavern chamber, black glass floor, ember-lit fissure, layered steam, columns.
8. **Camera:** Ultra-wide establishing vista — Panavision Primo 24mm, deep stop, from high at the threshold.
9. **Lighting/materials:** Ember glow low, cold grey above, heavy shadow, steam catching the warm light.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:36–10:38`; physically plausible period detail.
11. **Mood:** The first congregation, and it has no idea it is being watched.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage

## PROMPT 320 — `VAL-EP001-IMG0320`

1. **Scene ID:** `VAL-EP001-IMG0320`
2. **Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
3. **Timestamp:** `10:38–10:40`
4. **Narration reference:** “the first witnesses crept to”
5. **Main subject:** Medium close-up, closing the batch on the human face rather than the animal: the young herdsman's head and shoulders, crouched behind a lip of black rock, his head turned away and slightly down so only the line of his jaw, cheek and brow show; his eyes are wide and fixed on something out of frame and out of sight, his mouth slightly open, soot on his cheekbone, hair hanging forward. The rock in front of him is black and wet.
6. **Character continuity:** `CHAR-VAL-002` (Stage A): 24-year-old young Valyrian herdsman — sharp chiselled face, high angular cheekbones, hard masculine jaw, clean-shaven with faint stubble shadow, cool porcelain-ivory skin smudged with basalt soot, hair colour #EFE8D8, a cool luminous pale silver-gold that reads almost white in cold light — never blonde, never honey, never brown, shoulder-blade length, worn loose with two thin narrow temple braids only; ash-grey wool tunic, plain brown leather jerkin, rawhide forearm wraps, goat-leather boots with wrapped cross-bound gaiters, bronze-tipped mountain spear. Head turned away past the camera, sighting off-frame: no eye and no face to camera.
7. **Environment:** `LOC-VAL-003` — the black rock lip he is hiding behind, steam rising beyond it.
8. **Camera:** Medium close-up atmospheric focal beat — Panavision Primo 50mm, close, shallow focus.
9. **Lighting/materials:** Warm ember rim light from off-frame right, cold key on the far cheek, deep shadow.
10. **Composition:** Full-bleed 16:9 cinematic frame at `10:38–10:40`; physically plausible period detail.
11. **Mood:** The face of a man who has just understood his own size.
12. **Visual style:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded period detail, obsidian black, sulphur yellow and cold grey palette, restrained natural film grain, realistic exposure.
13. **Output:** 16:9, target `1376x768`, sRGB PNG.
14. **Negative prompt:** no faces turned to camera, no glowing eyes, no violet iris,, no six-limbed dragon, no four legs plus wings, no extra legs, no second pair of wings, no feathered wings, no bird anatomy, no horse or wolf anatomy, no glowing red or orange body, no fire breath fireball, no flame jet, no smoke from the mouth, no cut or forged stone, no masonry, no temple, no mine timber, no writing or runes, no hood, no cowl, no ankle-length coat, no balding, no bald crown, no visible scalp, no braided crown, no fishtail braid, no shaved scalp, no blonde or honey hair, no snow, no ice, no frost, no pale white ground crust, no modern objects, no text, watermark, map, borders, letterboxing, black bars, collage
