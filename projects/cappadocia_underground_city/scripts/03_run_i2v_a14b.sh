#!/usr/bin/env bash
# Shot 01 — Cappadocia underground city
# Image-to-video path: locks the tunnel framing to keyframes/kf01_tunnel.png and lets
# Wan2.2 I2V-A14B animate the dolly forward. Best consistency across a seed sweep,
# because every take starts from the exact same composition.
#
#   START_FRAME=keyframes/kf01_tunnel.png GPUS=8 bash scripts/03_run_i2v_a14b.sh
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)}"
PROJ_DIR="${PROJ_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

CKPT_DIR="${CKPT_DIR:-$REPO_ROOT/Wan2.2-I2V-A14B}"
START_FRAME="${START_FRAME:-$PROJ_DIR/keyframes/kf01_tunnel.png}"
# I2V output aspect follows the input image; announce the 9:16 area explicitly.
SIZE="${SIZE:-720*1280}"
PROMPT_FILE="${PROMPT_FILE:-$(dirname "$0")/../prompt_motion.txt}"
SEED="${SEED:-20261031}"
OUT_DIR="${OUT_DIR:-$PROJ_DIR/out}"
FRAMES="${FRAMES:-81}"
STEPS="${STEPS:-40}"
GPUS="${GPUS:-8}"

mkdir -p "$OUT_DIR"
TAG="i2v14b_$(basename "${START_FRAME%.*}")_s${SEED}"
OUT_FILE="${OUT_FILE:-$OUT_DIR/${TAG}.mp4}"
PROMPT="$(tr '\n' ' ' < "$PROMPT_FILE" | sed 's/  */ /g')"

echo ">> task=i2v-A14B start=$START_FRAME size=$SIZE frames=$FRAMES seed=$SEED -> $OUT_FILE"
python -m torch.distributed.run --nproc_per_node="$GPUS" "$REPO_ROOT/generate.py" \
  --task i2v-A14B \
  --size "$SIZE" \
  --ckpt_dir "$CKPT_DIR" \
  --image "$START_FRAME" \
  --frame_num "$FRAMES" \
  --sample_steps "$STEPS" \
  --sample_solver unipc \
  --base_seed "$SEED" \
  --save_file "$OUT_FILE" \
  --prompt "$PROMPT"

echo ">> done: $OUT_FILE"
echo ">> delivery master: bash scripts/04_postprocess_9x16.sh \"$OUT_FILE\""
