#!/usr/bin/env python3
"""
v2 Inference: Process one HuggingFace shard at a time.

Downloads each shard to /tmp (container disk), processes it, saves results
to /workspace, then deletes the shard before downloading the next.

This avoids: streaming 1-shard bug, workspace quota, and memory issues.
"""
import os, sys, time, json
import numpy as np
os.environ['HF_TOKEN'] = os.environ.get('HF_TOKEN', '')
os.environ['HF_HOME'] = '/tmp/HF_TOKEN_REDACTED'
os.environ['HF_DATASETS_CACHE'] = '/tmp/HF_TOKEN_REDACTED/datasets'

import torch
import torch.nn as nn
import timm
from torchvision import transforms
import pandas as pd

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"
SHARD_DIR = f"{OUTPUT_DIR}/shard_results"
os.makedirs(SHARD_DIR, exist_ok=True)

print("=" * 70, flush=True)
print("v2 SHARD-BY-SHARD INFERENCE", flush=True)
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
CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL']
N_SHARDS = 28

# Check which shards are done
done = set()
for f in os.listdir(SHARD_DIR):
    if f.startswith('shard_') and f.endswith('.parquet'):
        done.add(int(f.split('_')[1].split('.')[0]))
print(f"  Shards done: {sorted(done) if done else 'none'}", flush=True)

t_global = time.time()
total_all = 0

for shard in range(N_SHARDS):
    if shard in done:
        try:
            sdf = pd.read_parquet(f"{SHARD_DIR}/shard_{shard:02d}.parquet")
            total_all += len(sdf)
            print(f"\n[Shard {shard}/27] SKIP ({len(sdf):,} already done)", flush=True)
        except:
            done.discard(shard)  # Re-process if can't read
        if shard in done:
            continue

    print(f"\n[Shard {shard}/27] Downloading...", flush=True)
    t_shard = time.time()

    # Download just this shard using data_files
    try:
        from datasets import load_dataset
        shard_file = f"data/train-{shard:05d}-of-{N_SHARDS:05d}.parquet"
        ds = load_dataset("mwalmsley/gz_desi", data_files=shard_file,
                          split="train", cache_dir="/tmp/HF_TOKEN_REDACTED/datasets")
        n_rows = len(ds)
        print(f"  Downloaded: {n_rows:,} galaxies ({time.time()-t_shard:.0f}s)", flush=True)
    except Exception as e:
        print(f"  ERROR downloading shard {shard}: {e}", flush=True)
        # Try alternative: streaming with skip
        try:
            ds_stream = load_dataset("mwalmsley/gz_desi", data_files=shard_file,
                                     split="train", streaming=True)
            rows = list(ds_stream)
            n_rows = len(rows)
            print(f"  Streamed: {n_rows:,} galaxies", flush=True)
            # Create a simple indexed accessor
            class ListDataset:
                def __init__(self, data):
                    self.data = data
                def __len__(self):
                    return len(self.data)
                def __getitem__(self, i):
                    return self.data[i]
            ds = ListDataset(rows)
        except Exception as e2:
            print(f"  FATAL: Cannot load shard {shard}: {e2}", flush=True)
            continue

    # Process shard
    catalog = []
    BS = 64
    ibatch, mbatch = [], []
    n_err = 0

    for i in range(n_rows):
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
        except:
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
                    'class': CLASS_NAMES[cls], 'confidence': float(p.max()),
                })
            ibatch, mbatch = [], []

            if len(catalog) % 10000 < BS:
                elapsed = time.time() - t_shard
                rate = len(catalog) / elapsed if elapsed > 0 else 0
                print(f"    {len(catalog):,}/{n_rows:,} | {rate:.0f}/s", flush=True)

    # Process remaining
    if ibatch:
        bt = torch.stack(ibatch).to(DEVICE)
        with torch.no_grad():
            probs = torch.softmax(model(bt), dim=1).cpu().numpy()
        for m, p in zip(mbatch, probs):
            cls = int(p.argmax())
            catalog.append({
                'id_str': m['id_str'], 'ra': m['ra'], 'dec': m['dec'],
                'p_cw': float(p[0]), 'p_ccw': float(p[1]), 'p_ns': float(p[2]),
                'class': CLASS_NAMES[cls], 'confidence': float(p.max()),
            })

    # Save shard results
    sdf = pd.DataFrame(catalog)
    sdf.to_parquet(f"{SHARD_DIR}/shard_{shard:02d}.parquet")
    total_all += len(catalog)

    cw = (sdf['class'] == 'CW').sum()
    ccw = (sdf['class'] == 'CCW').sum()
    ns = (sdf['class'] == 'NOT_SPIRAL').sum()
    elapsed = time.time() - t_shard

    print(f"  Shard {shard} done: {len(catalog):,} in {elapsed/60:.1f}min | CW={cw:,} CCW={ccw:,} NS={ns:,}", flush=True)
    print(f"  TOTAL: {total_all:,}/8.67M ({total_all/8670000*100:.1f}%)", flush=True)

    # Clean cache to free /tmp space
    import shutil
    shutil.rmtree("/tmp/HF_TOKEN_REDACTED", ignore_errors=True)
    os.makedirs("/tmp/HF_TOKEN_REDACTED/datasets", exist_ok=True)

# Merge all shards
print(f"\n[Final] Merging {len(os.listdir(SHARD_DIR))} shards...", flush=True)
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
