"""Episode selection for the v2 pipeline (timeline, graphics, renderer, music fetch).

    EP=DUN001 python tools/v2_timeline.py --wav /tmp/vo.wav
    EP=DUN001 python tools/render_v2.py --audio mix.wav --out master.mp4

EP defaults to DUN003 and then reproduces the delivered DUN003 v2 paths exactly.
Every other episode uses the flat layout:
    data/<ep>.py                         script + shots + graphics (+ SPECIAL_PAUSE, MAPS, music_edl, PROLOGUE)
    20_voiceover/<EP>/raw/<SID>.mp3      one voice take per section
    20_voiceover/<EP>/<EP>_words.json    faster-whisper word times (tools/ci_align.py)
    22_edit/<EP>/                        timeline, SRT, chapters, mix, logs
    21_music/<EP>/                       music fetch list, EDL, tracks/ (CI only)
    19_batches/<EP>/stills_jpg|maps/     stills and animated maps
"""
import importlib, os, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
EP = os.environ.get('EP', 'DUN003').upper()
sys.path.insert(0, str(ROOT / 'data'))

if EP == 'DUN003':
    D = importlib.import_module('dun003_v2')
    VO = ROOT / '20_voiceover/DUN003/v2'
    RAW = VO / 'raw14'
    WORDS = VO / 'DUN003_v2_words.json'
    OUT = ROOT / '22_edit/DUN003/v2'
    TAG = 'DUN003_v2'
    EDL = ROOT / '21_music/DUN003/DUN003_MUSIC_EDL_v2.json'
    CLIPS = [('H_I', ['H', 'I']), ('II', ['II']), ('CTA_A', ['CA']), ('III', ['III']), ('IV', ['IV']), ('V', ['V']),
             ('VI', ['VI']), ('VII', ['VII']), ('VIII', ['VIII']), ('IX', ['IX']), ('X', ['X']), ('CTA_B', ['CB'])]
    MAPS = {'MAP:A': 'DUN003_MAP_A_spice_lever.mp4', 'MAP:B': 'DUN003_MAP_B_jihad_spread.mp4',
            'MAP:C': 'DUN003_MAP_C_wallach_ix.mp4'}
else:
    D = importlib.import_module(EP.lower())
    VO = ROOT / '20_voiceover' / EP
    RAW = VO / 'raw'
    WORDS = VO / f'{EP}_words.json'
    OUT = ROOT / '22_edit' / EP
    TAG = EP
    EDL = ROOT / '21_music' / EP / f'{EP}_MUSIC_EDL.json'
    CLIPS = getattr(D, 'CLIPS', None) or [(s[0], [s[0]]) for s in D.SECTIONS]
    MAPS = D.MAPS

STILLS = ROOT / '19_batches' / EP / 'stills_jpg'
MAPDIR = ROOT / '19_batches' / EP / 'maps'
MUSIC = ROOT / '21_music' / EP
TIMELINE = OUT / f'{TAG}_timeline.json'
