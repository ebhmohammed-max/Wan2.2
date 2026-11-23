# THE DUNE ARCHIVES — Master Production Library (repo side)

This is the foundation for a faceless, cinematic YouTube documentary channel about the Dune universe. The look is ultra-realistic 3D historical reconstruction, and every claim is labelled by continuity.

**Google Drive mirror:** "THE DUNE ARCHIVES — MASTER PRODUCTION LIBRARY" (`1qPGXQPQMMAu1Jc5yAofn_BtjRcbhe4jo`).
- Repo files keep their names on Drive.
- Folder and file IDs are listed in `00_master/MASTER_INDEX_AND_TRACKER.md`.

## Layout

| Path | Contents | Drive folder |
|---|---|---|
| `00_master/` | Master index & tracker, status report, repo capability report, top-10 | 00_MASTER_PROJECT_MANAGEMENT |
| `01_lore/` | Canon & sourcing policy | 01_COMPLETE_DUNE_LORE_DATABASE |
| `02_timeline/` | Master timeline (MD/CSV) | 02_MASTER_HISTORICAL_TIMELINE |
| `03_topic_bank/` | 213 topics (CSV/JSON/MD/XLSX) | 03_TOPIC_BANK |
| `04_characters/` | Character database | 04_CHARACTER_DATABASE |
| `05_houses/` | Great Houses (16 fields) | 05_GREAT_HOUSES_AND_DYNASTIES |
| `06_factions/` | Factions | 06_FACTIONS_AND_SECRET_SOCIETIES |
| `07_planets/` | Planets & geography | 07_PLANETS_AND_GEOGRAPHY |
| `08_technology/` | Technology & artifacts | 08_TECHNOLOGY_AND_ARTIFACTS |
| `09_religion/` | Ecology, religion, philosophy | 09_RELIGIONS_AND_PHILOSOPHIES |
| `13_visual_bible/` | Visual style bible | 13_VISUAL_STYLE_BIBLE |
| `14_continuity/` | Character continuity sheets (text) | 14_CHARACTER_CONTINUITY_SHEETS |
| `15_hooks/` | Hook library (1,065) + storytelling framework | 15_STORYTELLING_AND_HOOK_LIBRARY |
| `16_youtube/` | Competitor & audience research | 16_YOUTUBE_COMPETITOR_RESEARCH |
| `17_templates/` | Script template | 17_DOCUMENTARY_SCRIPTS |
| `18_storyboards/` | Storyboard template & conventions | 18_STORYBOARDS |
| `templates/maps/` | Map-scene JSON templates | 20_MAPS_AND_ANIMATIONS |
| `25_sources/` | Sources & citations | 25_RESEARCH_SOURCES_AND_CITATIONS |
| `26_learning_log/` | Channel learning log | 26_CHANNEL_LEARNING_LOG |
| `data/` | Source-of-truth lore & topic data (Python) | — |
| `tools/` | `build_databases.py`, `motion_engine.py`, `map_animator.py` | — |

## Rebuild

```bash
python3 -m venv /home/user/.venv-dune && /home/user/.venv-dune/bin/pip install numpy pillow imageio imageio-ffmpeg openpyxl
/home/user/.venv-dune/bin/python projects/dune_archives/tools/build_databases.py
```

## Rules that matter most

The rules are in `01_lore/CANON_POLICY.md`:
- Never merge continuities.
- No actor likenesses.
- No invented quotations or numbers.
- Maps are schematic.
- At most 10 images per batch.
- No production starts without approval of topic, duration and image quantity.
