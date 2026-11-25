#!/usr/bin/env python3
"""Normalise generated stills to 1920x1080 q92 JPG (letterbox auto-crop, centre 16:9 crop) and build a QC contact sheet.

  python tools/still_norm.py <stills_jpg dir> <contact_sheet.jpg> <png> [<png> ...]
Letterbox rows count as bars only when mean < 4 and std < 3; crop only if both bars exceed 8 px.
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw


def norm(f, outdir):
    im = Image.open(f).convert('RGB')
    a = np.asarray(im.convert('L'), float)
    rows = [(r.mean() < 4 and r.std() < 3) for r in a]
    top = next(i for i, v in enumerate(rows) if not v)
    bot = next(i for i, v in enumerate(rows[::-1]) if not v)
    if top > 8 and bot > 8:
        im = im.crop((0, top, im.width, im.height - bot))
    W, H = im.size
    tr = 16 / 9
    if W / H > tr:
        nw = int(H * tr); im = im.crop(((W - nw) // 2, 0, (W - nw) // 2 + nw, H))
    else:
        nh = int(W / tr); im = im.crop((0, (H - nh) // 2, W, (H - nh) // 2 + nh))
    im = im.resize((1920, 1080), Image.LANCZOS)
    im.save(os.path.join(outdir, os.path.basename(f).rsplit('.', 1)[0] + '.jpg'), quality=92)
    print(os.path.basename(f), W, H, top, bot)
    return im


if __name__ == '__main__':
    outdir, sheet_path, files = sys.argv[1], sys.argv[2], sys.argv[3:]
    sheet = Image.new('RGB', (1600, 450 * ((len(files) + 1) // 2)))
    for k, f in enumerate(files):
        t = norm(f, outdir).resize((800, 450))
        ImageDraw.Draw(t).text((8, 8), os.path.basename(f)[14:50], fill='yellow')
        sheet.paste(t, ((k % 2) * 800, (k // 2) * 450))
    sheet.save(sheet_path, quality=85)
