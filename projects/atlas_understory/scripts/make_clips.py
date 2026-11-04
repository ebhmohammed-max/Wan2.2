#!/usr/bin/env python3
"""Atlas Understory — still-to-clip motion, plain video only.

Implements the three editor motion recipes the v4 Shot Map assigns to
background plates, at 1920x1080 / 24 fps / H.264 yuv420p / faststart,
with NO audio track, no titles, no captions.

  M02  pullout 6 %      slow centred zoom out 1.06 -> 1.00
  M03  layer parallax   lateral drift with a 3-plane depth approximation
  M08  A/B crop crossfade   same still, wide crop -> tighter crop, crossfaded

Usage:  make_clips.py stills_dir clips_dir manifest.json
manifest: [{"image":"C01-S002-A","shot":"C01-S002","motion":"M03","duration":6.208}, ...]
"""
import json, math, pathlib, subprocess, sys

import numpy as np
from PIL import Image, ImageFilter
import imageio_ffmpeg

OUT_W, OUT_H = 1920, 1080
FPS = 24
OVERS = 1.16  # working canvas overscan so warps never show an edge


def ease(t: float) -> float:
    """smooth in/out"""
    return 0.5 - 0.5 * math.cos(math.pi * t)


def warp(img: Image.Image, scale: float, dx: float, dy: float) -> Image.Image:
    """Zoom by `scale` about the image centre plus pixel offset (dx, dy)."""
    w, h = img.size
    cx, cy = w / 2.0, h / 2.0
    a = 1.0 / scale
    c = (cx + dx) - (OUT_W / 2.0) / scale
    f = (cy + dy) - (OUT_H / 2.0) / scale
    return img.transform((OUT_W, OUT_H), Image.AFFINE, (a, 0, c, 0, a, f),
                         resample=Image.BICUBIC)


def depth_weights(img: Image.Image):
    """3-plane weight maps from a cheap depth proxy (vertical position + luminance)."""
    small = img.convert("L").resize((240, 135), Image.BILINEAR)
    lum = np.asarray(small.filter(ImageFilter.GaussianBlur(4)), dtype=np.float32) / 255.0
    yy = np.linspace(0.0, 1.0, 135, dtype=np.float32)[:, None]
    d = 0.55 * yy + 0.45 * lum          # 0 = far/top, 1 = near/bottom
    d = np.clip((d - 0.28) / 0.5, 0.0, 1.0)
    near = d ** 2
    far = (1.0 - d) ** 2
    mid = np.clip(1.0 - near - far, 0.0, None)
    tot = near + mid + far + 1e-6
    out = []
    for m in (near, mid, far):
        im = Image.fromarray((np.clip(m / tot, 0, 1) * 255).astype(np.uint8))
        out.append(np.asarray(im.resize((OUT_W, OUT_H), Image.BICUBIC),
                              dtype=np.float32)[..., None] / 255.0)
    return out  # near, mid, far


def frame_M02(base, t, weights=None):
    s = 1.06 - 0.06 * ease(t)
    return warp(base, s, 0.0, 0.0)


def frame_M03(base, t, weights):
    e = ease(t)
    dx = (e - 0.5) * 2.0 * 26.0          # travel +-26 px at 1080
    dy = math.sin(math.pi * t) * -6.0
    s = 1.055 - 0.02 * e
    near, mid, far = weights
    layers = [warp(base, s, dx * 1.55, dy * 1.5),
              warp(base, s, dx * 0.95, dy * 1.0),
              warp(base, s, dx * 0.45, dy * 0.55)]
    arr = [np.asarray(l, dtype=np.float32) for l in layers]
    out = arr[0] * near + arr[1] * mid + arr[2] * far
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def frame_M08(base, t, weights=None):
    """wide crop -> tighter crop, crossfaded over the middle of the shot."""
    s_a = 1.0 + 0.012 * ease(t)
    s_b = 1.16 + 0.012 * ease(t)
    a = warp(base, s_a, 0.0, 0.0)
    b = warp(base, s_b, 10.0, -6.0)
    m = min(1.0, max(0.0, (t - 0.18) / 0.64))
    m = ease(m)
    out = np.asarray(a, dtype=np.float32) * (1 - m) + np.asarray(b, dtype=np.float32) * m
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


MOTION = {"M02": frame_M02, "M03": frame_M03, "M08": frame_M08}


def render(still: pathlib.Path, out: pathlib.Path, motion: str, duration: float) -> None:
    img = Image.open(still).convert("RGB")
    w = int(round(OUT_W * OVERS))
    h = int(round(OUT_H * OVERS))
    base = img.resize((w, h), Image.LANCZOS)
    weights = depth_weights(base) if motion == "M03" else None
    fn = MOTION[motion]
    n = max(1, int(round(duration * FPS)))
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OUT_W}x{OUT_H}",
           "-r", str(FPS), "-i", "-",
           "-an", "-c:v", "libx264", "-preset", "slow", "-crf", "17",
           "-pix_fmt", "yuv420p", "-profile:v", "high",
           "-movflags", "+faststart", "-r", str(FPS), str(out)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        t = i / (n - 1) if n > 1 else 0.0
        fr = fn(base, t, weights)
        p.stdin.write(np.asarray(fr, dtype=np.uint8).tobytes())
    p.stdin.close()
    if p.wait() != 0:
        raise RuntimeError(f"ffmpeg failed on {out}")
    print(f"{out.name}  {motion}  {n} frames  {n / FPS:.2f}s")


def main() -> None:
    stills = pathlib.Path(sys.argv[1])
    clips = pathlib.Path(sys.argv[2])
    manifest = json.loads(pathlib.Path(sys.argv[3]).read_text())
    clips.mkdir(parents=True, exist_ok=True)
    for row in manifest:
        still = stills / f"{row['image']}.png"
        out = clips / f"{row['shot']}_{row['motion']}.mp4"
        render(still, out, row["motion"], float(row["duration"]))


if __name__ == "__main__":
    main()
