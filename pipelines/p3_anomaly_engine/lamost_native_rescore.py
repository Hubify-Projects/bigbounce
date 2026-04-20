#!/usr/bin/env python3
"""
LAMOST DR10 Native BigAE RE-SCORE — P3-PATHC-LAMOST-NATIVE-RETRAIN (close-out)
==============================================================================
Re-scores all 11.4M LAMOST DR10 LRS spectra with the NATIVELY trained BigAE
(best_lamost_native.pt, val_loss=0.0329 gate PASS attempt 2 from fire #80).

This replaces the cross-transfer (DESI-trained) anomaly scores written by
lamost_scan_v2.py in /workspace/bigbounce_scan/outputs/lamost/lamost_batch_*.parquet
(107 files, 11,240,648 scored / 43,915 anom / 40h runtime — PRESERVED here as
the Paper 3 §7.1 "before native retrain" baseline; this script writes to a
DIFFERENT output directory and does not touch them).

Pipeline (forked from lamost_scan_v2.py with the minimal delta):
  1. Load best_lamost_native.pt onto cuda:0 eval mode.
  2. Fetch LAMOST DR10 LRS per-night tar list from the v2.0 endpoint.
  3. Resume via checkpoint.json done_nights set.
  4. For each unprocessed night: download tar, extract all .fits.gz, parallel
     decode (8 threads) through gzip + astropy.io.fits, resample each FLUX +
     WAVELENGTH to 496-bin DESI grid, median-normalize.
  5. **NEW (LAMOST fire #80 lesson): defensive outlier reject |x|>100 +
     np.clip(-10, 10) on every resampled vector before GPU inference.**
  6. Stack → GPU forward → per-spec MSE → anomaly_score.
  7. Buffer 100K rows → write parquet `lamost_native_batch_NNNN.parquet` under
     outputs/lamost_native/scores/ (8-col schema matching cross-transfer for
     easy before/after diff).
  8. Delete tar, checkpoint done_nights every 5 nights.

Output schema: obsid, ra, dec, objtype, z, snr, anomaly_score, rB, rR, rZ.
Same columns as cross-transfer output → enables direct per-object diff between
cross-transfer score and native score for Paper 3 §7.1 "before / after" table.

Budget: ~40h @ $1.19/h = ~$48 pod spend. Runs in parallel with sdss_native_rescore.
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

# Fire #80 outlier-clipping lesson applied preventively
MAX_ABS_TOL = 100.0
CLIP_RANGE = 10.0


def resample_fast(wave, flux):
    """Fast resampling + median normalize + defensive outlier filter+clip."""
    resampled = np.interp(DESI_WAVE, wave, flux, left=0, right=0).astype(np.float32)
    valid = resampled != 0
    if valid.sum() < 100:
        return None
    med = np.median(resampled[valid])
    if med > 0 and np.isfinite(med):
        resampled /= med
    else:
        return None
    # Fire #80 lesson: reject extreme post-normalize outliers + clip tails
    if not np.isfinite(resampled).all():
        return None
    if np.abs(resampled).max() > MAX_ABS_TOL:
        return None
    np.clip(resampled, -CLIP_RANGE, CLIP_RANGE, out=resampled)
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
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 BigBounce-PathC-NativeRescore/1.0"})
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
            file_data = []
            for m in members:
                try:
                    file_data.append(tar.extractfile(m).read())
                except:
                    pass

        with ThreadPoolExecutor(max_workers=8) as pool:
            parsed = list(pool.map(read_one_fits, file_data))

        spectra = []
        meta = []
        for r in parsed:
            if r is not None:
                spectra.append(r[0])
                meta.append(r[1:])

        if not spectra:
            return results

        # GPU batch inference, capped at 8192 per chunk for memory safety
        X = np.stack(spectra).astype(np.float32)
        scores_all = np.empty(len(X), dtype=np.float32)
        residuals_all = np.empty_like(X)
        chunk = 8192
        with torch.no_grad():
            for j in range(0, len(X), chunk):
                xb = torch.from_numpy(X[j:j+chunk]).to(device)
                recon = model(xb)
                resid = (xb - recon).cpu().numpy()
                residuals_all[j:j+chunk] = resid
                scores_all[j:j+chunk] = np.mean(resid**2, axis=1)

        for k in range(len(meta)):
            obsid, ra, dec, objtype, z, snr = meta[k]
            results.append({
                'obsid': obsid, 'ra': ra, 'dec': dec,
                'objtype': objtype, 'z': z, 'snr': snr,
                'anomaly_score': float(scores_all[k]),
                'rB': float(np.mean(residuals_all[k, :170]**2)),
                'rR': float(np.mean(residuals_all[k, 170:340]**2)),
                'rZ': float(np.mean(residuals_all[k, 340:]**2)),
            })
    except Exception as e:
        print(f'  Error: {e}', flush=True)
    return results


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Device: {device}', flush=True)

    out_dir = '/workspace/bigbounce_scan/outputs/lamost_native/scores'
    temp_dir = '/workspace/bigbounce_scan/temp/lamost_native_rescore'
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    model_path = '/workspace/bigbounce_scan/outputs/lamost_native/best_lamost_native.pt'
    model = BigAE(496, 128).to(device)
    state = torch.load(model_path, map_location=device)
    if isinstance(state, dict) and 'state_dict' in state:
        model.load_state_dict(state['state_dict'])
    else:
        model.load_state_dict(state)
    model.eval()
    print(f'Model loaded: {model_path}', flush=True)

    ckpt_path = os.path.join(out_dir, 'checkpoint.json')
    if os.path.exists(ckpt_path):
        with open(ckpt_path) as f:
            ckpt = json.load(f)
        done_nights = set(ckpt.get('done_nights', []))
        total_scored = ckpt.get('total_scored', 0)
        total_anomalies = ckpt.get('total_anomalies', 0)
        batch_idx = ckpt.get('batch_idx', 0)
        print(f'Resume: {len(done_nights)} nights done, {total_scored:,} scored', flush=True)
    else:
        done_nights = set(); total_scored = total_anomalies = batch_idx = 0

    url = 'http://www.lamost.org/dr10/v2.0/tar/lrs-fits/'
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=60).read().decode()
    tarballs = sorted(set(re.findall(r'(\d{8}\.tar\.gz)', html)))
    print(f'Tarballs: {len(tarballs)}, Done: {len(done_nights)}', flush=True)

    row_buffer = []
    t0 = time.time()
    n_done = 0

    for ti, tarname in enumerate(tarballs):
        night = tarname.replace('.tar.gz', '')
        if night in done_nights:
            continue

        tar_path = os.path.join(temp_dir, tarname)
        if not os.path.exists(tar_path):
            if not download_with_retry(f'http://www.lamost.org/dr10/v2.0/tar/lrs-fits/{tarname}', tar_path):
                print(f'  Download FAILED: {tarname}', flush=True)
                continue

        rows = process_tarball(tar_path, model, device)
        n_anom = sum(1 for r in rows if r['anomaly_score'] > 5.0)
        row_buffer.extend(rows)
        total_scored += len(rows)
        total_anomalies += n_anom
        done_nights.add(night)
        n_done += 1

        if os.path.exists(tar_path):
            os.remove(tar_path)

        if len(row_buffer) >= 100000 and HAS_PARQUET:
            pq.write_table(pa.Table.from_pylist(row_buffer),
                          os.path.join(out_dir, f'lamost_native_batch_{batch_idx:04d}.parquet'),
                          compression='zstd')
            print(f'  Batch {batch_idx}: {len(row_buffer):,} rows ({total_scored:,} total, {total_anomalies:,} anom score>5)', flush=True)
            batch_idx += 1
            row_buffer = []

        if n_done % 5 == 0:
            with open(ckpt_path, 'w') as f:
                json.dump({'done_nights': list(done_nights), 'total_scored': total_scored,
                          'total_anomalies': total_anomalies, 'batch_idx': batch_idx}, f)

        if n_done % 10 == 0 and n_done > 0:
            elapsed = time.time() - t0
            rate = n_done / elapsed * 3600
            rem = sum(1 for t in tarballs if t.replace('.tar.gz','') not in done_nights)
            eta = rem / (n_done / elapsed) / 3600 if n_done > 0 else 0
            print(f'  [{ti+1}/{len(tarballs)}] {n_done} nights | {total_scored:,} scored | {total_anomalies:,} score>5 | {rate:.0f}/h | ETA: {eta:.1f}h', flush=True)

    if row_buffer and HAS_PARQUET:
        pq.write_table(pa.Table.from_pylist(row_buffer),
                      os.path.join(out_dir, f'lamost_native_batch_{batch_idx:04d}.parquet'),
                      compression='zstd')

    elapsed = time.time() - t0
    print(f'\n{"="*60}\nCOMPLETE: {total_scored:,} LAMOST spectra, {total_anomalies:,} score>5, {elapsed/3600:.1f}h\n{"="*60}', flush=True)
    with open(ckpt_path, 'w') as f:
        json.dump({'done_nights': list(done_nights), 'total_scored': total_scored,
                  'total_anomalies': total_anomalies, 'batch_idx': batch_idx, 'status': 'COMPLETE'}, f)


if __name__ == '__main__':
    main()
