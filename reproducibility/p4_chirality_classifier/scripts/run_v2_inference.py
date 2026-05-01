#!/usr/bin/env python3
"""
v2 Inference: Classify 8.67M GZ DESI galaxies with bias-hardened 3-class model.

Model: chirality_model_v2_best.pt (93.7% val accuracy, all bias tests PASS)
Classes: CW (0) / CCW (1) / NOT_SPIRAL (2)
Output: chirality_catalog_v2_full.parquet + dipole analysis
"""

import os, sys, time, json
import numpy as np
import torch
import torch.nn as nn
import timm
from torchvision import transforms
from datasets import load_dataset
import pandas as pd

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"

print("=" * 70, flush=True)
print("v2 CHIRALITY INFERENCE: 8.67M GALAXIES", flush=True)
print("=" * 70, flush=True)

# Load v2 model
print("[1] Loading v2 model...", flush=True)

class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(nn.LayerNorm(384), nn.Linear(384,512), nn.GELU(), nn.Dropout(0.3),
                               nn.Linear(512,256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256,3))
    def forward(self, x): return self.h(x)

encoder = timm.create_model('vit_small_patch16_224', pretrained=False, num_classes=0)
head = Head()

ckpt = torch.load(f"{OUTPUT_DIR}/chirality_model_v2_best.pt", weights_only=True)
encoder.load_state_dict(ckpt['enc'])
head.load_state_dict(ckpt['head'])

class Model(nn.Module):
    def __init__(self, e, h):
        super().__init__()
        self.e = e
        self.h = h
    def forward(self, x): return self.h(self.e(x))

model = Model(encoder, head).to(DEVICE).eval()
print(f"  Loaded v2 (val_acc={ckpt['val_acc']:.4f}, 3-class)", flush=True)

tfm = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225]),
])

# Check for resume
resume_n = 0
catalog = []
ckpts = sorted([f for f in os.listdir(OUTPUT_DIR) if f.startswith('v2_ckpt_') and f.endswith('.parquet')])
if ckpts:
    try:
        df = pd.read_parquet(f"{OUTPUT_DIR}/{ckpts[-1]}")
        resume_n = len(df)
        catalog = df.to_dict('records')
        print(f"  Resuming from {resume_n:,} ({ckpts[-1]})", flush=True)
    except: pass

# Inference
print(f"\n[2] Inference (resume={resume_n:,})...", flush=True)
ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)
print("  Iterator ready", flush=True)

n = 0
n_proc = resume_n
n_err = 0
t0 = time.time()
BS = 64
ibatch, mbatch = [], []
last_hb = time.time()
CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL']

for row in ds:
    n += 1
    if n <= resume_n:
        if n % 1000000 == 0: print(f"    Skip {n:,}/{resume_n:,}", flush=True)
        continue

    # Heartbeat
    now = time.time()
    if now - last_hb > 60:
        print(f"    [hb] row={n:,} proc={n_proc:,} batch={len(ibatch)} err={n_err}", flush=True)
        last_hb = now

    img = row.get('image')
    if img is None: continue
    try:
        ibatch.append(tfm(img))
        mbatch.append({
            'id_str': str(row.get('id_str', '')),
            'ra': float(row.get('ra', 0)),
            'dec': float(row.get('dec', 0)),
        })
    except:
        n_err += 1; continue

    if len(ibatch) >= BS:
        bt = torch.stack(ibatch).to(DEVICE)
        with torch.no_grad():
            probs = torch.softmax(model(bt), dim=1).cpu().numpy()

        for m, p in zip(mbatch, probs):
            cls = int(p.argmax())
            catalog.append({
                'id_str': m['id_str'], 'ra': m['ra'], 'dec': m['dec'],
                'p_cw': float(p[0]), 'p_ccw': float(p[1]), 'p_ns': float(p[2]),
                'class': CLASS_NAMES[cls],
                'chirality': CLASS_NAMES[cls] if cls < 2 else 'AMBIGUOUS',
                'confidence': float(p.max()),
            })

        n_proc += len(ibatch)
        ibatch, mbatch = [], []

    # Progress every 5K
    if n_proc > resume_n and n_proc % 5000 == 0 and n_proc != getattr(sys, '_lp', 0):
        sys._lp = n_proc
        el = time.time() - t0
        rate = (n_proc - resume_n) / el if el > 0 else 0
        eta = (8670000 - n_proc) / rate / 3600 if rate > 0 else 999
        recent = catalog[-5000:]
        rc = sum(1 for r in recent if r['class'] == 'CW')
        rcc = sum(1 for r in recent if r['class'] == 'CCW')
        rns = sum(1 for r in recent if r['class'] == 'NOT_SPIRAL')
        print(f"    {n_proc:>9,}/8.67M | {rate:.0f}/s | ETA {eta:.1f}h | CW={rc} CCW={rcc} NS={rns}", flush=True)

    # Checkpoint every 250K
    if n_proc > resume_n and n_proc % 250000 == 0 and n_proc != getattr(sys, '_lc', 0):
        sys._lc = n_proc
        pd.DataFrame(catalog).to_parquet(f"{OUTPUT_DIR}/v2_ckpt_{n_proc:08d}.parquet")
        print(f"    *** CHECKPOINT {n_proc:,} ***", flush=True)

# Remaining
if ibatch:
    bt = torch.stack(ibatch).to(DEVICE)
    with torch.no_grad():
        probs = torch.softmax(model(bt), dim=1).cpu().numpy()
    for m, p in zip(mbatch, probs):
        cls = int(p.argmax())
        catalog.append({
            'id_str': m['id_str'], 'ra': m['ra'], 'dec': m['dec'],
            'p_cw': float(p[0]), 'p_ccw': float(p[1]), 'p_ns': float(p[2]),
            'class': CLASS_NAMES[cls], 'chirality': CLASS_NAMES[cls] if cls < 2 else 'AMBIGUOUS',
            'confidence': float(p.max()),
        })
    n_proc += len(ibatch)

# Save
print(f"\n[3] Saving catalog ({n_proc:,})...", flush=True)
df = pd.DataFrame(catalog)
df.to_parquet(f"{OUTPUT_DIR}/chirality_catalog_v2_full.parquet")

ncw = (df['class']=='CW').sum()
nccw = (df['class']=='CCW').sum()
nns = (df['class']=='NOT_SPIRAL').sum()
n_spiral = ncw + nccw
cw_frac = ncw / n_spiral if n_spiral > 0 else 0

print(f"  CW: {ncw:,} ({ncw/n_proc*100:.1f}%)", flush=True)
print(f"  CCW: {nccw:,} ({nccw/n_proc*100:.1f}%)", flush=True)
print(f"  NOT_SPIRAL: {nns:,} ({nns/n_proc*100:.1f}%)", flush=True)
print(f"  CW/(CW+CCW): {cw_frac:.4f}", flush=True)

# Dipole
print("\n[4] Dipole fit on spirals...", flush=True)
try:
    import healpy as hp
    NSIDE = 64
    spirals = df[df['class'].isin(['CW','CCW']) & (df['confidence'] > 0.7)]
    if len(spirals) > 1000:
        cw_map = np.zeros(hp.nside2npix(NSIDE))
        ccw_map = np.zeros(hp.nside2npix(NSIDE))
        theta = np.radians(90 - spirals['dec'].values)
        phi = np.radians(spirals['ra'].values % 360)
        pix = hp.ang2pix(NSIDE, theta, phi)
        for p, c in zip(pix, spirals['class'].values):
            if c == 'CW': cw_map[p] += 1
            else: ccw_map[p] += 1
        tot = cw_map + ccw_map
        mask = tot > 10
        asym = np.full(len(tot), hp.UNSEEN)
        asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot[mask]
        mono, dip = hp.remove_dipole(asym, bad=hp.UNSEEN, fitval=True)
        amp = np.sqrt(np.sum(dip**2))
        l = np.degrees(np.arctan2(dip[1], dip[0])) % 360
        b = np.degrees(np.arcsin(dip[2]/amp)) if amp > 0 else 0
        # Bootstrap
        boots = []
        for _ in range(1000):
            s = asym.copy(); v = s[s!=hp.UNSEEN]; np.random.shuffle(v); s[s!=hp.UNSEEN] = v
            _, d = hp.remove_dipole(s, bad=hp.UNSEEN, fitval=True)
            boots.append(np.sqrt(np.sum(d**2)))
        sigma = (amp - np.mean(boots)) / np.std(boots)
        pval = np.mean(np.array(boots) >= amp)
        print(f"  Monopole: {mono:.4f}", flush=True)
        print(f"  Dipole: A={amp:.4f} (l,b)=({l:.1f},{b:.1f}) {sigma:.1f}σ p={pval:.4f}", flush=True)
        dipole = {'monopole':float(mono),'amplitude':float(amp),'l':float(l),'b':float(b),'sigma':float(sigma),'p':float(pval),'n_spirals':int(len(spirals))}
    else:
        dipole = {'error': f'Only {len(spirals)} spirals'}
except Exception as e:
    dipole = {'error': str(e)}
    print(f"  Error: {e}", flush=True)

json.dump({'n_total':n_proc,'n_cw':int(ncw),'n_ccw':int(nccw),'n_ns':int(nns),
           'cw_spiral_frac':float(cw_frac),'model_val_acc':float(ckpt['val_acc']),
           'runtime_h':float((time.time()-t0)/3600),'dipole':dipole},
          open(f"{OUTPUT_DIR}/v2_inference_summary.json",'w'), indent=2)

print(f"\n{'='*70}", flush=True)
print(f"v2 DONE: {n_proc:,} | CW {ncw:,} CCW {nccw:,} NS {nns:,} | CW/(CW+CCW)={cw_frac:.4f}", flush=True)
print(f"{'='*70}", flush=True)
