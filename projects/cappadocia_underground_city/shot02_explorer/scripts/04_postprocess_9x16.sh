#!/usr/bin/env bash
# Shot 02 shares the delivery chain with shot 01: exact 9:16 1080x1920, grade,
# micro-sharpen, film grain, H.264 CRF 19 faststart. Thin wrapper so there is
# only one implementation of the crop/grade maths in this project.
#
#   bash scripts/04_postprocess_9x16.sh out/i2v14b_kf01_walk_s20261031.mp4
#   GRAIN=0 SKIP_GRADE=1 FPS=24 bash scripts/04_postprocess_9x16.sh raw.mp4
set -euo pipefail
exec bash "$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/scripts/04_postprocess_9x16.sh" "$@"
