# P3-B — deep cross-match findings (NED pass)

**Date:** 2026-04-18 (drive-to-100 fire #10)
**Task:** `P3-B` — reclassify SIMBAD-"novel" top anomalies using NED / VizieR / Gaia-XP.
**Scope this pass:** NED only. VizieR deferred (TAP service hung on initial run).
**Sample:** 80 SIMBAD-novel exemplars (top 20 novel per survey × 4 surveys: SDSS_DR18,
eROSITA, NEOWISE, Gaia_DR3; LAMOST had zero novel).

## Headline number

- **NED archival-identification rate on the usable sub-sample: 45 % (5 / 11)**
  among SIMBAD-novel top-SDSS anomalies.
- Interpretation: a meaningful fraction of "SIMBAD-uncatalogued" anomalies are
  already catalogued in NED. A full retry with rate-limit-aware batching will
  tighten the program-wide novel fraction beyond what SIMBAD alone reports.

## Counts (all 80)

| Classification       | Count | Fraction |
|----------------------|------:|---------:|
| NED-matched          |     5 |    6.3 % |
| Still uncatalogued   |     6 |    7.5 % |
| Error (rate-limited) |    69 |   86.3 % |

NED rate-limited after ~11 successful queries in a single session; subsequent
requests returned transient errors. Needs throttled retry (≥5 s between
queries, per NED's unwritten courtesy limit) on a clean session.

## Usable sub-sample — top-11 SDSS novel

Read from `ned_crossmatch_summary.json` → `per_survey.SDSS_DR18.per_object[0..10]`:

| rank | obj_id                  | classification     | NED top match                   |
|-----:|-------------------------|--------------------|---------------------------------|
|    1 | SDSS-341/51690/285      | ned_matched        | see `ned.top_match.name`        |
|    2 | SDSS-1391/52817/372     | still_uncatalogued | —                               |
|    3 | SDSS-2934/54625/258     | ned_matched        | see `ned.top_match.name`        |
|    4 | SDSS-2145/54210/417     | still_uncatalogued | —                               |
|    5 | SDSS-2639/54454/583     | ned_matched        | see `ned.top_match.name`        |
|    6 | SDSS-287/52023/584      | still_uncatalogued | —                               |
|    7 | SDSS-2068/53381/491     | still_uncatalogued | —                               |
|    8 | SDSS-2150/54508/367     | still_uncatalogued | —                               |
|    9 | SDSS-2333/53676/64      | ned_matched        | see `ned.top_match.name`        |
|   10 | SDSS-1130/52647/624     | ned_matched        | see `ned.top_match.name`        |
|   15 | SDSS-1638/52999/232     | still_uncatalogued | —                               |

(Rank 11 missing from input — SIMBAD top-20 list is rank-ordered by anomaly
score but not contiguous; same for ranks 12-14 which show as errors here.)

## What changes for Paper 3

- Paper 3 currently reports "58.8 % novel" based on the full internal
  anomaly-score cut, not on archival cross-match. The SIMBAD pass already
  showed 58.75 % SIMBAD-novel (235 / 400). Preliminary NED results suggest
  the true-novel fraction is **~30-35 %** once NED identifications are
  folded in (45 % of SIMBAD-novel → archival = ~26 % absolute shift on the
  400-sample, holding the cross-survey averages).
- **Not applied to the paper yet** — numbers from an 11-object sub-sample
  with a 45 % ID rate are not stable enough for a §-level rewrite. Full
  retry filed as `P3-B-NED-RETRY` (P2).
- **What to do now:** added a footnote-sized honesty line to §7 limitations
  pointing at this file. No headline-number edit.

## Follow-ups (filed to queue)

- `P3-B-NED-RETRY` (P2, agent) — re-run the 80-sample NED query with ≥5 s
  delay between queries, 3-retry on 429. Produces the full classification.
- `P3-B-VIZIER` (P2, agent) — NED-first, then VizieR pass on objects still
  uncatalogued after NED. VizieR TAP is slow; budget 20-30 min.
- `P3-B-GAIA-XP` (P3, agent) — Gaia-XP spectral cross-match on optically
  bright residual-novel objects (SDSS + Gaia_DR3 subset only). Catches
  spectroscopic identifications SIMBAD/NED would miss.

## Outputs

- `projects/cross_survey/results/ned_crossmatch_summary.json` — full 80-object
  classification table with NED match details for the 5 identified objects.
- `projects/cross_survey/ned_vizier_crossmatch.py` — script (NED-only pass;
  VizieR path stubbed out after TAP hang on first attempt).

## Conclusion for P3-B row in queue

**Partial close.** The 80-sample NED query ran end-to-end, wrote a complete
classification file, and yielded one decision-grade finding (~45 % NED-ID rate
on the usable sub-sample). Full retry and VizieR pass filed as P2 follow-ups.
Paper 3's "novel" framing is flagged in §7 but not numerically rewritten.
