# PART 6AC — IMAGE PROMPT BATCH 044 (`VAL-EP001-IMG0431` – `VAL-EP001-IMG0440`)

**Series:** *The Ancient World of Ice and Fire*
**Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
**Batch:** 044 of 105 · `14:20–14:40` · 10 frames · 2 seconds/frame · Ch. IV

**Visual standard:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, physically grounded detail, restrained natural film grain. Two halves, two climates: **steaming Sothoryos jungle** then **black volcanic caldera**.

**Continuity:** *…from the bleak, icy wastes of Ib in the Shivering Sea to the steaming, plague-ridden jungles of Sothoryos in the far south, where smaller, fireless kin called wyverns still hunt today. Those scattered skeletons suggest a sobering truth: dragons once ranged across much of the prehistoric world, dying out everywhere else over unrecorded ages…*

**The argument closes and the counter-argument opens.** The bone evidence finishes its journey from ice to jungle, and then the narration turns: the same fossils that prove dragons existed everywhere also prove they *failed* everywhere except Valyria. The caldera half is where the episode pivots from "dragons were real" to "and only one place kept them."

**NEW LOCATION — `SOTH-JUNGLE`:**
- Steaming, plague-ridden, oppressive: wet black loam, grey limestone, buttress-rooted hardwoods, strangler vines, moss in sodden ropes, standing black water, steam haze.
- **Flat diffused steam-filtered light only.** No golden light, no sunbeams, no sun disc, no blue sky, no turquoise water, no beach, no bright flowers, no postcard tropics.
- Bone is black fossil, moss-taken, roots grown through it, and any fractured face shows **concentric lamellae** — the detail that proves bone rather than timber.
- Wyverns as **silhouettes only**: small, distant, no fire, no colour. No faces, no maester, no expedition.

**Render/QC status:** **6 of 10 approved and uploaded · 2 REJECTED · 2 not yet rendered.** Five letterbox crops.

| Frame | Status | Note |
| :--- | :--- | :--- |
| `IMG0431` | ✅ Approved, uploaded | 24mm steep up the trunk: black fossil arc swallowed by roots and moss. Reframed 12–755. |
| `IMG0432` | ✅ Approved, uploaded | **Proves it's bone.** 85mm macro, fractured cross-section with concentric lamellae. Reframed 12–755. |
| `IMG0433` | ✅ Approved, uploaded | 85mm: the split bone holding a mirror-still black pool, one leaf. Reframed 12–755. |
| `IMG0434` | ✅ Approved, uploaded | 100mm: the crimson-seeded seedling in the bone socket. *Note: greens slightly lush.* Reframed 12–755. |
| `IMG0435` | ✅ Approved, uploaded | 40mm: two wyverns as distant silhouettes over the muddy river. Reframed 12–755. |
| `IMG0436` | ❌ **REJECTED** | **Built cathedral nave** — fluted columns with capitals, rose-window aperture, plus lava bloom and white steam. |
| `IMG0437` | ✅ Approved, uploaded | **Best dragon frame of the production.** 40mm OTS; four limbs confirmed at 2x. Reframed 40–727. |
| `IMG0438` | ❌ **REJECTED** | Cour sed ashlar masonry and a carved frieze; glowing white god-ray beam. Same root cause. |
| `IMG0439` | ⏳ **PENDING** | Not rendered — cap exhausted by the jungle half and the two rejects. |
| `IMG0440` | ⏳ **PENDING** | Not rendered — same. |

**The repeat offender: the caldera keeps rendering as a cathedral.** `IMG0310` failed this way in Batch 031, and `0436` and `0438` both failed it again in the same batch. The mechanism is now clear and written into the bible: **"hexagonal basalt pillars rising to a lost ceiling" is read by the model as architecture**, because the phrase describes a *colonnade with a vault*. The fix is to describe rock as rock — prisms of uneven height, jagged broken tops, no capitals, no drum sections, no plinths, a ceiling of collapsed rubble and darkness — and to negate masonry, ashlar, arches, vaults, rose windows, frieze, pilasters and light shafts **by name**. Batch 031 learned this and it was not carried forward as a hard rule; it is now `9b` in the location bible.

**What worked, precisely.** `0432` and `0433` work because they specify bone *structure* — concentric lamellae, radial fracture lines, a water-worn glassy inner curve — rather than "ancient bone". `0437` works because the limb count is stated numerically and negatively at once ("exactly four limbs — no third leg, no fourth leg, no arms") and the dragon is described as *watching*, which gives it intent without a facial expression. `0435` works because the wyverns are small, distant and colourless.

**Lessons to carry into 045:**

1. **A colonnade is a building; a cluster of prisms is geology.** Never describe a rock chamber in architectural vocabulary — no "rising to a lost ceiling", no "between the pillars". Say prisms, broken tops, rubble, darkness.
2. **Structure is the difference between bone and wood.** Lamellae, fracture lines, porosity and a worn inner curve read instantly as skeletal; "old bone" reads as a log.
3. **State limb counts numerically *and* negatively, every single time.** It is the only reliable way to hold four limbs, and it must be re-checked at 2x on every dragon frame — `0437` passed only because it was checked.
4. **Deferral is cheaper than compromise, but two rejects in one batch is a signal, not bad luck.** Both came from the same prompt pattern; the pattern is now banned in writing rather than hoped against.
5. **Silhouettes carry mythic scale; detail destroys it.** `0435`'s wyverns are two dark marks in a grey sky and they are more convincing than any rendered creature would be at that distance.

**Next — Batch 045 (`IMG0441`–`0450`, `14:40–15:00`):** returns to the caldera with `LOC-VAL-003` and `DRG-VAL-001` as the taming riddle resolves. **Order of work:** re-render `0436` and `0438` first with the new anti-architecture brief, then render `0439` and `0440`, then open 045.
