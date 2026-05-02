"""
R42 Wave 14-FFF: P4-CM-M1 FULL HARD FIX
Recalibrate Catalog B Platt scaling against independent GZ1 labels.

Finding (Gemini-3.1-Pro P4-CM-M1): Catalog B Platt calibration is circular
because it was fit against CE-ResNet consensus labels, inheriting CE-ResNet's
systematic bias. Independent GZ1 human-vote CW/CCW labels (P_CW, P_ACW) are
already available and provide bias-independent ground truth.

Method:
  1. Load GZ1 table (OBJID, RA, DEC, P_CW, P_ACW, SPIRAL)
  2. Cross-match GZ1 with chirality catalog by position (<= 1 arcsec)
  3. Filter to confident GZ1 CW/CCW spirals (SPIRAL=1, max(P_CW,P_ACW) > 0.6)
  4. Fit new Platt (A, B) via L-BFGS on GZ1 binary CW labels
  5. Apply GZ1-calibrated Platt to full catalog, compute CW fraction
  6. Compare: original CE-ResNet Platt vs GZ1 Platt

Output: pipelines/p2_chirality/r42_results/wave_14_fff_gz1_platt_recal.json
"""
import json
import time
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.spatial import cKDTree

t0 = time.time()

print("=== P4-CM-M1 GZ1 Platt Recalibration (Wave 14-FFF) ===")

# --- 1. Load GZ1 ---
print("Loading GZ1 table...")
gz1 = pd.read_csv('/workspace/gz1_table2.csv.gz', compression='gzip')
print(f"  GZ1 rows: {len(gz1):,}")

# Parse sexagesimal RA/DEC to decimal degrees
def hms_to_deg(s):
    """HH:MM:SS.s -> decimal degrees"""
    s = str(s).strip()
    parts = s.split(':')
    h, m, sc = float(parts[0]), float(parts[1]), float(parts[2])
    return (h + m/60 + sc/3600) * 15.0

def dms_to_deg(s):
    """DD:MM:SS.s -> decimal degrees (handles negative)"""
    s = str(s).strip()
    sign = -1 if s.startswith('-') else 1
    s = s.lstrip('+-')
    parts = s.split(':')
    d, m, sc = float(parts[0]), float(parts[1]), float(parts[2])
    return sign * (d + m/60 + sc/3600)

print("  Parsing GZ1 coordinates...")
gz1['ra_deg'] = gz1['RA'].apply(hms_to_deg)
gz1['dec_deg'] = gz1['DEC'].apply(dms_to_deg)

# Filter to spirals with confident CW or CCW vote
gz1_spiral = gz1[gz1['SPIRAL'] == 1].copy()
gz1_spiral['max_cw_acw'] = gz1_spiral[['P_CW', 'P_ACW']].max(axis=1)
gz1_conf = gz1_spiral[gz1_spiral['max_cw_acw'] > 0.6].copy()
gz1_conf['gz1_label'] = (gz1_conf['P_CW'] > gz1_conf['P_ACW']).astype(int)
print(f"  GZ1 spirals: {len(gz1_spiral):,}")
print(f"  GZ1 confident CW/CCW (threshold 0.6): {len(gz1_conf):,}")
print(f"  GZ1 CW fraction (human votes): {gz1_conf['gz1_label'].mean():.4f}")

# --- 2. Load chirality catalog ---
print("Loading chirality catalog...")
cat = pd.read_parquet('/workspace/r42_b20/chirality_catalog/catalog_production.parquet',
                      columns=['dr8_id', 'ra', 'dec', 'p_cw_raw_x', 'p_ccw_raw_x',
                               'p_ns_raw_x', 'class_eq', 'confidence_eq',
                               'p_cw_eq', 'p_ccw_eq'])
print(f"  Catalog rows: {len(cat):,}")

# --- 3. Cross-match by position ---
print("Cross-matching GZ1 x chirality catalog by position...")
# Convert to 3D unit vectors for KDTree matching
def radec_to_xyz(ra_deg, dec_deg):
    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    x = np.cos(dec) * np.cos(ra)
    y = np.cos(dec) * np.sin(ra)
    z = np.sin(dec)
    return np.stack([x, y, z], axis=1)

cat_xyz = radec_to_xyz(cat['ra'].values, cat['dec'].values)
gz1_xyz = radec_to_xyz(gz1_conf['ra_deg'].values, gz1_conf['dec_deg'].values)

tree = cKDTree(cat_xyz)
# 1 arcsec = pi/648000 radians; chord distance for small angles ~ 2*sin(theta/2) ~ theta
match_tol = 1.0 / 3600.0 * np.pi / 180.0  # 1 arcsec in radians chord
dists, idxs = tree.query(gz1_xyz, k=1, workers=-1)
matched = dists < match_tol

gz1_matched = gz1_conf.iloc[matched].copy()
gz1_matched['cat_idx'] = idxs[matched]
cat_matched = cat.iloc[gz1_matched['cat_idx'].values].copy()

n_matched = len(gz1_matched)
print(f"  Matched GZ1 x catalog within 1 arcsec: {n_matched:,}")
print(f"  GZ1 CW fraction (matched): {gz1_matched['gz1_label'].mean():.4f}")

if n_matched < 1000:
    print("ERROR: Too few matches for reliable Platt fitting. Exiting.")
    exit(1)

# --- 4. Fit Platt (A, B) against GZ1 labels ---
# Platt scaling: p_cal = sigmoid(A * logit + B) where logit = log(p/(1-p))
# Original CE-ResNet Platt: A=1/4.65=-0.2151, B=-1.58
A_orig = 1.0 / 4.65
B_orig = -1.58

p_raw = cat_matched['p_cw_raw_x'].values.clip(1e-6, 1-1e-6)
logit_raw = np.log(p_raw / (1 - p_raw))
y_gz1 = gz1_matched['gz1_label'].values.astype(float)

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def platt_nll(params, logits, labels):
    """Negative log-likelihood for Platt scaling"""
    A, B = params
    p_cal = sigmoid(A * logits + B)
    p_cal = p_cal.clip(1e-7, 1-1e-7)
    nll = -np.mean(labels * np.log(p_cal) + (1-labels) * np.log(1-p_cal))
    return nll

print("Fitting GZ1 Platt parameters via L-BFGS...")
result = minimize(platt_nll, x0=[A_orig, B_orig], args=(logit_raw, y_gz1),
                  method='L-BFGS-B', options={'maxiter': 1000, 'ftol': 1e-12})
A_gz1, B_gz1 = result.x
print(f"  Original CE-ResNet Platt: A={A_orig:.4f}, B={B_orig:.4f}")
print(f"  GZ1-recalibrated Platt:   A={A_gz1:.4f}, B={B_gz1:.4f}")

# --- 5. Apply GZ1 Platt to full catalog ---
print("Applying GZ1 Platt to full catalog...")
p_raw_full = cat['p_cw_raw_x'].values.clip(1e-6, 1-1e-6)
logit_full = np.log(p_raw_full / (1 - p_raw_full))

# Original CE-ResNet Platt calibrated
p_catb_orig = sigmoid(A_orig * logit_full + B_orig)
# GZ1-recalibrated
p_catb_gz1 = sigmoid(A_gz1 * logit_full + B_gz1)

# Catalog B original: class assigned by p_catb_orig > 0.5 (after 3-class softmax proxy)
# Use p_cw_raw_x directly to simulate Catalog B threshold
# The paper Catalog B threshold is 0.5 (Platt calibrated)
def classify(p_cw_cal, p_ccw_raw, p_ns_raw):
    """Classify to CW/CCW/NS after CW Platt calibration"""
    # NS stays as raw (not calibrated), CW is calibrated
    # Majority class wins
    labels = []
    for pcw, pccw, pns in zip(p_cw_cal, p_ccw_raw, p_ns_raw):
        if pcw >= max(pccw, pns):
            labels.append('CW')
        elif pccw >= max(pcw, pns):
            labels.append('CCW')
        else:
            labels.append('NS')
    return labels

# Simplified: just compare p_catb > 0.5 for CW classification (Catalog B style)
# Restrict to spirals (exclude NS): is_spiral_orig, is_spiral_gz1
# Use raw classification to find spirals, then Platt for CW/CCW within spirals
is_spiral = (cat['p_ns_raw_x'].values < 0.5)  # rough spiral filter
p_cw_orig_cal = p_catb_orig[is_spiral]
p_cw_gz1_cal = p_catb_gz1[is_spiral]

cw_frac_orig = (p_cw_orig_cal > 0.5).mean()
cw_frac_gz1 = (p_cw_gz1_cal > 0.5).mean()

# Catalog C equivariant (ground truth for comparison)
spiral_mask = cat['class_eq'].isin(['CW', 'CCW'])
cw_frac_catc = (cat.loc[spiral_mask, 'class_eq'] == 'CW').mean()

print(f"\n=== CW Fraction Comparison ===")
print(f"  Catalog C (equivariant TTA, Catalog C spirals):  {cw_frac_catc:.6f}")
print(f"  Catalog B CE-ResNet Platt (is_spiral filter):    {cw_frac_orig:.6f}")
print(f"  Catalog B GZ1 Platt (is_spiral filter):          {cw_frac_gz1:.6f}")
print(f"  Delta (GZ1 vs CE-ResNet Platt):                  {cw_frac_gz1 - cw_frac_orig:+.6f}")

# --- 6. Calibration quality on matched set ---
p_orig_matched = sigmoid(A_orig * logit_raw + B_orig)
p_gz1_matched = sigmoid(A_gz1 * logit_raw + B_gz1)

acc_orig = ((p_orig_matched > 0.5) == y_gz1).mean()
acc_gz1 = ((p_gz1_matched > 0.5) == y_gz1).mean()
brier_orig = np.mean((p_orig_matched - y_gz1)**2)
brier_gz1 = np.mean((p_gz1_matched - y_gz1)**2)

print(f"\n=== Calibration Quality on GZ1 Matched Set (n={n_matched:,}) ===")
print(f"  CE-ResNet Platt accuracy: {acc_orig:.4f}, Brier: {brier_orig:.4f}")
print(f"  GZ1 Platt accuracy:       {acc_gz1:.4f}, Brier: {brier_gz1:.4f}")

wall = time.time() - t0

result_json = {
    "wave": "14-FFF",
    "finding": "P4-CM-M1",
    "approach": "FULL HARD FIX -- GZ1 Platt recalibration",
    "n_gz1_total": int(len(gz1)),
    "n_gz1_spirals": int(len(gz1_spiral)),
    "n_gz1_confident": int(len(gz1_conf)),
    "n_matched_1arcsec": int(n_matched),
    "gz1_cw_fraction_human": float(gz1_conf['gz1_label'].mean()),
    "gz1_cw_fraction_matched": float(gz1_matched['gz1_label'].mean()),
    "platt_orig": {"A": float(A_orig), "B": float(B_orig)},
    "platt_gz1": {"A": float(A_gz1), "B": float(B_gz1)},
    "cw_frac_catc_equivariant": float(cw_frac_catc),
    "cw_frac_catb_ceresnet": float(cw_frac_orig),
    "cw_frac_catb_gz1": float(cw_frac_gz1),
    "delta_gz1_vs_ceresnet": float(cw_frac_gz1 - cw_frac_orig),
    "calibration_quality": {
        "ceresnet": {"accuracy": float(acc_orig), "brier_score": float(brier_orig)},
        "gz1": {"accuracy": float(acc_gz1), "brier_score": float(brier_gz1)}
    },
    "wall_seconds": round(wall, 1),
    "verdict": "FULL HARD FIX: GZ1-recalibrated Platt computed; CW fraction shift quantified"
}

import os
os.makedirs('/workspace/r42_results', exist_ok=True)
with open('/workspace/r42_results/wave_14_fff_gz1_platt_recal.json', 'w') as f:
    json.dump(result_json, f, indent=2)

print(f"\nWall time: {wall:.1f}s")
print("Output: /workspace/r42_results/wave_14_fff_gz1_platt_recal.json")
print("=== P4-CM-M1 DONE ===")
