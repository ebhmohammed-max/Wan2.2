#!/usr/bin/env python3
"""Narration + music over the 10:56 continuous cut.

Narration: every audio/vo_NN.mp3 (chunks of the approved v4 script, verbatim), measured,
sped by ONE uniform tempo factor so the read lands at the script's pace inside 10:56:01,
placed with 1.0 s seams, loudness-normalised to -16 LUFS.

Music: 'Ambiment' by Kevin MacLeod (CC BY 4.0) - quiet ambient bed, trimmed to film length,
faded in and out, sat well under the voice and side-chain ducked by the narration.

Outputs:
  audio/narration_10m56.wav       voice only, film length
  audio/music_10m56_ducked.wav    music after ducking, film length
  audio/mix_10m56.wav             finished mix (pre-master)
  audio/mix_10m56_master.wav      mix after two-pass loudnorm to -16 LUFS / -1.5 dBTP
  audio/video_10m56_with_vo_music.mp4
"""
import glob, json, pathlib, re, subprocess

FF = "/home/user/Wan2.2/.venv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v9.0.2"
BASE = pathlib.Path("/home/user/Wan2.2/projects/atlas_understory")
AUD = BASE / "audio"
MUSIC = pathlib.Path("/home/user/Wan2.2/google_drive/Ambiment - Kevin MacLeod (CC BY 4.0).mp3")
VIDEO_IN = pathlib.Path(
    "/home/user/Wan2.2/google_drive/00_v2 COMPLETE 10m56:01 - continuous plate cut (VO + edit bed).mp4")
VIDEO_IN_ALT = pathlib.Path("/home/user/Wan2.2/google_drive")
VIDEO_OUT = AUD / "video_10m56_with_vo_music.mp4"
FILM = 656.042
START = 1.2
END_TARGET = 649.0
GAP = 1.0
WORDS = 1427


def probe(p):
    out = subprocess.run([FF, "-i", str(p)], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    if not m:
        raise SystemExit(f"cannot probe {p}")
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def run(cmd, label):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2500:])
        raise SystemExit(f"{label} failed")
    print(f"{label} ok", flush=True)


def find_video() -> pathlib.Path:
    if VIDEO_IN.exists():
        return VIDEO_IN
    hits = sorted(VIDEO_IN_ALT.glob("00_v2 COMPLETE 10m56*.mp4"))
    if not hits:
        raise SystemExit("source video not found")
    return hits[0]


def main() -> None:
    files = sorted(glob.glob(str(AUD / "vo_*.mp3")))
    durs = [probe(f) for f in files]
    n = len(files)
    total = sum(durs)
    target = END_TARGET - START - GAP * (n - 1)
    k = max(1.0, total / target)
    starts, t = [], START
    for d in durs:
        starts.append(t)
        t += d / k + GAP
    end = starts[-1] + durs[-1] / k
    print(f"{n} chunks | raw {total:.1f}s | tempo x{k:.3f} | ~{WORDS/(total/60)*k:.0f} wpm | "
          f"voice {starts[0]:.1f}->{end:.1f}s of {FILM:.1f}s", flush=True)

    inputs = []
    for f in files:
        inputs += ["-i", f]
    inputs += ["-i", str(MUSIC)]

    vo_chains = []
    for i in range(n):
        ms = int(starts[i] * 1000)
        vo_chains.append(
            f"[{i}:a]atempo={k:.4f},aresample=48000,aformat=channel_layouts=stereo,"
            f"adelay={ms}|{ms},apad=whole_dur={FILM}[v{i}]")
    vo_mix = ("" .join(f"[v{i}]" for i in range(n))
              + f"amix=inputs={n}:normalize=0:dropout_transition=0")
    vo_out = f"{vo_mix},loudnorm=I=-16:TP=-2:LRA=11[vo]"
    music_chain = (f"[{n}:a]atrim=0:{FILM},asetpts=N/SR/TB,aresample=48000,"
                   f"aformat=channel_layouts=stereo,volume=0.16,"
                   f"afade=t=in:st=0:d=6,afade=t=out:st={FILM - 10}:d=10[mus]")
    duck = ("[mus][vo]sidechaincompress=threshold=0.035:ratio=7:attack=15:"
            "release=520:makeup=1[musd]")
    tail = f"apad=whole_dur={FILM},atrim=0:{FILM},asetpts=N/SR/TB[aout]"

    graph_voice = ";".join(vo_chains + [vo_out])
    graph_music = ";".join(vo_chains + [vo_out, music_chain, duck, f"[musd]{tail}"])
    graph_mix = ";".join(vo_chains + [vo_out, music_chain, duck,
                                      f"[vo][musd]amix=inputs=2:normalize=0,alimiter=limit=0.95,{tail}"])

    run([FF, "-y", "-loglevel", "error", *inputs, "-filter_complex", graph_voice,
         "-map", "[vo]", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
         str(AUD / "narration_10m56.wav")], "voice bed")
    run([FF, "-y", "-loglevel", "error", *inputs, "-filter_complex", graph_music,
         "-map", "[aout]", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
         str(AUD / "music_10m56_ducked.wav")], "music bed")
    run([FF, "-y", "-loglevel", "error", *inputs, "-filter_complex", graph_mix,
         "-map", "[aout]", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
         str(AUD / "mix_10m56.wav")], "mix")

    # two-pass loudness master: the graph loudnorm only sees the voice stream (it is
    # normalised against a padded file, so it lands ~-23 LUFS), so the finished mix gets
    # its own measured, linear loudnorm to -16 LUFS / -1.5 dBTP.
    mix = AUD / "mix_10m56.wav"
    meas = subprocess.run([FF, "-hide_banner", "-i", str(mix), "-af",
                           "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
                           "-f", "null", "-"], capture_output=True, text=True).stderr
    vals = json.loads(meas[meas.rindex("{"):meas.rindex("}") + 1])
    master = AUD / "mix_10m56_master.wav"
    run([FF, "-y", "-loglevel", "error", "-i", str(mix), "-af",
         (f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={vals['input_i']}"
          f":measured_TP={vals['input_tp']}:measured_LRA={vals['input_lra']}"
          f":measured_thresh={vals['input_thresh']}:offset={vals['target_offset']}"
          ":linear=true,aresample=48000"),
         "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(master)], "master")

    video = find_video()
    run([FF, "-y", "-loglevel", "error", "-i", str(video), "-i", str(master),
         "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "112k",
         "-ac", "2", "-af", f"apad=whole_dur={FILM},atrim=0:{FILM}",
         "-movflags", "+faststart", str(VIDEO_OUT)], "mux")
    print("VIDEO", VIDEO_OUT.name, f"{VIDEO_OUT.stat().st_size/1e6:.1f} MB", flush=True)
    json.dump({"tempo": k, "starts": starts, "durs": durs, "end": end,
               "wpm": WORDS / (total / 60) * k,
               "music": "Ambiment - Kevin MacLeod (incompetech.com), CC BY 4.0"},
              open(AUD / "vo_timeline.json", "w"), indent=1)


if __name__ == "__main__":
    main()
