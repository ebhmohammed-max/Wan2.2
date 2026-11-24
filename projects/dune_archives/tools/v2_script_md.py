#!/usr/bin/env python3
"""Regenerate 17_scripts/DUN003_SCRIPT_v2.0.md from data/dun003_v2.py (single source of truth).

  python tools/v2_script_md.py [--status "APPROVED ..."]
Runtime numbers come from 22_edit/DUN003/v2/DUN003_v2_timeline.json when it exists.
"""
import argparse, glob, json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'data'))
import dun003_v2 as D  # noqa: E402

LABEL = {'STAT': 'label', 'NAME': 'name', 'PLACE': 'place', 'YEAR': 'year', 'NOTE': 'head', 'TITLE': 'title',
         'FILE': 'title', 'END': 'title', 'CHAPTER': 'title'}


def still_title(key):
    if key.startswith('MAP:'):
        return {'MAP:A': 'Map A: The Oldest Lever', 'MAP:B': 'Map B: The Jihad', 'MAP:C': 'Map C: Wallach IX'}[key]
    b, s = int(key[1:4]), int(key[5:8])
    f = glob.glob(str(ROOT / f'19_batches/DUN003/stills_jpg/DUN003_BATCH{b:03d}_SCENE{s:03d}_*'))
    name = re.sub(r'^DUN003_BATCH\d+_SCENE\d+_', '', os.path.basename(f[0])).rsplit('.', 1)[0] if f else key
    return name.replace('_', ' ').title()


def gfx_tag(kind, p):
    if kind == 'DOSSIER':
        return '{DOSSIER: four-power dossier}'
    if kind == 'SUB':
        return '{SUB: animated subscribe button + bell}'
    if kind == 'END':
        return '{END: like · comment · subscribe · next: %s}' % p.get('title', '')
    return '{%s: %s}' % (kind, p.get(LABEL.get(kind, ''), ''))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--status', default='**APPROVED** (turn 39), updated turn 41 with the Mythic Archives branding and '
                                         'the subscribe / like / comment calls to action.')
    a = ap.parse_args()
    tl = ROOT / '22_edit/DUN003/v2/DUN003_v2_timeline.json'
    T = json.load(open(tl)) if tl.exists() else None
    out = [f'# DUN003 v2 SCRIPT: {D.TITLE}', '',
           f'Status: {a.status}', '',
           'A storytelling cut built on the Hook Bible (`15_hooks/DUNE_ARCHIVES_HOOK_BIBLE.md`). '
           'Narrator: voice-14. A Mythic Archives production (@TheRealMythicArchives).', '',
           '**Changes from v1:**',
           '- Rewrote the cold open as a story-first hook, using archetype 1 ("The God Who Can See His Doom") '
           'combined with archetype 6 ("The Gift").',
           '- Removed every cinema, release and "book vs film" reference, along with the archive card and author commentary.',
           '- Told the story as in-universe history, in present tense, with a re-hook at every chapter seam.',
           '- No disclaimer or label is burned into the video.',
           '- Turn 41: "The Mythic Archives presents" title kicker and channel ident; a subscribe pitch (CA) after '
           'chapter II with an animated subscribe button and bell; an outro (CB) asking for comments, likes and '
           'subscriptions, over the end card. VIII now reads "Hayt turns on the emperor."', '',
           'Every shot cuts on the word it illustrates (**[cut → still]**), and every graphic appears on its word '
           '(**{GFX}**). Generated from `data/dun003_v2.py` by `tools/v2_script_md.py`.', '']
    total = 0
    for sid, name, num, lines in D.SECTIONS:
        words = sum(len(t.split()) for t, *_ in lines)
        total += words
        head = f'Chapter {num}: {name}' if num else f'{sid}: {name}'
        out.append(f'## {head}  ({words} words, ≈{round(words / 2.35)} s)')
        out.append('')
        for text, shots, gfx in lines:
            out.append(f'> {text}')
            tags = [f'[cut on "{s[0]}" → {still_title(s[1])}]' for s in shots]
            tags += [gfx_tag(g[1], g[2]) for g in gfx]
            if tags:
                out.append('  ' + ' '.join(tags))
            out.append('')
        if sid == 'H':
            out += ['*Channel ident: THE MYTHIC ARCHIVES · WESTEROS • ARRAKIS • MIDDLE-EARTH · '
                    'A MYTHIC ARCHIVES PRODUCTION · RECORD 003*', '']
    out.append('')
    if T:
        d = T['duration']
        out.append(f'**Total: {total} words. Programme runtime {int(d // 60)}:{d % 60:05.2f} '
                   f'({len(T["shots"])} shots, {len(T["graphics"])} graphics), from the voice-14 timeline.**')
    else:
        out.append(f'**Total: {total} words.**')
    p = ROOT / '17_scripts/DUN003_SCRIPT_v2.0.md'
    p.write_text('\n'.join(out) + '\n')
    print('wrote', p, total, 'words')


if __name__ == '__main__':
    main()
