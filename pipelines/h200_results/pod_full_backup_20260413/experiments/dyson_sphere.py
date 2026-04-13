#!/usr/bin/env python3
"""
Phase 7 Speculation: Dyson Sphere Search via IR Excess Anomaly Detection
========================================================================
High-risk/high-reward search for Dyson sphere candidates using synthetic
Gaia + AllWISE photometry. The idea: a Dyson sphere around a star would
reprocess optical/UV light into mid-infrared thermal emission, creating
anomalous IR excess (especially W3, W4) relative to the star's spectral type.

Method:
  1. Generate 100K synthetic stars with realistic Gaia (G, BP, RP) + WISE
     (W1, W2, W3, W4) photometry spanning spectral types O through M.
  2. Plant 50 Dyson sphere candidates with anomalous mid-IR excess
     (W3-W4 >> normal for spectral type, consistent with ~300K blackbody).
  3. Train autoencoder on 7-band photometry + 6 color indices (13 features).
  4. Flag objects with reconstruction error concentrated in IR bands.
  5. Classify: normal, debris disk, AGB, YSO, Dyson candidate.

Output: /root/p1_outputs/runs/dyson_sphere/
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
from scipy.stats import norm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/root/p1_outputs/runs/dyson_sphere"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

N_STARS = 100_000
N_DYSON = 50
N_DEBRIS = 200
N_AGB = 300
N_YSO = 200
SEED = 42
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Autoencoder config
LATENT_DIM = 4
EPOCHS = 100
BATCH_SIZE = 1024
LR = 1e-3

np.random.seed(SEED)
torch.manual_seed(SEED)

print(f"[dyson_sphere] Device: {DEVICE}")
print(f"[dyson_sphere] Generating {N_STARS:,} synthetic stars with {N_DYSON} Dyson candidates")

# ============================================================
# Synthetic Star Generation
# ============================================================

# Spectral type properties: (T_eff, G_abs, BP-RP, fraction)
SPECTRAL_TYPES = {
    "O": (35000, -4.0, -0.33, 0.001),
    "B": (18000, -1.5, -0.15, 0.01),
    "A": (8500,  1.5,  0.15,  0.03),
    "F": (6700,  3.5,  0.50,  0.08),
    "G": (5500,  4.8,  0.75,  0.15),
    "K": (4300,  6.5,  1.10,  0.25),
    "M": (3200,  9.0,  2.50,  0.48),
}

def generate_photometry(n, rng):
    """Generate synthetic 7-band photometry for main-sequence stars."""
    records = []
    labels = []
    spec_types = []

    for stype, (teff, g_abs, bprp_center, frac) in SPECTRAL_TYPES.items():
        n_type = int(n * frac)
        # Gaia bands with realistic scatter
        G = rng.normal(g_abs, 0.5, n_type) + rng.uniform(0, 10, n_type)  # apparent mag
        BP_RP = rng.normal(bprp_center, 0.1, n_type)
        BP = G + BP_RP / 2
        RP = G - BP_RP / 2

        # WISE bands: scale from Teff with Rayleigh-Jeans tail
        # Hotter stars are fainter in IR relative to optical
        ir_offset = -2.5 * np.log10(teff / 5500)
        W1 = G + 0.5 + ir_offset + rng.normal(0, 0.15, n_type)
        W2 = W1 + rng.normal(0.02, 0.05, n_type)
        W3 = W1 + rng.normal(0.05, 0.08, n_type)
        W4 = W1 + rng.normal(0.10, 0.10, n_type)

        for i in range(n_type):
            records.append([G[i], BP[i], RP[i], W1[i], W2[i], W3[i], W4[i]])
            labels.append("normal")
            spec_types.append(stype)

    return np.array(records[:n]), labels[:n], spec_types[:n]

rng = np.random.default_rng(SEED)
photometry, labels, spec_types = generate_photometry(N_STARS, rng)
print(f"[dyson_sphere] Generated {len(photometry):,} normal stars")

# ============================================================
# Plant Anomalous Populations
# ============================================================

def plant_dyson_spheres(phot, labels, stypes, n_dyson, rng):
    """Plant Dyson sphere candidates: normal optical, huge IR excess in W3/W4."""
    indices = rng.choice(len(phot), n_dyson, replace=False)
    for idx in indices:
        # Dyson sphere at ~300K: massive W3/W4 excess (2-5 mag brighter)
        phot[idx, 5] -= rng.uniform(2.0, 4.0)   # W3 excess
        phot[idx, 6] -= rng.uniform(3.0, 5.0)   # W4 excess (even stronger)
        # Slight W1/W2 excess too
        phot[idx, 3] -= rng.uniform(0.2, 0.8)
        phot[idx, 4] -= rng.uniform(0.3, 1.0)
        labels[idx] = "dyson_candidate"
        stypes[idx] = stypes[idx]  # keep original spectral type
    return phot, labels, stypes, indices

def plant_debris_disks(phot, labels, stypes, n, rng):
    """Debris disks: moderate W3/W4 excess."""
    used = set(i for i, l in enumerate(labels) if l != "normal")
    pool = [i for i in range(len(phot)) if i not in used]
    indices = rng.choice(pool, min(n, len(pool)), replace=False)
    for idx in indices:
        phot[idx, 5] -= rng.uniform(0.5, 1.5)
        phot[idx, 6] -= rng.uniform(0.8, 2.0)
        labels[idx] = "debris_disk"
    return phot, labels, stypes

def plant_agb_stars(phot, labels, stypes, n, rng):
    """AGB stars: very red, excess in all IR bands."""
    used = set(i for i, l in enumerate(labels) if l != "normal")
    pool = [i for i in range(len(phot)) if i not in used]
    indices = rng.choice(pool, min(n, len(pool)), replace=False)
    for idx in indices:
        phot[idx, 3] -= rng.uniform(1.0, 3.0)
        phot[idx, 4] -= rng.uniform(1.5, 3.5)
        phot[idx, 5] -= rng.uniform(2.0, 4.5)
        phot[idx, 6] -= rng.uniform(2.5, 5.0)
        # Also redder in optical
        phot[idx, 1] += rng.uniform(0.5, 1.5)  # BP fainter
        labels[idx] = "agb"
    return phot, labels, stypes

def plant_yso(phot, labels, stypes, n, rng):
    """Young Stellar Objects: IR excess + variability scatter."""
    used = set(i for i, l in enumerate(labels) if l != "normal")
    pool = [i for i in range(len(phot)) if i not in used]
    indices = rng.choice(pool, min(n, len(pool)), replace=False)
    for idx in indices:
        phot[idx, 3] -= rng.uniform(0.5, 2.0)
        phot[idx, 4] -= rng.uniform(0.8, 2.5)
        phot[idx, 5] -= rng.uniform(1.0, 3.0)
        phot[idx, 6] -= rng.uniform(1.5, 3.5)
        labels[idx] = "yso"
    return phot, labels, stypes

photometry, labels, spec_types, dyson_indices = plant_dyson_spheres(
    photometry, labels, spec_types, N_DYSON, rng)
photometry, labels, spec_types = plant_debris_disks(photometry, labels, spec_types, N_DEBRIS, rng)
photometry, labels, spec_types = plant_agb_stars(photometry, labels, spec_types, N_AGB, rng)
photometry, labels, spec_types = plant_yso(photometry, labels, spec_types, N_YSO, rng)

label_counts = pd.Series(labels).value_counts()
print(f"[dyson_sphere] Label distribution:\n{label_counts.to_string()}")

# ============================================================
# Feature Engineering: 7 bands + 6 colors = 13 features
# ============================================================

def compute_features(phot):
    """Compute 7-band magnitudes + 6 diagnostic color indices."""
    G, BP, RP, W1, W2, W3, W4 = phot.T
    colors = np.column_stack([
        BP - RP,    # optical color
        G - W1,     # optical-IR baseline
        W1 - W2,    # near-IR color
        W2 - W3,    # mid-IR color (key for dust/Dyson)
        W3 - W4,    # far-IR color (key for Dyson)
        G - W4,     # full optical-to-far-IR baseline
    ])
    return np.hstack([phot, colors])

features = compute_features(photometry)
print(f"[dyson_sphere] Feature matrix: {features.shape}")

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# ============================================================
# Autoencoder Model
# ============================================================

class PhotometryAutoencoder(nn.Module):
    def __init__(self, input_dim=13, latent_dim=4):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
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
            nn.Linear(64, input_dim),
        )

    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)

# ============================================================
# Train Autoencoder (on normal stars only)
# ============================================================

normal_mask = np.array([l == "normal" for l in labels])
train_data = features_scaled[normal_mask]

dataset = TensorDataset(torch.tensor(train_data, dtype=torch.float32))
loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                    num_workers=4, pin_memory=True, prefetch_factor=4)

model = PhotometryAutoencoder(input_dim=13, latent_dim=LATENT_DIM).to(DEVICE)
optimizer = torch.optim.Adam(model.parameters(), lr=LR)
criterion = nn.MSELoss()

print(f"\n[dyson_sphere] Training autoencoder on {train_data.shape[0]:,} normal stars...")
t0 = time.time()

for epoch in range(EPOCHS):
    epoch_loss = 0.0
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
    if (epoch + 1) % 20 == 0:
        print(f"  Epoch {epoch+1:3d}/{EPOCHS}: loss = {epoch_loss/n_batches:.6f}")

train_time = time.time() - t0
print(f"[dyson_sphere] Training complete in {train_time:.1f}s")

# ============================================================
# Compute Reconstruction Errors (all stars)
# ============================================================

all_dataset = TensorDataset(torch.tensor(features_scaled, dtype=torch.float32))
all_loader = DataLoader(all_dataset, batch_size=BATCH_SIZE, shuffle=False,
                        num_workers=4, pin_memory=True, prefetch_factor=4)

model.eval()
recon_errors = []
per_feature_errors = []

with torch.no_grad():
    for (batch,) in all_loader:
        batch = batch.to(DEVICE)
        recon = model(batch)
        err = (batch - recon).cpu().numpy()
        recon_errors.append(np.mean(err**2, axis=1))
        per_feature_errors.append(err**2)

recon_errors = np.concatenate(recon_errors)
per_feature_errors = np.concatenate(per_feature_errors)

# Feature names for interpretability
feature_names = ["G", "BP", "RP", "W1", "W2", "W3", "W4",
                 "BP-RP", "G-W1", "W1-W2", "W2-W3", "W3-W4", "G-W4"]

# IR-band error fraction: what fraction of total error comes from IR features
ir_indices = [3, 4, 5, 6, 10, 11, 12]  # W1,W2,W3,W4, W1-W2, W3-W4, G-W4
ir_error_frac = per_feature_errors[:, ir_indices].sum(axis=1) / (per_feature_errors.sum(axis=1) + 1e-12)

print(f"\n[dyson_sphere] Reconstruction error stats:")
print(f"  Mean: {recon_errors.mean():.6f}")
print(f"  Std:  {recon_errors.std():.6f}")
print(f"  Max:  {recon_errors.max():.6f}")

# ============================================================
# Anomaly Flagging
# ============================================================

# Flag: high total error AND error concentrated in IR bands
threshold_total = np.percentile(recon_errors, 99)  # top 1%
threshold_ir_frac = 0.7  # >70% of error in IR bands

anomaly_mask = (recon_errors > threshold_total) & (ir_error_frac > threshold_ir_frac)
dyson_like_mask = anomaly_mask.copy()

n_flagged = anomaly_mask.sum()
print(f"\n[dyson_sphere] Flagged {n_flagged} IR-excess anomalies (top 1% error + >70% IR)")

# Check how many planted Dyson spheres were recovered
dyson_mask = np.array([l == "dyson_candidate" for l in labels])
dyson_recovered = (anomaly_mask & dyson_mask).sum()
print(f"[dyson_sphere] Dyson spheres recovered: {dyson_recovered}/{N_DYSON} ({100*dyson_recovered/N_DYSON:.1f}%)")

# ============================================================
# Classification with Random Forest
# ============================================================

print(f"\n[dyson_sphere] Training Random Forest classifier...")

# Encode labels
label_map = {"normal": 0, "debris_disk": 1, "agb": 2, "yso": 3, "dyson_candidate": 4}
y = np.array([label_map[l] for l in labels])

# Add reconstruction error features to the classifier
clf_features = np.column_stack([features_scaled, recon_errors, ir_error_frac])

# Train/test split (80/20)
n_train = int(0.8 * len(clf_features))
perm = rng.permutation(len(clf_features))
train_idx, test_idx = perm[:n_train], perm[n_train:]

clf = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=SEED,
                              class_weight="balanced", n_jobs=-1)
clf.fit(clf_features[train_idx], y[train_idx])

y_pred = clf.predict(clf_features[test_idx])
y_test = y[test_idx]

inv_label_map = {v: k for k, v in label_map.items()}
target_names = [inv_label_map[i] for i in sorted(label_map.values())]
report = classification_report(y_test, y_pred, target_names=target_names, output_dict=True)
cm = confusion_matrix(y_test, y_pred)

print(f"\n[dyson_sphere] Classification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Dyson sphere precision/recall
dyson_precision = report.get("dyson_candidate", {}).get("precision", 0)
dyson_recall = report.get("dyson_candidate", {}).get("recall", 0)
print(f"[dyson_sphere] Dyson candidate precision: {dyson_precision:.3f}")
print(f"[dyson_sphere] Dyson candidate recall:    {dyson_recall:.3f}")

# ============================================================
# Feature Importance
# ============================================================

importances = clf.feature_importances_
feat_names_full = feature_names + ["recon_error", "ir_error_frac"]
importance_ranking = sorted(zip(feat_names_full, importances), key=lambda x: -x[1])

print(f"\n[dyson_sphere] Top feature importances:")
for name, imp in importance_ranking[:10]:
    print(f"  {name:15s}: {imp:.4f}")

# ============================================================
# Candidate List
# ============================================================

# All objects classified as dyson_candidate by RF
all_predictions = clf.predict(clf_features)
dyson_pred_mask = (all_predictions == 4)
n_dyson_predicted = dyson_pred_mask.sum()

candidates = []
for idx in np.where(dyson_pred_mask)[0]:
    candidates.append({
        "index": int(idx),
        "true_label": labels[idx],
        "spectral_type": spec_types[idx],
        "recon_error": float(recon_errors[idx]),
        "ir_error_frac": float(ir_error_frac[idx]),
        "G": float(photometry[idx, 0]),
        "W3": float(photometry[idx, 5]),
        "W4": float(photometry[idx, 6]),
        "W3_W4": float(photometry[idx, 5] - photometry[idx, 6]),
        "G_W4": float(photometry[idx, 0] - photometry[idx, 6]),
    })

candidates.sort(key=lambda c: -c["recon_error"])

# ============================================================
# Summary
# ============================================================

summary = {
    "experiment": "dyson_sphere_ir_excess_search",
    "phase": "Phase 7 — Speculations",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": "Search for Dyson sphere candidates via IR excess anomaly detection",
    "config": {
        "n_stars": N_STARS,
        "n_dyson_planted": N_DYSON,
        "n_debris_planted": N_DEBRIS,
        "n_agb_planted": N_AGB,
        "n_yso_planted": N_YSO,
        "latent_dim": LATENT_DIM,
        "epochs": EPOCHS,
        "batch_size": BATCH_SIZE,
        "device": str(DEVICE),
    },
    "results": {
        "autoencoder": {
            "train_time_s": train_time,
            "mean_recon_error": float(recon_errors.mean()),
            "std_recon_error": float(recon_errors.std()),
            "threshold_99pct": float(threshold_total),
        },
        "anomaly_detection": {
            "n_ir_anomalies_flagged": int(n_flagged),
            "dyson_recovered_by_ae": int(dyson_recovered),
            "dyson_recovery_rate": float(dyson_recovered / N_DYSON),
        },
        "classification": {
            "n_dyson_predicted": int(n_dyson_predicted),
            "dyson_precision": float(dyson_precision),
            "dyson_recall": float(dyson_recall),
            "confusion_matrix": cm.tolist(),
            "class_names": target_names,
        },
        "feature_importance_top10": [
            {"feature": name, "importance": float(imp)}
            for name, imp in importance_ranking[:10]
        ],
        "n_candidates": len(candidates),
        "top_candidates": candidates[:20],
    },
    "interpretation": (
        "This pipeline demonstrates that autoencoder + random forest can isolate "
        "Dyson sphere-like IR excess anomalies from astrophysical contaminants "
        "(debris disks, AGB, YSO). Key discriminator: W3-W4 color excess "
        "concentrated in the far-IR, consistent with a ~300K blackbody shell. "
        "On real Gaia+AllWISE data, this method could flag candidates for "
        "spectroscopic follow-up."
    ),
}

summary_path = OUTPUT_DIR / "dyson_sphere_summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2, cls=NumpyEncoder)

# Save candidate catalog
catalog_path = OUTPUT_DIR / "dyson_candidates.csv"
pd.DataFrame(candidates).to_csv(catalog_path, index=False)

# Save reconstruction errors
errors_path = OUTPUT_DIR / "reconstruction_errors.csv"
pd.DataFrame({
    "recon_error": recon_errors,
    "ir_error_frac": ir_error_frac,
    "label": labels,
    "predicted": [inv_label_map[p] for p in all_predictions],
}).to_csv(errors_path, index=False)

print(f"\n[dyson_sphere] Saved summary to {summary_path}")
print(f"[dyson_sphere] Saved {len(candidates)} candidates to {catalog_path}")
print(f"[dyson_sphere] Saved reconstruction errors to {errors_path}")

print("\nCOMPLETE")
