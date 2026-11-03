# The 2WULFFS Method — our operating standard

Distilled from **"AI through the eyes of an art director"** (2WULFFS, 2026, 102 pp). This is not a
summary for reading — it is the checklist I direct every shot with. When I hand you a package, it
should be visibly built on these rails.

---

## 0. The hierarchy of value

> **Strong ideas first, AI second.** The tool was never the idea. A beautiful image is not
> automatically interesting, and technically perfect is not culturally relevant.

Order of decisions, non-negotiable: **Insight → Idea → Visual rule → Execution → Prompt.**
A prompt is the last thing we write, never the first.

**The dragon test:** if you remove the spectacle and nothing is left, there was no idea. A surprising
image is not a strong idea.

**Consistency beats spectacle:** one great frame is an image; twenty connected frames are a world.

---

## 1. Before we touch the prompt (the decision grid)

Ten fields decided *before* generating. If these are vague, the model decides for us — and it has
terrible taste.

| Field | The question |
|---|---|
| **Subject** | Who/what are we looking at — cast, age, build, what must stay consistent |
| **Wardrobe / object** | Materials, silhouette, wear, branding level |
| **Action** | Exactly what happens. One readable action per shot |
| **Location** | Architecture, materials, scale, weather, era |
| **Time** | Period, season, time of day |
| **Light** | Source, hardness, direction, colour, practicals. One lighting logic for the whole film |
| **Camera** | Shot size, angle, lens, support, movement, observer vs participant |
| **Mood** | The emotional temperature, in 3–5 words |
| **Texture** | Grain, halation, skin, fabric, haze, imperfections |
| **Style** | What shelf does this sit on? Reference-era, not adjectives |

Plus two that outrank the rest: **What are the rules?** (what must never change) and **How does it
move?** (pace of character, camera, environment, edit).

---

## 2. The world rules sheet (creative bible)

Every project gets an **ALWAYS / NEVER** pair, written before generating. Knowing what you *don't*
want is art direction. Never list ~6 items; always list ~6.

```
Our world is: <5 adjectives, e.g. Raw / Intimate / Cold / Human / Lived-in>

ALWAYS                      NEVER
natural skin                perfect studio skin
available light             glossy fashion lighting
muted cold tones            loud colours
real locations              perfect AI compositions
relaxed tailoring           over-styled wardrobe
human imperfections         exaggerated expressions
```

**Restrictions create identity.** The rules apply to prompts, to casting, to the grade, to the edit.

---

## 3. References: show, don't describe

* Fewer, stronger references. **Ten images you understand** beat 200 you can't explain.
* Know what each reference is *for*: framing from one, light from another, attitude from a third,
  texture from somewhere else.
* Use `@IMAGE1`-style binding in prompts: *"character and wardrobe from @Image1, inside @Image2, lit
  and graded like @Image3."* Words explain it, references show it.
* Always attach a **location reference** — the environment carries most of the visual identity.
* No technical vocabulary? Upload the frame and ask what the angle/lens/light actually is.

---

## 4. Realness lives in what AI cleans up

Add imperfection deliberately:

`slightly awkward framing · messy flyaway hair · imperfect skin texture (visible pores, tiny
blemishes) · uneven lighting, one side under-exposed · wrinkled clothing · slightly missed focus ·
partially obstructed view · cluttered background · imperfect film scan · natural motion blur`

Explicitly ban the tell-tales: `no beauty retouching, no HDR, no glossy digital sharpness, no
oversaturation, no perfect AI composition`.

**Casting is art direction.** A perfect face is not a good cast — a distinctive, believable one is.

---

## 5. Lock the world, lock the cast, then shoot

1. **Lock the world** — generate a clean location still (2K+). Architecture, time, light, texture.
2. **Lock the character** — a reference sheet, not a pretty picture: full-body front, full-body back,
   face close-up, neutral standing pose, consistent wardrobe/hair/proportions, plain background,
   even light. Its job is evidence for the video model.
3. **Lock the product/object** the same way when it matters.
4. **Lock the base look** — one paragraph of look-language appended to *every* prompt on the project.
   The base stays the same; only the shot changes.

### Base-look discipline

> Once the foundation is set, stop reinventing the look with every prompt. Different coverage, one
> film.

---

## 6. Prompt architecture

### Images (and any still frame)

Decision grid first, then prose. Uppercase isn't magic; **specificity** is.

### Video — the eight-part spine

```
SUBJECT + WARDROBE + ACTION + ENVIRONMENT + CAMERA + LIGHTING + STYLE + DETAILS + MOOD
```

Written as one dense block, in that order, with continuity clauses ("continues walking for the
entire shot, never stopping or posing") and explicit references ("matching @IMAGE1").

**Long prompts are fine. Unread prompts are not.** Read the whole thing before pressing generate:
action, camera, continuity, timing, look. Cheapest place to catch a mistake.

### Depth of direction

One idea, many shots. Never tell the whole story in one generation. Break to beats
(`world → human → trigger → reaction → escalation → realization → payoff → hero`) and generate shot
by shot.

---

## 7. The iteration protocol

* **90/10.** 90 % is in our hands (direction, references, prompt, choice). The last 10 % is luck.
* **80 % there? Don't restart.** Edit the image / change one clause in the prompt.
* **Change one thing at a time**, or you won't know what fixed it.
* Diagnose before regenerating:
  character wrong → reference sheet · location wrong → location ref · action wrong → simplify and
  make it explicit · camera wrong → state size, angle, movement · looks too "AI" → simplify, ask for
  natural movement, physics, imperfections · too much happening → split the shot.
* **Test cheap, finish expensive.** Low resolution for blocking, high resolution only for keepers.
* **The first generation is almost never the work.**

---

## 8. Curation is the job

> Generating gives you options. Art direction is deciding which one deserves to survive.
> **Don't pick the prettiest shot. Pick the right shot.**

Kill list: beautiful-but-generic · impressive-but-too-much · perfect-but-no-feeling.
Keeper test: does it serve the idea, feel real, belong to the world, add something?

---

## 9. Coverage thinking (not shot-by-shot chronology)

Generate **categories**, not a storyboard, then build the film in the edit:

stillness · action · character close-up · object close-up · product · interaction · wide
establishing · medium connective · detail/texture · transition · hero · anchor.

Within each category the shot prompt only changes the shot — the base look, cast refs and world rules
stay fixed.

---

## 10. Sound decision (made before generating, not after)

* **Full sound** — fast concepts, ready-to-use, but baked together and hard to re-cut.
* **SFX + ambience only** — our default: footsteps, breath, fabric, doors, room tone, wind. Cutable.
* **No sound** — visual-only, full post control.

Natural SFX make AI footage feel physical; one good footstep can beat another hour of generating.

---

## 11. Edit rules that reliably save AI footage

`cut before it breaks` (get out at frame 60 if it falls apart at 90) · `find the best 12 frames of a
bad clip` · `cut on movement` to join unrelated generations · `speed ramps` for energy · `reframe the
generation` — crop, reposition, push in; compositions aren't sacred · `sound to make it real` ·
`silence as an effect` · `fake continuity` via screen direction, framing, energy · `grade everything
back into one world`.

Cut on energy, not the beat. Let shots breathe. Contrast drives dynamics (wide→close, still→moving,
quiet→loud). Never use a shot because it was hard to make.

---

## 12. Tool philosophy

* Master adapting to tools, not one tool. Each model has a personality; choose for the job, not hype.
* The fastest fix is often **not another prompt** — it's Photoshop, After Effects, the edit, or cutting
  around the problem.
* Everything changes constantly. Taste and direction are the durable assets.

---

## What I owe you on every deliverable

1. The idea in one sentence, and the contrast it's built on.
2. The world rules (ALWAYS / NEVER) and the locked base look.
3. Reference/cast sheet before shots.
4. Shot list by coverage bucket, each with the eight-part prompt and @IMAGE bindings.
5. The honest cut list: which takes to keep, which frames to cut before, what to fix outside AI.
6. Previz/an animatic so we argue about the film, not about renders.

If a package I hand you doesn't have 1–6, it isn't finished — no matter how good the stills look.
