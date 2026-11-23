"""Fast still-to-motion renderer (OpenCV + one ffmpeg pass), used by assemble_roughcut.py.

Same camera grammar as motion_engine.py (it imports `camera`, `ease`, OVERSCAN from there),
but about 10x faster on a 2-CPU box:
  * cv2.warpAffine on a uint8 overscan plate (sub-pixel, so slow push-ins don't judder),
  * vignette + film grain done by ffmpeg filters instead of numpy per frame,
  * the lower-third / corner-bug overlay PNG is composited in the same encode.
PARALLAX uses three warps blended by a cheap depth proxy, as motion_engine does.
"""
import math, subprocess
import cv2
import numpy as np
import motion_engine as me

FPS = me.FPS


def load_plate(path, W, H):
    im = cv2.imread(str(path), cv2.IMREAD_COLOR)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    h, w = im.shape[:2]
    target = W / H
    if w / h > target:
        nw = int(round(h * target)); x0 = (w - nw) // 2
        im = im[:, x0:x0 + nw]
    else:
        nh = int(round(w / target)); y0 = (h - nh) // 2
        im = im[y0:y0 + nh]
    return cv2.resize(im, (int(W * me.OVERSCAN), int(H * me.OVERSCAN)), interpolation=cv2.INTER_LANCZOS4)


def warp(plate, s, cx, cy, W, H):
    h, w = plate.shape[:2]
    vw, vh = (w / me.OVERSCAN) / s, (h / me.OVERSCAN) / s
    left = min(max(cx - vw / 2, 0), w - vw)
    top = min(max(cy - vh / 2, 0), h - vh)
    k = W / vw
    M = np.float32([[k, 0, -left * k], [0, k, -top * k]])
    return cv2.warpAffine(plate, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def depth_planes(frame):
    small = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY), (240, 135)).astype(np.float32) / 255
    small = cv2.GaussianBlur(small, (0, 0), 4)
    yy = np.linspace(0, 1, 135, dtype=np.float32)[:, None]
    d = np.clip((0.6 * yy + 0.4 * small - 0.28) / 0.5, 0, 1)
    near, far = d ** 2, (1 - d) ** 2
    mid = np.clip(1 - near - far, 0, 1)
    H, W = frame.shape[:2]
    return [cv2.resize(m, (W, H))[..., None] for m in (near, mid, far)]


def render(image, out, recipe, nframes, W, H, overlay_png, focus=(0.5, 0.5), crf=20, grain=6, seed=0):
    plate = load_plate(image, W, H)
    ph, pw = plate.shape[:2]
    rng = np.random.default_rng(seed)
    shake = 1.0 if recipe == 'WORM_RISE' else 0.0
    planes = depth_planes(warp(plate, 1.0, pw / 2, ph / 2, W, H)) if recipe == 'PARALLAX' else None
    vf = (f"[0:v]vignette=angle=PI/5,noise=c0s={grain}:c0f=t,format=yuv420p[b];"
          f"[b][1:v]overlay=0:0:format=auto,format=yuv420p")
    cmd = [me.FFMPEG, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
           '-r', str(FPS), '-i', '-', '-i', str(overlay_png), '-filter_complex', vf, '-frames:v', str(nframes),
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', str(crf), '-pix_fmt', 'yuv420p', '-an',
           '-video_track_timescale', '12288', str(out)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes):
        t = i / max(1, nframes - 1)
        if planes is not None:
            e = me.ease(t)
            layers = [warp(plate, 1.10, pw * (0.5 + k * (e - 0.5)), ph / 2, W, H).astype(np.float32)
                      for k in (0.10, 0.05, 0.02)]
            f = np.clip(layers[0] * planes[0] + layers[1] * planes[1] + layers[2] * planes[2], 0, 255).astype(np.uint8)
        else:
            s, cx, cy = me.camera(recipe, t, pw, ph, focus)
            if shake:
                amp = 4 + 10 * t
                cx += rng.normal(0, amp); cy += rng.normal(0, amp)
            f = warp(plate, s, cx, cy, W, H)
        p.stdin.write(np.ascontiguousarray(f).tobytes())
    p.stdin.close()
    if p.wait() != 0:
        raise RuntimeError(f'ffmpeg failed for {out}')
    return out
