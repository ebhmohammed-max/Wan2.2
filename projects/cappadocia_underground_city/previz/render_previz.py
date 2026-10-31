#!/usr/bin/env python3
"""Render a 9:16 cinematic motion previz (animatic) from the three keyframes.

This is NOT Wan2.2 output — it is a camera-move previz used to lock framing,
push-in speed and the tunnel -> chamber -> steps reveal before spending GPU
time on the diffusion takes.

Camera: one continuous eased dolly-in (scale 1.00 -> 1.16) with a slow downward
drift, dust motes with depth parallax, atmospheric lift, warm low-key grade,
vignette and film grain. Output 1080x1920 @ 24 fps, H.264 yuv420p.

Usage:  python previz/render_previz.py [--out previz/cappadocia_previz_9x16.mp4]
"""
import argparse
import math
import os

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageFilter

W, H = 1080, 1920          # 9:16 master
FPS = 24
SHOT_FRAMES = 6 * FPS      # 6 s per shot
XFADE = 1 * FPS            # 1 s crossfades
PLATE_SCALE = 2.6          # upscale factor so pushes stay sharp
SS = 2                     # supersample for dust/glow layers

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
KEYFRAMES = [
    ("kf01_tunnel.png", 0.00, 0.00),
    ("kf02_chamber_reveal.png", 0.35, 0.05),
    ("kf03_deep_hall.png", 0.55, 0.10),
]


def smoothstep(t):
    t = min(max(t, 0.0), 1.0)
    return t * t * (3.0 - 2.0 * t)


def load_plate(path):
    """Upscale a keyframe and centre-crop it to exactly 9:16."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    target = W / H
    if w / h > target:                      # too wide -> crop sides
        nw = int(round(h * target))
        box = ((w - nw) // 2, 0, (w + nw) // 2, h)
    else:                                   # too tall -> crop top/bottom
        nh = int(round(w / target))
        top = int(round((h - nh) * 0.42))   # keep a touch more ceiling
        box = (0, top, w, top + nh)
    im = im.crop(box)
    return im.resize((int(W * PLATE_SCALE), int(H * PLATE_SCALE)), Image.LANCZOS)


def camera_frame(plate, t, dy_bias):
    """t in 0..1 across the shot -> cropped 1080x1920 frame with eased push-in."""
    e = smoothstep(t)
    scale = 1.0 + 0.16 * e                                  # push forward
    pw, ph = plate.size
    cw, ch = pw / scale, ph / scale
    drift = (0.012 + dy_bias) * H * PLATE_SCALE * e          # reveal downward
    sway = math.sin(t * math.pi * 1.3) * 2.0 * PLATE_SCALE   # faint natural drift
    left = (pw - cw) / 2 + sway * 0.4
    top = (ph - ch) / 2 + min(drift, (ph - ch) / 2)
    frame = plate.crop((int(left), int(top), int(left + cw), int(top + ch)))
    return frame.resize((W, H), Image.BICUBIC)


def build_dust(n=110, seed=7):
    rng = np.random.default_rng(seed)
    return dict(
        x=rng.uniform(0, W, n),
        y=rng.uniform(0, H, n),
        z=rng.uniform(0.25, 1.0, n),                # depth: 1 = nearest
        size=rng.uniform(0.9, 2.8, n),
        amp=rng.uniform(0.10, 0.55, n),
        vx=rng.uniform(-0.10, 0.16, n),
        vy=rng.uniform(-0.22, -0.05, n),
        ph=rng.uniform(0, 2 * math.pi, n),
        om=rng.uniform(0.25, 0.9, n),
    )


def dust_layer(dust, frame_i, push):
    """Additive warm motes, with parallax + slow drift; returns float RGB layer."""
    lay = np.zeros((H // 2, W // 2, 3), dtype=np.float32)
    s = math.sin
    for i in range(len(dust["x"])):
        z = dust["z"][i]
        px = dust["x"][i] + dust["vx"][i] * frame_i + 6.0 * z * s(dust["om"][i] * frame_i / FPS + dust["ph"][i])
        py = dust["y"][i] + dust["vy"][i] * frame_i + 4.0 * z * math.cos(dust["om"][i] * frame_i / FPS + dust["ph"][i])
        # parallax: nearer motes fly outward as the camera pushes in
        px = (px - W / 2) * (1.0 + 0.10 * push * z) + W / 2
        py = (py - H / 2) * (1.0 + 0.10 * push * z) + H / 2
        px = px % W
        py = py % H
        hx, hy = px / 2.0, py / 2.0
        rad = max(0.8, dust["size"][i] * z)
        x0, x1 = int(hx - rad * 2) - 1, int(hx + rad * 2) + 2
        y0, y1 = int(hy - rad * 2) - 1, int(hy + rad * 2) + 2
        if x1 <= 0 or y1 <= 0 or x0 >= W // 2 or y0 >= H // 2:
            continue
        xs = np.arange(max(x0, 0), min(x1, W // 2))
        ys = np.arange(max(y0, 0), min(y1, H // 2))
        if xs.size == 0 or ys.size == 0:
            continue
        gx = np.exp(-((xs - hx) ** 2) / (2 * rad * rad))
        gy = np.exp(-((ys - hy) ** 2) / (2 * rad * rad))
        blob = np.outer(gy, gx) * dust["amp"][i] * (0.35 + 0.65 * z)
        oy, ox = ys[0], xs[0]
        lay[oy:oy + len(ys), ox:ox + len(xs), 0] += blob * 1.00
        lay[oy:oy + len(ys), ox:ox + len(xs), 1] += blob * 0.72
        lay[oy:oy + len(ys), ox:ox + len(xs), 2] += blob * 0.42
    return lay


def composite(f32, dust_lay, frame_i, rng):
    """Grade + haze + dust + vignette + grain on a float HxWx3 frame."""
    img = f32 / 255.0

    # gentle S-curve contrast, lifted blacks kept (documentary look)
    img = np.clip(img, 0, 1)
    img = img * img * (3 - 2 * img) * 0.55 + img * 0.45
    img = np.clip((img - 0.5) * 1.06 + 0.5 + 0.012, 0, 1)

    # warm low-key grade: amber in mids/highs, slightly cool-black shadows
    lum = img @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    warm = np.array([1.045, 1.000, 0.930], dtype=np.float32)
    cool = np.array([0.965, 0.990, 1.045], dtype=np.float32)
    img = img * (warm * lum[..., None] + cool * (1 - lum[..., None]))

    # atmospheric haze lift (very subtle, bottom-weighted)
    haze = np.linspace(0.030, 0.004, H, dtype=np.float32)[:, None, None]
    img = img + haze * np.array([1.0, 0.86, 0.66], dtype=np.float32)

    # dust motes
    d = np.asarray(
        Image.fromarray((np.clip(dust_lay, 0, 1) * 255).astype(np.uint8))
        .resize((W, H), Image.BILINEAR), dtype=np.float32) / 255.0
    img = img + d * 0.55

    # vignette
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    vig = np.clip(1.0 - 0.30 * np.clip(r - 0.35, 0, None) ** 1.5, 0.55, 1.0)[..., None]
    img = img * vig

    # film grain (luma-weighted) + a hair of chroma noise
    g = rng.normal(0.0, 1.0, (H, W, 1)).astype(np.float32)
    img = img + g * 0.013 * (0.45 + 0.55 * (1 - lum[..., None]))
    img = img + rng.normal(0.0, 1.0, (H, W, 3)).astype(np.float32) * 0.004

    return (np.clip(img, 0, 1) * 255).astype(np.uint8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "cappadocia_previz_9x16.mp4"))
    args = ap.parse_args()

    plates = []
    for name, dy_bias, _ in KEYFRAMES:
        p = os.path.join(ROOT, "keyframes", name)
        plates.append(load_plate(p))
        print(f"plate ready: {name} -> {plates[-1].size}")

    total = SHOT_FRAMES * len(plates) - XFADE * (len(plates) - 1)
    print(f"rendering {total} frames ({total / FPS:.2f}s) at {W}x{H}@{FPS}")

    dust = build_dust()
    rng = np.random.default_rng(11)
    writer = imageio.get_writer(
        args.out, fps=FPS, codec="libx264", quality=None, pixelformat="yuv420p",
        output_params=["-crf", "22", "-preset", "slow", "-tune", "film", "-movflags", "+faststart"],
        macro_block_size=8,
    )

    try:
        for i in range(total):
            acc = np.zeros((H, W, 3), dtype=np.float32)
            wsum = 0.0
            for k, (name, dy_bias, dy_shot) in enumerate(KEYFRAMES):
                start = k * (SHOT_FRAMES - XFADE)
                local = i - start
                if local < 0 or local >= SHOT_FRAMES:
                    continue
                t = local / (SHOT_FRAMES - 1)
                wgt = 1.0
                if k > 0 and local < XFADE:                      # fade in
                    wgt *= smoothstep(local / XFADE)
                if k < len(KEYFRAMES) - 1 and local >= SHOT_FRAMES - XFADE:  # fade out
                    wgt *= smoothstep((SHOT_FRAMES - 1 - local) / XFADE)
                if wgt <= 0:
                    continue
                fr = camera_frame(plates[k], t, dy_bias + dy_shot)
                fr = fr.filter(ImageFilter.GaussianBlur(radius=0.0))
                acc += np.asarray(fr, dtype=np.float32) * wgt
                wsum += wgt
            if wsum <= 0:
                acc = np.asarray(plates[0].resize((W, H)), dtype=np.float32)
            else:
                acc /= wsum

            push = min(i / total, 1.0)
            out = composite(acc, dust_layer(dust, i, push), i, rng)
            writer.append_data(out)
            if i % 24 == 0:
                print(f"  frame {i}/{total}", flush=True)
    finally:
        writer.close()

    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
