#!/usr/bin/env bash
# Shot 02 — "The Lantern" (the explorer walking the tunnel)
# Single-GPU route. Wan2.2 TI2V-5B at 704*1280, 121 frames @ 24 fps (5.04 s).
# Use I2V (START_FRAME=...) — text-only TI2V will invent a different man per seed.
#
#   START_FRAME=keyframes/kf01_walk.png bash scripts/02_run_ti2v_5b.sh
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)}"
PROJ_DIR="${PROJ_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

CKPT_DIR="${CKPT_DIR:-$REPO_ROOT/Wan2.2-TI2V-5B}"
START_FRAME="${START_FRAME:-$PROJ_DIR/keyframes/kf01_walk.png}"
PROMPT_FILE="${PROMPT_FILE:-$PROJ_DIR/prompt_motion.txt}"
SIZE="${SIZE:-704*1280}"          # the only vertical size TI2V-5B supports
SEED="${SEED:-20261031}"
OUT_DIR="${OUT_DIR:-$PROJ_DIR/out}"
FRAMES="${FRAMES:-121}"           # 4n+1 -> 121 @ 24 fps = 5.04 s
STEPS="${STEPS:-50}"
GUIDE="${GUIDE:-5.0}"

mkdir -p "$OUT_DIR"
TAG="ti2v5b_$(basename "${START_FRAME%.*}")_s${SEED}"
OUT_FILE="${OUT_FILE:-$OUT_DIR/${TAG}.mp4}"
PROMPT="$(tr '\n' ' ' < "$PROMPT_FILE" | sed 's/  */ /g')"

echo ">> task=ti2v-5B start=$START_FRAME size=$SIZE frames=$FRAMES seed=$SEED -> $OUT_FILE"
python "$REPO_ROOT/generate.py" \
  --task ti2v-5B \
  --size "$SIZE" \
  --ckpt_dir "$CKPT_DIR" \
  --image "$START_FRAME" \
  --frame_num "$FRAMES" \
  --sample_steps "$STEPS" \
  --sample_guide_scale "$GUIDE" \
  --sample_solver unipc \
  --base_seed "$SEED" \
  --offload_model True \
  --convert_model_dtype \
  --t5_cpu \
  --save_file "$OUT_FILE" \
  --prompt "$PROMPT"

echo ">> done: $OUT_FILE"
echo ">> delivery master: bash scripts/04_postprocess_9x16.sh \"$OUT_FILE\""
