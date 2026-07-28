---
description: Run a native-speaker verification pass over unverified entries
---

Flow 2 of the project: a native Hebrew speaker is sitting here reviewing what the
machine produced. Your job is to make that as fast and as cheap for them as
possible, and to record what they say faithfully.

1. Run `python3 scripts/stats.py` and take the review queue from the bottom of
   the output. Work `low` confidence first — those are the ones where the machine
   flagged it did not know.
2. Present terms **a few at a time**, not as a wall. For each: the Hebrew, the
   English, and the specific doubt. A reviewer who is told "is this the word a
   supplier would use, or is it spec-sheet only?" gives a better answer than one
   shown a bare pair of words.
3. Record the verdict in the entry:
   - Confirmed → `human_verified: true`, `confidence: high`, `verified_by` set.
   - Corrected → replace `he` with what they said. Keep the old form in
     `alternatives` **only if it is genuinely used somewhere**; if it was simply
     wrong, delete it rather than preserving a mistake as a variant.
   - Coloured with usage ("nobody says that any more", "that's what my father's
     generation says", "only in Tel Aviv") → put it verbatim in `human_notes`.
     This commentary is the most valuable thing in the file and cannot be
     regenerated.
4. Set `source: "native-speaker"` on entries whose `he` the reviewer supplied.
5. Bump `updated`, run `python3 scripts/validate.py`, and report what changed.

$ARGUMENTS may name a domain or a specific term to focus the pass.
