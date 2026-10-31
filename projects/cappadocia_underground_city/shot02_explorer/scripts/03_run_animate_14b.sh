#!/usr/bin/env bash
# Shot 02 — "The Lantern" (the explorer walking the tunnel)
# OPTIONAL, performance-driven route: Wan2.2-Animate-14B in animation mode.
# Use this when I2V loses the gait — feed a real walking reference clip (vertical,
# full-body, single person, camera moving backward) and let Animate retarget the
# motion onto the explorer identity still. Closest thing to "real walking" in Wan2.2.
#
#   REF_VIDEO=/path/walk_reference_9x16.mp4 GPUS=8 bash scripts/03_run_animate_14b.sh
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)}"
PROJ_DIR="${PROJ_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

CKPT_DIR="${CKPT_DIR:-$REPO_ROOT/Wan2.2-Animate-14B}"
REF_VIDEO="${REF_VIDEO:?set REF_VIDEO to a walking reference clip (mp4)}"
REF_IMAGE="${REF_IMAGE:-$PROJ_DIR/keyframes/kf01_walk.png}"
PROC_DIR="${PROC_DIR:-$PROJ_DIR/out/animate_process}"
GPUS="${GPUS:-8}"
SEED="${SEED:-20261031}"
OUT_DIR="${OUT_DIR:-$PROJ_DIR/out}"
OUT_FILE="${OUT_FILE:-$OUT_DIR/animate14b_explorer_s${SEED}.mp4}"

mkdir -p "$PROC_DIR" "$OUT_DIR"

echo ">> (1/2) preprocessing reference motion -> $PROC_DIR"
python "$REPO_ROOT/wan/modules/animate/preprocess/preprocess_data.py" \
  --ckpt_path "$CKPT_DIR/process_checkpoint" \
  --video_path "$REF_VIDEO" \
  --refer_path "$REF_IMAGE" \
  --save_path "$PROC_DIR" \
  --resolution_area 704 1280 \
  --retarget_flag \
  --use_flux

echo ">> (2/2) animate-14B (animation mode) -> $OUT_FILE"
python -m torch.distributed.run --nproc_per_node="$GPUS" "$REPO_ROOT/generate.py" \
  --task animate-14B \
  --ckpt_dir "$CKPT_DIR" \
  --src_root_path "$PROC_DIR" \
  --refert_num 1 \
  --base_seed "$SEED" \
  --save_file "$OUT_FILE" \
  --prompt "The man in the video walks slowly through the tunnel."

echo ">> done: $OUT_FILE"
echo ">> delivery master: bash scripts/04_postprocess_9x16.sh \"$OUT_FILE\""
