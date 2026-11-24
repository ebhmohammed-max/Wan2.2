"""Motion-graphics layer for DUN003 v2 (transparent, drawn with PIL in 1080p design units).

layers(event, lt, k) -> list of (RGBA PIL image, x, y, opacity) for an event at local time lt (s).
k = output height / 1080. Static parts are cached per event (event['_c']); only animated parts are
redrawn per frame. Kinds: NAME PLACE YEAR NOTE STAT CHAPTER TITLE IDENT DOSSIER FILE SUB END.
No disclaimers or labels are drawn here: the publisher adds those at upload.
Fonts (templates/fonts, OFL/Apache): Cinzel, Montserrat, Cormorant Garamond Italic, Material Symbols subset.
"""
import functools, glob, math, pathlib, textwrap

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
FD = ROOT / 'templates/fonts'
STILLS = ROOT / '19_batches/DUN003/stills_jpg'
LOGO = ROOT / 'templates/brand/mythic_archives_logo.png'

GOLD = (228, 192, 122)
GOLD_D = (168, 128, 66)
IVORY = (246, 238, 222)
DIM = (206, 198, 182)
INK = (44, 32, 20)
STAMP = (176, 34, 28)
YT_RED = (255, 0, 0)
FILES = {'cinzel': 'Cinzel-VF.ttf', 'mont': 'Montserrat-VF.ttf', 'corm': 'CormorantGaramond-Italic-VF.ttf',
         'icon0': 'MaterialSymbolsRounded-icons-fill0.ttf', 'icon1': 'MaterialSymbolsRounded-icons-fill1.ttf'}
ICON = {'like': '\uf577', 'bell': '\ue7f5', 'bell_on': '\ue7f7', 'comment': '\ue253', 'comment_f': '\ue0cb'}


@functools.lru_cache(None)
def font(name, size, weight=None):
    f = ImageFont.truetype(str(FD / FILES[name]), max(6, int(round(size))))
    if weight and not name.startswith('icon'):
        try:
            f.set_variation_by_axes([weight])
        except Exception:  # noqa
            pass
    return f


def clamp(x, a=0.0, b=1.0):
    return a if x < a else b if x > b else x


def ease(x):
    x = clamp(x); return x * x * (3 - 2 * x)


def eout(x):
    x = clamp(x); return 1 - (1 - x) ** 3


def eback(x, s=1.7):
    x = clamp(x); x -= 1; return 1 + x * x * ((s + 1) * x + s)


def env(lt, dur, fi=0.5, fo=0.45):
    a = eout(lt / fi) if fi > 0 else 1.0
    b = eout((dur - lt) / fo) if fo > 0 else 1.0
    return min(a, b)


def tw(text, f, tr=0):
    if not tr:
        return f.getlength(text)
    return sum(f.getlength(c) for c in text) + tr * (len(text) - 1)


def put(d, x, y, text, f, fill, tr=0, align='l'):
    """Text on a baseline at y, optional tracking; align l / c / r relative to x."""
    w = tw(text, f, tr)
    if align == 'c':
        x -= w / 2
    elif align == 'r':
        x -= w
    if not tr:
        d.text((x, y), text, font=f, fill=fill, anchor='ls')
        return w
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill, anchor='ls')
        x += f.getlength(ch) + tr
    return w


def shadow(img, r=7, op=0.8, dy=2, color=(0, 0, 0)):
    a = img.split()[3].filter(ImageFilter.GaussianBlur(r)).point(lambda v: int(v * op))
    sh = Image.new('RGBA', img.size, color + (0,))
    sh.putalpha(a)
    if dy:
        sh = ImageChops.offset(sh, 0, dy)
    return Image.alpha_composite(sh, img)


def wrap(text, f, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if f.getlength(t) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def hgrad(w, h, a0, a1, color=(0, 0, 0), soft_y=0):
    """Horizontal alpha gradient band (a0 at left -> a1 at right), optional soft top/bottom edges."""
    x = np.linspace(a0, a1, w, dtype=np.float32)[None, :].repeat(h, 0)
    if a0 > a1 and h < 400:  # lower-third style band: fade in from the left edge too
        ramp = min(w // 6, 90)
        x[:, :ramp] *= np.linspace(0, 1, ramp, dtype=np.float32)[None, :]
    if soft_y:
        y = np.ones(h, np.float32)
        r = np.linspace(0, 1, soft_y, dtype=np.float32)
        y[:soft_y] = r; y[-soft_y:] = r[::-1]
        x *= y[:, None]
    im = Image.new('RGBA', (w, h), color + (0,))
    im.putalpha(Image.fromarray(np.clip(x, 0, 255).astype(np.uint8)))
    return im


def band(W, H, cy, hh, a, k):
    """Soft dark horizontal band across the frame (legibility behind centred titles)."""
    y = np.arange(H, dtype=np.float32)
    al = a * np.exp(-((y - cy) / hh) ** 2)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    im.putalpha(Image.fromarray(np.repeat(al[:, None], W, 1).astype(np.uint8)))
    return im


def flat(W, H, a):
    return Image.new('RGBA', (W, H), (0, 0, 0, int(a)))


def still_path(key):
    b, s = int(key[1:4]), int(key[5:8])
    hits = glob.glob(str(STILLS / f'DUN003_BATCH{b:03d}_SCENE{s:03d}_*'))
    return hits[0]


def crop_still(key, w, h, focus=(0.5, 0.5)):
    im = Image.open(still_path(key)).convert('RGB')
    W0, H0 = im.size
    ar = w / h
    if W0 / H0 > ar:
        cw, ch = int(H0 * ar), H0
    else:
        cw, ch = W0, int(W0 / ar)
    cx, cy = focus[0] * W0, focus[1] * H0
    x0 = int(clamp(cx - cw / 2, 0, W0 - cw)); y0 = int(clamp(cy - ch / 2, 0, H0 - ch))
    return im.crop((x0, y0, x0 + cw, y0 + ch)).resize((int(w), int(h)), Image.LANCZOS)


@functools.lru_cache(None)
def logo(size):
    return Image.open(LOGO).convert('RGBA').resize((int(size), int(size)), Image.LANCZOS)


def cursor(k):
    s = 1.0 * k
    pts = [(0, 0), (0, 40), (10, 31), (17, 47), (24, 44), (17, 29), (30, 29)]
    im = Image.new('RGBA', (int(40 * s) + 6, int(54 * s) + 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    P = [(3 + x * s, 3 + y * s) for x, y in pts]
    d.polygon(P, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    d.line(P + [P[0]], fill=(0, 0, 0, 255), width=max(1, int(2 * s)))
    return shadow(im, r=3 * k, op=0.6, dy=2)


def pill(w, h, fill, k):
    im = Image.new('RGBA', (int(w), int(h)), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, int(w) - 1, int(h) - 1), radius=int(h / 2), fill=fill)
    return im


def scaled(img, s):
    if abs(s - 1) < 1e-3:
        return img, 0, 0
    w, h = img.size
    nw, nh = max(1, int(w * s)), max(1, int(h * s))
    return img.resize((nw, nh), Image.BILINEAR), (w - nw) / 2, (h - nh) / 2


# --------------------------------------------------------------------------- kinds
def _name(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'img' not in c:
        lw, lh = int(1100 * k), int(170 * k)
        im = hgrad(lw, lh, 175, 0, soft_y=int(40 * k))
        d = ImageDraw.Draw(im)
        d.rectangle((int(40 * k), int(34 * k), int(45 * k), int(128 * k)), fill=GOLD + (255,))
        put(d, 66 * k, 88 * k, p['name'], font('cinzel', 50 * k, 650), IVORY, tr=3 * k)
        put(d, 68 * k, 124 * k, p['role'].upper(), font('mont', 22 * k, 560), GOLD, tr=2.6 * k)
        c['img'] = shadow(im, r=5 * k, op=0.55)
    img = c['img']
    rev = eout(lt / 0.6)
    w = max(1, int(img.width * rev))
    return [(img.crop((0, 0, w, img.height)), 70 * k, H - 250 * k, env(lt, dur, 0.15, 0.45))]


def _place(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'img' not in c:
        lw, lh = int(1000 * k), int(150 * k)
        im = hgrad(lw, lh, 140, 0, soft_y=int(36 * k))
        d = ImageDraw.Draw(im)
        cx, cy, r = 32 * k, 62 * k, 9 * k
        d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=GOLD + (255,))
        w = put(d, 56 * k, 78 * k, p['place'], font('cinzel', 44 * k, 600), IVORY, tr=8 * k)
        d.rectangle((int(57 * k), int(90 * k), int(57 * k + w), int(92 * k)), fill=GOLD + (230,))
        put(d, 58 * k, 120 * k, p.get('sub', '').upper(), font('mont', 20 * k, 520), DIM, tr=3 * k)
        c['img'] = shadow(im, r=5 * k, op=0.55)
    img = c['img']
    w = max(1, int(img.width * eout(lt / 0.6)))
    return [(img.crop((0, 0, w, img.height)), 64 * k, 56 * k, env(lt, dur, 0.15, 0.45))]


def _year(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'img' not in c:
        lw, lh = int(1400 * k), int(190 * k)
        im = Image.new('RGBA', (lw, lh), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        fy = font('cinzel', 66 * k, 700)
        w = put(d, lw / 2, 92 * k, p['year'], fy, GOLD, tr=5 * k, align='c')
        for sgn in (-1, 1):
            x0 = lw / 2 + sgn * (w / 2 + 30 * k); x1 = lw / 2 + sgn * (w / 2 + 170 * k)
            d.line((min(x0, x1), 66 * k, max(x0, x1), 66 * k), fill=GOLD + (220,), width=max(1, int(2 * k)))
        put(d, lw / 2, 140 * k, p.get('sub', '').upper(), font('mont', 23 * k, 560), IVORY, tr=4.5 * k, align='c')
        c['img'] = shadow(im, r=8 * k, op=0.9)
    a = env(lt, dur, 0.55, 0.5)
    return [(c['img'], (W - c['img'].width) / 2, 40 * k - 14 * k * (1 - eout(lt / 0.6)), a)]


def _note(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'img' not in c:
        pw = int(600 * k)
        fb = font('corm', 32 * k, 520)
        lines = wrap(p['body'], fb, pw - 70 * k)
        ph = int((168 + 40 * len(lines) + 26) * k)
        im = Image.new('RGBA', (pw + int(24 * k), ph + int(24 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        o = int(12 * k)
        d.rounded_rectangle((o, o, o + pw, o + ph), radius=int(8 * k), fill=(10, 9, 8, 196),
                            outline=GOLD + (210,), width=max(1, int(2 * k)))
        for (x, y, sx, sy) in ((o, o, 1, 1), (o + pw, o, -1, 1), (o, o + ph, 1, -1), (o + pw, o + ph, -1, -1)):
            d.line((x, y + sy * 26 * k, x, y, x + sx * 26 * k, y), fill=GOLD + (255,), width=max(2, int(4 * k)))
        put(d, o + 34 * k, o + 52 * k, 'ARCHIVE NOTE', font('mont', 17 * k, 650), GOLD, tr=5 * k)
        put(d, o + 34 * k, o + 104 * k, p['head'], font('cinzel', 34 * k, 700), IVORY, tr=1.5 * k)
        d.line((o + 34 * k, o + 124 * k, o + 140 * k, o + 124 * k), fill=GOLD + (230,), width=max(1, int(2 * k)))
        y = o + 166 * k
        for ln in lines:
            put(d, o + 34 * k, y, ln, fb, IVORY)
            y += 40 * k
        c['img'] = shadow(im, r=10 * k, op=0.6, dy=4)
    s = eout(lt / 0.55)
    return [(c['img'], W - c['img'].width - 96 * k + 50 * k * (1 - s), 150 * k, env(lt, dur, 0.45, 0.45))]


def _fmt(v):
    return f'{int(round(v)):,}'


def _stat(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'lab' not in c:
        lw = int(1500 * k)
        im = Image.new('RGBA', (lw, int(150 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        put(d, lw / 2, 50 * k, p['label'], font('mont', 32 * k, 720), GOLD, tr=12 * k, align='c')
        if p.get('sub'):
            put(d, lw / 2, 104 * k, p['sub'], font('corm', 34 * k, 560), IVORY, align='c')
        c['lab'] = shadow(im, r=8 * k, op=0.95)
        c['bg'] = band(W, H, 610 * k, 190 * k, 120, k)
        c['last'] = None
    v = p['value'] * eout(lt / 1.25)
    txt = _fmt(v)
    if c['last'] != txt:
        f = font('cinzel', 124 * k, 800)
        nw = int(tw(txt, f, 2 * k) + 60 * k)
        im = Image.new('RGBA', (nw, int(170 * k)), (0, 0, 0, 0))
        put(ImageDraw.Draw(im), nw / 2, 135 * k, txt, f, IVORY, tr=2 * k, align='c')
        c['num'] = shadow(shadow(im, r=16 * k, op=0.55, dy=0, color=GOLD_D), r=6 * k, op=0.9)
        c['last'] = txt
    a = env(lt, dur, 0.3, 0.35)
    n = c['num']
    return [(c['bg'], 0, 0, a), (n, (W - n.width) / 2, 470 * k, a),
            (c['lab'], (W - c['lab'].width) / 2, 650 * k, a * eout((lt - 0.2) / 0.4))]


def _chapter(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'top' not in c:
        lw = int(1200 * k)
        im = Image.new('RGBA', (lw, int(80 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        w = put(d, lw / 2, 50 * k, f"CHAPTER {p['num']}", font('mont', 26 * k, 640), GOLD, tr=16 * k, align='c')
        for sgn in (-1, 1):
            x0 = lw / 2 + sgn * (w / 2 + 28 * k); x1 = lw / 2 + sgn * (w / 2 + 150 * k)
            d.line((min(x0, x1), 41 * k, max(x0, x1), 41 * k), fill=GOLD + (220,), width=max(1, int(2 * k)))
        c['top'] = shadow(im, r=6 * k, op=0.9)
        c['bg'] = band(W, H, 545 * k, 210 * k, 150, k)
        c['tt'] = {}
    tr = (4 + 5 * ease(lt / dur)) * k
    key = round(tr * 4)
    if key not in c['tt']:
        f = font('cinzel', 86 * k, 700)
        title = p['title'].upper()
        nw = int(tw(title, f, tr) + 80 * k)
        im = Image.new('RGBA', (nw, int(140 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        put(d, nw / 2, 100 * k, title, f, IVORY, tr=tr, align='c')
        cx, cy, r = nw / 2, 128 * k, 6 * k
        d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=GOLD + (255,))
        c['tt'] = {key: shadow(im, r=8 * k, op=0.9)}
    t_img = c['tt'][key]
    a = env(lt, dur, 0.6, 0.6)
    return [(c['bg'], 0, 0, a), (c['top'], (W - c['top'].width) / 2, 420 * k, a),
            (t_img, (W - t_img.width) / 2, 490 * k + 10 * k * (1 - eout(lt / 0.8)), a * eout((lt - 0.15) / 0.6))]


def _title(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'kick' not in c:
        lw = int(1600 * k)
        im = Image.new('RGBA', (lw, int(70 * k)), (0, 0, 0, 0))
        put(ImageDraw.Draw(im), lw / 2, 46 * k, p['kicker'], font('mont', 25 * k, 620), GOLD, tr=13 * k, align='c')
        c['kick'] = shadow(im, r=6 * k, op=0.9)
        im = Image.new('RGBA', (lw, int(90 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        put(d, lw / 2, 56 * k, p['sub'], font('corm', 50 * k, 600), IVORY, align='c')
        c['sub'] = shadow(im, r=7 * k, op=0.95)
        c['bg'] = band(W, H, 545 * k, 260 * k, 150, k)
        c['tt'] = {}
    tr = (8 + 16 * ease(lt / dur)) * k
    key = round(tr * 3)
    if key not in c['tt']:
        f = font('cinzel', 148 * k, 900)
        nw = int(tw(p['title'], f, tr) + 100 * k)
        im = Image.new('RGBA', (nw, int(200 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        put(d, nw / 2, 160 * k, p['title'], f, IVORY, tr=tr, align='c')
        d.line((nw / 2 - 180 * k, 190 * k, nw / 2 + 180 * k, 190 * k), fill=GOLD + (230,), width=max(1, int(2 * k)))
        c['tt'] = {key: shadow(shadow(im, r=22 * k, op=0.5, dy=0, color=GOLD_D), r=8 * k, op=0.9)}
    t_img = c['tt'][key]
    out = eout((dur - lt) / 0.8)
    return [(c['bg'], 0, 0, min(eout(lt / 0.8), out)),
            (c['kick'], (W - c['kick'].width) / 2, 352 * k, min(eout(lt / 0.8), out)),
            (t_img, (W - t_img.width) / 2, 410 * k, min(eout((lt - 0.4) / 1.2), out)),
            (c['sub'], (W - c['sub'].width) / 2, 618 * k, min(eout((lt - 1.3) / 0.9), out))]


def _ident(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'txt' not in c:
        lw = int(1500 * k)
        im = Image.new('RGBA', (lw, int(220 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        put(d, lw / 2, 66 * k, p['title'], font('cinzel', 64 * k, 700), IVORY, tr=10 * k, align='c')
        put(d, lw / 2, 120 * k, p['tag'], font('mont', 22 * k, 560), GOLD, tr=6 * k, align='c')
        d.line((lw / 2 - 60 * k, 148 * k, lw / 2 + 60 * k, 148 * k), fill=GOLD + (200,), width=max(1, int(2 * k)))
        put(d, lw / 2, 190 * k, p['sub'], font('mont', 19 * k, 600), DIM, tr=6 * k, align='c')
        c['txt'] = shadow(im, r=7 * k, op=0.95)
        g = Image.new('RGBA', (int(560 * k), int(560 * k)), GOLD_D + (0,))
        m = Image.new('L', g.size, 0)
        ImageDraw.Draw(m).ellipse((int(110 * k), int(110 * k), int(450 * k), int(450 * k)), fill=120)
        g.putalpha(m.filter(ImageFilter.GaussianBlur(50 * k)))
        c['glow'] = g
        c['logo'] = shadow(logo(int(270 * k)), r=14 * k, op=0.8, dy=4)
        c['bgf'] = flat(W, H, 150)
    s = 0.86 + 0.14 * eout(lt / 1.3)
    L, ox, oy = scaled(c['logo'], s)
    out = eout((dur - lt) / 0.6)
    a_logo = min(eout(lt / 0.6), out)
    pulse = 0.75 + 0.25 * math.sin(lt * 2.2)
    cx, cy = W / 2, 370 * k
    return [(c['bgf'], 0, 0, min(eout(lt / 0.5), out)),
            (c['glow'], cx - c['glow'].width / 2, cy - c['glow'].height / 2, a_logo * pulse),
            (L, cx - c['logo'].width / 2 + ox, cy - c['logo'].height / 2 + oy, a_logo),
            (c['txt'], (W - c['txt'].width) / 2, 540 * k, min(eout((lt - 0.6) / 0.8), out))]


def _card(key, focus, name, sub, k, border, bw):
    cw, ph = int(250 * k), int(300 * k)
    im = Image.new('RGBA', (cw + int(20 * k), ph + int(110 * k)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    o = int(10 * k)
    d.rectangle((o - bw, o - bw, o + cw + bw - 1, o + ph + bw - 1), fill=border + (255,))
    im.paste(crop_still(key, cw, ph, focus), (o, o))
    d.rectangle((o, o + ph - int(4 * k), o + cw, o + ph), fill=border + (255,))
    put(d, o + cw / 2, o + ph + 44 * k, name, font('cinzel', 30 * k, 700), IVORY, tr=2 * k, align='c')
    if sub:
        put(d, o + cw / 2, o + ph + 74 * k, sub, font('mont', 15 * k, 640), border, tr=3 * k, align='c')
    return shadow(im, r=10 * k, op=0.75, dy=4)


def _dossier(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'cards' not in c:
        c['cards'] = [_card(kk, f, n, s, k, GOLD, max(2, int(3 * k))) for kk, n, s, f in p['cards']]
        tk, tn, tf = p['target']
        c['target'] = _card(tk, tf, tn, 'THE TARGET', k, (214, 58, 46), max(3, int(5 * k)))
        st = Image.new('RGBA', (int(300 * k), int(110 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(st)
        d.rectangle((int(6 * k), int(6 * k), int(294 * k), int(104 * k)), outline=(214, 58, 46, 235), width=max(3, int(6 * k)))
        put(d, 150 * k, 76 * k, 'TARGET', font('mont', 50 * k, 850), (214, 58, 46), tr=6 * k, align='c')
        c['stamp'] = st.rotate(-12, expand=True, resample=Image.BICUBIC)
        c['bg'] = flat(W, H, 165)
        hd = Image.new('RGBA', (int(1500 * k), int(80 * k)), (0, 0, 0, 0))
        put(ImageDraw.Draw(hd), 750 * k, 50 * k, 'FOUR POWERS · ONE TARGET', font('mont', 26 * k, 680), GOLD,
            tr=12 * k, align='c')
        c['head'] = shadow(hd, r=6 * k, op=0.9)
    cw = c['cards'][0].width
    gap, agap = 26 * k, 110 * k
    total = 5 * cw + 3 * gap + agap
    x0, y0 = (W - total) / 2, 300 * k
    out = eout((dur - lt) / 0.5)
    L = [(c['bg'], 0, 0, min(eout(lt / 0.4), out)), (c['head'], (W - c['head'].width) / 2, 190 * k,
                                                     min(eout((lt - 0.1) / 0.5), out))]
    for i, card in enumerate(c['cards']):
        t0 = 0.25 + 0.32 * i
        s = eout((lt - t0) / 0.4)
        L.append((card, x0 + i * (cw + gap), y0 + 30 * k * (1 - s), min(s, out)))
    ta = 0.25 + 0.32 * 4 + 0.25
    xa = x0 + 4 * cw + 3 * gap
    # arrow
    s = eout((lt - ta + 0.2) / 0.4)
    if s > 0:
        ar = Image.new('RGBA', (int(agap), int(60 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(ar)
        ln = (agap - 30 * k) * s
        d.line((10 * k, 30 * k, 10 * k + ln, 30 * k), fill=GOLD + (255,), width=max(2, int(4 * k)))
        d.polygon([(10 * k + ln, 14 * k), (10 * k + ln + 18 * k, 30 * k), (10 * k + ln, 46 * k)], fill=GOLD + (255,))
        L.append((ar, xa, y0 + 150 * k, out))
    st = eout((lt - ta) / 0.4)
    L.append((c['target'], xa + agap, y0 + 30 * k * (1 - st), min(st, out)))
    ts = lt - ta - 0.45
    if ts > 0:
        sc = 1.0 + 0.6 * (1 - eout(ts / 0.18))
        S, ox, oy = scaled(c['stamp'], sc)
        L.append((S, xa + agap + cw / 2 - c['stamp'].width / 2 + ox, y0 + 90 * k + oy, min(eout(ts / 0.12), out)))
    return L


def _paper(w, h, k, seed=7):
    rng = np.random.default_rng(seed)
    base = np.zeros((h, w, 3), np.float32) + np.array([224, 210, 182], np.float32)
    n = rng.standard_normal((h // 4 + 1, w // 4 + 1)).astype(np.float32)
    n = np.array(Image.fromarray(((n * 20) + 128).clip(0, 255).astype(np.uint8)).resize((w, h), Image.BICUBIC),
                 np.float32) - 128
    base += n[..., None] * 0.35
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    v = ((xx / w - 0.5) ** 2 + (yy / h - 0.5) ** 2)
    base *= (1 - 0.55 * v)[..., None]
    im = Image.fromarray(base.clip(0, 255).astype(np.uint8)).convert('RGBA')
    return im


def _file(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    pw, ph = int(720 * k), int(800 * k)
    if 'panel' not in c:
        im = _paper(pw, ph, k)
        d = ImageDraw.Draw(im)
        put(d, 40 * k, 56 * k, 'THE MYTHIC ARCHIVES', font('mont', 17 * k, 640), INK, tr=4 * k)
        put(d, pw - 40 * k, 56 * k, 'SUBJECT FILE', font('mont', 17 * k, 760), STAMP, tr=4 * k, align='r')
        d.line((40 * k, 72 * k, pw - 40 * k, 72 * k), fill=INK + (200,), width=max(1, int(2 * k)))
        put(d, 40 * k, 134 * k, p['title'], font('cinzel', 50 * k, 800), INK, tr=2 * k)
        ph_ = crop_still(p['img'], int(250 * k), int(300 * k), p.get('focus', (0.5, 0.5)))
        fr = Image.new('RGBA', (int(270 * k), int(320 * k)), (250, 248, 240, 255))
        fr.paste(ph_, (int(10 * k), int(10 * k)))
        fr = shadow(fr.rotate(-2.5, expand=True, resample=Image.BICUBIC), r=6 * k, op=0.5, dy=3)
        im.alpha_composite(fr, (int(36 * k), int(160 * k)))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((int(70 * k), int(146 * k), int(92 * k), int(214 * k)), radius=int(10 * k),
                            outline=(120, 120, 124, 255), width=max(2, int(4 * k)))
        d.line((40 * k, 512 * k, pw - 40 * k, 512 * k), fill=INK + (160,), width=max(1, int(1 * k)))
        c['panel'] = shadow(im, r=16 * k, op=0.7, dy=6)
        st = Image.new('RGBA', (int(330 * k), int(130 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(st)
        d.rectangle((int(6 * k), int(6 * k), int(324 * k), int(124 * k)), outline=STAMP + (220,), width=max(3, int(7 * k)))
        put(d, 165 * k, 92 * k, p['stamp'], font('mont', 70 * k, 850), STAMP + (220,), tr=8 * k, align='c')
        c['stamp'] = st.rotate(12, expand=True, resample=Image.BICUBIC)
        c['fields'] = {}
    s = eout(lt / 0.6)
    out = eout((dur - lt) / 0.5)
    x = W - pw - 70 * k + 140 * k * (1 - s)
    y = 150 * k
    L = [(c['panel'], x - 16 * k, y - 16 * k, min(eout(lt / 0.4), out))]
    # typed fields
    state = []
    for i, (lab, val) in enumerate(p['fields']):
        t0 = 1.5 + 0.9 * i
        n = int(clamp((lt - t0) * 34, 0, len(val)))
        state.append(n if lt >= t0 else -1)
    key = tuple(state)
    if key not in c['fields']:
        fi = Image.new('RGBA', (pw, int(290 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(fi)
        for i, ((lab, val), n) in enumerate(zip(p['fields'], state)):
            if n < 0:
                continue
            yy = 40 * k + i * 50 * k
            put(d, 40 * k, yy, lab, font('mont', 17 * k, 760), STAMP, tr=3 * k)
            put(d, 200 * k, yy, val[:n], font('mont', 25 * k, 540), INK)
        c['fields'] = {key: fi}
    L.append((c['fields'][key], x, y + 520 * k, out))
    ts = lt - 0.9
    if ts > 0:
        sc = 1.0 + 0.7 * (1 - eout(ts / 0.18))
        S, ox, oy = scaled(c['stamp'], sc)
        L.append((S, x + 345 * k + ox, y + 230 * k + oy, min(eout(ts / 0.1), out)))
    return L


def _button_sub(state, k, press=1.0):
    """state 0 = Subscribe (red), 1 = Subscribed (grey + bell)."""
    w, h = 250 * k, 70 * k
    if state == 0:
        b = pill(w, h, YT_RED + (255,), k)
        put(ImageDraw.Draw(b), w / 2, h / 2 + 11 * k, 'Subscribe', font('mont', 29 * k, 700), (255, 255, 255), align='c')
    else:
        b = pill(w, h, (48, 48, 48, 255), k)
        d = ImageDraw.Draw(b)
        put(d, w / 2 + 20 * k, h / 2 + 11 * k, 'Subscribed', font('mont', 27 * k, 650), (236, 236, 236), align='c')
        d.text((22 * k, h / 2), ICON['bell_on'], font=font('icon1', 34 * k), fill=(236, 236, 236), anchor='lm')
    return scaled(b, press)


def _sub(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    cw, ch = int(1000 * k), int(170 * k)
    if 'card' not in c:
        im = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, cw - 1, ch - 1), radius=int(30 * k), fill=(16, 16, 16, 232),
                            outline=(255, 255, 255, 40), width=max(1, int(2 * k)))
        im.alpha_composite(logo(int(124 * k)), (int(26 * k), int(23 * k)))
        put(d, 172 * k, 80 * k, 'The Mythic Archives', font('mont', 40 * k, 720), (255, 255, 255))
        put(d, 174 * k, 120 * k, '@TheRealMythicArchives', font('mont', 21 * k, 520),
            (170, 170, 170))
        c['card'] = shadow(im, r=14 * k, op=0.7, dy=5)
        c['cur'] = cursor(k)
    s = eout(lt / 0.5)
    out = eout((dur - lt) / 0.5)
    a = min(eout(lt / 0.4), out)
    X, Y = (W - cw) / 2, H - ch - 90 * k + 60 * k * (1 - s)
    L = [(c['card'], X - 14 * k, Y - 14 * k, a)]
    ca, ba = p['click_at'], p.get('bell_at', p['click_at'] + 2)
    bx, by = X + cw - 250 * k - 120 * k, Y + 50 * k
    press = 1.0 - 0.07 * (1 - abs(clamp((lt - ca) / 0.08, -1, 1)))
    B, ox, oy = _button_sub(1 if lt >= ca + 0.06 else 0, k, press)
    L.append((B, bx + ox, by + oy, a))
    # bell
    ring = lt >= ba
    ang = 0.0
    if ring:
        q = lt - ba
        ang = 18 * math.sin(q * 26) * math.exp(-q * 3.2)
    bi = Image.new('RGBA', (int(70 * k), int(70 * k)), (0, 0, 0, 0))
    ImageDraw.Draw(bi).text((35 * k, 35 * k), ICON['bell_on' if ring else 'bell'], font=font('icon1' if ring else 'icon0', 50 * k),
                            fill=(255, 255, 255), anchor='mm')
    if ang:
        bi = bi.rotate(ang, resample=Image.BICUBIC, center=(35 * k, 12 * k))
    L.append((bi, X + cw - 100 * k, Y + 50 * k, a))
    # click ripple
    for t_click, (px, py) in ((ca, (bx + 125 * k, by + 35 * k)), (ba, (X + cw - 65 * k, Y + 85 * k))):
        q = lt - t_click
        if 0 <= q < 0.4:
            r = int(10 * k + 60 * k * eout(q / 0.4))
            rp = Image.new('RGBA', (2 * r + 4, 2 * r + 4), (0, 0, 0, 0))
            ImageDraw.Draw(rp).ellipse((2, 2, 2 * r + 2, 2 * r + 2), outline=(255, 255, 255, 200), width=max(2, int(4 * k)))
            L.append((rp, px - r - 2, py - r - 2, 1 - q / 0.4))
    # cursor path: enter -> subscribe button -> bell -> away
    p0 = (X + cw + 160 * k, Y + ch + 140 * k)
    p1 = (bx + 140 * k, by + 40 * k)
    p2 = (X + cw - 62 * k, Y + 90 * k)
    if ca - 1.2 <= lt <= ba + 0.9:
        if lt < ca - 0.15:
            u = eout((lt - (ca - 1.2)) / 1.05); P = (p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u)
        elif lt < ba - 0.6:
            P = p1
        elif lt < ba - 0.1:
            u = ease((lt - (ba - 0.6)) / 0.5); P = (p1[0] + (p2[0] - p1[0]) * u, p1[1] + (p2[1] - p1[1]) * u)
        else:
            P = p2
        ca_ = min(eout((lt - (ca - 1.2)) / 0.3), eout((ba + 0.9 - lt) / 0.3))
        L.append((c['cur'], P[0], P[1], min(ca_, a)))
    return L


def _end(e, lt, k, W, H):
    c, p, dur = e['_c'], e['p'], e['t1'] - e['t0']
    if 'bg' not in c:
        c['bg'] = hgrad(int(1250 * k), H, 215, 0)
        im = Image.new('RGBA', (int(1000 * k), int(150 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        im.alpha_composite(logo(int(104 * k)), (0, int(18 * k)))
        put(d, 126 * k, 70 * k, 'THE MYTHIC ARCHIVES', font('cinzel', 36 * k, 700), IVORY, tr=4 * k)
        put(d, 128 * k, 106 * k, p['brand'], font('mont', 18 * k, 640), GOLD, tr=5 * k)
        c['brand'] = shadow(im, r=6 * k, op=0.9)
        im = Image.new('RGBA', (int(1100 * k), int(220 * k)), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        put(d, 0, 44 * k, p['kicker'], font('mont', 24 * k, 640), GOLD, tr=12 * k)
        put(d, 0, 132 * k, p['title'], font('cinzel', 78 * k, 800), IVORY, tr=3 * k)
        d.line((0, 158 * k, 160 * k, 158 * k), fill=GOLD + (230,), width=max(1, int(2 * k)))
        put(d, 0, 200 * k, 'Record 004  ·  coming to the archive', font('corm', 34 * k, 560), DIM)
        c['next'] = shadow(im, r=8 * k, op=0.9)
        im = Image.new('RGBA', (int(1100 * k), int(110 * k)), (0, 0, 0, 0))
        put(ImageDraw.Draw(im), 0, 76 * k, 'HERO — OR TYRANT?', font('cinzel', 62 * k, 800), IVORY, tr=3 * k)
        c['q'] = shadow(shadow(im, r=18 * k, op=0.5, dy=0, color=GOLD_D), r=7 * k, op=0.9)
        c['cur'] = cursor(k)
    L = [(c['bg'], 0, 0, eout(lt / 0.8)),
         (c['brand'], 100 * k, 70 * k, eout((lt - 0.2) / 0.8)),
         (c['next'], 110 * k, 300 * k + 16 * k * (1 - eout((lt - 0.5) / 0.8)), eout((lt - 0.5) / 0.8))]
    qa = p['q_at']
    if lt >= qa:
        L.append((c['q'], 110 * k, 580 * k + 12 * k * (1 - eout((lt - qa) / 0.6)), eout((lt - qa) / 0.6)))
    # buttons: like, comment, subscribe (each pops on its word)
    y = 740 * k
    x = 110 * k
    for kind, t_on in (('like', p['like_at']), ('comment', p['comment_at']), ('sub', p['sub_at'])):
        q = lt - t_on
        if kind == 'sub':
            w = 250 * k
        else:
            w = 230 * k
        if q >= 0:
            s = eback(q / 0.45)
            if kind == 'sub':
                clicked = lt >= t_on + 1.3
                press = 1.0 - 0.07 * (1 - abs(clamp((lt - t_on - 1.25) / 0.08, -1, 1)))
                B, ox, oy = _button_sub(1 if clicked else 0, k, press)
            else:
                filled = kind == 'like' and q > 0.55
                B = pill(w, 70 * k, (255, 255, 255, 235) if filled else (32, 32, 32, 235), k)
                d = ImageDraw.Draw(B)
                col = (15, 15, 15) if filled else (255, 255, 255)
                ic = ICON['like'] if kind == 'like' else (ICON['comment'])
                d.text((26 * k, 35 * k), ic, font=font('icon1' if filled else 'icon0', 40 * k), fill=col, anchor='lm')
                put(d, 82 * k, 46 * k, 'Like' if kind == 'like' else 'Comment', font('mont', 28 * k, 700), col)
                ox = oy = 0
            S, sx, sy = scaled(B, max(0.05, s))
            L.append((S, x + sx + ox, y + sy + oy, clamp(q / 0.2)))
            if kind == 'sub' and t_on + 0.2 <= lt <= t_on + 2.2:
                P0 = (x + 420 * k, y + 260 * k); P1 = (x + 140 * k, y + 42 * k)
                u = eout((lt - t_on - 0.2) / 0.95)
                P = (P0[0] + (P1[0] - P0[0]) * u, P0[1] + (P1[1] - P0[1]) * u)
                L.append((c['cur'], P[0], P[1], min(clamp((lt - t_on - 0.2) / 0.2), clamp((t_on + 2.2 - lt) / 0.3))))
        x += w + 24 * k
    return L


KINDS = {'NAME': _name, 'PLACE': _place, 'YEAR': _year, 'NOTE': _note, 'STAT': _stat, 'CHAPTER': _chapter,
         'TITLE': _title, 'IDENT': _ident, 'DOSSIER': _dossier, 'FILE': _file, 'SUB': _sub, 'END': _end}


def layers(e, lt, k, W, H):
    e.setdefault('_c', {})
    return KINDS[e['kind']](e, lt, k, W, H)


def composite(frame, L):
    """Alpha-composite PIL RGBA layers onto an RGB uint8 numpy frame in place."""
    H, W = frame.shape[:2]
    for img, x, y, op in L:
        if op <= 0.003 or img is None:
            continue
        x, y = int(round(x)), int(round(y))
        w, h = img.size
        x0, y0, x1, y1 = max(0, x), max(0, y), min(W, x + w), min(H, y + h)
        if x1 <= x0 or y1 <= y0:
            continue
        a = np.asarray(img)[y0 - y:y1 - y, x0 - x:x1 - x]
        al = a[..., 3:4].astype(np.float32) * (op / 255.0)
        if not al.any():
            continue
        reg = frame[y0:y1, x0:x1].astype(np.float32)
        frame[y0:y1, x0:x1] = (reg + (a[..., :3].astype(np.float32) - reg) * al).astype(np.uint8)
    return frame
