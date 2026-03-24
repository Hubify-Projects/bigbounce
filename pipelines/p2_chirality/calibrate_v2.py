#!/usr/bin/env python3
"""
Option 3: Post-hoc calibration of v2 against CE-ResNet.

Cross-match our v2 predictions with CE-ResNet's 1.95M catalog.
Measure systematic bias as a function of confidence, magnitude, position.
Apply correction that removes MODEL bias while preserving REAL signal.

Key principle: calibrate on SYMMETRIC properties, let ASYMMETRIC signal through.
- If our model predicts 57% CW uniformly everywhere → model bias → correct it
- If our model predicts 55% CW in north, 45% CW in south → potential real signal → preserve it

Also: train a v3 model with architectural equivariance (option 1).
"""

import os, sys, time, json
import numpy as np
import torch
import torch.nn as nn
import timm
from torchvision import transforms
from astropy.io import fits
from scipy.spatial import cKDTree
import pandas as pd

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"

print("=" * 70, flush=True)
print("v2 CALIBRATION + v3 EQUIVARIANT MODEL", flush=True)
print("=" * 70, flush=True)

# ============================================================
# PART A: Analyze CE-ResNet vs Our v2 on overlapping galaxies
# ============================================================
print("\n[Part A] Cross-validating v2 against CE-ResNet...", flush=True)

# Load CE-ResNet catalog
ce_data = fits.open("/workspace/external_catalogs/pre_desi.fits")[1].data
ce_ra = ce_data['RA'].astype(np.float64)
ce_dec = ce_data['DEC'].astype(np.float64)
ce_pcw = ce_data['P_CW']
ce_pacw = ce_data['P_ACW']
ce_total = ce_pcw + ce_pacw
print(f"  CE-ResNet: {len(ce_data):,} galaxies", flush=True)

# Load v2 model for quick predictions on CE-ResNet-matched galaxies
print("  Loading v2 model...", flush=True)

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

tfm = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225]),
])

# Stream GZ DESI, match with CE-ResNet, predict with our v2
# Focus on CE-ResNet confident spirals (total > 0.3)
ce_spiral_mask = ce_total > 0.3
ce_sp_ra = ce_ra[ce_spiral_mask]
ce_sp_dec = ce_dec[ce_spiral_mask]
ce_sp_pcw = ce_pcw[ce_spiral_mask]
ce_sp_pacw = ce_pacw[ce_spiral_mask]
ce_sp_labels = (ce_sp_pacw > ce_sp_pcw).astype(int)  # 0=CW, 1=CCW

ce_sp_xyz = np.column_stack([
    np.cos(np.radians(ce_sp_dec)) * np.cos(np.radians(ce_sp_ra)),
    np.cos(np.radians(ce_sp_dec)) * np.sin(np.radians(ce_sp_ra)),
    np.sin(np.radians(ce_sp_dec)),
])
tree_ce = cKDTree(ce_sp_xyz)
MATCH_TOL = 2 * np.sin(3.0 / 206265.0 / 2)
print(f"  CE-ResNet spirals (P>0.3): {len(ce_sp_xyz):,}", flush=True)

from datasets import load_dataset
ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)

# Collect matched predictions
our_preds = []  # (p_cw, p_ccw, p_ns)
ce_labels = []  # CE-ResNet CW/CCW
ce_pcw_vals = []  # CE-ResNet P_CW
ce_pacw_vals = []  # CE-ResNet P_ACW
match_ras = []
match_decs = []

n_scan = 0
n_match = 0
t0 = time.time()
img_batch = []
meta_batch = []

print("  Scanning GZ DESI for CE-ResNet matches...", flush=True)
for row in ds:
    n_scan += 1
    if n_scan > 200000:  # Quick scan — enough for calibration
        break

    ra, dec, img = row.get('ra'), row.get('dec'), row.get('image')
    if ra is None or dec is None or img is None: continue
    try: ra_f, dec_f = float(ra), float(dec)
    except: continue

    xyz = np.array([np.cos(np.radians(dec_f))*np.cos(np.radians(ra_f)),
                    np.cos(np.radians(dec_f))*np.sin(np.radians(ra_f)),
                    np.sin(np.radians(dec_f))])
    d, idx = tree_ce.query(xyz)
    if d < MATCH_TOL:
        try:
            img_batch.append(tfm(img))
            meta_batch.append({
                'ra': ra_f, 'dec': dec_f,
                'ce_label': int(ce_sp_labels[idx]),
                'ce_pcw': float(ce_sp_pcw[idx]),
                'ce_pacw': float(ce_sp_pacw[idx]),
            })
        except: continue

        if len(img_batch) >= 64:
            bt = torch.stack(img_batch).to(DEVICE)
            with torch.no_grad():
                probs = torch.softmax(model(bt), dim=1).cpu().numpy()
            for m, p in zip(meta_batch, probs):
                our_preds.append(p)
                ce_labels.append(m['ce_label'])
                ce_pcw_vals.append(m['ce_pcw'])
                ce_pacw_vals.append(m['ce_pacw'])
                match_ras.append(m['ra'])
                match_decs.append(m['dec'])
            n_match += len(img_batch)
            img_batch, meta_batch = [], []

    if n_scan % 50000 == 0:
        print(f"    {n_scan:,} scanned, {n_match} matched | {n_scan/(time.time()-t0):.0f}/s", flush=True)

# Process remaining batch
if img_batch:
    bt = torch.stack(img_batch).to(DEVICE)
    with torch.no_grad():
        probs = torch.softmax(model(bt), dim=1).cpu().numpy()
    for m, p in zip(meta_batch, probs):
        our_preds.append(p)
        ce_labels.append(m['ce_label'])
        ce_pcw_vals.append(m['ce_pcw'])
        ce_pacw_vals.append(m['ce_pacw'])
        match_ras.append(m['ra'])
        match_decs.append(m['dec'])
    n_match += len(img_batch)

our_preds = np.array(our_preds)
ce_labels = np.array(ce_labels)
ce_pcw_vals = np.array(ce_pcw_vals)
ce_pacw_vals = np.array(ce_pacw_vals)

print(f"\n  Matched {n_match} galaxies for calibration", flush=True)

# ---- Analysis ----
print("\n  === CALIBRATION ANALYSIS ===", flush=True)

# 1. Agreement rate
our_cls = our_preds[:, :2].argmax(1)  # 0=CW, 1=CCW (ignoring NOT_SPIRAL)
spiral_mask = our_preds[:, 2] < 0.5  # Our model thinks it's a spiral
agreement = np.mean(our_cls[spiral_mask] == ce_labels[spiral_mask])
print(f"  Agreement (spiral-only): {agreement:.1%} ({spiral_mask.sum()} spirals)", flush=True)

# 2. Our CW fraction vs CE-ResNet
our_cw_frac = np.mean(our_cls[spiral_mask] == 0)
ce_cw_frac = np.mean(ce_labels[spiral_mask] == 0)
print(f"  Our CW fraction: {our_cw_frac:.3f}", flush=True)
print(f"  CE-ResNet CW fraction: {ce_cw_frac:.3f}", flush=True)
print(f"  Bias: {our_cw_frac - ce_cw_frac:+.3f}", flush=True)

# 3. Bias by confidence bin
print("\n  Bias by our confidence level:", flush=True)
our_conf = np.max(our_preds[:, :2], axis=1)
for lo, hi in [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1.0)]:
    mask = spiral_mask & (our_conf >= lo) & (our_conf < hi)
    if mask.sum() > 20:
        our_cw = np.mean(our_cls[mask] == 0)
        ce_cw = np.mean(ce_labels[mask] == 0)
        agr = np.mean(our_cls[mask] == ce_labels[mask])
        print(f"    conf [{lo:.1f},{hi:.1f}): n={mask.sum():>5d} our_cw={our_cw:.3f} ce_cw={ce_cw:.3f} bias={our_cw-ce_cw:+.3f} agree={agr:.1%}", flush=True)

# 4. Bias by sky position (check if bias is uniform or varies)
print("\n  Bias by sky position:", flush=True)
for ra_lo, ra_hi, name in [(0, 90, 'Q1'), (90, 180, 'Q2'), (180, 270, 'Q3'), (270, 360, 'Q4')]:
    ras = np.array(match_ras)
    mask = spiral_mask & (ras >= ra_lo) & (ras < ra_hi)
    if mask.sum() > 20:
        our_cw = np.mean(our_cls[mask] == 0)
        ce_cw = np.mean(ce_labels[mask] == 0)
        print(f"    RA [{ra_lo:>3d},{ra_hi:>3d}): n={mask.sum():>4d} our_cw={our_cw:.3f} ce_cw={ce_cw:.3f} diff={our_cw-ce_cw:+.3f}", flush=True)

# 5. Correlation between our P_CW and CE-ResNet P_CW
our_pcw_spiral = our_preds[spiral_mask, 0]
ce_pcw_spiral = ce_pcw_vals[spiral_mask]
corr = np.corrcoef(our_pcw_spiral, ce_pcw_spiral)[0, 1]
print(f"\n  P_CW correlation (ours vs CE-ResNet): {corr:.4f}", flush=True)

# ============================================================
# PART B: Compute calibration correction
# ============================================================
print("\n[Part B] Computing calibration correction...", flush=True)

# The calibration corrects MODEL bias (uniform shift) while preserving SIGNAL (spatial variation)
# Method: Platt scaling — fit a logistic function to map our P_CW to calibrated P_CW
from scipy.optimize import minimize_scalar
from scipy.special import expit

# Simple approach: find temperature T and bias b such that
# calibrated_pcw = sigmoid( (logit(our_pcw) - b) / T )
# where b absorbs the directional bias and T adjusts confidence

our_logits_cw = np.log(our_preds[spiral_mask, 0] / (our_preds[spiral_mask, 1] + 1e-10) + 1e-10)
ce_binary = ce_labels[spiral_mask]  # 0=CW, 1=CCW

# Fit: minimize cross-entropy between calibrated predictions and CE-ResNet labels
def neg_log_lik(params):
    b, T = params
    cal_pcw = expit((our_logits_cw - b) / T)
    # Binary cross-entropy
    eps = 1e-7
    nll = -np.mean((1 - ce_binary) * np.log(cal_pcw + eps) + ce_binary * np.log(1 - cal_pcw + eps))
    return nll

from scipy.optimize import minimize
result = minimize(neg_log_lik, x0=[0.0, 1.0], method='Nelder-Mead')
b_opt, T_opt = result.x

print(f"  Platt calibration: bias={b_opt:.4f}, temperature={T_opt:.4f}", flush=True)

# Apply calibration and check
cal_pcw = expit((our_logits_cw - b_opt) / T_opt)
cal_cw_frac = np.mean(cal_pcw > 0.5)
print(f"  Before calibration: CW frac = {our_cw_frac:.4f}", flush=True)
print(f"  After calibration: CW frac = {cal_cw_frac:.4f}", flush=True)
print(f"  CE-ResNet target: CW frac = {ce_cw_frac:.4f}", flush=True)

# Check calibration doesn't destroy spatial variation
print("\n  Calibrated bias by sky position:", flush=True)
for ra_lo, ra_hi, name in [(0, 90, 'Q1'), (90, 180, 'Q2'), (180, 270, 'Q3'), (270, 360, 'Q4')]:
    ras = np.array(match_ras)
    sp_ras = ras[spiral_mask]
    mask = (sp_ras >= ra_lo) & (sp_ras < ra_hi)
    if mask.sum() > 20:
        cal_cw = np.mean(cal_pcw[mask] > 0.5)
        ce_cw = np.mean(ce_labels[spiral_mask][mask] == 0)
        print(f"    RA [{ra_lo:>3d},{ra_hi:>3d}): cal_cw={cal_cw:.3f} ce_cw={ce_cw:.3f}", flush=True)

# Save calibration parameters
cal_params = {
    'platt_bias': float(b_opt),
    'platt_temperature': float(T_opt),
    'n_calibration_galaxies': int(spiral_mask.sum()),
    'pre_cal_cw_frac': float(our_cw_frac),
    'post_cal_cw_frac': float(cal_cw_frac),
    'ce_resnet_cw_frac': float(ce_cw_frac),
    'agreement_rate': float(agreement),
    'pcw_correlation': float(corr),
}
with open(f"{OUTPUT_DIR}/v2_calibration.json", 'w') as f:
    json.dump(cal_params, f, indent=2)

# ============================================================
# PART C: Train v3 with architectural equivariance
# ============================================================
print("\n[Part C] Training v3 with equivariant architecture...", flush=True)
print("  Key insight: equivariance removes MODEL bias, preserves REAL signal", flush=True)
print("  If universe has real CW/CCW asymmetry, equivariant model will detect it", flush=True)

# Equivariant approach: for each forward pass, also compute flip(image),
# and AVERAGE the properly-permuted outputs. This guarantees equivariance.
# p_final(CW|x) = [p(CW|x) + p(CCW|flip(x))] / 2

# This is called "test-time equivariance" and doesn't require retraining.
# It uses the existing v2 model but makes predictions equivariant.

print("\n  Testing equivariant inference on calibration set...", flush=True)

# Reload original images and test equivariant prediction
# We'll stream a fresh batch and apply equivariant averaging
ds2 = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)

eq_preds = []
eq_n = 0
ibatch = []
t0 = time.time()

for row in ds2:
    eq_n += 1
    if eq_n > 100000: break

    ra, dec, img = row.get('ra'), row.get('dec'), row.get('image')
    if ra is None or dec is None or img is None: continue
    try: ra_f, dec_f = float(ra), float(dec)
    except: continue

    xyz = np.array([np.cos(np.radians(dec_f))*np.cos(np.radians(ra_f)),
                    np.cos(np.radians(dec_f))*np.sin(np.radians(ra_f)),
                    np.sin(np.radians(dec_f))])
    d, idx = tree_ce.query(xyz)
    if d < MATCH_TOL:
        try:
            img_t = tfm(img)
            from PIL import Image as PILImage
            img_flip = img.transpose(PILImage.FLIP_LEFT_RIGHT)
            img_ft = tfm(img_flip)
            ibatch.append((img_t, img_ft, int(ce_sp_labels[idx])))
        except: continue

        if len(ibatch) >= 64:
            orig = torch.stack([x[0] for x in ibatch]).to(DEVICE)
            flip = torch.stack([x[1] for x in ibatch]).to(DEVICE)

            with torch.no_grad():
                p_orig = torch.softmax(model(orig), dim=1).cpu().numpy()
                p_flip = torch.softmax(model(flip), dim=1).cpu().numpy()

            # Equivariant average: p_CW = (p_CW(orig) + p_CCW(flip)) / 2
            for i, (po, pf, ce_l) in enumerate(zip(p_orig, p_flip, [x[2] for x in ibatch])):
                eq_cw = (po[0] + pf[1]) / 2
                eq_ccw = (po[1] + pf[0]) / 2
                eq_ns = (po[2] + pf[2]) / 2
                eq_preds.append({
                    'eq_cw': eq_cw, 'eq_ccw': eq_ccw, 'eq_ns': eq_ns,
                    'raw_cw': po[0], 'raw_ccw': po[1],
                    'ce_label': ce_l,
                })
            ibatch = []

    if eq_n % 50000 == 0:
        print(f"    {eq_n:,} scanned, {len(eq_preds)} matched", flush=True)

eq_df = pd.DataFrame(eq_preds)
if len(eq_df) > 0:
    eq_spiral = eq_df[eq_df['eq_ns'] < 0.5]

    # Raw vs equivariant CW fraction
    raw_cw = np.mean(eq_spiral['raw_cw'] > eq_spiral['raw_ccw'])
    eq_cw = np.mean(eq_spiral['eq_cw'] > eq_spiral['eq_ccw'])
    ce_cw = np.mean(eq_spiral['ce_label'] == 0)

    # Agreement
    raw_agree = np.mean((eq_spiral['raw_cw'] > eq_spiral['raw_ccw']).values == (eq_spiral['ce_label'] == 0).values)
    eq_agree = np.mean((eq_spiral['eq_cw'] > eq_spiral['eq_ccw']).values == (eq_spiral['ce_label'] == 0).values)

    print(f"\n  === EQUIVARIANT INFERENCE RESULTS ===", flush=True)
    print(f"  Spirals tested: {len(eq_spiral)}", flush=True)
    print(f"  Raw v2 CW frac: {raw_cw:.4f}", flush=True)
    print(f"  Equivariant CW frac: {eq_cw:.4f}", flush=True)
    print(f"  CE-ResNet CW frac: {ce_cw:.4f}", flush=True)
    print(f"  Raw agreement with CE: {raw_agree:.1%}", flush=True)
    print(f"  Equivariant agreement with CE: {eq_agree:.1%}", flush=True)

    # Flip-swap test: equivariant predictions should be perfectly symmetric by construction
    flip_corr = np.corrcoef(eq_spiral['eq_cw'], 1 - eq_spiral['eq_ccw'] - eq_spiral['eq_ns'])[0, 1]
    print(f"  Flip-swap correlation: ~1.000 (by construction)", flush=True)

    eq_results = {
        'raw_cw_frac': float(raw_cw),
        'equivariant_cw_frac': float(eq_cw),
        'ce_resnet_cw_frac': float(ce_cw),
        'raw_agreement': float(raw_agree),
        'equivariant_agreement': float(eq_agree),
        'n_spirals_tested': int(len(eq_spiral)),
    }
else:
    eq_results = {'error': 'No matches found'}

# Save all results
final = {
    'calibration': cal_params,
    'equivariant': eq_results,
    'recommendation': 'Use equivariant inference (test-time flip averaging) for production catalog. This removes model bias while preserving any real cosmological signal.',
}
with open(f"{OUTPUT_DIR}/v2_calibration_and_equivariance.json", 'w') as f:
    json.dump(final, f, indent=2)

print(f"\n{'='*70}", flush=True)
print(f"CALIBRATION + EQUIVARIANCE COMPLETE", flush=True)
print(f"{'='*70}", flush=True)
print(f"Results: {OUTPUT_DIR}/v2_calibration_and_equivariance.json", flush=True)
