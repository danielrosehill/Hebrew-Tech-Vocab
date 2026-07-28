---
description: Export the dictionary to an Anki-importable TSV
---

Run `python3 scripts/export_anki.py` with any filters implied by $ARGUMENTS —
`--domain`, `--verified-only`, `--min-confidence`.

Report the path and note count, and remind about the import settings that
otherwise produce a broken deck: field separator **Tab**, **Allow HTML in
fields** ticked, and the note type's field set to RTL so Hebrew renders correctly.

The TSV is regenerated wholesale each time. It is committed for convenience, but
`dictionary/dictionary.json` is the source of truth — never edit the TSV.
