#!/usr/bin/env python3
"""Build script, storyboard and image-batch manifests for one episode from data/<ep>_episode.py.

Run:  /home/user/.venv-dune/bin/python tools/build_episode.py dun003
Outputs:
  17_scripts/<EP>_SCRIPT_v0.1.md
  18_storyboards/<EP>_STORYBOARD.csv
  19_batches/<EP>/<EP>_BATCH###.json and <EP>_BATCH_INDEX.md
Validates: unique-image count, batch size (≤10), total runtime, VO word budget.
"""
import csv
import importlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data"))

STYLE = ("ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, fine film grain, "
         "full-bleed wide 16:9 cinematic frame, no black bars, important action kept in the central band for a later 2.39:1 crop")
NEGATIVE = ("text, letters, words, watermark, logo, signature, caption, actor likeness, celebrity, film still, "
            "cartoon, anime, illustration, oversaturated, neon, cyberpunk, extra fingers, deformed hands, "
            "blurry face, gore, blood, classical columns, Roman, Greek, Gothic, medieval architecture, "
            "rose window, battlements, rotor helicopter, propellers, elf ears, pointed ears")
ARCH_WORDS = ("hall", "chamber", "palace", "citadel", "window", "throne", "courtyard", "corridor", "temple",
              "apartments", "balcony", "audience", "nursery", "keep")
ARCH_GUARD = ("Architecture: austere monolithic desert stone, massive plain slabs and abstract geometric carving; "
              "no classical columns, no arches, no Gothic, Roman or medieval elements")
CRAFT_WORDS = ("ornithopter", "thopter", "transport", "frigate", "aircraft")
CRAFT_GUARD = "Ornithopters have NO rotors: articulated dragonfly-like flapping wings"
TEXTURE = "fine film grain, subtle atmospheric haze, tactile materials"
BATCH_SIZE = 10
SHOT_NAMES = {"EW": "epic wide shot, low horizon", "EST": "establishing shot", "MS": "medium shot",
              "CU": "portrait close-up, shallow depth of field", "INS": "macro insert shot"}


def tc(sec):
    sec = int(round(sec))
    return f"00:{sec // 60:02d}:{sec % 60:02d}"


def sentences(text):
    text = " ".join(text.split())
    return [s for s in re.split(r"(?<=[.!?])\s+", text) if s]


def prompt_for(shot, anchors):
    key, kind, lens, cs, body, light, mood, motion, label, n = shot
    subject = (anchors[cs] + ", " + body) if cs else body
    low = body.lower()
    if any(w in low for w in ARCH_WORDS):
        subject += ". " + ARCH_GUARD
    if any(w in low for w in CRAFT_WORDS):
        subject += ". " + CRAFT_GUARD
    return (f"{STYLE}. {subject}. Lighting: {light}. Camera: {SHOT_NAMES[kind]}, {lens} lens. "
            f"Mood: {mood}. Texture: {TEXTURE}. Original character design, not based on any real person. "
            f"No text anywhere in the image.")


def main(ep_mod):
    ep = importlib.import_module(f"{ep_mod}_episode")
    M, CH, S, MAPS, FACTS, A, L = ep.META, ep.CHAPTERS, ep.S, ep.MAPS, ep.FACTS, ep.ANCHORS, ep.LABEL_NAMES
    EP = M["id"]

    # ---------- validation ----------
    for ch in CH:
        for shot in S[ch["id"]]:
            assert len(shot) == 10, shot[0]
            if shot[3]:
                assert shot[3] in A, f"missing anchor {shot[3]}"
    uniques = [(ch["id"], s) for ch in CH for s in S[ch["id"]]]
    keys = [s[0] for _, s in uniques]
    assert len(keys) == len(set(keys)), "duplicate shot keys"
    total = sum(ch["dur"] for ch in CH)
    assert total == M["runtime_s"], total
    words = sum(len(ch["vo"].split()) for ch in CH)

    # ---------- number scenes + batches ----------
    scene_no, img_rows = 0, []
    for ch_id, s in uniques:
        scene_no += 1
        batch = (scene_no - 1) // BATCH_SIZE + 1
        sid = f"{EP}_SCENE{scene_no:03d}"
        fname = f"{EP}_BATCH{batch:03d}_SCENE{scene_no:03d}_{s[0]}.png"
        img_rows.append(dict(ch=ch_id, shot=s, scene_id=sid, scene_no=scene_no, batch=batch, file=fname))
    n_batches = img_rows[-1]["batch"]

    # ---------- storyboard rows ----------
    header = ["shot_no", "scene_id", "chapter", "timecode_in", "duration_s", "vo_line", "canon_label",
              "visual_label", "source_ref", "shot_type", "lens", "subject_continuity_id", "description", "light",
              "mood", "motion_recipe", "image_file", "unique_or_reuse", "reuse_of", "map_scene_json", "batch",
              "onscreen_text", "qc_status"]
    rows, t, shot_no = [], 0.0, 0
    by_ch = {}
    for r in img_rows:
        by_ch.setdefault(r["ch"], []).append(r)
    for ch in CH:
        seq = []
        for r in by_ch[ch["id"]]:
            seq.append(("U", r))
            if r["shot"][9] == 2:
                seq.append(("R", r))
        for (mch, after, mjson, cue, lab) in MAPS:
            if mch == ch["id"]:
                # insert after the (after)-th unique shot of the chapter
                idx, count = 0, -1
                for i, (k, _) in enumerate(seq):
                    if k == "U":
                        count += 1
                    if count == after:
                        idx = i + 1
                        if i + 1 < len(seq) and seq[i + 1][0] == "R":
                            idx = i + 2
                        break
                seq.insert(idx, ("M", (mjson, cue, lab)))
        dur_each = ch["dur"] / len(seq)
        sents = sentences(ch["vo"])
        wcum, wtot = [], sum(len(x.split()) for x in sents)
        acc = 0
        for x in sents:
            wcum.append((acc + len(x.split()) / 2) / wtot)
            acc += len(x.split())
        vo_by_shot = [[] for _ in seq]
        for x, mid in zip(sents, wcum):
            vo_by_shot[min(int(mid * len(seq)), len(seq) - 1)].append(x)
        for i, (kind, payload) in enumerate(seq):
            shot_no += 1
            vo = " ".join(vo_by_shot[i]) or "(VO continues / music breath)"
            onscreen = ""
            if ch["id"] == "01":
                onscreen = "ARCHIVE CARD (edit overlay)"
            if kind == "M":
                mjson, cue, lab = payload
                rows.append([shot_no, f"{EP}_MAP_{mjson.split('_MAP_')[1][0]}", ch["title"], tc(t),
                             round(dur_each, 1), vo, L[lab], "CREATIVE RECONSTRUCTION (schematic)", ch["src"],
                             "OH", "map", "", cue, "", "", "MAP", "", "MAP", "", mjson, "", "labels in edit",
                             "TO AUTHOR"])
            else:
                r = payload
                key, kind2, lens, cs, body, light, mood, motion, label, n = r["shot"]
                if kind == "R":
                    reuse_motion = {"PUSH_IN": "PULL_OUT", "PULL_OUT": "PUSH_IN", "DRIFT": "PUSH_IN",
                                    "PAN_LR": "PAN_RL", "PAN_RL": "PAN_LR"}.get(motion, "DRIFT")
                    rows.append([shot_no, r["scene_id"] + "R", ch["title"], tc(t), round(dur_each, 1), vo,
                                 L[label], "CREATIVE RECONSTRUCTION", ch["src"], "CROP", lens, cs,
                                 "reframe/crop of " + key, light, mood, reuse_motion, r["file"], "REUSE",
                                 r["scene_id"], "", r["batch"], onscreen, "PENDING"])
                else:
                    rows.append([shot_no, r["scene_id"], ch["title"], tc(t), round(dur_each, 1), vo, L[label],
                                 "CREATIVE RECONSTRUCTION", ch["src"], kind2, lens, cs, body, light, mood, motion,
                                 r["file"], "UNIQUE", "", "", r["batch"], onscreen, "PENDING"])
            t += dur_each
    sb = ROOT / f"18_storyboards/{EP}_STORYBOARD.csv"
    sb.parent.mkdir(parents=True, exist_ok=True)
    with sb.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

    # ---------- batch manifests ----------
    bdir = ROOT / f"19_batches/{EP}"
    bdir.mkdir(parents=True, exist_ok=True)
    idx_lines = [f"# {EP} — Image batch index", "",
                 f"Approved: **{M['images']}**. Max {BATCH_SIZE} images per batch. "
                 "Images are CREATIVE RECONSTRUCTIONS, not official artwork, and depict no actor.", "",
                 "| Batch | Scenes | Chapters | Status |", "|---|---|---|---|"]
    for b in range(1, n_batches + 1):
        items = [r for r in img_rows if r["batch"] == b]
        assert len(items) <= BATCH_SIZE
        man = {"episode": EP, "batch": f"BATCH{b:03d}", "max_batch_size": BATCH_SIZE, "status": "PENDING",
               "style": STYLE, "negative": NEGATIVE, "images": []}
        for r in items:
            key, kind2, lens, cs, body, light, mood, motion, label, n = r["shot"]
            man["images"].append({
                "scene_id": r["scene_id"], "file": r["file"], "chapter": r["ch"], "shot_type": kind2, "lens": lens,
                "continuity_id": cs, "canon_label_of_event": L[label], "visual_label": "CREATIVE RECONSTRUCTION",
                "motion_recipe": motion, "onscreen_uses": n, "prompt": prompt_for(r["shot"], A),
                "negative": NEGATIVE, "generator": None, "seed": None, "drive_file_id": None,
                "qc": "PENDING"})
        (bdir / f"{EP}_BATCH{b:03d}.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), "utf-8")
        chs = sorted({r["ch"] for r in items})
        idx_lines.append(f"| BATCH{b:03d} | {items[0]['scene_no']:03d}–{items[-1]['scene_no']:03d} | "
                         f"{', '.join(chs)} | PENDING |")
    (bdir / f"{EP}_BATCH_INDEX.md").write_text("\n".join(idx_lines) + "\n", "utf-8")

    # ---------- script ----------
    out = [f"# {EP} — {M['title']} — SCRIPT {M.get('script_version', 'v0.1')}", "",
           "| Field | Value |", "|---|---|",
           f"| Topic ID / tier | {EP} · {M['tier']} |",
           f"| Target runtime | {total // 60}:{total % 60:02d} (≈ {M['wpm']} wpm → budget {total // 60 * M['wpm']} words; "
           f"draft = {words} words) |",
           f"| Spoiler level | {M['spoilers']} |", f"| Continuity scope | {M['scope']} |",
           f"| Approved hooks | {M['hooks']} |", f"| Image budget (approved) | {M['images']} |",
           f"| Publish target | {M['publish_target']} |", f"| Status | {M['status']} |", "",
           "**Quote policy:** this draft contains NO direct quotations from the novels or from Frank Herbert. "
           "Everything is paraphrase. `[VERIFY]` items need a page check against a physical edition before LOCK.",
           "", "---", ""]
    t = 0
    for ch in CH:
        scenes = [r for r in img_rows if r["ch"] == ch["id"]]
        out.append(f"## {ch['id']}. {ch['title']} ({tc(t)[3:]}–{tc(t + ch['dur'])[3:]}, {ch['dur']} s, "
                   f"{len(ch['vo'].split())} words)")
        out.append(f"`[VISUALS: {scenes[0]['scene_id']}–{scenes[-1]['scene_id'][-3:]} · "
                   f"{len(scenes)} unique stills · BATCH {scenes[0]['batch']:03d}"
                   f"{'' if scenes[0]['batch'] == scenes[-1]['batch'] else '–%03d' % scenes[-1]['batch']}]`  ")
        out.append(f"`[SOURCE: {ch['src']}]`")
        for mch, after, mjson, cue, lab in MAPS:
            if mch == ch["id"]:
                out.append(f"`[MAP: {mjson} — {cue} — {L[lab]}]`")
        out.append("")
        for para in [p.strip() for p in ch["vo"].strip().split("\n\n")]:
            out.append("VO: " + " ".join(para.split()))
            out.append("")
        tag = {"10": "`[CANON TAGS: book points = ORIGINAL FRANK HERBERT CANON · Part Two points = FILM ADAPTATION · "
                     "Part Three expectations = ADAPTATION-SPECIFIC INTERPRETATION / reporting, re-check before publish]`",
               "11": "`[CANON TAGS: Herbert intent = paraphrase of 'Dune Genesis' (1980) [VERIFY] · teases = "
                     "ORIGINAL FRANK HERBERT CANON (Children of Dune, God Emperor of Dune)]`"}.get(
            ch["id"], "`[CANON TAG: ORIGINAL FRANK HERBERT CANON — visuals are CREATIVE RECONSTRUCTION]`")
        out.append(tag)
        out.append("")
        t += ch["dur"]
    out += ["END CARD: \"Visual reconstructions are original artistic interpretations, not official artwork, "
            "and do not depict any actor. Dune is the creation of Frank Herbert.\"", "", "---",
            "### Fact-check log", "| # | Claim | Label | Source to verify | Status |", "|---|---|---|---|---|"]
    for i, (c, lab, src) in enumerate(FACTS, 1):
        out.append(f"| {i} | {c} | {L[lab]} | {src} | VERIFY |")
    out += ["", "### Change log", "| Version | Date | Change | By |", "|---|---|---|---|",
            "| v0.1 | 2026-11-23 | First draft from approved topic, runtime and image budget | THE DUNE ARCHIVES agent |",
            "| v1.0 | 2026-11-23 | Approved as-is by the creative director (text locked; VERIFY page checks pending) | Creative director |"]
    sp = ROOT / f"17_scripts/{EP}_SCRIPT_{M.get('script_version', 'v0.1')}.md"
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text("\n".join(out) + "\n", "utf-8")

    n_unique = sum(1 for r in rows if r[17] == "UNIQUE")
    n_reuse = sum(1 for r in rows if r[17] == "REUSE")
    n_map = sum(1 for r in rows if r[17] == "MAP")
    summary = dict(episode=EP, runtime_s=total, vo_words=words, vo_minutes_at_wpm=round(words / M["wpm"], 2),
                   unique_stills=n_unique, reuse_shots=n_reuse, map_shots=n_map, onscreen_shots=len(rows),
                   batches=n_batches, avg_shot_s=round(total / len(rows), 2))
    print(json.dumps(summary, indent=1))
    return summary


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "dun003")
