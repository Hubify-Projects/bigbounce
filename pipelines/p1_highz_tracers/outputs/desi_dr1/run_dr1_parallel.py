#!/usr/bin/env python3
"""
DESI DR1 Full-Scale Inference on H200 GPU

With 8M+ spectra/sec inference, download is the ONLY bottleneck.
Use multiprocessing to download multiple files in parallel.
"""
import numpy as np, torch, torch.nn as nn
from astropy.io import fits
import urllib.request, re, os, json, time, glob
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

WORKSPACE = '/workspace/desi_dr1'
OUT = WORKSPACE + '/outputs'
TEMP = WORKSPACE + '/temp'
MODEL_PATH = WORKSPACE + '/model/best_model_47k.pt'
BASE = 'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/'
THRESHOLD = 5.0
PARALLEL_DOWNLOADS = 8

os.makedirs(OUT, exist_ok=True)
os.makedirs(TEMP, exist_ok=True)

class BigAE(nn.Module):
    def __init__(s,ni=496,nl=128):
        super().__init__()
        s.enc=nn.Sequential(nn.Linear(ni,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,128),nn.ReLU(),nn.Linear(128,nl))
        s.dec=nn.Sequential(nn.Linear(nl,128),nn.ReLU(),nn.Linear(128,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.1),nn.Linear(256,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(0.15),nn.Linear(512,ni))
    def forward(s,x): return s.dec(s.enc(x))

print('='*70)
print('DESI DR1 FULL-SCALE INFERENCE — H200 GPU')
print('='*70)

model = BigAE().cuda()
model.load_state_dict(torch.load(MODEL_PATH, map_location='cuda', weights_only=True))
model.eval()
print('Model loaded on H200 (150 GB VRAM)')

# Map ALL DR1 main survey pixels
print('\nMapping DESI DR1 pixels...')
all_pixels = []
for program in ['dark', 'bright']:
    url = BASE + 'main/' + program + '/'
    try:
        req = urllib.request.urlopen(url, timeout=15)
        groups = re.findall(r'href="(\d+)/"', req.read().decode())
        for g in groups:
            try:
                req2 = urllib.request.urlopen(url + g + '/', timeout=10)
                pixels = re.findall(r'href="(\d+)/"', req2.read().decode())
                for p in pixels:
                    all_pixels.append(('main', program, g, p))
            except: pass
    except: pass

print('Total DR1 main survey pixels: %d' % len(all_pixels))
print('Estimated spectra: ~%dM' % (len(all_pixels) * 650 // 1000000))

# Process function
lock = threading.Lock()
total_spec = [0]
total_anom = [0]
all_anomalies = []
processed = [0]

def process_pixel(args):
    survey, program, group, pixel = args
    fname = 'coadd-%s-%s-%s.fits' % (survey, program, pixel)
    fpath = TEMP + '/' + fname
    url = BASE + '%s/%s/%s/%s/%s' % (survey, program, group, pixel, fname)
    
    try:
        urllib.request.urlretrieve(url, fpath)
        sp = fits.open(fpath)
        fm = sp['FIBERMAP'].data
        
        def ds(a,f=16):
            n=a.shape[-1]//f*f; return a[...,:n].reshape(*a.shape[:-1],-1,f).mean(-1)
        
        flux = np.hstack([ds(sp['B_FLUX'].data), ds(sp['R_FLUX'].data), ds(sp['Z_FLUX'].data)])
        flux = np.nan_to_num(flux, 0, 0, 0).astype(np.float32)
        med = np.median(np.abs(flux), 1, keepdims=True)
        med = np.where(med > 0, med, 1)
        X = np.clip(flux / med, -10, 10)
        
        # GPU inference
        with torch.no_grad():
            Xt = torch.FloatTensor(X).cuda()
            rec = model(Xt)
            scores = torch.mean((Xt - rec)**2, dim=1).cpu().numpy()
        
        n_obj = len(fm)
        anoms = []
        for i in range(n_obj):
            if scores[i] >= THRESHOLD:
                ar = np.abs(X[i] - rec[i].cpu().numpy())
                rb=float(np.mean(ar[:172])); rr=float(np.mean(ar[172:317])); rz=float(np.mean(ar[317:]))
                w='B' if rb>=rr and rb>=rz else ('R' if rr>=rz else 'Z')
                anoms.append({
                    'tid':int(fm['TARGETID'][i]),
                    'ra':float(fm['TARGET_RA'][i]) if 'TARGET_RA' in fm.dtype.names else 0,
                    'dec':float(fm['TARGET_DEC'][i]) if 'TARGET_DEC' in fm.dtype.names else 0,
                    'score':float(scores[i]),'worst':w,'rB':rb,'rR':rr,'rZ':rz})
        
        sp.close()
        os.remove(fpath)
        
        with lock:
            total_spec[0] += n_obj
            total_anom[0] += len(anoms)
            all_anomalies.extend(anoms)
            processed[0] += 1
        
        return n_obj, len(anoms)
    except Exception as e:
        if os.path.exists(fpath):
            os.remove(fpath)
        with lock:
            processed[0] += 1
        return 0, 0

# Process with parallel downloads
print('\nProcessing with %d parallel downloads...' % PARALLEL_DOWNLOADS)
t0 = time.time()

with ThreadPoolExecutor(max_workers=PARALLEL_DOWNLOADS) as executor:
    futures = {executor.submit(process_pixel, px): px for px in all_pixels}
    
    for future in as_completed(futures):
        n, a = future.result()
        
        p = processed[0]
        if p % 100 == 0 and p > 0:
            elapsed = time.time() - t0
            rate = total_spec[0] / elapsed if elapsed > 0 else 0
            eta_h = (len(all_pixels) - p) / (p / elapsed) / 3600 if p > 0 else 0
            print('  [%d/%d] %d spectra, %d anomalies, %.0f spec/s, ETA: %.1fh' % (
                p, len(all_pixels), total_spec[0], total_anom[0], rate, eta_h))
            
            # Checkpoint
            with open(OUT + '/dr1_checkpoint.json', 'w') as f:
                json.dump({
                    'pixels': p, 'total_pixels': len(all_pixels),
                    'spectra': total_spec[0], 'anomalies': total_anom[0],
                    'elapsed': elapsed, 'rate': rate,
                    'top_anomalies': sorted(all_anomalies, key=lambda x: -x['score'])[:100],
                }, f)

elapsed = time.time() - t0
print('\n' + '='*70)
print('COMPLETE!')
print('  Pixels: %d' % processed[0])
print('  Spectra: %d' % total_spec[0])
print('  Anomalies (score > %.1f): %d' % (THRESHOLD, total_anom[0]))
print('  Time: %.0fs (%.1f hours)' % (elapsed, elapsed/3600))
print('  Rate: %.0f spectra/sec' % (total_spec[0]/elapsed if elapsed > 0 else 0))

# Sort anomalies by score and save
all_anomalies.sort(key=lambda x: -x['score'])
with open(OUT + '/dr1_full_catalog.json', 'w') as f:
    json.dump({
        'total_spectra': total_spec[0],
        'total_anomalies': total_anom[0],
        'threshold': THRESHOLD,
        'elapsed_s': elapsed,
        'top_1000': all_anomalies[:1000],
        'all_count': len(all_anomalies),
    }, f, indent=2)
print('Saved: dr1_full_catalog.json')

# Also save ALL anomalies (could be large)
with open(OUT + '/dr1_all_anomalies.json', 'w') as f:
    json.dump(all_anomalies, f)
print('Saved: dr1_all_anomalies.json (%d objects)' % len(all_anomalies))
