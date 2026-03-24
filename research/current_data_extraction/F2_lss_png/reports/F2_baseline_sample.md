# F2 Baseline Sample Design

**Date:** 2026-03-23
**Status:** DESIGN COMPLETE, DATA NOT YET ACQUIRED

---

## Baseline Tracer Sample

### Primary: DESI DR1 QSO Catalog

The highest-bias tracers available in current public data are quasars (QSOs) from DESI DR1.

| Property | Value | Source |
|----------|-------|--------|
| Survey | DESI DR1 spectroscopic | DESI public release |
| Tracer type | QSO (quasars) | DESI target selection |
| Approximate count | ~1.6 million | DESI DR1 statistics |
| Redshift range | 0.8 < z < 3.5 | QSO target selection |
| Sky coverage | ~14,000 deg² | DESI footprint |
| Linear bias | b ~ 2-4 (redshift dependent) | Literature estimates |
| PNG bias (b_φ) | b_φ ~ 2(b-1)δ_c ≈ 3-10 | Universality relation |

**Why QSOs for PNG:** Scale-dependent bias from local f_NL is proportional to b_φ × f_NL / k². High-bias tracers amplify the signal. QSOs are the highest-bias spectroscopic tracers currently available.

### Baseline PNG constraint

From DESI DR1 QSO SDB (approximate):
- f_NL^local = -3.6 ± 9.2 (single-tracer, QSO only)

From DESI DR1 P+B combination:
- f_NL^local = -0.1 ± 7.4

### Baseline Fisher sensitivity estimate

For a single tracer with number density n̄, bias b, and survey volume V:

σ(f_NL) ≈ 1 / [b_φ × (n̄V)^{1/2} × (some k-range factor)]

The k-range factor depends heavily on k_min (the minimum accessible wavenumber), which is limited by the survey footprint and systematic control.

---

## Enhanced Sample Strategies (F2.2)

### Strategy A: Purity-Optimized QSO Selection

Goal: Remove low-quality QSOs (spectroscopic failures, low-confidence redshifts, stellar contamination) to get a cleaner, higher-effective-bias sample.

Features for classification:
- DESI quality flags (ZWARN, DELTACHI2, etc.)
- Legacy Surveys photometry (g, r, z, W1, W2)
- Morphology indicators (PSF vs extended)
- Galactic extinction (E(B-V))

ML approach: XGBoost/LightGBM classifier trained on spectroscopic quality metrics, evaluated on spatial holdouts.

### Strategy B: High-z Enrichment via Photo-z

Goal: Extend effective QSO sample to higher redshifts where bias is larger.

Method: Use Legacy Surveys + unWISE photometry to identify high-z QSO candidates beyond DESI spectroscopic limits.

Risk: Photo-z contamination could introduce systematic biases that mimic or suppress PNG signal.

### Strategy C: Variability-Enhanced QSO Identification (P5 feed)

Goal: Use unTimely IR variability to identify additional QSOs missed by spectroscopic targeting.

Method: Cross-match DESI footprint with unTimely 32-epoch catalog, engineer variability features, train QSO classifier.

Risk: Variability selection could introduce selection biases correlated with sky position.

---

## Validation Requirements (F2.3-F2.5)

### Selection Function Audit (mandatory)

For every enhanced sample, test correlation with:
- Survey depth maps (Legacy Surveys randoms)
- PSF FWHM / seeing maps
- Galactic dust (E(B-V) from SFD)
- Stellar density (Gaia source counts)
- Survey region boundaries

If any correlation exceeds a predefined threshold, the enhancement is not trustworthy.

### Spatial Holdout Validation (mandatory)

Split by:
- North Galactic Cap vs South Galactic Cap
- High/low extinction regions
- High/low stellar density regions
- Individual DESI rosettes or tiles

Enhancement must be consistent across holdouts.

### Mock Injection/Recovery (mandatory before combination)

Use lognormal or EZmocks with known f_NL injection:
- Baseline sample recovery
- Enhanced sample recovery
- Bias and uncertainty comparison

---

## Data Acquisition Plan

| Dataset | Source | Size | Download method | Status |
|---------|--------|------|----------------|--------|
| DESI DR1 spectroscopic catalog | data.desi.lbl.gov | ~5 GB | wget / API | NOT YET |
| Legacy Surveys DR10 photometry | legacysurvey.org | ~100 GB (full) / ~5 GB (matched) | SQL query + API | NOT YET |
| unWISE catalog | unwise.me | ~50 GB (full) / ~2 GB (matched) | wget | NOT YET |
| unTimely (32 epochs) | unwise.me/unTimely | ~100 GB | wget | NOT YET |
| DESI randoms (for selection function) | data.desi.lbl.gov | ~2 GB | wget | NOT YET |
| Galactic maps (dust, stars) | Various | ~500 MB | wget | NOT YET |

### RunPod Requirements

| Task | Pod | Est. time | Est. cost |
|------|-----|-----------|-----------|
| Download + cross-match | 32-core CPU, 200GB disk | 4-6 hours | ~$5 |
| ML training (XGBoost) | Same pod | 1-2 hours | included |
| Mock generation | Same pod | 2-4 hours | included |

---

## Success Criteria

### Minimum viable
- Baseline sample documented with sky coverage, n(z), and contamination estimate
- Baseline PNG sensitivity reproduced from published Fisher estimate

### Good
- At least one enhanced sample passes the selection-function audit
- Mock injection shows improved recovery

### Excellent
- Enhanced sample gives σ(f_NL) < baseline by >10%
- Passes all spatial holdouts
- Mock injection shows unbiased recovery with reduced uncertainty

---

## Gating

- F2.1 is COMPLETE when baseline sample is documented and baseline PNG sensitivity is reproduced.
- F2.2 starts ONLY after F2.1 passes.
- F2.7 (combination) starts ONLY after F2.3-F2.5 pass.
