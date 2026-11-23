# Storyboard conventions
- One row per on-screen shot in `STORYBOARD_TEMPLATE.csv`. Columns map 1:1 to the 10-field decision grid (Visual Style Bible §2) plus motion/edit fields.
- `unique_or_reuse`: UNIQUE = new still to generate; REUSE = reframe/motion pass of an existing still (`reuse_of` = scene id). This is how the unique-image count stays well below the shot count.
- `motion_recipe` values are those implemented in `tools/motion_engine.py` (PUSH_IN, PULL_OUT, PAN_LR, PAN_RL, TILT_UP, TILT_DN, PARALLAX, DRIFT, WORM_RISE, HOLD) or MAP for `tools/map_animator.py`.
- Batches: group UNIQUE rows into batches of ≤10 → `19_IMAGE_GENERATION_BATCHES/DUN###_BATCH###.json`.
- Image filenames: `DUN###_BATCH###_SCENE###_SHORTDESC.png`.
