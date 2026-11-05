#!/usr/bin/env python3
"""Assemble the 10:56 continuous master: 98 slots in scripted order.

Slot order and durations come from /tmp/atlas_build/timeline.json (parsed from the
shot map and the delivery index). Plate slots use the delivered CRF-17 clips; the
49 graphic/photo slots use freshly rendered fill clips from the six worlds.

Uses the concat FILTER rather than the concat demuxer: stream-copy concatenation
silently drops ~0.05 s per join (measured 4.5 s over 98 joins), which would put the
master 4.5 s under the scripted 10:56:01. The filter concatenates decoded frames,
so the frame count lands exactly on 15,745.
"""
import json, pathlib, glob, subprocess, sys

FF = "/home/user/Wan2.2/.venv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v9.0.2"
BUILD = pathlib.Path("/tmp/atlas_build")
DRIVE = pathlib.Path("/home/user/Wan2.2/google_drive")
TARGET = BUILD / "atlas_understory_video01_FULL_10m56.mp4"
BITRATE = "1060k"


def build_inputs():
    tl = json.loads((BUILD / "timeline.json").read_text())
    fills = json.loads((BUILD / "fills.json").read_text())
    fill_by_shot = {f["shot"]: f for f in fills}
    paths, frames = [], 0
    for s in tl:
        if s["kind"] == "plate":
            hits = glob.glob(str(DRIVE / f"{s['shot']}_M*_1080p24.mp4"))
            assert len(hits) == 1, (s["shot"], hits)
            path = hits[0]
        else:
            f = fill_by_shot[s["shot"]]
            path = str(BUILD / "fills" / f"{f['name']}_{f['motion']}.mp4")
        assert pathlib.Path(path).exists(), path
        paths.append(path)
        frames += round(s["dur"] * 24)
    print(f"{len(paths)} slots, expected {frames} frames = {frames/24:.3f} s", flush=True)
    return paths


def run(cmd, label):
    print(label, flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:])
        raise SystemExit(f"ffmpeg failed ({r.returncode})")


def main() -> None:
    paths = build_inputs()
    n = len(paths)
    ins = []
    for p in paths:
        ins += ["-i", p]
    graph = "".join(f"[{i}:v]" for i in range(n)) + f"concat=n={n}:v=1:a=0[v]"
    common = [FF, "-y", "-loglevel", "error", *ins,
              "-filter_complex", graph, "-map", "[v]", "-an",
              "-c:v", "libx264", "-preset", "medium", "-b:v", BITRATE,
              "-maxrate", "1300k", "-bufsize", "2600k", "-pix_fmt", "yuv420p",
              "-profile:v", "high", "-r", "24", "-g", "48",
              "-passlogfile", str(BUILD / "x264pass")]
    run(common + ["-pass", "1", "-f", "null", "/dev/null"], "pass 1")
    run(common + ["-pass", "2", "-movflags", "+faststart", str(TARGET)], "pass 2")
    print("FINAL", TARGET, f"{TARGET.stat().st_size/1e6:.1f} MB", flush=True)


if __name__ == "__main__":
    main()
