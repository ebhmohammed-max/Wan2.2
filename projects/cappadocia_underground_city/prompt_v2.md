# Shot 01 — prompt v2 ("director's cut")

Rewritten to the 2WULFFS spine (`studio/2wulffs-playbook.md §6`) and to the project's creative bible
(`../CREATIVE_BIBLE.md`). `prompt_v2.txt` is the copy-paste block: body + `BASE_LOOK.txt` appended.

**Bindings**

| Token | Wan2.2 equivalent |
|---|---|
| `@WORLD` | conditioning image — start from `keyframes/kf01_tunnel.png` (I2V), or none for pure T2V |
| base look | appended verbatim at the end of `prompt_v2.txt` |

**Why v2 differs from v1**

| Spine part | v1 | v2 |
|---|---|---|
| Subject | "ancient underground city" | *an empty tunnel, deep enough that no daylight reaches it* — the subject is the emptiness |
| Action | "reveal enormous chamber" | the dolly is given a **speed** (slow walking pace) and a continuation clause ("continues into…"), which is what stops Wan2.2 stalling |
| Environment | "rough volcanic stone walls" | chisel tooling, soot above the niche, one lamp in a niche — physical evidence instead of adjectives |
| Camera | "smooth cinematic dolly forward" | 35mm, chest height, human-operated, faint drift, slightly late reframe, no cut/no zoom |
| Lighting | "dim warm oil-lamp lighting, volumetric" | **the lamp is the only source**, warm raking key on *one* wall, everything else black — the visual rule from the bible |
| Style | "photorealistic, ultra-detailed, 4K" | grain, halation, imperfect exposure, no HDR — realness vocabulary replaces perfection vocabulary |
| Details | "realistic dust particles" | dust drifting through the shaft, one doorway edge intruding frame-left (deliberate imperfection) |
| Mood | "mysterious documentary atmosphere" | "mysterious, withheld, physical — the camera only ever moves deeper" |

**Route.** Block it on TI2V-5B at 704×1280/121f/`--sample_steps 30`, then re-roll the keeper at 50
steps or on T2V-A14B at 720×1280/81f. `--base_seed` per take; sweep 4 seeds.

**Check on each take:** does the light source stay singular (AI adds lamps) · does the camera keep
moving deeper (no retreat or orbit) · do the hands/arch geometry deform (cut before it breaks) · is the
staircase still dark at the end (the withholding is the idea).
