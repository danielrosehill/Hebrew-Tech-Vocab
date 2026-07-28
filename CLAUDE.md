# Hebrew Tech Vocab

A bilingual Hebrew-English dictionary of technical and trade vocabulary — not
only software. Electrical, plumbing, hardware, tools, and the counter Hebrew for
buying them. See `README.md` for why.

## The one thing to get right

The project exists because Google Translate answers a different question than the
one being asked. It returns *a* correct Hebrew word; what is needed is *the* word
a supplier will recognise across a counter.

**So `he` holds the word to actually use, not the word that is officially
correct.** Where those differ, the official term goes in `alternatives` with a
note on who uses it. The canonical case: a circuit breaker is **אוטומט** in `he`,
with מא"ז / מפסק אוטומטי זעיר in `alternatives` as the formal form nobody says.

An entry that records only the meaning has failed, even when the translation is
right.

## Adding vocabulary

Use the **`vocab-capture` skill** (`.claude/skills/vocab-capture/SKILL.md`). It
covers both directions — Daniel explaining a term he has learned in the field, and
Daniel asking for research on one he hasn't — and it handles saving and
documenting the source image. Read it before writing any entry.

Field semantics live in `dictionary/schema.json`, which is the authority on what
each field means. Do not restate the schema here.

Do not add entries by hand-editing `dictionary.json` without going through the
skill's checks; the register research is the work, and skipping it produces
exactly the useless-but-correct output the repo was built to replace.

## Layout

| Path | |
|---|---|
| `dictionary/dictionary.json` | Source of truth |
| `dictionary/schema.json` | Field semantics |
| `sources/<slug>/` | Screenshots; sibling `sources/<slug>.md` documents each |
| `process/to-add/` | Words wanted where there is no source to capture |
| `scripts/` | `validate.py`, `stats.py`, `export_anki.py` — stdlib only, no deps |
| `anki/` | Generated deck; regenerated wholesale, never edited |
| `learning/` | TTS episode scripts |

## Conventions

- Run `python3 scripts/validate.py` after touching the dictionary. It catches
  duplicate ids, bad enum values, and `seen_at` paths pointing at images that
  aren't in the repo.
- Append to `entries`; never reorder or renumber. The file is reviewed by a human
  in a diff, so keep changes local.
- `id` is kebab-case and permanent once written.
- Bump `updated` at the top of the dictionary on every change.
- Nikud only where it disambiguates. Transliteration is plain Latin, no diacritics.
- Confidence is set honestly. A wrong `high` costs far more than an admitted `low`,
  because `low` is the queue the native-speaker pass works from.

## Researching Israeli vendor sites

Many geo-fence to Israeli IPs, so `WebFetch` returns a wall or nothing. Use
`mcp__gateway__fetch-and-convert__fetch_markdown`, which egresses from the home
Israeli residential connection, and `mcp__gateway__playwright__browser_navigate`
for JS-rendered pages.

## Slash commands

`/verify` `/find` `/stats` `/export-anki` `/tts-script` — defined in
`.claude/commands/`, which is the authority on their behaviour.

## Related repos

`Hebrew-TTS-Providers` (which TTS handles Hebrew), `English-Hebrew-Translation`
(translation APIs and MCP servers), `Hebrew-Language-Projects-Index`.
