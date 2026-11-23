#!/usr/bin/env python3
"""THE DUNE ARCHIVES — still-to-cinema motion engine (16:9 documentary master).

Turns a single still (AI-generated plate, map frame, artifact render) into a
short H.264 shot with motivated camera movement and atmospheric layers, so a
documentary built from static images never reads as a slideshow.

Lineage / reuse:
  * eased affine `warp` + 3-plane depth parallax adapted from
    projects/atlas_understory/scripts/make_clips.py
  * grain / smoothstep conventions adapted from
    projects/cappadocia_underground_city/previz/previz_lib.py
  Both are repo-local code; this module generalises them for 1920x1080
  documentary work and adds sand/dust, heat shimmer, light sweep, letterbox.

Motion recipes (use the one the storyboard calls for — never decorate):
  PUSH_IN     slow push toward a subject (tension, revelation)        1.00 -> 1.12
  PULL_OUT    slow reveal of scale (empires, deserts, fleets)         1.14 -> 1.00
  PAN_LR/RL   lateral travel across a wide plate (landscapes, rows)
  TILT_UP/DN  vertical travel (towers, heighliners, worm emergence)
  PARALLAX    3-plane depth drift (environments with foreground)
  DRIFT       near-static breathing hold (portraits, Bene Gesserit)
  WORM_RISE   tilt-up + building camera shake (sandworm emergence)
  HOLD        locked-off, atmosphere only (symbolic / text cards)

Atmosphere layers (optional, motivated): sand, dust, heat, lightsweep, shake.

Usage:
  python motion_engine.py --image plate.png --out shot.mp4 --recipe PUSH_IN \
      --duration 6 [--sand 0.6] [--heat 0.3] [--lightsweep] [--letterbox]
  python motion_engine.py --manifest shots.json --outdir clips/
    manifest: [{"image": "...", "out": "...", "recipe": "PULL_OUT",
                "duration": 7.5, "sand": 0.4, "heat": 0.0, "focus": [0.5, 0.45]}]
"""
import argparse
import json
import math
import pathlib
import subprocess

import numpy as np
from PIL import Image, ImageFilter

try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # pragma: no cover
    FFMPEG = "ffmpeg"

OUT_W, OUT_H = 1920, 1080
FPS = 24
OVERSCAN = 1.22           # working canvas so moves/shake never expose an edge
RNG = np.random.default_rng(10191)


# ------------------------------------------------------------------ easing --
def ease(t):
    """cosine ease in/out, 0..1 -> 0..1"""
    t = min(max(t, 0.0), 1.0)
    return 0.5 - 0.5 * math.cos(math.pi * t)


def ease_out(t):
    t = min(max(t, 0.0), 1.0)
    return 1 - (1 - t) ** 3


# ------------------------------------------------------------------ plates --
def load_plate(path):
    """Cover-crop to 16:9 and upscale to the overscan working canvas."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    target = OUT_W / OUT_H
    if w / h > target:
        nw = int(round(h * target))
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(round(w / target))
        im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    return im.resize((int(OUT_W * OVERSCAN), int(OUT_H * OVERSCAN)), Image.LANCZOS)


def warp(img, scale, cx, cy):
    """Return an OUT_W x OUT_H view of `img` zoomed by `scale` about (cx, cy)
    expressed in source pixels. scale=1 shows OUT_W/OVERSCAN-equivalent field."""
    w, h = img.size
    # visible window size in source px at this scale (base window = canvas / OVERSCAN)
    vw, vh = (w / OVERSCAN) / scale, (h / OVERSCAN) / scale
    left = min(max(cx - vw / 2, 0), w - vw)
    top = min(max(cy - vh / 2, 0), h - vh)
    k = vw / OUT_W
    return img.transform((OUT_W, OUT_H), Image.AFFINE, (k, 0, left, 0, k, top),
                         resample=Image.BICUBIC)


def depth_weights(img):
    """Cheap 3-plane depth proxy (vertical position + luminance), from atlas_understory."""
    small = img.convert("L").resize((240, 135), Image.BILINEAR)
    lum = np.asarray(small.filter(ImageFilter.GaussianBlur(4)), dtype=np.float32) / 255.0
    yy = np.linspace(0.0, 1.0, 135, dtype=np.float32)[:, None]
    d = np.clip((0.6 * yy + 0.4 * lum - 0.28) / 0.5, 0.0, 1.0)
    near, far = d ** 2, (1.0 - d) ** 2
    mid = np.clip(1.0 - near - far, 0.0, 1.0)
    up = lambda m: np.asarray(Image.fromarray((m * 255).astype(np.uint8)).resize(
        (OUT_W, OUT_H), Image.BILINEAR), dtype=np.float32)[..., None] / 255.0
    return up(near), up(mid), up(far)


# ------------------------------------------------------------- atmosphere --
class Sand:
    """Wind-driven sand/dust particles with motion streaks (Arrakis exteriors)."""

    def __init__(self, density=0.5, wind=(1.0, 0.12), warm=True):
        n = int(1400 * density)
        self.p = RNG.random((n, 2)) * [OUT_W, OUT_H]
        self.v = (RNG.normal(1.0, 0.35, (n, 1)) * np.array(wind)[None, :]) * 14.0
        self.s = RNG.uniform(0.6, 2.4, n)
        self.a = RNG.uniform(0.08, 0.45, n) * density
        self.col = np.array([232, 196, 140] if warm else [210, 210, 205], np.float32)

    def step_and_draw(self, frame):
        self.p += self.v
        self.p[:, 0] %= OUT_W
        self.p[:, 1] %= OUT_H
        layer = np.zeros((OUT_H, OUT_W), np.float32)
        x0 = self.p[:, 0].astype(int)
        y0 = np.clip(self.p[:, 1].astype(int), 0, OUT_H - 1)
        ln = np.maximum(1, (np.abs(self.v[:, 0]) * 0.5 * self.s).astype(int))
        for k in range(int(ln.max())):  # vectorised streaks, one pass per pixel of length
            m = ln > k
            xs = np.clip(x0[m] + k, 0, OUT_W - 1)
            np.maximum.at(layer, (y0[m], xs), self.a[m])
        layer = np.asarray(Image.fromarray((layer * 255).astype(np.uint8)).filter(
            ImageFilter.GaussianBlur(0.8)), np.float32) / 255.0
        f = frame.astype(np.float32)
        f = f * (1 - layer[..., None]) + self.col * layer[..., None]
        return f


def heat_shimmer(frame, t, amount):
    """Horizontal sinusoidal displacement, strongest near the horizon band."""
    if amount <= 0:
        return frame
    h = frame.shape[0]
    rows = np.arange(h)
    band = np.exp(-((rows / h - 0.55) ** 2) / 0.02)
    shift = (np.sin(rows * 0.09 + t * 6.0) * 3.0 * amount * band).astype(int)
    cols = (np.arange(frame.shape[1])[None, :] - shift[:, None]) % frame.shape[1]
    return frame[rows[:, None], cols]


def light_sweep(frame, t):
    """Slow diagonal sun/glow sweep — use for reveals and title moments."""
    yy, xx = np.mgrid[0:OUT_H, 0:OUT_W].astype(np.float32)
    pos = -0.3 + 1.6 * ease(t)
    d = (xx / OUT_W + 0.35 * yy / OUT_H) - pos
    glow = np.exp(-(d ** 2) / 0.012)[..., None] * 0.18
    return frame + glow * np.array([255, 214, 160], np.float32)


_VIG = {}


def _vignette(strength):
    if strength not in _VIG:
        yy, xx = np.mgrid[0:OUT_H, 0:OUT_W].astype(np.float32)
        r = np.sqrt(((xx - OUT_W / 2) / (OUT_W / 2)) ** 2 + ((yy - OUT_H / 2) / (OUT_H / 2)) ** 2)
        _VIG[strength] = (1 - strength * np.clip(r - 0.55, 0, 1) ** 1.5)[..., None].astype(np.float32)
    return _VIG[strength]


def grade(frame, grain=3.0, vignette=0.22):
    f = frame.astype(np.float32)
    if vignette:
        f *= _vignette(vignette)
    if grain:
        f += RNG.normal(0, grain, (OUT_H, OUT_W, 1))
    return np.clip(f, 0, 255).astype(np.uint8)


def letterbox(frame, ratio=2.39):
    bar = int((OUT_H - OUT_W / ratio) / 2)
    if bar > 0:
        frame[:bar] = 0
        frame[-bar:] = 0
    return frame


# ---------------------------------------------------------------- recipes --
def camera(recipe, t, w, h, focus):
    """Return (scale, cx, cy) for progress t in [0,1]."""
    e = ease(t)
    fx, fy = focus[0] * w, focus[1] * h
    c = (w / 2, h / 2)
    if recipe == "PUSH_IN":
        return 1.0 + 0.12 * e, c[0] + (fx - c[0]) * e, c[1] + (fy - c[1]) * e
    if recipe == "PULL_OUT":
        return 1.14 - 0.14 * e, fx + (c[0] - fx) * e, fy + (c[1] - fy) * e
    if recipe == "PAN_LR":
        return 1.10, w * (0.40 + 0.20 * e), c[1]
    if recipe == "PAN_RL":
        return 1.10, w * (0.60 - 0.20 * e), c[1]
    if recipe == "TILT_UP":
        return 1.10, c[0], h * (0.60 - 0.20 * e)
    if recipe == "TILT_DN":
        return 1.10, c[0], h * (0.40 + 0.20 * e)
    if recipe == "WORM_RISE":
        return 1.04 + 0.10 * ease_out(t), c[0], h * (0.62 - 0.22 * ease_out(t))
    if recipe == "DRIFT":
        return 1.03 + 0.02 * e, c[0] + 8 * math.sin(t * math.pi), c[1]
    return 1.0, c[0], c[1]  # HOLD / PARALLAX base


def render_shot(image, out, recipe="PUSH_IN", duration=6.0, sand=0.0, heat=0.0,
                lightsweep=False, shake=0.0, lb=False, focus=(0.5, 0.5), crf=18):
    plate = load_plate(image)
    w, h = plate.size
    n = max(1, int(round(duration * FPS)))
    sand_fx = Sand(sand) if sand > 0 else None
    if recipe == "WORM_RISE" and shake == 0.0:
        shake = 1.0
    planes = depth_weights(plate.resize((OUT_W, OUT_H))) if recipe == "PARALLAX" else None
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{OUT_W}x{OUT_H}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
           "-preset", "medium", "-crf", str(crf), "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", str(out)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        t = i / max(1, n - 1)
        s, cx, cy = camera(recipe, t, w, h, focus)
        if shake:
            amp = shake * (6 if recipe != "WORM_RISE" else 4 + 10 * t)
            cx += RNG.normal(0, amp)
            cy += RNG.normal(0, amp)
        if planes is not None:
            near, mid, far = planes
            e = ease(t)
            layers = [np.asarray(warp(plate, 1.10, w * (0.5 + k * (e - 0.5)), h / 2), np.float32)
                      for k in (0.10, 0.05, 0.02)]
            f = layers[0] * near + layers[1] * mid + layers[2] * far
        else:
            f = np.asarray(warp(plate, s, cx, cy), np.float32)
        if heat:
            f = heat_shimmer(f, t * duration, heat)
        if sand_fx is not None:
            f = sand_fx.step_and_draw(f)
        if lightsweep:
            f = light_sweep(f, t)
        f = grade(f)
        if lb:
            f = letterbox(f)
        proc.stdin.write(f.tobytes())
    proc.stdin.close()
    proc.wait()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image")
    ap.add_argument("--out")
    ap.add_argument("--recipe", default="PUSH_IN")
    ap.add_argument("--duration", type=float, default=6.0)
    ap.add_argument("--sand", type=float, default=0.0)
    ap.add_argument("--heat", type=float, default=0.0)
    ap.add_argument("--shake", type=float, default=0.0)
    ap.add_argument("--lightsweep", action="store_true")
    ap.add_argument("--letterbox", action="store_true")
    ap.add_argument("--focus", type=float, nargs=2, default=(0.5, 0.5))
    ap.add_argument("--manifest")
    ap.add_argument("--outdir", default=".")
    a = ap.parse_args()
    if a.manifest:
        for s in json.loads(pathlib.Path(a.manifest).read_text()):
            render_shot(s["image"], pathlib.Path(a.outdir) / s["out"], s.get("recipe", "PUSH_IN"),
                        s.get("duration", 6.0), s.get("sand", 0.0), s.get("heat", 0.0),
                        s.get("lightsweep", False), s.get("shake", 0.0), s.get("letterbox", False),
                        tuple(s.get("focus", (0.5, 0.5))))
    else:
        render_shot(a.image, a.out, a.recipe, a.duration, a.sand, a.heat, a.lightsweep,
                    a.shake, a.letterbox, tuple(a.focus))


if __name__ == "__main__":
    main()
