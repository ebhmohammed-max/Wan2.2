"""LOTR001: "Who Was Sauron Before He Was Evil?" (MIDDLE-EARTH · RECORD 001).

Same format as data/got001.py: SECTIONS = (sid, name, chapter num or None, [(narration, [shots], [graphics])]).
  shot    = (anchor, image_key, recipe[, focus])  - cut lands on the first word of `anchor`
  graphic = (anchor, KIND, {params}, dur_s)
Narration must match the voice-14 takes word for word (script 17_scripts/LOTR001_SCRIPT_v1.0.md,
approved 2026-11-25 "go on"). Takes: CLIPS below (10 takes; H+P and II+CA share a take).
Canon: books first; never name the author ("in the books"); late notes labelled; films/show labelled.
Shots and graphics are filled in after the shot list (data/lotr001_images.py).
"""

TITLE = "Who Was Sauron Before He Was Evil?"
EPISODE = "LOTR001"
RECORD = "MIDDLE-EARTH · RECORD 001"
GAP_AFTER_HOOK = 6.0
GAP_CHAPTER = 1.8

N, PL, YR, NOTE, STAT, CH, TTL, IDENT, DOSSIER, FILE, END = (
    'NAME', 'PLACE', 'YEAR', 'NOTE', 'STAT', 'CHAPTER', 'TITLE', 'IDENT', 'DOSSIER', 'FILE', 'END')


def k(n):
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


SECTIONS = [
 ('H', 'Hook', None, [
  ("On screen, he is an eye.", [("On screen,", k(11), "PUSH_IN")], []),
  ("A great eye of fire, burning on top of a black tower, watching everything.", [("A great", k(12), "PUSH_IN")], []),
  ("But the books tell a very different story.", [("But the", k(13), "PUSH_IN")], []),
  ("In the books, one of the wisest Elves in Middle-earth says something strange about him.", [("In the", k(7), "PUSH_IN")], []),
  ("\"For nothing is evil in the beginning.", [], []),
  ("Even Sauron was not so.\"", [("Even Sauron", k(14), "DRIFT")], []),
  ("Before the Dark Lord, before the Ring, before the Eye, he had another name.", [("Before the", k(15), "PUSH_IN")], []),
  ("A name that meant admirable.", [("A name", k(1), "PUSH_IN")], []),
  ("So who was Sauron, before he was evil?", [("So who", k(16), "PUSH_IN")], []),
 ]),

 ('P', 'Prologue: The Council of Elrond', None, [
  ("In Rivendell, in the autumn, a council gathers in the house of Elrond.", [("In Rivendell,", k(17), "PULL_OUT")], []),
  ("Elves, Dwarves, Men, two hobbits, and a third hobbit hiding in the corner, uninvited.", [("Elves, Dwarves,", k(18), "PAN_LR"), ("and a third", k(19), "PUSH_IN")], []),
  ("Frodo holds up a little ring of gold.", [("Frodo holds", k(20), "PUSH_IN")], []),
  ("Plain, smooth, and the most dangerous thing in the world.", [("Plain, smooth,", k(21), "PUSH_IN")], []),
  ("A man of Gondor asks: why not use it against the Enemy?", [("A man", k(22), "PUSH_IN")], []),
  ("And Elrond says no.", [("And Elrond", k(23), "PUSH_IN")], []),
  ("Whoever wields it will only become the next Dark Lord.", [("Whoever wields", k(24), "PUSH_IN")], []),
  ("\"For nothing is evil in the beginning,\" he says.", [("\"For nothing", k(25), "PUSH_IN")], []),
  ("\"Even Sauron was not so.\"", [], []),
  ("It is a single line, and the story moves on.", [("It is", k(17), "DRIFT")], []),
  ("But the books never forget it.", [("But the", k(26), "PUSH_IN")], []),
  ("They tell us exactly how a spirit of light became the Dark Lord.", [("They tell", k(10), "PUSH_IN")], []),
  ("And it begins long before the Sun, in a forge.", [("And it", k(27), "PUSH_IN")], []),
 ]),

 ('I', "The Smith's Apprentice", 'I', [
  ("Before the world was made, there were spirits.", [("Before the", k(28), "DRIFT")], []),
  ("The greatest were the Valar, the powers of the world.", [("The greatest", k(29), "TILT_UP")], []),
  ("Beneath them served the Maiar: lesser spirits, but mightier than any king.", [("Beneath them", k(30), "PAN_LR")], []),
  ("One of the Valar was Aulë, the smith.", [("One of", k(9), "PULL_OUT")], []),
  ("He shaped the mountains and loved stone, and metal, and gems.", [("He shaped", k(31), "PULL_OUT")], []),
  ("He loved making things, and he loved to teach.", [("He loved", k(32), "PUSH_IN")], []),
  ("Among the Maiar of his forge, one stood out.", [("Among the", k(33), "PUSH_IN")], []),
  ("The books say he was mighty in the lore of Aulë's people, and remained so to the end.", [("The books", k(34), "PUSH_IN")], []),
  ("In notes published long after the books, we even learn his first name.", [("In notes", k(35), "PUSH_IN")], []),
  ("Mairon.", [("Mairon.", k(1), "PUSH_IN")], []),
  ("In the elvish tongue, it means the admirable.", [], []),
  ("And he was.", [], []),
  ("His gift was order.", [("His gift", k(36), "PAN_LR")], []),
  ("He loved planning, and structure, and things working as they were meant to.", [("He loved", k(37), "DRIFT")], []),
  ("He disliked confusion, and waste.", [("He disliked", k(38), "PUSH_IN")], []),
  ("It was his virtue.", [], []),
  ("And according to those same notes, it was also the cause of his fall.", [("And according", k(39), "PUSH_IN")], []),
 ]),

 ('II', 'The Admirable and the Abhorred', 'II', [
  ("Among the Valar, one would not wait.", [("Among the", k(40), "PUSH_IN")], []),
  ("Melkor, the mightiest of them all, wanted to shape the world alone, quickly, and his way.", [("Melkor, the", k(41), "PULL_OUT")], []),
  ("The others worked slowly.", [("The others", k(42), "DRIFT")], []),
  ("They debated, and waited, and let things grow.", [], []),
  ("To a mind like Mairon's, it must have looked like chaos.", [("To a", k(43), "PUSH_IN")], []),
  ("Melkor looked like a master who got things done.", [("Melkor looked", k(44), "TILT_UP")], []),
  ("That, the notes say, is what first drew Mairon to him.", [("That, the", k(45), "PUSH_IN")], []),
  ("Not cruelty.", [("Not cruelty.", k(46), "PAN_LR")], []),
  ("Efficiency.", [], []),
  ("In the beginning of the world, the books say, Melkor seduced him to his side.", [("In the", k(47), "PUSH_IN")], []),
  ("The smith's apprentice left the light and knelt before his new master in the dark.", [("The smith's", k(48), "PULL_OUT")], []),
  ("Melkor became Morgoth, the Black Foe of the World.", [("Melkor became", k(49), "TILT_UP")], []),
  ("And Mairon was given a new name by those who feared him.", [("And Mairon", k(50), "DRIFT")], []),
  ("Sauron.", [("Sauron.", k(3), "PUSH_IN")], []),
  ("The abhorred.", [], []),
  ("The Grey Elves called him Gorthaur the Cruel.", [], []),
  ("The books say he was less evil than his master in only one way.", [("The books", k(51), "PUSH_IN")], []),
  ("For a long time, he served another, and not himself.", [("For a", k(52), "PULL_OUT")], []),
 ]),

 ('CA', 'Subscribe', None, [
  ("If you want to see Middle-earth the way it is in the books, subscribe to the Mythic Archives.", [("If you", k(53), "PULL_OUT")], []),
  ("Because the next part of this story takes place on an island of werewolves.", [("Because the", k(54), "PUSH_IN")], []),
 ]),

 ('III', 'The Isle of Werewolves', 'III', [
  ("In the wars of the First Age, the Elves held a white tower on an island in the river Sirion.", [("In the", k(55), "PULL_OUT")], []),
  ("Sauron took it.", [("Sauron took", k(56), "PUSH_IN")], []),
  ("Fear went before him, and the defenders fled.", [("Fear went", k(57), "PAN_RL")], []),
  ("The fair island became Tol-in-Gaurhoth, the Isle of Werewolves.", [("The fair", k(58), "PUSH_IN")], []),
  ("The books now call him a sorcerer of dreadful power, master of shadows and of phantoms, misshaping what he touched, twisting what he ruled.", [("The books", k(59), "PUSH_IN"), ("misshaping what", k(60), "DRIFT")], []),
  ("Lord of werewolves.", [("Lord of", k(61), "PAN_LR")], []),
  ("But his truest weapon was the lie.", [("But his", k(62), "PUSH_IN")], []),
  ("He lured an outlaw named Gorlim with a phantom of his wife's face at a lighted window, and promised to give her back if Gorlim betrayed his leader.", [("He lured", k(63), "PUSH_IN"), ("and promised", k(64), "PUSH_IN")], []),
  ("Gorlim broke.", [("Gorlim broke.", k(65), "PUSH_IN")], []),
  ("Then Sauron told him she was already dead.", [], []),
  ("One day, a band of Orcs passed the tower without reporting to him.", [("One day,", k(66), "PAN_LR")], []),
  ("Sauron had them seized.", [("Sauron had", k(67), "PUSH_IN")], []),
  ("They were not Orcs.", [("They were", k(68), "PUSH_IN")], []),
  ("They were Finrod Felagund, the golden-haired Elf-king, and a mortal man named Beren, in disguise.", [("They were", k(5), "PUSH_IN"), ("and a mortal", k(69), "PUSH_IN")], []),
  ("Finrod and Sauron fought, not with swords, but with songs of power.", [("Finrod and", k(70), "PUSH_IN")], []),
  ("Sauron sang of piercing, of opening, of treachery.", [("Sauron sang", k(71), "PUSH_IN")], []),
  ("Finrod sang of secrets kept, of the prison opening, and the chain that snaps.", [("Finrod sang", k(72), "PUSH_IN")], []),
  ("Sauron was stronger.", [("Sauron was", k(71), "PULL_OUT")], []),
  ("And Felagund fell before the throne.", [("And Felagund", k(73), "PULL_OUT")], []),
 ]),

 ('IV', 'Lúthien and the Hound', 'IV', [
  ("The prisoners were thrown into a pit.", [("The prisoners", k(74), "TILT_UP")], []),
  ("One by one, a wolf came for them in the dark, and not one betrayed the others.", [("One by", k(75), "PUSH_IN")], []),
  ("When at last it came for Beren, the Elf-king broke his chains and fought it with his bare hands.", [("the Elf-king", k(76), "PUSH_IN")], []),
  ("He saved his friend, and it cost him his life.", [("He saved", k(77), "PUSH_IN")], []),
  ("Then, from the bridge, there came a song.", [("Then, from", k(78), "PUSH_IN")], []),
  ("Lúthien had come.", [("Lúthien had", k(4), "PUSH_IN")], []),
  ("Her robe was blue as the unclouded heaven, her eyes grey as the starlit evening, her hair dark as the shadows of twilight.", [("Her robe", k(79), "TILT_UP"), ("her hair", k(80), "PUSH_IN")], []),
  ("Beside her walked Huan, the great hound of Valinor.", [("Beside her", k(8), "PUSH_IN")], []),
  ("Sauron sent his wolves to the bridge, one after another, and Huan slew each one in silence.", [("Sauron sent", k(81), "PUSH_IN"), ("and Huan", k(82), "PULL_OUT")], []),
  ("So Sauron went himself, in the shape of a werewolf, the greatest that had yet been.", [("So Sauron", k(83), "PUSH_IN")], []),
  ("Lúthien cast a fold of her dark cloak before his eyes.", [("Lúthien cast", k(84), "PUSH_IN")], []),
  ("And Huan sprang.", [("And Huan", k(85), "PUSH_IN")], []),
  ("Wolf, serpent, his own true shape.", [("Wolf, serpent,", k(86), "PUSH_IN")], []),
  ("Nothing Sauron became could break the hound's hold.", [], []),
  ("At last he yielded, and gave Lúthien the mastery of the tower.", [("At last", k(87), "PULL_OUT")], []),
  ("He fled as a vampire, great as a dark cloud across the moon.", [("He fled", k(88), "PAN_LR")], []),
 ]),

 ('V', 'The Door Back', 'V', [
  ("At the end of the First Age, the hosts of the Valar came in their wrath.", [("At the", k(89), "PULL_OUT")], []),
  ("Morgoth's fortress was broken, and Morgoth was thrust out of the world.", [("Morgoth's fortress", k(90), "PULL_OUT")], []),
  ("And Sauron did something no one expects from the Dark Lord.", [("And Sauron", k(91), "PUSH_IN")], []),
  ("He put on his fair form again, bowed before the herald of the Valar, and renounced all his evil deeds.", [("He put", k(92), "PUSH_IN"), ("bowed before", k(93), "PUSH_IN")], []),
  ("The books add a remarkable line: some hold that this was not falsely done.", [("The books", k(94), "PUSH_IN")], []),
  ("That Sauron truly repented, if only out of fear.", [], []),
  ("The herald told him to go into the West and face the judgement of the Valar.", [("The herald", k(95), "PUSH_IN")], []),
  ("It might mean a long servitude, to prove his good faith.", [], []),
  ("And Sauron could not bear it.", [("And Sauron", k(96), "PUSH_IN")], []),
  ("Under Morgoth, his power had been great.", [("Under Morgoth,", k(97), "PULL_OUT")], []),
  ("He was ashamed, and he would not return in humiliation.", [], []),
  ("So he hid himself in Middle-earth, and fell back into evil, for the bonds Morgoth had laid upon him were very strong.", [("So he", k(98), "PULL_OUT"), ("for the bonds", k(99), "PUSH_IN")], []),
  ("This is the hinge of his whole story.", [("This is", k(100), "PUSH_IN")], []),
  ("Not hatred.", [("Not hatred.", k(101), "PUSH_IN")], []),
  ("Pride.", [], []),
 ]),

 ('VI', 'The Lord of Gifts', 'VI', [
  ("He told himself a story.", [("He told", k(102), "PAN_LR")], []),
  ("The Valar had abandoned Middle-earth.", [], []),
  ("Someone had to heal it, and order it.", [("Someone had", k(103), "PUSH_IN")], []),
  ("Why not him?", [], []),
  ("In the Second Age, a stranger came to the Elves.", [("In the", k(104), "PUSH_IN")], []),
  ("He was fair, and wise, and generous, and he called himself Annatar, the Lord of Gifts.", [("He was", k(2), "PUSH_IN")], []),
  ("The High King, Gil-galad, would not let him in.", [("The High", k(105), "PUSH_IN")], []),
  ("But in Eregion, beside the walls of Moria, the Elven-smiths welcomed him.", [("But in", k(106), "PULL_OUT")], []),
  ("Their lord was Celebrimbor, grandson of Fëanor, and they hungered for knowledge.", [("Their lord", k(6), "PUSH_IN")], []),
  ("Annatar taught them.", [("Annatar taught", k(107), "PUSH_IN")], []),
  ("And with his teaching, they forged the Rings of Power.", [("And with", k(108), "PUSH_IN")], []),
  ("Then, in secret, in the Mountain of Fire, he made a ring of his own.", [("Then, in", k(109), "PUSH_IN")], []),
  ("One Ring, to rule all the others.", [("One Ring,", k(110), "PUSH_IN")], []),
  ("Into it he poured a great part of his own power.", [("Into it", k(111), "PUSH_IN")], []),
  ("But the moment he set it on his finger, the Elves were aware of him.", [("But the", k(112), "PUSH_IN"), ("the Elves", k(113), "PUSH_IN")], []),
  ("They knew him, and saw that he meant to master them.", [("They knew", k(114), "PUSH_IN")], []),
  ("In anger and fear, they took off their rings.", [("In anger", k(115), "PUSH_IN")], []),
  ("Three rings Celebrimbor had made alone, without Annatar's touch.", [("Three rings", k(116), "PUSH_IN")], []),
  ("Those, Sauron never found.", [], []),
  ("He took Celebrimbor and tormented him, and the lord of Eregion died without giving up the Three.", [("He took", k(117), "PULL_OUT"), ("and the lord", k(118), "PUSH_IN")], []),
  ("On television, before Annatar, he wore the face of a man called Halbrand, a lost king of the Southlands.", [("On television,", k(119), "DRIFT")], []),
  ("Halbrand is the show's invention.", [], []),
  ("In the books, Eregion knew only one mask: the Lord of Gifts.", [("In the", k(120), "PUSH_IN")], []),
 ]),

 ('VII', 'The Drowning of Númenor', 'VII', [
  ("Then came the Men of Númenor, the greatest kingdom of Men that ever was.", [("Then came", k(121), "PULL_OUT")], []),
  ("Their king, Ar-Pharazôn the Golden, landed with such a host that Sauron's armies fled.", [("Their king,", k(122), "PULL_OUT")], []),
  ("So Sauron humbled himself before the king, and let himself be carried across the sea.", [("So Sauron", k(123), "PUSH_IN")], []),
  ("A prisoner.", [("A prisoner.", k(124), "PUSH_IN")], []),
  ("Within three years, he was the king's closest counsellor.", [("Within three", k(125), "PUSH_IN")], []),
  ("He had the White Tree of the kings cut down, and raised a great temple to Melkor in its place.", [("He had", k(126), "PUSH_IN"), ("and raised", k(127), "TILT_UP")], []),
  ("At last he persuaded the king to sail against the Undying Lands themselves, to seize the life that never ends.", [("At last", k(128), "PAN_LR")], []),
  ("And the world was changed.", [("And the", k(129), "TILT_UP")], []),
  ("The sea opened, and Númenor fell into the abyss.", [("The sea", k(130), "PULL_OUT")], []),
  ("Sauron was in his temple when it went down.", [("Sauron was", k(127), "PUSH_IN")], []),
  ("His body was destroyed, and his spirit fled back over the dark water to Mordor.", [("His body", k(131), "PAN_LR")], []),
  ("But he had lost something forever.", [("But he", k(132), "PUSH_IN")], []),
  ("The books say he could never again take a form that seemed fair to Men.", [("The books", k(10), "PUSH_IN")], []),
  ("And the later notes add one last detail.", [("And the", k(35), "PUSH_IN")], []),
  ("Until the downfall of Númenor, he still called himself Mairon, the admirable.", [("Until the", k(1), "PUSH_IN")], []),
  ("After the drowning, the admirable was gone.", [("After the", k(133), "PULL_OUT")], []),
 ]),

 ('VIII', 'Four Fingers on the Black Hand', 'VIII', [
  ("He rebuilt.", [("He rebuilt.", k(134), "TILT_UP")], []),
  ("When the Last Alliance of Elves and Men besieged his tower, Sauron came out and fought Gil-galad and Elendil himself, and both of them fell.", [("When the", k(135), "PULL_OUT"), ("and both", k(136), "PUSH_IN")], []),
  ("Then Isildur cut the Ring from his hand.", [("Then Isildur", k(137), "PUSH_IN")], []),
  ("Isildur wrote that it was hot as a burning coal, and that his hand was scorched.", [("Isildur wrote", k(138), "PUSH_IN")], []),
  ("And here, the films and the books part ways.", [("And here,", k(13), "PUSH_IN")], []),
  ("On screen, the Eye is the Dark Lord himself, a giant fire on top of his tower.", [("On screen,", k(11), "PUSH_IN")], []),
  ("In the books, the Lidless Eye is his emblem, painted red on his soldiers' shields, and the Eye rimmed with fire appears in visions.", [("In the", k(139), "PAN_LR"), ("and the Eye", k(140), "PUSH_IN")], []),
  ("The books' Sauron has a body.", [("The books'", k(10), "PUSH_IN")], []),
  ("In the Dead Marshes, Gollum, who was tormented in Mordor, whispers to Frodo, \"He has only four on the Black Hand.", [("In the", k(141), "PAN_LR"), ("whispers to", k(142), "PUSH_IN")], []),
  ("But they are enough.\"", [], []),
  ("Four fingers.", [("Four fingers.", k(143), "PUSH_IN")], []),
  ("Most readers believe the missing one is the finger Isildur cut away, three thousand years before.", [], []),
  ("And when the Ring finally falls into the fire, a huge shape of shadow rises over Mordor, crowned with lightning, and stretches out a vast, threatening hand.", [("And when", k(144), "PUSH_IN"), ("a huge", k(145), "TILT_UP")], []),
  ("Then a great wind takes it, and it is all blown away.", [("Then a", k(146), "PULL_OUT")], []),
 ]),

 ('CB', 'Outro', None, [
  ("So, who was Sauron, before he was evil?", [("So, who", k(16), "PUSH_IN")], []),
  ("He was Mairon, the admirable.", [("He was", k(1), "PUSH_IN")], []),
  ("A craftsman who loved order so much that he forgot who the order was for.", [("A craftsman", k(147), "PUSH_IN")], []),
  ("He was offered one way back, and his pride closed the door.", [("He was", k(100), "PUSH_IN")], []),
  ("Nothing is evil in the beginning.", [("Nothing is", k(14), "PUSH_IN")], []),
  ("Could he have been saved, or was he lost the first time he knelt in the dark?", [("Could he", k(148), "PUSH_IN")], []),
  ("Tell us in the comments.", [("Tell us", k(149), "PULL_OUT")], []),
  ("Like this video if the books surprised you, and subscribe to the Mythic Archives for the next record from Middle-earth.", [], []),
 ]),

]

# one take may cover several sections (split at the quietest point between them; see tools/v2_timeline.py)
CLIPS = [('H_P', ['H', 'P']), ('I', ['I']), ('II_CA', ['II', 'CA']), ('III', ['III']), ('IV', ['IV']),
         ('V', ['V']), ('VI', ['VI']), ('VII', ['VII']), ('VIII', ['VIII']), ('CB', ['CB'])]

END_HOLD = 6.0
MAPS = {}


def narration(section):
    return " ".join(l[0] for l in section[3])


PROLOGUE = '0:00 Prologue: The Council of Elrond'
SPECIAL_PAUSE = {}
