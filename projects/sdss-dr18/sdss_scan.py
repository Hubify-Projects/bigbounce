#!/usr/bin/env python3
"""SDSS DR18 Plate-Based Anomaly Scan - downloads spec-lite files per plate."""
import numpy as np, torch, torch.nn as nn, os, json, time, urllib.request, traceback
from astropy.io import fits

try:
    import pyarrow as pa, pyarrow.parquet as pq
    HAS_PARQUET = True
except:
    HAS_PARQUET = False

class BigAE(nn.Module):
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(n_in,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,128),nn.ReLU(),nn.Linear(128,n_lat))
        self.dec = nn.Sequential(nn.Linear(n_lat,128),nn.ReLU(),nn.Linear(128,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,n_in))
    def forward(self, x): return self.dec(self.enc(x))
    def encode(self, x): return self.enc(x)

N_BINS = 496
WMIN, WMAX = 3600.0, 9800.0

def resample(wave, flux, ivar=None):
    dw = np.linspace(WMIN, WMAX, N_BINS)
    bw = (WMAX - WMIN) / N_BINS
    out = np.zeros(N_BINS, dtype=np.float32)
    for i in range(N_BINS):
        m = (wave >= dw[i]-bw/2) & (wave < dw[i]+bw/2)
        if np.any(m):
            if ivar is not None:
                w = np.clip(ivar[m], 0, None)
                out[i] = np.average(flux[m], weights=w) if np.sum(w)>0 else np.mean(flux[m])
            else:
                out[i] = np.mean(flux[m])
    med = np.median(out[out != 0])
    if med > 0: out /= med
    return out

def process_spec_file(path, model, device):
    """Process a single SDSS spec-lite FITS file."""
    rows = []
    try:
        with fits.open(path, memmap=True) as h:
            wave = 10**h[1].data['loglam']
            flux = h[1].data['flux'].astype(np.float32)
            ivar = h[1].data['ivar'].astype(np.float32)
            # Get metadata from HDU2 (catalog data)
            if len(h) > 2:
                cat = h[2].data
                ra = float(cat['PLUG_RA'][0]) if 'PLUG_RA' in cat.names else 0
                dec = float(cat['PLUG_DEC'][0]) if 'PLUG_DEC' in cat.names else 0
                z = float(cat['Z'][0]) if 'Z' in cat.names else 0
                zw = int(cat['ZWARNING'][0]) if 'ZWARNING' in cat.names else -1
                cls = str(cat['CLASS'][0]).strip() if 'CLASS' in cat.names else ''
                plate = int(cat['PLATE'][0]) if 'PLATE' in cat.names else 0
                mjd = int(cat['MJD'][0]) if 'MJD' in cat.names else 0
                fid = int(cat['FIBERID'][0]) if 'FIBERID' in cat.names else 0
            else:
                ra = dec = z = 0; zw = -1; cls = ''; plate = mjd = fid = 0

            spec = resample(wave, flux, ivar)
            if np.sum(spec != 0) < 100:
                return rows

            x = torch.tensor(spec).unsqueeze(0).to(device)
            with torch.no_grad():
                recon = model(x)
                latent = model.encode(x)
            res = (x - recon).cpu().numpy()[0]
            score = float(np.mean(res**2))
            lat = latent.cpu().numpy()[0]

            row = {'plate':plate,'mjd':mjd,'fiberid':fid,
                   'ra':ra,'dec':dec,'z':z,'zwarning':zw,'class':cls,
                   'anomaly_score':score,
                   'rB':float(np.mean(res[:170]**2)),
                   'rR':float(np.mean(res[170:340]**2)),
                   'rZ':float(np.mean(res[340:]**2))}
            for j in range(128):
                row[f'lat_{j:03d}'] = float(lat[j])
            rows.append(row)
    except Exception as e:
        pass
    return rows

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('='*60)
    print('SDSS DR18 PLATE-BASED ANOMALY SCAN')
    print('='*60)
    if torch.cuda.is_available():
        print(f'GPU: {torch.cuda.get_device_name(0)}')

    model = BigAE(496,128).to(device)
    model.load_state_dict(torch.load('best_model_47k.pt', map_location=device, weights_only=True))
    model.eval()
    print('Model loaded.')

    os.makedirs('outputs/sdss_dr18', exist_ok=True)
    os.makedirs('temp/sdss_specs', exist_ok=True)

    # Read plate-mjd-fiber list from spAll
    print('Reading spAll for plate list...')
    with fits.open('temp/sdss/spAll-v5_13_2.fits', memmap=True) as h:
        data = h[1].data
        n = len(data)
        plates = data['PLATE']
        mjds = data['MJD']
        fiberids = data['FIBERID']
        # Build unique (plate, mjd, fiberid) tuples
        specs = []
        for i in range(n):
            specs.append((int(plates[i]), int(mjds[i]), int(fiberids[i])))

    print(f'Total spectra: {len(specs):,}')

    # Checkpoint
    ckpt_path = 'outputs/sdss_dr18/checkpoint.json'
    if os.path.exists(ckpt_path):
        with open(ckpt_path) as f: ckpt = json.load(f)
        done_idx = ckpt.get('done_idx', 0)
        total_scored = ckpt.get('total_scored', 0)
        total_anomalies = ckpt.get('total_anomalies', 0)
        batch_idx = ckpt.get('batch_idx', 0)
    else:
        done_idx = total_scored = total_anomalies = batch_idx = 0

    print(f'Resuming from index {done_idx:,} ({total_scored:,} scored)')

    row_buffer = []
    t0 = time.time()
    base_url = "https://data.sdss.org/sas/dr18/spectro/sdss/redux/26/spectra/lite"

    for i in range(done_idx, len(specs)):
        plate, mjd, fid = specs[i]
        url = f"{base_url}/{plate:04d}/spec-{plate:04d}-{mjd}-{fid:04d}.fits"
        dest = f"temp/sdss_specs/spec-{plate:04d}-{mjd}-{fid:04d}.fits"

        try:
            if not os.path.exists(dest):
                urllib.request.urlretrieve(url, dest)
            rows = process_spec_file(dest, model, device)
            row_buffer.extend(rows)
            total_scored += len(rows)
            total_anomalies += sum(1 for r in rows if r['anomaly_score'] > 5.0)
        except:
            pass
        finally:
            if os.path.exists(dest):
                os.remove(dest)

        # Flush every 50K rows
        if len(row_buffer) >= 50000 and HAS_PARQUET:
            table = pa.Table.from_pylist(row_buffer)
            pq.write_table(table, f'outputs/sdss_dr18/sdss_batch_{batch_idx:04d}.parquet', compression='zstd')
            print(f'  Batch {batch_idx}: {len(row_buffer):,} rows ({total_scored:,} total, {total_anomalies:,} anomalies)')
            batch_idx += 1
            row_buffer = []
            with open(ckpt_path, 'w') as f:
                json.dump({'done_idx':i+1,'total_scored':total_scored,'total_anomalies':total_anomalies,'batch_idx':batch_idx}, f)

        # Progress every 500
        if (i - done_idx + 1) % 500 == 0 and total_scored > 0:
            elapsed = time.time() - t0
            rate = (i - done_idx + 1) / elapsed
            eta = (len(specs) - i) / rate / 3600
            print(f'  [{i+1:,}/{len(specs):,}] {total_scored:,} scored | {total_anomalies:,} anom | {rate:.0f} dl/s | ETA: {eta:.1f}h')

    # Final flush
    if row_buffer and HAS_PARQUET:
        table = pa.Table.from_pylist(row_buffer)
        pq.write_table(table, f'outputs/sdss_dr18/sdss_batch_{batch_idx:04d}.parquet', compression='zstd')

    elapsed = time.time() - t0
    print(f'\nCOMPLETE: {total_scored:,} scored, {total_anomalies:,} anomalies, {elapsed/3600:.1f}h')

if __name__ == '__main__':
    main()
