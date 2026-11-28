"""GOT003 (The Complete History of House Targaryen) image plan: look-book + batches of 10.

Book-first visuals: worlds/westeros/WESTEROS_BOOK_LOOKS.md section 7 (+ GOT003 script visual rules).
Prompt = STYLE + subject (+ cast anchors) + palette + camera + NO_TEXT.
Batch 1 = character / dragon / object reference stills; later batches pass them as refs.
The plan is extended batch by batch in tools/plans/got003_plan.py (B1 + PLAN); write_new() only writes batches
that do not exist yet and are complete (10 rows), so re-running never clobbers QC state.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / '19_batches/GOT003'
sys.path.insert(0, str(ROOT / 'tools/plans'))

STYLE = ('ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, fine film grain, '
         'full-bleed wide 16:9 cinematic frame, NO black bars, important action in the central band.')
PALETTE = ('Targaryen palette: obsidian black and blood red, dragonfire orange and ember gold, Valyrian smoke and ash, '
           'cold grey stone and dark sea; volumetric light, drifting embers or haze.')
NO_TEXT = ('Book-accurate original design, NOT the HBO TV design. Every face is an invented unknown person who must NOT '
           'resemble any actor or celebrity, especially the casts of Game of Thrones, House of the Dragon or A Knight of the '
           'Seven Kingdoms. NO arches, NO columns unless stated. No text, letters, runes, logos or symbols anywhere in the image.')
NEGATIVE = ('text, letters, runes, words, watermark, logo, caption, actor likeness, celebrity, TV still, cosplay wig, cartoon, '
            'anime, illustration, oversaturated, neon, gore, blood, wounds, extra fingers, deformed hands, black bars')
CAMERA = {'EW': 'epic wide shot, low horizon, 24mm lens', 'EST': 'establishing shot, 35mm lens',
          'MS': 'medium shot, 50mm lens', 'CU': 'portrait close-up, 85mm lens, shallow depth of field',
          'INS': 'macro insert, 100mm lens', 'OH': 'high overhead view'}
VAL = ('natural pale silver-gold Valyrian hair (NOT a flat white wig), luminous deep purple eyes, fine high cheekbones, '
       'an invented original face')
CAST = {
    'AEGON': (f'Aegon the Conqueror as described in the books, a grave imposing man of about thirty, {VAL}, close-cut hair, '
              'a strong jaw, clean-shaven, dark steel mail under a black surcoat with a red three-headed dragon worked in thread, '
              'a crown of dark rippled Valyrian steel set with square-cut rubies, the black-bladed Valyrian sword Blackfyre at his hip, '
              'silent and watchful'),
    'VISENYA': (f'Queen Visenya Targaryen as described in the books, a tall severe warrior woman of about thirty-two, {VAL}, '
                'hair in one tight warrior braid, a stern unsmiling mouth, dark mail over black leather, a long Valyrian steel sword '
                '(Dark Sister) with rippled grey steel at her hip'),
    'RHAENYS': (f'Queen Rhaenys Targaryen as described in the books, a bright warm playful young woman of about twenty-five, {VAL}, '
                'loose curling hair, a mischievous half-smile, flowing red and black silk with a light riding cloak'),
    'DAENYS': (f'Daenys the Dreamer, a Valyrian maiden of about fourteen, {VAL}, very long loose hair, wide haunted violet eyes, '
               'pale ivory silk nightgown'),
    'AENAR': (f'Lord Aenar Targaryen, a Valyrian dragonlord of about fifty, {VAL}, a short silver beard, a deep-lined resolute face, '
              'a dark red-black robe with a gold dragon clasp'),
    'GYLDAYN': ('an old archmaester of the Citadel, face NOT shown, an old man in a grey wool robe with a heavy chain collar of many '
                'linked metals, ink-stained hands with a quill'),
    'BALERION': ('Balerion the Black Dread as described in the books, a colossal ancient dragon with jet-black scales, wings as his '
                 'forelimbs vast enough to darken a town, two massive hind legs, a long horned head with teeth like black swords, '
                 'smoke curling from his nostrils, black fire edged with red'),
    'VHAGAR': ('Vhagar, a huge dragon with bronze scales tinted blue-green, wings as forelimbs, two hind legs, a long horned head, '
               'fierce'),
    'MERAXES': ('Meraxes, a large graceful dragon with silver-white scales shading to pale gold, wings as forelimbs, two hind legs, '
                'golden eyes'),
}


def key(n):
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


def prompt(typ, cast, body):
    who = '; '.join(CAST[c] for c in cast)
    subj = f'{who}, {body}' if who else body
    return f'{STYLE} {subj}. {PALETTE} Camera: {CAMERA[typ]}. Texture: fine film grain, atmospheric haze, tactile materials. {NO_TEXT}'


def _rows():
    import got003_plan as P
    rows = [(n, sl, ch, ty, ca, rc, bd, list(rf)) for n, sl, ch, ty, ca, rc, bd, rf in P.B1]
    num = {r[1]: r[0] for r in rows}
    n = len(rows)
    for sid, si, anc, shot, rec in P.PLAN:
        if isinstance(shot, tuple):
            n += 1
            slug, typ, cast, body, refs = shot
            num[slug] = n
            rows.append((n, slug, sid, typ, cast, rec, body, [r if isinstance(r, int) or ':' in str(r) else num[r] for r in refs]))
    return rows, num


ROWS, NUM = _rows()


def batch_json(n_batch, rows):
    imgs = []
    for n, slug, ch, typ, cast, rec, body, refs in rows:
        imgs.append({'scene_id': f'GOT003_SCENE{n:03d}', 'key': key(n),
                     'file': f'GOT003_BATCH{n_batch:03d}_SCENE{n:03d}_{slug}.png', 'chapter': ch, 'shot_type': typ,
                     'cast': cast, 'motion_recipe': rec, 'prompt': prompt(typ, cast, body), 'negative': NEGATIVE,
                     'refs': [x if isinstance(x, str) else key(x) for x in refs], 'qc': 'PENDING'})
    return {'episode': 'GOT003', 'batch': f'BATCH{n_batch:03d}', 'max_batch_size': 10, 'status': 'PLANNED',
            'style': STYLE, 'palette': PALETTE, 'images': imgs}


def write_new():
    OUT.mkdir(parents=True, exist_ok=True)
    nb = len(ROWS) // 10
    for b in range(1, nb + 1):
        p = OUT / f'GOT003_BATCH{b:03d}.json'
        if p.exists():
            continue
        p.write_text(json.dumps(batch_json(b, [r for r in ROWS if (r[0] - 1) // 10 + 1 == b]), indent=1, ensure_ascii=False))
        print('wrote', p.name)


if __name__ == '__main__':
    write_new()
