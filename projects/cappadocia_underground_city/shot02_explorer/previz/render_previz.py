#!/usr/bin/env python3
"""Shot 02 previz — the explorer walking the tunnel, 9:16 walking animatic.

NOT Wan2.2 output. Four keyframes of the same man (generated as edits of one
reference frame, so identity/clothing/light stay locked) cut on 0.5 s crossfades
and driven with:

  * a continuous slow push (1.02 -> 1.06, subject approaches faster than the
    camera retreats, so he grows slightly in frame),
  * a procedural walk bob — vertical weight shift + a quarter-degree roll at
    ~1.55 Hz, which is what makes a still-frame animatic read as *walking*,
  * lantern flicker: an additive amber bloom with irregular 0.75..1.25 intensity
    plus a global ±1.5 % exposure tremble,
  * the shot-01 finish: warm low-key grade, haze, dust, vignette, film grain.

1080x1920 @ 24 fps, ~5.2 s (matches a 121-frame TI2V-5B take), H.264 yuv420p.

Usage:  python previz/render_previz.py [--out previz/shot02_previz_9x16.mp4]
"""
import argparse
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIB = os.path.abspath(os.path.join(HERE, "..", "..", "previz"))
sys.path.insert(0, LIB)

from previz_lib import (FPS, H, W, build_dust, camera_frame, composite,  # noqa: E402
                        dust_layer, flicker_at, glow_layer, load_plate,
                        make_writer, smoothstep)

# beat: (keyframe, first frame, shots length, lantern glow spec (x, y, radius))
LAMP_A = (0.700, 0.680, 0.30)     # lantern held low at frame right (full-body beats)
LAMP_B = (0.845, 0.880, 0.34)     # lantern pushed to the frame edge (closer beat)
BEATS = [
    dict(kf="kf01_walk.png", start=0, length=40, lamp=LAMP_A),
    dict(kf="kf02_step.png", start=28, length=40, lamp=LAMP_A),
    dict(kf="kf03_stride.png", start=56, length=40, lamp=LAMP_A),
    dict(kf="kf04_close.png", start=88, length=36, lamp=LAMP_B),
]
XFADES = [12, 12, 8]              # per boundary; the last one cuts hard on purpose
WALK_HZ = 1.55
BOB_PX = 6.0                      # vertical weight shift, master pixels
ROLL_DEG = 0.28                   # subtle shoulder roll


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "shot02_previz_9x16.mp4"))
    ap.add_argument("--limit", type=int, default=0, help="render only N frames (smoke test)")
    args = ap.parse_args()

    plates = {}
    for b in BEATS:
        plates[b["kf"]] = load_plate(os.path.join(ROOT, "keyframes", b["kf"]))
        print(f"plate ready: {b['kf']} -> {plates[b['kf']].size}")

    total = max(b["start"] + b["length"] for b in BEATS)
    if args.limit:
        total = min(total, args.limit)
    print(f"rendering {total} frames ({total / FPS:.2f}s) at {W}x{H}@{FPS}")

    dust = build_dust(n=90, seed=23)
    rng = np.random.default_rng(5)
    writer = make_writer(args.out)
    try:
        for i in range(total):
            t_sec = i / FPS
            # walk bob, continuous across the cuts so it never pops
            bob = BOB_PX * math.sin(2 * math.pi * WALK_HZ * t_sec)
            bob += 1.6 * math.sin(2 * math.pi * WALK_HZ * 2 * t_sec + 0.9)
            roll = ROLL_DEG * math.sin(2 * math.pi * WALK_HZ * t_sec - 0.4)
            push = 1.02 + 0.04 * (i / max(total, 1))

            acc = np.zeros((H, W, 3), dtype=np.float32)
            wsum = 0.0
            lamp = None
            for k, b in enumerate(BEATS):
                local = i - b["start"]
                if local < 0 or local >= b["length"]:
                    continue
                wgt = 1.0
                if k > 0:
                    x = XFADES[k - 1]
                    if local < x:
                        wgt *= smoothstep(local / x)
                if k < len(BEATS) - 1:
                    x = XFADES[k]
                    if local >= b["length"] - x:
                        wgt *= smoothstep((b["length"] - 1 - local) / x)
                if wgt <= 0:
                    continue
                fr = camera_frame(plates[b["kf"]], zoom_to=push, t=1.0, dy=0.0,
                                  roll_deg=roll, shake_px=bob)
                acc += np.asarray(fr, dtype=np.float32) * wgt
                wsum += wgt
                lamp = b["lamp"] if wgt > 0.5 else (lamp or b["lamp"])
            acc = acc / wsum if wsum > 0 else np.asarray(plates[BEATS[0]["kf"]].resize((W, H)), dtype=np.float32)

            glow = glow_layer(lamp, t_sec)
            if glow is not None:
                acc = acc * flicker_at(t_sec, seed=1) ** 0.6   # exposure tremble
            out = composite(acc, dust_layer(dust, i, 0.4), i, rng, glow=glow)
            writer.append_data(out)
            if i % 24 == 0:
                print(f"  frame {i}/{total}", flush=True)
    finally:
        writer.close()

    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
