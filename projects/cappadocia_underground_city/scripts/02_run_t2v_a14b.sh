#!/usr/bin/env bash
# Shot 01 — Cappadocia underground city
# Highest-quality path: Wan2.2 T2V-A14B (MoE high/low noise experts), native 9:16.
# 720*1280 is an exact 9:16 frame; 81 frames @ 16 fps = 5.06 s per take.
#
# Multi-GPU (recommended, 8x A/H100):
#   GPUS=8 bash scripts/02_run_t2v_a14b.sh
# Single GPU with sequential expert offload (slow but works on ~48-80 GB):
#   GPUS=1 OFFLOAD=True bash scripts/02_run_t2v_a14b.sh
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)}"
PROJ_DIR="${PROJ_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

CKPT_DIR="${CKPT_DIR:-$REPO_ROOT/Wan2.2-T2V-A14B}"
PROMPT_FILE="${PROMPT_FILE:-$PROJ_DIR/prompt_master.txt}"
SEED="${SEED:-20261031}"
OUT_DIR="${OUT_DIR:-$PROJ_DIR/out}"
SIZE="${SIZE:-720*1280}"          # exact 9:16 (W*H)
FRAMES="${FRAMES:-81}"            # 4n+1 -> 81 @ 16 fps = 5.06 s
STEPS="${STEPS:-40}"
GPUS="${GPUS:-8}"
OFFLOAD="${OFFLOAD:-}"

mkdir -p "$OUT_DIR"
TAG="t2v14b_${SIZE//\*/x}_s${SEED}"
OUT_FILE="${OUT_FILE:-$OUT_DIR/${TAG}.mp4}"
PROMPT="$(tr '\n' ' ' < "$PROMPT_FILE" | sed 's/  */ /g')"

EXTRA=()
[[ -n "$OFFLOAD" ]] && EXTRA+=(--offload_model "$OFFLOAD")

echo ">> task=t2v-A14B size=$SIZE frames=$FRAMES seed=$SEED gpus=$GPUS -> $OUT_FILE"
python -m torch.distributed.run --nproc_per_node="$GPUS" "$REPO_ROOT/generate.py" \
  --task t2v-A14B \
  --size "$SIZE" \
  --ckpt_dir "$CKPT_DIR" \
  --frame_num "$FRAMES" \
  --sample_steps "$STEPS" \
  --sample_solver unipc \
  --base_seed "$SEED" \
  "${EXTRA[@]}" \
  --save_file "$OUT_FILE" \
  --prompt "$PROMPT"

echo ">> done: $OUT_FILE"
echo ">> delivery master: bash scripts/04_postprocess_9x16.sh \"$OUT_FILE\""
