# Coverage shot cards — shots 03–08

Eight-part spine for each: **SUBJECT + WARDROBE + ACTION + ENVIRONMENT + CAMERA + LIGHTING + STYLE +
DETAILS + MOOD**. Every prompt ends with `BASE_LOOK.txt` appended verbatim. Route note per card.

Wan2.2 reminders: aspect comes only from `--size` (`720*1280` exact 9:16 for A14B, `704*1280` for
5B, cropped to 9:16 in delivery). Keep a take to one readable action; if a card needs two actions,
it's two shots.

---

## 03 — TRIGGER · the carving

*Bucket: detail / texture · Route: TI2V-5B 704×1280, 121f @ 24fps (cheapest, texture-only shot)*

| Part | Direction |
|---|---|
| Subject | a weathered male hand, ochre dust in the knuckle creases |
| Wardrobe | coarse brown linen sleeve, frayed cuff, rope-belt shadow across the wrist |
| Action | the hand moves slowly across the wall, then stops; the fingertips settle into a carved incision and trace it |
| Environment | black volcanic tuff wall, chisel marks, lamp soot, a hand-carved geometric symbol about 20 cm across, older than the tunnel around it |
| Camera | 50mm macro-ish close, handheld, slightly high angle looking down at the wall, subtle operator drift, no cut |
| Lighting | the oil lamp enters from frame-right and rakes across the wall at a low angle so the incision fills with shadow; everything outside the lamp falloff is black |
| Style | observational artefact documentation, one continuous take, no reveal flourish |
| Details | dust lifting off the stone as the fingers pass, grain, halation on the flame edge, slight focus hunting when the hand comes close |
| Mood | quiet discovery — he is not surprised, he recognises it |

**Prompt**
> A WEATHERED MALE HAND WITH OCHRE DUST IN THE KNUCKLE CREASES, COARSE BROWN LINEN SLEEVE WITH A
> FRAYED CUFF, MOVES SLOWLY ACROSS A BLACK VOLCANIC TUFF WALL AND STOPS AS THE FINGERTIPS SETTLE INTO
> A HAND-CARVED GEOMETRIC SYMBOL AND TRACE ITS GROOVE. CHISEL MARKS, LAMP SOOT AND CENTURIES OF DUST ON
> THE STONE. 50MM CLOSE HANDHELD SHOT FROM A SLIGHTLY HIGH ANGLE LOOKING DOWN AT THE WALL WITH SUBTLE
> OPERATOR DRIFT, NO CUT. A SMALL BRASS OIL LAMP ENTERS FROM FRAME RIGHT AND RAKES ACROSS THE WALL AT A
> LOW ANGLE SO THE INCISION FILLS WITH SHADOW, EVERYTHING OUTSIDE THE LAMP FALL-OFF IS PURE BLACK.
> OBSERVATIONAL ARTEFACT DOCUMENTATION, QUIET DISCOVERY RATHER THAN SURPRISE, DUST LIFTING OFF THE STONE
> AS THE FINGERS PASS. + BASE_LOOK

*Check on take: fingers (fuse first), symbol geometry staying static, lamp falloff not blowing out.*

---

## 04 — REACTION · his face

*Bucket: character close-up · Route: I2V-A14B 720×1280 from `@CAST`, 81f @ 16fps*

| Part | Direction |
|---|---|
| Subject | the explorer, matching `@CAST` exactly — identity, beard, wardrobe |
| Wardrobe | linen tunic collar, sash edge, satchel strap; no costume drift |
| Action | he looks at the wall, then lifts his eyes a few degrees along the carving, breathes, blinks once. Nothing is "acted" |
| Environment | tunnel wall behind him, out of focus into black |
| Camera | 85mm intimate handheld portrait, chest up, eye level, natural focus correction, camera reacts slightly late |
| Lighting | lamp below frame-right lifts his cheekbone, nose and beard; the other half of his face stays in deep shadow; flame flicker moves the key across his skin |
| Style | ethnographic documentary portrait, no pose, no camera awareness |
| Details | real pores, sweat sheen, grey stubble, visible breath in cold air, grain, halation |
| Mood | recognition without explanation |

**Prompt**
> THE MAN MATCHING @CAST IN IDENTITY, FACIAL FEATURES, BEARD, SKIN TONE AND WARDROBE, WEARING THE SAME
> ROUGH BROWN LINEN TUNIC, RED WOOL SASH AND SATCHEL STRAP. HE LOOKS AT THE WALL BESIDE HIM, THEN LIFTS
> HIS EYES A FEW DEGREES ALONG THE CARVING, BREATHES, AND BLINKS ONCE — NOTHING IS ACTED. TUNNEL WALL
> BEHIND HIM FALLING INTO BLACK. 85MM INTIMATE HANDHELD CHEST-UP PORTRAIT AT EYE LEVEL WITH NATURAL FOCUS
> CORRECTION, THE CAMERA REACTING SLIGHTLY LATE. A SMALL BRASS LAMP BELOW FRAME RIGHT LIFTS HIS CHEEKBONE,
> NOSE AND BEARD WHILE THE OTHER HALF OF HIS FACE STAYS IN DEEP SHADOW, THE FLAME FLICKER MOVING THE KEY
> ACROSS HIS SKIN. REAL PORES, SWEAT SHEEN, GREY STUBBLE, FAINT VISIBLE BREATH. ETHNOGRAPHIC DOCUMENTARY
> PORTRAIT, NO POSE, NO CAMERA AWARENESS, RECOGNITION WITHOUT EXPLANATION. + BASE_LOOK

*Check: face must not morph (kill after 70 frames if it does), eyes tracking consistently, lamp hand not
entering frame.*

---

## 05 — ESCALATION · the second chamber

*Bucket: wide establishing, deeper · Route: TI2V-5B (text-only is fine — no cast), 121f @ 24fps*

| Part | Direction |
|---|---|
| Subject | the explorer as a small figure, lamp in hand, seen from behind and above |
| Wardrobe | brown linen, hood down, silhouette only |
| Action | he walks away from camera down three carved steps, lamp swinging once, then holds still |
| Environment | a second, older chamber: lower ceiling, rougher tooling, granary niches, a worn millstone, one collapsed arch — visibly pre-dating the first chamber |
| Camera | 35mm wide from a high corner, static with a slow creep forward, the frame reading as vertical depth into black |
| Lighting | two lamps only: his, and one guttering on a niche shelf 8 m away; cold stone beyond both |
| Style | patient documentary, hold longer than comfortable |
| Details | thin haze, dust in the lamp cone, wet sheen on one wall, imperfect framing with a column edge intruding |
| Mood | the city is bigger than the tour, and older |

**Prompt**
> THE EXPLORER WEARING ROUGH BROWN LINEN WALKS AWAY FROM CAMERA DOWN THREE CARVED STONE STEPS INTO A
> SECOND, OLDER CHAMBER, THE LAMP SWINGING ONCE IN HIS HAND BEFORE HE HOLDS STILL AS A SMALL FIGURE IN
> THE LOWER THIRD OF FRAME. LOWER CEILING, ROUGHER TOOLING, GRANARY NICHES, A WORN MILLSTONE AND ONE
> COLLAPSED ARCH, THE SPACE VISIBLY PRE-DATING THE TUNNEL BEHIND HIM. 35MM WIDE FROM A HIGH CORNER,
> STATIC WITH A VERY SLOW CREEP FORWARD, VERTICAL DEPTH READS AS A DESCENT INTO BLACK. TWO LAMPS ONLY,
> HIS AND ONE GUTTERING ON A NICHE SHELF DEEP IN FRAME, COLD STONE BEYOND BOTH. THIN HAZE AND DUST IN
> THE LAMP CONE, A COLUMN EDGE INTRUDING INTO THE FRAME, PATIENT OBSERVATIONAL DOCUMENTARY. + BASE_LOOK

*Check: figure scale vs architecture (the whole point of the shot), lamp count — AI loves adding lights,
so re-state "two lamps only" if it cheats.*

---

## 06 — REALIZATION · the shaft

*Bucket: detail + insert (two beats, one take each if needed) · Route: TI2V-5B*

| Part | Direction |
|---|---|
| Subject | a vertical ventilation shaft, ~40 cm wide, cut through 40 m of rock |
| Wardrobe | n/a |
| Action | nothing moves except a thin column of dust drifting *upward* in otherwise dead-still air |
| Environment | the shaft mouth in a chamber ceiling; tool marks spiral up inside it |
| Camera | 35mm looking straight up the shaft, slow tilt from wall to opening, handheld |
| Lighting | the lamp from below, so the shaft mouth disappears into a vanishing point of black — no daylight**
 |
| Style | physical, factual, no drama |
| Details | grit on the ledges, one root or hair-thin fibre, grain, halation |
| Mood | the city breathed — this is how |

**Prompt**
> A NARROW VERTICAL VENTILATION SHAFT ABOUT FORTY CENTIMETRES WIDE CUT THROUGH FORTY METRES OF VOLCANIC
> ROCK, SPIRAL TOOL MARKS VISIBLE UP ITS INSIDE, ITS MOUTH IN A CHAMBER CEILING. NOTHING MOVES EXCEPT A
> THIN COLUMN OF DUST DRIFTING SLOWLY UPWARD IN OTHERWISE DEAD-STILL AIR. 35MM HANDHELD SHOT LOOKING
> STRAIGHT UP THE SHAFT, SLOW TILT FROM THE WALL TO THE OPENING, THE SHAFT DISAPPEARING INTO A VANISHING
> POINT OF BLACK RATHER THAN DAYLIGHT. LIT ONLY FROM BELOW BY AN OFF-FRAME OIL LAMP. GRIT ON THE LEDGES,
> ONE HAIR-THIN FIBRE, PHYSICAL AND FACTUAL RATHER THAN DRAMATIC. + BASE_LOOK

*Check: no daylight at the top — if the model puts a bright hole there, re-state "no daylight, the shaft
ends in darkness" and regenerate.*

---

## 07 — PAYOFF · the top of the stairs

*Bucket: anchor / wide · Route: I2V-A14B from `@CAST`, 81f*

| Part | Direction |
|---|---|
| Subject | the explorer, now lit from below, standing at the head of the main staircase |
| Wardrobe | linen tunic, sash, boots, lamp now in the *left* hand (continuity: he turned) |
| Action | he stops, lifts the lamp once, and the frame holds on him not descending |
| Environment | the great stair shaft, steps dropping away into total black, carved walls either side |
| Camera | 35mm medium-wide from slightly below, gently drifting back two steps, vertical composition with the stairs biting the bottom of frame |
| Lighting | the lamp from below is the only source; the stairs get 3 m of light then nothing |
| Style | restrained, withholding — the film refuses the bottom of the city |
| Details | his shadow thrown up the wall behind him, dust, guttering flame, grain |
| Mood | awe with a floor of unease |

**Prompt**
> THE MAN MATCHING @CAST IN IDENTITY AND WARDROBE, ROUGH BROWN LINEN TUNIC, RED SASH, LEATHER BOOTS,
> HOLDING THE BRASS OIL LAMP IN HIS LEFT HAND, STANDS AT THE HEAD OF A GREAT CARVED STAIRCASE AND STOPS,
> LIFTING THE LAMP ONCE. CARVED STONE STAIRS DROP AWAY BESIDE HIM INTO TOTAL BLACK, CUT WALLS EITHER
> SIDE, THE STEPS BITING THE BOTTOM EDGE OF THE VERTICAL FRAME. 35MM MEDIUM-WIDE FROM SLIGHTLY BELOW,
> GENTLY DRIFTING BACKWARDS TWO STEPS. THE LAMP FROM BELOW IS THE ONLY SOURCE, GIVING THE STAIRS THREE
> METRES OF LIGHT AND THEN NOTHING, HIS SHADOW THROWN UP THE WALL BEHIND HIM. RESTRAINED AND WITHHOLDING,
> AWE WITH A FLOOR OF UNEASE, DUST AND A GUTTERING FLAME. + BASE_LOOK

*Check: shadow direction must match the lamp position, and the stairs must not resolve into detail — the
black is the point.*

---

## 08 — HERO · the empty chamber (final frame of the film)

*Bucket: held wide, no human, no motion · Route: TI2V-5B, or T2V-A14B for the finest stone*

| Part | Direction |
|---|---|
| Subject | the first chamber, now empty |
| Wardrobe | n/a |
| Action | the single lamp on the niche shelf gutters twice and steadies; nothing else happens |
| Environment | the columns from shot 01, seen from the stairs, every archway repeating into black |
| Camera | 35mm wide, locked off, slightly off-axis and too low — an imperfect final frame |
| Lighting | one practical lamp, most of the frame in black, no reveal |
| Style | end-of-film stillness, keeps the audience in the room |
| Details | dust settling, flame halation, one column edge out of focus in the foreground |
| Mood | the city stays. We leave |

**Prompt**
> THE GREAT UNDERCARVED CHAMBER FROM EARLIER, NOW EMPTY. MASSIVE HAND-CARVED TUFF COLUMNS AND REPEATING
> ARCHWAYS DISAPPEARING INTO TOTAL BLACKNESS, SEEN FROM THE TOP OF THE STONE STAIRS. A SINGLE OIL LAMP ON
> A NICHE SHELF GUTTERS TWICE AND STEADIES — NOTHING ELSE MOVES, NO PEOPLE, NO LIGHT SOURCE BEYOND IT.
> 35MM LOCKED-OFF WIDE, SLIGHTLY OFF-AXIS AND TOO LOW, AN IMPERFECT FINAL FRAME WITH A BLURRED COLUMN EDGE
> IN THE FOREGROUND. MOST OF THE FRAME IN BLACK, NO REVEAL, DUST SETTLING IN THE AIR, END-OF-FILM
> STILLNESS THAT KEEPS THE AUDIENCE IN THE ROOM. + BASE_LOOK

*Check: absolutely no figure, no extra lamps, no camera move. If the model drifts, take the first 48
frames and hold the last one as a freeze for the final beat.*

---

## Assembly order in the edit

`01 world (5s) → 02 human (5s) → 03 trigger (4s) → 04 reaction (4s) → 05 escalation (5s) →
06 realization (4s) → 07 payoff (6s, music-free) → 08 hero (4s, hold to black)`

Total ≈ 37 s. Cut on: a footfall (01→02), the hand stopping (02→03), his blink (03→04), the lamp swing
(04→05), the dust column (05→06), his stop (06→07), the flame gutter (07→08).
