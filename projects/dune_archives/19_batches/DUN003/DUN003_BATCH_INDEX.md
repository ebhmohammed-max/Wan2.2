# DUN003 — Image batch index

Approved: **150 unique stills · ~177 still-based shots + 3 map scenes ≈ 180 on-screen shots · 15 batches × 10**. Max 10 images per batch. Images are CREATIVE RECONSTRUCTIONS, not official artwork, and depict no actor.

| Batch | Scenes | Chapters | Status |
|---|---|---|---|
| BATCH001 | 001–010 | 00, 01 | **COMPLETE v2: 10/10 PASS, on Drive** |
| BATCH002 | 011–020 | 02 | **COMPLETE: 10/10 PASS, on Drive** |
| BATCH003 | 021–030 | 02, 03 | **COMPLETE: 10/10 PASS, on Drive** |
| BATCH004 | 031–040 | 03 | In progress: 3 PASS / 2 FIX / 1 FAIL (031–036); 037–040 pending |
| BATCH005 | 041–050 | 03, 04 | PENDING |
| BATCH006 | 051–060 | 04 | PENDING |
| BATCH007 | 061–070 | 04, 05 | PENDING |
| BATCH008 | 071–080 | 05, 06 | PENDING |
| BATCH009 | 081–090 | 06 | PENDING |
| BATCH010 | 091–100 | 06, 07 | PENDING |
| BATCH011 | 101–110 | 07, 08 | PENDING |
| BATCH012 | 111–120 | 08 | PENDING |
| BATCH013 | 121–130 | 09 | PENDING |
| BATCH014 | 131–140 | 09, 10 | PENDING |
| BATCH015 | 141–150 | 10, 11 | PENDING |

## QC log — BATCH001 v1 (2026-11-23)

| Scene | QC | Note |
|---|---|---|
| SCENE001 | PASS | Strong: scale, single shaft, palette. |
| SCENE002 | FIX | Eye whites not blue (needs blue-in-blue); throne carvings read as a real-world heraldic eagle → edit. Face = candidate CS-PAUL-C, needs director approval. |
| SCENE003 | FIX | Ornithopters rendered with helicopter rotors (violates bible §3) → edit to flapping wings. |
| SCENE004 | FAIL | Architecture reads as Roman/Jerusalem, mismatched with SCENE003 → regenerate with SCENE003 as reference. |
| SCENE005 | REJECTED | Face resembled a well-known actor + film-like stillsuit. File deleted, never uploaded. Regenerate as distant back view, face hidden. |
| SCENE006 | FIX | Eagle not hawk; hand reads ~60 years old → edit. |
| SCENE007 | PASS | Letterbox bars baked in; crop in edit. |
| SCENE008 | FAIL | Face does not match SCENE002; medieval European city → regenerate with SCENE002+003 references. |
| SCENE009 | PASS | Pseudo-letters on border; acceptable under motion blur, crop if needed. |
| SCENE010 | PASS | Clean negative space for archive card. |

**Tool constraint discovered:** the image tool allows at most 10 generations per turn → exactly one batch (or one batch of fixes) per turn.

## QC log — BATCH001 v2 (2026-11-23, turn 2)

| Scene | QC | Note |
|---|---|---|
| SCENE002 | PASS | PASS (director-selected redesign v1.2, option 2 of 2; director to confirm no likeness) |
| SCENE003 | PASS | PASS — regenerated (v1 lost between turns); flapping-wing ornithopters |
| SCENE004 | PASS | PASS — regenerated with SCENE003 reference; architecture matches |
| SCENE005 | PASS | PASS — back view, faces hidden (director rule) |
| SCENE006 | PASS | PASS — regenerated; hawk signet, ~30-year-old hand |
| SCENE008 | PASS | PASS — regenerated with SCENE002 v2 + SCENE003 refs; note: small background ornithopter slightly rotor-like, mask in edit if visible |

- **Paul redesigned (CS-PAUL v1.2).** The director flagged that the v1 SCENE002 face resembled a known actor. The v1 face is retired, and the director picked the new face from 2 options.
- **Images do NOT persist between turns** (git-ignored files are wiped). Rules from now on: upload every image to Drive in the same turn it is generated, and keep small JPEG anchor references in `anchors/`, which are committed.

## Reference anchors (committed, `anchors/`)
| File | Use |
|---|---|
| REF_CS-PAUL-C_v1.2.jpg | Paul (Emperor) face, front three-quarter. Pass it as a reference for every CS-PAUL-C or -D shot |
| REF_CS-PAUL-C_v1.2_profile.jpg | Paul profile |
| REF_LOC_ARRAKEEN_CITADEL.jpg | Citadel / Arrakeen architecture. Pass it as a reference for every Arrakeen exterior |

## QC log: BATCH002 v1 (2026-11-23, turn 3)

| Scene | QC | Note |
|---|---|---|
| SCENE011 | PASS | Worms read slightly airborne; dust overlay in motion pass |
| SCENE012 | FIX | Roman columns + Roman-style courtiers (Earth drift). Face = CS-SHADDAM draft, director approval pending. Regen with arch guard + face anchor ref |
| SCENE013 | PASS | — |
| SCENE014 | PASS | Original cylindrical heighliner design |
| SCENE015 | FIX | Gothic cathedral / rose window (Earth drift). Composition (far, from behind) is right; regen with arch guard |
| SCENE016 | HOLD | Face original (no match found by eye), but styling (blonde braided crown + crimson/gold + lion pendant) echoes a famous TV queen. Director decision |
| SCENE017 | FIX | 'elfin' produced pointed elf ears. Face = CS-CHANI-B draft (freckles, jaw scar, blue-in-blue OK). Fix ears via edit of anchors/REF_CS-CHANI-B_v1_draft.jpg |
| SCENE018 | PASS | Hawk signet matches SCENE006 |
| SCENE019 | PASS | — |
| SCENE020 | PASS | Wingless transports, no rotors |

**Changes this turn**
- **Faces protected against likeness before generating.** The CS-SHADDAM, CS-IRULAN and CS-CHANI-B anchors were rewritten with distinctive bone structure and markings, steering away from the film casting.
- **Builder guards added.** `ARCH_GUARD` adds austere monolithic stone with no columns or arches to any interior or architecture shot. `CRAFT_GUARD` adds "no rotors" to any aircraft shot. The negative list was extended.
- **Letterbox phrase replaced** with "full-bleed 16:9, no black bars". All 10 frames came out bar-free.
- Draft face anchors are saved in `anchors/` as `*_v1_draft.jpg` until the director approves them.

## QC log: turn 4 (2026-11-23)

| Scene | QC | Note |
|---|---|---|
| SCENE012 | PASS v2 | PASS v2: edited setting to monolithic stone; face approved (CS-SHADDAM v1) |
| SCENE015 | PASS v2 | PASS v2: monolithic hall, slit windows, distant back view |
| SCENE016 | PASS v2 | PASS v2: restyled per director (veil, ivory/pale gold, lion shoulder clasp); face kept (CS-IRULAN v2). Minor: blurred round niches in background |
| SCENE017 | PASS v2 | PASS v2: human ear, full blue-in-blue; face approved (CS-CHANI-B v1) |
| SCENE021 | PASS | Back view only (director rule) |
| SCENE022 | PASS | — |
| SCENE023 | PASS | — |
| SCENE024 | PASS | Back view only (director rule); throne matches SCENE002 basalt |
| SCENE025 | PASS | — |
| SCENE026 | PASS | — |

- **Director "go" recorded as:** Irulan restyle approved; Shaddam and Chani faces approved.
- **Rule enforcement:** the CS-PAUL-B anchor is now back-view only, and SCENE021 changed from CU to MS from behind. Before this fix, the director's young-Paul rule hadn't been applied to Batch 003 prompts. It was caught before generation.
- **Editing preserves faces:** face-preserving edits (012, 016, 017) kept the approved faces while fixing the setting, costume or ears. Prefer editing over regenerating once a face is approved.

## QC log: turn 5 (2026-11-23)

| Scene | QC | Note |
|---|---|---|
| SCENE027 | PASS | Citadel faint in mirage (REF_LOC anchor used) |
| SCENE028 | PASS | Paul face matches CS-PAUL-C anchor; sclera blue not clearly readable at this size |
| SCENE029 | PASS | — |
| SCENE030 | PASS | — |
| SCENE031 | PASS | Statues in ancient-style armour = deliberate echo of historical conquerors; faces eroded |
| SCENE032 | FIX | Read as Buddhist monks (saffron, shaven) + church thuribles = Earth-religion drift. Regen with hooded black/ochre priests |
| SCENE033 | PASS | — |
| SCENE034 | FIX | White sclera; edit to blue-in-blue (source anchors/EDITSRC_B004_SCENE034_FREMEN_GOVERNOR.jpg) |
| SCENE035 | PASS | — |
| SCENE036 | FAIL | ALIEN creatures in crowd: Dune has no aliens (canon). Regen; humans-only guard now in builder |

- **New canon guard:** every prompt now states "any people shown are fully human (no aliens, no creatures)". Aliens, Buddhist monks, saffron robes and Earth religious symbols are added to the negatives.
- **CS-ALIA-A/B hardened before first use.** The old anchor's "wide-set intense eyes" is the signature feature of the actress cast as Alia in *Part Three*. It's now a narrow heart-shaped face, small close-set deep-set eyes, an upturned nose, a lip scar and a blunt bob. Director approval is needed at first generation (SCENE037).
- **SCENE033** said "towering columns", which contradicted ARCH_GUARD. Now "sheer monolithic walls and massive square piers".
- **New tool `tools/rebuild_preserve.py`** rebuilds and keeps all QC'd records, batch statuses and this index automatically. It replaces the manual /tmp backup and restore.

## QC log: turn 6 (2026-11-23)

| Scene | QC | Note |
|---|---|---|
| SCENE032 v2 | PASS | Hooded black/ochre veiled priests, angular censers; Buddhist-monk drift fixed |
| SCENE034 v2 | PASS | Face-preserving eye edit: saturated blue eyes; everything else unchanged |
| SCENE036 v2 | PASS-FLAG | All humans now (alien FAIL fixed). Director flag: some figurines resemble Earth Madonna statuettes |
| SCENE037 | PENDING-APPROVAL | First CS-ALIA-B original face; ref saved as anchors/REF_CS-ALIA-B_v1_PENDING.jpg |
| SCENE038 | PASS | Back view, face hidden |
| SCENE039 | PASS | — |
| SCENE040 | PASS | Angular monolithic hall |
| SCENE041 | PASS | — |
| SCENE042 | PASS | No lettering on book |
| SCENE043 | PASS | Wallach IX = CREATIVE RECONSTRUCTION mood only |

- **Batch 004 closed** (pending the director's Alia decision and the S036 flag). Batch 005 is at 3/10.
- **Guild Navigator vs humans-only guard:** `build_episode.py` now has `human_clause()`. Navigator/tank shots (CS-EDRIC, S044/S049/S050) say "The Guild Navigator is a mutated human, not an alien; everyone else shown is fully human." In Frank Herbert canon, Navigators are humans mutated by spice (ORIGINAL FRANK HERBERT CANON). All other shots keep the strict humans-only clause.
- **Anchor hardening before first use:** CS-MOHIAM changed from "birdlike face, piercing pale eyes" to a broad, wrinkled, heavy-lidded original face with a chin mole and cropped grey hair (avoids a generic old-crone look that could converge on a known performer). The S-shot Irulan wording was aligned to the approved IRULAN v2 (veiled, pale gold/ivory gown).

## QC log: turn 7 (2026-11-23)

Director said "go on". By my stated default, that approves the **CS-ALIA-B v1 face** and the **S036 figurine fix**.

| Scene | QC | Note |
|---|---|---|
| SCENE036 v3 | PASS | Figurine-only edit: faceless hooded masculine emperor statuettes; Madonna read removed |
| SCENE037 v2 | PASS | Alia-B face APPROVED; eye edit now fully blue-in-blue. Ref: anchors/REF_CS-ALIA-B_v1.jpg |
| SCENE044 | PASS | Conspirators table; faces mostly hidden |
| SCENE045 | PENDING-APPROVAL | First CS-MOHIAM v1 face (ref anchors/REF_CS-MOHIAM_v1_PENDING.jpg) |
| SCENE046 | PASS | Minor: needle a little far from the neck; faces out of frame |
| SCENE047 | PASS | — |
| SCENE048 | PASS | — |
| SCENE049 | PENDING-APPROVAL | First CS-EDRIC v1 original Navigator design (ref anchors/REF_CS-EDRIC_v1_PENDING.jpg) |
| SCENE050 | PASS | Sclera pale blue, acceptable through glass |
| SCENE051 | PASS | — |

- **Batch 004 complete (10/10).** Batch 005 is closed pending two face approvals. Batch 006 is at 1/10.
- **The Navigator clause worked:** Edric reads as a changed human (human face, webbed hands, finned feet), not a creature.
- **Edits for small fixes keep working:** the figurine-only and eye-only edits changed just the target and left the rest of the frame intact.

## QC log: turn 8 (2026-11-23)

Director said "go on". By my stated default, that approves the **CS-MOHIAM v1** and **CS-EDRIC v1** designs (S045 and S049 are now PASS).

| Scene | QC | Note |
|---|---|---|
| SCENE052 | PASS | Heighliner hold; no rotors, no markings |
| SCENE053 | PENDING-APPROVAL | First CS-SCYTALE natural Face Dancer face (ref anchors/REF_CS-SCYTALE_v1_PENDING.jpg) |
| SCENE054 | PASS | Half-transformed face; no gore |
| SCENE055 | PASS | Sealed brutalist city |
| SCENE056 | PASS | Irulan v2 ref held |
| SCENE057 | PASS | Irulan v2 ref held; minor blurred arch in background |
| SCENE058 | PASS | Minor: vial neck slightly modern |
| SCENE059 | PASS | Chani-B ref held; minor Earth-style hurricane lamp at left edge |
| SCENE060 | PASS | Drive upload deferred (rate limit) |
| SCENE061 | PASS | Drive upload deferred (rate limit) |

- **Batch 005 complete (10/10).** Batch 006 is closed pending the Scytale face. Batch 007 is at 1/10.
- **Drive rate limit hit after 13 transfers in one reply.** S060, S061, index v8 and manifests v8 will be uploaded at the start of the next turn. Their `drive_file_id` values are null until then.

## QC log: turn 9 (2026-11-23)

Director said "go on". By my stated default, that approves the **CS-SCYTALE v1** natural face (S053 now PASS). S060 and S061 were uploaded at the start of this turn.

| Scene | QC | Note |
|---|---|---|
| SCENE063 | PASS | Edric ref held; tank carried through the throne hall |
| SCENE064 | PENDING-APPROVAL + FIX | Hayt from the Duncan-A ref; eyes need a faceted-metal edit |
| SCENE065 | PASS | Duncan's last stand, seen from behind |
| SCENE066 | PENDING-APPROVAL | First CS-DUNCAN-A face |
| SCENE067 | PASS | Axlotl vats, nothing explicit |
| SCENE069 | FIX | Paul's eyes are not blue-in-blue; eye edit queued |
| SCENE071 | PASS | Paul-C ref held |
| SCENE072 | PASS | Falcon-type hawk banner |
| SCENE075 | PASS | — |
| SCENE062 | not generated | The first attempt failed with a generator error, and the failed attempt counted toward the 10-per-turn cap |

- **Duncan sequencing:** I generated the defining Duncan-A portrait first, then built Hayt from it as a reference. The other Hayt close-ups (S068, S070, S073, S074) are held until the director approves the face.
- **Upload pacing:** two rounds of 5 uploads separated by a 25-second pause went through without hitting the rate limit.
