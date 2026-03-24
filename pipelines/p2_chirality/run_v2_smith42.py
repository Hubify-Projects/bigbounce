#!/usr/bin/env python3
"""
v2 Chirality Inference on Smith42/galaxies — 8.47M DESI Legacy DR8 images.

Downloads one shard at a time (5GB) to /tmp, processes with GPU, saves
results to /workspace, deletes shard, moves to next. Crash-recoverable
via per-shard checkpoint files.

Dataset: Smith42/galaxies (HuggingFace)
  - 192 train shards x 44,139 images x 5GB each
  - Columns: image (PIL), dr8_id (string)
  - Total: 8,474,688 galaxies

Model: chirality_model_v2_best.pt (93.7% val, 8/8 bias tests pass)
Output: per-shard parquets -> merged final catalog
"""
import os, sys, time, json, shutil
import numpy as np

# Set HF cache to /tmp (container disk, not workspace)
os.environ['HF_HOME'] = '/tmp/hf_smith42'
os.environ['HF_DATASETS_CACHE'] = '/tmp/hf_smith42/datasets'
HF_TOKEN = os.environ.get('HF_TOKEN', '')

import torch
import torch.nn as nn
import timm
from torchvision import transforms
from huggingface_hub import hf_hub_download
import pandas as pd
from PIL import Image
import io

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"
SHARD_DIR = f"{OUTPUT_DIR}/smith42_shards"
os.makedirs(SHARD_DIR, exist_ok=True)

N_SHARDS = 192
REPO = "Smith42/galaxies"
CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL']
BS = 64

print("=" * 70, flush=True)
print("v2 INFERENCE: Smith42/galaxies — 8.47M GALAXIES", flush=True)
print("=" * 70, flush=True)

# ---- Load model ----
print("[1] Loading v2 model...", flush=True)

class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(384), nn.Linear(384, 512), nn.GELU(), nn.Dropout(0.3),
            nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3))
    def forward(self, x):
        return self.h(x)

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
    def forward(self, x):
        return self.h(self.e(x))

model = Model(encoder, head).to(DEVICE).eval()
print(f"  Loaded (val_acc={ckpt['val_acc']:.4f})", flush=True)

tfm = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# ---- Check completed shards ----
done_shards = set()
for f in os.listdir(SHARD_DIR):
    if f.startswith('shard_') and f.endswith('.parquet'):
        try:
            snum = int(f.split('_')[1].split('.')[0])
            done_shards.add(snum)
        except:
            pass

already_galaxies = 0
for s in done_shards:
    try:
        sdf = pd.read_parquet(f"{SHARD_DIR}/shard_{s:04d}.parquet")
        already_galaxies += len(sdf)
    except:
        done_shards.discard(s)

print(f"  Shards done: {len(done_shards)}/{N_SHARDS} ({already_galaxies:,} galaxies)", flush=True)

# ---- Process each shard ----
print(f"\n[2] Processing {N_SHARDS} shards...", flush=True)
t_global = time.time()

for shard_idx in range(N_SHARDS):
    if shard_idx in done_shards:
        continue

    shard_file = f"data/train-{shard_idx:05d}-of-{N_SHARDS:05d}.parquet"
    print(f"\n[Shard {shard_idx}/{N_SHARDS-1}] Downloading {shard_file}...", flush=True)
    t_shard = time.time()

    # Download shard to /tmp
    try:
        local_path = hf_hub_download(
            repo_id=REPO,
            filename=shard_file,
            repo_type="dataset",
            token=HF_TOKEN,
            cache_dir="/tmp/hf_smith42",
        )
        dl_time = time.time() - t_shard
        print(f"  Downloaded in {dl_time:.0f}s", flush=True)
    except Exception as e:
        print(f"  ERROR downloading: {e}", flush=True)
        continue

    # Read parquet
    try:
        df = pd.read_parquet(local_path)
        n_rows = len(df)
        print(f"  Loaded: {n_rows:,} galaxies", flush=True)
    except Exception as e:
        print(f"  ERROR reading parquet: {e}", flush=True)
        continue

    # Process images
    catalog = []
    ibatch = []
    mbatch = []
    n_err = 0

    for i in range(n_rows):
        try:
            row = df.iloc[i]
            img = row['image']

            # Handle different image formats
            if isinstance(img, dict) and 'bytes' in img:
                img = Image.open(io.BytesIO(img['bytes']))
            elif isinstance(img, bytes):
                img = Image.open(io.BytesIO(img))
            elif not isinstance(img, Image.Image):
                n_err += 1
                continue

            if img.mode != 'RGB':
                img = img.convert('RGB')

            ibatch.append(tfm(img))
            mbatch.append({
                'dr8_id': str(row.get('dr8_id', '')),
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
                    'dr8_id': m['dr8_id'],
                    'p_cw': float(p[0]),
                    'p_ccw': float(p[1]),
                    'p_ns': float(p[2]),
                    'class': CLASS_NAMES[cls],
                    'confidence': float(p.max()),
                })

            ibatch = []
            mbatch = []

            if len(catalog) % 10000 < BS:
                elapsed = time.time() - t_shard
                rate = len(catalog) / (elapsed - dl_time) if (elapsed - dl_time) > 0 else 0
                print(f"    {len(catalog):,}/{n_rows:,} | {rate:.0f}/s | err={n_err}", flush=True)

    # Process remaining batch
    if ibatch:
        bt = torch.stack(ibatch).to(DEVICE)
        with torch.no_grad():
            probs = torch.softmax(model(bt), dim=1).cpu().numpy()
        for m, p in zip(mbatch, probs):
            cls = int(p.argmax())
            catalog.append({
                'dr8_id': m['dr8_id'],
                'p_cw': float(p[0]),
                'p_ccw': float(p[1]),
                'p_ns': float(p[2]),
                'class': CLASS_NAMES[cls],
                'confidence': float(p.max()),
            })

    # Save shard results
    shard_df = pd.DataFrame(catalog)
    shard_df.to_parquet(f"{SHARD_DIR}/shard_{shard_idx:04d}.parquet")

    cw = (shard_df['class'] == 'CW').sum()
    ccw = (shard_df['class'] == 'CCW').sum()
    ns = (shard_df['class'] == 'NOT_SPIRAL').sum()
    elapsed = time.time() - t_shard
    already_galaxies += len(catalog)
    done_shards.add(shard_idx)

    pct = already_galaxies / (N_SHARDS * 44139) * 100
    eta_h = (N_SHARDS - len(done_shards)) * elapsed / 3600

    print(f"  Shard {shard_idx} DONE: {len(catalog):,} in {elapsed/60:.1f}min | CW={cw:,} CCW={ccw:,} NS={ns:,} | err={n_err}", flush=True)
    print(f"  PROGRESS: {already_galaxies:,}/8.47M ({pct:.1f}%) | {len(done_shards)}/{N_SHARDS} shards | ETA={eta_h:.1f}h", flush=True)

    # Clean cache to free /tmp
    shutil.rmtree("/tmp/hf_smith42", ignore_errors=True)

# ---- Merge all shards ----
print(f"\n[3] Merging {len(done_shards)} shards...", flush=True)
all_dfs = []
for f in sorted(os.listdir(SHARD_DIR)):
    if f.endswith('.parquet'):
        all_dfs.append(pd.read_parquet(f"{SHARD_DIR}/{f}"))

final = pd.concat(all_dfs, ignore_index=True)
final.to_parquet(f"{OUTPUT_DIR}/chirality_catalog_v2_smith42.parquet")

n_total = len(final)
n_cw = (final['class'] == 'CW').sum()
n_ccw = (final['class'] == 'CCW').sum()
n_ns = (final['class'] == 'NOT_SPIRAL').sum()
n_spiral = n_cw + n_ccw
elapsed_h = (time.time() - t_global) / 3600

print(f"\n{'=' * 70}", flush=True)
print(f"COMPLETE: {n_total:,} galaxies in {elapsed_h:.1f}h", flush=True)
print(f"CW: {n_cw:,} ({n_cw/n_total*100:.1f}%)", flush=True)
print(f"CCW: {n_ccw:,} ({n_ccw/n_total*100:.1f}%)", flush=True)
print(f"NOT_SPIRAL: {n_ns:,} ({n_ns/n_total*100:.1f}%)", flush=True)
print(f"CW/(CW+CCW): {n_cw/n_spiral:.4f}", flush=True)
print(f"{'=' * 70}", flush=True)

json.dump({
    'dataset': 'Smith42/galaxies',
    'n_total': n_total, 'n_cw': int(n_cw), 'n_ccw': int(n_ccw), 'n_ns': int(n_ns),
    'cw_spiral_frac': float(n_cw / n_spiral),
    'runtime_h': float(elapsed_h),
    'n_shards': N_SHARDS,
    'model_val_acc': float(ckpt['val_acc']),
}, open(f"{OUTPUT_DIR}/smith42_summary.json", 'w'), indent=2)

print("\nCatalog saved: chirality_catalog_v2_smith42.parquet", flush=True)
