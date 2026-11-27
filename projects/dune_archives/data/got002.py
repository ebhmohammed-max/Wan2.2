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
  ('In every castle of the North, there is a godswood.', [('In every', k(11), 'PUSH_IN')], []),
  ('And at its heart stands a tree with bark as white as bone, leaves as red as blood, and a long, sad face carved into its trunk.', [('And at', k(10), 'PUSH_IN'), ('and a long', k(12), 'PUSH_IN')], []),
  ('The Starks pray before it.', [('The Starks', k(13), 'DRIFT')], []),
  ('But no Stark ever carved it.', [('But no', k(14), 'PUSH_IN')], []),
  ('Long before the first king, before the Wall, before a single man set foot in Westeros, someone else lived here.', [('Long before', k(15), 'PULL_OUT')], []),
  ("Small, and quick, and dappled like a deer, with eyes like a cat's.", [('Small, and', k(16), 'PUSH_IN')], []),
  ('They sang to the trees.', [('They sang', k(17), 'DRIFT')], []),
  ('And when men came, they broke the world to stop them.', [('And when', k(18), 'PUSH_IN')], []),
  ('So who was here before the First Men?', [('So who', k(19), 'PUSH_IN')], [('So who', TTL, {'kicker': 'THE MYTHIC ARCHIVES PRESENTS', 'title': 'BEFORE THE FIRST MEN', 'sub': 'The Ancient World of Westeros'}, 0)]),
 ]),

 ('P', 'Prologue: The Maester and the Boy', None, [
  ('In the first book, Bran Stark lies broken in Winterfell.', [('In the', k(20), 'PUSH_IN')], [('Bran Stark', PL, {'place': 'WINTERFELL', 'sub': 'A Game of Thrones · the first book'}, 4.0)]),
  ('He has fallen from a tower, and he will never walk again.', [('He has', k(21), 'TILT_UP')], []),
  ('To pass the long days, Maester Luwin gives him lessons.', [('To pass', k(22), 'PUSH_IN')], [('Maester Luwin', N, {'name': 'MAESTER LUWIN', 'role': 'Maester of Winterfell'}, 3.2)]),
  ('One afternoon, the lesson is about the children of the forest.', [('One afternoon,', k(23), 'PUSH_IN')], []),
  ('"They were a people of the Dawn Age," the maester says, "the very first, before kings and kingdoms."', [('"They were', k(6), 'PUSH_IN')], [('the maester', NOTE, {'head': 'IN THE BOOKS', 'body': "A Game of Thrones: Bran's lessons with Maester Luwin."}, 4.4)]),
  ('No castles.', [('No castles.', k(24), 'PAN_LR')], []),
  ('No cities.', [('No cities.', k(25), 'PULL_OUT')], []),
  ('No men at all.', [('No men', k(26), 'DRIFT')], []),
  ('Only the children, in the lands we now call the Seven Kingdoms.', [('Only the', k(27), 'PULL_OUT')], []),
  ('Bran asks if they are still out there.', [('Bran asks', k(28), 'PUSH_IN')], []),
  ('The maester says they are gone.', [('The maester', k(29), 'PUSH_IN')], []),
  ('But the wildling woman Osha, a prisoner in the castle, says something else.', [('But the', k(7), 'PUSH_IN')], [('Osha,', N, {'name': 'OSHA', 'role': 'Wildling · prisoner at Winterfell'}, 3.2)]),
  ('She says they still live, beyond the Wall.', [('She says', k(30), 'PULL_OUT')], []),
  ('One of them was lying.', [('One of', k(31), 'PUSH_IN')], []),
 ]),

 ('I', 'The Dawn Age', 'I', [
  ('The books describe them in careful detail.', [('The books', k(1), 'PUSH_IN')], []),
  ('They were small, about the size of human children, but they were not childlike.', [('They were', k(32), 'PUSH_IN')], []),
  ("Their skin was nut-brown, dappled with paler spots like a deer's.", [('Their skin', k(33), 'DRIFT')], []),
  ('Their ears were large.', [('Their ears', k(34), 'PUSH_IN')], []),
  ("Their eyes were gold and green, slitted like a cat's, made for seeing in the dark.", [('Their eyes', k(35), 'PUSH_IN')], []),
  ('And their hands had only three fingers and a thumb, with sharp black claws instead of nails.', [('And their', k(36), 'PUSH_IN')], [('only three', STAT, {'value': 3, 'label': 'FINGERS AND A THUMB', 'sub': 'Black claws instead of nails'}, 3.4)]),
  ('They had no cities, no metal, no writing.', [('They had', k(37), 'DRIFT')], []),
  ('They lived in caves, in crannogs, and in hidden villages in the trees.', [('They lived', k(38), 'PUSH_IN'), ('in crannogs', k(39), 'DRIFT'), ('villages in', k(40), 'TILT_UP')], []),
  ('Men and women hunted side by side, with bows of weirwood and blades of black volcanic glass.', [('Men and', k(41), 'PAN_LR')], []),
  ('Obsidian.', [('Obsidian.', k(42), 'PUSH_IN')], [('Obsidian.', N, {'name': 'OBSIDIAN', 'role': 'Volcanic glass · dragonglass'}, 2.8)]),
  ('The glass that, thousands of years later, men would call dragonglass.', [('The glass', k(43), 'PUSH_IN')], []),
  ('Their gods were the trees themselves.', [('Their gods', k(44), 'PULL_OUT')], []),
  ('They carved faces into the weirwoods, so the gods could watch over the forest.', [('They carved', k(45), 'PUSH_IN')], []),
  ('And a rare few were born with eyes as green as moss, or red as blood.', [('And a', k(3), 'PUSH_IN')], []),
  ('The greenseers.', [('The greenseers.', k(46), 'PUSH_IN')], [('The greenseers.', N, {'name': 'THE GREENSEERS', 'role': 'Eyes green as moss, or red as blood'}, 3.2)]),
  ('Through the weirwoods, they could see far away, and long ago.', [('Through the', k(47), 'DRIFT')], []),
  ('They were not alone.', [('They were', k(48), 'PAN_RL')], []),
  ('The giants lived here too, ten to fourteen feet tall, shaggy with fur, riding mammoths.', [('The giants', k(4), 'PUSH_IN'), ('riding mammoths', k(49), 'PAN_LR')], [('ten to', N, {'name': 'THE GIANTS', 'role': 'Ten to fourteen feet tall · mammoth riders'}, 3.4)]),
  ('The two peoples did not always get along.', [('The two', k(50), 'PUSH_IN')], []),
  ("The maesters record a giant's grave in the North, with obsidian arrowheads still lodged in its ribs.", [('The maesters', k(51), 'PUSH_IN')], [("a giant's", NOTE, {'head': "THE MAESTERS' HISTORIES", 'body': "A giant's grave in the North, obsidian arrowheads still lodged in its ribs."}, 4.6)]),
  ('For thousands of years, this was the whole world.', [('For thousands', k(52), 'PULL_OUT')], []),
  ('Then, from the east, came men.', [('Then, from', k(53), 'PUSH_IN')], []),
 ]),

 ('II', 'The Bridge of Land', 'II', [
  ('In those days, Westeros and the eastern continent were joined by a bridge of land, the Arm of Dorne.', [('In those', k(54), 'PULL_OUT')], [('the Arm', PL, {'place': 'THE ARM OF DORNE', 'sub': 'The land bridge to the east'}, 3.2)]),
  ('Across it came the First Men.', [('Across it', k(55), 'PAN_LR')], []),
  ('The maesters cannot agree when.', [('The maesters', k(56), 'PUSH_IN')], []),
  ('Some say twelve thousand years ago.', [('Some say', k(57), 'PUSH_IN')], [('twelve thousand', YR, {'year': '12,000 YEARS AGO', 'sub': 'Or eight, say others · the First Men cross'}, 3.6)]),
  ('Others say eight.', [('Others say', k(55), 'PAN_RL')], []),
  ('They carried bronze swords and great leather shields.', [('They carried', k(5), 'PUSH_IN'), ('great leather', k(58), 'PUSH_IN')], [('bronze swords', N, {'name': 'THE FIRST MEN', 'role': 'Bronze, horses, and their own gods'}, 3.2)]),
  ('They rode horses, animals the children had never seen.', [('They rode', k(59), 'PUSH_IN')], []),
  ('And they brought their own gods.', [('And they', k(60), 'DRIFT')], []),
  ('At first, the histories say, the children welcomed them.', [('At first,', k(61), 'PUSH_IN')], []),
  ('But the First Men cleared the forests for their fields.', [('But the', k(62), 'PAN_LR')], []),
  ('Then they began to fear the faces in the trees.', [('Then they', k(63), 'PUSH_IN')], []),
  ('They believed the children used them to spy.', [('They believed', k(64), 'PUSH_IN')], []),
  ('So they burned the weirwoods, and cut them down.', [('So they', k(65), 'PUSH_IN'), ('and cut', k(66), 'PULL_OUT')], []),
  ('And the children went to war.', [('And the', k(67), 'PUSH_IN')], []),
 ]),

 ('CA', 'Subscribe', None, [
  ('What the children did next changed the shape of the continent.', [('What the', k(68), 'PUSH_IN')], []),
  ('If you want Westeros the way it is in the books, subscribe to the Mythic Archives.', [('If you', k(10), 'DRIFT')], []),
 ]),

 ('III', 'The Hammer of the Waters', 'III', [
  ('The war lasted for centuries.', [('The war', k(69), 'PAN_LR')], []),
  ('The children had weirwood bows and obsidian.', [('The children', k(70), 'PUSH_IN')], []),
  ('The First Men had bronze, and numbers.', [('The First', k(71), 'PULL_OUT')], []),
  ('In the riverlands, one legendary warrior earned the name Brandon of the Bloody Blade.', [('In the', k(72), 'PUSH_IN')], [('Brandon of', N, {'name': 'BRANDON OF THE BLOODY BLADE', 'role': 'Legendary hero of the First Men'}, 3.6)]),
  ('The children were losing.', [('The children', k(73), 'PAN_RL')], []),
  ('So their greenseers turned to the darkest magic they had.', [('So their', k(74), 'PUSH_IN')], []),
  ('Legend says they gathered and called down the hammer of the waters.', [('Legend says', k(75), 'TILT_UP'), ('the hammer', k(76), 'PUSH_IN')], [('called down', NOTE, {'head': 'LEGEND', 'body': 'The Hammer of the Waters: the greenseers break the Arm of Dorne.'}, 4.2)]),
  ('The sea rose.', [('The sea', k(77), 'PUSH_IN')], []),
  ('The land shook.', [('The land', k(78), 'PULL_OUT')], []),
  ('And the Arm of Dorne broke apart.', [('And the', k(79), 'PULL_OUT')], []),
  ('Where the bridge had stood, there was only water, and a broken chain of islands that we now call the Stepstones.', [('Where the', k(80), 'PAN_LR')], [('the Stepstones.', PL, {'place': 'THE STEPSTONES', 'sub': 'What remains of the Arm of Dorne'}, 4.0)]),
  ('It was too late.', [('It was', k(81), 'DRIFT')], []),
  ('The door was closed, but the First Men were already through.', [('The door', k(82), 'PUSH_IN')], []),
  ('Legend says the greenseers tried once more, in the North, at the narrow neck of land between the swamps.', [('Legend says', k(83), 'PULL_OUT')], []),
  ("At the ancient fortress of Moat Cailin, one ruined tower still bears their name: the Children's Tower, where they called upon their gods to bring the hammer down again.", [('At the', k(84), 'PUSH_IN')], [('Moat Cailin,', PL, {'place': 'MOAT CAILIN', 'sub': "The Children's Tower · the Neck"}, 4.0)]),
  ('Some say that is why the Neck is drowned and full of bogs today.', [('Some say', k(85), 'PAN_LR')], []),
  ('But the Neck held.', [('But the', k(86), 'PUSH_IN')], []),
  ('And the war went on.', [('And the', k(69), 'PAN_RL')], []),
 ]),

 ('IV', 'The Isle of Faces', 'IV', [
  ('At last, both sides grew weary.', [('At last,', k(87), 'PUSH_IN')], []),
  ('In the middle of a great lake in the riverlands, called the Gods Eye, there is a small island.', [('In the', k(88), 'PUSH_IN')], [('called the', PL, {'place': 'THE GODS EYE', 'sub': 'The Isle of Faces · the riverlands'}, 4.0)]),
  ('There, the greenseers and wood dancers of the children met the chiefs and heroes of the First Men, and made the Pact.', [('There, the', k(89), 'PUSH_IN')], []),
  ('The First Men would take the coasts, the high plains and bright meadows, the mountains and the bogs.', [('The First', k(90), 'PAN_LR')], []),
  ('The deep woods would belong to the children forever.', [('The deep', k(91), 'PUSH_IN')], []),
  ('And no more weirwoods would be put to the axe, anywhere in the realm.', [('And no', k(92), 'PUSH_IN')], []),
  ('So that the gods could witness it, a face was carved into every tree on the island.', [('So that', k(93), 'PAN_LR')], []),
  ('From that day it was called the Isle of Faces.', [('From that', k(94), 'PULL_OUT')], []),
  ('A secret order, the green men, was formed to guard it.', [('A secret', k(95), 'PUSH_IN')], [('the green', N, {'name': 'THE GREEN MEN', 'role': 'Guardians of the Isle of Faces'}, 3.2)]),
  ('In the books, some say they guard it still.', [('In the', k(96), 'PUSH_IN')], []),
  ('What followed were four thousand years of friendship.', [('What followed', k(97), 'PAN_LR')], [('four thousand', STAT, {'value': 4000, 'label': 'YEARS OF FRIENDSHIP', 'sub': 'The Pact · the Age of Heroes'}, 3.4)]),
  ('The Age of Heroes.', [('The Age', k(98), 'PULL_OUT')], []),
  ('In time, the First Men put aside the gods they had brought with them, and worshipped the old gods of the forest.', [('In time,', k(99), 'PUSH_IN')], []),
  ('When the Long Night fell, men and children fought side by side.', [('When the', k(100), 'PUSH_IN')], []),
  ("And according to the Night's Watch, the children once gave the brothers a hundred obsidian daggers every year.", [('And according', k(101), 'PUSH_IN')], [('a hundred', STAT, {'value': 100, 'label': 'OBSIDIAN DAGGERS', 'sub': "Every year, says the Night's Watch"}, 3.1)]),
 ]),

 ('V', 'The Seven-Pointed Star', 'V', [
  ('Then, the books say, a new people crossed the narrow sea.', [('Then, the', k(102), 'PAN_LR')], []),
  ('The Andals.', [('The Andals.', k(8), 'PUSH_IN')], [('The Andals.', N, {'name': 'THE ANDALS', 'role': 'Iron, steel, and the Seven'}, 3.0)]),
  ('They had iron and steel.', [('They had', k(103), 'PUSH_IN')], []),
  ('And they had a new faith, the Seven, with seven-pointed stars carved into their own chests.', [('And they', k(104), 'PUSH_IN')], []),
  ('To the Andals, the faces in the trees were idols.', [('To the', k(105), 'PUSH_IN')], []),
  ('They cut down the weirwoods, hunted the children who were left, and swept away the kingdoms of the First Men, one by one.', [('They cut', k(106), 'PULL_OUT'), ('hunted the', k(107), 'PAN_RL'), ('and swept', k(108), 'PULL_OUT')], []),
  ('In the riverlands, there is a hill called High Heart.', [('In the', k(109), 'PUSH_IN')], [('called High', PL, {'place': 'HIGH HEART', 'sub': 'The riverlands'}, 2.8)]),
  ('Around its crown stand thirty-one white stumps, the remains of a sacred weirwood grove.', [('Around its', k(110), 'PAN_LR')], [('thirty-one', STAT, {'value': 31, 'label': 'WEIRWOOD STUMPS', 'sub': 'High Heart'}, 3.0)]),
  ('The songs say an Andal king killed the children there and cut the grove down.', [('The songs', k(111), 'PUSH_IN')], [('The songs', NOTE, {'head': 'THE SONGS', 'body': 'Told in the songs. Not every history in the books agrees.'}, 4.4)]),
  ('The smallfolk say the hill is still haunted by their ghosts.', [('The smallfolk', k(112), 'DRIFT')], []),
  ('But one kingdom never fell.', [('But one', k(113), 'PULL_OUT')], []),
  ('At Moat Cailin, the Andals were broken against the ruins and the bogs.', [('At Moat', k(114), 'PUSH_IN')], []),
  ('The North stayed a land of the First Men.', [('The North', k(115), 'PUSH_IN')], []),
  ('That is why, thousands of years later, the Starks still pray before a heart tree, and not in a sept.', [('That is', k(13), 'DRIFT'), ('not in', k(116), 'PUSH_IN')], []),
 ]),

 ('VI', 'The Show and the Books', 'VI', [
  ('On television, the children of the forest have skin like bark and leaves growing from their bodies.', [('On television,', k(117), 'PUSH_IN')], [('have skin', NOTE, {'head': 'THE SHOW', 'body': 'Game of Thrones on HBO, season 6. Not in the books.'}, 5.0)]),
  ('And in one scene, they bind a First Man to a weirwood, and drive a blade of dragonglass into his heart.', [('And in', k(118), 'PUSH_IN')], []),
  ('He becomes the first White Walker.', [('He becomes', k(119), 'PUSH_IN')], []),
  ('The children, the show says, created their own destroyer.', [('The children,', k(120), 'PUSH_IN')], []),
  ('None of that is in the books.', [('None of', k(121), 'PUSH_IN')], [('None of', NOTE, {'head': 'IN THE BOOKS', 'body': 'The children never create the Others. Where the Others came from is never said.'}, 5.0)]),
  ('In the books, the children are not plants.', [('In the', k(1), 'PUSH_IN')], []),
  ('They are small, dappled, golden-eyed hunters with claws.', [('They are', k(122), 'PUSH_IN')], []),
  ('And the books never say where the Others came from.', [('And the', k(123), 'PUSH_IN')], []),
  ('Nothing in them blames the children.', [('Nothing in', k(124), 'PUSH_IN')], []),
  ('In the books, the children were the ones who stood beside men when the cold came.', [('In the', k(100), 'PUSH_IN')], []),
 ]),

 ('VII', 'The Last Singers', 'VII', [
  ('Beyond the Wall, in the last published novel, Bran finally finds them.', [('Beyond the', k(125), 'PUSH_IN')], []),
  ('They save him from the dead in the snow, and carry him into a cave beneath a hollow hill.', [('They save', k(126), 'PUSH_IN'), ('and carry', k(127), 'PUSH_IN')], [('They save', NOTE, {'head': 'IN THE BOOKS', 'body': "A Dance with Dragons: Bran's chapters beyond the Wall."}, 4.4)]),
  ('One of them is called Leaf.', [('One of', k(2), 'PUSH_IN')], [('called Leaf.', N, {'name': 'LEAF', 'role': 'One of those who sing the song of earth'}, 3.2)]),
  ('She tells him that "children" is only what men call them.', [('She tells', k(128), 'PUSH_IN')], []),
  ('The giants call them the little squirrel people.', [('The giants', k(129), 'PUSH_IN')], []),
  ('Their own name is older: those who sing the song of earth.', [('Their own', k(130), 'DRIFT')], []),
  ('"Before your Old Tongue was spoken," she says, "we had been singing our songs for ten thousand years."', [('"Before your', k(131), 'DRIFT')], []),
  ('Deep in the cave, Bran meets the last greenseer: a pale, withered man, half swallowed by the roots of a weirwood, his one red eye glowing in the dark.', [('Deep in', k(9), 'PUSH_IN'), ('half swallowed', k(132), 'PUSH_IN')], [('the last', N, {'name': 'THE LAST GREENSEER', 'role': 'Half swallowed by a weirwood'}, 3.4)]),
  ('Through the trees, Bran begins to see the past.', [('Through the', k(133), 'PUSH_IN')], []),
  ('In one vision, he watches the First Men offer blood to the heart tree of Winterfell.', [('In one', k(134), 'DRIFT')], []),
  ('He tastes it in his mouth.', [('He tastes', k(135), 'PUSH_IN')], []),
  ('Where are the rest of them?', [('Where are', k(136), 'PUSH_IN')], []),
  ('Leaf answers that the singers have gone into the earth, into the stones, and into the trees.', [('Leaf answers', k(137), 'DRIFT')], []),
  ('"That was in the dawn of days, when our sun was rising," she says.', [('"That was', k(15), 'PULL_OUT')], []),
  ('"Now it sinks, and this is our long dwindling."', [('"Now it', k(138), 'PULL_OUT')], []),
  ('The giants are almost gone too.', [('The giants', k(139), 'PUSH_IN')], []),
  ('The mammoths are down to a few hundred.', [('The mammoths', k(140), 'PAN_LR')], []),
  ('"In the world that men have made," she says, "there is no room for them, or us."', [('"In the', k(141), 'PULL_OUT')], []),
  ('But the old weapons still work.', [('But the', k(142), 'PUSH_IN')], []),
  ("On a hill beyond the Wall, the Night's Watch finds a buried bundle of dragonglass.", [('On a', k(143), 'PULL_OUT'), ('a buried', k(144), 'PUSH_IN')], [('On a', PL, {'place': 'THE FIST OF THE FIRST MEN', 'sub': 'Beyond the Wall · above the Milkwater'}, 4.0)]),
  ('Months later, a frightened young brother named Samwell Tarly drives a dragonglass dagger into one of the Others, and it melts away.', [('Months later,', k(145), 'PUSH_IN')], [('Samwell Tarly', N, {'name': 'SAMWELL TARLY', 'role': "Brother of the Night's Watch"}, 3.2)]),
  ("The children's glass, waiting in the ground for eight thousand years.", [("The children's", k(146), 'PUSH_IN')], [('eight thousand', STAT, {'value': 8000, 'label': 'YEARS IN THE GROUND', 'sub': "The children's glass"}, 3.2)]),
 ]),

 ('CB', 'Outro', None, [
  ('So, who was here before the First Men?', [('So, who', k(19), 'PUSH_IN')], [('So, who', END, {'kicker': 'WATCH NEXT', 'title': 'THE OTHERS', 'brand': 'A MYTHIC ARCHIVES PRODUCTION', 'sub': 'What the books really say  ·  coming to the archive', 'q': 'INVADERS — OR GUARDIANS?', 'q_at': 'Were the', 'comment_at': 'comments', 'like_at': 'Like', 'sub_at': 'subscribe'}, 0)]),
  ('A small, singing people who carved the gods into the trees, and broke the land itself to defend them.', [('A small,', k(17), 'DRIFT'), ('and broke', k(79), 'PULL_OUT')], []),
  ('They lost their world.', [('They lost', k(147), 'PUSH_IN')], []),
  ('But they kept their bargain, and taught the newcomers to pray.', [('But they', k(99), 'PUSH_IN')], []),
  ('Were the First Men invaders who stole a world, or did the Pact make them its guardians?', [('Were the', k(148), 'PUSH_IN')], []),
  ('Tell us what you think in the comments.', [('Tell us', k(10), 'PUSH_IN')], []),
  ('Like this video if the books surprised you, and subscribe to the Mythic Archives.', [('Like this', k(94), 'PULL_OUT')], []),
  ('The archive is always open.', [('The archive', k(149), 'PULL_OUT')], []),
 ]),

]

# one take may cover several sections (split at the quietest point between them; see tools/v2_timeline.py)
CLIPS = [('H_P', ['H', 'P']), ('I', ['I']), ('II_CA', ['II', 'CA']), ('III', ['III']), ('IV', ['IV']), ('V', ['V']), ('VI', ['VI']), ('VII', ['VII']), ('CB', ['CB'])]

IDENT_SHOT = (k(150), "PUSH_IN", {"title": "THE MYTHIC ARCHIVES", "tag": "WESTEROS  •  ARRAKIS  •  MIDDLE-EARTH",
                                   "sub": "A MYTHIC ARCHIVES PRODUCTION  ·  WESTEROS  ·  RECORD 002"})
END_HOLD = 6.0
MAPS = {}


def narration(section):
    return " ".join(l[0] for l in section[3])


PROLOGUE = '0:00 Prologue: The Maester and the Boy'
SPECIAL_PAUSE = {
    'so who was here before the first men?': 1.0, 'one of them was lying.': 1.0, 'then, from the east, came men.': 1.0,
    'and the children went to war.': 1.1, 'and the war went on.': 1.0, 'some say they guard it still.': 0.9,
    'the andals.': 0.8, 'and not in a sept.': 1.1, 'none of that is in the books.': 1.0,
    'this is our long dwindling."': 1.0, 'waiting in the ground for eight thousand years.': 1.2,
}


def music_edl(S, total, ident, phrase_after, phrase_end):
    """GOT002 cue sheet: Kevin MacLeod (incompetech, CC BY 4.0), same approach and loudness as GOT001/LOTR001.
    Dawn-Age palette: plucked/sacred/medieval for the children and the Pact, darker beds for the war and the Andals.
    Track choices are provisional; the CI mix check validates them."""
    def cue(cid, name, track, start, end, offset, fade_in=1.5, fade_out=2.5, gain_db=0, **kw):
        return dict(cue=cid, name=name, track=track, start=round(start, 2), end=round(end, 2), offset=offset,
                    fade_in=fade_in, fade_out=fade_out, gain_db=gain_db, **kw)
    cues = [
        cue('M1', 'The Godswood (hook)', 'Lost_Frontier', 0.0, ident[0] + 1.2, 0.0, fade_in=0.0, gain_db=-2, hp=110),
        cue('M2', 'Archive (ident)', 'Deliberate_Thought', ident[0] - 1.2, S['P']['start'] + 2.0, 30.0, fade_in=1.2, gain_db=-1),
        cue('M3', 'The Maester and the Boy', 'Teller_of_the_Tales', S['P']['start'] - 0.4, S['I']['gap_start'] + 0.6, 0.0),
        cue('M4', 'The Dawn Age', 'Virtutes_Instrumenti', S['I']['gap_start'] - 0.4, S['II']['gap_start'] + 0.6, 0.0),
        cue('M5', 'The Bridge of Land', 'Lord_of_the_Land', S['II']['gap_start'] - 0.4, S['CA']['gap_start'] + 1.0, 0.0),
        cue('M2b', 'Subscribe (archive theme)', 'Deliberate_Thought', S['CA']['gap_start'] - 0.2, S['III']['gap_start'] + 0.8,
            30.0, fade_in=1.0, fade_out=2.0, gain_db=-1),
        cue('M6', 'The Hammer of the Waters', 'Crusade', S['III']['gap_start'] - 0.4, S['IV']['gap_start'] + 0.6, 0.0, gain_db=-1),
        cue('M7', 'The Isle of Faces', 'Angevin', S['IV']['gap_start'] - 0.4, S['V']['gap_start'] + 0.6, 0.0),
        cue('M8', 'The Seven-Pointed Star', 'Dark_Times', S['V']['gap_start'] - 0.4, S['VI']['gap_start'] + 0.6, 0.0),
        cue('M9', 'The Show and the Books', 'Crypto', S['VI']['gap_start'] - 0.4, S['VII']['gap_start'] + 0.6, 2.0, gain_db=-1),
        cue('M10', 'The Last Singers', 'Night_Vigil', S['VII']['gap_start'] - 0.4, S['CB']['gap_start'] + 1.6, 0.0,
            fade_out=3.5, gain_db=-1),
        cue('M11', 'Outro (archive theme)', 'Deliberate_Thought', S['CB']['gap_start'] - 0.6, total, 30.0,
            fade_in=2.0, fade_out=3.0, gain_db=-2),
    ]
    return dict(episode='GOT002', timeline=f'voice-14 VO, programme {total} s', bed_lufs=-23.0,
                notes='start/end = programme seconds; offset = seconds into the source track. Kevin MacLeod '
                      '(incompetech.com), CC BY 4.0.',
                cues=cues,
                sfx=[dict(type='wind', start=0.0, end=18.0, level_db=-40, note='soft wind in the godswood under the hook')],
                silences=[])
