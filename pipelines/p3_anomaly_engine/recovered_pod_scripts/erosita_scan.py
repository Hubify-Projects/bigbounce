#!/usr/bin/env python3
"""
eROSITA DR1 X-ray Anomaly Detection
930,203 X-ray sources with 529 columns — tabular anomaly detection.
Uses autoencoder on normalized multi-band fluxes/rates/counts.
"""
import numpy as np, torch, torch.nn as nn, os, json, time, urllib.request, tarfile
try:
    import pyarrow as pa, pyarrow.parquet as pq
    HAS_PARQUET = True
except:
    HAS_PARQUET = False

from astropy.io import fits
from astropy.table import Table

# Feature columns to use for anomaly detection
# Multi-band count rates and fluxes across all eROSITA energy bands
RATE_COLS = [f'ML_RATE_{b}' for b in ['1','P1','P2','P3','P4','P5','P6','P7','P8','P9','S']]
FLUX_COLS = [f'ML_FLUX_{b}' for b in ['1','P1','P2','P3','P4','P5','P6','P7','P8','P9','S']]
CTS_COLS = [f'ML_CTS_{b}' for b in ['1','P1','P2','P3','P4','P5','P6','P7','P8','P9','S']]
LIKE_COLS = [f'DET_LIKE_{b}' for b in ['1','P1','P2','P3','P4','P5','P6','P7','P8','P9','S']]
META_COLS = ['EXT', 'EXT_LIKE', 'POS_ERR']

ALL_FEATURE_COLS = RATE_COLS + FLUX_COLS + CTS_COLS + LIKE_COLS + META_COLS
N_FEATURES = len(ALL_FEATURE_COLS)  # 47

class XRayAE(nn.Module):
    """Autoencoder for tabular X-ray source features."""
    def __init__(self, n_in, n_lat=16):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 128), nn.BatchNorm1d(128), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(128, 64), nn.BatchNorm1d(64), nn.ReLU(), nn.Dropout(0.05),
            nn.Linear(64, 32), nn.ReLU(),
            nn.Linear(32, n_lat)
        )
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 32), nn.ReLU(),
            nn.Linear(32, 64), nn.BatchNorm1d(64), nn.ReLU(), nn.Dropout(0.05),
            nn.Linear(64, 128), nn.BatchNorm1d(128), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(128, n_in)
        )
    def forward(self, x): return self.dec(self.enc(x))
    def encode(self, x): return self.enc(x)


def download_catalog(out_dir):
    """Download eROSITA DR1 main catalog."""
    fits_path = os.path.join(out_dir, 'eRASS1_Main.v1.1.fits')
    if os.path.exists(fits_path):
        print(f'Catalog already exists: {fits_path}')
        return fits_path

    tgz_path = os.path.join(out_dir, 'eRASS1_Main.v1.2.fits.tar.gz')
    extracted = os.path.join(out_dir, 'eRASS1_Main.v1.2.fits')
    if os.path.exists(extracted):
        return extracted

    # Try v1.2 compressed first (613 MB)
    url = 'https://erosita.mpe.mpg.de/dr1/AllSkySurveyData_dr1/Catalogues_dr1/MerloniA_DR1/eRASS1_Main.v1.2.fits.tar.gz'
    print(f'Downloading eROSITA DR1 catalog ({url})...')
    try:
        urllib.request.urlretrieve(url, tgz_path)
        print(f'Download complete. Extracting...')
        with tarfile.open(tgz_path, 'r:gz') as tar:
            tar.extractall(path=out_dir)
        # Find the extracted FITS file
        for root, dirs, files in os.walk(out_dir):
            for f in files:
                if f.endswith('.fits') and 'Main' in f:
                    found = os.path.join(root, f)
                    print(f'Extracted: {found}')
                    return found
    except Exception as e:
        print(f'v1.2 download failed: {e}')

    # Fallback to v1.1 uncompressed (959 MB)
    url2 = 'https://erosita.mpe.mpg.de/dr1/AllSkySurveyData_dr1/Catalogues_dr1/MerloniA_DR1/eRASS1_Main.v1.1.fits'
    print(f'Trying v1.1 ({url2})...')
    urllib.request.urlretrieve(url2, fits_path)
    return fits_path


def extract_features(table):
    """Extract and normalize feature matrix from the catalog."""
    n = len(table)
    features = np.zeros((n, N_FEATURES), dtype=np.float32)

    for i, col in enumerate(ALL_FEATURE_COLS):
        if col in table.colnames:
            vals = np.array(table[col], dtype=np.float64)
            # Replace NaN/inf with 0
            vals = np.nan_to_num(vals, nan=0.0, posinf=0.0, neginf=0.0)
            features[:, i] = vals.astype(np.float32)

    # Log-scale the rates, fluxes, counts (all positive)
    n_log = len(RATE_COLS) + len(FLUX_COLS) + len(CTS_COLS)
    features[:, :n_log] = np.log1p(np.abs(features[:, :n_log])) * np.sign(features[:, :n_log])

    # Normalize each column to zero mean, unit variance
    means = np.mean(features, axis=0)
    stds = np.std(features, axis=0)
    stds[stds < 1e-10] = 1.0
    features = (features - means) / stds

    return features, means, stds


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Device: {device}')
    out_dir = '/workspace/bigbounce/outputs/erosita'
    os.makedirs(out_dir, exist_ok=True)

    # Download catalog
    fits_path = download_catalog(out_dir)
    print(f'Reading catalog: {fits_path}')
    table = Table.read(fits_path)
    n_src = len(table)
    print(f'Sources: {n_src:,} ({len(table.colnames)} columns)')

    # Extract features
    print(f'Extracting {N_FEATURES} features...')
    features, means, stds = extract_features(table)
    print(f'Feature matrix: {features.shape}')

    # Train autoencoder
    N_LAT = 16
    model = XRayAE(N_FEATURES, N_LAT).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)

    # Train/val split (80/20 random)
    np.random.seed(42)
    idx = np.random.permutation(n_src)
    n_train = int(0.8 * n_src)
    train_idx, val_idx = idx[:n_train], idx[n_train:]

    train_data = torch.tensor(features[train_idx]).to(device)
    val_data = torch.tensor(features[val_idx]).to(device)
    all_data = torch.tensor(features).to(device)

    BATCH = 8192
    EPOCHS = 100
    best_val_loss = float('inf')
    patience = 15
    no_improve = 0

    print(f'\nTraining XRayAE: {N_FEATURES}→128→64→32→{N_LAT}→32→64→128→{N_FEATURES}')
    print(f'Train: {n_train:,}, Val: {n_src - n_train:,}, Epochs: {EPOCHS}\n')

    t0 = time.time()
    for epoch in range(EPOCHS):
        model.train()
        perm = torch.randperm(n_train, device=device)
        epoch_loss = 0.0
        n_batches = 0
        for i in range(0, n_train, BATCH):
            batch = train_data[perm[i:i+BATCH]]
            recon = model(batch)
            loss = nn.functional.mse_loss(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1
        scheduler.step()

        # Validation
        model.eval()
        with torch.no_grad():
            val_recon = model(val_data)
            val_loss = nn.functional.mse_loss(val_recon, val_data).item()

        avg_train = epoch_loss / n_batches
        if (epoch + 1) % 10 == 0 or epoch == 0:
            print(f'  Epoch {epoch+1:3d}: train={avg_train:.6f}, val={val_loss:.6f}')

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            no_improve = 0
            torch.save(model.state_dict(), os.path.join(out_dir, 'xray_ae_model.pt'))
        else:
            no_improve += 1
            if no_improve >= patience:
                print(f'  Early stopping at epoch {epoch+1}')
                break

    train_time = time.time() - t0
    print(f'\nTraining done: {train_time:.1f}s, best val loss: {best_val_loss:.6f}')

    # Load best model and score everything
    model.load_state_dict(torch.load(os.path.join(out_dir, 'xray_ae_model.pt'), weights_only=True))
    model.eval()

    print('Scoring all sources...')
    all_scores = []
    all_latents = []
    with torch.no_grad():
        for i in range(0, n_src, BATCH):
            batch = all_data[i:i+BATCH]
            recon = model(batch)
            latent = model.encode(batch)
            scores = torch.mean((batch - recon)**2, dim=1)
            all_scores.append(scores.cpu().numpy())
            all_latents.append(latent.cpu().numpy())

    scores = np.concatenate(all_scores)
    latents = np.concatenate(all_latents)

    # Build output catalog
    print('Building output catalog...')
    rows = []
    for i in range(n_src):
        row = {
            'iauname': str(table['IAUNAME'][i]) if 'IAUNAME' in table.colnames else f'src_{i}',
            'ra': float(table['RA'][i]),
            'dec': float(table['DEC'][i]),
            'anomaly_score': float(scores[i]),
            'ml_flux_1': float(table['ML_FLUX_1'][i]) if 'ML_FLUX_1' in table.colnames else 0.0,
            'ml_rate_1': float(table['ML_RATE_1'][i]) if 'ML_RATE_1' in table.colnames else 0.0,
            'det_like_1': float(table['DET_LIKE_1'][i]) if 'DET_LIKE_1' in table.colnames else 0.0,
            'ext': float(table['EXT'][i]) if 'EXT' in table.colnames else 0.0,
            'ext_like': float(table['EXT_LIKE'][i]) if 'EXT_LIKE' in table.colnames else 0.0,
            'pos_err': float(table['POS_ERR'][i]) if 'POS_ERR' in table.colnames else 0.0,
        }
        for j in range(N_LAT):
            row[f'lat_{j:02d}'] = float(latents[i, j])
        rows.append(row)

    if HAS_PARQUET:
        pq.write_table(pa.Table.from_pylist(rows), os.path.join(out_dir, 'erosita_anomalies.parquet'), compression='zstd')
        print(f'Saved: erosita_anomalies.parquet')

    # Summary
    threshold = np.percentile(scores, 99)  # top 1%
    n_anom = int(np.sum(scores > threshold))
    top100_idx = np.argsort(scores)[-100:][::-1]

    summary = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'n_sources': n_src,
        'n_features': N_FEATURES,
        'latent_dim': N_LAT,
        'train_time_s': train_time,
        'best_val_loss': best_val_loss,
        'anomaly_threshold_99pct': float(threshold),
        'n_anomalies_top1pct': n_anom,
        'mean_score': float(np.mean(scores)),
        'median_score': float(np.median(scores)),
        'max_score': float(np.max(scores)),
        'top_20': [
            {
                'rank': k+1,
                'iauname': rows[int(idx)]['iauname'],
                'ra': rows[int(idx)]['ra'],
                'dec': rows[int(idx)]['dec'],
                'anomaly_score': rows[int(idx)]['anomaly_score'],
                'ml_flux_1': rows[int(idx)]['ml_flux_1'],
                'det_like_1': rows[int(idx)]['det_like_1'],
            }
            for k, idx in enumerate(top100_idx[:20])
        ]
    }

    with open(os.path.join(out_dir, 'erosita_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'\nSummary saved. Top 1% threshold: {threshold:.4f}')
    print(f'Total anomalies (top 1%): {n_anom:,}')
    print(f'\nTop 10 X-ray anomalies:')
    for item in summary['top_20'][:10]:
        print(f"  #{item['rank']}: {item['iauname']}  score={item['anomaly_score']:.4f}  flux={item['ml_flux_1']:.2e}  RA={item['ra']:.4f} DEC={item['dec']:.4f}")

    print(f'\n{"="*60}\nCOMPLETE: {n_src:,} X-ray sources scored\n{"="*60}')

if __name__ == '__main__':
    main()
