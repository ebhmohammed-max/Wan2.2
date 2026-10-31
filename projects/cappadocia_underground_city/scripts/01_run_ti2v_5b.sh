#!/usr/bin/env bash
# Shot 01 — Cappadocia underground city
# Primary path: Wan2.2 TI2V-5B, vertical 9:16, 121 frames @ 24 fps (5.04 s per take).
# Fits a single 24 GB consumer card (RTX 4090) with model offload.
#
#   bash scripts/01_run_ti2v_5b.sh                 # text-to-video take
#   START_FRAME=keyframes/kf01_tunnel.png bash scripts/01_run_ti2v_5b.sh   # image-to-video from keyframe
#   SEED=42 PROMPT_FILE=prompt_motion.txt bash scripts/01_run_ti2v_5b.sh
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)}"
PROJ_DIR="${PROJ_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

CKPT_DIR="${CKPT_DIR:-$REPO_ROOT/Wan2.2-TI2V-5B}"        # the 5B checkpoint dir
PROMPT_FILE="${PROMPT_FILE:-$PROJ_DIR/prompt_master.txt}"
SEED="${SEED:-20261031}"
OUT_DIR="${OUT_DIR:-$PROJ_DIR/out}"
SIZE="${SIZE:-704*1280}"                                  # only vertical size TI2V-5B supports
FRAMES="${FRAMES:-121}"                                   # 4n+1 -> 121 @ 24 fps = 5.04 s
STEPS="${STEPS:-50}"
GUIDE="${GUIDE:-5.0}"
START_FRAME="${START_FRAME:-}"                            # optional: first-frame image

mkdir -p "$OUT_DIR"
TAG="ti2v5b_${SIZE//\*/x}_s${SEED}$([ -n "$START_FRAME" ] && echo "_i2v")"
OUT_FILE="${OUT_FILE:-$OUT_DIR/${TAG}.mp4}"

PROMPT="$(tr '\n' ' ' < "$PROMPT_FILE" | sed 's/  */ /g')"

EXTRA=()
if [[ -n "$START_FRAME" ]]; then
  EXTRA+=(--image "$(cd "$PROJ_DIR" && realpath -m "$START_FRAME")")
fi

echo ">> task=ti2v-5B size=$SIZE frames=$FRAMES seed=$SEED -> $OUT_FILE"
python "$REPO_ROOT/generate.py" \
  --task ti2v-5B \
  --size "$SIZE" \
  --ckpt_dir "$CKPT_DIR" \
  --frame_num "$FRAMES" \
  --sample_steps "$STEPS" \
  --sample_guide_scale "$GUIDE" \
  --sample_solver unipc \
  --base_seed "$SEED" \
  --offload_model True \
  --convert_model_dtype \
  --t5_cpu \
  --save_file "$OUT_FILE" \
  "${EXTRA[@]}" \
  --prompt "$PROMPT"

echo ">> done: $OUT_FILE"
echo ">> exact 9:16 master: bash scripts/04_postprocess_9x16.sh \"$OUT_FILE\""
