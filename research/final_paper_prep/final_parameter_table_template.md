# Final Parameter Table Template — Paper 1

**Created:** 2026-03-11
**Status:** full_tension filled; others pending freeze

---

## Table: MCMC Cosmological Parameter Constraints (ΛCDM + ΔN_eff)

| Parameter | full_tension | planck_bao_sn | planck_only | planck_bao | ΛCDM Reference |
|-----------|-------------|---------------|-------------|------------|----------------|
| **H₀** [km/s/Mpc] | 67.68 ± 1.06 | _pending_ | _pending_ | _pending_ | 67.36 ± 0.54 |
| **ΔN_eff** | −0.020 ± 0.169 | _pending_ | _pending_ | _pending_ | 0 (SM) |
| **N_eff** | 3.026 ± 0.169 | _pending_ | _pending_ | _pending_ | 3.046 (SM) |
| **τ** | 0.054 ± 0.007 | _pending_ | _pending_ | _pending_ | 0.054 ± 0.007 |
| **σ₈** | 0.803 ± 0.008 | _pending_ | _pending_ | _pending_ | 0.811 ± 0.006 |
| **Ω_m** | 0.308 ± 0.005 | _pending_ | _pending_ | _pending_ | 0.315 ± 0.007 |
| **n_s** | 0.965 ± 0.006 | _pending_ | _pending_ | _pending_ | 0.965 ± 0.004 |
| **S₈** | 0.814 ± 0.008 | _pending_ | _pending_ | _pending_ | 0.832 ± 0.013 |
| **Age** [Gyr] | 13.82 ± 0.17 | _pending_ | _pending_ | _pending_ | 13.80 ± 0.02 |
| **Convergence** | FROZEN (9/9) | RUNNING | PAUSED | PAUSED | — |
| **Chains** | 6 | 6 | — | — | — |
| **Samples** | 175,545 | ~3,500 | — | — | — |
| **Notes** | Anchor result | No H₀/S₈ priors | CMB only | CMB + BAO | Planck 2018 |

## Dataset Specifications

| Dataset | Likelihoods | External Priors | Role |
|---------|------------|-----------------|------|
| full_tension | Planck NPIPE + BAO DR16 + Pantheon+ | Riess 2020 H₀ + DES S₈ | Anchor (max constraining power) |
| planck_bao_sn | Planck NPIPE + BAO DR16 + Pantheon+ | None | Tension-free comparison |
| planck_only | Planck NPIPE | None | Pure CMB constraint |
| planck_bao | Planck NPIPE + BAO DR16 | None | Intermediate |
| ΛCDM Reference | — | — | Planck 2018 Table 2 (TT,TE,EE+lowE+lensing) |

## Formatting Notes for Paper

- Report means ± 1σ (68% CL) throughout
- Round to: H₀ (2 decimal), ΔN_eff (3 decimal), τ (3 decimal), σ₈ (3 decimal), Ω_m (3 decimal), n_s (3 decimal), S₈ (3 decimal), Age (2 decimal)
- Include convergence status row to indicate reliability
- Bold the full_tension column as the primary result
- Note in caption: "All values are posterior means with 68% credible intervals from Cobaya MCMC sampling with CAMB."
