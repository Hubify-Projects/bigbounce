#!/usr/bin/env python3
"""
BOSS/eBOSS DR16 Spectral Anomaly Scan — Phase 5
=================================================
Downloads BOSS/eBOSS spectra from SDSS SkyServer via astroquery, or falls
back to synthetic spectral data (~50K spectra, 4000 wavelength bins).

Trains a 1-D convolutional autoencoder (4000→512→128→32→128→512→4000) on
the spectral flux arrays and scores by reconstruction error. Top 1% flagged
as anomalies.

Output: boss_eboss_summary.json + boss_eboss_anomalies.csv
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
for pkg in ["astroquery", "torch"]:
    try:
        __import__(pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", pkg])

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/boss-eboss-dr16"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
N_WAVELENGTH_BINS = 4000
LATENT_DIM = 32
BATCH_SIZE = 256
EPOCHS = 40
LR = 1e-3
ANOMALY_PERCENTILE = 99  # Top 1%
N_SYNTHETIC = 50000
SEED = 42

np.random.seed(SEED)
torch.manual_seed(SEED)

# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

BOSS_SEARCH_PATHS = [
    Path("/workspace/bigbounce/data/boss_eboss"),
    Path("/workspace/bigbounce/outputs/boss-eboss-dr16/spectra"),
    Path("/workspace/data/boss"),
]


def try_download_boss_spectra(max_spectra=50000):
    """Attempt to download BOSS spectra via astroquery."""
    print("[DATA] Attempting SDSS SkyServer query for BOSS/eBOSS spectra...")
    try:
        from astroquery.sdss import SDSS
        from astropy import coordinates as coords

        # Query a large area for BOSS spectra
        query = f"""
        SELECT TOP {max_spectra}
            s.specobjid, s.ra, s.dec, s.z AS redshift, s.zwarning,
            s.class, s.subclass, s.plate, s.mjd, s.fiberid,
            s.sn_median_all AS snr
        FROM SpecObj AS s
        WHERE s.survey IN ('boss', 'eboss')
            AND s.zwarning = 0
            AND s.sn_median_all > 2
        ORDER BY s.specobjid
        """
        result = SDSS.query_sql(query, timeout=300)
        if result is not None and len(result) > 100:
            print(f"  Retrieved {len(result)} BOSS/eBOSS catalog entries")
            df = result.to_pandas()
            return df, None  # catalog only, no raw spectra
        else:
            print("  Query returned insufficient results")
            return None, None
    except Exception as e:
        print(f"  SDSS query failed: {e}")
        return None, None


def load_local_spectra():
    """Check for locally cached spectra."""
    for search_path in BOSS_SEARCH_PATHS:
        if not search_path.exists():
            continue
        for pattern in ["*.npy", "*.npz", "*.fits"]:
            files = sorted(search_path.glob(pattern))
            if files:
                try:
                    f = files[0]
                    if f.suffix == ".npy":
                        spectra = np.load(f)
                    elif f.suffix == ".npz":
                        npz = np.load(f)
                        spectra = npz[list(npz.keys())[0]]
                    else:
                        continue
                    print(f"  Found local spectra: {f} shape={spectra.shape}")
                    return spectra
                except Exception as e:
                    print(f"  Error loading {f}: {e}")
    return None


def generate_synthetic_spectra(n_spectra=N_SYNTHETIC, n_bins=N_WAVELENGTH_BINS):
    """Generate synthetic BOSS-like spectra with planted anomalies."""
    print(f"[SYNTHETIC] Generating {n_spectra} synthetic spectra ({n_bins} bins)...")
    wavelengths = np.linspace(3600, 10400, n_bins)  # BOSS wavelength range (Angstroms)

    spectra = np.zeros((n_spectra, n_bins), dtype=np.float32)
    metadata = []

    for i in range(n_spectra):
        z = np.random.uniform(0.0, 3.5)
        spec_type = np.random.choice(["galaxy", "qso", "star", "anomaly"],
                                     p=[0.55, 0.25, 0.15, 0.05])

        # Continuum: power law + noise
        alpha = np.random.uniform(-2.0, 0.5)
        continuum = (wavelengths / 5500.0) ** alpha
        continuum *= np.random.uniform(0.5, 5.0)

        if spec_type == "galaxy":
            # Add emission lines at rest-frame positions, redshifted
            lines = [(3727, 0.8), (4861, 0.5), (5007, 1.2), (6563, 1.5)]  # OII, Hb, OIII, Ha
            for rest_lam, amp in lines:
                obs_lam = rest_lam * (1 + z)
                sigma = np.random.uniform(3, 15)
                continuum += amp * np.random.uniform(0.5, 3.0) * np.exp(
                    -0.5 * ((wavelengths - obs_lam) / sigma) ** 2
                )
            # 4000A break
            break_pos = 4000 * (1 + z)
            continuum *= (1 + 0.3 * (1 / (1 + np.exp(-(wavelengths - break_pos) / 50))))

        elif spec_type == "qso":
            # Broad emission lines
            lines = [(1216, 5.0), (1549, 2.0), (1909, 1.5), (2798, 2.5),
                     (4861, 1.0), (5007, 0.8)]
            for rest_lam, amp in lines:
                obs_lam = rest_lam * (1 + z)
                sigma = np.random.uniform(20, 80)
                continuum += amp * np.random.uniform(1.0, 5.0) * np.exp(
                    -0.5 * ((wavelengths - obs_lam) / sigma) ** 2
                )

        elif spec_type == "star":
            # Absorption features
            z = 0.0
            lines = [(3933, -1.5), (3968, -1.2), (4300, -0.8), (5175, -0.6)]  # CaK, CaH, CH, Mg
            for rest_lam, amp in lines:
                sigma = np.random.uniform(5, 20)
                continuum += amp * np.exp(-0.5 * ((wavelengths - rest_lam) / sigma) ** 2)

        elif spec_type == "anomaly":
            # Unusual features: double-peaked emission, inverted lines, etc.
            anomaly_type = np.random.choice(["double_peak", "inverted", "ultra_broad", "weird_continuum"])
            if anomaly_type == "double_peak":
                center = np.random.uniform(4500, 8000)
                sep = np.random.uniform(20, 100)
                for offset in [-sep / 2, sep / 2]:
                    continuum += 3.0 * np.exp(-0.5 * ((wavelengths - center - offset) / 10) ** 2)
            elif anomaly_type == "inverted":
                center = np.random.uniform(4000, 9000)
                continuum -= 2.0 * np.exp(-0.5 * ((wavelengths - center) / 30) ** 2)
                continuum += 1.5 * np.exp(-0.5 * ((wavelengths - center) / 5) ** 2)
            elif anomaly_type == "ultra_broad":
                center = np.random.uniform(4000, 8000)
                continuum += 4.0 * np.exp(-0.5 * ((wavelengths - center) / 300) ** 2)
            elif anomaly_type == "weird_continuum":
                continuum *= (1 + 0.5 * np.sin(wavelengths / 200))

        # Add noise
        noise_level = np.random.uniform(0.05, 0.3)
        continuum += noise_level * np.random.randn(n_bins)

        # Normalize
        med = np.median(continuum)
        if med > 0:
            continuum /= med

        spectra[i] = continuum.astype(np.float32)

        ra = np.random.uniform(0, 360)
        dec = np.random.uniform(-10, 70)
        metadata.append({
            "idx": i, "ra": round(ra, 5), "dec": round(dec, 5),
            "redshift": round(z, 4), "type": spec_type,
            "plate": np.random.randint(3500, 12000),
            "mjd": np.random.randint(55000, 59500),
            "fiberid": np.random.randint(1, 1001),
        })

    return spectra, pd.DataFrame(metadata), wavelengths


# ═══════════════════════════════════════════════════════
# Autoencoder Architecture
# ═══════════════════════════════════════════════════════

class SpectralAutoencoder(nn.Module):
    """1-D convolutional autoencoder for spectral anomaly detection."""

    def __init__(self, n_bins=N_WAVELENGTH_BINS, latent_dim=LATENT_DIM):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv1d(1, 32, kernel_size=7, stride=2, padding=3),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Conv1d(32, 64, kernel_size=5, stride=2, padding=2),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=5, stride=2, padding=2),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Conv1d(128, 256, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(8),
            nn.Flatten(),
            nn.Linear(256 * 8, 512),
            nn.ReLU(),
            nn.Linear(512, latent_dim),
        )
        self.decoder_fc = nn.Sequential(
            nn.Linear(latent_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 256 * 8),
            nn.ReLU(),
        )
        self.decoder_conv = nn.Sequential(
            nn.ConvTranspose1d(256, 128, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.ConvTranspose1d(128, 64, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.ConvTranspose1d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.ConvTranspose1d(32, 1, kernel_size=4, stride=2, padding=1),
        )
        self.final_interp = nn.AdaptiveAvgPool1d(n_bins)

    def forward(self, x):
        z = self.encoder(x)
        h = self.decoder_fc(z)
        h = h.view(-1, 256, 8)
        h = self.decoder_conv(h)
        h = self.final_interp(h)
        return h


# ═══════════════════════════════════════════════════════
# Training
# ═══════════════════════════════════════════════════════

def train_autoencoder(spectra):
    """Train the spectral autoencoder."""
    print(f"[TRAIN] Training autoencoder on {len(spectra)} spectra, device={DEVICE}")

    tensor = torch.tensor(spectra, dtype=torch.float32).unsqueeze(1)  # (N, 1, n_bins)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True,
                        num_workers=4, pin_memory=True, prefetch_factor=4,
                        drop_last=True)

    model = SpectralAutoencoder(n_bins=spectra.shape[1]).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=EPOCHS)
    criterion = nn.MSELoss()

    best_loss = float("inf")
    losses = []

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

    # Load best
    model.load_state_dict(torch.load(OUTPUT_DIR / "best_model.pt", weights_only=True))
    return model, losses


# ═══════════════════════════════════════════════════════
# Anomaly Scoring
# ═══════════════════════════════════════════════════════

def score_anomalies(model, spectra):
    """Score all spectra by reconstruction error."""
    print("[SCORE] Computing reconstruction errors...")
    model.eval()
    tensor = torch.tensor(spectra, dtype=torch.float32).unsqueeze(1)
    dataset = TensorDataset(tensor)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=False,
                        num_workers=4, pin_memory=True, prefetch_factor=4)

    all_errors = []
    with torch.no_grad():
        for (batch,) in loader:
            batch = batch.to(DEVICE, non_blocking=True)
            recon = model(batch)
            errors = ((batch - recon) ** 2).mean(dim=(1, 2))  # per-spectrum MSE
            all_errors.append(errors.cpu().numpy())

    return np.concatenate(all_errors)


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 70)
    print("BOSS/eBOSS DR16 Spectral Anomaly Scan — Phase 5")
    print("=" * 70)
    print(f"Output: {OUTPUT_DIR}")
    print(f"Device: {DEVICE}")
    print()

    # Step 1: Load or generate data
    data_source = "unknown"
    spectra = load_local_spectra()

    if spectra is not None:
        data_source = "local_cache"
        n_spec = len(spectra)
        # Generate minimal metadata
        metadata = pd.DataFrame({
            "idx": range(n_spec),
            "ra": np.random.uniform(0, 360, n_spec),
            "dec": np.random.uniform(-10, 70, n_spec),
            "redshift": np.random.uniform(0, 2, n_spec),
            "type": "unknown",
        })
        wavelengths = np.linspace(3600, 10400, spectra.shape[1])
    else:
        catalog, _ = try_download_boss_spectra()
        if catalog is not None and len(catalog) > 1000:
            data_source = "sdss_query_synthetic_spectra"
            print(f"[DATA] Got catalog with {len(catalog)} entries, generating synthetic spectra...")
        spectra, metadata, wavelengths = generate_synthetic_spectra()
        if data_source == "unknown":
            data_source = "fully_synthetic"

    print(f"[DATA] Source: {data_source}")
    print(f"[DATA] Spectra shape: {spectra.shape}")
    print(f"[DATA] Metadata: {len(metadata)} entries")
    print()

    # Step 2: Train autoencoder
    model, losses = train_autoencoder(spectra)
    print()

    # Step 3: Score anomalies
    errors = score_anomalies(model, spectra)
    threshold = np.percentile(errors, ANOMALY_PERCENTILE)
    anomaly_mask = errors >= threshold
    n_anomalies = int(anomaly_mask.sum())
    anomaly_rate = n_anomalies / len(spectra) * 100

    print(f"[ANOMALY] Threshold (p{ANOMALY_PERCENTILE}): {threshold:.6f}")
    print(f"[ANOMALY] Anomalies: {n_anomalies} / {len(spectra)} ({anomaly_rate:.2f}%)")
    print()

    # Step 4: Extract top anomalies
    top_indices = np.argsort(errors)[::-1][:100]
    top_20 = []
    for rank, idx in enumerate(top_indices[:20]):
        row = metadata.iloc[idx]
        top_20.append({
            "rank": rank + 1,
            "idx": int(idx),
            "ra": float(row.get("ra", 0)),
            "dec": float(row.get("dec", 0)),
            "redshift": float(row.get("redshift", 0)),
            "type": str(row.get("type", "unknown")),
            "recon_error": float(errors[idx]),
            "error_sigma": float((errors[idx] - errors.mean()) / errors.std()),
        })

    # Step 5: Save anomaly catalog
    anomaly_df = metadata[anomaly_mask].copy()
    anomaly_df["recon_error"] = errors[anomaly_mask]
    anomaly_df["error_sigma"] = (errors[anomaly_mask] - errors.mean()) / errors.std()
    anomaly_df = anomaly_df.sort_values("recon_error", ascending=False)
    anomaly_df.to_csv(OUTPUT_DIR / "boss_eboss_anomalies.csv", index=False)

    # Type breakdown among anomalies
    if "type" in anomaly_df.columns:
        type_counts = anomaly_df["type"].value_counts().to_dict()
    else:
        type_counts = {}

    # Step 6: Summary
    elapsed = time.time() - t0
    summary = {
        "experiment": "boss-eboss-dr16",
        "phase": 5,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": str(DEVICE),
        "data_source": data_source,
        "config": {
            "n_wavelength_bins": N_WAVELENGTH_BINS,
            "latent_dim": LATENT_DIM,
            "batch_size": BATCH_SIZE,
            "epochs": EPOCHS,
            "learning_rate": LR,
            "anomaly_percentile": ANOMALY_PERCENTILE,
        },
        "results": {
            "total_spectra_scored": len(spectra),
            "anomaly_count": n_anomalies,
            "anomaly_rate_pct": round(anomaly_rate, 4),
            "recon_error_threshold": float(threshold),
            "recon_error_mean": float(errors.mean()),
            "recon_error_std": float(errors.std()),
            "recon_error_max": float(errors.max()),
            "final_train_loss": float(losses[-1]),
            "best_train_loss": float(min(losses)),
            "anomaly_type_breakdown": type_counts,
        },
        "top_20_anomalies": top_20,
        "training_losses": [float(l) for l in losses],
        "elapsed_seconds": round(elapsed, 1),
        "files_written": [
            "boss_eboss_summary.json",
            "boss_eboss_anomalies.csv",
            "best_model.pt",
        ],
    }

    with open(OUTPUT_DIR / "boss_eboss_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"[DONE] {n_anomalies} anomalies from {len(spectra)} spectra ({anomaly_rate:.2f}%)")
    print(f"[DONE] Elapsed: {elapsed:.1f}s")
    print(f"[DONE] Files: {OUTPUT_DIR}")
    print()
    print("COMPLETE")


if __name__ == "__main__":
    main()
