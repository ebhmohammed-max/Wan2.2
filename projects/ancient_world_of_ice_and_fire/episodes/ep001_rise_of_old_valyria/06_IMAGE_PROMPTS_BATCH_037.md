# PART 6Z — IMAGE PROMPT BATCH 037 (`VAL-EP001-IMG0361` – `VAL-EP001-IMG0370`)

**Series:** *The Ancient World of Ice and Fire*
**Episode:** EP001 — *Before the Dragons: The Rise of Old Valyria*
**Batch:** 037 of 105 · `12:00–12:20` · 10 frames · 2 seconds/frame · Ch. IV

**Visual standard:** Photoreal live-action 65mm historical cinema, ARRI Alexa 65, Panavision Primo spherical primes, Kodak Vision3 500T, realistic physically grounded natural history detail, emerald highland green, weathered black basalt and cold grey mist, restrained natural film grain, realistic exposure.

**Continuity:** *For the pastoral clans below, discovery brought terror long before it promised dominion. A single hungry dragon descending through morning mist could scatter an entire valley's flock in heartbeats, leaving behind nothing save scorched wool, blackened stone, and smoking craters.*

**Structure — a new movement, and the return of people.** For nine batches the episode has been inside the caldera with the animal alone; from here it is outside, in `LOC-VAL-002`, among the clans. `0361`–`0365` are the pastoral world and the first sight of the thing coming down through mist; `0366`–`0370` are the raid itself and its aftermath. The emotional register moves from dread to **terror**, and the palette moves with it — emerald and grey daylight instead of obsidian and ember.

**Standing directives carried forward, plus two new ones:**
- **The dragon must be VISIBLE.** Fragments govern pose, not legibility.
- **The dark-is-beautiful rule inverts here.** In the caldera, dark meant keep the frame black. Here the frame must be *daylit*, which means the dragon is a dark silhouette against pale mist — so contrast, not luminance, carries it.
- **The location has a hard form.** *Round* low-slung basalt huts with *conical* slate roofs, wattle folds, open unenclosed meadow. No gables, no chimneys, no boundary walls, no field grid, no roads.
- **People are legible but never portrait-lit.** Backs of heads, profiles, mid-distance. Loose unbound silver-white hair; braids must be actively negated.
- **The animal must not become a wyvern in silhouette.** New this batch and the cause of three rejections.

**Render/QC status:** **2 of 10 approved · 3 rejected for rerender · 5 not yet generated.** Generation cap (10/turn) reached.

| Frame | Status | Note |
| :--- | :--- | :--- |
| `IMG0361` | ✅ Approved | **Pass 2.** Pastoral homestead on a cold overcast morning: three circular dry-stacked basalt huts with conical slate roofs and rafter ends showing at the eaves, a large wattle hurdle fold full of long-woolled sheep, two shepherds in undyed wool and sheepskin seen from behind with loose pale hair, a steaming mineral stream cutting through open emerald meadow, heavy grey mist, a smoking cone beyond. Pass 1 had been a European postcard: gabled cottages, chimneys, dry-stone boundary walls, a field grid and a golden sunset. Reframed rows 12–755. |
| `IMG0362` | ❌ Rerender | Over-the-shoulder out of the valley. The *shot* now works — the back of the head with loose silver-white hair, no braids, correct clothing, valley and flock beyond. But the distant animal is a **wyvern**: tiny narrow body, whip tail, huge thin bat wings and a headless silhouette with dangling clawed legs. |
| `IMG0363` | ❌ Rerender | Wide panic shot. Sheep scattering and the two running shepherds are right, but the flying animal is again a **wyvern** with whip tail and hanging clawed legs, plus one shepherd in dark navy and one honey-blonde. |
| `IMG0364` | ❌ Rerender | UWA vista. The settlement is now correct — round huts, conical roofs, wattle folds, no walls or field grid — but the animal overhead has a **barbed, spiked tail tip and a dangling clawed leg**, and its head is invisible. |
| `IMG0365` | ✅ Approved | **Pass 1.** Wing membrane close-up: one smooth taut dark sheet between three long straight rib-spars, beaded with condensation, ragged torn trailing margin at lower left, and a healed semicircular scar reading as a pale seam near the top right. No head, no body, no face. Reframed rows 12–755. |
| `IMG0366` | ⏳ Queued | MS 35mm — lateral tracking of the flock scattering. |
| `IMG0367` | ⏳ Queued | MCU 65mm — the animal at low level over the valley. |
| `IMG0368` | ⏳ Queued | MS 50mm — shepherds driving the flock, eyes up. |
| `IMG0369` | ⏳ Queued | WS 35mm — scorched wool, blackened stone, smoking crater. |
| `IMG0370` | ⏳ Queued | UWA 24mm — high geographic reveal of the raided valley. |

**Rerender brief (applies to `0362`, `0363`, `0364`):**

1. **The animal is a heavy iron-armoured beast, not a wyvern.** Every flying frame in the batch came back with a tiny narrow body, whip tail, oversized thin bat wings, dangling clawed legs and a headless blob. The problem was writing "no head detail" — the model deleted the head. Rewrite positively and at the silhouette level: **"an enormous deep barrel chest, a thick short ringed neck, a heavy blunt wedge-shaped head with a broad flat crocodilian snout and two swept-back horns clearly present in the silhouette, two wings thick at the shoulder tapering to ragged tips, wing-arms folded tight against the body, a long thick tapering tail."** Negatives: "no wyvern, no pterosaur, no tiny narrow body, no whip-thin tail, no headless shape, no featureless blob, no dangling clawed legs."
2. **`0363` also needs its people corrected:** "no blonde hair, no braids, no plaits, no dark navy or black clothing on the people" — one shepherd came back honey-blonde and one in navy.

**Lessons from this batch to carry into 038:**

1. **A location carried only in the bible will drift unless its form is written into every prompt.** Pass 1 produced a European pastoral postcard — gables, chimneys, boundary walls, a field grid, a golden sunset — because "terraced meadows and basalt dwellings" was too loose. The three words that fixed it were **round, conical, unenclosed**.
2. **Negating a feature deletes it here, it does not hide it.** "No head detail" removed the head; "no ribs" in an earlier batch removed the ribs *and* the structure they belonged to. Positive silhouette descriptions are the only reliable control at distance.
3. **The animal has a shape signature that must survive scaling.** Barrel chest, thick short neck, blunt wedge skull, folded wing-arms, thick tapering tail. Without those five descriptors it degrades into a generic wyvern.
4. **Silhouette is now the primary QC axis across both locations.** In the caldera it failed as a biped and as a feathered fan; outdoors it fails as a wyvern. The common cause is the same: too little positive description of the mass.
5. **The membrane close-up remains the safest frame in the episode** — `0365` passed first time, as every membrane macro has, and it is also the frame that carries the bible's healed tear-scar most clearly.
