# Track C v2: Upgraded Birefringence Summary-Likelihood Inference

## What This Is

Gaussian summary-likelihood inference on the cosmic birefringence angle β using published measurements from Planck NPIPE (Eskilt 2022) and ACT DR6 (Diego-Palazuelos & Komatsu 2025).

## What This Is NOT

- NOT a map-level CMB analysis
- NOT a harmonic-space EB/TB likelihood
- NOT a derivation of f_photon from first principles
- NOT a full MCMC (analytically tractable; sampler would be performative)

## Data Sources

| Source | β (deg) | σ (deg) | arXiv |
|--------|---------|---------|-------|
| Eskilt 2022 (Planck NPIPE) | 0.30 | 0.11 | 2205.13962 |
| Diego-Palazuelos & Komatsu 2025 (ACT DR6) | 0.215 | 0.074 | 2503.14452 |

## Run

```bash
cd v2/scripts
python3 track_c_summary_likelihood.py
```

Runtime: < 3 seconds. No external dependencies beyond numpy, scipy, matplotlib.

## Outputs

- `track_c_v2_beta_posterior.pdf` — Posterior on β
- `track_c_v2_fphoton_posterior.pdf` — Derived posterior on f_photon
- `track_c_v2_degeneracy.pdf` — 2D (f_photon, C₀) constraint
- `track_c_v2_corner.pdf` — Summary corner plot
- `track_c_v2_results_summary.txt` — Full results table
- `track_c_v2_likelihood_table.csv` — Machine-readable results

## Key Result

β = 0.242° ± 0.061° (3.9σ from zero)
f_photon = 1.73 ± 0.44 (for C₀ = 1)
Bayes factor BF(β≠0) ≈ 13 (moderate-to-strong evidence)
