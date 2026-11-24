#!/usr/bin/env python3
"""Word-level timestamps for VO takes (runs on the GitHub Actions runner; needs faster-whisper + model download).

  python ci_align.py <dir with *.mp3> <out.json>

Output: {"<clip stem>": [[word, start_s, end_s, prob], ...], ...}
Script-to-transcript matching happens later (tools/v2_timeline.py), so transcription errors on
proper nouns only cost that one word's anchor, never the whole alignment.
"""
import glob, json, os, subprocess, sys, time
import numpy as np
import imageio_ffmpeg
from faster_whisper import WhisperModel

PROMPT = ("Muad'Dib, Paul Atreides, Arrakis, Arrakeen, Fremen, Irulan, Chani, Qizarate, Korba, Fedaykin, "
          "Wallach Nine, Bene Gesserit, Mohiam, Edric, Scytale, Bene Tleilax, Tleilaxu, Hayt, Mentat, ghola, "
          "Lichna, Otheym, Bijaz, Shai-Hulud, Sietch Tabr, Leto, Ghanima, Alia, crysknife, Mythic Archives.")
PROMPTS = {  # proper-noun hints per episode (EP env var; default DUN003 = PROMPT above)
    'DUN001': ("Butlerian Jihad, Omnius, Erasmus, Agamemnon, Xerxes, Titans, cymeks, Serena Butler, Manion, "
               "Xavier Harkonnen, Iblis Ginjo, Vorian Atreides, Dream Voyager, Salusa Secundus, Giedi Prime, "
               "Corrin, Tlulaxa, hrethgir, Hrethgir, Abulurd, Faykan, Corrino, Lankiveil, Mentats, Arrakis, "
               "Golden Lion Throne, Mythic Archives."),
}
PROMPT = PROMPTS.get(os.environ.get('EP', 'DUN003').upper(), PROMPT)

src, out = sys.argv[1], sys.argv[2]
model = WhisperModel(os.environ.get('WHISPER_MODEL', 'small.en'), device='cpu', compute_type='int8',
                     cpu_threads=os.cpu_count())
res = {}
for f in sorted(glob.glob(os.path.join(src, '*.mp3'))):
    t0 = time.time()
    pcm = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-v', 'error', '-i', f, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    audio = np.frombuffer(pcm, np.float32).copy()
    segs, _ = model.transcribe(audio, language='en', word_timestamps=True, beam_size=5, initial_prompt=PROMPT,
                               vad_filter=False, condition_on_previous_text=True)
    words = [[w.word.strip(), round(w.start, 3), round(w.end, 3), round(w.probability, 3)]
             for s in segs for w in s.words]
    res[os.path.splitext(os.path.basename(f))[0]] = words
    print(os.path.basename(f), len(words), 'words', round(time.time() - t0, 1), 's', flush=True)
json.dump(res, open(out, 'w'), indent=0)
