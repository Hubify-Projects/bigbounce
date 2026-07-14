#!/usr/bin/env python3
"""
Pipeline B: DESI DR1 Full-Scale GPU Inference

Scores ALL 18.7 million DESI DR1 spectra using the trained BigAE model
on a GPU pod for 100x faster inference.

Architecture:
  1. Download DR1 healpix coadd files in batches
  2. Load + downsample spectra (CPU)
  3. Score through BigAE on GPU (batch size 8192)
  4. Save anomalies (score > 5.0) to JSON
  5. Delete raw FITS
  6. Repeat until all healpix pixels processed

Expected:
  - 18.7M spectra / 8192 batch / ~0.01s per batch = ~23 min inference
  - Download is the bottleneck (~4 days for all coadd files)
  - Anomalies at score > 7: ~18,000
  - Genuinely novel (not in SIMBAD): ~3,000-5,000

Usage:
  python 13_desi_dr1_gpu_inference.py --threshold 5.0 --batch-size 8192
"""

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from astropy.io import fits
import urllib.request
import re
import os
import json
import time
import glob
import shutil
import argparse


class BigAE(nn.Module):
    """Same architecture as the trained model."""
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, n_lat))
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, n_in))

    def forward(self, x):
        return self.dec(self.enc(x))


def downsample(arr, factor=16):
    """Downsample spectral axis by averaging bins."""
    n = arr.shape[-1] // factor * factor
    return arr[..., :n].reshape(*arr.shape[:-1], -1, factor).mean(axis=-1)


def process_coadd(fpath, model, device, threshold=5.0):
    """Process a single coadd file and return high-score anomalies."""
    sp = fits.open(fpath)
    fm = sp['FIBERMAP'].data

    # Downsample and concatenate arms
    flux = np.hstack([
        downsample(sp['B_FLUX'].data),
        downsample(sp['R_FLUX'].data),
        downsample(sp['Z_FLUX'].data)
    ])
    flux = np.nan_to_num(flux, nan=0, posinf=0, neginf=0).astype(np.float32)

    # Normalize per-spectrum
    med = np.median(np.abs(flux), axis=1, keepdims=True)
    med = np.where(med > 0, med, 1.0)
    X = np.clip(flux / med, -10, 10)

    # GPU inference
    model.eval()
    with torch.no_grad():
        Xt = torch.FloatTensor(X).to(device)
        # Process in chunks if needed
        scores = []
        for i in range(0, len(Xt), 8192):
            batch = Xt[i:i+8192]
            recon = model(batch)
            s = torch.mean((batch - recon) ** 2, dim=1)
            scores.append(s.cpu().numpy())
        scores = np.concatenate(scores)

    # Extract anomalies above threshold
    anomalies = []
    for i in range(len(fm)):
        if scores[i] < threshold:
            continue

        spec = X[i]
        with torch.no_grad():
            rec = model(torch.FloatTensor(spec).unsqueeze(0).to(device)).cpu().numpy()[0]

        ar = np.abs(spec - rec)
        rb = float(np.mean(ar[:172]))
        rr = float(np.mean(ar[172:317]))
        rz = float(np.mean(ar[317:]))
        worst = 'B' if rb >= rr and rb >= rz else ('R' if rr >= rz else 'Z')

        anomalies.append({
            'tid': int(fm['TARGETID'][i]),
            'ra': float(fm['TARGET_RA'][i]) if 'TARGET_RA' in fm.dtype.names else 0,
            'dec': float(fm['TARGET_DEC'][i]) if 'TARGET_DEC' in fm.dtype.names else 0,
            'score': float(scores[i]),
            'worst': worst,
            'rB': rb, 'rR': rr, 'rZ': rz,
        })

    sp.close()
    return len(fm), anomalies


def map_dr1_pixels():
    """Map all available healpix pixels in DESI DR1."""
    base = 'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/'
    all_pixels = []

    for survey in ['main']:  # DR1 main survey has the bulk
        for program in ['dark', 'bright']:
            url = base + survey + '/' + program + '/'
            try:
                req = urllib.request.urlopen(url, timeout=15)
                groups = re.findall(r'href="(\d+)/"', req.read().decode())
                for g in groups:
                    try:
                        req2 = urllib.request.urlopen(url + g + '/', timeout=10)
                        pixels = re.findall(r'href="(\d+)/"', req2.read().decode())
                        for p in pixels:
                            all_pixels.append((survey, program, g, p))
                    except:
                        pass
            except:
                pass

    return all_pixels


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=float, default=5.0)
    parser.add_argument('--batch-size', type=int, default=8192)
    parser.add_argument('--model-path', type=str, default='best_model_47k.pt')
    parser.add_argument('--output-dir', type=str, default='outputs')
    parser.add_argument('--temp-dir', type=str, default='temp')
    parser.add_argument('--max-pixels', type=int, default=0, help='0 = all')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.temp_dir, exist_ok=True)

    # Setup device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('Device:', device)

    # Load model
    print('Loading model from', args.model_path)
    model = BigAE(496, 128).to(device)
    model.load_state_dict(torch.load(args.model_path, map_location=device))
    model.eval()
    print('Model loaded.')

    # Map pixels
    print('Mapping DESI DR1 healpix pixels...')
    pixels = map_dr1_pixels()
    print('Total pixels:', len(pixels))

    if args.max_pixels > 0:
        pixels = pixels[:args.max_pixels]
        print('Limited to', args.max_pixels)

    # Process
    base = 'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/'
    total_spec = 0
    total_anom = 0
    all_anomalies = []
    t0 = time.time()

    for i, (survey, program, group, pixel) in enumerate(pixels):
        fname = 'coadd-%s-%s-%s.fits' % (survey, program, pixel)
        fpath = os.path.join(args.temp_dir, fname)
        url = base + '%s/%s/%s/%s/%s' % (survey, program, group, pixel, fname)

        try:
            urllib.request.urlretrieve(url, fpath)
            n_obj, anoms = process_coadd(fpath, model, device, args.threshold)
            total_spec += n_obj
            total_anom += len(anoms)
            all_anomalies.extend(anoms)
        except:
            pass

        # Delete immediately
        if os.path.exists(fpath):
            os.remove(fpath)

        if (i + 1) % 50 == 0:
            elapsed = time.time() - t0
            rate = total_spec / elapsed if elapsed > 0 else 0
            print('  [%d/%d] %d spectra, %d anomalies, %.0fs, %.0f spec/s' % (
                i + 1, len(pixels), total_spec, total_anom, elapsed, rate))

            # Checkpoint save
            with open(os.path.join(args.output_dir, 'dr1_anomalies_checkpoint.json'), 'w') as f:
                json.dump({
                    'pixels_processed': i + 1,
                    'total_pixels': len(pixels),
                    'total_spectra': total_spec,
                    'total_anomalies': total_anom,
                    'threshold': args.threshold,
                    'elapsed_s': elapsed,
                    'anomalies': all_anomalies[-1000:],  # last 1000
                }, f)

    # Final save
    elapsed = time.time() - t0
    print('\nCOMPLETE: %d spectra, %d anomalies from %d pixels in %.0fs' % (
        total_spec, total_anom, len(pixels), elapsed))

    with open(os.path.join(args.output_dir, 'dr1_full_anomaly_catalog.json'), 'w') as f:
        json.dump({
            'total_spectra': total_spec,
            'total_anomalies': total_anom,
            'threshold': args.threshold,
            'elapsed_s': elapsed,
            'anomalies': all_anomalies,
        }, f, indent=2)
    print('Saved: dr1_full_anomaly_catalog.json')


if __name__ == '__main__':
    main()
