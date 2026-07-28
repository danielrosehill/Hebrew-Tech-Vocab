# Source: electrical cable subcategories

**Captured:** 2026-07-28
**Vendor:** unidentified Israeli cable supplier — the first result returned when
searching for a power cable. URL not recorded at capture time; if this vendor is
identified later, rename this folder to the vendor slug and note it here.
**Image:** `cables/cable-subcategories.png`

## What the page is

A category grid on a cable supplier's site, splitting cable into eight
subcategories with a representative product photo for each. Eight tiles, in the
order they appear right-to-left:

| Hebrew | Entry id |
|---|---|
| אביזרים לכבלים | `cable-accessories`, `cable-lug` |
| כבלים גמישים | `flexible-cable` |
| כבלי פיקוד | `control-cable`, `shielded` |
| כבלי כוח מתח ביניים | `medium-voltage`, `power-cable` |
| כבלי כוח מתח נמוך | `low-voltage` |
| כבלים מיוחדים | — (too vague to enter) |
| כבלים חסיני אש | `fire-resistant-cable` |
| חוטים | `wire` |

## Why it was captured

The starting point was an ordinary need — basic cable for a five-metre run,
terminated at home — and no way to tell from the category names which tile leads
there. This is the exact failure the repository is for: every one of these eight
translates cleanly and none of the translations tells you where to click.

The answer, for the record: **כבלים גמישים** for a lead you terminate yourself,
**חוטים** if you are pulling single conductors through existing conduit. The two
מתח tiles are the utility/installation split and neither is a false lead so much
as a scale filter.

## What the page taught beyond its own words

- **מתח נמוך does not mean what an English speaker hears.** In distribution terms
  it covers ordinary 230V mains. There is no tile here for what an anglophone
  calls low voltage. See `low-voltage`.
- **The photos disambiguate what the words cannot.** The armour on the מתח ביניים
  tile, the tinned braid on the פיקוד tile, and the orange sheath on the חסיני אש
  tile each identify the cable faster than the label does. Worth keeping the image
  rather than only the terms.
- **כבלים מיוחדים ("special cables") is a genuine catch-all**, not a term. Left
  out of the dictionary deliberately.

## Follow-ups

- Identify the vendor and record the URL.
- Confirm `stranded` (שזור vs גדילי) and `per-metre` (מטר vs מטר רץ) against a
  real shelf label or a counter conversation — both are `confidence: low`.
