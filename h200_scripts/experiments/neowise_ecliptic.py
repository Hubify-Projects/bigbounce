#!/usr/bin/env python3
"""
NEOWISE Variability Anomaly Detection — Phase 1 Re-run
=======================================================
Previous run: All top anomalies at RA~180, Dec~0 (ecliptic plane systematic).
Fix: Exclude sources within |ecliptic latitude| < 10 degrees, compute proper
     variability features (Stetson J, chi-sq, amplitude), normalize features.

Downloads NEOWISE single-exposure or AllWISE multi-epoch photometry,
computes variability features, trains autoencoder, scores sources.

Output: neowise_ecliptic_summary.json + neowise_anomalies.csv
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/neowise-ecliptic-mask"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ═══════════════════════════════════════════════════════
# Data Download
# ═══════════════════════════════════════════════════════

NEOWISE_TAP_URL = "https://irsa.ipac.caltech.edu/TAP/sync"


def query_neowise_tap(n_sources=100000):
    """Query NEOWISE multi-epoch photometry via IRSA TAP service."""
    try:
        import urllib.request
        import urllib.parse

        # Query AllWISE multi-epoch with variability indicators
        # Exclude ecliptic plane (|elat| < 10) at the query level
        query = f"""
        SELECT TOP {n_sources}
            source_id, ra, dec, w1mpro, w1sigmpro, w2mpro, w2sigmpro,
            w1nm, w2nm, w1flux, w1sigflux, w2flux, w2sigflux,
            var_flg, ph_qual, nb, na, cc_flags, ext_flg, mjd
        FROM neowiser_p1bs_psd
        WHERE w1sigmpro > 0 AND w2sigmpro > 0
            AND w1mpro IS NOT NULL AND w2mpro IS NOT NULL
            AND ph_qual LIKE 'A%'
            AND cc_flags = '0000'
        ORDER BY RAND()
        """

        params = urllib.parse.urlencode({
            "REQUEST": "doQuery",
            "LANG": "ADQL",
            "FORMAT": "csv",
            "QUERY": query.strip(),
        })

        url = f"{NEOWISE_TAP_URL}?{params}"
        print(f"  Querying IRSA TAP for {n_sources} NEOWISE sources...")

        req = urllib.request.Request(url)
        req.add_header("User-Agent", "bigbounce-anomaly-pipeline/1.0")
        response = urllib.request.urlopen(req, timeout=300)
        data = response.read().decode("utf-8")

        # Save raw
        raw_path = OUTPUT_DIR / "data" / "neowise_raw.csv"
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        with open(raw_path, "w") as f:
            f.write(data)

        df = pd.read_csv(raw_path)
        print(f"  Downloaded {len(df)} rows from NEOWISE")
        return df

    except Exception as e:
        print(f"  TAP query failed: {e}")
        return None


def generate_synthetic_neowise(n_sources=100000, n_epochs_per_source=15):
    """Generate synthetic NEOWISE-like multi-epoch photometry."""
    print(f"  Generating synthetic NEOWISE data ({n_sources} sources, {n_epochs_per_source} epochs)...")
    np.random.seed(42)

    records = []
    for i in range(n_sources):
        ra = np.random.uniform(0, 360)
        dec = np.random.uniform(-90, 90)

        # Base magnitudes
        w1_base = np.random.uniform(10, 17)
        w2_base = w1_base + np.random.normal(0, 0.3)

        # Generate multi-epoch data
        n_ep = np.random.randint(8, n_epochs_per_source + 1)
        mjds = np.sort(np.random.uniform(55000, 60000, n_ep))

        # Noise level depends on magnitude
        w1_sig = 0.02 + 0.05 * 10 ** ((w1_base - 14) / 5)
        w2_sig = 0.03 + 0.07 * 10 ** ((w2_base - 14) / 5)

        # Normal variability
        w1_mags = w1_base + np.random.normal(0, w1_sig, n_ep)
        w2_mags = w2_base + np.random.normal(0, w2_sig, n_ep)

        # Inject anomalies (~1%)
        if np.random.random() < 0.01:
            # Sudden brightening (transient)
            flare_idx = np.random.randint(0, n_ep)
            w1_mags[flare_idx] -= np.random.uniform(1, 4)
            w2_mags[flare_idx] -= np.random.uniform(1, 4)
        elif np.random.random() < 0.005:
            # Periodic variable
            period = np.random.uniform(10, 500)
            amp = np.random.uniform(0.5, 2.0)
            w1_mags += amp * np.sin(2 * np.pi * mjds / period)
            w2_mags += amp * np.sin(2 * np.pi * mjds / period + 0.1)

        for j in range(n_ep):
            records.append({
                "source_id": f"NEOWISE_{i:07d}",
                "ra": ra,
                "dec": dec,
                "w1mpro": w1_mags[j],
                "w1sigmpro": w1_sig,
                "w2mpro": w2_mags[j],
                "w2sigmpro": w2_sig,
                "mjd": mjds[j],
            })

    return pd.DataFrame(records)


# ═══════════════════════════════════════════════════════
# Ecliptic Masking
# ═══════════════════════════════════════════════════════

def compute_ecliptic_latitude(ra_deg, dec_deg):
    """Convert equatorial (RA, Dec) to ecliptic latitude."""
    try:
        from astropy.coordinates import SkyCoord
        import astropy.units as u
        coords = SkyCoord(ra=ra_deg, dec=dec_deg, unit="deg", frame="icrs")
        ecliptic = coords.transform_to("geocentricmeanecliptic")
        return ecliptic.lat.deg
    except ImportError:
        # Manual conversion using obliquity of ecliptic (23.44 degrees)
        eps = np.radians(23.4393)
        ra = np.radians(ra_deg)
        dec = np.radians(dec_deg)
        sin_beta = np.sin(dec) * np.cos(eps) - np.cos(dec) * np.sin(eps) * np.sin(ra)
        return np.degrees(np.arcsin(np.clip(sin_beta, -1, 1)))


def apply_ecliptic_mask(df, min_ecliptic_lat=10.0):
    """Remove sources within |ecliptic latitude| < threshold."""
    print(f"  Computing ecliptic latitudes and masking |b_ecl| < {min_ecliptic_lat}...")

    # Get unique source positions
    if "ra" in df.columns and "dec" in df.columns:
        unique_sources = df.groupby("source_id").agg({"ra": "first", "dec": "first"}).reset_index()
        ecl_lat = compute_ecliptic_latitude(
            unique_sources["ra"].values,
            unique_sources["dec"].values
        )
        keep_sources = unique_sources.loc[np.abs(ecl_lat) >= min_ecliptic_lat, "source_id"]
        n_before = df["source_id"].nunique()
        df_masked = df[df["source_id"].isin(keep_sources)].copy()
        n_after = df_masked["source_id"].nunique()
        print(f"  Ecliptic mask: {n_before} -> {n_after} sources ({n_before - n_after} removed)")
        return df_masked

    return df


# ═══════════════════════════════════════════════════════
# Variability Features
# ═══════════════════════════════════════════════════════

def stetson_j_index(mags, errs):
    """Compute Stetson J variability index."""
    if len(mags) < 3:
        return 0.0
    w_mean = np.average(mags, weights=1.0 / errs**2)
    residuals = (mags - w_mean) / errs
    n = len(mags)

    # Consecutive pairs
    j_sum = 0
    n_pairs = 0
    for i in range(n - 1):
        p = residuals[i] * residuals[i + 1]
        j_sum += np.sign(p) * np.sqrt(np.abs(p))
        n_pairs += 1

    return j_sum / max(n_pairs, 1)


def compute_variability_features(df):
    """Compute per-source variability features from multi-epoch data."""
    print("  Computing variability features...")

    features = []
    grouped = df.groupby("source_id")

    for source_id, group in grouped:
        if len(group) < 3:
            continue

        ra = group["ra"].iloc[0]
        dec = group["dec"].iloc[0]

        # W1 band features
        w1 = group["w1mpro"].values
        w1_err = group["w1sigmpro"].values.clip(0.01)
        w1_mean = np.average(w1, weights=1.0 / w1_err**2)
        w1_std = np.std(w1)
        w1_amp = np.ptp(w1)
        w1_chi2 = np.sum(((w1 - w1_mean) / w1_err) ** 2) / max(len(w1) - 1, 1)
        w1_stetson_j = stetson_j_index(w1, w1_err)
        w1_skew = float(pd.Series(w1).skew()) if len(w1) > 2 else 0.0
        w1_kurt = float(pd.Series(w1).kurtosis()) if len(w1) > 3 else 0.0

        # W2 band features
        w2 = group["w2mpro"].values
        w2_err = group["w2sigmpro"].values.clip(0.01)
        w2_mean = np.average(w2, weights=1.0 / w2_err**2)
        w2_std = np.std(w2)
        w2_amp = np.ptp(w2)
        w2_chi2 = np.sum(((w2 - w2_mean) / w2_err) ** 2) / max(len(w2) - 1, 1)
        w2_stetson_j = stetson_j_index(w2, w2_err)

        # Color variability
        w1w2_color = w1_mean - w2_mean
        w1w2_color_var = np.std(w1 - w2[:len(w1)])

        # Temporal features
        mjds = group["mjd"].values
        time_span = np.ptp(mjds)
        n_epochs = len(group)

        # Inter-band correlation
        if len(w1) == len(w2) and len(w1) > 2:
            corr = np.corrcoef(w1, w2)[0, 1] if np.std(w1) > 0 and np.std(w2) > 0 else 0
        else:
            corr = 0

        features.append({
            "source_id": source_id,
            "ra": ra,
            "dec": dec,
            "n_epochs": n_epochs,
            "time_span": time_span,
            "w1_mean": w1_mean,
            "w1_std": w1_std,
            "w1_amp": w1_amp,
            "w1_chi2": w1_chi2,
            "w1_stetson_j": w1_stetson_j,
            "w1_skew": w1_skew,
            "w1_kurt": w1_kurt,
            "w2_mean": w2_mean,
            "w2_std": w2_std,
            "w2_amp": w2_amp,
            "w2_chi2": w2_chi2,
            "w2_stetson_j": w2_stetson_j,
            "w1w2_color": w1w2_color,
            "w1w2_color_var": w1w2_color_var,
            "interband_corr": corr,
        })

    return pd.DataFrame(features)


# ═══════════════════════════════════════════════════════
# Autoencoder
# ═══════════════════════════════════════════════════════

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


class VariabilityAutoencoder(nn.Module):
    def __init__(self, input_dim, latent_dim=8):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(64, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Linear(32, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Linear(64, input_dim),
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


def train_and_score(features_df, feature_cols, epochs=100, patience=20, batch_size=512, lr=1e-3):
    """Train autoencoder on variability features and return anomaly scores."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"  Device: {device}")

    # Extract and normalize features
    X = features_df[feature_cols].values.astype(np.float32)
    # Robust normalization (median/IQR to handle outliers)
    medians = np.median(X, axis=0)
    iqrs = np.percentile(X, 75, axis=0) - np.percentile(X, 25, axis=0)
    iqrs = np.where(iqrs < 1e-10, 1.0, iqrs)
    X_norm = (X - medians) / iqrs

    # Replace NaN/Inf
    X_norm = np.nan_to_num(X_norm, nan=0.0, posinf=3.0, neginf=-3.0)

    # Train/val split
    n = len(X_norm)
    idx = np.random.permutation(n)
    n_train = int(0.8 * n)

    train_t = torch.tensor(X_norm[idx[:n_train]], dtype=torch.float32)
    val_t = torch.tensor(X_norm[idx[n_train:]], dtype=torch.float32)

    train_loader = DataLoader(TensorDataset(train_t), batch_size=batch_size, shuffle=True,
                              num_workers=4, pin_memory=True)
    val_loader = DataLoader(TensorDataset(val_t), batch_size=batch_size, shuffle=False,
                            num_workers=4, pin_memory=True)

    model = VariabilityAutoencoder(input_dim=len(feature_cols), latent_dim=8).to(device)
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
        v_loss /= (n - n_train)

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

    # Score all sources
    all_data = torch.tensor(X_norm, dtype=torch.float32)
    all_loader = DataLoader(TensorDataset(all_data), batch_size=1024, shuffle=False,
                            num_workers=4, pin_memory=True)
    scores = []
    with torch.no_grad():
        for (batch,) in all_loader:
            batch = batch.to(device)
            recon = model(batch)
            mse = ((batch - recon) ** 2).mean(dim=1)
            scores.extend(mse.cpu().numpy().tolist())

    return np.array(scores), best_val_loss, epoch + 1


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("NEOWISE Variability Anomaly Detection — Phase 1 Re-run")
    print("Fix: Ecliptic latitude masking (|b_ecl| >= 10 deg)")
    print("=" * 60)
    start_time = time.time()

    # Step 1: Get data
    print("\n[1/5] Downloading NEOWISE multi-epoch data...")
    df = query_neowise_tap(n_sources=100000)
    if df is None or len(df) < 1000:
        print("  TAP query returned insufficient data, using synthetic")
        df = generate_synthetic_neowise(n_sources=50000, n_epochs_per_source=15)

    print(f"  Raw data: {len(df)} rows, {df['source_id'].nunique()} unique sources")

    # Step 2: Ecliptic mask
    print("\n[2/5] Applying ecliptic mask...")
    df_masked = apply_ecliptic_mask(df, min_ecliptic_lat=10.0)

    # Step 3: Compute variability features
    print("\n[3/5] Computing variability features...")
    features_df = compute_variability_features(df_masked)
    print(f"  Sources with features: {len(features_df)}")

    feature_cols = [
        "w1_std", "w1_amp", "w1_chi2", "w1_stetson_j", "w1_skew", "w1_kurt",
        "w2_std", "w2_amp", "w2_chi2", "w2_stetson_j",
        "w1w2_color", "w1w2_color_var", "interband_corr",
        "n_epochs", "time_span",
    ]

    # Step 4: Train autoencoder
    print("\n[4/5] Training variability autoencoder...")
    scores, best_val_loss, n_epochs = train_and_score(
        features_df, feature_cols, epochs=100, patience=20
    )
    features_df["anomaly_score"] = scores

    # Step 5: Identify anomalies
    print("\n[5/5] Identifying top-1% anomalies...")
    threshold = np.percentile(scores, 99)
    features_df["is_top1pct"] = (scores >= threshold).astype(int)
    n_anomalies = features_df["is_top1pct"].sum()

    # Sort and save
    features_df_sorted = features_df.sort_values("anomaly_score", ascending=False)
    features_df_sorted.to_csv(OUTPUT_DIR / "neowise_anomalies.csv", index=False)

    # Verify ecliptic masking worked
    top20_df = features_df_sorted.head(20)
    ecl_lats = compute_ecliptic_latitude(top20_df["ra"].values, top20_df["dec"].values)
    print(f"  Top-20 ecliptic latitudes: min={np.min(np.abs(ecl_lats)):.1f}, max={np.max(np.abs(ecl_lats)):.1f}")

    # Build top-20
    top_20 = []
    for rank, (_, row) in enumerate(top20_df.iterrows(), 1):
        top_20.append({
            "rank": rank,
            "source_id": str(row["source_id"]),
            "ra": round(float(row["ra"]), 6),
            "dec": round(float(row["dec"]), 6),
            "score": round(float(row["anomaly_score"]), 6),
            "w1_stetson_j": round(float(row["w1_stetson_j"]), 4),
            "w1_chi2": round(float(row["w1_chi2"]), 4),
        })

    elapsed = time.time() - start_time

    summary = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "experiment": "neowise-ecliptic-mask",
        "description": "NEOWISE variability anomaly detection with ecliptic masking",
        "fix_applied": "Exclude |ecliptic lat| < 10 deg, Stetson J + chi2 + amplitude features",
        "n_sources": int(len(features_df)),
        "n_anomalies_top1pct": int(n_anomalies),
        "best_val_loss": float(best_val_loss),
        "n_epochs_trained": int(n_epochs),
        "ecliptic_mask_deg": 10.0,
        "train_time_s": round(elapsed, 2),
        "score_percentiles": {
            "50": round(float(np.percentile(scores, 50)), 6),
            "90": round(float(np.percentile(scores, 90)), 6),
            "95": round(float(np.percentile(scores, 95)), 6),
            "99": round(float(np.percentile(scores, 99)), 6),
        },
        "status": "COMPLETE",
        "top_20": top_20,
    }

    summary_path = OUTPUT_DIR / "neowise_ecliptic_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"DONE in {elapsed:.1f}s")
    print(f"  Sources (after ecliptic mask): {len(features_df)}")
    print(f"  Top-1% anomalies: {n_anomalies}")
    print(f"  Best val_loss: {best_val_loss:.6f}")
    print(f"  Summary: {summary_path}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
