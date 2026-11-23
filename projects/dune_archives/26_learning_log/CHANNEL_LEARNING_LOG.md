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
- **Generated images vanish between turns** (git-ignored workspace files are not kept). Upload to Drive in the same turn, and commit about 300 KB JPEG anchor references to `19_batches/<EP>/refs/` so face and location continuity survives across turns.
- A Batch 001 rerun took 7 image generations. Fixes eat into the 10-per-turn limit, so batches with many faces should be budgeted at about 7 new images plus 3 spare for fixes.
