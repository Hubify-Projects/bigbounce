#!/usr/bin/env python3
"""
SDSS DR18 Anomaly Scan via spPlate bulk files.
Each spPlate contains all ~640 spectra for one plate.
2,506 plates × ~640 spectra = ~1.6M spectra.
"""
import numpy as np, torch, torch.nn as nn, os, json, time, urllib.request, re, traceback
from astropy.io import fits
from concurrent.futures import ThreadPoolExecutor

try:
    import pyarrow as pa, pyarrow.parquet as pq
    HAS_PARQUET = True
except:
    HAS_PARQUET = False
    print("WARNING: no pyarrow, results will be JSON only")

class BigAE(nn.Module):
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(n_in,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,128),nn.ReLU(),nn.Linear(128,n_lat))
        self.dec = nn.Sequential(nn.Linear(n_lat,128),nn.ReLU(),nn.Linear(128,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,n_in))
    def forward(self, x): return self.dec(self.enc(x))
    def encode(self, x): return self.enc(x)

WMIN, WMAX, NBINS = 3600.0, 9800.0, 496

def resample_batch(wave, flux_batch):
    """Resample a batch of spectra (N, npix) to the DESI 496-bin grid."""
    desi_wave = np.linspace(WMIN, WMAX, NBINS)
    bw = (WMAX - WMIN) / NBINS
    N = flux_batch.shape[0]
    result = np.zeros((N, NBINS), dtype=np.float32)
    for i in range(NBINS):
        mask = (wave >= desi_wave[i] - bw/2) & (wave < desi_wave[i] + bw/2)
        if np.any(mask):
            result[:, i] = np.mean(flux_batch[:, mask], axis=1)
    # Normalize per spectrum
    for j in range(N):
        med = np.median(result[j][result[j] != 0])
        if med > 0:
            result[j] /= med
    return result

def get_plate_mjd_list(plate_dir):
    """Get (plate, mjd) pairs from SAS directory listing."""
    plate_list_file = os.path.join(os.path.dirname(__file__), 'plate_list.json')
    if os.path.exists(plate_list_file):
        with open(plate_list_file) as f:
            plates = json.load(f)
    else:
        url = 'https://data.sdss.org/sas/dr18/spectro/sdss/redux/26/'
        html = urllib.request.urlopen(url, timeout=30).read().decode()
        plates = re.findall(r'href="(\d{4})/"', html)
        with open(plate_list_file, 'w') as f:
            json.dump(plates, f)

    # For each plate, find the MJD from the directory
    plate_mjd = []
    for plate in plates:
        url = f'https://data.sdss.org/sas/dr18/spectro/sdss/redux/26/{plate}/'
        try:
            html = urllib.request.urlopen(url, timeout=10).read().decode()
            spplates = re.findall(r'spPlate-\d{4}-(\d{5})\.fits', html)
            for mjd in set(spplates):
                plate_mjd.append((plate, mjd))
        except:
            pass
    return plate_mjd

def download_spplate(plate, mjd, temp_dir):
    url = f'https://data.sdss.org/sas/dr18/spectro/sdss/redux/26/{plate}/spPlate-{plate}-{mjd}.fits'
    dest = os.path.join(temp_dir, f'spPlate-{plate}-{mjd}.fits')
    if os.path.exists(dest):
        return dest
    try:
        urllib.request.urlretrieve(url, dest)
        return dest
    except:
        return None

def process_spplate(path, model, device):
    """Process all spectra in an spPlate file."""
    rows = []
    try:
        with fits.open(path, memmap=True) as h:
            hdr = h[0].header
            flux = h[0].data.astype(np.float32)  # (nfiber, npix)
            nfiber, npix = flux.shape

            # Wavelength from header
            coeff0 = hdr.get('COEFF0', 3.5798)
            coeff1 = hdr.get('COEFF1', 0.0001)
            wave = 10**(coeff0 + coeff1 * np.arange(npix))

            plate = hdr.get('PLATEID', 0)
            mjd = hdr.get('MJD', 0)

            # Resample all spectra at once
            resampled = resample_batch(wave, flux)

            # Filter out empty spectra
            valid = np.sum(resampled != 0, axis=1) >= 100
            valid_idx = np.where(valid)[0]
            if len(valid_idx) == 0:
                return rows

            resampled_valid = resampled[valid_idx]

            # Batch through model
            x = torch.tensor(resampled_valid).to(device)
            with torch.no_grad():
                recon = model(x)
                latent = model.encode(x)

            residuals = (x - recon).cpu().numpy()
            scores = np.mean(residuals**2, axis=1)
            latents = latent.cpu().numpy()

            # Build rows
            for k, idx in enumerate(valid_idx):
                row = {
                    'plate': int(plate), 'mjd': int(mjd), 'fiberid': int(idx + 1),
                    'anomaly_score': float(scores[k]),
                    'rB': float(np.mean(residuals[k, :170]**2)),
                    'rR': float(np.mean(residuals[k, 170:340]**2)),
                    'rZ': float(np.mean(residuals[k, 340:]**2)),
                }
                for j in range(128):
                    row[f'lat_{j:03d}'] = float(latents[k, j])
                rows.append(row)
    except Exception as e:
        traceback.print_exc()
    return rows

def main():
    device = torch.device('cpu')  # BigAE is tiny, CPU is fine
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print('='*60)
    print('SDSS DR18 ANOMALY SCAN (spPlate bulk)')
    print('='*60)

    model_path = os.path.join(script_dir, 'best_model_47k.pt')
    model = BigAE(496, 128).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))
    model.eval()
    print('Model loaded.')

    out_dir = os.path.join(script_dir, 'outputs')
    temp_dir = os.path.join(script_dir, 'temp')
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    # Checkpoint
    ckpt_path = os.path.join(out_dir, 'checkpoint.json')
    if os.path.exists(ckpt_path):
        with open(ckpt_path) as f:
            ckpt = json.load(f)
        done_plates = set(ckpt.get('done_plates', []))
        total_scored = ckpt.get('total_scored', 0)
        total_anomalies = ckpt.get('total_anomalies', 0)
        batch_idx = ckpt.get('batch_idx', 0)
    else:
        done_plates = set()
        total_scored = total_anomalies = batch_idx = 0

    # Get plate list
    print('Getting plate-MJD list...')
    plate_mjd = get_plate_mjd_list(script_dir)
    print(f'Total plate-MJD combos: {len(plate_mjd)}')
    print(f'Already done: {len(done_plates)}')

    row_buffer = []
    t0 = time.time()
    n_done = 0

    for pi, (plate, mjd) in enumerate(plate_mjd):
        key = f'{plate}-{mjd}'
        if key in done_plates:
            continue

        # Download
        path = download_spplate(plate, mjd, temp_dir)
        if path is None:
            continue

        # Process
        rows = process_spplate(path, model, device)
        row_buffer.extend(rows)
        total_scored += len(rows)
        total_anomalies += sum(1 for r in rows if r['anomaly_score'] > 5.0)
        done_plates.add(key)
        n_done += 1

        # Clean up
        if os.path.exists(path):
            os.remove(path)

        # Flush every 50K rows
        if len(row_buffer) >= 50000 and HAS_PARQUET:
            table = pa.Table.from_pylist(row_buffer)
            pq.write_table(table, os.path.join(out_dir, f'sdss_batch_{batch_idx:04d}.parquet'), compression='zstd')
            print(f'  Batch {batch_idx}: {len(row_buffer):,} rows ({total_scored:,} total, {total_anomalies:,} anomalies)')
            batch_idx += 1
            row_buffer = []
            with open(ckpt_path, 'w') as f:
                json.dump({'done_plates': list(done_plates), 'total_scored': total_scored,
                          'total_anomalies': total_anomalies, 'batch_idx': batch_idx}, f)

        # Progress every 20 plates
        if n_done % 20 == 0 and n_done > 0:
            elapsed = time.time() - t0
            rate = n_done / elapsed
            remaining = len(plate_mjd) - pi
            eta = remaining / rate / 3600 if rate > 0 else 0
            print(f'  [{pi+1}/{len(plate_mjd)}] {n_done} plates | {total_scored:,} scored | {total_anomalies:,} anom | {rate:.1f} plates/s | ETA: {eta:.1f}h')

    # Final flush
    if row_buffer and HAS_PARQUET:
        table = pa.Table.from_pylist(row_buffer)
        pq.write_table(table, os.path.join(out_dir, f'sdss_batch_{batch_idx:04d}.parquet'), compression='zstd')
        batch_idx += 1

    elapsed = time.time() - t0
    print(f'\n{"="*60}\nCOMPLETE: {total_scored:,} spectra, {total_anomalies:,} anomalies, {elapsed/3600:.1f}h\n{"="*60}')

    with open(ckpt_path, 'w') as f:
        json.dump({'done_plates': list(done_plates), 'total_scored': total_scored,
                  'total_anomalies': total_anomalies, 'batch_idx': batch_idx, 'status': 'COMPLETE'}, f)

if __name__ == '__main__':
    main()
