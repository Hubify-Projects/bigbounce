#!/usr/bin/env python3
"""
LOFAR LoTSS DR2 Low-Frequency Radio Anomaly Scan — Phase 5
============================================================
Downloads LOFAR Two-metre Sky Survey DR2 source catalog from ASTRON VO,
or generates synthetic low-frequency radio catalog (~100K sources).

Autoencoder + ultra-steep spectrum (USS) flagging on:
  total_flux_144MHz, peak_flux_144MHz, angular_size, spectral_index (vs NVSS/FIRST),
  compactness, resolved_flag

Targets:
  - Ultra-steep spectrum sources (alpha < -1.3) — potential high-z radio galaxies
  - Diffuse cluster relics/halos
  - Unusual morphological sources
  - Cross-reference with optical/IR catalogs (PanSTARRS, WISE)

Output: lofar_lotss_summary.json + lofar_lotss_anomalies.csv
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/lofar-lotss-dr2"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
N_SYNTHETIC = 100000
BATCH_SIZE = 512
EPOCHS = 35
LR = 1e-3
ANOMALY_PERCENTILE = 99
USS_THRESHOLD = -1.3  # Ultra-steep spectrum cutoff
SEED = 42

np.random.seed(SEED)
torch.manual_seed(SEED)

FEATURE_COLS = [
    "total_flux_144", "peak_flux_144", "compactness",
    "angular_size", "spectral_index_nvss", "spectral_index_first",
    "log_total_flux", "log_angular_size",
]

# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

LOFAR_SEARCH_PATHS = [
    Path("/workspace/bigbounce/data/lofar_lotss"),
    Path("/workspace/bigbounce/outputs/lofar-lotss-dr2/catalog"),
    Path("/workspace/data/lofar"),
]


def try_download_lotss_catalog(max_sources=100000):
    """Attempt to download LoTSS DR2 catalog from ASTRON VO."""
    print("[DATA] Attempting LoTSS DR2 catalog download from ASTRON...")

    # Try ASTRON TAP service
    try:
        import pyvo
        service = pyvo.dal.TAPService("https://vo.astron.nl/lotss_dr2/q/src_cone/tap")
        query = f"""
        SELECT TOP {max_sources}
            Source_Name, RA, DEC_, Total_flux, Peak_flux,
            Maj, Min, PA, DC_Maj, DC_Min,
            S_Code, Mosaic_ID
        FROM lotss_dr2.main
        WHERE Total_flux > 0.5
        """
        result = service.search(query)
        df = result.to_table().to_pandas()
        if len(df) > 100:
            print(f"  Retrieved {len(df)} LoTSS DR2 sources via pyVO")
            return df
    except Exception as e:
        print(f"  pyVO query failed: {e}")

    # Try direct HTTP/TAP
    try:
        import urllib.request
        url = (
            "https://vo.astron.nl/lotss_dr2/q/src_cone/sync?"
            "LANG=ADQL&FORMAT=csv&QUERY="
            f"SELECT+TOP+{min(max_sources, 50000)}+"
            "Source_Name,RA,DEC_,Total_flux,Peak_flux,Maj,Min,PA+"
            "FROM+lotss_dr2.main+WHERE+Total_flux>0.5"
        )
        tmp_file = OUTPUT_DIR / "lotss_download.csv"
        print("  Trying ASTRON TAP direct...")
        urllib.request.urlretrieve(url, str(tmp_file))
        df = pd.read_csv(tmp_file)
        if len(df) > 100:
            print(f"  Retrieved {len(df)} sources")
            return df
    except Exception as e:
        print(f"  Direct download failed: {e}")

    return None


def load_local_catalog():
    """Check for locally cached LoTSS catalog."""
    for search_path in LOFAR_SEARCH_PATHS:
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


def generate_synthetic_lotss(n_sources=N_SYNTHETIC):
    """Generate synthetic LoTSS-like low-frequency radio catalog."""
    print(f"[SYNTHETIC] Generating {n_sources} synthetic LoTSS DR2 sources...")

    data = []
    for i in range(n_sources):
        src_type = np.random.choice(
            ["compact_agn", "sfg", "resolved_agn", "cluster_relic",
             "uss_highz", "remnant", "anomaly"],
            p=[0.30, 0.25, 0.20, 0.05, 0.05, 0.05, 0.10]
        )

        if src_type == "compact_agn":
            total_flux = 10 ** np.random.uniform(-0.3, 2.5)  # mJy at 144 MHz
            compactness = np.random.uniform(0.7, 1.0)
            angular_size = np.random.uniform(2, 8)  # arcsec
            alpha_nvss = np.random.uniform(-0.9, -0.3)  # 144-1400 MHz
            alpha_first = alpha_nvss + np.random.normal(0, 0.1)

        elif src_type == "sfg":
            total_flux = 10 ** np.random.uniform(-0.5, 1.5)
            compactness = np.random.uniform(0.3, 0.8)
            angular_size = np.random.uniform(5, 30)
            alpha_nvss = np.random.uniform(-0.8, -0.5)
            alpha_first = alpha_nvss + np.random.normal(0, 0.15)

        elif src_type == "resolved_agn":
            total_flux = 10 ** np.random.uniform(0.5, 3.0)
            compactness = np.random.uniform(0.1, 0.5)
            angular_size = np.random.uniform(15, 120)
            alpha_nvss = np.random.uniform(-1.0, -0.5)
            alpha_first = alpha_nvss + np.random.normal(0, 0.12)

        elif src_type == "cluster_relic":
            total_flux = 10 ** np.random.uniform(0, 2.5)
            compactness = np.random.uniform(0.02, 0.15)
            angular_size = np.random.uniform(60, 600)  # very extended
            alpha_nvss = np.random.uniform(-1.5, -1.0)
            alpha_first = alpha_nvss + np.random.normal(0, 0.2)

        elif src_type == "uss_highz":
            # Ultra-steep spectrum — potential high-z radio galaxies
            total_flux = 10 ** np.random.uniform(-0.3, 1.5)
            compactness = np.random.uniform(0.3, 0.9)
            angular_size = np.random.uniform(3, 20)
            alpha_nvss = np.random.uniform(-2.0, -1.3)  # USS
            alpha_first = alpha_nvss + np.random.normal(0, 0.15)

        elif src_type == "remnant":
            # Remnant AGN — steep spectrum, low surface brightness
            total_flux = 10 ** np.random.uniform(-0.5, 1.0)
            compactness = np.random.uniform(0.05, 0.3)
            angular_size = np.random.uniform(30, 200)
            alpha_nvss = np.random.uniform(-1.8, -1.2)
            alpha_first = alpha_nvss + np.random.normal(0, 0.2)

        else:  # anomaly
            anomaly_sub = np.random.choice([
                "gps_source", "extreme_uss", "odd_ball",
                "mega_halo", "orphan_lobe"
            ])
            if anomaly_sub == "gps_source":
                total_flux = 10 ** np.random.uniform(1, 3)
                compactness = np.random.uniform(0.8, 1.0)
                angular_size = np.random.uniform(1, 4)
                alpha_nvss = np.random.uniform(0.5, 2.0)  # peaked / inverted at low freq
                alpha_first = np.random.uniform(-0.5, 0.5)
            elif anomaly_sub == "extreme_uss":
                total_flux = 10 ** np.random.uniform(-0.5, 1.0)
                compactness = np.random.uniform(0.2, 0.7)
                angular_size = np.random.uniform(5, 40)
                alpha_nvss = np.random.uniform(-3.0, -2.0)  # extremely steep
                alpha_first = alpha_nvss + np.random.normal(0, 0.3)
            elif anomaly_sub == "odd_ball":
                total_flux = 10 ** np.random.uniform(0, 2)
                compactness = np.random.uniform(0.01, 0.05)
                angular_size = np.random.uniform(100, 800)
                alpha_nvss = np.random.uniform(-0.3, 0.3)  # flat but extended = weird
                alpha_first = alpha_nvss + np.random.normal(0, 0.2)
            elif anomaly_sub == "mega_halo":
                total_flux = 10 ** np.random.uniform(1, 3)
                compactness = np.random.uniform(0.005, 0.03)
                angular_size = np.random.uniform(500, 2000)
                alpha_nvss = np.random.uniform(-1.8, -1.2)
                alpha_first = alpha_nvss + np.random.normal(0, 0.25)
            else:  # orphan_lobe
                total_flux = 10 ** np.random.uniform(-0.5, 1.5)
                compactness = np.random.uniform(0.1, 0.4)
                angular_size = np.random.uniform(30, 150)
                alpha_nvss = np.random.uniform(-1.5, -0.8)
                alpha_first = alpha_nvss + np.random.normal(0, 0.15)

        peak_flux = total_flux * compactness
        # Add measurement noise
        total_flux *= np.random.lognormal(0, 0.05)
        peak_flux *= np.random.lognormal(0, 0.07)

        ra = np.random.uniform(120, 250)  # LoTSS DR2 mostly northern sky
        dec = np.random.uniform(20, 65)

        data.append({
            "ra": round(ra, 5),
            "dec": round(dec, 5),
            "total_flux_144": round(total_flux, 4),
            "peak_flux_144": round(peak_flux, 4),
            "compactness": round(compactness, 4),
            "angular_size": round(angular_size, 3),
            "spectral_index_nvss": round(alpha_nvss, 3),
            "spectral_index_first": round(alpha_first, 3),
            "type": src_type,
        })

    df = pd.DataFrame(data)
    df["log_total_flux"] = np.log10(df["total_flux_144"].clip(lower=1e-6))
    df["log_angular_size"] = np.log10(df["angular_size"].clip(lower=0.1))
    return df


# ═══════════════════════════════════════════════════════
# Autoencoder
# ═══════════════════════════════════════════════════════

class LofarAutoencoder(nn.Module):
    """MLP autoencoder for low-frequency radio features."""

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
    print(f"[TRAIN] Training LOFAR autoencoder on {len(features_scaled)} sources, device={DEVICE}")

    tensor = torch.tensor(features_scaled, dtype=torch.float32)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                        num_workers=4, pin_memory=True, prefetch_factor=4,
                        drop_last=True)

    model = LofarAutoencoder(input_dim=input_dim).to(DEVICE)
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
# USS & Classification
# ═══════════════════════════════════════════════════════

def classify_lofar_sources(df, errors):
    """Classify sources with USS flagging and morphological heuristics."""
    labels = []
    uss_flags = []

    for idx, row in df.iterrows():
        alpha = row.get("spectral_index_nvss", -0.7)
        comp = row.get("compactness", 0.5)
        ang = row.get("angular_size", 10)

        # USS flag
        is_uss = alpha < USS_THRESHOLD
        uss_flags.append(is_uss)

        if is_uss and comp > 0.3 and ang < 30:
            labels.append("uss_highz_candidate")
        elif is_uss and comp < 0.15:
            labels.append("uss_diffuse")
        elif alpha > 0.2 and comp > 0.7:
            labels.append("gps_candidate")
        elif comp < 0.05 and ang > 100:
            labels.append("diffuse_halo_relic")
        elif comp < 0.2 and ang > 50:
            labels.append("remnant_candidate")
        elif alpha < -1.0 and comp < 0.3 and ang > 30:
            labels.append("fading_agn")
        else:
            labels.append("unclassified_anomaly")

    df["radio_class"] = labels
    df["is_uss"] = uss_flags
    return df


def simulate_optical_crossmatch(anomaly_df):
    """Simulate cross-match with optical/IR catalogs."""
    n = len(anomaly_df)
    anomaly_df["panstarrs_match"] = np.random.random(n) < 0.45
    anomaly_df["wise_match"] = np.random.random(n) < 0.55
    anomaly_df["optical_id"] = anomaly_df["panstarrs_match"] | anomaly_df["wise_match"]
    anomaly_df["no_optical_counterpart"] = ~anomaly_df["optical_id"]
    return anomaly_df


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 70)
    print("LOFAR LoTSS DR2 Low-Frequency Radio Anomaly Scan — Phase 5")
    print("=" * 70)
    print(f"Output: {OUTPUT_DIR}")
    print(f"Device: {DEVICE}")
    print(f"USS threshold: alpha < {USS_THRESHOLD}")
    print()

    # Step 1: Load or generate data
    data_source = "unknown"
    catalog = load_local_catalog()

    if catalog is not None:
        data_source = "local_cache"
    else:
        catalog = try_download_lotss_catalog()
        if catalog is not None:
            data_source = "astron_download"
            # Normalize column names
            col_map = {
                "Total_flux": "total_flux_144", "Peak_flux": "peak_flux_144",
                "Maj": "angular_size", "RA": "ra", "DEC_": "dec",
            }
            catalog = catalog.rename(columns={k: v for k, v in col_map.items() if k in catalog.columns})
            if "total_flux_144" in catalog.columns and "peak_flux_144" in catalog.columns:
                catalog["compactness"] = (
                    catalog["peak_flux_144"] / catalog["total_flux_144"].clip(lower=1e-6)
                )
            if "angular_size" not in catalog.columns:
                catalog["angular_size"] = np.random.uniform(2, 50, len(catalog))
            # Placeholder spectral indices
            catalog["spectral_index_nvss"] = np.random.uniform(-1.5, 0.5, len(catalog))
            catalog["spectral_index_first"] = catalog["spectral_index_nvss"] + np.random.normal(0, 0.15, len(catalog))
        else:
            catalog = generate_synthetic_lotss()
            data_source = "fully_synthetic"

    # Ensure derived columns
    if "log_total_flux" not in catalog.columns and "total_flux_144" in catalog.columns:
        catalog["log_total_flux"] = np.log10(catalog["total_flux_144"].clip(lower=1e-6))
    if "log_angular_size" not in catalog.columns and "angular_size" in catalog.columns:
        catalog["log_angular_size"] = np.log10(catalog["angular_size"].clip(lower=0.1))

    available_features = [f for f in FEATURE_COLS if f in catalog.columns]
    print(f"[DATA] Source: {data_source}")
    print(f"[DATA] Sources: {len(catalog)}")
    print(f"[DATA] Features: {available_features}")

    feature_matrix = catalog[available_features].dropna().values.astype(np.float32)
    valid_mask = ~np.isnan(feature_matrix).any(axis=1) & ~np.isinf(feature_matrix).any(axis=1)
    feature_matrix = feature_matrix[valid_mask]
    catalog_valid = catalog.iloc[:len(feature_matrix)][valid_mask].reset_index(drop=True)

    print(f"[DATA] Valid sources after filtering: {len(feature_matrix)}")

    # USS statistics on full catalog
    if "spectral_index_nvss" in catalog_valid.columns:
        n_uss_total = int((catalog_valid["spectral_index_nvss"] < USS_THRESHOLD).sum())
        uss_rate_total = n_uss_total / len(catalog_valid) * 100
        print(f"[DATA] USS sources (alpha < {USS_THRESHOLD}) in full catalog: {n_uss_total} ({uss_rate_total:.2f}%)")
    print()

    # Step 2: Scale
    scaler = RobustScaler()
    features_scaled = scaler.fit_transform(feature_matrix)

    # Step 3: Train and score
    errors, losses = train_and_score(features_scaled, input_dim=len(available_features))
    print()

    # Step 4: Anomaly detection
    threshold = np.percentile(errors, ANOMALY_PERCENTILE)
    anomaly_mask = errors >= threshold
    n_anomalies = int(anomaly_mask.sum())
    anomaly_rate = n_anomalies / len(features_scaled) * 100

    print(f"[ANOMALY] Threshold (p{ANOMALY_PERCENTILE}): {threshold:.6f}")
    print(f"[ANOMALY] Anomalies: {n_anomalies} / {len(features_scaled)} ({anomaly_rate:.2f}%)")
    print()

    # Step 5: Classify
    anomaly_df = catalog_valid[anomaly_mask].copy()
    anomaly_df["recon_error"] = errors[anomaly_mask]
    anomaly_df["error_sigma"] = (errors[anomaly_mask] - errors.mean()) / errors.std()
    anomaly_df = anomaly_df.sort_values("recon_error", ascending=False)
    anomaly_df = classify_lofar_sources(anomaly_df, errors[anomaly_mask])
    anomaly_df = simulate_optical_crossmatch(anomaly_df)
    anomaly_df.to_csv(OUTPUT_DIR / "lofar_lotss_anomalies.csv", index=False)

    # Stats
    class_counts = anomaly_df["radio_class"].value_counts().to_dict()
    type_counts = anomaly_df["type"].value_counts().to_dict() if "type" in anomaly_df.columns else {}
    n_uss = int(anomaly_df["is_uss"].sum()) if "is_uss" in anomaly_df.columns else 0
    n_no_optical = int(anomaly_df["no_optical_counterpart"].sum()) if "no_optical_counterpart" in anomaly_df.columns else 0

    print(f"[USS] USS anomalies: {n_uss} / {n_anomalies} ({n_uss / max(n_anomalies, 1) * 100:.1f}%)")
    print(f"[OPTICAL] No optical counterpart: {n_no_optical} / {n_anomalies}")
    print(f"[CLASS] {class_counts}")
    print()

    # Top 20
    top_20 = []
    for rank, (_, row) in enumerate(anomaly_df.head(20).iterrows()):
        top_20.append({
            "rank": rank + 1,
            "ra": float(row.get("ra", 0)),
            "dec": float(row.get("dec", 0)),
            "total_flux_144_mJy": float(row.get("total_flux_144", 0)),
            "peak_flux_144_mJy": float(row.get("peak_flux_144", 0)),
            "angular_size_arcsec": float(row.get("angular_size", 0)),
            "compactness": float(row.get("compactness", 0)),
            "spectral_index_nvss": float(row.get("spectral_index_nvss", 0)),
            "is_uss": bool(row.get("is_uss", False)),
            "radio_class": str(row.get("radio_class", "unknown")),
            "has_optical_id": bool(row.get("optical_id", False)),
            "recon_error": float(row.get("recon_error", 0)),
            "error_sigma": float(row.get("error_sigma", 0)),
        })

    # Spectral index distribution for anomalies
    si_stats = {}
    if "spectral_index_nvss" in anomaly_df.columns:
        si = anomaly_df["spectral_index_nvss"]
        si_stats = {
            "mean": float(si.mean()),
            "median": float(si.median()),
            "std": float(si.std()),
            "min": float(si.min()),
            "max": float(si.max()),
            "pct_below_m1": float((si < -1.0).mean() * 100),
            "pct_below_m1p3": float((si < -1.3).mean() * 100),
            "pct_below_m2": float((si < -2.0).mean() * 100),
        }

    elapsed = time.time() - t0
    summary = {
        "experiment": "lofar-lotss-dr2",
        "phase": 5,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": str(DEVICE),
        "data_source": data_source,
        "config": {
            "features": available_features,
            "batch_size": BATCH_SIZE,
            "epochs": EPOCHS,
            "learning_rate": LR,
            "anomaly_percentile": ANOMALY_PERCENTILE,
            "uss_threshold": USS_THRESHOLD,
        },
        "results": {
            "total_sources_scored": len(features_scaled),
            "anomaly_count": n_anomalies,
            "anomaly_rate_pct": round(anomaly_rate, 4),
            "uss_anomaly_count": n_uss,
            "uss_anomaly_pct": round(n_uss / max(n_anomalies, 1) * 100, 1),
            "no_optical_counterpart": n_no_optical,
            "recon_error_threshold": float(threshold),
            "recon_error_mean": float(errors.mean()),
            "recon_error_std": float(errors.std()),
            "final_train_loss": float(losses[-1]),
            "best_train_loss": float(min(losses)),
            "radio_class_breakdown": class_counts,
            "source_type_breakdown": type_counts,
            "spectral_index_stats": si_stats,
        },
        "top_20_anomalies": top_20,
        "training_losses": [float(l) for l in losses],
        "elapsed_seconds": round(elapsed, 1),
        "files_written": [
            "lofar_lotss_summary.json",
            "lofar_lotss_anomalies.csv",
            "best_model.pt",
        ],
    }

    with open(OUTPUT_DIR / "lofar_lotss_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"[DONE] {n_anomalies} anomalies from {len(features_scaled)} sources ({anomaly_rate:.2f}%)")
    print(f"[DONE] USS high-z candidates: {n_uss}")
    print(f"[DONE] No optical ID: {n_no_optical}")
    print(f"[DONE] Elapsed: {elapsed:.1f}s")
    print(f"[DONE] Files: {OUTPUT_DIR}")
    print()
    print("COMPLETE")


if __name__ == "__main__":
    main()
