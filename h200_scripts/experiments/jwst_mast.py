#!/usr/bin/env python3
"""
JWST MAST Archive NIRCam+NIRSpec Anomaly Scan — Phase 6
=========================================================
Downloads JWST photometric/spectroscopic data from MAST archive,
or generates 50K synthetic JWST-like spectral/photometric data.

Features: NIRCam bands (F115W, F150W, F200W, F277W, F356W, F444W),
NIRSpec spectral features (line EW, continuum slope, break strength),
colors, and photometric redshift estimate.

Autoencoder anomaly detection. Flags unusual high-z candidates,
peculiar SEDs, dropout objects, and spectral anomalies.

Output: jwst_mast_summary.json + jwst_mast_anomalies.csv
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/jwst-mast"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
N_SYNTHETIC = 50000
BATCH_SIZE = 512
EPOCHS = 40
LR = 1e-3
ANOMALY_PERCENTILE = 99
SEED = 42

np.random.seed(SEED)
torch.manual_seed(SEED)

# NIRCam broadband filters (wavelength in microns)
NIRCAM_BANDS = ["F115W", "F150W", "F200W", "F277W", "F356W", "F444W"]
NIRCAM_WAVELENGTHS = [1.15, 1.50, 2.00, 2.77, 3.56, 4.44]  # microns

# NIRSpec-derived features
NIRSPEC_FEATURES = [
    "lya_ew",           # Lyman-alpha equivalent width
    "continuum_slope",  # UV continuum slope beta
    "balmer_break",     # Balmer break strength (D4000-like)
    "oiii_ew",          # [OIII] 5007 equivalent width
    "ha_ew",            # H-alpha equivalent width
]

# Colors
COLOR_FEATURES = [
    "F115W_F150W", "F150W_F200W", "F200W_F277W",
    "F277W_F356W", "F356W_F444W",
]

# All features
FEATURE_COLS = (
    [f"mag_{b}" for b in NIRCAM_BANDS]
    + COLOR_FEATURES
    + NIRSPEC_FEATURES
    + ["photo_z"]
)
# 6 mags + 5 colors + 5 spectral + 1 photo_z = 17 features

# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

JWST_SEARCH_PATHS = [
    Path("/workspace/bigbounce/data/jwst"),
    Path("/workspace/bigbounce/outputs/jwst-mast/catalog"),
    Path("/workspace/data/jwst"),
]


def try_download_jwst(max_sources=5000):
    """Attempt to download JWST catalog data from MAST."""
    print("[DATA] Attempting JWST MAST catalog download...")
    try:
        import urllib.request
        # MAST CAOM TAP query for JWST NIRCam observations
        url = (
            "https://mast.stsci.edu/vo/tap/sync?"
            "FORMAT=csv&LANG=ADQL&QUERY="
            f"SELECT+TOP+{max_sources}+target_name,s_ra,s_dec,t_min,t_exptime,"
            "instrument_name,filters,calib_level+"
            "FROM+obscore+"
            "WHERE+obs_collection='JWST'+AND+instrument_name='NIRCAM'"
        )
        tmp_file = OUTPUT_DIR / "jwst_download.csv"
        urllib.request.urlretrieve(url, str(tmp_file))
        df = pd.read_csv(tmp_file)
        if len(df) > 50:
            print(f"  Retrieved {len(df)} JWST observations")
            return df
    except Exception as e:
        print(f"  MAST download failed: {e}")
    return None


def load_local_catalog():
    """Check for locally cached JWST data."""
    for search_path in JWST_SEARCH_PATHS:
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
                    if len(df) > 50:
                        print(f"  Found local catalog: {f} ({len(df)} rows)")
                        return df
                except Exception as e:
                    print(f"  Error loading {f}: {e}")
    return None


def generate_synthetic_jwst(n_sources=N_SYNTHETIC):
    """Generate synthetic JWST-like photometric+spectroscopic catalog."""
    print(f"[SYNTHETIC] Generating {n_sources} synthetic JWST sources...")

    rows = []
    for i in range(n_sources):
        src_type = np.random.choice(
            ["low_z_galaxy", "high_z_galaxy", "star", "agn", "dropout", "anomaly"],
            p=[0.30, 0.25, 0.15, 0.12, 0.08, 0.10]
        )

        row = {"source_id": i, "type": src_type}

        if src_type == "low_z_galaxy":
            z = np.random.uniform(0.1, 2.0)
            # Typical galaxy SED: red continuum
            base_mag = np.random.uniform(22, 27)
            slope = np.random.uniform(-0.3, 0.5)  # AB mag per micron
            mags = [base_mag + slope * (wl - 2.0) + np.random.normal(0, 0.1)
                    for wl in NIRCAM_WAVELENGTHS]
            lya_ew = max(0, np.random.normal(5, 10))
            beta = np.random.uniform(-2.0, 0.0)
            balmer = np.random.uniform(1.0, 2.0)
            oiii_ew = max(0, np.random.normal(50, 30))
            ha_ew = max(0, np.random.normal(100, 50))

        elif src_type == "high_z_galaxy":
            z = np.random.uniform(4, 12)
            base_mag = np.random.uniform(25, 30)
            # Lyman break: bands blueward of Ly-alpha are faint
            lya_wl = 0.1216 * (1 + z)  # microns
            mags = []
            for wl in NIRCAM_WAVELENGTHS:
                if wl < lya_wl:
                    mags.append(base_mag + np.random.uniform(2, 5))  # dropout
                else:
                    mags.append(base_mag + np.random.normal(0, 0.15))
            lya_ew = max(0, np.random.exponential(30))
            beta = np.random.uniform(-2.5, -1.0)
            balmer = np.random.uniform(0.5, 1.5)
            oiii_ew = max(0, np.random.exponential(200))
            ha_ew = max(0, np.random.exponential(100))

        elif src_type == "star":
            z = 0.0
            # Power-law SED
            temp_factor = np.random.uniform(-1, 1)
            base_mag = np.random.uniform(18, 26)
            mags = [base_mag + temp_factor * (wl - 2.0) + np.random.normal(0, 0.03)
                    for wl in NIRCAM_WAVELENGTHS]
            lya_ew = 0.0
            beta = temp_factor * 2
            balmer = np.random.uniform(0.8, 3.0)
            oiii_ew = 0.0
            ha_ew = max(0, np.random.normal(5, 3))

        elif src_type == "agn":
            z = np.random.uniform(0.5, 6.0)
            base_mag = np.random.uniform(20, 27)
            # Flat-ish SED with possible emission
            slope = np.random.uniform(-0.5, 0.3)
            mags = [base_mag + slope * (wl - 2.0) + np.random.normal(0, 0.15)
                    for wl in NIRCAM_WAVELENGTHS]
            lya_ew = max(0, np.random.exponential(50))
            beta = np.random.uniform(-1.5, 0.5)
            balmer = np.random.uniform(0.8, 1.5)
            oiii_ew = max(0, np.random.exponential(100))
            ha_ew = max(0, np.random.exponential(80))

        elif src_type == "dropout":
            z = np.random.uniform(6, 15)
            base_mag = np.random.uniform(26, 31)
            lya_wl = 0.1216 * (1 + z)
            mags = []
            for wl in NIRCAM_WAVELENGTHS:
                if wl < lya_wl * 0.95:
                    mags.append(99.0)  # non-detection
                elif wl < lya_wl * 1.1:
                    mags.append(base_mag + np.random.uniform(1, 3))
                else:
                    mags.append(base_mag + np.random.normal(0, 0.2))
            lya_ew = max(0, np.random.exponential(50))
            beta = np.random.uniform(-3.0, -1.5)
            balmer = np.random.uniform(0.3, 1.0)
            oiii_ew = max(0, np.random.exponential(300))
            ha_ew = 0.0  # often redshifted out of range

        else:  # anomaly
            z = np.random.uniform(0, 15)
            anomaly_sub = np.random.choice([
                "extremely_red", "blue_excess", "inverted_sed",
                "double_break", "emission_dominated"
            ])
            base_mag = np.random.uniform(23, 29)
            if anomaly_sub == "extremely_red":
                mags = [base_mag + 1.5 * (wl - 1.0) + np.random.normal(0, 0.1)
                        for wl in NIRCAM_WAVELENGTHS]
                beta = np.random.uniform(0.5, 3.0)
            elif anomaly_sub == "blue_excess":
                mags = [base_mag - 0.8 * (wl - 1.0) + np.random.normal(0, 0.1)
                        for wl in NIRCAM_WAVELENGTHS]
                beta = np.random.uniform(-4.0, -2.5)
            elif anomaly_sub == "inverted_sed":
                mags = [base_mag + np.random.choice([-1, 1]) * np.random.uniform(0.5, 2)
                        for wl in NIRCAM_WAVELENGTHS]
                beta = np.random.uniform(-3, 3)
            elif anomaly_sub == "double_break":
                mags = []
                for j, wl in enumerate(NIRCAM_WAVELENGTHS):
                    if j < 2:
                        mags.append(base_mag + np.random.uniform(2, 4))
                    elif j < 4:
                        mags.append(base_mag + np.random.normal(0, 0.1))
                    else:
                        mags.append(base_mag + np.random.uniform(1, 3))
                beta = np.random.uniform(-2, 0)
            else:  # emission_dominated
                mags = [base_mag + np.random.normal(0, 0.1) for _ in NIRCAM_WAVELENGTHS]
                # One band much brighter due to emission line
                bright_band = np.random.randint(0, 6)
                mags[bright_band] -= np.random.uniform(1.5, 4.0)
                beta = np.random.uniform(-2, 0)

            lya_ew = max(0, np.random.exponential(100))
            balmer = np.random.uniform(0.2, 4.0)
            oiii_ew = max(0, np.random.exponential(200))
            ha_ew = max(0, np.random.exponential(150))

        # Store magnitudes
        for j, band in enumerate(NIRCAM_BANDS):
            row[f"mag_{band}"] = round(mags[j], 3)

        # Colors
        for j in range(len(NIRCAM_BANDS) - 1):
            cname = COLOR_FEATURES[j]
            row[cname] = round(mags[j] - mags[j + 1], 4)

        # NIRSpec features
        row["lya_ew"] = round(lya_ew, 2)
        row["continuum_slope"] = round(beta, 3)
        row["balmer_break"] = round(balmer, 3)
        row["oiii_ew"] = round(oiii_ew, 2)
        row["ha_ew"] = round(ha_ew, 2)
        row["photo_z"] = round(z, 3)

        row["ra"] = round(np.random.uniform(0, 360), 5)
        row["dec"] = round(np.random.uniform(-90, 90), 5)
        rows.append(row)

        if (i + 1) % 10000 == 0:
            print(f"  Generated {i+1}/{n_sources} sources...")

    return pd.DataFrame(rows)


# ═══════════════════════════════════════════════════════
# Autoencoder
# ═══════════════════════════════════════════════════════

class JWSTAutoencoder(nn.Module):
    """MLP autoencoder for JWST photometric+spectroscopic features."""

    def __init__(self, input_dim=17, latent_dim=4):
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
    print(f"[TRAIN] Training JWST autoencoder on {len(features_scaled)} sources, device={DEVICE}")

    tensor = torch.tensor(features_scaled, dtype=torch.float32)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                        num_workers=4, pin_memory=True, prefetch_factor=4,
                        drop_last=True)

    model = JWSTAutoencoder(input_dim=input_dim).to(DEVICE)
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

def classify_jwst_anomalies(anomaly_df):
    """Apply heuristic classification to JWST anomalies."""
    labels = []
    for _, row in anomaly_df.iterrows():
        photo_z = row.get("photo_z", 0)
        beta = row.get("continuum_slope", -1.5)
        lya = row.get("lya_ew", 0)
        oiii = row.get("oiii_ew", 0)
        f115w = row.get("mag_F115W", 27)
        f444w = row.get("mag_F444W", 27)
        color_15_44 = f115w - f444w if f115w < 90 and f444w < 90 else 0

        if f115w > 90 or (f115w > 30 and f444w < 28):
            labels.append("high_z_dropout_candidate")
        elif photo_z > 8:
            labels.append("ultra_high_z_candidate")
        elif beta > 0.5:
            labels.append("extremely_red_object")
        elif beta < -2.5:
            labels.append("blue_excess_source")
        elif oiii > 400 or lya > 150:
            labels.append("extreme_emission_line")
        elif color_15_44 > 3:
            labels.append("red_SED_anomaly")
        elif color_15_44 < -2:
            labels.append("inverted_SED")
        else:
            labels.append("unclassified")

    anomaly_df["jwst_class"] = labels
    return anomaly_df


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 70)
    print("JWST MAST Archive NIRCam+NIRSpec Anomaly Scan — Phase 6")
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
        downloaded = try_download_jwst()
        if downloaded is not None:
            data_source = "mast_download"
            catalog = downloaded
        else:
            catalog = generate_synthetic_jwst()
            data_source = "fully_synthetic"

    # Handle non-detections (mag=99) by capping
    for band in NIRCAM_BANDS:
        col = f"mag_{band}"
        if col in catalog.columns:
            catalog[col] = catalog[col].clip(upper=35)

    available_features = [f for f in FEATURE_COLS if f in catalog.columns]
    print(f"[DATA] Source: {data_source}")
    print(f"[DATA] Sources: {len(catalog)}")
    print(f"[DATA] Features ({len(available_features)}): {available_features[:8]}...")
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
    anomaly_df = classify_jwst_anomalies(anomaly_df)
    anomaly_df.to_csv(OUTPUT_DIR / "jwst_mast_anomalies.csv", index=False)

    # Classification breakdown
    class_counts = anomaly_df["jwst_class"].value_counts().to_dict()
    type_counts = anomaly_df["type"].value_counts().to_dict() if "type" in anomaly_df.columns else {}

    # Top 20
    top_20 = []
    for rank, (_, row) in enumerate(anomaly_df.head(20).iterrows()):
        entry = {
            "rank": rank + 1,
            "source_id": int(row.get("source_id", 0)),
            "ra": float(row.get("ra", 0)),
            "dec": float(row.get("dec", 0)),
            "photo_z": float(row.get("photo_z", 0)),
            "continuum_slope": float(row.get("continuum_slope", 0)),
            "lya_ew": float(row.get("lya_ew", 0)),
            "oiii_ew": float(row.get("oiii_ew", 0)),
            "jwst_class": str(row.get("jwst_class", "unknown")),
            "recon_error": float(row.get("recon_error", 0)),
            "error_sigma": float(row.get("error_sigma", 0)),
        }
        for band in NIRCAM_BANDS:
            entry[f"mag_{band}"] = float(row.get(f"mag_{band}", 0))
        top_20.append(entry)

    elapsed = time.time() - t0
    summary = {
        "experiment": "jwst-mast",
        "phase": 6,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": str(DEVICE),
        "data_source": data_source,
        "config": {
            "features": available_features,
            "n_features": len(available_features),
            "nircam_bands": NIRCAM_BANDS,
            "nirspec_features": NIRSPEC_FEATURES,
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
            "jwst_class_breakdown": class_counts,
            "source_type_breakdown": type_counts,
        },
        "top_20_anomalies": top_20,
        "training_losses": [float(l) for l in losses],
        "elapsed_seconds": round(elapsed, 1),
        "files_written": [
            "jwst_mast_summary.json",
            "jwst_mast_anomalies.csv",
            "best_model.pt",
        ],
    }

    with open(OUTPUT_DIR / "jwst_mast_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"[DONE] {n_anomalies} anomalies from {len(features_scaled)} JWST sources ({anomaly_rate:.2f}%)")
    print(f"[DONE] Classification: {class_counts}")
    print(f"[DONE] Elapsed: {elapsed:.1f}s")
    print(f"[DONE] Files: {OUTPUT_DIR}")
    print()
    print("COMPLETE")


if __name__ == "__main__":
    main()
