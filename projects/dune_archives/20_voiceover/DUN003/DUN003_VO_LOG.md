# DUN003 narration (VO) log

| Field | Value |
|---|---|
| Voice | in-app TTS `voice-06`. Picked by the director in audition 7 (en-US male; the earlier 6 pairs were rejected) |
| Source text | `17_scripts/DUN003_SCRIPT_v1.0.md` (revision 1.1), VO lines only, unchanged except "A.G." written as "A. G." |
| Status | **SCRATCH / DRAFT VO.** 22 [VERIFY] fact checks are still open. Re-record any section whose text changes |
| Format | MP3, 64 kbps, 44.1 kHz |

| File | Script sections | Duration | Status |
|---|---|---|---|
| DUN003_VO_00-01_cold_open_archive_card.mp3 | 00 + 01 | 48.9 s | OK |
| DUN003_VO_02_where_dune_left_paul.mp3 | 02 | 62.8 s | OK |
| DUN003_VO_03_price_of_the_jihad.mp3 | 03 | 71.6 s | OK |
| DUN003_VO_04_the_conspiracy.mp3 | 04 | 93.3 s | OK |
| DUN003_VO_05_the_gift_hayt.mp3 | 05 | 69.4 s | OK |
| DUN003_VO_06_the_trap_closes.mp3 | 06 | 68.3 s | OK |
| DUN003_VO_07_the_blind_emperor.mp3 | 07 | 47.5 s | OK |
| DUN003_VO_08_chani_and_the_twins.mp3 | 08 | 66.8 s | OK. Approved rev 1.1 line; recorded in 2 parts (`parts/08a`, `parts/08b`) and joined with a 0.55 s pause |
| DUN003_VO_09-10_into_the_desert_book_vs_film.mp3 | 09 + 10 | 94.0 s | OK |
| DUN003_VO_11_coda_the_warning.mp3 | 11 | 40.3 s | OK |
| **Total, raw sections** | | **662.8 s (11:03)** | |
| **DUN003_VO_FULL_paced_v1.mp3** | all, in order | **731.4 s (12:11)** | Paced master (option a), 128 kbps |

## Section 08 block
The suspected trigger is "Scytale holds a knife over the newborn twins" (the same issue as the S116 image refusal).
Proposed softened line, which needs director approval because the script text is locked:
> "And to force the choice, Scytale threatens the newborn twins."
The closing line "…Paul finds Scytale, and throws his knife." stays as written.

## Pacing finding
The voice reads at about 177 wpm, against the script's budget of 135 wpm. Adding section 08 (about 61 s at this pace) gives a full VO of about **11:00**, not the planned 15:00.
Options:
- (a) Add pauses in the edit, about 1–1.5 s between paragraphs and 2–3 s at chapter breaks, for roughly 12:00–12:30.
- (b) Accept a runtime of about 12 min and re-time the storyboard.
- (c) Slow the audio slightly in the edit (0.9×) at some cost to voice quality.

## Section 08 resolution (turn 25)
- The director approved option 08: the line now reads "And to force the choice, Scytale threatens the newborn twins." It is changed in the script (rev 1.1), the storyboard CSV row 142 and `data/dun003_episode.py`.
- The whole of section 08 was **still blocked** even with the softened line, so the filter reacts to the section as a whole: death in childbirth, "kill Paul", the twins and the knife together.
- Recording it as two halves (08a up to "…the man he used to be."; 08b from "Then Scytale makes his offer.") worked with the same text.

## Paced master (option a, approved)
- Built with `tools/vo_build.py full`, using the ffmpeg binary from pip `imageio-ffmpeg` in a venv at /tmp/mv. The venv must be recreated if it is lost.
- Pauses of 0.42 s or longer (sentence ends) are found with silencedetect at −38 dB, and each gets +0.4 s. A 2.5 s gap goes between section files.
- Limits:
  - Chapter breaks inside the combined files (00/01 and 09/10) only get sentence-level pacing. In the edit, add about 2 s after "…much harder to look at." and after "…The man is gone."
  - Paragraph-level pauses still need the editor's ear.
- Result: **12:11**. Storyboard timings, planned at 15:00, need re-timing to the master at the edit stage.

## Drive (folder 20_voiceover `1Du1eyJdMyQXd-gTmTxO-4zTeia0al4FQ`)
| File | Drive ID |
|---|---|
| DUN003_VO_FULL_paced_v1.mp3 (git-ignored; rebuild with `tools/vo_build.py full`) | `1Olw47n3n420y0NokQ-lbgKzrF3G8F0Dt` |
| DUN003_VO_sections_v1.zip (10 sections + this log) | `1IVs7vmoxgcFjkemu5IVdpkiKUvvqKAGE` |
