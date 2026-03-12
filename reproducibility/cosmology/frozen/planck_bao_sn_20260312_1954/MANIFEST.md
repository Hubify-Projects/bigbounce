# Frozen Artifact Pack: planck_bao_sn

**Dataset:** planck_bao_sn (Planck + BAO + Pantheon SN, no H0/S8 priors)
**Freeze timestamp:** 2026-03-12 19:54 UTC
**Total accepted samples:** 132,949 (6 chains)
**Convergence:** ALL R-hat < 1.002, min ESS = 4,692

## Contents

### chains/
- `chain_01/` through `chain_06/`: MCMC chain files
  - `spin_torsion.1.txt` — chain samples (weight, -logpost, parameters)
  - `spin_torsion.checkpoint` — Cobaya checkpoint
  - `spin_torsion.covmat` — proposal covariance matrix
  - `spin_torsion.progress` — chain progress log
  - `spin_torsion.input.yaml` — original configuration
  - `spin_torsion.updated.yaml` — updated configuration with derived settings

### configs/
- YAML configurations from the chain directory

### diagnostics/
- `convergence_report.txt` — R-hat, ESS, and parameter summary

### SHA256SUMS.txt
- Checksums for all files in this frozen pack

## Sampled Parameters
- logA, nnu (Neff), ns, ombh2, omch2, tau, theta_MC_100
- A_planck, amp_143, amp_217, amp_143x217
- n_143, n_217, n_143x217, calTE, calEE

## Derived Parameters
- H0, sigma8, omegam, S8, age, delta_neff

## Key Results (preliminary, 20% burn-in)
- H0 = 67.79 ± 1.09 km/s/Mpc
- delta_neff = +0.065 (positive shift vs full_tension's -0.020)
- sigma8 = 0.812 ± 0.009
- omegam = 0.312 ± 0.006
- tau = 0.056 ± 0.007

## Comparison with full_tension
- H0: +0.14 (0.1σ shift)
- delta_neff: +0.085 (0.5σ shift, both consistent with SM)
- sigma8: +0.009 (1.1σ shift)

## Convergence Summary
All 9/9 freeze gates pass:
- R-hat: all < 0.002 (targets: H0 < 0.01, dNeff < 0.01, tau < 0.02)
- ESS: all > 4,600 (targets: H0 > 2000, dNeff > 2000, tau > 1000)
- Drift: all < 0.07σ (target < 0.1σ)
