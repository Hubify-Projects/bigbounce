# P3-A — TESS TIC 374313355 Lomb-Scargle periodicity search

**Status:** complete via FFI-cutout fallback (fire #15 closes both
P3-A and P3-A-ALT).
**Pod:** `uyl9w5oo37uf06` (H100 SXM · 2026-04-18 07:58–08:04 UTC).

## Final result

- **Coordinates:** RA = 160.148889°, Dec = +5.091599° (ICRS),
  Tmag = 18.52 (faint — explains absence from SPOC light-curve
  pipeline, which focuses on brighter stars).
- **Data source:** `lightkurve.search_tesscut("TIC 374313355")` returned
  3 FFI cutouts (TESS sectors 45, 46, 72).
- **Light curve:** N = 3,321 photometric points, built from sector-46
  cutout aperture photometry.
- **Lomb-Scargle peak frequency:** $f = 0.07256$ d⁻¹.
- **Peak period:** $P = 13.782$ days.
- **Peak power:** 0.310.
- **False-alarm probability:** $3.9 \times 10^{-263}$ — the periodicity
  is overwhelmingly significant.

## Interpretation

A 13.8-day periodicity in a faint TESS source is astrophysically
plausible. At Tmag ≈ 18.5 and period in this range, the candidate
most-likely sources are:

1. **Detached eclipsing binary.** TESS's cadence and faint-source
   photometry both reach this regime for EB detection.
2. **Long-rotation-period red-giant variable.** The 13.8-d timescale is
   at the upper tail of rotational modulation but within observed
   ranges.
3. **Long-period Cepheid or RR-Lyrae harmonic.** Less likely given the
   magnitude; needs Gaia DR3 distance + spectral-type cross-check.

A full identification requires:
- SIMBAD / Gaia DR3 cross-match at (160.149°, +5.092°) to type-classify.
- Sector 45 + 72 light curve co-processing to check phase stability
  across 1-yr baselines.
- Radial-velocity follow-up if type remains ambiguous.

Filed as `P3-A-TYPING` (P3) for the above follow-ups. For Paper 3 §7.3
the current result already closes the "periodicity yes/no" question:
**yes, with FAP = 4e-263**.

## Why the original search failed

`lightkurve.search_lightcurve("TIC 374313355")` returned 0 products
because TIC 374313355 at Tmag = 18.5 is below SPOC pipeline processing
thresholds. The SPOC pipeline delivers post-processed light curves only
for stars bright enough for expected-noise exoplanet detection. The
FFI cutout pathway bypasses SPOC and reconstructs photometry directly
from the full-frame image stack, which works for faint targets.

## Provenance

- Script: on-pod `/workspace/p3a_alt.sh`
- Outputs: `alt_search.json`, `alt_search.log`
- Original NO_DATA log: `result.json`, `run.log`
- Pod workspace: `/workspace/bigbounce/pipelines/p3_anomaly_engine/p3a_tess_374313355_lomb_scargle/`
- Rsynced to local 2026-04-18 drive-to-100 fire #15.
