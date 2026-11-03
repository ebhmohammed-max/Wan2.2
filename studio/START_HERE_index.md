# WAN 2.2 — Cappadocia Underground City

One film, vertical 9:16, directed to the 2WULFFS method. Everything I make lives in this folder.

---

## The film

**Idea (one sentence):** *a single lamp reveals a city that was built never to be seen.*

Cappadocia's underground cities were refuge cities — thousands of people, eight levels down, with
rolling stone doors and ventilation shafts, built to be **invisible from above**. That insight drives
every creative decision: the lamp is the only light source, the light radius is the edge of the world,
and the camera only ever travels deeper.

**Contrast engine:** one small flame × architecture for thousands · human silence × the memory of a
city full of noise · curiosity × the need to hide · warm life × cold stone.

**Visual rule:** the lamp is the cinematographer. Nothing exists outside its reach.

---

## Where everything is

| Folder | What's inside | Status |
|---|---|---|
| `00 — Creative Direction (2WULFFS method)` | the method as our operating standard, the creative bible (insight → idea → visual rule → execution), the locked base look, the 8-bucket coverage plan, and the director's-cut prompts (v2) | done |
| `Cappadocia Underground City / Shot 01 — The City Below` | empty tunnel dollies into the lamp-lit chamber; 3 world keyframes, 16 s previz, all generation + delivery scripts, prompt v2 | built |
| `Cappadocia Underground City / Shot 02 — The Lantern` | the explorer walks toward a backwards-tracking camera; cast evidence sheet, 4 identity-locked keyframes, 5.2 s walking previz, I2V/TI2V/Animate routes, prompt v2 | built |
| `Cappadocia Underground City / Takes & Finals` | final graded 1080×1920 masters and the assembled cut | waiting on GPU renders |

Source of truth for code and scripts: the repository branch `arena/434d1f27-wan2-2`
(pull request #1 on `ebhmohammed-max/Wan2.2`).

---

## The 8-beat structure

`01 world → 02 human → 03 trigger → 04 reaction → 05 escalation → 06 realization → 07 payoff → 08 hero`

Shots 01–02 are built. Shots 03–08 have written shot cards (eight-part prompts + what to check on each
take) in the creative direction folder — they need a GPU to render.

| # | Beat | Bucket | Status |
|---|---|---|---|
| 01 | WORLD | wide establishing | built |
| 02 | HUMAN | medium tracking | built |
| 03 | TRIGGER | detail / texture | card ready |
| 04 | REACTION | character close-up | card ready |
| 05 | ESCALATION | wide, deeper | card ready |
| 06 | REALIZATION | detail + insert | card ready |
| 07 | PAYOFF | anchor / wide | card ready |
| 08 | HERO | held wide, no motion | card ready |

Estimated assembled length: **≈ 37 seconds.**

---

## Production rules I work to

* Idea before AI. The prompt is the last thing written, never the first.
* One locked base look appended to every prompt — the base stays the same, only the shot changes.
* ALWAYS: warm lamp as the only key, real tuff texture, deep crushed blacks, imperfect handheld
  framing, human scale. NEVER: daylight, HDR, teal-and-orange, smooth new stone, modern objects.
* Identity is evidence, not description — the cast sheet and `@CAST` plate, not adjectives.
* Generate coverage buckets, not chronology. Cut in the edit.
* Cut before it breaks: Wan2.2 takes drift after ~70 frames; keep 60–90 of 121.
* Sound is decided before generating: SFX + ambience only, no music; one deliberate silence before
  the payoff.
* Curation: don't pick the prettiest shot, pick the right shot.

---

## Notes

* Renders are 704×1280 (5B) or 720×1280 (14B); delivery chains crop and grade to exact 1080×1920 9:16.
* Previz MP4s in the shot folders are animatics, not model output — approval tools, not deliverables.
* The reference PDF this was directed from is not stored in the shared folders.
