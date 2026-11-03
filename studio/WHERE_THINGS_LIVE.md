# Where things live

**Rule, standing order:** every artifact I create for this work — docs, keyframes, previz, prompts,
renders, decks — is saved to the Drive folder **"Wan 2.2"**, and committed to this repo when it's
code or text. Drive is the deliverable surface; the repo is the source of truth.

**Drive root:** [`Wan 2.2`](https://drive.google.com/drive/folders/1g3RBP2siBPUFmIF1B3P5YZtU2CrCOghB)
(id `1g3RBP2siBPUFmIF1B3P5YZtU2CrCOghB`, owned by Eshan Mohammed)

```
Wan 2.2/
├── START HERE — Project Index            Google Doc: idea, structure, rules, status
├── 00 — Creative Direction (2WULFFS method)
│   ├── 2wulffs-playbook.md               the method as our operating standard
│   ├── CREATIVE_BIBLE.md                 insight → idea → visual rule → execution
│   ├── COVERAGE_SHOTS.md                 8-bucket coverage plan, shot cards 03–08
│   ├── BASE_LOOK.txt                     locked look, appended to every prompt
│   ├── shot01_prompt_v2.txt
│   └── shot02_prompt_v2.txt
└── Cappadocia Underground City
    ├── Shot 01 — The City Below          previz, keyframes/, scripts/, prompts
    ├── Shot 02 — The Lantern             previz, keyframes/ (incl. cast sheet), scripts/, prompts
    └── Takes & Finals                    final graded 9:16 masters + assembled cut
```

Known folder ids (use these instead of re-creating anything):

| Folder | id |
|---|---|
| `Wan 2.2` (root) | `1g3RBP2siBPUFmIF1B3P5YZtU2CrCOghB` |
| `00 — Creative Direction (2WULFFS method)` | `12Oc84GVpjMOVsnt32GPzyHLGrWbTUs8Q` |
| `Cappadocia Underground City` | `1Zv_SPdbwy_tBt5lEiFCfMgXBXTLGe91x` |
| `Shot 01 — The City Below` | `1ajxivl_eIFzUVXhP3GqU7pDlTzrdBlWq` |
| `Shot 02 — The Lantern` | `1h9uvhEDqLfhE8QN8-C6rzdNrUS5UBXRH` |
| `Takes & Finals` | `1TPzVFRnaUoa1yJqRo5aue39ssM14xK2d` |

## Repo ↔ Drive mapping

| Repo path | Drive location |
|---|---|
| `studio/2wulffs-playbook.md` | `00 — Creative Direction` (same name) |
| `studio/START_HERE_index.md` | `Wan 2.2 / START HERE — Project Index` (as a Google Doc) |
| `projects/cappadocia_underground_city/CREATIVE_BIBLE.md`, `COVERAGE_SHOTS.md`, `BASE_LOOK.txt`, `prompt_v2.txt` | `00 — Creative Direction` |
| `projects/.../keyframes/`, `previz/*.mp4`, `prompt*.txt`, `scripts/*.sh`, `README.md` | the matching `Shot 0X` folder, mirrored (`keyframes/` and `scripts/` as subfolders) |
| `projects/.../out/*` (takes) | uploaded only when a take is worth keeping → `Takes & Finals` |

## Housekeeping conventions

* **Never commit third-party reference material.** Downloaded PDFs go to `/home/user/refs/`, which is
  gitignored (`refs/`, `google_drive/`).
* **Drive folders are moved, not duplicated**, when structure changes — links stay valid.
* **Naming:** `Shot 0X — <title>` for shots, `NN — <title>` for numbered top-level docs, files keep
  their repo names so a file on Drive can be traced to a path in git.
* `.sh` files uploaded to Drive lose their executable bit; re-`chmod +x` after downloading.
