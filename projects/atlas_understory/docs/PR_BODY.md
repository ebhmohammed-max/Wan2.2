## What this branch contains

Two complete delivery packages, both with media in the Drive folder **Wan 2.2** (never in git).

### 1. Cappadocia underground city — 9:16 shot package (previz, not a final render)
- Prompt package, negative terms and prompt-craft notes.
- Identity-locked keyframes for shot 01 (the tunnel) and shot 02 (the explorer), with a character sheet as cast evidence.
- A shared previz library — plates, eased camera moves, dust, lantern flicker, grade and encode — driving both shots.
- Rendered 1080×1920 16 s animatics plus the I2V/TI2V run scripts.
- Directed to the 2WULFFS method: `studio/2wulffs-playbook.md`, a project creative bible, prompt v2 with an annotated diff, and coverage cards for shots 03–08.

### 2. Atlas Understory Video 01 — 49 plate positions, 49 distinct images, 49 clips
Fuller detail is in `projects/atlas_understory/docs/`, and in the Drive docs `01 — Batch Log`, `02 — Shot-map audit`, `03 — Delivery index`.

- **48 generated cinematic plates + 1 sourced Met photograph**, each mastered to 3840×2160 16:9 (Lanczos → unsharp → grain σ2.2 → −6 % vignette).
- **49 motion clips**, 1920×1080 24 fps CFR, H.264 CRF 17, `+faststart`, no audio stream anywhere, cut at the shot map's own durations with the approved recipes (M02 pull-out 6 %, M03 three-plane parallax, M08 A/B crop crossfade).
- Final plate bed: 49 clips in shot order, **327.71 s**, `12xfAFXo3fSe8_APrzTv1sc3HAaMJCRKG`.
- Six worlds carry the film: A01 deep water descent, A02 seabed survey, A03 the sealing world, A04 clay & impressions, A05 museum study, A06 Alexandria.

**The post-audit pass.** The shot map marked 19 of the 49 plate positions REUSE — Chapter 4 replaying Chapter 1's images, Chapter 5 replaying Chapter 2's — so the second half of the film re-showed frames the audience had already seen twice. All 19 were replaced with genuinely new plates at the same durations and recipes. Zero timeline change. A numeric clone screen (mean abs difference vs anchor at 192×108, <22 = near-copy) caught two failures (C04-S006 6.86, C04-S012 2.01) that were re-shot; C04-S002 was re-shot again by eye after a glyph-like relief appeared on stone that must read as blank.

**Tier 3 spares.** Six alternates, one per world, built from each world's anchor and screened the same way (all 36–53 against the threshold). Masters only, no clips — none is in the cut. T3-A05 was re-shot once because its first version's sealings read as glyph-like stamps.

### Verification
Durations probed against the manifests (all within 0.06 s), every clip 1920×1080 with no audio stream, and every master MD5-hashed — **49 unique stills, zero duplicates**.

### Held throughout
Script, shot order, durations, overlays and accessions are untouched. No generated frame depicts the ring engraving, the BM coin, the Met bulla, a palace plan, a findspot, an administrator or a merchant; no legible inscription, legend or numeral; faces anonymous; no baked text, logos or watermarks; no voiceover, music, titles or captions.

### Two things reserved to the founder
- The sourced bulla is Met **1978.93.30**, not the scripted 1978.93.29 (the scripted object's image host is outside this sandbox's allowlist). The overlay copy still says .29 — flagged, not rewritten.
- C02-S007 and C02-S009 deliberately reuse C02-S005-A at wide and overhead framings, as the shot map specifies; their qualifier copy describes that object. Closed as a decision, not a gap.

### Repo hygiene
`stills/`, `clips/`, `google_drive/`, `refs/`, `image-search/` and `.venv/` stay out of git; Drive is the source of truth for media.
