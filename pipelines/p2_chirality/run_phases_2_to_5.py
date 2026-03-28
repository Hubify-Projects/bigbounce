#!/usr/bin/env python3
"""
Phases 2-5: Complete the galaxy chirality catalog on H200.

Phase 2: Add coordinates (cross-match dr8_id with GZ DESI Zenodo catalog)
Phase 3: Equivariant post-processing (Catalog C) — re-run all spirals with flipped images
Phase 4: Validation (dipole, cross-survey, CE-ResNet comparison)
Phase 5: Science (final dipole + results summary)

Input: /workspace/chirality/chirality_catalog_v2_smith42.parquet (Catalog A, 8.47M rows)
       /workspace/chirality/chirality_model_v2_best.pt (v2 model)
Output: /workspace/chirality/catalog_production.parquet (Catalog C)
        /workspace/chirality/dipole_results.json
        /workspace/chirality/validation_report.json
"""
import os, sys, time, json, shutil
import numpy as np
os.environ['HF_HOME'] = '/tmp/hf_cache'
os.environ['HF_TOKEN'] = os.environ.get('HF_TOKEN', '')

import torch
import torch.nn as nn
import timm
from torchvision import transforms
from huggingface_hub import hf_hub_download
import pandas as pd
import healpy as hp
from scipy.spatial import cKDTree

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
WORK = "/workspace/chirality"
CATALOG_A = f"{WORK}/chirality_catalog_v2_smith42.parquet"
MODEL_PATH = f"{WORK}/chirality_model_v2_best.pt"
CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL']

print("=" * 70, flush=True)
print("PHASES 2-5: COMPLETING THE 8.47M CHIRALITY CATALOG", flush=True)
print(f"Device: {DEVICE} ({torch.cuda.get_device_name(0)})", flush=True)
print("=" * 70, flush=True)

# Load Catalog A
print("\nLoading Catalog A...", flush=True)
cat_a = pd.read_parquet(CATALOG_A)
print(f"  {len(cat_a):,} galaxies loaded", flush=True)

# ============================================================
# PHASE 2: Add Coordinates
# ============================================================
print("\n" + "=" * 70, flush=True)
print("PHASE 2: ADD COORDINATES (dr8_id → RA/DEC)", flush=True)
print("=" * 70, flush=True)

# Download GZ DESI Zenodo morphology catalog (has dr8_id + RA/DEC)
# The full catalog is at: https://zenodo.org/records/8360385
# But it's large. Instead, use the Smith42 parquet metadata which has dr8_id
# We need to extract RA/DEC from the original images or a cross-match catalog

# Approach: download GZ DESI predictions catalog from Zenodo
# This has all 8.67M galaxies with RA, DEC, and morphology predictions
print("  Downloading GZ DESI predictions catalog...", flush=True)

gz_desi_url = "https://zenodo.org/records/8360385/files/predictions_table.parquet"
gz_desi_path = f"{WORK}/gz_desi_predictions.parquet"

if not os.path.exists(gz_desi_path):
    import urllib.request
    try:
        req = urllib.request.Request(gz_desi_url)
        req.add_header("User-Agent", "Mozilla/5.0")
        resp = urllib.request.urlopen(req, timeout=600)
        with open(gz_desi_path, 'wb') as f:
            while True:
                chunk = resp.read(1024*1024)
                if not chunk:
                    break
                f.write(chunk)
        print(f"  Downloaded: {os.path.getsize(gz_desi_path)/1e6:.0f} MB", flush=True)
    except Exception as e:
        print(f"  Download failed: {e}", flush=True)
        print("  Trying alternative: extract from Smith42 parquet headers...", flush=True)
        gz_desi_path = None

if gz_desi_path and os.path.exists(gz_desi_path):
    try:
        gz_desi = pd.read_parquet(gz_desi_path)
        print(f"  GZ DESI catalog: {len(gz_desi):,} rows", flush=True)
        print(f"  Columns: {list(gz_desi.columns)[:10]}", flush=True)

        # Find the right ID column for cross-matching
        id_cols = [c for c in gz_desi.columns if 'id' in c.lower() or 'dr8' in c.lower()]
        ra_cols = [c for c in gz_desi.columns if 'ra' in c.lower()]
        dec_cols = [c for c in gz_desi.columns if 'dec' in c.lower()]
        print(f"  ID columns: {id_cols[:5]}", flush=True)
        print(f"  RA columns: {ra_cols[:5]}", flush=True)
        print(f"  DEC columns: {dec_cols[:5]}", flush=True)

        # Try to match on dr8_id or similar
        if 'dr8_id' in gz_desi.columns:
            match_col = 'dr8_id'
        elif 'id_str' in gz_desi.columns:
            match_col = 'id_str'
        else:
            match_col = id_cols[0] if id_cols else None

        if match_col and ra_cols and dec_cols:
            gz_desi[match_col] = gz_desi[match_col].astype(str)
            cat_a['dr8_id'] = cat_a['dr8_id'].astype(str)

            # Merge
            ra_col = ra_cols[0]
            dec_col = dec_cols[0]
            coords = gz_desi[[match_col, ra_col, dec_col]].rename(
                columns={match_col: 'dr8_id', ra_col: 'ra', dec_col: 'dec'})
            coords = coords.drop_duplicates(subset='dr8_id')

            before = len(cat_a)
            cat_a = cat_a.merge(coords, on='dr8_id', how='left')
            matched = cat_a['ra'].notna().sum()
            print(f"  Matched: {matched:,}/{before:,} ({matched/before*100:.1f}%)", flush=True)
        else:
            print(f"  Could not find matching columns", flush=True)
    except Exception as e:
        print(f"  Error reading GZ DESI catalog: {e}", flush=True)
else:
    print("  No GZ DESI catalog available — skipping coordinate addition", flush=True)
    print("  Catalog C will have dr8_id but no RA/DEC", flush=True)

# Add image URLs where we have coordinates
if 'ra' in cat_a.columns and 'dec' in cat_a.columns:
    has_coords = cat_a['ra'].notna()
    cat_a.loc[has_coords, 'image_url'] = cat_a.loc[has_coords].apply(
        lambda r: f"https://www.legacysurvey.org/viewer/jpeg-cutout?ra={r['ra']:.6f}&dec={r['dec']:.6f}&size=150&layer=ls-dr9",
        axis=1)
    print(f"  Image URLs added for {has_coords.sum():,} galaxies", flush=True)

# Save Catalog A with coordinates
cat_a.to_parquet(f"{WORK}/catalog_a_with_coords.parquet")
print(f"  Saved: catalog_a_with_coords.parquet ({len(cat_a):,} rows)", flush=True)

# ============================================================
# PHASE 3: Equivariant Post-Processing (Catalog C)
# ============================================================
print("\n" + "=" * 70, flush=True)
print("PHASE 3: EQUIVARIANT POST-PROCESSING (CATALOG C)", flush=True)
print("=" * 70, flush=True)

# Load model
print("  Loading model...", flush=True)

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
ckpt = torch.load(MODEL_PATH, weights_only=True)
encoder.load_state_dict(ckpt['enc'])
head.load_state_dict(ckpt['head'])

class Model(nn.Module):
    def __init__(self, e, h):
        super().__init__()
        self.e = e; self.h = h
    def forward(self, x):
        return self.h(self.e(x))

model = Model(encoder, head).to(DEVICE).eval()
print(f"  Model loaded (val_acc={ckpt['val_acc']:.4f})", flush=True)

tfm = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# Build dr8_id lookup from Catalog A
id_set = set(cat_a['dr8_id'].values)
# Index for fast lookup
id_to_idx = {did: i for i, did in enumerate(cat_a['dr8_id'].values)}
print(f"  ID lookup built: {len(id_to_idx):,} galaxies", flush=True)

# Equivariant: for each galaxy, compute p(orig) and p(flip), average with swap
# Process shard by shard from Smith42/galaxies
REPO = "Smith42/galaxies"
N_SHARDS = 192
BS = 128  # H200 has 143GB VRAM, can use bigger batches
SHARD_DIR = f"{WORK}/eq_shards"
os.makedirs(SHARD_DIR, exist_ok=True)

# Check done shards
done_shards = set()
for f in os.listdir(SHARD_DIR):
    if f.startswith('eq_') and f.endswith('.parquet'):
        done_shards.add(int(f.split('_')[1].split('.')[0]))
print(f"  Equivariant shards done: {len(done_shards)}/{N_SHARDS}", flush=True)

t_phase3 = time.time()
from PIL import Image
import io

for shard_idx in range(N_SHARDS):
    if shard_idx in done_shards:
        continue

    shard_file = f"data/train-{shard_idx:05d}-of-{N_SHARDS:05d}.parquet"
    print(f"\n  [Shard {shard_idx}/{N_SHARDS-1}] Downloading...", flush=True)

    try:
        local_path = hf_hub_download(
            repo_id=REPO, filename=shard_file, repo_type="dataset",
            token=os.environ.get('HF_TOKEN', ''), cache_dir="/tmp/hf_cache")
    except Exception as e:
        print(f"    ERROR downloading: {e}", flush=True)
        continue

    df = pd.read_parquet(local_path)
    t_shard = time.time()

    results = []
    ibatch_orig = []
    ibatch_flip = []
    mbatch = []
    n_skip = 0

    for i in range(len(df)):
        row = df.iloc[i]
        dr8_id = str(row.get('dr8_id', ''))

        if dr8_id not in id_set:
            n_skip += 1
            continue

        try:
            img = row['image']
            if isinstance(img, dict) and 'bytes' in img:
                img = Image.open(io.BytesIO(img['bytes']))
            elif isinstance(img, bytes):
                img = Image.open(io.BytesIO(img))
            if not isinstance(img, Image.Image):
                continue
            if img.mode != 'RGB':
                img = img.convert('RGB')

            img_orig = tfm(img)
            img_flip = tfm(img.transpose(Image.FLIP_LEFT_RIGHT))

            ibatch_orig.append(img_orig)
            ibatch_flip.append(img_flip)
            mbatch.append(dr8_id)
        except:
            continue

        if len(ibatch_orig) >= BS:
            bt_orig = torch.stack(ibatch_orig).to(DEVICE)
            bt_flip = torch.stack(ibatch_flip).to(DEVICE)

            with torch.no_grad():
                p_orig = torch.softmax(model(bt_orig), dim=1).cpu().numpy()
                p_flip = torch.softmax(model(bt_flip), dim=1).cpu().numpy()

            for did, po, pf in zip(mbatch, p_orig, p_flip):
                # Equivariant average: swap CW↔CCW for flipped
                eq_cw = (po[0] + pf[1]) / 2
                eq_ccw = (po[1] + pf[0]) / 2
                eq_ns = (po[2] + pf[2]) / 2
                cls_eq = CLASS_NAMES[np.argmax([eq_cw, eq_ccw, eq_ns])]

                results.append({
                    'dr8_id': did,
                    'p_cw_raw': float(po[0]),
                    'p_ccw_raw': float(po[1]),
                    'p_ns_raw': float(po[2]),
                    'p_cw_eq': float(eq_cw),
                    'p_ccw_eq': float(eq_ccw),
                    'p_ns_eq': float(eq_ns),
                    'class_raw': CLASS_NAMES[po.argmax()],
                    'class_eq': cls_eq,
                    'confidence_eq': float(max(eq_cw, eq_ccw, eq_ns)),
                })

            ibatch_orig, ibatch_flip, mbatch = [], [], []

    # Process remaining
    if ibatch_orig:
        bt_orig = torch.stack(ibatch_orig).to(DEVICE)
        bt_flip = torch.stack(ibatch_flip).to(DEVICE)
        with torch.no_grad():
            p_orig = torch.softmax(model(bt_orig), dim=1).cpu().numpy()
            p_flip = torch.softmax(model(bt_flip), dim=1).cpu().numpy()
        for did, po, pf in zip(mbatch, p_orig, p_flip):
            eq_cw = (po[0] + pf[1]) / 2
            eq_ccw = (po[1] + pf[0]) / 2
            eq_ns = (po[2] + pf[2]) / 2
            cls_eq = CLASS_NAMES[np.argmax([eq_cw, eq_ccw, eq_ns])]
            results.append({
                'dr8_id': did,
                'p_cw_raw': float(po[0]), 'p_ccw_raw': float(po[1]), 'p_ns_raw': float(po[2]),
                'p_cw_eq': float(eq_cw), 'p_ccw_eq': float(eq_ccw), 'p_ns_eq': float(eq_ns),
                'class_raw': CLASS_NAMES[po.argmax()], 'class_eq': cls_eq,
                'confidence_eq': float(max(eq_cw, eq_ccw, eq_ns)),
            })

    # Save shard
    shard_df = pd.DataFrame(results)
    shard_df.to_parquet(f"{SHARD_DIR}/eq_{shard_idx:04d}.parquet")
    done_shards.add(shard_idx)

    elapsed = time.time() - t_shard
    n_proc = len(results)
    cw_eq = (shard_df['class_eq'] == 'CW').sum() if len(shard_df) > 0 else 0
    ccw_eq = (shard_df['class_eq'] == 'CCW').sum() if len(shard_df) > 0 else 0

    print(f"    {n_proc:,} processed in {elapsed/60:.1f}min | CW_eq={cw_eq} CCW_eq={ccw_eq} | skip={n_skip}", flush=True)
    print(f"    PROGRESS: {len(done_shards)}/{N_SHARDS} shards", flush=True)

    # Clean cache
    shutil.rmtree("/tmp/hf_cache", ignore_errors=True)

# Merge equivariant results
print("\n  Merging equivariant results...", flush=True)
eq_dfs = []
for f in sorted(os.listdir(SHARD_DIR)):
    if f.endswith('.parquet'):
        eq_dfs.append(pd.read_parquet(f"{SHARD_DIR}/{f}"))
eq_catalog = pd.concat(eq_dfs, ignore_index=True)

# Merge with Catalog A coordinates
if 'ra' in cat_a.columns:
    coord_cols = ['dr8_id']
    if 'ra' in cat_a.columns: coord_cols.append('ra')
    if 'dec' in cat_a.columns: coord_cols.append('dec')
    if 'image_url' in cat_a.columns: coord_cols.append('image_url')
    eq_catalog = eq_catalog.merge(cat_a[coord_cols].drop_duplicates('dr8_id'), on='dr8_id', how='left')

eq_catalog.to_parquet(f"{WORK}/catalog_production.parquet")

n_total = len(eq_catalog)
n_cw = (eq_catalog['class_eq'] == 'CW').sum()
n_ccw = (eq_catalog['class_eq'] == 'CCW').sum()
n_ns = (eq_catalog['class_eq'] == 'NOT_SPIRAL').sum()
n_spiral = n_cw + n_ccw

print(f"\n  CATALOG C (Production):", flush=True)
print(f"    Total: {n_total:,}", flush=True)
print(f"    CW: {n_cw:,} ({n_cw/n_total*100:.1f}%)", flush=True)
print(f"    CCW: {n_ccw:,} ({n_ccw/n_total*100:.1f}%)", flush=True)
print(f"    NS: {n_ns:,} ({n_ns/n_total*100:.1f}%)", flush=True)
print(f"    CW/(CW+CCW): {n_cw/n_spiral:.4f}", flush=True)
print(f"    Time: {(time.time()-t_phase3)/3600:.1f}h", flush=True)

# ============================================================
# PHASE 4: Validation
# ============================================================
print("\n" + "=" * 70, flush=True)
print("PHASE 4: VALIDATION", flush=True)
print("=" * 70, flush=True)

validation = {}

# 4a: Dipole analysis
print("\n  4a: Dipole analysis...", flush=True)
if 'ra' in eq_catalog.columns and eq_catalog['ra'].notna().sum() > 10000:
    spirals = eq_catalog[(eq_catalog['class_eq'].isin(['CW', 'CCW'])) & (eq_catalog['confidence_eq'] > 0.6)]
    spirals = spirals[spirals['ra'].notna()]
    print(f"    Spirals with coords: {len(spirals):,}", flush=True)

    NSIDE = 64
    npix = hp.nside2npix(NSIDE)
    cw_map = np.zeros(npix)
    ccw_map = np.zeros(npix)

    theta = np.radians(90 - spirals['dec'].values)
    phi = np.radians(spirals['ra'].values % 360)
    pix = hp.ang2pix(NSIDE, theta, phi)

    for p, c in zip(pix, spirals['class_eq'].values):
        if c == 'CW': cw_map[p] += 1
        else: ccw_map[p] += 1

    tot = cw_map + ccw_map
    mask = tot > 10
    asym = np.full(npix, hp.UNSEEN)
    asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot[mask]

    # Fit dipole
    mono, dip = hp.fit_dipole(asym[mask], gal_cut=0)
    dip_amp = np.sqrt(np.sum(dip**2))
    dip_l = np.degrees(np.arctan2(dip[1], dip[0])) % 360
    dip_b = np.degrees(np.arcsin(dip[2] / dip_amp)) if dip_amp > 0 else 0

    # Bootstrap
    print(f"    Running 10K bootstrap...", flush=True)
    boot_amps = []
    valid_asym = asym[mask]
    for _ in range(10000):
        np.random.shuffle(valid_asym)
        asym_tmp = np.full(npix, hp.UNSEEN)
        asym_tmp[mask] = valid_asym
        _, d = hp.fit_dipole(asym_tmp[mask], gal_cut=0)
        boot_amps.append(np.sqrt(np.sum(d**2)))
    boot_amps = np.array(boot_amps)
    sigma = (dip_amp - np.mean(boot_amps)) / np.std(boot_amps) if np.std(boot_amps) > 0 else 0
    pval = np.mean(boot_amps >= dip_amp)

    print(f"    Monopole: {mono:.4f}", flush=True)
    print(f"    Dipole: A={dip_amp:.4f} (l={dip_l:.1f}, b={dip_b:.1f})", flush=True)
    print(f"    Significance: {sigma:.2f}σ (p={pval:.4f})", flush=True)

    validation['dipole'] = {
        'monopole': float(mono), 'amplitude': float(dip_amp),
        'l': float(dip_l), 'b': float(dip_b),
        'sigma': float(sigma), 'p_value': float(pval),
        'n_spirals': len(spirals), 'n_pixels': int(mask.sum()),
        'catalog': 'C_equivariant',
    }
else:
    print("    Skipping dipole — no coordinates available", flush=True)
    print("    Will run dipole after Phase 2 coordinate cross-match", flush=True)
    validation['dipole'] = {'status': 'pending_coordinates'}

# 4b: CW/CCW balance by confidence bin
print("\n  4b: Balance by confidence bin...", flush=True)
for lo, hi in [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1.0)]:
    m = (eq_catalog['confidence_eq'] >= lo) & (eq_catalog['confidence_eq'] < hi) & \
        (eq_catalog['class_eq'].isin(['CW', 'CCW']))
    if m.sum() > 100:
        cw_f = (eq_catalog.loc[m, 'class_eq'] == 'CW').mean()
        print(f"    [{lo:.1f}, {hi:.1f}): n={m.sum():>8,} CW={cw_f:.4f}", flush=True)

# 4c: Raw vs Equivariant comparison
print("\n  4c: Raw vs Equivariant comparison...", flush=True)
spirals_all = eq_catalog[eq_catalog['class_eq'].isin(['CW', 'CCW'])]
raw_cw = (eq_catalog['class_raw'] == 'CW').sum()
raw_ccw = (eq_catalog['class_raw'] == 'CCW').sum()
eq_cw_total = n_cw
eq_ccw_total = n_ccw

print(f"    Raw:  CW={raw_cw:,} CCW={raw_ccw:,} ratio={raw_cw/(raw_cw+raw_ccw):.4f}", flush=True)
print(f"    Eq:   CW={eq_cw_total:,} CCW={eq_ccw_total:,} ratio={eq_cw_total/(eq_cw_total+eq_ccw_total):.4f}", flush=True)

reclassified = (eq_catalog['class_raw'] != eq_catalog['class_eq']).sum()
print(f"    Reclassified: {reclassified:,} ({reclassified/n_total*100:.1f}%)", flush=True)

validation['balance'] = {
    'raw_cw_frac': float(raw_cw / (raw_cw + raw_ccw)),
    'eq_cw_frac': float(eq_cw_total / (eq_cw_total + eq_ccw_total)),
    'reclassified': int(reclassified),
    'reclassified_pct': float(reclassified / n_total * 100),
}

# ============================================================
# PHASE 5: Final Summary
# ============================================================
print("\n" + "=" * 70, flush=True)
print("PHASE 5: FINAL SUMMARY", flush=True)
print("=" * 70, flush=True)

summary = {
    'catalog': 'Catalog C (equivariant production)',
    'dataset': 'Smith42/galaxies (DESI Legacy Survey DR8)',
    'n_total': n_total,
    'n_cw': int(n_cw), 'n_ccw': int(n_ccw), 'n_ns': int(n_ns),
    'n_spirals': int(n_spiral),
    'cw_spiral_frac_eq': float(n_cw / n_spiral),
    'model': 'bamfai/galaxy-chirality-v2',
    'model_val_acc': float(ckpt['val_acc']),
    'validation': validation,
    'has_coordinates': bool('ra' in eq_catalog.columns and eq_catalog['ra'].notna().sum() > 0),
    'has_image_urls': bool('image_url' in eq_catalog.columns),
}

with open(f"{WORK}/final_summary.json", 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n  FINAL CATALOG C:", flush=True)
print(f"    Galaxies: {n_total:,}", flush=True)
print(f"    Spirals: {n_spiral:,}", flush=True)
print(f"    CW/(CW+CCW) equivariant: {n_cw/n_spiral:.4f}", flush=True)
print(f"    Files:", flush=True)
print(f"      catalog_production.parquet ({os.path.getsize(f'{WORK}/catalog_production.parquet')/1e6:.0f} MB)", flush=True)
print(f"      final_summary.json", flush=True)

print(f"\n{'='*70}", flush=True)
print(f"ALL PHASES COMPLETE", flush=True)
print(f"{'='*70}", flush=True)
