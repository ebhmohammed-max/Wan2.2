#!/usr/bin/env python3
"""Rebuild an episode with build_episode.py while PRESERVING all QC work.

build_episode.py regenerates every batch manifest and the batch index from the data module,
which wipes per-image QC fields, Drive IDs, batch statuses and the hand-written QC log.
This wrapper snapshots them first, rebuilds, then restores:
  * every image whose qc != PENDING keeps its old record (prompt included, since that is what generated it)
  * batch "status" strings are kept
  * the batch index file is kept verbatim
  * the combined ALL_BATCH_MANIFESTS.json is regenerated
Usage: python3 tools/rebuild_preserve.py dun003
"""
import json, pathlib, subprocess, sys

ep = sys.argv[1].lower()
EP = ep.upper()
root = pathlib.Path(__file__).resolve().parent.parent
bdir = root / "19_batches" / EP
snap = {f.name: json.loads(f.read_text()) for f in sorted(bdir.glob(f"{EP}_BATCH0*.json"))}
index = bdir / f"{EP}_BATCH_INDEX.md"
index_txt = index.read_text() if index.exists() else None

subprocess.run([sys.executable, str(root / "tools" / "build_episode.py"), ep], check=True,
               stdout=subprocess.DEVNULL, cwd=root)

kept = 0
for name, old in snap.items():
    f = bdir / name
    new = json.loads(f.read_text())
    olds = {i["scene_id"]: i for i in old["images"]}
    for i, im in enumerate(new["images"]):
        o = olds.get(im["scene_id"])
        if o and o.get("qc", "PENDING") != "PENDING":
            new["images"][i] = o
            kept += 1
    if old.get("status", "PENDING") != "PENDING":
        new["status"] = old["status"]
    f.write_text(json.dumps(new, indent=1, ensure_ascii=False))
if index_txt is not None:
    index.write_text(index_txt)
allm = [json.loads(f.read_text()) for f in sorted(bdir.glob(f"{EP}_BATCH0*.json"))]
(bdir / f"{EP}_ALL_BATCH_MANIFESTS.json").write_text(json.dumps(allm, indent=1, ensure_ascii=False))
print(f"rebuilt {EP}: {len(allm)} batches, {kept} QC'd image records preserved")
