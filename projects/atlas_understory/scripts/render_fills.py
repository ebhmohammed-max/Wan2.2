#!/usr/bin/env python3
"""Render the 49 fill clips with 2 worker processes, skipping finished files."""
import json, os, sys, pathlib
from multiprocessing import Pool

sys.path.insert(0, "/home/user/Wan2.2/projects/atlas_understory/scripts")
from make_clips import render

STILLS = pathlib.Path("/tmp/atlas_build/fill_stills")
OUT = pathlib.Path("/tmp/atlas_build/fills")


def job(row):
    out = OUT / f"{row['shot']}_{row['motion']}.mp4"
    if out.exists() and out.stat().st_size > 100_000:
        return f"skip {out.name}"
    render(STILLS / f"{row['image']}.png", out, row["motion"], float(row["duration"]))
    return f"done {out.name}"


if __name__ == "__main__":
    man = json.loads(pathlib.Path("/tmp/atlas_build/fill_manifest.json").read_text())
    with Pool(2) as p:
        for msg in p.imap_unordered(job, man):
            print(msg, flush=True)
    print("FILLS_DONE", flush=True)
