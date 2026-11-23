"""MASTER HISTORICAL TIMELINE — THE DUNE ARCHIVES.

Each row: (sort_key, date_label, event, continuity_label, source, confidence, doc_notes)
continuity_label vocabulary (never merge):
  ORIGINAL FRANK HERBERT CANON | EXPANDED DUNE UNIVERSE | FILM ADAPTATION |
  TELEVISION ADAPTATION | SHARED OR OVERLAPPING CONTINUITY |
  ADAPTATION-SPECIFIC INTERPRETATION | FAN THEORY | CREATIVE RECONSTRUCTION
confidence: HIGH (well attested in source) / MEDIUM (attested, exact figure to verify
against text before scripting) / LOW (secondary sources disagree).
Dates: BG = Before Guild, AG = After Guild (Spacing Guild calendar).
Any Gregorian conversion is FAN THEORY / CREATIVE RECONSTRUCTION.
"""

OFH, EDU, FILM, TV, SHARED, ADAPT, FAN, RECON = (
    "ORIGINAL FRANK HERBERT CANON", "EXPANDED DUNE UNIVERSE", "FILM ADAPTATION",
    "TELEVISION ADAPTATION", "SHARED OR OVERLAPPING CONTINUITY",
    "ADAPTATION-SPECIFIC INTERPRETATION", "FAN THEORY", "CREATIVE RECONSTRUCTION")

TIMELINE = [
    # ---------------- DEEP PAST ----------------
    (-20000, "Remote antiquity", "Old Terra (Earth) is humanity's origin world; references survive only as fragments in Imperial culture (e.g. place-names, Zensunni migration lore).", OFH, "Dune appendices; God Emperor of Dune", "HIGH", "Use only as fragmentary 'lost Earth' imagery; never depict a specific Earth city as canon."),
    (-19000, "Undated, before the Jihad", "Zensunni Wanderers migrate across many worlds (Poritrin, Bela Tegeuse, Salusa Secundus, etc. named in appendix lore) before reaching Arrakis — ancestors of the Fremen.", OFH, "Dune, Appendix II (Religion of Dune) / Terminology", "MEDIUM", "Order and number of migration stops: verify against the appendix before scripting."),
    (-15000, "Thousands of years BG", "Thinking machines become central to human civilisation; humans grow dependent on them.", SHARED, "Implied in Dune (Butlerian Jihad entry); dramatised in Legends of Dune", "HIGH", "Herbert gives the dependence, not the machine empire."),
    (-1100, "c. 1,000+ years BG", "Rise of the Old Empire and Titans / cymeks; Omnius evermind conquers the Synchronized Worlds.", EDU, "Legends of Dune: The Butlerian Jihad (2002)", "HIGH", "Pure EU. Never present Omnius/Erasmus/cymeks as Frank Herbert canon."),
    (-201, "201 BG", "Butlerian Jihad begins — a crusade against computers, thinking machines and conscious robots.", OFH, "Dune, Terminology of the Imperium ('BUTLERIAN JIHAD')", "HIGH", "Core date is Herbert's. HOW it began differs by continuity (see next rows)."),
    (-201.1, "201 BG", "EU trigger: Serena Butler's infant son is killed by the robot Erasmus, igniting the holy war.", EDU, "Legends of Dune: The Butlerian Jihad", "HIGH", "Contrast with Herbert's framing (human moral revolt) and the Dune Encyclopedia's Jehanne Butler (estate-ruled non-canon)."),
    (-201.2, "1984 reference work", "Dune Encyclopedia (ed. Willis McNelly) presents Jehanne Butler as the Jihad's figurehead; later superseded and declared non-canon by the Herbert estate.", FAN, "The Dune Encyclopedia (1984)", "HIGH", "Label as NON-CANON REFERENCE (treated under FAN THEORY bucket for safety). Great 'three versions of one war' segment."),
    (-108, "108 BG", "Butlerian Jihad concludes. The commandment against machines 'in the likeness of a human mind' enters the Orange Catholic Bible tradition.", OFH, "Dune, Terminology; Chapterhouse references", "HIGH", "Quote the commandment ONLY verbatim from a checked edition."),
    (-108.5, "After the Jihad", "Human-computer disciplines arise to replace machines: Mentats, Bene Gesserit, Spacing Guild navigators (spice-driven).", OFH, "Dune (Appendix / Terminology)", "HIGH", "EU dramatises founders (Gilbertus Albans, Raquella, Norma Cenva)."),
    (-88, "88 BG", "Battle of Corrin near Sigma Draconis: the ruling house from Salusa Secundus takes the name Corrino.", OFH, "Dune, Terminology ('CORRIN, BATTLE OF')", "HIGH", "EU (The Battle of Corrin, 2004) adds Abulurd Harkonnen's disgrace and the Atreides-Harkonnen feud's origin."),
    (-88.5, "88 BG", "Origin of the Atreides–Harkonnen feud: a Harkonnen is branded a coward after Corrin (EU dramatisation: Abulurd Harkonnen and Vorian Atreides).", EDU, "Legends of Dune: The Battle of Corrin", "HIGH", "Herbert states an ancient feud; the specific Abulurd story is EU."),
    (-83, "c. 80s BG", "Founding era of the Sisterhood at Rossak; Raquella Berto-Anirul becomes the first Reverend Mother (EU).", EDU, "Legends of Dune / Sisterhood of Dune", "HIGH", ""),
    (-82, "c. 10,000 years before Paul", "Dune: Prophecy — Valya and Tula Harkonnen lead the early Sisterhood; Desmond Hart appears at the Imperial court of Javicco Corrino.", TV, "Dune: Prophecy S1 (HBO, Nov 2024)", "HIGH", "TV chronology and characterisation diverge from Sisterhood of Dune; keep separate rows. Prophecy S2 expected late 2026."),
    (0, "0 / 1 AG", "Spacing Guild monopoly on space travel; Guild calendar begins (AG).", OFH, "Dune (dating convention)", "HIGH", "EU attributes foldspace and navigators to Norma Cenva and the Venport family."),
    (97, "c. 1st century AG", "Great Convention establishes the rules of war, including the ban on atomics against humans and the Landsraad/Guild/Emperor balance.", SHARED, "Concept: Dune; date: EU/secondary", "MEDIUM", "Treat the date as EU/secondary unless verified."),
    (1000, "Undated millennia", "Imperium of the Corrino Padishah Emperors (81 emperors up to Shaddam IV) with Sardaukar trained on Salusa Secundus.", OFH, "Dune", "HIGH", "'Shaddam IV, 81st Padishah Emperor' — verify ordinal in edition."),
    (9900, "Undated", "Bene Gesserit breeding program aims to produce the Kwisatz Haderach.", OFH, "Dune", "HIGH", ""),
    (10111, "c. 10111 AG", "Harkonnens receive Arrakis fief (quasi-fief stewardship for spice).", EDU, "Secondary/EU timelines", "LOW", "Original states roughly 80 years of Harkonnen rule; exact year is EU/secondary."),
    (10140, "c. 10140 AG", "Leto Atreides I born (EU dating).", EDU, "Prelude to Dune", "MEDIUM", ""),
    (10154, "10154 AG", "Jessica born (EU dating); daughter of Baron Vladimir Harkonnen and Gaius Helen Mohiam (EU detail).", EDU, "Prelude to Dune", "MEDIUM", "Herbert: Jessica is the Baron's daughter (Dune). Mohiam as mother = EU."),
    (10156, "10156 AG", "Shaddam IV becomes Padishah Emperor (EU: after Elrood IX's poisoning).", EDU, "Prelude to Dune: House Corrino era", "MEDIUM", ""),
    (10175, "10175 AG", "Paul Atreides born on Caladan to Duke Leto I and Lady Jessica, who defied orders to bear a daughter.", OFH, "Dune (age 15 at story start)", "HIGH", ""),
    (10176, "c. 10170s AG", "EU: Ix falls to the Bene Tleilax; House Vernius exiled (Prelude trilogy).", EDU, "Prelude to Dune: House Atreides", "MEDIUM", ""),
    (10191, "10191 AG", "House Atreides takes Arrakis. Gom jabbar test. Harkonnen-Sardaukar attack; Duke Leto dies; Paul and Jessica flee to the Fremen.", OFH, "Dune (Book I-II)", "HIGH", "Film: Part One (2021) ends with Paul joining the Fremen. 1984 film compresses events."),
    (10191.5, "10191 AG", "Paul kills Jamis; joins Sietch Tabr as Usul / Muad'Dib. Jessica becomes Reverend Mother; Alia is 'pre-born' in the womb.", OFH, "Dune (Book II)", "HIGH", "Villeneuve Part Two: Alia remains unborn throughout (ADAPTATION-SPECIFIC INTERPRETATION)."),
    (10193, "c. 10193 AG", "Paul drinks the Water of Life, unites Fremen, rides sandworms against Shaddam IV at Arrakeen; kills Feyd-Rautha; takes the throne by marrying Irulan.", OFH, "Dune (Book III)", "HIGH", "Book: Alia kills the Baron; Part Two: Paul kills the Baron. 1984: rain falls on Arrakis. Never merge."),
    (10194, "10193–10205 AG", "Muad'Dib's Jihad: Fremen legions conquer the Imperium in Paul's name.", OFH, "Dune Messiah", "HIGH", "Casualty figures stated by Paul in Messiah (dozens of billions; ninety planets sterilised) — verify exact wording before quoting."),
    (10195, "10193–10205 AG (EU interquel)", "Paul of Dune / Winds of Dune fill the Jihad years.", EDU, "Paul of Dune (2008), Winds of Dune (2009)", "HIGH", ""),
    (10205, "c. 10205–10207 AG", "Dune Messiah: conspiracy of Mohiam, Edric, Scytale and Irulan. Hayt (Duncan ghola) given to Paul. Stone burner blinds Paul. Chani dies bearing twins Leto II and Ghanima. Paul walks into the desert.", OFH, "Dune Messiah (1969)", "HIGH", "Adapted by Dune: Part Three (release 18 Dec 2026). Expect film deviations — log them after release."),
    (10216, "c. 10216–10219 AG", "Children of Dune: the Preacher; Alia's possession by the Baron (Abomination); Leto II dons the sandtrout skin and begins his metamorphosis; Paul is killed; Alia leaps to her death.", OFH, "Children of Dune (1976)", "HIGH", "Sci-Fi Channel miniseries 'Children of Dune' (2003) = TELEVISION ADAPTATION."),
    (10219, "10219 AG", "Leto II assumes the throne; the Golden Path begins.", OFH, "Children of Dune", "HIGH", ""),
    (10225, "10225 AG", "Count Hasimir Fenring dies (EU/secondary date).", EDU, "Secondary timelines", "LOW", ""),
    (10256, "10256 AG", "Lady Jessica dies (EU/secondary date).", EDU, "Secondary timelines", "LOW", ""),
    (12000, "10219–13725 AG", "Leto's Peace: ~3,500-year reign. Fish Speakers army; Duncan Idaho gholas; spice hoard; Arrakis largely greened except the Sareer.", OFH, "God Emperor of Dune (1981)", "HIGH", ""),
    (13724, "c. 13724 AG", "Siona Atreides, invisible to prescience, joins Leto's design; Hwi Noree of Ix; Duncan and Siona plot the assassination.", OFH, "God Emperor of Dune", "HIGH", ""),
    (13725, "c. 13725 AG", "Leto II dies when his cart falls from a bridge into the Idaho River during the procession to his wedding; his body splits into sandtrout. Famine Times and the Scattering follow.", OFH, "God Emperor of Dune", "HIGH", "Exact year computed from the ~3,500-year reign — verify before on-screen dating."),
    (14500, "Famine Times → Scattering", "Humanity disperses beyond the Old Empire into the unknown — the outcome of the Golden Path.", OFH, "Heretics of Dune (backstory)", "HIGH", ""),
    (15200, "c. 1,500 years after Leto II", "Heretics of Dune: Honored Matres return from the Scattering; Sheeana commands worms on Rakis; Bashar Miles Teg; Duncan ghola awakened.", OFH, "Heretics of Dune (1984)", "HIGH", ""),
    (15229, "c. 15229 AG", "Honored Matres destroy Rakis; Miles Teg dies; a single worm is carried off-world by the Bene Gesserit.", OFH, "Heretics of Dune", "MEDIUM", "AG year from secondary timelines; the event itself is HIGH confidence."),
    (15240, "Shortly after Rakis", "Chapterhouse: Dune — Chapterhouse planet desertified; Odrade dies; Murbella unites Bene Gesserit and Honored Matres; Duncan, Sheeana and others escape on a no-ship.", OFH, "Chapterhouse: Dune (1985)", "HIGH", "Frank Herbert's final novel; ends on a cliffhanger (Daniel and Marty)."),
    (15260, "Following Chapterhouse", "Hunters of Dune / Sandworms of Dune: the enemy is revealed as Omnius and Erasmus; Kralizec; resolution of the no-ship's journey.", EDU, "Hunters of Dune (2006), Sandworms of Dune (2007)", "HIGH", "EU authors state these are based on Frank Herbert's 'Dune 7' outline; the outline itself is not published in full — treat attribution claims as EU."),
    # ---------------- REAL-WORLD PUBLICATION & ADAPTATION TIMELINE ----------------
    (90001, "1965", "Dune published (serialised in Analog 1963–65).", OFH, "Publication history", "HIGH", "Real-world chronology rows (90000+) support 'making of' topics."),
    (90002, "1969", "Dune Messiah published.", OFH, "Publication history", "HIGH", ""),
    (90003, "1970s", "Alejandro Jodorowsky's unmade adaptation (documentary 'Jodorowsky's Dune', 2013).", FILM, "Film history", "HIGH", "Unmade — present as history, not continuity."),
    (90004, "1976", "Children of Dune published.", OFH, "Publication history", "HIGH", ""),
    (90005, "1981", "God Emperor of Dune published.", OFH, "Publication history", "HIGH", ""),
    (90006, "1984", "Heretics of Dune published; David Lynch's Dune film released; Dune Encyclopedia published.", SHARED, "Publication / film history", "HIGH", ""),
    (90007, "1985", "Chapterhouse: Dune published.", OFH, "Publication history", "HIGH", ""),
    (90008, "11 Feb 1986", "Frank Herbert dies.", OFH, "Biography", "HIGH", ""),
    (90009, "1992", "Dune II video game (Westwood) introduces House Ordos and popularises RTS.", ADAPT, "Game history", "HIGH", "House Ordos is game-only."),
    (90010, "1999–2001", "Prelude to Dune trilogy (Brian Herbert & Kevin J. Anderson).", EDU, "Publication history", "HIGH", ""),
    (90011, "2000 / 2003", "Sci-Fi Channel miniseries: Frank Herbert's Dune (2000) and Children of Dune (2003).", TV, "TV history", "HIGH", ""),
    (90012, "2002–2004", "Legends of Dune trilogy (Butlerian Jihad era).", EDU, "Publication history", "HIGH", ""),
    (90013, "2006–2007", "Hunters of Dune; Sandworms of Dune.", EDU, "Publication history", "HIGH", ""),
    (90014, "2012–2016", "Great Schools of Dune trilogy (Sisterhood, Mentats, Navigators).", EDU, "Publication history", "HIGH", ""),
    (90015, "2020–2022", "Caladan trilogy (Duke, Lady, Heir of Caladan).", EDU, "Publication history", "HIGH", ""),
    (90016, "Oct 2021", "Dune (Denis Villeneuve) — adapts roughly the first half of the novel.", FILM, "Film history", "HIGH", ""),
    (90017, "Mar 2024", "Dune: Part Two released.", FILM, "Film history", "HIGH", ""),
    (90018, "17 Nov 2024", "Dune: Prophecy S1 premieres on HBO (6 episodes).", TV, "TV history", "HIGH", ""),
    (90019, "18 Dec 2026", "Dune: Part Three (adapting Dune Messiah) scheduled for release.", FILM, "movieinsider / trade reports (2026)", "HIGH", "25 days after this report — strongest timeliness window."),
    (90020, "Late 2026 (TBC)", "Dune: Prophecy S2 (8 episodes) expected on HBO/Max; no firm date at time of writing.", TV, "projectcasting / collider (2026)", "MEDIUM", ""),
]
