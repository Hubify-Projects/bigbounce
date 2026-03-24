#!/usr/bin/env python3
"""
Chirality v2 FAST: Pre-tensored training with flip-equivariance loss.
Reuses cross-match data from train_chirality_v2.py but with GPU-native training.

Key improvements over v1:
1. 3 classes: CW/CCW/NOT_SPIRAL
2. Flip-equivariance consistency loss
3. Chirality-aware flip augmentation (on tensor, fast)
4. All training data pre-transformed to tensors
"""

import os, sys, time, json
import numpy as np
import torch
import torch.nn as nn
import timm
from torchvision import transforms
from PIL import Image, ImageEnhance
from datasets import load_dataset
import pandas as pd
import urllib.request, gzip, io

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"

print("=" * 70, flush=True)
print("CHIRALITY v2 FAST TRAINING", flush=True)
print("=" * 70, flush=True)

# ---- Step 1: Collect training images (reuse cross-match logic) ----
print("\n[1] Collecting training data...", flush=True)

# Load GZ1
gz1_file = "/workspace/gz1_table2.csv.gz"
if not os.path.exists(gz1_file):
    req = urllib.request.Request("https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.gz")
    req.add_header("User-Agent", "Mozilla/5.0")
    with open(gz1_file, 'wb') as f:
        f.write(urllib.request.urlopen(req, timeout=120).read())

gz1 = pd.read_csv(gz1_file, compression='gzip')
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy.spatial import cKDTree

cw_g = gz1[gz1['P_CW'] > 0.7].sample(n=min(19613, len(gz1[gz1['P_CW'] > 0.7])), random_state=42)
acw_g = gz1[gz1['P_ACW'] > 0.7].sample(n=min(19613, len(gz1[gz1['P_ACW'] > 0.7])), random_state=42)
labeled = pd.concat([
    cw_g[['RA','DEC']].assign(label=0),
    acw_g[['RA','DEC']].assign(label=1),
], ignore_index=True)
coords = SkyCoord(ra=labeled['RA'].values, dec=labeled['DEC'].values, unit=(u.hourangle, u.deg))
gz1_ra = coords.ra.deg.astype(np.float64)
gz1_dec = coords.dec.deg.astype(np.float64)
gz1_labels = labeled['label'].values.astype(np.int64)
gz1_xyz = np.column_stack([np.cos(np.radians(gz1_dec))*np.cos(np.radians(gz1_ra)),
                           np.cos(np.radians(gz1_dec))*np.sin(np.radians(gz1_ra)),
                           np.sin(np.radians(gz1_dec))])
tree_gz1 = cKDTree(gz1_xyz)
MATCH_TOL = 2 * np.sin(3.0/206265.0/2)
print(f"  GZ1 KD-tree: {len(gz1_xyz)} galaxies", flush=True)

# Load CE-ResNet
from astropy.io import fits
ce_data = fits.open("/workspace/external_catalogs/pre_desi.fits")[1].data
ce_pcw, ce_pacw = ce_data['P_CW'], ce_data['P_ACW']
# Not-spiral: very low chirality
ns_mask = (ce_pcw + ce_pacw) < 0.02
ns_ra = ce_data['RA'][ns_mask].astype(np.float64)
ns_dec = ce_data['DEC'][ns_mask].astype(np.float64)
ns_xyz = np.column_stack([np.cos(np.radians(ns_dec))*np.cos(np.radians(ns_ra)),
                          np.cos(np.radians(ns_dec))*np.sin(np.radians(ns_ra)),
                          np.sin(np.radians(ns_dec))])
ns_idx = np.random.choice(len(ns_xyz), min(50000, len(ns_xyz)), replace=False)
tree_ns = cKDTree(ns_xyz[ns_idx])
# Confident spirals
conf_mask = (ce_pcw > 0.4) | (ce_pacw > 0.4)
conf_ra = ce_data['RA'][conf_mask].astype(np.float64)
conf_dec = ce_data['DEC'][conf_mask].astype(np.float64)
conf_labels = (ce_pacw[conf_mask] > ce_pcw[conf_mask]).astype(np.int64)
conf_xyz = np.column_stack([np.cos(np.radians(conf_dec))*np.cos(np.radians(conf_ra)),
                            np.cos(np.radians(conf_dec))*np.sin(np.radians(conf_ra)),
                            np.sin(np.radians(conf_dec))])
tree_ce = cKDTree(conf_xyz)
print(f"  CE-ResNet: {np.sum(ns_mask):,} not-spiral, {np.sum(conf_mask):,} confident spirals", flush=True)

# Scan GZ DESI
print("  Scanning GZ DESI (150K)...", flush=True)
tfm = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor(),
                           transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])])

ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)
imgs, lbls = [], []
n_gz1, n_ce, n_ns, n_scanned = 0, 0, 0, 0
t0 = time.time()

for row in ds:
    n_scanned += 1
    if n_scanned > 150000: break
    ra, dec, img = row.get('ra'), row.get('dec'), row.get('image')
    if ra is None or dec is None or img is None: continue
    try: ra_f, dec_f = float(ra), float(dec)
    except: continue

    xyz = np.array([np.cos(np.radians(dec_f))*np.cos(np.radians(ra_f)),
                    np.cos(np.radians(dec_f))*np.sin(np.radians(ra_f)),
                    np.sin(np.radians(dec_f))])

    d1, i1 = tree_gz1.query(xyz)
    if d1 < MATCH_TOL:
        imgs.append(tfm(img)); lbls.append(int(gz1_labels[i1])); n_gz1 += 1; continue

    if n_ce < 20000:
        d2, i2 = tree_ce.query(xyz)
        if d2 < MATCH_TOL:
            imgs.append(tfm(img)); lbls.append(int(conf_labels[i2])); n_ce += 1; continue

    if n_ns < 8000:
        d3, i3 = tree_ns.query(xyz)
        if d3 < MATCH_TOL:
            imgs.append(tfm(img)); lbls.append(2); n_ns += 1; continue

    if n_scanned % 50000 == 0:
        print(f"    {n_scanned:,} | gz1={n_gz1} ce={n_ce} ns={n_ns} | {n_scanned/(time.time()-t0):.0f}/s", flush=True)

# Add synthetic not-spiral
for _ in range(2000):
    arr = np.random.randint(0, 50, (224, 224, 3), dtype=np.uint8)
    t = transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])(
        torch.from_numpy(arr).permute(2,0,1).float()/255)
    imgs.append(t); lbls.append(2)

print(f"\n  Done ({time.time()-t0:.0f}s): gz1={n_gz1} ce={n_ce} ns={n_ns}+2000syn = {len(imgs)} total", flush=True)

# ---- Step 2: Prepare tensors ----
print("\n[2] Preparing training tensors...", flush=True)
X = torch.stack(imgs)
Y = torch.tensor(lbls, dtype=torch.long)
n = len(X)

perm = torch.randperm(n)
n_val = max(n // 5, 500)
X_val, Y_val = X[perm[:n_val]].to(DEVICE), Y[perm[:n_val]].to(DEVICE)
X_train, Y_train = X[perm[n_val:]], Y[perm[n_val:]]

# Val PIL images not needed — audits use tensors directly

lc = np.bincount(Y_train.numpy(), minlength=3)
w = 1.0 / (lc + 1); w = w / w.sum() * 3
print(f"  Train: {len(X_train)} Val: {len(X_val)}", flush=True)
print(f"  CW={lc[0]} CCW={lc[1]} NS={lc[2]} weights={w}", flush=True)

# ---- Step 3: Build model ----
print("\n[3] Building model...", flush=True)
encoder = timm.create_model('vit_small_patch16_224', pretrained=True, num_classes=0).to(DEVICE)

class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(nn.LayerNorm(384), nn.Linear(384,512), nn.GELU(), nn.Dropout(0.3),
                               nn.Linear(512,256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256,3))
    def forward(self, x): return self.h(x)

head = Head().to(DEVICE)

for p in encoder.parameters(): p.requires_grad = False
for blk in encoder.blocks[-6:]:
    for p in blk.parameters(): p.requires_grad = True
for p in encoder.norm.parameters(): p.requires_grad = True

def model_fwd(x): return head(encoder(x))

nt = sum(p.numel() for p in list(encoder.parameters())+list(head.parameters()) if p.requires_grad)
print(f"  Trainable: {nt:,}", flush=True)

# ---- Step 4: Train ----
print("\n[4] Training with flip-equivariance loss...", flush=True)

criterion = nn.CrossEntropyLoss(weight=torch.FloatTensor(w).to(DEVICE))
flip_perm = torch.tensor([1,0,2], dtype=torch.long)  # CW↔CCW swap
FLIP_W = 0.5
BS = 128

opt = torch.optim.AdamW([
    {'params': head.parameters(), 'lr': 3e-4},
    {'params': [p for p in encoder.parameters() if p.requires_grad], 'lr': 2e-5},
], weight_decay=0.02)
sched = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(opt, T_0=10, T_mult=2)

best_va = 0; best_ep = 0; pat = 0

for ep in range(80):
    encoder.train(); head.train()
    shuf = torch.randperm(len(X_train))
    tot_cls, tot_flip, tot_c, tot_n = 0, 0, 0, 0

    for s in range(0, len(X_train), BS):
        idx = shuf[s:s+BS]
        xb = X_train[idx].to(DEVICE)
        yb = Y_train[idx].to(DEVICE)

        # Classification loss
        logits = model_fwd(xb)
        cls_loss = criterion(logits, yb)

        # Flip-equivariance loss
        xf = torch.flip(xb, [3])  # horizontal flip
        logits_f = model_fwd(xf)
        probs = torch.softmax(logits, dim=1)
        probs_f = torch.softmax(logits_f, dim=1)
        expected = probs[:, flip_perm]
        flip_loss = nn.functional.mse_loss(probs_f, expected)

        loss = cls_loss + FLIP_W * flip_loss

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(list(encoder.parameters())+list(head.parameters()), 1.0)
        opt.step()

        tot_cls += cls_loss.item() * len(xb)
        tot_flip += flip_loss.item() * len(xb)
        tot_c += (logits.argmax(1) == yb).sum().item()
        tot_n += len(xb)

    sched.step()

    # Validate
    encoder.eval(); head.eval()
    with torch.no_grad():
        vl = model_fwd(X_val)
        va = (vl.argmax(1) == Y_val).float().mean().item()
        # Per-class
        pc = {}
        for c, nm in enumerate(['CW','CCW','NS']):
            m = Y_val == c
            if m.sum() > 0:
                pc[nm] = (vl.argmax(1)[m] == c).float().mean().item()
            else:
                pc[nm] = 0

    if va > best_va:
        best_va = va; best_ep = ep+1; pat = 0
        torch.save({'enc': encoder.state_dict(), 'head': head.state_dict(),
                     'val_acc': va, 'epoch': ep+1, 'n_classes': 3},
                   f"{OUTPUT_DIR}/chirality_model_v2_best.pt")
    else:
        pat += 1

    if (ep+1) % 3 == 0 or pat == 0:
        print(f"  Ep{ep+1:>3d}: cls={tot_cls/tot_n:.4f} flip={tot_flip/tot_n:.5f} train={tot_c/tot_n:.3f} val={va:.3f} best={best_va:.3f} {pc}", flush=True)

    if pat >= 15: print(f"  Early stop ep{ep+1}", flush=True); break

print(f"\n  BEST: val={best_va:.4f} at ep{best_ep}", flush=True)

# Load best
ckpt = torch.load(f"{OUTPUT_DIR}/chirality_model_v2_best.pt", weights_only=True)
encoder.load_state_dict(ckpt['enc']); head.load_state_dict(ckpt['head'])
encoder.eval(); head.eval()

# ---- Step 5: Bias hardening audit ----
print("\n[5] Bias hardening audit...", flush=True)

def pred_tensors(t):
    with torch.no_grad():
        return torch.softmax(model_fwd(t.to(DEVICE)), dim=1).cpu().numpy()

# T1: Flip-swap
p_o = pred_tensors(X_val[:500])
p_f = pred_tensors(torch.flip(X_val[:500], [3]))
swap_err = np.mean(np.abs(p_o[:,0] - p_f[:,1]))
swap_corr = np.corrcoef(p_o[:,0], p_f[:,1])[0,1]
print(f"  Flip-swap: err={swap_err:.4f} corr={swap_corr:.4f} ({'PASS' if swap_corr>0.8 else 'FAIL'})", flush=True)

# T2: Rotation
from torchvision.transforms.functional import rotate as tv_rotate
rot_agrs = []
for ang in [15, 45, 90, 135, 180, 270]:
    p_r = pred_tensors(tv_rotate(X_val[:300], ang))
    agr = np.mean(p_o[:300].argmax(1) == p_r.argmax(1))
    rot_agrs.append(agr)
avg_rot = np.mean(rot_agrs)
print(f"  Rotation avg: {avg_rot:.3f} ({'PASS' if avg_rot>0.8 else 'FAIL'})", flush=True)

# T3: Artifacts (blank sky)
blank = torch.randn(100, 3, 224, 224) * 0.1
p_blank = pred_tensors(blank)
blank_ns = np.mean(p_blank.argmax(1) == 2)
blank_cw = np.mean(p_blank.argmax(1) == 0)
print(f"  Blank→NS: {blank_ns:.1%} CW: {blank_cw:.1%} ({'PASS' if blank_cw<0.3 else 'FAIL'})", flush=True)

# T4: CW/CCW balance (spiral-only)
p_all = pred_tensors(X_val)
spiral = p_all.argmax(1) != 2
if spiral.sum() > 50:
    cw_f = np.mean(p_all[spiral].argmax(1) == 0)
    print(f"  CW frac (spirals): {cw_f:.3f} ({'PASS' if abs(cw_f-0.5)<0.1 else 'FAIL'})", flush=True)

# T5: Perturbation (brightness)
bright = X_val[:200] * 1.5
bright = torch.clamp(bright, -3, 3)
p_br = pred_tensors(bright)
p_o200 = pred_tensors(X_val[:200])
br_agr = np.mean(p_o200.argmax(1) == p_br.argmax(1))
print(f"  Bright pert: {br_agr:.3f} ({'PASS' if br_agr>0.8 else 'FAIL'})", flush=True)

# Save results
results = {
    'val_accuracy': float(best_va),
    'best_epoch': int(best_ep),
    'flip_swap_corr': float(swap_corr),
    'flip_swap_err': float(swap_err),
    'rotation_avg': float(avg_rot),
    'blank_ns_rate': float(blank_ns),
    'blank_cw_rate': float(blank_cw),
    'cw_frac_spirals': float(cw_f) if spiral.sum() > 50 else None,
    'brightness_agreement': float(br_agr),
    'n_train': int(len(X_train)),
    'n_val': int(len(X_val)),
    'training_data': {'gz1': n_gz1, 'ce_spiral': n_ce, 'not_spiral': n_ns+2000},
}

with open(f"{OUTPUT_DIR}/v2_fast_results.json", 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n{'='*70}", flush=True)
print(f"v2 COMPLETE: val={best_va:.4f} | flip_corr={swap_corr:.3f} | rot={avg_rot:.3f} | blank_ns={blank_ns:.1%}", flush=True)
print(f"{'='*70}", flush=True)
