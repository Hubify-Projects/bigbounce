# F1.3 Injection/Recovery Report

**Date:** 2026-03-22
**Level:** INJECTION_VALIDATED
**Status:** ALL TESTS PASS

---

## What Was Done

Built and ran a bispectrum injection/recovery test that validates the template-recast methodology used in F1.1 to project Planck's local-template f_NL constraint onto the matter-bounce template.

The test generates 2D Gaussian random fields, injects non-Gaussianity with known shape (local or bounce), measures the bispectrum, and fits it with both local and bounce template estimators.  The key quantity is the **amplitude ratio** r = (local estimator on bounce signal) / (local estimator on local signal), which should match the analytically predicted template overlap.

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Grid | 128 x 128 |
| Realizations | 200 per test |
| f_NL injected | -4.375 (= -35/8) |
| A_s | 0.1 (boosted for high S/N) |
| k-bins | 10 (logarithmic) |
| Bounce polynomial | C = (2, 7, 3, -12, -69, 19) |
| Seed | 20260322 |
| Runtime | 4.4 seconds |

The boosted amplitude A_s = 0.1 (vs realistic ~10^-9) ensures high signal-to-noise per realization.  This does NOT affect the overlap ratio r, which is a geometric property of the shape functions.  The test validates the ratio, not absolute calibration.

## Shape Function Verification

| Configuration | BNL | Ratio to local |
|--------------|-----|----------------|
| Squeezed (0.001, 1, 1) | -4.3741 | 0.9998 |
| Equilateral (1, 1, 1) | -3.9844 | 0.9107 |
| Folded (1, 0.5, 0.5) | -2.2500 | 0.5143 |

All match the verified Cai polynomial values.

## Results

### Test A: Local injection (calibration baseline)

| Metric | Value |
|--------|-------|
| Injection | f_NL = -4.375, local shape |
| Recovered (raw) | -149,888,045 +/- 1,300,266 |
| Sign | Correct (negative) |
| Detection significance | 115.3 sigma |
| Verdict | **PASS** |

The absolute value has a large FFT normalization factor (~3.4 x 10^7), which is expected and cancels in the ratio test.

### Test B: Bounce injection (KEY ratio test)

| Metric | Value |
|--------|-------|
| Injection | f_NL = -4.375, bounce shape |
| Local estimator | -134,872,764 +/- 1,290,357 |
| Bounce estimator | -152,342,098 +/- 1,471,497 |
| **r_measured** | **0.900 +/- 0.012** |
| r_predicted (CMB Fisher) | 0.876 +/- 0.02 |
| r_predicted (generic) | 0.84 +/- 0.02 |
| Tension | 1.0 sigma |
| In range [0.80, 0.95] | Yes |
| Verdict | **PASS** |

The bounce estimator recovers 13% more amplitude than the local estimator when applied to a bounce signal (|bounce_est|/|local_est| = 1.13), confirming it is a better-matched template.

### Test C: Null injection

| Metric | Value |
|--------|-------|
| Injection | f_NL = 0 |
| Recovered (local) | -74,328 +/- 35,283 |
| Tension with zero | 2.1 sigma |
| Null / signal fraction | 0.05% |
| Verdict | **PASS** |

## Summary of All Sub-Tests

| Test | Description | Result |
|------|-------------|--------|
| A_local_detection | Signal detected with correct sign | PASS |
| B_ratio_recovery | r = 0.900 consistent with 0.876 | PASS |
| B_bounce_better_matched | Bounce estimator > local on bounce signal | PASS |
| C_null_consistent | Null injection consistent with zero | PASS |
| C_null_small | Null << signal | PASS |

## Key Finding

**r_measured = 0.900 +/- 0.012 is consistent with r_predicted = 0.876 +/- 0.02 at 1.0 sigma.**

The slight upward bias (0.900 vs 0.876) is expected from the coarse k-binning (10 bins) used in the bounce injection, which smooths the BNL variation within bins.  The binned injection slightly over-weights squeezed configurations (where BNL ratio ~ 1) relative to the analytic integral.  This systematic is well within the measurement uncertainty.

## What This Validates

1. **The template-recast formula works.**  When a local-template estimator is applied to a bounce-shaped bispectrum, it recovers r times the true amplitude, where r is the shape overlap factor.

2. **The F1.1 recast is now INJECTION_VALIDATED.**  The Planck constraint recast:
   - f_NL^bounce = f_NL^local / r = -0.9 / 0.876 = -1.0 +/- 5.8
   - was TRIAGE_RECAST (based on published numbers only)
   - is now INJECTION_VALIDATED (methodology confirmed by simulation)

3. **The bounce estimator is better matched** (as expected).  It recovers ~13% more signal when the true shape is the bounce template.

## What This Does NOT Validate

- Absolute f_NL calibration (only the ratio)
- Full CMB pipeline (beam, noise, masking, lensing)
- 3D spherical harmonic analysis (this is a 2D flat-sky test)
- Map-level data products

## Caveats

1. 2D grid (not 3D CMB spherical harmonics) — validates methodology, not full pipeline
2. Boosted A_s for high S/N — does NOT affect the ratio r
3. Bounce injection uses binned BNL approximation (10 k-bins, angle-averaged)
4. Absolute f_NL calibration has FFT-convention offset; only the RATIO is tested
5. No beam, noise, or mask effects

## Next Gating Step

- F1.4: Robustness suite (vary grid size, k-bins, A_s, realizations)
- F1.5: Null / false-positive controls (wrong template injections, biased estimators)

## Files

- Script: `scripts/f1_injection_recovery.py`
- Output: `outputs/F1_injection_recovery.json`
- Prerequisite: `outputs/F1_baseline_recast.json` (F1.1)
