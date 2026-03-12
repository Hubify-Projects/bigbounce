# Master Cosmology Results Table — Paper 1

**Created:** 2026-03-11
**Status:** full_tension populated; remaining datasets pending freeze

---

## Table: Cosmological Parameter Constraints (ΛCDM + ΔN_eff)

All values are posterior means ± 1σ (68% credible intervals) from Cobaya MCMC with CAMB.

| Parameter | full_tension | planck_bao_sn | planck_only | planck_bao | Notes |
|-----------|-------------|---------------|-------------|------------|-------|
| H₀ [km/s/Mpc] | **67.68 ± 1.06** | _pending_ | _pending_ | _pending_ | Planck 2018 ΛCDM: 67.36 ± 0.54 |
| ΔN_eff | **−0.020 ± 0.169** | _pending_ | _pending_ | _pending_ | SM: 0; consistent with zero |
| τ | **0.054 ± 0.007** | _pending_ | _pending_ | _pending_ | Planck 2018: 0.054 ± 0.007 |
| σ₈ | **0.803 ± 0.008** | _pending_ | _pending_ | _pending_ | Planck 2018: 0.811 ± 0.006 |
| Ω_m | **0.308 ± 0.005** | _pending_ | _pending_ | _pending_ | Planck 2018: 0.315 ± 0.007 |
| n_s | **0.965 ± 0.006** | _pending_ | _pending_ | _pending_ | Planck 2018: 0.965 ± 0.004 |
| S₈ | **0.814 ± 0.008** | _pending_ | _pending_ | _pending_ | Planck 2018: 0.832 ± 0.013 |

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
| planck_bao_sn | RUNNING | 6 | ~12,000 | 0.0064 | 420 |
| planck_only | PAUSED | — | — | — | — |
| planck_bao | PAUSED | — | — | — | — |

### Dataset Definitions

| Dataset | Likelihoods | External Priors |
|---------|------------|-----------------|
| full_tension | Planck NPIPE (TT,TE,EE+lowT+lowE+lensing) + BAO DR16 + Pantheon+ | Riess 2020 H₀ + DES S₈ |
| planck_bao_sn | Planck NPIPE + BAO DR16 + Pantheon+ | None |
| planck_only | Planck NPIPE | None |
| planck_bao | Planck NPIPE + BAO DR16 | None |

### Key Findings (full_tension only)

1. **ΔN_eff = −0.020 ± 0.169** — consistent with zero (Standard Model). The spin-torsion model's ΔN_eff parameter is not required by the data but is not excluded either.
2. **H₀ = 67.68 ± 1.06** — consistent with Planck ΛCDM. ΔN_eff does not resolve the Hubble tension.
3. **S₈ = 0.814 ± 0.008** — intermediate between Planck (0.832) and DES Y3 (0.776), reflecting the compromise from including both datasets.
4. **Strong H₀–ΔN_eff degeneracy** (r = 0.95) — positive ΔN_eff shifts H₀ upward, as expected from CMB physics.
