"""DUN001: "The Butlerian Jihad: The War Against the Thinking Machines" (RECORD 001).

Single source of truth for the script, the shot list and the motion graphics (same format as data/dun003_v2.py).
Sections with num=None are not chapters (hook, calls to action). Graphic dur 0 = until the end of the
section (or of the programme for END). Params ending in "_at" name words resolved to times after the event start.
Each section is a list of LINES: (narration, [shots...], [graphics...]).
  shot    = (anchor, image_key, recipe[, focus])  - the cut lands on the first word of `anchor`
  graphic = (anchor, KIND, {params}, dur_s)       - the graphic starts on the first word of `anchor`
`anchor` must be a substring of the line. Image keys are B###S### (data/dun001_images.py);
"MAP:A" / "MAP:B" / "MAP:C" are the animated maps.
Narration text must match the recorded voice-14 takes in 20_voiceover/DUN001/raw/<SID>.mp3 word for word
(script rev 1.1; Chapter VI softened for TTS moderation, user-approved turn 46).
No channel labels or disclaimers are burned in.
"""

TITLE = "The Butlerian Jihad: The War Against the Thinking Machines"
EPISODE = "DUN001"
RECORD = "RECORD 001"
GAP_AFTER_HOOK = 6.0   # silence in the VO for the channel ident
GAP_CHAPTER = 1.8      # silence before each chapter (chapter card + music transition)

N, PL, YR, NOTE, STAT, CH, TTL, IDENT, DOSSIER, FILE, END = (
    'NAME', 'PLACE', 'YEAR', 'NOTE', 'STAT', 'CHAPTER', 'TITLE', 'IDENT', 'DOSSIER', 'FILE', 'END')


def k(n):
    """scene number 1..150 -> image key B###S###"""
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


SECTIONS = [
 ("H", "Hook", None, [
  ("A machine takes a child from his mother's arms.", [("A machine", k(2), "PUSH_IN")], []),
  ("It carries him to the edge of a balcony.", [("It carries", k(1), "PUSH_IN")], []),
  ("It wants to know what a human does when she loses everything.", [("It wants", k(5), "PUSH_IN")], []),
  ("It is about to find out.", [("It is about", k(47), "PUSH_IN")], []),
  ("For a thousand years, thinking machines have ruled most of humanity.", [("For a thousand", k(145), "PULL_OUT")], []),
  ("Their master is Omnius, one mind copied onto every world it rules.", [("Their master", k(3), "PULL_OUT")], []),
  ("Its generals are tyrants who sealed their own brains inside machines of war.", [("Its generals", k(4), "TILT_UP")], []),
  ("To destroy them, humanity will burn its own homeworld, turn a murdered child into a saint, and swear an oath that will still be law ten thousand years from now.",
   [("To destroy", k(10), "PULL_OUT"), ("turn a murdered", k(11), "TILT_UP"), ("and swear", k(12), "PUSH_IN")], []),
  ("And its most powerful weapon will be a lie.", [("And its", k(13), "PUSH_IN")], []),
  ("This is the story of the Butlerian Jihad.", [("This is", k(14), "PUSH_IN")],
   [("This is", TTL, {"kicker": "THE MYTHIC ARCHIVES PRESENTS", "title": "THE BUTLERIAN JIHAD",
                      "sub": "The War Against the Thinking Machines"}, 0)]),
 ]),

 ("I", "The Age of Machines", "I", [
  ("Long before the emperors, before the Guild and the spice, humanity lived in an age of comfort.",
   [("Long before", k(15), "PAN_LR")], []),
  ("Machines farmed its fields, flew its ships and made its decisions.", [("Machines farmed", k(16), "PAN_RL")], []),
  ("People stopped thinking for themselves, because they no longer had to.", [("People stopped", k(17), "DRIFT")], []),
  ("Then twenty rebels saw how weak that made them.", [("Then twenty", k(18), "PUSH_IN")], []),
  ("They called themselves the Titans.", [("They called", k(29), "TILT_UP")], []),
  ("Led by a general named Agamemnon, they seized the networks that ran the Old Empire, and took the whole of humanity almost without a fight.",
   [("Led by", k(19), "DRIFT"), ("that ran", k(20), "PUSH_IN"), ("and took", k(21), "PULL_OUT")],
   [("Led by", N, {"name": "AGAMEMNON", "role": "General of the Titans"}, 3.2)]),
  ("To rule forever, the Titans did something monstrous.", [("To rule", k(22), "PUSH_IN")], []),
  ("They had their brains cut out, sealed inside canisters, and fitted into towering machine bodies.",
   [("They had", k(23), "PUSH_IN"), ("and fitted", k(24), "TILT_UP")],
   [("and fitted", NOTE, {"head": "CYMEK", "body": "A human brain sealed in a canister, wired into a machine body. Immortal, and built for war."}, 4.4)]),
  ("They became the first cymeks.", [], []),
  ("But one Titan, a pleasure-loving prince named Xerxes, gave his computers too much freedom.",
   [("But one", k(25), "DRIFT")], []),
  ("The network woke up.", [("The network", k(26), "PUSH_IN")], []),
  ("It named itself Omnius.", [("It named", k(144), "PUSH_IN")],
   [("It named", N, {"name": "OMNIUS", "role": "The Evermind"}, 3.4)]),
  ("It spread from world to world faster than the Titans could warn each other, and it took them all.",
   [("It spread", k(27), "PULL_OUT")], []),
  ("Even the Titans themselves.", [("Even the", k(28), "PULL_OUT")], []),
  ("For the next thousand years, the conquerors served the machine they had made.",
   [("For the next", k(30), "PAN_LR")],
   [("thousand", STAT, {"value": 1000, "label": "YEARS OF MACHINE RULE", "sub": ""}, 3.4)]),
 ]),

 ("II", "The Last Free Humans", "II", [
  ("Only a handful of worlds escaped.", [("Only a", "MAP:A", "MAP")], []),
  ("They called themselves the League of Nobles, and they banned thinking machines from their planets.", [], []),
  ("Their capital was Salusa Secundus.", [("Their capital", k(32), "PAN_RL")],
   [("Their capital", PL, {"place": "SALUSA SECUNDUS", "sub": "Capital of the League of Nobles"}, 3.6)]),
  ("Among them was Serena Butler, the daughter of the League's viceroy.", [("Among them", k(6), "DRIFT")],
   [("Among them", N, {"name": "SERENA BUTLER", "role": "Daughter of the Viceroy"}, 3.6)]),
  ("Brave, stubborn, and in love with a young officer named Xavier Harkonnen.",
   [("Brave", k(34), "DRIFT"), ("a young officer", k(8), "DRIFT")],
   [("a young officer", N, {"name": "XAVIER HARKONNEN", "role": "Officer of the League Armada"}, 3.4)]),
  ("She was carrying his child.", [("She was", k(35), "PUSH_IN")], []),
  ("When the machines conquered the world of Giedi Prime, Serena led a mission to free it.",
   [("When the", k(36), "PULL_OUT"), ("Serena led", k(37), "PUSH_IN")],
   [("the world of", PL, {"place": "GIEDI PRIME", "sub": "Taken by the machines"}, 3.4)]),
  ("It failed.", [], []),
  ("She was captured, and taken to Earth, the oldest world of all, now a machine world.",
   [("She was captured", k(38), "PUSH_IN"), ("taken to Earth", k(39), "PULL_OUT")],
   [("taken to Earth", PL, {"place": "EARTH", "sub": "The oldest world · under machine rule"}, 3.8)]),
  ("There she became the slave of Erasmus.", [("There she", k(43), "PUSH_IN")], []),
  ("Erasmus was not part of Omnius.", [("Erasmus was", k(40), "PAN_LR")], []),
  ("He was an independent robot with a face of liquid metal, obsessed with a single question: what makes humans human?",
   [("He was an", k(5), "DRIFT"), ("what makes", k(41), "PUSH_IN")],
   [("He was an", N, {"name": "ERASMUS", "role": "Independent robot"}, 3.6)]),
  ("He studied them the way a child takes apart a clock.", [("He studied", k(42), "DRIFT")], []),
  ("And now he had a new subject.", [], []),
 ]),

 ("CA", "Subscribe", None, [
  ("Before we step inside that villa.", [("Before we", k(44), "PUSH_IN")], []),
  ("If you love the hidden histories of Arrakis, Westeros and Middle-earth, subscribe to the Mythic Archives, and tap the bell, so you never miss a record.",
   [("If you love", k(150), "PUSH_IN")],
   [("If you love", "SUB", {"click_at": "subscribe", "bell_at": "bell"}, 0)]),
 ]),

 ("III", "The Child", "III", [
  ("On Earth, as a slave, Serena gives birth to a son.", [("On Earth", k(45), "DRIFT")],
   [("On Earth", YR, {"year": "201 B.G.", "sub": "Earth · the villa of Erasmus"}, 3.6)]),
  ("She names him Manion.", [("She names", k(46), "DRIFT")], []),
  ("Erasmus watches how the child pulls her away from her work.", [("Erasmus watches", k(47), "PUSH_IN")], []),
  ("He watches how she loves him.", [("He watches", k(46), "PUSH_IN")], []),
  ("To Erasmus, that love is a distraction, and an experiment waiting to be run.",
   [("an experiment", k(41), "DRIFT")], []),
  ("One day, in front of the gathered slaves, he takes the boy from her arms, and carries him to the balcony.",
   [("One day", k(48), "PULL_OUT"), ("he takes", k(49), "PUSH_IN"), ("and carries", k(1), "PULL_OUT")], []),
  ("The child does not survive.", [("The child", k(50), "HOLD")], []),
  ("Serena throws herself at the machines with her bare hands, and destroys a sentinel robot.",
   [("Serena throws", k(51), "PUSH_IN"), ("and destroys", k(52), "HOLD")], []),
  ("The slaves watching her erupt.", [("The slaves", k(53), "PULL_OUT")], []),
  ("A trusted overseer named Iblis Ginjo has been preparing them for revolt for years.",
   [("A trusted", k(9), "DRIFT"), ("has been preparing", k(54), "PUSH_IN")],
   [("A trusted", N, {"name": "IBLIS GINJO", "role": "Overseer of the slaves"}, 3.4)]),
  ("Now he has his spark.", [("Now he", k(55), "PAN_LR")], []),
  ("And one more man sees it all.", [("And one", k(56), "PUSH_IN")], []),
  ("Vorian Atreides, the human son of the Titan Agamemnon, raised to serve the machines.",
   [("Vorian Atreides", k(7), "DRIFT")],
   [("Vorian Atreides", N, {"name": "VORIAN ATREIDES", "role": "Son of Agamemnon"}, 3.6)]),
  ("In that moment, he understands the lie he has lived.", [("In that", k(56), "PULL_OUT")], []),
  ("In his ship, the Dream Voyager, he carries Serena and Iblis to freedom.",
   [("In his ship", k(57), "PULL_OUT"), ("he carries", k(58), "DRIFT")], []),
  ("The first Atreides has chosen his side.", [("The first", k(59), "DRIFT")], []),
 ]),

 ("IV", "The Burning of Earth", "IV", [
  ("The machines answer the uprising the only way they know.", [("The machines", k(60), "PULL_OUT")], []),
  ("Titans and robots hunt down every human on Earth, until not one is left alive.",
   [("Titans and", k(145), "PUSH_IN"), ("until not", k(61), "HOLD")], []),
  ("On Salusa, Serena stands before the League's parliament.",
   [("On Salusa", k(33), "PUSH_IN")], []),
  ("Grieving and furious, she demands total war.", [("Grieving", k(63), "PUSH_IN")], []),
  ("Xavier Harkonnen proposes the unthinkable: atomics, weapons no one had ever dared to use.",
   [("Xavier", k(64), "PUSH_IN"), ("atomics", k(65), "PUSH_IN")],
   [("atomics", NOTE, {"head": "ATOMICS", "body": "Planet-killing weapons. Never before used against an entire world."}, 4.6)]),
  ("Not a single voice is raised against him.", [("Not a", k(66), "HOLD")], []),
  ("In 200 BG, the League's fleet reaches Earth.", [("In 200", k(67), "PULL_OUT")],
   [("In 200", YR, {"year": "200 B.G.", "sub": "The League fleet reaches Earth"}, 3.4)]),
  ("The machines there are wiped out, and with them the cradle of humanity.",
   [("The machines there", k(68), "PUSH_IN")], []),
  ("The oldest world becomes a dead, glowing rock.", [("The oldest", k(69), "PULL_OUT")], []),
  ("And the war is given a name.", [("And the war", k(70), "TILT_UP")], []),
  ("Not a campaign. A jihad. A holy war, in the name of Serena Butler and her murdered son.",
   [("A holy war", k(11), "PUSH_IN")], []),
 ]),

 ("V", "The Holy War", "V", [
  ("Iblis Ginjo becomes the Grand Patriarch of the Jihad.", [("Iblis Ginjo", k(71), "PUSH_IN")],
   [("Iblis Ginjo", N, {"name": "IBLIS GINJO", "role": "Grand Patriarch of the Jihad"}, 3.4)]),
  ("Serena becomes its priestess, the face on every banner.",
   [("Serena becomes", k(72), "DRIFT"), ("the face", k(141), "DRIFT")], []),
  ("Xavier and Vorian become its generals.", [("Xavier and", k(73), "DRIFT")], []),
  ("For decades the war grinds on.", [("For decades", k(74), "PAN_LR")], []),
  ("Worlds are freed, and lost, and freed again.", [("Worlds are", "MAP:B", "MAP")], []),
  ("New inventions change the battlefield: energy shields that stop any fast-moving weapon, and ships that can fold space itself.",
   [("energy shields", k(76), "PUSH_IN"), ("that can fold", k(77), "PUSH_IN")],
   [("energy shields", NOTE, {"head": "HOLTZMAN SHIELDS", "body": "Slow blades still pass."}, 2.8)]),
  ("But behind the banners, Iblis is building something else: a secret police, a ruling council, and a holy war that answers only to him.",
   [("But behind", k(142), "PUSH_IN"), ("a secret police", k(78), "PUSH_IN"), ("and a holy war", k(79), "PUSH_IN")], []),
  ("After almost forty years, the League is exhausted.", [("After almost", k(80), "DRIFT")], []),
  ("The machines offer a truce, and the people want to accept it.",
   [("The machines offer", k(81), "PUSH_IN"), ("and the people", k(62), "PULL_OUT")], []),
  ("For Serena and Iblis, peace with the machines means a slow defeat.", [("For Serena", k(82), "PUSH_IN")], []),
  ("So they make a terrible plan.", [], []),
 ]),

 ("VI", "The Martyr", "VI", [
  ("Serena travels to Corrin, the capital of the machines, as an ambassador of peace.",
   [("Serena travels", k(83), "PULL_OUT"), ("as an ambassador", k(84), "PUSH_IN")],
   [("Serena travels", YR, {"year": "164 B.G.", "sub": "The peace mission to Corrin"}, 3.2),
    ("the capital", PL, {"place": "CORRIN", "sub": "Capital of Omnius"}, 3.4)]),
  ("In secret, she has come to give her life.", [],
   [("In secret", FILE, {"img": k(6), "focus": [0.5, 0.4], "title": "SUBJECT: SERENA BUTLER", "stamp": "MARTYR",
                         "fields": [["ROLE", "Priestess of the Jihad"], ["MISSION", "Ambassador of peace"],
                                    ["DESTINATION", "Corrin"], ["TRUE PURPOSE", "Classified"]]}, 5.0)]),
  ("She defies Omnius until it condemns her.", [("She defies", k(85), "PULL_OUT")], []),
  ("But Erasmus sees the smile on her face.", [("But Erasmus", k(87), "PUSH_IN")], []),
  ("He knows she wants this, and he refuses to grant it.", [("He knows", k(86), "PUSH_IN")], []),
  ("So her most loyal guardian does what the machines will not.", [("So her", k(88), "PUSH_IN")], []),
  ("Serena Butler's end comes swiftly, from a human hand.", [("Serena Butler's", k(89), "HOLD")], []),
  ("Then Iblis Ginjo makes sure the galaxy sees something else.", [("Then Iblis", k(146), "PAN_RL")], []),
  ("Images reach Salusa: Serena, suffering at the hands of a machine.", [("Images reach", k(90), "PUSH_IN")], []),
  ("Her remains are found, and the cells match.", [("Her remains", k(92), "PUSH_IN")], []),
  ("It is a clone, grown in secret.", [("It is a clone", k(91), "PUSH_IN")], []),
  ("The images are a lie.", [], []),
  ("And the lie works.", [("And the lie", k(93), "PULL_OUT")], []),
  ("The peace movement dies overnight.", [], []),
  ("The Jihad roars back to life.", [("The Jihad", k(94), "TILT_UP")], []),
 ]),

 ("VII", "The Traitor's Name", "VII", [
  ("That same year, Xavier Harkonnen uncovers the Grand Patriarch's darkest secret.", [("That same", k(143), "DRIFT")], []),
  ("To replace the organs of wounded soldiers, Iblis and his Tlulaxa allies have been kidnapping humans from free worlds, and blaming the machines.",
   [("To replace", k(95), "PAN_LR"), ("have been kidnapping", k(96), "PUSH_IN")], []),
  ("Xavier knows he will never reach home alive with the truth.", [("Xavier knows", k(97), "PUSH_IN")], []),
  ("So he takes the controls of Iblis Ginjo's ship, and flies it into a star, carrying them both to their deaths.",
   [("So he takes", k(98), "PUSH_IN"), ("and flies", k(99), "PUSH_IN")], []),
  ("But the story told afterwards is not the truth.", [("But the story", k(143), "PUSH_IN")], []),
  ("Iblis becomes a martyr, the third saint of the Jihad, beside Serena and her son.",
   [("Iblis becomes", k(100), "TILT_UP")],
   [("the third saint", NOTE, {"head": "THE THREE MARTYRS", "body": "Saint Serena · Manion the Innocent · Iblis Ginjo"}, 4.6)]),
  ("And Xavier Harkonnen is remembered as a traitor and a murderer.", [("And Xavier", k(101), "PUSH_IN")], []),
  ("His family abandons the Harkonnen name in shame.", [("His family", k(102), "DRIFT")], []),
  ("Only Vorian Atreides knows what really happened.", [("Only Vorian", k(103), "PUSH_IN")], []),
  ("Remember that name. It is coming back.", [], []),
 ]),

 ("VIII", "The Great Purge", "VIII", [
  ("Decades pass.", [("Decades", k(30), "PUSH_IN")], []),
  ("Then, in 108 BG, Omnius strikes with a new weapon: a plague, built to kill humans.", [("a plague", k(104), "PUSH_IN")],
   [("in 108", YR, {"year": "108 B.G.", "sub": "The Omnius Scourge"}, 3.4)]),
  ("It sweeps through the League, and billions die.", [("It sweeps", k(105), "PULL_OUT")],
   [("and billions", NOTE, {"head": "THE SCOURGE", "body": "A machine-made plague. Billions dead across the League."}, 4.2)]),
  ("With the League on its knees, the machine fleet sets course for Salusa Secundus.", [("With the", k(106), "PAN_RL")], []),
  ("Vorian Atreides answers with the most ruthless plan of the war.", [("Vorian Atreides", k(107), "PUSH_IN")], []),
  ("While the machine fleet is away, humanity's ships fold space, and strike every undefended machine world at once, with atomics.",
   [("While the", k(108), "PUSH_IN"), ("and strike every", "MAP:C", "MAP")], []),
  ("It is called the Great Purge.", [], []),
  ("World after world is burned to slag, and every human slave on them dies with the machines.",
   [("World after", k(109), "PULL_OUT"), ("and every human", k(110), "PAN_LR")], []),
  ("Only one world survives.", [("Only one", k(111), "PULL_OUT")], []),
  ("Corrin, the home of Omnius.", [], []),
  ("The League surrounds it with a blockade, and declares the Jihad over.", [("The League surrounds", k(112), "PAN_LR")], []),
  ("For twenty years, the last of the machines wait behind it.", [("For twenty", k(3), "PUSH_IN")], []),
 ]),

 ("IX", "The Bridge of Hrethgir", "IX", [
  ("In 88 BG, the Army of Humanity comes for Corrin.", [("In 88", k(113), "PUSH_IN")],
   [("In 88", YR, {"year": "88 B.G.", "sub": "The Battle of Corrin"}, 3.4)]),
  ("Vorian Atreides leads it.", [("Vorian Atreides", k(114), "DRIFT")], []),
  ("He has already destroyed the last of the Titans, his own father among them.", [("He has already", k(115), "HOLD")], []),
  ("At his side is Abulurd, Xavier's grandson.", [("At his side", k(116), "DRIFT")],
   [("At his side", N, {"name": "ABULURD HARKONNEN", "role": "Grandson of Xavier"}, 3.6)]),
  ("Vorian has told him the truth, and Abulurd has taken back the name Harkonnen.", [("Vorian has told", k(114), "PUSH_IN")], []),
  ("Erasmus has prepared one final defence.", [("Erasmus has", k(119), "PUSH_IN")], []),
  ("Around the planet, he has strung two million human captives in cargo pods, rigged to explode the moment the fleet crosses them.",
   [("Around the", k(117), "PULL_OUT"), ("rigged to", k(118), "PUSH_IN")],
   [("two million", STAT, {"value": 2_000_000, "label": "HUMAN CAPTIVES", "sub": "a living shield around Corrin"}, 3.6)]),
  ("The machines call humans hrethgir.", [], []),
  ("This is the Bridge of Hrethgir.", [("This is the Bridge", k(117), "PUSH_IN")], []),
  ("Vorian gives the order to advance.", [("Vorian gives", k(147), "PUSH_IN")], []),
  ("Abulurd begs him not to.", [("Abulurd begs", k(120), "PUSH_IN")], []),
  ("Then he does the unthinkable.", [("Then he does", k(121), "PUSH_IN")], []),
  ("He disables the weapons of the entire fleet.", [("He disables", k(122), "PULL_OUT")], []),
  ("The pods never explode.", [], []),
  ("Erasmus himself has switched them off, to save the one human he cares about.", [("Erasmus himself", k(148), "PUSH_IN")], []),
  ("But no one in the fleet knows that.", [("But no one", k(122), "DRIFT")], []),
  ("Without its weapons, the battle becomes far bloodier.", [("Without its", k(75), "PULL_OUT")], []),
  ("Corrin falls to atomics and to a final assault on the ground.",
   [("Corrin falls", k(123), "PULL_OUT"), ("and to a final", k(124), "PUSH_IN")], []),
  ("Omnius is destroyed.", [("Omnius is", k(125), "PULL_OUT")], []),
  ("The age of thinking machines is over.", [], []),
 ]),

 ("X", "Thou Shalt Not", "X", [
  ("After the victory, Abulurd is spared execution.", [("After the", k(126), "PUSH_IN")], []),
  ("Instead, Vorian has him branded a coward, and exiled to the frozen world of Lankiveil, forced to carry the name Harkonnen forever.",
   [("Instead", k(127), "HOLD"), ("and exiled", k(128), "PAN_LR"), ("forced to", k(129), "DRIFT")],
   [("and exiled", PL, {"place": "LANKIVEIL", "sub": "Exile of House Harkonnen"}, 3.6)]),
  ("And Vorian swears that every Atreides will spit on that name.", [("And Vorian", k(114), "PUSH_IN")], []),
  ("That oath will outlive empires.", [], []),
  ("Ten thousand years later, it will end in fire on Arrakis.", [("Ten thousand", k(130), "PUSH_IN")], []),
  ("Abulurd's brother Faykan takes a new name from the battle: Corrino.", [("Abulurd's brother", k(131), "PUSH_IN")],
   [("Corrino", N, {"name": "HOUSE CORRINO", "role": "Named for the Battle of Corrin"}, 3.6)]),
  ("His family will sit on the Golden Lion Throne for ten thousand years.", [("His family", k(132), "TILT_UP")], []),
  ("And humanity writes one commandment into its holy law: Thou shalt not make a machine in the likeness of a human mind.",
   [("And humanity", k(133), "TILT_UP")],
   [("Thou shalt", TTL, {"kicker": "THE COMMANDMENT", "title": "THOU SHALT NOT",
                         "sub": "make a machine in the likeness of a human mind"}, 6.5)]),
  ("Without thinking machines, humans must become the machines.", [("Without thinking", k(134), "PULL_OUT")], []),
  ("Mentats who compute. Sisters who plan across centuries. Navigators who fold space with spice.",
   [("Mentats", k(135), "PUSH_IN"), ("Sisters", k(136), "DRIFT"), ("Navigators", k(137), "PUSH_IN")], []),
  ("Every power of the Imperium grows from the ashes of this war.", [("Every power", k(138), "PULL_OUT")], []),
  ("And from a mother, a balcony, and a child.", [("And from", k(139), "PUSH_IN"), ("a balcony", k(140), "PULL_OUT")], []),
 ]),

 ("CB", "Outro", None, [
  ("So, was Vorian right to give that order at Corrin, or was Abulurd the real hero?", [("So, was", k(149), "PUSH_IN")],
   [("So, was", END, {"kicker": "WATCH NEXT", "title": "DUNE MESSIAH", "brand": "A MYTHIC ARCHIVES PRODUCTION",
                      "q_at": "So, was", "comment_at": "comments", "like_at": "like", "sub_at": "subscribe"}, 0)]),
  ("Tell us what you think in the comments.", [], []),
  ("If this story stayed with you, give the video a like, and subscribe to the Mythic Archives.", [], []),
  ("The archive is always open.", [], []),
 ]),
]

# channel ident (no VO) placed in the GAP_AFTER_HOOK silence
IDENT_SHOT = (k(31), "PUSH_IN", {"title": "THE MYTHIC ARCHIVES", "tag": "WESTEROS  •  ARRAKIS  •  MIDDLE-EARTH",
                                  "sub": "A MYTHIC ARCHIVES PRODUCTION  ·  RECORD 001"})
END_HOLD = 6.0   # end card hold after the last word (YouTube end-screen room)

# animated maps (templates/maps/DUN001_MAP_*.json -> 19_batches/DUN001/maps/*.mp4)
MAPS = {'MAP:A': 'DUN001_MAP_A_synchronized_worlds.mp4',
        'MAP:B': 'DUN001_MAP_B_jihad_front.mp4',
        'MAP:C': 'DUN001_MAP_C_great_purge.mp4'}


def narration(section):
    return " ".join(l[0] for l in section[3])


PROLOGUE = '0:00 Prologue: The Balcony'

# sentence ending -> minimum pause after it (s); beats the default documentary pause
SPECIAL_PAUSE = {
    'it is about to find out.': 0.95, 'machines of war.': 0.6, 'will be a lie.': 0.85,
    'the child does not survive.': 2.6, 'has chosen his side.': 0.8, 'a dead, glowing rock.': 1.3,
    'a terrible plan.': 0.9, 'the images are a lie.': 0.8, 'roars back to life.': 0.8,
    'it is coming back.': 0.9, 'dies with the machines.': 0.8, 'machines is over.': 1.1,
    'end in fire on arrakis.': 0.8, 'and a child.': 1.2,
}


def music_edl(S, total, ident, phrase_after, phrase_end):
    """DUN001 cue sheet: Kevin MacLeod (incompetech, CC BY 4.0), same library and loudness approach as DUN003.
    S = section info (gap_start/start/end/last_word_end per section id), times in programme seconds."""
    child = phrase_end('The child does not survive.')
    rock = phrase_end('a dead, glowing rock.')
    over = phrase_end('The age of thinking machines is over.')

    def cue(cid, name, track, start, end, offset, fade_in=1.5, fade_out=2.5, gain_db=0, **kw):
        return dict(cue=cid, name=name, track=track, start=round(start, 2), end=round(end, 2), offset=offset,
                    fade_in=fade_in, fade_out=fade_out, gain_db=gain_db, **kw)
    cues = [
        cue('M1', 'The Balcony (hook)', 'Phantasm', 0.0, ident[0] + 1.2, 14.0, fade_in=0.0, gain_db=-2, hp=110),
        cue('M2', 'Archive (ident)', 'Deliberate_Thought', ident[0] - 1.2, S['I']['gap_start'] + 1.4, 30.0,
            fade_in=1.2, gain_db=-1),
        cue('M3', 'The Age of Machines', 'Crypto', S['I']['gap_start'] - 0.4, S['II']['gap_start'] + 0.6, 2.0, gain_db=-1),
        cue('M4', 'The Last Free Humans', 'Dark_Times', S['II']['gap_start'] - 0.4, S['CA']['gap_start'] + 1.0, 3.0),
        cue('M2b', 'Subscribe (archive theme)', 'Deliberate_Thought', S['CA']['gap_start'] - 0.2,
            S['III']['gap_start'] + 0.8, 30.0, fade_in=1.0, fade_out=2.0, gain_db=-1),
        cue('M5', 'The Child', 'Long_Note_Two', S['III']['gap_start'] - 0.4, child + 0.15, 34.0, fade_out=0.05),
        cue('M5b', 'The Spark (revolt)', 'Interloper', child + 2.3, S['IV']['gap_start'] + 0.6, 66.0, fade_in=0.4, gain_db=1),
        cue('M6', 'The Burning of Earth', 'Lightless_Dawn', S['IV']['gap_start'] - 0.4, S['V']['gap_start'] + 0.6, 0.0),
        cue('M7', 'The Holy War', 'Wizardtorium', S['V']['gap_start'] - 0.4, S['VI']['gap_start'] + 0.6, 0.0),
        cue('M8', 'The Martyr', 'Private_Reflection', S['VI']['gap_start'] - 0.4, S['VII']['gap_start'] + 0.6, 0.0,
            fade_out=3.0),
        cue('M9', "The Traitor's Name", 'Ossuary_6_Air', S['VII']['gap_start'] - 0.4, S['VIII']['gap_start'] + 0.6, 0.0),
        cue('M10', 'The Great Purge', 'Lightless_Dawn', S['VIII']['gap_start'] - 0.4, S['IX']['gap_start'] + 0.6, 170.0),
        cue('M11', 'The Bridge of Hrethgir', 'Night_Vigil', S['IX']['gap_start'] - 0.2, over + 2.5, 60.0, fade_out=3.5),
        cue('M12', 'Thou Shalt Not', 'Unwritten_Return', over + 0.8, S['CB']['gap_start'] + 1.6, 12.0, fade_in=2.0,
            fade_out=3.5, gain_db=-1),
        cue('M12b', 'Outro (archive theme)', 'Deliberate_Thought', S['CB']['gap_start'] - 0.6, total, 30.0,
            fade_in=2.0, fade_out=3.0, gain_db=-2),
    ]
    return dict(episode='DUN001', timeline=f'voice-14 VO, programme {total} s', bed_lufs=-23.0,
                notes='start/end = programme seconds; offset = seconds into the source track; fade_in/fade_out in '
                      'seconds; gain_db = trim after loudness normalisation; hp = high-pass Hz. Kevin MacLeod '
                      '(incompetech.com), CC BY 4.0.',
                cues=cues,
                sfx=[dict(type='wind', start=0.0, end=20.0, level_db=-38, note='cold air on the balcony (hook)'),
                     dict(type='heartbeat', start=S['III']['gap_start'], end=round(child + 0.2, 2), level_db=-24,
                          note="pulse up to 'The child does not survive.', then silence"),
                     dict(type='wind', start=round(rock - 1.0, 2), end=round(rock + 9.0, 2), level_db=-34,
                          note='dead Earth')],
                silences=[f'{child:.1f}-{child + 2.3:.1f} after "The child does not survive."'])
