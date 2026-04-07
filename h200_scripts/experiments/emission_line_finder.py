#!/usr/bin/env python3
"""
Experiment: Automated Emission Line Detection in Spectra

Generate 50K synthetic spectra (4000 wavelength bins, 3500-10000A) with planted
emission lines at various redshifts. Train a 1D CNN to detect and locate emission
lines (multi-label classification + regression for line centers). Apply to the
anomaly population to auto-measure redshifts and classify AGN vs star-forming
via BPT diagram proxies.

Lines planted: H-alpha (6563A), H-beta (4861A), [OIII]5007, [NII]6584,
               Ly-alpha (1216A), MgII (2800A), CIV (1549A)

Method:
  - Synthetic spectra: continuum (power-law + noise) + Gaussian emission lines
  - Redshift range: 0 < z < 3.5 (different lines enter/exit the window)
  - 1D CNN: Conv1D backbone -> dual heads (classification + center regression)
  - BPT proxy: log([NII]/H-alpha) vs log([OIII]/H-beta) from detected line fluxes
  - PyTorch DataLoader with GPU acceleration

Output: /workspace/bigbounce/outputs/emission-line-finder/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split

from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
from sklearn.metrics import classification_report, confusion_matrix

# ============================================================
# NumpyEncoder for JSON serialization
# ============================================================

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super().default(obj)

# ============================================================
# Configuration
# ============================================================

OUTPUT_DIR = "/workspace/bigbounce/outputs/emission-line-finder"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

N_SPECTRA = 50000
N_BINS = 4000
WAVE_MIN = 3500.0  # Angstroms
WAVE_MAX = 10000.0  # Angstroms
WAVELENGTH = np.linspace(WAVE_MIN, WAVE_MAX, N_BINS)

# Emission lines: name -> rest-frame wavelength (Angstroms)
EMISSION_LINES = {
    'Ly_alpha': 1216.0,
    'CIV':      1549.0,
    'MgII':     2800.0,
    'H_beta':   4861.0,
    'OIII_5007': 5007.0,
    'NII_6584': 6584.0,
    'H_alpha':  6563.0,
}
LINE_NAMES = list(EMISSION_LINES.keys())
N_LINES = len(LINE_NAMES)

# Redshift range
Z_MIN = 0.0
Z_MAX = 3.5

# Training
BATCH_SIZE = 256
N_EPOCHS = 25
LR = 1e-3
NUM_WORKERS = 4

print("=" * 70)
print("EXPERIMENT: Automated Emission Line Detection")
print(f"  Device: {DEVICE}")
print(f"  Spectra: {N_SPECTRA}, Bins: {N_BINS}")
print(f"  Wavelength range: {WAVE_MIN}-{WAVE_MAX} A")
print(f"  Lines: {N_LINES} ({', '.join(LINE_NAMES)})")
print("=" * 70)

# ============================================================
# Synthetic Spectrum Generation
# ============================================================

def generate_continuum(n, rng):
    """Generate power-law continuum: F ~ lambda^alpha with noise."""
    alpha = rng.uniform(-2.0, 0.5, size=(n, 1))
    # Normalize wavelength
    lam_norm = WAVELENGTH[None, :] / 5500.0
    continuum = lam_norm ** alpha
    # Add broadband noise
    noise_level = rng.uniform(0.01, 0.15, size=(n, 1))
    noise = rng.normal(0, 1, size=(n, N_BINS)) * noise_level
    return continuum + noise, alpha.flatten()

def add_emission_lines(spectra, rng):
    """Plant emission lines at random redshifts. Return labels."""
    n = spectra.shape[0]
    redshifts = rng.uniform(Z_MIN, Z_MAX, size=n)

    # Labels: binary presence of each line + center positions (in bin index)
    line_present = np.zeros((n, N_LINES), dtype=np.float32)
    line_centers = np.full((n, N_LINES), -1.0, dtype=np.float32)  # -1 = not present

    for i in range(n):
        z = redshifts[i]
        # Randomly select which lines to plant (60-100% of visible lines)
        for j, (name, rest_wave) in enumerate(EMISSION_LINES.items()):
            obs_wave = rest_wave * (1 + z)
            if WAVE_MIN < obs_wave < WAVE_MAX:
                # Plant with 70% probability
                if rng.random() < 0.70:
                    # Line parameters
                    flux = rng.uniform(0.5, 20.0)
                    sigma_a = rng.uniform(2.0, 15.0)  # Angstroms
                    # Convert to bin space
                    bin_center = (obs_wave - WAVE_MIN) / (WAVE_MAX - WAVE_MIN) * N_BINS
                    sigma_bins = sigma_a / ((WAVE_MAX - WAVE_MIN) / N_BINS)
                    # Add Gaussian line
                    bins = np.arange(N_BINS)
                    line_profile = flux * np.exp(-0.5 * ((bins - bin_center) / sigma_bins) ** 2)
                    spectra[i] += line_profile
                    line_present[i, j] = 1.0
                    line_centers[i, j] = bin_center / N_BINS  # Normalize to [0, 1]

    return spectra, line_present, line_centers, redshifts

def generate_dataset():
    """Generate full synthetic spectral dataset."""
    print("\n[1/5] Generating synthetic spectra...")
    t0 = time.time()
    rng = np.random.default_rng(42)

    spectra, alphas = generate_continuum(N_SPECTRA, rng)
    spectra, line_present, line_centers, redshifts = add_emission_lines(spectra, rng)

    # Normalize each spectrum to unit peak
    peak_vals = np.max(np.abs(spectra), axis=1, keepdims=True)
    peak_vals = np.maximum(peak_vals, 1e-8)
    spectra = spectra / peak_vals

    # Convert to float32
    spectra = spectra.astype(np.float32)

    n_with_lines = int(np.sum(np.any(line_present > 0, axis=1)))
    total_lines = int(np.sum(line_present))
    print(f"  Generated {N_SPECTRA} spectra in {time.time() - t0:.1f}s")
    print(f"  Spectra with >= 1 line: {n_with_lines} ({100*n_with_lines/N_SPECTRA:.1f}%)")
    print(f"  Total planted lines: {total_lines}")
    for j, name in enumerate(LINE_NAMES):
        count = int(np.sum(line_present[:, j]))
        print(f"    {name}: {count} ({100*count/N_SPECTRA:.1f}%)")

    return spectra, line_present, line_centers, redshifts, alphas

# ============================================================
# PyTorch Dataset & DataLoader
# ============================================================

class SpectraDataset(Dataset):
    def __init__(self, spectra, line_present, line_centers):
        self.spectra = torch.from_numpy(spectra).unsqueeze(1)  # (N, 1, N_BINS)
        self.line_present = torch.from_numpy(line_present)
        self.line_centers = torch.from_numpy(line_centers)

    def __len__(self):
        return self.spectra.shape[0]

    def __getitem__(self, idx):
        return self.spectra[idx], self.line_present[idx], self.line_centers[idx]

# ============================================================
# 1D CNN Model
# ============================================================

class EmissionLineCNN(nn.Module):
    """1D CNN with dual heads: classification (line present) + regression (line center)."""
    def __init__(self, n_bins=N_BINS, n_lines=N_LINES):
        super().__init__()
        # Backbone: 1D conv layers with pooling
        self.backbone = nn.Sequential(
            nn.Conv1d(1, 32, kernel_size=15, padding=7),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.MaxPool1d(4),  # -> 1000

            nn.Conv1d(32, 64, kernel_size=11, padding=5),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.MaxPool1d(4),  # -> 250

            nn.Conv1d(64, 128, kernel_size=7, padding=3),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.MaxPool1d(5),  # -> 50

            nn.Conv1d(128, 256, kernel_size=5, padding=2),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(10),  # -> 10
        )
        feat_dim = 256 * 10

        # Classification head: sigmoid per line
        self.cls_head = nn.Sequential(
            nn.Linear(feat_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, n_lines),
        )

        # Regression head: line center position [0, 1] per line
        self.reg_head = nn.Sequential(
            nn.Linear(feat_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, n_lines),
            nn.Sigmoid(),
        )

    def forward(self, x):
        features = self.backbone(x)
        features = features.view(features.size(0), -1)
        cls_logits = self.cls_head(features)
        centers = self.reg_head(features)
        return cls_logits, centers

# ============================================================
# Training
# ============================================================

def train_model(spectra, line_present, line_centers):
    print("\n[2/5] Training 1D CNN emission line detector...")
    t0 = time.time()

    dataset = SpectraDataset(spectra, line_present, line_centers)
    n_train = int(0.8 * len(dataset))
    n_val = len(dataset) - n_train
    train_ds, val_ds = random_split(dataset, [n_train, n_val],
                                     generator=torch.Generator().manual_seed(42))

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                              num_workers=NUM_WORKERS, pin_memory=True, prefetch_factor=4)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False,
                            num_workers=NUM_WORKERS, pin_memory=True, prefetch_factor=4)

    model = EmissionLineCNN().to(DEVICE)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=N_EPOCHS)

    bce_loss_fn = nn.BCEWithLogitsLoss()
    mse_loss_fn = nn.MSELoss(reduction='none')

    best_val_loss = float('inf')
    history = []

    for epoch in range(N_EPOCHS):
        # Train
        model.train()
        train_cls_loss = 0.0
        train_reg_loss = 0.0
        n_batches = 0
        for spec_batch, lp_batch, lc_batch in train_loader:
            spec_batch = spec_batch.to(DEVICE, non_blocking=True)
            lp_batch = lp_batch.to(DEVICE, non_blocking=True)
            lc_batch = lc_batch.to(DEVICE, non_blocking=True)

            cls_logits, centers = model(spec_batch)

            # Classification loss
            cls_loss = bce_loss_fn(cls_logits, lp_batch)

            # Regression loss: only for lines that are present
            mask = lp_batch > 0.5
            reg_loss_all = mse_loss_fn(centers, lc_batch)
            if mask.any():
                reg_loss = reg_loss_all[mask].mean()
            else:
                reg_loss = torch.tensor(0.0, device=DEVICE)

            loss = cls_loss + 5.0 * reg_loss  # Weight regression higher

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_cls_loss += cls_loss.item()
            train_reg_loss += reg_loss.item()
            n_batches += 1

        scheduler.step()

        # Validate
        model.eval()
        val_cls_loss = 0.0
        val_reg_loss = 0.0
        val_batches = 0
        with torch.no_grad():
            for spec_batch, lp_batch, lc_batch in val_loader:
                spec_batch = spec_batch.to(DEVICE, non_blocking=True)
                lp_batch = lp_batch.to(DEVICE, non_blocking=True)
                lc_batch = lc_batch.to(DEVICE, non_blocking=True)

                cls_logits, centers = model(spec_batch)
                cls_loss = bce_loss_fn(cls_logits, lp_batch)
                mask = lp_batch > 0.5
                reg_loss_all = mse_loss_fn(centers, lc_batch)
                if mask.any():
                    reg_loss = reg_loss_all[mask].mean()
                else:
                    reg_loss = torch.tensor(0.0, device=DEVICE)

                val_cls_loss += cls_loss.item()
                val_reg_loss += reg_loss.item()
                val_batches += 1

        avg_train_cls = train_cls_loss / n_batches
        avg_train_reg = train_reg_loss / n_batches
        avg_val_cls = val_cls_loss / val_batches
        avg_val_reg = val_reg_loss / val_batches
        val_total = avg_val_cls + 5.0 * avg_val_reg

        history.append({
            'epoch': epoch + 1,
            'train_cls_loss': avg_train_cls,
            'train_reg_loss': avg_train_reg,
            'val_cls_loss': avg_val_cls,
            'val_reg_loss': avg_val_reg,
        })

        if val_total < best_val_loss:
            best_val_loss = val_total
            torch.save(model.state_dict(), os.path.join(OUTPUT_DIR, "best_model.pt"))

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  Epoch {epoch+1:3d}/{N_EPOCHS}: "
                  f"train_cls={avg_train_cls:.4f} train_reg={avg_train_reg:.6f} | "
                  f"val_cls={avg_val_cls:.4f} val_reg={avg_val_reg:.6f}")

    print(f"  Training complete in {time.time() - t0:.1f}s")
    print(f"  Best val loss: {best_val_loss:.4f}")

    # Load best model
    model.load_state_dict(torch.load(os.path.join(OUTPUT_DIR, "best_model.pt"),
                                      weights_only=True))
    return model, val_ds, history

# ============================================================
# Evaluation & BPT Classification
# ============================================================

def evaluate_model(model, val_ds):
    print("\n[3/5] Evaluating on validation set...")
    model.eval()
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False,
                            num_workers=NUM_WORKERS, pin_memory=True, prefetch_factor=4)

    all_preds = []
    all_labels = []
    all_center_preds = []
    all_center_true = []

    with torch.no_grad():
        for spec_batch, lp_batch, lc_batch in val_loader:
            spec_batch = spec_batch.to(DEVICE, non_blocking=True)
            cls_logits, centers = model(spec_batch)
            probs = torch.sigmoid(cls_logits).cpu().numpy()
            all_preds.append(probs)
            all_labels.append(lp_batch.numpy())
            all_center_preds.append(centers.cpu().numpy())
            all_center_true.append(lc_batch.numpy())

    preds = np.concatenate(all_preds, axis=0)
    labels = np.concatenate(all_labels, axis=0)
    center_preds = np.concatenate(all_center_preds, axis=0)
    center_true = np.concatenate(all_center_true, axis=0)

    # Binary predictions at threshold 0.5
    pred_binary = (preds > 0.5).astype(int)

    # Per-line metrics
    line_metrics = {}
    for j, name in enumerate(LINE_NAMES):
        tp = int(np.sum((pred_binary[:, j] == 1) & (labels[:, j] == 1)))
        fp = int(np.sum((pred_binary[:, j] == 1) & (labels[:, j] == 0)))
        fn = int(np.sum((pred_binary[:, j] == 0) & (labels[:, j] == 1)))
        tn = int(np.sum((pred_binary[:, j] == 0) & (labels[:, j] == 0)))
        precision = tp / max(tp + fp, 1)
        recall = tp / max(tp + fn, 1)
        f1 = 2 * precision * recall / max(precision + recall, 1e-8)

        # Center regression error (only where line present)
        mask = labels[:, j] > 0.5
        if mask.any():
            center_err = np.abs(center_preds[mask, j] - center_true[mask, j])
            mean_err_bins = float(np.mean(center_err) * N_BINS)
            mean_err_angstrom = float(np.mean(center_err) * (WAVE_MAX - WAVE_MIN))
        else:
            mean_err_bins = -1.0
            mean_err_angstrom = -1.0

        line_metrics[name] = {
            'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn,
            'precision': round(precision, 4),
            'recall': round(recall, 4),
            'f1': round(f1, 4),
            'mean_center_error_bins': round(mean_err_bins, 2),
            'mean_center_error_angstrom': round(mean_err_angstrom, 2),
        }
        print(f"  {name:12s}: P={precision:.3f} R={recall:.3f} F1={f1:.3f} "
              f"center_err={mean_err_angstrom:.1f}A")

    return line_metrics, preds, labels, center_preds, center_true

def bpt_classification(preds, center_preds, labels):
    """Classify AGN vs star-forming using BPT diagram proxies from detected lines."""
    print("\n[4/5] BPT diagram classification...")

    # We need H-alpha, H-beta, [OIII], [NII] all detected
    idx_hb = LINE_NAMES.index('H_beta')
    idx_oiii = LINE_NAMES.index('OIII_5007')
    idx_nii = LINE_NAMES.index('NII_6584')
    idx_ha = LINE_NAMES.index('H_alpha')

    pred_binary = (preds > 0.5).astype(int)

    # Spectra where all 4 BPT lines are detected
    bpt_mask = (pred_binary[:, idx_ha] == 1) & (pred_binary[:, idx_hb] == 1) & \
               (pred_binary[:, idx_oiii] == 1) & (pred_binary[:, idx_nii] == 1)

    n_bpt = int(np.sum(bpt_mask))
    print(f"  Spectra with all 4 BPT lines detected: {n_bpt}")

    if n_bpt == 0:
        print("  No BPT-classifiable spectra found.")
        return {'n_bpt_classifiable': 0}

    # Use detection probability as flux proxy (in real data we'd measure actual fluxes)
    ha_flux = preds[bpt_mask, idx_ha]
    hb_flux = preds[bpt_mask, idx_hb]
    oiii_flux = preds[bpt_mask, idx_oiii]
    nii_flux = preds[bpt_mask, idx_nii]

    # BPT ratios (using log of probability ratios as proxy)
    log_nii_ha = np.log10(np.clip(nii_flux / ha_flux, 1e-3, 100))
    log_oiii_hb = np.log10(np.clip(oiii_flux / hb_flux, 1e-3, 100))

    # Kewley+01 maximum starburst line: log([OIII]/Hb) = 0.61 / (log([NII]/Ha) - 0.47) + 1.19
    # Above this line -> AGN; below -> star-forming
    kewley_boundary = np.where(
        log_nii_ha < 0.47,
        0.61 / (log_nii_ha - 0.47) + 1.19,
        np.inf
    )

    is_agn = log_oiii_hb > kewley_boundary
    n_agn = int(np.sum(is_agn))
    n_sf = n_bpt - n_agn

    print(f"  AGN-classified: {n_agn} ({100*n_agn/n_bpt:.1f}%)")
    print(f"  Star-forming:   {n_sf} ({100*n_sf/n_bpt:.1f}%)")

    bpt_results = {
        'n_bpt_classifiable': n_bpt,
        'n_agn': n_agn,
        'n_star_forming': n_sf,
        'agn_fraction': round(n_agn / n_bpt, 4),
        'log_nii_ha_mean': round(float(np.mean(log_nii_ha)), 4),
        'log_oiii_hb_mean': round(float(np.mean(log_oiii_hb)), 4),
    }
    return bpt_results

# ============================================================
# Anomaly Population Application
# ============================================================

def apply_to_anomalies(model):
    """Generate anomaly-like spectra and apply the trained detector."""
    print("\n[5/5] Applying to simulated anomaly population...")
    rng = np.random.default_rng(123)

    # Generate 5000 anomaly-like spectra (higher noise, unusual continua)
    n_anom = 5000
    spectra_anom, _ = generate_continuum(n_anom, rng)
    # Add extra noise for anomaly character
    spectra_anom += rng.normal(0, 0.1, spectra_anom.shape)
    spectra_anom, lp_anom, lc_anom, z_anom, = add_emission_lines(spectra_anom, rng)[:4]

    # Normalize
    peak_vals = np.max(np.abs(spectra_anom), axis=1, keepdims=True)
    peak_vals = np.maximum(peak_vals, 1e-8)
    spectra_anom = (spectra_anom / peak_vals).astype(np.float32)

    # Run through model
    anom_ds = SpectraDataset(spectra_anom, lp_anom, lc_anom)
    anom_loader = DataLoader(anom_ds, batch_size=BATCH_SIZE, shuffle=False,
                             num_workers=NUM_WORKERS, pin_memory=True, prefetch_factor=4)

    model.eval()
    all_preds = []
    all_centers = []
    with torch.no_grad():
        for spec_batch, _, _ in anom_loader:
            spec_batch = spec_batch.to(DEVICE, non_blocking=True)
            cls_logits, centers = model(spec_batch)
            all_preds.append(torch.sigmoid(cls_logits).cpu().numpy())
            all_centers.append(centers.cpu().numpy())

    preds = np.concatenate(all_preds, axis=0)
    centers = np.concatenate(all_centers, axis=0)
    pred_binary = (preds > 0.5).astype(int)

    # Estimate redshifts from detected line centers
    estimated_z = []
    for i in range(n_anom):
        z_estimates = []
        for j, (name, rest_wave) in enumerate(EMISSION_LINES.items()):
            if pred_binary[i, j] == 1:
                obs_wave = centers[i, j] * (WAVE_MAX - WAVE_MIN) + WAVE_MIN
                z_est = (obs_wave / rest_wave) - 1.0
                if -0.01 < z_est < 5.0:
                    z_estimates.append(z_est)
        if z_estimates:
            estimated_z.append(float(np.median(z_estimates)))
        else:
            estimated_z.append(-1.0)

    estimated_z = np.array(estimated_z)
    valid = estimated_z > 0
    n_valid = int(np.sum(valid))

    if n_valid > 0:
        z_err = np.abs(estimated_z[valid] - z_anom[valid])
        print(f"  Anomaly spectra with redshift estimate: {n_valid}/{n_anom}")
        print(f"  Median |z_est - z_true|: {np.median(z_err):.4f}")
        print(f"  Mean |z_est - z_true|:   {np.mean(z_err):.4f}")
        print(f"  Fraction with |dz| < 0.01: {np.mean(z_err < 0.01):.3f}")
        print(f"  Fraction with |dz| < 0.05: {np.mean(z_err < 0.05):.3f}")
    else:
        z_err = np.array([])
        print("  No valid redshift estimates for anomaly spectra.")

    anomaly_results = {
        'n_anomaly_spectra': n_anom,
        'n_with_redshift': n_valid,
        'median_z_error': round(float(np.median(z_err)), 5) if len(z_err) > 0 else None,
        'mean_z_error': round(float(np.mean(z_err)), 5) if len(z_err) > 0 else None,
        'frac_dz_lt_0.01': round(float(np.mean(z_err < 0.01)), 4) if len(z_err) > 0 else None,
        'frac_dz_lt_0.05': round(float(np.mean(z_err < 0.05)), 4) if len(z_err) > 0 else None,
        'lines_detected_per_spectrum': round(float(np.mean(np.sum(pred_binary, axis=1))), 2),
    }
    return anomaly_results

# ============================================================
# Main
# ============================================================

def main():
    t_start = time.time()

    # Generate data
    spectra, line_present, line_centers, redshifts, alphas = generate_dataset()

    # Train model
    model, val_ds, history = train_model(spectra, line_present, line_centers)

    # Evaluate
    line_metrics, preds, labels, center_preds, center_true = evaluate_model(model, val_ds)

    # BPT classification
    bpt_results = bpt_classification(preds, center_preds, labels)

    # Apply to anomalies
    anomaly_results = apply_to_anomalies(model)

    # Save summary
    elapsed = time.time() - t_start
    summary = {
        'experiment': 'emission_line_finder',
        'n_spectra': N_SPECTRA,
        'n_bins': N_BINS,
        'wavelength_range_A': [WAVE_MIN, WAVE_MAX],
        'n_lines': N_LINES,
        'line_names': LINE_NAMES,
        'n_epochs': N_EPOCHS,
        'device': str(DEVICE),
        'training_history': history,
        'line_metrics': line_metrics,
        'bpt_classification': bpt_results,
        'anomaly_application': anomaly_results,
        'elapsed_seconds': round(elapsed, 1),
    }

    out_path = os.path.join(OUTPUT_DIR, "emission_line_finder_summary.json")
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)
    print(f"\nSaved summary to {out_path}")

    # Save training history CSV
    hist_df = pd.DataFrame(history)
    hist_df.to_csv(os.path.join(OUTPUT_DIR, "training_history.csv"), index=False)

    print(f"\nTotal elapsed: {elapsed:.1f}s")
    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
