#!/usr/bin/env python3
"""
Chandra CSC 2.1 X-ray Source Anomaly Detection — Phase 6
==========================================================
Downloads Chandra Source Catalog 2.1 data or generates 80K synthetic
X-ray sources with realistic property distributions.

Features: flux (soft/medium/hard bands), hardness ratios HR1/HR2,
extent, variability index, pile-up fraction.

Autoencoder anomaly detection + heuristic classification into:
ultra-soft, ultra-hard, extended transient, heavily absorbed.

Output: chandra_csc21_summary.json + chandra_csc21_anomalies.csv
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/chandra-csc21"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
N_SYNTHETIC = 80000
BATCH_SIZE = 512
EPOCHS = 40
LR = 1e-3
ANOMALY_PERCENTILE = 99
SEED = 42

np.random.seed(SEED)
torch.manual_seed(SEED)

# Chandra energy bands (keV)
# Soft: 0.5-1.2, Medium: 1.2-2.0, Hard: 2.0-7.0
FLUX_BANDS = ["flux_soft", "flux_medium", "flux_hard"]
FEATURE_COLS = [
    "log_flux_soft", "log_flux_medium", "log_flux_hard",
    "hr1", "hr2",
    "log_extent", "variability_index", "pileup_fraction",
]

# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

CSC_SEARCH_PATHS = [
    Path("/workspace/bigbounce/data/chandra"),
    Path("/workspace/bigbounce/outputs/chandra-csc21/catalog"),
    Path("/workspace/data/chandra"),
]


def try_download_csc(max_sources=10000):
    """Attempt to download CSC 2.1 data via CXC TAP."""
    print("[DATA] Attempting Chandra CSC 2.1 download...")
    try:
        import urllib.request
        url = (
            "https://cda.cfa.harvard.edu/csctap/sync?"
            "FORMAT=csv&LANG=ADQL&QUERY="
            f"SELECT+TOP+{max_sources}+name,ra,dec,"
            "flux_aper_b,flux_aper_s,flux_aper_m,flux_aper_h,"
            "hard_hm,hard_ms,extent_flag,var_flag+"
            "FROM+csc21.master_source"
        )
        tmp_file = OUTPUT_DIR / "csc_download.csv"
        urllib.request.urlretrieve(url, str(tmp_file))
        df = pd.read_csv(tmp_file)
        if len(df) > 100:
            print(f"  Retrieved {len(df)} CSC 2.1 sources")
            return df
    except Exception as e:
        print(f"  CSC download failed: {e}")
    return None


def load_local_catalog():
    """Check for locally cached Chandra data."""
    for search_path in CSC_SEARCH_PATHS:
        if not search_path.exists():
            continue
        for pattern in ["*.csv", "*.parquet", "*.fits"]:
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


def generate_synthetic_csc(n_sources=N_SYNTHETIC):
    """Generate synthetic Chandra-like X-ray source catalog."""
    print(f"[SYNTHETIC] Generating {n_sources} synthetic Chandra X-ray sources...")

    rows = []
    for i in range(n_sources):
        src_type = np.random.choice(
            ["normal_star", "xrb", "agn", "cluster", "snr", "anomaly"],
            p=[0.25, 0.20, 0.25, 0.10, 0.10, 0.10]
        )

        row = {"source_id": i, "type": src_type}

        if src_type == "normal_star":
            # Coronal emission: soft-dominated
            flux_soft = 10 ** np.random.uniform(-15, -13)
            flux_medium = flux_soft * 10 ** np.random.uniform(-1.0, 0.0)
            flux_hard = flux_soft * 10 ** np.random.uniform(-2.0, -0.5)
            extent = np.random.uniform(0, 1)  # point-like
            variability = np.random.uniform(0, 3)
            pileup = np.random.uniform(0, 0.05)

        elif src_type == "xrb":
            # X-ray binary: strong, variable, can be soft or hard
            state = np.random.choice(["soft_state", "hard_state"])
            base_flux = 10 ** np.random.uniform(-14, -11)
            if state == "soft_state":
                flux_soft = base_flux
                flux_medium = base_flux * 10 ** np.random.uniform(-0.5, 0.0)
                flux_hard = base_flux * 10 ** np.random.uniform(-1.5, -0.3)
            else:
                flux_hard = base_flux
                flux_medium = base_flux * 10 ** np.random.uniform(-0.5, 0.0)
                flux_soft = base_flux * 10 ** np.random.uniform(-1.5, -0.5)
            extent = np.random.uniform(0, 1)
            variability = np.random.uniform(2, 10)  # highly variable
            pileup = np.random.uniform(0, 0.3)

        elif src_type == "agn":
            # AGN: moderate hardness, low variability on short timescales
            base_flux = 10 ** np.random.uniform(-15, -12)
            nh = 10 ** np.random.uniform(20, 23)  # column density
            absorption_factor = np.exp(-nh / 1e22)
            flux_soft = base_flux * absorption_factor * np.random.lognormal(0, 0.3)
            flux_medium = base_flux * np.random.lognormal(0, 0.2)
            flux_hard = base_flux * np.random.lognormal(0, 0.2) * 1.5
            extent = np.random.uniform(0, 2)
            variability = np.random.uniform(0, 4)
            pileup = np.random.uniform(0, 0.1)

        elif src_type == "cluster":
            # Galaxy cluster: extended, soft thermal emission
            flux_soft = 10 ** np.random.uniform(-14, -12)
            flux_medium = flux_soft * 10 ** np.random.uniform(-0.5, 0.3)
            flux_hard = flux_soft * 10 ** np.random.uniform(-1.5, -0.3)
            extent = np.random.uniform(10, 120)  # very extended (arcsec)
            variability = np.random.uniform(0, 1)  # stable
            pileup = np.random.uniform(0, 0.02)

        elif src_type == "snr":
            # Supernova remnant: extended, can be soft or mixed
            flux_soft = 10 ** np.random.uniform(-14, -12)
            flux_medium = flux_soft * 10 ** np.random.uniform(-0.5, 0.5)
            flux_hard = flux_soft * 10 ** np.random.uniform(-1.0, 0.3)
            extent = np.random.uniform(5, 60)
            variability = np.random.uniform(0, 1)
            pileup = np.random.uniform(0, 0.02)

        else:  # anomaly
            anomaly_sub = np.random.choice([
                "ultra_soft", "ultra_hard", "extended_transient",
                "heavily_absorbed", "super_eddington", "tde_candidate"
            ])
            if anomaly_sub == "ultra_soft":
                flux_soft = 10 ** np.random.uniform(-13, -11)
                flux_medium = flux_soft * 10 ** np.random.uniform(-3, -1.5)
                flux_hard = flux_soft * 10 ** np.random.uniform(-5, -2)
                extent = np.random.uniform(0, 3)
                variability = np.random.uniform(1, 5)
                pileup = np.random.uniform(0, 0.15)
            elif anomaly_sub == "ultra_hard":
                flux_hard = 10 ** np.random.uniform(-13, -11)
                flux_medium = flux_hard * 10 ** np.random.uniform(-2, -0.5)
                flux_soft = flux_hard * 10 ** np.random.uniform(-4, -1.5)
                extent = np.random.uniform(0, 2)
                variability = np.random.uniform(0, 3)
                pileup = np.random.uniform(0, 0.2)
            elif anomaly_sub == "extended_transient":
                base_flux = 10 ** np.random.uniform(-13, -11)
                flux_soft = base_flux * np.random.lognormal(0, 0.5)
                flux_medium = base_flux * np.random.lognormal(0, 0.5)
                flux_hard = base_flux * np.random.lognormal(0, 0.5)
                extent = np.random.uniform(5, 30)  # extended
                variability = np.random.uniform(5, 15)  # very variable
                pileup = np.random.uniform(0, 0.1)
            elif anomaly_sub == "heavily_absorbed":
                intrinsic = 10 ** np.random.uniform(-12, -10)
                nh = 10 ** np.random.uniform(23, 25)
                flux_soft = intrinsic * np.exp(-nh / 5e21) + 1e-18
                flux_medium = intrinsic * np.exp(-nh / 5e22) * 0.5
                flux_hard = intrinsic * 0.8
                extent = np.random.uniform(0, 2)
                variability = np.random.uniform(0, 3)
                pileup = np.random.uniform(0, 0.05)
            elif anomaly_sub == "super_eddington":
                flux_soft = 10 ** np.random.uniform(-11, -9)
                flux_medium = flux_soft * 0.7
                flux_hard = flux_soft * 0.3
                extent = np.random.uniform(0, 1)
                variability = np.random.uniform(3, 10)
                pileup = np.random.uniform(0.2, 0.8)  # high pileup
            else:  # tde_candidate
                flux_soft = 10 ** np.random.uniform(-13, -11)
                flux_medium = flux_soft * 10 ** np.random.uniform(-1, 0)
                flux_hard = flux_soft * 10 ** np.random.uniform(-2, -0.5)
                extent = np.random.uniform(0, 2)
                variability = np.random.uniform(5, 20)  # extreme variability
                pileup = np.random.uniform(0, 0.15)

        # Add measurement noise
        for f_name in ["flux_soft", "flux_medium", "flux_hard"]:
            locals()[f_name] = eval(f_name) * np.random.lognormal(0, 0.05)

        flux_s = flux_soft
        flux_m = flux_medium
        flux_h = flux_hard

        # Hardness ratios: HR = (H - S) / (H + S)
        hr1 = (flux_m - flux_s) / (flux_m + flux_s + 1e-20)
        hr2 = (flux_h - flux_m) / (flux_h + flux_m + 1e-20)

        row["flux_soft"] = flux_s
        row["flux_medium"] = flux_m
        row["flux_hard"] = flux_h
        row["log_flux_soft"] = round(np.log10(max(flux_s, 1e-20)), 4)
        row["log_flux_medium"] = round(np.log10(max(flux_m, 1e-20)), 4)
        row["log_flux_hard"] = round(np.log10(max(flux_h, 1e-20)), 4)
        row["hr1"] = round(np.clip(hr1, -1, 1), 4)
        row["hr2"] = round(np.clip(hr2, -1, 1), 4)
        row["extent"] = round(extent, 3)
        row["log_extent"] = round(np.log10(max(extent, 0.1)), 4)
        row["variability_index"] = round(variability, 3)
        row["pileup_fraction"] = round(np.clip(pileup, 0, 1), 4)

        row["ra"] = round(np.random.uniform(0, 360), 5)
        row["dec"] = round(np.random.uniform(-90, 90), 5)
        rows.append(row)

        if (i + 1) % 20000 == 0:
            print(f"  Generated {i+1}/{n_sources} sources...")

    return pd.DataFrame(rows)


# ═══════════════════════════════════════════════════════
# Autoencoder
# ═══════════════════════════════════════════════════════

class ChandraAutoencoder(nn.Module):
    """MLP autoencoder for Chandra X-ray source features."""

    def __init__(self, input_dim=8, latent_dim=3):
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
    print(f"[TRAIN] Training Chandra autoencoder on {len(features_scaled)} sources, device={DEVICE}")

    tensor = torch.tensor(features_scaled, dtype=torch.float32)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                        num_workers=4, pin_memory=True, prefetch_factor=4,
                        drop_last=True)

    model = ChandraAutoencoder(input_dim=input_dim).to(DEVICE)
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

def classify_xray_anomalies(anomaly_df):
    """Apply heuristic classification to X-ray anomalies."""
    labels = []
    for _, row in anomaly_df.iterrows():
        hr1 = row.get("hr1", 0)
        hr2 = row.get("hr2", 0)
        extent = row.get("extent", 0)
        var_idx = row.get("variability_index", 0)
        pileup = row.get("pileup_fraction", 0)
        log_fs = row.get("log_flux_soft", -15)
        log_fh = row.get("log_flux_hard", -15)

        if hr1 < -0.6 and hr2 < -0.3:
            labels.append("ultra_soft")
        elif hr2 > 0.5 and hr1 > 0.2:
            labels.append("ultra_hard")
        elif extent > 10 and var_idx > 5:
            labels.append("extended_transient")
        elif log_fh - log_fs > 2 and hr2 > 0.3:
            labels.append("heavily_absorbed")
        elif pileup > 0.3:
            labels.append("pileup_dominated")
        elif var_idx > 8:
            labels.append("extreme_variable")
        elif extent > 30:
            labels.append("large_extended")
        elif log_fs > -11 or log_fh > -11:
            labels.append("super_luminous")
        else:
            labels.append("unclassified")

    anomaly_df["xray_class"] = labels
    return anomaly_df


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 70)
    print("Chandra CSC 2.1 X-ray Source Anomaly Detection — Phase 6")
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
        downloaded = try_download_csc()
        if downloaded is not None:
            data_source = "csc_download"
            catalog = downloaded
        else:
            catalog = generate_synthetic_csc()
            data_source = "fully_synthetic"

    available_features = [f for f in FEATURE_COLS if f in catalog.columns]
    print(f"[DATA] Source: {data_source}")
    print(f"[DATA] Sources: {len(catalog)}")
    print(f"[DATA] Features ({len(available_features)}): {available_features}")
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
    anomaly_df = classify_xray_anomalies(anomaly_df)
    anomaly_df.to_csv(OUTPUT_DIR / "chandra_csc21_anomalies.csv", index=False)

    # Classification breakdown
    class_counts = anomaly_df["xray_class"].value_counts().to_dict()
    type_counts = anomaly_df["type"].value_counts().to_dict() if "type" in anomaly_df.columns else {}

    # Top 20
    top_20 = []
    for rank, (_, row) in enumerate(anomaly_df.head(20).iterrows()):
        top_20.append({
            "rank": rank + 1,
            "source_id": int(row.get("source_id", 0)),
            "ra": float(row.get("ra", 0)),
            "dec": float(row.get("dec", 0)),
            "log_flux_soft": float(row.get("log_flux_soft", 0)),
            "log_flux_medium": float(row.get("log_flux_medium", 0)),
            "log_flux_hard": float(row.get("log_flux_hard", 0)),
            "hr1": float(row.get("hr1", 0)),
            "hr2": float(row.get("hr2", 0)),
            "extent": float(row.get("extent", 0)),
            "variability_index": float(row.get("variability_index", 0)),
            "pileup_fraction": float(row.get("pileup_fraction", 0)),
            "xray_class": str(row.get("xray_class", "unknown")),
            "recon_error": float(row.get("recon_error", 0)),
            "error_sigma": float(row.get("error_sigma", 0)),
        })

    elapsed = time.time() - t0
    summary = {
        "experiment": "chandra-csc21",
        "phase": 6,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": str(DEVICE),
        "data_source": data_source,
        "config": {
            "features": available_features,
            "n_features": len(available_features),
            "energy_bands_keV": {"soft": "0.5-1.2", "medium": "1.2-2.0", "hard": "2.0-7.0"},
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
            "xray_class_breakdown": class_counts,
            "source_type_breakdown": type_counts,
        },
        "top_20_anomalies": top_20,
        "training_losses": [float(l) for l in losses],
        "elapsed_seconds": round(elapsed, 1),
        "files_written": [
            "chandra_csc21_summary.json",
            "chandra_csc21_anomalies.csv",
            "best_model.pt",
        ],
    }

    with open(OUTPUT_DIR / "chandra_csc21_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"[DONE] {n_anomalies} anomalies from {len(features_scaled)} X-ray sources ({anomaly_rate:.2f}%)")
    print(f"[DONE] Classification: {class_counts}")
    print(f"[DONE] Elapsed: {elapsed:.1f}s")
    print(f"[DONE] Files: {OUTPUT_DIR}")
    print()
    print("COMPLETE")


if __name__ == "__main__":
    main()
