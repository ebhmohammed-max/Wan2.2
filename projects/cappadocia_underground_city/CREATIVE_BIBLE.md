# Creative bible — "THE CITY THAT DIDN'T WANT TO BE FOUND"

Cappadocia underground city · vertical 9:16 · Wan2.2 · built to the 2WULFFS method
(`studio/2wulffs-playbook.md`). Idea first, AI second.

---

## 1. Insight → Idea → Visual rule → Execution

**INSIGHT.** The underground cities of Cappadocia (Derinkuyu, Kaymaklı) were not palaces or tombs.
They were **refuge cities**: thousands of people, livestock, granaries, wine presses, churches, dug
eight levels down, with rolling stone doors and ventilation shafts. Their entire genius is that they
were built to be *invisible from above* — the deeper you go, the harder you are to find.

**IDEA — one sentence.**
> *A single lamp reveals a city that was built never to be seen.*

**CONTRAST (the engine of the film).**

| | |
|---|---|
| one small flame | × architecture built for thousands |
| human silence | × the memory of a city full of noise |
| the explorer's curiosity | × the inhabitants' need to hide |
| warm living light | × cold dead stone |
| a 5 cm chassis of rock overhead | × an entire world underneath |

**VISUAL RULE — the one rule everything obeys.**
> **The lamp is the cinematographer.** Nothing exists on screen outside the lamp's reach; the light
> radius defines the edge of the world. The camera only ever travels **deeper**. Deeper = older
> carving, colder stone, thinner light.

**EXECUTION.** A four-shot micro-film, no narration, sound-led. It ends on the stairs that go further
down than we can see — the film withholds the bottom of the city.

---

## 2. World rules (creative bible)

**Our world is:** Silent / Ancient / Lamp-lit / Physical / Withholding

| ALWAYS | NEVER |
|---|---|
| warm lamp as the only key light | daylight, floodlights, "cinematic" blue moonlight |
| real volcanic tuff texture — chisel marks, soot, dust | clean, smooth, new-looking stone |
| deep crushed blacks, 1 stop under | HDR, lifted shadows, visible detail everywhere |
| imperfect handheld-ish camera, late reframes | perfect gimbal symmetry, hero compositions |
| human scale for contrast (a person, a lamp, a hand) | architecture porn with no point of view |
| sound: breath, steps, dripping, air | music stings, whooshes, riser SFX |
| ochre / umber / charred grey | teal-and-orange, neon, saturated colour |
| symmetrical, hand-carved arches that repeat into dark | melted, warped, CGI-looking geometry |

**Banned objects:** modern anything — cables, electric light, signage, zips, synthetic fabric,
watches, plastic.

---

## 3. Locked base look

`BASE_LOOK.txt` is appended to **every** prompt in this project. The base stays the same; only the
shot changes. Do not re-invent the look per shot — that is what makes twenty frames feel like twenty
different films.

---

## 4. Cast & world references (generated before any shot)

| Asset | File | Purpose |
|---|---|---|
| World plate — tunnel | `keyframes/kf01_tunnel.png` | the approach, the doorway, the dust shaft |
| World plate — chamber | `keyframes/kf02_chamber_reveal.png` | scale, columns, stairs down |
| World plate — deep hall | `keyframes/kf03_deep_hall.png` | the deepest level, steps into black |
| Cast — explorer | `shot02_explorer/keyframes/kf00_character_sheet.png` | front / back / face / neutral pose, wardrobe locked |
| Cast in world | `shot02_explorer/keyframes/kf01_walk.png` | identity + lighting reference for every shot 02+ take |

Prompt binding convention (mirrors the `@IMAGE` system in the guide, mapped to Wan2.2 CLI flags):

```
@WORLD   -> --image keyframes/kf02_chamber_reveal.png   (location + light + grade)
@CAST    -> --image shot02_explorer/keyframes/kf01_walk.png (identity, wardrobe, lamp)
@SHEET   -> shot02_explorer/keyframes/kf00_character_sheet.png (consistency evidence)
```

Wan2.2 takes one conditioning image per run, so a shot that needs both cast **and** world starts from
the cast plate and carries the world in text + base look; the world plate is used for the empty-beat
generations. (In a reference-first model like Seedance/Higgsfield this is one `@Image1/@Image2`
prompt — the shot cards below are written so they translate either way.)

---

## 5. Coverage plan — 8 buckets, not a storyboard

Generate categories, assemble in the edit. **Bold** = already built in this repo.

| # | Beat | Bucket | Shot | Length | Status |
|---|---|---|---|---|---|
| 01 | WORLD | wide establishing | empty tunnel, dolly forward, doorway glowing, dust in a single shaft of lamp light | 5 s | **built** (`shot 01`) |
| 02 | HUMAN | medium tracking | explorer walks toward backwards-tracking camera, lamp swinging, hand on wall | 5 s | **built** (`shot 02`) |
| 03 | TRIGGER | detail / texture | a hand + lamp raking across a hand-carved wall symbol; soot-blackened incision | 5 s | to generate |
| 04 | REACTION | character close-up | his face as the carving resolves in the lamp light; breath visible, no expression played | 5 s | to generate |
| 05 | ESCALATION | wide, deeper | second chamber, visibly older carving, fewer lamps, colder stone, figure tiny | 5 s | to generate |
| 06 | REALIZATION | detail + insert | the ventilation shaft: a thin column of dust moving in dead-still air; rolling stone door edge | 5 s | to generate |
| 07 | PAYOFF | anchor / wide | he stands at the top of the stairs, lamp the only light, steps disappearing into black | 5 s | to generate |
| 08 | HERO | held wide, no motion | the same chamber, empty, one guttering lamp, film ends before the bottom of the city | 5 s | to generate |

Shot cards with eight-part prompts for 03–08: `COVERAGE_SHOTS.md`.

---

## 6. Sound (decided before generating)

**SFX + ambience only. No music, no dialogue, no narration.**

| Layer | Content |
|---|---|
| bed | low underground room tone, faint moving air through the ventilation shaft |
| body | boots on dust and stone, fabric, a hand dragging on rock, breath |
| props | brass lantern handle creak, flame flutter, small metal jingle |
| punctuation | one distant rockfall; a single water drip used as a rhythm (never twice in a row) |
| silence | full drop-out for 0.5 s before shot 07 — the loudest moment in the film |

Music, if ever added: one sustained bowed note, entering only at shot 07. Never a riser.

---

## 7. Edit & grade

* **Cut before it breaks.** A Wan2.2 take drifts after ~70 frames → keep 60–90 of 121; hands and
  faces decay first.
* **Cut on movement** — a footfall, the lamp swing, a hand leaving the wall — to join separate
  generations.
* **Reframe freely.** 9:16 crop out of a 704×1280 take gives us a free push-in and a tighter shot.
* **Fake continuity** with screen direction and lamp position: the lamp always sits frame-right until
  shot 07, where it crosses to frame-left as he turns down the stairs.
* **Grade all takes back into one world:** −1 stop exposure, crushed blacks, ochre/umber balance,
  halation on the flame, one grain plate over the whole film.

---

## 8. What v1 of this package got wrong (audit against the guide)

| v1 | Problem | v2 |
|---|---|---|
| "photorealistic, ultra-detailed, 4K, cinematic" | asks for exactly the AI perfection the guide says to fight | base look now asks for grain, halation, imperfect exposure, no HDR |
| prompts began with adjectives | no decisions behind them; the model decided the taste | decision grid + eight-part spine, decisions written down first |
| no idea, no rules | pretty footage with nothing underneath | insight → idea → visual rule, ALWAYS/NEVER sheet |
| no cast sheet | identity held by luck across seeds | character sheet + `@CAST` plate, identity is evidence not description |
| two shots, no coverage plan | nothing to cut together | 8-bucket coverage plan, film ends withholding the bottom of the city |
| no sound plan | visual-only, would feel like a screensaver | SFX-only design with a silence beat |
| "documentary" used as a style word | style ≠ direction | documentary *logic*: observer camera, late reframes, one lamp |
