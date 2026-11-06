# ATLAS UNDERSTORY · VIDEO 01 — HYPERFRAMES FINISHING BIBLE
### The complete build instruction for the HyperFrames agent
Version 1.0 · 6 November 2026 · for HyperFrames 0.9.2 or later

---

## 0. HOW TO USE THIS DOCUMENT

**You are the finishing agent on a locked film.** The picture is cut, the narration is recorded, the music is mixed.
Nothing about the edit is yours to change. Everything about the *surface* of this film — its titles, chapter system,
evidence panels, diagrams, map, captions, disclosures, transitions, texture, and end card — is yours to design and
build to the standard set out below.

Read this document in full before you open the project. It is long because every decision you would otherwise have
to guess at is already made here, and because a documentary about evidence has to be more careful than a product
film. If you skip to the commands in Part 12 you will produce something that renders and is wrong.

**Authority order — when two instructions conflict, the higher one wins:**

1. This document (the founder's current instruction).
2. The v4 handoff package — `02_Full_Script_Clean_v4_HANDOFF` and `10_Image_Budget_and_Shot_Map_v4_HANDOFF`
   (especially its **Graphic Specifications** sheet), for the *text content* of each graphic slot.
3. `11_Style_and_Continuity_Bible_v4`, for disclosure language and evidence boundaries.
4. Your own judgement, last, and only where this document is silent.

**The one-line version:** build a calm, exact, archive-dossier finish for a 10:56 documentary — 46 evidence panels,
3 structural diagrams, 1 schematic locator map, 3 archive-photo panels, a five-chapter system, one burn-in caption
track, one end card that states the film's limit honestly — and do it without moving a single frame of the picture.

**What "pinnacle" means here.** Not more effects. In a film whose whole argument is *"the image does not prove the
job"*, the finish must practise what the narration preaches: restraint, legibility, attribution, and nothing invented.
The audience should feel a scholar's desk, not a title-sequence showreel. Every flourish that cannot survive the
question *"what does this claim?"* is deleted.

---

## 1. THE FILM

**Title:** *The Lighthouse Ring Found in Alexandria's Sunken Palace*
**Series:** Atlas Understory · Episode 01
**Runtime:** 10:56:01 — 15,745 frames at 24 fps — 656.042 seconds exactly.
**Spoken:** 1,427 words in 48 VO segments across five chapters; voice from 1.200 s to 639.330 s.
**Music:** "Ambiment" by Kevin MacLeod (incompetech.com), CC BY 4.0 — credit is a legal obligation, not a courtesy.

### 1.1 What the film argues

A bronze ring-signet, reported from the submerged royal quarter of Alexandria, is said to carry a lighthouse image,
and the excavation team proposes it points to a lighthouse-related administrator. The film tests that proposal and
finds it *possible but unproven*. It separates four things that are routinely conflated:

- **A picture is not a job.** Recognising the Pharos tells you the subject of an image, not the occupation of the hand
  that wore it.
- **A findspot is not a function.** A palace setting can support an administrative reading; it does not establish it.
- **An association is not a manufacture date.** Pottery of the second century AD beside the ring dates the context,
  and the report itself allows the ring to be earlier.
- **Context is the evidence.** What a survey becomes, and what is lost when a site goes unrecorded, is the film's
  real subject.

The closing line is the film's spine: *"We can recognize the tower. We still cannot name the hand."*

**Your finish must never resolve that open thread.** No graphic may imply an owner, an office, a name, a percentage
of certainty, or a reconstruction of the object. The film's honesty *is* the production value.

### 1.2 The structure you are finishing — read this twice

The narration runs straight through five chapters. **The picture does not.** The frozen shot map braids all five
chapters together, one beat at a time:

- The 98 shots alternate strictly: **odd beat numbers are graphic panels, even beat numbers are photographic plates.**
  The map states it as a rule: *"No consecutive plate run exceeds one shot."*
- Within each beat, the five chapters rotate in order C01 → C02 → C03 → C04 → C05.
- So the film plays: five evidence panels (one per chapter), then five living plates (one per chapter), then five
  panels, and so on — 22 beats of ~31 seconds: **eleven panel racks, ten plate racks, and a single-shot tail**.

**Why this matters to you, in one sentence:** a panel on screen at 08:53 belongs to Chapter 5's beat, but the
narration playing at 08:53 is still finishing Chapter 4. **No panel can rely on the narration that happens to be
playing.** Panels must be self-sufficient evidence cards, readable cold, with their own source line. Never write
"as you can hear", never use a pronoun that depends on the surrounding VO, never assume the viewer just heard the
segment that panel was authored for.

Two consequences you must design for:

1. **A persistent chapter rail** (Part 5.2) tells the viewer which chapter the *argument* is in, even while the imagery
   rotates. This is the single most important thing you add to the film.
2. **Every panel is a closed exhibit**: header, content, source, done. It should survive being paused, screenshotted,
   and read in a museum. That is the design target.

### 1.3 The five chapters, with estimated narration onsets

Exact onsets come from your alignment pass (Part 7). These estimates are proportional to word count and are within a
few seconds; use them only to plan the build, never to place a chapter card.

| # | Title (from the script) | First segment | Est. onset | Words |
|---|---|---|---|---|
| I | A Tower on a Ring | VO-C01-B01 | 00:00:01:05 (1.20 s) | 258 |
| II | A Picture Is Not a Job | VO-C02-B01 | ≈ 00:01:56:19 | 319 |
| III | The Palace and the Alternative | VO-C03-B01 | ≈ 00:04:19:16 | 295 |
| IV | The Date Beside the Ring | VO-C04-B01 | ≈ 00:06:31:18 | 277 |
| V | What the Evidence Supports | VO-C05-B01 | ≈ 00:08:35:16 | 277 |

Chapter headings and VO IDs are **never spoken and never on screen as read-aloud text**. The chapter *titles* may
appear on chapter cards, exactly as written above.

---

## 2. THE ASSETS — EVERYTHING YOU NEED, AND WHERE IT IS

All Drive ids below are live. Verify each with a metadata read before you build; if an id fails, stop and report it
rather than substituting something similar.

### 2.1 The picture and the sound — the two files you actually edit

| What | Name | Drive id | Facts |
|---|---|---|---|
| **THE MASTER** | `01_v3 COMPLETE 10m56:01 — narration + music.mp4` | `1DHxtoMn6HBBXwFHUNc9iW_wIVrs3e4OQ` | 1920×1080 · 24 fps CFR · **15,745 frames = 00:10:56:01** · H.264 High ~1057 kb/s · AAC-LC 48 kHz stereo, **−16.0 LUFS**, true peak −1.9 dBFS · 96.6 MB · `+faststart` |
| Narration stem (no music) | `Atlas Understory 01 — narration stem (no music) 10m56.mp3` | `1wSMI8sqQl7YEpQqtxIvNO_cOoZx4ICFy` | 192 kb/s mp3 · 00:10:56.04 · **use this for transcription and caption sync**, not the mixed master |
| Un-narrated picture (for clean plate diffing) | `00_v2 COMPLETE 10m56:01 — continuous plate cut (VO + edit bed).mp4` | `1GHn7S9-XsOrY57hEJkSdko_Xhjo1GkJD` | 15,745 frames · no audio · 86.9 MB |

**Rule: the master is the picture and the sound. You add layers on top of it and you hand it back unchanged
underneath.** If your compositor forces a re-encode, the re-encode must be visually lossless (ProRes 422 HQ or
better) and the audio must be decoded to PCM without any gain change.

### 2.2 The content authority

| What | Name | Id | Use |
|---|---|---|---|
| The spoken script (verbatim) | `02_Full_Script_Clean_v4_HANDOFF` | `14k_ODWncBuLTn0AE5c6LydA-EHxzCteMfxf-uCp3EXg` | Caption wording, on-screen citations, chapter titles |
| **The shot map workbook** | `10_Image_Budget_and_Shot_Map_v4_HANDOFF` | `1wKuxtjWPIHIBzOc0O8Ph0Sw7RBhM_B4YO7UJ7rPgFZ4` | **The `Graphic Specifications` sheet is the text of your 46 panels; `VO Sync` ties script to time; `Style and Rules` governs labels; `Source Register` holds attributions** |
| The cue sheet (98 rows) | `04 — Cue sheet 10:56:01` | `1ypJuaO_3NF9AuUCZXp546aAnuK11LRA932cUqmk8w0I` | Every shot's in/out timecode, duration, frames, type, MG/VX id |
| Style & continuity bible | `11_Style_and_Continuity_Bible_v4` | `1oRXXLsD0Pj9_gmHxaQ9gwBkk5-H1ykYC3oxhLcrD7Ts` | Disclosure wording, evidence boundaries |
| Met bulla insert note | `C02-S005-A_insert_caption.md` | in `1eiaDRCMHh7GmaTdv704CT-0BgU1KTMTk` | The accession correction you must apply (Part 3.3) |

### 2.3 The picture assets, if you need to rebuild anything

49 plate clips at **CRF 17, 1080p24** — better than anything inside the 1.06 Mbps master. If a shot must be
re-cut or a reveal needs a cleaner source, take the clip, not the master:

| Folder | Id |
|---|---|
| v2 — Cinematic Rebuild (root, holds the bed + `Audio (voiceover + music)`) | `1XEjoQvvZseZvwcntun68cwoRZiXoZwjf` |
| v2 · Batch 0 — six anchors | `1osH2leZ3CUwDHF7JuRUkFPPZm-rMMTkR` |
| v2 · Batch 1 — Chapter 1 edits | `1TCzB7TR3fKWlIgjYXloAEhZRtIILMkvd` |
| v2 · Batch 2 — Chapter 2 edits | `1EEVfP9PKfhp8gN6t9DfPOR78uQFLoPLT` |
| v2 · Batch 3 — Chapter 3 edits | `1lcDfuDonyaJgrzYUmb2RgCOdABFJWmWy` |
| v2 · Batch 4 — Chapter 4 plates | `1jrZ9NsQC5NyJHCMbKe8BB3NrZTAG90Ui` |
| v2 · Batch 5 — Chapter 5 plates | `1CRsdh46fqx3lQI7mAM_a7DMeEdC0LVak` |
| v2 · INSERT — C02-S005-A sourced Met bulla (photo + untouched source) | `1eiaDRCMHh7GmaTdv704CT-0BgU1KTMTk` |
| Audio (voiceover + music) | `1A3l3Ajey8NWXvpazg2QpCHUssbgxq05T` |

### 2.4 Where you deliver

Video 01 root: **`1llRO_x9IFZMg2mDs6ikUCXitsHi_RTpK`** → folder `v2 — Cinematic Rebuild` (`1XEjoQvvZseZvwcntun68cwoRZiXoZwjf`).
Create a subfolder **`08 — Finishing (HyperFrames)`** and put everything in it. Do not add loose files to the root.
Do not modify, re-upload or trash the master, the plate clips, the docs or the audio.

### 2.5 The local support files that ship with this brief

| File | Contents |
|---|---|
| `SCRIPT_VERBATIM.md` | All 48 segments, character for character, with VO IDs |
| `OVERLAY_TIMELINE.csv` | All 98 slots: in/out TC, duration, frames, type, MG/VX, beat number, template, motion |
| `SEGMENT_TIMING_estimate.csv` | 48 estimated segment onsets (planning only) |
| `CHAPTER_TIMING_estimate.csv` | 5 estimated chapter onsets (planning only) |
| `PANEL_MOTIFS.md` | The twelve argument motifs each panel must anchor to |
| `TRANSITION_MAP.csv` | Every permitted transition event and its exact frame |
| `FACT_STRINGS.md` | The only on-screen factual strings you may set in type |
| `PRONUNCIATION_AND_SPELLING.md` | Spelling locks for captions and ASR repair |

---

## 3. ABSOLUTE PROHIBITIONS

These are not style preferences. Any of them appearing in a delivered frame is a delivery failure, and any of them
appearing in a *claim* is a legal and editorial failure.

### 3.1 Never depict, reconstruct, draw, model, trace or "reinterpret" any of these

1. **The ring**, its bezel, its engraved face, or any part of it.
2. **The lighthouse engraving** — not as line art, not as a silhouette, not as a "stylised icon", not as an SVG path,
   not as a shader, not as a particle assembly that resolves into it.
3. **The British Museum coin** — no obverse, no reverse, no Hadrian head, no Isis Pharia, no Pharos on a coin.
4. **The Met bulla** — no drawing, no model, no "impression diagram" that restages its moth design.
5. **A palace floor plan**, any architectural plan, axonometric, cutaway or section of the royal quarter.
6. **A findspot map**: no seabed plan, no survey grid, no bathymetric surface, no wreck outline, no site boundary,
   no dive track, no artifact scatter.
7. **A portrait of any person in the story** — no administrator, no merchant, no excavator, no scholar, no diver,
   no face at all. Hands are already in the plates; you add none.
8. **Any invented document**: no fake papyrus, no fake inscription, no fake catalogue card, no fake letter, no fake
   photograph of an excavation. If a panel needs a document, it is *set in type*, not staged as an object.

**What you may draw:** abstract, structural, non-representational diagrams — arrows, brackets, rails, timelines,
lanes, matrices, decision paths, labelled nodes, quantified *counting* that comes from the script — plus a regional
locator map from public-domain geodata. That is the entire visual vocabulary of the graphic layer. It is enough.

### 3.2 No legible pseudo-antiquity, anywhere, ever

No invented Greek, Latin, Demotic, hieroglyphic, Aramaic, Parthian or "ancient-looking" glyph strings. No decorative
lettering that reads as an inscription. No "engraved" text on a surface. No stamp-like motifs. Type in this film is
**modern editorial type only** — serif, grotesque, mono — and it always belongs to us, never to the object.

### 3.3 The accession flag — a correction you must apply, and must not hide

The script's handoff was written for Met object **1978.93.29**. The delivered photograph is object **1978.93.30**
(a neighbouring Parthian bulla; 5.51 × 7.8 cm; un-baked clay; Iran, Shahr-i Qumis / ancient Hecatompylos;
Purchase, H. Dunscombe Colt Gift, 1978; public domain).

- **On screen:** the caption block reads `Met 1978.93.30 | Bulla | Iran, Shahr-i Qumis | Not from Alexandria` and the
  credit line reads `The Metropolitan Museum of Art, 1978.93.30. Purchase, H. Dunscombe Colt Gift, 1978. Public domain.`
- **Never rewrite the narration or its wording.** Do not "fix" the script; the accession appears only in the panel.
- **Report it.** One line in `HF05_qa_report.md` and one row in `HF04_shot_report.csv` noting the delivered accession
  and that the scripted number was superseded — so the flag is visible to the founder, not buried.

### 3.4 Nothing you add may make a claim the film does not make

Permitted factual content is exactly: the verbatim script (App. A), the permitted fact strings (App. C), the object
metadata in Part 3.3, and the source names the script itself names. **No additional numbers, dates, dimensions,
percentages, comparisons, "probability" language, timelines, or attributions.** If a panel would be stronger with a
fact you do not have, it stays weaker. That is the rule.

### 3.5 Banned stylistic families (see App. D for the full registry blacklist)

Neon, glow, glitch/RGB-split, chromatic aberration as decoration, matrix/ASCII decode, hologram, liquid glass,
chrome/liquid metal, 3D extruded logos, app/device mockups, browser/terminal/code frames, chat and social cards,
confetti, emoji, particle bursts that resolve into text, kinetic "slam", slot-machine/flip-board numerals, carousels,
tickers, marquees, "count-up stats", progress rings, gauge arcs, "AI" motifs, logo stings and bumpers.

If a name in the registry sounds like it belongs to a product launch, it does not belong in this film.

---

## 4. THE DESIGN SYSTEM — LOCK THIS BEFORE YOU BUILD ONE PANEL

Every value below is a token. Build them once, as a single `system` composition plus CSS variables, and never
hard-code a colour, size or duration anywhere else. If you find yourself typing a hex value outside the token file,
stop.

### 4.1 Palette

The film's plates are amber/torchlight, navy/teal water, clay/ochre, and cold museum shadow. The graphic layer is
**ink, bone, ivory, with one warm accent and one cold accent** — it must feel like paper on a dark desk, never like a
UI. Nothing in the graphic layer may be pure black or pure white.

| Token | Hex | Use | Share of graphic pixels |
|---|---|---|---|
| `--ink` | `#0A0B0C` | Panel ground, scrims, end card | 55–70 % |
| `--slate` | `#14161A` | Raised panel, table band | 10–20 % |
| `--bone` | `#C9BFA9` | Secondary text, hairlines, rules | 8–12 % |
| `--ivory` | `#EFE7D6` | Primary text, display type | 6–10 % |
| `--amber` | `#C08A3E` | The one warm accent: numerals, active lane, key word | ≤ 3 % |
| `--teal` | `#2D6C6E` | Cold accent: "context / site / method" class tags | ≤ 2 % |
| `--rust` | `#8E3B2A` | Only for the disconfirming branch ("not established") | ≤ 1 % |

Rules: amber and teal never appear in the same element. Rust never appears without the word *not*, *cannot*,
*unproven* or *alternative* in the same group. No gradients on text. No colour-coded "good/bad" traffic lights.

### 4.2 Typography — three faces, all open-licence, all self-hosted

| Role | Face | Weights | Where |
|---|---|---|---|
| Display / titles / chapter numerals | **Spectral** (SIL OFL) | 300, 400 | Title card, chapter cards, end-card mark, panel headlines |
| Text / captions / body | **Inter Tight** (SIL OFL) | 400, 500 | Captions, panel body, source lines |
| Labels / data / accession | **IBM Plex Mono** (SIL OFL) | 400, 500 | Kickers, class tags, accession blocks, timecodes, credits |

**You must `@font-face` every face from local files.** The linter will fire `font_family_without_font_face` and
`system_font_will_alias` otherwise, and a system fallback silently changes every measurement in the film.

Type scale at 1920×1080 (locked):

| Token | Size / line-height | Tracking | Case |
|---|---|---|---|
| `--t-title` | 118 / 0.94 | −0.02 em | Uppercase, Spectral 300 |
| `--t-subtitle` | 34 / 1.30 | 0 | Sentence case, Inter Tight 400 |
| `--t-chapter-num` | 168 / 1.00 | −0.03 em | Roman numeral, Spectral 300, amber |
| `--t-chapter-name` | 46 / 1.15 | 0.01 em | Spectral 400, ivory |
| `--t-panel-head` | 44 / 1.12 | −0.01 em | Spectral 400, ivory |
| `--t-body` | 26 / 1.46 | 0.005 em | Inter Tight 400, bone |
| `--t-quote` | 38 / 1.34 | 0 | Spectral 300, ivory (only for verbatim quotes) |
| `--t-caption` | 34 / 1.32 | 0.005 em | Inter Tight 500, ivory 94 % |
| `--t-label` | 13 / 1.20 | 0.14 em | IBM Plex Mono 500, uppercase, bone |
| `--t-mono` | 20 / 1.30 | 0.02 em | IBM Plex Mono 400, ivory |

No condensed, no script, no handwritten, no outline, no gradient fill, no drop shadow on text **except** the caption
shadow in 4.6. Never let a headline exceed 3 lines. Never centre body copy.

### 4.3 Grid, margins, safe areas

- Canvas 1920 × 1080. 12 columns. Outer margin **104 px**. Gutter **24 px**. Column width **112 px**.
- Baseline grid **8 px**. Everything sits on it.
- **Title-safe: 96 px on all sides.** No type, no rule, no logo may cross it.
- **Caption-safe: 192 px on all sides.** Captions live inside it, and no panel content may occupy the bottom 192 px
  band while a caption is up.
- Panel composition: header rail on the top baseline (y = 216), body block from y = 288 to y = 792, footer rule at
  y = 872, footer text baselines at y = 900–936.
- The **chapter rail** (5.2) occupies x = 64–80 — that is outside the 104 px margin by design; it is furniture, not
  content.

### 4.4 Surface and texture — the only permitted "look" layer

Applied to the *graphic layer only*, never to the plate plates underneath (those are already graded):

| Layer | Setting | Notes |
|---|---|---|
| Paper fibre | 5 % opacity, 1:1 texel map, no scroll | Ties panels to a physical desk |
| Fine grain | 3.2 % at 1080p, animated at 24 fps, 2-frame cycle | Must be deterministic — no RNG per frame |
| Vignette | −7 %, 42 % radius, soft | Keeps eye centre |
| Hairlines | 1 px @ 100 % bone, 0.5 px @ 40 % | The film's only "decoration" |
| Scrim behind type over picture | ink at 22 % (chapter band) / 38 % (lower third) | Full-bleed, feathered 64 px |
| Chromatic aberration | **0** | Banned |
| Scanline / CRT | **0** | Banned |
| Bloom / glow | **0** | Banned |

Grain and fibre go on a top-most `--z texture` layer with `mix-blend-mode: overlay` so they unify panels, map, photo
and picture *after* compositing. One grain for the whole film, not one per element. Texture must not move relative to
the frame; it may only re-seed on a 2-frame cycle.

### 4.5 Motion grammar — one family, three durations, no exceptions

| Token | Duration | Easing | Used for |
|---|---|---|---|
| `--m-in` | 0.55 s | `power3.out` | Element entrance (rail wipe, header, body blocks) |
| `--m-hold` | — | `none` | Held panels drift at 1.5 % scale over the shot (see `Drift Hold`) |
| `--m-out` | 0.36 s | `power2.in` | Exit, always finishing 8 frames before the cut |
| `--m-draw` | 0.90 s | `power2.inOut` | Rules, underlines, arcs, connector paths |
| `--m-stagger` | 0.06 s | — | Between sibling lines/rows; max 8 siblings |

Hard rules:
- **Two moving elements at most** at any instant on the graphic layer.
- **No entrance in the first 6 frames of a shot** and **no exit in the last 6 frames** of a shot except the mandated
  8-frame exit before a cut. The cut must be clean.
- **No `elastic`, `bounce`, `back`, `rough`, `wiggle`, no infinite repeats, no random.** The linter bans
  `gsap_infinite_repeat` and `non_deterministic_code`; the film bans them for taste.
- **No CSS transitions or CSS animations.** HyperFrames lints `css_transition_used`; all motion is GSAP on the timeline
  so it is seekable and deterministic.
- **No transform on the container that holds the timeline clips** — plates must composite untouched.
- Motion blur: allowed only on the paper wipe, shutter 0.35, and it must be exported through HyperFrames' own
  `data-hf-motion-blur` mechanism, not a fake CSS filter.

### 4.6 The caption style (locked)

- Inter Tight 500, 34 px, line-height 1.32, colour `--ivory` at 94 %, `text-shadow: 0 2px 10px rgba(6,7,8,.72)`.
- Centred, max **2 lines**, max **42 characters per line**, widow control on (never leave one word alone).
- Baseline: block bottom sits at y = **936** (inside caption-safe).
- No box, no bar, no background plate, no karaoke highlight, no per-word animation, **no emoji**.
- Cue in on the first phoneme of the segment, cue out 6 frames after the last. Minimum on screen 24 frames.
- If a segment exceeds 2 lines at 42 characters, split it at a clause boundary into consecutive cues — never truncate,
  never paraphrase, never change a word (Part 7.3).

---

## 5. THE OVERLAY FAMILIES — EIGHT TEMPLATES, NOT NINETY-EIGHT DESIGNS

Everything you build is one of eight things. Build each as a reusable HyperFrames composition with variables, then
instance it. Ninety-eight bespoke layouts is how a film starts to look like a slide deck.

### 5.1 `TITLE` — the opening lockup (one instance)

Slot: **C01-S001, 00:00:00:00 → 00:00:06:05** (149 frames). This is a graphic slot; the panel text from the map
supplies the deck's opening statement, and the film's title lockup sits with it.

Layout:
```
y 300   THE LIGHTHOUSE RING                    --t-title, Spectral 300, ivory
y 430   Found in Alexandria's Sunken Palace     --t-subtitle, Inter Tight 400, bone
y 500   ───────────────  (rule 96 px, amber, --m-draw)
y 540   ATLAS UNDERSTORY · EPISODE 01           --t-label, Plex Mono, amber
```
- Title enters on a masked rise (16 px travel) + 0.9 opacity, 0.55 s, word-group stagger 0.06 s.
- Rule draws left→right in 0.9 s starting 0.18 s after the second line settles.
- Kicker fades up last, 0.36 s.
- Everything exits by frame 141 (5.875 s) so the cut at 149 is clean.
- **Do not** add a logo mark, a lens flare, a light sweep, a particle field or a "film-strip" motif.

### 5.2 `RAIL` — the persistent chapter rail (five instances, one continuous element)

The braid means the picture's chapter and the argument's chapter differ. The rail resolves it.

- A **1 px vertical hairline** at x = 72, from y = 216 to y = 864, `--bone` at 28 %.
- At its centre, the **current narration chapter numeral** (I–V), `--t-label` size ×1.4, ink box behind, amber.
- Below the numeral, the chapter title, rotated −90°, `--t-label`, bone 60 %, max 22 characters visible
  (use the short forms: `A TOWER ON A RING`, `A PICTURE IS NOT A JOB`, `THE PALACE AND THE ALTERNATIVE`,
  `THE DATE BESIDE THE RING`, `WHAT THE EVIDENCE SUPPORTS` — the long ones rotate fully; do not clip words).
- On each chapter change: numeral crossfades via a 12-frame y-shift (−8 px), old out / new in overlapping 6 frames.
  **The rail never moves horizontally and never scales.** It is the one still point in the film.
- The rail is present from 00:00:01:05 (first VO) to 00:10:39:08 (last VO) and fades out 12 frames before the end card.

### 5.3 `CHAPTER` — five chapter cards, 3.5 s each

Placed at the **exact VO onset of each chapter's first segment** (Ch. I is handled by the TITLE; so four cards:
II, III, IV, V — plus Ch. I's card is the title itself).

- Full-bleed **ink scrim at 22 %** rises over 10 frames, holds, falls over 10 frames.
- Numeral at y = 430 (Roman, `--t-chapter-num`, amber), title at y = 560 (`--t-chapter-name`, ivory),
  a 160 px hairline between them drawing in `--m-draw`.
- The card is over **live picture**, not black. Do not cut to black — the picture is continuous and must stay so.
- Entry 0.55 s, hold 2.1 s, exit 0.36 s, total 3.5 s, all inside the chapter's first shot.
- No "chapter" word, no episode number repeated, no drop shadow, no wipe transition into or out of the card.

### 5.4 `PANEL` — the 42 DOC/ARTICLE evidence panels (three sub-templates)

Every one of these carries **text that comes from the shot map's `Graphic Specifications` sheet**, set exactly.
You own the layout, the hierarchy and the motion. You do **not** own the words.

Anatomy (all three sub-templates):
```
y 216   [class tag]              [chapter numeral]                    [MG id, mono, 12 % opacity, debug-only]
y 240   ─────────────────────────────────────────────────────────── hairline 1 px bone 32 %
y 288   HEADLINE (--t-panel-head, max 3 lines, 104 px margin)
y 400   body / quote / rows
y 792   [optional diagram band]
y 872   ─────────────────────────────────────────────────────────── hairline 1 px bone 32 %
y 900   SOURCE LINE (--t-label)                    [ATTRIBUTION] (--t-label, right-aligned)
```

**P1 · `CITE`** — a quotation or a museum's stated description.
- Body is `--t-quote` at 38 px, max 4 lines, hanging indent 26 px, opening quote glyph in amber at 0.5 opacity.
- Source line always names the institution and, where the script does, the document type.
- Motion: quote lines stagger up 8 px, 0.06 s apart; rule under the quote draws 0.9 s.
- Use when the map's text is a *statement by an institution*.

**P2 · `FACT`** — catalogue data for an object.
- Two-column mono table: label left (bone 60 %), value right (ivory), row height 56 px, 24 px gutters, hairline row
  rules at 18 % bone.
- Accession strings, dimensions, culture, medium, find region, credit — never more than 6 rows.
- Motion: rows stagger in 0.06 s, values one frame behind labels; no counting, no typewriter.
- Use for the Met bulla panels and any catalogue panel.

**P3 · `LOGIC`** — the film's comparative machinery: two lanes, three parts, a decision path.
- Two or three lanes across the 12-column grid, each with a mono lane label, a short claim in body type, and a
  hairline connector. If a lane is *disconfirming*, its label is `--rust` and its connector is dashed.
- Motion: lanes build left→right, 0.12 s apart; connectors draw `--m-draw`.
- Use for "picture vs job", "administrative vs merchant", "association vs manufacture", "object / context / site".

Common panel behaviour:
- Enter: header hairline wipes left→right (0.4 s), then headline, then body stagger, then footer rule draw (0.5 s).
  Total entrance ≤ 1.4 s. The panel must be fully readable within 1.6 s of the cut.
- Hold: `Drift Hold` — 1.5 % scale over the shot, origin at the type block, never on the whole frame.
- Exit: 8 frames, opacity only, finishing on the last frame before the cut.
- If a panel's text is long enough to need >3 headline lines or >5 body lines, **reduce the type size one step and
  widen the measure — do not shorten the text**.

### 5.5 `DIAGRAM` — the three VX slots (structural, no invented quantities)

| Slot | TC | Subject (from the film's own argument) | Build |
|---|---|---|---|
| `VX-001` | 07:46:04 | **Three questions, three kinds of evidence** — object type / palace setting / manufacture date | Three vertical lanes; each: question (body), "what would answer it" (bone 60 %), hairline base. No icons. |
| `VX-002` | 06:53:12 | **How a survey feature becomes a site** — archives & texts → multibeam bathymetry → side-scan sonar → test excavation → inventory, drawing, photography, mapping | Horizontal pipeline, 5 nodes, 1 px connectors, 8 px node ticks. **No survey imagery, no sonar graphic, no seabed.** |
| `VX-003` | 01:22:17 | **Association is not manufacture** — context (2nd c. AD ceramics) vs object (report allows earlier) | Two parallel timelines with a shared "reported" bracket; the earlier-object branch is dashed `--rust`; the qualification is set in type, verbatim from the report. |

Rules: every node label is text from the map/script; every connector is 1 px; every diagram is monochrome + one
accent; **no animation may suggest data being measured** (no progressive fills, no gauges, no counting numerals).
Build-in is a stagger of nodes; the connectors draw after their node arrives.

### 5.6 `MAP` — the one MAP slot (C01-S005, 00:02:08:23 → 00:02:15:15)

A **schematic locator**, not a survey.

- Data: **Natural Earth 1:10m** (public domain) land + coastline + country boundaries only. No hillshade, no
  bathymetry, no hydrology, no roads, no labels from the dataset.
- Projection: Equal Earth or Natural Earth; extent: Mediterranean + Egypt + Iran (lon 20°→56°E, lat 22°→42°N).
- Land `--slate` at 55 % on `--ink`; coastlines 1 px bone 35 %; graticule at 12 % bone, 10° spacing, **no coordinate
  numerals** (numerals read as data we do not have).
- Two markers, identical treatment: **Alexandria** (with the note *royal quarter · Antirhodos* as a second, smaller
  line — no island outline, no site plan) and **Shahr-i Qumis / Hecatompylos (Iran)**.
- Marker: 6 px amber dot + 1 px ring, connecting hairline to a label block; `--m-draw` arc for the connecting line.
- Mandatory disclosure, bottom-left inside the map: `SCHEMATIC LOCATOR — NOT A SURVEY` (`--t-label`, bone 70 %),
  and bottom-right `Coastlines: Natural Earth (public domain)`.
- **Banned:** arrow lines implying routes or voyages, distance figures, "0 km" scale bars (we have no measured
  distance to show), animated zoom into a site, any inset, any bathymetry, any "findspot" marker.

### 5.7 `PHOTO` — the three archive-photograph slots (C02-S005, C02-S007, C02-S009)

The one real photograph in the film, used three times. It must read as *document*, not as decoration.

- Image: unmodified. No crop inside the object, no grade, no AI upscale, no sharpen. Fit the object's plate to the
  panel with a 24 px ink matte; keep the object's own aspect.
- Frame: 1 px bone 40 % rule around the image, with 12 px corner ticks (mono, 1 px) — a museum mount, not a
  drop-shadowed card.
- Accession block (P2 `FACT` anatomy) at the right or below: `Met 1978.93.30` / `Bulla` / `Iran, Shahr-i Qumis` /
  `Not from Alexandria` (last line in `--amber`, it is the point of the panel).
- Credit line, `--t-label`, bottom: `The Metropolitan Museum of Art, 1978.93.30. Purchase, H. Dunscombe Colt Gift,
  1978. Public domain.`
- Motion: **M14 alternate underline reveal** as the shot map specifies — the underline draws in 0.9 s under the
  accession line, image at 4 % push (1.00 → 1.04) across the shot, everything else still.
- If two further public-domain Met bullae ever arrive, slots C02-S007 and C02-S009 take them instead of repeating
  this one. Until then: **same object, three framings** — and say so in the report.

### 5.8 `BUG` — the disclosure bug

The style bible requires an editor label on reconstructed plates. It has never been executed. You will execute it,
quietly:

- Text: `ILLUSTRATIVE RECONSTRUCTION — NOT THE EXCAVATION`, `--t-label` at 11 px, tracked +0.14 em, `--ivory` at 46 %.
- Position: x = 104, baseline y = 1002 (bottom-left, below caption-safe, inside title-safe).
- Appearance: **first plate shot of every plate rack** (11 times in the film), 12-frame fade in, held 4.0 s, 8-frame
  fade out — not on every cut. This keeps the label honest without strobing.
- Second bug, map only: `SCHEMATIC LOCATOR — NOT A SURVEY` (Part 5.6).
- Third bug, photo slots: `ARCHIVE PHOTOGRAPH — UNMODIFIED` at the same position, same behaviour.
- No other bug, stamp, watermark, logo or corner mark anywhere in the film.

### 5.9 `ENDCARD` — the last fifteen seconds

The voice ends at 00:10:39:08. The picture runs to 00:10:56:01. **That 16.7-second tail is the end card** and it is
where the film pays its debts.

- From frame 15334 (10:39:10) an ink scrim rises to 82 % over 20 frames, over the continuing plate. No cut to black.
- Two columns, `--t-label` and `--t-body`, 90 % of the block inside title-safe:
  - **Left column — the film.** Title, series mark `ATLAS UNDERSTORY`, episode number, runtime `10:56`, and the
    one-line honest summary set in `--t-quote` at 30 px: `A reported lighthouse image. An unproven office.`
  - **Right column — the debts.** `Narration: original, written for this film.` · `Music: "Ambiment" by Kevin
    MacLeod (incompetech.com) — licensed under Creative Commons Attribution 4.0, creativecommons.org/licenses/by/4.0/.
    Changed in length and format.` · `Bulla photograph: The Metropolitan Museum of Art, 1978.93.30. Purchase,
    H. Dunscombe Colt Gift, 1978. Public domain.` · `Plate imagery: illustrative reconstruction, generated for this
    film; not the excavation.` · `Map geodata: Natural Earth (public domain).`
- A single 1 px bone rule between columns, drawing in `--m-draw`.
- The final 12 frames fade the whole graphic layer to 0 — leaving the plate alone, which is how the film should end.
- **No** "subscribe", no URL, no QR code, no logo sting, no music-swell flourish.

### 5.10 What this film does **not** get

No lower thirds on plates (the film has no interviewees, no titles, no affiliations to declare — a lower third would
invent a speaker). No progress bar. No timecode. No "chapter 3 of 5" chip. No watermarks. No end-roll longer than
@:10:56. No credits crawl over the final shot beyond the block in 5.9.

---

## 6. THE 98-SLOT PLAN

`OVERLAY_TIMELINE.csv` is the machine-readable version of this section; build from the CSV, not from prose.

### 6.1 The beat structure

- 22 beats. Beat *n* = the shots whose number is `S00n`. Each beat holds one shot per chapter (five in most beats,
  three or four in the last beats, because chapters have 18–22 shots).
- **Odd beats are panel racks** (graphic + photo slots). **Even beats are plate racks.**
- Racks therefore alternate every ~31 s: 10 panel racks, 11 plate racks, one rack at the tail with a single shot.

### 6.2 What goes on each rack type

**Panel rack (odd beat).** Five panels back-to-back, one per chapter, each ~5–7 s. Design consequences:
- The five panels of a rack must feel like **five documents on one desk**: same ground, same header rail, same footer
  position, same entrance rhythm. Vary only the sub-template (CITE / FACT / LOGIC), the content, and one accent.
- Because they are consecutive, movement must alternate: panel 1 enters from the left rail, panel 2 from the top,
  panel 3 from the left, and so on — but *only* in the direction of the hairline wipe, never a slide, never a spin.
- Each panel is a closed exhibit: a viewer pausing at any frame must see class tag, source, and attribution.

**Plate rack (even beat).** Five plates, ~5–7 s each, with no graphic layer except:
- the `RAIL` (always),
- the `BUG` on the first plate of the rack only,
- the `CHAPTER` card if a chapter onset falls inside it,
- `CAPTION` (always, when there is speech),
- a `TRANSITION` at the rack boundary (Part 8).

**The first rack (beat S001) is the overture:** five graphic slots, 0:00–0:31. `TITLE` goes on the first; the other
four carry their map panels but are dressed as **contents cards** — the numeral of their chapter at 22 % opacity
behind the panel (the film's only use of a watermark-scale numeral), so the first 31 seconds read as a table of
contents rather than five unrelated documents.

**The last rack (beat S022)** is one plate (C02-S022, 10:49:09 → 10:56:01) which carries the `ENDCARD`.

### 6.3 Per-slot truth table

Take in/out timecodes, durations and frame counts **only** from `OVERLAY_TIMELINE.csv`, which is generated from the
delivered cue sheet. Never retype a timecode from this document. If the CSV and the master disagree, the master wins
and you stop and report.

---

## 7. CAPTIONS — THE PART THAT IS EASIEST TO GET WRONG

The film is a documentary whose credibility rests on exact quotation. A caption that paraphrases is a lie; a caption
that drifts is a defect.

### 7.1 What the captions are

- **Burned-in subtitles** (Part 4.6) on the programme itself, plus a **sidecar `.srt` and `.vtt`** for platforms.
- They render **the spoken words only**. No speaker labels (there is one narrator), no sound descriptions,
  no music cues, no chapter labels.
- They are **verbatim**: 1,427 words, 48 segments, character for character from `SCRIPT_VERBATIM.md`.

### 7.2 How to get the timing — transcription is for timing only, never for wording

1. Run the transcription tool on the **narration stem** (`1wSMI8sqQl7YEpQqtxIvNO_cOoZx4ICFy`), not the mixed master,
   so the music bed cannot confuse the model.
   Verify the exact flag set with `hyperframes transcribe --help` before you run it; request word-level timings if
   the tool offers them.
2. You now have ASR words with timings and **wrong spellings**. Discard the ASR text entirely.
3. **Align the authoritative script to the ASR timings** segment by segment, in order, 48 of 48. Use a constrained
   aligner (DTW on word counts / longest common subsequence on lowercase alphanumerics) — never free-form matching,
   never re-ordering. Insertions from the ASR are matched to the nearest script token and ignored; substitutions keep
   the script spelling and take the ASR time.
4. Emit one cue per **script segment** by default. Split only per 7.3.
5. **Verify:** every one of the 48 segment onsets must fall within the spoken span, must increase monotonically, and
   must be separated by 0.05–0.60 s. Print the alignment table to the QA report.

**Known ASR traps** (expect and correct all of these — see `PRONUNCIATION_AND_SPELLING.md`):
`Antirhodos` (not "anti rodos / anterodos"), `Pharos` (not "pharaoh's"), `Isis Pharia` (not "Isis feria"),
`Hecatompylos`, `Shahr-i Qumis`, `Goddio`, `Margaret Miles`, `UA.News`, `Live Science`, `UNESCO`, `bulla`,
`ring-signet`, `multibeam bathymetry`, `side-scan sonar`, `Parthian`, `Ptolemaic` (if it appears), `in situ`,
`amuletic`, `copper-alloy`.

### 7.3 Cue rules

| Rule | Value |
|---|---|
| Max lines per cue | 2 |
| Max characters per line | 42 |
| Max characters per second (reading rate) | 17 |
| Min on-screen | 24 frames (1.0 s) |
| Max on-screen | 144 frames (6.0 s) |
| Cue in | first phoneme of the segment (frame-accurate) |
| Cue out | last phoneme + 6 frames |
| Gap between cues | ≥ 4 frames |
| Split points | clause boundaries only — after `,` `.` `?` `;` `:` or before a coordinating conjunction |
| Breaks | never break `ring-signet`, `Shahr-i Qumis`, `in situ`, `AD 133` or a numeral from its unit |
| Punctuation | keep the script's own; curly apostrophes stay curly |

If a segment needs more than 2 lines at 42 characters: split into consecutive cues, keep the exact words, and keep
the cue boundary on a clause. If it *still* exceeds 17 CPS, you may shorten the on-screen dwell only by starting the
cue earlier within its own segment — never by cutting words.

### 7.4 Caption position discipline

The caption band (y 830–960) must stay clear of panel content. Therefore:
- Panel footer rules and footers sit at y ≤ 936… **conflict** — resolve it by moving panel footers to y = 812–860
  whenever a caption is up during that panel, or by lifting the caption block to y = 900 when a panel footer exists.
  Choose one rule per rack and keep it: **panels in packs put their footer at y = 812; captions always sit at 936.**
- Never place a caption over the photo panel's credit line; the credit line moves to the panel's right column top.

### 7.5 The `.srt` / `.vtt`

- 24 fps, frame-accurate, `HH:MM:SS,mmm` (SRT) and `HH:MM:SS.mmm` (VTT), UTF-8, no BOM, no styling tags, no `{\an8}`.
- Exactly the same cue boundaries as the burned-in track — export both from the same data structure, never re-time.
- Filenames: `HF03_Atlas_Understory_01_captions.srt` / `.vtt`.

---

## 8. TRANSITIONS — YOU CANNOT RE-CUT, SO YOU DRESS THE CUTS

The picture is locked: 15,745 frames, 98 slots, cuts already made. A transition in this film is therefore an
**overlay event on top of an existing cut**, never a re-cut, never a cross-dissolve of two clips, never a
frame-rate ramp, never a speed change. `TRANSITION_MAP.csv` lists every permitted event and its frame.

### 8.1 The four transition recipes

| Token | Recipe | Length | Where | Notes |
|---|---|---|---|---|
| `--tr-wipe` | Bone paper band, 1 px leading edge, sweeps L→R, 8 % opacity, motion blur 0.35 | 10 frames | **Every rack boundary** (21 in the film) | The film's rhythm; feels like a page turning on a desk |
| `--tr-leak` | Warm amber light wash from one edge, 18 % peak, 0.5 s ease | 6 frames | **Chapter onsets** (II, III, IV, V) | Sits over the cut; never covers type |
| `--tr-ink` | 2-frame ink dip to 22 %, then 2-frame recovery | 4 frames | **Act breaks only: Ch. III and Ch. V onsets** | The film's two structural hinges |
| `--tr-grain` | Grain surge from 3.2 % → 9 % → 3.2 % | 8 frames | **Rides with every `--tr-leak`** | Ties the digital surface to the archive idea |

Nothing else. **No transition on an ordinary cut.** No fade to black except the final 12 frames. No white flash, no
iris, no wipe with a hard edge, no "glitch", no zoom blur, no shutter.

### 8.2 Rules

- A transition **must not** cover: a caption in its first 8 frames, a panel headline in its first 12 frames, or the
  chapter card's numeral. If a collision exists, delay the transition by up to 8 frames or drop it — drop first.
- A transition may not change the frame's average luminance by more than 12 % at its peak (measure it; a light leak
  that reads as a flash is a defect).
- Never transition on two consecutive cuts. Minimum spacing: 12 seconds of programme between events.
- Every event is logged in `HF04_shot_report.csv` with its frame, recipe, and peak luminance delta.

---

## 9. AUDIO — THE MIX IS APPROVED; YOU DO NOT TOUCH IT

The delivered master carries narration and music at −16.0 LUFS integrated, true peak −1.9 dBFS, with the music bed
side-chain ducked under the voice. That mix is approved. Your job is to **carry it through unchanged**.

- Decode to PCM 48 kHz stereo. **No gain, no limiter, no EQ, no denoise, no "mastering", no normalisation.**
- Re-verify after your render: integrated loudness must be **−16.0 LUFS ±0.1**, true peak **≤ −1.8 dBFS**, and a
  **null test against the master must residual below −60 dBFS peak**. Report both numbers.
- Do not re-time audio. If your render pipeline needs audio padded to picture length, pad with silence, never with
  tone, and never by looping.

### 9.1 Optional sound design — phase 5, gated, opt-in only

If (and only if) the founder asks for it, you may add a **sound-effects stem** for the graphic layer, under these
constraints:

- SFX only at chapter onsets and rack boundaries: paper turn, lamp strike, a low room tone bed at −52 LUFS.
- Peak level of any SFX: **−42 LUFS short-term**; it must be inaudible as an event unless listened for.
- The narration and music beds must be untouched; deliver the SFX as a separate stem (`HF07_sfx_stem.wav`) plus a
  mixed variant (`HF01b`) so the founder can choose.
- Use the `SFX ONLY` workflow, not the music workflow. Do not add any music of your own — the licence situation is
  settled and adding a second track would break the credit chain.

### 9.2 The credit obligation (non-negotiable)

"Ambiment" by Kevin MacLeod is **CC BY 4.0**. The attribution must appear:

1. On the **end card** (Part 5.9), with author, source, licence link, and the "changed in length and format" note.
2. In the **Drive file description** of every deliverable that contains the music.
3. In `HF05_qa_report.md`.

CC BY is satisfied only when all four of those elements are present. Missing one is a licence breach, not a style
issue.

---

## 10. TECHNICAL SPECIFICATION

### 10.1 Canvas and timebase

| Property | Value |
|---|---|
| Canvas | 1920 × 1080, square pixels |
| Frame rate | 24.000 fps **exact**, CFR, no drop-frame, no variable timing |
| Duration | **15,745 frames = 656.042 s = 00:10:56:01** |
| Composition root | one root composition, `data-composition-id="atlas-understory-01"`, `data-fps="24"`, `data-width="1920"`, `data-height="1080"`, `data-composition-duration="656.042"` |
| Time source | the root's duration is **declared**, never derived from content (the linter checks) |
| Nested compositions | one per template (`title`, `chapter`, `panel-cite`, `panel-fact`, `panel-logic`, `diagram`, `map`, `photo`, `rail`, `bug`, `endcard`, `captions`), each with its own duration |
| Clips | every timed element carries `data-start` and `data-duration`; every timed element carries the clip class (lints `timed_element_missing_clip_class`) |
| Media | the master is a `video` element: **muted**, `data-media-start="0"`, one audio source only |

### 10.2 Deliverable encodes

| File | Container / codec | Audio | Notes |
|---|---|---|---|
| `HF01_Atlas_Understory_01_FINISH_1080p24.mov` | QuickTime · **ProRes 422 HQ**, yuv422p10le, BT.709 | PCM 24-bit 48 kHz stereo, **copied from the master** | The programme master. This is the file the founder keeps. |
| `HF02_Atlas_Understory_01_OVERLAY_ALPHA_1080p24.mov` | QuickTime · **ProRes 4444 with straight alpha** | none | Overlays only, transparent everywhere else, for future re-grades |
| `HF00_Atlas_Understory_01_review_540x960k.mp4` | H.264 High, 960×540, CRF 23, `+faststart` | AAC 128 kb/s | Review copy, ≤ 60 MB |
| `HF03_…captions.srt` / `.vtt` | text | — | Same cue data as the burn-in |
| `HF04_shot_report.csv` | text | — | One row per overlay instance + one row per transition |
| `HF05_qa_report.md` | text | — | Every gate in Part 13, with measured values |
| `HF06_atlas-understory-01.hyperframes.zip` | zip | — | Project source, fonts included, no media above 100 MB |

Colour: render **BT.709** with the master's own transform. Do not apply a display transform, do not "convert HDR",
do not add film emulation LUTs. The plates are already graded; your layer is graphic and must land in the same space.

### 10.3 Upload rules

- One file per request. Anything over **100 MB** must be split or sent through the resumable upload path.
- Name files exactly as above. No `final_final`. If you re-render, version the name (`…_v2.mov`) and say which is
  current in the QA report.
- Every upload carries a description that includes: the film, the runtime and frame count, the spec line, the music
  credit, and the sentence *"Picture is the locked v3 cut; no frames were retimed."*

---

## 11. HYPERFRAMES CONFORMANCE — BE LINT-CLEAN BEFORE YOU RENDER

HyperFrames validates structure aggressively. These are the rules you are most likely to break, written as
pre-emptive instructions. Run `hyperframes lint` early and often; a clean lint is a precondition for a good render,
and a *warning* today is a broken frame tomorrow at 4× speed.

### 11.1 Structure and timeline

- One root composition, one root id, one set of dimensions. No `template` wrapper around a standalone composition
  (`standalone_composition_wrapped_in_template`).
- Declare the root duration; do not derive it (`root_composition_duration_derived`,
  `root_composition_missing_duration_source`).
- No `negative_z_index`; build stacking with explicit ordered groups.
- No clip may end past the root duration (`clip_ends_past_root_duration`), no nested clip may be invisible
  (`nested_clip_never_visible`), no duplicate composition ids, no duplicate media ids.
- Every timed element needs timing attributes *and* the clip class (`timeline_element_missing_timing`,
  `timed_element_missing_clip_class`, `timeline_id_mismatch`).
- Keep timelines human: if a track exceeds the density the linter allows (`timeline_track_too_dense`), split the
  material into subcompositions per rack — 22 racks is the natural split.
- No comment left visible in markup (`visible_markup_comment`); no unclosed tags.

### 11.2 Media

- The picture element: `<video muted>` **with** `data-hf-muted`, a single `data-media-source`, `data-media-start="0"`.
  Declaring audio on a muted video (`video_muted_with_declared_audio`) and double-sourcing audio
  (`video_audio_double_source`) are both errors.
- No `base64` media (`base64_media_prohibited`), no placeholder URLs (`placeholder_media_url`), no unreachable URLs
  (`inaccessible_media_url`), no `src` past the media's end.
- Audio element(s) use `data-audio-group`, not imperative control (`imperative_media_control`). No `data-fx-carve`
  trickery on the approved mix.
- Self-closing media tags are banned; close them properly.

### 11.3 Animation

- All motion through the registered GSAP timeline. **No CSS transitions or animations** (`css_transition_used`).
- Register the timeline before any async build (`gsap_timeline_registered_before_async_build`), and never return a
  timeline where a tween is expected.
- No infinite repeats, no `repeat: -1`, no `requestAnimationFrame` loops (`gsap_infinite_repeat`,
  `requestanimationframe_in_composition`, `non_deterministic_code`).
- No transforms on the clip element itself (`gsap_animates_clip_element`) — that would move the picture.
- Never start a full-screen overlay visible (`gsap_fullscreen_overlay_starts_visible`): scrims start at 0 and are
  tweened. This single rule, ignored, produces a black film.
- No animating non-transform properties for motion (`gsap_non_transform_motion`), no `from` opacity no-ops, no
  overlapping tweens on the same property (`overlapping_gsap_tweens`), no relative-value second writers, no function
  values that measure the DOM (`gsap_function_value_hazard`).
- Every frame must be seekable: a cold seek to frame 9,000 must produce exactly the frame a cold seek to 8,999
  produces plus one. Test it (Part 13.11).

### 11.4 Type and texture

- Every font `@font-face`'d from a local file (`font_family_without_font_face`, `system_font_will_alias`).
- Text that sits inside a textured layer needs its mask (`texture_text_missing_mask`); texture classes must exist
  (`texture_class_unknown`), extend a base (`texture_class_missing_base`), and never put a drop shadow on text
  (`texture_drop_shadow_on_text`).
- SVG draw-ons: no CSS `stroke-dasharray` fighting the draw-on (`svg_drawon_css_dasharray_conflict`), measure paths
  after `d` is set (`svg_measure_before_path_d`), round caps need a hidden dash (`svg_round_cap_hidden_dash`).
  For the map's arcs and the panel rules, prefer a plain 1 px `scaleX` rule over a stroke draw-on.

### 11.5 Captions

- One caption track only (`multiple_caption_tracks`), with `data-track-kind="caption"`
  (`caption_track_kind_missing`), transcript inline (`caption_transcript_not_inline`), container positioned, not
  relative (`caption_container_relative_position`), hard kill on exit (`caption_exit_missing_hard_kill`),
  fit-text consistent (`caption_fittext_scale_mismatch`), overflow-proof (`caption_text_overflow_risk`,
  `caption_overflow_clips_scaled_words`), shadow on the text not the container
  (`caption_textshadow_on_group_container`).

### 11.6 Registry items you may use, and the ones you may not

**Verified names from the HyperFrames capability atlas.** Before using one, open its docs page in-session and confirm
behaviour and parameters; if an item does something other than its name implies, choose the closest honest match and
record the substitution in `HF04_shot_report.csv`.

**Approved — build with these:**

| Job | Items |
|---|---|
| Title / chapter lockups | `Titlecard Calm`, `Titlecard Lockup` |
| Evidence panels | `Line-by-Line Slide`, `Staggered Fade Up`, `Drift Hold`, `Inline Highlight`, `Marker Highlight`, `Word-Sweep Highlight`, `Notes Reveal`, `Separator` |
| Structural diagrams | `Flowchart`, `Flowchart Vertical`, `Decision Tree`, `Comparison Split`, `Line-by-Line Slide` |
| Map | `World Map` (feed it Natural Earth yourself), `SVG Stroke Trace` for the connectors, `Offset Path Traveler` only if it stays a hairline |
| Archive photo | `Spotlight Card`, `Outline Draw` (for the M14 underline), `Freeze-Frame Dressing` (only if it adds no ornament) |
| Texture / finish | `Grain Overlay`, `Grain Field`, `Warm Grain`, `Vignette`, `Texture`, `Thin Film` (≤ 40 % opacity) |
| Transitions | `Dissolve Transitions` (as the base for `--tr-wipe`), `Light Transitions` (for `--tr-leak`), `Organic Light Leak Overlay` (at ≤ 18 %), `Directional Wipe` (single direction only) |
| Archival sparingly (max 2 uses in the film) | `Torn Paper Rip`, `Ridged Burn`, `Halftone Dissolve` |
| Captions | the caption system's own neutral track; `Caption Editorial Emphasis` may be used on **no more than six** load-bearing lines (list them in the report) |
| Audio (phase 5 only) | `SFX ONLY` workflow |

**Banned — see Appendix D.** In one line: if it belongs to a product launch, a social platform, a developer tool,
a music video, or a 2026 UI trend, it is not in this film.

### 11.7 Project hygiene

- Workspace: `projects/atlas-understory-01/`, compositions in `compositions/`, assets in `assets/{video,audio,fonts,geo,texture}`,
  data in `data/` (the two CSVs and the script). No media inside the HTML.
- Under 100 KB per composition file (`composition_file_too_large`); if a rack composition grows past that, split by
  panel.
- Keep the 22 racks as subcompositions and one thin root that sequences them — it keeps every file small, makes cold
  seeks cheap, and makes a single-panel revision a one-file change.

---

## 12. THE BUILD — PHASE BY PHASE, WITH COMMANDS AND GATES

Work in this order. **Do not start a phase until the previous gate passes.** Each gate is a measurement, not an
opinion; write the measured value into `HF05_qa_report.md` as you go. If a gate fails twice, stop and report instead
of working around it.

> **On the commands below.** The verbs are HyperFrames' own (`init`, `add`, `lint`, `validate`, `check`, `doctor`,
> `compositions`, `timeline`, `keyframes`, `transcribe`, `measure`, `compare`, `diff`, `capture`, `snapshot`,
> `preview`, `render`, `normalize-audio`, `media-treatment`, `grade-compare`, `audio`, `beats`, `inspect`, `info`,
> `skills`, `present`, `publish`). Flags vary by version — **run `--help` once per verb and use the real flags**,
> then record the exact command lines you used in the QA report so the build is reproducible.

### PHASE 0 — Intake and verification (no design yet)

```bash
hyperframes doctor
hyperframes info
mkdir -p projects/atlas-understory-01 && cd projects/atlas-understory-01
hyperframes init atlas-understory-01 --width 1920 --height 1080 --fps 24
```
Then pull the assets and **verify them by probe, not by trusting the description**:
```bash
ffprobe -v error -count_frames -select_streams v:0 \
  -show_entries stream=nb_read_frames,r_frame_rate,width,height,pix_fmt \
  -show_entries format=duration -of default=nw=1 "$MASTER"
```
**GATE 0** — all of these must be true, or stop:
- `nb_read_frames = 15745`
- `duration = 656.042` (± 0.001)
- `r_frame_rate = 24/1`, `1920×1080`, `yuv420p`
- audio stream: AAC 48 kHz, 2 ch; measured integrated **−16.0 LUFS**, true peak ≤ **−1.8 dBFS**
  (use the `measure` verb or `ffmpeg -af ebur128`)
- the narration stem is **639.330 s of speech span** and contains **no music** (check by measuring spectral flatness
  in a gap, or simply trust the file's provenance and note it)

Write the master's SHA-256 into the report. Every later diff is against this byte-exact file.

### PHASE 1 — The timeline skeleton

```bash
hyperframes compositions add root
hyperframes timeline import data/OVERLAY_TIMELINE.csv     # or generate compositions from it
```
- One root composition, duration declared `656.042`.
- One `<video muted data-media-start="0">` for the master, one `<audio data-audio-group="mix">` for its audio.
- 22 subcompositions (`rack-01` … `rack-22`) sequenced back-to-back with `data-start` / `data-duration` taken from
  the CSV, summing **exactly** to 15,745 frames.

**GATE 1** — `hyperframes lint` reports **0 errors**; the root's declared duration equals 656.042; the sum of rack
durations equals 656.042; a cold seek to frame 15,744 shows the last frame of the last rack (not a blank).

### PHASE 2 — The system

Build `compositions/system.html`: tokens (colours, type scale, spacing, motion), the three `@font-face` declarations,
the texture stack, the grid overlay (debug-only, gated behind a `data-debug` flag), and the rail.

**GATE 2** — one frame rendered with a test panel: no font fallback (compare glyph widths against a reference
render), grain present at 3.2 %, vignette at −7 %, rail hairline at x = 72, everything on the 8 px baseline.
`hyperframes lint` still 0 errors.

### PHASE 3 — Captions (do these before the panels; they constrain the panel footer heights)

```bash
hyperframes transcribe assets/audio/narration_stem.mp3 --words    # confirm flags with --help
python tools/align_script_to_asr.py data/SCRIPT_VERBATIM.md asr.json > data/captions.json
hyperframes add caption-track            # the neutral track only
```
- Build the caption track from `data/captions.json`; export `.srt` and `.vtt` from the same file.
- **GATE 3** — see 13.4/13.5: 48/48 segments aligned, monotonic, caption text identical to the script after
  normalisation, every cue inside its segment, reading rate ≤ 17 CPS.

### PHASE 4 — Panels, rack by rack (the bulk of the work)

For each odd rack, in order: build the five panels from the shot map's `Graphic Specifications`, using the correct
sub-template. Suggested workflow per rack:
```bash
hyperframes add panel-cite panel-fact panel-logic    # instantiate the three templates if not hand-built
hyperframes preview --composition rack-03 --frames 0-250
hyperframes capture --composition rack-03 --frames 24,72,120 --out qa/rack-03
```
Rules you will be tempted to break, and must not:
- Text exactly as specified in the map; if the map's text is missing for a slot, put `TEXT PENDING — DO NOT RENDER`
  in the composition and list it in the report. **Never invent panel copy to fill a hole.**
- Entrance ≤ 1.4 s; readable within 1.6 s; exit complete 8 frames before the cut.
- One accent colour per panel; amber/teal never together; rust only for a disconfirming branch.

**GATE 4** — every odd-rack panel captured at 3 frames (in, mid, out): no overflow, no collision with caption band,
source line present, attribution present, class tag present. 46/46 panels accounted for (42 + 3 diagrams + 1 map).

### PHASE 5 — Photo panels, map, diagrams

**GATE 5** — the photo is unmodified (pixel-compare a 200 × 200 patch of the object against the source file: mean
abs diff ≤ 1); the map carries both disclosures; no diagram contains a numeral that is not in Appendix C.

### PHASE 6 — Film furniture: title, chapter cards, rail, bugs, end card

**GATE 6** — title card legible at 540p; chapter cards land within ±2 frames of the aligned chapter onsets; rail
numerals change exactly once per chapter; bugs appear 11 times (once per plate rack) and nowhere else; end card
begins at frame 15334 and the graphic layer is fully transparent by frame 15,745.

### PHASE 7 — Transitions and texture pass

Apply `TRANSITION_MAP.csv` exactly. Then the global texture stack.

**GATE 7** — 21 wipes + 4 leaks + 2 dips + 4 grain surges + 1 end-card rise, all logged; peak luminance delta ≤ 12 %
per event; no transition lands on a caption's first 8 frames.

### PHASE 8 — Conformance loop

```bash
hyperframes lint --strict
hyperframes validate
hyperframes check
hyperframes doctor
hyperframes measure --loudness --truepeak
hyperframes compare --reference "$MASTER" --candidate qa/overlay-off.mov --ssim
```
**GATE 8** — 0 errors, 0 warnings; loudness −16.0 ± 0.1 LUFS; true peak ≤ −1.8 dBFS; the **overlay-off** render is
SSIM ≥ 0.995 against the master, frame for frame at 24 sampled frames (this is the proof you did not touch the
picture).

### PHASE 9 — Render and deliver

```bash
hyperframes render --composition root --fps 24 --out out/HF01.mov --codec prores422hq --audio pcm_s24le
hyperframes render --composition root --fps 24 --out out/HF02.mov --codec prores4444 --alpha --no-video-source
hyperframes render --composition root --fps 24 --out out/HF00.mp4 --scale 0.5 --codec h264 --crf 23
```
**GATE 9** — Part 13 fully green; Part 14 file list complete; uploads named and described to spec.

### PHASE 10 — Only if commissioned: SFX stem

Part 9.1. Deliver `HF07_sfx_stem.wav` + `HF01b` and nothing else changes.

---

## 13. QA — SIXTEEN GATES, EACH WITH A NUMBER

Measure all of these on the **delivered files**, not on the project. Record every value in `HF05_qa_report.md`,
including the ones that failed on the first pass (with the fix).

| # | Gate | Method | Pass |
|---|---|---|---|
| 1 | Frame census | `ffprobe -count_frames` on HF01 | **exactly 15,745** decoded frames |
| 2 | Duration | same probe | 656.042 s ± 1 frame |
| 3 | Picture untouched | render with overlays disabled; `compare --ssim` at 24 sampled frames across all 98 slots | **SSIM ≥ 0.995** each; zero frame-shift |
| 4 | Audio null test | decode HF01 audio, invert, sum with master audio, measure peak | residual **≤ −60 dBFS** |
| 5 | Loudness | `measure --loudness --truepeak` | **−16.0 LUFS ±0.1**, TP **≤ −1.8 dBFS** |
| 6 | Caption alignment | 48 segment onsets vs VO energy envelope onsets | **±2 frames** each; monotonic; span 1.2 → 639.33 s ±2 frames |
| 7 | Caption fidelity | normalise (whitespace, curly quotes) and compare cue text to script, character by character | **0 differences**, 1,427 words, 48 segments |
| 8 | Reading rate | per cue: chars ÷ duration | **≤ 17 CPS**, ≤ 2 lines, ≤ 42 chars/line |
| 9 | Safe areas | measure bounding boxes of every type element | inside 96 px title-safe; captions inside 192 px |
| 10 | Legibility | downscale frames to 540p; measure caption contrast against the underlying pixels at 12 frames per cue | **≥ 4.5:1** |
| 11 | Determinism | render frames 4,096–4,100 twice; compare | **bit-identical** (or SSIM 1.000) |
| 12 | Cold-seek integrity | cold seek to frames 0, 3,333, 9,111, 15,744; compare with sequential render | identical within SSIM 0.999 |
| 13 | No stray text | OCR 60 sampled plate-rack frames | only the expected bug string appears |
| 14 | Grade isolation | sample plate-only regions outside all overlays; compare to master | **ΔE ≤ 1.0** |
| 15 | Lint / validate / doctor | the four commands | 0 errors, 0 warnings |
| 16 | Licence & credit | end card, Drive descriptions, QA report | all four CC BY elements present in all three places |

Any gate that cannot be measured because a tool is unavailable must be recorded as **NOT MEASURED** with the reason.
An unmeasured gate is not a passed gate, and a delivery with `NOT MEASURED` in it must say so in the first paragraph
of the report.

---

## 14. DELIVERABLES

Into Drive `08 — Finishing (HyperFrames)` under `1XEjoQvvZseZvwcntun68cwoRZiXoZwjf`:

1. `HF01_Atlas_Understory_01_FINISH_1080p24.mov` — ProRes 422 HQ + PCM, 656.042 s, −16.0 LUFS.
2. `HF02_Atlas_Understory_01_OVERLAY_ALPHA_1080p24.mov` — ProRes 4444 + alpha, overlays only.
3. `HF00_Atlas_Understory_01_review_540x960k.mp4` — H.264 review copy (the one the founder will actually watch first).
4. `HF03_Atlas_Understory_01_captions.srt` and `.vtt`.
5. `HF04_shot_report.csv` — one row per overlay instance and per transition: `id, kind, template, in_tc, out_tc,
   frames, element, registry_item, text_hash, source_line, transition, peak_luma_delta, notes`.
6. `HF05_qa_report.md` — the 16 gates with measured values, the flag list from Part 15, the alignment table, the six
   caption lines that received editorial emphasis, and the exact command lines used.
7. `HF06_atlas-understory-01.hyperframes.zip` — the project, fonts included.

Every upload's description must contain the runtime/frame count, the spec line, the music credit, and the sentence
*"Picture is the locked v3 cut; no frames were retimed."*

---

## 15. THE FLAGS — RAISE THESE, NEVER SILENTLY SOLVE THEM

1. **The accession.** Met `1978.93.30` is on screen; the script's handoff was written for `1978.93.29`. Flagged in the
   panel, in the QA report, and in a comment on the panel composition.
2. **The British Museum coin** appears in the script but the film has no photograph of it. If a panel needs it and
   there is no cleared image, the panel stays typographic (a citation panel). Non-commercial licensing is not
   permission for a commercial video; do not download and use a BM image on your own authority.
3. **Photo reuse.** The same bulla appears three times. Two further public-domain Met bullae would fix it; that is a
   sourcing job outside your remit. Say so in one line.
4. **The shot map's text.** If `Graphic Specifications` is missing a slot's text, render `TEXT PENDING — DO NOT RENDER`
   and list it. 46 slots, 46 texts — report the count you actually found.
5. **The braid.** If any instruction elsewhere assumes chapters play in order, that instruction is wrong for this cut.
   **Do not re-cut.** Report the conflict; the braid is the delivered design.
6. **The map's licence line.** Natural Earth is public domain; if you switch datasets, the licence changes and the
   disclosure must change with it.
7. **Pronunciation checks** that the handoff lists as open (the place name and the scholars' names) — if the delivered
   read differs from the script's spelling, that is a caption question for the founder, not a fix for you.
8. **Anything that looks like an improvement to the script.** There is no such thing in this film. The words are
   approved and the voice is recorded.

---

## 16. THE TWENTY RULES

1. The picture is locked. 15,745 frames in, 15,745 frames out.
2. The words are locked. Captions are verbatim; panels use the map's text; nothing is invented.
3. The audio mix is approved. Carry it; prove it with a null test.
4. Never draw the ring, the engraving, the coin, the bulla, a palace plan, a findspot, or a person.
5. Type is modern editorial type. Never pseudo-antiquity, never an inscription.
6. Every panel is a closed exhibit: tag, content, source, attribution.
7. No panel depends on the narration beneath it — the film braids; panels must stand alone.
8. The rail is the one still point: it tells the viewer which chapter the argument is in.
9. Two moving elements at most; one easing family; three durations.
10. No motion in the first 6 frames or the last 6 frames of a shot; exits finish 8 frames before the cut.
11. Odd beats are evidence; even beats are worlds. Keep that contrast sharp.
12. Disclose the reconstruction, quietly and often enough: 11 bugs, one per plate rack.
13. Transitions dress existing cuts; they never re-cut. Four recipes, in one rhythm.
14. Captions: 2 lines, 42 characters, 17 CPS, ±2 frames, zero paraphrases.
15. Granite rules: no glows, no glitch, no neon, no confetti, no carousels, no UI mockups.
16. Every frame must be reachable cold and must render identically twice.
17. Lint clean before every render; measured gates before every upload.
18. Credit the music everywhere the music goes.
19. Flag the accession, the photo reuse, and any missing panel text. Never solve them silently.
20. When in doubt, remove the decoration and let the sentence be the graphic.

---

## APPENDIX A — the 48 segments (alignment anchors)

Full text in `SCRIPT_VERBATIM.md`. Use this table to sanity-check your aligner: **first four words** and word count
per segment. If a segment's ASR match does not begin with something close to these words, the alignment has slipped.

| # | Segment | Chapter | Words | Opens with |
|---|---|---|---|---|
| 1 | `C01-B01` | 01 | 27 | *Alexandria’s lighthouse appears on…* |
| 2 | `C01-B02` | 01 | 29 | *That is the connection…* |
| 3 | `C01-B03` | 01 | 29 | *On October seventh, twenty…* |
| 4 | `C01-B04` | 01 | 30 | *The team describes it…* |
| 5 | `C01-B05` | 01 | 31 | *What can one ring…* |
| 6 | `C01-B06` | 01 | 26 | *One question concerns what…* |
| 7 | `C01-B07` | 01 | 28 | *First, look at the…* |
| 8 | `C01-B08` | 01 | 29 | *A signet can press…* |
| 9 | `C01-B09` | 01 | 29 | *That explains a possible…* |
| 10 | `C02-B01` | 02 | 29 | *The Metropolitan Museum describes…* |
| 11 | `C02-B02` | 02 | 30 | *Those examples concern engraved…* |
| 12 | `C02-B03` | 02 | 27 | *A second museum object…* |
| 13 | `C02-B04` | 02 | 27 | *The museum says a…* |
| 14 | `C02-B05` | 02 | 31 | *This is comparative evidence,…* |
| 15 | `C02-B06` | 02 | 27 | *Now compare the lighthouse…* |
| 16 | `C02-B07` | 02 | 28 | *Its catalog describes Hadrian’s…* |
| 17 | `C02-B08` | 02 | 32 | *That answers the novelty…* |
| 18 | `C02-B09` | 02 | 29 | *But what does recognizing…* |
| 19 | `C02-B10` | 02 | 30 | *Imagine a modern city…* |
| 20 | `C02-B11` | 02 | 29 | *The picture has taken…* |
| 21 | `C03-B01` | 03 | 26 | *The project’s published methods…* |
| 22 | `C03-B02` | 03 | 30 | *One technique is multibeam…* |
| 23 | `C03-B03` | 03 | 31 | *The methods account also…* |
| 24 | `C03-B04` | 03 | 28 | *Excavation adds inventories, drawings,…* |
| 25 | `C03-B05` | 03 | 29 | *That gives the palace…* |
| 26 | `C03-B06` | 03 | 30 | *An Alexandrian merchant is…* |
| 27 | `C03-B07` | 03 | 30 | *This changes the test.…* |
| 28 | `C03-B08` | 03 | 31 | *The merchant suggestion does…* |
| 29 | `C03-B09` | 03 | 30 | *A hypothesis is an…* |
| 30 | `C03-B10` | 03 | 30 | *What would be lost…* |
| 31 | `C04-B01` | 04 | 30 | *The announcement reports the…* |
| 32 | `C04-B02` | 04 | 29 | *The pottery association and…* |
| 33 | `C04-B03` | 04 | 31 | *Consider a hypothetical example:…* |
| 34 | `C04-B04` | 04 | 30 | *That resolves our pottery…* |
| 35 | `C04-B05` | 04 | 32 | *The palace’s royal history…* |
| 36 | `C04-B06` | 04 | 32 | *A useful physical detail…* |
| 37 | `C04-B07` | 04 | 30 | *That suggests one possible…* |
| 38 | `C04-B08` | 04 | 32 | *Separate the claims: the…* |
| 39 | `C04-B09` | 04 | 31 | *One question remains about…* |
| 40 | `C05-B01` | 05 | 35 | *UNESCO’s account of its…* |
| 41 | `C05-B02` | 05 | 31 | *The point is to…* |
| 42 | `C05-B03` | 05 | 29 | *Return to the palace…* |
| 43 | `C05-B04` | 05 | 28 | *The merchant suggestion demonstrates…* |
| 44 | `C05-B05` | 05 | 31 | *Three pieces remain distinct:…* |
| 45 | `C05-B06` | 05 | 31 | *The strongest responsible answer…* |
| 46 | `C05-B07` | 05 | 33 | *In plain words, the…* |
| 47 | `C05-B08` | 05 | 32 | *A related investigation could…* |
| 48 | `C05-B09` | 05 | 27 | *That person’s identity is…* |

---

## APPENDIX B — the 22 racks, verified

Frame totals in this table sum to **15,745** — the same number the master decodes to. Use it to lay out the root
composition; use `OVERLAY_TIMELINE.csv` for anything finer.

| Rack | Kind | Shots | From | To | Frames | The shots in it (P = plate, G = graphic panel, F = archive photo) |
|---|---|---|---|---|---|---|
| S001 | PANEL · overture | 5 | 00:00:00:00 | 00:00:31:04 | 748 | `C01-S001` G, `C02-S001` G, `C03-S001` G, `C04-S001` G, `C05-S001` G |
| S002 | PLATE | 5 | 00:00:31:04 | 00:01:02:05 | 745 | `C01-S002` P, `C02-S002` P, `C03-S002` P, `C04-S002` P, `C05-S002` P |
| S003 | PANEL | 5 | 00:01:02:05 | 00:01:34:18 | 781 | `C01-S003` G, `C02-S003` G, `C03-S003` G, `C04-S003` G, `C05-S003` G |
| S004 | PLATE | 5 | 00:01:34:18 | 00:02:08:23 | 821 | `C01-S004` P, `C02-S004` P, `C03-S004` P, `C04-S004` P, `C05-S004` P |
| S005 | PANEL | 5 | 00:02:08:23 | 00:02:43:05 | 822 | `C01-S005` G, `C03-S005` G, `C04-S005` G, `C05-S005` G, `C02-S005` F |
| S006 | PLATE | 5 | 00:02:43:05 | 00:03:17:00 | 811 | `C01-S006` P, `C02-S006` P, `C03-S006` P, `C04-S006` P, `C05-S006` P |
| S007 | PANEL | 5 | 00:03:17:00 | 00:03:50:03 | 795 | `C01-S007` G, `C03-S007` G, `C04-S007` G, `C05-S007` G, `C02-S007` F |
| S008 | PLATE | 5 | 00:03:50:03 | 00:04:22:23 | 788 | `C01-S008` P, `C02-S008` P, `C03-S008` P, `C04-S008` P, `C05-S008` P |
| S009 | PANEL | 5 | 00:04:22:23 | 00:04:57:16 | 833 | `C01-S009` G, `C03-S009` G, `C04-S009` G, `C05-S009` G, `C02-S009` F |
| S010 | PLATE | 5 | 00:04:57:16 | 00:05:33:02 | 850 | `C01-S010` P, `C02-S010` P, `C03-S010` P, `C04-S010` P, `C05-S010` P |
| S011 | PANEL | 5 | 00:05:33:02 | 00:06:06:21 | 811 | `C01-S011` G, `C02-S011` G, `C03-S011` G, `C04-S011` G, `C05-S011` G |
| S012 | PLATE | 5 | 00:06:06:21 | 00:06:40:16 | 811 | `C01-S012` P, `C02-S012` P, `C03-S012` P, `C04-S012` P, `C05-S012` P |
| S013 | PANEL | 5 | 00:06:40:16 | 00:07:14:11 | 811 | `C01-S013` G, `C02-S013` G, `C03-S013` G, `C04-S013` G, `C05-S013` G |
| S014 | PLATE | 5 | 00:07:14:11 | 00:07:46:04 | 761 | `C01-S014` P, `C02-S014` P, `C03-S014` P, `C04-S014` P, `C05-S014` P |
| S015 | PANEL | 5 | 00:07:46:04 | 00:08:19:17 | 805 | `C01-S015` G, `C02-S015` G, `C03-S015` G, `C04-S015` G, `C05-S015` G |
| S016 | PLATE | 5 | 00:08:19:17 | 00:08:53:07 | 806 | `C01-S016` P, `C02-S016` P, `C03-S016` P, `C04-S016` P, `C05-S016` P |
| S017 | PANEL | 5 | 00:08:53:07 | 00:09:28:00 | 833 | `C01-S017` G, `C02-S017` G, `C03-S017` G, `C04-S017` G, `C05-S017` G |
| S018 | PLATE | 5 | 00:09:28:00 | 00:10:02:17 | 833 | `C01-S018` P, `C02-S018` P, `C03-S018` P, `C04-S018` P, `C05-S018` P |
| S019 | PANEL | 3 | 00:10:02:17 | 00:10:22:18 | 481 | `C02-S019` G, `C03-S019` G, `C05-S019` G |
| S020 | PLATE | 3 | 00:10:22:18 | 00:10:42:17 | 479 | `C02-S020` P, `C03-S020` P, `C05-S020` P |
| S021 | PANEL | 1 | 00:10:42:17 | 00:10:49:09 | 160 | `C02-S021` G |
| S022 | PLATE · tail + end card | 1 | 00:10:49:09 | 00:10:56:01 | 160 | `C02-S022` P |

**22 racks · 98 shots · 15,745 frames.** Eleven racks are panels, ten are plates, and one is the single-shot tail. The alternation is the film's breathing.



---

## APPENDIX C — the only factual strings you may set in type

Everything below is either in the script, in the delivered object's catalogue record, or in the delivered photograph's
own credit. **Nothing else.** If a string is not here and not verbatim in `SCRIPT_VERBATIM.md`, you may not set it.

### C.1 The comparative object (the only object with catalogue data in the film)

```
Met 1978.93.30
Bulla
Un-baked clay
5.51 × 7.8 cm
Parthian, 2nd century BC – 1st century AD
Iran, Shahr-i Qumis (ancient Hecatompylos)
Purchase, H. Dunscombe Colt Gift, 1978
The Metropolitan Museum of Art · Public domain
Not from Alexandria
```
Disclosure that must accompany it wherever it appears: `Comparative evidence. Not the ring, and not from Alexandria.`

### C.2 The museum coin — cited, never pictured

```
British Museum
Copper-alloy coin, minted in Alexandria
AD 133–134
Obverse: Hadrian
Reverse: Isis Pharia and the Pharos
```
If a BM photograph is not cleared, this is a **typographic citation panel only**. No drawn coin, no "reconstruction",
no placeholder graphic of a coin. Ever.

### C.3 Institutions, places, names, dates — as the script uses them

`Alexandria` · `Antirhodos` · `Pharos` · `the royal quarter` · `Shahr-i Qumis` · `Hecatompylos` · `Iran` ·
`the Metropolitan Museum of Art` · `the British Museum` · `UNESCO` · `its underwater heritage convention` ·
`Goddio` · `Margaret Miles` · `Live Science` · `UA.News` · `7 October 2026` · `2nd century AD` · `Roman period`

### C.4 Counts that are genuinely in the script

`Four impressions` (bulla) · `Three pieces remain distinct` · `Five chapters` (title/contents use only) ·
`48`/`1,427` (never as on-screen claims about the film — they belong in metadata, not on screen)

### C.5 Absolutely forbidden in type

Percentages · probabilities · "likely/unlikely" scalars · km or miles · dates not listed above · dimensions not listed
above · object numbers other than 1978.93.30 (except in the report, never on screen) · accession `1978.93.29` ·
any quotation not verbatim from the script · any invented institution, journal, scholar or excavation season ·
"BCE" (the script writes BC/AD — follow the script).

---

## APPENDIX D — the registry blacklist

Grouped by why they are wrong here. Where a name appears in the capability atlas, it is quoted exactly.

**Product-launch apparatus** (this is not a launch): `App Showcase`, `Product Promo`, `Product Turntable`,
`CTA Close`, `CTA Lockup`, `Store Badge Lockup`, `Trust Strip`, `Social Proof Card`, `Testimonial Card`,
`Testimonial Proof Card`, `Logo Sting`, `Logo Intro Sequence`, `Logo Outro`, `Logo Brand Close`, `Logo Wall`,
`Extruded Logo`, `Rubber Band Bumper`, `Blue Sweater Intro Video`.

**Platform and UI idioms** (we are not selling an app): every `Carousel*`, `Orbit Carousel*`, `Circle Carousel*`,
`Path Carousel*`, `Cuboid Carousel`, `Screen Flow Carousel`, `Share Sheet Carousel`, `Vision Carousel*`,
`Browser Device Stage`, `Device Frame Stage`, `iPhone & MacBook 3D Showcase`, `Multi Device Splay`,
`macOS Notification`, `iOS 26 Liquid Glass Home Screen`, `Liquid Glass*`, `Liquid Metal`, `Chrome Orb`, `Glass Hero`,
`Menu Morph`, `Modal Morph`, `Tabs Slide Indicator`, `Settings Toggle Flow`, `Signup Flow`, `Onboarding Stepper Flow`,
`Swipe Rail`, `Sheet Spring-Up`, `Pull to Refresh`, `Native Notification Pop`, `Notification Cascade`,
`Notification Pileup`, `Notification Stack`, `Typing Indicator`, `Chat Message`, `Chat Thread`, `AI Chat Reveal`,
`ChatGPT Exchange`, `Claude Exchange`, `Prompt`/`Typed Prompt`, `Instagram Follow`, `TikTok Follow`, `X Follow Card`,
`X Post Card`, `Reddit Post Card`, `Spotify Now Playing`, `News Ticker`, `Ticker Takeover`, `Week in Merges`.

**Developer and data-app theatre**: `Terminal Simulator`, `Code Typing`, `Code Scroll`, every `Code Snippet – *`,
`Code Diff`, `Code 3D Extrude`, `Code Particle Assemble`, `Code Shader Dissolve`, `Code Morph`, `Telemetry HUD`,
`Camcorder HUD`, `Oscilloscope Trace`, `Waveform` (as decoration), `Animated Bar Chart`, `Bar Chart Race`,
`Count Up`, `Count-Up Stat Card`, `Conic Progress Ring`, `Hairline Arc Gauge`, `NYT Graph`, `Minimal Line Graph`,
`Data Chart`, `NYC Paris Flight`, `US Map`/`US Bubble Map`/`US Flow Map`/`US Hex Grid Map`/`Spain Map`
(geodata must be Natural Earth for this film's locator, not a country-specific template).

**Loud motion and texture** (banned outright): `Glitch`, `Glitch RGB`, `Caption Glitch Rgb`, `RGB Glitch Text`,
`Neon Accent`, `Neon Border`, `Neon Glow`, `Caption Neon *`, `Chromatic Fringe Title`, `Chromatic Radial Split`,
`Chromatic Aberration Wipe`, `Matrix Decode`, `Caption Matrix Decode`, `ASCII Render Pass`, `ASCII Trail Reveal`,
`Char Slam Explode`, `Headline Slam`, `Kinetic Slam`, `Caption Kinetic Slam`, `Shutter Slam`, `Slot Machine Roll`,
`Split-Flap Board`, `Confetti`, `Emoji Pop`, `Caption Emoji Pop`, `Particle Burst`, `Caption Particle Burst`,
`Particle Text Dissolve`, `Pill Karaoke`, `Caption Pill Karaoke`, `Hologram`, `Holographic`, `Holographic`,
`Whip Pan`, `Whip Pan Cut`, `Camera Shake`, `Camera Punch-In`, `Dolly Zoom (Vertigo Shot)`, `Shatter`,
`Destruction Transitions`, `Flash Through White`, `Anamorphic Streak Flare`, `Lens Flare`, `Godrays`,
`Starfield`, `Aurora`, `Aurora Drift`, `Nebula`, `Spiral Galaxy`, `Plasma`, `Voronoi` (as decoration),
`Fractal Noise`, `Worley Noise`, `Gabor Noise`, `Swirl`, `Swirl Vortex`, `Goo`, `Gooey Split`.

**AI and avatar apparatus**: `Avatar Cloud`, `Avatar Group Hover`, `Avatar Presenter`, `HeyGen Avatar Promo Card`,
`AI Answer Rank`, `Agent Cursor`, `Multiplayer Cursors`, every `Cursor *` variant.

**Also banned by judgement even though not listed above:** film-strip borders, sepia "old photo" filters on modern
type, dust-and-scratch overlays at more than 4 % opacity, VHS timing bars, camera-shake on a graphic, and any
transition that draws attention to itself.

**What remains approved** is in Part 11.6. If a job cannot be done with an approved item, build it by hand from type,
hairlines and 1 px geometry. That is the intended method for at least half of this film.

---

## APPENDIX E — spelling and pronunciation locks for captions

The narration is recorded and correct. Captions follow the **script's** spelling, always. These are the words where
ASR will drift and where a "helpful" autocorrect would introduce an error:

| Caption must read | ASR will often produce | Note |
|---|---|---|
| Alexandria’s | Alexandrias / Alexandria's | keep the curly apostrophe |
| Antirhodos | anti rodos, Anterodos, Antirodos | one word, lower-case `rh` |
| Pharos | Pharaoh’s, Faros, pharaohs | the lighthouse, not a king |
| Isis Pharia | Isis Feria, Iris Faria | two words, capital P |
| Hadrian’s | Hadrians, Adrian's | |
| Shahr-i Qumis | Shahri Qumis, Shari Kumis | hyphens and lower-case `i` |
| Hecatompylos | Hecatompilos, Hecatompylus | |
| Goddio | Godio, Goddios | Franck Goddio |
| Margaret Miles | Margret Miles | |
| UA.News | UA News, YouA News | period, no space |
| Live Science | LiveScience | two words |
| UNESCO | Unesco, U.N.E.S.C.O. | all caps |
| bulla | bulls, boola, bowl | |
| ring-signet | ring signet, ring cygnet | hyphen kept |
| multibeam bathymetry | multi-beam bathymetry | one word |
| side-scan sonar | sidescan, side scan | hyphen kept |
| amuletic | amuletik, amulet ic | |
| in situ | insitu, in-situ | two words, no hyphen |
| copper-alloy | copper alloy | hyphen kept |
| Parthian | Parthian, Parthean | |
| second century AD | 2nd century AD | **the script spells it out — keep it spelled out** |
| AD one thirty-three to one thirty-four | 133–134 | **spell it out in the caption, exactly as spoken** |

Rule: if the voice says a number as words, the caption says the words. Captions are a transcript, not a summary.

---

## APPENDIX F — the six caption lines that may receive emphasis

Use `Caption Editorial Emphasis` on **no more than six** moments, and only where the sentence is the film's argument.
Proposed (confirm against the delivered audio before applying):

1. `The picture alone cannot settle that connection.` (VO-C01-B02)
2. `It cannot, without more evidence, identify the occupation of the person carrying it.` (VO-C02-B09)
3. `A hypothesis is an explanation that needs testing.` (VO-C03-B09)
4. `The receipt does not make the keepsake new.` (VO-C04-B03)
5. `Bringing them together gives context without producing a named owner.` (VO-C05-B05)
6. `We can recognize the tower. We still cannot name the hand.` (VO-C05-B09)

Emphasis means: the line holds 6 frames longer, its weight shifts 500 → 600, and its leading key word takes amber.
Nothing else. No scale, no colour fill, no underline sweep, no sound effect.

---

## APPENDIX G — first-day checklist

Print this. Tick it. It is the whole brief in sixteen lines.

1. Probe the master: 15,745 frames, 656.042 s, 24/1, 1920×1080. Record the SHA-256.
2. Measure the audio: −16.0 LUFS, TP ≤ −1.8. Write it down; you will prove it again at the end.
3. Load the script and the cue sheet. Confirm 48 segments and 98 slots.
4. Align: 48/48, monotonic, ±2 frames. Export the alignment table.
5. Build the tokens. Three faces `@font-face`'d. No system fallback.
6. Build the rail. It never moves again.
7. Build the three panel templates and one diagram template. Lint clean.
8. Build rack S001 (the overture) end to end. Get it right before scaling; everything else is a variation.
9. Captions on, footer at 812. Check the collision; check 540p legibility.
10. Build the map last of the graphic families — it is the one with a licence line.
11. Then racks S003 … S021 in order. Same templates, different text.
12. Furniture: title, four chapter cards, bugs, end card.
13. Transitions from the map, exactly, no extras.
14. Conformance loop: lint, validate, check, doctor. Zero, zero, zero, zero.
15. Render HF00 review first. Watch it once at 1× with sound before you render the master. Fix what you see.
16. Render HF01, HF02, captions, report, zip. Upload. Credit the music. Flag the accession.

---

*End of brief. The film's standard is the sentence it ends on: we can recognize the tower, and we still cannot name
the hand. Your finish has to be able to say the same about itself — it may show what is known, and it must never
pretend to know the rest.*
