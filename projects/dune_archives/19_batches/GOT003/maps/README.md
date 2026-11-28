# GOT003 animated maps + document mockups
Rendered by `tools/got003_maps.py` (EP=GOT003) from the text-free base art in `../maps_base/`.
All words, routes, pins, shields, handwriting, strikes and stamps are drawn in code and timed to the narration
(word cues resolved against `22_edit/GOT003/GOT003_timeline.json`). Each clip's length equals its on-screen shot
(+0.4 s); `render_v2.py` streams it for MAP:* shots. Re-render after any timeline change:
`EP=GOT003 python tools/got003_maps.py` (all) or `... M02 K09` (some); `--frames KEY` = 6-frame QC sheet in `../maps_qc/`.
Maps carry 'SCHEMATIC · AFTER THE MAPS IN THE BOOKS'; mockups carry 'RECONSTRUCTED DOCUMENT · ILLUSTRATIVE'.

## Where the mp4s live
The 29 clips total ~108 MB, so they are **not committed** (`.gitignore`: `19_batches/GOT003/maps/*.mp4`).
They are rebuilt exactly from code + `maps_base/` art: locally with `EP=GOT003 python tools/got003_maps.py`,
and in CI by `.github/workflows/got003_master.yml` (step "render maps + mockups"), which runs right after
`v2_timeline.py`, so clip lengths and word cues always match the final edit.
