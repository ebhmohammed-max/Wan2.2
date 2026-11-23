# DUN003 music credits and licences (v1, 2026-11-23)

Every music track in DUN003 is by **Kevin MacLeod (incompetech.com)**, licensed **CC BY 4.0**. Monetised YouTube use is allowed **as long as the credit block below is in the video description**. Kevin MacLeod says his music is not in Content ID. If a third party ever claims a track, dispute it and cite this licence.
All SFX (wind, tinnitus ring, heartbeat) are synthesised in `tools/mix_music.py`, so they need no licence.

## Paste into the YouTube description

```
Music:
"Lightless Dawn" Kevin MacLeod (incompetech.com)
"Deliberate Thought" Kevin MacLeod (incompetech.com)
"Dark Times" Kevin MacLeod (incompetech.com)
"Long Note Two" Kevin MacLeod (incompetech.com)
"Mysterioso March" Kevin MacLeod (incompetech.com)
"Phantasm" Kevin MacLeod (incompetech.com)
"Interloper" Kevin MacLeod (incompetech.com)
"Wizardtorium" Kevin MacLeod (incompetech.com)
"Private Reflection" Kevin MacLeod (incompetech.com)
"Night Vigil" Kevin MacLeod (incompetech.com)
"Unwritten Return" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

## Licence log

| Cue(s) | Track | Artist | Source URL | ISRC | Licence | Source sha256 |
|---|---|---|---|---|---|---|
| M1, M12 | Lightless Dawn | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Lightless%20Dawn.mp3 | USUAN1100655 | CC BY 4.0 | `59fd69e4432c9588…` |
| M2, M12b | Deliberate Thought | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Deliberate%20Thought.mp3 | USUAN1100261 | CC BY 4.0 | `243d5543c930bf54…` |
| M3 | Dark Times | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Dark%20Times.mp3 | USUAN1100747 | CC BY 4.0 | `8c05efb338ee645a…` |
| M4 | Long Note Two | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Long%20Note%20Two.mp3 | USUAN1100420 | CC BY 4.0 | `53fd96b8fdcae5d2…` |
| M5 | Mysterioso March | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Mysterioso%20March.mp3 | USUAN1100143 | CC BY 4.0 | `89a78f20e2c4e9dc…` |
| M6 | Phantasm | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Phantasm.mp3 | USUAN1100113 | CC BY 4.0 | `f5d2256207776d57…` |
| M7 | Interloper | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Interloper.mp3 | USUAN1100401 | CC BY 4.0 | `f979f0a000e45e70…` |
| M8 | Wizardtorium | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Wizardtorium.mp3 | USUAN1100007 | CC BY 4.0 | `fe19fd3846895309…` |
| M9 | Private Reflection | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Private%20Reflection.mp3 | USUAN1100587 | CC BY 4.0 | `fc8aa81f59749ee9…` |
| M10 | Night Vigil | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Night%20Vigil.mp3 | USUAN1900047 | CC BY 4.0 | `315009fda5154a09…` |
| M11 | Unwritten Return | Kevin MacLeod | https://incompetech.com/music/royalty-free/mp3-royaltyfree/Unwritten%20Return.mp3 | USUAN1500037 | CC BY 4.0 | `1d8036f3d6374ab8…` |

Two more tracks were fetched as alternates but are not used: Ossuary 6 - Air and Crypto, both Kevin MacLeod, CC BY 4.0.
The cue timings are in `DUN003_MUSIC_EDL.json`. To rebuild the mix, run `tools/mix_music.py`. The source mp3s are not kept in git: re-fetch them with `tools/ci_fetch_assets.py music` (CI) or download them from the URLs above.
