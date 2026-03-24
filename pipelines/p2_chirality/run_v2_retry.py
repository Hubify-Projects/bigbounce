#!/usr/bin/env python3
"""
v2 Inference with automatic retry on shard boundaries.

The HF streaming iterator dies after ~310K galaxies (1 shard).
This script detects the stop and restarts, skipping already-processed IDs.
Saves after each shard-worth of data.
"""
import os, sys, time, json
import numpy as np
os.environ['HF_TOKEN'] = os.environ.get('HF_TOKEN', 'HF_TOKEN_REDACTED')

import torch
import torch.nn as nn
import timm
from torchvision import transforms
from datasets import load_dataset
import pandas as pd

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"
CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL']

print("=" * 70, flush=True)
print("v2 RETRY-BASED INFERENCE: 8.67M GALAXIES", flush=True)
print("=" * 70, flush=True)

# Load model
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
        self.e = e; self.h = h
    def forward(self, x): return self.h(self.e(x))

model = Model(encoder, head).to(DEVICE).eval()
print(f"  Model loaded (val_acc={ckpt['val_acc']:.4f})", flush=True)

tfm = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225]),
])

# Load existing results
catalog_file = f"{OUTPUT_DIR}/v2_catalog_retry.parquet"
if os.path.exists(catalog_file):
    existing = pd.read_parquet(catalog_file)
    processed_ids = set(existing['id_str'].values)
    all_rows = existing.to_dict('records')
    print(f"  Resuming from {len(all_rows):,} existing galaxies", flush=True)
else:
    processed_ids = set()
    all_rows = []
    print(f"  Starting fresh", flush=True)

TARGET = 8_670_000
BS = 64
MAX_RETRIES = 35  # More than 28 shards, in case some retries are needed

t_global = time.time()

for attempt in range(MAX_RETRIES):
    if len(all_rows) >= TARGET * 0.95:  # Close enough
        break

    n_before = len(all_rows)
    print(f"\n[Attempt {attempt+1}] Starting stream (have {len(all_rows):,}/{TARGET:,})...", flush=True)

    try:
        ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)
    except Exception as e:
        print(f"  Failed to create iterator: {e}", flush=True)
        time.sleep(10)
        continue

    n_new = 0
    n_skip = 0
    ibatch, mbatch = [], []
    t_attempt = time.time()

    try:
        for row in ds:
            id_str = str(row.get('id_str', ''))

            # Skip already processed
            if id_str in processed_ids:
                n_skip += 1
                if n_skip % 100000 == 0:
                    print(f"    Skipping... {n_skip:,} (have {len(all_rows):,})", flush=True)
                continue

            img = row.get('image')
            if img is None:
                continue

            try:
                ibatch.append(tfm(img))
                mbatch.append({'id_str': id_str,
                               'ra': float(row.get('ra', 0)),
                               'dec': float(row.get('dec', 0))})
            except:
                continue

            if len(ibatch) >= BS:
                bt = torch.stack(ibatch).to(DEVICE)
                with torch.no_grad():
                    probs = torch.softmax(model(bt), dim=1).cpu().numpy()
                for m, p in zip(mbatch, probs):
                    cls = int(p.argmax())
                    all_rows.append({
                        'id_str': m['id_str'], 'ra': m['ra'], 'dec': m['dec'],
                        'p_cw': float(p[0]), 'p_ccw': float(p[1]), 'p_ns': float(p[2]),
                        'class': CLASS_NAMES[cls], 'confidence': float(p.max()),
                    })
                    processed_ids.add(m['id_str'])
                n_new += len(ibatch)
                ibatch, mbatch = [], []

                if n_new % 10000 < BS:
                    elapsed = time.time() - t_attempt
                    rate = n_new / elapsed if elapsed > 0 else 0
                    print(f"    +{n_new:,} new | total {len(all_rows):,}/{TARGET:,} | {rate:.0f}/s", flush=True)

    except Exception as e:
        print(f"  Iterator error: {e}", flush=True)

    # Process remaining batch
    if ibatch:
        bt = torch.stack(ibatch).to(DEVICE)
        with torch.no_grad():
            probs = torch.softmax(model(bt), dim=1).cpu().numpy()
        for m, p in zip(mbatch, probs):
            cls = int(p.argmax())
            all_rows.append({
                'id_str': m['id_str'], 'ra': m['ra'], 'dec': m['dec'],
                'p_cw': float(p[0]), 'p_ccw': float(p[1]), 'p_ns': float(p[2]),
                'class': CLASS_NAMES[cls], 'confidence': float(p.max()),
            })
            processed_ids.add(m['id_str'])
        n_new += len(ibatch)

    n_after = len(all_rows)
    print(f"  Attempt {attempt+1} done: +{n_after - n_before:,} new, total {n_after:,}", flush=True)

    # Save checkpoint after each attempt
    df = pd.DataFrame(all_rows)
    df.to_parquet(catalog_file)
    print(f"  Saved checkpoint: {catalog_file} ({len(df):,} rows)", flush=True)

    if n_after == n_before:
        print(f"  No new galaxies — dataset may be exhausted or stuck", flush=True)
        # Wait and retry
        time.sleep(30)

# Final save
df = pd.DataFrame(all_rows)
df.to_parquet(f"{OUTPUT_DIR}/chirality_catalog_v2_full.parquet")

n_cw = (df['class'] == 'CW').sum()
n_ccw = (df['class'] == 'CCW').sum()
n_ns = (df['class'] == 'NOT_SPIRAL').sum()
elapsed_h = (time.time() - t_global) / 3600

print(f"\n{'='*70}", flush=True)
print(f"COMPLETE: {len(df):,} galaxies in {elapsed_h:.1f}h", flush=True)
print(f"CW: {n_cw:,} CCW: {n_ccw:,} NS: {n_ns:,} CW/(CW+CCW)={n_cw/(n_cw+n_ccw):.4f}", flush=True)
print(f"{'='*70}", flush=True)

json.dump({
    'n_total': len(df), 'n_cw': int(n_cw), 'n_ccw': int(n_ccw), 'n_ns': int(n_ns),
    'cw_spiral_frac': float(n_cw/(n_cw+n_ccw)), 'runtime_h': float(elapsed_h),
    'n_attempts': attempt + 1,
}, open(f"{OUTPUT_DIR}/v2_retry_summary.json", 'w'), indent=2)
