# Track C Method Audit

**Date:** 2026-03-13
**Auditor:** Claude (automated audit)
**Program:** Extension Program — Track C (Parity/CMB Birefringence)

---

## 1. Scripts Inventory

| Script | Lines | Runtime | Dependencies |
|--------|-------|---------|--------------|
| `consistency_window.py` | ~120 | <1 sec | numpy, matplotlib |
| `gaussian_posterior.py` | ~180 | <1 sec | numpy, scipy.stats, matplotlib |
| `eb_shape_comparison.py` | ~200 | <1 sec | numpy, matplotlib |

**Total runtime: <3 seconds on any machine.**

---

## 2. Script-by-Script Method Description

### 2a. `consistency_window.py`

**What it does:** Pure algebraic parameter translation.

**Core computation:**
```
EPSILON = (ALPHA_OVER_M * M_PL_GEV)  # ≈ 2.435e-3 (dimensionless)
C_0 = 2.725 (rad/deg conversion absorbed)
f_photon = beta_rad / (EPSILON * C_0)
```

**Input parameters:**
- `ALPHA_OVER_M = 1.0e-21` GeV⁻¹ (from paper's one-loop scaling ansatz)
- `M_PL_GEV = 2.435e18` GeV (reduced Planck mass)
- Published β measurements: Eskilt 2022 (0.30° ± 0.11°), ACT DR6 (0.215° ± 0.074°)

**Method:** Division. No sampling, no optimization, no fitting. Converts observed β to the f_photon value required for consistency with the framework's α/M.

**Priors:** None. No Bayesian inference is performed.

**Sampler:** None.

**Output:** A plot showing f_photon vs β with observational bands overlaid.

---

### 2b. `gaussian_posterior.py`

**What it does:** Textbook inverse-variance weighted average of two published Gaussian measurements.

**Core computation:**
```
# Inverse-variance weighted average (textbook formula)
weights = 1.0 / sigmas**2
beta_combined = np.sum(betas * weights) / np.sum(weights)
sigma_combined = 1.0 / np.sqrt(np.sum(weights))

# Parameter translation
f_photon = beta_combined_rad / (EPSILON * C_0)
sigma_f = sigma_combined_rad / (EPSILON * C_0)
```

**Input data (2 measurements):**
| Source | β (deg) | σ_β (deg) | Origin |
|--------|---------|-----------|--------|
| Eskilt 2022 (Planck) | 0.300 | 0.110 | arXiv: 2205.13962 |
| Diego-Palazuelos & Komatsu 2025 (ACT DR6) | 0.215 | 0.074 | arXiv: 2509.13654 |

**Excluded data:**
- Minami & Komatsu 2020: superseded by Eskilt 2022 (same dataset, improved analysis)
- SPIDER 2025: calibration degeneracy between β and instrument angle

**Method:** `scipy.stats.norm` is used ONLY for plotting Gaussian curves — not for sampling or inference. The weighted average is computed by direct formula.

**Priors:** None.

**Sampler:** None. Zero MCMC iterations. Zero sampling of any kind.

**Output:** Gaussian curves for individual and combined β, mapped g_eff and f_photon distributions.

---

### 2c. `eb_shape_comparison.py`

**What it does:** Forward model computation of the predicted EB cross-spectrum.

**Core computation:**
```
C_ell_EB = 0.5 * np.sin(2 * beta_rad) * (C_ell_EE - C_ell_BB)
```

**Input:**
- `beta = 0.2415°` (from the weighted average above)
- EE and BB spectra: analytic approximations (NOT CAMB-computed; CAMB not available locally)

**Method:** Applies the standard isotropic birefringence formula. Computes a ratio diagnostic: C_ℓ^{EB}/(C_ℓ^{EE} - C_ℓ^{BB}) should be ℓ-independent for uniform birefringence.

**Priors:** None.

**Sampler:** None.

**Output:** Forward-model EB spectrum and isotropy diagnostic plot.

---

## 3. What Is NOT Done

| Method | Present? |
|--------|----------|
| MCMC sampling | NO |
| Nested sampling | NO |
| Maximum likelihood estimation | NO |
| χ² minimization | NO |
| Profile likelihood | NO |
| Grid scan over parameter space | NO |
| Bayesian model comparison | NO |
| Any optimization algorithm | NO |
| Any sampling algorithm | NO |

---

## 4. Audit Verdict

**Track C performs zero statistical inference.** Every computation is either:
1. Algebraic parameter translation (division by known constants)
2. Textbook weighted averaging of published results
3. Forward model evaluation at a fixed parameter value

The <3 second total runtime is scientifically legitimate because no iterative computation is required. The methods are correct for what they claim to do.
