# F1 — Bounce-Specific Bispectrum / f_NL Current-Data Extraction

## Scientific Question

Is current CMB data already more informative about the canonical matter-bounce f_NL signal than generic local-template summaries suggest?

## Canonical Target

f_NL = -35/8 = -4.375 (Planck convention, 92% confidence)

## Pipeline Stages

| Stage | Description | Gating |
|-------|-------------|--------|
| F1.1 | Baseline local f_NL reproduction | Must pass before anything else |
| F1.2 | Bounce-template handling | Requires F1.1 |
| F1.3 | Injection / recovery | Requires F1.2 |
| F1.4 | Robustness suite | Requires F1.3 |
| F1.5 | Null / false-positive controls | Requires F1.3 |
| F1.6 | Final output | Requires F1.4 + F1.5 |

## Current Status

| Stage | Status | Level |
|-------|--------|-------|
| F1.1 | IN PROGRESS | — |
| F1.2-F1.6 | Not started | — |

## Data Products Required

### For F1.1 (baseline reproduction)

The most accessible path to reproducing a Planck-era local f_NL constraint is NOT to re-run the full Planck bispectrum pipeline (which requires internal ESA code). Instead:

**Path A (recommended): Fisher-matrix recast**
- Input: Planck 2018 published constraint f_NL^local = -0.9 ± 5.1 (temperature + polarization)
- Method: Recast onto bounce template using the verified shape overlap r = 0.84 ± 0.02
- Validation: Reproduce the published local-template number first, then apply projection
- Advantage: No map-level products needed; fully reproducible from published numbers
- Limitation: TRIAGE_RECAST level until validated by injection/recovery on simulations

**Path B (stretch): Map-level estimator**
- Input: Planck PR3 SMICA/NILC/SEVEM component-separated maps + confidence masks + beam files
- Method: Build or adapt a KSW-like bispectrum estimator
- Validation: Reproduce published f_NL^local from maps
- Advantage: Could genuinely extract more information with bounce-matched template
- Limitation: Much harder; Planck bispectrum estimator code is not public
- Alternative: Use PolyBin (Philcox) or similar public binned bispectrum code if available

**Decision: Start with Path A to establish the recast baseline, then attempt Path B if public estimator code is found.**

### For F1.3+ (injection/recovery)

- FFP10 / FFP8 Planck simulation suite (public on PLA)
- Gaussian CMB simulations with known f_NL injected
- Need: healpy for map manipulation, NaMaster or equivalent for power spectra
