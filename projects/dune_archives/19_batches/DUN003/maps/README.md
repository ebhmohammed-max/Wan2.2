# DUN003 animated maps (turn 29, 2026-11-23)

Rendered with `tools/map_animator.py` at 1920×1080, 24 fps, H.264, no audio. The scene files are in `templates/maps/`.
Render environment: a venv with `numpy pillow imageio-ffmpeg`. Each map takes about 2 minutes on CPU.

| Map | Storyboard shot | Cut in (VO master v2) | On screen | Rendered | Content |
|---|---|---|---|---|---|
| DUN003_MAP_A_spice_lever.mp4 | 19 (ch. 02) | 69.12 s | 6.4 s | 8.0 s | Power diagram: Arrakis (spice), then the Spacing Guild, then the Empire. Title "The oldest lever" |
| DUN003_MAP_B_jihad_spread.mp4 | 38 (ch. 03) | 135.59 s | 3.4 s | 6.0 s | The jihad radiating from Arrakis to unnamed RECON worlds, with 3 widening territory fills. Subtitle "12 years · about 61 billion dead (Paul's own tally)" |
| DUN003_MAP_C_wallach_ix.mp4 | 56 (ch. 04) | 206.90 s | 5.5 s | 7.0 s | Guild heighliner (Edric), Tleilax (Scytale) and Arrakis (Irulan) converge on Wallach IX (Mohiam), then the plot turns on Arrakis |

- Each render runs 1.5–2.6 s longer than its storyboard slot, so the editor has room to trim. MAP B fills its 3.4 s slot only by its fast first half. If the edit allows, extend the slot to about 5 s.
- **Canon safety:**
  - Every frame carries a provenance caption: SCHEMATIC / CREATIVE RECONSTRUCTION, with artistic positions.
  - Only Arrakis, Wallach IX and Tleilax are named. All other worlds are unnamed RECON dots.
  - The Guild start point is RECON.
- **QC (frame checks at the start, middle and end): PASS.** Layout v2 fixed routes crossing labels in A, B and C.
