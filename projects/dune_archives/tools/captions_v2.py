#!/usr/bin/env python3
"""Burned-in captions for v2 renders (switched on per episode with D.BURN_CAPTIONS = True).

Spec (GOT003, approved script production notes):
  * max 2 lines x ~38 characters, each cue held 1-6 s, broken at sentence / clause boundaries and pauses
  * serif (Cormorant Garamond, OFL) in #F2E8D5 on a 55 % dark band, sitting in the lower 12 % of the frame
  * hidden during TITLE / IDENT / CHAPTER / END cards; lifted above lower-thirds (NAME / PLACE / YEAR / NOTE / STAT)
Cues are built from the timeline's word list (script spelling, spoken timing), so they always match the edit.

  EP=GOT003 python tools/captions_v2.py            # writes 22_edit/<EP>/<EP>_captions.json + prints stats
"""
import functools, json, pathlib, re, sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONT = ROOT / 'templates/fonts/CormorantGaramond-VF.ttf'
MAXC, MAXL, MIN_T, MAX_T = 38, 2, 1.0, 6.0
INK = (242, 232, 213)
HIDE = {'TITLE', 'IDENT', 'CHAPTER', 'END'}
LOWER = {'NAME', 'PLACE', 'YEAR', 'NOTE', 'STAT'}


def wrap(words):
    """Balanced 1-2 line wrap; returns list of lines or None if it can't fit."""
    txt = ' '.join(words)
    if len(txt) <= MAXC:
        return [txt]
    best = None
    for k in range(1, len(words)):
        a, b = ' '.join(words[:k]), ' '.join(words[k:])
        if len(a) <= MAXC and len(b) <= MAXC:
            sc = abs(len(a) - len(b)) - (6 if re.search(r'[,;:]$', words[k - 1]) else 0)
            if best is None or sc < best[0]:
                best = (sc, [a, b])
    return best[1] if best else None


def split(ws):
    """Split one sentence (list of (w, s, e)) into the fewest balanced parts that each fit 2x38 and <= 6 s,
    preferring clause boundaries (commas etc.) near the balanced cut points."""
    words = [w for w, _, _ in ws]
    if wrap(words) is not None and ws[-1][2] - ws[0][1] <= MAX_T:
        return [ws]
    n = 2
    while n <= len(ws):
        L = len(' '.join(words))
        parts, i0 = [], 0
        for p in range(1, n):
            target = L * p / n
            best = None
            for k in range(i0 + 1, len(ws)):
                pos = len(' '.join(words[:k]))
                sc = abs(pos - target) - (10 if re.search(r'[,;:]$', words[k - 1]) else 0)
                if best is None or sc < best[0]:
                    best = (sc, k)
            parts.append(ws[i0:best[1]]); i0 = best[1]
        parts.append(ws[i0:])
        if all(pt and wrap([w for w, _, _ in pt]) is not None and pt[-1][2] - pt[0][1] <= MAX_T for pt in parts):
            return parts
        n += 1
    return [[w] for w in ws]


def build(tl):
    W = tl['words']
    sents, cur = [], []
    for w, s, e in W:
        if cur and s - cur[-1][2] > 0.7:
            sents.append(cur); cur = []
        cur.append((w, s, e))
        if re.search(r'[.?!]["\u201d]?$', w):
            sents.append(cur); cur = []
    if cur:
        sents.append(cur)
    cues = []
    for se in sents:
        for pt in split(se):
            cues.append([pt[0][1], pt[-1][2], wrap([w for w, _, _ in pt])])
    # hold rules: end a touch after speech, at least MIN_T, never overlapping the next cue
    for i, c in enumerate(cues):
        nxt = cues[i + 1][0] if i + 1 < len(cues) else c[1] + 2
        c[1] = min(max(c[1] + 0.25, c[0] + MIN_T), nxt - 0.04, c[0] + MAX_T + 0.4)
    return [dict(t0=round(a, 3), t1=round(b, 3), lines=l) for a, b, l in cues]


@functools.lru_cache(None)
def font(px):
    f = ImageFont.truetype(str(FONT), px)
    try:
        f.set_variation_by_axes([560])
    except Exception:  # noqa
        pass
    return f


class Captions:
    def __init__(self, tl, W, H):
        self.cues, self.W, self.H, self.k = build(tl), W, H, H / 1080
        self.t0s = np.array([c['t0'] for c in self.cues])
        self.cache = {}

    def patch(self, i):
        if i not in self.cache:
            k = self.k
            f = font(int(round(44 * k)))
            lines = self.cues[i]['lines']
            lh = int(round(50 * k))
            tw = max(f.getbbox(s)[2] for s in lines)
            pw, ph = tw + int(56 * k), lh * len(lines) + int(22 * k)
            im = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
            d = ImageDraw.Draw(im)
            d.rounded_rectangle([0, 0, pw - 1, ph - 1], radius=int(10 * k), fill=(8, 6, 5, 140))  # 55 % band
            for j, s in enumerate(lines):
                d.text((pw / 2, int(11 * k) + lh * j + lh / 2), s, font=f, anchor='mm', fill=INK + (255,))
            self.cache[i] = np.asarray(im).astype(np.float32) / 255.0
        return self.cache[i]

    def apply(self, frame, tg, active_kinds):
        if active_kinds & HIDE:
            return frame
        i = int(np.searchsorted(self.t0s, tg, 'right')) - 1
        if i < 0 or tg >= self.cues[i]['t1']:
            return frame
        c = self.cues[i]
        a = min(1.0, (tg - c['t0']) / 0.12, (c['t1'] - tg) / 0.12)
        p = self.patch(i)
        ph, pw = p.shape[:2]
        bottom = self.H - int(round(26 * self.k)) - (int(round(150 * self.k)) if active_kinds & LOWER else 0)
        x0, y0 = (self.W - pw) // 2, bottom - ph
        reg = frame[y0:y0 + ph, x0:x0 + pw].astype(np.float32)
        al = p[..., 3:] * a
        frame[y0:y0 + ph, x0:x0 + pw] = (reg * (1 - al) + p[..., :3] * 255 * al).astype(np.uint8)
        return frame


if __name__ == '__main__':
    sys.path.insert(0, str(ROOT / 'tools'))
    import episode as E  # noqa: E402
    tl = json.load(open(E.TIMELINE))
    cues = build(tl)
    out = E.OUT / f'{E.TAG}_captions.json'
    out.write_text(json.dumps(cues, indent=0))
    d = [c['t1'] - c['t0'] for c in cues]
    print(f'{len(cues)} cues -> {out.name}; hold {min(d):.2f}-{max(d):.2f}s, mean {sum(d) / len(d):.2f}s; '
          f'max line {max(len(s) for c in cues for s in c["lines"])} chars; '
          f'3-line cues: {sum(len(c["lines"]) > 2 for c in cues)}; None: {sum(c["lines"] is None for c in cues)}')
