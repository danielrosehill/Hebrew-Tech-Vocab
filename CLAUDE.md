# Hebrew Tech Vocab

## Project Overview

A bilingual Hebrew-English tech vocabulary dictionary. Words go through two flows:

1. **Flow 1 (Machine)**: Daniel defines words → Claude retrieves translations → populates `dictionary/dictionary.json` with `human_verified: false`
2. **Flow 2 (Human)**: A native speaker reviews → confirms or corrects → sets `human_verified: true`, adds notes

### Key Files

- `dictionary/dictionary.json` — Source of truth for all vocabulary entries
- `process/to-add/` — Words queued for translation (organized by theme)
- `sources/` — Reference material and screenshots

### Dictionary Entry Schema

Each entry in `dictionary.json` should follow this structure:

```json
{
  "english": "rate limiting",
  "hebrew": "הגבלת קצב",
  "transliteration": "hagbalat ketzev",
  "category": "networking",
  "type": "translation|transliteration|hybrid",
  "example_en": "The server is rate limiting me",
  "example_he": "השרת מגביל את הקצב שלי",
  "human_verified": false,
  "human_notes": null,
  "source": "claude"
}
```

### Translation Guidelines

- Prefer the word people actually use in Israeli tech, not the "official" Academy Hebrew
- Flag when both a transliteration (e.g., בלוטוס) and a Hebrew coinage exist
- Note if a term is falling out of favor or is generational
- Use nikud (vowel marks) only when disambiguation is needed

## Slash Commands

### /add-words
Process words from `process/to-add/` files. For each word:
1. Read the English term and example sentence
2. Provide Hebrew translation, transliteration, category, and type classification
3. Generate a Hebrew example sentence
4. Append the entry to `dictionary/dictionary.json` with `human_verified: false`
5. Remove the processed word from the to-add file

### /review
Display the current dictionary entries that have `human_verified: false` in a readable table format (English | Hebrew | Transliteration | Category) so Daniel can share with a native speaker for review.

### /verify
Mark specific dictionary entries as human-verified. Accepts the English term and optional human notes. Sets `human_verified: true` and appends any notes.

### /stats
Show dictionary statistics: total entries, verified vs unverified, breakdown by category and type (translation/transliteration/hybrid).

### /export-anki
Export the dictionary to an Anki-compatible TSV file with columns: front (English + example), back (Hebrew + transliteration + example).

### /tts-script
Generate a TTS learning script from the dictionary. Alternates English and Hebrew with pauses, suitable for spaced-repetition audio episodes. Output as a structured text file ready for TTS processing.

### /find
Search the dictionary for a specific English or Hebrew term and display its full entry.

### /add-source
Add a new source document or screenshot to `sources/` with a corresponding markdown description file.
