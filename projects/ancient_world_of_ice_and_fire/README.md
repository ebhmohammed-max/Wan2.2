# THE ANCIENT WORLD OF ICE AND FIRE — PRODUCTION REPOSITORY
**Genre:** Long-Form 65mm Live-Action / Physically Realistic 3D Historical Cinema Documentary Series  
**Universe:** George R. R. Martin's *A Song of Ice and Fire* (Book Canon Priority)  
**Starting Era:** Pre-Valyrian Antiquity & The Rise of Old Valyria (ca. 5,000+ BC)  
**Master Google Drive Archive:** `Game of thrones YT` (`1ymYd6xYO3MyJ-IXaYyo2YrBclUGYzJGo`)

---

## 1. MANDATORY VISUAL PRODUCTION CADENCE (`30 IMAGES / MINUTE`)

- **Image Rate:** **30 images per minute** of finished narration (**1 image every 2.0 seconds**).
- **Minimum Episode Duration:** **30 minutes** (Preferred: **30–40 minutes**).
- **Batch Size:** **Exactly 10 images per production batch** (**20.0 seconds** of narration per batch · **3 batches per minute**).
- **Scene Identifier Format:** 4-digit zero-padded IDs (`VAL-EP001-IMG0001` through `VAL-EP001-IMG1050`).

| Episode Duration | Total Seconds | Total Images (`30 / min`) | Production Batches (`10 / batch`) |
| :--- | :--- | :--- | :--- |
| **30 minutes** | 1,800 s | **900 images** | **90 batches** |
| **35 minutes** *(Episode 001)* | 2,100 s | **1,050 images** | **105 batches** |
| **40 minutes** | 2,400 s | **1,200 images** | **120 batches** |
| **45 minutes** | 2,700 s | **1,350 images** | **135 batches** |

---

## 2. LOCKED CINEMATIC VISUAL STANDARD (65MM LIVE-ACTION HISTORICAL RECONSTRUCTION)

Calibrated directly to the flagship *The Trojan War: The Legend, the City and the Evidence* production benchmark:
- **Camera & Optics:** Adult cinematic physically realistic 3D historical reconstruction and live-action **ARRI Alexa 65 / 65mm large-format location photography** with **Panavision Primo / Cooke Panchro spherical cinema prime lenses** (`24mm`, `28mm`, `35mm`, `40mm`, `50mm`, `85mm`). Honest architectural and geological verticals, level optical horizons, natural depth of field, and fine organic 35mm/65mm photochemical grain.
- **Signature Color Grade (`Kodak Vision3 500T 5219`):**
  - **Highlights:** Warm sandstone, pale ochre, and low-angle raking golden-hour or morning sunlight (`3200K–4300K`) with smooth theatrical roll-off.
  - **Midtones:** Subdued, archaeological earth pigments—raw undyed linen, weathered limestone and mud-brick, dry tawny grass, dusty Mediterranean wild olive, oxidized dark olive-brown bronze, and soot-darkened columnar basalt.
  - **Shadows:** Deep, rich **ink-navy and cool slate shadows** preserving physical surface texture.
- **Grounded Physical Framing:** Every frame is anchored to a real tripod, rocky headland, ship rail, tabletop surface, or high mountain-ridge vantage with tactile foreground geology/materials and authentic atmospheric distance haze—never miniature floating island dioramas or rigid video-game symmetry.
- **Strict Anti-CGI Guardrails:** Zero floating particle/ember swarms, zero neon cartoon lava rivers, zero tropical cyan water, zero purple/magenta fantasy skies, zero glossy plastic skin/armor, and zero baked-in text, subtitles, or watermarks.

---

## 3. REPOSITORY & GOOGLE DRIVE ARCHITECTURE

```text
projects/ancient_world_of_ice_and_fire/
├── README.md                                        # Series Overview, 30-Img/Min Rules & 65mm Visual Spec
├── database/                                        # Section 15: Persistent Continuity Database (A–H)
│   ├── A_MASTER_TIMELINE.md                         # Master chronological canon timeline
│   ├── B_CHARACTER_DATABASE.md                      # Permanent Character Identity Sheets (22 fields)
│   ├── C_FAMILY_DATABASE.md                         # Dynasties, Houses, and Succession Records
│   ├── D_LOCATION_DATABASE.md                       # Environment & Architectural Profiles (11 fields)
│   ├── E_DRAGON_DATABASE.md                         # Dragon & Creature Profiles (13 fields, 4-limb canon)
│   ├── F_EPISODE_DATABASE.json                      # Episode production status registry
│   ├── G_VISUAL_ASSET_DATABASE.json                 # Approved reference plates, MD5s & Drive IDs
│   └── H_UNRESOLVED_LORE_DATABASE.md                # Disputed accounts, maester debates & GRRM mysteries
└── episodes/
    └── ep001_rise_of_old_valyria/
        ├── EP001_MASTER_PRODUCTION_PACKAGE.md       # Unified Parts 1–8 Master Deliverable
        ├── EP001_Verified_Drive_Inventory.json      # Checksum-verified Google Drive asset inventory
        ├── 00_PRIVATE_RESEARCH_AND_SOURCES.md       # Claim-by-claim canon verification & citations
        ├── 01_EPISODE_BLUEPRINT.md                  # Part 1: Episode Blueprint (35:00 · 1,050 Images · 105 Batches)
        ├── 02_COMPLETE_NARRATION_SCRIPT.md          # Part 2: Complete 35:00 Narration Script (4,580 spoken words)
        ├── 02_SPOKEN_NARRATION_ONLY.txt             # Pure spoken VO text (word-count verified)
        ├── 03_SCENE_BREAKDOWN_1050_SCENES.md        # Part 3: Complete 1,050-scene (2s/cut) chronological plan
        ├── 03_SCENE_BREAKDOWN_1050_SCENES.json      # Machine-readable 1,050-scene timestamp & VO sync table
        ├── 03_SCENE_BREAKDOWN_1050_SCENES.csv       # Spreadsheet-ready 1,050-shot timed edit map
        ├── 04_CHARACTER_BIBLE.md                    # Part 4: Episode 001 Character Bible
        ├── 05_LOCATION_AND_DRAGON_BIBLE.md          # Part 5: Episode 001 Location & Dragon Bible
        ├── 06_IMAGE_PROMPTS_BATCH_001.md            # Part 6: Upgraded 65mm Prompts (VAL-EP001-IMG0001–IMG0010)
        ├── 06_BATCH_001_MANIFEST.json               # Machine-readable JSON manifest for Batch 001
        ├── 06_IMAGE_PROMPTS_BATCH_002.md            # Part 6: Upgraded 65mm Prompts (VAL-EP001-IMG0011–IMG0020)
        ├── 06_BATCH_002_MANIFEST.json               # Machine-readable JSON manifest for Batch 002
        ├── 06_IMAGE_PROMPTS_BATCH_003.md            # Part 6: Upgraded 65mm Prompts (VAL-EP001-IMG0021–IMG0030)
        ├── 06_BATCH_003_MANIFEST.json               # Machine-readable JSON manifest for Batch 003
        ├── 06_IMAGE_PROMPTS_BATCH_004.md            # Part 6: Upgraded 65mm Prompts (VAL-EP001-IMG0031–IMG0040)
        ├── 06_BATCH_004_MANIFEST.json               # Machine-readable JSON manifest for Batch 004
        ├── 06_IMAGE_PROMPTS_BATCH_005.md            # Part 6: Upgraded 65mm Prompts (VAL-EP001-IMG0041–IMG0050)
        ├── 06_BATCH_005_MANIFEST.json               # Machine-readable JSON manifest for Batch 005
        ├── 06_IMAGE_PROMPTS_BATCH_006.md            # Part 6: Upgraded 65mm Prompts (VAL-EP001-IMG0051–IMG0060)
        ├── 06_BATCH_006_MANIFEST.json               # Machine-readable JSON manifest for Batch 006
        ├── 07_CONTINUITY_AND_QC_REPORT.md           # Part 7: Continuity Audit & 65mm Phase-D QC Log (Batches 001–006)
        ├── 08_YOUTUBE_PUBLISHING_PACKAGE.md         # Part 8: YouTube SEO, Chapters, Thumbnail & Teaser
        ├── STORYBOARD_BATCH_001_PREVIEW.html        # Visual 16:9 Storyboard & 2s Cut Sync Viewer (00:00–00:20)
        ├── STORYBOARD_BATCH_002_PREVIEW.html        # Visual 16:9 Storyboard & 2s Cut Sync Viewer (00:20–00:40)
        ├── STORYBOARD_BATCH_003_PREVIEW.html        # Visual 16:9 Storyboard & 2s Cut Sync Viewer (00:40–01:00)
        ├── STORYBOARD_BATCH_004_PREVIEW.html        # Visual 16:9 Storyboard & 2s Cut Sync Viewer (01:00–01:20)
        ├── STORYBOARD_BATCH_005_PREVIEW.html        # Visual 16:9 Storyboard & 2s Cut Sync Viewer (01:20–01:40)
        ├── STORYBOARD_BATCH_006_PREVIEW.html        # Visual 16:9 Storyboard & 2s Cut Sync Viewer (01:40–02:00)
        └── assets/
            ├── references/                          # Locked Character Identity Reference Plates
            ├── batch_001/                           # 65mm Cinematic Batch 001 Stills (IMG0001–IMG0010 · 00:00–00:20)
            ├── batch_002/                           # 65mm Cinematic Batch 002 Stills (IMG0011–IMG0020 · 00:20–00:40)
            ├── batch_003/                           # 65mm Cinematic Batch 003 Stills (IMG0021–IMG0030 · 00:40–01:00)
            ├── batch_004/                           # 65mm Cinematic Batch 004 Stills (IMG0031–IMG0040 · 01:00–01:20)
            ├── batch_005/                           # 65mm Cinematic Batch 005 Stills (IMG0041–IMG0050 · 01:20–01:40)
            ├── batch_006/                           # 65mm Cinematic Batch 006 Stills (IMG0051–IMG0060 · 01:40–02:00)
            └── chapter_01_anchor_plates/            # Pre-Approved Chapter I Master Environment Anchors
```

---

## 4. ACTIVE PRODUCTION STATUS

| Episode | Title | Duration | Total Frames (`30/min`) | Completed Batches | Completed Frames | Next Queued Batch |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`EP001`** | **Before the Dragons: The Rise of Old Valyria** | `35:00` (`4,580` words) | **1,050** (`105` batches) | **Batches 001–006** (`00:00–02:00`) | **60 / 1,050** (`IMG0001–IMG0060`) | **Batch 007** (`02:00–02:20`, `IMG0061–IMG0070`) |
