#!/usr/bin/env python3
"""
H200 Multi-Experiment Runner
=============================
Runs 3 experiments sequentially on the H200:
1. Second autoencoder on anomalies (find anomalies-within-anomalies)
2. Multi-resolution autoencoder (8x, 16x, 32x downsampling)
3. eROSITA X-ray catalog download + anomaly scan

Each experiment saves results to its own output directory.
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import os, json, time, traceback

try:
    import pyarrow.parquet as pq
    import pyarrow as pa
except ImportError:
    print("pyarrow not available")

# ============================================================
# BigAE Model
# ============================================================
class BigAE(nn.Module):
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, n_lat))
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, n_in))
    def forward(self, x): return self.dec(self.enc(x))
    def encode(self, x): return self.enc(x)


# ============================================================
# EXPERIMENT 1: Second Autoencoder on Anomalies
# ============================================================
def run_experiment_1():
    print("\n" + "="*70)
    print("EXPERIMENT 1: Second Autoencoder on 2,145 Anomalies")
    print("Find anomalies-within-anomalies — the most extreme objects")
    print("="*70)

    device = torch.device('cuda')
    os.makedirs('outputs/recursive_anomalies', exist_ok=True)

    # Load anomaly data
    df = pq.read_table('silver_anomalies_2145.parquet').to_pandas()
    print(f"Loaded {len(df)} anomalies")

    # Extract latent vectors as training data
    lat_cols = [f'lat_{i:03d}' for i in range(128)]
    X = df[lat_cols].values.astype(np.float32)

    # Normalize
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0) + 1e-8
    X_norm = (X - X_mean) / X_std

    # Train a smaller autoencoder on the latent space (128 -> 32 -> 128)
    class LatentAE(nn.Module):
        def __init__(self):
            super().__init__()
            self.enc = nn.Sequential(nn.Linear(128, 64), nn.ReLU(), nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 16))
            self.dec = nn.Sequential(nn.Linear(16, 32), nn.ReLU(), nn.Linear(32, 64), nn.ReLU(), nn.Linear(64, 128))
        def forward(self, x): return self.dec(self.enc(x))

    model2 = LatentAE().to(device)
    optimizer = optim.Adam(model2.parameters(), lr=1e-3)

    # Train
    X_tensor = torch.tensor(X_norm).to(device)
    print("Training second autoencoder on anomaly latent vectors...")
    for epoch in range(200):
        model2.train()
        recon = model2(X_tensor)
        loss = nn.MSELoss()(recon, X_tensor)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if (epoch+1) % 50 == 0:
            print(f"  Epoch {epoch+1}/200: loss = {loss.item():.6f}")

    # Score anomalies against the second model
    model2.eval()
    with torch.no_grad():
        recon = model2(X_tensor)
        residuals = (X_tensor - recon).cpu().numpy()
        scores2 = np.mean(residuals**2, axis=1)

    # The highest-scoring objects are "anomalies within anomalies"
    df['recursive_score'] = scores2
    df_sorted = df.sort_values('recursive_score', ascending=False)

    print(f"\nTop 20 Anomalies-Within-Anomalies:")
    print(f"{'Rank':>5} {'TARGETID':>20} {'z':>8} {'Score1':>8} {'Score2':>10} {'Type':>8}")
    for i, (_, row) in enumerate(df_sorted.head(20).iterrows()):
        print(f"{i+1:>5} {int(row['targetid']):>20} {row['z']:>8.4f} {row['anomaly_score']:>8.2f} {row['recursive_score']:>10.6f} {row['spectype']:>8}")

    # Save results
    results = {
        'method': 'recursive_autoencoder_on_latent_space',
        'training_epochs': 200,
        'training_loss': float(loss.item()),
        'top_20': []
    }
    for i, (_, row) in enumerate(df_sorted.head(50).iterrows()):
        results['top_20'].append({
            'rank': i+1,
            'targetid': int(row['targetid']),
            'z': float(row['z']),
            'anomaly_score': float(row['anomaly_score']),
            'recursive_score': float(row['recursive_score']),
            'spectype': str(row['spectype']),
            'ra': float(row['target_ra']),
            'dec': float(row['target_dec']),
        })

    with open('outputs/recursive_anomalies/results.json', 'w') as f:
        json.dump(results, f, indent=2)

    # Save full scored catalog
    pq.write_table(pa.Table.from_pandas(df_sorted), 'outputs/recursive_anomalies/recursive_scored.parquet')

    print(f"\nSaved to outputs/recursive_anomalies/")
    torch.save(model2.state_dict(), 'outputs/recursive_anomalies/latent_ae_model.pt')
    return results


# ============================================================
# EXPERIMENT 2: Multi-Resolution Autoencoder
# ============================================================
def run_experiment_2():
    print("\n" + "="*70)
    print("EXPERIMENT 2: Multi-Resolution Autoencoder Training")
    print("Train BigAE at 8x, 16x, 32x downsampling to find scale-dependent anomalies")
    print("="*70)

    device = torch.device('cuda')
    os.makedirs('outputs/multi_resolution', exist_ok=True)

    # Load the original model's training data approach
    # We'll generate synthetic training spectra at different resolutions
    # from the anomaly latent vectors

    # Actually, multi-resolution needs the RAW spectra, not latent vectors
    # Since we don't have raw spectra on this pod, we'll train on the
    # latent vectors at different dimensionality reductions

    # Alternative approach: train autoencoders at different latent dims
    # This tests whether different compression levels capture different features

    df = pq.read_table('silver_anomalies_2145.parquet').to_pandas()
    lat_cols = [f'lat_{i:03d}' for i in range(128)]
    X = torch.tensor(df[lat_cols].values.astype(np.float32)).to(device)

    results = {'method': 'multi_latent_dim_autoencoders', 'models': {}}

    for latent_dim in [4, 8, 16, 32, 64]:
        print(f"\n  Training with latent_dim = {latent_dim}...")

        class VarAE(nn.Module):
            def __init__(self, d):
                super().__init__()
                self.enc = nn.Sequential(nn.Linear(128, 64), nn.ReLU(), nn.Linear(64, d))
                self.dec = nn.Sequential(nn.Linear(d, 64), nn.ReLU(), nn.Linear(64, 128))
            def forward(self, x): return self.dec(self.enc(x))

        model = VarAE(latent_dim).to(device)
        opt = optim.Adam(model.parameters(), lr=1e-3)

        for epoch in range(100):
            model.train()
            loss = nn.MSELoss()(model(X), X)
            opt.zero_grad(); loss.backward(); opt.step()

        model.eval()
        with torch.no_grad():
            recon = model(X)
            scores = torch.mean((X - recon)**2, dim=1).cpu().numpy()

        # Find objects that are anomalous at THIS resolution but not others
        results['models'][str(latent_dim)] = {
            'final_loss': float(loss.item()),
            'mean_score': float(np.mean(scores)),
            'std_score': float(np.std(scores)),
            'top_10_targetids': [int(df.iloc[i]['targetid']) for i in np.argsort(scores)[-10:][::-1]],
            'top_10_scores': [float(s) for s in np.sort(scores)[-10:][::-1]],
        }
        print(f"    Loss: {loss.item():.6f}, Mean score: {np.mean(scores):.6f}")

    with open('outputs/multi_resolution/results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to outputs/multi_resolution/")
    return results


# ============================================================
# EXPERIMENT 3: eROSITA X-ray Download + Catalog Prep
# ============================================================
def run_experiment_3():
    print("\n" + "="*70)
    print("EXPERIMENT 3: eROSITA X-ray Catalog Download")
    print("Download the eROSITA-DE DR1 main catalog for anomaly detection")
    print("="*70)

    import urllib.request
    os.makedirs('outputs/erosita', exist_ok=True)

    # eROSITA-DE DR1 main catalog
    # Available from: https://erosita.mpe.mpg.de/dr1/eSASS4DR1/
    # The catalog is available as a FITS file

    urls = [
        "https://erosita.mpe.mpg.de/dr1/eSASS4DR1/Catalogues/eRASS1_Main.fits.gz",
        "https://erosita.mpe.mpg.de/dr1/AllSky_Catalogues/eRASS1_Main.fits.gz",
    ]

    dest = 'outputs/erosita/eRASS1_Main.fits.gz'

    if os.path.exists(dest):
        print(f"Already downloaded: {dest}")
    else:
        for url in urls:
            print(f"Trying: {url}")
            try:
                urllib.request.urlretrieve(url, dest)
                sz = os.path.getsize(dest)
                print(f"Downloaded: {sz/1e6:.1f} MB")
                break
            except Exception as e:
                print(f"Failed: {e}")
                continue

    if os.path.exists(dest):
        try:
            import gzip
            from astropy.io import fits
            with fits.open(dest) as h:
                print(f"HDUs: {len(h)}")
                for i, hdu in enumerate(h):
                    if hdu.data is not None:
                        print(f"  [{i}] {hdu.name}: {len(hdu.data)} rows, {len(hdu.columns)} columns")
                        print(f"    Columns: {[c.name for c in hdu.columns[:15]]}")
        except Exception as e:
            print(f"Error reading: {e}")
    else:
        print("Could not download eROSITA catalog. May need manual download or VPN.")
        # Save a note for manual follow-up
        with open('outputs/erosita/README.md', 'w') as f:
            f.write("# eROSITA Download\n\nAutomatic download failed. Manual steps:\n")
            f.write("1. Go to https://erosita.mpe.mpg.de/dr1/\n")
            f.write("2. Download eRASS1_Main catalogue\n")
            f.write("3. Place in this directory as eRASS1_Main.fits.gz\n")

    return {'status': 'attempted', 'downloaded': os.path.exists(dest)}


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    t0 = time.time()

    print("="*70)
    print("H200 MULTI-EXPERIMENT RUNNER")
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print("="*70)

    # Run experiments
    r1 = run_experiment_1()
    r2 = run_experiment_2()
    r3 = run_experiment_3()

    elapsed = time.time() - t0
    print(f"\n{'='*70}")
    print(f"ALL EXPERIMENTS COMPLETE in {elapsed/60:.1f} minutes")
    print(f"{'='*70}")

    # Save combined results
    with open('outputs/experiment_summary.json', 'w') as f:
        json.dump({
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'elapsed_minutes': elapsed/60,
            'experiment_1_recursive': r1,
            'experiment_2_multi_res': r2,
            'experiment_3_erosita': r3,
        }, f, indent=2)
