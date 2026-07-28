---
description: Look up a term in the dictionary, in either language
---

Search `dictionary/dictionary.json` for: $ARGUMENTS

Match against `en`, `he`, `translit`, `gloss` and `alternatives[].he`. Hebrew
input may arrive without final-letter normalisation or with a definite article
prefixed — strip a leading ה and try again before concluding there is no match.

For each hit, show the Hebrew, transliteration, gender and plural, the example
sentence, any alternatives with their register, and the usage note. Say whether
it is human verified.

If nothing matches, say so in one line and offer to research and add it via the
`vocab-capture` skill — do not silently invent an answer, which is the failure
mode this whole repository exists to avoid.
