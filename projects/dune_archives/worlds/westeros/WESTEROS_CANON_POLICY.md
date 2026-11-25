# WESTEROS — Canon Policy (Mythic Archives) · v1.1 · 2026-11-25

**Director's rule (2026-11-24):** *"GoT follows books, interviews, articles, and shows — but books are the first priority. Bring the books to life, from stories to artworks, down to small attributes and characteristics."*

## 1. Source hierarchy (higher always wins)

| Tier | Source | How we use it | Script tag |
|---|---|---|---|
| **1** | **The five novels:** *A Game of Thrones*, *A Clash of Kings*, *A Storm of Swords*, *A Feast for Crows*, *A Dance with Dragons* | The ground truth for events, dialogue, appearance, heraldry, objects and places. Quote or closely paraphrase. | `[B:<book> <chapter>]` e.g. `[B:AGOT Sansa II]` |
| **1b** | GRRM's other canon prose: *Tales of Dunk and Egg* (*A Knight of the Seven Kingdoms*), the published *Winds of Winter* sample chapters | Same weight as the novels, but sample chapters are flagged as "may change". | `[B:…]` / `[TWOW-sample]` |
| **2** | GRRM's in-world histories: *The World of Ice & Fire*, *Fire & Blood*, *The Rise of the Dragon*, *The Lands of Ice and Fire* (maps) | Canon, **but written in-world by maesters who can be biased or wrong.** Narrate it as an account ("the maesters record…", "according to Archmaester Gyldayn…"), never as flat fact when sources inside the book disagree. | `[W]` / `[F&B]` |
| **3** | GRRM's own words: interviews, *Not a Blog*, *So Spake Martin* answers, GRRM-approved art (e.g. Marc Simonetti's Iron Throne, which GRRM called "absolutely right") | Fills gaps the books leave (sizes, designs, intent). Name the source on screen or in narration ("Martin has said…"). | `[G:<source, date>]` |
| **4** | Reputable articles and reference sites (Tower of the Hand, A Wiki of Ice and Fire, major press) | For **finding** passages only. Every claim must be traced back to tiers 1–3 before it is scripted. | none (we cite the tier it points to) |
| **5** | HBO *Game of Thrones* / *House of the Dragon* | Only where the books say nothing, and always labelled. Also a deliberate content pillar: "Book vs Show" segments. **Never** silently replace a book detail with a show detail. | `[S]` + narration "In the show…" |

**Conflicts:**
- Book vs show → book.
- Novel vs in-world history → the novel, then note the discrepancy if it is interesting.
- Two maester accounts disagree → present both ("Some say… others claim…"). Do not pick one silently.
- GRRM interview vs book → the book, unless GRRM explicitly corrected an error (e.g. a later-edition fix).

## 2. Unresolved mysteries and theories
- Theories (R+L=J, Azor Ahai, Aegon's identity, etc.) are always framed as theories with the textual evidence shown. **Never stated as fact**, even where the show confirmed them. Example: "The show confirmed it. The books have not."
- The open questions go into an episode's "mystery" beat. They are strong debate questions for the end card.

## 3. Fact-check gate (every script, before VO)
1. Every factual sentence carries a tag (tags are removed from the spoken text automatically).
2. Each `[B]` claim names its chapter. Spot-check at least 20 claims against the text, as DUN003 did (22/22 PASS).
3. `[S]` claims are listed in a "show-only" table at the end of the script, so the director can see exactly what the books don't say.
4. Book-accurate ages, appearances and heraldry are taken from `WESTEROS_BOOK_LOOKS.md`. Any new character gets an entry there first.

## 4. Content safety (needed for both platforms and the generators)
- **Ages follow the books:** Daenerys is 13 at her wedding, Sansa 11, Arya 9, Bran 7, Robb and Jon 14.
  - No child or teenager is ever depicted in a sexual or suggestive way, including the Dothraki wedding and the Sansa–Tyrion wedding.
  - Weddings are shown as ceremony and spectacle. Wedding nights are not shown or described.
- **No nudity.** Torture and sexual violence are referenced, not shown or described in detail.
- **Violence:** show the moment before and the aftermath (banners falling, music stopping, a goblet dropped), not gore.
  - Example: the Red Wedding is told through *The Rains of Castamere* starting and the doors closing.
  - Expect TTS and image moderation to block graphic lines, as happened on DUN001. Show softened lines to the director before recording.
- **No actor likenesses** from HBO or the films. Every character gets an original, book-described design (see the looks file).
- **No copying any artist's painting.** GRRM-approved art guides *what* a thing is (the throne's scale, asymmetry and steps), not a copy of the composition.

## 4b. Likeness rule: no actor or celebrity faces (v1.1, director's order, 2026-11-25)
**Why it matters on YouTube:**
- A photoreal AI image that looks like a real actor counts as synthetic content simulating an identifiable person. That person can file a privacy request to have the whole video removed; blurring is the only partial fix.
- Realistic likenesses also trigger YouTube's altered-or-synthetic disclosure rules, and HBO's costume and make-up designs (the show's Night King, for example) are their designs.
- An original, book-described face is legally cleaner and is the channel's selling point: *Westeros the way Martin wrote it*.

**Rules:**
1. Every face is an invented unknown person. Every prompt says: "must NOT resemble any actor or celebrity, especially the cast of Game of Thrones or House of the Dragon".
2. Anchor each character on **book attributes that differ from the show casting**. Hair colour, age, build and the scars or marks Martin gives them are the strongest levers (see the looks file).
3. Show-only characters and scenes (the show's Night King, the show-only Arya scene) appear only as silhouettes, from behind, or as hands and objects. No face, no HBO make-up.
4. **Face QC is mandatory for every still with a visible face.** View it at full size and ask: "Would a fan name an actor?" If yes or maybe, mark it FIX and redo it. The redo uses the corrected anchor and goes into the next wave of the same turn.
5. Delivered episodes are not exempt. If a likeness is found later, replace the still and re-render.

**Known drift types** (the generator pulls these looks toward the show; counter them on purpose):

| Look that drifts | Drifts toward | Counter with book attributes |
|---|---|---|
| Dark-haired bearded man in a black Night's Watch fur cloak | Show's Jon Snow | Age, gaunt or long face, grey-streaked or braided hair, scars, a different beard |
| Heavy young man in black | Show's Sam | Pink moon face, several chins, clean-shaven, fair hair |
| Boy with a brown mop of hair | Show's Bran | Tully auburn-red hair, blue eyes, freckles, age 7–9 |
| Red-haired wildling girl | Show's Ygritte | Round peasant face, pug nose, slightly crooked teeth, pale blue eyes |
| Silver-haired young woman | Show's Daenerys | Age 13–15, violet eyes, book costume |

GOT001 casualties fixed in turn 67: S001 (Night's King anchor redesigned), S004, S005, S023, S026.

## 5. Practical consequence for production
The visual identity of a Westeros episode comes from **book descriptions**, not the show: the hulking Iron Throne, the Others in their shifting armor, Tyrion's mismatched eyes and ruined nose, the Hound's missing ear, the two-legged dragons. These differences are a selling point: *"This is Westeros the way Martin wrote it."*
