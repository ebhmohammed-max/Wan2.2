# 08 — Finishing (HyperFrames) · what is in this folder

Everything here is one instruction set for the HyperFrames finishing agent, for **Atlas Understory · Video 01 ·
"The Lighthouse Ring Found in Alexandria's Sunken Palace"** (10:56:01, 15,745 frames, 24 fps).

| File | What it is | Read |
|---|---|---|
| `00_KICKOFF.txt` | The message to paste to the agent to open the job | **first** |
| `HYPERFRAMES_BUILD_BRIEF.md` | The full build instruction — sections 0–16, appendices A–G | **second, in full** |
| `SCRIPT_VERBATIM.md` | All 48 spoken segments, character for character | during Phase 3 |
| `OVERLAY_TIMELINE.csv` | All 98 slots: TC, duration, frames, type, MG/VX, rack, template, motion | during Phase 1 |
| `PANEL_MOTIFS.md` | The twelve argument motifs that decide what each panel is | during Phase 4 |
| `FACT_STRINGS.md` | The only factual strings that may be set in type | during Phase 4 |
| `PRONUNCIATION_AND_SPELLING.md` | ASR repair locks and caption spelling rules | during Phase 3 |
| `TRANSITION_MAP.csv` | 29 permitted transition events, with frames and rules | during Phase 7 |
| `COLOR_TYPE_TOKENS.css` | Locked tokens: palette, type scale, grid, motion, texture | during Phase 2 |
| `CHAPTER_TIMING_estimate.csv` | 5 chapter onsets, word-count proportion (planning only) | planning |
| `SEGMENT_TIMING_estimate.csv` | 48 segment onsets, same method (planning only) | planning |

## The three numbers the whole job hangs on

- **15,745 frames** in, 15,745 frames out. No retime, no re-cut, no frame-rate change.
- **656.042 s** at 24.000 fps CFR. Every overlay is timed against this, not against a scrubber.
- **−16.0 LUFS / true peak −1.9 dBFS.** The approved mix is carried through untouched and proved with a null test.

## The one design decision that matters most

The frozen shot map braids all five chapters together, one beat at a time — five evidence panels (one per chapter),
then five living plates (one per chapter), repeated 22 times — while the narration runs straight through the chapters.
So a panel is never heard with its own chapter's voice. That is why the brief adds a **persistent chapter rail** and
demands that **every panel be a closed exhibit** that can be read cold, paused, and screenshotted.

Everything else in the brief follows from those two facts.

## Honest status

- This is an instruction set, not a render. No frame has been produced yet.
- The 46 panel *texts* live in the shot map's `Graphic Specifications` sheet (Drive
  `1wKuxtjWPIHIBzOc0O8Ph0Sw7RBhM_B4YO7UJ7rPgFZ4`). If any slot's text is missing, the agent must render
  `TEXT PENDING — DO NOT RENDER` and list it. Invented panel copy is a failure, not a fix.
- Chapter onsets in the two estimate files are proportional to word count, within a few seconds. The agent's
  transcription-and-alignment pass replaces them; the brief requires ±2 frames against that alignment.
- The Met accession on screen is **1978.93.30**, not the scripted 1978.93.29. That is reported, never rewritten.
