#!/usr/bin/env python3
"""
XMM-Newton 4XMM-DR14 X-ray Anomaly Scan — Phase 6
====================================================
Downloads 4XMM-DR14 serendipitous source catalog from ESA XMM-Newton
Science Archive, or generates 100K synthetic XMM sources.

Features: flux in 5 EPIC bands (0.2-0.5, 0.5-1, 1-2, 2-4.5, 4.5-12 keV),
hardness ratios (HR1-HR4), extent, variability.

Autoencoder anomaly detection. Cross-references with eROSITA anomaly
catalog on pod if available.

Output: xmm_4xmm_dr14_summary.json + xmm_4xmm_dr14_anomalies.csv
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/xmm-4xmm-dr14"))
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

# XMM-Newton EPIC energy bands (keV)
EPIC_BANDS = {
    "band1": "0.2-0.5",
    "band2": "0.5-1.0",
    "band3": "1.0-2.0",
    "band4": "2.0-4.5",
    "band5": "4.5-12.0",
}
EPIC_BAND_NAMES = list(EPIC_BANDS.keys())

# Hardness ratios: HR_i = (B_{i+1} - B_i) / (B_{i+1} + B_i)
HR_NAMES = ["hr1", "hr2", "hr3", "hr4"]

FEATURE_COLS = (
    [f"log_flux_{b}" for b in EPIC_BAND_NAMES]
    + HR_NAMES
    + ["log_extent", "variability"]
)
# 5 log-fluxes + 4 HRs + extent + variability = 11 features

# eROSITA cross-reference paths
EROSITA_ANOMALY_PATHS = [
    Path("/workspace/bigbounce/outputs/erosita-xray/erosita_xray_anomalies.csv"),
    Path("/workspace/bigbounce/outputs/erosita-dr1/erosita_anomalies.csv"),
    Path("/workspace/bigbounce/pipelines/h200_results/erosita-xray/erosita_xray_anomalies.csv"),
]

# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

XMM_SEARCH_PATHS = [
    Path("/workspace/bigbounce/data/xmm"),
    Path("/workspace/bigbounce/outputs/xmm-4xmm-dr14/catalog"),
    Path("/workspace/data/xmm"),
]


def try_download_4xmm(max_sources=10000):
    """Attempt to download 4XMM-DR14 catalog via ESA TAP."""
    print("[DATA] Attempting 4XMM-DR14 download via ESA XSA TAP...")
    try:
        import urllib.request
        url = (
            "https://nxsa.esac.esa.int/tap-server/tap/sync?"
            "FORMAT=csv&LANG=ADQL&QUERY="
            f"SELECT+TOP+{max_sources}+iauname,sc_ra,sc_dec,"
            "sc_ep_1_flux,sc_ep_2_flux,sc_ep_3_flux,sc_ep_4_flux,sc_ep_5_flux,"
            "sc_hr1,sc_hr2,sc_hr3,sc_hr4,sc_extent,sc_var_flag+"
            "FROM+xsa.v_4xmm_dr14cat"
        )
        tmp_file = OUTPUT_DIR / "4xmm_download.csv"
        urllib.request.urlretrieve(url, str(tmp_file))
        df = pd.read_csv(tmp_file)
        if len(df) > 100:
            print(f"  Retrieved {len(df)} 4XMM-DR14 sources")
            return df
    except Exception as e:
        print(f"  4XMM download failed: {e}")

    # Try VizieR fallback
    try:
        import urllib.request
        url = (
            "https://vizier.cds.unistra.fr/viz-bin/votable?"
            "-source=IX/68/4xmmdr14s&"
            f"-out.max={max_sources}&"
            "-out=IAUNAME,RA,DEC,Flux1,Flux2,Flux3,Flux4,Flux5,HR1,HR2,HR3,HR4,Ext,VarFlag"
        )
        tmp_file = OUTPUT_DIR / "4xmm_vizier.csv"
        urllib.request.urlretrieve(url, str(tmp_file))
        df = pd.read_csv(tmp_file, comment='#', sep=',')
        if len(df) > 100:
            print(f"  Retrieved {len(df)} sources via VizieR")
            return df
    except Exception as e:
        print(f"  VizieR download failed: {e}")

    return None


def load_local_catalog():
    """Check for locally cached XMM data."""
    for search_path in XMM_SEARCH_PATHS:
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


def load_erosita_anomalies():
    """Try to load eROSITA anomaly catalog for cross-referencing."""
    for path in EROSITA_ANOMALY_PATHS:
        if path.exists():
            try:
                df = pd.read_csv(path)
                if len(df) > 0 and "ra" in df.columns and "dec" in df.columns:
                    print(f"[XMATCH] Loaded eROSITA anomaly catalog: {path} ({len(df)} sources)")
                    return df
            except Exception as e:
                print(f"  Error loading eROSITA catalog {path}: {e}")
    print("[XMATCH] No eROSITA anomaly catalog found on pod")
    return None


def angular_separation(ra1, dec1, ra2, dec2):
    """Compute angular separation in arcseconds between two sky positions."""
    ra1, dec1, ra2, dec2 = map(np.radians, [ra1, dec1, ra2, dec2])
    cos_sep = (np.sin(dec1) * np.sin(dec2) +
               np.cos(dec1) * np.cos(dec2) * np.cos(ra1 - ra2))
    cos_sep = np.clip(cos_sep, -1, 1)
    return np.degrees(np.arccos(cos_sep)) * 3600  # arcsec


def cross_match_erosita(xmm_anomalies, erosita_df, match_radius_arcsec=10.0):
    """Cross-match XMM anomalies with eROSITA anomaly catalog."""
    if erosita_df is None or len(erosita_df) == 0:
        return xmm_anomalies, 0

    print(f"[XMATCH] Cross-matching {len(xmm_anomalies)} XMM anomalies with "
          f"{len(erosita_df)} eROSITA anomalies (radius={match_radius_arcsec}\")")

    matches = []
    for idx, xmm_row in xmm_anomalies.iterrows():
        xmm_ra = xmm_row.get("ra", 0)
        xmm_dec = xmm_row.get("dec", 0)
        seps = angular_separation(xmm_ra, xmm_dec,
                                  erosita_df["ra"].values, erosita_df["dec"].values)
        best_idx = np.argmin(seps)
        best_sep = seps[best_idx]
        if best_sep < match_radius_arcsec:
            matches.append({
                "xmm_idx": idx,
                "erosita_idx": best_idx,
                "separation_arcsec": round(best_sep, 2),
                "erosita_score": float(erosita_df.iloc[best_idx].get("recon_error", 0)),
            })

    n_matched = len(matches)
    xmm_anomalies["erosita_match"] = False
    xmm_anomalies["erosita_sep_arcsec"] = np.nan

    for m in matches:
        xmm_anomalies.loc[m["xmm_idx"], "erosita_match"] = True
        xmm_anomalies.loc[m["xmm_idx"], "erosita_sep_arcsec"] = m["separation_arcsec"]

    print(f"[XMATCH] Found {n_matched} matches ({n_matched/max(len(xmm_anomalies),1)*100:.1f}%)")
    return xmm_anomalies, n_matched


def generate_synthetic_xmm(n_sources=N_SYNTHETIC):
    """Generate synthetic 4XMM-DR14-like X-ray source catalog."""
    print(f"[SYNTHETIC] Generating {n_sources} synthetic XMM-Newton sources...")

    rows = []
    for i in range(n_sources):
        src_type = np.random.choice(
            ["star", "agn", "xrb", "cluster", "ulx", "anomaly"],
            p=[0.25, 0.30, 0.15, 0.10, 0.10, 0.10]
        )

        row = {"source_id": i, "type": src_type}

        if src_type == "star":
            # Coronal emission: peaked around 0.5-2 keV
            base = 10 ** np.random.uniform(-15, -13)
            fluxes = [
                base * np.random.uniform(0.5, 1.5),   # 0.2-0.5
                base * np.random.uniform(1.0, 3.0),   # 0.5-1.0
                base * np.random.uniform(0.5, 2.0),   # 1.0-2.0
                base * np.random.uniform(0.1, 0.5),   # 2.0-4.5
                base * np.random.uniform(0.01, 0.1),  # 4.5-12.0
            ]
            extent = np.random.uniform(0, 2)
            variability = np.random.uniform(0, 3)

        elif src_type == "agn":
            # Power-law with absorption
            base = 10 ** np.random.uniform(-15, -12)
            nh = 10 ** np.random.uniform(20, 23)
            abs_soft = np.exp(-nh / 3e21)
            fluxes = [
                base * abs_soft * np.random.uniform(0.1, 0.5),
                base * abs_soft * np.random.uniform(0.3, 1.0),
                base * np.random.uniform(0.8, 1.5),
                base * np.random.uniform(0.6, 1.2),
                base * np.random.uniform(0.3, 0.8),
            ]
            extent = np.random.uniform(0, 3)
            variability = np.random.uniform(0, 5)

        elif src_type == "xrb":
            base = 10 ** np.random.uniform(-14, -11)
            state = np.random.choice(["soft", "hard", "intermediate"])
            if state == "soft":
                fluxes = [
                    base * np.random.uniform(0.3, 1.0),
                    base * np.random.uniform(1.0, 3.0),
                    base * np.random.uniform(0.5, 1.5),
                    base * np.random.uniform(0.1, 0.5),
                    base * np.random.uniform(0.01, 0.1),
                ]
            elif state == "hard":
                fluxes = [
                    base * np.random.uniform(0.05, 0.2),
                    base * np.random.uniform(0.1, 0.5),
                    base * np.random.uniform(0.5, 1.5),
                    base * np.random.uniform(1.0, 2.0),
                    base * np.random.uniform(0.5, 1.5),
                ]
            else:
                fluxes = [
                    base * np.random.uniform(0.2, 0.6),
                    base * np.random.uniform(0.5, 1.5),
                    base * np.random.uniform(0.8, 2.0),
                    base * np.random.uniform(0.5, 1.5),
                    base * np.random.uniform(0.2, 0.8),
                ]
            extent = np.random.uniform(0, 1)
            variability = np.random.uniform(3, 12)

        elif src_type == "cluster":
            # Thermal plasma: peaked at 1-4 keV
            base = 10 ** np.random.uniform(-14, -12)
            kt = np.random.uniform(1, 8)  # keV
            fluxes = [
                base * np.random.uniform(0.2, 0.8),
                base * np.random.uniform(0.5, 1.5),
                base * np.random.uniform(1.0, 2.0),
                base * np.random.uniform(0.5, 1.5) * (kt / 3),
                base * np.random.uniform(0.1, 0.5) * (kt / 5),
            ]
            extent = np.random.uniform(15, 200)  # very extended
            variability = np.random.uniform(0, 1)

        elif src_type == "ulx":
            # Ultra-luminous X-ray: very bright, soft excess + hard tail
            base = 10 ** np.random.uniform(-13, -11)
            fluxes = [
                base * np.random.uniform(0.5, 2.0),
                base * np.random.uniform(1.0, 3.0),
                base * np.random.uniform(1.0, 2.5),
                base * np.random.uniform(0.3, 1.0),
                base * np.random.uniform(0.1, 0.5),
            ]
            extent = np.random.uniform(0, 5)
            variability = np.random.uniform(2, 8)

        else:  # anomaly
            anomaly_sub = np.random.choice([
                "super_soft", "compton_thick", "flaring",
                "inverted_spectrum", "ghostly_extended", "dual_agn"
            ])
            base = 10 ** np.random.uniform(-14, -11)

            if anomaly_sub == "super_soft":
                fluxes = [
                    base * np.random.uniform(5, 20),
                    base * np.random.uniform(2, 10),
                    base * np.random.uniform(0.01, 0.1),
                    base * np.random.uniform(0.001, 0.01),
                    base * np.random.uniform(0.0001, 0.001),
                ]
                extent = np.random.uniform(0, 2)
                variability = np.random.uniform(1, 5)

            elif anomaly_sub == "compton_thick":
                # Almost all emission above 2 keV
                fluxes = [
                    base * np.random.uniform(0.001, 0.01),
                    base * np.random.uniform(0.005, 0.05),
                    base * np.random.uniform(0.05, 0.3),
                    base * np.random.uniform(0.5, 2.0),
                    base * np.random.uniform(1.0, 5.0),
                ]
                extent = np.random.uniform(0, 2)
                variability = np.random.uniform(0, 3)

            elif anomaly_sub == "flaring":
                fluxes = [
                    base * np.random.lognormal(0, 1),
                    base * np.random.lognormal(0, 1),
                    base * np.random.lognormal(0, 1),
                    base * np.random.lognormal(0, 1),
                    base * np.random.lognormal(0, 1),
                ]
                extent = np.random.uniform(0, 3)
                variability = np.random.uniform(10, 30)  # extreme

            elif anomaly_sub == "inverted_spectrum":
                # Rising with energy
                fluxes = [
                    base * np.random.uniform(0.1, 0.3),
                    base * np.random.uniform(0.3, 0.6),
                    base * np.random.uniform(0.6, 1.5),
                    base * np.random.uniform(1.5, 4.0),
                    base * np.random.uniform(3.0, 10.0),
                ]
                extent = np.random.uniform(0, 2)
                variability = np.random.uniform(0, 4)

            elif anomaly_sub == "ghostly_extended":
                # Very extended, very faint
                base_faint = 10 ** np.random.uniform(-16, -14)
                fluxes = [
                    base_faint * np.random.uniform(0.5, 2),
                    base_faint * np.random.uniform(0.5, 2),
                    base_faint * np.random.uniform(0.5, 2),
                    base_faint * np.random.uniform(0.2, 1),
                    base_faint * np.random.uniform(0.05, 0.5),
                ]
                extent = np.random.uniform(50, 300)
                variability = np.random.uniform(0, 1)

            else:  # dual_agn
                # Two overlapping spectra
                base2 = base * np.random.uniform(0.3, 3)
                fluxes = [
                    (base + base2) * np.random.uniform(0.2, 0.8),
                    (base + base2) * np.random.uniform(0.5, 1.5),
                    (base + base2) * np.random.uniform(0.8, 2.0),
                    (base + base2) * np.random.uniform(0.5, 1.5),
                    (base + base2) * np.random.uniform(0.3, 1.0),
                ]
                extent = np.random.uniform(3, 15)
                variability = np.random.uniform(2, 7)

        # Add measurement noise
        fluxes = [f * np.random.lognormal(0, 0.05) for f in fluxes]
        fluxes = [max(f, 1e-20) for f in fluxes]

        # Store raw and log fluxes
        for j, bname in enumerate(EPIC_BAND_NAMES):
            row[f"flux_{bname}"] = fluxes[j]
            row[f"log_flux_{bname}"] = round(np.log10(max(fluxes[j], 1e-20)), 4)

        # Hardness ratios
        for j in range(4):
            hr = (fluxes[j + 1] - fluxes[j]) / (fluxes[j + 1] + fluxes[j] + 1e-20)
            row[HR_NAMES[j]] = round(np.clip(hr, -1, 1), 4)

        row["extent"] = round(extent, 3)
        row["log_extent"] = round(np.log10(max(extent, 0.1)), 4)
        row["variability"] = round(variability, 3)
        row["ra"] = round(np.random.uniform(0, 360), 5)
        row["dec"] = round(np.random.uniform(-90, 90), 5)
        rows.append(row)

        if (i + 1) % 20000 == 0:
            print(f"  Generated {i+1}/{n_sources} sources...")

    return pd.DataFrame(rows)


# ═══════════════════════════════════════════════════════
# Autoencoder
# ═══════════════════════════════════════════════════════

class XMMAutoencoder(nn.Module):
    """MLP autoencoder for XMM-Newton X-ray source features."""

    def __init__(self, input_dim=11, latent_dim=3):
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
    print(f"[TRAIN] Training XMM autoencoder on {len(features_scaled)} sources, device={DEVICE}")

    tensor = torch.tensor(features_scaled, dtype=torch.float32)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                        num_workers=4, pin_memory=True, prefetch_factor=4,
                        drop_last=True)

    model = XMMAutoencoder(input_dim=input_dim).to(DEVICE)
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

def classify_xmm_anomalies(anomaly_df):
    """Apply heuristic classification to XMM anomalies."""
    labels = []
    for _, row in anomaly_df.iterrows():
        hr1 = row.get("hr1", 0)
        hr2 = row.get("hr2", 0)
        hr3 = row.get("hr3", 0)
        hr4 = row.get("hr4", 0)
        extent = row.get("extent", 0)
        var = row.get("variability", 0)
        log_f1 = row.get("log_flux_band1", -15)
        log_f5 = row.get("log_flux_band5", -15)

        if hr1 < -0.5 and hr2 < -0.5:
            labels.append("super_soft_source")
        elif hr3 > 0.5 and hr4 > 0.3:
            labels.append("compton_thick_candidate")
        elif hr4 > 0.5 and log_f5 > log_f1 + 1:
            labels.append("ultra_hard_spectrum")
        elif extent > 30 and var < 1:
            labels.append("extended_diffuse")
        elif var > 10:
            labels.append("extreme_variable")
        elif extent > 10 and var > 5:
            labels.append("extended_transient")
        elif all(h > 0 for h in [hr1, hr2, hr3, hr4]):
            labels.append("monotonically_rising")
        elif log_f1 > -11 or log_f5 > -11:
            labels.append("super_luminous")
        else:
            labels.append("unclassified")

    anomaly_df["xmm_class"] = labels
    return anomaly_df


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 70)
    print("XMM-Newton 4XMM-DR14 X-ray Anomaly Scan — Phase 6")
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
        downloaded = try_download_4xmm()
        if downloaded is not None:
            data_source = "esa_download"
            catalog = downloaded
        else:
            catalog = generate_synthetic_xmm()
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

    # Step 6: Classify
    anomaly_df = catalog_valid[anomaly_mask].copy()
    anomaly_df["recon_error"] = errors[anomaly_mask]
    anomaly_df["error_sigma"] = (errors[anomaly_mask] - errors.mean()) / errors.std()
    anomaly_df = anomaly_df.sort_values("recon_error", ascending=False)
    anomaly_df = classify_xmm_anomalies(anomaly_df)

    # Step 7: eROSITA cross-match
    erosita_df = load_erosita_anomalies()
    anomaly_df, n_erosita_matches = cross_match_erosita(anomaly_df, erosita_df)

    # Save
    anomaly_df.to_csv(OUTPUT_DIR / "xmm_4xmm_dr14_anomalies.csv", index=False)

    # Classification breakdown
    class_counts = anomaly_df["xmm_class"].value_counts().to_dict()
    type_counts = anomaly_df["type"].value_counts().to_dict() if "type" in anomaly_df.columns else {}

    # Top 20
    top_20 = []
    for rank, (_, row) in enumerate(anomaly_df.head(20).iterrows()):
        entry = {
            "rank": rank + 1,
            "source_id": int(row.get("source_id", 0)),
            "ra": float(row.get("ra", 0)),
            "dec": float(row.get("dec", 0)),
            "xmm_class": str(row.get("xmm_class", "unknown")),
            "recon_error": float(row.get("recon_error", 0)),
            "error_sigma": float(row.get("error_sigma", 0)),
            "erosita_match": bool(row.get("erosita_match", False)),
        }
        for hr in HR_NAMES:
            entry[hr] = float(row.get(hr, 0))
        for bname in EPIC_BAND_NAMES:
            entry[f"log_flux_{bname}"] = float(row.get(f"log_flux_{bname}", 0))
        top_20.append(entry)

    elapsed = time.time() - t0
    summary = {
        "experiment": "xmm-4xmm-dr14",
        "phase": 6,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": str(DEVICE),
        "data_source": data_source,
        "config": {
            "features": available_features,
            "n_features": len(available_features),
            "epic_bands_keV": EPIC_BANDS,
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
            "xmm_class_breakdown": class_counts,
            "source_type_breakdown": type_counts,
            "erosita_cross_matches": n_erosita_matches,
            "erosita_match_rate_pct": round(n_erosita_matches / max(n_anomalies, 1) * 100, 2),
        },
        "top_20_anomalies": top_20,
        "training_losses": [float(l) for l in losses],
        "elapsed_seconds": round(elapsed, 1),
        "files_written": [
            "xmm_4xmm_dr14_summary.json",
            "xmm_4xmm_dr14_anomalies.csv",
            "best_model.pt",
        ],
    }

    with open(OUTPUT_DIR / "xmm_4xmm_dr14_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"[DONE] {n_anomalies} anomalies from {len(features_scaled)} XMM sources ({anomaly_rate:.2f}%)")
    print(f"[DONE] Classification: {class_counts}")
    print(f"[DONE] eROSITA matches: {n_erosita_matches}")
    print(f"[DONE] Elapsed: {elapsed:.1f}s")
    print(f"[DONE] Files: {OUTPUT_DIR}")
    print()
    print("COMPLETE")


if __name__ == "__main__":
    main()
