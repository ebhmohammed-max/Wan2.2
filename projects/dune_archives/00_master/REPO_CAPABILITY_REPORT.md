# THE DUNE ARCHIVES — Repo & Environment Capability Report (v1.0 — 2026-11-23)

**Repo:** `ebhmohammed-max/Wan2.2`
**Branch:** `arena/e01ea136-wan2-2` (base `a0070b8`)
**Basis:** everything below was inspected and run in this sandbox. "Tested" means the agent executed it here.

## 1. Environment (measured)

| Item | Status |
|---|---|
| CPU / RAM / disk | 2 vCPU · ~3 GB RAM · ~20 GB free |
| GPU | **None** (`nvidia-smi` absent) |
| Python | 3.11.2. The system pip is PEP-668-locked, so the project uses the venv `/home/user/.venv-dune` (numpy, pillow, imageio, imageio-ffmpeg, matplotlib, openpyxl) |
| ffmpeg | No system binary. The imageio-ffmpeg bundled binary (v9.0.2 build) works |
| ImageMagick | `convert` present |
| Torch / Wan2.2 weights | **Not installed / not present** |

## 2. What the repo contains

| Component | Path | Capability | Usable here? |
|---|---|---|---|
| Wan2.2 model code | `generate.py`, `wan/` | Text-to-video / image-to-video / TI2V (A14B MoE, 5B) | **No.** Needs a CUDA GPU (≥24 GB for the 5B at 720p, multi-GPU for A14B), torch, flash-attn and ~tens of GB of weights |
| Wan2.2 render scripts | `projects/cappadocia_underground_city/scripts/01–05_*.sh` | Wrappers for TI2V-5B / T2V-A14B / I2V-A14B, post-process, seed sweeps | Only on an external GPU host. They can be reused as-is with Dune prompts |
| Still mastering | `projects/atlas_understory/scripts/make_stills.py` | 1376×768 → 3840×2160 master (crop, Lanczos, unsharp, grain, vignette) | **Yes** (CPU) |
| Still-to-clip motion | `projects/atlas_understory/scripts/make_clips.py` | 1080p 24 fps H.264: pull-out, 3-plane parallax, crossfade | **Yes** (CPU) |
| 9:16 animatics | `projects/cappadocia_underground_city/previz/previz_lib.py` | Push-ins, shake, dust, lantern flicker, grain | **Yes** (CPU) |
| ASOIAF pipeline template | `projects/ancient_world_of_ice_and_fire/` | Research → script → scene CSV/JSON → 10-image batch manifests → QC → YouTube package → storyboard HTML | **Yes**, as a structural template (not modified) |
| Art-direction method | `studio/2wulffs-playbook.md` | Decision grid and ALWAYS/NEVER rules | Applied in the Visual Style Bible |

## 3. New Dune tooling built this session (tested)

| Tool | Path | What it does | Test result |
|---|---|---|---|
| Motion engine | `projects/dune_archives/tools/motion_engine.py` | 16:9 1080p24 H.264 shots from one still. 10 recipes: PUSH_IN, PULL_OUT, PAN_LR/RL, TILT_UP/DN, PARALLAX, DRIFT, WORM_RISE, HOLD. Optional sand particles, heat shimmer, light sweep, shake, 2.39 letterbox, grade. Manifest batch mode | Rendered WORM_RISE + sand + heat + lightsweep + letterbox, and PARALLAX, on a synthetic plate. ~0.5–0.6 s/frame on 2 vCPU |
| Map animator | `projects/dune_archives/tools/map_animator.py` | JSON-driven animated maps in 4 styles (imperial, noir, political, arrakis). Node reveals with pulse, glowing routes with a comet head, territories, typed labels, slow push. Canon-ring styling per node. **Mandatory provenance caption** ("Schematic reconstruction…") | Rendered the 12 s template `templates/maps/MAP_TEMPLATE_imperial_routes.json`. Fixed a bug where the title was cropped by the push (overlays are now screen-space). ~0.65 s/frame |
| Database builder | `projects/dune_archives/tools/build_databases.py` | Regenerates every lore DB, the topic bank (CSV/JSON/MD/XLSX) and the hook library from `data/*.py` | Runs in <1 s |

**Render-time budget (CPU, this sandbox):** about 3.5–4 CPU-hours per 10 minutes of finished motion at 1080p. Feasible overnight. Faster with x264 `veryfast` or on a bigger machine.

## 4. What is NOT available (honest limits)

- **Video generation (Wan2.2):** not possible here. It needs an external GPU machine; the scripts exist.
- **Image generation:** not run this session, by instruction (no images until topic and quantity are approved).
- **TTS / voice-over and music generation:** no TTS tool was confirmed in the repo for this pipeline. VO must come from the creator, an external TTS, or a session voice tool if approved later. **SFX library:** none in the repo.
- **YouTube Analytics / Data API:** not connected. All "search demand" scores are editorial estimates.
- **Primary texts:** the novels are not available in the sandbox, so `[VERIFY]` flags must be page-checked by a human or a licensed e-book.
- **Fandom / Wikipedia:** blocked from this sandbox (fetch failures).

## 5. Recommended production path (per episode)

1. Script + storyboard CSV (templates in `17_templates` / `18_storyboards`).
2. UNIQUE shot list → batches of at most 10 images → generation (after approval) → `19_IMAGE_GENERATION_BATCHES`.
3. QC against the Visual Style Bible checklist.
4. `make_stills.py` (4K masters) → `motion_engine.py` (shots) + `map_animator.py` (maps).
5. ffmpeg assembly + VO + music/SFX → `22_VIDEO_PROJECTS` → `23_FINAL_EXPORTS`.
6. Optional hero shots: Wan2.2 I2V on an external GPU from approved stills, using the Cappadocia scripts.
