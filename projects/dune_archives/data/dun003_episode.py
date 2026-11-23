"""DUN003 — Dune Messiah Explained Before Part Three — single source of truth.

Approved by the creative director on 2026-11-23:
  topic DUN003 · runtime ~15 min · 150 unique stills in 15 batches of 10.

tools/build_episode.py turns this module into:
  17_scripts/DUN003_SCRIPT_v0.1.md
  18_storyboards/DUN003_STORYBOARD.csv
  19_batches/DUN003/DUN003_BATCH###.json  (+ DUN003_BATCH_INDEX.md)

Label keys:
  O ORIGINAL FRANK HERBERT CANON · F FILM ADAPTATION
  A ADAPTATION-SPECIFIC INTERPRETATION · X FAN THEORY · R CREATIVE RECONSTRUCTION
Every image is a CREATIVE RECONSTRUCTION visually. `label` records the canon status
of the event or claim the shot illustrates.
"""

META = {
    "id": "DUN003",
    "title": "Dune Messiah Explained Before Part Three",
    "tier": "STANDARD",
    "runtime_s": 900,
    "wpm": 135,  # cinematic narration pace incl. music breaths
    "spoilers": "SPOILERS: DUNE (1965), DUNE MESSIAH (1969); light tease of CHILDREN OF DUNE",
    "scope": "ORIGINAL FRANK HERBERT CANON primary; FILM ADAPTATION comparisons labelled in ch. 11",
    "hooks": "H3 (cold open), H4 (re-hook ~25%), H5 (archive card)",
    "images": "150 unique stills · ~177 still-based shots + 3 map scenes ≈ 180 on-screen shots · 15 batches × 10",
    "publish_target": "12–15 Dec 2026 (Dune: Part Three opens 18 Dec 2026)",
    "status": "DIRECTOR APPROVED 2026-11-23 (text locked) — [VERIFY] page checks still open before publish",
    "script_version": "v1.0",
}

# Continuity anchors (from 14_continuity sheets + DUN003 addendum).
ANCHORS = {
    "CS-PAUL-B": "young man about seventeen with a broad angular face, heavy straight dark brows, deep-set narrow eyes, prominent aquiline nose with a slight bump, wide thin-lipped mouth, strong square jaw, close-cropped dark brown hair shaved short at the sides, sun-darkened olive skin, pale scar cutting through the left eyebrow, lean wiry build",
    "CS-PAUL-C": "man about thirty with a broad angular face, heavy straight brow ridge, deep-set narrow eyes entirely blue including the whites, prominent aquiline nose with a slight bump from an old break, wide thin-lipped mouth, strong square jaw under a short dense dark beard, close-cropped dark brown hair shaved short at the sides, early grey streaks at the temples, weathered sun-darkened olive skin, pale scar cutting through the left eyebrow, lean wiry build",
    "CS-PAUL-D": "man about thirty with a broad angular face, heavy straight brow ridge, prominent aquiline nose with a slight bump, wide thin-lipped mouth, strong square jaw under a short dense dark beard, close-cropped dark brown hair with early grey at the temples, weathered olive skin, eyes covered by dark smoked-glass lenses, faint healed burn scarring at the temples, calm composed expression",
    "CS-PAUL-E": "gaunt blind man in his late thirties with a broad angular face, prominent aquiline nose with a slight bump, long matted dark brown hair streaked with grey, ragged beard, eyes covered by a strip of dark cloth, rough sun-bleached desert robe",
    "CS-CHANI-B": "slight wiry Fremen woman about thirty, fine-boned angular face with high flat cheekbones, ordinary rounded human ears, wide-set eyes, a small straight nose with a band of freckles across it, thin-lipped mouth, narrow pointed chin, straight dark auburn-red hair pulled back into a single tight braid threaded with small metal water rings, small notch scar on upper right ear, faint pale scar along the right jawline, eyes entirely saturated blue including the whites (no white sclera), sun-darkened weathered skin",
    "CS-IRULAN": "tall regal woman in her early thirties, long narrow face with a high forehead, strong straight nose, deep-set cool grey eyes under heavy lids, thin composed lips, a small dark mole on the left cheekbone, long neck, pale-gold hair worn in a tight braided crown, faint ink stains on right fingertips, gold and scarlet court gown with a lion clasp",
    "CS-ALIA-A": "small girl about two years old with bronze-auburn hair, wide-set intense eyes entirely blue, unnervingly adult expression",
    "CS-ALIA-B": "girl about fifteen with bronze-auburn hair, wide-set intense eyes entirely blue, strong straight brow line, unnervingly adult expression, black and gold priestly robes",
    "CS-MOHIAM": "very old woman with a birdlike face, thin lipless mouth, piercing pale eyes, deep black hood and aba robe",
    "CS-SCYTALE": "smooth hairless androgynous face with flat indistinct features and pale eyes, plain grey garments",
    "CS-DUNCAN-A": "compact muscular man about thirty, tight black curly hair, round jaw with cleft chin, olive-brown skin, warm brown eyes, dark green and black military uniform with a small red hawk insignia",
    "CS-DUNCAN-B": "compact muscular man about thirty, tight black curly hair, round jaw with cleft chin, olive-brown skin, faceted metallic steel-grey artificial eyes, plain grey tunic",
    "CS-LETO2-A": "boy about nine with dark hair, strong straight brow line, sharp cheekbones, entirely blue eyes, simple Fremen robe",
    # DUN003 addendum — ORIGINAL DESIGN, pending director approval.
    "CS-SHADDAM": "heavy-set emperor in his seventies, broad fleshy face with heavy jowls, thick hooked nose, small sharp hazel eyes under bushy grey-red brows, thinning red hair streaked with grey combed straight back, short pointed red-grey beard, gold and scarlet military uniform with a golden lion clasp",
    "CS-EDRIC": "long-limbed elongated humanoid with webbed fingers and finned feet, small smooth head, drifting inside a tall sealed tank of swirling orange gas",
    "CS-KORBA": "heavy-set middle-aged Fremen priest with shaved head, ritual scars on scalp, ochre and black robes, entirely blue eyes, zealous stare",
    "CS-LICHNA": "young Fremen woman about twenty, narrow face, dark hair under a hood, entirely blue eyes, plain desert robe",
    "CS-OTHEYM": "very old emaciated Fremen veteran, deeply lined face, wispy white beard, fierce entirely blue eyes, worn robe",
    "CS-BIJAZ": "dwarf the size of a child, wide round face, grey-tinged skin, sly glittering eyes, plain dun robe",
}

LABEL_NAMES = {
    "O": "ORIGINAL FRANK HERBERT CANON",
    "F": "FILM ADAPTATION",
    "A": "ADAPTATION-SPECIFIC INTERPRETATION",
    "X": "FAN THEORY",
    "R": "CREATIVE RECONSTRUCTION",
}

# Chapters: id, title, duration (s), source note, VO (paragraphs separated by blank lines).
CHAPTERS = [
    dict(id="00", title="COLD OPEN", dur=50, src="Dune (1965) Book III; Dune Messiah (1969) opening [VERIFY]", vo="""
He won.

Twelve years ago, a young exile came out of the deep desert of Arrakis with an army, a religion, and the throne of the known universe. Every prophecy came true.

Now he rules from a citadel built out of his own legend. Whole worlds pray to his name.

And he has spent every one of those twelve years looking for a way out.

So what happens to Paul Atreides after he wins?

This is the story Frank Herbert wrote next. It is the story the final film of the trilogy is built on. And it is the story that turns the hero of Dune into something much harder to look at.
"""),
    dict(id="01", title="ARCHIVE CARD", dur=15, src="H5", vo="""
The Dune Archives. Era: about ten thousand two hundred A.G. Subject: Dune Messiah. Source: the original Frank Herbert novels. Where the record goes silent, we reconstruct, and we will say so on screen.
"""),
    dict(id="02", title="WHERE DUNE LEFT PAUL", dur=100, src="Dune (1965) Book III [VERIFY]", vo="""
To understand Messiah, start where Dune ends.

In the closing pages of the first novel, Paul defeats the Harkonnens, humbles the Padishah Emperor Shaddam the Fourth, and takes the throne with the oldest lever in the Imperium. He can destroy the spice. Without spice, the Spacing Guild cannot navigate. Without the Guild, there is no empire.

To make his claim legal, Paul marries Shaddam's eldest daughter, the Princess Irulan. But it is a marriage in name only. The woman he loves, the Fremen Chani, stays at his side as his concubine. She is the one he means to be the mother of his children.

And Paul has seen something else. In his visions, a holy war pours out of Arrakis in his name, carried by Fremen legions across the stars. He has tried to stop it. He has seen that he cannot. Even if he died, his legend would march on without him.

The first novel ends there, on a victory. Most readers closed the book believing they had read the story of a hero.

Dune Messiah opens about twelve years later. The jihad has done exactly what he feared.
"""),
    dict(id="03", title="THE PRICE OF THE JIHAD", dur=90, src="Dune Messiah — Paul's casualty tally [VERIFY figures & context]", vo="""
Herbert does not show the war in battle scenes. He shows it in arithmetic. The jihad is not a single war. It is twelve years of conquest, conversion and purge, fought by people who believe their emperor is God.

In Messiah, Paul tallies the cost himself. Roughly sixty-one billion dead. Ninety planets sterilized. Hundreds more broken. He measures himself against the worst tyrants of humanity's ancient past, and finds that they were amateurs.

Around him, a priesthood called the Qizarate has turned his life into scripture. Fremen who once counted every drop of water now govern worlds. His image is sold, worshipped and obeyed. Even his sister Alia, born already awake with the memories of generations, is venerated as a goddess.

And the man at the centre of it can see the future. That is the trap. His prescience does not set him free. It shows him narrow paths, and every path he can see leads somewhere worse.

His enemies are counting on exactly that.

Dune: Part Three arrives on the eighteenth of December, 2026, and this is the story it is built on. So before you see what the film does with it, here is what the book actually says.
"""),
    dict(id="04", title="THE CONSPIRACY", dur=120, src="Dune Messiah — Wallach IX meeting [VERIFY]", vo="""
On Wallach Nine, home world of the Bene Gesserit, four powers meet in secret.

The first is the Sisterhood itself, in the person of the Reverend Mother Gaius Helen Mohiam. She is the same woman who once tested a teenage Paul with the gom jabbar. The Bene Gesserit spent some ninety generations breeding toward a Kwisatz Haderach they could control. They got one they cannot. Now they want his bloodline.

The second is the Spacing Guild, in the person of a Steersman named Edric, who floats inside a sealed tank of orange spice gas. The Guild resents being held hostage by the man who controls the spice. And Edric brings a unique weapon. Prescient beings like him leave blind spots in Paul's vision. While a Navigator sits at the table, Paul cannot see the plot.

The third is the Bene Tleilax, secretive masters of genetics, in the person of Scytale, a Face Dancer who can wear any face and any voice.

The fourth is the most personal. Princess Irulan, Paul's wife in name only. She was trained by the Sisterhood, she is the daughter of the emperor Paul deposed, and she has been denied the one thing that would secure her place in history, the mother of his heir. In secret, she has been slipping contraceptives into Chani's food.

None of them can simply kill Paul. Killing a messiah only makes a martyr. Their plan is subtler. They will try to break him from the inside, through his grief, his loyalties and his own legend.

And the first move is a gift.
"""),
    dict(id="05", title="THE GIFT: HAYT", dur=90, src="Dune Messiah — Hayt presented by Edric [VERIFY]", vo="""
Edric arrives at court as the Guild's ambassador, and he brings a present from the Tleilaxu.

It is a man who died for him. Duncan Idaho, the Atreides swordmaster who gave his life so that Paul and his mother could escape the Harkonnen attack. The last time Paul saw that face, Duncan was holding back Imperial Sardaukar so that a boy and his mother could reach the desert.

The Tleilaxu recovered his body and grew it again in their axlotl tanks. This is a ghola, with the same flesh, the same face and the same tight black curls, but none of the memories. They call him Hayt. In place of his own eyes he has faceted Tleilaxu metal eyes, and he has been trained as a Mentat and a philosopher.

Paul knows the gift is a weapon. He accepts it anyway. Herbert makes that choice the emotional core of the book. Paul would rather keep a poisoned piece of his past than lose it twice.

Hayt serves him honestly, as far as he understands honesty. He questions Paul, warns him, even challenges the religion built around him. But beneath his training lies something he does not know about, a conditioning planted by the Tleilaxu, waiting for one specific moment.

Remember that. It comes back at the worst possible time.
"""),
    dict(id="06", title="THE TRAP CLOSES", dur=105, src="Dune Messiah — Otheym, Lichna, Bijaz, stone burner [VERIFY sequence]", vo="""
Meanwhile the conspiracy reaches into the one people Paul trusts most, the Fremen.

Some of the old desert fighters resent what empire has made of them. Water-rich, city-bound, softened. A faction of naibs and priests begins to plot against the man they once followed into battle.

A message reaches Paul from Otheym, one of his original Fedaykin death commandos, carried by Otheym's daughter Lichna. But the real Lichna is already dead. The young woman standing in front of Paul is Scytale, wearing her face.

Paul goes anyway, at night, through the city to Otheym's house. The old fighter is dying, and he gives Paul a strange inheritance. A Tleilaxu dwarf named Bijaz, a living recorder who has memorised the names of the traitors among the Fremen. It is real intelligence, and it is a second Tleilaxu trap.

Then, outside in the street, the conspirators set off a stone burner.

A stone burner is an atomic weapon, forbidden under the Great Convention, and its light burns out the eyes of those who see it. Paul has foreseen this moment, and he walks into it anyway. Men around him are blinded. So is Paul.
"""),
    dict(id="07", title="THE BLIND EMPEROR", dur=60, src="Dune Messiah — Fremen custom; vision-sight [VERIFY]", vo="""
Under Fremen law, the blind are given to the desert. A man without eyes is a burden on the tribe.

But Paul does not behave like a blind man. To the horror of everyone around him, he moves through rooms without hesitation. He recognises faces. He promises the soldiers blinded with him new Tleilaxu eyes.

He can do this because his prescience has replaced his sight. He follows his vision of each moment and lays it over the world in front of him. To the Fremen, it looks like proof of godhood. To Paul, it is the loneliest kind of sight there is, because he can no longer tell where the world ends and the vision begins. The Fremen call it a miracle. Paul knows it is borrowed time. It only works as long as the future he is following holds.

And the future is about to change.
"""),
    dict(id="08", title="CHANI AND THE TWINS", dur=90, src="Dune Messiah — birth at Sietch Tabr; Hayt; Scytale [VERIFY]", vo="""
Chani is pregnant at last. She escaped Irulan's contraceptives by returning to a desert diet, but the damage is done, and the pregnancy is racing forward at a dangerous pace.

At Sietch Tabr, Chani goes into labour, and Paul's vision fails him. He has seen one child, a daughter. Chani gives birth to two. A boy, Leto, and a girl, Ghanima.

Chani dies.

At that moment, two traps spring at once.

Chani's death is exactly the moment the Tleilaxu conditioning was waiting for. Hayt moves to kill Paul, but the command collides with everything Duncan Idaho was, and something breaks open. Duncan's memories come flooding back. A ghola has recovered the man he used to be.

Then Scytale makes his offer. The Tleilaxu can bring Chani back, as a ghola. The price is everything Paul holds. And to press the point, Scytale holds a knife over the newborn twins.

Paul's vision ended with Chani. Now he is truly blind. And then, he sees, through the eyes of his infant son. Through Leto's eyes, Paul finds Scytale, and throws his knife.
"""),
    dict(id="09", title="INTO THE DESERT", dur=60, src="Dune Messiah — ending [VERIFY]", vo="""
The conspiracy is broken. And Paul is finished anyway.

He has been offered a way back to sight, to Chani, to power, and he has seen where every one of those paths leads.

So the Emperor of the Known Universe does the one thing Fremen law asks of a blind man. He walks alone into the deep desert, and gives himself to Shai-Hulud.

Behind him, Alia takes the regency for the twins, with the restored Duncan Idaho at her side. And Irulan, who helped bring about Chani's death, devotes herself to raising Chani's children.

There is no grave and no body. Only a legend that no longer needs him.

The empire survives. The legend grows. The man is gone.
"""),
    dict(id="10", title="BOOK VS FILM: WHAT TO WATCH FOR", dur=70, src="Dune: Part Two (2024) — FILM ADAPTATION; Part Three reporting [VERIFY]", vo="""
So how much of this will reach the screen? Here the records diverge, and we will be precise about what is book and what is film.

In the novels, Chani loves Paul and stays at his side to the end. In Dune: Part Two, she rejects his holy war and walks away from him. That is the film's own choice.

In the novels, Alia is already born and walking by the final battle, and the jihad that follows runs for twelve years. The films compress that timeline.

Part Three is adapted from Messiah, and reporting so far points to the conspiracy, Irulan and the ghola at its core. Beyond that, anything you read about how it ends is speculation, and we will label it that way.

What is certain is that the book does not end in triumph. If the film is faithful, the audience that cheered Paul in Part Two is about to watch him lose everything.
"""),
    dict(id="11", title="CODA: THE WARNING", dur=50, src="Frank Herbert, 'Dune Genesis', OMNI, July 1980 — paraphrase only [VERIFY]", vo="""
Frank Herbert later wrote that Dune was never meant to celebrate its hero. Messiah completes the warning. Charismatic leaders are dangerous because people want to follow them, and even a good man, handed absolute power and absolute belief, can become a catastrophe.

Not every reader welcomed that. Many who loved the triumph of the first book did not want to be told the triumph was the disaster. That was exactly Herbert's point.

But Paul's story is not quite over. A blind preacher will one day walk out of that same desert. And the son whose eyes Paul borrowed will choose the path his father refused, a path that will take three and a half thousand years.

That is the next record in the archive.
"""),
]

# Shots per chapter. Tuple:
# (KEY, shot, lens, continuity_id or "", body, light, mood, motion, label, n_shots)
# n_shots = 2 → the still is also used as a REUSE reframe (crop/second motion pass).
S = {}
S["00"] = [
    ("THRONE_ROOM_SHAFT", "EW", "24mm", "", "vast stone throne hall of the Arrakeen citadel, a raised empty throne carved from dark basalt, tiny armoured guards along the far walls for scale, sand-coloured monumental architecture", "a single hard shaft of white desert light through a high slit window, floating dust motes", "awe", "PUSH_IN", "O", 2),
    ("PAUL_EMPEROR_PORTRAIT", "CU", "85mm", "CS-PAUL-C", "seated on a dark stone throne, black imperial robe with muted red hawk embroidery at the collar, gaze slightly off camera, haunted", "hard side light from a single shaft, deep shadow", "dread", "DRIFT", "O", 2),
    ("CITADEL_EXTERIOR_DAWN", "EW", "18mm", "", "colossal citadel of sand-coloured stone rising above the desert city of Arrakeen, stepped terraces, tiny figures and ornithopters with articulated insect-like flapping wings, towering rock cliffs of the Shield Wall behind", "low dawn sun, long shadows, heat haze", "awe", "PULL_OUT", "O", 2),
    ("PILGRIM_CROWDS", "EW", "24mm", "", "endless crowds of robed pilgrims filling a vast plaza before the citadel, arms raised, plain cloth banners with no lettering, dust haze", "hard morning sun", "awe", "PAN_LR", "O", 1),
    ("YOUNG_PAUL_DESERT_MEMORY", "MS", "50mm", "CS-PAUL-B", "wearing a grey-brown stillsuit and hooded cloak, walking along a dune crest, small figure against vast sand, a hooded woman following far behind", "dusk, warm rim light", "resolve", "PARALLAX", "O", 1),
    ("HAND_ON_THRONE_ARM", "INS", "100mm macro", "", "a man's hand wearing a signet ring engraved with a hawk, resting on a worn basalt throne arm, sand grains in the carved grooves", "single shaft of light", "intrigue", "HOLD", "O", 1),
    ("PRESCIENCE_BRANCHES", "EW", "24mm", "", "a lone robed silhouette standing on a narrow stone causeway above an infinite desert haze, faint glowing cinnamon-orange threads of possible paths branching ahead, most fading into darkness", "volumetric spice haze", "dread", "PUSH_IN", "R", 1),
    ("PAUL_WINDOW_SILHOUETTE", "MS", "35mm", "CS-PAUL-C", "silhouetted at a tall balcony window looking out over the city of Arrakeen, black robe edges lit orange", "golden-hour backlight", "grief", "DRIFT", "O", 1),
    ("MANUSCRIPT_DESK", "INS", "100mm macro", "", "an ancient archive desk with handwritten parchment pages covered in blurred illegible glyphs, a bronze stylus, fine sand scattered across the paper", "warm glowglobe light", "intrigue", "PUSH_IN", "R", 1),
]
S["01"] = [
    ("ARCHIVE_VAULT", "EST", "35mm", "", "a vast dim archive vault carved into living rock, shelves of crystal record spools and scrolls receding into darkness, open central space with negative room for a title overlay", "a single warm floating glowglobe, drifting dust", "intrigue", "PUSH_IN", "R", 1),
]
S["02"] = [
    ("BATTLE_ARRAKEEN_STORM", "EW", "18mm", "", "Fremen legions riding giant ringed sandworms with crystal-toothed maws through a massive sandstorm toward towering cliffs, tiny riders for scale, dust plumes", "storm-dimmed orange light", "awe", "WORM_RISE", "O", 2),
    ("SHADDAM_DEFEATED", "MS", "50mm", "CS-SHADDAM", "standing defeated in a damaged audience chamber, shoulders sagging, courtiers in plain dark robes retreating behind him", "dusty diffused light through a broken roof", "defeat", "HOLD", "O", 1),
    ("SPICE_THREAT", "INS", "100mm macro", "", "a hand holding a fistful of glittering cinnamon-orange spice melange, letting it pour through the fingers, desert out of focus behind", "hard sun, glinting particles", "resolve", "PUSH_IN", "O", 1),
    ("GUILD_HEIGHLINER_ORBIT", "EW", "18mm", "", "an immense elongated Guild heighliner hanging in orbit above the ochre disc of a desert planet, tiny frigates nearby for scale", "starlight and planet glow", "awe", "TILT_UP", "O", 1),
    ("WEDDING_IRULAN", "EST", "35mm", "", "a cold formal imperial marriage in a cavernous hall seen from far behind the assembly, faces not visible, a slight young man in black and a tall pale-gold-haired woman in a gold and scarlet gown standing an arm's length apart, rows of nobles", "high windows, cool daylight", "cold", "PUSH_IN", "O", 1),
    ("IRULAN_PORTRAIT", "CU", "85mm", "CS-IRULAN", "composed but resentful sidelong glance, palace interior behind", "soft high-key light", "intrigue", "DRIFT", "O", 2),
    ("CHANI_PORTRAIT", "CU", "85mm", "CS-CHANI-B", "Fremen robes with restrained imperial jewellery, quiet steady gaze", "warm sietch lamp light", "tenderness", "DRIFT", "O", 2),
    ("PAUL_CHANI_HANDS", "INS", "100mm macro", "", "two hands entwined, a woman's wrist with a bracelet of small metal water rings, a man's hand with a hawk signet ring, rough woven fabric beneath", "warm lamp light", "tenderness", "HOLD", "O", 1),
    ("JIHAD_VISION", "EW", "24mm", "", "a prescient vision: endless columns of desert warriors with plain green banners pouring from the dunes into a star-filled sky, ghostly double exposure over a burning world", "orange volumetric light", "dread", "PULL_OUT", "R", 1),
    ("FREMEN_LEGION_MARCH", "EW", "24mm", "", "thousands of Fremen warriors in grey-brown stillsuits and hooded cloaks marching in columns toward waiting troop transports on a sand plain", "hard white sun, heat haze", "resolve", "PAN_RL", "O", 1),
    ("YOUNG_EMPEROR_GAZE", "CU", "85mm", "CS-PAUL-B", "wearing a black imperial robe, staring into the middle distance, troubled", "single motivated key light", "dread", "PUSH_IN", "O", 1),
    ("BURNING_CITY_DISTANT", "EW", "24mm", "", "a foreign city skyline burning on the night horizon, seen from a ridge where silhouetted hooded warriors stand watching", "fire glow against night", "grief", "PARALLAX", "O", 1),
    ("TIME_PASSAGE_DUNES", "EW", "18mm", "", "sweeping dunes with long shadows, wind streaming sand from the crests, timeless", "low raking sun", "melancholy", "PAN_LR", "R", 1),
    ("PAUL_ASCENDS_THRONE", "MS", "50mm", "CS-PAUL-B", "wearing a black imperial robe, climbing the steps to a vast throne, courtiers kneeling on either side", "shaft of light from above", "resolve", "PUSH_IN", "O", 1),
    ("SIETCH_TABR_INTERIOR", "EST", "35mm", "", "a Fremen sietch carved into rock, woven hangings, covered water basins, families moving between chambers", "pools of amber glowglobe light", "warmth", "PARALLAX", "O", 1),
    ("LION_THRONE_ABANDONED", "EST", "35mm", "", "an ornate throne of gold and pale crystal carved with lions in an abandoned imperial throne room, dust sheets over furniture", "soft cool light through tall windows", "defeat", "HOLD", "R", 1),
    ("DESERT_TO_CITADEL", "EW", "24mm", "", "the deep desert at noon with heat shimmer, a distant citadel silhouette on the horizon", "hard white sun", "foreboding", "PUSH_IN", "R", 1),
]
S["03"] = [
    ("PAUL_LEDGER", "EST", "35mm", "CS-PAUL-C", "seated at a stone desk in a dim study among piles of record crystals, staring at a glowing projection of star systems", "amber glowglobe plus cool projection light", "guilt", "PUSH_IN", "O", 2),
    ("STERILIZED_PLANET", "EW", "18mm", "", "a dead planet seen from orbit, ash-grey and cratered, thin glowing scars of old fires, a single warship silhouette in the foreground", "cold starlight", "dread", "PULL_OUT", "O", 1),
    ("ASH_FIELD_SURVIVOR", "EW", "24mm", "", "a vast field of ash and ruined towers under a grey sky, one cloaked figure walking among the ruins for scale", "flat overcast", "grief", "PAN_LR", "O", 1),
    ("ANCIENT_TYRANTS_ECHO", "EST", "24mm", "", "a hall of colossal weathered stone statues of nameless ancient conquerors with eroded faces, one tiny robed man standing at their feet", "single shaft of light", "intrigue", "TILT_UP", "R", 1),
    ("QIZARATE_PRIESTS", "MS", "50mm", "", "a procession of priests in ochre and black robes carrying smoking censers through a temple corridor", "incense haze, warm side light", "zeal", "PAN_RL", "O", 1),
    ("TEMPLE_INTERIOR", "EW", "24mm", "", "a vast desert temple with towering columns, worshippers prostrate on the stone floor, smoke rising in light shafts", "volumetric light shafts", "awe", "PULL_OUT", "O", 2),
    ("FREMEN_GOVERNOR", "MS", "50mm", "", "a weathered Fremen man in rich robes seated in an off-world palace, a fountain of running water behind him, uneasy", "soft palace light", "irony", "DRIFT", "O", 1),
    ("WATER_FOUNTAIN_EXCESS", "INS", "50mm", "", "water spilling lavishly from an ornate fountain in a desert city, a Fremen child staring at it", "hard sun, sparkling water", "irony", "HOLD", "R", 1),
    ("ICONS_MARKET", "MS", "35mm", "", "a crowded bazaar stall selling small carved figurines of a hooded faceless emperor, pilgrims bargaining", "dusty slanted light", "cynicism", "PAN_LR", "O", 1),
    ("ALIA_REGENT_PORTRAIT", "CU", "85mm", "CS-ALIA-B", "temple smoke behind her, still and watchful", "single shaft of light", "unease", "DRIFT", "O", 2),
    ("PAUL_TRAPPED_VISION", "MS", "35mm", "", "a robed man in a dark chamber surrounded by ghostly translucent echoes of himself walking away in different directions, all fading", "orange volumetric glow", "dread", "PUSH_IN", "R", 1),
    ("NARROW_PATH_CANYON", "EW", "24mm", "", "a single narrow path through a deep canyon of red rock, walls closing in, a small hooded figure walking", "a thin slit of hard light from above", "claustrophobia", "PUSH_IN", "R", 1),
    ("SHADOW_WATCHERS", "EST", "35mm", "", "cloaked figures in a shadowed upper gallery watching a throne hall far below", "low light, deep shadow", "intrigue", "DRIFT", "R", 1),
    ("HOURGLASS_SAND", "INS", "100mm macro", "", "an ornate hourglass with spice-orange sand running out on a stone ledge, desert window behind", "warm side light", "urgency", "HOLD", "R", 1),
    ("ANCIENT_BOOK_LECTERN", "EST", "35mm", "", "an ancient leather-bound book on a stone lectern in an archive vault, fine sand drifting across it", "warm glowglobe", "anticipation", "PUSH_IN", "R", 1),
]
S["04"] = [
    ("WALLACH_IX_EXTERIOR", "EW", "18mm", "", "a cold grey world, a complex of dark stone buildings on a windswept plateau, tiny hooded figures crossing a courtyard", "pale low sun, cold dusk", "secrecy", "PULL_OUT", "R", 2),
    ("CONSPIRATORS_TABLE", "EST", "35mm", "", "a circular stone chamber with four presences around a table: an old hooded woman, a tall tank of orange gas with a vague humanoid shape, a plain grey-robed figure, a pale-gold-haired woman in a gold gown", "low light, pools of shadow", "intrigue", "PUSH_IN", "O", 2),
    ("MOHIAM_PORTRAIT", "CU", "85mm", "CS-MOHIAM", "watching from deep within her hood", "single low glowglobe", "menace", "DRIFT", "O", 1),
    ("GOM_JABBAR_MEMORY", "INS", "100mm macro", "", "an old woman's hand holding a long fine needle near a young man's neck, a small black box nearby, faces out of frame", "dim warm light", "dread", "PUSH_IN", "O", 1),
    ("BREEDING_RECORDS", "EST", "35mm", "", "an archive of endless shelves of faintly glowing genealogical record crystals, black-robed women moving among them", "cool dim light", "intrigue", "PAN_LR", "R", 1),
    ("BG_SISTERS_CIRCLE", "EW", "24mm", "", "a circle of black-robed women in deep hoods standing in a stone hall, faces hidden", "single overhead light", "control", "DRIFT", "O", 1),
    ("EDRIC_TANK", "MS", "50mm", "CS-EDRIC", "the tank mounted on a dark metal platform in a shadowed chamber", "orange glow from the gas", "eerie", "DRIFT", "O", 2),
    ("EDRIC_EYE", "INS", "100mm macro", "", "extreme close-up through tank glass of an inhuman eye, entirely blue, orange vapour swirling", "orange glow", "eerie", "PUSH_IN", "O", 1),
    ("PRESCIENCE_BLIND_SPOT", "EW", "24mm", "", "an abstract branching web of glowing orange future-threads with a dark void at its centre where the threads vanish", "volumetric glow", "mystery", "PUSH_IN", "R", 1),
    ("HEIGHLINER_HOLD", "EW", "18mm", "", "the cavernous interior of a Guild heighliner hold, house frigates docked inside like toys", "cold metallic light with warm accents", "awe", "TILT_UP", "R", 1),
    ("SCYTALE_BLANK", "CU", "85mm", "CS-SCYTALE", "neutral expression, plain background", "flat grey light", "unsettling", "DRIFT", "O", 2),
    ("SCYTALE_MORPH", "MS", "50mm", "CS-SCYTALE", "mid-transformation, half of the face smooth and blank, the other half becoming a weathered man's face", "a moving band of light across the face", "uncanny", "HOLD", "O", 1),
    ("TLEILAXU_CITY", "EW", "24mm", "", "a city of dark enclosed towers under a hazy sky, small grey-robed figures in the streets", "overcast", "secrecy", "PAN_RL", "R", 1),
    ("IRULAN_WRITING", "MS", "50mm", "CS-IRULAN", "seated at a writing desk, writing on parchment in elegant illegible script", "warm lamp light", "ambition", "PUSH_IN", "O", 1),
    ("IRULAN_LATTICE", "CU", "85mm", "CS-IRULAN", "watching through a carved lattice screen as a red-haired Fremen woman crosses a courtyard below", "backlight through the lattice", "jealousy", "DRIFT", "O", 1),
    ("CONTRACEPTIVE_VIAL", "INS", "100mm macro", "", "a tiny crystal vial tipping clear drops into a bowl of food on a silver tray", "dim warm light", "betrayal", "HOLD", "O", 1),
    ("CHANI_MEAL", "MS", "50mm", "CS-CHANI-B", "eating at a low table in palace apartments, unaware, a servant leaving the room", "soft window light", "tension", "PUSH_IN", "O", 1),
    ("MARTYR_SHRINE", "EW", "24mm", "", "a colossal shrine with burning offerings and immense grieving crowds", "firelight", "dread", "PULL_OUT", "R", 1),
    ("FOUR_SHADOWS", "EST", "35mm", "", "four long shadows cast across a stone floor converging on the base of a single throne", "low raking sun", "intrigue", "HOLD", "R", 1),
    ("VEILED_GIFT_DOORWAY", "MS", "50mm", "", "a hooded figure standing behind a sheer veil in a tall citadel doorway", "strong backlight", "mystery", "PUSH_IN", "R", 1),
]
S["05"] = [
    ("EDRIC_AUDIENCE", "EW", "24mm", "", "a tall tank of orange gas carried into a vast throne hall on a platform by grey-robed attendants, a distant figure on the throne, courtiers lining the hall", "single shaft of light", "ceremony", "PUSH_IN", "O", 2),
    ("HAYT_REVEAL", "MS", "50mm", "CS-DUNCAN-B", "standing motionless before a throne", "shaft of light", "shock", "PUSH_IN", "O", 2),
    ("DUNCAN_LAST_STAND", "EW", "24mm", "CS-DUNCAN-A", "fighting alone in a narrow rock corridor against many armoured soldiers, blades raised, dust, no gore", "firelight", "sacrifice", "PARALLAX", "O", 1),
    ("DUNCAN_SWORDMASTER", "CU", "85mm", "CS-DUNCAN-A", "a warm confident half-smile", "warm daylight", "nostalgia", "DRIFT", "O", 1),
    ("AXLOTL_VATS", "EST", "35mm", "", "a dim laboratory with rows of sealed organic vats glowing faintly, grey-robed technicians, nothing explicit", "dim sickly light", "unease", "PAN_LR", "R", 1),
    ("HAYT_EYES", "INS", "100mm macro", "CS-DUNCAN-B", "extreme close-up of the faceted metallic artificial eyes reflecting light", "hard key light", "uncanny", "PUSH_IN", "O", 2),
    ("PAUL_HAYT_FACEOFF", "MS", "35mm", "", "a bearded man in a black imperial robe and a curly-haired man in a grey tunic facing each other across a stone chamber", "a shaft of light falling between them", "tension", "HOLD", "O", 1),
    ("HAYT_MENTAT", "MS", "50mm", "CS-DUNCAN-B", "seated cross-legged in a dark study, metal eyes glinting, deep in calculation", "low lamp light", "intellect", "DRIFT", "O", 1),
    ("PAUL_DECISION", "CU", "85mm", "CS-PAUL-C", "eyes closed, pained, accepting", "side light", "grief", "PUSH_IN", "O", 1),
    ("ATREIDES_BANNER", "INS", "50mm", "", "an old faded hawk banner in green and black, torn, hanging in a shadowed citadel corridor", "dim light", "memory", "HOLD", "R", 1),
    ("HAYT_BALCONY", "MS", "35mm", "", "a curly-haired man in a grey tunic speaking beside a robed emperor on a balcony above worshipping crowds", "backlight", "candor", "DRIFT", "O", 1),
    ("HAYT_TRAINING", "EST", "35mm", "CS-DUNCAN-B", "practising alone with a short blade in a training hall, a faint shimmer of a personal shield around him", "light shafts", "discipline", "PARALLAX", "O", 1),
    ("HIDDEN_CONDITIONING", "EW", "24mm", "", "abstract: a human head in profile formed of fine sand with a single glowing thread knotted deep inside", "volumetric light", "foreboding", "PUSH_IN", "R", 1),
    ("TLEILAXU_WATCHER", "MS", "50mm", "", "a small grey-skinned man in a dark robe watching through a narrow window from a dark room", "dim light", "menace", "HOLD", "R", 1),
    ("HAYT_DOORWAY_GUARD", "EST", "35mm", "CS-DUNCAN-B", "standing guard in a doorway at night outside a sleeping chamber", "warm corridor backlight", "ambiguity", "HOLD", "O", 1),
]
S["06"] = [
    ("FREMEN_NAIBS_SECRET", "EST", "35mm", "", "old Fremen leaders with entirely blue eyes whispering in a dark rock alcove, faces half lit", "single oil lamp", "conspiracy", "PUSH_IN", "O", 1),
    ("SOFT_FREMEN_CITY", "MS", "35mm", "", "Fremen in fine city robes without stillsuits lounging by a water garden", "soft afternoon light", "decay", "PAN_LR", "O", 1),
    ("KORBA_PRIEST", "CU", "85mm", "CS-KORBA", "incense smoke drifting past", "warm side light", "zeal", "DRIFT", "O", 1),
    ("LICHNA_ARRIVAL", "MS", "50mm", "CS-LICHNA", "kneeling before armed guards in a citadel corridor, eyes downcast", "torchlight", "deception", "PUSH_IN", "O", 1),
    ("LICHNA_FACE_SEAM", "CU", "85mm", "CS-LICHNA", "a faint unnatural seam of light along the jaw suggesting a mask beneath", "hard side light", "eerie", "HOLD", "O", 2),
    ("ARRAKEEN_NIGHT_STREETS", "EW", "24mm", "", "narrow streets of a desert city at night with sparse floating glowglobes, a hooded escort moving through", "two moons and glowglobes", "danger", "PARALLAX", "R", 1),
    ("PAUL_NIGHT_ESCORT", "MS", "35mm", "", "a man in a plain hooded desert cloak walking with two guards through a dark alley", "low light", "resolve", "PAN_RL", "O", 1),
    ("OTHEYM_HOUSE", "EST", "35mm", "", "a modest mud-and-stone house with a low door in a poor district, oil lamps in the window", "warm lamp glow at night", "foreboding", "PUSH_IN", "R", 1),
    ("OTHEYM_DYING", "CU", "85mm", "CS-OTHEYM", "lying on worn cushions, trembling hands", "oil lamp light", "pathos", "DRIFT", "O", 1),
    ("BIJAZ_PORTRAIT", "MS", "50mm", "CS-BIJAZ", "seated on a low stool, sly grin", "oil lamp light", "sly", "DRIFT", "O", 2),
    ("BIJAZ_RECITING", "CU", "85mm", "CS-BIJAZ", "mid-speech, eyes glittering", "oil lamp light", "menace", "PUSH_IN", "O", 1),
    ("RECORD_CRYSTALS_TRAY", "INS", "100mm macro", "", "a tray of small engraved record crystals passed between two hands", "oil lamp light", "intrigue", "HOLD", "R", 1),
    ("STONE_BURNER_DEVICE", "INS", "50mm", "", "a crude cylindrical device of dark metal half buried in sand beside a wall, a faint red glow", "night", "dread", "PUSH_IN", "R", 1),
    ("GUARDS_TAKE_COVER", "MS", "35mm", "", "soldiers in a street turning away and throwing arms over their faces as white light begins", "sudden white flash", "panic", "HOLD", "O", 1),
    ("STONE_BURNER_FLASH", "EW", "24mm", "", "a blinding white-violet flash erupting over the rooftops of a city district at night, silhouetted towers, a wall of dust", "overexposed flash", "catastrophe", "PULL_OUT", "O", 2),
    ("AFTERMATH_STREET", "EW", "24mm", "", "a burnt, glassy street at dawn, smoke rising, figures wandering with hands over their eyes, no gore", "grey dawn", "grief", "PAN_LR", "O", 1),
    ("PAUL_STANDING_ASH", "MS", "50mm", "CS-PAUL-D", "standing upright amid smoke, face turned from camera, cloak scorched", "grey smoky light", "resolve", "DRIFT", "O", 1),
    ("MELTED_STONE", "INS", "100mm macro", "", "a stone wall glazed and melted into glass by heat, embers glowing", "ember light", "aftermath", "HOLD", "R", 1),
]
S["07"] = [
    ("FREMEN_LAW_DESERT", "EW", "24mm", "", "a blind Fremen elder led to the edge of open desert by tribe members, then left alone facing the dunes", "hard sun", "sorrow", "PULL_OUT", "O", 1),
    ("PAUL_BLIND_PORTRAIT", "CU", "85mm", "CS-PAUL-D", "in a black imperial robe", "soft side light", "eerie calm", "DRIFT", "O", 2),
    ("PAUL_WALKS_COURT", "EST", "35mm", "CS-PAUL-D", "walking confidently down a crowded throne hall while courtiers recoil in awe", "shaft of light", "awe", "PUSH_IN", "O", 1),
    ("BLINDED_SOLDIERS", "MS", "35mm", "", "a row of soldiers with bandaged eyes seated against a wall, a robed man's hand resting on one shoulder", "dim light", "compassion", "PAN_LR", "O", 1),
    ("TLEILAXU_EYES_TRAY", "INS", "100mm macro", "", "a velvet-lined tray holding pairs of faceted metallic artificial eyes", "cold light", "unease", "HOLD", "O", 1),
    ("VISION_OVERLAY_ROOM", "EST", "35mm", "", "a dim room overlaid with glowing orange outlines of every object, as if seen through vision instead of eyes", "volumetric glow", "mystery", "PUSH_IN", "R", 1),
    ("FREMEN_AWE", "CU", "85mm", "", "a young Fremen guard with entirely blue eyes wide in reverent awe", "side light", "awe", "DRIFT", "O", 1),
    ("PAUL_BALCONY_MOONS", "MS", "35mm", "CS-PAUL-D", "alone on a balcony at night, face raised to the wind, two moons in the sky", "moonlight", "foreboding", "DRIFT", "O", 1),
    ("CRACKING_CRYSTAL", "INS", "100mm macro", "", "a thin crystal pane with a spreading crack catching orange light", "warm light", "foreboding", "HOLD", "R", 1),
    ("SANDSTORM_APPROACH", "EW", "18mm", "", "a massive wall of sandstorm approaching a rock cliff at sunset", "orange sunset", "foreboding", "PULL_OUT", "R", 1),
]
S["08"] = [
    ("CHANI_DESERT_MEAL", "MS", "50mm", "CS-CHANI-B", "eating simple desert food in a sietch, one hand resting on her belly", "amber lamp light", "hope", "DRIFT", "O", 1),
    ("CHANI_PAIN", "CU", "85mm", "CS-CHANI-B", "sweating and pained, clutching her robe", "low amber light", "fear", "PUSH_IN", "O", 1),
    ("SIETCH_TABR_EXTERIOR", "EW", "24mm", "", "a rock cliff with hidden cave entrances at dusk, stillsuited guards, an ornithopter with folded articulated wings landed nearby", "dusk", "tension", "PULL_OUT", "R", 1),
    ("BIRTH_CHAMBER", "EST", "35mm", "", "a sietch chamber with Fremen midwives and an old woman in a black hood around a woman lying on cushions, modest and implied", "warm lamps", "tension", "PUSH_IN", "O", 1),
    ("PAUL_WAITING", "MS", "50mm", "CS-PAUL-D", "standing in a rock corridor outside a chamber, one hand on the wall", "low light", "dread", "HOLD", "O", 1),
    ("TWINS_NEWBORN", "INS", "50mm", "", "two newborn infants wrapped in woven Fremen blankets side by side", "soft warm light", "wonder", "DRIFT", "O", 2),
    ("CHANI_HAND_STILL", "INS", "100mm macro", "", "a woman's hand with a bracelet of water rings lying still on rough fabric", "fading lamp light", "grief", "HOLD", "O", 1),
    ("PAUL_GRIEF", "CU", "85mm", "CS-PAUL-D", "head bowed, one hand over his face", "dark, single low light", "grief", "PUSH_IN", "O", 2),
    ("HAYT_TRIGGERED", "MS", "50mm", "CS-DUNCAN-B", "mid-step toward the camera with a blade drawn, face contorted in internal struggle", "hard side light", "violence", "PUSH_IN", "O", 1),
    ("DUNCAN_AWAKENS", "CU", "85mm", "CS-DUNCAN-B", "tears on his face, recognition dawning", "light warming across the face", "revelation", "DRIFT", "O", 1),
    ("SCYTALE_KNIFE_CRADLE", "MS", "35mm", "CS-SCYTALE", "standing in a sietch chamber holding a knife over a cradle with two infants, a blind man standing in the doorway", "lamp light", "menace", "HOLD", "O", 1),
    ("LETO_INFANT_EYES", "INS", "100mm macro", "", "close-up of a newborn's eyes, impossibly aware, entirely blue", "soft light", "eerie", "PUSH_IN", "O", 1),
    ("INFANT_POV", "EW", "18mm", "", "a low wide view from cradle height of a lamplit rock chamber, a grey-robed figure looming, a man in the doorway", "volumetric haze", "tension", "PUSH_IN", "R", 1),
    ("CRYSKNIFE_THROWN", "INS", "100mm macro", "", "a milky-white curved crystal knife spinning through lamplit air", "amber light", "climax", "HOLD", "O", 1),
    ("SCYTALE_FALLEN", "EST", "35mm", "", "a grey-robed figure fallen on a stone floor, no gore, an intact cradle nearby, lamps flickering", "dim light", "release", "PULL_OUT", "O", 1),
]
S["09"] = [
    ("PAUL_LEAVES_SIETCH", "MS", "35mm", "CS-PAUL-D", "in a simple desert robe walking out of a cave mouth into blinding light while Fremen stand aside", "strong backlight", "resolve", "PULL_OUT", "O", 2),
    ("LONE_FIGURE_DUNES", "EW", "18mm", "", "a tiny lone robed figure walking across endless dunes at dawn", "low dawn sun", "sublime", "PULL_OUT", "O", 2),
    ("FOOTPRINTS_ERASED", "INS", "50mm", "", "footprints in sand being erased by wind", "low raking light", "loss", "HOLD", "R", 1),
    ("WORM_SIGN_HORIZON", "EW", "24mm", "", "the dust plume of an approaching sandworm on the horizon behind a distant lone figure", "hard sun", "awe", "WORM_RISE", "O", 1),
    ("ALIA_ON_THRONE", "MS", "50mm", "CS-ALIA-B", "seated alone on a vast dark throne", "shaft of light", "power", "PUSH_IN", "O", 1),
    ("DUNCAN_AND_ALIA", "EST", "35mm", "", "a curly-haired man with metallic eyes standing beside a young bronze-haired woman in black and gold on a balcony", "dusk", "alliance", "DRIFT", "O", 1),
    ("IRULAN_WITH_TWINS", "MS", "50mm", "CS-IRULAN", "holding an infant in a sietch nursery, softened expression", "warm lamp light", "redemption", "DRIFT", "O", 1),
    ("CITADEL_DUSK", "EW", "18mm", "", "the citadel at dusk with lights in the windows, crowds still gathered below", "dusk", "legacy", "PULL_OUT", "O", 2),
    ("SHRINE_LAMPS", "INS", "50mm", "", "hundreds of small oil lamps and offerings at a desert shrine", "warm flame light", "devotion", "TILT_UP", "R", 1),
    ("EMPTY_THRONE_SAND", "EST", "35mm", "", "an empty dark throne with sand drifting across its steps", "shaft of light", "absence", "PUSH_IN", "R", 1),
    ("DUNE_SUNSET_ABSENCE", "EW", "18mm", "", "a dune crest silhouetted against an enormous sunset, no figure", "golden light", "elegy", "PAN_LR", "R", 1),
]
S["10"] = [
    ("ARCHIVE_TWO_SCROLLS", "EST", "35mm", "", "two different ancient manuscripts laid side by side on an archive table, blurred illegible script", "split lighting, warm left, cool right", "analysis", "PUSH_IN", "R", 1),
    ("CHANI_AT_PAULS_SIDE", "MS", "50mm", "CS-CHANI-B", "standing beside a robed emperor in a throne hall, her hand on his arm", "warm light", "loyalty", "DRIFT", "O", 1),
    ("LONE_RIDER_BACK", "EW", "24mm", "", "a lone Fremen woman seen from behind standing on a dune crest, staff in hand, open desert ahead", "hard afternoon sun", "independence", "PULL_OUT", "F", 1),
    ("ALIA_TODDLER", "CU", "85mm", "CS-ALIA-A", "in a sietch, watching the camera", "amber light", "eerie", "DRIFT", "O", 1),
    ("TIMELINE_STRATA", "EW", "24mm", "", "abstract: a desert cliff face with visible bands of strata glowing faintly, each band a different era", "volumetric light", "analysis", "PAN_LR", "R", 1),
    ("REEL_IN_SAND", "INS", "50mm", "", "a vintage film reel half buried in sand", "warm side light", "adaptation", "HOLD", "R", 1),
    ("HAYT_PROFILE", "CU", "85mm", "CS-DUNCAN-B", "profile silhouette, metallic eye catching light", "dark rim light", "intrigue", "DRIFT", "O", 1),
    ("SHATTERED_MIRROR_FACES", "MS", "50mm", "", "a grey-robed figure reflected in a shattered mirror, each shard showing a different face", "hard side light", "uncertainty", "HOLD", "R", 1),
    ("DIVERGING_RIDGES", "EW", "18mm", "", "two dune ridges diverging under a storm sky", "storm light", "uncertainty", "PULL_OUT", "R", 1),
    ("FROZEN_CROWD", "EW", "24mm", "", "a vast cheering crowd in a plaza frozen mid-motion, dust hanging in the air", "suspended golden light", "irony", "PUSH_IN", "R", 1),
]
S["11"] = [
    ("WRITERS_DESK_1960S", "EST", "35mm", "", "a 1960s writer's desk with a manual typewriter, stacks of manuscript pages with illegible text, a desert plant on the windowsill, no person present", "warm afternoon window light", "reflection", "PUSH_IN", "R", 1),
    ("FOLLOWERS_INTO_STORM", "EW", "24mm", "", "a sea of robed followers walking behind a single banner-bearer into a storm", "storm light", "warning", "PULL_OUT", "R", 1),
    ("CRACKED_STATUE", "CU", "50mm", "", "the head of a colossal hooded hero statue with a crack running through its face, sand blowing", "hard sun", "warning", "TILT_UP", "R", 1),
    ("PREACHER_TEASE", "MS", "50mm", "CS-PAUL-E", "led by a young guide, emerging from a dust haze", "hard hazy light", "mystery", "PUSH_IN", "O", 1),
    ("LETO_BOY_TEASE", "CU", "85mm", "CS-LETO2-A", "staring at the horizon", "golden light", "destiny", "DRIFT", "O", 1),
    ("GOLDEN_PATH_TEASE", "EW", "18mm", "", "a single golden path of light stretching across the dunes to the horizon, distant ancient ruins", "golden light", "awe", "PUSH_IN", "R", 1),
    ("SANDTROUT_HAND", "INS", "100mm macro", "", "a child's hand in the sand with a thin silver-grey membrane creeping over it", "low light", "unease", "HOLD", "O", 1),
    ("ARCHIVE_DOOR_CLOSING", "EST", "35mm", "", "a massive stone archive door closing on a vault, the last glowglobe light", "amber light", "closure", "PULL_OUT", "R", 1),
    ("END_CARD_DUNES", "EW", "24mm", "", "a dark minimal dune landscape at blue hour with large negative space for end-card text", "blue hour", "calm", "HOLD", "R", 1),
]

# Map scenes (rendered by tools/map_animator.py; not part of the 150 stills).
# (chapter, insert after shot index, scene JSON to author, VO cue, label)
MAPS = [
    ("02", 3, "templates/maps/DUN003_MAP_A_spice_lever.json", "Guild ↔ spice ↔ throne schematic", "R"),
    ("03", 1, "templates/maps/DUN003_MAP_B_jihad_spread.json", "Schematic spread of the jihad (positions artistic, RECON)", "R"),
    ("04", 0, "templates/maps/DUN003_MAP_C_wallach_ix.json", "Wallach IX → Arrakis schematic route (RECON)", "R"),
]

# Fact-check log: claim, label, source to verify.
FACTS = [
    ("Messiah opens ~12 years after Paul takes the throne", "O", "Dune Messiah, opening chapters"),
    ("Paul's tally: ~61 billion dead, 90 planets sterilized, ~500 demoralized; comparison with ancient tyrants", "O", "Dune Messiah, Paul–Korba conversation [VERIFY speaker/context]"),
    ("Conspiracy meets on Wallach IX: Mohiam, Edric, Scytale, Irulan", "O", "Dune Messiah ch. 1"),
    ("Navigator presence clouds Paul's prescience", "O", "Dune Messiah"),
    ("Irulan secretly gives Chani contraceptives", "O", "Dune Messiah"),
    ("Hayt = Duncan Idaho ghola, metal eyes, Mentat/Zensunni training, given via Edric", "O", "Dune Messiah"),
    ("Lichna is dead; Scytale impersonates her", "O", "Dune Messiah"),
    ("Otheym gives Paul the dwarf Bijaz, who holds traitors' names", "O", "Dune Messiah"),
    ("Stone burner blinds Paul; forbidden atomic weapon", "O", "Dune Messiah"),
    ("Fremen custom abandons the blind to the desert", "O", "Dune Messiah"),
    ("Paul foresaw one daughter; twins Leto II and Ghanima born at Sietch Tabr; Chani dies", "O", "Dune Messiah, final chapters"),
    ("Chani's death triggers Hayt's conditioning; Duncan's memories return", "O", "Dune Messiah"),
    ("Scytale offers a Chani ghola; terms [VERIFY exact terms]", "O", "Dune Messiah"),
    ("Paul sees through infant Leto's eyes and kills Scytale with a thrown knife", "O", "Dune Messiah"),
    ("Paul walks into the desert; Alia regent; Duncan with Alia; Irulan devotes herself to the twins", "O", "Dune Messiah, ending"),
    ("Part Two: Chani rejects the holy war and leaves Paul", "F", "Dune: Part Two (2024)"),
    ("Films compress the timeline; Alia unborn in Part Two", "F", "Dune (2021), Dune: Part Two (2024)"),
    ("Part Three release 18 Dec 2026; adapts Messiah", "F", "studio release schedule (re-check before publish)"),
    ("Herbert on the dangers of charismatic leaders / the superhero", "O", "Frank Herbert, 'Dune Genesis', OMNI, July 1980 — paraphrase only"),
    ("Duncan dies holding off Sardaukar while Paul and Jessica escape (Paul does not witness the death)", "O", "Dune (1965) Book I"),
    ("Messiah received a mixed reaction from some readers of Dune", "O", "secondary: publication history / reviews [VERIFY]"),
    ("Preacher (Children of Dune); Leto II's 3,500-year path (God Emperor)", "O", "Children of Dune (1976); God Emperor of Dune (1981)"),
]
