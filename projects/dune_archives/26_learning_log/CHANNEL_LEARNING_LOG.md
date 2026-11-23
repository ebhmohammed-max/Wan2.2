# THE DUNE ARCHIVES — Channel Learning Log

| Date | Learning | Source | Action |
|---|---|---|---|
| 2026-11-23 | Part Three opens 18 Dec 2026 (adapts Messiah) — Messiah primers are time-critical | Trade press | Recommend DUN003 first |
| 2026-11-23 | Late-book (Leto II / Golden Path) long-form videos appearing Oct–Nov 2026; no reconstruction-style competitor found | YouTube listings | EPIC slot for DUN020/DUN019 |
| 2026-11-23 | Fandom/Wikipedia not fetchable from sandbox | Tool errors | Rely on primary texts + search; log [VERIFY] |
| 2026-11-23 | CPU render speed: motion_engine ≈0.5–0.6 s/frame at 1080p (2 vCPU) ⇒ ~3.5–4 h CPU per 10 min of motion | Local benchmark | Render overnight / in parallel batches |

## 2026-11-23 — DUN003 Batch 001 (first image run)
- **Likeness risk is real.** A prompt for a young, dark-haired man in a stillsuit in the desert produced a face resembling a well-known actor, even though no names were used. Rule from now on: young-Paul shots are back or distant views until a director-approved, more distinctive CS-PAUL-B anchor exists. Every face shot gets a likeness check before upload.
- **Learned defaults leak in.** "Ornithopter" produced helicopter rotors. Prompts must spell out "no rotors, articulated flapping wings".
- **"Desert city/citadel" drifts toward Earth history** (Roman, medieval). Pass an approved establishing still as a reference image for every later location shot.
- **Generic "hawk" emblems come out as real-world heraldic eagles.** Specify a stylised hawk in profile and avoid heraldic eagle forms.
- **Throughput:** at most 10 image generations per turn, which works out to one batch, or its fixes, per turn.

## 2026-11-23: Paul redesign and storage lesson
- **The director confirmed a likeness problem in scene 002** (the bearded emperor). The cause was the v1 anchor text itself: narrow oval face, wavy dark hair, wiry. Character anchors must be built from *distinctive* features (bone structure, nose, hairline, scars), never from soft, generic "handsome young man" traits. Paul was redesigned (CS-PAUL v1.2) and the director chose the new face from 2 options.
- **Generated images vanish between turns** (git-ignored workspace files are not kept). Upload to Drive in the same turn, and commit about 300 KB JPEG anchor references to `19_batches/<EP>/anchors/` so face and location continuity survives across turns.
- A Batch 001 rerun took 7 image generations. Fixes eat into the 10-per-turn limit, so batches with many faces should be budgeted at about 7 new images plus 3 spare for fixes.

## 2026-11-23: Batch 002 lessons
- **Words get taken literally.** "elfin face" produced pointed elf ears. Describe anatomy, not metaphor: "fine-boned", "pointed chin".
- **Formal interiors drift toward Earth history**: a Roman audience hall, a Gothic wedding cathedral. Fixed at the builder level with ARCH_GUARD, which every interior prompt now gets automatically.
- **Costume-plus-colour combinations can evoke famous characters even when the face is original.** Here, blonde braided crown + crimson/gold + lion = a well-known TV queen. Likeness QC now checks the *styling* as well as the face.
- **The "no black bars" wording works**: 10/10 frames are full-bleed.
- Prompting 10 new shots per turn leaves no spare for fixes. Fix-heavy batches will roll their fixes into the start of the next turn.

## 2026-11-23: turn 4
- **Face-preserving edits work.** Passing the image and saying "keep the face exactly, change only X" fixed the setting (Shaddam), styling (Irulan) and ears plus sclera (Chani) without losing approved faces. This is the preferred fix route.
- **Director rules must be written into the anchor itself.** A per-shot reminder isn't enough. The young-Paul back-view rule had been applied by hand in Batch 001 but not in the data, so Batch 003 contained a young-Paul close-up. It was caught before generation, and CS-PAUL-B is now a back-view-only anchor.
- **Explicit "slit windows" plus "no arches" gives a clean brutalist hall.** Round niches can still creep into blurred backgrounds; acceptable when out of focus.

## 2026-11-23: turn 5
- **Generic "bazaar / pilgrims from many worlds" invites sci-fi aliens.** Dune has none. Every prompt now carries a humans-only clause.
- **"Priests + censers + ochre" reads as Buddhist monks or Catholic thuribles.** Invented religions need invented visual cues: hoods, veils, black-and-ochre, angular metalwork. Name the Earth looks to avoid.
- **Check every new face anchor against the current casting before first use** (as done for Alia). This is now a standing pre-flight step for each batch.
- **Passing the approved anchor JPEG as a reference held Paul's face** in a new setting (SCENE028).

## 2026-11-23: turn 6
- **Global guards need canon-aware exceptions.** The humans-only clause would have blocked Guild Navigators, who are spice-mutated humans in Frank Herbert canon. `human_clause()` now switches to "mutated human, not an alien" only for Navigator/tank shots.
- **Invented-religion cues worked.** Hood + veil + black/ochre + angular censers on rods produced priests with no Earth-religion read (S032 v2).
- **Figurines of a "hooded robed figure" drift toward Madonna statuettes.** For religious merchandise, specify masculine, faceless, armoured or angular silhouettes and name the Earth looks to avoid.
- **Eye-only edits fix blue-in-blue reliably** when the prompt says "irises AND whites both blue, no white sclera". New portraits still often render partly white sclera on the first pass.
- **The venv at /home/user/.venv-dune can vanish between turns.** ImageMagick `convert` is a dependable fallback for JPEG anchors.

## 2026-11-23: turn 7
- **Describe mutated humans by what stays human.** "Human face that is subtly wrong, webbed fingers, finned feet, not a giant head, not a fish, not an alien" produced a believable Navigator. It also stayed clear of earlier film designs.
- **Object-only edits are reliable.** Replacing only the figurines kept every person, coin and light the same. Use targeted edits before full regenerations.
- **The second eye-edit pass reached full blue-in-blue on Alia.** Plan an eye edit after every new spice-eyed portrait.
- **Using the spare 10th slot to start the next batch keeps the pace at about 10 accepted images per turn.**

## 2026-11-23: turn 8
- **Drive upload rate limit:** about 13 file transfers in one reply hit Merge's limit. Keep each reply to at most 12 uploads. Upload the index and manifests first so the record is never missing, and defer images instead.
- **Reference-image scenes held the faces** of Irulan (×2) and Chani in new settings. Every recurring character with an approved anchor should now be generated from its reference image.
- **Props drift to Earth objects** (a hurricane lamp, a screw-neck bottle). Name sci-fi alternatives for props: "angular brass oil vessel", "faceted crystal ampoule".

## 2026-11-23: turn 9
- **Failed generations count toward the 10-image cap.** Put the most important or dependent shots early in the turn and keep 1 slot spare for retries.
- **Uploads of about 5 per round with a 25-second pause** avoided Merge's rate limit (12 transfers in this reply).
- **"Faceted metallic eyes" in a reference-based edit came out as pale silver eyes.** The look needs a dedicated eye-only edit with explicit words: "polished steel, geometric facets, no iris, no pupil".
- **Medium shots built from a face reference can drop the blue-in-blue eyes.** Repeat "eyes entirely blue including the whites" in every Paul prompt, even when using the reference.
- **Hold dependent shots until a new face is approved.** This avoids spending the generation budget on a face that might be rejected.

## 2026-11-23: turn 10
- **Eye-only edits with explicit material words work:** "polished faceted steel, many small flat geometric facets, no iris, no pupil, no white sclera, no glow" fixed S064 in one pass. The blue-in-blue edit on S069 also worked in one pass.
- **Chaining references** (approved face → eye-edited image as the new ref) kept Hayt consistent across 5 shots.
- **"Old Fremen with entirely blue eyes" still rendered white sclera** (S078), even with "no white sclera" in the prompt. Plan an eye edit for every blue-eyed close or medium shot.
- **"Plain grey tunic" tends to render as a modern T-shirt or loungewear.** Next time try "coarse woven grey tunic, high collar, wrapped belt".
- **Two upload rounds of 6 with a 15-second pause** stayed within the rate limit.

## 2026-11-23: turn 11
- **Blue-in-blue fails in nearly every first-pass render**, even with "whites also blue" spelled out (S079, S080, S086). The eye-only edit with "whites completely replaced by a darker deep blue" works first time. Budget 1 edit per blue-eyed close-up.
- **"Fremen in fine city robes" drifted to biblical, Greco-Roman, long-haired Hollywood looks** (S079). Specify hair covered or short, sun-darkened desert faces, and a Fremen cut.
- **Describing dwarfism as "adult man with dwarfism, fully human, not a goblin"** gave a respectful, human result. It was so photographic that the likeness risk needs a human check.
- **Glowglobes in exteriors** sometimes render as lamps on posts. Add "no posts, hovering freely".

## 2026-11-23: turn 12
- **"Smoked-glass lenses" alone renders as modern wire-frame sunglasses.** "Frameless round near-black lenses, no bridge, no temple arms, held by a thin band" got much closer in one edit.
- **Fixing the S079 look** (short hair, head-cloths, desert-cut robes) **dropped the blue eyes entirely.** Every blue-eyed group shot needs a planned eye edit.
- **"Silhouetted towers" in a city-wide shot drifted to modern glass skyscrapers** (S092). Use "blank windowless monolithic stone towers, no glass, no windows".
- **Reference chaining continues to hold faces well:** Lichna in S081 and Bijaz in S088 both matched their refs first time.

## 2026-11-23: turn 13
- **"Blank windowless monolithic stone towers, no glass" plus "deep night, black starry sky"** fixed the skyscraper/daytime drift in S092 in one try.
- **Black imperial robe + round dark lenses can read as Neo from The Matrix** (S098), especially when the robe renders as a long fitted coat. For Paul-D wide shots use "loose layered black desert robe with hood down, wide sleeves, not a coat".
- **"Grey stillsuits" sometimes reproduces the ribbed 2021/2024 film costume** (S099). Consider "plain matte grey stillsuit with simple seams, original design".
- **"Tribe members walking away" at small scale picks up modern backpacks.** Add "no backpacks, no modern gear".

## 2026-11-23: turn 14
- **Ornithopter solved:** "winged aircraft shaped like a large mechanical dragonfly, long segmented fuselage, glass cockpit, four long thin articulated insect wings folded back; NO rotors, NO propellers, NO helicopter blades, NO tail rotor" (S108). Reuse this wording verbatim.
- **"Loose layered black desert robe with wide sleeves, hood down, not a fitted coat"** removed the Matrix read for Paul-D (S103, S110).
- **The Chani-B ref transfers well into new poses**, including pregnancy (S106) and pain (S107).
- **"Abstract geometric carving" can render as a Greek-key meander** (S103). Add "no meander or Greek key patterns".

## 2026-11-23: turn 15
- **Blue-in-blue eyes CAN work first time** when they are the subject of the shot (S117 macro): "the whites of the eyes also completely deep blue, no white visible anywhere in the eyes".
- **"Curved double-edged blade" can give a double-ENDED knife** (S119). Write "single curved blade, hilt at one end only".
- **"Holding a knife over a cradle with two infants" failed to generate** (S116, probably a safety refusal). Reframe so the threat is implied: blade lowered, infants out of frame or only the cradle edge visible.
- The Duncan-B ref with "polished faceted steel, no iris, no pupil, no glow" stays reliable (S114, S115).

## 2026-11-23: turn 16
- **Implying the threat fixed the refusal** (S116): knife held low at the side, only the cradle rim visible with its contents out of frame, gaze toward the doorway.
- **"ONE curved blade only… hilt at the other end only (not double-ended)"** fixed the crysknife (S119 v2).
- **The Alia-B ref keeps blue-in-blue eyes without an edit**, even with two refs combined (S125, S126). Always zoom-crop the eyes to confirm.
- **Drive limit is tighter than logged:** it failed on the 8th upload of this reply (6, then a 20 s sleep, then 2 succeeded before failure). Use at most 6 per reply, or sleep 30 s or more between rounds.

## 2026-11-23: turn 17
- **Spreading uploads across the reply avoided the rate limit**: 3 at the start, 10 generations in between, then 3 at the end, all succeeded.
- "Small clay dish lamps" reads as Indian diyas. Next time try "squat lidded stone oil cups" or glowglobes instead.
- "Plain matte grey stillsuit" still drifts toward segmented film armour in back views (S134). Add "smooth one-piece suit, no armour plates, no segments".
- "About two years old" plus an adult reference renders a 4–5-year-old (S135). Write "toddler, chubby baby cheeks, very small" if a true 2-year-old is needed.

## 2026-11-23: turn 18
- **"Distant ancient ruins" gives Palmyra-style Roman arches and columns** (S147). Always add the no-arches, no-columns clause, even in pure landscape shots.
- A blindfolded, hooded, bearded blind prophet reads strongly as Christ-like (S145). If the director wants less of that: shorter beard, sand-goggle scars, Fremen-style head-cloth instead of a hood.
- "Child's hand" in macro can render as an adolescent hand (S148). Add "small chubby child's hand, short fingers".
- Blue-in-blue eyes held first time again on a close portrait (S146).

## 2026-11-23: turn 19 (image set complete)
- **Object-swap edits work cleanly** (S059: hurricane lamp to glowglobe; everything else held).
- **Eyewear edits overshoot**: asking for a thin band instead of a temple arm gave a thick band and bigger lenses (S094 v2). Say "very thin dark cord, same lens size".
- **Episode total:** 150 unique stills, all PASS. About 19 turns at 10 generations per turn; roughly 25% of slots went to fixes, remakes and eye edits.
- **Drive throughput is now the bottleneck** at 6 uploads per reply. Next episode: upload while generating, or batch the uploads as a zip.

## DUN003 turn 23 (2026-11-23): narration voice audition, no voice chosen
- The in-app TTS audition tool (add_voice/generate_speech) exists. It used the cold-open lines "He won… after he wins?" as the test passage.
- 6 pairs (12 voices) were all rejected by the director:
  - 2 pairs with no preset (narration);
  - 2 pairs of deep US male (entertainment, advertising);
  - 2 pairs of British male (narration, entertainment).
- The director's brief: male, US accent, deep and gravelly, epic trailer style. A British male was tried at the director's request.
- Lesson: the in-app voice range may not cover an epic trailer-style narrator. Consider an external TTS service (e.g. ElevenLabs voice library) or a human VO artist, working from a VO-ready script.
