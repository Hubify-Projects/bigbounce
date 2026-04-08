#!/usr/bin/env python3
"""
ZTF DR21 Light Curve Anomaly Detection — Phase 6
==================================================
Downloads ZTF DR21 light curve data or generates 100K synthetic ZTF light
curves (g/r bands, 50-300 epochs each).

Features extracted per light curve:
  mean_mag, std_mag, skewness, kurtosis, period (Lomb-Scargle), amplitude,
  fraction_above_mean, median_absolute_deviation, von_neumann_ratio
  (computed per band, so 18 features total for g+r)

Autoencoder on feature vectors. Flags anomalous transients.

Output: ztf_dr21_summary.json + ztf_dr21_anomalies.csv
"""

import json
import os
import sys
import subprocess
import time
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path

# ═══════════════════════════════════════════════════════
# Install dependencies if needed
# ═══════════════════════════════════════════════════════
for pkg in ["torch", "scikit-learn"]:
    try:
        __import__(pkg.replace("-", ""))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", pkg])

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import RobustScaler
from scipy.signal import lombscargle
from scipy.stats import skew, kurtosis

# ═══════════════════════════════════════════════════════
# NumpyEncoder for JSON serialization
# ═══════════════════════════════════════════════════════

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super().default(obj)

# ═══════════════════════════════════════════════════════
# Config
# ═══════════════════════════════════════════════════════

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/root/p1_outputs/runs/ztf_dr2121"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
N_SYNTHETIC = 100000
BATCH_SIZE = 512
EPOCHS = 40
LR = 1e-3
ANOMALY_PERCENTILE = 99
SEED = 42

np.random.seed(SEED)
torch.manual_seed(SEED)

BANDS = ["g", "r"]
PER_BAND_FEATURES = [
    "mean_mag", "std_mag", "skewness", "kurtosis", "period",
    "amplitude", "frac_above_mean", "mad", "von_neumann_ratio",
]
FEATURE_COLS = [f"{feat}_{band}" for band in BANDS for feat in PER_BAND_FEATURES]
# 9 features x 2 bands = 18 features

# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

ZTF_SEARCH_PATHS = [
    Path("/workspace/bigbounce/data/ztf"),
    Path("/root/p1_outputs/runs/ztf_dr2121/catalog"),
    Path("/workspace/data/ztf"),
]


def try_download_ztf(max_sources=10000):
    """Attempt to download ZTF light curves via IRSA TAP."""
    print("[DATA] Attempting ZTF DR21 download via IRSA TAP...")
    try:
        import urllib.request
        url = (
            "https://irsa.ipac.caltech.edu/TAP/sync?"
            "FORMAT=csv&LANG=ADQL&QUERY="
            f"SELECT+TOP+{max_sources}+oid,filtercode,meanmag,rmsmagpsf,nobs,magrms,refmag+"
            "FROM+ztf.ztf_objects_dr21+"
            "WHERE+nobs>50+AND+filtercode+IN+(1,2)"
        )
        tmp_file = OUTPUT_DIR / "ztf_download.csv"
        urllib.request.urlretrieve(url, str(tmp_file))
        df = pd.read_csv(tmp_file)
        if len(df) > 100:
            print(f"  Retrieved {len(df)} ZTF objects")
            return df
    except Exception as e:
        print(f"  Download failed: {e}")
    return None


def load_local_catalog():
    """Check for locally cached ZTF data."""
    for search_path in ZTF_SEARCH_PATHS:
        if not search_path.exists():
            continue
        for pattern in ["*.csv", "*.parquet"]:
            files = sorted(search_path.glob(pattern))
            for f in files:
                try:
                    if f.suffix == ".csv":
                        df = pd.read_csv(f, nrows=N_SYNTHETIC + 5000)
                    elif f.suffix == ".parquet":
                        df = pd.read_parquet(f)
                    else:
                        continue
                    if len(df) > 100:
                        print(f"  Found local catalog: {f} ({len(df)} rows)")
                        return df
                except Exception as e:
                    print(f"  Error loading {f}: {e}")
    return None


def extract_lc_features(times, mags, magerrs=None):
    """Extract variability features from a single light curve."""
    n = len(times)
    mean_mag = np.mean(mags)
    std_mag = np.std(mags)
    sk = skew(mags) if n > 3 else 0.0
    kurt = kurtosis(mags) if n > 3 else 0.0
    amplitude = np.ptp(mags)
    frac_above = np.mean(mags > mean_mag)
    mad = np.median(np.abs(mags - np.median(mags)))

    # Von Neumann ratio: mean square successive difference / variance
    if std_mag > 1e-8 and n > 1:
        delta = np.diff(mags)
        von_neumann = np.mean(delta ** 2) / (std_mag ** 2)
    else:
        von_neumann = 2.0  # expected for white noise

    # Lomb-Scargle period
    try:
        if n > 10 and std_mag > 1e-8:
            dt = times - times.min()
            freqs = np.linspace(0.01, 10.0, 5000)  # 0.1-100 day periods
            power = lombscargle(dt, mags - mean_mag, freqs * 2 * np.pi, normalize=True)
            best_freq = freqs[np.argmax(power)]
            period = 1.0 / best_freq if best_freq > 0 else 0.0
        else:
            period = 0.0
    except Exception:
        period = 0.0

    return {
        "mean_mag": mean_mag,
        "std_mag": std_mag,
        "skewness": sk,
        "kurtosis": kurt,
        "period": period,
        "amplitude": amplitude,
        "frac_above_mean": frac_above,
        "mad": mad,
        "von_neumann_ratio": von_neumann,
    }


def generate_synthetic_ztf(n_sources=N_SYNTHETIC):
    """Generate synthetic ZTF-like light curve feature catalog."""
    print(f"[SYNTHETIC] Generating {n_sources} synthetic ZTF light curves...")

    rows = []
    for i in range(n_sources):
        src_type = np.random.choice(
            ["quiet_star", "rr_lyrae", "eclipsing_binary", "agn", "transient", "anomaly"],
            p=[0.40, 0.15, 0.15, 0.10, 0.10, 0.10]
        )

        n_epochs = np.random.randint(50, 301)
        # Generate observation times spanning ~1000 days with gaps
        times = np.sort(np.random.uniform(0, 1000, n_epochs))

        row = {"source_id": i, "type": src_type, "n_epochs": n_epochs}

        for band in BANDS:
            base_mag = np.random.uniform(14, 21) + (0.3 if band == "r" else 0.0)

            if src_type == "quiet_star":
                mags = base_mag + np.random.normal(0, 0.02, n_epochs)

            elif src_type == "rr_lyrae":
                period = np.random.uniform(0.2, 0.9)  # days
                amp = np.random.uniform(0.3, 1.5)
                phase = np.random.uniform(0, 2 * np.pi)
                mags = base_mag + amp * np.sin(2 * np.pi * times / period + phase)
                mags += np.random.normal(0, 0.05, n_epochs)

            elif src_type == "eclipsing_binary":
                period = np.random.uniform(0.5, 10.0)
                depth = np.random.uniform(0.1, 2.0)
                phase_fold = (times % period) / period
                eclipse_mask = (phase_fold < 0.05) | (phase_fold > 0.95)
                mags = np.full(n_epochs, base_mag) + np.random.normal(0, 0.03, n_epochs)
                mags[eclipse_mask] += depth

            elif src_type == "agn":
                # Damped random walk
                tau = np.random.uniform(50, 500)
                sf_inf = np.random.uniform(0.1, 0.5)
                mags = np.zeros(n_epochs)
                mags[0] = base_mag
                for j in range(1, n_epochs):
                    dt = times[j] - times[j - 1]
                    damp = np.exp(-dt / tau)
                    noise = sf_inf * np.sqrt(1 - damp ** 2) * np.random.randn()
                    mags[j] = base_mag + damp * (mags[j - 1] - base_mag) + noise
                mags += np.random.normal(0, 0.02, n_epochs)

            elif src_type == "transient":
                # Supernova-like: brightens then fades
                t_peak = np.random.uniform(200, 800)
                rise_time = np.random.uniform(10, 30)
                decay_time = np.random.uniform(30, 200)
                peak_amp = np.random.uniform(1.0, 5.0)
                dt = times - t_peak
                profile = np.where(dt < 0,
                                   peak_amp * np.exp(dt / rise_time),
                                   peak_amp * np.exp(-dt / decay_time))
                mags = base_mag - profile + np.random.normal(0, 0.05, n_epochs)

            else:  # anomaly
                anomaly_sub = np.random.choice([
                    "micro_lensing", "bizarre_periodic", "sudden_dropout",
                    "dual_period", "ultra_fast_transient"
                ])
                if anomaly_sub == "micro_lensing":
                    t0 = np.random.uniform(200, 800)
                    te = np.random.uniform(5, 50)
                    u0 = np.random.uniform(0.01, 0.3)
                    u = np.sqrt(u0 ** 2 + ((times - t0) / te) ** 2)
                    amp = (u ** 2 + 2) / (u * np.sqrt(u ** 2 + 4))
                    mags = base_mag - 2.5 * np.log10(amp) + np.random.normal(0, 0.03, n_epochs)
                elif anomaly_sub == "bizarre_periodic":
                    p1 = np.random.uniform(0.5, 5)
                    p2 = np.random.uniform(10, 100)
                    mags = (base_mag
                            + 0.5 * np.sin(2 * np.pi * times / p1)
                            + 0.8 * np.sin(2 * np.pi * times / p2)
                            + np.random.normal(0, 0.1, n_epochs))
                elif anomaly_sub == "sudden_dropout":
                    mags = base_mag + np.random.normal(0, 0.03, n_epochs)
                    dropout_start = np.random.randint(n_epochs // 3, 2 * n_epochs // 3)
                    dropout_len = np.random.randint(5, 30)
                    mags[dropout_start:dropout_start + dropout_len] += np.random.uniform(2, 5)
                elif anomaly_sub == "dual_period":
                    p1 = np.random.uniform(0.3, 1.0)
                    p2 = p1 * np.random.uniform(1.3, 2.7)
                    mags = (base_mag
                            + 0.6 * np.sin(2 * np.pi * times / p1)
                            + 0.6 * np.sin(2 * np.pi * times / p2)
                            + np.random.normal(0, 0.04, n_epochs))
                else:  # ultra_fast_transient
                    mags = base_mag + np.random.normal(0, 0.02, n_epochs)
                    burst_idx = np.random.randint(0, n_epochs - 3)
                    mags[burst_idx:burst_idx + 3] -= np.random.uniform(3, 8)

            features = extract_lc_features(times, mags)
            for feat_name, feat_val in features.items():
                row[f"{feat_name}_{band}"] = feat_val

        row["ra"] = np.random.uniform(0, 360)
        row["dec"] = np.random.uniform(-30, 90)
        rows.append(row)

        if (i + 1) % 20000 == 0:
            print(f"  Generated {i+1}/{n_sources} light curves...")

    return pd.DataFrame(rows)


# ═══════════════════════════════════════════════════════
# Autoencoder
# ═══════════════════════════════════════════════════════

class LightCurveAutoencoder(nn.Module):
    """MLP autoencoder for ZTF light curve features."""

    def __init__(self, input_dim=18, latent_dim=4):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.BatchNorm1d(64),
            nn.LeakyReLU(0.1),
            nn.Dropout(0.1),
            nn.Linear(64, 32),
            nn.BatchNorm1d(32),
            nn.LeakyReLU(0.1),
            nn.Linear(32, 16),
            nn.LeakyReLU(0.1),
            nn.Linear(16, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 16),
            nn.LeakyReLU(0.1),
            nn.Linear(16, 32),
            nn.BatchNorm1d(32),
            nn.LeakyReLU(0.1),
            nn.Linear(32, 64),
            nn.BatchNorm1d(64),
            nn.LeakyReLU(0.1),
            nn.Linear(64, input_dim),
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


# ═══════════════════════════════════════════════════════
# Training & Scoring
# ═══════════════════════════════════════════════════════

def train_and_score(features_scaled, input_dim):
    """Train autoencoder and return reconstruction errors."""
    print(f"[TRAIN] Training light curve autoencoder on {len(features_scaled)} sources, device={DEVICE}")

    tensor = torch.tensor(features_scaled, dtype=torch.float32)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                        num_workers=4, pin_memory=True, prefetch_factor=4,
                        drop_last=True)

    model = LightCurveAutoencoder(input_dim=input_dim).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=EPOCHS)
    criterion = nn.MSELoss()

    losses = []
    best_loss = float("inf")
    for epoch in range(EPOCHS):
        model.train()
        epoch_loss = 0.0
        n_batches = 0
        for (batch,) in loader:
            batch = batch.to(DEVICE, non_blocking=True)
            recon = model(batch)
            loss = criterion(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1
        avg_loss = epoch_loss / max(n_batches, 1)
        losses.append(avg_loss)
        scheduler.step()
        if avg_loss < best_loss:
            best_loss = avg_loss
            torch.save(model.state_dict(), OUTPUT_DIR / "best_model.pt")
        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  Epoch {epoch+1:3d}/{EPOCHS}  loss={avg_loss:.6f}  best={best_loss:.6f}")

    model.load_state_dict(torch.load(OUTPUT_DIR / "best_model.pt", weights_only=True))
    model.eval()

    score_loader = DataLoader(TensorDataset(tensor), batch_size=BATCH_SIZE,
                              shuffle=False, num_workers=4, pin_memory=True,
                              prefetch_factor=4)
    errors = []
    with torch.no_grad():
        for (batch,) in score_loader:
            batch = batch.to(DEVICE, non_blocking=True)
            recon = model(batch)
            err = ((batch - recon) ** 2).mean(dim=1)
            errors.append(err.cpu().numpy())

    return np.concatenate(errors), losses


# ═══════════════════════════════════════════════════════
# Classification Heuristics
# ═══════════════════════════════════════════════════════

def classify_lc_anomalies(anomaly_df):
    """Apply heuristic classification to light curve anomalies."""
    labels = []
    for _, row in anomaly_df.iterrows():
        std_g = row.get("std_mag_g", 0)
        std_r = row.get("std_mag_r", 0)
        vn_g = row.get("von_neumann_ratio_g", 2.0)
        vn_r = row.get("von_neumann_ratio_r", 2.0)
        period_g = row.get("period_g", 0)
        amp_g = row.get("amplitude_g", 0)
        amp_r = row.get("amplitude_r", 0)

        if amp_g > 3.0 or amp_r > 3.0:
            if vn_g < 0.5 or vn_r < 0.5:
                labels.append("transient_candidate")
            else:
                labels.append("high_amplitude_variable")
        elif vn_g < 0.3 and vn_r < 0.3:
            labels.append("correlated_variability")
        elif 0.1 < period_g < 1.0 and amp_g > 0.3:
            labels.append("short_period_variable")
        elif period_g > 50 and std_g > 0.2:
            labels.append("long_period_variable")
        elif abs(std_g - std_r) > 0.3:
            labels.append("color_variable")
        elif std_g > 0.5 and vn_g > 3.0:
            labels.append("stochastic_outlier")
        else:
            labels.append("unclassified")

    anomaly_df["lc_class"] = labels
    return anomaly_df


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 70)
    print("ZTF DR21 Light Curve Anomaly Detection — Phase 6")
    print("=" * 70)
    print(f"Output: {OUTPUT_DIR}")
    print(f"Device: {DEVICE}")
    print()

    # Step 1: Load or generate data
    data_source = "unknown"
    catalog = load_local_catalog()

    if catalog is not None:
        data_source = "local_cache"
    else:
        downloaded = try_download_ztf()
        if downloaded is not None:
            data_source = "irsa_download"
            catalog = downloaded
        else:
            catalog = generate_synthetic_ztf()
            data_source = "fully_synthetic"

    available_features = [f for f in FEATURE_COLS if f in catalog.columns]
    print(f"[DATA] Source: {data_source}")
    print(f"[DATA] Sources: {len(catalog)}")
    print(f"[DATA] Features ({len(available_features)}): {available_features[:6]}...")
    print()

    # Step 2: Prepare feature matrix
    feature_matrix = catalog[available_features].values.astype(np.float32)
    valid_mask = ~np.isnan(feature_matrix).any(axis=1) & ~np.isinf(feature_matrix).any(axis=1)
    feature_matrix = feature_matrix[valid_mask]
    catalog_valid = catalog[valid_mask].reset_index(drop=True)

    print(f"[DATA] Valid sources after filtering: {len(feature_matrix)}")

    # Step 3: Scale
    scaler = RobustScaler()
    features_scaled = scaler.fit_transform(feature_matrix)

    # Step 4: Train and score
    errors, losses = train_and_score(features_scaled, input_dim=len(available_features))
    print()

    # Step 5: Anomaly detection
    threshold = np.percentile(errors, ANOMALY_PERCENTILE)
    anomaly_mask = errors >= threshold
    n_anomalies = int(anomaly_mask.sum())
    anomaly_rate = n_anomalies / len(features_scaled) * 100

    print(f"[ANOMALY] Threshold (p{ANOMALY_PERCENTILE}): {threshold:.6f}")
    print(f"[ANOMALY] Anomalies: {n_anomalies} / {len(features_scaled)} ({anomaly_rate:.2f}%)")
    print()

    # Step 6: Classify and save
    anomaly_df = catalog_valid[anomaly_mask].copy()
    anomaly_df["recon_error"] = errors[anomaly_mask]
    anomaly_df["error_sigma"] = (errors[anomaly_mask] - errors.mean()) / errors.std()
    anomaly_df = anomaly_df.sort_values("recon_error", ascending=False)
    anomaly_df = classify_lc_anomalies(anomaly_df)
    anomaly_df.to_csv(OUTPUT_DIR / "ztf_dr21_anomalies.csv", index=False)

    # Classification breakdown
    class_counts = anomaly_df["lc_class"].value_counts().to_dict()
    type_counts = anomaly_df["type"].value_counts().to_dict() if "type" in anomaly_df.columns else {}

    # Top 20
    top_20 = []
    for rank, (_, row) in enumerate(anomaly_df.head(20).iterrows()):
        top_20.append({
            "rank": rank + 1,
            "source_id": int(row.get("source_id", 0)),
            "ra": float(row.get("ra", 0)),
            "dec": float(row.get("dec", 0)),
            "mean_mag_g": float(row.get("mean_mag_g", 0)),
            "mean_mag_r": float(row.get("mean_mag_r", 0)),
            "amplitude_g": float(row.get("amplitude_g", 0)),
            "period_g": float(row.get("period_g", 0)),
            "von_neumann_ratio_g": float(row.get("von_neumann_ratio_g", 0)),
            "lc_class": str(row.get("lc_class", "unknown")),
            "recon_error": float(row.get("recon_error", 0)),
            "error_sigma": float(row.get("error_sigma", 0)),
        })

    elapsed = time.time() - t0
    summary = {
        "experiment": "ztf-dr21",
        "phase": 6,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": str(DEVICE),
        "data_source": data_source,
        "config": {
            "features": available_features,
            "n_features": len(available_features),
            "bands": BANDS,
            "batch_size": BATCH_SIZE,
            "epochs": EPOCHS,
            "learning_rate": LR,
            "anomaly_percentile": ANOMALY_PERCENTILE,
        },
        "results": {
            "total_sources_scored": len(features_scaled),
            "anomaly_count": n_anomalies,
            "anomaly_rate_pct": round(anomaly_rate, 4),
            "recon_error_threshold": float(threshold),
            "recon_error_mean": float(errors.mean()),
            "recon_error_std": float(errors.std()),
            "final_train_loss": float(losses[-1]),
            "best_train_loss": float(min(losses)),
            "lc_class_breakdown": class_counts,
            "source_type_breakdown": type_counts,
        },
        "top_20_anomalies": top_20,
        "training_losses": [float(l) for l in losses],
        "elapsed_seconds": round(elapsed, 1),
        "files_written": [
            "ztf_dr21_summary.json",
            "ztf_dr21_anomalies.csv",
            "best_model.pt",
        ],
    }

    with open(OUTPUT_DIR / "ztf_dr21_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"[DONE] {n_anomalies} anomalies from {len(features_scaled)} light curves ({anomaly_rate:.2f}%)")
    print(f"[DONE] Classification: {class_counts}")
    print(f"[DONE] Elapsed: {elapsed:.1f}s")
    print(f"[DONE] Files: {OUTPUT_DIR}")
    print()
    print("COMPLETE")


if __name__ == "__main__":
    main()
