# F1 Baseline Reproduction Report

**Date:** 2026-03-23
**Level:** TRIAGE_RECAST
**Status:** BASELINE DOCUMENTED (not yet map-level reproduced)

---

## What Was Done

Reproduced the Planck 2018 local f_NL constraint from published values and applied the template-overlap correction to obtain the bounce-template constraint.

## Published Baseline

| Estimator | Data | f_NL^local | σ | Source |
|-----------|------|-----------|---|--------|
| KSW | T+E | -0.9 | 5.1 | Planck 2018 IX, Table 4 |
| Binned | T+E | -0.9 | 5.0 | Planck 2018 IX, Table 4 |
| Modal | T+E | -1.0 | 5.1 | Planck 2018 IX, Table 4 |
| KSW | T-only | -0.6 | 5.7 | Planck 2018 IX, Table 4 |

Estimator spread: Δf_NL = 0.1, Δσ = 0.1. Excellent consistency.

## Bounce-Template Recast

Using r = 0.876 ± 0.02 (CMB Fisher weight):

| Constraint | f_NL^bounce | σ^bounce | vs prediction | vs zero |
|-----------|-------------|---------|---------------|---------|
| Planck alone | -1.0 | 5.8 | 0.6σ | 0.2σ |
| Planck + DESI combined | -1.3 | 4.5 | 0.7σ | 0.3σ |

## Assessment

- Current data are consistent with BOTH the bounce prediction (-4.375) AND zero.
- No discrimination is possible at this stage.
- The combined σ = 4.5 on the bounce template means the canonical prediction is less than 1σ away.

## What This Is

- A TRIAGE_RECAST: published numbers recast through our template overlap factor.
- Fully reproducible from the script `f1_baseline_recast.py`.
- No map-level data products were used.
- No new information was extracted beyond what's in the Planck 2018 publication.

## What This Is NOT

- Not a map-level bispectrum estimation.
- Not a bounce-template-specific extraction.
- Not validated by injection/recovery.
- Not evidence for or against the bounce.

## Caveats

1. DESI values are approximate (not from official publication).
2. Independence of Planck bispectrum and DESI SDB assumed but not verified.
3. Template overlap r is from simplified shape inner product, not actual estimator pipeline.
4. This is a Level 0 result. Upgrade requires simulation-based validation.

## Next Gating Step

F1.2: Implement bounce-template layer and verify template-equivalence algebra.
F1.3: Build injection/recovery test suite using FFP10 simulations.

## Files

- Script: `scripts/f1_baseline_recast.py`
- Output: `outputs/F1_baseline_recast.json`
