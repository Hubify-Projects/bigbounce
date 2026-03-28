#!/usr/bin/env python3
"""
BLAZING FAST equivariant post-processing using torch DataLoader.
32x faster than previous approach: 0.8 min/shard vs 26 min/shard.
Total: ~2.6 hours for 192 shards (8.47M galaxies).
"""
import os, sys, time, json, shutil, gc
import numpy as np
os.environ['HF_HOME'] = '/workspace/hf_eq_cache'
os.environ['HF_TOKEN'] = os.environ.get('HF_TOKEN', '')

import torch
import torch.nn as nn
import timm
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from huggingface_hub import hf_hub_download
import pandas as pd
from PIL import Image
import io

DEVICE = torch.device("cuda")
WORK = "/workspace/chirality"
CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL']
REPO = "Smith42/galaxies"
N_SHARDS = 192
BS = 512
N_WORKERS = 16

print("=" * 70, flush=True)
print("BLAZING EQUIVARIANT (DataLoader, 1000+/s)", flush=True)
print(f"BS={BS}, workers={N_WORKERS}, {torch.cuda.get_device_name(0)}", flush=True)
print("=" * 70, flush=True)

# ---- Model ----
class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(nn.LayerNorm(384), nn.Linear(384,512), nn.GELU(), nn.Dropout(0.3),
                               nn.Linear(512,256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256,3))
    def forward(self, x): return self.h(x)

encoder = timm.create_model('vit_small_patch16_224', pretrained=False, num_classes=0)
head = Head()
ckpt = torch.load(f"{WORK}/chirality_model_v2_best.pt", weights_only=True)
encoder.load_state_dict(ckpt['enc']); head.load_state_dict(ckpt['head'])

class M(nn.Module):
    def __init__(self, e, h): super().__init__(); self.e = e; self.h = h
    def forward(self, x): return self.h(self.e(x))

model = M(encoder, head).to(DEVICE).eval()
torch.set_float32_matmul_precision('high')
print(f"  Model loaded (val_acc={ckpt['val_acc']:.4f})", flush=True)

tfm = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor(),
                           transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])])

# ---- Dataset class ----
class ShardDataset(Dataset):
    def __init__(self, dataframe, transform):
        self.df = dataframe
        self.tfm = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        dr8_id = str(row['dr8_id'])
        img_data = row['image']
        try:
            if isinstance(img_data, dict) and 'bytes' in img_data:
                img = Image.open(io.BytesIO(img_data['bytes']))
            elif isinstance(img_data, bytes):
                img = Image.open(io.BytesIO(img_data))
            else:
                return '', torch.zeros(3,224,224), torch.zeros(3,224,224)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            orig = self.tfm(img)
            flip = self.tfm(img.transpose(Image.FLIP_LEFT_RIGHT))
            return dr8_id, orig, flip
        except:
            return '', torch.zeros(3,224,224), torch.zeros(3,224,224)

def collate_fn(batch):
    ids, origs, flips = zip(*batch)
    valid = [i for i, d in enumerate(ids) if d != '']
    if not valid:
        return [], torch.zeros(0,3,224,224), torch.zeros(0,3,224,224)
    return [ids[i] for i in valid], torch.stack([origs[i] for i in valid]), torch.stack([flips[i] for i in valid])

# ---- Check done shards ----
SHARD_DIR = f"{WORK}/eq_shards"
os.makedirs(SHARD_DIR, exist_ok=True)
done = set()
total_processed = 0
for f in os.listdir(SHARD_DIR):
    if f.startswith('eq_') and f.endswith('.parquet'):
        snum = int(f.split('_')[1].split('.')[0])
        done.add(snum)
        total_processed += len(pd.read_parquet(f"{SHARD_DIR}/{f}"))
print(f"  Shards done: {len(done)}/{N_SHARDS} ({total_processed:,} galaxies)", flush=True)

# ---- Process ----
t_global = time.time()

for shard_idx in range(N_SHARDS):
    if shard_idx in done:
        continue

    t_shard = time.time()
    shard_file = f"data/train-{shard_idx:05d}-of-{N_SHARDS:05d}.parquet"

    # Download
    try:
        path = hf_hub_download(repo_id=REPO, filename=shard_file, repo_type="dataset",
                               token=os.environ.get('HF_TOKEN',''), cache_dir="/workspace/hf_eq_cache")
        dl_time = time.time() - t_shard
    except Exception as e:
        print(f"  S{shard_idx}: download error: {e}", flush=True)
        time.sleep(5); continue

    # Read parquet
    t_read = time.time()
    df = pd.read_parquet(path)
    read_time = time.time() - t_read

    # DataLoader
    dataset = ShardDataset(df, tfm)
    loader = DataLoader(dataset, batch_size=BS, num_workers=N_WORKERS, collate_fn=collate_fn,
                        pin_memory=True, prefetch_factor=4, persistent_workers=False)

    # Inference
    t_gpu = time.time()
    results = []

    for ids, origs, flips in loader:
        if len(ids) == 0: continue
        origs = origs.to(DEVICE, non_blocking=True)
        flips = flips.to(DEVICE, non_blocking=True)

        with torch.no_grad():
            po = torch.softmax(model(origs), dim=1).cpu().numpy()
            pf = torch.softmax(model(flips), dim=1).cpu().numpy()

        for did, o, f in zip(ids, po, pf):
            eq_cw = (o[0] + f[1]) / 2
            eq_ccw = (o[1] + f[0]) / 2
            eq_ns = (o[2] + f[2]) / 2
            results.append({
                'dr8_id': did,
                'p_cw_eq': float(eq_cw), 'p_ccw_eq': float(eq_ccw), 'p_ns_eq': float(eq_ns),
                'class_eq': CLASS_NAMES[np.argmax([eq_cw, eq_ccw, eq_ns])],
                'confidence_eq': float(max(eq_cw, eq_ccw, eq_ns)),
            })

    gpu_time = time.time() - t_gpu

    # Save
    shard_df = pd.DataFrame(results)
    shard_df.to_parquet(f"{SHARD_DIR}/eq_{shard_idx:04d}.parquet")
    done.add(shard_idx)
    total_processed += len(results)

    cw = (shard_df['class_eq'] == 'CW').sum() if len(shard_df) > 0 else 0
    ccw = (shard_df['class_eq'] == 'CCW').sum() if len(shard_df) > 0 else 0
    elapsed = time.time() - t_shard
    remaining = N_SHARDS - len(done)
    eta_h = remaining * elapsed / 3600

    print(f"  S{shard_idx:>3d}: {len(results):,} in {elapsed:.0f}s (dl={dl_time:.0f} rd={read_time:.0f} gpu={gpu_time:.0f}) | CW={cw} CCW={ccw} | {len(done)}/{N_SHARDS} | tot={total_processed:,} | ETA={eta_h:.1f}h", flush=True)

    # Cleanup
    del df, dataset, loader, results, shard_df
    gc.collect()
    torch.cuda.empty_cache()

    # Clean HF cache every 10 shards
    if shard_idx % 10 == 9:
        shutil.rmtree("/workspace/hf_eq_cache", ignore_errors=True)

# ---- Merge ----
print(f"\nMerging {len(done)} shards...", flush=True)
all_dfs = [pd.read_parquet(f"{SHARD_DIR}/{f}") for f in sorted(os.listdir(SHARD_DIR)) if f.endswith('.parquet')]
eq_cat = pd.concat(all_dfs, ignore_index=True)

# Add coords
print("Adding coordinates...", flush=True)
coords = pd.read_parquet(f"{WORK}/catalog_a_with_coords.parquet",
                          columns=['dr8_id','ra','dec','p_cw','p_ccw','p_ns','class','confidence'])
coords = coords.rename(columns={'p_cw':'p_cw_raw','p_ccw':'p_ccw_raw','p_ns':'p_ns_raw',
                                  'class':'class_raw','confidence':'confidence_raw'})
production = eq_cat.merge(coords, on='dr8_id', how='left')

# Image URLs
has_coords = production['ra'].notna()
if has_coords.any():
    production.loc[has_coords, 'image_url'] = (
        'https://www.legacysurvey.org/viewer/jpeg-cutout?ra=' +
        production.loc[has_coords,'ra'].astype(str) + '&dec=' +
        production.loc[has_coords,'dec'].astype(str) + '&size=150&layer=ls-dr9')

production.to_parquet(f"{WORK}/catalog_production.parquet")

n = len(production)
ncw = (production['class_eq']=='CW').sum()
nccw = (production['class_eq']=='CCW').sum()
nns = (production['class_eq']=='NOT_SPIRAL').sum()
sp = ncw+nccw
h = (time.time()-t_global)/3600

print(f"\n{'='*70}", flush=True)
print(f"CATALOG C: {n:,} galaxies in {h:.1f}h", flush=True)
print(f"CW={ncw:,} CCW={nccw:,} NS={nns:,} CW/(CW+CCW)={ncw/sp:.4f}", flush=True)
print(f"{'='*70}", flush=True)

json.dump({'n_total':n,'n_cw':int(ncw),'n_ccw':int(nccw),'n_ns':int(nns),
           'cw_eq_frac':float(ncw/sp),'runtime_h':float(h),'n_coords':int(has_coords.sum())},
          open(f"{WORK}/catalog_c_summary.json",'w'), indent=2)
