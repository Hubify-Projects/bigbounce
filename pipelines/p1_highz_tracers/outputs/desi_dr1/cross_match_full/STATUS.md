# Full Catalog Cross-Match Status

**Date:** 2026-03-26
**Issue:** CDS xMatch service is down (connection reset errors from both local and H200 pod)

## What we've confirmed so far (individual queries, NOT bulk)

| Database | Sample checked | Matches | Method | Status |
|----------|---------------|---------|--------|--------|
| SIMBAD | Top 100 | 0/100 (0%) | TAP individual queries | COMPLETE |
| NED | Top 50 | 3/50 (6%) | HTTP cone search | COMPLETE |
| SDSS DR18 | Top 50 | — | API returned 500 errors | RETRY NEEDED |
| Gaia DR3 | Top 50 | — | CDS API errors | RETRY NEEDED |

## What we still need (full 195,829 catalog)

| Database | Catalog ID | Why it matters | Status |
|----------|-----------|---------------|--------|
| AllWISE | vizier:II/328/allwise | 750M IR sources — are our objects known photometric sources? | CDS DOWN |
| SIMBAD | simbad | 17M characterized objects — are any already studied? | CDS DOWN |
| Gaia DR3 | vizier:I/355/gaiadr3 | 1.8B stars — are any Galactic stars? (parallax test) | CDS DOWN |
| SDSS DR16 | vizier:V/154/sdss16 | 1B photometric objects — coverage overlap? | CDS DOWN |
| Milliquas v8 | vizier:VII/290/catalog | 1M QSOs — are any known quasars? | CDS DOWN |
| Liang+2023 | Not in Vizier | Prior DESI EDR anomalies — overlap? | NEED CATALOG |
| Nicolaou+2026 | Not in Vizier | Prior DESI EDR anomalies — overlap? | NEED CATALOG |

## Plan when CDS recovers

Script `bulk_cross_match_all.py` is ready and tested. It uses CDS xMatch in 5K chunks with automatic fallback. Run it as soon as CDS services recover (typically within hours).

## Alternative approaches if CDS stays down

1. **Download AllWISE catalog locally** (~300GB) and use astropy cross-match
2. **Use IRSA TAP** (irsa.ipac.caltech.edu) for AllWISE instead of CDS
3. **Use ESA Gaia Archive** (gea.esac.esa.int) for Gaia instead of CDS
4. **Run on the H200 pod** with astroquery (already installed)

## What we CAN honestly say now

"Of the top 100 most anomalous DESI DR1 spectra, 0/100 are in SIMBAD and 3/50 checked are in NED (as IR sources only). Full catalog cross-matching against AllWISE, Gaia, SDSS, and Milliquas is pending due to CDS service outage. We do not claim the full 195,829 are previously unidentified until comprehensive cross-matching is complete."
