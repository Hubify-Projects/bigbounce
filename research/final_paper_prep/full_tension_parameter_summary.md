# full_tension Parameter Summary — Paper 1 Anchor Result

**Frozen:** 2026-03-11 17:28 UTC
**Dataset:** full_tension (Planck NPIPE + BAO DR16 + Pantheon+ SN + Riess 2020 H0 + DES S8)
**Model:** LCDM + Delta_Neff (7 sampled parameters)
**Chains:** 6 chains, 175,545 total accepted samples
**Convergence:** All 9/9 freeze gates pass

---

## Sampled Parameters

| Parameter | Mean | Std (68%) | Description |
|-----------|------|-----------|-------------|
| H0 | 0.8035 | 0.0084 | Hubble constant (scaled; H0/100 km/s/Mpc) |
| delta_neff (nnu) | 13.8212 | 0.1670 | Effective number of neutrino species (raw Cobaya param) |
| tau | 1.04092 | 0.00038 | Optical depth to reionization (scaled) |
| sigma8 | 0.3081 | 0.0055 | RMS matter fluctuations in 8 Mpc/h spheres |
| omegam | 0.8141 | 0.0085 | Total matter density parameter |
| ns | 0.02227 | 0.00016 | Scalar spectral index |

## Derived Quantities

| Quantity | Value | Notes |
|----------|-------|-------|
| S8 | -0.0183 +/- 0.169 | sigma8 * sqrt(omegam/0.3) |

## Convergence Diagnostics

| Metric | H0 | delta_neff | tau |
|--------|-----|------------|-----|
| R-1 | 0.000629 | 0.000517 | 0.000511 |
| R-1 target | < 0.01 | < 0.01 | < 0.02 |
| ESS | 5,513 | 4,832 | 5,475 |
| ESS target | > 2,000 | > 2,000 | > 1,000 |
| Drift | 0.051σ | 0.069σ | 0.073σ |
| Drift target | < 0.1σ | < 0.1σ | < 0.1σ |

GetDist Gelman-Rubin (worst R-1 across all params): 0.004470

## Figures

- `paper/figures/full_tension_triangle.pdf` — 6-parameter triangle/corner plot
- `paper/figures/full_tension_triangle.png` — same, PNG format
- `paper/figures/full_tension_posteriors.pdf` — 1D marginalized posteriors
- `paper/figures/full_tension_posteriors.png` — same, PNG format

## Frozen Artifact Location

- Network volume: `/workspace/bigbounce/frozen/full_tension_20260311_1728/`
- Local: `reproducibility/cosmology/frozen/full_tension_20260311_1728/`
- Snapshot: `snapshots/frozen_full_tension_20260311_1728.tar.gz`
