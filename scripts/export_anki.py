#!/usr/bin/env python3
"""Export the dictionary as an Anki-importable TSV.

Anki's plain-text importer takes tab-separated fields, one note per line, with
HTML allowed inside a field. Newlines inside a field must therefore be <br>,
not literal newlines. Fields exported, in order:

    front  back  tags

    python3 scripts/export_anki.py                     # everything, to anki/
    python3 scripts/export_anki.py --domain electrical # one domain
    python3 scripts/export_anki.py --verified-only     # human-checked only
    python3 scripts/export_anki.py --min-confidence medium

Import settings in Anki: field separator Tab, "Allow HTML in fields" ticked,
and set the note's deck language/direction so Hebrew renders RTL.
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DICT = ROOT / "dictionary" / "dictionary.json"
OUT_DIR = ROOT / "anki"

CONF_ORDER = {"low": 0, "medium": 1, "high": 2}


def esc(text: str) -> str:
    """Anki TSV: tabs break the row, newlines break the note."""
    return text.replace("\t", " ").replace("\n", "<br>")


def build_front(e: dict) -> str:
    parts = [f"<b>{esc(e['en'])}</b>"]
    if e.get("gloss"):
        parts.append(f"<div style='font-size:0.85em;color:#666'>{esc(e['gloss'])}</div>")
    if e.get("example_en"):
        parts.append(f"<div style='font-size:0.85em'><i>{esc(e['example_en'])}</i></div>")
    return "".join(parts)


def build_back(e: dict) -> str:
    parts = [f"<div dir='rtl' style='font-size:1.6em'>{esc(e['he'])}</div>",
             f"<div style='color:#666'>{esc(e['translit'])}</div>"]

    if e.get("pos") == "noun":
        bits = []
        if e.get("gender") in ("m", "f"):
            bits.append(e["gender"])
        if e.get("plural_he"):
            bits.append(f"pl. <span dir='rtl'>{esc(e['plural_he'])}</span>")
        if bits:
            parts.append(f"<div style='font-size:0.85em;color:#888'>{' · '.join(bits)}</div>")

    if e.get("example_he"):
        parts.append(f"<div dir='rtl' style='margin-top:0.5em'>{esc(e['example_he'])}</div>")

    for alt in e.get("alternatives", []):
        parts.append(
            f"<div style='font-size:0.8em;color:#888;margin-top:0.4em'>"
            f"<span dir='rtl'>{esc(alt['he'])}</span> "
            f"({esc(alt['register'])}) — {esc(alt['note'])}</div>")

    if e.get("notes"):
        parts.append(f"<div style='font-size:0.8em;color:#a00;margin-top:0.5em'>"
                     f"{esc(e['notes'])}</div>")

    return "".join(parts)


def build_tags(e: dict) -> str:
    tags = [e["domain"], e["register"], e["confidence"]]
    if e.get("subdomain"):
        tags.append(e["subdomain"])
    if e.get("human_verified"):
        tags.append("verified")
    return " ".join(t.replace(" ", "-") for t in tags)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain")
    ap.add_argument("--verified-only", action="store_true")
    ap.add_argument("--min-confidence", choices=["low", "medium", "high"], default="low")
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args()

    entries = json.loads(DICT.read_text(encoding="utf-8"))["entries"]

    if args.domain:
        entries = [e for e in entries if e["domain"] == args.domain]
    if args.verified_only:
        entries = [e for e in entries if e.get("human_verified")]
    floor = CONF_ORDER[args.min_confidence]
    entries = [e for e in entries if CONF_ORDER[e["confidence"]] >= floor]

    if not entries:
        print("Nothing matched those filters.")
        return

    out = args.output
    if out is None:
        OUT_DIR.mkdir(exist_ok=True)
        stem = f"hebrew-tech-vocab-{args.domain}" if args.domain else "hebrew-tech-vocab"
        out = OUT_DIR / f"{stem}.tsv"

    lines = [f"{build_front(e)}\t{build_back(e)}\t{build_tags(e)}" for e in entries]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} notes to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
