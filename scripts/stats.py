#!/usr/bin/env python3
"""Summarise the dictionary: size, coverage by domain, and what needs review.

    python3 scripts/stats.py
"""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DICT = ROOT / "dictionary" / "dictionary.json"


def bar(n: int, total: int, width: int = 24) -> str:
    filled = round(width * n / total) if total else 0
    return "#" * filled + "." * (width - filled)


def table(title: str, counts: Counter, total: int) -> None:
    print(f"\n{title}")
    for key, n in counts.most_common():
        print(f"  {key:<14} {n:>4}  {bar(n, total)}")


def main() -> None:
    data = json.loads(DICT.read_text(encoding="utf-8"))
    entries = data["entries"]
    total = len(entries)

    verified = sum(1 for e in entries if e.get("human_verified"))
    with_example = sum(1 for e in entries if e.get("example_he"))
    with_source = sum(1 for e in entries if e.get("seen_at"))
    with_alts = sum(1 for e in entries if e.get("alternatives"))

    print(f"Hebrew Tech Vocab — {total} entries, updated {data['updated']}")
    print(f"  human verified   {verified:>4} / {total}")
    print(f"  with an example  {with_example:>4} / {total}")
    print(f"  with a source    {with_source:>4} / {total}")
    print(f"  with alternates  {with_alts:>4} / {total}")

    table("By domain", Counter(e["domain"] for e in entries), total)
    table("By register", Counter(e["register"] for e in entries), total)
    table("By type", Counter(e.get("type", "unset") for e in entries), total)
    table("By confidence", Counter(e["confidence"] for e in entries), total)

    review = [e for e in entries
              if not e.get("human_verified") and e["confidence"] in ("low", "medium")]
    if review:
        print(f"\nQueue for the native-speaker pass ({len(review)}):")
        for e in sorted(review, key=lambda x: x["confidence"]):
            flag = "!" if e["confidence"] == "low" else " "
            print(f"  {flag} {e['he']:<20} {e['en']}")


if __name__ == "__main__":
    main()
