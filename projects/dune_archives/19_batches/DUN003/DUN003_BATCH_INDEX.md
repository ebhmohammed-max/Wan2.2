# DUN003 — Image batch index

Approved: **150 unique stills · ~177 still-based shots + 3 map scenes ≈ 180 on-screen shots · 15 batches × 10**. Max 10 images per batch. Images are CREATIVE RECONSTRUCTIONS, not official artwork, and depict no actor.

| Batch | Scenes | Chapters | Status |
|---|---|---|---|
| BATCH001 | 001–010 | 00, 01 | **COMPLETE v2: 10/10 PASS, on Drive** |
| BATCH002 | 011–020 | 02 | **COMPLETE: 10/10 PASS, on Drive** |
| BATCH003 | 021–030 | 02, 03 | In progress: 6/10 PASS (021–026); 027–030 next |
| BATCH004 | 031–040 | 03 | PENDING |
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
