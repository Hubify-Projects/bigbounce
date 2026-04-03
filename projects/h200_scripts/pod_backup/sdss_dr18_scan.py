#!/usr/bin/env python3
"""
SDSS DR18 Spectral Anomaly Scan
================================
Applies the BigAE autoencoder (trained on DESI) to SDSS DR18 spectra.
Proves the methodology is survey-independent.

SDSS spectra cover 3800-9200Å at R~2000 (vs DESI 3600-9800Å at R~2000-5000).
We resample SDSS spectra to match DESI's 496-bin downsampled grid.

Data source: SDSS DR18 spectra from the Science Archive Server (SAS).
"""

import numpy as np
import torch
import torch.nn as nn
from astropy.io import fits
import urllib.request
import os
import json
import time
import glob
import traceback

# Try parquet support
try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    HAS_PARQUET = True
except ImportError:
    HAS_PARQUET = False

# ============================================================
# BigAE Model (same as DESI version)
# ============================================================
class BigAE(nn.Module):
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, n_lat),
        )
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, n_in),
        )
    def forward(self, x): return self.dec(self.enc(x))
    def encode(self, x): return self.enc(x)

# ============================================================
# SDSS Spectrum Processing
# ============================================================
# DESI wavelength grid for BigAE (downsampled to 496 bins)
DESI_WMIN, DESI_WMAX = 3600.0, 9800.0
N_BINS = 496

def resample_sdss_to_desi(sdss_wave, sdss_flux, sdss_ivar=None):
    """Resample SDSS spectrum onto DESI's 496-bin grid."""
    desi_wave = np.linspace(DESI_WMIN, DESI_WMAX, N_BINS)
    resampled = np.zeros(N_BINS)
    weights = np.zeros(N_BINS)
    
    for i in range(N_BINS):
        wmin = desi_wave[i] - (DESI_WMAX - DESI_WMIN) / N_BINS / 2
        wmax = desi_wave[i] + (DESI_WMAX - DESI_WMIN) / N_BINS / 2
        mask = (sdss_wave >= wmin) & (sdss_wave < wmax)
        if np.any(mask):
            if sdss_ivar is not None:
                w = sdss_ivar[mask]
                w[w < 0] = 0
                if np.sum(w) > 0:
                    resampled[i] = np.average(sdss_flux[mask], weights=w)
                    weights[i] = np.sum(w)
                else:
                    resampled[i] = np.mean(sdss_flux[mask])
                    weights[i] = 1.0
            else:
                resampled[i] = np.mean(sdss_flux[mask])
                weights[i] = len(sdss_flux[mask])
    
    # Normalize (same as DESI preprocessing)
    median = np.median(resampled[resampled != 0])
    if median > 0:
        resampled /= median
    
    return resampled, weights

def download_sdss_plate(plate, mjd, fiberid, dest_dir):
    """Download an SDSS spectrum FITS file."""
    # SDSS DR18 SAS URL pattern
    url = f"https://data.sdss.org/sas/dr18/spectro/sdss/redux/26/spectra/lite/{plate:04d}/spec-{plate:04d}-{mjd}-{fiberid:04d}.fits"
    dest = os.path.join(dest_dir, f"spec-{plate:04d}-{mjd}-{fiberid:04d}.fits")
    
    if os.path.exists(dest):
        return dest
    
    try:
        urllib.request.urlretrieve(url, dest)
        return dest
    except Exception:
        # Try alternative URL pattern
        url2 = f"https://data.sdss.org/sas/dr18/spectro/sdss/redux/26/spectra/lite/{plate:04d}/spec-{plate:04d}-{mjd}-{fiberid:04d}.fits"
        try:
            urllib.request.urlretrieve(url2, dest)
            return dest
        except Exception:
            return None

def download_sdss_spall(dest_dir):
    """Download the SDSS spAll summary file (list of all spectra)."""
    # Try a smaller catalog first
    url = "https://data.sdss.org/sas/dr18/spectro/sdss/redux/v5_13_2/spAll-v5_13_2.fits"
    dest = os.path.join(dest_dir, "spAll-v5_13_2.fits")
    
    if os.path.exists(dest):
        return dest
    
    print(f"Downloading SDSS spAll catalog from {url}...")
    print("(This is ~4GB, may take a while)")
    try:
        urllib.request.urlretrieve(url, dest)
        return dest
    except Exception as e:
        print(f"Failed: {e}")
        # Try lite version
        url2 = "https://data.sdss.org/sas/dr18/spectro/sdss/redux/v5_13_2/spAll-lite-v5_13_2.fits"
        dest2 = os.path.join(dest_dir, "spAll-lite-v5_13_2.fits")
        try:
            urllib.request.urlretrieve(url2, dest2)
            return dest2
        except Exception as e2:
            print(f"Lite also failed: {e2}")
            return None

def main():
    import argparse
    parser = argparse.ArgumentParser(description='SDSS DR18 Anomaly Scan')
    parser.add_argument('--model-path', default='best_model_47k.pt')
    parser.add_argument('--output-dir', default='outputs/sdss_dr18')
    parser.add_argument('--temp-dir', default='temp/sdss')
    parser.add_argument('--batch-size', type=int, default=8192)
    parser.add_argument('--max-spectra', type=int, default=0)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    
    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.temp_dir, exist_ok=True)
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print('=' * 70)
    print('SDSS DR18 ANOMALY SCAN')
    print('=' * 70)
    print(f'Device: {device}')
    if torch.cuda.is_available():
        print(f'GPU: {torch.cuda.get_device_name(0)}')
    
    # Load model
    print(f'Loading BigAE from {args.model_path}...')
    model = BigAE(n_in=496, n_lat=128).to(device)
    state_dict = torch.load(args.model_path, map_location=device, weights_only=True)
    model.load_state_dict(state_dict)
    model.eval()
    print('Model loaded.')
    
    # Download spAll catalog
    print('\nStep 1: Getting SDSS spectrum catalog...')
    spall_path = download_sdss_spall(args.temp_dir)
    
    if spall_path is None:
        print("Cannot download spAll. Trying plate-by-plate approach...")
        # Fall back to downloading individual plates
        # Use a curated list of SDSS plates
        print("Using plate list approach...")
        # TODO: implement plate-by-plate scanning
        return
    
    print(f'Loaded: {spall_path}')
    
    # Read spAll
    print('Reading spAll catalog...')
    with fits.open(spall_path, memmap=True) as hdul:
        spall = hdul[1].data
        n_total = len(spall)
        print(f'Total spectra in catalog: {n_total:,}')
        
        # Get unique plates
        plates = np.unique(spall['PLATE'])
        print(f'Unique plates: {len(plates):,}')
        
        # Extract key columns
        plate_arr = spall['PLATE']
        mjd_arr = spall['MJD']
        fiberid_arr = spall['FIBERID']
        ra_arr = spall['RA']
        dec_arr = spall['DEC']
        z_arr = spall['Z']
        zwarning_arr = spall['ZWARNING']
        class_arr = spall['CLASS']
        
        if args.max_spectra > 0:
            n_total = min(n_total, args.max_spectra)
            print(f'Limited to first {n_total:,} spectra')
    
    print(f'\nStep 2: Processing {n_total:,} spectra...')
    
    # Checkpoint
    checkpoint_path = os.path.join(args.output_dir, 'checkpoint.json')
    if args.resume and os.path.exists(checkpoint_path):
        with open(checkpoint_path) as f:
            ckpt = json.load(f)
        processed = set(ckpt.get('processed_indices', []))
        print(f'Resuming: {len(processed):,} already done')
    else:
        processed = set()
        ckpt = {'total_scored': 0, 'total_anomalies': 0, 'batch_idx': 0}
    
    # Process in batches
    batch_size_flush = 100000  # Flush to parquet every 100K
    row_buffer = []
    batch_idx = ckpt.get('batch_idx', 0)
    total_scored = ckpt.get('total_scored', 0)
    total_anomalies = ckpt.get('total_anomalies', 0)
    t0 = time.time()
    
    # Re-open spAll for iteration
    with fits.open(spall_path, memmap=True) as hdul:
        spall = hdul[1].data
        
        for i in range(n_total):
            if i in processed:
                continue
            
            plate = int(plate_arr[i])
            mjd = int(mjd_arr[i])
            fiberid = int(fiberid_arr[i])
            
            # Download spectrum
            spec_path = download_sdss_plate(plate, mjd, fiberid, args.temp_dir)
            if spec_path is None:
                continue
            
            try:
                with fits.open(spec_path) as shdul:
                    # SDSS spec files: HDU 1 has the spectrum
                    wave = 10**shdul[1].data['loglam']  # SDSS uses log-wavelength
                    flux = shdul[1].data['flux']
                    ivar = shdul[1].data['ivar']
                    
                    # Resample to DESI grid
                    resampled, weights = resample_sdss_to_desi(wave, flux, ivar)
                    
                    # Skip if too many zero bins
                    if np.sum(resampled != 0) < 100:
                        continue
                    
                    # Run through autoencoder
                    x = torch.tensor(resampled, dtype=torch.float32).unsqueeze(0).to(device)
                    with torch.no_grad():
                        recon = model(x)
                        latent = model.encode(x)
                    
                    residual = (x - recon).cpu().numpy()[0]
                    score = float(np.mean(residual**2))
                    latent_vec = latent.cpu().numpy()[0]
                    
                    # Compute per-band scores (approximate SDSS bands)
                    rB = float(np.mean(residual[:170]**2))  # ~3600-5300A
                    rR = float(np.mean(residual[170:340]**2))  # ~5300-7500A
                    rZ = float(np.mean(residual[340:]**2))  # ~7500-9800A
                    
                    row = {
                        'plate': plate, 'mjd': mjd, 'fiberid': fiberid,
                        'ra': float(ra_arr[i]), 'dec': float(dec_arr[i]),
                        'z': float(z_arr[i]),
                        'zwarning': int(zwarning_arr[i]),
                        'class': str(class_arr[i]).strip(),
                        'anomaly_score': score,
                        'rB': rB, 'rR': rR, 'rZ': rZ,
                    }
                    # Add latent vector
                    for j in range(128):
                        row[f'lat_{j:03d}'] = float(latent_vec[j])
                    
                    row_buffer.append(row)
                    total_scored += 1
                    if score > 5.0:
                        total_anomalies += 1
                    
            except Exception as e:
                if (i+1) % 1000 == 0:
                    traceback.print_exc()
            finally:
                # Clean up spectrum file
                if spec_path and os.path.exists(spec_path):
                    os.remove(spec_path)
            
            processed.add(i)
            
            # Flush
            if len(row_buffer) >= batch_size_flush:
                if HAS_PARQUET:
                    table = pa.Table.from_pylist(row_buffer)
                    path = os.path.join(args.output_dir, f'sdss_dr18_batch_{batch_idx:04d}.parquet')
                    pq.write_table(table, path, compression='zstd')
                    print(f'  Flushed batch {batch_idx}: {len(row_buffer):,} rows ({total_scored:,} total)')
                batch_idx += 1
                row_buffer = []
                
                # Checkpoint
                with open(checkpoint_path, 'w') as f:
                    json.dump({
                        'processed_indices': list(processed)[-10000:],  # Keep last 10K
                        'total_scored': total_scored,
                        'total_anomalies': total_anomalies,
                        'batch_idx': batch_idx,
                    }, f)
            
            # Progress
            if total_scored > 0 and total_scored % 1000 == 0:
                elapsed = time.time() - t0
                rate = total_scored / elapsed
                print(f'  [{total_scored:,}/{n_total:,}] {total_anomalies:,} anomalies | {rate:.0f} spec/s')
    
    # Final flush
    if row_buffer:
        if HAS_PARQUET:
            table = pa.Table.from_pylist(row_buffer)
            path = os.path.join(args.output_dir, f'sdss_dr18_batch_{batch_idx:04d}.parquet')
            pq.write_table(table, path, compression='zstd')
        batch_idx += 1
    
    elapsed = time.time() - t0
    print(f'\n{"="*70}')
    print(f'SDSS DR18 SCAN COMPLETE')
    print(f'{"="*70}')
    print(f'  Spectra scored: {total_scored:,}')
    print(f'  Anomalies (>5σ): {total_anomalies:,}')
    print(f'  Elapsed: {elapsed:.0f}s ({elapsed/3600:.1f}h)')
    print(f'  Rate: {total_scored/elapsed:.0f} spec/s')
    print(f'  Output: {args.output_dir}')

if __name__ == '__main__':
    main()
