#!/usr/bin/env python3
"""Read the v4 Shot Map workbook and emit per-batch clip manifests.

Every BACKGROUND PLATE row is one clip. Motion codes M02 / M03 / M08 are the
only recipes assigned to plates in v4; durations come straight from the sheet.
"""
import json, pathlib, re

import shutil, tempfile

import openpyxl

WB_RAW = pathlib.Path(__file__).resolve().parents[3] / "google_drive" / "10_Image_Budget_and_Shot_Map_v4_HANDOFF"
OUT = pathlib.Path(__file__).resolve().parents[1]


def main() -> None:
    # the Drive export lands without an .xlsx suffix; openpyxl needs one
    tmp = pathlib.Path(tempfile.gettempdir()) / "shotmap_v4.xlsx"
    shutil.copyfile(WB_RAW, tmp)
    wb = openpyxl.load_workbook(tmp, data_only=True)
    ws = wb["Shot Map"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = {h: i for i, h in enumerate(rows[0])}
    batches = {}
    for r in rows[1:]:
        if "PLATE" not in str(r[hdr["Visual type"]] or "").upper():
            continue
        shot = r[hdr["Shot ID"]]
        image = r[hdr["Image IDs"]]
        motion = str(r[hdr["Motion recipe (editor)"]])
        dur = float(r[hdr["Duration seconds"]])
        batch = int(float(r[hdr["Batch"]]))
        code = re.match(r"(M\d+)", motion).group(1)
        assert code in {"M02", "M03", "M08"}, (shot, motion)
        batches.setdefault(batch, []).append(
            {"shot": shot, "image": image, "motion": code, "duration": round(dur, 3),
             "class": r[hdr["Creation/use class"]]})
    for b, items in sorted(batches.items()):
        items.sort(key=lambda x: x["shot"])
        p = OUT / f"manifest_batch{b}.json"
        p.write_text(json.dumps(items, indent=1) + "\n")
        print(f"batch {b}: {len(items)} clips -> {p.name}")


if __name__ == "__main__":
    main()
