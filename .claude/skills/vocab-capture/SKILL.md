---
name: vocab-capture
description: Turn a screenshot of an Israeli product listing, sign, spec sheet or invoice into dictionary entries. Use whenever Daniel pastes an image of Hebrew technical or trade vocabulary, or describes a term he has learned in the field. Handles both directions — he explains a term he knows, or asks for research on one he doesn't.
---

# Vocabulary capture

The repository exists because Google Translate answers a different question than
the one being asked. It returns *a* correct Hebrew word. What is needed is *the*
word a supplier will recognise across a counter in Jerusalem.

Every entry therefore has to record register, not just meaning.

## The two directions

A capture starts with an image, a link, or a spoken observation. Establish which
direction it is before doing anything else — if it is not stated, ask, in one line.

### Direction A — "I don't know this"

Daniel is looking at something he cannot resolve. Research it, then write entries
marked `"source": "claude"`, `"human_verified": false`, with an honest
`confidence`.

1. Read every Hebrew string in the image. Do not skip ones that look like
   boilerplate — category names are exactly the vocabulary being hunted.
2. For each candidate term, decide whether it earns an entry. It does if any of:
   it names a thing he might have to ask for; it is a category label he would need
   to navigate a site; it is a false friend; the machine translation is misleading.
   It does not if it is a brand, a model number, or transparent English.
3. Research the register. This is the actual work, and it is not translation:
   - What does a supplier's site call it (catalogue Hebrew)?
   - What would a tradesperson say out loud (trade Hebrew)?
   - Is there an Academy term nobody uses? That goes in `alternatives`, never in `he`.
   - Is the English word simply used as-is? Then `type: borrowed` and say so.
4. Write the entry. `he` is the form to actually use. Everything else is `alternatives`.
5. Set `confidence` honestly. `low` is not a failure — it is the queue for the
   native-speaker pass, and a wrong `high` is far more expensive than an admitted
   `low`. Where uncertain, say in `notes` exactly what needs checking.

**Researching Israeli vendor sites:** many geo-fence to Israeli IPs. `WebFetch`
will fail or return a wall. Use `mcp__gateway__fetch-and-convert__fetch_markdown`,
which egresses from the home Israeli residential connection, and
`mcp__gateway__playwright__browser_navigate` for anything JS-rendered. Ivory,
Zap, and the trade wholesalers are all worth reading directly rather than guessing.

### Direction B — "I know this"

Daniel is recording something learned in the field — from a tradesperson, a shop
counter, a delivery, a failed purchase. **This is the higher-value direction.**
It is first-hand register data, which is the one thing research cannot supply.

1. Capture what he said, in his framing. If he says a word is what people
   *actually* say, that word becomes `he` even if it contradicts every dictionary.
2. Set `"source": "daniel"`, `"human_verified": true`, `"confidence": "high"`.
3. Put the anecdote in `human_notes` — who said it, in what shop, what the
   misunderstanding was. The story is the mnemonic and is worth more than the gloss.
4. Do not sand it down into neutral catalogue prose. "The guy in the shop had no
   idea what I meant until I said אוטומט" is the useful record.
5. If an entry already exists from Direction A, upgrade it in place: correct `he`,
   flip `human_verified`, keep the machine guess in `alternatives` if it is a real
   form, and delete it if it was simply wrong.

## Saving the source image

Always save it. Screenshots of listings are kept as reference for a personal
glossary — fair use, unmodified, credited to the vendor by name in the source note.

- Vendor known → `sources/<vendor-slug>/<descriptive-name>.png`
- Vendor unknown → `sources/<topic-slug>/<descriptive-name>.png`
- Annotated version alongside the original, suffixed `-annotated`. Never overwrite
  the original — the circles are Daniel's reading of it and are themselves data.
- Name files for content, not `image copy 3.png`.

Each source folder has a sibling markdown file, `sources/<slug>.md`, which records:
vendor and URL, the date captured, what the page was, which entry `id`s came out
of it, and anything about the vendor's own naming habits worth remembering.
Add to that file on every capture; do not start a second one.

Reference the image from each entry's `seen_at` as a repo-relative path.

## Writing entries

Schema and field semantics: `dictionary/schema.json`. Read it before writing.

Rules that the schema cannot enforce:

- **`he` is the useful form, not the correct one.** אוטומט, not מפסק אוטומטי זעיר.
  If those two conflict, the conflict itself is the entry's reason to exist.
- **Nouns carry gender and plural.** A dictionary you cannot form a sentence from
  is a word list. Construct plurals (`נעל כבל` → `נעלי כבל`) matter most.
- **Examples are sentences said in a shop**, not textbook sentences. "קפץ לי
  האוטומט" teaches more than "המפסק האוטומטי נותק".
- **Notes carry the trap.** False friends (מתח נמוך is mains), homographs
  (מטען is also an explosive charge), brand-as-noun (וואגו), what the counter
  staff will assume you meant.
- **Roots are mnemonics.** Note them where they help: מסוכך from סכך, as in סוכה.
- `id` is kebab-case, stable, never renamed once written.
- Append to `entries`; do not reorder existing ones. Keep the file readable —
  it is reviewed by a human in a diff.
- Bump `updated` at the top of the file.

## After writing

State plainly: how many entries added, how many are `low` confidence and why,
and which ones you would most want a native speaker to check. Do not claim a
term is in use if what you actually did was translate it.
