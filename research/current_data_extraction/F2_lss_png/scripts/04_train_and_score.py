#!/usr/bin/env python3.8
import numpy as np, json, os, time
from astropy.io import fits
from sklearn.preprocessing import StandardScaler
import torch
import sys
sys.path.insert(0, '/dev/shm/bigbounce/pipeline_B/scripts')
from importlib import import_module

OUT = '/dev/shm/bigbounce/pipeline_B/outputs'
DATA = '/dev/shm/bigbounce/pipeline_B/data'
os.makedirs(OUT, exist_ok=True)

print('='*60)
print('PIPELINE B STEP 4: TRAIN AUTOENCODER + SCORE ALL OBJECTS')
print('='*60)

# Load catalog
print('Loading catalog...')
hdu = fits.open(DATA + '/desi_edr_zcatalog.fits')
cat = hdu[1].data

# Build feature matrix (same as PCA baseline)
feature_cols = []
feat_names = []
for col in cat.dtype.names:
    if col in ['Z','ZERR','DELTACHI2'] or 'FLUX' in col or 'FIBERFLUX' in col:
        vals = cat[col]
        if len(vals.shape) == 1:
            feature_cols.append(vals.astype(np.float32))
            feat_names.append(col)
        elif len(vals.shape) == 2:
            for i in range(min(vals.shape[1], 5)):
                feature_cols.append(vals[:,i].astype(np.float32))
                feat_names.append('%s_%d' % (col, i))

X = np.column_stack(feature_cols)
mask_good = np.all(np.isfinite(X), axis=1)
X_clean = X[mask_good]
good_indices = np.where(mask_good)[0]
print('Features: %d columns, %d clean objects' % (X_clean.shape[1], X_clean.shape[0]))

# Sky-region split (NOT random) — use RA for holdout
ra = cat['TARGET_RA'][mask_good] if 'TARGET_RA' in cat.dtype.names else np.zeros(len(X_clean))
# North (RA 100-260) vs South (RA 260-100)
is_north = (ra > 100) & (ra < 260)
# Train on north (larger), validate on part of north, test on south
n_north = np.sum(is_north)
n_south = np.sum(~is_north)
print('Sky split: North=%d, South=%d' % (n_north, n_south))

# Further split north into train/val
rng = np.random.default_rng(42)
north_idx = np.where(is_north)[0]
rng.shuffle(north_idx)
n_val = min(50000, len(north_idx) // 10)
val_idx = north_idx[:n_val]
train_idx = north_idx[n_val:]
test_idx = np.where(~is_north)[0]

print('Train: %d, Val: %d, Test (South): %d' % (len(train_idx), len(val_idx), len(test_idx)))

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_clean[train_idx])
X_val = scaler.transform(X_clean[val_idx])
X_test = scaler.transform(X_clean[test_idx])

# Import autoencoder
spec = import_module('03_spectral_autoencoder')

# Train
print('\nTraining autoencoder...')
t0 = time.time()
model, history = spec.train_autoencoder(
    X_train, X_val,
    input_dim=X_train.shape[1],
    latent_dim=32,
    epochs=30,
    batch_size=1024,
    lr=1e-3
)
elapsed = time.time() - t0
print('Training done in %.0fs' % elapsed)

# Score ALL objects
print('\nScoring all objects...')
X_all_scaled = scaler.transform(X_clean)
scores, latents = spec.compute_anomaly_catalog(model, X_all_scaled)
print('Scores: min=%.6f, median=%.6f, max=%.6f' % (
    np.min(scores), np.median(scores), np.max(scores)))

# Compare with PCA baseline
print('\n--- COMPARISON: Autoencoder vs PCA ---')
from sklearn.decomposition import PCA
pca = PCA(n_components=10)
X_pca = pca.fit_transform(X_all_scaled[:500000])
X_pca_recon = pca.inverse_transform(X_pca)
pca_errors = np.mean((X_all_scaled[:500000] - X_pca_recon)**2, axis=1)
ae_errors = scores[:500000]

# Correlation between PCA and AE anomaly scores
corr = np.corrcoef(pca_errors, ae_errors)[0,1]
print('PCA vs AE score correlation: %.3f' % corr)

# Top-100 overlap
pca_top100 = set(np.argsort(pca_errors)[-100:])
ae_top100 = set(np.argsort(ae_errors)[-100:])
overlap = len(pca_top100 & ae_top100)
print('Top-100 overlap: %d/100' % overlap)

# AE improvement: does AE find anomalies PCA misses?
ae_unique = ae_top100 - pca_top100
print('AE-unique top anomalies: %d' % len(ae_unique))

# Anomaly type breakdown (top 500)
top500_idx = np.argsort(scores)[-500:]
top500_orig = good_indices[top500_idx]
if 'SPECTYPE' in cat.dtype.names:
    types = cat['SPECTYPE'][top500_orig]
    unique_t, counts_t = np.unique(types, return_counts=True)
    print('\nTop 500 anomaly types:')
    for t, c in sorted(zip(unique_t, counts_t), key=lambda x: -x[1]):
        print('  %-15s %5d' % (t.strip(), c))

# High-z QSO anomaly enrichment
if 'SPECTYPE' in cat.dtype.names and 'Z' in cat.dtype.names:
    qso_mask = np.array([s.strip() == 'QSO' for s in cat['SPECTYPE'][good_indices]])
    z_vals = cat['Z'][good_indices]
    highz_qso = qso_mask & (z_vals > 1.5)
    
    # Are high-z QSOs enriched in anomalies?
    median_score_all = np.median(scores)
    median_score_highz_qso = np.median(scores[highz_qso])
    print('\nHigh-z QSO anomaly enrichment:')
    print('  Median score (all): %.6f' % median_score_all)
    print('  Median score (QSO z>1.5): %.6f' % median_score_highz_qso)
    print('  Enrichment: %.2fx' % (median_score_highz_qso / median_score_all))

# Test set performance (South sky)
test_scores = scores[test_idx]
train_scores = scores[train_idx]
print('\nSky holdout (Gate 5):')
print('  Train median score: %.6f' % np.median(train_scores))
print('  Test (South) median: %.6f' % np.median(test_scores))
print('  Ratio: %.3f (should be ~1.0 if no leakage)' % (np.median(test_scores)/np.median(train_scores)))

# Save results
print('\nSaving...')
np.save(OUT + '/anomaly_scores.npy', scores)
np.save(OUT + '/latent_embeddings.npy', latents)
np.save(OUT + '/good_indices.npy', good_indices)

result = {
    'n_objects': int(len(scores)),
    'n_features': int(X_clean.shape[1]),
    'train_loss_final': float(history['train_loss'][-1]),
    'val_loss_final': float(history['val_loss'][-1]),
    'score_median': float(np.median(scores)),
    'score_p99': float(np.percentile(scores, 99)),
    'pca_ae_correlation': float(corr),
    'top100_overlap': int(overlap),
    'training_time_s': float(elapsed),
    'sky_holdout_ratio': float(np.median(test_scores)/np.median(train_scores)),
    'status': 'BASELINE_REPRODUCED' if corr > 0.5 else 'NEEDS_INVESTIGATION',
}
with open(OUT + '/step4_autoencoder_results.json', 'w') as fp:
    json.dump(result, fp, indent=2)
print('Saved: anomaly_scores.npy, latent_embeddings.npy, step4_autoencoder_results.json')
print('Status: %s' % result['status'])

hdu.close()
torch.save(model.state_dict(), OUT + '/autoencoder_model.pt')
print('Model saved: autoencoder_model.pt')
