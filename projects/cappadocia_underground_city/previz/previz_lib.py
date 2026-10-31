#!/usr/bin/env python3
"""Shared previz library: plates, camera moves, dust, flicker, grade, encode.

Used by both shot renderers:
  previz/render_previz.py                 shot 01 — the empty tunnel reveal
  ../shot02_explorer/previz/render_previz.py  shot 02 — the explorer walking

Everything renders at 1080x1920 (exact 9:16) @ 24 fps and is an ANIMATIC, not
model output: keyframes driven by eased moves, dust, lantern flicker, film grain.
"""
import math

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageFilter

W, H = 1080, 1920          # 9:16 master
FPS = 24
PLATE_SCALE = 2.6          # upscale factor so pushes stay sharp

AMBER = np.array([1.0, 0.72, 0.42], dtype=np.float32)


def smoothstep(t):
    t = min(max(t, 0.0), 1.0)
    return t * t * (3.0 - 2.0 * t)


# ---------------------------------------------------------------- plates ----
def load_plate(path, scale=PLATE_SCALE):
    """Load a keyframe and centre-crop it to exactly 9:16 at `scale` x master."""
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
    return im.resize((int(W * scale), int(H * scale)), Image.LANCZOS)


def camera_frame(plate, zoom_to=1.16, t=0.0, dy=0.0, roll_deg=0.0, shake_px=0.0):
    """Crop an eased push-in window from a plate -> 1080x1920 frame.

    zoom_to : final scale relative to the plate (1.0 = untouched framing)
    t       : 0..1 progress through the move (smoothstep applied)
    dy      : downward drift, as a fraction of master height
    roll_deg: tiny camera roll, degrees
    shake_px: vertical bob in master pixels (walk weight shift)
    """
    e = smoothstep(t)
    scale = 1.0 + (zoom_to - 1.0) * e
    pw, ph = plate.size
    cw, ch = pw / scale, ph / scale
    left = (pw - cw) / 2
    top = (ph - ch) / 2 + min(dy * H * PLATE_SCALE * e, (ph - ch) / 2)
    top += shake_px * PLATE_SCALE
    frame = plate.crop((int(left), int(top), int(left + cw), int(top + ch))).resize((W, H), Image.BICUBIC)
    if abs(roll_deg) > 1e-3:
        # rotate a slightly oversized copy so corners never show
        big = frame.resize((int(W * 1.08), int(H * 1.08)), Image.BICUBIC)
        big = big.rotate(roll_deg, resample=Image.BICUBIC, center=(big.size[0] / 2, big.size[1] / 2))
        ox, oy = (big.size[0] - W) // 2, (big.size[1] - H) // 2
        frame = big.crop((ox, oy, ox + W, oy + H))
    return frame


# ------------------------------------------------------------------ dust ----
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


def dust_layer(dust, frame_i, push=0.0):
    """Additive warm motes with depth parallax; returned at half resolution."""
    lay = np.zeros((H // 2, W // 2, 3), dtype=np.float32)
    s = math.sin
    for i in range(len(dust["x"])):
        z = dust["z"][i]
        px = dust["x"][i] + dust["vx"][i] * frame_i + 6.0 * z * s(dust["om"][i] * frame_i / FPS + dust["ph"][i])
        py = dust["y"][i] + dust["vy"][i] * frame_i + 4.0 * z * math.cos(dust["om"][i] * frame_i / FPS + dust["ph"][i])
        px = (px - W / 2) * (1.0 + 0.10 * push * z) + W / 2
        py = (py - H / 2) * (1.0 + 0.10 * push * z) + H / 2
        px %= W
        py %= H
        hx, hy = px / 2.0, py / 2.0
        rad = max(0.8, dust["size"][i] * z)
        x0, x1 = int(hx - rad * 2) - 1, int(hx + rad * 2) + 2
        y0, y1 = int(hy - rad * 2) - 1, int(hy + rad * 2) + 2
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


# -------------------------------------------------------- lantern glow ----
def flicker_at(t_sec, seed=0):
    """Irregular 0.75..1.25 lamp flicker: two sines + a slow random walk."""
    a = math.sin(t_sec * 7.3 + seed) * 0.6 + math.sin(t_sec * 17.9 + seed * 2.1) * 0.3
    b = math.sin(t_sec * 1.7 + seed * 0.7) * 0.7
    return 1.0 + 0.13 * a + 0.07 * b


def glow_layer(spec, t_sec):
    """Radial amber bloom for a lamp. spec = (x, y, radius) in 0..1 of the frame."""
    if spec is None:
        return None
    x, y, r = spec[0] * W, spec[1] * H, spec[2] * H
    g = flicker_at(t_sec)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d2 = ((xx - x) ** 2 + (yy - y) ** 2) / (2.0 * (r / 2.2) ** 2)
    fall = np.exp(-d2).astype(np.float32) * 0.55 * g
    return fall[..., None] * AMBER


# ----------------------------------------------------------------- grade ----
def composite(f32, dust_lay, frame_i, rng, glow=None, warm_shift=1.0):
    """Grade + haze + dust + lamp glow + vignette + grain on a float HxWx3 frame."""
    img = np.clip(f32 / 255.0, 0, 1)

    # gentle S-curve contrast, lifted blacks kept (documentary look)
    img = img * img * (3 - 2 * img) * 0.55 + img * 0.45
    img = np.clip((img - 0.5) * 1.06 + 0.5 + 0.012, 0, 1)

    # warm low-key grade: amber in mids/highs, slightly cool-black shadows
    lum = img @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    warm = np.array([1.045, 1.000, 0.930], dtype=np.float32) * warm_shift
    cool = np.array([0.965, 0.990, 1.045], dtype=np.float32)
    img = img * (warm * lum[..., None] + cool * (1 - lum[..., None]))

    # atmospheric haze lift (very subtle, bottom-weighted)
    haze = np.linspace(0.030, 0.004, H, dtype=np.float32)[:, None, None]
    img = img + haze * np.array([1.0, 0.86, 0.66], dtype=np.float32)

    # dust motes
    if dust_lay is not None:
        d = np.asarray(
            Image.fromarray((np.clip(dust_lay, 0, 1) * 255).astype(np.uint8))
            .resize((W, H), Image.BILINEAR), dtype=np.float32) / 255.0
        img = img + d * 0.55

    # lantern bloom (additive, sits under the grain)
    if glow is not None:
        img = img + glow

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


# ---------------------------------------------------------------- encode ----
def make_writer(path, fps=FPS, crf="22"):
    return imageio.get_writer(
        path, fps=fps, codec="libx264", quality=None, pixelformat="yuv420p",
        output_params=["-crf", crf, "-preset", "slow", "-tune", "film", "-movflags", "+faststart"],
        macro_block_size=8,
    )


def soft_blur(frame, radius=0.0):
    return frame.filter(ImageFilter.GaussianBlur(radius=radius)) if radius > 0 else frame
