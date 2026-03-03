# Implementation Map: Paper Claims → Code → Output

This document maps every "This work" numerical result in the paper to the
code and configuration that produces it.

## Cosmological Fits (Tables I, III, IV, V, XI)

| Paper Result | Value | Config | Notes |
|-------------|-------|--------|-------|
| H₀ (MCMC fit) | 69.2 ± 0.8 km/s/Mpc | `cosmology/cobaya_full_tension.yaml` | ΛCDM + ΔN_eff, stock CAMB |
| σ₈ (MCMC fit) | 0.785 ± 0.016 | `cosmology/cobaya_full_tension.yaml` | Derived parameter |
| ΔN_eff | 0.3 ± 0.2 | `cosmology/cobaya_full_tension.yaml` | Free parameter (nnu - 3.046) |
| χ²_eff | 1148.3 | `cosmology/cobaya_full_tension.yaml` | From chain maximum likelihood |
| ln B (Planck+BAO) | -1.2 ± 0.3 | Requires PolyChord nested sampling | Not provided; see KNOWN_GAPS |
| ln B (full tension) | +4.8 ± 0.5 | Requires PolyChord nested sampling | Not provided; see KNOWN_GAPS |
| Tension σ (H₀ vs SH0ES) | 2.93σ | Arithmetic: (69.2-73.04)/√(0.8²+1.04²) | No code needed |
| Tension σ (σ₈ vs Planck) | 1.52σ | Arithmetic: (0.785-0.811)/√(0.016²+0.006²) | No code needed |

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

1. **Bayes factors (ln B)**: Require PolyChord nested sampling runs which are
   computationally expensive and not included. The configs could be modified
   to use PolyChord by changing the sampler block.

2. **Corner plots**: Not pre-generated. Can be produced from chains using
   GetDist after running the MCMC.

3. **CNN galaxy classifier**: The paper references a CNN for galaxy spin
   classification. No CNN training code is provided. The hierarchical fit
   uses published CW/CCW counts from the literature.

4. **EB/TB power spectra**: Not computed from Planck maps. All birefringence
   values are literature citations (Minami & Komatsu 2020, Eskilt 2022).
