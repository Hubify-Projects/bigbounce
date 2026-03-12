# full_tension Parameter Mapping Audit

**Date:** 2026-03-11 17:55 UTC
**Status:** RESOLVED — all parameters verified against Cobaya config

---

## Critical Bug Found and Fixed

**All previous diagnostic reports (freeze_diagnostics.json, parameter_summary.json, the freeze confirmation, and the interpretation note) contained WRONG parameter values** due to an off-by-one column mapping error.

### Root Cause

The chain file header starts with `#` followed by whitespace:
```
#        weight    minuslogpost    logA    nnu    ns    ...
```

When parsed with `.strip().split()`, the `#` becomes its own token at index 0. The diagnostic scripts did `header[0] = header[0].lstrip("#")` which produced an empty string `""` at index 0, but `numpy.loadtxt()` correctly skips the `#` comment line and reads data columns starting at 0 = weight.

Result: every column index in the analysis was shifted by +1. `col_idx["H0"]` pointed to sigma8, etc.

### Fix

Replace:
```python
header[0] = header[0].lstrip("#")
```
With:
```python
header = tokens[1:] if tokens[0] == '#' else tokens
```

### Impact

| What was reported | Reported value | What it actually was | Correct value |
|-------------------|---------------|---------------------|---------------|
| H0 | 0.803 | sigma8 | **67.68 km/s/Mpc** |
| delta_neff | 13.82 | age (Gyr) | **-0.019** |
| tau | 1.041 | theta_MC_100 | **0.054** |
| ns | 0.022 | ombh2 | **0.965** |
| sigma8 | 0.308 | omegam | **0.803** |
| omegam | 0.814 | S8 | **0.308** |

**The chain data was always correct.** Only the analysis scripts were wrong. The frozen artifact pack chain files are valid.

**Convergence is confirmed** with corrected analysis: all 9/9 freeze gates pass with correct column mapping.

---

## Complete Parameter Mapping Table

### Sampled Parameters (7 cosmological)

| Chain column | Raw name | Physical meaning | Prior | Unit | Correct mean | Correct std | Safe to quote? |
|-------------|----------|-----------------|-------|------|-------------|------------|---------------|
| 2 | logA | log(10^10 A_s) | [1.61, 3.91] | dimensionless | 3.036 | 0.015 | Yes (derived As preferred) |
| 3 | nnu | N_eff | [2.046, 5.046] | dimensionless | 3.027 | 0.169 | Yes |
| 4 | ns | Scalar spectral index | [0.8, 1.2] | dimensionless | 0.965 | 0.006 | Yes |
| 5 | ombh2 | Baryon density Omega_b h^2 | [0.005, 0.1] | dimensionless | 0.02226 | 0.00016 | Yes |
| 6 | omch2 | CDM density Omega_c h^2 | [0.001, 0.99] | dimensionless | 0.1182 | 0.0028 | Yes |
| 7 | tau | Optical depth to reionization | [0.01, 0.8] | dimensionless | 0.054 | 0.007 | Yes |
| 8 | theta_MC_100 | 100 * theta_MC (CosmoMC convention) | [0.5, 10] | dimensionless | 1.04092 | 0.00038 | Yes |

### Derived Parameters

| Chain column | Raw name | Definition | Unit | Correct mean | Correct std | Safe to quote? |
|-------------|----------|-----------|------|-------------|------------|---------------|
| 19 | As | 1e-10 * exp(logA) | dimensionless | ~2.1e-9 | | Yes |
| 20 | H0 | CAMB-derived Hubble constant | km/s/Mpc | 67.68 | 1.06 | **Yes** |
| 21 | sigma8 | RMS matter fluctuations (8 Mpc/h) | dimensionless | 0.803 | 0.008 | **Yes** |
| 22 | omegam | Total matter density parameter | dimensionless | 0.308 | 0.005 | **Yes** |
| 23 | S8 | sigma8 * sqrt(Omega_m / 0.3) | dimensionless | 0.814 | 0.008 | **Yes** |
| 24 | delta_neff | nnu - 3.046 | dimensionless | -0.019 | 0.169 | **Yes** |
| 25 | age | Age of universe | Gyr | 13.82 | 0.17 | Yes |

### Nuisance Parameters (not for paper)

| Chain columns | Names | Purpose |
|--------------|-------|---------|
| 9 | A_planck | Planck calibration |
| 10-15 | amp_143, amp_217, amp_143x217, n_143, n_217, n_143x217 | CamSpec foreground |
| 16-17 | calTE, calEE | TE/EE calibration |
| 18 | Mb | SN absolute magnitude |

### Chi-squared columns (diagnostic only)

| Chain columns | Names |
|--------------|-------|
| 26-45 | chi2__BAO, chi2__CMB, chi2__Mb, chi2__SN, minuslogprior, chi2 (total), per-likelihood chi2 |

---

## Verification Method

1. Read first data row from chain_01
2. Compare each value against expected physical range from the Cobaya config priors/refs
3. Confirmed: weight column 0 contains small integers (1-20), NOT minuslogpost
4. Confirmed: H0 column 20 contains values ~67-74 km/s/Mpc, NOT ~0.8
5. All 15 checked parameters match expected ranges

---

## Key Physics Notes

### delta_neff = -0.019 +/- 0.169

The posterior is **consistent with Delta_Neff = 0** (standard model N_eff = 3.046). This is the full_tension (kitchen sink) result where all probes constrain simultaneously. The constraint is:

- N_eff = 3.027 +/- 0.169 (68% CL)
- Delta_Neff = -0.019 +/- 0.169 (68% CL)
- |Delta_Neff| < 0.35 at 95% CL (approximate)

This is **not** a detection of extra radiation — it's a constraint. The spin-torsion model predicts Delta_Neff > 0, so this result constrains the model's parameter space.

### H0 = 67.68 +/- 1.06 km/s/Mpc

Consistent with Planck LCDM (67.4 +/- 0.5) within 1sigma, but with larger error bars due to the extra N_eff degree of freedom. Lower than SH0ES (73.0 +/- 1.0), showing the Hubble tension is not resolved by Delta_Neff alone in this model.

### S8 = 0.814 +/- 0.008

This is slightly high compared to DES Y3 (0.776 +/- 0.017), but the S8_DES likelihood is included as a prior in this run, so the S8 constraint is a compromise.

---

## Answer

**Are the frozen full_tension parameter values now safe to use in the paper?**

**YES** — with the corrected column mapping, all parameters are in standard physical units and can be quoted directly. Use the CORRECTED values from `freeze_diagnostics_CORRECTED.json` and `parameter_summary_CORRECTED.json`, NOT the original (buggy) files.

**What needs correcting?**
- Replace all `_CORRECTED` files as the canonical versions in the frozen pack
- The old (buggy) `freeze_diagnostics.json`, `parameter_summary.json` and plot files should be marked as SUPERSEDED
- The freeze confirmation report needs updating with correct values
- The interpretation note's parameter concerns are now resolved

---

## Files

| File | Status |
|------|--------|
| `freeze_diagnostics_CORRECTED.json` | CANONICAL — use this |
| `parameter_summary_CORRECTED.json` | CANONICAL — use this |
| `full_tension_triangle_CORRECTED.png/pdf` | CANONICAL — use this |
| `full_tension_posteriors_CORRECTED.png/pdf` | CANONICAL — use this |
| `full_tension_chain_comparison_CORRECTED.png` | CANONICAL — use this |
| `freeze_diagnostics.json` | SUPERSEDED — off-by-one bug |
| `parameter_summary.json` | SUPERSEDED — off-by-one bug |
| `full_tension_triangle.png/pdf` | SUPERSEDED — wrong labels |
| `full_tension_posteriors.png/pdf` | SUPERSEDED — wrong values |
