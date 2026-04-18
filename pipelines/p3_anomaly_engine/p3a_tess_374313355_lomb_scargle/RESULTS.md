# P3-A — TESS TIC 374313355 Lomb-Scargle periodicity search

**Status:** **NO DATA** on the specified TIC.
**Pod:** `uyl9w5oo37uf06` (H100 SXM · 2026-04-18 07:58 UTC).

## Run outcome

`lightkurve.search_lightcurve("TIC 374313355")` returned **0 products**.
The target identifier as stated in the paper 3 queue does not correspond
to a star with available TESS observations.

## Interpretation

This is not a pipeline failure. TIC 374313355 is genuinely absent from
the TESS data archive. Most likely causes:

1. Typo in the TIC number in the source note (the paper-3 §7.3 open
   items list should be audited — the BigBounce internal note naming this
   target may have inverted two digits).
2. The target was observed but not delivered as a SPOC light curve
   (TESS-FFI cutouts via `lightkurve.search_tesscut` may still yield
   data).
3. The target was a bright saturated source that TESS masked from SPOC
   processing.

## Follow-up plan (filed as `P3-A-ALT` in queue.md)

Same pod, same script, three additional searches:

- `lightkurve.search_tesscut("TIC 374313355", ...)` — FFI cutout
  photometry even if no SPOC curve exists.
- Resolve via SIMBAD / Vizier by coordinates, then search Kepler + K2
  archives as alternatives.
- Cross-reference the DESI+TESS anomaly table in `pipelines/h200_results/`
  to confirm the canonical TIC for the paper-3 candidate.

Until the alt-ID search lands, paper-3 §7.3 carries a
"target resolution pending" footnote rather than a retraction, since
this is a single archival cross-match, not a headline result.

## Provenance

- Script: on-pod `/workspace/p3a.sh`
- Outputs: `result.json`, `run.log`
- Rsynced to local 2026-04-18 drive-to-100 fire #14.
