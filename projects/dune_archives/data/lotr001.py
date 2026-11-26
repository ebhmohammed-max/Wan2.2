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
  ("On screen, he is an eye.", [], []),
  ("A great eye of fire, burning on top of a black tower, watching everything.", [], []),
  ("But the books tell a very different story.", [], []),
  ("In the books, one of the wisest Elves in Middle-earth says something strange about him.", [], []),
  ("\"For nothing is evil in the beginning.", [], []),
  ("Even Sauron was not so.\"", [], []),
  ("Before the Dark Lord, before the Ring, before the Eye, he had another name.", [], []),
  ("A name that meant admirable.", [], []),
  ("So who was Sauron, before he was evil?", [], []),
 ]),

 ('P', 'Prologue: The Council of Elrond', None, [
  ("In Rivendell, in the autumn, a council gathers in the house of Elrond.", [], []),
  ("Elves, Dwarves, Men, two hobbits, and a third hobbit hiding in the corner, uninvited.", [], []),
  ("Frodo holds up a little ring of gold.", [], []),
  ("Plain, smooth, and the most dangerous thing in the world.", [], []),
  ("A man of Gondor asks: why not use it against the Enemy?", [], []),
  ("And Elrond says no.", [], []),
  ("Whoever wields it will only become the next Dark Lord.", [], []),
  ("\"For nothing is evil in the beginning,\" he says.", [], []),
  ("\"Even Sauron was not so.\"", [], []),
  ("It is a single line, and the story moves on.", [], []),
  ("But the books never forget it.", [], []),
  ("They tell us exactly how a spirit of light became the Dark Lord.", [], []),
  ("And it begins long before the Sun, in a forge.", [], []),
 ]),

 ('I', "The Smith's Apprentice", 'I', [
  ("Before the world was made, there were spirits.", [], []),
  ("The greatest were the Valar, the powers of the world.", [], []),
  ("Beneath them served the Maiar: lesser spirits, but mightier than any king.", [], []),
  ("One of the Valar was Aulë, the smith.", [], []),
  ("He shaped the mountains and loved stone, and metal, and gems.", [], []),
  ("He loved making things, and he loved to teach.", [], []),
  ("Among the Maiar of his forge, one stood out.", [], []),
  ("The books say he was mighty in the lore of Aulë's people, and remained so to the end.", [], []),
  ("In notes published long after the books, we even learn his first name.", [], []),
  ("Mairon.", [], []),
  ("In the elvish tongue, it means the admirable.", [], []),
  ("And he was.", [], []),
  ("His gift was order.", [], []),
  ("He loved planning, and structure, and things working as they were meant to.", [], []),
  ("He disliked confusion, and waste.", [], []),
  ("It was his virtue.", [], []),
  ("And according to those same notes, it was also the cause of his fall.", [], []),
 ]),

 ('II', 'The Admirable and the Abhorred', 'II', [
  ("Among the Valar, one would not wait.", [], []),
  ("Melkor, the mightiest of them all, wanted to shape the world alone, quickly, and his way.", [], []),
  ("The others worked slowly.", [], []),
  ("They debated, and waited, and let things grow.", [], []),
  ("To a mind like Mairon's, it must have looked like chaos.", [], []),
  ("Melkor looked like a master who got things done.", [], []),
  ("That, the notes say, is what first drew Mairon to him.", [], []),
  ("Not cruelty.", [], []),
  ("Efficiency.", [], []),
  ("In the beginning of the world, the books say, Melkor seduced him to his side.", [], []),
  ("The smith's apprentice left the light and knelt before his new master in the dark.", [], []),
  ("Melkor became Morgoth, the Black Foe of the World.", [], []),
  ("And Mairon was given a new name by those who feared him.", [], []),
  ("Sauron.", [], []),
  ("The abhorred.", [], []),
  ("The Grey Elves called him Gorthaur the Cruel.", [], []),
  ("The books say he was less evil than his master in only one way.", [], []),
  ("For a long time, he served another, and not himself.", [], []),
 ]),

 ('CA', 'Subscribe', None, [
  ("If you want to see Middle-earth the way it is in the books, subscribe to the Mythic Archives.", [], []),
  ("Because the next part of this story takes place on an island of werewolves.", [], []),
 ]),

 ('III', 'The Isle of Werewolves', 'III', [
  ("In the wars of the First Age, the Elves held a white tower on an island in the river Sirion.", [], []),
  ("Sauron took it.", [], []),
  ("Fear went before him, and the defenders fled.", [], []),
  ("The fair island became Tol-in-Gaurhoth, the Isle of Werewolves.", [], []),
  ("The books now call him a sorcerer of dreadful power, master of shadows and of phantoms, misshaping what he touched, twisting what he ruled.", [], []),
  ("Lord of werewolves.", [], []),
  ("But his truest weapon was the lie.", [], []),
  ("He lured an outlaw named Gorlim with a phantom of his wife's face at a lighted window, and promised to give her back if Gorlim betrayed his leader.", [], []),
  ("Gorlim broke.", [], []),
  ("Then Sauron told him she was already dead.", [], []),
  ("One day, a band of Orcs passed the tower without reporting to him.", [], []),
  ("Sauron had them seized.", [], []),
  ("They were not Orcs.", [], []),
  ("They were Finrod Felagund, the golden-haired Elf-king, and a mortal man named Beren, in disguise.", [], []),
  ("Finrod and Sauron fought, not with swords, but with songs of power.", [], []),
  ("Sauron sang of piercing, of opening, of treachery.", [], []),
  ("Finrod sang of secrets kept, of the prison opening, and the chain that snaps.", [], []),
  ("Sauron was stronger.", [], []),
  ("And Felagund fell before the throne.", [], []),
 ]),

 ('IV', 'Lúthien and the Hound', 'IV', [
  ("The prisoners were thrown into a pit.", [], []),
  ("One by one, a wolf came for them in the dark, and not one betrayed the others.", [], []),
  ("When at last it came for Beren, the Elf-king broke his chains and fought it with his bare hands.", [], []),
  ("He saved his friend, and it cost him his life.", [], []),
  ("Then, from the bridge, there came a song.", [], []),
  ("Lúthien had come.", [], []),
  ("Her robe was blue as the unclouded heaven, her eyes grey as the starlit evening, her hair dark as the shadows of twilight.", [], []),
  ("Beside her walked Huan, the great hound of Valinor.", [], []),
  ("Sauron sent his wolves to the bridge, one after another, and Huan slew each one in silence.", [], []),
  ("So Sauron went himself, in the shape of a werewolf, the greatest that had yet been.", [], []),
  ("Lúthien cast a fold of her dark cloak before his eyes.", [], []),
  ("And Huan sprang.", [], []),
  ("Wolf, serpent, his own true shape.", [], []),
  ("Nothing Sauron became could break the hound's hold.", [], []),
  ("At last he yielded, and gave Lúthien the mastery of the tower.", [], []),
  ("He fled as a vampire, great as a dark cloud across the moon.", [], []),
 ]),

 ('V', 'The Door Back', 'V', [
  ("At the end of the First Age, the hosts of the Valar came in their wrath.", [], []),
  ("Morgoth's fortress was broken, and Morgoth was thrust out of the world.", [], []),
  ("And Sauron did something no one expects from the Dark Lord.", [], []),
  ("He put on his fair form again, bowed before the herald of the Valar, and renounced all his evil deeds.", [], []),
  ("The books add a remarkable line: some hold that this was not falsely done.", [], []),
  ("That Sauron truly repented, if only out of fear.", [], []),
  ("The herald told him to go into the West and face the judgement of the Valar.", [], []),
  ("It might mean a long servitude, to prove his good faith.", [], []),
  ("And Sauron could not bear it.", [], []),
  ("Under Morgoth, his power had been great.", [], []),
  ("He was ashamed, and he would not return in humiliation.", [], []),
  ("So he hid himself in Middle-earth, and fell back into evil, for the bonds Morgoth had laid upon him were very strong.", [], []),
  ("This is the hinge of his whole story.", [], []),
  ("Not hatred.", [], []),
  ("Pride.", [], []),
 ]),

 ('VI', 'The Lord of Gifts', 'VI', [
  ("He told himself a story.", [], []),
  ("The Valar had abandoned Middle-earth.", [], []),
  ("Someone had to heal it, and order it.", [], []),
  ("Why not him?", [], []),
  ("In the Second Age, a stranger came to the Elves.", [], []),
  ("He was fair, and wise, and generous, and he called himself Annatar, the Lord of Gifts.", [], []),
  ("The High King, Gil-galad, would not let him in.", [], []),
  ("But in Eregion, beside the walls of Moria, the Elven-smiths welcomed him.", [], []),
  ("Their lord was Celebrimbor, grandson of Fëanor, and they hungered for knowledge.", [], []),
  ("Annatar taught them.", [], []),
  ("And with his teaching, they forged the Rings of Power.", [], []),
  ("Then, in secret, in the Mountain of Fire, he made a ring of his own.", [], []),
  ("One Ring, to rule all the others.", [], []),
  ("Into it he poured a great part of his own power.", [], []),
  ("But the moment he set it on his finger, the Elves were aware of him.", [], []),
  ("They knew him, and saw that he meant to master them.", [], []),
  ("In anger and fear, they took off their rings.", [], []),
  ("Three rings Celebrimbor had made alone, without Annatar's touch.", [], []),
  ("Those, Sauron never found.", [], []),
  ("He took Celebrimbor and tormented him, and the lord of Eregion died without giving up the Three.", [], []),
  ("On television, before Annatar, he wore the face of a man called Halbrand, a lost king of the Southlands.", [], []),
  ("Halbrand is the show's invention.", [], []),
  ("In the books, Eregion knew only one mask: the Lord of Gifts.", [], []),
 ]),

 ('VII', 'The Drowning of Númenor', 'VII', [
  ("Then came the Men of Númenor, the greatest kingdom of Men that ever was.", [], []),
  ("Their king, Ar-Pharazôn the Golden, landed with such a host that Sauron's armies fled.", [], []),
  ("So Sauron humbled himself before the king, and let himself be carried across the sea.", [], []),
  ("A prisoner.", [], []),
  ("Within three years, he was the king's closest counsellor.", [], []),
  ("He had the White Tree of the kings cut down, and raised a great temple to Melkor in its place.", [], []),
  ("At last he persuaded the king to sail against the Undying Lands themselves, to seize the life that never ends.", [], []),
  ("And the world was changed.", [], []),
  ("The sea opened, and Númenor fell into the abyss.", [], []),
  ("Sauron was in his temple when it went down.", [], []),
  ("His body was destroyed, and his spirit fled back over the dark water to Mordor.", [], []),
  ("But he had lost something forever.", [], []),
  ("The books say he could never again take a form that seemed fair to Men.", [], []),
  ("And the later notes add one last detail.", [], []),
  ("Until the downfall of Númenor, he still called himself Mairon, the admirable.", [], []),
  ("After the drowning, the admirable was gone.", [], []),
 ]),

 ('VIII', 'Four Fingers on the Black Hand', 'VIII', [
  ("He rebuilt.", [], []),
  ("When the Last Alliance of Elves and Men besieged his tower, Sauron came out and fought Gil-galad and Elendil himself, and both of them fell.", [], []),
  ("Then Isildur cut the Ring from his hand.", [], []),
  ("Isildur wrote that it was hot as a burning coal, and that his hand was scorched.", [], []),
  ("And here, the films and the books part ways.", [], []),
  ("On screen, the Eye is the Dark Lord himself, a giant fire on top of his tower.", [], []),
  ("In the books, the Lidless Eye is his emblem, painted red on his soldiers' shields, and the Eye rimmed with fire appears in visions.", [], []),
  ("The books' Sauron has a body.", [], []),
  ("In the Dead Marshes, Gollum, who was tormented in Mordor, whispers to Frodo, \"He has only four on the Black Hand.", [], []),
  ("But they are enough.\"", [], []),
  ("Four fingers.", [], []),
  ("Most readers believe the missing one is the finger Isildur cut away, three thousand years before.", [], []),
  ("And when the Ring finally falls into the fire, a huge shape of shadow rises over Mordor, crowned with lightning, and stretches out a vast, threatening hand.", [], []),
  ("Then a great wind takes it, and it is all blown away.", [], []),
 ]),

 ('CB', 'Outro', None, [
  ("So, who was Sauron, before he was evil?", [], []),
  ("He was Mairon, the admirable.", [], []),
  ("A craftsman who loved order so much that he forgot who the order was for.", [], []),
  ("He was offered one way back, and his pride closed the door.", [], []),
  ("Nothing is evil in the beginning.", [], []),
  ("Could he have been saved, or was he lost the first time he knelt in the dark?", [], []),
  ("Tell us in the comments.", [], []),
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
