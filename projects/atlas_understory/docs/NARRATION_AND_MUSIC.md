# Atlas Understory — Video 01: narration and music

Sheet for the v3 deliverable: the 10:56:01 continuous plate cut with the full spoken script and a
background music bed.

- Video: `01_v3 COMPLETE 10m56:01 — narration + music.mp4` (Drive id `1WO01KHN53AQVAUTp04g-v9GCNa_BeLhr`)
- Picture: the v2 plate cut, stream-copied — **no picture re-encode, no change to shot order, durations or overlays**
- Audio: AAC-LC 112 kb/s stereo 48 kHz, master **−16 LUFS** integrated, **−1.5 dBTP**
- Length: **15,745 frames = 00:10:56:01** at 24 fps; audio 00:10:56.04

## Narration

The script copy is authoritative and is spoken **verbatim** — no rewrites, no added claims, no
paraphrase, no reordering.

| Item | Value |
|---|---|
| Words | 1,427 |
| Segments | 48, in script order |
| Renders | 13 (`audio/vo_01.mp3` … `vo_13.mp3`) |
| Voice | `voice-00`, English, narration register |
| Raw speech | 626.1 s |
| Delivered pace | ≈ 137 words per minute |
| Tempo applied | **×1.000** — the read already sits at or below the scripted pace, so nothing was sped up |
| Lead-in | 1.2 s |
| Seam between segments | 1.0 s |
| Voice span | 1.2 s → 639.3 s of 656.04 s (16.7 s of tail) |

The 17-second tail is deliberate: the last line is a full stop, and the film needs room to breathe
before the music resolves.

## Music

| Item | Value |
|---|---|
| Track | **"Ambiment" — Kevin MacLeod (incompetech.com)** |
| Licence | **Creative Commons Attribution 4.0 (CC BY 4.0)** — https://creativecommons.org/licenses/by/4.0/ |
| Source | 22:52 mp3, from the project's `Audio (voiceover + music)` folder |
| Used | 0:00 → 10:56 of the track (first cue), changed in length and format |
| Level | 0.16 (≈ −16 dB under the voice) |
| Fades | 6 s in, 10 s out |
| Ducking | side-chain compressor keyed by the narration — threshold 0.035, ratio 7, attack 15 ms, release 520 ms |

**Credit line for the deliverable, on screen or in the description:**

> Music: "Ambiment" by Kevin MacLeod (incompetech.com) — licensed under Creative Commons
> Attribution 4.0, https://creativecommons.org/licenses/by/4.0/. Changed in length and format.

CC BY 4.0 obliges us to name the work, name the author, link the licence, and state that we changed
it. All four are in the credit line above and in the Drive file description.

## Measured

| Measure | Value |
|---|---|
| Mix before mastering | −23.25 LUFS, true peak −6.77 dBFS, LRA 28.6 LU |
| Master | −16.8 LUFS integrated (ebur128), −1.5 dBTP ceiling |
| Video | 1920×1080, H.264 High ≈ 1057 kb/s, 24 fps CFR, `+faststart` |
| Size | 96.3 MB |

The wide loudness range is the film's own shape — long quiet openings, a dense middle — and was left
alone deliberately: the master is a linear gain, not a compressor.

## How it was built

`scripts/assemble_vo.py`, four stages, each printed as it completes:

1. **voice bed** — every chunk `atempo` × 1.000 → `adelay` to its scripted slot → `apad` to film length → `amix` → `loudnorm I=-16 TP=-2`
2. **music bed** — `atrim 0:656.042` → `volume 0.16` → fade in/out → `sidechaincompress` keyed by the voice
3. **mix** — voice + ducked music → `alimiter 0.95` → `apad`/`atrim` to exactly 656.042 s
4. **master + mux** — two-pass `loudnorm` on the finished mix → picture stream copied, audio encoded `apad`-ed to film length

Timeline data (per-segment starts, durations, tempo, pace) is in `audio/vo_timeline.json`.

## Two things to know

1. **Pace.** The read came out at ≈ 137 wpm; the script was timed at 145 wpm. Because 626 s of speech
   in 656 s of film already fits with 17 s to spare, **no tempo change was applied** — the voice is
   exactly as recorded. If you want it brisker, a ×1.05 tempo against the same timeline gains about
   13 s of air without touching any wording; say the word and it is a one-line change.
2. **Picture is still stand-in.** The 49 plate slots hold renders, not the editor's finished graphics
   panels, and there are no title cards or captions. This is the narration/music gate; laying the real
   panels over those slots is the next gate.

## Credit to keep visible

- Narration: original, written for this film from the approved script
- Music: "Ambiment" by Kevin MacLeod (incompetech.com), CC BY 4.0, changed in length and format
- Plate imagery: generated for this project; the Met bulla photograph is public domain,
  acc. 1978.93.30 (the scripted 1978.93.29 was not available — **flagged, not rewritten**)
