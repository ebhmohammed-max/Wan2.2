#!/usr/bin/env python3
"""Atlas Understory — still mastering.

Takes the raw generated PNG (1376x768) and produces the deliverable
3840x2160 16:9 master:
  - centre-crop to exact 16:9
  - Lanczos upscale to 3840x2160
  - gentle detail unsharp (radius 2.0, 55 %, threshold 3)
  - fine monochrome grain (sigma 2.2) to keep the upscale from looking plastic
  - very subtle vignette (-6 % at corners)

No text, letters, logos or captions are added at any point.
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageFilter

W, H = 3840, 2160
SRC = pathlib.Path(__file__).resolve().parents[1] / "stills" / "batch0_src"
DST = pathlib.Path(__file__).resolve().parents[1] / "stills" / "batch0"


def master(src: pathlib.Path, dst: pathlib.Path) -> None:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    # centre crop to exact 16:9
    target_w = int(round(h * 16 / 9))
    if target_w <= w:
        left = (w - target_w) // 2
        im = im.crop((left, 0, left + target_w, h))
    else:
        target_h = int(round(w * 9 / 16))
        top = (h - target_h) // 2
        im = im.crop((0, top, w, top + target_h))

    im = im.resize((W, H), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=2.0, percent=55, threshold=3))

    a = np.asarray(im).astype(np.float32)
    # vignette: 1.0 centre -> 0.94 corners
    ys = np.linspace(-1, 1, H, dtype=np.float32)[:, None]
    xs = np.linspace(-1, 1, W, dtype=np.float32)[None, :]
    r = np.sqrt(xs ** 2 + ys ** 2) / np.sqrt(2.0)
    vig = 1.0 - 0.06 * (r ** 2.2)
    a *= vig[..., None]
    # fine grain
    rng = np.random.default_rng(7)
    grain = rng.normal(0.0, 2.2, (H, W, 1)).astype(np.float32)
    a += grain
    a = np.clip(a, 0, 255).astype(np.uint8)
    Image.fromarray(a).save(dst, "PNG", optimize=True)
    print(f"mastered {src.name} -> {dst.name} ({W}x{H})")


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    names = sys.argv[1:] or sorted(p.stem.replace("_raw", "") for p in SRC.glob("*_raw.png"))
    for n in names:
        master(SRC / f"{n}_raw.png", DST / f"{n}.png")


if __name__ == "__main__":
    main()
