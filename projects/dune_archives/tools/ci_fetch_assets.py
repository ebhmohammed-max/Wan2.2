#!/usr/bin/env python3
"""Runs on a GitHub Actions runner (which has open internet; the Arena sandbox does not).

Jobs (pick with argv):
  stills   download the 150 DUN003 stills from Drive (folder shared by link for the
           duration of the fetch) using 22_edit/DUN003/stills_fetch_list.json, and save them
           as JPG q90 (long edge <= 1920) in 19_batches/DUN003/stills_jpg/
  catalog  build compact catalogues of free, monetisation-safe music libraries
           (incompetech = Kevin MacLeod, CC BY 4.0; FreePD = CC0) into 21_music/catalog/
  music    download the tracks listed in 21_music/DUN003/music_fetch_list.json into
           21_music/DUN003/tracks/ (re-encoded to 192k stereo mp3), with a sha256 + source log
"""
import hashlib, io, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (DuneArchives asset fetch; contact via GitHub)"}


def get(url, tries=4, timeout=90):
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except Exception as e:  # noqa
            last = e
            time.sleep(2 + 3 * k)
    raise RuntimeError(f"{url}: {last}")


def stills():
    from PIL import Image
    lst = json.load(open(os.path.join(ROOT, "22_edit/DUN003/stills_fetch_list.json")))
    out = os.path.join(ROOT, "19_batches/DUN003/stills_jpg")
    os.makedirs(out, exist_ok=True)
    log = []
    for e in lst:
        stem = os.path.splitext(e["name"])[0]
        dst = os.path.join(out, stem + ".jpg")
        if os.path.exists(dst):
            continue
        urls = [f"https://drive.usercontent.google.com/download?id={e['drive_id']}&export=download&confirm=t",
                f"https://drive.google.com/uc?export=download&id={e['drive_id']}"]
        ok = False
        for u in urls:
            try:
                data, ct = get(u)
                im = Image.open(io.BytesIO(data)).convert("RGB")
                w, h = im.size
                s = min(1.0, 1920 / max(w, h))
                if s < 1:
                    im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
                im.save(dst, "JPEG", quality=90, optimize=True)
                log.append(f"OK {stem} src={w}x{h} out={im.size[0]}x{im.size[1]} {os.path.getsize(dst)//1024}KB")
                ok = True
                break
            except Exception as ex:  # noqa
                log.append(f"retry {stem} via next url: {ex}")
        if not ok:
            log.append(f"FAIL {stem}")
    open(os.path.join(out, "_fetch_log.txt"), "w").write("\n".join(log) + "\n")
    print("\n".join(log[-5:]))


def catalog():
    out = os.path.join(ROOT, "21_music/catalog")
    os.makedirs(out, exist_ok=True)
    notes = []
    # incompetech (Kevin MacLeod) full piece list
    for u in ["https://incompetech.com/music/royalty-free/pieces.json",
              "https://incompetech.com/music/royalty-free/pieces.php"]:
        try:
            data, ct = get(u)
            pieces = json.loads(data)
            keep = []
            for p in pieces:
                keep.append({k: p.get(k) for k in ("title", "filename", "feel", "instruments", "bpm", "length",
                                                    "genre", "description", "uuid", "isrc", "sheetmusic") if k in p})
            json.dump(keep, open(os.path.join(out, "incompetech_pieces.json"), "w"), indent=0)
            notes.append(f"incompetech: {len(keep)} pieces from {u}; keys={sorted(pieces[0].keys())}")
            break
        except Exception as ex:  # noqa
            notes.append(f"incompetech {u}: {ex}")
    # FreePD (CC0) category pages
    fp = {}
    for cat in ["epic", "scoring", "horror", "world", "electronic", "misc", "upbeat", "romantic", "comedy"]:
        u = f"https://freepd.com/{cat}.php"
        try:
            html, _ = get(u)
            html = html.decode("utf-8", "ignore")
            links = sorted(set(re.findall(r'(?:href|src)="([^"]+\.mp3)"', html)))
            fp[cat] = [urllib.parse.urljoin(u, l) for l in links]
            notes.append(f"freepd {cat}: {len(links)} mp3")
        except Exception as ex:  # noqa
            notes.append(f"freepd {cat}: {ex}")
    json.dump(fp, open(os.path.join(out, "freepd_tracks.json"), "w"), indent=0)
    open(os.path.join(out, "_catalog_log.txt"), "w").write("\n".join(notes) + "\n")
    print("\n".join(notes))


def music():
    import subprocess
    lst = json.load(open(os.path.join(ROOT, "21_music/DUN003/music_fetch_list.json")))
    out = os.path.join(ROOT, "21_music/DUN003/tracks")
    os.makedirs(out, exist_ok=True)
    log = []
    for e in lst:
        dst = os.path.join(out, e["id"] + ".mp3")
        if os.path.exists(dst):
            continue
        try:
            data, ct = get(e["url"], timeout=180)
            raw = dst + ".src"
            open(raw, "wb").write(data)
            sha = hashlib.sha256(data).hexdigest()
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-ac", "2", "-ar", "44100",
                            "-b:a", "160k", dst], check=True)
            os.remove(raw)
            dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                  "default=nw=1:nk=1", dst], capture_output=True, text=True).stdout.strip()
            log.append(f"OK {e['id']} {dur}s sha256(src)={sha} ct={ct} url={e['url']}")
        except Exception as ex:  # noqa
            log.append(f"FAIL {e['id']} {e['url']}: {ex}")
    open(os.path.join(out, "_fetch_log.txt"), "a").write("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    for job in sys.argv[1:]:
        {"stills": stills, "catalog": catalog, "music": music}[job]()
