#!/usr/bin/env python3
"""Shot 01 previz — the empty tunnel reveal, 9:16 cinematic animatic.

NOT Wan2.2 output. Three keyframes on one eased dolly-in (1.00 -> 1.16) with
1 s crossfades, dust with depth parallax, warm low-key grade, vignette, grain.
1080x1920 @ 24 fps, 16 s, H.264 yuv420p. Shared code lives in ../previz/previz_lib.py

Usage:  python previz/render_previz.py [--out previz/cappadocia_previz_9x16.mp4]
"""
import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from previz_lib import (FPS, H, W, build_dust, camera_frame, composite,  # noqa: E402
                        dust_layer, load_plate, make_writer, smoothstep)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SHOT_FRAMES = 6 * FPS      # 6 s per beat
XFADE = 1 * FPS            # 1 s crossfades
BEATS = [                  # (file, downward drift through the beat)
    ("kf01_tunnel.png", 0.00),
    ("kf02_chamber_reveal.png", 0.05),
    ("kf03_deep_hall.png", 0.10),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "cappadocia_previz_9x16.mp4"))
    ap.add_argument("--limit", type=int, default=0, help="render only N frames (smoke test)")
    args = ap.parse_args()

    plates = []
    for name, _ in BEATS:
        plates.append(load_plate(os.path.join(ROOT, "keyframes", name)))
        print(f"plate ready: {name} -> {plates[-1].size}")

    total = SHOT_FRAMES * len(plates) - XFADE * (len(plates) - 1)
    if args.limit:
        total = min(total, args.limit)
    print(f"rendering {total} frames ({total / FPS:.2f}s) at {W}x{H}@{FPS}")

    dust = build_dust()
    rng = np.random.default_rng(11)
    writer = make_writer(args.out)
    try:
        for i in range(total):
            acc = np.zeros((H, W, 3), dtype=np.float32)
            wsum = 0.0
            for k, (_, dy_bias) in enumerate(BEATS):
                local = i - k * (SHOT_FRAMES - XFADE)
                if local < 0 or local >= SHOT_FRAMES:
                    continue
                wgt = 1.0
                if k > 0 and local < XFADE:
                    wgt *= smoothstep(local / XFADE)
                if k < len(BEATS) - 1 and local >= SHOT_FRAMES - XFADE:
                    wgt *= smoothstep((SHOT_FRAMES - 1 - local) / XFADE)
                if wgt <= 0:
                    continue
                fr = camera_frame(plates[k], zoom_to=1.16, t=local / (SHOT_FRAMES - 1), dy=0.012 + dy_bias)
                acc += np.asarray(fr, dtype=np.float32) * wgt
                wsum += wgt
            acc = acc / wsum if wsum > 0 else np.asarray(plates[0].resize((W, H)), dtype=np.float32)

            out = composite(acc, dust_layer(dust, i, min(i / max(total, 1), 1.0)), i, rng)
            writer.append_data(out)
            if i % 24 == 0:
                print(f"  frame {i}/{total}", flush=True)
    finally:
        writer.close()

    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
