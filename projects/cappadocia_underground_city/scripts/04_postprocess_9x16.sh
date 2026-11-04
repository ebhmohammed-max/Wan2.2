#!/usr/bin/env bash
# Shot 01 — Cappadocia underground city
# Turn a raw Wan2.2 take into a delivery-ready vertical master: 1080x1920, exact 9:16,
# 24 fps, yuv420p, faststart, light cinematic finish.
#
#   bash scripts/04_postprocess_9x16.sh out/ti2v5b_704x1280_s20261031.mp4
#   GRAIN=0 SKIP_GRADE=1 bash scripts/04_postprocess_9x16.sh raw.mp4   # clean pass
#
# Why the crop: TI2V-5B only supports 704x1280 (ratio 0.5500, i.e. 2.2 % narrower than
# 9:16). Cropping 1280 -> 1252 px of height gives 704x1252 = 0.5623, which scales to
# 1080x1920 with a 0.04 % aspect error — visually zero, and no stretch on faces/arches.
# T2V/I2V-A14B output 720x1280 and is already exact 9:16 (no crop applied).
set -euo pipefail

IN="${1:?usage: 04_postprocess_9x16.sh <input.mp4> [output.mp4]}"
NAME="$(basename "${IN%.*}")"
OUT="${2:-$(dirname "$IN")/${NAME}_1080x1920_9x16.mp4}"

GRAIN="${GRAIN:-6}"          # film-grain strength (0 disables; grain is expensive in bitrate)
SKIP_GRADE="${SKIP_GRADE:-0}"
FPS="${FPS:-0}"              # 0 = keep source fps; 24 = retime (A14B takes are 16 fps)

FFMPEG="${FFMPEG:-ffmpeg}"
command -v "$FFMPEG" >/dev/null || {
  echo "ffmpeg not on PATH. Try: FFMPEG=\$(python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')" >&2
  exit 1
}

# ffmpeg exits non-zero when no output file is given, hence the `|| true`
INFO=$("$FFMPEG" -hide_banner -i "$IN" 2>&1 || true)
WH=$(printf '%s\n' "$INFO" | sed -n 's/.*Video: .*, \([0-9]\{2,5\}\)x\([0-9]\{2,5\}\)[ ,].*/\1x\2/p' | head -1)
[ -n "$WH" ] || { echo "could not read video dimensions from $IN" >&2; exit 1; }
W="${WH%x*}"
H="${WH#*x}"
echo ">> source: ${W}x${H}"

VF=""
# --- vertical 9:16 frame -----------------------------------------------------
if [ "$W" = "704" ] && [ "$H" = "1280" ]; then
  VF="crop=704:1252:0:14"
fi
VF="${VF:+$VF,}scale=1080:1920:flags=lanczos,setsar=1"

# --- optional retime to 24 fps ----------------------------------------------
if [ "$FPS" = "24" ]; then
  VF="$VF,fps=24"
fi

# --- cinematic finish --------------------------------------------------------
if [ "$SKIP_GRADE" = "0" ]; then
  # gentle contrast + warm lamp bias + tiny lift, then micro-sharpen the stone texture
  VF="$VF,eq=contrast=1.06:brightness=0.008:saturation=1.02:gamma=1.02,colorbalance=rs=.02:bs=-.02:rm=.015:bm=-.015,unsharp=5:5:0.35:5:5:0.0"
fi
if [ "$GRAIN" != "0" ]; then
  VF="$VF,noise=alls=${GRAIN}:allf=t+u"
fi
VF="$VF,format=yuv420p"

echo ">> writing $OUT"
"$FFMPEG" -y -hide_banner -loglevel warning -i "$IN" \
  -vf "$VF" \
  -c:v libx264 -profile:v high -crf 19 -preset slow -tune film \
  -pix_fmt yuv420p -movflags +faststart -an \
  "$OUT"

echo ">> ok: $OUT"
"$FFMPEG" -hide_banner -i "$OUT" 2>&1 | grep -E "Duration|Stream" || true
