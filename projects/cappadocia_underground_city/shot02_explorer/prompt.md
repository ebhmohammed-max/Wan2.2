# Shot 02 — "The Lantern" (the explorer)

Vertical 9:16 · walking character shot · 5 s per Wan2.2 take · no text, no logo

Character: man, late fifties, short grey-streaked beard, sun-worn lined face, rough undyed
brown linen tunic, rope belt, faded dark red wool sash, worn leather boots, small leather
satchel, brass oil lantern. Established in `keyframes/kf01_walk.png` — **that image is the
identity reference**. Every take should start from it, or from a still that was itself derived
from it, so the face never drifts between takes.

---

## Master prompt (T2V / TI2V — copy verbatim)

A medium full-body tracking shot of an ancient male explorer walking slowly toward the camera
through a narrow hand-carved volcanic stone tunnel beneath Cappadocia, Turkey. He is a weathered
man in his late fifties, short grey-streaked dark beard, deep-set eyes, sun-worn lined skin,
wearing rough undyed brown linen clothing with a rope belt, a faded dark red wool sash, worn
leather boots and a small leather satchel. He carries a small glowing brass oil lantern in one
hand and his free hand rests flat against the rough carved stone wall, fingertips trailing along
the rock as he examines the passage. He takes slow natural realistic steps; the linen tunic and
sash move subtly with each step and the lantern swings gently on its handle, casting warm
flickering light across his face and the chiselled walls. The camera tracks smoothly backward
ahead of him, holding a steady medium full-body framing, no cuts. Realistic human gait and weight
shift, anatomically correct hands, consistent facial features. Cinematic documentary lighting,
warm lamp key light in deep shadow, volumetric haze, slow dust motes, ultra-detailed stone and
fabric texture, photorealistic, subtle film grain, vertical composition.

## Motion-only prompt (I2V — the reference frame already carries the look)

Slow natural walking motion toward the camera: three unhurried steps with realistic weight shift,
heel-to-toe footfalls, subtle swing of the linen tunic and the red sash. The brass lantern sways
gently in his hand, its flame flickering so the warm light ripples across his face and the carved
stone walls. His free hand slides slowly along the rock beside him. The camera tracks backward
smoothly at walking pace, holding the medium full-body framing steady, no cuts and no zoom. Steady
breathing, small natural head movements, stable face, photorealistic, subtle film grain.

## Extra negative terms

Wan2.2's built-in negative prompt (`wan/configs/shared_config.py → sample_neg_prompt`) already
covers blur, subtitles, over-exposure and static frames. For a walking human, add these — they are
set on the config/pipeline (`n_prompt=`), not on the CLI:

```
extra fingers, fused fingers, too many fingers, missing fingers, deformed hands, warped wrists,
extra limbs, extra arms, duplicated body, face morphing, identity change, aging jump, melting
features, foot sliding, floating feet, skating gait, rubber legs, bent knees, broken neck,
warped lantern, detached lantern, lantern in both hands, modern clothing, zipper, wristwatch,
text, subtitles, watermark, logo, cartoon, cgi, plastic skin, oversaturated, flicker
```

## Why this prompt is built the way it is

* **Identity lives in the image, not the text.** Wan2.2-T2V will invent a new man every seed.
  Image-to-video from `kf01_walk.png` is the only reliable way to hold the face — that is why the
  primary script here is `01_run_i2v_a14b.sh`, and why `kf02–kf04` were generated as *edits* of
  kf01 rather than fresh images.
* **Three steps, not a walk cycle.** Five seconds at 16–24 fps is ~3 unhurried steps. Asking for
  "walking quickly" or "several steps" turns into foot sliding; "three unhurried steps with
  heel-to-toe footfalls" stays physical.
* **Camera and subject moves are stated separately**, otherwise Wan averages them and he stops
  walking toward a static camera.
* **Hands fail first.** Keep at least one hand at rest (flat on the wall — that's in the prompt)
  so only the lantern hand has to animate, and add the finger negatives above.
* **Lantern = the light rig.** "lantern swings gently, casting warm flickering light" is what
  produces the moving key on his face; without that clause the lamp tends to freeze as a prop.
* **Framing lock:** "medium full-body framing, no cuts, no zoom" keeps the model from cutting or
  punching in mid-take. Pass `--frame_num 81` (A14B) / `121` (5B) so the take matches 5 s.
