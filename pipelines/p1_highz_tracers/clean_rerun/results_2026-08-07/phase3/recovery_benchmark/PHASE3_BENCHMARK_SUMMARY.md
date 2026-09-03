# Ledger #8 — known-object recovery benchmark on the phase-3 S>8 sample

**SAMPLE-V1 (provenance under review: possible sky-fiber contamination —
negative TARGETIDs).** 3,232/3,810 rows (84.8%) of the enriched sample carry
negative `targetid` values. Coordinator is verifying the contamination claim;
pod 8ofv5d4ynu7hku is held running pending the verdict. **No paper-vs-release
decision is recorded here** — numbers below are reported as-is with this
caveat, per coordinator instruction (2026-09-03).

## VizieR positional cross-match (5 fetched reference classes vs S>8, n=3,810)

See `recovery_benchmark.md`/`.json` in this directory for the full Wilson-CI
table. Headline: **0/0/0/0/0 matches** across all 5 fetched reference classes
(BAL quasars, Roma-BZCAT blazars, CV/white-dwarf binaries, Lyman-alpha
emitters, superluminous-SN hosts) against the footprint-restricted reference
counts (27–5,285 candidates per class within DESI footprint). No class
clears the ledger #8 confirmed-class bar (>=1 class, enrichment >10x, >=5
matches). Consistent with — though not proof of — the contamination caveat:
if a large fraction of rows are sky-fiber placeholders rather than real
sources, a positional cross-match against real astrophysical catalogues
would be expected to under-recover.

Note: the benchmark script (`benchmark_known_object_recovery.py`) previously
crashed on sexagesimal RA/Dec strings from 4 of the 5 fetched VizieR classes
(ROMA-BZCAT, CV/WD binaries, LAEs, SLSN hosts return `"18 32 04.5"`-style RA,
not decimal degrees) — fixed in this session by parsing via
`astropy.coordinates.SkyCoord(unit=(u.hourangle, u.deg))` when the column is
not directly float-castable, converting to decimal degrees before the
existing `crossmatch_positional()` logic. No other script logic changed.

## Pod's own SIMBAD/NED cross-match (flagship_crossmatch_*.parquet)

- Matched: 92 / 3,810 (2.4%); Unmatched: 3,718 / 3,810 (97.6%)
- SIMBAD: 2/92 identified (`otype` = G, i.e. galaxy); 90/92 SIMBAD-blank
- NED: 91/92 identified — types: IrS (infrared source) 49, G (galaxy) 23,
  `*` (star) 14, UvS (UV source) 5, blank 1

## Taxonomy (descriptive families, Q1 labels; flagship_taxonomy.json)

8 descriptive clusters over the unmatched (no known-counterpart) population,
sizes: 1589, 1032, 556, 239, 142, 80, 47, 33 (sum 3,718 — matches the
SIMBAD/NED-unmatched count). These are unsupervised (UMAP + clustering)
groupings, not confirmed physical classes.

## Ledger #8 answer

**Deferred.** Per coordinator hold (2026-09-03), no paper-vs-release
decision is recorded while the negative-TARGETID / sky-fiber-contamination
provenance question is open. If contamination is confirmed, these numbers
(0 recovered reference classes, 2.4% SIMBAD/NED-matched) may reflect
non-astrophysical rows rather than a genuine null result on the anomaly
catalogue — the benchmark should be re-run against a contamination-filtered
sample once the coordinator's verdict lands.
