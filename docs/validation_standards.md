# Validation Standards for Current-Data Extraction Pipelines

**Applies to:** F1 (bispectrum), F2 (LSS/PNG), F3 (CMB residuals/EB)
**Version:** 1.0
**Date:** 2026-03-23

---

## Result Taxonomy

Every pipeline output must be tagged with exactly one of these levels:

| Level | Label | Meaning |
|-------|-------|---------|
| 0 | `TRIAGE_RECAST` | Fast approximate recast of published numbers. No new data products used. Useful for scoping only. |
| 1 | `BASELINE_REPRODUCED` | A known published result has been reproduced within documented tolerance using the same data products. |
| 2 | `INJECTION_VALIDATED` | Synthetic signal injections are recovered within bias and calibration tolerances. |
| 3 | `ROBUSTNESS_PARTIAL` | Some but not all robustness checks passed. Failures documented. |
| 4 | `ROBUSTNESS_PASSED` | All mandatory robustness checks passed (masks, frequencies, holdouts, nulls). |
| 5 | `PUBLICATION_READY_CANDIDATE` | All of the above plus nuisance audit, false-positive controls, and uncertainty calibration. |

Nothing should be described as "publication-ready" or used in paper claims unless it reaches Level 5. Levels 0-2 are internal working results only.

---

## Mandatory Sections for Every Pipeline

### 1. Benchmark Reproduction
- Reproduce a known published result before attempting anything new.
- Document: published value, our value, tolerance, data products used.
- If reproduction fails, STOP. Write failure report. Do not proceed.

### 2. Injection / Recovery
- Inject known signals (null, local template, bounce template, convention variants).
- Recover amplitude, measure bias, measure uncertainty calibration.
- This is the analog of synthetic spiral injection in chirality.

### 3. Null Tests
- Run pipeline on null simulations / Gaussian mocks.
- Verify zero recovery (no false positive signal).
- Document any non-zero bias and its source.

### 4. Holdout Robustness
- Split by: sky region, mask variant, frequency, map product choice, redshift bin.
- Result must not depend on a single favorable choice.

### 5. Calibration / Uncertainty
- Verify that reported uncertainties are calibrated.
- Use injection ensembles to check coverage.
- Report any under- or over-coverage.

### 6. Leakage / Nuisance Audit
- Test whether results correlate with known nuisance fields (dust, seeing, depth, stellar density).
- Compare against metadata-only baselines where applicable.

### 7. Final Claim Language
- Acceptable: "current data remain broadly consistent with the bounce prediction"
- Acceptable: "matched-template extraction is modestly more informative than generic local recast"
- Acceptable: "no meaningful improvement over generic local recast"
- NOT acceptable: "current data confirm the bounce" (unless Level 5 with >3σ)

---

## Combination Rules

- Do not assume dataset independence without documentation.
- If combining CMB + LSS, document overlap (lensing, ISW, etc.).
- If combining Planck + ACT, document frequency overlap and calibration correlation.
- Covariance assumptions must be explicit in every combination.

---

## Model / ML Standards (F2 specific)

- Always compare against simple non-ML baselines (e.g., color cuts, magnitude thresholds).
- Use spatial/healpix split validation, never random split alone.
- Write a `model_card.md` for every trained model.
- Write a `bias_audit.md` for every model-selected catalog.
- Optimize for cosmology utility (effective bias × number density × purity), not classification accuracy alone.

---

## File Standards

- Every pipeline must output:
  - `outputs/*_metrics.json` — quantitative results
  - `outputs/*_plots/` — figures
  - `reports/*_report.md` — narrative audit
  - `manifests/*_manifest.json` — exact file list with hashes
  - `audits/*_audit.json` — structured pass/fail for each validation step

- Scripts must fail loudly on: missing files, wrong shapes, NaN values, suspicious covariance.
- All intermediate outputs must be saved (no silent overwrite without checkpointing).
