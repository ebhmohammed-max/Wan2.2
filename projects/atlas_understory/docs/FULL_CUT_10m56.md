# The complete cut — 10:56:01, 98 slots, continuous plates

Delivered 2026-11-05 to the Video 01 root: `1llRO_x9IFZMg2mDs6ikUCXitsHi_RTpK`

| | |
|---|---|
| File | `00_v2 COMPLETE 10m56:01 — continuous plate cut (VO + edit bed).mp4` |
| Drive id | `1GHn7S9-XsOrY57hEJkSdko_Xhjo1GkJD` |
| Length | **15,745 frames = 00:10:56:01 at 24 fps** (the handoff's own figure) |
| Spec | 1920×1080, 24 fps CFR, H.264 High, yuv420p, no audio stream, ~1.06 Mbps |
| Size | 86.9 MB |
| Cue sheet | `04 — Cue sheet 10:56:01` — Google Sheet `1ypJuaO_3NF9AuUCZXp546aAnuK11LRA932cUqmk8w0I` |

## What it is

Every one of the script's 98 shots, in scripted order, at its scripted duration, with the picture
never stopping. The 49 background-plate positions play the approved clips at native speed, motion
untouched. The other 49 positions — 46 editor graphics and the 3 photo framings — carry plate
imagery from the six worlds instead of standing empty, so the film runs continuously at 10:56.

This is a **VO + edit bed**. It is the timing spine the script was written for: drop the narration
on the cue sheet's timecodes, then lay the real graphics panels over the 49 filled slots.

## How it was built

1. Slot list and durations parsed from the shot map audit (98 shots) and the delivery index (49 clip ids).
2. 49 approved clips pulled back from Drive — every duration re-probed against the shot map, 0 mismatches.
3. 49 fill clips rendered from the six world anchors and the six Tier 3 spares, using the same
   three approved recipes (M02 / M03 / M08), at each slot's own scripted duration. World per slot =
   the nearest plate shot's world, so chapters stay inside their own chapter.
4. Assembled with ffmpeg's concat **filter**, not the concat demuxer. This matters: stream-copy
   concatenation drops ~0.05 s at every join — 4.5 s across 98 joins — which put the first build at
   10:51.50. The filter concatenates decoded frames, and the master lands exactly on 15,745 frames.
5. Two-pass ABR encode at 1.06 Mbps to fit Drive's single-request upload path (masters above
   ~100 MB cannot be uploaded here).

## Two things to know before you edit

- **The 49 filled slots are stand-ins.** They are plate imagery, not the graphic panels. When the
  graphics agent delivers, cut the panels over those slots — the timecodes are in the cue sheet.
- **This file is a review/assembly master, not the edit-grade source.** At 1.06 Mbps it is soft
  against the original clips. For the edit, use the 49 individual clips in the batch folders
  (CRF 17, 1080p24) — same durations, better picture. Ask and I can produce a high-bitrate
  assembly master by splitting it across two files or using the resumable upload path.

## What the timing matches

- Scripted runtime: 10:56.01 (1,427 spoken words at 145 wpm, 10 % of runtime reserved for pauses).
- Frames 0–15,745, no gaps, no overlaps — Out values exclusive, exactly as the shot map specifies.
- Plate-dominant screen time upstream of the graphics: 49.95 % of the runtime (49 of 98 slots).

## Verified

- 15,745 frames decoded from the delivered file — matches the cue sheet frame for frame.
- 1920×1080, 24 fps CFR, yuv420p, High profile; **no audio stream present** (VO goes in as a separate layer).
- 86.9 MB, uploaded whole.

## Still yours

- The Met accession flag (1978.93.30 delivered vs 1978.93.29 scripted) — untouched, as agreed.
- C02-S007 / C02-S009 keep the single sourced photograph, per the shot map.
