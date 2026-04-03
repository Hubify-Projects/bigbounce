#!/usr/bin/env python3
"""
LAMOST DR10 v2.0 LRS Anomaly Scan — OPTIMIZED v2
Key optimizations:
1. np.interp instead of manual bin loop (100x faster per spectrum)
2. Batch GPU inference with larger batches
3. ThreadPoolExecutor for parallel FITS decompression
"""
import numpy as np, torch, torch.nn as nn, os, json, time, urllib.request, tarfile, gzip, re
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor

try:
    import pyarrow as pa, pyarrow.parquet as pq
    HAS_PARQUET = True
except:
    HAS_PARQUET = False

from astropy.io import fits
import warnings
warnings.filterwarnings('ignore')

class BigAE(nn.Module):
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(n_in,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,128),nn.ReLU(),nn.Linear(128,n_lat))
        self.dec = nn.Sequential(nn.Linear(n_lat,128),nn.ReLU(),nn.Linear(128,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,n_in))
    def forward(self, x): return self.dec(self.enc(x))
    def encode(self, x): return self.enc(x)

WMIN, WMAX, NBINS = 3600.0, 9800.0, 496
DESI_WAVE = np.linspace(WMIN, WMAX, NBINS).astype(np.float32)

def resample_fast(wave, flux):
    """Fast resampling using np.interp (orders of magnitude faster)."""
    # np.interp handles out-of-range with fill_value
    resampled = np.interp(DESI_WAVE, wave, flux, left=0, right=0).astype(np.float32)
    valid = resampled != 0
    if valid.sum() < 100:
        return None
    med = np.median(resampled[valid])
    if med > 0 and np.isfinite(med):
        resampled /= med
    return resampled

def read_one_fits(data):
    """Read a single .fits.gz from bytes. Returns tuple or None."""
    try:
        decompressed = gzip.decompress(data)
        with fits.open(BytesIO(decompressed), memmap=False) as h:
            hdr = h[0].header
            obsid = hdr.get('OBSID', 0)
            ra = hdr.get('RA', 0.0)
            dec = hdr.get('DEC', 0.0)
            objtype = hdr.get('CLASS', hdr.get('OBJTYPE', ''))
            z = hdr.get('Z', 0.0)
            snr = hdr.get('SNRG', hdr.get('SNRU', 0.0))
            if len(h) < 2 or h[1].data is None:
                return None
            tbl = h[1].data
            flux = np.array(tbl['FLUX'], dtype=np.float32).flatten()
            wave = np.array(tbl['WAVELENGTH'], dtype=np.float32).flatten()
            if len(flux) < 100:
                return None
            resampled = resample_fast(wave, flux)
            if resampled is None:
                return None
            return (resampled, int(obsid), float(ra), float(dec), str(objtype), float(z), float(snr))
    except:
        return None

def download_with_retry(url, dest, max_retries=3):
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 BigBounce/1.0"})
            resp = urllib.request.urlopen(req, timeout=300)
            with open(dest, 'wb') as f:
                while True:
                    chunk = resp.read(131072)
                    if not chunk: break
                    f.write(chunk)
            return True
        except:
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
    return False

def process_tarball(tar_path, model, device):
    """Process all spectra in a tarball using parallel decompression."""
    results = []
    try:
        with tarfile.open(tar_path, 'r:gz') as tar:
            members = [m for m in tar.getmembers() if m.name.endswith('.fits.gz') and m.isreg()]
            # Read all file data
            file_data = []
            for m in members:
                try:
                    file_data.append(tar.extractfile(m).read())
                except:
                    pass

        # Parallel FITS reading (CPU-bound decompression + parsing)
        with ThreadPoolExecutor(max_workers=8) as pool:
            parsed = list(pool.map(read_one_fits, file_data))

        # Collect valid results
        spectra = []
        meta = []
        for r in parsed:
            if r is not None:
                spectra.append(r[0])
                meta.append(r[1:])

        if not spectra:
            return results

        # GPU batch inference
        x = torch.tensor(np.stack(spectra)).to(device)
        with torch.no_grad():
            recon = model(x)
        residuals = (x - recon).cpu().numpy()
        scores = np.mean(residuals**2, axis=1)

        for k in range(len(meta)):
            obsid, ra, dec, objtype, z, snr = meta[k]
            results.append({
                'obsid': obsid, 'ra': ra, 'dec': dec,
                'objtype': objtype, 'z': z, 'snr': snr,
                'anomaly_score': float(scores[k]),
                'rB': float(np.mean(residuals[k, :170]**2)),
                'rR': float(np.mean(residuals[k, 170:340]**2)),
                'rZ': float(np.mean(residuals[k, 340:]**2)),
            })
    except Exception as e:
        print(f'  Error: {e}')
    return results

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Device: {device}')
    out_dir = '/workspace/bigbounce/outputs/lamost'
    temp_dir = '/workspace/bigbounce/temp_lamost'
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    model = BigAE(496, 128).to(device)
    model.load_state_dict(torch.load('/workspace/bigbounce/best_model_47k.pt', map_location=device, weights_only=True))
    model.eval()
    print('Model loaded.')

    ckpt_path = os.path.join(out_dir, 'checkpoint.json')
    if os.path.exists(ckpt_path):
        with open(ckpt_path) as f: ckpt = json.load(f)
        done_nights = set(ckpt.get('done_nights', []))
        total_scored = ckpt.get('total_scored', 0)
        total_anomalies = ckpt.get('total_anomalies', 0)
        batch_idx = ckpt.get('batch_idx', 0)
    else:
        done_nights = set(); total_scored = total_anomalies = batch_idx = 0

    url = 'http://www.lamost.org/dr10/v2.0/tar/lrs-fits/'
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=60).read().decode()
    tarballs = sorted(set(re.findall(r'(\d{8}\.tar\.gz)', html)))
    print(f'Tarballs: {len(tarballs)}, Done: {len(done_nights)}')

    row_buffer = []; t0 = time.time(); n_done = 0

    for ti, tarname in enumerate(tarballs):
        night = tarname.replace('.tar.gz', '')
        if night in done_nights: continue

        tar_path = os.path.join(temp_dir, tarname)
        if not os.path.exists(tar_path):
            if not download_with_retry(f'http://www.lamost.org/dr10/v2.0/tar/lrs-fits/{tarname}', tar_path):
                continue

        rows = process_tarball(tar_path, model, device)
        n_anom = sum(1 for r in rows if r['anomaly_score'] > 5.0)
        row_buffer.extend(rows)
        total_scored += len(rows)
        total_anomalies += n_anom
        done_nights.add(night)
        n_done += 1

        if os.path.exists(tar_path): os.remove(tar_path)

        if len(row_buffer) >= 100000 and HAS_PARQUET:
            pq.write_table(pa.Table.from_pylist(row_buffer),
                          os.path.join(out_dir, f'lamost_batch_{batch_idx:04d}.parquet'), compression='zstd')
            print(f'  Batch {batch_idx}: {len(row_buffer):,} rows ({total_scored:,} total, {total_anomalies:,} anom)')
            batch_idx += 1; row_buffer = []

        if n_done % 5 == 0:
            with open(ckpt_path, 'w') as f:
                json.dump({'done_nights': list(done_nights), 'total_scored': total_scored,
                          'total_anomalies': total_anomalies, 'batch_idx': batch_idx}, f)

        if n_done % 10 == 0 and n_done > 0:
            elapsed = time.time() - t0
            rate = n_done / elapsed * 3600
            rem = sum(1 for t in tarballs if t.replace('.tar.gz','') not in done_nights)
            eta = rem / (n_done / elapsed) / 3600 if n_done > 0 else 0
            print(f'  [{ti+1}/{len(tarballs)}] {n_done} nights | {total_scored:,} scored | {total_anomalies:,} anom | {rate:.0f}/h | ETA: {eta:.1f}h')

    if row_buffer and HAS_PARQUET:
        pq.write_table(pa.Table.from_pylist(row_buffer),
                      os.path.join(out_dir, f'lamost_batch_{batch_idx:04d}.parquet'), compression='zstd')

    elapsed = time.time() - t0
    print(f'\n{"="*60}\nCOMPLETE: {total_scored:,} LAMOST spectra, {total_anomalies:,} anomalies, {elapsed/3600:.1f}h\n{"="*60}')
    with open(ckpt_path, 'w') as f:
        json.dump({'done_nights': list(done_nights), 'total_scored': total_scored,
                  'total_anomalies': total_anomalies, 'batch_idx': batch_idx, 'status': 'COMPLETE'}, f)

if __name__ == '__main__':
    main()
