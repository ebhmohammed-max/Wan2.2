# Narration build — state on disk

Voice: `voice-00` (auditioned on the film's opening lines, user-selected).

Chunks recorded so far — `audio/vo_01.mp3` … `audio/vo_10.mp3`, **478.0 s total**, covering
VO-C01-B01 through VO-C04-B07 (40 of the script's 48 segments, verbatim).

Still to record (3 chunks, ~2 minutes of audio):

- **vo_11** — C04-B08, C04-B09, C05-B01, C05-B02
- **vo_12** — C05-B03, C05-B04, C05-B05
- **vo_13** — C05-B06, C05-B07, C05-B08, C05-B09

Then `scripts/assemble_vo.py` measures the 13 chunks, applies one uniform tempo factor so the read
lands at ~145 wpm inside 10:56:01, places them with 1.0 s seams, loudness-normalises to −16 LUFS,
and muxes AAC onto the existing video without touching the picture.

Limit hit: speech generation is capped at 10 clips per turn, which is why this stopped at 10.
