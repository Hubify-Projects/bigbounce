# GPU Run Snapshot — 20260305_0824

## Hardware
- **Pod**: RunPod RTX 6000 Ada (48GB VRAM)
- **CPU**: 128 cores
- **RAM**: 503Gi
- **Pod ID**: 47htajss1ng2ig
- **Cost**: ~$0.74/hr

## Software
- Cobaya 3.6.1
- CAMB 1.6.5
- GetDist 1.7.5
- Python 3.11.10

## Dataset Combinations
| Dataset | Chains | Description |
|---------|--------|-------------|
| planck_only | 7 (1 original + 6 parallel) | Planck TTTEEE+lowl+lowE+lensing |
| planck_bao | 7 (1 original + 6 parallel) | + BAO (6dFGS, SDSS DR7, SDSS DR16) |
| planck_bao_sn | 7 (1 original + 6 parallel) | + Pantheon+ SN Ia |
| full_tension | 7 (1 original + 6 parallel) | + SH0ES H₀ + DES Y3 S₈ priors |

## Chain Count Summary
- **4** dataset combinations
- **7** chains per dataset (1 original + 6 parallel)
- **28** total chains
- **31** Cobaya processes (28 python + 3 bash wrappers)

## Timeline
- Original chains started: ~2026-03-04 08:47 UTC
- Parallel chains started: ~2026-03-04 18:30 UTC
- Snapshot taken: Thu Mar  5 08:25:54 UTC 2026
- Run duration: ~24h

## Git
- Commit: de652f8f32928472ef5816ab7ded6e8f048c8d4f
- Branch: main

## Convergence Status at Snapshot
BigBounce MCMC Freeze Check — 2026-03-05 08:24:53 UTC
Targets: Rhat_m1 < 0.01 (H0..sigma8), < 0.02 (tau), Drift < 0.2σ
====================================================================================================

--- PLANCK ONLY ---
  [all_chains]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=0.8546, delta_neff=0.6845, sigma8=0.5854
    Drift20/40 < 0.2σ: FAIL  (H0=-0.5368σ [FAIL], delta_neff=-0.7434σ [FAIL])
    ESS(H0) = 48.1   ESS(ΔNeff) = 45.8
    >> all_chains OVERALL: FAIL
  [cohort_new]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=0.8546, delta_neff=0.6845, sigma8=0.5854
    Drift20/40 < 0.2σ: FAIL  (H0=-0.5368σ [FAIL], delta_neff=-0.7434σ [FAIL])
    ESS(H0) = 48.1   ESS(ΔNeff) = 45.8
    >> cohort_new OVERALL: FAIL

--- PLANCK BAO ---
  [all_chains]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=1.5840, delta_neff=0.8474, sigma8=0.5566
    Drift20/40 < 0.2σ: PASS  (H0=-0.1193σ [PASS], delta_neff=-0.1190σ [PASS])
    ESS(H0) = 51.9   ESS(ΔNeff) = 40.0
    >> all_chains OVERALL: FAIL
  [cohort_new]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=1.5840, delta_neff=0.8474, sigma8=0.5566
    Drift20/40 < 0.2σ: PASS  (H0=-0.1193σ [PASS], delta_neff=-0.1190σ [PASS])
    ESS(H0) = 51.9   ESS(ΔNeff) = 40.0
    >> cohort_new OVERALL: FAIL

--- PLANCK BAO SN ---
  [all_chains]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=0.8326, delta_neff=0.6807, sigma8=0.5558
    Drift20/40 < 0.2σ: FAIL  (H0=-0.3095σ [FAIL], delta_neff=-0.4233σ [FAIL])
    ESS(H0) = 94.2   ESS(ΔNeff) = 55.4
    >> all_chains OVERALL: FAIL
  [cohort_new]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=0.8326, delta_neff=0.6807, sigma8=0.5558
    Drift20/40 < 0.2σ: FAIL  (H0=-0.3095σ [FAIL], delta_neff=-0.4233σ [FAIL])
    ESS(H0) = 94.2   ESS(ΔNeff) = 55.4
    >> cohort_new OVERALL: FAIL

--- FULL TENSION ---
  [all_chains]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=0.9165, sigma8=0.5695, ns=0.3718
    Drift20/40 < 0.2σ: PASS  (H0=-0.0539σ [PASS], delta_neff=-0.1068σ [PASS])
    ESS(H0) = 61.7   ESS(ΔNeff) = 41.7
    >> all_chains OVERALL: FAIL
  [cohort_new]
    Rhat_m1 < 0.01 (core) + < 0.02 (tau): FAIL
    Bottlenecks: tau=0.9165, sigma8=0.5695, ns=0.3718
    Drift20/40 < 0.2σ: PASS  (H0=-0.0539σ [PASS], delta_neff=-0.1068σ [PASS])
    ESS(H0) = 61.7   ESS(ΔNeff) = 41.7
    >> cohort_new OVERALL: FAIL

## Config Differences
Original vs parallel chains have 2 non-blocking MCMC tuning diffs:
- burn_in: 0.3 → 0.1
- learn_proposal_Rminus1_max: 30 → 50
These affect efficiency only, not the target posterior.

## Notes
- This GPU run serves as a **validation run** (not canonical)
- Canonical results will come from CPU primary runs
- GPU chains may continue running in background
