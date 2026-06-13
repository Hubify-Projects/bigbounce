# Implementation Map: Paper Claims → Code → Output

This document maps every "This work" numerical result in the paper to the
code and configuration that produces it.

Last synced to paper version: v1B.0.68 (2026-06-13, EXT9 closure wave).

## Cosmological Fits (Table I — ΛCDM+ΔNeff frozen chains)

| Paper Result | Full-tension value | Planck+BAO+SN value | Config | Notes |
|-------------|-------------------|---------------------|--------|-------|
| H₀ (MCMC fit) | 67.68 ± 1.06 km/s/Mpc | 67.78 ± 1.09 km/s/Mpc | `cosmology/cobaya_full_tension.yaml` / `cobaya_planck_bao_sn.yaml` | ΛCDM + ΔNeff, stock CAMB |
| σ₈ (MCMC fit) | 0.803 ± 0.008 | 0.812 ± 0.009 | `cosmology/cobaya_full_tension.yaml` | Derived parameter |
| ΔNeff | −0.020 ± 0.169 | +0.058 ± 0.179 | `cosmology/cobaya_full_tension.yaml` | Free parameter (nnu − 3.046); consistent with zero in both combinations |
| χ²_total (w0wa iter2 chain) | 14037.4 ± 5.6 | — | `cosmology/iter2_converged_2026-05-18/` | GetDist weighted-sample average; channels BAO 10.6, CMB 10983.9, SN 3043.0 |
| ln B (any combination) | Not computed | Not computed | Requires PolyChord nested sampling | Not provided; see KNOWN_GAPS |
| H₀ tension vs SH0ES | 3.6σ | 3.6σ | Arithmetic from Table I | (67.68 − 73.04)/√(1.06²+1.04²) ≈ 3.6σ; no code needed |

## Galaxy Spin Fit (Table II, Fig. 2)

| Paper Result | Value | Code | Notes |
|-------------|-------|------|-------|
| A₀ | 0.003 ± 0.001 | `galaxy_spins/spin_fit_stan.py` | Hierarchical Bayesian fit |
| p (power-law) | 0.5 ± 0.3 | `galaxy_spins/spin_fit_stan.py` | |
| q (exp. decay) | 0.5 ± 0.3 | `galaxy_spins/spin_fit_stan.py` | |
| Dipole axis | (l~52°, b~68°) | `galaxy_spins/spin_fit_stan.py` | |

## CMB E-B (Sec. III.A)

| Paper Result | Value | Code | Notes |
|-------------|-------|------|-------|
| β ≈ 0.30° | Planck measurement | N/A — literature value | Minami & Komatsu (2020) |
| C_ℓ^EB formula | Eq. (6) | N/A — standard formula | Textbook result |

## KNOWN GAPS

1. **Bayes factors (ln B)**: Not computed. Require PolyChord nested sampling.
   The Cobaya YAMLs can be adapted; see KNOWN_GAPS.md §3 for details.

2. **Corner plots**: Not pre-generated. Produce from committed frozen chains
   using GetDist after running `reproduce_cosmology.sh`.

3. **Galaxy spin classifier**: The ALP consistency check uses published
   CW/CCW counts from the literature; no CNN training code is provided here.
   Production chirality pipeline is in `pipelines/p2_chirality/`.

4. **EB/TB power spectra**: Not recomputed from Planck maps. All birefringence
   values are literature citations (Minami & Komatsu 2020, Eskilt 2022).
   NaMaster injection-recovery tests validate the pipeline approach.
