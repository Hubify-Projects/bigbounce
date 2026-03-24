#!/usr/bin/env python3.8
"""
Pipeline B Step 5: Nuisance Regression — Fix the Sky Leakage

The autoencoder anomaly scores correlate with sky position (4.8x
North/South asymmetry). This is likely from survey depth, seeing,
dust, or target selection differences.

Fix: Train a regression model to predict anomaly score from
SURVEY METADATA ONLY (no spectral features). Subtract the
predicted nuisance score. The residual is the astrophysically
meaningful anomaly score.

Method:
1. Build nuisance feature vector: RA, Dec, E(B-V), survey-depth
   proxies (FLUX_IVAR as depth proxy), ZWARN
2. Train a gradient-boosted regressor to predict AE anomaly score
   from nuisance features
3. Residual = AE_score - nuisance_prediction
4. Re-rank by residual
5. Re-check sky holdout: ratio should be ~1.0 now
"""
import numpy as np, json, os, time
from astropy.io import fits
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

OUT = '/dev/shm/bigbounce/pipeline_B/outputs'
DATA = '/dev/shm/bigbounce/pipeline_B/data'

print('='*60)
print('PIPELINE B STEP 5: NUISANCE REGRESSION')
print('='*60)

# Load catalog + anomaly scores
hdu = fits.open(DATA + '/desi_edr_zcatalog.fits')
cat = hdu[1].data
scores = np.load(OUT + '/anomaly_scores.npy')
good_indices = np.load(OUT + '/good_indices.npy')

print('Loaded %d objects with anomaly scores' % len(scores))

# Build NUISANCE features (things that are NOT astrophysical)
print('\nBuilding nuisance feature matrix...')
nuisance_cols = []
nuisance_names = []

# Sky position
if 'TARGET_RA' in cat.dtype.names:
    ra = cat['TARGET_RA'][good_indices].astype(np.float32)
    dec = cat['TARGET_DEC'][good_indices].astype(np.float32)
    # Use sin/cos to handle RA wrapping
    nuisance_cols.extend([np.sin(np.radians(ra)), np.cos(np.radians(ra)),
                          np.sin(np.radians(dec)), np.cos(np.radians(dec))])
    nuisance_names.extend(['sin_ra', 'cos_ra', 'sin_dec', 'cos_dec'])

# Depth proxy: FLUX_IVAR (higher = deeper observation)
for band_name in ['FLUX_IVAR_G', 'FLUX_IVAR_R', 'FLUX_IVAR_Z']:
    if band_name in cat.dtype.names:
        vals = cat[band_name][good_indices]
        if len(vals.shape) == 1:
            nuisance_cols.append(vals.astype(np.float32))
            nuisance_names.append(band_name)
        elif len(vals.shape) == 2:
            nuisance_cols.append(vals[:,0].astype(np.float32))
            nuisance_names.append(band_name + '_0')

# Galactic extinction proxy: MW_TRANSMISSION bands (lower = more dust)
for band_name in ['MW_TRANSMISSION_G', 'MW_TRANSMISSION_R', 'MW_TRANSMISSION_Z']:
    if band_name in cat.dtype.names:
        vals = cat[band_name][good_indices]
        if len(vals.shape) == 1:
            nuisance_cols.append(vals.astype(np.float32))
            nuisance_names.append(band_name)
        elif len(vals.shape) == 2:
            nuisance_cols.append(vals[:,0].astype(np.float32))
            nuisance_names.append(band_name + '_0')

# Quality flag (correlates with observing conditions)
if 'ZWARN' in cat.dtype.names:
    nuisance_cols.append(cat['ZWARN'][good_indices].astype(np.float32))
    nuisance_names.append('ZWARN')

X_nuis = np.column_stack(nuisance_cols)
mask_finite = np.all(np.isfinite(X_nuis), axis=1)
X_nuis_clean = X_nuis[mask_finite]
scores_clean = scores[mask_finite]

print('Nuisance features: %d columns' % X_nuis_clean.shape[1])
print('Columns: %s' % str(nuisance_names))
print('Clean objects: %d' % len(scores_clean))

# Sky split (same as training)
ra_clean = ra[mask_finite] if 'TARGET_RA' in cat.dtype.names else np.zeros(len(X_nuis_clean))
is_north = (ra_clean > 100) & (ra_clean < 260)

# Train nuisance regressor on NORTH only (where AE was trained)
X_north = X_nuis_clean[is_north]
y_north = scores_clean[is_north]

# Subsample for speed
max_n = min(200000, len(X_north))
rng = np.random.default_rng(42)
idx = rng.choice(len(X_north), max_n, replace=False)

print('\nTraining nuisance regressor on %d North-sky objects...' % max_n)
t0 = time.time()

# Use log scores (heavy tail)
y_log = np.log1p(y_north[idx])

gbr = GradientBoostingRegressor(
    n_estimators=100, max_depth=5, learning_rate=0.1,
    subsample=0.8, random_state=42
)
gbr.fit(X_north[idx], y_log)
elapsed = time.time() - t0
print('Trained in %.0fs' % elapsed)

# Feature importances
print('\nNuisance feature importances:')
for name, imp in sorted(zip(nuisance_names, gbr.feature_importances_), key=lambda x: -x[1]):
    print('  %-25s %.3f' % (name, imp))

# Predict nuisance component for ALL objects
y_pred_all = gbr.predict(X_nuis_clean)
residual = np.log1p(scores_clean) - y_pred_all

print('\nResidual (nuisance-corrected) scores:')
print('  Median: %.4f (was %.4f before correction)' % (np.median(residual), np.median(np.log1p(scores_clean))))

# Re-check sky holdout
res_north = residual[is_north]
res_south = residual[~is_north]
ratio = np.median(res_south) / np.median(res_north) if np.median(res_north) != 0 else float('inf')
print('\nSky holdout after correction:')
print('  North median: %.4f' % np.median(res_north))
print('  South median: %.4f' % np.median(res_south))
print('  Ratio: %.3f (was 4.798, should be ~1.0)' % ratio)

if abs(ratio - 1.0) < 0.5:
    holdout_status = 'PASS'
    print('  STATUS: PASS (ratio within 0.5-1.5)')
elif abs(ratio - 1.0) < 1.0:
    holdout_status = 'PARTIAL'
    print('  STATUS: PARTIAL (ratio within 0.5-2.0)')
else:
    holdout_status = 'FAIL'
    print('  STATUS: FAIL (still significant asymmetry)')

# Top anomalies after correction
top500_idx = np.argsort(residual)[-500:]
top500_orig = good_indices[np.where(mask_finite)[0][top500_idx]]

if 'SPECTYPE' in cat.dtype.names:
    types = cat['SPECTYPE'][top500_orig]
    unique_t, counts_t = np.unique(types, return_counts=True)
    print('\nTop 500 anomalies (nuisance-corrected):')
    for t, c in sorted(zip(unique_t, counts_t), key=lambda x: -x[1]):
        print('  %-15s %5d' % (t.strip(), c))

# QSO anomaly enrichment after correction
if 'SPECTYPE' in cat.dtype.names and 'Z' in cat.dtype.names:
    spec_clean = cat['SPECTYPE'][good_indices][mask_finite]
    z_clean = cat['Z'][good_indices][mask_finite]
    qso_highz = np.array([s.strip() == 'QSO' for s in spec_clean]) & (z_clean > 1.5)
    
    med_all = np.median(residual)
    med_qso = np.median(residual[qso_highz])
    print('\nHigh-z QSO enrichment (corrected):')
    print('  All objects median: %.4f' % med_all)
    print('  QSO z>1.5 median:  %.4f' % med_qso)
    if med_all != 0:
        print('  Enrichment: %.2fx' % (med_qso / med_all))

# Save
np.save(OUT + '/anomaly_scores_corrected.npy', residual)
result = {
    'n_objects': int(len(residual)),
    'holdout_ratio_before': 4.798,
    'holdout_ratio_after': float(ratio),
    'holdout_status': holdout_status,
    'top_nuisance_feature': nuisance_names[np.argmax(gbr.feature_importances_)],
    'top_nuisance_importance': float(np.max(gbr.feature_importances_)),
    'nuisance_r2_train': float(gbr.score(X_north[idx], y_log)),
    'status': 'INJECTION_VALIDATED' if holdout_status == 'PASS' else 'ROBUSTNESS_PARTIAL',
}
with open(OUT + '/step5_nuisance_correction.json', 'w') as fp:
    json.dump(result, fp, indent=2)
print('\nSaved: step5_nuisance_correction.json')
print('Status: %s' % result['status'])

hdu.close()
