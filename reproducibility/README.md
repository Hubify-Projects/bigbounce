# Reproducibility Bundle

**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology: Phenomenological Constraints and Correlated Signatures
**Author:** Houston Golden
**Version:** v0.9.0 (2026-03-03)

## Quick Start

```bash
# 1. Create environment
pip install cobaya==3.5.4 getdist cmdstanpy arviz pandas numpy matplotlib
cobaya-install cosmo -p ./packages
install_cmdstan

# 2. Reproduce cosmological fits (~4-12h per config)
cd cosmology && bash reproduce_cosmology.sh

# 3. Reproduce galaxy spin fit (~10-30min)
cd galaxy_spins && bash reproduce_spins.sh
```

## Repository Structure

```
reproducibility/
├── README.md                  # This file
├── cosmology/
│   ├── cobaya_planck.yaml           # Planck-only (Table IV row 1)
│   ├── cobaya_planck_bao.yaml       # Planck + BAO (Table IV row 2)
│   ├── cobaya_planck_bao_sn.yaml    # Planck + BAO + SN (Table IV row 3)
│   ├── cobaya_full_tension.yaml     # Full tension dataset (Tables III, IV row 4)
│   └── reproduce_cosmology.sh       # One-command reproduction
├── galaxy_spins/
│   ├── spin_fit_stan.py             # Hierarchical Bayesian model (Stan)
│   ├── reproduce_spins.sh           # One-command reproduction
│   ├── DEPRECATED.md                # Deprecation notice for old data file
│   └── galaxy_spin_data_DEPRECATED.csv  # DEPRECATED — do not use
├── cmb_eb/
│   └── (empty — CMB EB values are literature citations, not original analysis)
├── results/
│   └── (populated by running reproduce scripts)
├── docs/
│   ├── IMPLEMENTATION_MAP.md        # Paper claim → code → output mapping
│   └── KNOWN_GAPS.md               # Honest disclosure of gaps
└── figures/
    └── (populated by running reproduce scripts)
```

## What This Bundle Reproduces

| Paper Result | Reproducible? | How |
|-------------|:---:|-----|
| H₀ = 69.2 ± 0.8 | YES | `cobaya_full_tension.yaml` with stock CAMB |
| σ₈ = 0.785 ± 0.016 | YES | `cobaya_full_tension.yaml` with stock CAMB |
| ΔN_eff ≈ 0.3 | YES | `cobaya_full_tension.yaml` with stock CAMB |
| Galaxy spin A₀, p, q | YES | `spin_fit_stan.py` + Shamir (2024) aggregate counts |
| χ²_eff, AIC, BIC | YES | From MCMC chain maximum likelihood |
| ln B (Bayes factors) | PARTIAL | Requires PolyChord (not included) |
| β ≈ 0.30° birefringence | N/A | Literature value (Planck) |
| Corner plots | YES | From chains using GetDist |

## What This Bundle Does NOT Reproduce

See `docs/KNOWN_GAPS.md` for full details:

1. **No custom CAMB modifications** — model uses standard ΛCDM + N_eff
2. **No pre-computed chains** — must be generated (~4-12h per config)
3. **No CNN classifier** — uses published catalogs
4. **No CMB map analysis** — birefringence is literature-cited
5. **No nested sampling** — Bayes factors require PolyChord

## Hardware Notes

- MCMC runs: 4+ CPU cores recommended, ~8 GB RAM
- Stan fit: Any modern laptop, ~1 GB RAM
- Disk: ~1 GB per MCMC chain set

## Known Issues

- The DES Y3 S8 constraint in `cobaya_full_tension.yaml` is approximated
  as a Gaussian prior, not the full 3x2pt likelihood.
- The Planck NPIPE likelihood (`CamSpec`) may produce slightly different
  results than the older `plikHM` likelihood used in some Planck papers.

## License

MIT License. See LICENSE file.

## Citation

```bibtex
@article{Golden2026,
  author = {Golden, Houston},
  title = {Geometric Dark Energy from Spin-Torsion Cosmology:
           Phenomenological Constraints and Correlated Signatures},
  year = {2026},
  eprint = {XXXX.XXXXX},
  archivePrefix = {arXiv},
  primaryClass = {gr-qc}
}
```
