#!/usr/bin/env python3
"""GOT003 code-animated maps (M01-M12) and in-world document mockups (K01-K19).

Base art is text-free (19_batches/GOT003/maps_base/*.jpg, generated); EVERYTHING readable - names, routes,
pins, sigil shields, handwriting, strikes, stamps - is drawn here, so nothing is ever misspelled by an image model.

Beats are timed to the narration: a cue is either seconds from the shot start (float) or a spoken word
('Winterfell', 'Vale#2' = 2nd occurrence, 'dragon+0.4' = offset) resolved against GOT003_timeline.json words
inside that shot's window. Clip length = the shot's on-screen length (+0.4 s), so render_v2.py streams it 1:1.

  EP=GOT003 python tools/got003_maps.py            # render all to 19_batches/GOT003/maps/
  EP=GOT003 python tools/got003_maps.py M02 K09    # render some
  EP=GOT003 python tools/got003_maps.py --frames M02   # QC contact sheet only (6 frames), no mp4
"""
import functools, json, math, os, pathlib, re, subprocess, sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'data'))
import got003 as D  # noqa: E402

try:
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # pragma: no cover
    FF = 'ffmpeg'

BASE = ROOT / '19_batches/GOT003/maps_base'
OUT = ROOT / '19_batches/GOT003/maps'
FD = ROOT / 'templates/fonts'
TL = json.load(open(ROOT / '22_edit/GOT003/GOT003_timeline.json'))
W, H, FPS, SS = 1920, 1080, 24, 1.5

INK = (52, 34, 18)
BROWN = (96, 62, 30)
RED = (150, 22, 18)
BLOOD = (120, 10, 10)
GOLD = (196, 150, 60)
GREEN = (40, 110, 52)
BLACK = (18, 14, 12)
HALO = (238, 224, 190)
WF = (78, 140, 70)          # wildfire green
PROV_MAP = 'SCHEMATIC  ·  AFTER THE MAPS IN THE BOOKS'
PROV_DOC = 'RECONSTRUCTED DOCUMENT  ·  ILLUSTRATIVE'


@functools.lru_cache(None)
def font(name, size):
    f = {'cinzel': 'Cinzel-VF.ttf', 'corm': 'CormorantGaramond-Italic-VF.ttf'}[name]
    ft = ImageFont.truetype(str(FD / f), max(6, int(round(size))))
    if name == 'cinzel':
        try:
            ft.set_variation_by_axes([600])
        except Exception:  # noqa
            pass
    return ft


def ease(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


# ----------------------------------------------------------------------------------------------- cues
def norm(w):
    w = re.sub(r"[^a-z0-9']", '', w.lower())
    return w[:-2] if w.endswith("'s") else w.rstrip("'")


class Cues:
    def __init__(self, key):
        sh = [s for s in TL['shots'] if s['key'] == f'MAP:{key}']
        if not sh:
            raise SystemExit(f'{key}: not in timeline')
        self.t0 = sh[0]['t0']
        self.dur = max(s['t1'] - s['t0'] for s in sh) + 0.4
        self.words = [(norm(w), a - self.t0) for w, a, b in TL['words'] if self.t0 - 0.05 <= a < self.t0 + self.dur]

    def __call__(self, c):
        if c is None or isinstance(c, (int, float)):
            return c
        m = re.match(r"^(.+?)(?:#(\d+))?([+-][\d.]+)?$", c)
        word, nth, off = norm(m.group(1)), int(m.group(2) or 1), float(m.group(3) or 0)
        hits = [t for w, t in self.words if w == word]
        if len(hits) < nth:
            raise SystemExit(f'cue {c!r} not spoken in window: {" ".join(w for w, _ in self.words)}')
        return max(0.0, hits[nth - 1] + off)


# ----------------------------------------------------------------------------------------------- items
def L(at, x, y, text, size=30, color=INK, font_='cinzel', anchor='mm', dur=0.6, out=None, halo=True, spacing=1):
    return dict(k='label', at=at, x=x, y=y, text=text, size=size, color=color, font=font_, anchor=anchor, dur=dur,
                out=out, halo=halo, spacing=spacing)


def PIN(at, x, y, color=RED, r=9, out=None):
    return dict(k='pin', at=at, x=x, y=y, color=color, r=r, dur=0.9, out=out)


def ROUTE(at, pts, color=RED, dur=1.6, width=5, dash=False, arrow=True, out=None):
    return dict(k='route', at=at, pts=pts, color=color, dur=dur, width=width, dash=dash, arrow=arrow, out=out)


def TINT(at, x, y, r, color, alpha=0.38, dur=0.8, out=None):
    return dict(k='tint', at=at, x=x, y=y, r=r, color=color, alpha=alpha, dur=dur, out=out)


def FIRE(at, x, y, r=40):
    return dict(k='fire', at=at, x=x, y=y, r=r, dur=99, live=True)


def SIGIL(at, x, y, field, charge, size=46):
    return dict(k='sigil', at=at, x=x, y=y, field=field, charge=charge, size=size, dur=0.6)


def WRITE(at, x, y, lines, size=40, color=INK, dur=None, font_='corm', lh=1.32, blur=0, align='l', width=None):
    return dict(k='write', at=at, x=x, y=y, lines=lines if isinstance(lines, list) else [lines], size=size, color=color,
                dur=dur, font=font_, lh=lh, blur=blur, align=align, width=width)


def STRIKE(at, x0, x1, y, color=RED, dur=0.35, width=4):
    return dict(k='strike', at=at, x0=x0, x1=x1, y=y, color=color, dur=dur, width=width)


def STAMP(at, x, y, text, color=RED, size=40, rot=-8):
    return dict(k='stamp', at=at, x=x, y=y, text=text, color=color, size=size, rot=rot, dur=0.35)


def SEAL(at, x, y, r, color, glyph='sun'):
    return dict(k='seal', at=at, x=x, y=y, r=r, color=color, glyph=glyph, dur=0.01)


def TALLY(at, x, y, n, dur, color=INK, size=38):
    return dict(k='tally', at=at, x=x, y=y, n=n, dur=dur, color=color, size=size)


def EMBLEM(at, x, y, r, dark, light):
    """Duotone medallion cut from the generated gold-dragon coin (three-headed dragon relief) - house colours."""
    return dict(k='emblem', at=at, x=x, y=y, r=r, dark=dark, light=light, dur=0.6)


def CAM(at, cx, cy, vh, dur=1.6):
    return dict(at=at, cx=cx, cy=cy, vh=vh, dur=dur)


# ----------------------------------------------------------------------------------------------- scenes
WB = 'WESTEROS_v2.jpg'
# Westeros (WESTEROS_v2.jpg, 1536x1024) place coordinates - schematic, read off the base art
P = dict(WALL=(755, 62), WINTERFELL=(705, 235), EYRIE=(945, 505), HARRENHAL=(742, 588), GODSEYE=(722, 612),
         IRON=(545, 612), CASTERLY=(560, 668), KL=(868, 662), DRAGONSTONE=(968, 688), STORMSEND=(985, 772),
         HIGHGARDEN=(595, 790), OLDTOWN=(470, 882), SUNSPEAR=(1160, 925), TARTH=(1075, 790), ROOKSREST=(925, 618),
         TUMBLETON=(700, 705), RIVERRUN=(650, 590), DRIFTMARK=(1000, 655))
KINGDOMS = dict(NORTH=(715, 235, 235), VALE=(950, 525, 120), RIVER=(705, 590, 105), IRONI=(545, 612, 60),
                WEST=(565, 680, 85), REACH=(600, 800, 135), STORM=(905, 765, 100), DORNE=(935, 925, 150))
ESS = dict(BRAAVOS=(500, 330), PENTOS=(425, 470), MYR=(445, 560), LYS=(320, 600), VOLANTIS=(640, 760),
           MEEREEN=(825, 650))
DRN = dict(HELLHOLT=(230, 820), SUNSPEAR=(1300, 735), PRINCES=(540, 235), BONEWAY=(1010, 215), GREENBLOOD=(640, 440))


def S(base, title, items, cam=None, prov=PROV_MAP, cam0=None):
    return dict(base=base, title=title, items=items, cam=cam or [], prov=prov, cam0=cam0)


VOLC = [(740, 295), (670, 370), (745, 375), (820, 335), (870, 345), (935, 350), (965, 395), (645, 430), (990, 435),
        (650, 490), (975, 505), (690, 540), (755, 575), (860, 580)]

SCENES = {
    # ------------------------------------------------------------------ maps
    'M01': S('VALYRIA.jpg', 'THE VALYRIAN FREEHOLD  ·  THE DOOM', [
        L(0.3, 810, 470, 'VALYRIA', 40, RED),
        PIN(0.3, 812, 488, RED),
        L(0.6, 300, 450, 'DRAGONSTONE', 24, INK),
        ROUTE(0.5, [(812, 488), (620, 600), (420, 590), (305, 495)], BROWN, dur=2.2, dash=True, width=4),
        *[FIRE('Flames-0.2' if i == 0 else f'Flames+{0.12 * i:.2f}', x, y - 8, 34) for i, (x, y) in enumerate(VOLC)],
        L('Fourteen+0.2', 810, 650, 'THE FOURTEEN FLAMES', 34, RED),
        TINT('split', 810, 450, 330, (190, 60, 20), 0.30, dur=2.5),
        L('miles', 810, 705, 'EVERY HILL FOR FIVE HUNDRED MILES', 24, BLOOD),
    ], cam=[CAM(0, 700, 470, 900, 0.01), CAM('Twelve', 810, 450, 640, 3.0), CAM('split', 810, 470, 840, 4.0)]),

    'M02': S(WB, 'WESTEROS  ·  BEFORE THE CONQUEST', [
        *[TINT('seven+0.1', *KINGDOMS[n], c, 0.36, dur=1.2) for n, c in
          (('NORTH', (150, 160, 170)), ('VALE', (90, 130, 190)), ('RIVER', (40, 40, 40)), ('IRONI', (40, 40, 40)),
           ('WEST', (170, 30, 30)), ('REACH', (60, 130, 60)), ('STORM', (190, 160, 40)), ('DORNE', (220, 120, 30)))],
        L('war', 755, 140, 'SEVEN KINGDOMS  ·  SEVEN KINGS  ·  ALL AT WAR', 28, BLOOD),
        SIGIL('North', 705, 300, (150, 155, 160), (240, 240, 240)), L('North+0.2', 705, 350, 'THE NORTH', 26),
        L('Starks', 705, 380, 'STARK OF WINTERFELL', 20, BROWN), PIN('Winterfell', *P['WINTERFELL']),
        SIGIL('Vale', 1040, 470, (110, 160, 210), (245, 245, 245)), L('Vale+0.2', 1040, 520, 'THE VALE', 26),
        L('Arryns', 1040, 550, 'ARRYN OF THE EYRIE', 20, BROWN), PIN('Eyrie', *P['EYRIE']),
        SIGIL('west', 470, 680, (160, 20, 20), (220, 180, 60)), L('west+0.2', 470, 730, 'THE WESTERLANDS', 24),
        L('Lannisters', 470, 758, 'LANNISTER OF CASTERLY ROCK', 18, BROWN), PIN('Casterly', *P['CASTERLY']),
        SIGIL('Reach', 610, 830, (240, 240, 230), (50, 120, 50)), L('Reach+0.2', 610, 880, 'THE REACH', 26),
        L('Gardeners', 610, 908, 'GARDENER OF HIGHGARDEN', 18, BROWN), PIN('Highgarden', *P['HIGHGARDEN']),
        SIGIL('Stormlands', 1010, 840, (210, 170, 40), (20, 20, 20)), L('Stormlands+0.2', 1010, 890, 'THE STORMLANDS', 24),
        L('Durrandons', 1010, 918, "DURRANDON OF STORM'S END", 18, BROWN), PIN('Storm', *P['STORMSEND']),
        SIGIL('south', 1000, 960, (220, 110, 30), (200, 30, 30)), L('south+0.2', 1100, 965, 'DORNE', 26, anchor='lm'),
        L('Martells', 1100, 992, 'MARTELL', 18, BROWN, anchor='lm'), PIN('Dorne', *P['SUNSPEAR']),
        L('seven+0.6', 640, 552, 'HARREN THE BLACK', 18, BLACK), L('seven+0.6', 545, 572, 'IRON ISLANDS', 16, BLACK),
    ], cam=[CAM(0, 768, 512, 1024, 0.01), CAM('North-0.8', 715, 300, 560, 1.4), CAM('Vale-0.8', 960, 520, 560, 1.4),
            CAM('west-0.8', 560, 700, 560, 1.4), CAM('Reach-0.8', 620, 830, 560, 1.4),
            CAM('Stormlands-0.8', 960, 820, 560, 1.4), CAM('south-0.8', 1000, 900, 600, 1.4)]),

    'M03': S(WB, 'AEGON LANDS  ·  THE AEGONFORT', [
        L(0.0, 985, 705, 'DRAGONSTONE', 12), PIN(0.0, *P['DRAGONSTONE'], BLACK),
        ROUTE(0.2, [P['DRAGONSTONE'], (930, 660), P['KL']], RED, dur=1.4),
        PIN(1.5, *P['KL'], RED), L(1.6, 860, 640, 'THREE HILLS  ·  THE AEGONFORT', 12, RED),
        L('sixteen', 850, 690, 'FEWER THAN 1,600 MEN', 11, BROWN),
    ], cam=[CAM(0, 915, 670, 300, 0.01), CAM(0.2, 900, 668, 270, 4.0)]),

    'M04': S(WB, "AEGON'S CONQUEST", [
        TINT(0.0, *KINGDOMS['RIVER'], BLOOD, 0.42), TINT(0.0, *KINGDOMS['WEST'], BLOOD, 0.42),
        TINT(0.0, *KINGDOMS['REACH'], BLOOD, 0.42), TINT(0.0, *KINGDOMS['STORM'], BLOOD, 0.42),
        FIRE(0.0, *P['HARRENHAL'], 26), L(0.0, 742, 560, 'HARRENHAL', 16, BLACK),
        L('dominoes', 760, 140, 'THE KINGDOMS FALL', 30, BLOOD),
        PIN('Eyrie', *P['EYRIE'], (90, 130, 190)), L('Eyrie+0.2', 945, 470, 'THE EYRIE', 22),
        L('mountain', 1030, 560, 'HIGH ABOVE ANY ARMY', 16, BROWN),
        ROUTE('castle', [P['KL'], (900, 600), P['EYRIE']], RED, dur=1.6),
        L('dragon-0.6', 870, 590, 'VISENYA  ·  VHAGAR', 16, RED),
        TINT('dragon', *KINGDOMS['VALE'], BLOOD, 0.42),
    ], cam=[CAM(0, 768, 600, 820, 0.01), CAM('Vale', 900, 560, 520, 2.0)]),

    'M05': S('DORNE.jpg', 'DORNE  ·  UNCONQUERED', [
        L(0.2, 700, 150, 'THE RED MOUNTAINS', 30, BLOOD),
        L(0.5, DRN['PRINCES'][0], 280, "PRINCE'S PASS", 20), L(0.5, DRN['BONEWAY'][0], 262, 'THE BONEWAY', 20),
        L(0.8, 230, 880, 'HELLHOLT', 22), L(0.8, 1300, 800, 'SUNSPEAR', 24),
        *[PIN('learned', x, y, (220, 110, 30), 11, out='melted') for x, y in
          ((360, 640), (720, 700), (990, 680), (500, 480), (850, 450), (1150, 560))],
        L('battle', 760, 370, 'THEY WOULD NOT GIVE BATTLE', 24, BLOOD),
        ROUTE('dragons', [(600, 0), (560, 300), (420, 560)], RED, dur=1.3),
        ROUTE('dragons+0.2', [(1000, 0), (980, 300), (860, 560)], RED, dur=1.3),
        *[PIN('back', x, y, (220, 110, 30), 11) for x, y in
          ((360, 640), (720, 700), (990, 680), (500, 480), (850, 450), (1150, 560))],
    ], cam=[CAM(0, 768, 512, 864, 0.01), CAM(2.0, 760, 500, 760, 10.0)]),

    'M06': S(WB, "JAEHAERYS'S ROADS", [
        PIN(0.0, *P['KL'], RED), L(0.0, 900, 640, "KING'S LANDING", 16, RED, anchor='lm'),
        ROUTE(0.4, [P['KL'], (790, 560), (720, 430), P['WINTERFELL'], (740, 140), P['WALL']], (120, 70, 20), dur=3.0, width=6),
        L(1.4, 790, 300, 'THE KINGSROAD', 22, BROWN),
        ROUTE(1.0, [P['KL'], (700, 720), P['HIGHGARDEN'], P['OLDTOWN']], (120, 70, 20), dur=2.2, width=5),
        L(2.4, 640, 730, 'THE ROSEROAD', 18, BROWN),
        ROUTE(1.4, [P['KL'], (700, 650), P['CASTERLY']], (120, 70, 20), dur=1.8, width=5),
        L(2.8, 650, 636, 'THE GOLDROAD', 16, BROWN),
        ROUTE('realm', [P['KL'], (1000, 400), (920, 150), (760, 70)], (200, 200, 210), dur=2.4, dash=True, width=4),
        L('realm+1.6', 950, 230, 'ALYSANNE  ·  SILVERWING TO THE WALL', 16, (90, 90, 110)),
    ], cam=[CAM(0, 768, 470, 1000, 0.01), CAM(0.5, 780, 430, 900, 7.0)]),

    'M07': S(WB, 'BLACKS AND GREENS  ·  129 AC', [
        L('greens', 560, 760, 'THE GREENS', 28, GREEN),
        TINT('greens', *KINGDOMS['REACH'], GREEN, 0.34), TINT('greens+0.3', *KINGDOMS['WEST'], GREEN, 0.34),
        TINT('greens+0.6', *KINGDOMS['STORM'], GREEN, 0.30),
        L('sons', 560, 790, 'OLDTOWN  ·  CASTERLY ROCK  ·  STORMS END', 14, GREEN),
        L('blacks', 900, 380, 'THE BLACKS', 28, BLACK),
        TINT('blacks', *KINGDOMS['NORTH'], BLACK, 0.30), TINT('blacks+0.3', *KINGDOMS['VALE'], BLACK, 0.34),
        TINT('blacks+0.6', *KINGDOMS['RIVER'], BLACK, 0.30), PIN('blacks', *P['DRAGONSTONE'], BLACK),
        L('Rhaenyra', 1000, 715, 'DRAGONSTONE', 16, BLACK),
        PIN('Daemon', *P['HARRENHAL'], RED), L('Daemon+0.1', 742, 560, 'PRINCE DAEMON', 18, RED),
    ], cam=[CAM(0, 768, 560, 900, 0.01), CAM('blacks', 800, 520, 900, 2.0)]),

    'M08': S(WB, 'THE DANCE OF THE DRAGONS  ·  129-131 AC', [
        *[L(0.3 + 0.25 * i, x, y - 22, n, 14, BLOOD) for i, (n, (x, y)) in
          enumerate((("ROOK'S REST", P['ROOKSREST']), ('TUMBLETON', P['TUMBLETON']), ('THE GODS EYE', P['GODSEYE'])))],
        *[PIN(0.3 + 0.25 * i, *p, BLOOD, 7) for i, p in enumerate((P['ROOKSREST'], P['TUMBLETON'], P['GODSEYE']))],
        PIN('storm', *P['STORMSEND'], (190, 160, 40)), L('storm+0.2', 985, 800, "STORM'S END", 20),
        PIN('Rhaenyra', *P['DRAGONSTONE'], BLACK), L('Rhaenyra', 990, 712, 'DRAGONSTONE', 16, BLACK),
        ROUTE('Lucerys', [P['DRAGONSTONE'], (1010, 730), P['STORMSEND']], (60, 80, 130), dur=2.0, dash=True),
        L('Arrax', 1060, 735, 'LUCERYS  ·  ARRAX', 16, (60, 80, 130), anchor='lm'),
        L('Vhagar', 925, 780, 'AEMOND  ·  VHAGAR', 18, GREEN, anchor='rm'), PIN('Aemond', 975, 770, GREEN, 12),
    ], cam=[CAM(0, 820, 660, 520, 0.01), CAM('storm', 950, 720, 360, 2.5)]),

    'M09': S('DORNE.jpg', "THE YOUNG DRAGON'S CONQUEST  ·  157 AC", [
        ROUTE(0.0, [(540, 0), DRN['PRINCES'], (650, 520), (1000, 680), DRN['SUNSPEAR']], RED, dur=2.4),
        ROUTE(0.3, [(1010, 0), DRN['BONEWAY'], (1150, 500), DRN['SUNSPEAR']], RED, dur=2.0),
        PIN(2.2, *DRN['SUNSPEAR'], RED), L(2.3, 1300, 800, 'SUNSPEAR', 24),
        L('single', 760, 330, 'WITHOUT A SINGLE DRAGON', 24, BLOOD),
    ], cam=[CAM(0, 768, 480, 864, 0.01), CAM(0.4, 900, 520, 760, 3.6)]),

    'M10': S('REDGRASS.jpg', 'REDGRASS FIELD  ·  196 AC', [
        *[SIGIL(0.2 + 0.15 * i, x, y, BLACK, RED, 40) for i, (x, y) in enumerate(((1120, 300), (1200, 360), (1080, 420)))],
        L(0.6, 1160, 220, 'THE KING', 22, BLACK),
        *[SIGIL(0.5 + 0.15 * i, x, y, RED, BLACK, 40) for i, (x, y) in enumerate(((420, 600), (520, 660), (360, 700)))],
        L(0.9, 450, 540, 'BLACKFYRE', 22, RED),
        ROUTE('rose', [(520, 640), (760, 560), (1000, 440)], RED, dur=1.5, width=8),
        L('rose+0.4', 1290, 170, "RAVEN'S TEETH", 18, BROWN), PIN('rose+0.4', 1260, 210, (230, 230, 230), 8),
    ], cam=[CAM(0, 768, 512, 864, 0.01), CAM(0.3, 800, 470, 760, 4.6)]),

    'M11': S(WB, "ROBERT'S REBELLION  ·  282 AC", [
        PIN(0.0, *P['KL'], RED), L(0.0, 830, 690, "KING'S LANDING", 16, RED, anchor='rm'),
        PIN('Eddard', *P['WINTERFELL'], (150, 155, 160)), L('Eddard+0.1', 705, 270, 'EDDARD STARK', 18),
        PIN('Robert', *P['STORMSEND'], (210, 170, 40)), L('Robert+0.1', 985, 805, 'ROBERT BARATHEON', 18),
        ROUTE('demanded', [P['KL'], (880, 560), P['EYRIE']], RED, dur=1.4, dash=True),
        PIN('Arryn', *P['EYRIE'], (110, 160, 210)), L('Arryn+0.1', 945, 470, 'JON ARRYN', 20),
        STAMP('refused', 1085, 600, 'REFUSED', RED, 30, -10),
        TINT('refused', *KINGDOMS['VALE'], (110, 160, 210), 0.36),
    ], cam=[CAM(0, 820, 560, 820, 0.01), CAM('Arryn', 900, 610, 600, 2.0)]),

    'M12': S('ESSOS.jpg', 'THE BEGGAR KING  ·  THE FREE CITIES', [
        L(0.0, 120, 330, 'WESTEROS', 20, BROWN),
        PIN(0.0, *ESS['BRAAVOS'], BLACK), L(0.0, 500, 300, 'BRAAVOS', 18),
        ROUTE(0.3, [ESS['BRAAVOS'], ESS['PENTOS'], ESS['MYR'], ESS['LYS'], ESS['VOLANTIS']], RED, dur=3.0, dash=True),
        L(1.0, 425, 500, 'PENTOS', 16), L(1.6, 470, 590, 'MYR', 16), L(2.2, 320, 630, 'LYS', 16),
        L(2.8, 640, 790, 'VOLANTIS', 16),
        L('money', 760, 160, 'FROM CITY TO CITY', 24, BLOOD),
    ], cam=[CAM(0, 520, 520, 700, 0.01), CAM(0.3, 560, 560, 640, 4.6)]),

    # ------------------------------------------------------------------ mockups
    'K01': S('PROP_BOOK.jpg', 'A HISTORY OF THE TARGARYEN KINGS', [
        WRITE(0.0, 340, 110, ['Fire & Blood', ''], 52, INK, dur=0.01),
        WRITE(0.0, 340, 200, ['being a history of the Targaryen', 'kings of Westeros, set down by', 'an Archmaester of the Citadel', '',
                               'Of the death of the old king, the', 'accounts are not in agreement...'], 36, INK, dur=0.01),
        WRITE('disagree', 900, 120, ['Septon Eustace:'], 34, RED, dur=0.5),
        WRITE('disagree+0.4', 900, 168, ['"the queen was blameless"'], 34, INK, dur=0.9),
        WRITE('histories', 900, 300, ['Grand Maester Munkun:'], 34, RED, dur=0.6),
        WRITE('histories+0.5', 900, 348, ['"the truth lies between"'], 34, INK, dur=0.9),
        WRITE('story', 900, 480, ['Mushroom, the fool:'], 34, RED, dur=0.6),
        WRITE('story+0.5', 900, 528, ['"I was there. Under the bed."'], 34, INK, dur=1.0),
        STAMP('sure', 1110, 650, 'NOBODY IS SURE', RED, 34, -9),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 470, 900, 0.01), CAM(0.5, 1020, 400, 640, 9.0)]),

    'K02': S('PROP_SCROLL.jpg', 'THE DREAM OF DAENYS', [
        WRITE(0.0, 320, 260, ['I saw the hills split open, and the sky', 'burn, and Valyria fall into the sea.'], 52, INK, dur=2.2),
        WRITE(2.4, 1000, 500, ['- Daenys'], 44, RED, dur=0.6),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 400, 820, 0.01), CAM(0.1, 820, 400, 720, 3.6)]),

    'K03': S('PROP_VELLUM.jpg', 'HOUSE TARGARYEN  ·  THE LINE OF AENAR', [
        L(0.2, 845, 230, 'AENAR THE EXILE', 34, INK), L(0.4, 845, 265, 'LORD OF DRAGONSTONE', 18, BROWN),
        ROUTE(0.6, [(845, 285), (845, 330)], INK, dur=0.4, width=3, arrow=False),
        L(1.0, 845, 360, 'DAENYS THE DREAMER  =  GAEMON', 30, RED),
        ROUTE(1.4, [(845, 385), (845, 470)], INK, dur=0.6, width=3, arrow=False),
        L(1.9, 845, 500, '. . .  A CENTURY ON DRAGONSTONE  . . .', 20, BROWN),
        ROUTE(2.2, [(845, 525), (845, 590)], INK, dur=0.4, width=3, arrow=False),
        L(2.6, 845, 620, 'AERION  =  VALAENA VELARYON', 26, INK),
        ROUTE(2.9, [(845, 645), (845, 680), (560, 680), (560, 710)], INK, dur=0.6, width=3, arrow=False),
        ROUTE(2.9, [(845, 680), (845, 710)], INK, dur=0.4, width=3, arrow=False),
        ROUTE(2.9, [(845, 680), (1130, 680), (1130, 710)], INK, dur=0.6, width=3, arrow=False),
        L(3.4, 560, 740, 'VISENYA', 28, RED), L(3.4, 845, 740, 'AEGON', 34, RED), L(3.4, 1130, 740, 'RHAENYS', 28, RED),
        L('strongest', 845, 790, 'NOT THE RICHEST  ·  NOT THE STRONGEST', 18, BROWN),
        STAMP('dream', 1150, 380, 'THE DREAM', RED, 30, -8),
    ], prov=PROV_DOC, cam=[CAM(0, 845, 300, 480, 0.01), CAM(1.6, 845, 500, 760, 3.0)]),

    'K04': S('PROP_SCROLL.jpg', 'THE IRON THRONE', [
        WRITE(0.0, 320, 220, ['Of the seat of King Aegon, made from', 'the swords of his fallen enemies...'], 40, BROWN, dur=0.01),
        WRITE('king', 380, 420, ['"A king should never', '  sit easy."'], 72, INK, dur=2.0),
        WRITE('dangerous', 960, 650, ['- Aegon, First of His Name'], 36, RED, dur=0.9),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 420, 820, 0.01), CAM(0.2, 780, 470, 640, 7.0)]),

    'K05': S('PROP_SCROLL.jpg', 'A LETTER FROM THE PRINCESS OF DORNE', [
        SEAL(0.0, 820, 735, 62, (200, 100, 30), 'sun'),
        WRITE(0.0, 320, 190, ['To Aegon, of House Targaryen -'], 40, INK, dur=0.01),
        WRITE(0.0, 320, 270, ['  ' + 'mmmm nnmm mmnmn mm nmmmnn mm' * 1, 'nmmn mm nmnnm mmmn nm mmnnmmn',
                               'mmnm nmmm mm nnmmm nmn mmnnm', 'nn mmmnm nmmm nnm mmnm nnmmm'], 44, INK, dur=0.01, blur=6),
        WRITE(0.0, 900, 600, ['- Deria, Princess of Dorne'], 38, INK, dur=0.01),
        STAMP('knows', 830, 420, 'CONTENTS UNKNOWN', RED, 44, -6),
        L('peace', 560, 610, 'AFTER IT  ·  PEACE', 28, BLOOD),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 470, 860, 0.01), CAM(0.2, 836, 450, 700, 9.0)]),

    'K06': S('PROP_BOOK.jpg', 'THE JAEHAERYS CODE', [
        WRITE(0.0, 330, 110, ['the laws of the North', 'the laws of the Vale', 'the laws of the Rock', 'the laws of the Reach',
                               'the laws of the Stormlands', 'the laws of Dorne', 'the laws of the Iron Isles'], 36, INK,
              dur=0.01, lh=1.9),
        *[STRIKE(0.3 + 0.22 * i, 325, 760, 128 + i * 68, RED, 0.2) for i in range(7)],
        L('one-0.2', 1110, 380, 'ONE LAW', 64, RED),
        L('seven', 1110, 460, 'FOR ALL THE SEVEN KINGDOMS', 22, INK),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 470, 900, 0.01), CAM(0.1, 900, 440, 760, 3.6)]),

    'K07': S('PROP_LEDGER.jpg', 'THE GREAT COUNCIL OF 101 AC', [
        WRITE(0.0, 300, 120, ['Great Council at Harrenhal,', 'the hundred and first year'], 38, INK, dur=0.01),
        WRITE(0.0, 300, 280, ['Prince Viserys'], 40, INK, dur=0.01), WRITE(0.0, 300, 560, ['Laenor, son of Rhaenys'], 36, INK, dur=0.01),
        TALLY(0.2, 840, 290, 40, 3.2), TALLY(0.4, 840, 570, 2, 0.8),
        L('man', 520, 790, 'A MAN, OVER A WOMAN', 26, BLOOD),
        STAMP('Viserys', 1060, 450, 'CHOSEN', RED, 36, -8),
    ], prov=PROV_DOC, cam=[CAM(0, 790, 470, 900, 0.01), CAM(0.1, 800, 450, 760, 4.6)]),

    'K08': S('PROP_SCROLL.jpg', 'THE HEIR TO THE IRON THRONE', [
        WRITE(0.0, 320, 200, ['Be it known in all the Seven Kingdoms:'], 44, INK, dur=0.01),
        WRITE(0.0, 320, 300, ['the Princess Rhaenyra Targaryen is heir', 'to the Iron Throne.'], 50, INK, dur=0.01),
        WRITE(0.0, 860, 560, ['- Viserys, First of His Name'], 38, RED, dur=0.01),
        STRIKE('heir', 900, 1230, 380, RED, 0.5, 5),
        STAMP('remained', 520, 560, 'NEVER REVOKED', RED, 36, -7),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 420, 800, 0.01), CAM(0.1, 820, 400, 680, 4.4)]),

    'K09': S('PROP_LEDGER.jpg', 'THE DRAGONS OF THE DANCE', [
        WRITE(0.0, 300, 115, ['Arrax', 'Meleys', 'Vermax', 'Syrax', 'Caraxes', 'Vhagar', 'Tyraxes', 'Dreamfyre', 'Shrykos',
                               'Morghul'], 34, INK, dur=0.01, lh=1.95),
        WRITE(0.0, 830, 115, ['Sunfyre', 'Seasmoke', 'Tessarion', 'Vermithor', 'Moondancer', 'Stormcloud', 'Grey Ghost',
                               'Morning', 'Silverwing', 'Sheepstealer'], 34, INK, dur=0.01, lh=1.95),
        *[STRIKE(0.2 + 0.2 * i, 292, 560, 136 + i * 66, RED, 0.18) for i in range(10)],
        *[STRIKE(2.2 + 0.2 * i, 822, 1100, 136 + i * 66, RED, 0.18) for i in range(7)],
        L('handful', 1150, 760, 'A HANDFUL LEFT', 24, BLOOD),
    ], prov=PROV_DOC, cam=[CAM(0, 790, 470, 900, 0.01), CAM(0.1, 800, 470, 820, 6.0)]),

    'K11': S('PROP_SCROLL.jpg', 'THE DEATHBED DECREE  ·  184 AC', [
        WRITE(0.0, 320, 200, ['I, Aegon, Fourth of My Name, do declare', 'every child of my body, born out of', 'wedlock, to be trueborn.'],
              46, INK, dur=0.01),
        WRITE(0.0, 860, 560, ['- Aegon R.'], 40, RED, dur=0.01),
        STAMP('Every', 1100, 470, 'ALL OF THEM', RED, 40, -8),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 420, 820, 0.01), CAM(0.1, 820, 380, 660, 6.0)]),

    'K12': S('PROP_VELLUM.jpg', 'TWO DRAGONS', [
        EMBLEM(0.0, 620, 450, 190, BLACK, (200, 30, 24)), L(0.0, 620, 690, 'TARGARYEN', 30, INK), L(0.0, 620, 728, 'RED DRAGON ON BLACK', 18, BROWN),
        EMBLEM('reversed', 1070, 450, 190, (170, 20, 16), (10, 8, 8)), L('reversed', 1070, 690, 'BLACKFYRE', 30, RED),
        L('reversed+0.2', 1070, 728, 'BLACK DRAGON ON RED', 18, BROWN),
    ], prov=PROV_DOC, cam=[CAM(0, 845, 500, 760, 0.01), CAM(0.1, 845, 500, 700, 3.0)]),

    'K13': S('PROP_LEDGER.jpg', 'A RIDDLE OF THOSE YEARS', [
        WRITE('riddle', 300, 250, ['How many eyes', 'does Lord Bloodraven', 'have?'], 56, INK, dur=2.6),
        WRITE('have+0.6', 830, 520, ['A thousand eyes,', 'and one.'], 56, RED, dur=1.6),
    ], prov=PROV_DOC, cam=[CAM(0, 790, 470, 860, 0.01), CAM(0.1, 800, 470, 700, 6.0)]),

    'K14': S('PROP_BOOK.jpg', 'A LETTER FROM SUMMERHALL  ·  259 AC', [
        WRITE(0.0, 330, 110, ['mmnmn nnmm mmmn nm nmmnn', 'nm mmnnm mnmm nmmm nnm', 'mmn nmmnm nnmm mn nmmm', 'nmmm mmnn nm mnmnm mm',
                               'mm nnmmn mmmn nmn mmnn', 'nmnm mm nnmmm mnm nmm'], 38, INK, dur=0.01, blur=7, lh=1.9),
        WRITE(0.0, 880, 110, ['nmm mmnnm nmmn nm mmnm', 'mnmn mm nnmm mnmmn nm', 'mmnm nnmm mn nmmmn mm', 'nn mmnmm nmnm mmn nmm'],
              38, INK, dur=0.01, blur=7, lh=1.9),
        WRITE('fragments', 360, 260, ['...Summerhall...'], 42, INK, dur=0.6),
        WRITE('blood-0.1', 880, 330, ['...the blood of the dragon...'], 42, RED, dur=0.9),
        WRITE('gathered', 920, 470, ['...gathered in one...'], 42, RED, dur=0.8),
    ], prov=PROV_DOC, cam=[CAM(0, 836, 470, 860, 0.01), CAM(0.1, 1000, 420, 620, 6.0)]),

    'K15': S('PROP_LEDGER.jpg', 'THE WILDFIRE CACHES', [
        WRITE(0.0, 300, 115, ['Caches of the substance,', 'laid down at the king\'s command'], 36, INK, dur=0.01),
        WRITE(0.6, 300, 280, ['beneath the Sept of Baelor', 'beneath Flea Bottom', 'beneath the stables', 'at the seven gates',
                               'in the cellars of the Red Keep'], 36, INK, dur=4.0, lh=1.9),
        *[WRITE(1.0 + 0.8 * i, 1000, 290 + i * 68, ['jars'], 36, WF, dur=0.4) for i in range(5)],
        L('terror', 1050, 760, 'THE GUILD OF ALCHEMISTS', 22, WF),
    ], prov=PROV_DOC, cam=[CAM(0, 790, 470, 900, 0.01), CAM(0.1, 780, 480, 760, 8.0)]),

    'K16': S('PROP_LEDGER.jpg', 'THE TOURNEY AT HARRENHAL  ·  281 AC', [
        WRITE(0.0, 300, 115, ['The great tourney at Harrenhal', 'in the year of the false spring'], 36, INK, dur=0.01),
        WRITE(0.0, 300, 300, ['Final tilt: Prince Rhaegar', 'unhorses Ser Barristan Selmy'], 36, INK, dur=0.01),
        WRITE('champion', 830, 300, ['Champion:', 'Prince Rhaegar Targaryen'], 38, RED, dur=1.2),
        WRITE('queen', 830, 470, ['Queen of Love and Beauty:'], 36, INK, dur=1.2),
        WRITE('Elia', 860, 560, ['Elia Martell ?'], 40, (120, 110, 100), dur=1.0),
    ], prov=PROV_DOC, cam=[CAM(0, 790, 470, 900, 0.01), CAM(0.1, 1000, 470, 640, 9.0)]),

    'K18': S('PROP_VELLUM.jpg', 'THE KINGS OF THE IRON THRONE', [
        WRITE(0.0, 380, 190, ['I    Aegon the Conqueror', 'I    Aenys', 'I    Maegor the Cruel', 'I    Jaehaerys the Conciliator',
                               'I    Viserys', 'II   Aegon  ( Rhaenyra, disputed )'], 38, INK, dur=0.01, lh=1.45),
        WRITE('Third', 380, 190 + 6 * 38 * 1.45, ['III  Aegon the Dragonbane'], 40, RED, dur=1.4),
    ], prov=PROV_DOC, cam=[CAM(0, 845, 420, 760, 0.01), CAM(0.1, 760, 470, 600, 5.6)]),

    'K19': S('PROP_COIN.jpg', 'THE GOLD DRAGON  ·  COIN OF THE REALM', [
    ], prov='', cam=[CAM(0, 836, 470, 900, 0.01), CAM(0.5, 600, 480, 760, 9.0), CAM('sons', 1200, 480, 760, 6.0)]),
}


# ----------------------------------------------------------------------------------------------- renderer
class Scene:
    def __init__(self, key):
        self.key, self.sp = key, SCENES[key]
        self.cue = Cues(key)
        self.dur = self.cue.dur
        im = Image.open(BASE / self.sp['base']).convert('RGB')
        self.bw, self.bh = im.size
        im = im.resize((int(self.bw * SS), int(self.bh * SS)), Image.LANCZOS)
        self.pad = int(max(im.size) * 0.3)
        # the sheet lies on a dark table: pad with dark wood-brown + a soft drop shadow (no mirrored edges)
        pw, ph = im.width + 2 * self.pad, im.height + 2 * self.pad
        rng = np.random.default_rng(7)
        tab = np.full((ph, pw, 3), (26, 19, 14), np.float32) + rng.normal(0, 3, (ph, pw, 1))
        sh = np.zeros((ph, pw), np.float32)
        o = int(14 * SS)
        sh[self.pad + o:self.pad + im.height + o, self.pad + o:self.pad + im.width + o] = 1
        sh = cv2.GaussianBlur(sh, (0, 0), 22 * SS)
        tab *= (1 - 0.7 * sh)[..., None]
        tab[self.pad:self.pad + im.height, self.pad:self.pad + im.width] = np.asarray(im)
        self.base = Image.fromarray(np.clip(tab, 0, 255).astype(np.uint8))
        self.items = []
        for it in self.sp['items']:
            it = dict(it)
            it['t'] = self.cue(it['at'])
            it['to'] = self.cue(it.get('out'))
            if it['k'] == 'write' and it['dur'] is None:
                it['dur'] = 0.06 * sum(len(s) for s in it['lines'])
            self.items.append(it)
        self.cams = sorted([dict(c, t=self.cue(c['at'])) for c in self.sp['cam']], key=lambda c: c['t'])
        if not self.cams:
            self.cams = [dict(t=0, cx=self.bw / 2, cy=self.bh / 2, vh=self.bh, dur=0.01),
                         dict(t=0.01, cx=self.bw / 2, cy=self.bh / 2, vh=self.bh * 0.85, dur=self.dur)]
        self.baked = self.base.copy()
        self.done = set()
        self._cache = {}

    # coordinates: base px -> padded SS canvas
    def P(self, x, y):
        return (x * SS + self.pad, y * SS + self.pad)

    def cam(self, t):
        c = self.cams[0]
        cx, cy, vh = c['cx'], c['cy'], c['vh']
        for c in self.cams[1:]:
            if t <= c['t']:
                break
            e = ease((t - c['t']) / max(1e-3, c['dur']))
            cx, cy, vh = cx + (c['cx'] - cx) * e, cy + (c['cy'] - cy) * e, vh + (c['vh'] - vh) * e
        # keep a zoomed view on the sheet (no table showing) whenever the view is smaller than the sheet
        vw = vh * 16 / 9
        if vw < self.bw:
            cx = min(max(cx, vw / 2), self.bw - vw / 2)
        if vh < self.bh:
            cy = min(max(cy, vh / 2), self.bh - vh / 2)
        return cx, cy, vh

    # ---- item drawing (img: PIL RGB, drawn with RGBA blending). p = animation progress 0..1, a = opacity
    def draw(self, img, it, t):
        lt = t - it['t']
        p = ease(lt / max(1e-3, it['dur']))
        a = p
        if it.get('to') is not None and t > it['to']:
            a *= 1 - ease((t - it['to']) / 0.6)
        if a <= 0.005:
            return
        d = ImageDraw.Draw(img, 'RGBA')
        k = it['k']
        if k == 'label':
            x, y = self.P(it['x'], it['y'] - 6 * (1 - p))
            f = font(it['font'], it['size'] * SS)
            txt = it['text']
            if it['halo']:
                d.text((x, y), txt, font=f, anchor=it['anchor'], fill=HALO + (int(150 * a),),
                       stroke_width=int(4 * SS), stroke_fill=HALO + (int(110 * a),))
            d.text((x, y), txt, font=f, anchor=it['anchor'], fill=tuple(it['color']) + (int(255 * a),))
        elif k == 'pin':
            x, y = self.P(it['x'], it['y'])
            r = it['r'] * SS
            pulse = (lt % 2.0) / 2.0
            rr = r * (1 + 2.2 * pulse)
            d.ellipse([x - rr, y - rr, x + rr, y + rr], outline=tuple(it['color']) + (int(160 * a * (1 - pulse)),),
                      width=int(2 * SS))
            d.ellipse([x - r - 3, y - r - 3, x + r + 3, y + r + 3], fill=HALO + (int(200 * a),))
            d.ellipse([x - r, y - r, x + r, y + r], fill=tuple(it['color']) + (int(255 * a),))
        elif k == 'route':
            pts = [self.P(*q) for q in it['pts']]
            seg = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
            tot = sum(seg) or 1
            want, acc, out = tot * p, 0.0, [pts[0]]
            for i, s in enumerate(seg):
                if acc + s >= want:
                    f_ = (want - acc) / max(1e-6, s)
                    out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f_, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f_))
                    break
                out.append(pts[i + 1]); acc += s
            col = tuple(it['color']) + (int(235 * a),)
            w = int(it['width'] * SS)
            if it['dash']:
                dense = []
                for i in range(len(out) - 1):
                    n = max(1, int(math.dist(out[i], out[i + 1]) / 4))
                    dense += [(out[i][0] + (out[i + 1][0] - out[i][0]) * j / n, out[i][1] + (out[i + 1][1] - out[i][1]) * j / n)
                              for j in range(n)]
                dense.append(out[-1])
                L_ = 0.0
                for i in range(len(dense) - 1):
                    if int(L_ / (9 * SS)) % 2 == 0:
                        d.line([dense[i], dense[i + 1]], fill=col, width=w)
                    L_ += math.dist(dense[i], dense[i + 1])
            else:
                d.line(out, fill=HALO + (int(120 * a),), width=w + int(4 * SS), joint='curve')
                d.line(out, fill=col, width=w, joint='curve')
            if it['arrow'] and len(out) >= 2:
                (x0, y0), (x1, y1) = out[-2], out[-1]
                ang = math.atan2(y1 - y0, x1 - x0)
                s = 9 * SS + w
                tri = [(x1 + math.cos(ang) * s, y1 + math.sin(ang) * s),
                       (x1 + math.cos(ang + 2.5) * s, y1 + math.sin(ang + 2.5) * s),
                       (x1 + math.cos(ang - 2.5) * s, y1 + math.sin(ang - 2.5) * s)]
                d.polygon(tri, fill=col)
        elif k == 'tint':
            key = ('tint', it['r'], tuple(it['color']))
            if key not in self._cache:
                r = int(it['r'] * SS)
                yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
                m = np.clip(1 - np.sqrt(xx ** 2 + yy ** 2) / r, 0, 1) ** 0.7
                self._cache[key] = m
            m = self._cache[key]
            x, y = self.P(it['x'], it['y'])
            self.blend(img, m * it['alpha'] * a, it['color'], x, y, mode='mul')
        elif k == 'fire':
            r = it['r'] * SS
            fl = 0.75 + 0.25 * math.sin(lt * 11 + it['x']) * math.sin(lt * 7.3 + it['y'])
            key = ('fire', int(r))
            if key not in self._cache:
                R = int(r * 1.6)
                yy, xx = np.mgrid[-R:R + 1, -R:R + 1]
                self._cache[key] = np.clip(1 - np.sqrt(xx ** 2 + yy ** 2) / R, 0, 1) ** 1.6
            x, y = self.P(it['x'], it['y'])
            self.blend(img, self._cache[key] * min(1, lt / 0.4) * fl, (255, 120, 30), x, y, mode='add')
            self.blend(img, self._cache[key] ** 3 * min(1, lt / 0.4) * fl, (255, 230, 150), x, y, mode='add')
        elif k == 'sigil':
            x, y = self.P(it['x'], it['y'])
            s = it['size'] * SS * (0.85 + 0.15 * p)
            shield = [(x - s * 0.5, y - s * 0.55), (x + s * 0.5, y - s * 0.55), (x + s * 0.5, y + s * 0.05),
                      (x, y + s * 0.6), (x - s * 0.5, y + s * 0.05)]
            d.polygon([(px + 3 * SS, py + 3 * SS) for px, py in shield], fill=(0, 0, 0, int(80 * a)))
            d.polygon(shield, fill=tuple(it['field']) + (int(255 * a),), outline=GOLD + (int(255 * a),),
                      width=max(2, int(s * 0.05)))
            ch = it['charge']
            if isinstance(ch, tuple) and len(ch) == 2 and ch[0] == 'dragon':
                self.dragon(d, x, y - s * 0.02, s * 0.62, tuple(ch[1]) + (int(255 * a),))
            else:   # neutral heraldry: a broad bend in the house's second colour (no invented charges)
                bw_ = s * 0.16
                d.polygon([(x - s * 0.5, y - s * 0.55 + bw_ * 0.2), (x - s * 0.5 + bw_ * 1.2, y - s * 0.55),
                           (x + s * 0.5, y + s * 0.05 - bw_ * 0.9), (x + s * 0.5 - bw_ * 0.4, y + s * 0.05 + bw_ * 0.5)],
                          fill=tuple(ch) + (int(255 * a),))
                d.polygon(shield, outline=GOLD + (int(255 * a),), width=max(2, int(s * 0.05)))
        elif k == 'write':
            self.write(img, it, lt, a)
        elif k == 'strike':
            x0, y0 = self.P(it['x0'], it['y'])
            x1, _ = self.P(it['x1'], it['y'])
            d.line([(x0, y0), (x0 + (x1 - x0) * p, y0 + 2 * SS * p)], fill=tuple(it['color']) + (230,), width=int(it['width'] * SS))
        elif k == 'stamp':
            key = ('stamp', it['text'], it['size'])
            if key not in self._cache:
                f = font('cinzel', it['size'] * SS)
                bb = f.getbbox(it['text'])
                tw, th = bb[2] - bb[0], bb[3] - bb[1]
                pad = int(18 * SS)
                st = Image.new('RGBA', (tw + 2 * pad, th + 2 * pad), (0, 0, 0, 0))
                sd = ImageDraw.Draw(st)
                sd.rectangle([4, 4, st.width - 5, st.height - 5], outline=tuple(it['color']) + (255,), width=int(4 * SS))
                sd.text((pad - bb[0], pad - bb[1]), it['text'], font=f, fill=tuple(it['color']) + (255,))
                noise = (np.random.default_rng(3).random((st.height, st.width)) > 0.18).astype(np.uint8)
                arr = np.asarray(st).copy(); arr[..., 3] = arr[..., 3] * noise
                self._cache[key] = Image.fromarray(arr).rotate(it['rot'], expand=True, resample=Image.BICUBIC)
            st = self._cache[key]
            sc = 1.6 - 0.6 * p
            st2 = st.resize((max(1, int(st.width * sc)), max(1, int(st.height * sc))), Image.BILINEAR)
            if a < 1:
                arr = np.asarray(st2).copy(); arr[..., 3] = (arr[..., 3] * a).astype(np.uint8); st2 = Image.fromarray(arr)
            x, y = self.P(it['x'], it['y'])
            img.paste(st2, (int(x - st2.width / 2), int(y - st2.height / 2)), st2)
        elif k == 'seal':
            x, y = self.P(it['x'], it['y'])
            r = it['r'] * SS
            c = tuple(it['color'])
            d.ellipse([x - r * 1.05, y - r * 0.98, x + r * 1.02, y + r * 1.04], fill=tuple(int(v * 0.7) for v in c) + (255,))
            d.ellipse([x - r, y - r, x + r, y + r], fill=c + (255,))
            d.ellipse([x - r * 0.8, y - r * 0.8, x + r * 0.8, y + r * 0.8], outline=tuple(int(v * 0.75) for v in c) + (255,),
                      width=int(3 * SS))
            dk = tuple(int(v * 0.6) for v in c) + (255,)
            for i in range(12):                                   # sun rays pierced by a spear
                an = i * math.pi / 6
                d.line([(x + math.cos(an) * r * 0.25, y + math.sin(an) * r * 0.25),
                        (x + math.cos(an) * r * 0.62, y + math.sin(an) * r * 0.62)], fill=dk, width=int(3 * SS))
            d.ellipse([x - r * 0.22, y - r * 0.22, x + r * 0.22, y + r * 0.22], fill=dk)
            d.line([(x - r * 0.7, y + r * 0.7), (x + r * 0.7, y - r * 0.7)], fill=dk, width=int(4 * SS))
        elif k == 'emblem':
            key = ('emblem', it['dark'], it['light'], it['r'])
            if key not in self._cache:
                coin = cv2.cvtColor(cv2.imread(str(BASE / 'PROP_COIN.jpg')), cv2.COLOR_BGR2GRAY).astype(np.float32)
                R = 330
                cr = coin[470 - R:470 + R, 564 - R:564 + R]
                lo, hi = np.percentile(cr, 8), np.percentile(cr, 99)
                lum = np.clip((cr - lo) / (hi - lo), 0, 1) ** 1.6
                dk, lt_ = np.array(it['dark'], np.float32), np.array(it['light'], np.float32)
                rgb = dk + (lt_ - dk) * lum[..., None]
                yy, xx = np.mgrid[-R:R, -R:R]
                rr = np.sqrt(xx ** 2 + yy ** 2)
                al = np.clip((R * 0.97 - rr) / 3, 0, 1)
                ring = (np.abs(rr - R * 0.93) < 7).astype(np.float32)
                rgb = rgb * (1 - ring[..., None]) + np.array(GOLD, np.float32) * ring[..., None]
                im_ = Image.fromarray(np.dstack([rgb, al * 255]).astype(np.uint8), 'RGBA')
                sz = int(it['r'] * 2 * SS)
                self._cache[key] = im_.resize((sz, sz), Image.LANCZOS)
            em = self._cache[key]
            if a < 1:
                arr = np.asarray(em).copy(); arr[..., 3] = (arr[..., 3] * a).astype(np.uint8); em = Image.fromarray(arr)
            x, y = self.P(it['x'], it['y'])
            img.paste(em, (int(x - em.width / 2), int(y - em.height / 2)), em)
        elif k == 'tally':
            x, y = self.P(it['x'], it['y'])
            n = int(round(it['n'] * p))
            h, g = it['size'] * SS, it['size'] * SS * 0.26
            col = tuple(it['color']) + (240,)
            for i in range(n):
                grp, j = divmod(i, 5)
                gx = x + grp * (5 * g + g * 1.6)
                row = 0
                if gx >= x + 6 * (5 * g + g * 1.6):
                    row = int((gx - x) // (6 * (5 * g + g * 1.6)))
                    gx -= row * 6 * (5 * g + g * 1.6)
                gy = y + row * h * 1.4
                if j < 4:
                    d.line([(gx + j * g, gy), (gx + j * g + 2, gy + h)], fill=col, width=int(2.4 * SS))
                else:
                    d.line([(gx - g * 0.5, gy + h * 0.8), (gx + 3.6 * g, gy + h * 0.15)], fill=col, width=int(2.4 * SS))

    def dragon(self, d, x, y, s, col):
        """A simple heraldic three-headed dragon silhouette (body, wings, three necks) - abstract, readable at size."""
        def P_(u, v):
            return (x + u * s, y + v * s)
        d.polygon([P_(-0.15, 0.05), P_(0.15, 0.05), P_(0.1, 0.42), P_(0.0, 0.5), P_(-0.1, 0.42)], fill=col)   # body
        d.polygon([P_(-0.12, 0.0), P_(-0.62, -0.32), P_(-0.48, 0.02), P_(-0.6, 0.1), P_(-0.14, 0.18)], fill=col)  # wing L
        d.polygon([P_(0.12, 0.0), P_(0.62, -0.32), P_(0.48, 0.02), P_(0.6, 0.1), P_(0.14, 0.18)], fill=col)  # wing R
        for hx, hy in ((-0.32, -0.42), (0.0, -0.55), (0.32, -0.42)):
            d.line([P_(0, 0.05), P_(hx * 0.6, hy * 0.6), P_(hx, hy)], fill=col, width=max(2, int(s * 0.09)), joint='curve')
            d.polygon([P_(hx - 0.07, hy + 0.02), P_(hx + 0.1, hy - 0.03), P_(hx + 0.02, hy + 0.08)], fill=col)
        d.line([P_(0.0, 0.48), P_(0.18, 0.6), P_(0.3, 0.5)], fill=col, width=max(2, int(s * 0.05)))      # tail

    def blend(self, img, m, color, x, y, mode='mul'):
        arr = np.asarray(img)
        h, w = m.shape
        x0, y0 = int(x - w // 2), int(y - h // 2)
        xa, ya, xb, yb = max(0, x0), max(0, y0), min(arr.shape[1], x0 + w), min(arr.shape[0], y0 + h)
        if xa >= xb or ya >= yb:
            return
        mm = m[ya - y0:yb - y0, xa - x0:xb - x0, None]
        reg = arr[ya:yb, xa:xb].astype(np.float32)
        c = np.array(color, np.float32)
        if mode == 'add':
            reg = reg + mm * c * 0.9
        else:  # stain the parchment (multiply-ish) so it reads painted, not pasted
            reg = reg * (1 - mm) + (reg * (c / 255.0) * 0.6 + c * 0.4) * mm
        img.paste(Image.fromarray(np.clip(reg, 0, 255).astype(np.uint8)), (xa, ya))

    def write(self, img, it, lt, a):
        key = ('write', id(it))
        if key not in self._cache:
            f = font(it['font'], it['size'] * SS)
            pats = []
            for s in it['lines']:
                bb = f.getbbox(s or ' ')
                pw, ph = max(4, bb[2] + int(10 * SS)), int(it['size'] * SS * 1.5)
                pt = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
                ImageDraw.Draw(pt).text((0, int(it['size'] * SS * 0.2)), s, font=f, fill=tuple(it['color']) + (235,))
                if it['blur']:
                    pt = pt.filter(ImageFilter.GaussianBlur(it['blur'] * SS))
                pats.append(pt)
            self._cache[key] = pats
        pats = self._cache[key]
        tot = sum(p.width for p in pats) or 1
        shown = tot * min(1.0, lt / max(1e-3, it['dur']))
        x, y = self.P(it['x'], it['y'])
        lh = it['size'] * SS * it['lh']
        for i, pt in enumerate(pats):
            if shown <= 0:
                break
            wv = int(min(pt.width, shown))
            shown -= pt.width
            crop = pt.crop((0, 0, wv, pt.height))
            arr = np.asarray(crop).copy()
            if wv < pt.width:            # soft pen edge
                edge = min(wv, int(18 * SS))
                if edge > 0:
                    arr[:, wv - edge:, 3] = (arr[:, wv - edge:, 3] * np.linspace(1, 0, edge)[None, :]).astype(np.uint8)
            if a < 1:
                arr[..., 3] = (arr[..., 3] * a).astype(np.uint8)
            crop = Image.fromarray(arr)
            img.paste(crop, (int(x), int(y + i * lh)), crop)

    def finished(self, it, t):
        return (not it.get('live') and it.get('to') is None and it['k'] not in ('pin',)
                and t >= it['t'] + it['dur'] + 0.05)

    def frame(self, t):
        for i, it in enumerate(self.items):                 # bake settled items once, in authoring order
            if i not in self.done and self.finished(it, t):
                self.draw(self.baked, it, t)
                self.done.add(i)
        img = self.baked.copy()
        for i, it in enumerate(self.items):
            if i not in self.done and t >= it['t']:
                self.draw(img, it, t)
        cx, cy, vh = self.cam(t)
        s = H / (vh * SS)
        X, Y = self.P(cx, cy)
        M = np.float32([[s, 0, W / 2 - s * X], [0, s, H / 2 - s * Y]])
        out = cv2.warpAffine(np.asarray(img), M, (W, H), flags=cv2.INTER_AREA if s < 0.8 else cv2.INTER_LINEAR,
                             borderMode=cv2.BORDER_REPLICATE)
        return self.screen(out, t)

    def screen(self, fr, t):
        if 'scr' not in self._cache:
            o = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            d = ImageDraw.Draw(o)
            if self.sp['title']:
                f = font('cinzel', 30)
                bb = d.textbbox((70, 62), self.sp['title'], font=f, anchor='lm')
                d.rectangle([bb[0] - 22, bb[1] - 14, bb[2] + 22, bb[3] + 14], fill=(14, 10, 8, 150))
                d.line([bb[0] - 22, bb[3] + 14, bb[2] + 22, bb[3] + 14], fill=(196, 150, 60, 230), width=2)
                d.text((70, 62), self.sp['title'], font=f, anchor='lm', fill=(242, 232, 213, 255))
            if self.sp['prov']:
                d.text((W - 60, 56), self.sp['prov'], font=font('cinzel', 18), anchor='rm', fill=(242, 232, 213, 200),
                       stroke_width=2, stroke_fill=(14, 10, 8, 140))
            self._cache['scr'] = np.asarray(o).astype(np.float32) / 255.0
        o = self._cache['scr']
        a = o[..., 3:] * ease((t - 0.2) / 0.5)
        return (fr.astype(np.float32) * (1 - a) + o[..., :3] * 255 * a).astype(np.uint8)


def render(key, frames_only=False):
    sc = Scene(key)
    n = int(round(sc.dur * FPS))
    OUT.mkdir(parents=True, exist_ok=True)
    if frames_only:
        ts = [sc.dur * f for f in (0.02, 0.2, 0.4, 0.6, 0.8, 0.98)]
        fr, i, picks = None, 0, []
        for j in range(n):           # step through so baking state is right
            t = j / FPS
            if i < len(ts) and t >= ts[i]:
                picks.append(cv2.resize(sc.frame(t), (640, 360), interpolation=cv2.INTER_AREA)); i += 1
            elif j % 6 == 0:
                for k_, it in enumerate(sc.items):
                    if k_ not in sc.done and sc.finished(it, t):
                        sc.draw(sc.baked, it, t); sc.done.add(k_)
        while len(picks) < 6:
            picks.append(np.zeros((360, 640, 3), np.uint8))
        sheet = np.vstack([np.hstack(picks[0:2]), np.hstack(picks[2:4]), np.hstack(picks[4:6])])
        p = OUT.parent / 'maps_qc' / f'GOT003_{key}_qc.jpg'
        p.parent.mkdir(exist_ok=True)
        cv2.imwrite(str(p), cv2.cvtColor(sheet, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 85])
        return str(p)
    out = OUT / D.MAPS[f'MAP:{key}']
    cmd = [FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', str(out) + '.tmp.mp4']
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for j in range(n):
        pr.stdin.write(sc.frame(j / FPS).tobytes())
    pr.stdin.close()
    if pr.wait():
        raise RuntimeError(key)
    os.replace(str(out) + '.tmp.mp4', out)
    return f'{out.name} {sc.dur:.1f}s'


if __name__ == '__main__':
    args = sys.argv[1:]
    fo = '--frames' in args
    keys = [a for a in args if not a.startswith('--')] or list(SCENES)
    for k in keys:
        print(k, render(k, fo), flush=True)
