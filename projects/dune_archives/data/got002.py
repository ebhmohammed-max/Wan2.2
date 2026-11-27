"""GOT002: "Before the First Men: The Ancient World of Westeros" (WESTEROS · RECORD 002).

Same format as data/got001.py: SECTIONS = (sid, name, chapter num or None, [(narration, [shots], [graphics])]).
  shot    = (anchor, image_key, recipe[, focus])  - cut lands on the first word of `anchor`
  graphic = (anchor, KIND, {params}, dur_s)
Narration must match the voice-14 takes word for word (script 17_scripts/GOT002_SCRIPT_v1.0.md,
approved 2026-11-27 "go on"; duration 10+ min chosen by the director). Takes: CLIPS below (9 takes).
Canon: books first; never name the author ("in the books"); in-world histories told as accounts; show labelled.
Shots and graphics are filled in after the shot list (data/got002_images.py).
"""

TITLE = "Before the First Men: The Ancient World of Westeros"
EPISODE = "GOT002"
RECORD = "WESTEROS · RECORD 002"
GAP_AFTER_HOOK = 6.0
GAP_CHAPTER = 1.8

N, PL, YR, NOTE, STAT, CH, TTL, IDENT, DOSSIER, FILE, END = (
    'NAME', 'PLACE', 'YEAR', 'NOTE', 'STAT', 'CHAPTER', 'TITLE', 'IDENT', 'DOSSIER', 'FILE', 'END')


def k(n):
    return f'B{(n - 1) // 10 + 1:03d}S{n:03d}'


SECTIONS = [
 ('H', 'Hook', None, [
  ("In every castle of the North, there is a godswood.", [], []),
  ("And at its heart stands a tree with bark as white as bone, leaves as red as blood, and a long, sad face carved into its trunk.", [], []),
  ("The Starks pray before it.", [], []),
  ("But no Stark ever carved it.", [], []),
  ("Long before the first king, before the Wall, before a single man set foot in Westeros, someone else lived here.", [], []),
  ("Small, and quick, and dappled like a deer, with eyes like a cat's.", [], []),
  ("They sang to the trees.", [], []),
  ("And when men came, they broke the world to stop them.", [], []),
  ("So who was here before the First Men?", [], []),
 ]),

 ('P', 'Prologue: The Maester and the Boy', None, [
  ("In the first book, Bran Stark lies broken in Winterfell.", [], []),
  ("He has fallen from a tower, and he will never walk again.", [], []),
  ("To pass the long days, Maester Luwin gives him lessons.", [], []),
  ("One afternoon, the lesson is about the children of the forest.", [], []),
  ("\"They were a people of the Dawn Age,\" the maester says, \"the very first, before kings and kingdoms.\"", [], []),
  ("No castles.", [], []),
  ("No cities.", [], []),
  ("No men at all.", [], []),
  ("Only the children, in the lands we now call the Seven Kingdoms.", [], []),
  ("Bran asks if they are still out there.", [], []),
  ("The maester says they are gone.", [], []),
  ("But the wildling woman Osha, a prisoner in the castle, says something else.", [], []),
  ("She says they still live, beyond the Wall.", [], []),
  ("One of them was lying.", [], []),
 ]),

 ('I', 'The Dawn Age', 'I', [
  ("The books describe them in careful detail.", [], []),
  ("They were small, about the size of human children, but they were not childlike.", [], []),
  ("Their skin was nut-brown, dappled with paler spots like a deer's.", [], []),
  ("Their ears were large.", [], []),
  ("Their eyes were gold and green, slitted like a cat's, made for seeing in the dark.", [], []),
  ("And their hands had only three fingers and a thumb, with sharp black claws instead of nails.", [], []),
  ("They had no cities, no metal, no writing.", [], []),
  ("They lived in caves, in crannogs, and in hidden villages in the trees.", [], []),
  ("Men and women hunted side by side, with bows of weirwood and blades of black volcanic glass.", [], []),
  ("Obsidian.", [], []),
  ("The glass that, thousands of years later, men would call dragonglass.", [], []),
  ("Their gods were the trees themselves.", [], []),
  ("They carved faces into the weirwoods, so the gods could watch over the forest.", [], []),
  ("And a rare few were born with eyes as green as moss, or red as blood.", [], []),
  ("The greenseers.", [], []),
  ("Through the weirwoods, they could see far away, and long ago.", [], []),
  ("They were not alone.", [], []),
  ("The giants lived here too, ten to fourteen feet tall, shaggy with fur, riding mammoths.", [], []),
  ("The two peoples did not always get along.", [], []),
  ("The maesters record a giant's grave in the North, with obsidian arrowheads still lodged in its ribs.", [], []),
  ("For thousands of years, this was the whole world.", [], []),
  ("Then, from the east, came men.", [], []),
 ]),

 ('II', 'The Bridge of Land', 'II', [
  ("In those days, Westeros and the eastern continent were joined by a bridge of land, the Arm of Dorne.", [], []),
  ("Across it came the First Men.", [], []),
  ("The maesters cannot agree when.", [], []),
  ("Some say twelve thousand years ago.", [], []),
  ("Others say eight.", [], []),
  ("They carried bronze swords and great leather shields.", [], []),
  ("They rode horses, animals the children had never seen.", [], []),
  ("And they brought their own gods.", [], []),
  ("At first, the histories say, the children welcomed them.", [], []),
  ("But the First Men cleared the forests for their fields.", [], []),
  ("Then they began to fear the faces in the trees.", [], []),
  ("They believed the children used them to spy.", [], []),
  ("So they burned the weirwoods, and cut them down.", [], []),
  ("And the children went to war.", [], []),
 ]),

 ('CA', 'Subscribe', None, [
  ("What the children did next changed the shape of the continent.", [], []),
  ("If you want Westeros the way it is in the books, subscribe to the Mythic Archives.", [], []),
 ]),

 ('III', 'The Hammer of the Waters', 'III', [
  ("The war lasted for centuries.", [], []),
  ("The children had weirwood bows and obsidian.", [], []),
  ("The First Men had bronze, and numbers.", [], []),
  ("In the riverlands, one legendary warrior earned the name Brandon of the Bloody Blade.", [], []),
  ("The children were losing.", [], []),
  ("So their greenseers turned to the darkest magic they had.", [], []),
  ("Legend says they gathered and called down the hammer of the waters.", [], []),
  ("The sea rose.", [], []),
  ("The land shook.", [], []),
  ("And the Arm of Dorne broke apart.", [], []),
  ("Where the bridge had stood, there was only water, and a broken chain of islands that we now call the Stepstones.", [], []),
  ("It was too late.", [], []),
  ("The door was closed, but the First Men were already through.", [], []),
  ("Legend says the greenseers tried once more, in the North, at the narrow neck of land between the swamps.", [], []),
  ("At the ancient fortress of Moat Cailin, one ruined tower still bears their name: the Children's Tower, where they called upon their gods to bring the hammer down again.", [], []),
  ("Some say that is why the Neck is drowned and full of bogs today.", [], []),
  ("But the Neck held.", [], []),
  ("And the war went on.", [], []),
 ]),

 ('IV', 'The Isle of Faces', 'IV', [
  ("At last, both sides grew weary.", [], []),
  ("In the middle of a great lake in the riverlands, called the Gods Eye, there is a small island.", [], []),
  ("There, the greenseers and wood dancers of the children met the chiefs and heroes of the First Men, and made the Pact.", [], []),
  ("The First Men would take the coasts, the high plains and bright meadows, the mountains and the bogs.", [], []),
  ("The deep woods would belong to the children forever.", [], []),
  ("And no more weirwoods would be put to the axe, anywhere in the realm.", [], []),
  ("So that the gods could witness it, a face was carved into every tree on the island.", [], []),
  ("From that day it was called the Isle of Faces.", [], []),
  ("A secret order, the green men, was formed to guard it.", [], []),
  ("In the books, some say they guard it still.", [], []),
  ("What followed were four thousand years of friendship.", [], []),
  ("The Age of Heroes.", [], []),
  ("In time, the First Men put aside the gods they had brought with them, and worshipped the old gods of the forest.", [], []),
  ("When the Long Night fell, men and children fought side by side.", [], []),
  ("And according to the Night's Watch, the children once gave the brothers a hundred obsidian daggers every year.", [], []),
 ]),

 ('V', 'The Seven-Pointed Star', 'V', [
  ("Then, the books say, a new people crossed the narrow sea.", [], []),
  ("The Andals.", [], []),
  ("They had iron and steel.", [], []),
  ("And they had a new faith, the Seven, with seven-pointed stars carved into their own chests.", [], []),
  ("To the Andals, the faces in the trees were idols.", [], []),
  ("They cut down the weirwoods, hunted the children who were left, and swept away the kingdoms of the First Men, one by one.", [], []),
  ("In the riverlands, there is a hill called High Heart.", [], []),
  ("Around its crown stand thirty-one white stumps, the remains of a sacred weirwood grove.", [], []),
  ("The songs say an Andal king killed the children there and cut the grove down.", [], []),
  ("The smallfolk say the hill is still haunted by their ghosts.", [], []),
  ("But one kingdom never fell.", [], []),
  ("At Moat Cailin, the Andals were broken against the ruins and the bogs.", [], []),
  ("The North stayed a land of the First Men.", [], []),
  ("That is why, thousands of years later, the Starks still pray before a heart tree, and not in a sept.", [], []),
 ]),

 ('VI', 'The Show and the Books', 'VI', [
  ("On television, the children of the forest have skin like bark and leaves growing from their bodies.", [], []),
  ("And in one scene, they bind a First Man to a weirwood, and drive a blade of dragonglass into his heart.", [], []),
  ("He becomes the first White Walker.", [], []),
  ("The children, the show says, created their own destroyer.", [], []),
  ("None of that is in the books.", [], []),
  ("In the books, the children are not plants.", [], []),
  ("They are small, dappled, golden-eyed hunters with claws.", [], []),
  ("And the books never say where the Others came from.", [], []),
  ("Nothing in them blames the children.", [], []),
  ("In the books, the children were the ones who stood beside men when the cold came.", [], []),
 ]),

 ('VII', 'The Last Singers', 'VII', [
  ("Beyond the Wall, in the last published novel, Bran finally finds them.", [], []),
  ("They save him from the dead in the snow, and carry him into a cave beneath a hollow hill.", [], []),
  ("One of them is called Leaf.", [], []),
  ("She tells him that \"children\" is only what men call them.", [], []),
  ("The giants call them the little squirrel people.", [], []),
  ("Their own name is older: those who sing the song of earth.", [], []),
  ("\"Before your Old Tongue was spoken,\" she says, \"we had been singing our songs for ten thousand years.\"", [], []),
  ("Deep in the cave, Bran meets the last greenseer: a pale, withered man, half swallowed by the roots of a weirwood, his one red eye glowing in the dark.", [], []),
  ("Through the trees, Bran begins to see the past.", [], []),
  ("In one vision, he watches the First Men offer blood to the heart tree of Winterfell.", [], []),
  ("He tastes it in his mouth.", [], []),
  ("Where are the rest of them?", [], []),
  ("Leaf answers that the singers have gone into the earth, into the stones, and into the trees.", [], []),
  ("\"That was in the dawn of days, when our sun was rising,\" she says.", [], []),
  ("\"Now it sinks, and this is our long dwindling.\"", [], []),
  ("The giants are almost gone too.", [], []),
  ("The mammoths are down to a few hundred.", [], []),
  ("\"In the world that men have made,\" she says, \"there is no room for them, or us.\"", [], []),
  ("But the old weapons still work.", [], []),
  ("On a hill beyond the Wall, the Night's Watch finds a buried bundle of dragonglass.", [], []),
  ("Months later, a frightened young brother named Samwell Tarly drives a dragonglass dagger into one of the Others, and it melts away.", [], []),
  ("The children's glass, waiting in the ground for eight thousand years.", [], []),
 ]),

 ('CB', 'Outro', None, [
  ("So, who was here before the First Men?", [], []),
  ("A small, singing people who carved the gods into the trees, and broke the land itself to defend them.", [], []),
  ("They lost their world.", [], []),
  ("But they kept their bargain, and taught the newcomers to pray.", [], []),
  ("Were the First Men invaders who stole a world, or did the Pact make them its guardians?", [], []),
  ("Tell us what you think in the comments.", [], []),
  ("Like this video if the books surprised you, and subscribe to the Mythic Archives.", [], []),
  ("The archive is always open.", [], []),
 ]),

]

# one take may cover several sections (split at the quietest point between them; see tools/v2_timeline.py)
CLIPS = [('H_P', ['H', 'P']), ('I', ['I']), ('II_CA', ['II', 'CA']), ('III', ['III']), ('IV', ['IV']), ('V', ['V']), ('VI', ['VI']), ('VII', ['VII']), ('CB', ['CB'])]

END_HOLD = 6.0
MAPS = {}


def narration(section):
    return " ".join(l[0] for l in section[3])


PROLOGUE = '0:00 Prologue: The Maester and the Boy'
SPECIAL_PAUSE = {}
