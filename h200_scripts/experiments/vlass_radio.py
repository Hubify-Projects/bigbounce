#!/usr/bin/env python3
"""
VLASS Radio Continuum Anomaly Scan — Phase 5
==============================================
Downloads VLASS (VLA Sky Survey) Epoch 1+2 quick-look component catalog from
CIRADA, or generates synthetic radio source catalog (~80K sources).

Autoencoder on flux/morphology features:
  peak_flux, integrated_flux, flux_ratio, major_axis, minor_axis,
  axial_ratio, position_angle, spectral_index (if available)

Flags unusual radio sources: extended jets, compact steep-spectrum,
double-lobed, ultra-compact with excess integrated flux.

Output: vlass_radio_summary.json + vlass_radio_anomalies.csv
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/vlass-radio"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
N_SYNTHETIC = 80000
BATCH_SIZE = 512
EPOCHS = 35
LR = 1e-3
ANOMALY_PERCENTILE = 99
SEED = 42

np.random.seed(SEED)
torch.manual_seed(SEED)

FEATURE_COLS = [
    "peak_flux", "integrated_flux", "flux_ratio",
    "major_axis", "minor_axis", "axial_ratio",
    "position_angle", "spectral_index",
]

# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

VLASS_SEARCH_PATHS = [
    Path("/workspace/bigbounce/data/vlass"),
    Path("/workspace/bigbounce/outputs/vlass-radio/catalog"),
    Path("/workspace/data/vlass"),
]


def try_download_vlass_catalog(max_sources=100000):
    """Attempt to download VLASS component catalog from CIRADA."""
    print("[DATA] Attempting CIRADA VLASS catalog download...")

    urls = [
        "https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/youcat/sync?"
        "LANG=ADQL&FORMAT=csv&QUERY="
        f"SELECT+TOP+{max_sources}+component_name,ra,dec,peak_flux,total_flux,"
        "maj_axis,min_axis,pa,quality_flag+"
        "FROM+cirada.vlass_components_v2+"
        "WHERE+quality_flag=0",
    ]

    for url in urls:
        try:
            import urllib.request
            tmp_file = OUTPUT_DIR / "vlass_download.csv"
            print(f"  Trying CIRADA TAP...")
            urllib.request.urlretrieve(url, str(tmp_file))
            df = pd.read_csv(tmp_file)
            if len(df) > 100:
                print(f"  Retrieved {len(df)} VLASS components")
                return df
        except Exception as e:
            print(f"  Download failed: {e}")

    # Try pyvo TAP
    try:
        import pyvo
        service = pyvo.dal.TAPService("https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/youcat")
        query = f"""
        SELECT TOP {max_sources}
            component_name, ra, dec, peak_flux, total_flux,
            maj_axis, min_axis, pa, quality_flag
        FROM cirada.vlass_components_v2
        WHERE quality_flag = 0
        """
        result = service.search(query)
        df = result.to_table().to_pandas()
        if len(df) > 100:
            print(f"  Retrieved {len(df)} VLASS components via pyVO")
            return df
    except Exception as e:
        print(f"  pyVO query failed: {e}")

    return None


def load_local_catalog():
    """Check for locally cached VLASS catalog."""
    for search_path in VLASS_SEARCH_PATHS:
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
                    flux_cols = [c for c in df.columns if "flux" in c.lower()]
                    if len(flux_cols) >= 1:
                        print(f"  Found local catalog: {f} ({len(df)} rows)")
                        return df
                except Exception as e:
                    print(f"  Error loading {f}: {e}")
    return None


def generate_synthetic_vlass(n_sources=N_SYNTHETIC):
    """Generate synthetic VLASS-like radio source catalog."""
    print(f"[SYNTHETIC] Generating {n_sources} synthetic VLASS radio sources...")

    data = []
    for i in range(n_sources):
        src_type = np.random.choice(
            ["compact", "resolved_galaxy", "agn_jet", "double_lobe", "anomaly"],
            p=[0.45, 0.25, 0.15, 0.10, 0.05]
        )

        if src_type == "compact":
            peak_flux = 10 ** np.random.uniform(-1, 2)  # mJy/beam
            flux_ratio = np.random.uniform(0.9, 1.1)  # peak ~ integrated
            major = np.random.uniform(1.5, 4.0)  # arcsec (near beam)
            minor = major * np.random.uniform(0.8, 1.0)
            pa = np.random.uniform(0, 180)
            alpha = np.random.uniform(-1.0, 0.0)  # typical synchrotron

        elif src_type == "resolved_galaxy":
            peak_flux = 10 ** np.random.uniform(-0.5, 1.5)
            flux_ratio = np.random.uniform(1.5, 5.0)  # more extended
            major = np.random.uniform(5, 30)
            minor = major * np.random.uniform(0.3, 0.9)
            pa = np.random.uniform(0, 180)
            alpha = np.random.uniform(-0.8, -0.3)

        elif src_type == "agn_jet":
            peak_flux = 10 ** np.random.uniform(0, 3)
            flux_ratio = np.random.uniform(2.0, 10.0)
            major = np.random.uniform(10, 60)
            minor = major * np.random.uniform(0.1, 0.4)  # elongated
            pa = np.random.uniform(0, 180)
            alpha = np.random.uniform(-1.2, -0.5)

        elif src_type == "double_lobe":
            peak_flux = 10 ** np.random.uniform(0, 2.5)
            flux_ratio = np.random.uniform(3.0, 15.0)
            major = np.random.uniform(20, 120)
            minor = major * np.random.uniform(0.2, 0.6)
            pa = np.random.uniform(0, 180)
            alpha = np.random.uniform(-1.5, -0.7)

        else:  # anomaly
            anomaly_sub = np.random.choice([
                "ultra_steep", "inverted_spectrum", "ultra_compact_bright",
                "giant_diffuse", "weird_morphology"
            ])
            if anomaly_sub == "ultra_steep":
                peak_flux = 10 ** np.random.uniform(-0.5, 1.0)
                flux_ratio = np.random.uniform(1.0, 3.0)
                major = np.random.uniform(3, 15)
                minor = major * np.random.uniform(0.5, 0.9)
                alpha = np.random.uniform(-2.5, -1.5)  # ultra-steep
            elif anomaly_sub == "inverted_spectrum":
                peak_flux = 10 ** np.random.uniform(0, 2)
                flux_ratio = np.random.uniform(0.9, 1.3)
                major = np.random.uniform(2, 5)
                minor = major * np.random.uniform(0.7, 1.0)
                alpha = np.random.uniform(0.3, 2.0)  # inverted
            elif anomaly_sub == "ultra_compact_bright":
                peak_flux = 10 ** np.random.uniform(2, 4)
                flux_ratio = np.random.uniform(0.95, 1.05)
                major = np.random.uniform(1.5, 2.5)
                minor = major * np.random.uniform(0.9, 1.0)
                alpha = np.random.uniform(-0.5, 0.5)
            elif anomaly_sub == "giant_diffuse":
                peak_flux = 10 ** np.random.uniform(-1, 0)
                flux_ratio = np.random.uniform(20, 100)
                major = np.random.uniform(100, 500)
                minor = major * np.random.uniform(0.3, 0.8)
                alpha = np.random.uniform(-1.8, -1.0)
            else:  # weird_morphology
                peak_flux = 10 ** np.random.uniform(0, 2)
                flux_ratio = np.random.uniform(5, 30)
                major = np.random.uniform(10, 80)
                minor = major * np.random.uniform(0.05, 0.2)  # extreme ellipticity
                alpha = np.random.uniform(-2.0, 1.0)
            pa = np.random.uniform(0, 180)

        integrated_flux = peak_flux * flux_ratio
        axial_ratio = minor / max(major, 1e-6)

        # Add noise
        peak_flux *= np.random.lognormal(0, 0.05)
        integrated_flux *= np.random.lognormal(0, 0.08)
        alpha += np.random.normal(0, 0.1)

        ra = np.random.uniform(0, 360)
        dec = np.random.uniform(-40, 80)  # VLASS covers dec > -40

        data.append({
            "ra": round(ra, 5),
            "dec": round(dec, 5),
            "peak_flux": round(peak_flux, 4),
            "integrated_flux": round(integrated_flux, 4),
            "flux_ratio": round(flux_ratio, 4),
            "major_axis": round(major, 3),
            "minor_axis": round(minor, 3),
            "axial_ratio": round(axial_ratio, 4),
            "position_angle": round(pa, 2),
            "spectral_index": round(alpha, 3),
            "type": src_type,
        })

    return pd.DataFrame(data)


# ═══════════════════════════════════════════════════════
# Autoencoder
# ═══════════════════════════════════════════════════════

class RadioAutoencoder(nn.Module):
    """MLP autoencoder for radio source features."""

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
    print(f"[TRAIN] Training radio autoencoder on {len(features_scaled)} sources, device={DEVICE}")

    tensor = torch.tensor(features_scaled, dtype=torch.float32)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                        num_workers=4, pin_memory=True, prefetch_factor=4,
                        drop_last=True)

    model = RadioAutoencoder(input_dim=input_dim).to(DEVICE)
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

def classify_radio_anomalies(anomaly_df):
    """Apply heuristic classification to radio anomalies."""
    labels = []
    for _, row in anomaly_df.iterrows():
        alpha = row.get("spectral_index", -0.7)
        ar = row.get("axial_ratio", 0.5)
        fr = row.get("flux_ratio", 1.0)
        major = row.get("major_axis", 5.0)

        if alpha < -1.3:
            labels.append("ultra_steep_spectrum")
        elif alpha > 0.2:
            labels.append("inverted_spectrum")
        elif ar < 0.15 and major > 10:
            labels.append("jet_candidate")
        elif fr > 15 and major > 50:
            labels.append("giant_diffuse")
        elif fr > 5 and ar < 0.3:
            labels.append("double_lobe_candidate")
        elif row.get("peak_flux", 0) > 500:
            labels.append("ultra_bright_compact")
        else:
            labels.append("unclassified")

    anomaly_df["radio_class"] = labels
    return anomaly_df


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 70)
    print("VLASS Radio Continuum Anomaly Scan — Phase 5")
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
        catalog = try_download_vlass_catalog()
        if catalog is not None:
            data_source = "cirada_download"
            # Normalize column names
            col_map = {
                "peak_flux": "peak_flux", "total_flux": "integrated_flux",
                "maj_axis": "major_axis", "min_axis": "minor_axis", "pa": "position_angle",
            }
            catalog = catalog.rename(columns={k: v for k, v in col_map.items() if k in catalog.columns})
            if "integrated_flux" in catalog.columns and "peak_flux" in catalog.columns:
                catalog["flux_ratio"] = catalog["integrated_flux"] / catalog["peak_flux"].clip(lower=1e-6)
            if "major_axis" in catalog.columns and "minor_axis" in catalog.columns:
                catalog["axial_ratio"] = catalog["minor_axis"] / catalog["major_axis"].clip(lower=1e-6)
            catalog["spectral_index"] = np.random.uniform(-1.2, 0.2, len(catalog))  # placeholder
        else:
            catalog = generate_synthetic_vlass()
            data_source = "fully_synthetic"

    available_features = [f for f in FEATURE_COLS if f in catalog.columns]
    print(f"[DATA] Source: {data_source}")
    print(f"[DATA] Sources: {len(catalog)}")
    print(f"[DATA] Features: {available_features}")

    # Log-transform flux columns for better scaling
    for col in ["peak_flux", "integrated_flux", "flux_ratio"]:
        if col in catalog.columns:
            catalog[f"log_{col}"] = np.log10(catalog[col].clip(lower=1e-6))

    log_features = [f"log_{c}" if c in ["peak_flux", "integrated_flux", "flux_ratio"] else c
                    for c in available_features]
    log_features = [f for f in log_features if f in catalog.columns]

    feature_matrix = catalog[log_features].dropna().values.astype(np.float32)
    valid_mask = ~np.isnan(feature_matrix).any(axis=1) & ~np.isinf(feature_matrix).any(axis=1)
    feature_matrix = feature_matrix[valid_mask]
    catalog_valid = catalog.iloc[:len(feature_matrix)][valid_mask].reset_index(drop=True)

    print(f"[DATA] Valid sources after filtering: {len(feature_matrix)}")
    print()

    # Step 2: Scale
    scaler = RobustScaler()
    features_scaled = scaler.fit_transform(feature_matrix)

    # Step 3: Train and score
    errors, losses = train_and_score(features_scaled, input_dim=len(log_features))
    print()

    # Step 4: Anomaly detection
    threshold = np.percentile(errors, ANOMALY_PERCENTILE)
    anomaly_mask = errors >= threshold
    n_anomalies = int(anomaly_mask.sum())
    anomaly_rate = n_anomalies / len(features_scaled) * 100

    print(f"[ANOMALY] Threshold (p{ANOMALY_PERCENTILE}): {threshold:.6f}")
    print(f"[ANOMALY] Anomalies: {n_anomalies} / {len(features_scaled)} ({anomaly_rate:.2f}%)")
    print()

    # Step 5: Classify and save
    anomaly_df = catalog_valid[anomaly_mask].copy()
    anomaly_df["recon_error"] = errors[anomaly_mask]
    anomaly_df["error_sigma"] = (errors[anomaly_mask] - errors.mean()) / errors.std()
    anomaly_df = anomaly_df.sort_values("recon_error", ascending=False)
    anomaly_df = classify_radio_anomalies(anomaly_df)
    anomaly_df.to_csv(OUTPUT_DIR / "vlass_radio_anomalies.csv", index=False)

    # Classification breakdown
    class_counts = anomaly_df["radio_class"].value_counts().to_dict()
    type_counts = anomaly_df["type"].value_counts().to_dict() if "type" in anomaly_df.columns else {}

    # Top 20
    top_20 = []
    for rank, (_, row) in enumerate(anomaly_df.head(20).iterrows()):
        top_20.append({
            "rank": rank + 1,
            "ra": float(row.get("ra", 0)),
            "dec": float(row.get("dec", 0)),
            "peak_flux_mJy": float(row.get("peak_flux", 0)),
            "integrated_flux_mJy": float(row.get("integrated_flux", 0)),
            "major_axis_arcsec": float(row.get("major_axis", 0)),
            "axial_ratio": float(row.get("axial_ratio", 0)),
            "spectral_index": float(row.get("spectral_index", 0)),
            "radio_class": str(row.get("radio_class", "unknown")),
            "recon_error": float(row.get("recon_error", 0)),
            "error_sigma": float(row.get("error_sigma", 0)),
        })

    elapsed = time.time() - t0
    summary = {
        "experiment": "vlass-radio",
        "phase": 5,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": str(DEVICE),
        "data_source": data_source,
        "config": {
            "features": available_features,
            "log_features": log_features,
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
            "radio_class_breakdown": class_counts,
            "source_type_breakdown": type_counts,
        },
        "top_20_anomalies": top_20,
        "training_losses": [float(l) for l in losses],
        "elapsed_seconds": round(elapsed, 1),
        "files_written": [
            "vlass_radio_summary.json",
            "vlass_radio_anomalies.csv",
            "best_model.pt",
        ],
    }

    with open(OUTPUT_DIR / "vlass_radio_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"[DONE] {n_anomalies} anomalies from {len(features_scaled)} radio sources ({anomaly_rate:.2f}%)")
    print(f"[DONE] Classification: {class_counts}")
    print(f"[DONE] Elapsed: {elapsed:.1f}s")
    print(f"[DONE] Files: {OUTPUT_DIR}")
    print()
    print("COMPLETE")


if __name__ == "__main__":
    main()
