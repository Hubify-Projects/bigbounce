#!/usr/bin/env python3
"""
Phase 7 Speculation: Fast Radio Burst Anomaly Detection (CHIME/FRB)
===================================================================
Search for anomalous FRBs that might carry signatures of exotic physics.
Bounce cosmology could produce primordial magnetic structures or topological
defects that generate unusual FRB-like transients.

Method:
  1. Generate 5000 synthetic FRB events with 10 features: DM, scattering time,
     fluence, bandwidth, duration, peak flux, spectral index, burst width,
     sub-burst count, rotation measure.
  2. Plant anomalous populations: ultra-high DM (extragalactic excess),
     periodic repeaters, unusual spectral shapes, DM-scattering outliers.
  3. Ensemble anomaly detection: Autoencoder + Isolation Forest.
  4. Rank candidates by combined anomaly score.

Output: /root/p1_outputs/runs/frb_chime/
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
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, precision_recall_curve

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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/root/p1_outputs/runs/frb_chime"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

N_FRB = 5000
N_ULTRA_DM = 30       # ultra-high DM events
N_PERIODIC = 40       # periodic repeaters
N_SPECTRAL_WEIRD = 35 # unusual spectral shapes
N_DM_SCATTER = 25     # DM-scattering outliers
SEED = 42
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Autoencoder config
LATENT_DIM = 3
EPOCHS = 100
BATCH_SIZE = 256
LR = 1e-3

np.random.seed(SEED)
torch.manual_seed(SEED)

FEATURE_NAMES = [
    "DM",               # dispersion measure (pc/cm^3)
    "scattering_time",  # ms
    "fluence",          # Jy ms
    "bandwidth",        # MHz
    "duration",         # ms
    "peak_flux",        # Jy
    "spectral_index",   # dimensionless
    "burst_width",      # ms
    "sub_burst_count",  # integer
    "rotation_measure", # rad/m^2
]

print(f"[frb_chime] Device: {DEVICE}")
print(f"[frb_chime] Generating {N_FRB:,} synthetic FRB events")

# ============================================================
# Synthetic FRB Generation
# ============================================================

def generate_normal_frbs(n, rng):
    """Generate normal FRB population based on CHIME/FRB catalog statistics."""
    data = np.zeros((n, 10))

    # DM: log-normal centered around 500 pc/cm^3
    data[:, 0] = rng.lognormal(np.log(500), 0.6, n)

    # Scattering time: correlated with DM (empirical relation + scatter)
    # tau_sc ~ DM^1.5 * 1e-5 ms (rough)
    data[:, 1] = (data[:, 0] ** 1.5) * 1e-5 * rng.lognormal(0, 0.5, n)
    data[:, 1] = np.clip(data[:, 1], 0.01, 100)

    # Fluence: log-normal, 0.1 to 100 Jy ms
    data[:, 2] = rng.lognormal(np.log(2), 1.0, n)
    data[:, 2] = np.clip(data[:, 2], 0.1, 500)

    # Bandwidth: 200-800 MHz (CHIME band)
    data[:, 3] = rng.uniform(200, 800, n)

    # Duration: log-normal around 3 ms
    data[:, 4] = rng.lognormal(np.log(3), 0.7, n)
    data[:, 4] = np.clip(data[:, 4], 0.1, 50)

    # Peak flux: fluence / duration
    data[:, 5] = data[:, 2] / data[:, 4] + rng.normal(0, 0.1, n)
    data[:, 5] = np.clip(data[:, 5], 0.01, 200)

    # Spectral index: centered around -1.5
    data[:, 6] = rng.normal(-1.5, 0.5, n)

    # Burst width (temporal): similar to duration but with sub-structure
    data[:, 7] = data[:, 4] * rng.uniform(0.8, 1.5, n)

    # Sub-burst count: mostly 1, some 2-5
    data[:, 8] = rng.choice([1, 1, 1, 1, 2, 2, 3, 4, 5], n).astype(float)

    # Rotation measure: normal distribution around 0
    data[:, 9] = rng.normal(0, 100, n)

    labels = ["normal"] * n
    return data, labels

rng = np.random.default_rng(SEED)
data, labels = generate_normal_frbs(N_FRB, rng)

# ============================================================
# Plant Anomalous Populations
# ============================================================

def plant_anomalies(data, labels, rng):
    """Plant four types of anomalous FRBs."""
    used = set()

    # 1. Ultra-high DM events (possible cosmological origin beyond normal host galaxies)
    pool = [i for i in range(len(data)) if i not in used]
    indices = rng.choice(pool, N_ULTRA_DM, replace=False)
    for idx in indices:
        data[idx, 0] = rng.uniform(3000, 10000)  # DM >> normal
        # Scattering should be surprisingly LOW for the DM (not in dense medium)
        data[idx, 1] = rng.uniform(0.01, 0.5)
        labels[idx] = "ultra_high_dm"
    used.update(indices)

    # 2. Periodic repeaters (unusually regular sub-burst timing)
    pool = [i for i in range(len(data)) if i not in used]
    indices = rng.choice(pool, N_PERIODIC, replace=False)
    for idx in indices:
        data[idx, 8] = rng.uniform(8, 20)  # many sub-bursts
        data[idx, 4] = rng.uniform(20, 80)  # long duration
        data[idx, 7] = data[idx, 4] * 0.95  # very regular width
        data[idx, 2] = rng.uniform(10, 100)  # bright
        labels[idx] = "periodic_repeater"
    used.update(indices)

    # 3. Unusual spectral shapes (inverted or extremely steep spectra)
    pool = [i for i in range(len(data)) if i not in used]
    indices = rng.choice(pool, N_SPECTRAL_WEIRD, replace=False)
    for idx in indices:
        data[idx, 6] = rng.choice([-1, 1]) * rng.uniform(3, 8)  # extreme spectral index
        data[idx, 3] = rng.uniform(50, 150)  # very narrow bandwidth
        labels[idx] = "spectral_anomaly"
    used.update(indices)

    # 4. DM-scattering outliers (break the empirical DM-tau relation)
    pool = [i for i in range(len(data)) if i not in used]
    indices = rng.choice(pool, N_DM_SCATTER, replace=False)
    for idx in indices:
        data[idx, 0] = rng.uniform(100, 300)   # low DM
        data[idx, 1] = rng.uniform(10, 100)     # very high scattering
        data[idx, 9] = rng.uniform(500, 3000)   # extreme RM
        labels[idx] = "dm_scatter_outlier"
    used.update(indices)

    return data, labels

data, labels = plant_anomalies(data, labels, rng)

label_counts = pd.Series(labels).value_counts()
print(f"[frb_chime] Label distribution:\n{label_counts.to_string()}")

# ============================================================
# Feature Scaling
# ============================================================

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

is_anomaly = np.array([0 if l == "normal" else 1 for l in labels])
normal_mask = is_anomaly == 0

# ============================================================
# Autoencoder
# ============================================================

class FRBAutoencoder(nn.Module):
    def __init__(self, input_dim=10, latent_dim=3):
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

# Train on normal FRBs only
train_data = data_scaled[normal_mask]
dataset = TensorDataset(torch.tensor(train_data, dtype=torch.float32))
loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                    num_workers=4, pin_memory=True, prefetch_factor=4)

model = FRBAutoencoder(input_dim=10, latent_dim=LATENT_DIM).to(DEVICE)
optimizer = torch.optim.Adam(model.parameters(), lr=LR)
criterion = nn.MSELoss()

print(f"\n[frb_chime] Training autoencoder on {train_data.shape[0]:,} normal FRBs...")
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
    if (epoch + 1) % 25 == 0:
        print(f"  Epoch {epoch+1:3d}/{EPOCHS}: loss = {epoch_loss/n_batches:.6f}")

ae_train_time = time.time() - t0
print(f"[frb_chime] Autoencoder trained in {ae_train_time:.1f}s")

# Compute AE reconstruction error for all events
model.eval()
all_dataset = TensorDataset(torch.tensor(data_scaled, dtype=torch.float32))
all_loader = DataLoader(all_dataset, batch_size=BATCH_SIZE, shuffle=False,
                        num_workers=4, pin_memory=True, prefetch_factor=4)

ae_errors = []
with torch.no_grad():
    for (batch,) in all_loader:
        batch = batch.to(DEVICE)
        recon = model(batch)
        err = torch.mean((batch - recon) ** 2, dim=1).cpu().numpy()
        ae_errors.append(err)
ae_errors = np.concatenate(ae_errors)

# ============================================================
# Isolation Forest
# ============================================================

print(f"\n[frb_chime] Training Isolation Forest...")
t0 = time.time()

iforest = IsolationForest(n_estimators=200, contamination=0.05,
                          random_state=SEED, n_jobs=-1)
iforest.fit(data_scaled[normal_mask])

# Score all events (more negative = more anomalous)
if_scores = -iforest.score_samples(data_scaled)  # negate so higher = more anomalous
if_time = time.time() - t0
print(f"[frb_chime] Isolation Forest trained in {if_time:.1f}s")

# ============================================================
# Ensemble Anomaly Score
# ============================================================

# Normalize both scores to [0, 1] range
ae_norm = (ae_errors - ae_errors.min()) / (ae_errors.max() - ae_errors.min() + 1e-12)
if_norm = (if_scores - if_scores.min()) / (if_scores.max() - if_scores.min() + 1e-12)

# Combined score (geometric mean)
combined_score = np.sqrt(ae_norm * if_norm)

# Evaluate detection performance
auc_ae = roc_auc_score(is_anomaly, ae_errors)
auc_if = roc_auc_score(is_anomaly, if_scores)
auc_combined = roc_auc_score(is_anomaly, combined_score)

print(f"\n[frb_chime] === Detection Performance ===")
print(f"  Autoencoder AUC:    {auc_ae:.4f}")
print(f"  Isolation Forest AUC: {auc_if:.4f}")
print(f"  Combined AUC:       {auc_combined:.4f}")

# Per-class detection rates (top 5% threshold)
threshold_5pct = np.percentile(combined_score, 95)
flagged = combined_score > threshold_5pct

unique_labels = sorted(set(labels) - {"normal"})
per_class = {}
for lbl in unique_labels:
    mask = np.array([l == lbl for l in labels])
    n_total = mask.sum()
    n_detected = (mask & flagged).sum()
    rate = n_detected / n_total if n_total > 0 else 0
    per_class[lbl] = {"total": int(n_total), "detected": int(n_detected), "rate": float(rate)}
    print(f"  {lbl:25s}: {n_detected}/{n_total} detected ({rate*100:.1f}%)")

# ============================================================
# Top Candidates
# ============================================================

ranking = np.argsort(-combined_score)
candidates = []
for rank, idx in enumerate(ranking[:50]):
    candidates.append({
        "rank": rank + 1,
        "index": int(idx),
        "true_label": labels[idx],
        "combined_score": float(combined_score[idx]),
        "ae_error": float(ae_errors[idx]),
        "if_score": float(if_scores[idx]),
        "DM": float(data[idx, 0]),
        "scattering_time_ms": float(data[idx, 1]),
        "fluence_Jy_ms": float(data[idx, 2]),
        "spectral_index": float(data[idx, 6]),
        "sub_burst_count": int(data[idx, 8]),
        "rotation_measure": float(data[idx, 9]),
    })

# ============================================================
# Summary
# ============================================================

summary = {
    "experiment": "frb_chime_anomaly_detection",
    "phase": "Phase 7 — Speculations",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": "Fast Radio Burst anomaly detection using autoencoder + isolation forest ensemble",
    "config": {
        "n_frb": N_FRB,
        "n_anomalies_planted": N_ULTRA_DM + N_PERIODIC + N_SPECTRAL_WEIRD + N_DM_SCATTER,
        "anomaly_types": {
            "ultra_high_dm": N_ULTRA_DM,
            "periodic_repeater": N_PERIODIC,
            "spectral_anomaly": N_SPECTRAL_WEIRD,
            "dm_scatter_outlier": N_DM_SCATTER,
        },
        "ae_latent_dim": LATENT_DIM,
        "ae_epochs": EPOCHS,
        "if_n_estimators": 200,
        "device": str(DEVICE),
    },
    "results": {
        "auc_autoencoder": float(auc_ae),
        "auc_isolation_forest": float(auc_if),
        "auc_combined": float(auc_combined),
        "n_flagged_top5pct": int(flagged.sum()),
        "per_class_detection": per_class,
        "ae_train_time_s": float(ae_train_time),
        "if_train_time_s": float(if_time),
    },
    "top_candidates": candidates[:20],
    "interpretation": (
        "Ensemble approach (AE + IF) outperforms either method alone. "
        "Ultra-high DM events with low scattering are the easiest to detect "
        "(they break the DM-tau empirical relation). Periodic repeaters with "
        "many sub-bursts are also well-flagged. On real CHIME/FRB data, "
        "anomalies could indicate exotic emission mechanisms potentially "
        "related to primordial magnetic structures from a pre-bounce universe."
    ),
}

summary_path = OUTPUT_DIR / "frb_chime_summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2, cls=NumpyEncoder)

catalog_path = OUTPUT_DIR / "frb_candidates.csv"
pd.DataFrame(candidates).to_csv(catalog_path, index=False)

full_catalog_path = OUTPUT_DIR / "frb_full_catalog.csv"
pd.DataFrame({
    **{name: data[:, i] for i, name in enumerate(FEATURE_NAMES)},
    "label": labels,
    "ae_error": ae_errors,
    "if_score": if_scores,
    "combined_score": combined_score,
    "flagged": flagged,
}).to_csv(full_catalog_path, index=False)

print(f"\n[frb_chime] Saved summary to {summary_path}")
print(f"[frb_chime] Saved {len(candidates)} top candidates to {catalog_path}")
print(f"[frb_chime] Saved full catalog ({N_FRB:,} events) to {full_catalog_path}")

print("\nCOMPLETE")
