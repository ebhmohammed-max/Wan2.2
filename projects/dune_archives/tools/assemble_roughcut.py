#!/usr/bin/env python3
"""Assemble an episode rough cut (or a slate animatic) from the timed storyboard.

  python assemble_roughcut.py DUN003 --vo <master.mp3> --out <file.mp4>
        [--images <dir with the batch PNG/JPGs downloaded from Drive>]
        [--animatic] [--res 1920x1080] [--crf 20] [--workdir /tmp/rc] [--jobs 2]

How each storyboard row becomes a segment:
  * MAP rows: the rendered map clip from 19_batches/<EP>/maps/, scaled and trimmed (last frame
    held if it's too short)
  * image rows: motion_engine.render_shot(image, recipe from the storyboard, exact length). REUSE/CROP
    rows use the same plate with a tighter focus
  * missing image, or --animatic: a slate card showing shot number, scene, recipe, description and VO line
Overlays: the `onscreen_text` column is burned in as a lower third. The archive card gets its title card.
Every image or slate shot carries a small "CREATIVE RECONSTRUCTION" corner bug; map clips carry their own caption.
Cut points come from `tc_in_s` (retime_storyboard.py), converted to exact frame counts so nothing drifts.
The VO master is muxed at 0 s, padded with silence to the programme length.
"""
import argparse, csv, glob, io, json, math, os, pathlib, subprocess, sys, textwrap
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import imageio_ffmpeg  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 24
ARCHIVE_CARD = ['THE DUNE ARCHIVES', 'ERA: c. 10,200 A.G.', 'SUBJECT: DUNE MESSIAH',
                'SOURCE: THE ORIGINAL FRANK HERBERT NOVELS', 'RECONSTRUCTIONS ARE LABELLED ON SCREEN']
SKIP_TEXT = {'', 'labels in edit'}


def font(size, bold=False):
    p = '/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf' % ('-Bold' if bold else '')
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()


def overlay_png(path, W, H, text, archive=False, bug=True):
    """Transparent overlay: optional lower-third text, optional archive card, corner bug."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    k = H / 1080
    if archive:
        d.rectangle((0, 0, W, H), fill=(5, 8, 14, 170))
        y = int(330 * k)
        for i, line in enumerate(ARCHIVE_CARD):
            f = font(int((54 if i == 0 else 30) * k), bold=(i == 0))
            d.text((int(160 * k), y), line, font=f, fill=(236, 214, 170, 255) if i == 0 else (220, 220, 220, 255))
            y += int((90 if i == 0 else 52) * k)
    elif text:
        f = font(int(30 * k), bold=True)
        tw = d.textlength(text, font=f)
        x0, y0 = int(90 * k), int(H - 190 * k)
        d.rectangle((x0 - int(24 * k), y0 - int(18 * k), x0 + tw + int(24 * k), y0 + int(52 * k)), fill=(0, 0, 0, 165))
        d.text((x0, y0), text, font=f, fill=(240, 222, 186, 255))
    if bug:
        f = font(int(18 * k))
        d.text((W - int(330 * k), int(40 * k)), 'CREATIVE RECONSTRUCTION', font=f, fill=(230, 230, 230, 150))
    im.save(path)
    return path


def slate_png(path, W, H, r, missing):
    im = Image.new('RGB', (W, H), (14, 16, 22))
    d = ImageDraw.Draw(im)
    k = H / 1080
    d.text((int(80 * k), int(70 * k)),
           f"SHOT {int(r['shot_no']):03d}  ·  {r['scene_id']}  ·  {r['shot_type']}  ·  {r['motion_recipe']}",
           font=font(int(34 * k), True), fill=(226, 186, 110))
    d.text((int(80 * k), int(122 * k)), f"{r['chapter']}  ·  mood: {r['mood']}", font=font(int(24 * k)), fill=(170, 170, 180))
    y = int(220 * k)
    for line in textwrap.wrap(r['description'], 70)[:7]:
        d.text((int(80 * k), y), line, font=font(int(32 * k)), fill=(230, 230, 230))
        y += int(46 * k)
    y = max(y + int(30 * k), int(640 * k))
    vo = r['vo_line']
    for line in textwrap.wrap(f'VO: {vo}', 78)[:4]:
        d.text((int(80 * k), y), line, font=font(int(28 * k)), fill=(240, 210, 150))
        y += int(40 * k)
    d.text((int(80 * k), int(H - 80 * k)),
           (f"IMAGE: {r['image_file']}" if r['image_file'] else 'MAP') + ('   [ANIMATIC SLATE — image not loaded]' if missing else ''),
           font=font(int(20 * k)), fill=(120, 125, 140))
    im.save(path)
    return path


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(' '.join(cmd[:6]) + '...\n' + p.stderr[-2000:])


def enc_args(W, H, crf):
    return ['-vf', f'scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast',
            '-crf', str(crf), '-an', '-video_track_timescale', '12288']


def build_segment(i, r, nframes, a):
    W, H = a.W, a.H
    wd = pathlib.Path(a.workdir)
    seg = wd / f'seg_{i:03d}.mp4'
    if seg.exists() and seg.stat().st_size > 0 and not a.force:
        return seg
    text = r['onscreen_text'].strip()
    archive = 'ARCHIVE CARD' in text
    text = '' if (text in SKIP_TEXT or archive) else text
    dur = nframes / FPS
    is_map = r['unique_or_reuse'] == 'MAP'
    img = None
    if not is_map and not a.animatic and a.images and r['image_file']:
        stem = pathlib.Path(r['image_file']).stem
        hits = sorted(glob.glob(os.path.join(a.images, stem + '.*')))
        img = hits[0] if hits else None
    base = wd / f'base_{i:03d}.mp4'
    if is_map:
        mp4 = ROOT / '19_batches' / a.ep / 'maps' / pathlib.Path(r['map_scene_json']).name.replace('.json', '.mp4')
        run([FF, '-y', '-loglevel', 'error', '-i', str(mp4), '-vf',
             f'tpad=stop_mode=clone:stop_duration=30', '-frames:v', str(nframes), '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '16', '-an', str(base)])
    elif img:
        import motion_engine
        focus = (0.5, 0.42) if r['unique_or_reuse'] == 'REUSE' else (0.5, 0.5)
        motion_engine.render_shot(img, str(base), recipe=r['motion_recipe'] or 'DRIFT', duration=dur + 0.05,
                                  focus=focus, crf=16)
    else:
        png = slate_png(wd / f'slate_{i:03d}.png', W, H, r, missing=True)
        run([FF, '-y', '-loglevel', 'error', '-loop', '1', '-framerate', str(FPS), '-i', str(png),
             '-frames:v', str(nframes), '-c:v', 'libx264', '-preset', 'veryfast', '-tune', 'stillimage', '-crf', '16',
             '-pix_fmt', 'yuv420p', str(base)])
    ov = overlay_png(wd / f'ov_{i:03d}.png', W, H, text, archive=archive, bug=not is_map)
    run([FF, '-y', '-loglevel', 'error', '-i', str(base), '-i', str(ov), '-filter_complex',
         f'[0:v]scale={W}:{H}:flags=lanczos,fps={FPS}[b];[b][1:v]overlay=0:0,format=yuv420p',
         '-frames:v', str(nframes), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', str(a.crf), '-an',
         '-video_track_timescale', '12288', str(seg)])
    base.unlink(missing_ok=True)
    return seg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ep')
    ap.add_argument('--vo', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--images')
    ap.add_argument('--animatic', action='store_true')
    ap.add_argument('--res', default='1920x1080')
    ap.add_argument('--crf', type=int, default=20)
    ap.add_argument('--workdir', default='/tmp/rc')
    ap.add_argument('--jobs', type=int, default=2)
    ap.add_argument('--hold', type=float, default=2.0, help='end-card hold after the last VO')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    a.W, a.H = map(int, a.res.split('x'))
    pathlib.Path(a.workdir).mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(ROOT / f'18_storyboards/{a.ep}_STORYBOARD.csv', newline='')))
    tcs = [float(r['tc_in_s']) for r in rows]
    end = tcs[-1] + float(rows[-1]['duration_s'])
    fr = [round(t * FPS) for t in tcs] + [round(end * FPS)]
    jobs = [(i, r, fr[i + 1] - fr[i]) for i, r in enumerate(rows)]
    with ThreadPoolExecutor(a.jobs) as ex:
        segs = list(ex.map(lambda j: build_segment(j[0], j[1], j[2], a), jobs))
    lst = pathlib.Path(a.workdir) / 'concat.txt'
    lst.write_text(''.join(f"file '{s}'\n" for s in segs))
    vid = pathlib.Path(a.workdir) / 'video.mp4'
    run([FF, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(vid)])
    run([FF, '-y', '-loglevel', 'error', '-i', str(vid), '-i', a.vo, '-filter_complex', '[1:a]apad[a]',
         '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', f'{fr[-1] / FPS:.3f}',
         '-movflags', '+faststart', a.out])
    print('wrote', a.out, 'frames', fr[-1], 'duration', round(fr[-1] / FPS, 2))


if __name__ == '__main__':
    main()
