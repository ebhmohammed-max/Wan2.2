# Atlas Understory — Video 01 · Production Plan & Batch Log

Source of truth: the matched **v4 handoff pair** only.
- Script: `02_Full_Script_Clean_v4_HANDOFF` (Drive `14k_ODWncBuLTn0AE5c6LydA-EHxzCteMfxf-uCp3EXg`)
- Shot Map workbook: `10_Image_Budget_and_Shot_Map_v4_HANDOFF` (Drive `1wKuxtjWPIHIBzOc0O8Ph0Sw7RBhM_B4YO7UJ7rPgFZ4`)
- Style & Continuity Bible `11…v4` · Anchor Pack & Batch Plan `12…v4`

Output folder: Drive **Video 01** `1llRO_x9IFZMg2mDs6ikUCXitsHi_RTpK`

## What is being made

1,427 spoken words · 5 chapters · 48 VO segments · 98 shots · frames 0–15,745 @ 24 fps (draft 10:56:01).
My scope is **only the 30 generated background plates (6 ANCHOR + 24 EDIT)** plus the **1 sourced Met bulla photo**, each turned into a **plain motion clip**. No voiceover, no music, no titles, no captions — as instructed.

Nothing else in the 98-shot timeline is mine: the 42 DOC/ARTICLE panels, 3 DATA VIZ, 1 MAP and the 48 MG/VX units belong to the graphics/editor agent.

## The six anonymous anchor families (Batch 0)

| Family | Anchor image ID | First shot | Subject — anonymous by rule |
|---|---|---|---|
| A01 | C01-S002-A | C01-S002 | generic underwater water column, soft silt, broad lateral light |
| A02 | C01-S004-A | C01-S004 | natural seabed, one irregular unworked rock edge, low side light |
| A03 | C01-S006-A | C01-S006 | abstract unformed bronze material surface, grazing amber light — **not a ring/coin/inscription** |
| A04 | C01-S008-A | C01-S008 | unmarked unbaked clay surface, warm raking light — no seal/stamp/moth/jar |
| A05 | C01-S010-A | C01-S010 | empty dark display surface, restrained overhead pool of light |
| A06 | C01-S012-A | C01-S012 | water/sediment interface, fine natural ripples, diffuse cool light |

The four EDIT variations per family are fixed by the Shot Map: **var 1 = closer crop / foreground, var 2 = 30° oblique, var 3 = overhead, var 4 = low-angle diagonal.**

## Batch ladder

| Batch | Scope | New generated files | Status |
|---|---|---|---|
| 0 | 6 anonymous anchors | 6 | **DELIVERED** (stills + clips) — awaiting lead approval of the anchor files |
| 1 | Chapter 1 hook/promise edits | 3 (A01, A02, A03 var 1) | next |
| 2 | Chapter 2 | 11 (A04, A05, A06, A01, A02, A03, A04, A05, A06 var 1–2; A01, A02 var 3) + 1 sourced Met bulla | queued |
| 3 | Chapter 3 | 10 (A03, A04, A05, A06 var 3; A01, A02, A03, A04, A05, A06 var 4) | queued |
| 4 | Chapter 4 | 0 — REUSE of C01-* files only | — |
| 5 | Chapter 5 | 0 — REUSE of C02-* files only | — |

Reserve: 3 generated files, unspent until a real failure exists.

## Motion recipes (per shot, from the Shot Map)

Only three recipes are assigned to plates, and each clip implements exactly one:

- **M02 — pullout 6 %**: slow centred zoom out 1.06 → 1.00, cosine eased.
- **M03 — modest layer parallax**: lateral drift with a cheap 3-plane depth proxy (near/mid/far weight maps), each plane offset at 1.55 / 0.95 / 0.45 of the travel.
- **M08 — same-still A/B crop crossfade**: wide crop → tighter crop, crossfaded through the middle ~64 % of the shot; costs zero extra images.

## Technical delivery

- Stills: 3840 × 2160, 16:9, PNG. Generated at 1376 × 768 natively, centre-cropped to exact 16:9, Lanczos-upscaled, gentle unsharp (r 2.0 / 55 % / thr 3), fine grain σ2.2, −6 % corner vignette. **Log note: the upscale adds no new detail — if a 4K native pass is ever wanted, that is a re-render decision, not an edit.**
- Clips: 1920 × 1080, 24 fps CFR, H.264 High, yuv420p, CRF 17, `+faststart`, **no audio stream at all**.
- No baked text, letters, numerals, logos, captions or watermarks in any frame.

## Evidence boundary respected

Nothing generated depicts the ring, its lighthouse engraving, the Met/British Museum objects, the bulla, a palace plan, a findspot, an administrator or a merchant. Generated assets are anonymous illustrative backgrounds/material studies. The editor adds `Illustrative background — not the excavation site` and `Illustrative material study` labels; they are not in these frames.

## Files

- `scripts/make_stills.py` — still mastering pipeline
- `scripts/make_clips.py` — motion renderer (M02 / M03 / M08)
- `manifest_batch0.json` — shot → image → motion → duration mapping
- `stills/batch0/`, `clips/batch0/` — local masters (gitignored; the Drive copies are canonical)
