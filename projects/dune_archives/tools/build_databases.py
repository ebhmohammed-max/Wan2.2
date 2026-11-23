#!/usr/bin/env python3
"""Generate every THE DUNE ARCHIVES research database from projects/dune_archives/data/*.py.

Outputs (Markdown for Docs, CSV for Sheets, JSON for tooling, XLSX for the topic bank):
  02_timeline/MASTER_TIMELINE.{md,csv}
  03_topic_bank/TOPIC_BANK.{md,csv,json,xlsx}
  04_characters/CHARACTER_DATABASE.{md,csv}
  05_houses/GREAT_HOUSES.{md,csv}
  06_factions/FACTIONS.{md,csv}
  07_planets/PLANETS_AND_GEOGRAPHY.{md,csv}
  08_technology/TECHNOLOGY_AND_ARTIFACTS.{md,csv}
  09_religion/ECOLOGY_RELIGION_PHILOSOPHY.{md,csv}
  15_hooks/HOOK_LIBRARY.{md,csv}
Run:  /home/user/.venv-dune/bin/python tools/build_databases.py
"""
import csv
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data"))

from lore_timeline import TIMELINE  # noqa: E402
from lore_characters import C as CHARACTERS  # noqa: E402
from lore_houses_factions import HOUSES, HOUSE_FIELDS, FACTIONS  # noqa: E402
from lore_world import PLANETS, TECH, ECO_RELIGION  # noqa: E402
from topics_a import TOPICS_A  # noqa: E402
from topics_b import TOPICS_B  # noqa: E402
from topics_c import TOPICS_C  # noqa: E402
from topics_d import TOPICS_D  # noqa: E402

VERSION = "v1.0 — 2026-11-23"
LABELS = {"O": "ORIGINAL FRANK HERBERT CANON", "E": "EXPANDED DUNE UNIVERSE", "F": "FILM ADAPTATION",
          "T": "TELEVISION ADAPTATION", "S": "SHARED OR OVERLAPPING CONTINUITY",
          "A": "ADAPTATION-SPECIFIC INTERPRETATION", "X": "FAN THEORY", "R": "CREATIVE RECONSTRUCTION"}
TIERS = {"M": ("MINI", "3–8 min", 6), "S": ("STANDARD", "10–20 min", 14), "E": ("EPIC", "40–75 min", 50)}
CRIT = ["curiosity", "search_demand", "evergreen", "visual_potential", "canon_defensibility",
        "emotional_stakes", "competitive_gap", "production_feasibility"]
CATS = {"HIST": "History & Events", "CHAR": "Character Biography", "HOUSE": "Great Houses & Dynasties",
        "FACT": "Factions & Secret Societies", "PLAN": "Planets & Geography", "TECH": "Technology & Artifacts",
        "ECO": "Ecology & Creatures", "REL": "Religion & Philosophy", "ADAPT": "Adaptations Compared",
        "MYTH": "Myths & Canon Disputes", "WHATIF": "What-If (Fan Theory)", "TIMELY": "Timely / Release Tie-in",
        "MAKING": "Real-World Making-of", "BATTLE": "Battles & Warfare"}


def out(rel):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def write_csv(rel, header, rows):
    with out(rel).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def md_escape(s):
    return str(s).replace("|", "/").replace("\n", " ")


def md_table(header, rows):
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(md_escape(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


HEADER_NOTE = ("> **Continuity labels are mandatory.** ORIGINAL FRANK HERBERT CANON · EXPANDED DUNE UNIVERSE · FILM ADAPTATION · "
               "TELEVISION ADAPTATION · SHARED OR OVERLAPPING CONTINUITY · ADAPTATION-SPECIFIC INTERPRETATION · FAN THEORY · "
               "CREATIVE RECONSTRUCTION. Never merge continuities. `[VERIFY]` = check against the printed text before scripting.\n")


# ------------------------------------------------------------------ timeline --
def build_timeline():
    rows = sorted(TIMELINE, key=lambda r: r[0])
    hdr = ["date", "event", "continuity_label", "source", "confidence", "documentary_notes"]
    data = [r[1:] for r in rows]
    write_csv("02_timeline/MASTER_TIMELINE.csv", hdr, data)
    inuni = [r for r in data if not rows[data.index(r)][0] >= 90000]
    real = [r for r in data if rows[data.index(r)][0] >= 90000]
    md = [f"# THE DUNE ARCHIVES — Master Historical Timeline ({VERSION})\n", HEADER_NOTE,
          "Calendar: **BG** = Before Guild, **AG** = After Guild. Gregorian conversions (e.g. '1 AG ≈ 13360 AD') are "
          "**FAN THEORY / CREATIVE RECONSTRUCTION** and must never appear on screen as fact.\n",
          "Confidence: **HIGH** = well attested; **MEDIUM** = attested, exact wording/figure to verify; **LOW** = secondary sources disagree.\n",
          f"## A. In-universe chronology ({len(inuni)} entries)\n", md_table(hdr, inuni),
          f"\n\n## B. Real-world publication & adaptation chronology ({len(real)} entries)\n", md_table(hdr, real),
          "\n\n## Known date disputes\n",
          "- **Butlerian Jihad 201–108 BG** — dates from Herbert's glossary; narrative of the war differs across Herbert / Dune Encyclopedia / Legends of Dune.\n"
          "- **Harkonnen stewardship start (10111 AG)** — secondary/EU; the novel gives an approximate span only.\n"
          "- **Messiah dating (10205 vs 10207 AG)** — sources compute differently from '12 years of jihad'. Use 'twelve years after Paul's ascension' on screen.\n"
          "- **Leto II's death (~13725 AG)** — computed from a ~3,500-year reign; avoid a precise year on screen unless verified.\n"
          "- **Heretics/Chapterhouse AG years** — from secondary timelines; anchor on screen as '~1,500 years after Leto II'.\n"
          "- **Dune: Prophecy** — show-specific chronology; never align it to Sisterhood of Dune dates without a label.\n"]
    out("02_timeline/MASTER_TIMELINE.md").write_text("\n".join(md), encoding="utf-8")
    return len(rows)


# ---------------------------------------------------------------- characters --
def build_characters():
    keys = list(CHARACTERS[0].keys())
    write_csv("04_characters/CHARACTER_DATABASE.csv", keys, [[c[k] for k in keys] for c in CHARACTERS])
    md = [f"# THE DUNE ARCHIVES — Character Database ({VERSION})\n", HEADER_NOTE,
          "**Likeness rule:** visual briefs describe ORIGINAL channel designs. Never base a face, build or costume on any actor "
          "who has portrayed the role, and never describe generated art as official.\n",
          f"**{len(CHARACTERS)} characters.** Summary table first, full records below.\n",
          md_table(["ID", "Name", "Era", "Origin label", "Doc potential"],
                   [[c["id"], c["name"], c["era"], c["origin_label"], c["doc_potential"]] for c in CHARACTERS]), "\n"]
    for c in CHARACTERS:
        md.append(f"\n## {c['id']} — {c['name']}\n")
        for k in keys[2:]:
            if c[k] != "":
                md.append(f"- **{k.replace('_', ' ').title()}:** {c[k]}")
    out("04_characters/CHARACTER_DATABASE.md").write_text("\n".join(md), encoding="utf-8")
    return len(CHARACTERS)


# -------------------------------------------------------- houses & factions --
def build_houses_factions():
    write_csv("05_houses/GREAT_HOUSES.csv", HOUSE_FIELDS, [[h[k] for k in HOUSE_FIELDS] for h in HOUSES])
    md = [f"# THE DUNE ARCHIVES — Great Houses & Dynasties ({VERSION})\n", HEADER_NOTE,
          f"Each House is documented across **16 fields**: {', '.join(HOUSE_FIELDS)}.\n",
          "Heraldry & colours marked `[VERIFY]` or `RECON` must be confirmed or labelled before use in a visual.\n"]
    for h in HOUSES:
        md.append(f"\n## {h['name']}\n")
        for i, k in enumerate(HOUSE_FIELDS, 1):
            md.append(f"{i}. **{k.replace('_', ' ').title()}:** {h[k]}")
    out("05_houses/GREAT_HOUSES.md").write_text("\n".join(md), encoding="utf-8")
    fh = ["faction", "continuity_label", "summary", "base", "visual_cues", "documentary_notes"]
    write_csv("06_factions/FACTIONS.csv", fh, FACTIONS)
    out("06_factions/FACTIONS.md").write_text(
        f"# THE DUNE ARCHIVES — Factions & Secret Societies ({VERSION})\n\n{HEADER_NOTE}\n{md_table(fh, FACTIONS)}\n", encoding="utf-8")
    return len(HOUSES), len(FACTIONS)


# ------------------------------------------------------------------- world --
def build_world():
    ph = ["planet", "continuity_label", "type_climate", "established_facts", "reconstruction_latitude", "visual_brief", "doc_potential"]
    write_csv("07_planets/PLANETS_AND_GEOGRAPHY.csv", ph, PLANETS)
    out("07_planets/PLANETS_AND_GEOGRAPHY.md").write_text(
        f"# THE DUNE ARCHIVES — Planets & Geography ({VERSION})\n\n{HEADER_NOTE}\n"
        "**Geography rule:** Herbert published an *Arrakis* polar map in the Dune appendix, but **no interstellar coordinates**. "
        "All galaxy-scale maps are CREATIVE RECONSTRUCTION and carry the on-screen caption *'Schematic reconstruction — relative "
        "positions are artistic'* (enforced by `tools/map_animator.py`). Never invent precise coordinates, distances, or planetary "
        "statistics.\n\n" + md_table(ph, PLANETS) + "\n", encoding="utf-8")
    th = ["technology", "continuity_label", "description", "rules_limits", "visual_brief"]
    write_csv("08_technology/TECHNOLOGY_AND_ARTIFACTS.csv", th, TECH)
    out("08_technology/TECHNOLOGY_AND_ARTIFACTS.md").write_text(
        f"# THE DUNE ARCHIVES — Technology & Artifacts ({VERSION})\n\n{HEADER_NOTE}\n"
        "Design rule: all hardware is redesigned from text descriptions. Do **not** reproduce film designs (e.g. 2021 dragonfly "
        "ornithopters, 1984 weirding modules).\n\n" + md_table(th, TECH) + "\n", encoding="utf-8")
    eh = ["topic", "continuity_label", "summary", "documentary_angle"]
    write_csv("09_religion/ECOLOGY_RELIGION_PHILOSOPHY.csv", eh, ECO_RELIGION)
    out("09_religion/ECOLOGY_RELIGION_PHILOSOPHY.md").write_text(
        f"# THE DUNE ARCHIVES — Ecology, Religion & Philosophy ({VERSION})\n\n{HEADER_NOTE}\n"
        "Quotation rule: only two verbatim lines are cleared for use without re-checking (the Litany's opening and the Butlerian "
        "commandment) — and even these must be matched to a specific edition in 25_RESEARCH_SOURCES before the voice-over is "
        "recorded. Never paraphrase inside quotation marks.\n\n" + md_table(eh, ECO_RELIGION) + "\n", encoding="utf-8")
    return len(PLANETS), len(TECH), len(ECO_RELIGION)


# --------------------------------------------------------------- topic bank --
def parse_topics():
    raw = (TOPICS_A + TOPICS_B + TOPICS_C + TOPICS_D).strip().splitlines()
    topics = []
    for i, line in enumerate([l for l in raw if l.strip()], 1):
        title, cat, era, labs, tier, q, tw, vis, st, sc = line.split("|")
        scores = [10 if ch == "X" else int(ch) for ch in sc]
        tname, trange, tmin = TIERS[tier]
        timely = (cat == "TIMELY" or any(k in title for k in ("Messiah", "Part Three", "Prophecy", "Hayt", "Irulan"))
                  or any(k in era for k in ("10205", "10,000 yrs before Paul", "c. 83 BG")))
        topics.append(dict(
            id=f"DUN{i:03d}", title=title, category=CATS[cat], era=era,
            continuity=" + ".join(LABELS[c] for c in labs.split("+")), tier=tname, duration_range=trange,
            est_minutes=tmin, core_question=q, key_revelation=tw, opening_visual=vis, stakes=st,
            **dict(zip(CRIT, scores)), total_score=sum(scores), timely_2026=("YES" if timely else ""),
            est_unique_images=f"{tmin * 5}–{tmin * 8}", est_onscreen_shots=f"{tmin * 10}–{tmin * 15}",
            canon_risk=("HIGH — multiple continuities" if len(labs.split("+")) > 2 else
                        "MEDIUM — label every claim" if "+" in labs or labs in ("X", "A") else "LOW"),
            status="PROPOSED"))
    return topics


def hooks_for(t):
    short = t["title"].split(":")[0]
    labs = t["continuity"].split(" + ")
    cont = ("The records disagree. In this file we separate " + ", ".join(l.title() for l in labs) +
            " — and we'll tell you which is which.") if len(labs) > 1 else (
        f"Source: {labs[0].title()}. Where the record goes silent, we reconstruct — and we will say so on screen.")
    return [
        ("H1", "Question", t["core_question"]),
        ("H2", "Revelation", t["key_revelation"]),
        ("H3", "Cold open (visual + VO)", f"[OPEN ON: {t['opening_visual']}] VO: \"{t['core_question']}\""),
        ("H4", "Stakes (use as re-hook at ~25%)", t["stakes"]),
        ("H5", "Archive signature / continuity", f"THE DUNE ARCHIVES. Era: {t['era']}. Subject: {short}. {cont}"),
    ]


def build_topic_bank():
    topics = parse_topics()
    keys = list(topics[0].keys())
    write_csv("03_topic_bank/TOPIC_BANK.csv", keys, [[t[k] for k in keys] for t in topics])
    out("03_topic_bank/TOPIC_BANK.json").write_text(json.dumps(topics, indent=1, ensure_ascii=False), encoding="utf-8")
    by_tier = {n: [t for t in topics if t["tier"] == n] for n in ("MINI", "STANDARD", "EPIC")}
    md = [f"# THE DUNE ARCHIVES — Topic Bank ({VERSION})\n",
          f"**{len(topics)} topics** — MINI {len(by_tier['MINI'])} · STANDARD {len(by_tier['STANDARD'])} · EPIC {len(by_tier['EPIC'])}.\n",
          "Scores are **editorial estimates (1–10)**, not analytics — no YouTube Analytics or keyword-volume tool is connected. "
          "`search_demand` reflects observed competitor coverage and release timing, not measured volume.\n",
          "Criteria: " + ", ".join(CRIT) + ". Total out of 80. `timely_2026` = tie-in with *Dune: Part Three* (18 Dec 2026) or *Dune: Prophecy* S2.\n",
          "Image estimates use 5–8 unique stills per minute and 10–15 on-screen shots per minute (each still yields 1–3 shots via motion "
          "recipes / reframes). These are planning numbers only; the image quantity is approved per episode.\n"]
    cols = ["id", "title", "category", "continuity", "est_minutes", "total_score", "timely_2026"]
    for n, lst in by_tier.items():
        lst = sorted(lst, key=lambda t: -t["total_score"])
        md += [f"\n## {n} ({TIERS[{'MINI': 'M', 'STANDARD': 'S', 'EPIC': 'E'}[n]][1]}) — {len(lst)} topics, sorted by score\n",
               md_table(cols, [[t[c] for c in cols] for t in lst])]
    out("03_topic_bank/TOPIC_BANK.md").write_text("\n".join(md), encoding="utf-8")
    # XLSX
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill
        from openpyxl.utils import get_column_letter
        wb = Workbook()
        ws = wb.active
        ws.title = "ALL_TOPICS"
        for name, lst in [("ALL_TOPICS", topics)] + [(n, by_tier[n]) for n in by_tier]:
            sh = ws if name == "ALL_TOPICS" else wb.create_sheet(name)
            sh.append(keys)
            for t in sorted(lst, key=lambda t: -t["total_score"]):
                sh.append([t[k] for k in keys])
            for c in sh[1]:
                c.font = Font(bold=True, color="FFFFFF")
                c.fill = PatternFill("solid", fgColor="8A5A1F")
            sh.freeze_panes = "C2"
            for i, k in enumerate(keys, 1):
                sh.column_dimensions[get_column_letter(i)].width = 48 if k in ("title", "core_question", "key_revelation", "opening_visual", "stakes") else 14
        wb.save(out("03_topic_bank/TOPIC_BANK.xlsx"))
    except ImportError:
        print("openpyxl missing — XLSX skipped")
    # Hooks
    hrows = []
    for t in topics:
        for hid, kind, text in hooks_for(t):
            hrows.append([t["id"], t["title"], hid, kind, text])
    write_csv("15_hooks/HOOK_LIBRARY.csv", ["topic_id", "topic_title", "hook_id", "hook_type", "hook_text"], hrows)
    md = [f"# THE DUNE ARCHIVES — Hook Library ({VERSION})\n",
          f"**{len(hrows)} hooks** — 5 per topic × {len(topics)} topics. Every hook is drawn from that topic's own question, revelation, "
          "opening image and stakes. Hooks are **drafts**: each must pass the Hook QC in `15_hooks/STORYTELLING_FRAMEWORK.md` "
          "(true to canon label, no false promise, no copied competitor phrasing) before use.\n"]
    for t in topics:
        md.append(f"\n### {t['id']} — {t['title']}  \n*{t['tier']} · {t['continuity']}*\n")
        for hid, kind, text in hooks_for(t):
            md.append(f"- **{hid} {kind}:** {text}")
    out("15_hooks/HOOK_LIBRARY.md").write_text("\n".join(md), encoding="utf-8")
    return topics, len(hrows)


if __name__ == "__main__":
    n_tl = build_timeline()
    n_ch = build_characters()
    n_h, n_f = build_houses_factions()
    n_p, n_t, n_e = build_world()
    topics, n_hooks = build_topic_bank()
    summary = dict(timeline=n_tl, characters=n_ch, houses=n_h, factions=n_f, planets=n_p, tech=n_t,
                   eco_religion=n_e, topics=len(topics), hooks=n_hooks,
                   tiers={k: sum(1 for t in topics if t["tier"] == k) for k in ("MINI", "STANDARD", "EPIC")})
    out("00_master/build_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))
    top = sorted(topics, key=lambda t: (-t["total_score"], t["id"]))[:25]
    for t in top:
        print(t["id"], t["total_score"], t["tier"], t["timely_2026"], t["title"])
