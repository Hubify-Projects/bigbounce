#!/usr/bin/env python3
"""
Phase B: Classify ALL 8.67M GZ DESI galaxies using the trained chirality model.

Simple, robust inference — no DataLoader complexity, just stream + batch + classify.
Saves checkpoints every 500K to protect against crashes.

At ~35/s (HuggingFace streaming bottleneck), full run takes ~69 hours.
"""

import os
import sys
import time
import json
import numpy as np

print("=" * 70, flush=True)
print("CHIRALITY INFERENCE: 8.67M GALAXIES", flush=True)
print("=" * 70, flush=True)

os.system("pip install -q torch torchvision timm datasets healpy pandas scipy")

import torch
import torch.nn as nn
import timm
from torchvision import transforms
from datasets import load_dataset
import pandas as pd

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"

print(f"  Device: {DEVICE}", flush=True)
if torch.cuda.is_available():
    print(f"  GPU: {torch.cuda.get_device_name(0)}", flush=True)

# ---- Load model ----
print("\n[1] Loading trained model...", flush=True)

class ChiralityHead(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.head = nn.Sequential(
            nn.LayerNorm(dim), nn.Linear(dim, 512), nn.GELU(), nn.Dropout(0.3),
            nn.Linear(512, 128), nn.GELU(), nn.Dropout(0.2), nn.Linear(128, 2))
    def forward(self, x):
        return self.head(x)

encoder = timm.create_model('vit_small_patch16_224', pretrained=False, num_classes=0)
chirality_head = ChiralityHead(384)

ckpt = torch.load(f"{OUTPUT_DIR}/chirality_model_best.pt", weights_only=True)
encoder.load_state_dict(ckpt['encoder_state'])
chirality_head.load_state_dict(ckpt['head_state'])

class ChiralityModel(nn.Module):
    def __init__(self, e, h):
        super().__init__()
        self.e = e
        self.h = h
    def forward(self, x):
        return self.h(self.e(x))

model = ChiralityModel(encoder, chirality_head).to(DEVICE)
model.eval()
print(f"  Loaded (val_acc={ckpt.get('val_acc', 0):.4f})", flush=True)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# ---- Check for resume ----
resume_n = 0
catalog_rows = []
ckpt_files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.startswith('catalog_ckpt_') and f.endswith('.parquet')])
if ckpt_files:
    latest = ckpt_files[-1]
    try:
        df = pd.read_parquet(f"{OUTPUT_DIR}/{latest}")
        resume_n = len(df)
        catalog_rows = df.to_dict('records')
        print(f"  Resuming from {resume_n:,} ({latest})", flush=True)
    except Exception:
        resume_n = 0

# ---- Inference ----
print(f"\n[2] Inference on 8.67M galaxies (resume_from={resume_n:,})...", flush=True)

ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)
print("  Iterator ready", flush=True)

n = 0
n_processed = resume_n
n_errors = 0
t_start = time.time()
last_heartbeat = time.time()
BATCH = 64
img_batch = []
meta_batch = []

for row in ds:
    # Heartbeat every 60s to detect stalls
    now = time.time()
    if now - last_heartbeat > 60:
        print(f"    [heartbeat] row={n:,} processed={n_processed:,} batch={len(img_batch)} errors={n_errors}", flush=True)
        last_heartbeat = now
    n += 1

    # Skip already processed
    if n <= resume_n:
        if n % 500000 == 0:
            print(f"    Skipping {n:,}/{resume_n:,}", flush=True)
        continue

    img = row.get('image')
    if img is None:
        continue

    try:
        img_t = transform(img)
        img_batch.append(img_t)
        meta_batch.append({
            'id_str': str(row.get('id_str', '')),
            'ra': float(row.get('ra', 0)),
            'dec': float(row.get('dec', 0)),
        })
    except Exception:
        n_errors += 1
        continue

    if len(img_batch) >= BATCH:
        bt = torch.stack(img_batch).to(DEVICE)
        with torch.no_grad():
            probs = torch.softmax(model(bt), dim=1).cpu().numpy()

        for meta, prob in zip(meta_batch, probs):
            catalog_rows.append({
                'id_str': meta['id_str'],
                'ra': meta['ra'],
                'dec': meta['dec'],
                'p_cw': float(prob[0]),
                'p_ccw': float(prob[1]),
                'chirality': 'CW' if prob[0] > prob[1] else 'CCW',
                'confidence': float(max(prob[0], prob[1])),
            })

        n_processed += len(img_batch)
        img_batch = []
        meta_batch = []

    # Progress print (with dedup)
    if n_processed > resume_n and n_processed % 5000 == 0 and n_processed != getattr(sys, '_last_print', 0):
        sys._last_print = n_processed
        elapsed = time.time() - t_start
        rate = (n_processed - resume_n) / elapsed if elapsed > 0 else 0
        eta_h = (8670000 - n_processed) / rate / 3600 if rate > 0 else 999
        n_cw = sum(1 for r in catalog_rows[-5000:] if r['chirality'] == 'CW')
        print(f"    {n_processed:>9,}/8.67M | {rate:.0f}/s | ETA {eta_h:.1f}h | last5K CW%={n_cw/50:.1f}%", flush=True)

    # Checkpoint every 500K
    if n_processed > resume_n and n_processed % 500000 == 0 and n_processed != getattr(sys, '_last_ckpt', 0):
        sys._last_ckpt = n_processed
        ckpt_df = pd.DataFrame(catalog_rows)
        ckpt_df.to_parquet(f"{OUTPUT_DIR}/catalog_ckpt_{n_processed:08d}.parquet")
        print(f"    *** CHECKPOINT {n_processed:,} saved ***", flush=True)

# Process remaining batch
if img_batch:
    bt = torch.stack(img_batch).to(DEVICE)
    with torch.no_grad():
        probs = torch.softmax(model(bt), dim=1).cpu().numpy()
    for meta, prob in zip(meta_batch, probs):
        catalog_rows.append({
            'id_str': meta['id_str'],
            'ra': meta['ra'],
            'dec': meta['dec'],
            'p_cw': float(prob[0]),
            'p_ccw': float(prob[1]),
            'chirality': 'CW' if prob[0] > prob[1] else 'CCW',
            'confidence': float(max(prob[0], prob[1])),
        })
    n_processed += len(img_batch)

# ---- Save final catalog ----
print(f"\n[3] Saving final catalog ({n_processed:,})...", flush=True)
catalog_df = pd.DataFrame(catalog_rows)
catalog_df.to_parquet(f"{OUTPUT_DIR}/chirality_catalog_full.parquet")

n_cw = (catalog_df['chirality'] == 'CW').sum()
n_ccw = (catalog_df['chirality'] == 'CCW').sum()
n_hc = (catalog_df['confidence'] > 0.9).sum()

# ---- Dipole fit ----
print("\n[4] Dipole fit...", flush=True)
try:
    import healpy as hp
    NSIDE = 64
    cw_map = np.zeros(hp.nside2npix(NSIDE))
    ccw_map = np.zeros(hp.nside2npix(NSIDE))
    hc = catalog_df[catalog_df['confidence'] > 0.7]
    if len(hc) > 1000:
        theta = np.radians(90.0 - hc['dec'].values)
        phi = np.radians(hc['ra'].values % 360)
        pix = hp.ang2pix(NSIDE, theta, phi)
        for p, c in zip(pix, hc['chirality'].values):
            if c == 'CW': cw_map[p] += 1
            else: ccw_map[p] += 1
        total = cw_map + ccw_map
        mask = total > 10
        asym = np.full(len(total), hp.UNSEEN)
        asym[mask] = (cw_map[mask] - ccw_map[mask]) / total[mask]
        mono, dipole = hp.remove_dipole(asym, bad=hp.UNSEEN, fitval=True)
        dip_amp = np.sqrt(np.sum(dipole**2))
        dip_l = np.degrees(np.arctan2(dipole[1], dipole[0])) % 360
        dip_b = np.degrees(np.arcsin(dipole[2] / dip_amp)) if dip_amp > 0 else 0

        # Bootstrap significance
        boot_amps = []
        for _ in range(1000):
            s = asym.copy()
            v = s[s != hp.UNSEEN]
            np.random.shuffle(v)
            s[s != hp.UNSEEN] = v
            _, d = hp.remove_dipole(s, bad=hp.UNSEEN, fitval=True)
            boot_amps.append(np.sqrt(np.sum(d**2)))
        sigma = (dip_amp - np.mean(boot_amps)) / np.std(boot_amps)
        p_val = np.mean(np.array(boot_amps) >= dip_amp)

        print(f"  Monopole: {mono:.4f}", flush=True)
        print(f"  Dipole: A={dip_amp:.4f}, (l,b)=({dip_l:.1f},{dip_b:.1f}), {sigma:.1f}σ (p={p_val:.4f})", flush=True)
        dipole_res = {'monopole': float(mono), 'amplitude': float(dip_amp), 'l': float(dip_l), 'b': float(dip_b), 'sigma': float(sigma), 'p_value': float(p_val)}
    else:
        dipole_res = {'error': 'Too few high-confidence galaxies'}
except Exception as e:
    print(f"  Error: {e}", flush=True)
    dipole_res = {'error': str(e)}

# ---- Save summary ----
summary = {
    'n_total': n_processed, 'n_cw': int(n_cw), 'n_ccw': int(n_ccw),
    'cw_fraction': float(n_cw / n_processed) if n_processed > 0 else 0,
    'n_high_conf_09': int(n_hc), 'n_errors': n_errors,
    'runtime_hours': float((time.time() - t_start) / 3600),
    'model_val_acc': float(ckpt.get('val_acc', 0)),
    'dipole': dipole_res,
}
with open(f"{OUTPUT_DIR}/inference_summary.json", 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n{'='*70}", flush=True)
print(f"DONE: {n_processed:,} galaxies | CW {n_cw:,} ({n_cw/n_processed*100:.1f}%) | CCW {n_ccw:,} ({n_ccw/n_processed*100:.1f}%)", flush=True)
print(f"High conf (>0.9): {n_hc:,}", flush=True)
print(f"{'='*70}", flush=True)
