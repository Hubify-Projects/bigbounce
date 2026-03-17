# Track C: Parity / CMB Birefringence Analysis

## What this analysis does

This analysis asks a single, well-defined question:

> **Given the spin-torsion operator scale alpha/M ~ 10^{-21} GeV^{-1}, what effective photon-torsion coupling f_photon is needed to reproduce observed cosmic birefringence beta ~ 0.30 deg?**

Answer: f_photon ~ O(1). No fine-tuning is required.

## What this analysis does NOT claim

- It does **not** derive f_photon from first principles.
- It does **not** predict the birefringence angle.
- It does **not** claim the spin-torsion framework uniquely explains birefringence.
- It does **not** resolve the photon-torsion coupling gap (see below).

## The photon-torsion coupling gap

The spin-torsion framework has a parity-odd gravitational operator:

    L_PV = (alpha/M) * epsilon^{abcd} K_{ab} R_{cd}

This operator acts on the gravitational sector. It does **not** directly couple to photons. For cosmic birefringence to occur, there must be a coupling between the torsion field and the electromagnetic field. This coupling is parameterized by f_photon but not derived from the theory.

The parameterization is:

    beta = g_eff * C_0
    g_eff = (alpha/M) * f_photon * M_Pl

where C_0 ~ O(1) radian is a geometric/cosmological factor encoding the integrated field excursion.

## Scripts

### 1. `scripts/consistency_window.py`
Maps out what f_photon is required as a function of the geometric factor C_0, overlaid with observed birefringence constraints.

```bash
python scripts/consistency_window.py
```

**Outputs:**
- `outputs/consistency_window.pdf` / `.png` — f_photon vs beta with observational bands
- `outputs/consistency_window_summary.txt` — numerical summary

### 2. `scripts/gaussian_posterior.py`
Computes the combined Gaussian posterior on beta from independent published measurements (Eskilt 2022 + Diego-Palazuelos & Komatsu 2025), then maps to posteriors on g_eff and f_photon.

```bash
python scripts/gaussian_posterior.py
```

**Outputs:**
- `outputs/beta_posterior.pdf` / `.png` — individual and combined beta posteriors
- `outputs/geff_posterior.pdf` / `.png` — posteriors on g_eff and f_photon
- `outputs/posterior_summary.txt` — summary statistics with confidence intervals

### 3. `scripts/eb_shape_comparison.py`
Forward-models the EB cross-spectrum from isotropic birefringence using the exact relation:

    C_l^{EB} = sin(2*beta)/2 * (C_l^{EE} - C_l^{BB})

Shows the isotropy diagnostic: the ratio C_l^{EB}/(C_l^{EE} - C_l^{BB}) should be constant across all ell for isotropic birefringence.

```bash
python scripts/eb_shape_comparison.py
```

**Outputs:**
- `outputs/eb_shape_comparison.pdf` / `.png` — EE, BB, and predicted EB spectra
- `outputs/eb_ratio_diagnostic.pdf` / `.png` — ratio diagnostic plot

Uses CAMB if available; falls back to an analytic approximation for spectrum shape.

## Data

`data/published_birefringence_measurements.csv` contains published Gaussian constraints on the isotropic birefringence angle:

| Experiment | beta (deg) | sigma (deg) | Status |
|---|---|---|---|
| Minami & Komatsu 2020 | 0.35 | 0.14 | Superseded by Eskilt 2022 |
| Eskilt 2022 | 0.30 | 0.11 | Independent, used in fit |
| Diego-Palazuelos & Komatsu 2025 | 0.215 | 0.074 | Independent, used in fit |
| SPIDER 2025 | 0.50 | 0.07 | Calibration degeneracy caveat |

## Requirements

```bash
pip install -r requirements.txt
```

Core: numpy, scipy, matplotlib, pyyaml
Optional: camb (for accurate CMB power spectra in eb_shape_comparison.py)

## Configuration

All analysis parameters are in `configs/analysis_config.yaml`.
