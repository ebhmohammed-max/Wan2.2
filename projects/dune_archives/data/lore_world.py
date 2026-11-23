"""PLANETS, TECHNOLOGY, ECOLOGY / RELIGION / PHILOSOPHY — THE DUNE ARCHIVES.
Geography rule: Herbert published an Arrakis polar map (Dune appendix) but NO
interstellar coordinates. All galaxy-scale maps are CREATIVE RECONSTRUCTION.
"""
from lore_timeline import OFH, EDU, FILM, TV, SHARED, ADAPT, RECON

# (name, label, type/climate, established facts, reconstruction latitude, visual brief, doc potential)
PLANETS = [
    ("Arrakis / Dune / Rakis", OFH, "Desert world; no open water; sole natural spice source (until Rakis' destruction)",
     "Arrakeen, Carthag, the Shield Wall, the Great Flat, polar ice cap, sietches (Tabr), Habbanya ridge, Funeral Plain; two moons; sandworms; Coriolis storms; greened under Leto II except the Sareer; destroyed by Honored Matres (Heretics)",
     "Exact dune heights, city layouts, sietch interiors = RECONSTRUCTION. Appendix map positions approximate.",
     "Ochre-to-bone sand; white-hot sky; heat shimmer; deep blue shadows; spice-blow cinnamon haze", 10),
    ("Caladan", OFH, "Ocean world, temperate", "Atreides homeworld; seas, cliffs, pundi rice", "Castle architecture = RECON",
     "Grey-green seas, rain, granite cliffs, warm interiors", 7),
    ("Giedi Prime / Gammu", OFH, "Industrial Harkonnen world; renamed Gammu by Heretics era", "Harkonnen capital; later Gammu where the Duncan ghola is raised",
     "Sun colour and architecture = RECON (Part Two's black sun is FILM ADAPTATION — do not copy)", "Oily industrial dark, sodium-orange light, blue griffin", 7),
    ("Kaitain", OFH, "Imperial capital", "Seat of the Padishah Emperors at the time of Dune", "Palace scale/design = RECON", "Gold, marble, gardens, controlled weather", 6),
    ("Salusa Secundus", OFH, "Hell-world prison planet", "Original Corrino world; Sardaukar trained here; Shaddam's exile; (EU) devastated by atomics", "Landscapes = RECON", "Scorched ruins, storms, prison camps", 7),
    ("Ix", OFH, "Machine culture world", "Ixian technology; no-ships; Hwi Noree", "EU: underground cities beneath the surface", "Clean metallic caverns, cold blue light", 7),
    ("Tleilax (Thalim)", OFH, "Bene Tleilax homeworld", "Axlotl tanks (revealed in Heretics/Chapterhouse); Bandalong city (Heretics)", "City design = RECON", "Sterile, labyrinthine, secretive", 7),
    ("Wallach IX", OFH, "Bene Gesserit school world", "Mother School of the Bene Gesserit in Dune era", "Architecture = RECON", "Austere halls, blue twilight", 6),
    ("Chapterhouse", OFH, "Bene Gesserit secret homeworld (late era)", "Deliberately desertified to host sandworms (Chapterhouse: Dune)", "Landscapes = RECON", "Orchards giving way to sand", 6),
    ("Junction", OFH, "Guild planet → Honored Matre base", "Site of Odrade's death and Murbella's ascension", "", "", 5),
    ("Ecaz", SHARED, "Jungle/botanical world", "Fogwood; Ecazi sculptors (ORIGINAL mentions [VERIFY])", "House Ecaz detail EU", "Mist forests", 4),
    ("Richese", OFH, "Machine culture", "Rival to Ix (ORIGINAL mention)", "", "", 3),
    ("Ginaz", SHARED, "Archipelago (EU)", "Swordmasters of Ginaz", "Islands = EU", "", 4),
    ("Lampadas", OFH, "Bene Gesserit library world", "Destroyed by Honored Matres (Chapterhouse); Rebecca and the Lampadas horde", "", "", 5),
    ("Corrin", EDU, "Omnius's capital world (red giant star)", "Battle of Corrin (88 BG) is ORIGINAL as a battle; the machine world is EU", "", "Red giant sun", 6),
    ("Rossak", EDU, "Toxic jungle world (EU)", "Sorceresses; Sisterhood origin (EU)", "", "", 5),
    ("Poritrin", SHARED, "Zensunni slave world (EU detail)", "Named in Zensunni migrations (ORIGINAL); Holtzman/slave revolt detail EU", "", "", 4),
    ("Old Terra (Earth)", OFH, "Humanity's origin", "Referenced obliquely (Zensunni, Agamemnon descent)", "Any depiction = RECON", "Fragmentary ruins only", 6),
]

# (name, label, description, rules/limits, visual brief)
TECH = [
    ("Holtzman shield", OFH, "Personal and house-scale force fields that stop fast projectiles; slow blades penetrate.", "Shields enrage sandworms; lasgun + shield = pseudo-atomic explosion", "Faint blue-shimmer membrane (RECON look)"),
    ("Lasgun", OFH, "Continuous-wave laser weapon.", "Interaction with shields is catastrophic for both", "Thin incandescent beam"),
    ("Holtzman engine / foldspace", OFH, "Space-folding drive navigated by spice-prescient Guild navigators.", "Without navigators, folding is lethal (EU dramatises)", "Heighliner holds; no visible motion"),
    ("Heighliner", OFH, "Guild super-carrier holding frigates of many Houses.", "Scale: book describes vast holds [VERIFY dimension claims]", "Immense, featureless; scale cues essential"),
    ("Ornithopter", OFH, "Wing-flapping aircraft of Arrakis.", "Book: flapping wings; films use dragonfly-like designs (FILM — do not copy)", "Original insect-avian design for the channel"),
    ("Carryall", OFH, "Heavy lifter that rescues spice harvesters from worms.", "", "Large ribbed lifter"),
    ("Spice harvester / factory", OFH, "Mobile mining crawler.", "Worm-sign warnings; carryall extraction", "Massive tracked machine in dust"),
    ("Stillsuit", OFH, "Fremen body-water recycling suit.", "Loses a thimble of water a day if well made (book) [VERIFY wording]", "Layered, filter tubes, nose plugs"),
    ("Thumper", OFH, "Stake that drums the sand to summon a worm.", "", "Simple spring-driven stake"),
    ("Maker hooks", OFH, "Hooks used to ride sandworms by prying open ring segments.", "", ""),
    ("Crysknife", OFH, "Sacred blade made from a sandworm tooth.", "Must be fixed or kept in contact with a body or it disintegrates (book)", "Milky-white curved blade"),
    ("Hunter-seeker", OFH, "Suspensor-borne assassination needle guided by an operator.", "", "Tiny metallic sliver"),
    ("Poison snooper", OFH, "Detector for poisons in food.", "", ""),
    ("Glowglobe", OFH, "Suspensor-floated light.", "", "Floating amber orbs"),
    ("Suspensor", OFH, "Anti-gravity field (Holtzman).", "Baron's belts", ""),
    ("Stone burner", OFH, "Atomic weapon that blinds those who see it.", "Used against Paul (Messiah)", "Blinding white flash"),
    ("Family atomics", OFH, "Great House arsenals; banned against humans by the Great Convention.", "Paul blasts the Shield Wall", "Restrained depiction"),
    ("Gom jabbar", OFH, "Poison needle used in the Bene Gesserit humanity test.", "", "Needle on a fingertip"),
    ("Axlotl tanks", OFH, "Tleilaxu biological 'tanks' for gholas and spice production.", "Their nature is revealed late (Chapterhouse) — sensitive; handle tastefully", "Never graphic"),
    ("Gholas", OFH, "Cloned individuals grown from cells; memory restorable (Hayt).", "", ""),
    ("Face Dancers", OFH, "Tleilaxu shape-shifters.", "", "Morph sequences"),
    ("No-ship / no-chamber", OFH, "Ixian devices invisible to prescience.", "God Emperor/Heretics era", "Distortion field look (RECON)"),
    ("T-probe", OFH, "Ixian mind-probe.", "Heretics era", ""),
    ("Solido projector", OFH, "3D holographic projector.", "", ""),
    ("Weirding modules", ADAPT, "Sound-amplifying weapons.", "1984 FILM ONLY — not in the books", "Do not use as canon"),
    ("Thinking machines / cymeks", EDU, "Robots and human-brained machine bodies.", "EU only", ""),
]

# (topic, label, summary, documentary angle)
ECO_RELIGION = [
    ("Spice (melange) life cycle", OFH, "Sandtrout → sandworm cycle; pre-spice mass; spice blow. Sandtrout encapsulate water, making Arrakis a desert.", "The ecology that made an empire — and the twist that the worms made the desert"),
    ("Sandworms (Shai-Hulud)", OFH, "Giant worms; drawn to rhythm and shields; water poison to them; source of crysknives and Water of Life.", "Size claims vary — book cites up to ~400 m [VERIFY]"),
    ("Water of Life", OFH, "Bile of a drowned young worm; a Reverend Mother converts it; deadly to most men.", "Paul's transformation"),
    ("Terraforming plan", OFH, "Pardot & Liet-Kynes' multi-century plan to green Arrakis.", "Fulfilled under Leto II, destroying the worms' habitat"),
    ("Fremen water discipline", OFH, "Deathstills reclaim bodies' water; water rings as currency; tears as gift.", ""),
    ("Orange Catholic Bible", OFH, "Ecumenical scripture produced after the Jihad by the C.E.T. (Commission of Ecumenical Translators).", "Appendix II context"),
    ("Butlerian commandment", OFH, "Prohibition on machines in the likeness of a human mind.", "Quote verbatim only"),
    ("Zensunni / Zenshiite", OFH, "Religious lineages of the Fremen ancestors.", ""),
    ("Missionaria Protectiva", OFH, "Bene Gesserit seeding of protective myths across worlds — Paul exploits it.", "The engineered messiah"),
    ("Litany Against Fear", OFH, "Bene Gesserit litany beginning 'I must not fear. Fear is the mind-killer.'", "Quote verified opening only"),
    ("Kwisatz Haderach", OFH, "Male Bene Gesserit able to see where they cannot; 'shortening of the way'.", ""),
    ("Other Memory", OFH, "Ancestral memories of Reverend Mothers and the pre-born.", "Abomination danger"),
    ("Golden Path", OFH, "Leto II's plan to save humanity from extinction through enforced peace and the Scattering.", "Flagship philosophical topic"),
    ("Cult of Muad'Dib / Qizarate", OFH, "Religion and bureaucracy built on Paul.", "Herbert's warning about charismatic leaders"),
    ("Herbert's 'superhero' warning", SHARED, "Herbert stated in interviews that Paul is a warning about charismatic leaders.", "Quote only from a verified interview transcript"),
    ("'The spice must flow'", ADAPT, "Famous line from the 1984 film — not in the 1965 novel's text.", "Myth-busting episode"),
    ("Ecology of the Sareer", OFH, "The last desert preserved by Leto II.", ""),
    ("Kralizec", OFH, "Typhoon struggle / end-of-universe battle prophecy.", "EU resolves in Sandworms"),
]
