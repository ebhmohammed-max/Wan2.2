"""GOT001: "The Night King: Who Was He Really?" (WESTEROS · RECORD 001).

Same format as data/dun001.py: SECTIONS = (sid, name, chapter num or None, [(narration, [shots], [graphics])]).
  shot    = (anchor, image_key, recipe[, focus])  - cut lands on the first word of `anchor`
  graphic = (anchor, KIND, {params}, dur_s)
Narration must match the voice-14 takes in 20_voiceover/GOT001/raw/<SID>.mp3 word for word
(script 17_scripts/GOT001_SCRIPT_v1.0.md, approved 2026-11-24).
Canon: books first; the show's Night King is labelled and shown only in silhouette.
"""

TITLE = "The Night King: Who Was He Really?"
EPISODE = "GOT001"
RECORD = "WESTEROS · RECORD 001"
GAP_AFTER_HOOK = 6.0
GAP_CHAPTER = 1.8

N, PL, YR, NOTE, STAT, CH, TTL, IDENT, DOSSIER, FILE, END = (
    'NAME', 'PLACE', 'YEAR', 'NOTE', 'STAT', 'CHAPTER', 'TITLE', 'IDENT', 'DOSSIER', 'FILE', 'END')


def k(n):
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


SECTIONS = [
 ("H", "Hook", None, [
  ("On television, he is the king of the dead.", [("On television", k(11), "PULL_OUT")], []),
  ("A crown of ice grows from his skull.", [("A crown", k(12), "PUSH_IN")], []),
  ("He raises armies with a lift of his arms, and when he finally falls, every dead thing in the world falls with him.",
   [("He raises", k(13), "TILT_UP"), ("and when", k(14), "PULL_OUT")], []),
  ("But George R. R. Martin's books tell a very different story.", [("But George", k(15), "PUSH_IN")], []),
  ("In the books, the Night's King was a man.", [("In the books", k(1), "PUSH_IN")], []),
  ("A brother of the Night's Watch, who fell in love with a woman whose skin was white as the moon, and whose eyes were like blue stars.",
   [("A brother", k(16), "PUSH_IN"), ("whose skin", k(2), "PUSH_IN")], []),
  ("When it was over, his name was erased from history.", [("When it", k(17), "PUSH_IN")], []),
  ("So who was he really?", [("So who", k(18), "DRIFT")],
   [("So who", TTL, {"kicker": "THE MYTHIC ARCHIVES PRESENTS", "title": "THE NIGHT KING",
                     "sub": "Who Was He Really?"}, 0)]),
 ]),

 ("P", "Prologue: The Castle of Ghosts", None, [
  ("On the Wall stands the oldest castle of the Night's Watch, and the largest.", [("On the Wall", k(9), "PULL_OUT")],
   [("On the Wall", PL, {"place": "THE NIGHTFORT", "sub": "The Wall · abandoned two hundred years"}, 4.0)]),
  ("They call it the Nightfort.", [("They call", k(19), "PUSH_IN")], []),
  ("Its towers are broken.", [("Its towers", k(20), "TILT_UP")], []),
  ("Its halls are full of rats and dust.", [("Its halls", k(21), "PAN_LR")], []),
  ("For two hundred years, no brother has lived there.", [("For two", k(22), "PULL_OUT")], []),
  ("When young Bran Stark shelters inside its walls, he remembers the stories his old nurse told him about this place.",
   [("When young", k(23), "PAN_LR"), ("he remembers", k(4), "PUSH_IN")],
   [("When young", N, {"name": "BRAN STARK", "role": "Heir of Winterfell"}, 3.4)]),
  ("Here, the Rat Cook served a king a pie made from the king's own son.", [("Here, the Rat", k(24), "PUSH_IN")], []),
  ("Here, the seventy-nine sentinels were sealed into the ice for deserting, and still stand watch, facing north.",
   [("Here, the seventy-nine", k(25), "TILT_UP"), ("and still", k(143), "PUSH_IN")], []),
  ("And here, before all of them, Night's King had reigned, until his name was wiped from the memory of man.",
   [("And here", k(26), "PUSH_IN"), ("until his", k(27), "PULL_OUT")], []),
 ]),

 ("I", "The Thirteenth Lord Commander", "I", [
  ("The story begins at the end of the Long Night, a winter that lasted a generation.", [("The story", k(28), "PAN_LR")], []),
  ("When the darkness finally broke, men raised a Wall of ice seven hundred feet high.", [("When the darkness", k(29), "PULL_OUT")],
   [("seven", STAT, {"value": 700, "label": "FEET OF ICE", "sub": "The Wall"}, 3.4)]),
  ("Legend says it was built by Brandon the Builder, the first Stark king, with the help of giants and the children of the forest.",
   [("Legend says", k(30), "PAN_RL"), ("and the children", k(31), "PUSH_IN")],
   [("Legend says", N, {"name": "BRANDON THE BUILDER", "role": "First King of Winter · legend"}, 3.6)]),
  ("And they founded a brotherhood to guard it.", [("And they", k(32), "PULL_OUT")], []),
  ("The Night's Watch: men who took no wives, held no lands, and fathered no children.", [("The Night's Watch:", k(33), "PAN_LR")], []),
  ("The Night's King was the thirteenth man to lead them.", [("The Night's King", k(34), "PUSH_IN")],
   [("thirteenth", N, {"name": "THE NIGHT'S KING", "role": "13th Lord Commander of the Night's Watch"}, 3.8)]),
  ("Old Nan said he was a warrior who knew no fear.", [("Old Nan", k(3), "PUSH_IN")],
   [("Old Nan", N, {"name": "OLD NAN", "role": "Storyteller of Winterfell"}, 3.2)]),
  ("\"And that was the fault in him,\" she would add, \"for all men must know fear.\"", [("\"And that", k(35), "PUSH_IN")], []),
  ("Fear is what keeps a man on top of the Wall, watching the dark.", [("Fear is", k(36), "DRIFT")], []),
  ("A man who fears nothing might look at the dark and want to walk into it.", [("A man who", k(37), "TILT_UP")], []),
 ]),

 ("II", "The Corpse Queen", "II", [
  ("One night, from the top of the Wall, he saw her.", [("One night", k(38), "PUSH_IN")], []),
  ("A woman with skin as white as the moon and eyes like blue stars.", [("A woman", k(39), "PUSH_IN"), ("eyes like", k(147), "PUSH_IN")], []),
  ("Fearing nothing, he chased her, and caught her, and loved her, though her skin was cold as ice.",
   [("Fearing nothing", k(40), "PAN_LR"), ("and caught", k(41), "PUSH_IN")], []),
  ("And with his love, Old Nan said, he gave her his soul.", [("And with", k(42), "PUSH_IN")], []),
  ("The books never say what she was.", [("The books", k(43), "DRIFT")], []),
  ("But skin like that and eyes like blue stars are what the Others look like.", [("But skin", k(44), "PAN_RL")], []),
  ("And the tales call her the corpse queen.", [("And the tales", k(45), "PUSH_IN")],
   [("corpse", N, {"name": "THE CORPSE QUEEN", "role": "Skin white as the moon · eyes like blue stars"}, 3.6)]),
  ("He brought her back through the Wall to the Nightfort, and proclaimed her a queen, and himself her king.",
   [("He brought", k(46), "PUSH_IN"), ("and proclaimed", k(47), "PULL_OUT")], []),
  ("With strange sorceries, he bound his sworn brothers to his will.", [("With strange", k(48), "DRIFT")], []),
  ("The men who swore to guard the realms of men now served a king of the night.", [("The men", k(49), "PUSH_IN")], []),
  ("For thirteen years, Night's King and his corpse queen ruled the Wall.", [("For thirteen", k(50), "PULL_OUT")],
   [("thirteen", STAT, {"value": 13, "label": "YEARS OF THE NIGHT'S KING", "sub": ""}, 3.4)]),
 ]),

 ("CA", "Subscribe", None, [
  ("Before we find out who brought him down, and what they found when they did: if you want Westeros the way Martin wrote it, subscribe to the Mythic Archives.",
   [("Before we", k(51), "PAN_LR"), ("if you want", k(146), "PULL_OUT")], [("if you want", "SUB", {"click_at": "subscribe"}, 0)]),
 ]),

 ("III", "Two Kings Against One", "III", [
  ("His fall took something the North had never seen before: an alliance between enemies.",
   [("His fall", k(52), "PULL_OUT"), ("an alliance", k(53), "PUSH_IN")], []),
  ("The King of Winter in Winterfell, and Joramun, King-beyond-the-Wall, the wildling who, legends say, blew the Horn of Winter and woke giants from the earth.",
   [("The King", k(8), "PUSH_IN"), ("and Joramun", k(7), "TILT_UP"), ("and woke", k(54), "TILT_UP")],
   [("The King", N, {"name": "THE KING OF WINTER", "role": "House Stark of Winterfell"}, 3.0),
    ("and Joramun", N, {"name": "JORAMUN", "role": "King-beyond-the-Wall"}, 3.4)]),
  ("A Stark and a wildling.", [("A Stark", k(55), "PUSH_IN")], []),
  ("Men who had fought each other for generations, now marching together against the Watch itself.",
   [("Men who", k(148), "PAN_RL"), ("now marching", k(56), "PAN_RL")], []),
  ("They broke the Night's King, and freed his brothers from their bondage.", [("They broke", k(57), "PUSH_IN")], []),
  ("Then they discovered what he had been doing all those years.", [("Then they", k(58), "PUSH_IN")], []),
  ("He had been making sacrifices to the Others.", [("He had", k(59), "DRIFT")], []),
  ("So every record of him was destroyed.", [("So every", k(60), "PUSH_IN")], []),
  ("His deeds were struck from the histories.", [("His deeds", k(61), "PUSH_IN")], []),
  ("Even his name was forbidden.", [("Even his", k(17), "PUSH_IN")], []),
  ("That is why, eight thousand years later, nobody in Westeros knows what he was called.", [("That is why", k(62), "PULL_OUT")],
   [("eight", STAT, {"value": 8000, "label": "YEARS OF SILENCE", "sub": ""}, 3.4)]),
 ]),

 ("IV", "A Stark of Winterfell", "IV", [
  ("But Old Nan had an idea.", [("But Old", k(63), "PUSH_IN")], []),
  ("She always ended the story the same way.", [("She always", k(64), "PUSH_IN")], []),
  ("\"Some say he was a Bolton.", [("\"Some say", k(65), "PAN_LR")], []),
  ("Some say a Magnar out of Skagos, some say Umber, Flint, or Norrey.", [("Some say a", k(66), "PAN_RL")], []),
  ("Some would have you think he was a Woodfoot, from them who ruled Bear Island.\"", [("Some would", k(67), "PAN_LR")], []),
  ("\"He never was,\" she said.", [("\"He never", k(68), "PUSH_IN")], []),
  ("\"He was a Stark, the brother of the man who brought him down.\"", [("\"He was a Stark, the", k(69), "PUSH_IN")], []),
  ("Then she pinched little Bran's nose.", [("Then she", k(70), "PUSH_IN")], []),
  ("\"He was a Stark of Winterfell, and who can say?", [("\"He was a Stark of", k(71), "PULL_OUT")], []),
  ("Mayhaps his name was Brandon.\"", [("Mayhaps", k(72), "PUSH_IN")], []),
  ("She said one more thing, which Bran never forgot.", [("She said", k(73), "PUSH_IN")], []),
  ("\"Night's King was only a man by light of day.", [("\"Night's King", k(74), "DRIFT")], []),
  ("But the night was his to rule.\"", [("But the night", k(75), "PUSH_IN")], []),
  ("It is not a strange guess.", [("It is not", k(76), "PUSH_IN")], []),
  ("House Stark has always loved the name.", [("House Stark", k(149), "PUSH_IN")], []),
  ("Brandon the Builder.", [("Brandon the Builder.", k(30), "PAN_RL")], []),
  ("Brandon the Shipwright, who sailed west and never returned.", [("Brandon the Shipwright", k(77), "PULL_OUT")], []),
  ("Brandon the Burner.", [("Brandon the Burner.", k(78), "PAN_LR")], []),
  ("Bran's own uncle Brandon.", [("Bran's own", k(79), "PUSH_IN")], []),
  ("A Stark brother bringing down a Stark brother.", [("A Stark brother", k(80), "PUSH_IN")], []),
  ("The family whose words are \"Winter is coming\" may have given the Others their greatest ally.",
   [("The family", k(81), "TILT_UP")], []),
 ]),

 ("V", "The Black Gate", "V", [
  ("The Nightfort still has one secret.", [("The Nightfort", k(82), "PUSH_IN")], []),
  ("In its kitchens there is an old well, and at the bottom of the well, there is a door.",
   [("In its", k(83), "PUSH_IN"), ("there is a door", k(84), "PULL_OUT")], []),
  ("The Watch calls it the Black Gate.", [("The Watch", k(10), "PUSH_IN")],
   [("The Watch", PL, {"place": "THE BLACK GATE", "sub": "Beneath the Nightfort"}, 3.6)]),
  ("But it isn't black at all.", [("But it", k(85), "DRIFT")], []),
  ("It is pale white weirwood, glowing like milk and moonlight, and it has a face.",
   [("It is pale", k(144), "TILT_UP"), ("and it has", k(86), "PUSH_IN")], []),
  ("When Bran's party reaches it, the face opens its eyes.", [("When Bran's", k(87), "PUSH_IN"), ("the face", k(88), "PUSH_IN")], []),
  ("\"Who are you?\" it asks.", [("\"Who are", k(89), "PUSH_IN")], []),
  ("A brother of the Watch, Samwell Tarly, answers with the words of his oath.", [("A brother", k(5), "DRIFT"), ("answers", k(90), "PUSH_IN")],
   [("Samwell", N, {"name": "SAMWELL TARLY", "role": "Brother of the Night's Watch"}, 3.2)]),
  ("\"I am the sword in the darkness.", [("\"I am the sword", k(91), "TILT_UP")], []),
  ("I am the watcher on the walls.", [("I am the watcher", k(92), "DRIFT")], []),
  ("I am the shield that guards the realms of men.\"", [("I am the shield", k(93), "PULL_OUT")], []),
  ("\"Then pass,\" the door says.", [("\"Then pass", k(94), "PUSH_IN")], []),
  ("Its mouth opens wide, and they walk through, under the Wall, into the North.", [("and they walk", k(95), "PUSH_IN")], []),
  ("A secret door through the Wall, in the castle where a Lord Commander once let the cold inside.",
   [("A secret", k(96), "DRIFT")], []),
  ("The books never connect the two.", [("The books", k(97), "HOLD")], []),
  ("But it is hard not to wonder.", [("But it is", k(98), "PULL_OUT")], []),
 ]),

 ("VI", "The King of the Dead", "VI", [
  ("Then, in 2014, the show gave the name to someone new.", [("Then, in", k(99), "PUSH_IN")],
   [("Then, in", NOTE, {"head": "THE SHOW", "body": "Everything in this chapter appears only in the HBO series, not in the books."}, 4.6)]),
  ("In the fourth season, a White Walker rides through the snow carrying a baby to an altar of ice.",
   [("In the fourth", k(100), "PAN_LR"), ("to an altar", k(101), "PUSH_IN")], []),
  ("A crown of icy horns rises from his head.", [("A crown", k(12), "PUSH_IN")], []),
  ("He touches the child's cheek, and its eyes turn blue.", [("He touches", k(102), "PUSH_IN")], []),
  ("HBO's official guide briefly named him the Night's King, then quietly removed the name.",
   [("HBO's", k(145), "PAN_LR"), ("then quietly", k(103), "HOLD")], []),
  ("The show's version became its great villain.", [("The show's", k(11), "PULL_OUT")], []),
  ("At Hardhome, he lifts his arms and the dead rise to join him.", [("At Hardhome", k(104), "TILT_UP"), ("and the dead", k(142), "PUSH_IN")], []),
  ("Beyond the Wall, he brings down one of Daenerys's dragons and raises it as his own.", [("Beyond the", k(105), "PAN_RL")], []),
  ("In the sixth season, the show reveals his origin.", [("In the sixth", k(106), "PULL_OUT")], []),
  ("Long ago, the children of the forest bound a man of the First Men to a weirwood tree and drove a blade of dragonglass into his heart.",
   [("Long ago", k(107), "PUSH_IN")], []),
  ("He became the first White Walker.", [("He became", k(108), "PUSH_IN")], []),
  ("At Winterfell, in the final season, Arya Stark kills him with a Valyrian steel dagger, and his entire army falls with him.",
   [("At Winterfell", k(109), "PUSH_IN"), ("and his entire", k(110), "PULL_OUT")], []),
  ("None of that happens in the books.", [("None of", k(111), "HOLD")], []),
 ]),

 ("VII", "Martin's Answer", "VII", [
  ("When fans asked Martin whether the show's Night King and the book's Night's King were the same person, he gave a careful answer.",
   [("When fans", k(112), "PUSH_IN"), ("were the same", k(15), "PUSH_IN")], []),
  ("\"As for the Night's King, the form I prefer, in the books he is a legendary figure, akin to Lann the Clever and Brandon the Builder, and no more likely to have survived to the present day than they have.\"",
   [("\"As for", k(113), "PAN_LR"), ("akin to", k(114), "PUSH_IN"), ("and Brandon", k(30), "PAN_RL"), ("and no more", k(115), "DRIFT")],
   [("\"As for", NOTE, {"head": "GEORGE R. R. MARTIN",
                        "body": "\u201cIn the books he is a legendary figure, akin to Lann the Clever and Brandon the Builder, "
                                "and no more likely to have survived to the present day than they have.\u201d"}, 12.5)]),
  ("In other words, the Night's King of the books is a legend, like the trickster who stole Casterly Rock and the builder of the Wall.",
   [("In other", k(116), "PULL_OUT"), ("and the builder", k(29), "PULL_OUT")], []),
  ("He may never even have existed.", [("He may", k(117), "DRIFT")], []),
  ("Notice the name, too.", [("Notice", k(118), "PUSH_IN")], []),
  ("Martin prefers Night's King, with an S, like a title.", [("Martin prefers", k(34), "PUSH_IN")],
   [("Martin prefers", NOTE, {"head": "NIGHT'S KING", "body": "Martin's spelling: a title, like King in the North. The show's spelling: Night King."}, 5.6)]),
  ("The show dropped the S.", [], []),
  ("And the books have no Night King at all.", [("And the books", k(119), "PULL_OUT")], []),
  ("No one in the novels knows who leads the Others, or whether anyone does.", [("No one in", k(120), "PUSH_IN")], []),
  ("No one knows where they came from.", [("No one knows", k(121), "PAN_LR")], []),
  ("The children of the forest creating them is the show's idea, not Martin's.", [("The children", k(122), "PUSH_IN")], []),
 ]),

 ("VIII", "The Ranger with Cold Hands", "VIII", [
  ("But Martin's books are full of legends that turn out to be real.", [("But Martin's", k(123), "PUSH_IN")], []),
  ("In the last published novel, a strange rider guides Bran north.", [("In the last", k(124), "PAN_LR")], []),
  ("He wears the black of the Night's Watch, rides a great elk, and hides his face behind a scarf.", [("He wears", k(6), "PAN_LR")], []),
  ("His hands are black, and cold as iron.", [("His hands", k(125), "PUSH_IN")], []),
  ("He cannot cross the Wall.", [("He cannot", k(126), "TILT_UP")], []),
  ("\"There are spells woven into it,\" he says, \"old ones, and strong.\"", [("\"There are", k(127), "DRIFT")], []),
  ("The children of the forest put it more simply: \"They killed him long ago.\"", [("The children", k(128), "PUSH_IN")], []),
  ("Readers call him Coldhands.", [("Readers", k(129), "PUSH_IN")],
   [("Readers", N, {"name": "COLDHANDS", "role": "A Dance with Dragons"}, 3.2)]),
  ("Some believe he is a forgotten brother of the Watch.", [("Some believe", k(130), "DRIFT")], []),
  ("A few wonder if he is something older.", [("A few", k(131), "PULL_OUT")], []),
  ("And beyond the Wall, the wildlings have been searching for something.", [("And beyond", k(132), "PAN_RL")], []),
  ("\"We opened half a hundred graves,\" the wildling girl Ygritte cries, \"and never found the Horn of Joramun.\"",
   [("\"We opened", k(133), "PULL_OUT"), ("the wildling", k(134), "PUSH_IN")], []),
  ("The horn of the very king who brought down the Night's King.", [("The horn", k(7), "TILT_UP")], []),
  ("Martin has explained none of it.", [("Martin has", k(135), "PUSH_IN")], []),
  ("The Winds of Winter, the book that should bring the Long Night, is still unpublished, fifteen years after the last.",
   [("The Winds", k(136), "PUSH_IN")], []),
  ("So for now, the Night's King remains what Old Nan made him.", [("So for now", k(137), "DRIFT")], []),
  ("A man by day.", [("A man by", k(74), "DRIFT")], []),
  ("A legend by night.", [("A legend", k(138), "TILT_UP")], []),
  ("And a Stark, perhaps, whose name was Brandon.", [("And a Stark", k(139), "PUSH_IN")], []),
 ]),

 ("CB", "Outro", None, [
  ("So, was the Night's King a traitor who gave his soul to the enemy, or a man who saw the truth about the Others before anyone else?",
   [("So, was", k(140), "PUSH_IN")],
   [("So, was", END, {"kicker": "WATCH NEXT", "title": "BEFORE THE FIRST MEN", "brand": "A MYTHIC ARCHIVES PRODUCTION",
                      "sub": "The Ancient World of Westeros  ·  coming to the archive", "q": "TRAITOR — OR PROPHET?",
                      "q_at": "So, was", "comment_at": "comments", "like_at": "like", "sub_at": "subscribe"}, 0)]),
  ("Tell us what you think in the comments.", [], []),
  ("If this story stayed with you, give the video a like, and subscribe to the Mythic Archives.", [], []),
  ("The archive is always open.", [("The archive", k(150), "PULL_OUT")], []),
 ]),
]

IDENT_SHOT = (k(141), "PUSH_IN", {"title": "THE MYTHIC ARCHIVES", "tag": "WESTEROS  •  ARRAKIS  •  MIDDLE-EARTH",
                                   "sub": "A MYTHIC ARCHIVES PRODUCTION  ·  WESTEROS  ·  RECORD 001"})
END_HOLD = 6.0
MAPS = {}


def narration(section):
    return " ".join(l[0] for l in section[3])


PROLOGUE = '0:00 Prologue: The Castle of Ghosts'

SPECIAL_PAUSE = {
    'so who was he really?': 0.9, 'from the memory of man.': 1.0, 'and want to walk into it.': 0.9,
    'he gave her his soul.': 0.9, 'ruled the wall.': 1.0, 'what he was called.': 1.0,
    'mayhaps his name was brandon."': 1.0, 'their greatest ally.': 1.0, 'hard not to wonder.': 1.0,
    'none of that happens in the books.': 1.1, 'not martin\'s.': 1.0, 'whose name was brandon.': 1.4,
}


def music_edl(S, total, ident, phrase_after, phrase_end):
    """GOT001 cue sheet: Kevin MacLeod (incompetech, CC BY 4.0), same approach and loudness as DUN001.
    Track choices are provisional; the CI mix check validates them."""
    def cue(cid, name, track, start, end, offset, fade_in=1.5, fade_out=2.5, gain_db=0, **kw):
        return dict(cue=cid, name=name, track=track, start=round(start, 2), end=round(end, 2), offset=offset,
                    fade_in=fade_in, fade_out=fade_out, gain_db=gain_db, **kw)
    cues = [
        cue('M1', 'King of the Dead (hook)', 'Phantasm', 0.0, ident[0] + 1.2, 14.0, fade_in=0.0, gain_db=-2, hp=110),
        cue('M2', 'Archive (ident)', 'Deliberate_Thought', ident[0] - 1.2, S['P']['start'] + 2.0, 30.0, fade_in=1.2, gain_db=-1),
        cue('M3', 'Castle of Ghosts', 'Ossuary_6_Air', S['P']['start'] - 0.4, S['I']['gap_start'] + 0.6, 0.0),
        cue('M4', 'The Thirteenth Lord Commander', 'Lightless_Dawn', S['I']['gap_start'] - 0.4, S['II']['gap_start'] + 0.6, 0.0),
        cue('M5', 'The Corpse Queen', 'Long_Note_Two', S['II']['gap_start'] - 0.4, S['CA']['gap_start'] + 1.0, 34.0),
        cue('M2b', 'Subscribe (archive theme)', 'Deliberate_Thought', S['CA']['gap_start'] - 0.2, S['III']['gap_start'] + 0.8,
            30.0, fade_in=1.0, fade_out=2.0, gain_db=-1),
        cue('M6', 'Two Kings Against One', 'Dark_Times', S['III']['gap_start'] - 0.4, S['IV']['gap_start'] + 0.6, 3.0),
        cue('M7', 'A Stark of Winterfell', 'Private_Reflection', S['IV']['gap_start'] - 0.4, S['V']['gap_start'] + 0.6, 0.0),
        cue('M8', 'The Black Gate', 'Night_Vigil', S['V']['gap_start'] - 0.4, S['VI']['gap_start'] + 0.6, 60.0),
        cue('M9', 'The King of the Dead', 'Crypto', S['VI']['gap_start'] - 0.4, S['VII']['gap_start'] + 0.6, 2.0, gain_db=-1),
        cue('M10', "Martin's Answer", 'Lightless_Dawn', S['VII']['gap_start'] - 0.4, S['VIII']['gap_start'] + 0.6, 170.0),
        cue('M11', 'The Ranger with Cold Hands', 'Unwritten_Return', S['VIII']['gap_start'] - 0.4, S['CB']['gap_start'] + 1.6,
            12.0, fade_out=3.5, gain_db=-1),
        cue('M12', 'Outro (archive theme)', 'Deliberate_Thought', S['CB']['gap_start'] - 0.6, total, 30.0,
            fade_in=2.0, fade_out=3.0, gain_db=-2),
    ]
    return dict(episode='GOT001', timeline=f'voice-14 VO, programme {total} s', bed_lufs=-23.0,
                notes='start/end = programme seconds; offset = seconds into the source track. Kevin MacLeod '
                      '(incompetech.com), CC BY 4.0.',
                cues=cues,
                sfx=[dict(type='wind', start=0.0, end=20.0, level_db=-38, note='cold wind under the hook')],
                silences=[])
