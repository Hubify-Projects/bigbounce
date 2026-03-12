# Paper 2 Snapshot — 2026-03-06 07:06 UTC

Self-contained archive of all Paper 2 first-run outputs across four research tracks.

## Snapshot Contents

| Track | Directory | Files | Run Outputs | Figures |
|-------|-----------|-------|-------------|---------|
| WP4 ΔNeff microphysics | `paper2/wp4_dneff_microphysics/` | 41 | reheating (24k pts) + decay (32k pts) | 4 (PDF+PNG) |
| WP5 Spin amplitude | `paper2/wp5_spin_amplitude/` | 16 | 100k MC samples | 3 (PNG) |
| P7 CNN spin classifier | `paper2/p7_cnn_spin_classifier/` | 2223 | ResNet-18 model + 2000 images | 2 (PNG) |
| P6 CMB EB birefringence | `paper2/p6_cmb_eb_pipeline/` | 15 | Tier 1 registry + forest plot | 2 (PDF+PNG) |
| **Total** | | **2296** | | |

Checksums: `SHA256SUMS.txt` (2296 entries)

---

## Track A — WP4 ΔNeff Microphysics

- **Pod**: paper2-wp4-dneff (bpou58tmt95jjb), RTX A5000
- **Run ID**: reheating + decay first pass
- **Python**: 3.11, numpy/scipy/matplotlib
- **Framing**: Candidate microphysics realization (NOT first-principles derivation)

### Dataset Sources
- Planck 2018 parameters (arXiv:1807.06209)
- BBN constraints Yeh+2022 (arXiv:2204.11297), Burns+2024 (arXiv:2401.15054)

### Commands
```bash
python scan.py --model reheating --output runs/reheating/
python scan.py --model decay --output runs/decay/
python plots.py --input runs/ --output figures/
```

### Key Results
- Reheating: 100x80x3 = 24,000 grid points, T_rh = {1e6, 1e9, 1e12} GeV
  - Best fit: ΔNeff = 0.155, Br_dr = 0.014, g*_hidden = 6.25, T_rh = 1e6 GeV
- Decay: 100x80x4 = 32,000 grid points, 4 (Br_dark, Y_X) configurations
  - Best fit: ΔNeff = 0.150, m_X = 2.66e6 GeV, τ_X = 9.4e-5 s (fiducial)
- Constraints: BBN_max = 0.5, CMB_max = 0.34, target = [0.10, 0.20]

### Run Outputs
- `runs/reheating/scan_results.csv`, `summary.json`, 8x .npy grids
- `runs/decay/scan_results.csv`, `summary.json`, 10x .npy grids
- `figures/fig1_reheating_contours.{pdf,png}`
- `figures/fig2_decay_contours.{pdf,png}`
- `figures/fig3_allowed_regions.{pdf,png}`
- `figures/fig4_model_comparison.{pdf,png}`

---

## Track B — WP5 Spin Amplitude

- **Pod**: paper2-wp5-spin (mz3srzbzxxv1yj), RTX A5000
- **Run ID**: first_run (100k MC)
- **Python**: 3.11, numpy/scipy/matplotlib
- **Framing**: Phenomenological parity-odd tidal torque mapping (NOT torsion derivation)

### Dataset Sources
- Galaxy spin counts Shamir 2024 (arXiv:2401.09450)
- TTT parameters Porciani+2002 (MNRAS 332, 325)

### Commands
```bash
python monte_carlo_sensitivity.py --n_samples 100000 --output runs/first_run/
```

### Key Results
- 100,000 MC samples of (λ, σ_lnλ, δ_rms, ε_PO)
- Required ε_PO for A₀ = 0.003: median 0.244, 68% CI [0.14, 0.38], 95% CI [0.09, 0.55]
- A₀ ≈ ε_PO × 0.015 scaling relation

### Run Outputs
- `runs/first_run/mc_samples.csv` (100k rows)
- `runs/first_run/summary.txt`
- `runs/first_run/A0_vs_epsPO.png`
- `runs/first_run/required_epsPO_hist.png`
- `runs/first_run/corner_plot.png`

---

## Track C — P7 CNN Spin Classifier

- **Pod**: paper2-p7-cnn (pkysk4lbaqnhm0), RTX A5000
- **Run ID**: first_run (10 epochs, synthetic data)
- **Python**: 3.x, PyTorch 2.x, torchvision
- **Framing**: Pipeline/data product (NOT cosmological measurement)

### Dataset Sources
- Synthetic fallback (2000 procedural PIL spirals) — SDSS not available on pod
- SYNTHETIC_DATA_FLAG.txt present in data directory

### Commands
```bash
bash reproduce_training.sh
# Executed: dataset_build_sdss_gz.py --use_synthetic + train_resnet18.py --epochs 10
```

### Key Results
- **FAIL** — test_acc = 0.487 (random chance)
- val_acc = 0.553, test_loss = 0.700
- 1400 train / 300 val / 300 test split
- Model: ResNet-18 pretrained, AdamW lr=1e-4, CosineAnnealing, label_smoothing=0.1

### Root Cause (see failure_analysis.txt)
1. RandomHorizontalFlip(p=0.5) conflicts with parity augmentation → 50% label corruption
2. 100% synthetic data (procedural spirals, not real galaxies)
3. 1400 images for 11M-param model

### Run Outputs
- `runs/first_run/model.pt` (46 MB — should be discarded)
- `runs/first_run/classification_report.txt`
- `runs/first_run/confusion_matrix.png`, `training_curves.png`
- `runs/first_run/hyperparams.json`, `training_curves.json`, `test_predictions.json`
- `data/images/cw/` (1000 synthetic CW images)
- `data/images/ccw/` (1000 synthetic CCW images)
- `data/catalog.csv`
- `failure_analysis.txt` (post-run diagnostic)

---

## Track D — P6 CMB EB Birefringence

- **Pod**: paper2-p6-eb (uktt3hghbs1djo), RTX A5000
- **Run ID**: tier1_first_run
- **Python**: 3.11, numpy/scipy/matplotlib
- **Framing**: Two-tier (Tier 1 = literature registry, Tier 2 = map estimator, NOT attempted)

### Dataset Sources
- Minami & Komatsu 2020 (arXiv:2011.11254)
- Eskilt 2022 (arXiv:2205.13962)
- Eskilt et al. 2022 (arXiv:2203.04830)
- Zagatti et al. 2025 (arXiv:2502.07654)
- Diego-Palazuelos & Komatsu 2025 (arXiv:2509.13654)
- SPIDER Collaboration 2025 (arXiv:2510.25489)

### Commands
```bash
python beta_registry.py --output runs/tier1_first_run/
```

### Key Results
- β (stat only, all 6) = 0.358 ± 0.025 deg (χ² = 12.4, p = 0.030)
- β (stat+syst, all 6) = 0.294 ± 0.032 deg (χ² = 1.9, p = 0.859)
- β (independent only, 4) = 0.392 ± 0.033 deg (χ² = 9.4, p = 0.024)
- Tier 2 NOT attempted (requires 13 GB Planck PR4/NPIPE maps + healpy)

### Run Outputs
- `runs/tier1_first_run/beta_registry.json`
- `runs/tier1_first_run/beta_summary.json`
- `runs/tier1_first_run/forest_plot.pdf`
- `runs/tier1_first_run/forest_plot.png`

---

## Environment Summary

| Pod | Hardware | Python | Status |
|-----|----------|--------|--------|
| paper2-wp4-dneff | RTX A5000, 96 vCPU | 3.11 | STOPPED 2026-03-06 |
| paper2-wp5-spin | RTX A5000, 96 vCPU | 3.11 | STOPPED 2026-03-06 |
| paper2-p7-cnn | RTX A5000, 96 vCPU | 3.x | TERMINATED |
| paper2-p6-eb | RTX A5000, 96 vCPU | 3.11 | STOPPED 2026-03-06 |

## Archive Integrity

Source archives (in parent directory):
- `wp4_archive.tar.gz` — SHA256: a0aad2899064d7055955c3628b755d45208a2fd396b083df87f6af86b84915d3
- `wp5_archive.tar.gz` — SHA256: 5817f19056227aff8b0a9a1e1309e2e97cdaca2845576c671d615d8a669f5477
- `p7_archive.tar.gz` — SHA256: f01a10aa35831cdc777b55fa6b5810c3ec31670dd17eacfc2fb9462cdfc30ec6
- `p6_archive.tar.gz` — SHA256: a456eca86e4c15ca93e859644d00125b22b58e6f48cd181e42639e6a788e913b

Per-file checksums: `SHA256SUMS.txt` (verify with `shasum -c SHA256SUMS.txt`)
