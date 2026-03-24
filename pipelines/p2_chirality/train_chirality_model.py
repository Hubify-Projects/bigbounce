#!/usr/bin/env python3
"""
Phase A: Train the BEST chirality classifier before scaling to 8.67M.

Strategy:
1. Quick cross-match scan (first 500K of GZ DESI → ~27K matched training images)
2. Train with end-to-end ViT fine-tuning + data augmentation
3. Run exhaustive bias audits
4. Benchmark against published results
5. Only proceed to Phase B (full inference) if mirror test >80%

This script produces a trained model. The full inference is separate.
"""

import os
import sys
import time
import json
import numpy as np

print("=" * 70)
print("CHIRALITY MODEL TRAINING (QUALITY-FIRST)")
print("=" * 70)

print("\n[Setup] Installing dependencies...")
os.system("pip install -q torch torchvision timm datasets healpy pillow pandas astropy scipy")

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from datasets import load_dataset
import pandas as pd
import urllib.request
import gzip
import io

print(f"  PyTorch {torch.__version__}, CUDA: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"  GPU: {torch.cuda.get_device_name(0)}")

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# Step 1: Load GZ1 CW/CCW Labels
# ============================================================
print("\n[Step 1] Loading Galaxy Zoo 1 CW/CCW labels...")

gz1_file = "/workspace/gz1_table2.csv.gz"
if not os.path.exists(gz1_file):
    print("  Downloading from S3...")
    req = urllib.request.Request("https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.gz")
    req.add_header("User-Agent", "Mozilla/5.0")
    resp = urllib.request.urlopen(req, timeout=120)
    with open(gz1_file, 'wb') as f:
        f.write(resp.read())

gz1 = pd.read_csv(gz1_file, compression='gzip')
print(f"  GZ1: {len(gz1)} galaxies")

# Select confident spirals (0.7 threshold for cleaner labels)
cw_gal = gz1[gz1['P_CW'] > 0.7].copy()
acw_gal = gz1[gz1['P_ACW'] > 0.7].copy()

n_per = min(len(cw_gal), len(acw_gal))
cw_sample = cw_gal.sample(n=n_per, random_state=42)
acw_sample = acw_gal.sample(n=n_per, random_state=42)

labeled = pd.concat([
    cw_sample[['RA', 'DEC', 'P_CW', 'P_ACW']].assign(label=0),
    acw_sample[['RA', 'DEC', 'P_CW', 'P_ACW']].assign(label=1),
], ignore_index=True)
print(f"  Balanced set: {len(labeled)} ({n_per} CW + {n_per} CCW)")

# Convert sexagesimal to decimal degrees
from astropy.coordinates import SkyCoord
import astropy.units as u

coords = SkyCoord(ra=labeled['RA'].values, dec=labeled['DEC'].values,
                  unit=(u.hourangle, u.deg))
gz1_ra = coords.ra.deg.astype(np.float64)
gz1_dec = coords.dec.deg.astype(np.float64)
gz1_labels = labeled['label'].values.astype(np.int64)
gz1_p_cw = labeled['P_CW'].values.astype(np.float64)
gz1_p_acw = labeled['P_ACW'].values.astype(np.float64)

# ============================================================
# Step 2: Cross-match with GZ DESI Images (first 500K only)
# ============================================================
print("\n[Step 2] Cross-matching GZ1 × GZ DESI (first 500K galaxies)...")

from scipy.spatial import cKDTree
import timm

# Build KD-tree
gz1_ra_rad = np.radians(gz1_ra)
gz1_dec_rad = np.radians(gz1_dec)
gz1_xyz = np.column_stack([
    np.cos(gz1_dec_rad) * np.cos(gz1_ra_rad),
    np.cos(gz1_dec_rad) * np.sin(gz1_ra_rad),
    np.sin(gz1_dec_rad),
])
tree = cKDTree(gz1_xyz)
MATCH_TOL_CART = 2 * np.sin(3.0 / 206265.0 / 2)  # 3 arcsec

print(f"  KD-tree: {len(gz1_xyz)} GZ1 galaxies")

# Image transforms — CRITICAL: no horizontal or vertical flips!
# Flipping CHANGES chirality (CW↔CCW) which corrupts labels.
# Only use chirality-preserving augmentations: rotation, color jitter, scale.
train_transform = transforms.Compose([
    transforms.Resize((240, 240)),
    transforms.RandomCrop(224),
    transforms.RandomRotation(360),  # rotation preserves chirality
    transforms.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.1),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

val_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Stream and collect matches
ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)

# Store raw PIL images (for augmented resampling during training)
matched_pil_images = []
matched_labels_list = []
matched_metadata = []
matched_gz1_set = set()
n_scanned = 0
t0 = time.time()
SCAN_LIMIT = 500_000  # Quick scan for training data

for row in ds:
    n_scanned += 1
    if n_scanned > SCAN_LIMIT:
        break

    ra = row.get('ra')
    dec = row.get('dec')
    img = row.get('image')
    if ra is None or dec is None or img is None:
        continue

    try:
        ra_f = float(ra)
        dec_f = float(dec)
    except (TypeError, ValueError):
        continue

    ra_rad = np.radians(ra_f)
    dec_rad = np.radians(dec_f)
    xyz = np.array([
        np.cos(dec_rad) * np.cos(ra_rad),
        np.cos(dec_rad) * np.sin(ra_rad),
        np.sin(dec_rad),
    ])
    dist, idx = tree.query(xyz, k=1)

    if dist < MATCH_TOL_CART:
        label = int(gz1_labels[idx])
        matched_pil_images.append(img.copy())  # store PIL image
        matched_labels_list.append(label)
        matched_metadata.append({
            'ra': ra_f, 'dec': dec_f,
            'gz1_idx': int(idx),
            'p_cw': float(gz1_p_cw[idx]),
            'p_acw': float(gz1_p_acw[idx]),
            'label': label,
            'sep_arcsec': float(dist * 206265),
        })
        matched_gz1_set.add(int(idx))

    if n_scanned % 50000 == 0:
        elapsed = time.time() - t0
        rate = n_scanned / elapsed
        n_m = len(matched_pil_images)
        print(f"    {n_scanned:>7,} scanned | {n_m:>5,} matched | unique GZ1 {len(matched_gz1_set):>5,}/{len(gz1_labels)} | {rate:.0f}/s")

elapsed = time.time() - t0
n_matched = len(matched_pil_images)
print(f"\n  Scan complete: {n_matched} matches from {n_scanned:,} ({elapsed/60:.1f} min)")
print(f"  Unique GZ1 galaxies matched: {len(matched_gz1_set)}/{len(gz1_labels)}")

# Save metadata
pd.DataFrame(matched_metadata).to_csv(f"{OUTPUT_DIR}/crossmatch_metadata.csv", index=False)

# ============================================================
# Step 3: Prepare Training Data
# ============================================================
print(f"\n[Step 3] Preparing training data ({n_matched} galaxies)...")

labels_arr = np.array(matched_labels_list)
n_cw = (labels_arr == 0).sum()
n_ccw = (labels_arr == 1).sum()
print(f"  CW: {n_cw}, CCW: {n_ccw}")

# Split: 80% train, 20% val
indices = np.arange(n_matched)
np.random.seed(42)
np.random.shuffle(indices)
n_val = max(n_matched // 5, 200)
val_indices = indices[:n_val]
train_indices = indices[n_val:]

print(f"  Train: {len(train_indices)}, Val: {len(val_indices)}")

# Custom dataset with chirality-aware flip augmentation
# For each image, 50% chance to horizontally flip it AND swap the label (CW↔CCW)
# This explicitly teaches the model that flipping changes chirality
class GalaxyChiralityDataset(Dataset):
    def __init__(self, pil_images, labels, transform, flip_augment=False):
        self.images = pil_images
        self.labels = labels
        self.transform = transform
        self.flip_augment = flip_augment

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img = self.images[idx]
        label = self.labels[idx]

        # Chirality-aware flip: flip image AND swap label
        if self.flip_augment and np.random.random() > 0.5:
            from PIL import Image
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            label = 1 - label  # CW(0)↔CCW(1)

        img_t = self.transform(img)
        return img_t, label

train_imgs = [matched_pil_images[i] for i in train_indices]
train_lbls = [matched_labels_list[i] for i in train_indices]
val_imgs = [matched_pil_images[i] for i in val_indices]
val_lbls = [matched_labels_list[i] for i in val_indices]

# Train WITH flip augmentation (label-corrected), val WITHOUT
train_dataset = GalaxyChiralityDataset(train_imgs, train_lbls, train_transform, flip_augment=True)
val_dataset = GalaxyChiralityDataset(val_imgs, val_lbls, val_transform, flip_augment=False)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True, num_workers=4, pin_memory=True)
val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False, num_workers=2, pin_memory=True)

# ============================================================
# Step 4: Build and Train Model (End-to-End)
# ============================================================
print(f"\n[Step 4] Building and training end-to-end model...")

# Load ViT-Small encoder
encoder = timm.create_model('vit_small_patch16_224', pretrained=True, num_classes=0)
embed_dim = 384

# Chirality classification head
class ChiralityHead(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.head = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, 512),
            nn.GELU(),
            nn.Dropout(0.3),
            nn.Linear(512, 128),
            nn.GELU(),
            nn.Dropout(0.2),
            nn.Linear(128, 2),
        )
    def forward(self, x):
        return self.head(x)

chirality_head = ChiralityHead(embed_dim)

# Unfreeze last 4 encoder blocks for end-to-end training
for param in encoder.parameters():
    param.requires_grad = False
for block in encoder.blocks[-4:]:
    for param in block.parameters():
        param.requires_grad = True
for param in encoder.norm.parameters():
    param.requires_grad = True

class ChiralityModel(nn.Module):
    def __init__(self, enc, head):
        super().__init__()
        self.enc = enc
        self.head = head
    def forward(self, x):
        return self.head(self.enc(x))

model = ChiralityModel(encoder, chirality_head).to(DEVICE)

n_trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
n_total = sum(p.numel() for p in model.parameters())
print(f"  Parameters: {n_trainable:,} trainable / {n_total:,} total")

# Optimizer with differential learning rates
optimizer = torch.optim.AdamW([
    {'params': chirality_head.parameters(), 'lr': 3e-4},
    {'params': [p for p in encoder.parameters() if p.requires_grad], 'lr': 3e-5},
], weight_decay=0.01)

scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer, T_0=10, T_mult=2)
criterion = nn.CrossEntropyLoss()

# Training loop
best_val_acc = 0
best_epoch = 0
patience = 15
patience_counter = 0

print("  Training (up to 60 epochs)...")
for epoch in range(60):
    model.train()
    train_loss = 0
    train_correct = 0
    train_total = 0

    for batch_imgs, batch_lbls in train_loader:
        batch_imgs = batch_imgs.to(DEVICE)
        batch_lbls = torch.tensor(batch_lbls, dtype=torch.long).to(DEVICE)

        logits = model(batch_imgs)
        loss = criterion(logits, batch_lbls)

        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

        train_loss += loss.item() * len(batch_imgs)
        train_correct += (logits.argmax(1) == batch_lbls).sum().item()
        train_total += len(batch_imgs)

    scheduler.step()

    # Validate
    model.eval()
    val_correct = 0
    val_total = 0
    with torch.no_grad():
        for batch_imgs, batch_lbls in val_loader:
            batch_imgs = batch_imgs.to(DEVICE)
            batch_lbls = torch.tensor(batch_lbls, dtype=torch.long).to(DEVICE)
            logits = model(batch_imgs)
            val_correct += (logits.argmax(1) == batch_lbls).sum().item()
            val_total += len(batch_imgs)

    train_acc = train_correct / train_total
    val_acc = val_correct / val_total
    avg_loss = train_loss / train_total

    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_epoch = epoch + 1
        torch.save({
            'encoder_state': encoder.state_dict(),
            'head_state': chirality_head.state_dict(),
            'val_acc': val_acc,
            'epoch': epoch + 1,
        }, f"{OUTPUT_DIR}/chirality_model_best.pt")
        patience_counter = 0
    else:
        patience_counter += 1

    if (epoch + 1) % 5 == 0 or patience_counter == 0:
        print(f"    Epoch {epoch+1:>3d}: loss={avg_loss:.4f} train_acc={train_acc:.3f} val_acc={val_acc:.3f} best={best_val_acc:.3f} (ep{best_epoch})")

    if patience_counter >= patience:
        print(f"    Early stopping at epoch {epoch+1}")
        break

print(f"\n  BEST: val_acc={best_val_acc:.4f} at epoch {best_epoch}")

# Load best checkpoint
ckpt = torch.load(f"{OUTPUT_DIR}/chirality_model_best.pt", weights_only=True)
encoder.load_state_dict(ckpt['encoder_state'])
chirality_head.load_state_dict(ckpt['head_state'])
model.eval()

# ============================================================
# Step 5: Exhaustive Bias Audits
# ============================================================
print(f"\n[Step 5] Exhaustive bias audits...")

# Audit 1: Mirror test — flip image, CW↔CCW should swap
print("  Audit 1: Mirror test (horizontal flip)")
n_flip = 0
n_same = 0
n_audit = min(2000, len(val_imgs))

with torch.no_grad():
    for i in range(0, n_audit, 64):
        batch_pil = val_imgs[i:i+64]
        # Original
        batch_orig = torch.stack([val_transform(img) for img in batch_pil]).to(DEVICE)
        pred_orig = model(batch_orig).argmax(1)
        # Horizontally flipped
        from PIL import Image
        batch_flip = torch.stack([val_transform(img.transpose(Image.FLIP_LEFT_RIGHT)) for img in batch_pil]).to(DEVICE)
        pred_flip = model(batch_flip).argmax(1)

        for po, pf in zip(pred_orig, pred_flip):
            if po.item() != pf.item():
                n_flip += 1
            else:
                n_same += 1

mirror_rate = n_flip / (n_flip + n_same)
print(f"    Flip rate: {mirror_rate:.1%} (target: >80%)")
print(f"    {'PASS' if mirror_rate > 0.80 else 'FAIL'}")

# Audit 2: Null test — CW fraction on unflipped galaxies
print("\n  Audit 2: Null test (CW/CCW balance)")
n_cw_pred = 0
n_total_pred = 0
with torch.no_grad():
    for i in range(0, n_audit, 64):
        batch_pil = val_imgs[i:i+64]
        batch_t = torch.stack([val_transform(img) for img in batch_pil]).to(DEVICE)
        preds = model(batch_t).argmax(1)
        n_cw_pred += (preds == 0).sum().item()
        n_total_pred += len(preds)

cw_frac = n_cw_pred / n_total_pred
print(f"    CW fraction: {cw_frac:.3f} (target: 0.50 ± 0.05)")
print(f"    {'PASS' if abs(cw_frac - 0.5) < 0.05 else 'FAIL'}")

# Audit 3: Confidence distribution
print("\n  Audit 3: Confidence distribution")
all_confs = []
with torch.no_grad():
    for i in range(0, n_audit, 64):
        batch_pil = val_imgs[i:i+64]
        batch_t = torch.stack([val_transform(img) for img in batch_pil]).to(DEVICE)
        probs = torch.softmax(model(batch_t), dim=1).cpu().numpy()
        all_confs.extend(np.max(probs, axis=1).tolist())

all_confs = np.array(all_confs)
print(f"    Mean confidence: {all_confs.mean():.3f}")
print(f"    Std confidence: {all_confs.std():.3f}")
print(f"    >0.7: {(all_confs > 0.7).sum()} ({(all_confs > 0.7).mean():.1%})")
print(f"    >0.9: {(all_confs > 0.9).sum()} ({(all_confs > 0.9).mean():.1%})")

# Audit 4: Rotation invariance — 90° rotation should NOT change chirality
print("\n  Audit 4: Rotation invariance")
n_rot_consistent = 0
n_rot_total = 0
with torch.no_grad():
    for i in range(0, min(500, n_audit), 32):
        batch_pil = val_imgs[i:i+32]
        batch_orig = torch.stack([val_transform(img) for img in batch_pil]).to(DEVICE)
        pred_orig = model(batch_orig).argmax(1)
        # 90° rotation (PIL rotate)
        batch_rot = torch.stack([val_transform(img.rotate(90)) for img in batch_pil]).to(DEVICE)
        pred_rot = model(batch_rot).argmax(1)
        n_rot_consistent += (pred_orig == pred_rot).sum().item()
        n_rot_total += len(pred_orig)

rot_consistency = n_rot_consistent / n_rot_total
print(f"    90° rotation consistency: {rot_consistency:.1%} (target: >80%)")
print(f"    {'PASS' if rot_consistency > 0.80 else 'FAIL'}")

# Audit 5: Check against GZ1 label accuracy
print("\n  Audit 5: Agreement with GZ1 crowd labels")
correct_vs_gz1 = 0
total_vs_gz1 = 0
with torch.no_grad():
    for i in range(0, n_audit, 64):
        batch_pil = val_imgs[i:i+64]
        batch_t = torch.stack([val_transform(img) for img in batch_pil]).to(DEVICE)
        preds = model(batch_t).argmax(1).cpu().numpy()
        true_lbls = val_lbls[i:i+64]
        for p, t in zip(preds, true_lbls):
            correct_vs_gz1 += (p == t)
            total_vs_gz1 += 1

gz1_agreement = correct_vs_gz1 / total_vs_gz1
print(f"    Agreement with GZ1 labels: {gz1_agreement:.1%}")

# Summary
audit_results = {
    'mirror_flip_rate': float(mirror_rate),
    'mirror_pass': bool(mirror_rate > 0.80),
    'cw_fraction': float(cw_frac),
    'null_pass': bool(abs(cw_frac - 0.5) < 0.05),
    'confidence_mean': float(all_confs.mean()),
    'confidence_std': float(all_confs.std()),
    'rotation_consistency': float(rot_consistency),
    'gz1_agreement': float(gz1_agreement),
    'val_accuracy': float(best_val_acc),
    'best_epoch': int(best_epoch),
    'n_training': int(len(train_indices)),
    'n_validation': int(len(val_indices)),
}

all_pass = mirror_rate > 0.80 and abs(cw_frac - 0.5) < 0.05 and rot_consistency > 0.80
audit_results['all_pass'] = bool(all_pass)

with open(f"{OUTPUT_DIR}/audit_results.json", 'w') as f:
    json.dump(audit_results, f, indent=2)

print(f"\n{'='*70}")
print(f"TRAINING COMPLETE")
print(f"{'='*70}")
print(f"  Val accuracy: {best_val_acc:.3f}")
print(f"  Mirror test: {mirror_rate:.1%} {'PASS' if mirror_rate > 0.80 else 'FAIL'}")
print(f"  Null test: CW={cw_frac:.3f} {'PASS' if abs(cw_frac - 0.5) < 0.05 else 'FAIL'}")
print(f"  Rotation: {rot_consistency:.1%} {'PASS' if rot_consistency > 0.80 else 'FAIL'}")
print(f"  GZ1 agreement: {gz1_agreement:.1%}")
print(f"  Overall: {'ALL AUDITS PASS — ready for inference' if all_pass else 'NEEDS IMPROVEMENT'}")
print(f"  Model saved: {OUTPUT_DIR}/chirality_model_best.pt")
