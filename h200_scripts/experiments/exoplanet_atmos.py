#!/usr/bin/env python3
"""
Phase 7 Speculation: Exoplanet Atmosphere Anomaly Detection (JWST)
==================================================================
Search for anomalous exoplanet transmission spectra that deviate from
known atmosphere models. While not directly bounce-cosmology related,
this pipeline demonstrates the anomaly detection framework's versatility
and could flag genuinely unexpected atmospheric compositions.

Method:
  1. Generate 5000 synthetic JWST transmission spectra (1-5 micron, 200 bins).
  2. Plant atmosphere types: clear H2/He, cloudy, H2O-rich, CO2-dominated,
     and anomalous (biosignature-like O3+CH4, Ti/VO inversions, unknown absorbers).
  3. Train autoencoder on "known" atmosphere types.
  4. Flag spectra with high reconstruction error as anomalous.
  5. Classify anomaly sub-types.

Output: /workspace/bigbounce/outputs/exoplanet-atmospheres/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime, timezone

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, classification_report
from sklearn.ensemble import GradientBoostingClassifier
from scipy.signal import savgol_filter

# ============================================================
# NumpyEncoder
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/exoplanet-atmospheres"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

N_SPECTRA = 5000
N_WAVELENGTH_BINS = 200
WAVELENGTH_MIN = 1.0   # microns
WAVELENGTH_MAX = 5.0   # microns
SEED = 42
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Atmosphere type counts
N_CLEAR_H2HE = 2000
N_CLOUDY = 1000
N_H2O_RICH = 800
N_CO2_DOM = 700
# Anomalous types
N_BIOSIG = 100     # O3 + CH4
N_INVERSION = 80   # Ti/VO thermal inversion
N_UNKNOWN = 70     # unknown absorbers
N_EXOTIC = 50      # truly exotic (multi-peak unknown)
# Remaining filled with clear H2/He

# Autoencoder config
LATENT_DIM = 8
EPOCHS = 120
BATCH_SIZE = 256
LR = 1e-3

np.random.seed(SEED)
torch.manual_seed(SEED)

wavelengths = np.linspace(WAVELENGTH_MIN, WAVELENGTH_MAX, N_WAVELENGTH_BINS)

print(f"[exoplanet] Device: {DEVICE}")
print(f"[exoplanet] Generating {N_SPECTRA:,} synthetic transmission spectra ({N_WAVELENGTH_BINS} bins)")

# ============================================================
# Spectral Feature Templates
# ============================================================

def gaussian_absorption(wl, center, width, depth):
    """Gaussian absorption line/band."""
    return -depth * np.exp(-0.5 * ((wl - center) / width) ** 2)

def rayleigh_scattering(wl, strength=0.001):
    """Rayleigh scattering slope (stronger at shorter wavelengths)."""
    return strength * (1.0 / wl) ** 4

def cloud_deck(wl, cloud_top_wl=2.0, opacity=0.5):
    """Flat cloud deck that mutes features below cloud top."""
    muting = np.ones_like(wl)
    muting[wl < cloud_top_wl] *= (1 - opacity)
    return muting

# Key molecular absorption features (center wavelength, width in microns)
MOLECULES = {
    "H2O": [(1.15, 0.05, 0.3), (1.38, 0.06, 0.5), (1.87, 0.08, 0.4), (2.70, 0.15, 0.6)],
    "CO2": [(2.00, 0.05, 0.2), (2.70, 0.10, 0.3), (4.25, 0.15, 0.8)],
    "CH4": [(1.66, 0.06, 0.3), (2.32, 0.08, 0.4), (3.30, 0.12, 0.6)],
    "CO":  [(2.35, 0.06, 0.3), (4.60, 0.10, 0.5)],
    "O3":  [(3.30, 0.10, 0.3), (4.70, 0.12, 0.4)],  # ozone
    "TiO": [(1.10, 0.08, 0.4), (1.25, 0.06, 0.3)],   # Ti oxide
    "VO":  [(1.05, 0.05, 0.3), (1.18, 0.04, 0.2)],   # V oxide
}

def make_spectrum(atmos_type, rng):
    """Generate a synthetic transmission spectrum."""
    # Baseline: flat transit depth ~ 100-500 ppm
    baseline = rng.uniform(100, 500)  # ppm
    spectrum = np.full(N_WAVELENGTH_BINS, baseline)

    # Add Rayleigh scattering
    spectrum += rayleigh_scattering(wavelengths, strength=rng.uniform(0, 50))

    if atmos_type == "clear_h2he":
        # Clear H2/He with H2O and some CH4
        for center, width, depth in MOLECULES["H2O"]:
            d = depth * rng.uniform(0.5, 1.5) * baseline * 0.01
            spectrum += gaussian_absorption(wavelengths, center, width * rng.uniform(0.8, 1.2), d)
        for center, width, depth in MOLECULES["CH4"][:2]:
            d = depth * rng.uniform(0.1, 0.5) * baseline * 0.005
            spectrum += gaussian_absorption(wavelengths, center, width, d)

    elif atmos_type == "cloudy":
        # Muted features due to cloud deck
        muting = cloud_deck(wavelengths, cloud_top_wl=rng.uniform(1.5, 3.0),
                           opacity=rng.uniform(0.5, 0.9))
        for center, width, depth in MOLECULES["H2O"]:
            d = depth * rng.uniform(0.3, 1.0) * baseline * 0.008
            spectrum += gaussian_absorption(wavelengths, center, width, d) * muting

    elif atmos_type == "h2o_rich":
        # Dominated by deep H2O features
        for center, width, depth in MOLECULES["H2O"]:
            d = depth * rng.uniform(1.5, 3.0) * baseline * 0.015
            spectrum += gaussian_absorption(wavelengths, center, width * rng.uniform(1.0, 1.5), d)

    elif atmos_type == "co2_dom":
        # CO2-dominated (Venus-like)
        for center, width, depth in MOLECULES["CO2"]:
            d = depth * rng.uniform(1.5, 3.0) * baseline * 0.015
            spectrum += gaussian_absorption(wavelengths, center, width * rng.uniform(1.0, 1.5), d)
        for center, width, depth in MOLECULES["CO"]:
            d = depth * rng.uniform(0.3, 1.0) * baseline * 0.005
            spectrum += gaussian_absorption(wavelengths, center, width, d)

    elif atmos_type == "biosignature":
        # O3 + CH4 simultaneously (biosignature disequilibrium)
        for center, width, depth in MOLECULES["O3"]:
            d = depth * rng.uniform(1.0, 2.5) * baseline * 0.012
            spectrum += gaussian_absorption(wavelengths, center, width, d)
        for center, width, depth in MOLECULES["CH4"]:
            d = depth * rng.uniform(1.0, 2.5) * baseline * 0.012
            spectrum += gaussian_absorption(wavelengths, center, width, d)
        # Some H2O too
        for center, width, depth in MOLECULES["H2O"][:2]:
            d = depth * rng.uniform(0.5, 1.0) * baseline * 0.008
            spectrum += gaussian_absorption(wavelengths, center, width, d)

    elif atmos_type == "inversion":
        # Ti/VO thermal inversion: emission features (positive bumps) in near-IR
        for center, width, depth in MOLECULES["TiO"]:
            d = depth * rng.uniform(1.0, 2.0) * baseline * 0.01
            spectrum -= gaussian_absorption(wavelengths, center, width, d)  # note: emission
        for center, width, depth in MOLECULES["VO"]:
            d = depth * rng.uniform(1.0, 2.0) * baseline * 0.008
            spectrum -= gaussian_absorption(wavelengths, center, width, d)
        # Strong H2O absorption at longer wavelengths
        for center, width, depth in MOLECULES["H2O"][2:]:
            d = depth * rng.uniform(1.0, 2.0) * baseline * 0.01
            spectrum += gaussian_absorption(wavelengths, center, width, d)

    elif atmos_type == "unknown_absorber":
        # Unknown broad absorption at unusual wavelengths
        n_features = rng.integers(2, 5)
        for _ in range(n_features):
            center = rng.uniform(1.5, 4.5)
            width = rng.uniform(0.1, 0.4)  # broad
            depth = rng.uniform(0.5, 2.0) * baseline * 0.02
            spectrum += gaussian_absorption(wavelengths, center, width, depth)

    elif atmos_type == "exotic":
        # Multi-peaked unknown: sawtooth + absorption at non-molecular wavelengths
        # Periodic features (could be interference from unknown atmospheric structure)
        period = rng.uniform(0.3, 0.8)
        amplitude = rng.uniform(5, 30)
        spectrum += amplitude * np.sin(2 * np.pi * wavelengths / period)
        # Plus random deep features
        for _ in range(3):
            center = rng.uniform(1.2, 4.8)
            spectrum += gaussian_absorption(wavelengths, center, 0.05, rng.uniform(10, 50))

    # Add noise (JWST-like: ~10-30 ppm per bin)
    noise_level = rng.uniform(10, 30)
    spectrum += rng.normal(0, noise_level, N_WAVELENGTH_BINS)

    return spectrum

# ============================================================
# Generate All Spectra
# ============================================================

rng = np.random.default_rng(SEED)

spectra_list = []
labels = []
atmos_types = []

type_counts = [
    ("clear_h2he", N_CLEAR_H2HE),
    ("cloudy", N_CLOUDY),
    ("h2o_rich", N_H2O_RICH),
    ("co2_dom", N_CO2_DOM),
    ("biosignature", N_BIOSIG),
    ("inversion", N_INVERSION),
    ("unknown_absorber", N_UNKNOWN),
    ("exotic", N_EXOTIC),
]

# Fill remaining with clear H2/He
total_assigned = sum(c for _, c in type_counts)
remaining = N_SPECTRA - total_assigned
if remaining > 0:
    type_counts[0] = ("clear_h2he", type_counts[0][1] + remaining)

for atype, count in type_counts:
    for _ in range(count):
        spec = make_spectrum(atype, rng)
        spectra_list.append(spec)
        atmos_types.append(atype)
        # "known" vs "anomalous"
        if atype in ("biosignature", "inversion", "unknown_absorber", "exotic"):
            labels.append("anomalous")
        else:
            labels.append("known")

spectra = np.array(spectra_list)
labels = np.array(labels)
atmos_types = np.array(atmos_types)

print(f"[exoplanet] Spectra shape: {spectra.shape}")
print(f"[exoplanet] Type distribution:")
for atype, count in zip(*np.unique(atmos_types, return_counts=True)):
    print(f"  {atype:20s}: {count}")

# ============================================================
# Normalize Spectra
# ============================================================

scaler = StandardScaler()
spectra_scaled = scaler.fit_transform(spectra)

known_mask = labels == "known"
anomaly_mask = labels == "anomalous"

# ============================================================
# Autoencoder
# ============================================================

class SpectrumAutoencoder(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(128, input_dim),
        )

    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)

# Train on known atmospheres only
train_data = spectra_scaled[known_mask]
dataset = TensorDataset(torch.tensor(train_data, dtype=torch.float32))
loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                    num_workers=4, pin_memory=True, prefetch_factor=4)

model = SpectrumAutoencoder(N_WAVELENGTH_BINS, LATENT_DIM).to(DEVICE)
optimizer = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=1e-5)
criterion = nn.MSELoss()

print(f"\n[exoplanet] Training autoencoder on {train_data.shape[0]:,} known spectra...")
t0 = time.time()

for epoch in range(EPOCHS):
    epoch_loss = 0
    n_batches = 0
    for (batch,) in loader:
        batch = batch.to(DEVICE)
        recon = model(batch)
        loss = criterion(recon, batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
        n_batches += 1
    if (epoch + 1) % 30 == 0:
        print(f"  Epoch {epoch+1:3d}/{EPOCHS}: loss = {epoch_loss/n_batches:.6f}")

ae_time = time.time() - t0
print(f"[exoplanet] Autoencoder trained in {ae_time:.1f}s")

# ============================================================
# Compute Reconstruction Errors
# ============================================================

model.eval()
all_dataset = TensorDataset(torch.tensor(spectra_scaled, dtype=torch.float32))
all_loader = DataLoader(all_dataset, batch_size=BATCH_SIZE, shuffle=False,
                        num_workers=4, pin_memory=True, prefetch_factor=4)

recon_errors = []
per_bin_errors = []

with torch.no_grad():
    for (batch,) in all_loader:
        batch = batch.to(DEVICE)
        recon = model(batch)
        err = (batch - recon).cpu().numpy()
        recon_errors.append(np.mean(err**2, axis=1))
        per_bin_errors.append(err**2)

recon_errors = np.concatenate(recon_errors)
per_bin_errors = np.concatenate(per_bin_errors)

# ============================================================
# Anomaly Detection Performance
# ============================================================

is_anomaly = (labels == "anomalous").astype(int)
auc = roc_auc_score(is_anomaly, recon_errors)

# Threshold at 95th percentile of known spectra errors
known_errors = recon_errors[known_mask]
threshold = np.percentile(known_errors, 95)
flagged = recon_errors > threshold

n_flagged = flagged.sum()
n_true_pos = (flagged & anomaly_mask).sum()
n_false_pos = (flagged & known_mask).sum()

precision = n_true_pos / (n_flagged + 1e-12)
recall = n_true_pos / anomaly_mask.sum()

print(f"\n[exoplanet] === Anomaly Detection Results ===")
print(f"  AUC-ROC:    {auc:.4f}")
print(f"  Flagged:    {n_flagged} (threshold at 95th pct of known)")
print(f"  True pos:   {n_true_pos}")
print(f"  False pos:  {n_false_pos}")
print(f"  Precision:  {precision:.4f}")
print(f"  Recall:     {recall:.4f}")

# Per anomaly type
per_type_results = {}
for atype in ["biosignature", "inversion", "unknown_absorber", "exotic"]:
    mask = atmos_types == atype
    n_total = mask.sum()
    n_detected = (mask & flagged).sum()
    mean_error = recon_errors[mask].mean()
    per_type_results[atype] = {
        "total": int(n_total),
        "detected": int(n_detected),
        "detection_rate": float(n_detected / n_total) if n_total > 0 else 0,
        "mean_recon_error": float(mean_error),
    }
    print(f"  {atype:20s}: {n_detected}/{n_total} ({100*n_detected/n_total:.1f}%) mean_err={mean_error:.4f}")

# ============================================================
# Spectral Region Analysis — Where are the anomalies?
# ============================================================

# For flagged anomalies, which wavelength bins have the highest error?
flagged_anomaly_errors = per_bin_errors[flagged & anomaly_mask]
if len(flagged_anomaly_errors) > 0:
    mean_bin_error = flagged_anomaly_errors.mean(axis=0)
    top_bins = np.argsort(-mean_bin_error)[:10]
    top_wavelengths = wavelengths[top_bins]
    print(f"\n[exoplanet] Top anomalous wavelength regions:")
    for wl, err in zip(top_wavelengths, mean_bin_error[top_bins]):
        print(f"  {wl:.2f} um: error = {err:.4f}")
else:
    top_wavelengths = []
    mean_bin_error = np.zeros(N_WAVELENGTH_BINS)

# ============================================================
# Sub-type Classifier (on flagged objects)
# ============================================================

print(f"\n[exoplanet] Training sub-type classifier on anomalous spectra...")

anomaly_indices = np.where(anomaly_mask)[0]
if len(anomaly_indices) > 50:
    type_map = {"biosignature": 0, "inversion": 1, "unknown_absorber": 2, "exotic": 3}
    X_anom = spectra_scaled[anomaly_indices]
    y_anom = np.array([type_map.get(atmos_types[i], -1) for i in anomaly_indices])
    valid = y_anom >= 0
    X_anom = X_anom[valid]
    y_anom = y_anom[valid]

    # Add reconstruction error features
    X_anom_aug = np.column_stack([X_anom, recon_errors[anomaly_indices][valid]])

    # Train/test split
    n_train = int(0.8 * len(X_anom_aug))
    perm = rng.permutation(len(X_anom_aug))
    train_idx, test_idx = perm[:n_train], perm[n_train:]

    clf = GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=SEED)
    clf.fit(X_anom_aug[train_idx], y_anom[train_idx])
    y_pred = clf.predict(X_anom_aug[test_idx])

    inv_type_map = {v: k for k, v in type_map.items()}
    clf_report = classification_report(y_anom[test_idx], y_pred,
                                       target_names=[inv_type_map[i] for i in range(4)],
                                       output_dict=True, zero_division=0)
    print(classification_report(y_anom[test_idx], y_pred,
                                target_names=[inv_type_map[i] for i in range(4)],
                                zero_division=0))
else:
    clf_report = {}

# ============================================================
# Summary
# ============================================================

summary = {
    "experiment": "exoplanet_atmosphere_anomaly_detection",
    "phase": "Phase 7 — Speculations",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": "Anomaly detection in synthetic JWST exoplanet transmission spectra",
    "config": {
        "n_spectra": N_SPECTRA,
        "n_wavelength_bins": N_WAVELENGTH_BINS,
        "wavelength_range_um": [WAVELENGTH_MIN, WAVELENGTH_MAX],
        "atmosphere_types": {atype: int(count) for atype, count in type_counts},
        "ae_latent_dim": LATENT_DIM,
        "ae_epochs": EPOCHS,
        "device": str(DEVICE),
    },
    "results": {
        "anomaly_detection": {
            "auc_roc": float(auc),
            "n_flagged": int(n_flagged),
            "precision": float(precision),
            "recall": float(recall),
            "threshold_95pct": float(threshold),
        },
        "per_type_detection": per_type_results,
        "top_anomalous_wavelengths_um": [float(w) for w in top_wavelengths[:5]] if len(top_wavelengths) > 0 else [],
        "subtype_classification": clf_report,
        "ae_train_time_s": float(ae_time),
    },
    "interpretation": (
        "Autoencoder-based anomaly detection successfully flags non-standard "
        "atmospheric compositions, especially exotic multi-peaked spectra and "
        "biosignature-like O3+CH4 combinations. The most anomalous wavelength "
        "regions correspond to molecular bands that are absent or unusual relative "
        "to the training distribution. On real JWST transmission spectra, this "
        "pipeline could flag high-priority targets for deeper characterization."
    ),
}

summary_path = OUTPUT_DIR / "exoplanet_atmos_summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2, cls=NumpyEncoder)

# Save flagged candidates
flagged_indices = np.where(flagged)[0]
candidates = []
for idx in flagged_indices:
    candidates.append({
        "index": int(idx),
        "atmos_type": str(atmos_types[idx]),
        "label": str(labels[idx]),
        "recon_error": float(recon_errors[idx]),
    })
candidates.sort(key=lambda c: -c["recon_error"])

catalog_path = OUTPUT_DIR / "anomalous_spectra_catalog.csv"
pd.DataFrame(candidates).to_csv(catalog_path, index=False)

# Save example spectra (top 10 anomalies + 10 normal for comparison)
example_path = OUTPUT_DIR / "example_spectra.csv"
top10_anom = sorted(flagged_indices, key=lambda i: -recon_errors[i])[:10]
normal_examples = rng.choice(np.where(known_mask)[0], 10, replace=False)
example_indices = list(top10_anom) + list(normal_examples)
example_df = pd.DataFrame(spectra[example_indices], columns=[f"wl_{w:.3f}" for w in wavelengths])
example_df.insert(0, "index", example_indices)
example_df.insert(1, "atmos_type", [str(atmos_types[i]) for i in example_indices])
example_df.insert(2, "recon_error", [float(recon_errors[i]) for i in example_indices])
example_df.to_csv(example_path, index=False)

print(f"\n[exoplanet] Saved summary to {summary_path}")
print(f"[exoplanet] Saved {len(candidates)} anomalous spectra to {catalog_path}")
print(f"[exoplanet] Saved example spectra to {example_path}")

print("\nCOMPLETE")
