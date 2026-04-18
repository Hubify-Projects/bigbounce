# P3-B-DESI-EXT findings — DESI DR1 top-1000 CDS-XMatch sweep
**Date:** 2026-04-18
**Method:** CDS X-Match (astroquery.xmatch.XMatch), 20 curated catalogs, 10.0" radius.
**Closes:** P3-B-DESI-EXT.

## Sample
- Top 1000 DESI DR1 anomalies by score desc
- Score range: [12.676, 25.158]
- Ordering caveat: top-by-score, not top-SIMBAD-novel (DESI is ~99 % SIMBAD-novel at top 10K)

## Headline
- **Archival-ID rate: 82.2 %** (822/1000)
- Unmatched (not in any of 20 curated catalogs): 178
- Wall time: 13.6 s (0.2 min)

## Per-catalog match counts
| Catalog | Matched tids |
|---|---:|
| Gaia_DR3 | 85 |
| SDSS_DR16 | 368 |
| SDSS_DR12 | 321 |
| DESI_LS_DR9_N | 191 |
| DESI_LS_DR9_S | 559 |
| DES_DR2 | 67 |
| Pan-STARRS1_DR2 | 318 |
| AllWISE | 263 |
| CatWISE2020 | 492 |
| 2MASS_PSC | 34 |
| unWISE | 494 |
| GALEX_AIS_DR5 | 29 |
| GALEX_AIS_v2 | 37 |
| Chandra_CSC | 0 |
| XMM_4XMM-DR13 | 1 |
| NVSS | 1 |
| VLASS_QL | 1 |
| USNO-B1 | 133 |
| UCAC5 | 7 |
| APASS9 | 2 |

## Comparison to v2 SDSS
- v2 SDSS DR18 top-20 SIMBAD-novel → 100 % (20/20) via VizieR all-catalogs web API
- This run DESI DR1 top-1000 → 82.2 % via 20-catalog curated X-Match
- Methodological note: curated list is a subset of VizieR's ~25 k tables. A curated match is sufficient proof the anomaly is NOT uncataloged; a curated non-match is NOT proof of true novelty (could still be in a long-tail catalog).

## Paper 3 §5.1 implication
- The §5.1 honesty footnote (committed `0364a5d`) already reframes SIMBAD-novel as an upper bound on true novelty. This DESI-scale result operationalizes it on Paper 3's largest survey.
- Recommend the footnote cite the DESI rate (82 % on top-1000) alongside the SDSS rate (100 %).

## Files
- `projects/cross_survey/results/desi_xmatch_summary.json` — per-object JSON
- `projects/cross_survey/results/P3-B-DESI-EXT_findings.md` — this file
- `projects/cross_survey/desi_xmatch_crossmatch.py` — script
