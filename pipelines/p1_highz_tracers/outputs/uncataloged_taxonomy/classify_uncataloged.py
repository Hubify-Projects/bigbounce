#!/usr/bin/env python3
"""
Uncataloged Object Taxonomy Pipeline v3
========================================
Classifies 1,127 uncataloged DESI DR1 anomalies (not in SIMBAD or NED)
into astrophysical families.

Method:
  1. PCA 128-dim latent -> 20 components (88.6% variance)
  2. UMAP 20->2 (n_neighbors=15, min_dist=0.05) on LATENT ONLY
  3. HDBSCAN with leaf method (min_cluster_size=15, min_samples=3)
     -> finds 29 natural clusters + noise
  4. kNN reassignment of noise points to nearest cluster
  5. Rule-based astrophysical labeling from cluster properties
  6. Merge clusters with identical labels into families
"""

import json
import warnings
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from pathlib import Path
from collections import Counter

warnings.filterwarnings('ignore')

BASE = Path('/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs')
PARQUET_DIR = BASE / 'enhanced_18M_deduped'
CROSSMATCH_FILE = BASE / 'silver_crossmatch' / 'silver_crossmatch_results.json'
OUTPUT_DIR = BASE / 'uncataloged_taxonomy'

KNOWN_LINES = {
    'Ly-alpha': 1216, 'N V': 1240, 'Si IV': 1397, 'C IV': 1549,
    'He II': 1640, 'C III]': 1909, 'Fe II UV': 2400, 'Mg II': 2798,
    '[Ne V]': 3426, '[O II]': 3727, 'Ca II K': 3934, 'Ca II H': 3969,
    'H-delta': 4102, 'H-gamma': 4340, 'H-beta': 4861,
    '[O III] 4959': 4959, '[O III] 5007': 5007, 'Mg b': 5175,
    'Na D': 5893, '[O I]': 6300, 'H-alpha': 6563, '[N II]': 6584,
    '[S II] 6717': 6717, '[S II] 6731': 6731, 'Ca triplet': 8542,
    'TiO band': 7100, 'Na I (stellar)': 8190,
}


def identify_line(peak_obs, z):
    if pd.isna(peak_obs) or pd.isna(z) or z < -0.01:
        return 'unknown', np.nan
    rest = peak_obs / (1.0 + max(z, 0.0001))
    best_name, best_dist = None, np.inf
    for name, wave in KNOWN_LINES.items():
        d = abs(rest - wave)
        if d < best_dist:
            best_dist = d
            best_name = name
    return (best_name, rest) if best_dist < 80 else (f'unmatched ({rest:.0f}A)', rest)


def load_data():
    print("[1/6] Loading data...")
    with open(CROSSMATCH_FILE) as f:
        crossmatch = json.load(f)
    uncataloged_ids = {o['targetid'] for o in crossmatch
                       if not o['simbad']['found'] and not o['ned']['found']}
    print(f"       {len(uncataloged_ids)} uncataloged IDs")

    frames = []
    parquet_files = sorted(PARQUET_DIR.glob('desi_dr1_catalog_batch_*.parquet'))
    for i, pf in enumerate(parquet_files):
        df = pq.read_table(pf).to_pandas()
        max_snr = df[['median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z']].max(axis=1)
        match = df[(df['anomaly_score'] > 3.0) & (max_snr > 0.5) & df['targetid'].isin(uncataloged_ids)]
        if len(match):
            frames.append(match)
        if (i + 1) % 15 == 0:
            print(f"       {i+1}/{len(parquet_files)} files")
    result = pd.concat(frames, ignore_index=True).drop_duplicates(subset='targetid')
    print(f"       {len(result)} objects extracted")
    return result


def cluster(df):
    print("[2/6] Clustering...")
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import NearestNeighbors
    import umap
    import hdbscan

    lat_cols = [f'lat_{i:03d}' for i in range(128)]
    latent = np.nan_to_num(df[lat_cols].values, nan=0, posinf=0, neginf=0)
    latent_s = StandardScaler().fit_transform(latent)

    pca = PCA(n_components=20, random_state=42)
    lat_pca = pca.fit_transform(latent_s)
    print(f"       PCA: {pca.explained_variance_ratio_.sum():.3f} variance explained")

    emb = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.05,
                     random_state=42, n_jobs=1).fit_transform(lat_pca)
    print(f"       UMAP: {emb.shape}")

    clusterer = hdbscan.HDBSCAN(min_cluster_size=15, min_samples=3,
                                 cluster_selection_method='leaf', prediction_data=True)
    raw_labels = clusterer.fit_predict(emb)
    nc = len(set(raw_labels)) - (1 if -1 in raw_labels else 0)
    nn = (raw_labels == -1).sum()
    print(f"       HDBSCAN (leaf): {nc} clusters, {nn} noise ({nn/len(raw_labels)*100:.0f}%)")

    # kNN reassignment of noise
    noise_mask = raw_labels == -1
    labels = raw_labels.copy()
    is_core = np.ones(len(labels), dtype=bool)  # track which are core vs reassigned

    if noise_mask.sum() > 0:
        clustered_mask = ~noise_mask
        knn = NearestNeighbors(n_neighbors=1, metric='euclidean')
        knn.fit(emb[clustered_mask])
        dists, idxs = knn.kneighbors(emb[noise_mask])
        labels[noise_mask] = raw_labels[clustered_mask][idxs.flatten()]
        is_core[noise_mask] = False
        print(f"       Reassigned {noise_mask.sum()} noise points (median dist={np.median(dists):.3f})")

    print(f"       Final: {len(set(labels))} clusters, 0 noise")
    return emb, labels, is_core, pca


def characterize(df, labels, emb, is_core):
    print("[3/6] Characterizing clusters...")
    df = df.copy()
    df['cluster'] = labels
    df['umap_x'] = emb[:, 0]
    df['umap_y'] = emb[:, 1]
    df['is_core_member'] = is_core

    line_info = df.apply(lambda r: identify_line(r['peak_residual_wavelength'], r['z']), axis=1)
    df['rest_frame_line'] = [x[0] for x in line_info]
    df['rest_frame_peak'] = [x[1] for x in line_info]

    clusters = {}
    for label in sorted(set(labels)):
        sub = df[df['cluster'] == label]
        n = len(sub)
        n_core = int(sub['is_core_member'].sum())
        c = {'cluster_id': int(label), 'n_objects': n, 'n_core': n_core}

        # Redshift
        zv = sub['z'].dropna()
        for stat, fn in [('mean', 'mean'), ('median', 'median'), ('std', 'std'),
                         ('min', 'min'), ('max', 'max')]:
            c[f'z_{stat}'] = float(getattr(zv, fn)()) if len(zv) else None
        for q in [25, 75]:
            c[f'z_q{q}'] = float(zv.quantile(q/100)) if len(zv) else None

        # Score
        c['score_mean'] = float(sub['anomaly_score'].mean())
        c['score_median'] = float(sub['anomaly_score'].median())
        c['score_max'] = float(sub['anomaly_score'].max())

        # Colors
        for col in ['gr_color', 'rz_color', 'w1w2_color']:
            v = sub[col].dropna()
            for stat in ['mean', 'median', 'std']:
                c[f'{col}_{stat}'] = float(getattr(v, stat)()) if len(v) else None

        # Categorical distributions
        for col in ['spectype', 'morphtype', 'worst_band']:
            counts = sub[col].value_counts()
            c[f'{col}_dist'] = {str(k): int(v) for k, v in counts.items()}
            c[f'{col}_dom'] = str(counts.index[0]) if len(counts) else 'unknown'

        # Numeric scalars
        c['ps_frac'] = float(sub['is_point_source'].sum() / n) if n else 0
        for band in ['rB', 'rR', 'rZ']:
            v = sub[band].dropna()
            c[f'{band}_median'] = float(v.median()) if len(v) else None
        dc = sub['deltachi2'].dropna()
        c['dc2_median'] = float(dc.median()) if len(dc) else None

        # Peak residual
        pr = sub['peak_residual_wavelength'].dropna()
        c['peak_resid_mean'] = float(pr.mean()) if len(pr) else None
        c['peak_resid_std'] = float(pr.std()) if len(pr) else None

        # Rest-frame features
        rfp = sub['rest_frame_peak'].dropna()
        c['rest_peak_mean'] = float(rfp.mean()) if len(rfp) else None
        lc = sub['rest_frame_line'].value_counts()
        c['dom_line'] = str(lc.index[0]) if len(lc) else 'unknown'
        c['dom_line_frac'] = float(lc.iloc[0] / n) if len(lc) else 0
        c['top_lines'] = {str(k): int(v) for k, v in lc.head(5).items()}

        # zwarn
        c['zwarn_0_frac'] = float((sub['zwarn'] == 0).sum() / n) if n else 0
        c['zwarn_dist'] = {str(k): int(v) for k, v in sub['zwarn'].value_counts().head(5).items()}

        clusters[int(label)] = c

    return df, clusters


def assign_family(clusters, df):
    """Assign astrophysical family labels based on cluster properties."""
    print("[4/6] Assigning astrophysical families...")

    def g(c, key, default=0):
        v = c.get(key)
        return v if v is not None else default

    for cid, c in clusters.items():
        z = g(c, 'z_median')
        z25 = g(c, 'z_q25')
        z75 = g(c, 'z_q75')
        gr = g(c, 'gr_color_median')
        rz = g(c, 'rz_color_median')
        w12 = g(c, 'w1w2_color_median')
        ps = c.get('ps_frac', 0)
        spec = c.get('spectype_dom', '')
        sdist = c.get('spectype_dist', {})
        morph = c.get('morphtype_dom', '')
        dom_line = c.get('dom_line', '')
        dom_wb = c.get('worst_band_dom', '')
        score = c.get('score_median', 0)
        rB = g(c, 'rB_median')
        rR = g(c, 'rR_median')
        rZ = g(c, 'rZ_median')
        dc2 = g(c, 'dc2_median')
        zw0 = c.get('zwarn_0_frac', 0)
        n = c['n_objects']
        n_qso = sdist.get('QSO', 0)
        n_star = sdist.get('STAR', 0)
        n_gal = sdist.get('GALAXY', 0)
        rest_peak = g(c, 'rest_peak_mean')

        family = ''
        short = ''
        rat = []

        # ========= CLASSIFICATION DECISION TREE =========

        # STARS
        if spec == 'STAR' or (n_star / max(n, 1) > 0.4 and z < 0.005):
            short = 'Unusual stars'
            if gr < 0:
                family = 'Hot subluminous/WD candidates (blue stellar anomalies)'
                rat.append(f'stellar, very blue g-r={gr:.2f}')
            elif gr > 1.5:
                family = 'Cool/peculiar stellar spectra (possible carbon/M/L)'
                rat.append(f'stellar, red g-r={gr:.2f}')
            elif w12 > 0.5:
                family = 'IR-excess stars (possible circumstellar disk/symbiotic)'
                rat.append(f'stellar, W1-W2={w12:.2f}')
            else:
                family = 'Unusual stellar spectra (unclassified anomaly)'
                rat.append(f'stellar, g-r={gr:.2f}')

        # HIGH-Z QSOs (z > 2.5)
        elif (spec == 'QSO' or n_qso / max(n, 1) > 0.3) and z > 2.5:
            short = 'High-z QSOs'
            if w12 > 0.8:
                family = 'High-z reddened/obscured QSOs'
                rat.append(f'QSO z={z:.2f}, IR-bright W1-W2={w12:.2f}')
            elif gr < -0.1:
                family = 'High-z blue excess QSOs (possible BAL/unusual continuum)'
                rat.append(f'QSO z={z:.2f}, blue g-r={gr:.2f}')
            else:
                family = 'High-z QSO spectral anomalies'
                rat.append(f'QSO z={z:.2f}')

        # MID-Z QSOs (1 < z < 2.5)
        elif (spec == 'QSO' or n_qso / max(n, 1) > 0.25) and z > 1.0:
            short = 'Mid-z QSOs'
            family = 'Intermediate-z QSO anomalies (z~1-2.5)'
            rat.append(f'{n_qso}/{n} QSO, z={z:.2f}')

        # LOW-Z QSOs/AGN
        elif spec == 'QSO' or n_qso / max(n, 1) > 0.3:
            short = 'Low-z AGN'
            family = 'Low-z AGN/QSO anomalies'
            rat.append(f'{n_qso}/{n} QSO, z={z:.2f}')

        # HIGH-Z GALAXIES (z > 1.5)
        elif z > 1.5:
            short = 'High-z galaxies'
            if dom_line in ['Ly-alpha', 'C IV', 'C III]', 'N V', 'Si IV', 'He II']:
                family = f'High-z UV emission-line galaxies ({dom_line})'
                rat.append(f'z={z:.2f}, UV line {dom_line}')
            elif gr < 0.3:
                family = 'High-z blue galaxies (Lyman-break analogs)'
                rat.append(f'z={z:.2f}, blue g-r={gr:.2f}')
            elif rB > 2.0:
                family = 'High-z galaxies with UV excess'
                rat.append(f'z={z:.2f}, strong B-band residual rB={rB:.2f}')
            else:
                family = 'High-z galaxy anomalies'
                rat.append(f'z={z:.2f}')

        # IR-BRIGHT AGN CANDIDATES (any z)
        elif w12 > 0.8:
            short = 'IR-bright AGN'
            family = 'IR-bright AGN candidates (WISE color selection)'
            rat.append(f'W1-W2={w12:.2f} (AGN wedge), z={z:.2f}')

        # Z-BAND ANOMALIES
        elif dom_wb == 'Z' and rZ > 1.0:
            short = 'NIR anomaly'
            if z > 0.5:
                family = 'NIR-excess galaxies (dusty starbursts or evolved populations)'
            elif z < 0.2:
                family = 'Nearby galaxies with NIR spectral features'
            else:
                family = 'NIR-anomalous galaxies'
            rat.append(f'Z-band dominated rZ={rZ:.2f}, z={z:.2f}')

        # R-BAND ANOMALIES
        elif dom_wb == 'R' and rR > 1.0:
            short = 'Optical anomaly'
            if dom_line in ['H-alpha', '[N II]', '[S II] 6717', '[S II] 6731', '[O III] 5007']:
                family = f'Strong emission-line galaxies ({dom_line})'
                rat.append(f'R-band, line {dom_line}')
            else:
                family = 'Optical-band spectral anomalies'
                rat.append(f'R-band dominated rR={rR:.2f}')

        # RED GALAXIES (g-r > 1.0)
        elif gr > 1.0:
            short = 'Red galaxies'
            if dom_line in ['H-delta', 'H-gamma', 'Ca II K', 'Ca II H', 'Mg b']:
                family = 'Post-starburst (E+A) galaxy candidates'
                rat.append(f'red g-r={gr:.2f}, absorption: {dom_line}')
            elif dom_line in ['H-alpha', '[O III] 5007', '[N II]']:
                family = 'Red emission-line galaxies (LINER/Seyfert candidates)'
                rat.append(f'red g-r={gr:.2f}, emission: {dom_line}')
            else:
                family = 'Red anomalous galaxies (dusty/evolved/quenched)'
                rat.append(f'red g-r={gr:.2f}')

        # EXTREME UV-EXCESS (g-r < 0)
        elif gr < 0:
            short = 'Extreme UV'
            if z < 0.3:
                family = 'Extreme UV-excess nearby sources (BCD/AGN/peculiar)'
                rat.append(f'very blue g-r={gr:.2f}, z={z:.2f}')
            elif z < 1.0:
                family = 'Extreme UV-excess galaxies (strong starbursts or AGN)'
                rat.append(f'very blue g-r={gr:.2f}, z={z:.2f}')
            else:
                family = 'Extreme UV-excess mid-z sources'
                rat.append(f'very blue g-r={gr:.2f}, z={z:.2f}')

        # MODERATE BLUE (0 < g-r < 0.4)
        elif gr < 0.4:
            short = 'Blue galaxies'
            if dom_line in ['[O II]', '[O III] 5007', 'H-beta'] and z < 1.0:
                family = 'Blue emission-line galaxies (star-forming)'
                rat.append(f'g-r={gr:.2f}, emission: {dom_line}')
            elif rB > 2.0:
                family = 'Blue UV-excess galaxies (strong B-band anomaly)'
                rat.append(f'g-r={gr:.2f}, rB={rB:.2f}')
            elif z < 0.3:
                family = 'Nearby blue galaxies with spectral anomalies'
                rat.append(f'g-r={gr:.2f}, z={z:.2f}')
            elif z < 1.0:
                family = 'Blue star-forming galaxy anomalies'
                rat.append(f'g-r={gr:.2f}, z={z:.2f}')
            else:
                family = 'Blue intermediate-z galaxy anomalies'
                rat.append(f'g-r={gr:.2f}, z={z:.2f}')

        # GREEN VALLEY (0.4 < g-r < 0.8)
        elif gr < 0.8:
            short = 'Green valley'
            if dc2 < 10 and zw0 < 0.15:
                family = 'Transitional galaxies with uncertain classification'
                rat.append(f'green valley g-r={gr:.2f}, low deltachi2={dc2:.1f}')
            else:
                family = 'Green valley galaxy anomalies (transitional SF/quenching)'
                rat.append(f'g-r={gr:.2f}')

        # MODERATE RED (0.8 < g-r < 1.0)
        elif gr < 1.0:
            short = 'Moderately red'
            family = 'Moderately red galaxy anomalies'
            rat.append(f'g-r={gr:.2f}, z={z:.2f}')

        # CATCH-ALL
        else:
            short = 'Unclassified'
            family = f'Spectral anomalies ({spec}, z~{z:.1f})'
            rat.append(f'spectype={spec}, z={z:.2f}, g-r={gr:.2f}')

        # Enrichments
        if score > 8:
            rat.append(f'very high score ({score:.1f})')
        elif score > 5:
            rat.append(f'high score ({score:.1f})')
        rat.append(f'worst band: {dom_wb}')
        if dom_line and 'unmatched' not in dom_line:
            rat.append(f'spectral feature: {dom_line}')

        c['family'] = family
        c['family_short'] = short
        c['rationale'] = '; '.join(rat)

    # Summary table
    print()
    print(f"  {'ID':>4} {'N':>4} {'z':>6} {'Score':>5} {'g-r':>5} {'W12':>5}  {'Family'}")
    print(f"  {'--':>4} {'--':>4} {'--':>6} {'---':>5} {'---':>5} {'---':>5}  {'------'}")
    for cid in sorted(clusters.keys()):
        c = clusters[cid]
        tag = f'C{cid}'
        def f(v, fmt): return f'{v:{fmt}}' if v is not None else '  --'
        print(f"  {tag:>4} {c['n_objects']:>4} {f(c.get('z_median'),'.3f'):>6} "
              f"{c['score_median']:>5.1f} {f(c.get('gr_color_median'),'.2f'):>5} "
              f"{f(c.get('w1w2_color_median'),'.2f'):>5}  {c['family_short']}: {c['family'][:55]}")

    return clusters


def merge_families(clusters, df):
    """Merge clusters that got identical family labels into single families."""
    print("\n[5/6] Merging into families...")

    # Group clusters by family label
    family_groups = {}
    for cid, c in clusters.items():
        fam = c['family']
        if fam not in family_groups:
            family_groups[fam] = []
        family_groups[fam].append(cid)

    # Create family mapping: cluster_id -> family_id
    family_map = {}
    family_info = {}
    for fid, (fam, cluster_ids) in enumerate(sorted(family_groups.items(),
                                                      key=lambda x: -sum(clusters[c]['n_objects'] for c in x[1]))):
        total_n = sum(clusters[c]['n_objects'] for c in cluster_ids)
        for cid in cluster_ids:
            family_map[cid] = fid

        # Merge cluster stats for this family
        sub = df[df['cluster'].isin(cluster_ids)]

        fi = {
            'family_id': fid,
            'family': fam,
            'family_short': clusters[cluster_ids[0]]['family_short'],
            'n_objects': total_n,
            'source_clusters': cluster_ids,
            'rationale': clusters[cluster_ids[0]]['rationale'],
        }

        # Recompute stats from merged data
        zv = sub['z'].dropna()
        fi['z_median'] = float(zv.median()) if len(zv) else None
        fi['z_q25'] = float(zv.quantile(0.25)) if len(zv) else None
        fi['z_q75'] = float(zv.quantile(0.75)) if len(zv) else None
        fi['z_min'] = float(zv.min()) if len(zv) else None
        fi['z_max'] = float(zv.max()) if len(zv) else None

        fi['score_median'] = float(sub['anomaly_score'].median())
        fi['score_mean'] = float(sub['anomaly_score'].mean())
        fi['score_max'] = float(sub['anomaly_score'].max())

        for col in ['gr_color', 'rz_color', 'w1w2_color']:
            v = sub[col].dropna()
            fi[f'{col}_median'] = float(v.median()) if len(v) else None

        fi['spectype_dist'] = {str(k): int(v) for k, v in sub['spectype'].value_counts().items()}
        fi['morphtype_dist'] = {str(k): int(v) for k, v in sub['morphtype'].value_counts().items()}
        fi['worst_band_dist'] = {str(k): int(v) for k, v in sub['worst_band'].value_counts().items()}
        fi['ps_frac'] = float(sub['is_point_source'].sum() / total_n)

        for band in ['rB', 'rR', 'rZ']:
            v = sub[band].dropna()
            fi[f'{band}_median'] = float(v.median()) if len(v) else None

        fi['dc2_median'] = float(sub['deltachi2'].dropna().median()) if len(sub['deltachi2'].dropna()) else None
        fi['zwarn_0_frac'] = float((sub['zwarn'] == 0).sum() / total_n)

        # Lines
        lc = sub['rest_frame_line'].value_counts()
        fi['dom_line'] = str(lc.index[0]) if len(lc) else 'unknown'
        fi['top_lines'] = {str(k): int(v) for k, v in lc.head(5).items()}

        family_info[fid] = fi

    # Assign family_id to df
    df['family_id'] = df['cluster'].map(family_map)
    df['family'] = df['family_id'].map(lambda fid: family_info[fid]['family'])
    df['family_short'] = df['family_id'].map(lambda fid: family_info[fid]['family_short'])

    n_families = len(family_info)
    print(f"       {len(clusters)} clusters -> {n_families} families")

    # Print family summary
    print()
    print(f"  {'Fam':>4} {'N':>5} {'Clust':>6} {'z':>6} {'g-r':>5} {'W12':>5}  {'Family'}")
    print(f"  {'---':>4} {'--':>5} {'-----':>6} {'--':>6} {'---':>5} {'---':>5}  {'------'}")
    for fid in sorted(family_info.keys()):
        fi = family_info[fid]
        def f(v, fmt): return f'{v:{fmt}}' if v is not None else '  --'
        clust_str = ','.join(str(c) for c in fi['source_clusters'])
        print(f"  F{fid:>3} {fi['n_objects']:>5} {clust_str:>6} {f(fi.get('z_median'),'.3f'):>6} "
              f"{f(fi.get('gr_color_median'),'.2f'):>5} {f(fi.get('w1w2_color_median'),'.2f'):>5}  "
              f"{fi['family'][:55]}")

    return df, family_info, family_map


def create_outputs(df, clusters, family_info, family_map):
    print("\n[6/6] Generating outputs...")

    n_families = len(family_info)
    results = {
        'metadata': {
            'total_objects': int(len(df)),
            'n_clusters': len(clusters),
            'n_families': n_families,
            'method': 'PCA(128->20) -> UMAP(20->2, nn=15, md=0.05) -> HDBSCAN(leaf, mcs=15, ms=3) -> kNN noise reassign -> family merge',
            'source': 'DESI DR1 autoencoder anomalies NOT in SIMBAD or NED (3" match)',
        },
        'families': {str(fid): fi for fid, fi in family_info.items()},
        'clusters': {str(cid): c for cid, c in clusters.items()},
        'objects': []
    }

    for _, row in df.iterrows():
        cid = int(row['cluster'])
        fid = int(row['family_id'])
        obj = {
            'targetid': int(row['targetid']),
            'ra': float(row['target_ra']),
            'dec': float(row['target_dec']),
            'z': float(row['z']) if not pd.isna(row['z']) else None,
            'spectype': str(row['spectype']),
            'morphtype': str(row.get('morphtype', '')),
            'anomaly_score': float(row['anomaly_score']),
            'cluster': cid,
            'family_id': fid,
            'family': family_info[fid]['family'],
            'family_short': family_info[fid]['family_short'],
            'peak_residual_wavelength': float(row['peak_residual_wavelength']) if not pd.isna(row['peak_residual_wavelength']) else None,
            'rest_frame_line': str(row.get('rest_frame_line', '')),
            'gr_color': float(row['gr_color']) if not pd.isna(row['gr_color']) else None,
            'rz_color': float(row['rz_color']) if not pd.isna(row['rz_color']) else None,
            'w1w2_color': float(row['w1w2_color']) if not pd.isna(row['w1w2_color']) else None,
            'is_point_source': bool(row['is_point_source']),
            'worst_band': str(row['worst_band']),
            'is_core_member': bool(row['is_core_member']),
            'umap_x': float(row['umap_x']),
            'umap_y': float(row['umap_y']),
            'zwarn': int(row['zwarn']),
            'deltachi2': float(row['deltachi2']) if not pd.isna(row['deltachi2']) else None,
        }
        results['objects'].append(obj)

    with open(OUTPUT_DIR / 'taxonomy_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"       taxonomy_results.json")

    _make_plots(df, clusters, family_info, family_map)
    _make_summary(clusters, family_info, len(df))


def _make_plots(df, clusters, family_info, family_map):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    # Color palette for families
    n_fam = len(family_info)
    if n_fam <= 10:
        base = plt.cm.tab10
    elif n_fam <= 20:
        base = plt.cm.tab20
    else:
        base = plt.cm.gist_ncar

    fam_colors = {}
    for i, fid in enumerate(sorted(family_info.keys())):
        fam_colors[fid] = base(i / max(n_fam - 1, 1))

    # ---- Main figure: family clusters + spectype ----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 10))

    for fid in sorted(family_info.keys()):
        fi = family_info[fid]
        mask = df['family_id'] == fid
        sub = df[mask]
        ax1.scatter(sub['umap_x'], sub['umap_y'], c=[fam_colors[fid]],
                    s=16, alpha=0.65, edgecolors='none', zorder=2,
                    label=f"F{fid}: {fi['family_short']} (n={fi['n_objects']})")

    ax1.set_xlabel('UMAP 1', fontsize=13)
    ax1.set_ylabel('UMAP 2', fontsize=13)
    ax1.set_title('Uncataloged Anomaly Taxonomy\n1,127 DESI DR1 objects not in SIMBAD or NED', fontsize=14)
    # Smart legend placement
    leg = ax1.legend(fontsize=6.5, loc='best', framealpha=0.92, markerscale=2.0,
                     ncol=1 if n_fam <= 12 else 2)

    spec_colors = {'GALAXY': '#2196F3', 'QSO': '#FF5722', 'STAR': '#4CAF50'}
    for sp, color in spec_colors.items():
        mask = df['spectype'] == sp
        if mask.sum():
            ax2.scatter(df.loc[mask, 'umap_x'], df.loc[mask, 'umap_y'],
                        c=color, s=14, alpha=0.5, edgecolors='none',
                        label=f'{sp} (n={mask.sum()})')
    ax2.set_xlabel('UMAP 1', fontsize=13)
    ax2.set_ylabel('UMAP 2', fontsize=13)
    ax2.set_title('Colored by DESI Pipeline Spectype', fontsize=14)
    ax2.legend(fontsize=11, loc='best', framealpha=0.9)

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / 'taxonomy_umap.png', dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("       taxonomy_umap.png")

    # ---- Redshift ----
    fig2, ax3 = plt.subplots(figsize=(11, 9))
    sc = ax3.scatter(df['umap_x'], df['umap_y'], c=df['z'].clip(0, 5),
                     cmap='plasma', s=14, alpha=0.6, edgecolors='none')
    plt.colorbar(sc, ax=ax3, label='Redshift z', shrink=0.8)
    ax3.set_xlabel('UMAP 1', fontsize=13)
    ax3.set_ylabel('UMAP 2', fontsize=13)
    ax3.set_title('Uncataloged Anomalies by Redshift', fontsize=14)
    plt.tight_layout()
    fig2.savefig(OUTPUT_DIR / 'taxonomy_umap_redshift.png', dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig2)
    print("       taxonomy_umap_redshift.png")

    # ---- Score ----
    fig3, ax4 = plt.subplots(figsize=(11, 9))
    sc2 = ax4.scatter(df['umap_x'], df['umap_y'], c=df['anomaly_score'],
                      cmap='hot_r', s=14, alpha=0.6, edgecolors='none',
                      vmin=3, vmax=df['anomaly_score'].quantile(0.95))
    plt.colorbar(sc2, ax=ax4, label='Anomaly Score', shrink=0.8)
    ax4.set_xlabel('UMAP 1', fontsize=13)
    ax4.set_ylabel('UMAP 2', fontsize=13)
    ax4.set_title('Uncataloged Anomalies by Anomaly Score', fontsize=14)
    plt.tight_layout()
    fig3.savefig(OUTPUT_DIR / 'taxonomy_umap_score.png', dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig3)
    print("       taxonomy_umap_score.png")

    # ---- W1-W2 ----
    fig4, ax5 = plt.subplots(figsize=(11, 9))
    w12 = df['w1w2_color'].fillna(0).clip(-2, 3)
    sc3 = ax5.scatter(df['umap_x'], df['umap_y'], c=w12,
                      cmap='RdYlBu_r', s=14, alpha=0.6, edgecolors='none')
    plt.colorbar(sc3, ax=ax5, label='W1-W2 color', shrink=0.8)
    ax5.set_xlabel('UMAP 1', fontsize=13)
    ax5.set_ylabel('UMAP 2', fontsize=13)
    ax5.set_title('W1-W2 Color (>0.8 = AGN candidate)', fontsize=14)
    plt.tight_layout()
    fig4.savefig(OUTPUT_DIR / 'taxonomy_umap_w1w2.png', dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig4)
    print("       taxonomy_umap_w1w2.png")

    # ---- g-r color ----
    fig5, ax6 = plt.subplots(figsize=(11, 9))
    gr_vals = df['gr_color'].fillna(0).clip(-1, 3)
    sc4 = ax6.scatter(df['umap_x'], df['umap_y'], c=gr_vals,
                      cmap='coolwarm', s=14, alpha=0.6, edgecolors='none',
                      vmin=-0.5, vmax=2.0)
    plt.colorbar(sc4, ax=ax6, label='g-r color', shrink=0.8)
    ax6.set_xlabel('UMAP 1', fontsize=13)
    ax6.set_ylabel('UMAP 2', fontsize=13)
    ax6.set_title('g-r Color (blue = star-forming, red = quiescent)', fontsize=14)
    plt.tight_layout()
    fig5.savefig(OUTPUT_DIR / 'taxonomy_umap_gr.png', dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig5)
    print("       taxonomy_umap_gr.png")


def _make_summary(clusters, family_info, total):
    n_fam = len(family_info)
    L = []
    L.append('# Uncataloged Anomaly Taxonomy')
    L.append('')
    L.append(f'**Total objects classified:** {total}')
    L.append(f'**Spectral clusters found:** {len(clusters)}')
    L.append(f'**Astrophysical families:** {n_fam}')
    L.append(f'**Method:** PCA(128->20) + UMAP(20->2) + HDBSCAN(leaf) + kNN reassignment + family merge')
    L.append(f'**Source:** DESI DR1 spectral autoencoder anomalies with NO match in SIMBAD or NED (3")')
    L.append('')
    L.append('---')
    L.append('')

    # Summary table
    L.append('## Family Summary')
    L.append('')
    L.append('| ID | N | z (med) | Score | g-r | W1-W2 | Spectype | Family |')
    L.append('|----|---|---------|-------|-----|-------|----------|--------|')

    for fid in sorted(family_info.keys()):
        fi = family_info[fid]
        def f(v, fmt): return f'{v:{fmt}}' if v is not None else '--'
        dom_spec = max(fi['spectype_dist'], key=fi['spectype_dist'].get) if fi['spectype_dist'] else '--'
        L.append(f"| F{fid} | {fi['n_objects']} | {f(fi.get('z_median'),'.3f')} | "
                 f"{fi['score_median']:.1f} | {f(fi.get('gr_color_median'),'.2f')} | "
                 f"{f(fi.get('w1w2_color_median'),'.2f')} | {dom_spec} | {fi['family']} |")

    L.append('')
    L.append('---')
    L.append('')

    # Detailed profiles
    L.append('## Detailed Family Profiles')
    L.append('')

    for fid in sorted(family_info.keys()):
        fi = family_info[fid]
        L.append(f'### Family {fid}: {fi["family"]}')
        L.append('')
        L.append(f'**N = {fi["n_objects"]}** objects '
                 f'(from cluster{"s" if len(fi["source_clusters"])>1 else ""} '
                 f'{", ".join(str(c) for c in fi["source_clusters"])})')
        L.append('')

        if fi.get('rationale'):
            L.append(f'**Classification rationale:** {fi["rationale"]}')
            L.append('')

        if fi.get('z_median') is not None:
            L.append(f'- **Redshift:** median z = {fi["z_median"]:.3f}, '
                     f'IQR [{fi.get("z_q25",0):.3f}, {fi.get("z_q75",0):.3f}], '
                     f'range [{fi.get("z_min",0):.3f}, {fi.get("z_max",0):.3f}]')

        L.append(f'- **Anomaly score:** median = {fi["score_median"]:.1f}, '
                 f'mean = {fi["score_mean"]:.1f}, max = {fi["score_max"]:.1f}')

        gr = fi.get('gr_color_median')
        rz = fi.get('rz_color_median')
        w12 = fi.get('w1w2_color_median')
        if gr is not None:
            grr = f'{gr:.2f}' if gr is not None else '--'
            rzz = f'{rz:.2f}' if rz is not None else '--'
            w12s = f'{w12:.2f}' if w12 is not None else '--'
            L.append(f'- **Colors:** g-r = {grr}, r-z = {rzz}, W1-W2 = {w12s}')

        L.append(f'- **Spectype:** {fi["spectype_dist"]}')
        L.append(f'- **Morphology:** {fi["morphtype_dist"]}')
        L.append(f'- **Point source fraction:** {fi["ps_frac"]:.1%}')
        L.append(f'- **Worst band:** {fi["worst_band_dist"]}')

        rBv = fi.get('rB_median')
        rRv = fi.get('rR_median')
        rZv = fi.get('rZ_median')
        if rBv is not None:
            L.append(f'- **Band residuals (med):** rB = {rBv:.3f}, rR = {rRv:.3f}, rZ = {rZv:.3f}')

        if fi.get('dom_line') and 'unmatched' not in fi['dom_line']:
            L.append(f'- **Dominant spectral feature:** {fi["dom_line"]}')
        if fi.get('top_lines'):
            L.append(f'- **Top lines:** {fi["top_lines"]}')

        if fi.get('dc2_median') is not None:
            L.append(f'- **deltachi2 (med):** {fi["dc2_median"]:.1f}')
        L.append(f'- **Good redshift (zwarn=0):** {fi["zwarn_0_frac"]:.1%}')

        L.append('')
        L.append('---')
        L.append('')

    # Interpretation
    L.append('## Astrophysical Interpretation')
    L.append('')
    L.append('These 1,127 objects are spectral anomalies found by a 128-dimensional autoencoder ')
    L.append('trained on ~25K DESI DR1 spectra. They have NO counterpart in SIMBAD or NED within ')
    L.append('3 arcseconds -- genuinely uncataloged in major astronomical databases.')
    L.append('')
    L.append('The taxonomy uses a three-stage approach:')
    L.append('1. **Spectral clustering** via PCA + UMAP + HDBSCAN on autoencoder latent vectors')
    L.append('2. **Noise reassignment** via k-nearest-neighbor to the closest cluster')
    L.append('3. **Astrophysical labeling** using physical properties (z, colors, line IDs, morphology)')
    L.append('4. **Family merging** to combine clusters with identical physical interpretations')
    L.append('')
    L.append('### Key Findings')
    L.append('')

    for fid in sorted(family_info.keys()):
        fi = family_info[fid]
        L.append(f'- **F{fid} -- {fi["family"]}** ({fi["n_objects"]} objects): {fi["rationale"]}')
    L.append('')

    L.append('### Relevance to Bounce Cosmology')
    L.append('')
    L.append('The classified families feed into Pipeline 1 (tracer purification for f_NL):')
    L.append('')
    L.append('- High-z QSO and galaxy families provide potential tracers with distinctive ')
    L.append('  bias properties for primordial non-Gaussianity measurement')
    L.append('- UV-excess and emission-line families may include objects with unusual formation ')
    L.append('  histories sensitive to primordial conditions')
    L.append('- Family labels enable computing per-family halo bias b(z), the critical input ')
    L.append('  for improving sigma(f_NL) constraints')
    L.append('')

    with open(OUTPUT_DIR / 'taxonomy_summary.md', 'w') as f:
        f.write('\n'.join(L))
    print("       taxonomy_summary.md")


def main():
    print("=" * 70)
    print("UNCATALOGED ANOMALY TAXONOMY v3")
    print("=" * 70)
    print()
    df = load_data()
    emb, labels, is_core, pca = cluster(df)
    df, clusters = characterize(df, labels, emb, is_core)
    clusters = assign_family(clusters, df)
    df, family_info, family_map = merge_families(clusters, df)
    create_outputs(df, clusters, family_info, family_map)
    print()
    print("=" * 70)
    print("COMPLETE")
    print("=" * 70)


if __name__ == '__main__':
    main()
