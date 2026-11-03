# Shot 02 — "The Lantern"

Vertical 9:16 character shot for **Wan2.2**: an ancient explorer in rough brown linen walks slowly
toward a camera that tracks backward ahead of him through a hand-carved tunnel beneath Cappadocia,
a brass oil lantern swinging in one hand and his other hand trailing the stone wall.

Companion to shot 01 (`../` — the empty tunnel reveal). Same look, same delivery chain, but this
shot is about a *person*, which changes the production route: identity has to be locked in an
image, not described in text.

```
shot02_explorer/
├── prompt.md                      prompt + motion prompt + hand/face negatives + craft notes
├── prompt_master.txt              the prompt as fed to generate.py (T2V / TI2V)
├── prompt_motion.txt              motion-only prompt (I2V — the main route)
├── prompt_v2.txt / prompt_v2.md   director's cut: eight-part spine + @CAST binding + base look
├── keyframes/
│   ├── kf00_character_sheet.png   CAST EVIDENCE — front / back / face / neutral pose, wardrobe locked
│   ├── kf01_walk.png              IDENTITY REFERENCE — start frame, mid-stride, hand on wall
│   ├── kf02_step.png              one step further, weight shifted onto the front leg
│   ├── kf03_stride.png            two steps further, head turned to the wall, lantern swung back
│   └── kf04_close.png             three steps further, waist-up beat, lantern at frame edge
├── previz/
│   ├── render_previz.py           walking animatic renderer (walk bob + lantern flicker)
│   └── shot02_previz_9x16.mp4     1080x1920 @ 24 fps, 5.17 s
├── scripts/
│   ├── 01_run_i2v_a14b.sh         PRIMARY — I2V-A14B from the identity keyframe
│   ├── 02_run_ti2v_5b.sh          single-GPU route — TI2V-5B, 704x1280, 121f @ 24 fps
│   ├── 03_run_animate_14b.sh      performance-driven route — Wan2.2-Animate-14B
│   ├── 04_postprocess_9x16.sh     delegates to the shared 9:16 delivery chain
│   └── 05_sweep_seeds.sh          narrow seed sweep (hands + face are what break)
└── out/                           takes land here
```

## The idea behind the shot

From [`../CREATIVE_BIBLE.md`](../CREATIVE_BIBLE.md): *a single lamp reveals a city that was built never to
be seen.* So the lamp is the only key light, the light radius is the edge of the world, and the man is not
a tour guide — he is the first person to see this level in a very long time. Read his face, not the
architecture, for the beat.

Route: `prompt_v2.txt` + `@CAST` (`kf01_walk.png`) through `scripts/01_run_i2v_a14b.sh`. Judge takes with
`kf00_character_sheet.png` next to them — identity drift is measurable, not a matter of taste.

## The previz

`previz/shot02_previz_9x16.mp4` is a **walking animatic, not model output**. The four keyframes
were generated as edits of one reference frame, so the man, his clothing and the lamp light stay
identical; they are cut on 0.5 s crossfades and driven with:

* a continuous 1.02 → 1.06 push (he approaches slightly faster than the camera retreats),
* a procedural walk bob — 6 px vertical weight shift plus 0.28° of roll at 1.55 Hz, which is what
  makes still frames read as *walking* instead of sliding,
* lantern flicker — additive amber bloom with irregular 0.75–1.25 intensity and a ±1.5 % exposure
  tremble,
* the shot-01 finish: warm low-key grade, haze, dust, vignette, film grain.

Re-render after swapping keyframes (~2 min on 2 CPU cores):

```bash
python shot02_explorer/previz/render_previz.py --out shot02_explorer/previz/shot02_previz_9x16.mp4
```

## Generate the take

**Primary — I2V-A14B from the identity keyframe** (identity locked, 5.06 s, native 9:16):

```bash
cd projects/cappadocia_underground_city/shot02_explorer
CKPT_DIR=~/models/Wan2.2-I2V-A14B GPUS=8 bash scripts/01_run_i2v_a14b.sh
```

Then sweep seeds and pick on the hands:

```bash
SEEDS="20261031 7 42 1234" GPUS=8 bash scripts/05_sweep_seeds.sh
bash scripts/04_postprocess_9x16.sh out/i2v14b_kf01_walk_s20261031.mp4
```

**Single 24 GB GPU — TI2V-5B** (704×1280, 121 f @ 24 fps):

```bash
CKPT_DIR=~/models/Wan2.2-TI2V-5B START_FRAME=keyframes/kf01_walk.png \
  bash scripts/02_run_ti2v_5b.sh
```

**If I2V will not hold the gait — Animate-14B** (animation mode: retargets the motion of a real
walking clip onto the explorer identity still; needs MMAudio/flux preprocessing weights):

```bash
CKPT_DIR=~/models/Wan2.2-Animate-14B REF_VIDEO=/path/walk_9x16.mp4 GPUS=8 \
  bash scripts/03_run_animate_14b.sh
```

| Route | Frames / fps | Hardware | Wall clock (rough) |
|---|---|---|---|
| I2V-A14B 720×1280 | 81 @ 16 | 8× H100 / A100 | ~5–10 min |
| TI2V-5B 704×1280 | 121 @ 24 | 1× 4090 24 GB | ~10–20 min |
| Animate-14B 704×1280 | reference-driven | 1–8× 80 GB | preprocess + ~10 min |

## What to check on each take

1. **Hands** — the lantern hand and the wall hand. Reject on fused or extra fingers; nothing else
   in the shot matters if these break.
2. **Face stability** — identity should hold from frame 1 to 81; drift late in the take is normal,
   a different man at frame 40 is not.
3. **Foot contact** — sliding feet read as fake even when everything else is photoreal.
4. **Lantern light** — the warm key should move across his face with the swing. If the lamp stops
   flickering, the shot dies as a still life.
5. **Backward track** — the tunnel mouth behind him should recede steadily; no push-pull drift.
