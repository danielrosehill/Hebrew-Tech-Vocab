---
description: Generate a spaced-repetition audio script from the dictionary
---

Produce a script for a TTS-generated vocabulary episode, written to
`learning/episode-<date>-<topic>.md`.

Selection: $ARGUMENTS may give a domain, a confidence floor, or a count. Absent
that, take entries not covered in the most recent episode in `learning/`,
weighted towards `high` confidence — do not drill a term into memory before a
native speaker has confirmed it.

Structure each item so it works with eyes closed and hands full, which is when
this gets listened to:

1. English term, then a pause.
2. Hebrew, said slowly.
3. Hebrew again at natural speed.
4. The Hebrew example sentence.
5. One line of the usage note, in English, only where there is a genuine trap
   (false friend, wrong register, homograph). Skip it otherwise — the note is
   the payload for a handful of terms and dead air for the rest.

Mark language switches explicitly so a multilingual voice or a two-voice pipeline
can be driven from the file:

```
[EN] circuit breaker
[PAUSE 2s]
[HE-SLOW] אוטומט
[HE] אוטומט
[HE] קפץ לי האוטומט
[EN] The formal term is מא"ז, but nobody says it out loud.
```

Israeli-accented Hebrew TTS with correct stress is the constraint here; see
`danielrosehill/Hebrew-TTS-Providers` for which providers currently handle it.
