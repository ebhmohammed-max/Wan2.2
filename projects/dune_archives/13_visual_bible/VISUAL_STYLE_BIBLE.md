# THE DUNE ARCHIVES — Visual Style Bible (v1.0 — 2026-11-23)

**Identity:** ultra-realistic 3D cinematic sci-fi historical reconstruction. The look is "a documentary crew sent back through ten thousand years with an IMAX camera", not fan art and not a film still.

**Method:** this bible applies the repo's 2WULFFS playbook (`studio/2wulffs-playbook.md`). Every shot is decided in this order: **Insight → Idea → Visual rule → Execution → Prompt.** *Consistency beats spectacle.*

---

## 1. Insight → Idea → Visual rules

- **Insight:** Dune is about deep time, scale and ecology, and about how belief turns into power. Audiences already know the films' look. The channel wins by showing what the books describe and the films never show: the Butlerian Jihad, Leto II, the Scattering and Rakis burning. It should look like evidence rather than spectacle.
- **Idea:** *"The Archive."* Every episode is a recovered record. Images feel like reconstructions assembled by historians: grounded, physically lit and slightly weathered.
- **Visual rules (global):**
  1. Scale is always readable. Include a human figure, a vehicle or architecture for reference in every wide shot.
  2. Light is physical: a single dominant source, motivated, with atmospheric haze.
  3. Materials are tactile: sand grain, sweat salt, worn leather, oxidised metal, woven fibre.
  4. Restraint in colour: each era/planet uses one palette, with one accent colour at most.
  5. No action blur or chaos. The camera is a calm observer, even in battles.
  6. Text never appears inside generated images. Titles and labels are added in the edit.

## 2. The 10-field decision grid (fill for every shot)

| # | Field | Default / rule |
|---|---|---|
| 1 | Subject | One clear subject per frame. Characters by continuity-sheet ID (e.g. `CS-PAUL-B`) |
| 2 | Wardrobe | From the continuity sheet + era palette; no film-costume replication |
| 3 | Action | One verb. Slow, deliberate, readable |
| 4 | Location | From the planet table; label RECON if inferred |
| 5 | Time | Era tag + time of day |
| 6 | Light | Single motivated key; see the lighting table |
| 7 | Camera | Lens and height; see the camera language |
| 8 | Mood | One word (dread, awe, grief, resolve, intrigue) |
| 9 | Texture | Film grain (fine), haze, dust, specular sand glints |
| 10 | Style | "ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, anamorphic 2.39:1 framing inside 16:9" |

## 3. ALWAYS / NEVER world rules

| ALWAYS | NEVER |
|---|---|
| Original faces from the continuity sheets | Any actor likeness or named actor or film in a prompt |
| A human-scale reference in wide shots | Floating, unscaled objects |
| Blue-in-blue eyes only for spice-saturated characters | Blue eyes on off-world characters before their exposure |
| Stillsuits with nose plugs and catch-tubes on Fremen in the open desert | Bare-faced Fremen in the deep desert at noon |
| Shields shown as a faint shimmer; fights with slow blades | Guns firing through shields |
| Ornithopters with articulated flapping wings (book) | The 2021 dragonfly ornithopter silhouette |
| Sandworms with a ringed body, a crystal-toothed maw and a trailing dust plume | Eyes on sandworms; the 1984 three-lip "flower" maw |
| Era palette discipline (§4) | Neon or cyberpunk lighting |
| Text and labels added in the edit | Text, logos, watermarks or captions inside generated images |
| Reconstruction tags on maps and inferred geography | Precise "official" coordinates or invented planetary statistics |
| Violence implied (aftermath, shadows, scale) | Gore, torture detail, sexualised imagery |

## 4. Era and planet palettes

| Era / place | Palette | Light | Signature texture |
|---|---|---|---|
| Butlerian Jihad (201–108 BG, EU-heavy) | Cold steel, ash grey, ember orange | Fire against machine cold-light | Smoke, cracked chrome |
| Corrino Imperium / Kaitain | Gold, ivory, deep scarlet | Soft high-key sun, controlled sky | Marble, brocade |
| Caladan | Slate, sea-green, warm amber interiors | Overcast, rain | Wet granite, wool |
| Giedi Prime (RECON, not the film's black sun) | Oil black, sodium orange, griffin blue | Industrial sodium light, smog | Grime, rivets |
| Arrakis (open desert) | Bone, ochre, burnt sienna, deep blue shadow | Hard white sun, heat haze | Sand grain, spice haze |
| Arrakis (sietch) | Umber, glowglobe amber | Pools of warm light | Rock, woven fabric, water basins |
| Spice / prescience | Cinnamon-orange haze, blue-in-blue | Volumetric | Floating particulate |
| Leto II's Empire | Muted green Arrakis, silver-grey worm-flesh, Fish Speaker white | Even, lifeless "peace" light | Stillness, dust-free |
| Heretics / Chapterhouse | Desaturated, cold teal, Matre orange accents | Low-angle winter light | Stone, ash |

House accents (heraldry per `05_houses/GREAT_HOUSES.md`):
- **Atreides:** red hawk on green/black `[VERIFY]`.
- **Harkonnen:** blue griffin.
- **Corrino:** golden lion `[VERIFY]`.

## 5. Camera language

| Shot | Lens | Use |
|---|---|---|
| Epic wide (EW) | 18–24 mm, low horizon | Scale: worms, heighliners, armies |
| Establishing (EST) | 35 mm | Places, sietches, palaces |
| Medium (MS) | 50 mm | Characters in context |
| Portrait (CU) | 85 mm, shallow depth of field | Emotion, decisions |
| Insert (INS) | 100 mm macro | Crysknife, gom jabbar, spice, stillsuit detail |
| Overhead (OH) | Map / satellite | Geography (pair with `map_animator.py`) |

Motion recipes (`tools/motion_engine.py`):
- **PUSH_IN:** tension.
- **PULL_OUT:** scale reveal.
- **PAN:** landscapes.
- **TILT_UP:** towers and heighliners.
- **WORM_RISE:** emergence.
- **DRIFT:** portraits.
- **PARALLAX:** environments.
- **HOLD:** symbolic frames.

Atmosphere layers (sand, heat, lightsweep, shake) are used only when motivated.

## 6. Prompt formula (image-generation)

```
[STYLE] ultra-realistic 3D cinematic reconstruction, photoreal, physically based lighting, fine film grain,
[SUBJECT + CONTINUITY ID] <character sheet anchor text>,
[WARDROBE] ..., [ACTION] ..., [LOCATION + ERA] ..., [TIME] ..., [LIGHT] ..., [CAMERA] <lens, height, framing>,
[MOOD] ..., [TEXTURE] ..., composition safe for 16:9 with 2.39:1 letterbox, no text
NEGATIVE: text, watermark, logo, actor likeness, celebrity, film still, cartoon, anime, oversaturated, neon,
extra fingers, deformed hands, blurry face, gore
```

## 7. File naming and batching

- **Image name:** `DUN###_BATCH###_SCENE###_SHORTDESC.png`, e.g. `DUN003_BATCH001_SCENE004_THRONE_ROOM_SHAFT.png`.
- **Batch size:** at most 10 images per generation batch. Each batch has a manifest JSON that records prompt, seed, continuity IDs and canon label.
- **Unique images vs on-screen shots:**
  - One unique still produces 1–3 on-screen shots through motion recipes, reframes (wide / medium crop) and atmosphere passes.
  - Planning default: 5–8 unique stills and 10–15 shots per minute.
  - The final count is approved per episode by the creative director.

## 8. QC checklist (per image)

- [ ] Face matches the continuity sheet and resembles no actor. **Mandatory for every visible face, in every world (Dune films, HBO's GoT and HotD, the LotR and Hobbit films).** Check at full size: "would a fan name an actor?" If yes or maybe, FIX. See `worlds/westeros/WESTEROS_CANON_POLICY.md` §4b.
- [ ] Wardrobe, palette and heraldry match the era and house.
- [ ] Scale reference is present in wide shots.
- [ ] No text, watermark or logo.
- [ ] No film-design replication (ornithopter, stillsuit cut, worm maw).
- [ ] Hands, eyes and anatomy are clean.
- [ ] Canon label assigned in the manifest.
- [ ] Reconstructed geography is tagged RECON.
