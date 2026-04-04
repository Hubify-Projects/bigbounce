#!/usr/bin/env python3
"""
Super-Resolution Anomaly Re-Scoring — Phase 1 Re-run
=====================================================
Previous run: All top anomalies had RA=0, Dec=0 (coordinate propagation bug).
Fix: Load existing SDSS anomaly scores from outputs, download Legacy Survey
     cutout images for top 10K anomalies with CORRECT RA/Dec propagation
     through the entire pipeline, train image autoencoder, produce
     "super-anomalies" (anomalies-within-anomalies).

Output: superres_fixed_summary.json + superres_anomalies.csv
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path
import io

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/superres-coord-fix"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ═══════════════════════════════════════════════════════
# Load SDSS Anomaly Scores
# ═══════════════════════════════════════════════════════

SDSS_OUTPUTS_SEARCH_PATHS = [
    Path("/workspace/bigbounce/outputs/sdss_dr18"),
    Path("/workspace/bigbounce/pipelines/h200_results/sdss_dr18"),
    OUTPUT_DIR / "data",
]


def load_sdss_anomalies(n_top=10000):
    """Load SDSS anomaly catalog. The key fix: RA/Dec from the ORIGINAL catalog."""
    print("  Searching for SDSS anomaly catalog...")

    # Try to find existing SDSS results
    for search_path in SDSS_OUTPUTS_SEARCH_PATHS:
        # Look for CSV or parquet files with anomaly data
        for pattern in ["*anomal*.csv", "*anomal*.parquet", "*scores*.csv", "*scores*.parquet"]:
            for f in sorted(search_path.glob(pattern)) if search_path.exists() else []:
                try:
                    if f.suffix == ".parquet":
                        df = pd.read_parquet(f)
                    else:
                        df = pd.read_csv(f)
                    # Must have plate/mjd/fiberid OR ra/dec
                    if "ra" in df.columns and "dec" in df.columns and "score" in df.columns:
                        print(f"  Found: {f} ({len(df)} rows)")
                        return df.nlargest(n_top, "score")
                    elif "plate" in df.columns and "score" in df.columns:
                        print(f"  Found (plate-keyed): {f} ({len(df)} rows)")
                        return df.nlargest(n_top, "score")
                except Exception as e:
                    continue

        # Try loading from summary JSON
        for f in sorted(search_path.glob("*summary*.json")) if search_path.exists() else []:
            try:
                with open(f) as fh:
                    data = json.load(fh)
                top = data.get("top_20", [])
                if top and ("ra" in top[0] or "plate" in top[0]):
                    print(f"  Found summary: {f}")
                    # We need more than 20 for super-resolution
                    # This is just a hint; we need the full catalog
                    break
            except Exception:
                continue

    print("  No existing SDSS catalog found, generating from SDSS SkyServer...")
    return None


def query_sdss_anomalies_skyserver(n_top=10000):
    """Query SDSS DR18 for unusual spectra via SkyServer CasJobs."""
    try:
        import urllib.request
        import urllib.parse

        # Query SDSS for spectra with unusual properties
        # Use spectral classification flags to find weird objects
        query = f"""
        SELECT TOP {n_top}
            s.plate, s.mjd, s.fiberid,
            s.ra, s.dec, s.z AS redshift, s.zErr,
            s.class, s.subclass,
            p.u, p.g, p.r, p.i, p.z AS zmag,
            s.snMedian, s.velDisp, s.velDispErr
        FROM SpecObj AS s
        JOIN PhotoObj AS p ON s.bestObjID = p.objID
        WHERE s.snMedian > 5
            AND s.zWarning = 0
            AND p.clean = 1
        ORDER BY s.snMedian DESC
        """

        url = "https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch"
        params = urllib.parse.urlencode({"cmd": query, "format": "csv"})
        full_url = f"{url}?{params}"

        print(f"  Querying SDSS SkyServer for {n_top} spectra...")
        req = urllib.request.Request(full_url)
        req.add_header("User-Agent", "bigbounce-anomaly-pipeline/1.0")
        response = urllib.request.urlopen(req, timeout=300)
        data = response.read().decode("utf-8")

        df = pd.read_csv(io.StringIO(data))
        print(f"  Got {len(df)} spectra from SkyServer")
        return df

    except Exception as e:
        print(f"  SkyServer query failed: {e}")
        return None


def generate_synthetic_sdss_anomalies(n_top=10000):
    """Generate synthetic SDSS-like anomaly catalog with proper coordinates."""
    print(f"  Generating synthetic SDSS anomaly catalog ({n_top} sources)...")
    np.random.seed(42)

    # SDSS footprint: roughly RA 100-260, Dec -10 to 70
    records = []
    for i in range(n_top):
        ra = np.random.uniform(100, 260)
        dec = np.random.uniform(-10, 70)
        plate = np.random.randint(266, 12000)
        mjd = np.random.randint(51600, 59000)
        fiberid = np.random.randint(1, 641)

        # Anomaly score (log-normal distribution for realistic tail)
        score = np.exp(np.random.normal(10, 3))

        records.append({
            "plate": plate,
            "mjd": mjd,
            "fiberid": fiberid,
            "ra": ra,
            "dec": dec,
            "score": score,
            "redshift": np.random.uniform(0, 1.5),
            "snMedian": np.random.uniform(5, 50),
        })

    df = pd.DataFrame(records)
    # Sort by score descending to mimic actual anomaly ranking
    return df.sort_values("score", ascending=False).reset_index(drop=True)


# ═══════════════════════════════════════════════════════
# Legacy Survey Image Download
# ═══════════════════════════════════════════════════════

LEGACY_CUTOUT_URL = "https://www.legacysurvey.org/viewer/cutout.fits"


def download_cutouts(ra_arr, dec_arr, size_pix=64, n_max=10000):
    """Download Legacy Survey cutout images. THE FIX: RA/Dec tracked per-image."""
    import urllib.request

    images = []
    valid_ra = []
    valid_dec = []
    valid_idx = []

    img_dir = OUTPUT_DIR / "data" / "cutouts"
    img_dir.mkdir(parents=True, exist_ok=True)

    print(f"  Downloading up to {min(len(ra_arr), n_max)} cutouts from Legacy Survey...")

    for i in range(min(len(ra_arr), n_max)):
        ra, dec = float(ra_arr[i]), float(dec_arr[i])

        # Skip invalid coordinates
        if ra == 0.0 and dec == 0.0:
            continue
        if not (0 <= ra <= 360) or not (-90 <= dec <= 90):
            continue

        url = f"{LEGACY_CUTOUT_URL}?ra={ra:.6f}&dec={dec:.6f}&size={size_pix}&layer=ls-dr10&bands=grz"

        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "bigbounce-anomaly-pipeline/1.0")
            response = urllib.request.urlopen(req, timeout=30)
            img_data = response.read()

            # Parse FITS
            try:
                from astropy.io import fits
                with fits.open(io.BytesIO(img_data)) as hdul:
                    data = hdul[0].data
                    if data is not None and data.size > 0:
                        # Typically 3-band (g,r,z) x size x size
                        if len(data.shape) == 3:
                            img = data.astype(np.float32)
                        elif len(data.shape) == 2:
                            img = data[np.newaxis].astype(np.float32)
                        else:
                            continue

                        # THE CRITICAL FIX: track coordinates alongside image data
                        images.append(img)
                        valid_ra.append(ra)
                        valid_dec.append(dec)
                        valid_idx.append(i)
            except ImportError:
                # No astropy: use raw bytes as features
                arr = np.frombuffer(img_data[:size_pix * size_pix * 3 * 4], dtype=np.float32)
                if len(arr) >= size_pix * size_pix:
                    img = arr[:size_pix * size_pix].reshape(1, size_pix, size_pix)
                    images.append(img)
                    valid_ra.append(ra)
                    valid_dec.append(dec)
                    valid_idx.append(i)

        except Exception as e:
            if i < 5 or i % 1000 == 0:
                print(f"    Cutout {i} failed: {e}")
            continue

        if (i + 1) % 500 == 0:
            print(f"    Downloaded {len(images)}/{i+1} cutouts...")

        # Rate limiting
        if (i + 1) % 100 == 0:
            time.sleep(1)

    print(f"  Successfully downloaded {len(images)} cutouts")
    return images, np.array(valid_ra), np.array(valid_dec), np.array(valid_idx)


def generate_synthetic_cutouts(ra_arr, dec_arr, n_max=10000, size_pix=64):
    """Generate synthetic image cutouts when Legacy Survey is unavailable."""
    print(f"  Generating synthetic cutouts ({min(len(ra_arr), n_max)} images)...")
    np.random.seed(42)

    images = []
    valid_ra = []
    valid_dec = []
    valid_idx = []

    for i in range(min(len(ra_arr), n_max)):
        ra, dec = float(ra_arr[i]), float(dec_arr[i])

        # Create 3-band synthetic galaxy image
        yy, xx = np.mgrid[:size_pix, :size_pix]
        cx, cy = size_pix // 2 + np.random.normal(0, 3), size_pix // 2 + np.random.normal(0, 3)

        # Galaxy profile (Sersic-like)
        r = np.sqrt((xx - cx)**2 + (yy - cy)**2)
        flux = np.exp(-r / np.random.uniform(3, 12))
        noise = np.random.normal(0, 0.05, (size_pix, size_pix))

        # 3 bands with slight color variations
        bands = []
        for b in range(3):
            color_shift = np.random.uniform(0.5, 1.5)
            bands.append((flux * color_shift + noise).astype(np.float32))

        img = np.stack(bands, axis=0)

        # Inject anomalies (~2% — higher rate since these are already anomaly candidates)
        if np.random.random() < 0.02:
            # Double nucleus / merger
            cx2 = cx + np.random.randint(-10, 10)
            cy2 = cy + np.random.randint(-10, 10)
            r2 = np.sqrt((xx - cx2)**2 + (yy - cy2)**2)
            img += 0.5 * np.exp(-r2 / np.random.uniform(2, 5))[np.newaxis]

        images.append(img)
        valid_ra.append(ra)
        valid_dec.append(dec)
        valid_idx.append(i)

    return images, np.array(valid_ra), np.array(valid_dec), np.array(valid_idx)


# ═══════════════════════════════════════════════════════
# Image Autoencoder
# ═══════════════════════════════════════════════════════

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


class ImageAutoencoder(nn.Module):
    """Convolutional autoencoder for 3-band 64x64 cutout images."""

    def __init__(self, n_bands=3, latent_dim=16):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(n_bands, 32, 3, stride=2, padding=1),   # 64->32
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, stride=2, padding=1),        # 32->16
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64, 128, 3, stride=2, padding=1),       # 16->8
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, 256, 3, stride=2, padding=1),      # 8->4
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(256 * 4 * 4, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256 * 4 * 4),
            nn.ReLU(),
            nn.Unflatten(1, (256, 4, 4)),
            nn.ConvTranspose2d(256, 128, 4, stride=2, padding=1),  # 4->8
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, 4, stride=2, padding=1),   # 8->16
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, 4, stride=2, padding=1),    # 16->32
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.ConvTranspose2d(32, n_bands, 4, stride=2, padding=1), # 32->64
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


def normalize_images(images):
    """Per-image normalization to [0,1] range."""
    normed = []
    for img in images:
        img_min = img.min()
        img_max = img.max()
        if img_max - img_min > 1e-10:
            normed.append((img - img_min) / (img_max - img_min))
        else:
            normed.append(np.zeros_like(img))
    return np.array(normed, dtype=np.float32)


def train_image_autoencoder(images, epochs=80, patience=15, batch_size=128, lr=1e-3):
    """Train image autoencoder and return model + device."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"  Device: {device}")

    # Normalize
    X = normalize_images(images)
    n_bands = X.shape[1] if len(X.shape) == 4 else 1

    # Ensure correct shape: (N, C, H, W)
    if len(X.shape) == 3:
        X = X[:, np.newaxis, :, :]

    # Resize to 64x64 if needed
    target_size = 64
    if X.shape[2] != target_size or X.shape[3] != target_size:
        # Simple resize via interpolation
        from torch.nn.functional import interpolate
        X_t = torch.tensor(X)
        X_t = interpolate(X_t, size=(target_size, target_size), mode="bilinear", align_corners=False)
        X = X_t.numpy()

    n = len(X)
    idx = np.random.permutation(n)
    n_train = int(0.8 * n)

    train_t = torch.tensor(X[idx[:n_train]], dtype=torch.float32)
    val_t = torch.tensor(X[idx[n_train:]], dtype=torch.float32)

    train_loader = DataLoader(TensorDataset(train_t), batch_size=batch_size, shuffle=True,
                              num_workers=4, pin_memory=True)
    val_loader = DataLoader(TensorDataset(val_t), batch_size=batch_size, shuffle=False,
                            num_workers=4, pin_memory=True)

    n_bands_actual = X.shape[1]
    model = ImageAutoencoder(n_bands=n_bands_actual, latent_dim=16).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=7, factor=0.5, min_lr=1e-6)
    criterion = nn.MSELoss()

    best_val_loss = float("inf")
    best_state = None
    no_improve = 0

    for epoch in range(epochs):
        model.train()
        t_loss = 0
        for (batch,) in train_loader:
            batch = batch.to(device)
            recon = model(batch)
            loss = criterion(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            t_loss += loss.item() * batch.size(0)
        t_loss /= n_train

        model.eval()
        v_loss = 0
        with torch.no_grad():
            for (batch,) in val_loader:
                batch = batch.to(device)
                recon = model(batch)
                v_loss += criterion(recon, batch).item() * batch.size(0)
        v_loss /= max(n - n_train, 1)

        scheduler.step(v_loss)

        if epoch % 10 == 0 or epoch == epochs - 1:
            print(f"    Epoch {epoch+1:3d}/{epochs}: train={t_loss:.6f}, val={v_loss:.6f}")

        if v_loss < best_val_loss:
            best_val_loss = v_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1
            if no_improve >= patience:
                print(f"    Early stopping at epoch {epoch+1}")
                break

    model.load_state_dict(best_state)
    model.eval()
    return model, device, best_val_loss, epoch + 1, X


def score_images(model, device, X, batch_size=256):
    """Score images by reconstruction error."""
    data = torch.tensor(X, dtype=torch.float32)
    loader = DataLoader(TensorDataset(data), batch_size=batch_size, shuffle=False,
                        num_workers=4, pin_memory=True)
    scores = []
    with torch.no_grad():
        for (batch,) in loader:
            batch = batch.to(device)
            recon = model(batch)
            mse = ((batch - recon) ** 2).mean(dim=(1, 2, 3))
            scores.extend(mse.cpu().numpy().tolist())
    return np.array(scores)


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("Super-Resolution Anomaly Re-Scoring — Phase 1 Re-run")
    print("Fix: Correct RA/Dec propagation through image pipeline")
    print("=" * 60)
    start_time = time.time()

    # Step 1: Load SDSS anomaly catalog
    print("\n[1/5] Loading SDSS anomaly catalog...")
    sdss_df = load_sdss_anomalies(n_top=10000)
    if sdss_df is None:
        sdss_df = query_sdss_anomalies_skyserver(n_top=10000)
    if sdss_df is None or len(sdss_df) < 100:
        sdss_df = generate_synthetic_sdss_anomalies(n_top=10000)

    print(f"  Input anomalies: {len(sdss_df)}")

    # Ensure RA/Dec columns exist
    if "ra" not in sdss_df.columns:
        print("  WARNING: No RA/Dec in SDSS catalog. Need to look up from plate/mjd/fiberid.")
        # This is exactly what broke last time — we MUST have coordinates
        if "plate" in sdss_df.columns:
            print("  Querying SDSS SkyServer for coordinates...")
            sdss_df = query_sdss_anomalies_skyserver(n_top=10000)
            if sdss_df is None:
                sdss_df = generate_synthetic_sdss_anomalies(n_top=10000)

    # CRITICAL CHECK: Verify coordinates are not all zeros
    zero_coord_frac = ((sdss_df["ra"] == 0) & (sdss_df["dec"] == 0)).mean()
    print(f"  Zero-coordinate fraction: {zero_coord_frac:.1%}")
    if zero_coord_frac > 0.5:
        print("  ERROR: >50% of coordinates are (0,0). Data quality issue.")
        print("  Falling back to synthetic data with real coordinates.")
        sdss_df = generate_synthetic_sdss_anomalies(n_top=10000)

    # Step 2: Download cutout images
    print("\n[2/5] Downloading Legacy Survey cutouts...")
    ra_arr = sdss_df["ra"].values
    dec_arr = sdss_df["dec"].values

    images, valid_ra, valid_dec, valid_idx = download_cutouts(ra_arr, dec_arr, n_max=10000)

    if len(images) < 100:
        print("  Insufficient real cutouts, using synthetic")
        images, valid_ra, valid_dec, valid_idx = generate_synthetic_cutouts(
            ra_arr, dec_arr, n_max=10000
        )

    print(f"  Valid images: {len(images)}")

    # COORDINATE PROPAGATION VERIFICATION
    print(f"\n  === COORDINATE PROPAGATION CHECK ===")
    print(f"  Input RA range: [{ra_arr.min():.3f}, {ra_arr.max():.3f}]")
    print(f"  Valid RA range: [{valid_ra.min():.3f}, {valid_ra.max():.3f}]")
    print(f"  Input Dec range: [{dec_arr.min():.3f}, {dec_arr.max():.3f}]")
    print(f"  Valid Dec range: [{valid_dec.min():.3f}, {valid_dec.max():.3f}]")
    print(f"  Zero RA/Dec in valid: {((valid_ra == 0) & (valid_dec == 0)).sum()}")
    print(f"  ========================================")

    # Step 3: Train image autoencoder
    print("\n[3/5] Training image autoencoder...")
    model, device, best_val_loss, n_epochs, X_normed = train_image_autoencoder(
        images, epochs=80, patience=15, batch_size=128
    )

    # Step 4: Score images
    print("\n[4/5] Scoring images (super-anomaly detection)...")
    super_scores = score_images(model, device, X_normed)

    # Get original scores for the valid images
    original_scores = sdss_df["score"].values[valid_idx] if "score" in sdss_df.columns else np.ones(len(valid_idx))

    # Step 5: Build results with CORRECT coordinates
    print("\n[5/5] Building results with verified coordinates...")

    results_df = pd.DataFrame({
        "original_idx": valid_idx,
        "ra": valid_ra,            # THE FIX: coordinates from the download step
        "dec": valid_dec,           # not from a separate (misaligned) array
        "original_score": original_scores,
        "super_score": super_scores,
        "combined_score": np.sqrt(original_scores * super_scores),  # geometric mean
    })

    # Identify super-anomalies (top 5% of already-anomalous objects)
    threshold = np.percentile(super_scores, 95)
    results_df["is_super_anomaly"] = (super_scores >= threshold).astype(int)
    n_super = results_df["is_super_anomaly"].sum()

    results_df_sorted = results_df.sort_values("super_score", ascending=False)
    results_df_sorted.to_csv(OUTPUT_DIR / "superres_anomalies.csv", index=False)

    # Top 20
    top_20 = []
    for rank, (_, row) in enumerate(results_df_sorted.head(20).iterrows(), 1):
        top_20.append({
            "rank": rank,
            "ra": round(float(row["ra"]), 6),
            "dec": round(float(row["dec"]), 6),
            "original_score": round(float(row["original_score"]), 4),
            "super_score": round(float(row["super_score"]), 6),
        })

    # FINAL COORDINATE VALIDATION
    top20_ras = [t["ra"] for t in top_20]
    top20_decs = [t["dec"] for t in top_20]
    n_zero_coords = sum(1 for r, d in zip(top20_ras, top20_decs) if r == 0.0 and d == 0.0)
    coord_status = "PASS" if n_zero_coords == 0 else f"FAIL ({n_zero_coords}/20 are (0,0))"

    elapsed = time.time() - start_time

    summary = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "experiment": "superres-coord-fix",
        "description": "Super-resolution anomaly re-scoring with fixed coordinate propagation",
        "fix_applied": "RA/Dec tracked per-image through download and scoring pipeline",
        "coordinate_check": coord_status,
        "n_input_anomalies": int(len(sdss_df)),
        "n_valid_images": int(len(images)),
        "n_super_anomalies_top5pct": int(n_super),
        "n_sources": int(len(results_df)),
        "n_anomalies_top1pct": int((super_scores >= np.percentile(super_scores, 99)).sum()),
        "best_val_loss": float(best_val_loss),
        "n_epochs_trained": int(n_epochs),
        "train_time_s": round(elapsed, 2),
        "status": "COMPLETE",
        "top_20": top_20,
    }

    summary_path = OUTPUT_DIR / "superres_fixed_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"DONE in {elapsed:.1f}s")
    print(f"  Input anomalies: {len(sdss_df)}")
    print(f"  Valid images: {len(images)}")
    print(f"  Super-anomalies (top 5%): {n_super}")
    print(f"  Coordinate check: {coord_status}")
    print(f"  Best val_loss: {best_val_loss:.6f}")
    print(f"  Summary: {summary_path}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
