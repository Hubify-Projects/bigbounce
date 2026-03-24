#!/usr/bin/env python3
"""
v2 Inference on ALL 8.67M GZ DESI galaxies.

Uses non-streaming download (cached to /workspace/HF_TOKEN_REDACTED) to avoid
the 1-shard streaming bug. Processes with index-based access.

Saves per-shard checkpoints for crash recovery.
"""
import os, sys, time, json
import numpy as np
os.environ['HF_HOME'] = '/workspace/HF_TOKEN_REDACTED'
os.environ['HF_DATASETS_CACHE'] = '/workspace/HF_TOKEN_REDACTED/datasets'
os.environ['HF_TOKEN'] = os.environ.get('HF_TOKEN', 'HF_TOKEN_REDACTED')

import torch
import torch.nn as nn
import timm
from torchvision import transforms
import pandas as pd

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"
SHARD_DIR = f"{OUTPUT_DIR}/shard_catalogs"
os.makedirs(SHARD_DIR, exist_ok=True)

print("=" * 70, flush=True)
print("v2 FULL INFERENCE: 8.67M GALAXIES", flush=True)
print("=" * 70, flush=True)

# Load model
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
        self.e = e; self.h = h
    def forward(self, x): return self.h(self.e(x))

model = Model(encoder, head).to(DEVICE).eval()
print(f"  Loaded (val_acc={ckpt['val_acc']:.4f})", flush=True)

tfm = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225]),
])
CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL']

# Load full dataset (non-streaming, cached to /workspace)
print("\n[2] Loading full GZ DESI dataset (non-streaming, ~8.67M)...", flush=True)
print("  Downloading to /workspace/HF_TOKEN_REDACTED/ (may take 30-60 min first time)...", flush=True)
from datasets import load_dataset
ds = load_dataset("mwalmsley/gz_desi", split="train", cache_dir="/workspace/HF_TOKEN_REDACTED/datasets")
N = len(ds)
print(f"  Loaded: {N:,} galaxies", flush=True)

# Check which ranges are already processed
done_ranges = set()
for f in os.listdir(SHARD_DIR):
    if f.startswith('range_') and f.endswith('.parquet'):
        parts = f.replace('range_', '').replace('.parquet', '').split('_')
        done_ranges.add((int(parts[0]), int(parts[1])))

already_done = sum(hi - lo for lo, hi in done_ranges)
print(f"  Already processed: {already_done:,} galaxies ({len(done_ranges)} chunks)", flush=True)

# Process in chunks of 250K
CHUNK = 250000
BS = 64
t_global = time.time()

for chunk_start in range(0, N, CHUNK):
    chunk_end = min(chunk_start + CHUNK, N)

    if (chunk_start, chunk_end) in done_ranges:
        print(f"\n  Chunk [{chunk_start:,}-{chunk_end:,}]: SKIP (done)", flush=True)
        continue

    print(f"\n[Chunk {chunk_start:,}-{chunk_end:,}] Processing {chunk_end-chunk_start:,} galaxies...", flush=True)
    t_chunk = time.time()
    catalog = []
    n_proc = 0
    n_err = 0
    ibatch, mbatch = [], []

    for i in range(chunk_start, chunk_end):
        try:
            row = ds[i]
            img = row.get('image')
            if img is None:
                continue
            ibatch.append(tfm(img))
            mbatch.append({
                'id_str': str(row.get('id_str', '')),
                'ra': float(row.get('ra', 0)),
                'dec': float(row.get('dec', 0)),
            })
        except Exception:
            n_err += 1
            continue

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
                    'confidence': float(p.max()),
                })
            n_proc += len(ibatch)
            ibatch, mbatch = [], []

            if n_proc % 10000 < BS:
                elapsed = time.time() - t_chunk
                rate = n_proc / elapsed if elapsed > 0 else 0
                print(f"    {chunk_start+n_proc:,}/{N:,} | {rate:.0f}/s | err={n_err}", flush=True)

    # Remaining batch
    if ibatch:
        bt = torch.stack(ibatch).to(DEVICE)
        with torch.no_grad():
            probs = torch.softmax(model(bt), dim=1).cpu().numpy()
        for m, p in zip(mbatch, probs):
            cls = int(p.argmax())
            catalog.append({
                'id_str': m['id_str'], 'ra': m['ra'], 'dec': m['dec'],
                'p_cw': float(p[0]), 'p_ccw': float(p[1]), 'p_ns': float(p[2]),
                'class': CLASS_NAMES[cls],
                'confidence': float(p.max()),
            })
        n_proc += len(ibatch)

    # Save chunk
    chunk_df = pd.DataFrame(catalog)
    chunk_df.to_parquet(f"{SHARD_DIR}/range_{chunk_start}_{chunk_end}.parquet")

    cw = (chunk_df['class'] == 'CW').sum()
    ccw = (chunk_df['class'] == 'CCW').sum()
    ns = (chunk_df['class'] == 'NOT_SPIRAL').sum()
    elapsed = time.time() - t_chunk

    total_done = already_done + chunk_end
    pct = total_done / N * 100
    eta_h = (N - total_done) / (n_proc / elapsed) / 3600 if elapsed > 0 and n_proc > 0 else 999

    print(f"  Done: {n_proc:,} in {elapsed/60:.1f}min | CW={cw:,} CCW={ccw:,} NS={ns:,} | Total: {total_done:,}/{N:,} ({pct:.1f}%) ETA={eta_h:.1f}h", flush=True)
    already_done = total_done

# Merge all chunks
print(f"\n[Final] Merging all chunks...", flush=True)
all_dfs = []
for f in sorted(os.listdir(SHARD_DIR)):
    if f.endswith('.parquet'):
        all_dfs.append(pd.read_parquet(f"{SHARD_DIR}/{f}"))

final = pd.concat(all_dfs, ignore_index=True)
final.to_parquet(f"{OUTPUT_DIR}/chirality_catalog_v2_full.parquet")

n_cw = (final['class'] == 'CW').sum()
n_ccw = (final['class'] == 'CCW').sum()
n_ns = (final['class'] == 'NOT_SPIRAL').sum()
elapsed_h = (time.time() - t_global) / 3600

print(f"\n{'='*70}", flush=True)
print(f"COMPLETE: {len(final):,} galaxies in {elapsed_h:.1f}h", flush=True)
print(f"CW: {n_cw:,} CCW: {n_ccw:,} NS: {n_ns:,} CW/(CW+CCW)={n_cw/(n_cw+n_ccw):.4f}", flush=True)
print(f"{'='*70}", flush=True)

json.dump({
    'n_total': len(final), 'n_cw': int(n_cw), 'n_ccw': int(n_ccw), 'n_ns': int(n_ns),
    'cw_spiral_frac': float(n_cw/(n_cw+n_ccw)), 'runtime_h': float(elapsed_h),
}, open(f"{OUTPUT_DIR}/v2_full_summary.json", 'w'), indent=2)
