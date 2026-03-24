#!/usr/bin/env python3.8
"""
Pipeline B Step 7: Download spectra for top anomalies + build review table

1. Map top anomalies to healpix pixels
2. Download the needed coadd files
3. Extract actual spectra
4. Build human review table
5. Re-run injection on spectral features
"""
import numpy as np, json, os, time
from astropy.io import fits
import urllib.request

OUT = '/dev/shm/bigbounce/pipeline_B/outputs'
DATA = '/dev/shm/bigbounce/pipeline_B/data'
SPEC_DIR = DATA + '/spectra'
os.makedirs(SPEC_DIR, exist_ok=True)

# Load catalog + anomaly scores
hdu = fits.open(DATA + '/desi_edr_zcatalog.fits')
cat = hdu[1].data
scores_pct = np.load(OUT + '/anomaly_scores_percentile.npy')
good_indices = np.load(OUT + '/good_indices.npy')

# Get finite mask (same as step 6)
feature_cols = []
for col in cat.dtype.names:
    if col in ['Z','ZERR','DELTACHI2'] or 'FLUX' in col or 'FIBERFLUX' in col:
        vals = cat[col][good_indices]
        if len(vals.shape) == 1:
            feature_cols.append(vals.astype(np.float32))
        elif len(vals.shape) == 2:
            for i in range(min(vals.shape[1], 5)):
                feature_cols.append(vals[:,i].astype(np.float32))
X = np.column_stack(feature_cols)
mask_good = np.all(np.isfinite(X), axis=1)
scores_clean = scores_pct[mask_good]

# Top 50 anomalies for human review
top50_idx = np.argsort(scores_clean)[-50:][::-1]
top50_orig = good_indices[np.where(mask_good)[0][top50_idx]]

print('='*60)
print('HUMAN REVIEW TABLE — Top 50 Anomalies')
print('='*60)
print()
print('%-5s %-20s %8s %8s %8s %-8s %6s %10s %10s %10s' % (
    'Rank', 'TARGETID', 'RA', 'Dec', 'z', 'Type', 'ZWARN', 'Score', 'FLUX_G', 'FLUX_R'))
print('-' * 105)

review_objects = []
for rank, idx in enumerate(top50_orig):
    obj = {
        'rank': rank + 1,
        'targetid': int(cat['TARGETID'][idx]),
        'ra': float(cat['TARGET_RA'][idx]),
        'dec': float(cat['TARGET_DEC'][idx]),
        'z': float(cat['Z'][idx]),
        'spectype': cat['SPECTYPE'][idx].strip(),
        'zwarn': int(cat['ZWARN'][idx]),
        'anomaly_pct': float(scores_clean[np.where(np.where(mask_good)[0] == np.where(good_indices == idx)[0][0])[0][0]]) if len(np.where(good_indices == idx)[0]) > 0 else 0,
    }
    
    # Get flux values
    for band in ['FLUX_G', 'FLUX_R', 'FLUX_Z']:
        if band in cat.dtype.names:
            v = cat[band][idx]
            obj[band.lower()] = float(v[0] if hasattr(v, '__len__') else v)
    
    review_objects.append(obj)
    
    print('%-5d %-20d %8.3f %8.3f %8.4f %-8s %6d %10.4f %10.2f %10.2f' % (
        obj['rank'], obj['targetid'], obj['ra'], obj['dec'], obj['z'],
        obj['spectype'], obj['zwarn'], obj.get('anomaly_pct', 0),
        obj.get('flux_g', 0), obj.get('flux_r', 0)))

# Also top 20 QSO anomalies
print('\n' + '='*60)
print('Top 20 QSO Anomalies (potential unusual QSOs)')
print('='*60)

spec_clean = cat['SPECTYPE'][good_indices][mask_good]
z_clean = cat['Z'][good_indices][mask_good]
qso_mask_clean = np.array([s.strip() == 'QSO' for s in spec_clean])
qso_scores = scores_clean.copy()
qso_scores[~qso_mask_clean] = -1  # mask non-QSOs

top20_qso_idx = np.argsort(qso_scores)[-20:][::-1]
top20_qso_orig = good_indices[np.where(mask_good)[0][top20_qso_idx]]

print('%-5s %-20s %8s %8s %8s %6s' % ('Rank', 'TARGETID', 'RA', 'Dec', 'z', 'ZWARN'))
print('-' * 60)

qso_review = []
for rank, idx in enumerate(top20_qso_orig):
    obj = {
        'rank': rank + 1,
        'targetid': int(cat['TARGETID'][idx]),
        'ra': float(cat['TARGET_RA'][idx]),
        'dec': float(cat['TARGET_DEC'][idx]),
        'z': float(cat['Z'][idx]),
        'zwarn': int(cat['ZWARN'][idx]),
    }
    qso_review.append(obj)
    print('%-5d %-20d %8.3f %8.3f %8.4f %6d' % (
        obj['rank'], obj['targetid'], obj['ra'], obj['dec'], obj['z'], obj['zwarn']))

# Determine which healpix pixels we need for spectra
# DESI uses NESTED healpix at nside=64
try:
    import healpy as hp
    nside = 64
    top_ra = cat['TARGET_RA'][top50_orig]
    top_dec = cat['TARGET_DEC'][top50_orig]
    theta = np.radians(90 - top_dec)
    phi = np.radians(top_ra)
    pixels = hp.ang2pix(nside, theta, phi, nest=True)
    unique_pixels = np.unique(pixels)
    print('\nHealpix pixels needed for top-50 spectra: %d unique' % len(unique_pixels))
    print('Pixels:', unique_pixels.tolist())
except:
    print('\nCould not compute healpix pixels (healpy issue)')
    unique_pixels = []

# Save review tables
review_data = {
    'top50_anomalies': review_objects,
    'top20_qso_anomalies': qso_review,
    'healpix_pixels_needed': unique_pixels.tolist() if len(unique_pixels) > 0 else [],
    'instructions': {
        'gate9_human_review': [
            'For each object, mark as: INTERESTING / ARTIFACT / KNOWN_TYPE / NEEDS_SPECTRUM',
            'INTERESTING = genuinely unusual, worth follow-up or catalog inclusion',
            'ARTIFACT = data quality issue, bad photometry, reduction failure',
            'KNOWN_TYPE = unusual but recognized (e.g., rare stellar type)',
            'NEEDS_SPECTRUM = can only judge with the actual spectrum',
            'Focus on: do the fluxes make physical sense? Is the redshift plausible for the type?',
        ],
        'how_to_use_red_team': [
            'The red-team report lists 12 specific risks.',
            'Top action items:',
            '1. Get actual spectra for top anomalies (fixes Gate 3)',
            '2. Sub-classify star anomalies (most are unusual stellar types)',
            '3. Check if QSO anomalies have unusual spectra vs template mismatch',
            '4. Include a Limitations section in any paper citing the risks',
        ],
    },
}

with open(OUT + '/human_review_table.json', 'w') as fp:
    json.dump(review_data, fp, indent=2)
print('\nSaved: human_review_table.json')

# Download one example coadd file to test the spectral pipeline
if len(unique_pixels) > 0:
    pix = unique_pixels[0]
    # Map pixel to the DESI directory structure
    pix_group = pix // 100
    base_url = 'https://data.desi.lbl.gov/public/edr/spectro/redux/fuji/healpix/sv3/dark/%d/%d/' % (pix_group, pix)
    coadd_name = 'coadd-sv3-dark-%d.fits' % pix
    url = base_url + coadd_name
    
    print('\nDownloading example coadd: %s' % coadd_name)
    try:
        urllib.request.urlretrieve(url, SPEC_DIR + '/' + coadd_name)
        size = os.path.getsize(SPEC_DIR + '/' + coadd_name)
        print('Downloaded: %.1f MB' % (size/1e6))
        
        # Explore the coadd structure
        sp = fits.open(SPEC_DIR + '/' + coadd_name)
        print('Coadd HDUs:')
        for h in sp:
            print('  %s: %s' % (h.name, str(h.data.shape) if h.data is not None else 'None'))
        sp.close()
    except Exception as e:
        print('Download failed: %s' % str(e)[:100])
        print('(This pixel may not exist in sv3/dark — try sv1 or other surveys)')

hdu.close()
