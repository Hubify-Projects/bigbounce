#!/usr/bin/env python3
"""
Experiment: Simulate Time-Domain Behavior of Anomaly Types

For each anomaly type discovered in the multi-survey sweep (ultra-soft X-ray,
extreme variable, high-z dropout, etc.), simulate expected light curves in
optical (g, r, i) and IR (W1, W2) bands using physically motivated models:
  - AGN: Damped Random Walk (DRW) with tau and SF_inf parameters
  - Supernovae: Template light curves (Ia, IIP, Ibc)
  - Stable sources: Constant + Gaussian noise
  - TDE: Power-law decay t^{-5/3}
  - Extreme variables: High-amplitude sinusoidal + stochastic

Generate 10K light curves, train a classifier to identify anomaly types from
time-series features, and predict detectability by ZTF/LSST/Roman.

Output: /workspace/bigbounce/outputs/anomaly-lightcurve-sim/
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

from scipy.interpolate import interp1d
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

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

OUTPUT_DIR = "/workspace/bigbounce/outputs/anomaly-lightcurve-sim"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

N_LIGHTCURVES = 10000
N_TIMESTEPS = 200  # observation epochs
T_SPAN_DAYS = 1500.0  # ~4 years of monitoring

BANDS = ['g', 'r', 'i', 'W1', 'W2']
N_BANDS = len(BANDS)

# Band-specific properties: central wavelength (A), typical depth (5-sigma, AB mag)
BAND_PROPS = {
    'g':  {'wave': 4770, 'depth_ztf': 20.8, 'depth_lsst': 25.0, 'depth_roman': 26.5},
    'r':  {'wave': 6231, 'depth_ztf': 20.6, 'depth_lsst': 24.7, 'depth_roman': 26.5},
    'i':  {'wave': 7625, 'depth_ztf': 19.9, 'depth_lsst': 24.0, 'depth_roman': 26.0},
    'W1': {'wave': 33526, 'depth_ztf': None, 'depth_lsst': None, 'depth_roman': None},
    'W2': {'wave': 46028, 'depth_ztf': None, 'depth_lsst': None, 'depth_roman': None},
}

# Anomaly types from the multi-survey sweep
ANOMALY_TYPES = [
    'agn_variable',
    'ultra_soft_xray',
    'high_z_dropout',
    'extreme_variable',
    'sn_transient',
    'tde_candidate',
    'stable_anomaly',
]
N_CLASSES = len(ANOMALY_TYPES)

# Training
BATCH_SIZE = 128
N_EPOCHS = 30
LR = 5e-4
NUM_WORKERS = 4

print("=" * 70)
print("EXPERIMENT: Anomaly Light Curve Simulation & Classification")
print(f"  Device: {DEVICE}")
print(f"  Light curves: {N_LIGHTCURVES}, Timesteps: {N_TIMESTEPS}")
print(f"  Bands: {BANDS}")
print(f"  Anomaly types: {N_CLASSES}")
print("=" * 70)

# ============================================================
# Light Curve Generation Models
# ============================================================

def damped_random_walk(t, tau, sf_inf, mag0, rng):
    """Simulate AGN variability using Damped Random Walk (Kelly+09)."""
    n = len(t)
    mag = np.zeros(n)
    mag[0] = mag0
    for i in range(1, n):
        dt = t[i] - t[i-1]
        decay = np.exp(-dt / tau)
        var = sf_inf**2 * (1 - np.exp(-2*dt/tau))
        mag[i] = mag[i-1] * decay + rng.normal(0, np.sqrt(max(var, 1e-10)))
    return mag + mag0

def sn_template(t, t_peak, peak_mag, sn_type, rng):
    """Simplified supernova template light curve."""
    dt = t - t_peak
    if sn_type == 'Ia':
        # Type Ia: fast rise, ~15 day decline rate
        rise = np.where(dt < 0, peak_mag + 2.5 * np.log10(1 + np.exp(-dt/5.0)), peak_mag)
        decline = np.where(dt >= 0, peak_mag + 1.0 * (dt / 30.0)**1.2, 0)
        mag = np.where(dt < 0, rise, decline)
    elif sn_type == 'IIP':
        # Type IIP: plateau phase
        rise = np.where(dt < 0, peak_mag + 3.0 * np.exp(dt/10.0), peak_mag)
        plateau = np.where((dt >= 0) & (dt < 80), peak_mag + 0.01 * dt, 0)
        tail = np.where(dt >= 80, peak_mag + 0.8 + 0.015 * (dt - 80), 0)
        mag = np.where(dt < 0, rise, np.where(dt < 80, plateau, tail))
    else:  # Ibc
        rise = np.where(dt < 0, peak_mag + 2.0 * np.exp(dt/8.0), peak_mag)
        decline = np.where(dt >= 0, peak_mag + 1.5 * (dt / 25.0)**1.1, 0)
        mag = np.where(dt < 0, rise, decline)
    # Add noise
    mag += rng.normal(0, 0.05, len(t))
    return mag

def tde_lightcurve(t, t_peak, peak_mag, rng):
    """TDE: power-law decay t^{-5/3} after peak."""
    dt = t - t_peak
    rise = np.where(dt < 0, peak_mag + 3.0 * (1 - np.exp(dt / 20.0)), peak_mag)
    # t^{-5/3} decay
    decay = np.where(dt > 0, peak_mag + 2.5 * np.log10(1 + (dt / 30.0)**(5.0/3.0)), 0)
    mag = np.where(dt < 0, rise, decay)
    mag += rng.normal(0, 0.03, len(t))
    return mag

def extreme_variable(t, period, amplitude, mag0, rng):
    """Large-amplitude periodic + stochastic variability."""
    phase = 2 * np.pi * t / period
    periodic = amplitude * np.sin(phase + rng.uniform(0, 2*np.pi))
    stochastic = rng.normal(0, amplitude * 0.3, len(t))
    return mag0 + periodic + stochastic

def generate_lightcurves():
    """Generate 10K multi-band light curves for all anomaly types."""
    print("\n[1/5] Generating synthetic light curves...")
    t0 = time.time()
    rng = np.random.default_rng(42)

    # Irregular time sampling (realistic cadence)
    t_base = np.sort(rng.uniform(0, T_SPAN_DAYS, N_TIMESTEPS))

    per_class = N_LIGHTCURVES // N_CLASSES
    remainder = N_LIGHTCURVES - per_class * N_CLASSES

    all_lcs = []  # (N, N_BANDS, N_TIMESTEPS)
    all_labels = []

    for cls_idx, atype in enumerate(ANOMALY_TYPES):
        n_this = per_class + (1 if cls_idx < remainder else 0)

        for _ in range(n_this):
            # Slightly perturbed time sampling per source
            t = t_base + rng.normal(0, 2.0, N_TIMESTEPS)
            t = np.sort(t)
            t = np.clip(t, 0, T_SPAN_DAYS)

            lc_bands = np.zeros((N_BANDS, N_TIMESTEPS), dtype=np.float32)
            mag0 = rng.uniform(18.0, 23.0)

            if atype == 'agn_variable':
                tau = rng.uniform(50, 500)
                sf_inf = rng.uniform(0.1, 0.5)
                for b in range(N_BANDS):
                    color_offset = (b - 1) * rng.uniform(0.1, 0.4)
                    lc_bands[b] = damped_random_walk(t, tau, sf_inf, mag0 + color_offset, rng)

            elif atype == 'ultra_soft_xray':
                # Optically quiet, slight variability
                for b in range(N_BANDS):
                    noise = rng.normal(0, 0.02 + 0.01 * b, N_TIMESTEPS)
                    lc_bands[b] = mag0 + 0.3 * b + noise

            elif atype == 'high_z_dropout':
                # Faint in blue, visible in red/IR; effectively constant
                for b in range(N_BANDS):
                    if b < 2:  # g, r: dropout (very faint)
                        lc_bands[b] = mag0 + 4.0 + rng.normal(0, 0.5, N_TIMESTEPS)
                    else:
                        lc_bands[b] = mag0 + 0.2 * b + rng.normal(0, 0.05, N_TIMESTEPS)

            elif atype == 'extreme_variable':
                period = rng.uniform(30, 500)
                amplitude = rng.uniform(1.0, 3.0)
                for b in range(N_BANDS):
                    lc_bands[b] = extreme_variable(t, period, amplitude * (1 - 0.1*b),
                                                   mag0 + 0.2*b, rng)

            elif atype == 'sn_transient':
                t_peak = rng.uniform(200, T_SPAN_DAYS - 200)
                peak_mag = rng.uniform(17, 21)
                sn_type = rng.choice(['Ia', 'IIP', 'Ibc'])
                for b in range(N_BANDS):
                    lc_bands[b] = sn_template(t, t_peak, peak_mag + 0.3*b, sn_type, rng)

            elif atype == 'tde_candidate':
                t_peak = rng.uniform(200, T_SPAN_DAYS - 200)
                peak_mag = rng.uniform(18, 22)
                for b in range(N_BANDS):
                    lc_bands[b] = tde_lightcurve(t, t_peak, peak_mag + 0.2*b, rng)

            elif atype == 'stable_anomaly':
                # Constant + noise (spectrally anomalous but photometrically stable)
                for b in range(N_BANDS):
                    lc_bands[b] = mag0 + 0.3*b + rng.normal(0, 0.03, N_TIMESTEPS)

            all_lcs.append(lc_bands)
            all_labels.append(cls_idx)

    all_lcs = np.array(all_lcs, dtype=np.float32)  # (N, N_BANDS, N_TIMESTEPS)
    all_labels = np.array(all_labels, dtype=np.int64)

    # Normalize: subtract mean, divide by std per light curve
    for i in range(all_lcs.shape[0]):
        for b in range(N_BANDS):
            mu = np.mean(all_lcs[i, b])
            std = np.std(all_lcs[i, b])
            if std > 1e-6:
                all_lcs[i, b] = (all_lcs[i, b] - mu) / std
            else:
                all_lcs[i, b] = all_lcs[i, b] - mu

    print(f"  Generated {N_LIGHTCURVES} light curves in {time.time() - t0:.1f}s")
    for cls_idx, atype in enumerate(ANOMALY_TYPES):
        n = int(np.sum(all_labels == cls_idx))
        print(f"    {atype}: {n}")

    return all_lcs, all_labels

# ============================================================
# PyTorch Dataset & DataLoader
# ============================================================

class LightCurveDataset(Dataset):
    def __init__(self, lcs, labels):
        self.lcs = torch.from_numpy(lcs)  # (N, N_BANDS, N_TIMESTEPS)
        self.labels = torch.from_numpy(labels)

    def __len__(self):
        return self.lcs.shape[0]

    def __getitem__(self, idx):
        return self.lcs[idx], self.labels[idx]

# ============================================================
# 1D CNN Classifier for Light Curves
# ============================================================

class LightCurveCNN(nn.Module):
    """Multi-band 1D CNN for light curve classification."""
    def __init__(self, n_bands=N_BANDS, n_timesteps=N_TIMESTEPS, n_classes=N_CLASSES):
        super().__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv1d(n_bands, 32, kernel_size=7, padding=3),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.MaxPool1d(2),  # -> 100

            nn.Conv1d(32, 64, kernel_size=5, padding=2),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.MaxPool1d(2),  # -> 50

            nn.Conv1d(64, 128, kernel_size=5, padding=2),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.MaxPool1d(2),  # -> 25

            nn.Conv1d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(8),  # -> 8
        )

        self.classifier = nn.Sequential(
            nn.Linear(256 * 8, 256),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, n_classes),
        )

    def forward(self, x):
        features = self.conv_layers(x)
        features = features.view(features.size(0), -1)
        return self.classifier(features)

# ============================================================
# Training
# ============================================================

def train_model(all_lcs, all_labels):
    print("\n[2/5] Training light curve classifier...")
    t0 = time.time()

    dataset = LightCurveDataset(all_lcs, all_labels)
    n_train = int(0.8 * len(dataset))
    n_val = len(dataset) - n_train
    train_ds, val_ds = random_split(dataset, [n_train, n_val],
                                     generator=torch.Generator().manual_seed(42))

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                              num_workers=NUM_WORKERS, pin_memory=True, prefetch_factor=4)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False,
                            num_workers=NUM_WORKERS, pin_memory=True, prefetch_factor=4)

    model = LightCurveCNN().to(DEVICE)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=N_EPOCHS)
    loss_fn = nn.CrossEntropyLoss()

    best_val_acc = 0.0
    history = []

    for epoch in range(N_EPOCHS):
        model.train()
        train_loss = 0.0
        train_correct = 0
        train_total = 0
        for lc_batch, lab_batch in train_loader:
            lc_batch = lc_batch.to(DEVICE, non_blocking=True)
            lab_batch = lab_batch.to(DEVICE, non_blocking=True)

            logits = model(lc_batch)
            loss = loss_fn(logits, lab_batch)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss += loss.item() * lc_batch.size(0)
            train_correct += (logits.argmax(dim=1) == lab_batch).sum().item()
            train_total += lc_batch.size(0)

        scheduler.step()

        # Validate
        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for lc_batch, lab_batch in val_loader:
                lc_batch = lc_batch.to(DEVICE, non_blocking=True)
                lab_batch = lab_batch.to(DEVICE, non_blocking=True)
                logits = model(lc_batch)
                loss = loss_fn(logits, lab_batch)
                val_loss += loss.item() * lc_batch.size(0)
                val_correct += (logits.argmax(dim=1) == lab_batch).sum().item()
                val_total += lc_batch.size(0)

        train_acc = train_correct / train_total
        val_acc = val_correct / val_total

        history.append({
            'epoch': epoch + 1,
            'train_loss': round(train_loss / train_total, 4),
            'train_acc': round(train_acc, 4),
            'val_loss': round(val_loss / val_total, 4),
            'val_acc': round(val_acc, 4),
        })

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), os.path.join(OUTPUT_DIR, "best_lc_model.pt"))

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  Epoch {epoch+1:3d}/{N_EPOCHS}: "
                  f"train_acc={train_acc:.4f} val_acc={val_acc:.4f} "
                  f"val_loss={val_loss/val_total:.4f}")

    print(f"  Training complete in {time.time() - t0:.1f}s")
    print(f"  Best val accuracy: {best_val_acc:.4f}")

    model.load_state_dict(torch.load(os.path.join(OUTPUT_DIR, "best_lc_model.pt"),
                                      weights_only=True))
    return model, val_ds, history

# ============================================================
# Evaluation
# ============================================================

def evaluate_model(model, val_ds):
    print("\n[3/5] Evaluating classifier...")
    model.eval()
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False,
                            num_workers=NUM_WORKERS, pin_memory=True, prefetch_factor=4)

    all_preds = []
    all_labels = []
    with torch.no_grad():
        for lc_batch, lab_batch in val_loader:
            lc_batch = lc_batch.to(DEVICE, non_blocking=True)
            logits = model(lc_batch)
            all_preds.append(logits.argmax(dim=1).cpu().numpy())
            all_labels.append(lab_batch.numpy())

    preds = np.concatenate(all_preds)
    labels = np.concatenate(all_labels)

    # Per-class metrics
    class_metrics = {}
    for cls_idx, atype in enumerate(ANOMALY_TYPES):
        mask_true = labels == cls_idx
        mask_pred = preds == cls_idx
        tp = int(np.sum(mask_true & mask_pred))
        fp = int(np.sum(~mask_true & mask_pred))
        fn = int(np.sum(mask_true & ~mask_pred))
        precision = tp / max(tp + fp, 1)
        recall = tp / max(tp + fn, 1)
        f1 = 2 * precision * recall / max(precision + recall, 1e-8)
        class_metrics[atype] = {
            'precision': round(precision, 4),
            'recall': round(recall, 4),
            'f1': round(f1, 4),
            'n_true': int(np.sum(mask_true)),
        }
        print(f"  {atype:20s}: P={precision:.3f} R={recall:.3f} F1={f1:.3f}")

    overall_acc = float(np.mean(preds == labels))
    print(f"  Overall accuracy: {overall_acc:.4f}")
    return class_metrics, overall_acc, preds, labels

# ============================================================
# Detectability Analysis
# ============================================================

def detectability_analysis(all_lcs, all_labels):
    """Predict which anomaly types are detectable by ZTF, LSST, Roman."""
    print("\n[4/5] Survey detectability analysis...")

    surveys = {
        'ZTF': {'bands': ['g', 'r', 'i'], 'cadence_days': 3, 'depth': [20.8, 20.6, 19.9]},
        'LSST': {'bands': ['g', 'r', 'i'], 'cadence_days': 3, 'depth': [25.0, 24.7, 24.0]},
        'Roman': {'bands': ['r', 'i'], 'cadence_days': 5, 'depth': [26.5, 26.0]},
    }

    # For detectability, we need un-normalized magnitudes.
    # Since we normalized, we use variability amplitude as a proxy.
    # A source is "variable-detectable" if its amplitude > photometric error floor.

    detectability = {}
    for survey_name, spec in surveys.items():
        band_indices = [BANDS.index(b) for b in spec['bands'] if b in BANDS]

        type_detect = {}
        for cls_idx, atype in enumerate(ANOMALY_TYPES):
            mask = all_labels == cls_idx
            lcs_cls = all_lcs[mask]

            # Compute variability amplitude in relevant bands
            amplitudes = []
            for i in range(lcs_cls.shape[0]):
                band_amps = []
                for b in band_indices:
                    amp = np.std(lcs_cls[i, b])
                    band_amps.append(amp)
                amplitudes.append(np.max(band_amps))
            amplitudes = np.array(amplitudes)

            # "Detectable" if amplitude > 0.3 (3x noise in normalized space)
            # and has temporal structure (not just noise)
            detectable_frac = float(np.mean(amplitudes > 0.3))
            type_detect[atype] = {
                'detectable_fraction': round(detectable_frac, 4),
                'mean_amplitude': round(float(np.mean(amplitudes)), 4),
                'median_amplitude': round(float(np.median(amplitudes)), 4),
            }

        detectability[survey_name] = type_detect
        print(f"\n  {survey_name}:")
        for atype, d in type_detect.items():
            print(f"    {atype:20s}: detectable={d['detectable_fraction']:.3f} "
                  f"amp={d['mean_amplitude']:.3f}")

    return detectability

# ============================================================
# Feature Extraction for Interpretability
# ============================================================

def extract_features(all_lcs, all_labels):
    """Extract interpretable time-series features."""
    print("\n[5/5] Extracting time-series features...")
    t0 = time.time()

    features = []
    for i in range(all_lcs.shape[0]):
        feat = {}
        for b, band_name in enumerate(BANDS):
            lc = all_lcs[i, b]
            feat[f'{band_name}_std'] = float(np.std(lc))
            feat[f'{band_name}_skew'] = float(
                np.mean(((lc - np.mean(lc)) / max(np.std(lc), 1e-8))**3)
            )
            feat[f'{band_name}_kurtosis'] = float(
                np.mean(((lc - np.mean(lc)) / max(np.std(lc), 1e-8))**4) - 3.0
            )
            # Amplitude ratio: max-min range
            feat[f'{band_name}_range'] = float(np.max(lc) - np.min(lc))
            # Autocorrelation at lag 1
            if len(lc) > 1:
                feat[f'{band_name}_autocorr1'] = float(np.corrcoef(lc[:-1], lc[1:])[0, 1])
            else:
                feat[f'{band_name}_autocorr1'] = 0.0
        feat['label'] = int(all_labels[i])
        feat['type'] = ANOMALY_TYPES[all_labels[i]]
        features.append(feat)

    df = pd.DataFrame(features)
    csv_path = os.path.join(OUTPUT_DIR, "lightcurve_features.csv")
    df.to_csv(csv_path, index=False)
    print(f"  Extracted {len(df.columns)-2} features for {len(df)} light curves")
    print(f"  Saved to {csv_path}")

    # Feature importance summary (mean per class)
    feat_cols = [c for c in df.columns if c not in ('label', 'type')]
    summary = {}
    for atype in ANOMALY_TYPES:
        sub = df[df['type'] == atype]
        summary[atype] = {col: round(float(sub[col].mean()), 4) for col in feat_cols[:10]}

    print(f"  Feature extraction complete in {time.time() - t0:.1f}s")
    return summary

# ============================================================
# Main
# ============================================================

def main():
    t_start = time.time()

    # Generate light curves
    all_lcs, all_labels = generate_lightcurves()

    # Train classifier
    model, val_ds, history = train_model(all_lcs, all_labels)

    # Evaluate
    class_metrics, overall_acc, preds, labels = evaluate_model(model, val_ds)

    # Detectability
    detectability = detectability_analysis(all_lcs, all_labels)

    # Feature extraction
    feature_summary = extract_features(all_lcs, all_labels)

    # Save summary
    elapsed = time.time() - t_start
    summary = {
        'experiment': 'anomaly_lightcurve_sim',
        'n_lightcurves': N_LIGHTCURVES,
        'n_timesteps': N_TIMESTEPS,
        'n_bands': N_BANDS,
        'bands': BANDS,
        'anomaly_types': ANOMALY_TYPES,
        'n_classes': N_CLASSES,
        'n_epochs': N_EPOCHS,
        'device': str(DEVICE),
        'training_history': history,
        'classification_metrics': class_metrics,
        'overall_accuracy': overall_acc,
        'survey_detectability': detectability,
        'feature_summary': feature_summary,
        'elapsed_seconds': round(elapsed, 1),
    }

    out_path = os.path.join(OUTPUT_DIR, "lightcurve_sim_summary.json")
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)
    print(f"\nSaved summary to {out_path}")

    hist_df = pd.DataFrame(history)
    hist_df.to_csv(os.path.join(OUTPUT_DIR, "training_history.csv"), index=False)

    print(f"\nTotal elapsed: {elapsed:.1f}s")
    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
