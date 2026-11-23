#!/usr/bin/env python3
"""THE DUNE ARCHIVES — data-driven animated map template (1920x1080, 24 fps).

One renderer, many map stories. A JSON "map scene" declares a style, nodes
(planets / sietches / landmarks), routes (trade, fleet, migration), territories
and a timed list of beats. The renderer draws a dark cinematic sci-fi map and
animates: node reveal pulses, glowing route draw-on with a travelling comet head,
territory fills, label typing, and a slow camera push toward a focus point.

CANON SAFETY (mandatory — see 01_lore/CANON_POLICY.md):
  * Frank Herbert never published interstellar coordinates. Every interstellar
    map is SCHEMATIC. The renderer stamps a provenance caption on every frame:
      "SCHEMATIC RECONSTRUCTION — RELATIVE POSITIONS ARE ARTISTIC"
    unless the scene sets "provenance" explicitly (e.g. for the Arrakis polar map,
    "AFTER THE DUNE (1965) APPENDIX MAP — FEATURES APPROXIMATE").
  * Nodes carry a `canon` tag; ORIGINAL/EXPANDED/FILM/TV/RECON nodes get distinct
    ring styles so an editor can never silently mix continuities.

Styles: "imperial" (gold on deep navy), "noir" (amber on black), "political"
(minimal flat), "arrakis" (ochre planetary).

Usage:  python map_animator.py scene.json out.mp4
"""
import json
import math
import pathlib
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # pragma: no cover
    FFMPEG = "ffmpeg"

W, H, FPS = 1920, 1080, 24
SS = 2  # supersample for smooth lines

STYLES = {
    "imperial": dict(bg=(8, 12, 24), grid=(30, 44, 70), ink=(226, 186, 110), route=(255, 196, 96),
                     text=(236, 222, 196), terr=(150, 110, 50)),
    "noir": dict(bg=(6, 6, 7), grid=(34, 30, 26), ink=(214, 160, 84), route=(255, 170, 70),
                 text=(230, 214, 190), terr=(120, 70, 30)),
    "political": dict(bg=(18, 20, 24), grid=(40, 44, 52), ink=(200, 205, 215), route=(120, 190, 255),
                      text=(235, 238, 242), terr=(70, 110, 160)),
    "arrakis": dict(bg=(42, 28, 16), grid=(84, 60, 36), ink=(240, 200, 140), route=(255, 140, 60),
                    text=(250, 232, 200), terr=(170, 110, 50)),
}
CANON_RING = {"ORIGINAL": 0, "EXPANDED": 1, "FILM": 2, "TV": 2, "RECON": 3}


def font(size):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/dejavu/DejaVuSans.ttf"):
        if pathlib.Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def ease(t):
    t = min(max(t, 0.0), 1.0)
    return 0.5 - 0.5 * math.cos(math.pi * t)


def beat_progress(beat, t):
    return ease((t - beat["start"]) / max(1e-6, beat.get("dur", 1.0)))


def starfield(st, seed=7):
    rng = np.random.default_rng(seed)
    img = Image.new("RGB", (W * SS, H * SS), st["bg"])
    d = ImageDraw.Draw(img)
    for _ in range(2200):
        x, y = rng.integers(0, W * SS), rng.integers(0, H * SS)
        b = int(rng.uniform(40, 160))
        r = rng.choice([1, 1, 1, 2])
        d.ellipse((x, y, x + r, y + r), fill=(b, b, min(255, b + 20)))
    for gx in range(0, W * SS, 120 * SS):
        d.line([(gx, 0), (gx, H * SS)], fill=st["grid"], width=1)
    for gy in range(0, H * SS, 120 * SS):
        d.line([(0, gy), (W * SS, gy)], fill=st["grid"], width=1)
    return img


def render(scene, out):
    st = STYLES[scene.get("style", "imperial")]
    dur = scene["duration"]
    nodes = {n["id"]: n for n in scene["nodes"]}
    base = starfield(st)
    f_lab, f_cap = font(22 * SS), font(16 * SS)
    s_title, s_lab, s_cap = font(40), font(22), font(16)
    prov = scene.get("provenance", "SCHEMATIC RECONSTRUCTION — RELATIVE POSITIONS ARE ARTISTIC")
    focus = scene.get("camera", {}).get("focus", [0.5, 0.5])
    push = scene.get("camera", {}).get("push", 0.08)
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-crf", "18",
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    P = lambda n: (n["x"] * W * SS, n["y"] * H * SS)
    for i in range(int(dur * FPS)):
        t = i / FPS
        img = base.copy()
        glow = Image.new("RGB", img.size, (0, 0, 0))
        d, g = ImageDraw.Draw(img), ImageDraw.Draw(glow)
        for b in scene["beats"]:
            p = beat_progress(b, t)
            if p <= 0:
                continue
            if b["type"] == "territory":
                poly = [(x * W * SS, y * H * SS) for x, y in b["polygon"]]
                ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
                ImageDraw.Draw(ov).polygon(poly, fill=st["terr"] + (int(70 * p),),
                                           outline=st["ink"] + (int(200 * p),))
                img.paste(ov, (0, 0), ov)
                d = ImageDraw.Draw(img)
            elif b["type"] == "route":
                pts = [P(nodes[k]) for k in b["path"]]
                segs = list(zip(pts[:-1], pts[1:]))
                lens = [math.dist(a, c) for a, c in segs]
                total, drawn = sum(lens), sum(lens) * p
                acc, head = 0.0, pts[0]
                for (a, c), L in zip(segs, lens):
                    if acc >= drawn:
                        break
                    k = min(1.0, (drawn - acc) / L)
                    e = (a[0] + (c[0] - a[0]) * k, a[1] + (c[1] - a[1]) * k)
                    dash = b.get("dashed", False)
                    if dash:
                        nd = int(L * k // (24 * SS))
                        for j in range(nd):
                            if j % 2 == 0:
                                s0, s1 = j / max(1, nd), (j + 1) / max(1, nd)
                                q0 = (a[0] + (e[0] - a[0]) * s0, a[1] + (e[1] - a[1]) * s0)
                                q1 = (a[0] + (e[0] - a[0]) * s1, a[1] + (e[1] - a[1]) * s1)
                                d.line([q0, q1], fill=st["route"], width=3 * SS)
                    else:
                        d.line([a, e], fill=st["route"], width=3 * SS)
                    g.line([a, e], fill=st["route"], width=10 * SS)
                    head, acc = e, acc + L
                if p < 1:
                    r = 9 * SS
                    g.ellipse((head[0] - r * 2, head[1] - r * 2, head[0] + r * 2, head[1] + r * 2), fill=(255, 230, 180))
                    d.ellipse((head[0] - r / 2, head[1] - r / 2, head[0] + r / 2, head[1] + r / 2), fill=(255, 245, 220))
            elif b["type"] == "node":
                n = nodes[b["id"]]
                x, y = P(n)
                r = (10 + 6 * (1 - p)) * SS
                ring = CANON_RING.get(n.get("canon", "RECON"), 3)
                d.ellipse((x - r, y - r, x + r, y + r), outline=st["ink"], width=3 * SS)
                if ring == 0:
                    d.ellipse((x - r / 2.5, y - r / 2.5, x + r / 2.5, y + r / 2.5), fill=st["ink"])
                elif ring == 3:  # reconstruction: dashed look via gaps
                    d.arc((x - r - 8 * SS, y - r - 8 * SS, x + r + 8 * SS, y + r + 8 * SS), 0, 300, fill=st["ink"], width=SS)
                else:
                    d.ellipse((x - r - 8 * SS, y - r - 8 * SS, x + r + 8 * SS, y + r + 8 * SS), outline=st["ink"], width=SS)
                pulse = (t * 1.2) % 1.0
                pr = r + 40 * SS * pulse
                g.ellipse((x - pr, y - pr, x + pr, y + pr), outline=tuple(int(c * (1 - pulse)) for c in st["ink"]), width=2 * SS)
                g.ellipse((x - r * 2, y - r * 2, x + r * 2, y + r * 2), fill=tuple(int(c * 0.6) for c in st["ink"]))
                label = n["label"][: max(1, int(len(n["label"]) * min(1, p * 1.5)))]
                d.text((x + 22 * SS, y - 14 * SS), label.upper(), font=f_lab, fill=st["text"])
                if n.get("sub") and p > 0.6:
                    d.text((x + 22 * SS, y + 14 * SS), n["sub"], font=f_cap, fill=st["ink"])
        glow = glow.filter(ImageFilter.GaussianBlur(14 * SS))
        img = Image.fromarray(np.clip(np.asarray(img, np.int16) + np.asarray(glow, np.int16) * 0.9, 0, 255).astype(np.uint8))
        # slow camera push toward focus
        s = 1.0 + push * ease(t / dur)
        vw, vh = W * SS / s, H * SS / s
        cx, cy = focus[0] * W * SS, focus[1] * H * SS
        left = min(max(cx - vw / 2, 0), W * SS - vw)
        top = min(max(cy - vh / 2, 0), H * SS - vh)
        frame = img.crop((int(left), int(top), int(left + vw), int(top + vh))).resize((W, H), Image.LANCZOS)
        # screen-space overlays (never cropped by the camera push)
        sd = ImageDraw.Draw(frame)
        for b in scene["beats"]:
            if b["type"] != "title":
                continue
            a = min(1.0, beat_progress(b, t) * 1.4)
            if a <= 0:
                continue
            sd.text((90, 70), b["text"].upper(), font=s_title, fill=tuple(int(c * a) for c in st["text"]))
            if b.get("sub"):
                sd.text((92, 128), b["sub"], font=s_lab, fill=tuple(int(c * a) for c in st["ink"]))
        sd.text((90, H - 52), prov, font=s_cap, fill=tuple(int(c * 0.7) for c in st["text"]))
        proc.stdin.write(np.asarray(frame).tobytes())
    proc.stdin.close()
    proc.wait()
    return out


if __name__ == "__main__":
    render(json.loads(pathlib.Path(sys.argv[1]).read_text()), sys.argv[2])
