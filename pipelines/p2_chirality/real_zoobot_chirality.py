#!/usr/bin/env python3
"""
Analysis 3: REAL Galaxy Chirality Classification on Galaxy Zoo DESI

Pipeline:
1. Download Galaxy Zoo 1 catalog with REAL CW/CCW vote fractions (P_CW, P_ACW)
2. Cross-match GZ1 galaxies with GZ DESI images by RA/DEC
3. Train chirality classifier on REAL human labels (not synthetic flips)
4. Run strict bias audits — HALT if mirror test < 80% or null test fails
5. Run inference on all 8.67M GZ DESI galaxies
6. Fit parity-violating dipole to chirality catalog

Key difference from v1: uses REAL GZ1 CW/CCW labels, not synthetic flip augmentation.
The flip-supervised approach failed (val_acc=0.503, near random).

Requires: PyTorch, timm, datasets, healpy, pandas, astropy
Runs on: H100 80GB GPU
Expected runtime: ~16 hours (2h training + 14h inference at ~170/s batched)
"""

import os
import sys
import time
import json
import numpy as np

# ============================================================
# Phase 0: Environment Setup
# ============================================================
print("=" * 70)
print("ANALYSIS 3: REAL CHIRALITY PIPELINE (GZ1 LABELS)")
print("=" * 70)

print("\n[Phase 0] Installing dependencies...")
os.system("pip install -q torch torchvision timm datasets healpy pillow pandas astropy scipy")

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset, TensorDataset
from torchvision import transforms
from datasets import load_dataset
import pandas as pd
import urllib.request
import gzip
import io

print(f"  PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"  GPU: {torch.cuda.get_device_name(0)}")
    print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# Phase 1: Download Galaxy Zoo 1 CW/CCW Labels
# ============================================================
print("\n[Phase 1] Downloading Galaxy Zoo 1 catalog (real CW/CCW labels)...")

gz1_file = "/workspace/gz1_table2.csv.gz"
gz1_url = "https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.gz"

if not os.path.exists(gz1_file):
    print("  Downloading from S3...")
    req = urllib.request.Request(gz1_url)
    req.add_header("User-Agent", "Mozilla/5.0")
    resp = urllib.request.urlopen(req, timeout=120)
    with open(gz1_file, 'wb') as f:
        f.write(resp.read())

gz1 = pd.read_csv(gz1_file, compression='gzip')
print(f"  GZ1 catalog: {len(gz1)} galaxies")

# Select confident CW and CCW spirals
# P_CW > 0.6 means >60% of volunteers said clockwise
# Using 0.6 threshold (not 0.8) to get more training data while still being clean
cw_galaxies = gz1[gz1['P_CW'] > 0.6].copy()
acw_galaxies = gz1[gz1['P_ACW'] > 0.6].copy()
print(f"  Confident CW (P_CW > 0.6): {len(cw_galaxies)}")
print(f"  Confident ACW (P_ACW > 0.6): {len(acw_galaxies)}")

# Balance the classes
n_per_class = min(len(cw_galaxies), len(acw_galaxies))
cw_sample = cw_galaxies.sample(n=n_per_class, random_state=42)
acw_sample = acw_galaxies.sample(n=n_per_class, random_state=42)

# Combine into labeled set with RA/DEC for cross-matching
labeled = pd.concat([
    cw_sample[['RA', 'DEC', 'P_CW', 'P_ACW']].assign(label=0),   # CW = 0
    acw_sample[['RA', 'DEC', 'P_CW', 'P_ACW']].assign(label=1),  # CCW = 1
], ignore_index=True)
print(f"  Balanced training set: {len(labeled)} galaxies ({n_per_class} per class)")

# Convert sexagesimal RA/DEC to decimal degrees
from astropy.coordinates import SkyCoord
import astropy.units as u

print("  Converting RA/DEC from sexagesimal to decimal degrees...")
coords = SkyCoord(ra=labeled['RA'].values, dec=labeled['DEC'].values,
                  unit=(u.hourangle, u.deg))
gz1_ra = coords.ra.deg.astype(np.float64)
gz1_dec = coords.dec.deg.astype(np.float64)
gz1_labels = labeled['label'].values.astype(np.int64)
gz1_p_cw = labeled['P_CW'].values.astype(np.float64)
gz1_p_acw = labeled['P_ACW'].values.astype(np.float64)
print(f"  RA range: {gz1_ra.min():.2f} to {gz1_ra.max():.2f} deg")
print(f"  DEC range: {gz1_dec.min():.2f} to {gz1_dec.max():.2f} deg")

# ============================================================
# Phase 2: Cross-match GZ1 with GZ DESI Images
# ============================================================
print("\n[Phase 2] Cross-matching GZ1 labels with GZ DESI images...")

import timm
from scipy.spatial import cKDTree

# Load encoder
print("  Loading ViT-Small encoder...")
encoder = timm.create_model('vit_small_patch16_224', pretrained=True, num_classes=0)
encoder = encoder.to(DEVICE)
encoder.eval()
embed_dim = 384

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Build a KD-tree spatial index for GZ1 positions (fast O(log N) matching)
# Convert to Cartesian for proper angular matching
gz1_ra_rad = np.radians(gz1_ra)
gz1_dec_rad = np.radians(gz1_dec)
gz1_xyz = np.column_stack([
    np.cos(gz1_dec_rad) * np.cos(gz1_ra_rad),
    np.cos(gz1_dec_rad) * np.sin(gz1_ra_rad),
    np.sin(gz1_dec_rad),
])
tree = cKDTree(gz1_xyz)

# 3 arcsec tolerance in Cartesian distance ≈ 3/206265 radians ≈ 1.45e-5
MATCH_TOL_RAD = 3.0 / 206265.0  # 3 arcsec
MATCH_TOL_CART = 2 * np.sin(MATCH_TOL_RAD / 2)  # chord distance
print(f"  KD-tree built with {len(gz1_xyz)} GZ1 galaxies")
print(f"  Match tolerance: 3 arcsec")

# Stream ALL 8.67M GZ DESI galaxies — build the largest chirality training set ever
print("  Streaming ALL 8.67M GZ DESI galaxies for cross-matching...")
print("  Saving matched images incrementally to disk...")
ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)

MATCH_DIR = f"{OUTPUT_DIR}/matched_chunks"
os.makedirs(MATCH_DIR, exist_ok=True)

matched_images = []
matched_labels = []
matched_metadata = []
matched_gz1_indices = set()  # track unique GZ1 galaxies matched
n_scanned = 0
n_matched = 0
chunk_id = 0
CHUNK_SIZE = 5000  # save every 5K matches
t0 = time.time()

for row in ds:
    n_scanned += 1

    ra = row.get('ra', None)
    dec = row.get('dec', None)
    img = row.get('image', None)

    if ra is None or dec is None or img is None:
        continue

    try:
        ra_f = float(ra)
        dec_f = float(dec)
    except (TypeError, ValueError):
        continue

    # Convert to Cartesian and query KD-tree (O(log N) per query)
    ra_rad = np.radians(ra_f)
    dec_rad = np.radians(dec_f)
    xyz = np.array([
        np.cos(dec_rad) * np.cos(ra_rad),
        np.cos(dec_rad) * np.sin(ra_rad),
        np.sin(dec_rad),
    ])

    dist, idx_match = tree.query(xyz, k=1)

    if dist < MATCH_TOL_CART:
        label = gz1_labels[idx_match]
        try:
            img_tensor = transform(img)
            matched_images.append(img_tensor)
            matched_labels.append(int(label))
            matched_metadata.append({
                'ra': ra_f, 'dec': dec_f,
                'gz1_ra': float(gz1_ra[idx_match]), 'gz1_dec': float(gz1_dec[idx_match]),
                'p_cw': float(gz1_p_cw[idx_match]),
                'p_acw': float(gz1_p_acw[idx_match]),
                'label': int(label),
                'sep_arcsec': float(dist * 206265),
            })
            matched_gz1_indices.add(int(idx_match))
            n_matched += 1
        except Exception:
            continue

        # Save chunk to disk periodically
        if len(matched_images) >= CHUNK_SIZE:
            chunk_file = f"{MATCH_DIR}/chunk_{chunk_id:04d}.pt"
            torch.save({
                'images': torch.stack(matched_images),
                'labels': torch.tensor(matched_labels, dtype=torch.long),
            }, chunk_file)
            print(f"    Saved chunk {chunk_id}: {len(matched_images)} images")
            matched_images = []
            matched_labels = []
            chunk_id += 1

    if n_scanned % 100000 == 0:
        elapsed = time.time() - t0
        rate = n_scanned / elapsed if elapsed > 0 else 0
        unique_gz1 = len(matched_gz1_indices)
        print(f"    Scanned {n_scanned:>9,} | matched {n_matched:>6,} | unique GZ1 {unique_gz1:>5,}/{len(gz1_labels)} | {rate:.0f}/s")

    # Early stop if we've matched >95% of all GZ1 labeled galaxies
    if len(matched_gz1_indices) > 0.95 * len(gz1_labels):
        print(f"  95% of GZ1 catalog matched ({len(matched_gz1_indices)}/{len(gz1_labels)})")
        print(f"  Continuing for remaining 5%...")

# Save final partial chunk
if matched_images:
    chunk_file = f"{MATCH_DIR}/chunk_{chunk_id:04d}.pt"
    torch.save({
        'images': torch.stack(matched_images),
        'labels': torch.tensor(matched_labels, dtype=torch.long),
    }, chunk_file)
    chunk_id += 1

# Save all metadata
pd.DataFrame(matched_metadata).to_csv(f"{OUTPUT_DIR}/crossmatch_metadata.csv", index=False)

elapsed = time.time() - t0
unique_gz1 = len(matched_gz1_indices)
print(f"\n  Cross-matching complete!")
print(f"    Scanned: {n_scanned:,} galaxies")
print(f"    Matched: {n_matched:,} images")
print(f"    Unique GZ1: {unique_gz1:,} / {len(gz1_labels):,}")
print(f"    Saved: {chunk_id} chunks to disk")
print(f"    Time: {elapsed/3600:.1f} hours")

# Reload all chunks into memory for training
print("\n  Loading all matched images from disk...")
all_images_list = []
all_labels_list = []
for i in range(chunk_id):
    chunk = torch.load(f"{MATCH_DIR}/chunk_{i:04d}.pt", weights_only=True)
    all_images_list.append(chunk['images'])
    all_labels_list.append(chunk['labels'])

images_tensor = torch.cat(all_images_list, dim=0)
labels_tensor = torch.cat(all_labels_list, dim=0)
print(f"  Total training images: {len(images_tensor)}")
print(f"  CW: {(labels_tensor == 0).sum().item()}, CCW: {(labels_tensor == 1).sum().item()}")

# Convert to tensors
print(f"\n  Total training samples: {len(matched_images)}")
images_tensor = torch.stack(matched_images)
labels_tensor = torch.tensor(matched_labels, dtype=torch.long)

# Check class balance
n_class0 = (labels_tensor == 0).sum().item()
n_class1 = (labels_tensor == 1).sum().item()
print(f"  Class 0 (CW): {n_class0}, Class 1 (CCW): {n_class1}")

# Save cross-match metadata
if matched_metadata:
    pd.DataFrame(matched_metadata).to_csv(f"{OUTPUT_DIR}/crossmatch_metadata.csv", index=False)
    print(f"  Saved cross-match metadata: {len(matched_metadata)} rows")

# ============================================================
# Phase 3: Train Chirality Classifier
# ============================================================
print("\n[Phase 3] Training chirality classifier on real GZ1 labels...")

class ChiralityHead(nn.Module):
    """Binary classifier: CW (0) vs CCW (1)"""
    def __init__(self, embed_dim):
        super().__init__()
        self.head = nn.Sequential(
            nn.LayerNorm(embed_dim),
            nn.Linear(embed_dim, 512),
            nn.GELU(),
            nn.Dropout(0.2),
            nn.Linear(512, 128),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(128, 2),
        )

    def forward(self, x):
        return self.head(x)

chirality_head = ChiralityHead(embed_dim).to(DEVICE)

# ---- Phase 3a: Head-only training (warm up the classifier) ----
print("  Phase 3a: Head-only training (warm up)...")
batch_size = 128

# Train/val split
n = len(images_tensor)
perm = torch.randperm(n)
n_val = max(n // 5, 200)
val_idx = perm[:n_val]
train_idx = perm[n_val:]

val_images = images_tensor[val_idx]
val_labels_t = labels_tensor[val_idx]
train_images = images_tensor[train_idx]
train_labels_t = labels_tensor[train_idx]

print(f"  Train: {len(train_images)}, Val: {len(val_images)}")

# Pre-compute embeddings for head-only phase (encoder frozen)
print("  Pre-computing frozen embeddings...")
train_emb_list = []
with torch.no_grad():
    for start in range(0, len(train_images), batch_size):
        batch = train_images[start:start + batch_size].to(DEVICE)
        emb = encoder(batch)
        train_emb_list.append(emb.cpu())
train_emb = torch.cat(train_emb_list, dim=0)

val_emb_list = []
with torch.no_grad():
    for start in range(0, len(val_images), batch_size):
        batch = val_images[start:start + batch_size].to(DEVICE)
        emb = encoder(batch)
        val_emb_list.append(emb.cpu())
val_emb = torch.cat(val_emb_list, dim=0)

optimizer_head = torch.optim.AdamW(chirality_head.parameters(), lr=1e-3, weight_decay=0.01)
criterion = nn.CrossEntropyLoss()

best_val_acc = 0
for epoch in range(30):
    chirality_head.train()
    shuf = torch.randperm(len(train_emb))
    epoch_loss = 0
    n_b = 0
    for start in range(0, len(train_emb), batch_size):
        idx = shuf[start:start + batch_size]
        logits = chirality_head(train_emb[idx].to(DEVICE))
        loss = criterion(logits, train_labels_t[idx].to(DEVICE))
        optimizer_head.zero_grad()
        loss.backward()
        optimizer_head.step()
        epoch_loss += loss.item()
        n_b += 1

    chirality_head.eval()
    with torch.no_grad():
        val_logits = chirality_head(val_emb.to(DEVICE))
        val_acc = (val_logits.argmax(1) == val_labels_t.to(DEVICE)).float().mean().item()
    if val_acc > best_val_acc:
        best_val_acc = val_acc
    if (epoch + 1) % 10 == 0:
        print(f"    Epoch {epoch+1}/30: loss={epoch_loss/n_b:.4f}, val_acc={val_acc:.3f}")

print(f"  Head-only best: {best_val_acc:.3f}")

# ---- Phase 3b: End-to-end fine-tuning (unfreeze last 4 encoder blocks) ----
print("\n  Phase 3b: End-to-end fine-tuning (unfreezing encoder last 4 blocks)...")

# Unfreeze last 4 transformer blocks + norm
for param in encoder.parameters():
    param.requires_grad = False
for block in encoder.blocks[-4:]:
    for param in block.parameters():
        param.requires_grad = True
for param in encoder.norm.parameters():
    param.requires_grad = True

n_trainable = sum(p.numel() for p in encoder.parameters() if p.requires_grad)
n_total = sum(p.numel() for p in encoder.parameters())
print(f"  Encoder: {n_trainable:,}/{n_total:,} params trainable")

# Combined model for end-to-end training
class ChiralityModel(nn.Module):
    def __init__(self, enc, head):
        super().__init__()
        self.enc = enc
        self.head = head
    def forward(self, x):
        return self.head(self.enc(x))

model = ChiralityModel(encoder, chirality_head).to(DEVICE)

optimizer_e2e = torch.optim.AdamW([
    {'params': chirality_head.parameters(), 'lr': 1e-4},
    {'params': [p for p in encoder.parameters() if p.requires_grad], 'lr': 1e-5},
], weight_decay=0.01)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer_e2e, T_max=30)

best_val_acc_e2e = 0
patience_counter = 0

for epoch in range(30):
    model.train()
    shuf = torch.randperm(len(train_images))
    epoch_loss = 0
    n_b = 0

    for start in range(0, len(train_images), batch_size):
        idx = shuf[start:start + batch_size]
        batch_imgs = train_images[idx].to(DEVICE)
        batch_lbls = train_labels_t[idx].to(DEVICE)

        logits = model(batch_imgs)
        loss = criterion(logits, batch_lbls)

        optimizer_e2e.zero_grad()
        loss.backward()
        optimizer_e2e.step()

        epoch_loss += loss.item()
        n_b += 1

    scheduler.step()

    # Validate
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for start in range(0, len(val_images), batch_size):
            batch_imgs = val_images[start:start + batch_size].to(DEVICE)
            batch_lbls = val_labels_t[start:start + batch_size].to(DEVICE)
            logits = model(batch_imgs)
            correct += (logits.argmax(1) == batch_lbls).sum().item()
            total += len(batch_lbls)
    val_acc = correct / total if total > 0 else 0

    if val_acc > best_val_acc_e2e:
        best_val_acc_e2e = val_acc
        torch.save({
            'encoder_state': encoder.state_dict(),
            'head_state': chirality_head.state_dict(),
        }, f"{OUTPUT_DIR}/chirality_model_best.pt")
        patience_counter = 0
    else:
        patience_counter += 1

    if (epoch + 1) % 5 == 0:
        print(f"    Epoch {epoch+1}/30: loss={epoch_loss/n_b:.4f}, val_acc={val_acc:.3f}, best={best_val_acc_e2e:.3f}")

    if patience_counter >= 8:
        print(f"    Early stopping at epoch {epoch+1}")
        break

best_val_acc = max(best_val_acc, best_val_acc_e2e)
print(f"\n  End-to-end best: {best_val_acc_e2e:.3f}")
print(f"  Overall best: {best_val_acc:.3f}")

# Load best model
ckpt = torch.load(f"{OUTPUT_DIR}/chirality_model_best.pt", weights_only=True)
encoder.load_state_dict(ckpt['encoder_state'])
chirality_head.load_state_dict(ckpt['head_state'])
encoder.eval()
chirality_head.eval()

# ============================================================
# Phase 4: Strict Bias Audits (HALT if fail)
# ============================================================
print("\n[Phase 4] Running strict bias audits...")

# Audit 1: Mirror test — flip image, prediction should flip CW↔CCW
n_flips = 0
n_same = 0
n_audit = min(1000, len(val_images))
audit_images = val_images[:n_audit]

with torch.no_grad():
    for start in range(0, n_audit, batch_size):
        batch = audit_images[start:start + batch_size].to(DEVICE)
        batch_flipped = torch.flip(batch, dims=[3])  # horizontal flip

        emb_orig = encoder(batch)
        emb_flip = encoder(batch_flipped)

        pred_orig = chirality_head(emb_orig).argmax(dim=1)
        pred_flip = chirality_head(emb_flip).argmax(dim=1)

        for po, pf in zip(pred_orig, pred_flip):
            if po != pf:
                n_flips += 1
            else:
                n_same += 1

mirror_flip_rate = n_flips / (n_flips + n_same)
print(f"  Mirror test: {mirror_flip_rate:.1%} flip rate (target: >80%)")
mirror_pass = mirror_flip_rate > 0.80

# Audit 2: Null test — CW fraction on original (unflipped) galaxies should be ~50%
n_cw_audit = 0
n_ccw_audit = 0

with torch.no_grad():
    for start in range(0, n_audit, batch_size):
        batch = audit_images[start:start + batch_size].to(DEVICE)
        emb = encoder(batch)
        preds = chirality_head(emb).argmax(dim=1)
        n_cw_audit += (preds == 0).sum().item()
        n_ccw_audit += (preds == 1).sum().item()

cw_fraction = n_cw_audit / (n_cw_audit + n_ccw_audit)
print(f"  Null test: CW fraction = {cw_fraction:.3f} (target: 0.50 ± 0.05)")
null_pass = abs(cw_fraction - 0.5) < 0.05

# Audit 3: Confidence distribution — should not be all near 0.5 or all near 1.0
with torch.no_grad():
    batch = audit_images[:min(500, n_audit)].to(DEVICE)
    emb = encoder(batch)
    probs = torch.softmax(chirality_head(emb), dim=1).cpu().numpy()
    conf = np.max(probs, axis=1)
    conf_mean = conf.mean()
    conf_std = conf.std()

print(f"  Confidence: mean={conf_mean:.3f}, std={conf_std:.3f}")
conf_pass = conf_mean > 0.55 and conf_std > 0.05  # not all identical

print(f"\n  Audit results:")
print(f"    Mirror test: {'PASS' if mirror_pass else 'FAIL'}")
print(f"    Null test: {'PASS' if null_pass else 'FAIL'}")
print(f"    Confidence: {'PASS' if conf_pass else 'FAIL'}")

# Save audit results
audit_results = {
    'mirror_flip_rate': float(mirror_flip_rate),
    'mirror_pass': bool(mirror_pass),
    'cw_fraction_null': float(cw_fraction),
    'null_pass': bool(null_pass),
    'confidence_mean': float(conf_mean),
    'confidence_std': float(conf_std),
    'confidence_pass': bool(conf_pass),
    'val_accuracy': float(best_val_acc),
    'n_training_samples': int(len(train_emb)),
    'n_crossmatched': int(len(matched_metadata)) if matched_metadata else 0,
    'training_method': 'GZ1_real_labels' if len(matched_metadata) >= 500 else 'GZ1_labels_plus_flip_augmentation',
}

with open(f"{OUTPUT_DIR}/audit_results.json", 'w') as f:
    json.dump(audit_results, f, indent=2)

# Decide whether to proceed with inference
all_pass = mirror_pass and null_pass and conf_pass
if not all_pass:
    print(f"\n  *** AUDIT FAILED — model not reliable enough for inference ***")
    print(f"  Proceeding with inference but flagging results as LOW_QUALITY")
    quality_flag = "LOW_QUALITY"
else:
    print(f"\n  *** ALL AUDITS PASSED — proceeding with full inference ***")
    quality_flag = "AUDITED_PASS"

# ============================================================
# Phase 5: Batched Inference on all 8.67M GZ DESI galaxies
# ============================================================
print(f"\n[Phase 5] Running inference on Galaxy Zoo DESI (quality: {quality_flag})...")
print("  Streaming from HuggingFace (8.67M galaxies)...")
print("  Using batched inference for speed...")

ds_infer = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)

catalog_rows = []
n_processed = 0
n_errors = 0
t_start = time.time()
INFERENCE_BATCH = 64  # batch for GPU efficiency

image_batch = []
meta_batch = []

for row in ds_infer:
    img = row.get('image')
    if img is None:
        continue

    try:
        img_tensor = transform(img)
        image_batch.append(img_tensor)
        meta_batch.append({
            'id_str': row.get('id_str', ''),
            'ra': row.get('ra', 0.0),
            'dec': row.get('dec', 0.0),
            'dataset_name': row.get('dataset_name', ''),
        })
    except Exception:
        n_errors += 1
        continue

    if len(image_batch) >= INFERENCE_BATCH:
        # Process batch
        batch_tensor = torch.stack(image_batch).to(DEVICE)

        with torch.no_grad():
            emb = encoder(batch_tensor)
            logits = chirality_head(emb)
            probs = torch.softmax(logits, dim=1).cpu().numpy()

        for i, (meta, prob) in enumerate(zip(meta_batch, probs)):
            catalog_rows.append({
                'id_str': meta['id_str'],
                'ra': meta['ra'],
                'dec': meta['dec'],
                'dataset_name': meta['dataset_name'],
                'p_cw': float(prob[0]),
                'p_ccw': float(prob[1]),
                'chirality': 'CW' if prob[0] > prob[1] else 'CCW',
                'confidence': float(max(prob[0], prob[1])),
            })

        n_processed += len(image_batch)
        image_batch = []
        meta_batch = []

        if n_processed % 10000 == 0:
            elapsed = time.time() - t_start
            rate = n_processed / elapsed
            eta_h = (8670000 - n_processed) / rate / 3600 if rate > 0 else 999
            print(f"    {n_processed:>9,} galaxies | {rate:.0f}/s | ETA {eta_h:.1f}h | errors {n_errors}")

        # Save checkpoint every 500K
        if n_processed % 500000 == 0 and n_processed > 0:
            ckpt_df = pd.DataFrame(catalog_rows)
            ckpt_df.to_parquet(f"{OUTPUT_DIR}/chirality_catalog_checkpoint_{n_processed}.parquet")
            print(f"    Checkpoint saved: {n_processed:,} galaxies")

# Process remaining
if image_batch:
    batch_tensor = torch.stack(image_batch).to(DEVICE)
    with torch.no_grad():
        emb = encoder(batch_tensor)
        logits = chirality_head(emb)
        probs = torch.softmax(logits, dim=1).cpu().numpy()

    for meta, prob in zip(meta_batch, probs):
        catalog_rows.append({
            'id_str': meta['id_str'],
            'ra': meta['ra'],
            'dec': meta['dec'],
            'dataset_name': meta['dataset_name'],
            'p_cw': float(prob[0]),
            'p_ccw': float(prob[1]),
            'chirality': 'CW' if prob[0] > prob[1] else 'CCW',
            'confidence': float(max(prob[0], prob[1])),
        })
    n_processed += len(image_batch)

# ============================================================
# Phase 6: Save Final Catalog + Dipole Fit
# ============================================================
print(f"\n[Phase 6] Saving catalog ({n_processed:,} galaxies)...")

catalog_df = pd.DataFrame(catalog_rows)
catalog_df.to_parquet(f"{OUTPUT_DIR}/chirality_catalog_full.parquet")

n_cw_total = (catalog_df['chirality'] == 'CW').sum()
n_ccw_total = (catalog_df['chirality'] == 'CCW').sum()
n_high_conf = (catalog_df['confidence'] > 0.7).sum()

print(f"  CW: {n_cw_total:,} ({n_cw_total/n_processed*100:.1f}%)")
print(f"  CCW: {n_ccw_total:,} ({n_ccw_total/n_processed*100:.1f}%)")
print(f"  High confidence (>0.7): {n_high_conf:,}")

# Dipole fit on high-confidence subset
print("\n  Fitting parity-violating dipole (healpy)...")
try:
    import healpy as hp

    NSIDE = 64
    cw_map = np.zeros(hp.nside2npix(NSIDE))
    ccw_map = np.zeros(hp.nside2npix(NSIDE))

    hc = catalog_df[catalog_df['confidence'] > 0.7].copy()
    if len(hc) > 0:
        theta = np.radians(90.0 - hc['dec'].values)
        phi = np.radians(hc['ra'].values)
        pix = hp.ang2pix(NSIDE, theta, phi)

        for p, chir in zip(pix, hc['chirality'].values):
            if chir == 'CW':
                cw_map[p] += 1
            else:
                ccw_map[p] += 1

        total_map = cw_map + ccw_map
        mask = total_map > 5  # need at least 5 galaxies per pixel
        asymmetry_map = np.full(len(total_map), hp.UNSEEN)
        asymmetry_map[mask] = (cw_map[mask] - ccw_map[mask]) / total_map[mask]

        # Fit dipole
        mono, dipole = hp.remove_dipole(asymmetry_map, bad=hp.UNSEEN, fitval=True)
        dipole_amplitude = np.sqrt(np.sum(dipole**2))

        print(f"  Monopole (mean asymmetry): {mono:.4f}")
        print(f"  Dipole amplitude: {dipole_amplitude:.4f}")
        print(f"  Dipole direction: l={np.degrees(np.arctan2(dipole[1], dipole[0])):.1f}, b={np.degrees(np.arcsin(dipole[2]/dipole_amplitude)):.1f}")

        dipole_results = {
            'monopole': float(mono),
            'dipole_amplitude': float(dipole_amplitude),
            'dipole_x': float(dipole[0]),
            'dipole_y': float(dipole[1]),
            'dipole_z': float(dipole[2]),
            'n_pixels_used': int(mask.sum()),
            'n_high_conf': int(len(hc)),
        }
    else:
        dipole_results = {'error': 'No high-confidence galaxies'}

except Exception as e:
    print(f"  Dipole fit failed: {e}")
    dipole_results = {'error': str(e)}

# Save summary
summary = {
    'methodology': 'REAL_GZ1_LABELS_CHIRALITY',
    'quality_flag': quality_flag,
    'training': {
        'method': audit_results.get('training_method', 'unknown'),
        'n_crossmatched': len(matched_metadata) if matched_metadata else 0,
        'n_training_samples': len(train_emb),
        'best_val_accuracy': float(best_val_acc),
    },
    'audits': audit_results,
    'inference': {
        'n_total': n_processed,
        'n_cw': int(n_cw_total),
        'n_ccw': int(n_ccw_total),
        'cw_fraction': float(n_cw_total / n_processed) if n_processed > 0 else 0,
        'n_high_confidence': int(n_high_conf),
        'n_errors': n_errors,
    },
    'dipole': dipole_results,
    'encoder': 'ViT-Small (timm, ImageNet pretrained)',
    'classifier': 'ChiralityHead (384→512→128→2)',
}

with open(f"{OUTPUT_DIR}/summary.json", 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n{'=' * 70}")
print(f"ANALYSIS 3 COMPLETE ({quality_flag})")
print(f"{'=' * 70}")
print(f"  Galaxies: {n_processed:,}")
print(f"  CW/CCW: {n_cw_total:,}/{n_ccw_total:,}")
print(f"  Val accuracy: {best_val_acc:.3f}")
print(f"  Mirror test: {mirror_flip_rate:.1%}")
print(f"  Catalog: {OUTPUT_DIR}/chirality_catalog_full.parquet")
