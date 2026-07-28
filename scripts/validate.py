#!/usr/bin/env python3
"""Check dictionary.json against the schema's rules. Stdlib only, no deps.

Not a full JSON Schema implementation — it checks the things that actually go
wrong when entries are written by hand or by an LLM: missing required fields,
duplicate or malformed ids, bad enum values, and seen_at paths that point at
images which are not in the repo.

    python3 scripts/validate.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DICT = ROOT / "dictionary" / "dictionary.json"

REQUIRED = ["id", "en", "he", "translit", "domain", "register", "confidence",
            "human_verified"]

ENUMS = {
    "pos": {"noun", "verb", "adjective", "phrase", "abbreviation"},
    "gender": {"m", "f", "mf", "n/a"},
    "type": {"translation", "transliteration", "hybrid", "borrowed"},
    "register": {"trade", "colloquial", "formal", "borrowed"},
    "confidence": {"high", "medium", "low"},
}

ID_RE = re.compile(r"^[a-z0-9-]+$")
HEBREW_RE = re.compile(r"[֐-׿]")


def main() -> int:
    data = json.loads(DICT.read_text(encoding="utf-8"))
    entries = data["entries"]
    problems = []
    seen_ids = {}

    for i, e in enumerate(entries):
        where = f"entry {i} ({e.get('id', '<no id>')})"

        for field in REQUIRED:
            if field not in e or e[field] in ("", None):
                problems.append(f"{where}: missing required field '{field}'")

        eid = e.get("id", "")
        if eid and not ID_RE.match(eid):
            problems.append(f"{where}: id is not kebab-case")
        if eid in seen_ids:
            problems.append(f"{where}: duplicate id, first seen at entry {seen_ids[eid]}")
        seen_ids[eid] = i

        for field, allowed in ENUMS.items():
            if field in e and e[field] is not None and e[field] not in allowed:
                problems.append(f"{where}: {field}={e[field]!r} not in {sorted(allowed)}")

        # `he` should contain Hebrew unless the term is a straight borrowing.
        if e.get("type") != "borrowed" and not HEBREW_RE.search(e.get("he", "")):
            problems.append(f"{where}: 'he' has no Hebrew characters")

        for alt in e.get("alternatives", []):
            for field in ("he", "register", "note"):
                if field not in alt:
                    problems.append(f"{where}: alternative missing '{field}'")
            if alt.get("register") not in ENUMS["register"]:
                problems.append(f"{where}: alternative register={alt.get('register')!r} invalid")

        for path in e.get("seen_at", []):
            if path.startswith("http"):
                continue
            if not (ROOT / path).exists():
                problems.append(f"{where}: seen_at path not in repo: {path}")

        # A verified entry that nobody is credited for is usually a mistake.
        if e.get("human_verified") and not (e.get("human_notes") or e.get("verified_by")):
            problems.append(f"{where}: human_verified but no human_notes or verified_by")

    if problems:
        for p in problems:
            print(f"FAIL  {p}")
        print(f"\n{len(problems)} problem(s) across {len(entries)} entries.")
        return 1

    print(f"OK  {len(entries)} entries, no problems.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
