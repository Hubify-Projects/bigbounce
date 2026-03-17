# Track A: SMBH Seed Minimum Mass Analysis

## Scope

Forward-model constraint analysis computing the minimum seed mass required
to grow observed high-redshift supermassive black holes via Eddington-limited
accretion (Salpeter growth). This is NOT an MCMC fit -- it is a deterministic
calculation for each observed SMBH given growth assumptions.

The analysis compares results under two cosmologies:
- **Planck 2018**: H0 = 67.4, Om = 0.315, OL = 0.685
- **Framework (spin-torsion)**: H0 = 69.2, sigma8 = 0.785, DNeff = 0.24

## Inputs

Five observed high-z SMBHs (hardcoded from literature):
- UHZ-1: M_BH ~ 4e7 Msun at z = 10.1 (Bogdan et al. 2024)
- GN-z11: M_BH ~ 1.6e6 Msun at z = 10.6 (Maiolino et al. 2024)
- CEERS-1019: M_BH ~ 1e7 Msun at z = 8.68 (Larson et al. 2023)
- J0313-1806: M_BH ~ 1.6e9 Msun at z = 7.64 (Wang et al. 2021)
- J1342+0928: M_BH ~ 8e8 Msun at z = 7.54 (Banados et al. 2018)

## Outputs

Saved to `outputs/`:
- `minimum_seed_mass_vs_zseed.pdf` -- Minimum seed mass vs z_seed for each object
- `growth_time_consistency.pdf` -- M_seed vs available growth time
- `seed_mass_summary.csv` -- Table of M_seed,min at z_seed=20 for f_duty = 0.5, 0.7, 1.0

## How to Run

```bash
pip install -r requirements.txt
python scripts/minimum_seed_mass.py
```

All outputs are written to `outputs/`.
