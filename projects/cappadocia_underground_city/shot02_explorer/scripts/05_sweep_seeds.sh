#!/usr/bin/env bash
# Shot 02 — roll takes and pick the one with clean hands and a stable face.
# Faces and lantern fingers are the first things to break on a walking shot, so
# keep this sweep narrow (3–4 seeds) and watch the hands at frame ~40.
#
#   SEEDS="20261031 7 42 1234" GPUS=8 bash scripts/05_sweep_seeds.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEEDS="${SEEDS:-20261031 7 42 1234}"
RUNNER="${RUNNER:-$HERE/01_run_i2v_a14b.sh}"

for s in $SEEDS; do
  echo "== seed $s =="
  SEED="$s" bash "$RUNNER"
done

echo
echo "Take summary:"
for f in "$HERE"/../out/*.mp4; do
  [ -e "$f" ] || continue
  printf '%s  %s\n' "$(du -h "$f" | cut -f1)" "$(basename "$f")"
done
