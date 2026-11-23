# DUN003 edit package

| File | What it is |
|---|---|
| `DUN003_ANIMATIC_v1_720p.mp4` | **Slate animatic** with the real VO, built in the sandbox. There is one slate card per storyboard shot (shot number, scene, recipe, description, VO line), plus the 3 real map clips, the on-screen text and the archive card. Use it to review pacing and timing. The 150 stills are on Drive but couldn't be loaded here: the sandbox can't reach Google Drive file downloads. |
| `../../tools/assemble_roughcut.py` | The same assembler. Run it locally with the stills to get the **full-resolution motion rough cut** (see below). |
| `../../21_music/DUN003_MUSIC_CUE_SHEET.md` | Music and SFX cue sheet, timed to this timeline |
| `../../20_voiceover/DUN003/DUN003_VO_LOG.md` | VO files, chapter windows, and the method |

## Full rough cut on your machine (about 30–60 min on CPU)
1. Get the inputs from Drive:
   - Download the DUN003 folder (stills) into one directory, e.g. `~/dun003_images/`. File names must match the storyboard's `image_file` column; the extension can be .png or .jpg.
   - Also download `20_voiceover/DUN003_VO_FULL_paced_v2.mp3`.
2. Set up Python 3.10+:
   ```
   python -m venv venv && venv/bin/pip install numpy pillow imageio-ffmpeg
   ```
3. Run from `projects/dune_archives/`:
   ```
   venv/bin/python tools/assemble_roughcut.py DUN003 \
       --images ~/dun003_images --vo DUN003_VO_FULL_paced_v2.mp3 \
       --out DUN003_ROUGHCUT_v1_1080p.mp4 --res 1920x1080 --crf 18 --jobs 4
   ```
   - Each image shot is rendered with `motion_engine.py` using the storyboard's recipe (PUSH_IN, DRIFT, PAN…) at its exact length.
   - Any still that's missing falls back to a slate, so a partial download still produces a full-length cut.
4. In the NLE (Resolve or Premiere), on top of the rough cut:
   - music and SFX per the cue sheet;
   - the 2 s pauses after 00:37 and 10:24 (see the VO log), which push later material back by 2 s each;
   - the final colour pass.

## Version history
| Version | Date | Notes |
|---|---|---|
| Animatic v1 | 2026-11-23 | 720p slates with VO master v2, storyboard v4 and maps A/B/C. 12:11 |

## Drive
- Folder 22_edit: `1q8ObdH9yFb9Ld9gVlcwRICYYOyX4N-1T`
- Animatic v1: `1-xSH0X7JzFHwUljf8yFdc50-spwy2HvJ`
- Music cue sheet Doc (folder 21_music): `1cECIHREX6n_LKJqYCBeGRHyxeXVVTqWpFaeOBeacwTw`

## v1 master (2026-11-23)
- **The video:** 1920x1080 24p, 12:11, H.264 CRF 20 + AAC 320k. It has all 150 stills with storyboard camera moves (`tools/fast_motion.py`), the 3 animated maps, lower thirds, the archive card and the CREATIVE RECONSTRUCTION bug.
- **Audio:** `DUN003_MIX_v1.m4a`, which is the VO + music + SFX at -14 LUFS.
- **Rebuild (about 17 min on 2 CPUs):**
  ```
  python tools/assemble_roughcut.py DUN003 --vo 22_edit/DUN003/DUN003_MIX_v1.m4a \
    --images 19_batches/DUN003/stills_jpg --out DUN003_MASTER_v1_1080p.mp4 --crf 20 --abr 320k --jobs 2
  ```
- **Stills:** `19_batches/DUN003/stills_jpg/`, JPG q90 copies of the Drive PNGs, fetched by CI (`tools/ci_fetch_assets.py stills`).
- **Master on Drive:** the CI workflow `.github/workflows/dun003_master.yml` renders it on a GitHub runner and streams it into a Drive resumable-upload session.
- **Review copy:** `DUN003_REVIEW_v1_720p.mp4` (under 100 MB, git-ignored, on Drive).
- MASTER v1 on Drive: `1Jp5srTr7fRHaPxkAZ4zNZLMoM_kA1H1d`; REVIEW v1: `109KxMbBTj32bLVpB3Vzp2YqIWj_luPbs`; music credits Doc: `1W4kRnlpyaGAJXgInQlvjP0WzvoX684SmuCCcXAc4wxU`
