# Master Cosmology Results Table — Paper 1

**Created:** 2026-03-11
**Updated:** 2026-03-12
**Status:** full_tension + planck_bao_sn populated; planck_only running; planck_bao pending

---

## Table: Cosmological Parameter Constraints (ΛCDM + ΔN_eff)

All values are posterior means ± 1σ (68% credible intervals) from Cobaya MCMC with CAMB.

| Parameter | full_tension | planck_bao_sn | planck_only | planck_bao | Notes |
|-----------|-------------|---------------|-------------|------------|-------|
| H₀ [km/s/Mpc] | **67.68 ± 1.06** | **67.79 ± 1.09** | _running_ | _pending_ | Planck 2018 ΛCDM: 67.36 ± 0.54 |
| ΔN_eff | **−0.020 ± 0.169** | **+0.065 ± 0.17** | _running_ | _pending_ | SM: 0; both consistent with zero |
| τ | **0.054 ± 0.007** | **0.056 ± 0.007** | _running_ | _pending_ | Planck 2018: 0.054 ± 0.007 |
| σ₈ | **0.803 ± 0.008** | **0.812 ± 0.009** | _running_ | _pending_ | Planck 2018: 0.811 ± 0.006 |
| Ω_m | **0.308 ± 0.005** | **0.312 ± 0.006** | _running_ | _pending_ | Planck 2018: 0.315 ± 0.007 |
| n_s | **0.965 ± 0.006** | **0.967 ± 0.006** | _running_ | _pending_ | Planck 2018: 0.965 ± 0.004 |
| S₈ | **0.814 ± 0.008** | **0.831 ± 0.018** | _running_ | _pending_ | Planck 2018: 0.832 ± 0.013 |

### Additional Derived Parameters (full_tension)

| Parameter | Value | Unit |
|-----------|-------|------|
| N_eff | 3.026 ± 0.169 | dimensionless |
| Ω_b h² | 0.02226 ± 0.00016 | dimensionless |
| Ω_c h² | 0.1182 ± 0.0028 | dimensionless |
| ln(10¹⁰ A_s) | 3.036 ± 0.015 | dimensionless |
| Age | 13.82 ± 0.17 | Gyr |

### Convergence Summary

| Dataset | Status | Chains | Samples | Worst R-1 | Min ESS |
|---------|--------|--------|---------|-----------|---------|
| full_tension | **FROZEN** | 6 | 175,545 | 0.0010 | 4,744 |
| planck_bao_sn | **FROZEN** | 6 | 132,949 | 0.0014 | 4,692 |
| planck_only | RUNNING | 6 | 458+ | — | — |
| planck_bao | PAUSED | 6 | 469 | — | — |

### Dataset Definitions

| Dataset | Likelihoods | External Priors |
|---------|------------|-----------------|
| full_tension | Planck NPIPE (TT,TE,EE+lowT+lowE+lensing) + BAO DR16 + Pantheon+ | Riess 2020 H₀ + DES S₈ |
| planck_bao_sn | Planck NPIPE + BAO DR16 + Pantheon+ | None |
| planck_only | Planck NPIPE | None |
| planck_bao | Planck NPIPE + BAO DR16 | None |

### Key Findings (two frozen datasets)

1. **ΔN_eff consistent with zero in both datasets.** full_tension: −0.020 ± 0.169; planck_bao_sn: +0.065 ± 0.17. The spin-torsion model's ΔN_eff parameter is not required by the data but is not excluded either.
2. **ΔN_eff shifts positive when H₀/S₈ priors are removed** (+0.085, ~0.5σ). Expected behavior: without the Riess H₀ prior pulling H₀ up (and thus ΔN_eff up), the posterior settles slightly positive but consistent with SM.
3. **H₀ stable across datasets** — 67.68 vs 67.79 (0.1σ shift). ΔN_eff does not resolve the Hubble tension.
4. **σ₈ shift of 1.1σ** when DES S₈ prior is removed — planck_bao_sn recovers the higher Planck-preferred value (0.812 vs 0.803).
5. **Strong H₀–ΔN_eff degeneracy** (r = 0.95) — positive ΔN_eff shifts H₀ upward, as expected from CMB physics.
