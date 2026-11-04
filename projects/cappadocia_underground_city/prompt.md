# Shot 01 — "The City Below" (Cappadocia underground city)

Vertical 9:16 · single continuous dolly-in · 5 s per Wan2.2 take · no text, no logo

---

## Master prompt (T2V / TI2V — copy this verbatim)

A slow, continuous cinematic dolly shot moving forward through a narrow ancient underground
stone tunnel beneath Cappadocia, Turkey. Rough hand-carved volcanic tuff walls, scarred by chisel
marks and centuries of lamp soot, pass close to both edges of the frame around a low hand-carved
arched doorway ahead. As the camera glides forward the tunnel opens into an enormous mysterious
underground chamber: massive carved stone columns, hand-carved arched doorways and niches
receding into darkness, and a few ancient stone steps leading deeper into black shadow. Dim warm
oil lamps burn in wall niches, casting soft amber pools of light; realistic dust particles drift
slowly through thin volumetric light shafts and a delicate atmospheric haze softens the distant
architecture. The camera keeps one smooth, steady forward push with a faint natural drift,
gradually revealing the scale and depth of the architecture. Photorealistic, ultra-detailed natural
stone textures, historically inspired architecture, realistic documentary cinematography, natural
shadows, low-key dramatic lighting, subtle film grain, 4K quality, vertical composition.

## Motion-only prompt (I2V — start frame already carries the look)

The camera performs a smooth cinematic dolly forward at walking pace, gliding through the carved
stone doorway and into the dark chamber beyond, revealing the depth of the carved architecture as
lamps pass out of frame. Dust particles drift slowly through the warm volumetric light, faint haze
shifts in the air, flames flicker gently. Steady, stabilized documentary camera, no cuts, no zoom
snap, photorealistic, subtle natural film grain.

## Negative prompt

Wan2.2 ships a built-in negative prompt (`wan/configs/shared_config.py →
sample_neg_prompt`) that already suppresses blur, subtitles, over-exposure and static frames.
If you need the extra terms below, append them to that string — `generate.py` exposes no
`--negative_prompt` flag, so it must be set on the config / pipeline (`n_prompt=` in
`wan/text2video.py`, `wan/textimage2video.py`, `wan/image2video.py`):

```
text, subtitles, captions, watermark, logo, signature, UI overlay, cartoon, cgi, plastic texture,
oversaturated, neon colors, HDR halo, blown highlights, flat lighting, modern objects, people,
tourists, cables, electric lamps, fisheye, dutch angle, fast whip pan, blurry, low resolution,
jpeg artifacts, warped architecture, melted stone, duplicated archways, flicker
```

## Prompt-craft notes

* **Wan reads one dense paragraph best.** Keep it ~120–170 words; lead with camera + subject,
  then architecture, then light/atmosphere, then the look. The version above is ordered that way.
* **Say the move once, clearly.** "slow continuous dolly forward … one smooth steady push" beats
  stacking "dolly in, zoom in, push forward, tracking" — stacked verbs make Wan2.2 jitter.
* **Scale needs a reveal verb.** "the tunnel opens into … gradually revealing the scale" is what
  makes the model widen the space mid-take instead of starting wide.
* **Lighting words that survive diffusion:** "dim warm oil lamps", "volumetric light shafts",
  "atmospheric haze", "low-key". Avoid "bright", "softly lit" (flattens the carved stone).
* **Vertical framing:** Wan2.2 has no aspect token, so the composition comes from `--size`
  (see README). Words like "tall narrow frame, vertical composition" help a little; the
  resolution does the real work.
* **Seeds:** walls/stairs are the usual failure point. Roll 4–6 seeds and keep the one where the
  steps read cleanly; `--base_seed` is reproducible per take (suggested: 20261031, 20261101,
  7, 42, 1234, 9001).
