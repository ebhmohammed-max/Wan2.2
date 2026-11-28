# GOT003 SCRIPT v1.0: The Complete History of House Targaryen

Status: **v1.0 DRAFT, awaiting director approval** (2026-11-27). The VO is recorded only after approval.

**Topic:** chosen by the director on 2026-11-27: "The Complete History of House Targaryen", **duration 45+ minutes**.
Director additions for this episode:
- **Burned-in captions** across the whole video.
- **Maps** created as images and **animated with code** where needed.
- **Mockups.**
- "Rest is same as before": voice-14, books first, no author naming, no actor likenesses, 1080p CI master, Drive delivery.

**Canon:** books first (`worlds/westeros/WESTEROS_CANON_POLICY.md`).
- *Fire & Blood* and *The World of Ice & Fire* are written in-world by maesters. They are told as accounts: "the histories say…", "the maesters record…". Their in-world author, Archmaester Gyldayn, and his sources are named, because they are characters.
- The five novels and the three Dunk and Egg tales.
- *House of the Dragon*, *Game of Thrones* and *A Knight of the Seven Kingdoms* are named openly; their inventions are labelled.
- **The author is never named** (director rule §4c).
- Unpublished as of November 2026: *The Winds of Winter*, and the second volume of *Fire & Blood*.

**Format:** Mythic Archives v2, scaled to a long-form documentary.
- Story-first hook; 1 prologue and 10 chapters.
- Subscribe pitch at the II/III seam.
- Debate question, then like / subscribe over the end card.

**Length:** **6,850 spoken words**, about **46–47 min**. That uses GOT002's measured 149 wpm including pauses, plus 10 chapter cards and the map and mockup holds.

**Defaults** (changeable):
- Ident: **WESTEROS · RECORD 003**.
- Title: **THE COMPLETE HISTORY OF HOUSE TARGARYEN**, sub *Fire and Blood, from the Doom to the Last Dragon*.
- End card WATCH NEXT: **THE OTHERS** · *What the books really say*. This matches the GOT002 teaser.
- Debate pill: **"WHO WAS THE GREATEST TARGARYEN?"**

---

## Production plan (new for this episode)

### Burned-in captions
- **Source:** words.json from CI align, the same data as the `.srt`.
- **Grouping:** phrases of up to 2 lines × about 38 characters, broken at punctuation and pauses, held 1.0–6.0 s.
- **Style:** Cinzel-style serif in warm white (#F2E8D5), a soft dark shadow and a 55% dark band behind, in the lower 12% of the frame. Proper nouns are not highlighted, to stay readable.
- **Collision rule:** captions lift above any lower-third NAME/PLACE/NOTE graphic while it is on screen. They hide during TITLE, IDENT, CHAPTER cards and the end card.
- **Implementation:** a `captions` layer in `tools/gfx_v2.py` / `render_v2.py`, switched on per episode with `D.BURN_CAPTIONS = True`, and QC'd as a sheet before the master.

### Maps: generated as images, animated with code
- **Base art:** each base map is generated as a **text-free** painted parchment map: aged vellum, ink coastlines, painted mountains and forests.
- **Code layers:** all names, routes, arrows, pins, borders and dates are drawn in code, because AI-made text is unreliable.
- **Animation:**
  - slow push-in or pan to a region;
  - route lines that draw on with a moving head;
  - pulsing pins and banner sigils that fade in;
  - fire spreading as an animated mask;
  - territory fills that wipe in;
  - a date counter in the corner.
- **Planned maps (12):**
  1. **The Valyrian Freehold:** Valyria and the Fourteen Flames, then the Doom erupts (red pulse), ending on the Smoking Sea. Aenar's route Valyria → Dragonstone draws on.
  2. **Westeros before the Conquest:** the Seven Kingdoms fill in with their seven sigils.
  3. **Aegon's Landing:** Dragonstone → the three hills at the mouth of the Blackwater (Aegonfort).
  4. **The Conquest:** Harrenhal (fire icon), the Last Storm, the Field of Fire, the Eyrie (Visenya's flight), the Trident (Torrhen kneels), Oldtown (anointing). Kingdoms flip to black-and-red one by one.
  5. **Dorne unconquered:** the Hellholt, where Meraxes falls; a burning "Dragon's Wroth" sweep; DORNE stays uncoloured.
  6. **Jaehaerys's roads:** the Kingsroad and the other roads draw on across the realm; Alysanne's flight to the Wall and the New Gift.
  7. **Blacks and greens, 129 AC:** a split realm, with the blacks' and greens' holdings filling in.
  8. **The Dance:** Storm's End (Arrax), Rook's Rest, Tumbleton, King's Landing, then the Gods Eye duel and Dragonstone.
  9. **The Young Dragon and Dorne:** Daeron's three-pronged invasion (157 AC) and the Boneway; then Dorne rising.
  10. **Redgrass Field (196 AC):** a battle map with the Blackfyre host and the royal host; the Raven's Teeth arrow volleys; the flank collapse.
  11. **Robert's Rebellion:** Harrenhal 281, the Trident (Ruby Ford), the Sack of King's Landing and the Tower of Joy.
  12. **The exiles:** Dragonstone → Braavos → Pentos → the Dothraki Sea → Qarth → Slaver's Bay (Astapor, Yunkai, Meereen).

### Mockups: in-world documents and artifacts
- **How they are made:** each prop is generated **without text** (blank parchment, a ledger, a scroll, a coin or a tapestry). The legible in-world writing is set in code with a period hand-lettered font, so every word is real and spelled right.
- **Animation:** slow push-in, ink that writes on, a wax seal that stamps, a page turn, or a candle flicker.
- **Planned mockups (about 18):**
  1. A page of Archmaester Gyldayn's history, with margin notes from "Eustace", "Munkun" and "Mushroom" that disagree.
  2. Daenys's dream, as a scroll fragment.
  3. The Painted Table, also used as the map base.
  4. The Iron Throne decree: "A king should never sit easy."
  5. Princess Deria's sealed letter, which no one has ever read.
  6. Jaehaerys's Code: a law book.
  7. The Great Council of 101 AC: a ledger of claimants with tally marks.
  8. Viserys's proclamation naming Rhaenyra heir, with the lords' oath.
  9. **The Dragon Registry:** dragon, rider, colour and fate, filled in as the Dance destroys them.
  10. A green vs black ribbon chart.
  11. Aegon IV's deathbed decree legitimising his bastards.
  12. The Blackfyre and Targaryen banners, reversed colours side by side.
  13. A Raven's Teeth arrow fletching tag and a "thousand eyes and one" whisper-ledger.
  14. **Maester Corso's ink-blotted letter from Summerhall.** The real surviving fragments are set and the rest blotted out.
  15. A pyromancer's wildfire jar ledger under the Red Keep.
  16. The Tourney at Harrenhal roll (Rhaegar's crown of winter roses).
  17. A **Targaryen family tree** that grows king by king and recurs as a chapter transition.
  18. **The Kings of the Iron Throne:** a scroll of 17 Targaryen kings that ticks forward each chapter.
  - Plus a golden dragon coin, front and back, at the subscribe pitch.

### Still budget and schedule
- **Stills:** about **460 stills** for 47 min, plus 12 base maps and about 18 mockup props.
- **Generation:** about **490 generated images**, roughly **49 turns** at 10 per turn.
- **Pacing:** density drops from GOT002's 14 shots/min to about 10/min. The maps, mockups and family tree carry about 7–8 minutes of screen time with code animation.
- **VO:** about 6,850 words (~41,000 characters) is about 29 TTS clips under the 1,500-character cap. That is **3 turns** of recording at 10 clips per turn, done after approval. Then one CI align.
- **Render:** a 47-min 1080p render on CI may need about 2–3 h; the master workflow timeout is raised to 300 min. If one job is too slow, the master is split into 3 parts plus a concat job.

### Visual rules: book looks
These go into `WESTEROS_BOOK_LOOKS.md` §7 before the stills.
- **Valyrian blood:**
  - pale silver-gold hair and purple eyes (lilac, violet, indigo);
  - fine, "more than human" beauty, without a show likeness;
  - every royal face is an **original** face.
- **NO House of the Dragon or Game of Thrones cast likeness.** No Matt Smith, Emma D'Arcy, Milly Alcock, Olivia Cooke, Emily Carey, Paddy Considine, Tom Glynn-Carney, Ewan Mitchell, Emilia Clarke or Harry Lloyd. The Knight of the Seven Kingdoms cast is excluded too.
- **Aegon I:** grave, silent, imposing. Valyrian steel crown set with rubies; the sword Blackfyre.
- **Visenya:** stern warrior queen in mail; the sword Dark Sister.
- **Rhaenys:** bright and playful, among singers.
- **Balerion the Black Dread:** black scales and black fire; teeth like black swords. His skull lies in the Red Keep cellars.
- **Vhagar:** later vast and slow.
- **Meraxes:** silver-gold scales (◻ verify colour).
- **The Iron Throne (book look):** an "asymmetric monstrosity of spikes and jagged edges and twisted metal", high on a platform behind steep iron steps. **NOT the show's chair.**
- **Maegor:** huge, broad, brutal; a crown of iron (◻).
- **Jaehaerys and Alysanne:** handsome royal pair; dragons Vermithor (bronze) and Silverwing.
- **Rhaenyra:** "the Realm's Delight", silver-gold hair. In later years heavier and careworn (book), not the show's look.
- **Daemon:** lean, sharp-featured; Dark Sister; Caraxes the Blood Wyrm (red, long and serpentine).
- **Aemond:** one eye, with a sapphire in the empty socket; Vhagar.
- **Aegon II:** golden Sunfyre; badly burned later.
- **Dragonseeds:** Nettles is dark-haired and thin.
- **Aerys II:** gaunt, with long tangled silver hair and long yellow cracked nails.
- **Rhaegar:** melancholy, a silver harp, a black breastplate with a three-headed dragon in rubies.
- **Lyanna:** a crown of blue winter roses.
- **Daenerys (book):** a girl, silver-gold hair, violet eyes. **NO Emilia Clarke likeness**: an original face.
- **Dragons:** Drogon is black and red, Rhaegal green and bronze, Viserion cream and gold.
- **Bloodraven:** albino, one red eye, a port-wine birthmark (◻).
- **Dunk and Egg:** Dunk is very tall and broad; Egg is a bald boy.
- **Violence rule:** suggest it, never show it. Fire seen from far away, aftermath, empty armour, shadows. No gore and no cutting.

---

## Hook payoff checklist

| Hook line | Paid off in |
|---|---|
| A girl woke screaming from a dream of fire | Prologue: The Dreamer |
| Three dragons and fewer than sixteen hundred men | II The Field of Fire |
| A throne of melted swords | II The Field of Fire |
| A war that ended the dragons themselves | V The Dance of the Dragons, VI The Last Dragon |
| The last of them is still out there | X The Last Dragons |

---

## H: Hook

> Twelve years before the end of the world, a young girl woke screaming from a dream.
> She had seen her city burn. Mountains split open. The sky turned black, and a sea of fire swallowed the greatest empire men had ever built.

> Her father believed her. He sold everything he owned, gathered his family and five dragons, and sailed to a lonely rock at the edge of the world.
> Twelve years later, the dream came true.

> That girl's family would conquer a continent with three dragons and fewer than sixteen hundred men. They would sit on a throne of melted swords for almost three hundred years. They would build, and they would burn. And in the end, they would tear each other apart in a war that killed the dragons themselves.

> And the last of them is still out there. In the books, she is a young queen, far across the sea, with three dragons of her own.

> This is the complete history of House Targaryen.

*{TITLE: THE COMPLETE HISTORY OF HOUSE TARGARYEN · Fire and Blood, from the Doom to the Last Dragon · kicker "THE MYTHIC ARCHIVES PRESENTS"}*
*Channel ident: THE MYTHIC ARCHIVES · WESTEROS • ARRAKIS • MIDDLE-EARTH · A MYTHIC ARCHIVES PRODUCTION · WESTEROS · RECORD 003*

## Prologue: The Dreamer

*{MOCKUP 1: the Gyldayn page, with three margin hands that disagree}*

> Before we begin, a word about where this story comes from.
> In the books, the history of House Targaryen is written by a maester of the Citadel, Archmaester Gyldayn. He did not see any of it. He stitched it together from older accounts. One came from a pious septon who flattered the kings. One came from a grand maester who tried to be fair. And one came from a court fool named Mushroom, who claimed he had been hiding in every bedchamber in the Red Keep.
> They often disagree. So when this video says "the histories say", remember: even inside the story, nobody is completely sure what happened.

> Now, the dream.

*{MAP 1: The Valyrian Freehold}*

> More than four hundred years before the main books, the Freehold of Valyria ruled half the known world. It was not a kingdom. It was a freehold, ruled by some forty great families of dragonlords, who flew over their empire on dragons and mined its fire mountains for gold and slaves and power.
> The Targaryens were one of those families. They were not the richest. They were not the strongest. They were not even close.

*{NAME: DAENYS THE DREAMER · Maiden daughter of Aenar Targaryen}*

> Then Lord Aenar Targaryen's maiden daughter had a dream. The histories call her Daenys the Dreamer. She saw Valyria destroyed.
> Aenar believed her. He sold his lands in the Freehold, and moved his whole house, with all its wealth and its five dragons, to Dragonstone, a smoking island at the mouth of Blackwater Bay. It was the westernmost outpost of Valyria, a lonely rock on the edge of nowhere.
> The other dragonlords mocked him. A great lord, running from a girl's nightmare.

*{MOCKUP 2: Daenys's dream scroll · YR: 102 YEARS BEFORE THE CONQUEST}*

> Twelve years later, the Fourteen Flames woke.
> The histories say every hill for five hundred miles split open on the same day. Fire and ash filled the sky, so thick and so hot that even dragons fell burning from the air. Lakes boiled. Palaces and temples crumbled. The sea rushed in and swallowed what was left.
> Nobody agrees on what caused it. Some say the fire mountains simply erupted. Some say the Valyrians dug too deep. Some say the spells that held the mountains quiet for five thousand years finally failed.
> The maesters just call it the Doom.

*{PLACE: THE SMOKING SEA · Where Valyria once stood}*

> When it was over, the Freehold was gone. Its dragonlords, its cities, its sorcery, nearly every dragon in the world. Where Valyria had stood, there was only a broken scatter of islands in a dark, steaming water that sailors still call the Smoking Sea. Even now, in the books, men say no ship that sails there returns.
> Only one dragonlord family survived with its dragons intact. The family that had listened to a girl's dream.

> What followed is called the Century of Blood. The free cities of the east tore each other apart over Valyria's corpse.
> And for a hundred years, the Targaryens mostly stayed out of it. They sat on Dragonstone, looking east, toward the ruins of home.
> Then a boy named Aegon was born. And Aegon looked west.

## Chapter I: Three Dragons

*{CHAPTER I: THREE DRAGONS}*

> Aegon Targaryen grew up in a castle that looked like a nightmare.
> The Valyrians had raised Dragonstone with magic, shaping the black stone like soft clay. Its towers were carved as dragons, hunched along the walls as if about to take flight. Its gates were open dragon mouths. Gargoyles and stone wyverns crouched everywhere, and the whole mountain beneath it steamed and rumbled.

*{NAME: VISENYA TARGARYEN · Elder sister · Wielder of Dark Sister}*
*{NAME: RHAENYS TARGARYEN · Younger sister · Rider of Meraxes}*

> He had two sisters, and in the old Valyrian way, to keep the blood of the dragon pure, he married them both. The histories say he married Visenya first, out of duty, and Rhaenys out of love.
> They could not have been more different. Visenya, the elder, was a warrior. Stern, severe, hard to impress. She trained with the sword from girlhood, and she carried a blade of Valyrian steel called Dark Sister.
> Rhaenys, the younger, was bright and playful and curious. She loved music, and dancing, and clever company. She filled her halls with singers. And she flew her dragon simply because she loved to fly.
> Aegon himself was the hardest to read. The histories describe him as grave and quiet, a man who kept his own counsel. He carried his own Valyrian sword, a black blade called Blackfyre.

> And each of them had a dragon.
> Visenya rode Vhagar. Rhaenys rode Meraxes. And Aegon rode the greatest of them all. Balerion, the Black Dread.

*{NAME: BALERION · The Black Dread · Last dragon to have seen Valyria}*

> Balerion was the last living dragon to have seen Valyria itself. His scales were black. His fire was black. When he flew, the stories say, his shadow fell over whole towns at once, and people in the streets below would look up and see the sun go out.
> In the first book, a young Arya Stark gets lost in the cellars of the Red Keep and finds the old dragon skulls in the dark. The biggest of them has teeth like black swords, and a jaw so wide it could swallow a horse and rider whole. That was Balerion.

*{MOCKUP 3: The Painted Table}*

> In the great hall of Dragonstone, Aegon had a table made. Fifty feet long, cut in the shape of Westeros and painted with every forest, river, city and castle on the continent.
> And on it, there were no borders. No kingdoms. Just one land.
> Centuries later, in the books, Stannis Baratheon would stand at the same table and brood over the same map.

*{MAP 2: Westeros before the Conquest · seven sigils fade in}*

> Because when Aegon looked across the narrow sea, he did not see one land. He saw seven kingdoms, each with its own king, and all of them at war.
> In the North, the Starks of Winterfell. In the Vale, the Arryns of the Eyrie. In the west, the Lannisters of Casterly Rock. In the Reach, the Gardeners of Highgarden. In the Stormlands, the Durrandons of Storm's End. In the south, the Martells of Dorne.
> And in the riverlands, a cruel king from the Iron Islands named Harren the Black, who had just finished building the largest castle the world had ever seen.

> Why did Aegon go west? The histories do not agree.
> Some say it was simple ambition. Some say Daenys's old dream had shown more than the Doom. Others point to an insult. The storm king, Argilac the Arrogant, offered Aegon a marriage alliance. Aegon countered. And Argilac sent back an answer so insulting that there could only be one reply.

*{NOTE: THE SHOW · House of the Dragon adds a secret prophecy, "A Song of Ice and Fire", passed from king to heir. It is not in the books.}*

> In the show House of the Dragon, there is another reason. Aegon has a secret dream of a great winter coming from the north, and conquers Westeros to unite it against the dead. That prophecy is passed from king to heir, all the way down to Daenerys.
> It is a powerful idea. But it is the show's invention. In the books, no such dream is ever mentioned.

## Chapter II: The Field of Fire

*{CHAPTER II: THE FIELD OF FIRE}*

*{MAP 3: Aegon's Landing}*

> Aegon landed at the mouth of the Blackwater Rush, on three hills above a fishing village. He brought fewer than sixteen hundred men.
> On the highest hill, he built a rough fort of timber and earth. The Aegonfort. One day it would become the Red Keep, and the village below would grow into a city called King's Landing.
> Westeros still counts its years from his conquest. In the books, every date is so many years After the Conquest. A.C.

*{YR: 1 AC · After the Conquest}*

> The first great test came in the riverlands.
> Harren the Black had spent forty years building Harrenhal. Its walls were so high that no siege tower could reach them. Its five towers were the tallest in the realm. Its great hall could feast an army. And the histories say it was finished on the very day Aegon landed.

*{PLACE: HARRENHAL · The largest castle ever built}*

> Harren believed stone could not burn. He shut himself inside with his sons, and he waited.
> Aegon did not besiege the castle. He flew over the walls at dusk on Balerion.
> And the black fire poured down into the towers. Stone, it turns out, does not need to burn. It only needs to get hot enough. The towers became ovens. The great stones cracked, and glowed, and ran like candle wax.
> By morning, Harren the Black and his sons were gone, and his line with them. Three hundred years later, in the books, Harrenhal still stands half-ruined, its towers twisted and melted. People say it is cursed. Nearly every lord who has held it since has come to a bad end.

> In the south, Aegon's half-brother and general, Orys Baratheon, faced the storm king, Argilac the Arrogant, who had insulted Aegon in the first place. Argilac fell in the battle. Orys married the dead king's daughter, and took his castle, his banners and his words for his own.
> That is how House Baratheon began. As a Targaryen general's reward.

*{NAME: ORYS BARATHEON · Founder of House Baratheon}*

> Then came the moment that decided everything.
> Two kings joined forces against the dragons: Loren Lannister of the Rock, and Mern Gardener of the Reach. Together they marched with fifty-five thousand men, the largest army Westeros had ever seen.
> Aegon had about eleven thousand.

*{MAP 4: The Conquest · Field of Fire}*
*{STAT: 55,000 vs 11,000}*

> They met on open ground south of the Blackwater, in a dry summer, with the grass high and golden.
> For the first and only time in history, all three dragons flew into battle together. Vhagar. Meraxes. And Balerion.
> The grass caught at once. The wind did the rest.

> The histories say four thousand men burned that day. Mern Gardener, the last king of the Reach, died with his sons and his grandsons, and his line ended on that field.
> Loren Lannister lived. He knelt, and laid his crown at Aegon's feet.
> The battle has a name in the books. They call it the Field of Fire.

*{STAT: 4,000 · Men burned on the Field of Fire}*

> After that, the kingdoms fell like dominoes.
> In the Vale, the Arryns' queen regent believed the Eyrie could never fall. It stood on a mountain, high above any army. But no castle is high enough to stop a dragon. Visenya simply flew Vhagar up the mountain and landed in the castle yard.
> The boy king of the Vale, Ronnel Arryn, was taken up on Vhagar's back, flown three times around the mountain, and came down to surrender his crown.

> In the North, Torrhen Stark marched south with thirty thousand men. When he reached the Trident and saw the dragons, and heard what had happened to Harrenhal, he made the hardest choice a king can make. He knelt.
> The North remembers him as the King Who Knelt. But because he knelt, Winterfell never burned.

*{NAME: TORRHEN STARK · The King Who Knelt}*

> And in Oldtown, the High Septon of the Faith prayed for a sign. The gods, he said, told him not to oppose Aegon. So the city opened its gates, and the High Septon anointed Aegon king with the seven oils.

*{MOCKUP 4: "A king should never sit easy."}*

> Aegon now needed a throne.
> He had the swords of his fallen enemies gathered together, the songs say a thousand of them, and had them heated in Balerion's fire, then beaten and twisted into a seat.
> In the show, the Iron Throne is a neat, upright chair. In the books, it is something else entirely. An asymmetric monstrosity of spikes, jagged edges and twisted metal, rising high above the hall, reached by steep iron steps.
> It was meant to be uncomfortable. The histories say Aegon wanted it that way. A king, he said, should never sit easy.
> And the throne was dangerous. Kings who sat on it cut themselves on its blades. Later, people would whisper that the throne itself judged who was worthy, and drew the blood of those who were not.

*{NOTE: THE BOOKS · "An asymmetric monstrosity of spikes and jagged edges and twisted metal"}*

> Six kingdoms had fallen. One had not.

*{MAP 5: Dorne unconquered}*

> Dorne was a hot, dry land of deserts, red mountains and scorpions. And the Dornish had learned from the Field of Fire. They refused to give battle. When the dragons came, their armies simply melted into the desert. When the dragons left, they came back.
> Then, in the tenth year after the landing, Rhaenys and Meraxes flew over the castle of Hellholt. A bolt from a great Dornish scorpion struck Meraxes through the eye.
> The dragon fell. And Rhaenys fell with her.

*{PLACE: HELLHOLT · Where Meraxes fell, 10 AC}*

> Aegon's answer is remembered as the Dragon's Wroth. For two years, Aegon and Visenya burned every Dornish castle they could reach. Dorne still would not bend.
> In the end, a letter arrived from the Princess of Dorne. Aegon read it alone. No one knows what it said. But after he read it, he made peace, and never went to war in Dorne again.

*{MOCKUP 5: Princess Deria's sealed letter}*

> Aegon ruled for thirty-seven years. He died in his bed on Dragonstone, in peace, at the head of a dynasty.
> His family would not stay at peace for long.

## CA: Subscribe

*{MOCKUP: the golden dragon coin, front and back}*

> If you are enjoying this journey through the history of Westeros, subscribe to the Mythic Archives. We bring the books to life: the stories, the history, and the small details that make these worlds feel real.
> Now, the sons of the dragon.

## Chapter III: The Sons of the Dragon

*{CHAPTER III: THE SONS OF THE DRAGON}*
*{MOCKUP 17: family tree · Aegon I → Aenys / Maegor}*

> Aegon left two sons, by two different sisters. Each was raised by his own mother, and each became a mirror of her.
> Aenys, the son of Rhaenys, was gentle and dreamy, often sick as a boy, kind and eager to be loved. Maegor, the son of Visenya, was the opposite. Huge, strong, and fearless, a warrior from childhood, with his mother's iron and none of his father's patience.
> Aenys got the throne. Maegor got his father's sword, Blackfyre.

*{NAME: AENYS I · The gentle king · 37–42 AC}*

> Aenys wanted everyone to love him. Instead, the realm rose against him.
> The biggest threat was the Faith. Its holy orders, the Warrior's Sons and the Poor Fellows, had always hated the Targaryen custom of marrying brother to sister. When Aenys married his own daughter to his son, the High Septon called him an abomination. The Faith Militant rose across the realm.
> Aenys never recovered. He died after just five years on the throne. Some whispered that Visenya had helped him on his way, with one of her potions.

*{NAME: MAEGOR I · The Cruel · 42–48 AC}*

> Then came Maegor.
> He seized the throne, and claimed the greatest prize of all: Balerion, the Black Dread, who had flown under his father, and now flew under him.
> Maegor met the Faith with fire and steel. He crushed the Warrior's Sons. When his own nephew rose against him, he met him over the Gods Eye, dragon against dragon, and the nephew did not come back.
> He finished the Red Keep, and the histories say that when it was done, he had the builders put to death, so that no one would ever know its secret passages.

> He married six times. Three of those wives he wed on a single day. The court called them the Black Brides.
> And for all those marriages, Maegor had no living heir. The histories record only stillbirths, and dark rumours of curses.
> Within six years, the realm turned against him. His lords left him one by one, to join his young nephew Jaehaerys, who had come out of hiding with a dragon of his own.

> One morning, Maegor the Cruel was found dead, sitting upon the Iron Throne.
> Nobody knows what happened. Some say he took his own life. Some say someone helped him. And some say the throne itself finally made its judgement.

*{NOTE: LEGEND · "The throne killed him"}*

## Chapter IV: The Old King and the Good Queen

*{CHAPTER IV: THE OLD KING AND THE GOOD QUEEN}*

> The boy who took the throne after Maegor was fourteen years old. His name was Jaehaerys.
> He would rule for fifty-five years. And to this day, in the books, he is remembered as the wisest king who ever sat on the Iron Throne.

*{NAME: JAEHAERYS I · The Conciliator · 48–103 AC}*
*{STAT: 55 YEARS · The longest Targaryen reign}*

> He was not alone. He married his sister Alysanne, clever and warm and fearless, and the histories call her the Good Queen. Together, on the dragons Vermithor and Silverwing, they flew to every corner of the realm.
> And they did something no Targaryen had tried. They made the realm work.

> First, they made peace with the Faith. Jaehaerys's Hand, a wise septon named Barth, struck a bargain: the crown would protect the Faith, and in return, the Faith would lay down its swords forever. The Faith Militant was disbanded. And the Targaryens' marriages were declared an exception, blessed by the gods, because the dragonlords were not like other men.

*{MOCKUP 6: Jaehaerys's Code}*

> Then they built.
> Jaehaerys gave the realm one law, instead of seven. He built roads across Westeros, including the Kingsroad, which runs from King's Landing all the way to the Wall. He gave King's Landing wells and sewers. He gave the realm peace.

*{MAP 6: Jaehaerys's roads · the Kingsroad draws on to the Wall}*

> And Alysanne changed the lives of women. She persuaded the king to abolish the lord's right to the first night, an old custom that let a lord claim any bride on her wedding night. She flew Silverwing to the Wall, and gave the Night's Watch new lands to feed the brothers. To this day, the land is called the New Gift. And at Castle Black, the gate the Watch renamed in her honour is still called the Queensgate.

*{PLACE: THE QUEENSGATE · Castle Black, named for Good Queen Alysanne}*

> But the long reign had a sad heart.
> Jaehaerys and Alysanne had thirteen children, and outlived most of them. Their heir, Prince Aemon, was killed by raiders on the island of Tarth. Years later, their second son, Baelon, died too.
> And that raised a question that would haunt the family. Who inherits next?

*{MOCKUP 7: The Great Council of 101 AC}*

> Aemon had left a daughter, Rhaenys. Baelon had left a son, Viserys.
> In the hundred and first year after the Conquest, Jaehaerys called a Great Council at Harrenhal, and let the lords of the realm decide.
> The lords chose Viserys. A man, over a woman. The histories call Rhaenys the Queen Who Never Was.
> It seemed to settle things. In fact, it set a precedent that would rip the dynasty in half.

*{NAME: RHAENYS TARGARYEN · The Queen Who Never Was}*

> When the Old King died, the whole realm mourned him. His dragons had lived to be ancient. His peace had lasted half a century.
> It would not survive his grandson.

## Chapter V: The Dance of the Dragons

*{CHAPTER V: THE DANCE OF THE DRAGONS}*

> King Viserys the First was kind, generous, and fond of feasts and tourneys. He wanted, above all, to be liked.
> He also ruled at the very height of Targaryen power. There were more dragons in the realm than ever before. In the books, the histories call this the high summer of House Targaryen.

*{NAME: VISERYS I · 103–129 AC}*

> Viserys had one living child by his first wife: a daughter, Rhaenyra. The court called her the Realm's Delight.
> When his wife died in childbirth, and the son she bore died with her, Viserys did something no king had done. He named his daughter his heir. And he made the lords of the realm kneel and swear to defend her right.

*{MOCKUP 8: Viserys's proclamation naming Rhaenyra heir}*
*{NAME: RHAENYRA TARGARYEN · The Realm's Delight}*

> Then he married again. His new queen was Alicent Hightower, the daughter of his Hand. And she gave him sons. Aegon. Aemond. Daeron.
> Everyone at court could do the arithmetic. After the Great Council, the realm had chosen a man over a woman once before. And now the king had a son. But Viserys never changed his mind. Rhaenyra remained his heir.

> At a tourney, the histories say, Queen Alicent wore green, and Princess Rhaenyra wore the Targaryen red and black. From then on, the court split into two parties. The greens, who backed Alicent's sons. And the blacks, who backed Rhaenyra.

*{MOCKUP 10: green vs black ribbon chart}*

> Hovering between them was the king's brother, Prince Daemon. Brilliant, reckless, dangerous. He rode a long red dragon called Caraxes, the Blood Wyrm, and carried Dark Sister, Visenya's old sword. He formed the city watch and gave them their gold cloaks. The court called him the Rogue Prince.
> In time, Daemon married Rhaenyra, and joined the blacks.

*{NAME: DAEMON TARGARYEN · The Rogue Prince}*

> Rhaenyra's first three sons were dark-haired and brown-eyed, nothing like their Velaryon father. The court whispered about who their real father was.
> And at a funeral on Driftmark, the queen's young son Aemond climbed onto the oldest dragon in the world, Vhagar, and claimed her. Rhaenyra's boys attacked him for it. In the fight, Aemond lost an eye.
> Later, the histories say, he wore a sapphire in the empty socket. And he would say he had lost an eye, but gained a dragon.

*{NAME: AEMOND TARGARYEN · One eye · Rider of Vhagar}*

> In the hundred and twenty-ninth year, King Viserys died in his sleep.
> The greens hid his death. While the court was kept in the dark, they crowned Prince Aegon in the Dragonpit as King Aegon the Second.
> On Dragonstone, Rhaenyra was crowned as queen.
> Two monarchs. Two crowns. And dragons on both sides.

*{MAP 7: Blacks and greens, 129 AC}*
*{YR: 129 AC}*

> The first death came in a storm.
> Rhaenyra sent her second son, Lucerys, on his young dragon Arrax, to win the support of Storm's End. When he arrived, Aemond was already there, with Vhagar.
> Above Shipbreaker Bay, in a storm, Vhagar caught Arrax. Neither the boy nor his dragon survived.

*{NOTE: THE SHOW · In House of the Dragon, Vhagar acts against Aemond's will. In the books, it is not an accident.}*

> The war that followed is called the Dance of the Dragons. It was the darkest chapter in the family's history.
> In revenge for Lucerys, two killers crept into the Red Keep, and a child of the greens died. The histories remember them only as Blood and Cheese.
> At Rook's Rest, the Queen Who Never Was, Rhaenys, flew her old dragon Meleys against King Aegon on Sunfyre and Aemond on Vhagar. Rhaenys fell. Aegon survived, horribly burned.

*{MOCKUP 9: The Dragon Registry, first deaths crossed out}*

> The blacks needed more dragon riders. So they searched the realm for anyone with a drop of Targaryen blood. Bastards, mostly. Smallfolk who might claim a dragon and live. The histories call them the dragonseeds.
> Some served with honour. A thin, dark girl named Nettles tamed a wild dragon with nothing but patience and a sheep a day. But two dragonseeds turned traitor at the town of Tumbleton, and handed it to the greens.
> In the show, the third season of House of the Dragon ended at Tumbleton, in August twenty twenty-six. The final season is planned for twenty twenty-eight.

*{MAP 8: The Dance}*

> Rhaenyra took King's Landing, and sat on the Iron Throne herself. But she was a harsh ruler, suspicious and grieving, and the city came to hate her.
> One night, a mob led by a prophet called the Shepherd stormed the Dragonpit. Dragons are terrifying in the open sky. Chained in the dark, they could be overwhelmed. Several dragons died there. Rhaenyra's youngest son, Joffrey, died trying to reach his mother's dragon.

> Then came the duel the singers still sing about.
> Prince Daemon waited at Harrenhal. Aemond came for him on Vhagar. And above the lake called the Gods Eye, the two princes met, Caraxes against Vhagar, the Blood Wyrm against the oldest dragon alive.
> When Vhagar seized his dragon, Daemon leapt from Caraxes onto Vhagar's back, with Dark Sister in his hand. The histories say he drove it home through Aemond's empty eye.
> Then all of them, two princes and two dragons, fell together into the lake.

*{PLACE: THE GODS EYE · Where Daemon and Aemond fell, 130 AC}*

> Rhaenyra fled the city and sailed to Dragonstone, hoping to find safety there.
> King Aegon the Second was waiting for her, with his dragon Sunfyre.
> He gave his half-sister to the dragon, and her young son, also named Aegon, was made to watch.

> Aegon the Second did not enjoy his victory for long. Within the year, his own lords poisoned his wine.
> The war was over. And everyone had lost.

*{STAT: 2 YEARS · The Dance of the Dragons}*

> In the books, the Dance killed most of the royal family, and nearly every dragon in the realm. A house that had begun the war with more dragons than ever before ended it with a handful.
> And the boy who had watched his mother die became king.

## Chapter VI: The Last Dragon

*{CHAPTER VI: THE LAST DRAGON}*

> The new king was Aegon the Third. He was only a boy when he was crowned, and the histories say he was never young again.
> He was melancholy and withdrawn. He rarely smiled. He hated dragons, after what he had seen. The realm called him the Broken King. And they called him by another name too: Aegon the Dragonbane.

*{NAME: AEGON III · The Dragonbane · 131–157 AC}*

> Because during his reign, the last dragons died.
> The last of them was a small, sickly green female, who died in the hundred and fifty-third year after the Conquest. And with her, the age of dragons in Westeros seemed to end.

*{YR: 153 AC · The last dragon dies}*
*{MOCKUP 9: The Dragon Registry, every line crossed out}*

> Aegon tried to bring them back. He sent for mages from the east, nine of them, to hatch the remaining eggs. All nine failed.
> No dragon would be born in the world for nearly a hundred and fifty years.

> Aegon's son Daeron was the opposite of his father. Bold, bright and hungry for glory.
> At fourteen, King Daeron the First set out to finish the one thing Aegon the Conqueror never could. He conquered Dorne. Without a single dragon.

*{NAME: DAERON I · The Young Dragon · 157–161 AC}*
*{MAP 9: The Young Dragon and Dorne}*

> He marched through the mountain passes, took Sunspear, and wrote a famous account of his own victory. The Conquest of Dorne.
> But Dorne had not truly bent. It rose again behind him, and within a few years, the young king was dead, struck down under a banner of peace, at just eighteen years old.
> The histories say tens of thousands died to win Dorne, and keep it for a single summer.

> His brother Baelor took the throne, and the realm had never seen a king like him.
> Baelor the Blessed was a septon as well as a king. He walked barefoot all the way to Dorne to make peace. Along the way, he learned that his cousin, Prince Aemon the Dragonknight, was being held in a cage above a pit of vipers.
> Baelor walked straight into the pit to free him. The singers say the vipers bowed their heads to him. The histories say he was bitten many times, and Aemon had to carry him out on his back.

*{NAME: BAELOR I · The Blessed · 161–171 AC}*

> Baelor survived. And he came home stranger than ever.
> He shut his three sisters away in a tower of the Red Keep, so they would not tempt the men of the court. It was called the Maidenvault. He built the Great Sept of Baelor, with its seven crystal towers.
> In the show, Cersei Lannister blows it up with wildfire. In the books, it still stands.
> Baelor died after a long fast, still praying.

> Then came the worst king of all.
> His name was Aegon the Fourth. And the histories call him Aegon the Unworthy.

*{NAME: AEGON IV · The Unworthy · 172–184 AC}*

> He was greedy, lazy, and vain. He took mistress after mistress, and fathered bastards across the realm. He tried to build wooden dragons to invade Dorne, and they burned.
> But his worst act came on his deathbed. He legitimized all of his bastards. Every one of them, at once.

*{MOCKUP 11: Aegon IV's deathbed decree}*

> And years earlier, he had done something even more dangerous. He had given the sword Blackfyre, the sword of Aegon the Conqueror, not to his heir, but to his favourite bastard son, a young man named Daemon.
> In one stroke of a quill, he planted the seed of a war that would last sixty years.

## Chapter VII: The Black Dragon

*{CHAPTER VII: THE BLACK DRAGON}*

> The next king, Daeron the Second, was a scholar. Gentle, wise, and bookish. He was called Daeron the Good. And he finally did what no dragon or army could. He brought Dorne into the realm.
> Not with fire. With marriage. His sister wed the Prince of Dorne, and Dorne joined the Seven Kingdoms in peace.

*{NAME: DAERON II · The Good · 184–209 AC}*

> But many lords hated it. They hated the Dornish at court. They hated the king's books. And they whispered that Daeron was not really Aegon the Fourth's son at all, but the son of the queen and the Dragonknight.
> And there was another man in the realm who looked far more like a king.

*{NAME: DAEMON BLACKFYRE · The Black Dragon}*

> Daemon was tall, strong, and a famous warrior. He carried Blackfyre, the Conqueror's own sword. Knights loved him. And he had a claim.
> He took a new name: Daemon Blackfyre. And he reversed the Targaryen colours. Where the true king flew a red dragon on black, Daemon flew a black dragon on red.

*{MOCKUP 12: Targaryen and Blackfyre banners}*

> In the hundred and ninety-sixth year, he rose.
> The decisive battle was fought at a place called Redgrass Field. On one side, the Black Dragon and his knights. On the other, the king's men.

*{MAP 10: Redgrass Field · 196 AC}*

> And among the king's men was another of Aegon the Fourth's bastards. A pale, strange young man, an albino, with white hair and red eyes. His name was Brynden Rivers, but the realm would call him Bloodraven.
> Bloodraven commanded the archers. They called themselves the Raven's Teeth.
> When Daemon Blackfyre charged, Bloodraven's arrows found him, and both of his twin sons with him.

*{NAME: BRYNDEN RIVERS · Bloodraven · Commander of the Raven's Teeth}*

> The royal princes Baelor Breakspear and Maekar crushed the rest. But the dream of the black dragon did not die.
> Daemon's half-brother, Bittersteel, fled across the narrow sea, and founded a company of exiles that would become the most famous sellsword army in the world. The Golden Company.
> For sixty years, the Blackfyres would rise again and again. Five rebellions in all. The last of them ended in the two hundred and sixtieth year, when a young knight named Barristan Selmy killed the last Blackfyre pretender in single combat.

*{STAT: 5 · Blackfyre Rebellions}*

> And Bloodraven? He became the Hand of the King. The most feared man in the realm. A sorcerer, people whispered, with spies everywhere.
> There was a riddle in those years. How many eyes does Lord Bloodraven have? A thousand eyes, and one.

*{MOCKUP 13: "A thousand eyes, and one."}*

> A great sickness swept the realm in the year two hundred and nine and took King Daeron the Good with it. Years later, Bloodraven was arrested, and sent to the Wall. He became Lord Commander of the Night's Watch.
> And then one day, he rode beyond the Wall and vanished.
> If you watched our last episode, you know where he went. In the books, Bran Stark finds him deep beneath a hill, wound into the roots of a weirwood, still watching, with his one red eye.

## Chapter VIII: Egg and Summerhall

*{CHAPTER VIII: EGG AND SUMMERHALL}*

> Now the story comes to a small boy with a shaved head.
> He was called Egg. A fourth son of a fourth son, so far from the throne that nobody thought of him as a prince at all. As a boy, he shaved his head to hide his Targaryen hair, and served as squire to a huge, kind, poor hedge knight named Ser Duncan the Tall.

*{NAME: SER DUNCAN THE TALL · and his squire, "Egg"}*

> Their adventures are told in the books in three short tales of Dunk and Egg. And they are now a television series too: A Knight of the Seven Kingdoms.
> But nobody could have guessed where Egg would end up.

> In the two hundred and thirty-third year, the realm needed a new king again. Another Great Council was called.
> The crown was first offered to Egg's older brother, Aemon. But Aemon had already chosen a different life. He had forged a maester's chain, and taken vows. He refused.
> So the lords turned to Egg. He became King Aegon the Fifth. The realm called him Aegon the Unlikely.

*{NAME: AEGON V · The Unlikely · 233–259 AC}*

> And Aemon, so that no one could ever use him against his brother, went to the Wall. He would serve the Night's Watch as its maester for the rest of his long life.
> In the first book, he is the blind old man at Castle Black who teaches Jon Snow. Very few at the Wall even know he is a Targaryen.

> Egg had spent his boyhood on the roads with a hedge knight. He had slept in ditches and inns, and he had seen how the smallfolk lived. As king, he tried to help them. The great lords fought him at every turn.
> Ser Duncan the Tall became the Lord Commander of his Kingsguard.
> And Egg dreamed of one more thing. He dreamed of dragons.

> In the two hundred and fifty-ninth year, the royal family gathered at Summerhall, a summer palace in the Dornish Marches, to celebrate the birth of the king's first great-grandchild.
> Something happened there. Something involving fire.

*{MOCKUP 14: Maester Corso's ink-blotted letter}*

> The histories hold one surviving letter, written by the castle's maester before he died. It was ruined by a spill of ink. Only fragments can be read.
> The blood of the dragon, gathered in one. Seven eggs, to honour the seven gods. Pyromancers. Wildfire. The flames grew out of control.

*{PLACE: SUMMERHALL · Ruined by fire, 259 AC}*

> The fire destroyed Summerhall. It killed King Aegon the Fifth. It killed his son, Prince Duncan. And it killed Ser Duncan the Tall, who died trying to save his friend.
> In the books, nobody ever says exactly what happened. But the hints all point the same way. Egg tried to hatch dragons.

> And on that same day, in the middle of the grief and the smoke, a baby was born at Summerhall.
> His name was Rhaegar.
> All his life, the histories say, Rhaegar was drawn back to those ruins. He would go there alone, to brood, and to play his harp.

> There is one more thread. Prince Duncan, Egg's son, gave up his claim to the throne to marry a girl he loved, a girl named Jenny of Oldstones.
> Jenny had a strange friend: a tiny woods witch from the riverlands. If you watched our last episode, you may have met her. Many readers believe she is the ghost of High Heart, the tiny old woman who weeps whenever she hears the song of Jenny of Oldstones.
> And it was a woods witch who told the family a prophecy: that the prince that was promised would be born of the line of Aerys and Rhaella.
> So the next king married his son Aerys to his daughter Rhaella. Brother and sister.
> They would be the last king and queen of House Targaryen.

## Chapter IX: The Mad King

*{CHAPTER IX: THE MAD KING}*

> Aerys the Second came to the throne at eighteen, and at first, he seemed charming and full of promise.
> He named his boyhood friend, Tywin Lannister, as his Hand. And for twenty years, Tywin ran the realm, coldly, brilliantly, and well.

*{NAME: AERYS II · The Mad King · 262–283 AC}*

> But Aerys grew jealous. Jealous of Tywin's power, of his praise, of the way the realm credited Tywin for every success. He began to mock him. To insult him.
> And then came Duskendale.

> A minor lord of a port town refused to pay his taxes. Aerys went to Duskendale in person, to settle it. The lord seized him, and held the king of the Seven Kingdoms prisoner for half a year.
> Ser Barristan Selmy finally slipped into the town alone and brought him out.
> But the man who came out was not the man who went in.

*{PLACE: DUSKENDALE · Where the king was held captive, 277 AC}*

> Afterwards, Aerys would not leave the Red Keep. He trusted no one. He would not let a blade come near him, so he stopped cutting his hair and his nails. They grew long, tangled and yellow.
> And he found a new obsession. Fire. He surrounded himself with pyromancers, the alchemists of the wildfire guild, and he began to burn the people he feared.

*{MOCKUP 15: the pyromancers' ledger}*

> In the two hundred and eighty-first year, a great tourney was held at Harrenhal.
> Prince Rhaegar won it. And as the champion, he was meant to crown a lady as queen of love and beauty. Everyone expected him to crown his wife, Elia Martell of Dorne.
> Instead, he rode past her, and laid a crown of blue winter roses in the lap of Lyanna Stark.
> In the first book, Ned Stark remembers that moment as the moment all the smiles died.

*{MOCKUP 16: The Tourney at Harrenhal roll}*
*{NAME: LYANNA STARK · Crowned with winter roses}*

> A year later, Rhaegar and Lyanna disappeared together.
> Lyanna's brother Brandon rode to King's Landing and demanded that Rhaegar come out and face him. Aerys answered by putting Brandon and his father, Lord Rickard Stark, to death.
> Then he demanded the heads of Eddard Stark and Robert Baratheon. Their foster father, Jon Arryn, refused. And the realm rose.

*{MAP 11: Robert's Rebellion}*

> At the Trident, Robert Baratheon met Rhaegar in the river. Robert struck him with his great warhammer, and the rubies on Rhaegar's breastplate flew into the water. Men dove for them for years afterward. The place is still called the Ruby Ford.

*{PLACE: THE RUBY FORD · The Trident, 283 AC}*

> In King's Landing, Tywin Lannister arrived with an army, claiming to come to the king's aid. Aerys opened the gates. The Lannisters sacked the city.
> And in the throne room, a young knight of the Kingsguard named Jaime Lannister heard the king chanting the same words, over and over. Burn them all.
> Aerys had hidden caches of wildfire beneath the entire city, enough to burn it to the ground with everyone inside.
> Jaime killed him at the foot of the Iron Throne. For the rest of his life, the realm would call him Kingslayer. In the books, he tells the true story only once, to Brienne of Tarth, in a bath at Harrenhal.

*{NOTE: THE BOOKS · "Burn them all."}*

> Rhaegar's children did not survive the sack. And far to the south, in a tower in the mountains of Dorne, Lyanna Stark lay dying in a bed of blood, and made her brother promise something.
> Promise me, Ned.
> The books never tell us what he promised.

## Chapter X: The Last Dragons

*{CHAPTER X: THE LAST DRAGONS}*

> But the Targaryens were not quite finished.
> Before the city fell, Queen Rhaella had fled to Dragonstone, with her younger son Viserys. She was heavily pregnant. And as Robert's fleet gathered, a great storm struck the island, and wrecked the Targaryen ships at anchor.
> In the middle of that storm, Rhaella gave birth to a daughter, and died.
> The girl was named Daenerys. Daenerys Stormborn.

*{NAME: DAENERYS STORMBORN · Born on Dragonstone, 284 AC}*

> A loyal knight smuggled the two children across the sea to Braavos. Years later, Daenerys would remember only one happy place from her childhood: a big house with a red door, and a lemon tree outside her window.
> Then the knight died, and the money ran out. Viserys took his sister from city to city, selling their mother's crown to eat. Behind his back, people called him the beggar king.

*{MAP 12: The exiles}*

> And then Viserys sold Daenerys too. He married her to a Dothraki warlord, Khal Drogo, in exchange for an army that never came.
> Among her wedding gifts were three dragon eggs, turned to stone by the centuries.
> Viserys did get his crown in the end. A crown of molten gold, poured by Khal Drogo, when he grew tired of Viserys's threats.
> He was no dragon, Daenerys thought. Fire cannot kill a dragon.

> When Drogo died, Daenerys built him a funeral pyre, set her three stone eggs on it, and walked into the flames.
> In the morning, she rose from the ashes, unburnt. And three newborn dragons were clinging to her. One black, one green, one cream and gold. Drogon. Rhaegal. Viserion.
> The first dragons to be born in the world for nearly a century and a half.

*{STAT: ~145 YEARS · Without a dragon}*

> In the books that followed, Daenerys crossed the red waste, freed the slaves of Astapor, Yunkai and Meereen, and ruled Meereen as its queen, trying, and often failing, to make a broken city work.
> At the end of the fifth book, Drogon carries her out of a fighting pit and far into the Dothraki Sea. That is where her story stops. For now.

> But she is not the only Targaryen left in the books.
> Old Maester Aemon, Egg's brother, the last Targaryen at the Wall, dies at sea on his way to Oldtown, murmuring about dragons, and about her. In his last moments, he calls for his little brother. Egg. I dreamed that I was old.

> In the fifth book, a young man called Griff appears in Essos, claiming to be Rhaegar's son, Aegon, saved from the sack as a baby. And the army marching behind him is the Golden Company. The sellswords founded by Bittersteel, the Blackfyre exile.
> Many readers suspect he is not who he claims to be. That he may be a Blackfyre, at last coming home. The books have not said.

*{NOTE: THEORY · "Young Griff" may be a Blackfyre. The books have not confirmed it.}*

> And at the Wall, there is Jon Snow. A bastard of Winterfell, the son of Ned Stark. Or so everyone believes.
> In the show, it is confirmed: Jon is the son of Rhaegar and Lyanna, and his true name is Aegon Targaryen. In the books, it is one of the most famous theories ever written about a story that has not finished yet. The hints are all there. Promise me, Ned.

> The show gave the dynasty an ending. Daenerys burned King's Landing, Jon killed her, and Drogon melted the Iron Throne.
> In the books, that ending has not been written. The Winds of Winter is still unpublished. And so is the second half of Fire and Blood.

> So the history of House Targaryen is still open.
> It began, three hundred years ago, with a girl who dreamed of fire.
> It may end with a girl who walked into it.

## CB: Outro

*{END CARD: WATCH NEXT · THE OTHERS · What the books really say · debate pill "WHO WAS THE GREATEST TARGARYEN?"}*

> So who was the greatest Targaryen? Aegon the Conqueror, who built the realm with fire? Jaehaerys, who made it work? Egg, the unlikely king who loved the smallfolk? Or Daenerys, whose story is not over?
> Tell us in the comments.
> And if you want more of the books brought to life, like this video, and subscribe to the Mythic Archives. Next, we go north of the Wall, to the Others. And what the books really say about them.

---

## Fact sheet

Each claim is mapped to its tier. ✅ = confirmed against a quoted passage or a reference citing the chapter this session. ◻ = verify before VO.

| Claim | Tier / source |
|---|---|
| F&B is written in-world by Archmaester Gyldayn, using Septon Eustace, Grand Maester Munkun and Mushroom as conflicting sources | `[F&B]` ✅ |
| Daenys the Dreamer's dream 12 years before the Doom; Aenar moves the house and five dragons to Dragonstone | `[W]` via AWOIAF Doom of Valyria ✅ |
| Doom in 102 BC, "about a century before the Conquest"; every hill for 500 miles exploded; dragons died; lakes boiled; Fourteen Flames; Smoking Sea; theories (eruption / delved too deep / spells failed) | `[W]`, `[B:ADWD]` via AWOIAF ✅ |
| Valyria ruled by some forty dragonlord families; Freehold 5,000 years | `[W]` ✅ (◻ the "forty" wording) |
| Century of Blood | `[W]` ✅ |
| Dragonstone fused-stone dragon architecture | `[W]`, `[B:ACOK prologue]` ✅ |
| Aegon married Visenya (duty) and Rhaenys (desire); Visenya stern warrior with Dark Sister; Rhaenys playful, music, flew for joy; Aegon grave; Blackfyre | `[W]`, `[F&B]` ✅ |
| Balerion the last dragon to have seen Valyria; black fire; skull with teeth like black swords in the Red Keep cellars (Arya) | `[W]`, `[B:AGOT Arya III]` ✅ |
| Painted Table: about 50 ft, no borders; Stannis uses it | `[W]`, `[B:ASOS Davos]` ✅ (◻ the "no borders" detail) |
| Argilac's insulting reply to Aegon's counter-offer | `[F&B]` ✅ |
| HOTD's Aegon dream / "Song of Ice and Fire" is show-only | `[SHOW:HOTD S1]` ✅ |
| Landing with fewer than 1,600 men; Aegonfort → Red Keep, King's Landing; AC calendar | `[W]` ✅ |
| Harrenhal finished on the day Aegon landed; burned by Balerion; Harren and his sons died; "cursed" | `[W]`, `[F&B]` ✅ |
| Orys Baratheon defeats Argilac, marries Argella, takes sigil and words | `[W]` ✅ |
| Field of Fire: 55,000 vs 11,000; all three dragons the only time; 4,000 burned; Mern IX and his line died; Loren knelt | AWOIAF Field of Fire ✅ |
| Eyrie surrender: Visenya flies Vhagar; Ronnel Arryn flown around the mountain three times | `[W]` ✅ |
| Torrhen Stark marched with ~30,000 and knelt at the Trident ("the King Who Knelt") | `[W]` ✅ |
| Oldtown opened its gates; High Septon anointed Aegon | `[W]` ✅ (◻ "seven oils" wording) |
| Iron Throne from surrendered swords; "a thousand blades" per the songs; "asymmetric monstrosity of spikes and jagged edges and twisted metal"; "A king should never sit easy"; cuts kings | `[B:AGOT]`, `[F&B]` via AWOIAF Iron Throne ✅ |
| Meraxes killed at Hellholt by a scorpion bolt through the eye (10 AC); Rhaenys died; Dragon's Wroth two years; Princess Deria's letter, contents unknown; peace | `[W]`, `[F&B]` ✅ |
| Aegon I reigned 37 years, died at Dragonstone | `[W]` ✅ |
| Aenys gentle and sickly; Maegor strong; Maegor got Blackfyre; Faith Militant; Aenys married his daughter Rhaena to his son Aegon; died 42 AC; Visenya rumoured | `[F&B]` ✅ |
| Maegor claimed Balerion; defeated his nephew Aegon over the Gods Eye; builders of the Red Keep killed; six wives, three wed on one day ("Black Brides"); no living heir; found dead on the Iron Throne | `[F&B]` ✅ |
| Jaehaerys at 14; 48–103 AC; Alysanne; Vermithor and Silverwing; Septon Barth; Faith disarmed; Doctrine of Exceptionalism | `[F&B]` ✅ |
| Jaehaerys's Code; Kingsroad; wells and sewers in King's Landing | `[F&B]`, `[W]` ✅ |
| Alysanne: abolished lord's right of first night; New Gift; Queensgate | `[F&B]`, `[B:AGOT/ASOS]` ✅ |
| 13 children; Aemon killed on Tarth by Myrish raiders; Baelon died | `[F&B]` ✅ |
| Great Council of 101 AC at Harrenhal chooses Viserys over Rhaenys ("Queen Who Never Was") | `[F&B]` ✅ |
| Viserys I at the height of dragon power; Rhaenyra the "Realm's Delight"; Aemma died in childbirth, the son also died; Rhaenyra named heir, lords swore | `[F&B]` ✅ |
| Alicent Hightower; Aegon, Aemond, Daeron (and Helaena); green and black at the tourney | `[F&B]` ✅ |
| Daemon: Caraxes, Dark Sister, gold cloaks; married Rhaenyra | `[F&B]` ✅ |
| Rhaenyra's sons dark-haired; Aemond claims Vhagar at Driftmark, loses an eye; sapphire; "lost an eye, gained a dragon" | `[F&B]` ✅ (◻ quote wording) |
| Viserys died 129 AC; greens hid it and crowned Aegon II in the Dragonpit; Rhaenyra crowned on Dragonstone | `[F&B]` ✅ |
| Lucerys and Arrax killed above Shipbreaker Bay by Aemond and Vhagar; the show makes it Vhagar's disobedience | `[F&B]`, `[SHOW:HOTD S1E10]` ✅ |
| Blood and Cheese; Rook's Rest (Rhaenys and Meleys die; Aegon II burned) | `[F&B]` ✅ |
| Dragonseeds; Nettles tamed Sheepstealer with a sheep a day; Two Betrayers at Tumbleton | `[F&B]` ✅ |
| HOTD S3 finale at Tumbleton, Aug 9, 2026; S4 final, planned for 2028 | web 2026-08/09 ✅ |
| Storming of the Dragonpit (the Shepherd); Joffrey died trying to reach Syrax | `[F&B]` ✅ |
| Battle above the Gods Eye: Daemon leaps onto Vhagar, Dark Sister through Aemond's eye; all fall into the lake | `[F&B]` ✅ |
| Rhaenyra fed to Sunfyre on Dragonstone, her son Aegon made to watch; Aegon II poisoned within the year | `[F&B]` ✅ |
| Aegon III crowned at about 11; melancholy, "Broken King", "Dragonbane"; last dragon 153 AC, a small sickly green female; nine mages failed | `[F&B]`, `[W]` ✅ (◻ age at crowning) |
| Daeron I, the Young Dragon: conquered Dorne at 14, wrote *The Conquest of Dorne*, killed under a peace banner at 18 | `[W]` ✅ |
| Baelor walked barefoot to Dorne; went into the viper pit to free Aemon; bitten; Aemon carried him out; Maidenvault; Great Sept; died fasting | AWOIAF Baelor I ✅ |
| Great Sept destroyed in the show (S6), not in the books | `[SHOW:GoT S6E10]`, `[B:AFFC]` ✅ |
| Aegon IV: mistresses, bastards, wooden dragons burned, deathbed legitimization; gave Blackfyre to Daemon | `[W]` ✅ |
| Daeron II "the Good"; Dorne joined by marriage (187 AC); rumours he was the Dragonknight's son | `[W]` ✅ |
| Daemon Blackfyre reversed colours (black dragon on red); Redgrass Field 196 AC; Bloodraven's Raven's Teeth kill Daemon and his twin sons; Baelor Breakspear and Maekar; Bittersteel founds the Golden Company | `[W]`, `[D&E]` ✅ |
| Five Blackfyre rebellions; the last in 260 AC, Maelys killed by Barristan Selmy | `[W]` ✅ |
| Bloodraven Hand; "How many eyes does Lord Bloodraven have? A thousand eyes, and one."; Great Spring Sickness 209 AC killed Daeron II; sent to the Wall; Lord Commander; vanished; Bran finds him | `[D&E: The Mystery Knight]`, `[W]`, `[B:ADWD]` ✅ |
| Egg: fourth son of a fourth son, shaved head, squire to Dunk; three Dunk and Egg tales; *A Knight of the Seven Kingdoms* TV | `[D&E]` ✅ |
| Great Council of 233 AC: Aemon refused (maester), Egg chosen; Aemon to the Wall; blind maester at Castle Black | `[W]`, `[B:AGOT]` ✅ |
| Aegon V helped the smallfolk, lords resisted; Dunk Lord Commander of the Kingsguard | `[W]` ✅ |
| Summerhall 259 AC: birth of the first great-grandchild; Maester Corso's ink-blotted letter (fragments quoted); Aegon V, Prince Duncan and Ser Duncan the Tall died; Rhaegar born that day; Rhaegar went there to brood and play his harp | AWOIAF Tragedy at Summerhall ✅, `[B:ADWD Barristan]` ✅ |
| Prince Duncan gave up his claim for Jenny of Oldstones; her friend the woods witch = the ghost of High Heart; the prophecy that the prince that was promised comes from the line of Aerys and Rhaella | `[W]`, `[B:ADWD Barristan]`, `[B:ASOS Arya]` ✅ (the woods witch = ghost of High Heart link is told as what "many readers believe") |
| Aerys II at 18; Tywin Hand ~20 years; jealousy; Duskendale 277 AC, half a year captive; Barristan's rescue; hair and nails; pyromancers | `[W]`, `[B:ASOS/ADWD]` ✅ |
| Harrenhal tourney 281 AC; Rhaegar crowns Lyanna with blue winter roses passing Elia; "all the smiles died" | `[B:AGOT Eddard]` ✅ |
| Brandon and Rickard put to death; Jon Arryn refuses; Trident; rubies → Ruby Ford | `[B:AGOT]`, `[W]` ✅ |
| Sack: Tywin; Jaime kills Aerys ("Burn them all"); wildfire caches; Jaime tells Brienne in the Harrenhal bath | `[B:ASOS Jaime V]` ✅ |
| Lyanna "bed of blood", "Promise me, Ned" | `[B:AGOT Eddard]` ✅ |
| Daenerys born on Dragonstone in a storm that wrecked the fleet; Rhaella died; Braavos house with the red door and lemon tree; Viserys the beggar king; mother's crown sold | `[B:AGOT Daenerys I]`, `[W]` ✅ |
| Sold to Drogo; three petrified eggs; molten gold crown; "He was no dragon"; pyre; Drogon, Rhaegal, Viserion | `[B:AGOT]` ✅ |
| Red Waste; Astapor, Yunkai, Meereen; Drogon leaves the fighting pit; Dothraki Sea | `[B:ACOK–ADWD]` ✅ |
| Aemon dies at sea, "Egg, I dreamed that I was old" | `[B:AFFC Samwell]` ✅ (◻ exact wording) |
| Young Griff claims to be Aegon; Golden Company; Blackfyre theory | `[B:ADWD]` ✅ (theory labelled) |
| Jon = Aegon Targaryen in the show (S7); R+L=J theory in the books | `[SHOW:GoT S7]` ✅ |
| Show ending (S8): King's Landing burned, Jon kills Daenerys, Drogon melts the throne | `[SHOW:GoT S8]` ✅ |
| *Winds* and *F&B* vol. 2 unpublished (Nov 2026) | ✅ |

**Language softening for TTS and moderation:**
- The deaths at the Gods Eye, Dragonstone and the Sack are told without gore: "did not survive", "gave his half-sister to the dragon".
- The visuals follow the violence rule.

---

## Open questions for the director
1. **Mockups:** I read "mockups" as **in-video document and artifact mockups**: parchments, letters, decrees, the Dragon Registry, the family tree and coins, with real legible text set in code. If you meant **thumbnail or YouTube-page mockups** (or both), say so and I'll add them at the packaging stage.
2. **Length:** at 6,850 words this runs about 46–47 min. I can trim to exactly 45 or expand to about 55 (more on Rhaenyra and Daemon's years, or the Blackfyre rebellions).
3. **End card:** keep WATCH NEXT: THE OTHERS, or point to a Targaryen follow-up, such as "The Dance of the Dragons: Book vs Show"?
