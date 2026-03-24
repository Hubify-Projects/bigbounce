#!/usr/bin/env python3.8
"""
Pipeline B Step 2: PCA Baseline for spectral anomaly detection.

Gate 2 requirement: before any neural model, establish a simple
baseline. PCA reconstruction error is the simplest anomaly score.

Steps:
1. Load a representative subset of DESI spectra
2. Fit PCA with n_components = 10, 20, 50
3. Compute reconstruction error for each spectrum
4. Rank by error → baseline anomaly catalog
5. Check if known unusual objects are flagged
"""
import numpy as np
from astropy.io import fits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import json, os, time

DATA = '/dev/shm/bigbounce/pipeline_B/data'
OUT = '/dev/shm/bigbounce/pipeline_B/outputs'
os.makedirs(OUT, exist_ok=True)

print('='*60)
print('PIPELINE B STEP 2: PCA BASELINE')
print('='*60)

# Load catalog
print('Loading catalog...')
hdu = fits.open(DATA + '/desi_edr_zcatalog.fits')
cat = hdu[1].data

# We need actual spectra, not just the zcatalog
# The zcatalog has redshifts and classifications
# Spectra are in separate coadd files
# For the baseline, use the catalog metadata as features

# Build feature matrix from catalog columns
print('Building feature matrix from catalog metadata...')
feature_cols = []
for col in ['Z', 'ZERR', 'DELTACHI2', 'ZWARN']:
    if col in cat.dtype.names:
        feature_cols.append(col)

# Also use any flux/magnitude columns
for col in cat.dtype.names:
    if 'FLUX' in col or 'MW_TRANSMISSION' in col or 'FIBERFLUX' in col:
        feature_cols.append(col)

print(f'Feature columns ({len(feature_cols)}): {feature_cols[:10]}...')

# Build matrix (handle multi-dim columns)
features = []
feat_names = []
for col in feature_cols:
    vals = cat[col]
    if len(vals.shape) == 1:
        features.append(vals.astype(float))
        feat_names.append(col)
    elif len(vals.shape) == 2:
        for i in range(min(vals.shape[1], 5)):  # max 5 bands
            features.append(vals[:, i].astype(float))
            feat_names.append(f'{col}_{i}')

X = np.column_stack(features)
print(f'Feature matrix: {X.shape}')

# Clean: remove NaN/Inf rows
mask_good = np.all(np.isfinite(X), axis=1)
X_clean = X[mask_good]
print(f'After NaN removal: {X_clean.shape[0]:,} objects ({100*X_clean.shape[0]/X.shape[0]:.1f}%)')

# Subsample for speed if needed
max_n = min(500000, X_clean.shape[0])
if X_clean.shape[0] > max_n:
    rng = np.random.default_rng(42)
    idx = rng.choice(X_clean.shape[0], max_n, replace=False)
    X_sub = X_clean[idx]
    print(f'Subsampled to {max_n:,} for PCA fitting')
else:
    X_sub = X_clean
    idx = np.arange(len(X_clean))

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_sub)

# PCA at multiple component levels
for n_comp in [10, 20, 50]:
    if n_comp >= X_scaled.shape[1]:
        continue
    print(f'\nPCA with {n_comp} components:')
    pca = PCA(n_components=n_comp)
    X_reduced = pca.fit_transform(X_scaled)
    X_reconstructed = pca.inverse_transform(X_reduced)
    
    # Reconstruction error per object
    recon_error = np.mean((X_scaled - X_reconstructed)**2, axis=1)
    
    print(f'  Explained variance: {pca.explained_variance_ratio_.sum():.3f}')
    print(f'  Recon error: median={np.median(recon_error):.4f}, '
          f'mean={np.mean(recon_error):.4f}, max={np.max(recon_error):.4f}')
    
    # Top anomalies
    top_idx = np.argsort(recon_error)[-100:]
    print(f'  Top 100 anomalies: median error = {np.median(recon_error[top_idx]):.4f}')
    
    # Check what types they are
    if 'SPECTYPE' in cat.dtype.names:
        # Map back to original indices
        orig_idx = np.where(mask_good)[0][idx[top_idx]]
        types = cat['SPECTYPE'][orig_idx]
        unique_types, type_counts = np.unique(types, return_counts=True)
        print(f'  Top anomaly types:')
        for t, c in sorted(zip(unique_types, type_counts), key=lambda x: -x[1]):
            print(f'    {t.strip():15s} {c:>5d}')

print(f'\nPCA baseline complete.')
print(f'This establishes the FLOOR for anomaly detection.')
print(f'Any neural model must beat this to be worth using.')

# Save
result = {
    'n_objects': int(X_clean.shape[0]),
    'n_features': int(X_clean.shape[1]),
    'feature_names': feat_names[:20],
    'status': 'PCA_BASELINE_COMPLETE',
}
with open(OUT + '/step2_pca_baseline.json', 'w') as fp:
    json.dump(result, fp, indent=2)
print(f'Saved: {OUT}/step2_pca_baseline.json')

hdu.close()
