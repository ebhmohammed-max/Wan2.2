# Cappadocia Underground City — Wan2.2 shot package

Vertical 9:16 cinematic documentary sequence for **Wan2.2**, split into two shots:

| Shot | Beat | Primary route | Package |
|---|---|---|---|
| **01 "The City Below"** | empty tunnel dollies forward into an enormous lamp-lit chamber, steps descending into dark | TI2V-5B → T2V-A14B | this folder |
| **02 "The Lantern"** | an ancient explorer walks toward a backwards-tracking camera, lantern swinging, hand on the wall | I2V-A14B from the identity keyframe | [`shot02_explorer/`](shot02_explorer/README.md) |

Shared code: `previz/previz_lib.py` (plates, camera moves, dust, lantern glow, grade, encode) and
`scripts/04_postprocess_9x16.sh` (the one 9:16 delivery chain both shots use).

---

# Shot 01 — "The City Below"

Vertical 9:16 cinematic documentary shot for **Wan2.2**: one continuous dolly forward through a
hand-carved tunnel under Cappadocia that opens into an enormous lamp-lit underground chamber with
ancient stone steps leading into darkness.

This folder is a complete, self-contained shot package: locked prompt, exact 9:16 render settings,
three production routes (5B consumer / 14B quality / 14B image-to-video), a delivery post-process,
keyframes, and a rendered motion previz you can watch before burning GPU hours.

```
projects/cappadocia_underground_city/
├── prompt.md                     prompt + negative prompt + prompt-craft notes
├── prompt_master.txt             the prompt as fed to generate.py (T2V / TI2V)
├── prompt_motion.txt             motion-only prompt for image-to-video
├── keyframes/
│   ├── kf01_tunnel.png           start frame — narrow tunnel, arched doorway, dust shaft
│   ├── kf02_chamber_reveal.png   reveal frame — chamber opening up, stairs down
│   └── kf03_deep_hall.png        end frame — carved hall, steps into blackness
├── previz/
│   ├── render_previz.py          camera-move previz renderer (PIL + numpy + ffmpeg)
│   └── cappadocia_previz_9x16.mp4  1080x1920 @ 24 fps, 16 s, watchable animatic
├── scripts/
│   ├── 01_run_ti2v_5b.sh         Wan2.2 TI2V-5B, 704x1280, 121f @ 24 fps  (single GPU)
│   ├── 02_run_t2v_a14b.sh        Wan2.2 T2V-A14B, 720x1280,  81f @ 16 fps  (multi-GPU, best quality)
│   ├── 03_run_i2v_a14b.sh        Wan2.2 I2V-A14B from a keyframe (composition locked)
│   ├── 04_postprocess_9x16.sh    exact 9:16 1080x1920 delivery master + grain + grade
│   └── 05_sweep_seeds.sh         roll 6 seeds and pick the best take
└── out/                          takes land here
```

## The previz first

`previz/cappadocia_previz_9x16.mp4` is a **camera-move animatic, not model output** — the three
keyframes driven by a single eased 1.00→1.16 push-in with 1 s crossfades, plus drifting dust with
depth parallax, warm low-key grade, vignette and film grain. Use it to approve framing, push speed
and the tunnel → chamber → steps reveal; then match the same energy in the Wan take.

Re-render it after swapping keyframes:

```bash
python previz/render_previz.py --out previz/cappadocia_previz_9x16.mp4   # ~3 min on 2 CPU cores
```

## Generate the take

Weights are not in this repo. Download per the root `README.md` (`Model Download`) — you need
`Wan2.2-TI2V-5B` (≈10 GB) for route 1, and `Wan2.2-T2V-A14B` / `Wan2.2-I2V-A14B` (≈27 GB each) for
routes 2–3 — then point `CKPT_DIR` at them.

**Route 1 — TI2V-5B (start here; single 24 GB card)**

```bash
cd projects/cappadocia_underground_city
CKPT_DIR=~/models/Wan2.2-TI2V-5B bash scripts/01_run_ti2v_5b.sh
# or start from the keyframe, which holds the tunnel composition:
CKPT_DIR=~/models/Wan2.2-TI2V-5B START_FRAME=keyframes/kf01_tunnel.png \
  PROMPT_FILE=prompt_motion.txt bash scripts/01_run_ti2v_5b.sh
```

**Route 2 — T2V-A14B (best stone detail, native 9:16)**

```bash
CKPT_DIR=~/models/Wan2.2-T2V-A14B GPUS=8 bash scripts/02_run_t2v_a14b.sh
```

**Route 3 — I2V-A14B (max consistency across seeds)**

```bash
CKPT_DIR=~/models/Wan2.2-I2V-A14B GPUS=8 START_FRAME=keyframes/kf01_tunnel.png \
  bash scripts/03_run_i2v_a14b.sh
```

Then roll seeds and pick:

```bash
SEEDS="20261031 20261101 7 42 1234 9001" bash scripts/05_sweep_seeds.sh
```

### Expected cost per 5 s take (rough, adjust to your hardware)

| Route | Frames / fps | Steps | Hardware | Wall clock |
|---|---|---|---|---|
| TI2V-5B 704×1280 | 121 @ 24 | 50 | 1× 4090 24 GB, `--offload_model True --t5_cpu` | ~10–20 min |
| TI2V-5B 704×1280 | 121 @ 24 | 30 (preview) | 1× 4090 | ~6–12 min |
| T2V-A14B 720×1280 | 81 @ 16 | 40 | 8× H100 / A100 | ~5–10 min |
| I2V-A14B 720×1280 | 81 @ 16 | 40 | 8× H100 / A100 | ~5–10 min |

Drop `--sample_steps 50 → 30` while blocking the move; go back to 50 for the keeper.

## Aspect ratio — why the sizes are what they are

Wan2.2 has no aspect-ratio token; vertical framing comes purely from `--size`. From
`wan/configs/__init__.py`:

| Task | Vertical sizes | Ratio | Note |
|---|---|---|---|
| `t2v-A14B`, `i2v-A14B` | `720*1280` | 0.5625 | **exact 9:16** |
| `ti2v-5B` | `704*1280` | 0.5500 | 2.2 % narrower than 9:16 → cropped in step 04 |

`04_postprocess_9x16.sh` crops 704×1280 → 704×1252 (0.5623 ≈ 9:16) before scaling to 1080×1920, so
there is no stretch on arches or faces. A14B takes go straight to 1080×1920.

## Delivery master

```bash
bash scripts/04_postprocess_9x16.sh out/ti2v5b_704x1280_s20261031.mp4
# -> out/ti2v5b_704x1280_s20261031_1080x1920_9x16.mp4  (H.264, CRF 18, faststart, no audio)
```

Adds a light contrast/warm-lamp grade, micro-sharpen for the stone, and fine film grain
(`GRAIN=0` and `SKIP_GRADE=1` to disable). A14B takes are 16 fps — pass `FPS=24` to retime.

## Prompt

`prompt.md` holds the master prompt, the I2V motion-only variant, the extra negative terms, and the
reasoning behind the wording (one clear move, a reveal verb for scale, lamp/haze vocabulary that
survives diffusion). Keep the prompt one dense paragraph of ~120–170 words — that is what Wan2.2
encodes best.
