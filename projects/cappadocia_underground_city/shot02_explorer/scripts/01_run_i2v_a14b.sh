#!/usr/bin/env bash
# Shot 02 — "The Lantern" (the explorer walking the tunnel)
# PRIMARY route. Wan2.2 I2V-A14B started from the identity keyframe, so the face,
# clothing and lamplight stay locked while the walking motion is generated.
# 720*1280 is exact 9:16; 81 frames @ 16 fps = 5.06 s.
#
#   GPUS=8 bash scripts/01_run_i2v_a14b.sh
#   START_FRAME=keyframes/kf03_stride.png SEED=42 GPUS=8 bash scripts/01_run_i2v_a14b.sh
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)}"
PROJ_DIR="${PROJ_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

CKPT_DIR="${CKPT_DIR:-$REPO_ROOT/Wan2.2-I2V-A14B}"
START_FRAME="${START_FRAME:-$PROJ_DIR/keyframes/kf01_walk.png}"
PROMPT_FILE="${PROMPT_FILE:-$PROJ_DIR/prompt_motion.txt}"
SIZE="${SIZE:-720*1280}"          # I2V follows the image's 9:16 aspect; size sets the area
SEED="${SEED:-20261031}"
OUT_DIR="${OUT_DIR:-$PROJ_DIR/out}"
FRAMES="${FRAMES:-81}"            # 81 @ 16 fps = 5.06 s ≈ three unhurried steps
STEPS="${STEPS:-40}"
GPUS="${GPUS:-8}"
OFFLOAD="${OFFLOAD:-}"

mkdir -p "$OUT_DIR"
TAG="i2v14b_$(basename "${START_FRAME%.*}")_s${SEED}"
OUT_FILE="${OUT_FILE:-$OUT_DIR/${TAG}.mp4}"
PROMPT="$(tr '\n' ' ' < "$PROMPT_FILE" | sed 's/  */ /g')"

EXTRA=()
[[ -n "$OFFLOAD" ]] && EXTRA+=(--offload_model "$OFFLOAD")

echo ">> task=i2v-A14B start=$START_FRAME size=$SIZE frames=$FRAMES seed=$SEED gpus=$GPUS -> $OUT_FILE"
python -m torch.distributed.run --nproc_per_node="$GPUS" "$REPO_ROOT/generate.py" \
  --task i2v-A14B \
  --size "$SIZE" \
  --ckpt_dir "$CKPT_DIR" \
  --image "$START_FRAME" \
  --frame_num "$FRAMES" \
  --sample_steps "$STEPS" \
  --sample_solver unipc \
  --base_seed "$SEED" \
  "${EXTRA[@]}" \
  --save_file "$OUT_FILE" \
  --prompt "$PROMPT"

echo ">> done: $OUT_FILE"
echo ">> delivery master: bash scripts/04_postprocess_9x16.sh \"$OUT_FILE\""
