# Shot 02 — prompt v2 ("director's cut")

Rewritten to the 2WULFFS spine and the identity **evidence** model: the cast is no longer described,
it is referenced. `prompt_v2.txt` is the copy-paste block: body + `BASE_LOOK.txt` appended.

**Bindings**

| Token | File | Wan2.2 equivalent |
|---|---|---|
| `@CAST` | `keyframes/kf01_walk.png` | `--image` (I2V-A14B, or TI2V-5B with `--image`) |
| `@SHEET` | `keyframes/kf00_character_sheet.png` | the consistency evidence — front/back/face/neutral pose, used to judge takes, and as the reference image on any model that accepts several |

**Why v2 differs from v1**

| Spine part | v1 | v2 |
|---|---|---|
| Subject | narrative description of the man | **`@CAST` binding first**, physical description second — identity is proven, not re-invented per seed |
| Wardrobe | "rough brown linen clothing" | tunic with frayed hem, rope belt, faded dark red sash, satchel: the same six objects as the sheet, so drift is measurable |
| Action | "walks naturally toward camera, several realistic steps" | **three unhurried steps, heel-to-toe, and he never stops or poses** — a countable action plus a continuity clause |
| Environment | "mysterious underground stone tunnel" | the tunnel *is* the city's entrance: sooted arched doorway behind him falling into black |
| Camera | "camera smoothly tracks backward" | in front of him, at his walking speed, 50mm, medium full-body, human-operated, slightly late reframe, no cut/no zoom |
| Lighting | "warm flickering light across his face" | lamp is the **only** key, swings on its handle, rest of frame stays in shadow |
| Style | "cinematic documentary, photorealistic" | base look: 35mm, grain, halation, 1 stop under, no HDR |
| Details | "anatomically correct hands" | hands + one steady unblinking identity clause + fabric weave, dust on boots, pores and stubble |
| Mood | "realistic documentary atmosphere" | *a man walking into a city that was built to stay hidden* — the film's idea, in the shot |

**Route.** I2V-A14B from `@CAST`, 720×1280, 81f @ 16fps. Sweep 4 seeds, judge on hands → face stability
→ foot contact → lamp light movement → backward track (that order, that priority).

**Kill criteria.** Fused fingers on the lamp hand · face morph after ~frame 60 · sliding feet · lamp that
stops flickering · tunnel mouth that drifts forward with him.
