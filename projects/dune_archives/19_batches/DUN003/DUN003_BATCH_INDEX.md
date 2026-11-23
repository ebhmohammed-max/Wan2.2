# DUN003 — Image batch index

Approved: **150 unique stills · ~177 still-based shots + 3 map scenes ≈ 180 on-screen shots · 15 batches × 10**. Max 10 images per batch. Images are CREATIVE RECONSTRUCTIONS, not official artwork, and depict no actor.

| Batch | Scenes | Chapters | Status |
|---|---|---|---|
| BATCH001 | 001–010 | 00, 01 | v1 generated · 4 PASS / 3 FIX / 2 FAIL / 1 REJECTED (actor likeness, deleted) |
| BATCH002 | 011–020 | 02 | PENDING |
| BATCH003 | 021–030 | 02, 03 | PENDING |
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
