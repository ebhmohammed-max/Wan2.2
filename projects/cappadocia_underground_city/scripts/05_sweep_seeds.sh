#!/usr/bin/env bash
# Shot 01 — Cappadocia underground city
# Roll N takes with different seeds, then keep the one where the carved steps and
# archways read cleanly. Walls/stairs deform first when a seed is bad.
#
#   SEEDS="20261031 20261101 7 42 1234 9001" bash scripts/05_sweep_seeds.sh
#   START_FRAME=keyframes/kf01_tunnel.png SEEDS="11 22 33" bash scripts/05_sweep_seeds.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEEDS="${SEEDS:-20261031 20261101 7 42 1234 9001}"

for s in $SEEDS; do
  echo "== seed $s =="
  SEED="$s" bash "$HERE/01_run_ti2v_5b.sh"
done

echo
echo "Take summary (size / duration):"
for f in "$HERE"/../out/*.mp4; do
  [ -e "$f" ] || continue
  printf '%s  %s\n' "$(du -h "$f" | cut -f1)" "$(basename "$f")"
done
