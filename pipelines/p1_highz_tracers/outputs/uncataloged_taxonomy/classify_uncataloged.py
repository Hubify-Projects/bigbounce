#!/usr/bin/env python3
"""
Uncataloged Object Taxonomy Pipeline
=====================================
Classifies 1,127 uncataloged DESI DR1 anomalies (not in SIMBAD or NED)
into astrophysical families using UMAP + HDBSCAN on 128-dim latent vectors.

Steps:
  1. Load cross-match results to identify uncataloged targetids
  2. Extract those objects with ALL columns from parquet catalog
  3. PCA 128->20, UMAP 20->2, HDBSCAN clustering
  4. Characterize each cluster by physical properties
  5. Assign astrophysical labels
  6. Output taxonomy JSON, UMAP plot, summary markdown
"""

import json
import os
import sys
import warnings
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from pathlib import Path

warnings.filterwarnings('ignore')

# Paths
BASE = Path('/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs')
PARQUET_DIR = BASE / 'enhanced_18M_deduped'
CROSSMATCH_FILE = BASE / 'silver_crossmatch' / 'silver_crossmatch_results.json'
OUTPUT_DIR = BASE / 'uncataloged_taxonomy'

# Known emission/absorption lines (rest-frame, Angstroms)
KNOWN_LINES = {
    'Ly-alpha': 1216,
    'N V': 1240,
    'Si IV': 1397,
    'C IV': 1549,
    'C III]': 1909,
    'Mg II': 2798,
    '[O II]': 3727,
    'Ca II K': 3934,
    'Ca II H': 3969,
    'H-delta': 4102,
    'H-gamma': 4340,
    'H-beta': 4861,
    '[O III] 4959': 4959,
    '[O III] 5007': 5007,
    'Mg b': 5175,
    'Na D': 5893,
    'H-alpha': 6563,
    '[N II]': 6584,
    '[S II]': 6717,
    'Ca triplet': 8542,
    'TiO band': 7100,
    'Na I (stellar)': 8190,
}


def step1_load_uncataloged_ids():
    """Load cross-match results and return set of uncataloged targetids."""
    print("Step 1: Loading cross-match results...")
    with open(CROSSMATCH_FILE) as f:
        crossmatch = json.load(f)

    uncataloged_ids = set()
    for obj in crossmatch:
        if not obj['simbad']['found'] and not obj['ned']['found']:
            uncataloged_ids.add(obj['targetid'])

    print(f"  Found {len(uncataloged_ids)} uncataloged objects")
    return uncataloged_ids


def step2_extract_from_parquet(uncataloged_ids):
    """Extract uncataloged objects with all columns from parquet files."""
    print("Step 2: Extracting objects from parquet catalog...")

    parquet_files = sorted(PARQUET_DIR.glob('desi_dr1_catalog_batch_*.parquet'))
    print(f"  Scanning {len(parquet_files)} parquet files...")

    frames = []
    for i, pf in enumerate(parquet_files):
        df = pq.read_table(pf).to_pandas()
        # Apply silver-level filter: anomaly_score > 3.0 AND max SNR > 0.5
        max_snr = df[['median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z']].max(axis=1)
        mask_silver = (df['anomaly_score'] > 3.0) & (max_snr > 0.5)
        silver = df[mask_silver]
        # Filter to uncataloged
        match = silver[silver['targetid'].isin(uncataloged_ids)]
        if len(match) > 0:
            frames.append(match)
        if (i + 1) % 10 == 0:
            print(f"    Processed {i+1}/{len(parquet_files)} files, found {sum(len(f) for f in frames)} objects so far")

    result = pd.concat(frames, ignore_index=True)
    result = result.drop_duplicates(subset='targetid')
    print(f"  Extracted {len(result)} uncataloged objects with {len(result.columns)} columns")
    return result


def step3_clustering(df):
    """PCA 128->20, UMAP 20->2, HDBSCAN clustering."""
    print("Step 3: Dimensionality reduction and clustering...")

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    import umap
    import hdbscan

    # Extract latent vectors
    lat_cols = [f'lat_{i:03d}' for i in range(128)]
    latent = df[lat_cols].values

    # Handle any NaN/inf
    latent = np.nan_to_num(latent, nan=0.0, posinf=0.0, neginf=0.0)

    # Standardize
    scaler = StandardScaler()
    latent_scaled = scaler.fit_transform(latent)

    # PCA 128 -> 20
    print("  PCA 128 -> 20...")
    pca = PCA(n_components=20, random_state=42)
    latent_pca = pca.fit_transform(latent_scaled)
    print(f"  PCA variance explained: {pca.explained_variance_ratio_.sum():.3f}")

    # UMAP 20 -> 2
    print("  UMAP 20 -> 2 (n_neighbors=15, min_dist=0.05)...")
    reducer = umap.UMAP(
        n_components=2,
        n_neighbors=15,
        min_dist=0.05,
        metric='euclidean',
        random_state=42,
        n_jobs=1
    )
    embedding = reducer.fit_transform(latent_pca)
    print(f"  UMAP embedding shape: {embedding.shape}")

    # HDBSCAN
    print("  HDBSCAN (min_cluster_size=20)...")
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=20,
        min_samples=5,
        cluster_selection_method='eom',
        prediction_data=True
    )
    labels = clusterer.fit_predict(embedding)

    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = (labels == -1).sum()
    print(f"  Found {n_clusters} clusters, {n_noise} noise points ({n_noise/len(labels)*100:.1f}%)")

    return embedding, labels, pca


def identify_rest_frame_line(peak_wavelength_obs, z):
    """Given observed peak wavelength and redshift, find closest rest-frame line."""
    if pd.isna(peak_wavelength_obs) or pd.isna(z) or z < 0:
        return 'unknown', np.nan
    rest_wave = peak_wavelength_obs / (1.0 + z)
    best_line = None
    best_dist = np.inf
    for name, wave in KNOWN_LINES.items():
        dist = abs(rest_wave - wave)
        if dist < best_dist:
            best_dist = dist
            best_line = name
    # Only match if within 100A rest-frame
    if best_dist < 100:
        return best_line, rest_wave
    return f'unmatched ({rest_wave:.0f}A)', rest_wave


def step4_characterize_clusters(df, labels, embedding):
    """Characterize each cluster by physical properties."""
    print("Step 4: Characterizing clusters...")

    df = df.copy()
    df['cluster'] = labels
    df['umap_x'] = embedding[:, 0]
    df['umap_y'] = embedding[:, 1]

    # Compute rest-frame peak wavelength and line ID
    rest_info = df.apply(
        lambda row: identify_rest_frame_line(row['peak_residual_wavelength'], row['z']),
        axis=1
    )
    df['rest_frame_line'] = [r[0] for r in rest_info]
    df['rest_frame_peak'] = [r[1] for r in rest_info]

    clusters_info = {}
    unique_labels = sorted(set(labels))

    for label in unique_labels:
        mask = df['cluster'] == label
        subset = df[mask]
        n = len(subset)

        info = {
            'cluster_id': int(label),
            'n_objects': n,
            'label': 'noise' if label == -1 else f'cluster_{label}',
        }

        # Redshift stats
        z_vals = subset['z'].dropna()
        info['z_mean'] = float(z_vals.mean()) if len(z_vals) > 0 else None
        info['z_median'] = float(z_vals.median()) if len(z_vals) > 0 else None
        info['z_std'] = float(z_vals.std()) if len(z_vals) > 0 else None
        info['z_min'] = float(z_vals.min()) if len(z_vals) > 0 else None
        info['z_max'] = float(z_vals.max()) if len(z_vals) > 0 else None

        # Anomaly score
        info['anomaly_score_mean'] = float(subset['anomaly_score'].mean())
        info['anomaly_score_median'] = float(subset['anomaly_score'].median())

        # Peak residual wavelength
        prw = subset['peak_residual_wavelength'].dropna()
        info['peak_residual_mean'] = float(prw.mean()) if len(prw) > 0 else None
        info['peak_residual_std'] = float(prw.std()) if len(prw) > 0 else None

        # Rest-frame peak
        rfp = subset['rest_frame_peak'].dropna()
        info['rest_frame_peak_mean'] = float(rfp.mean()) if len(rfp) > 0 else None

        # Dominant rest-frame line
        line_counts = subset['rest_frame_line'].value_counts()
        if len(line_counts) > 0:
            info['dominant_line'] = line_counts.index[0]
            info['dominant_line_fraction'] = float(line_counts.iloc[0] / n)
            info['top_3_lines'] = {str(k): int(v) for k, v in line_counts.head(3).items()}

        # Spectral type distribution
        spectype_counts = subset['spectype'].value_counts()
        info['spectype_distribution'] = {str(k): int(v) for k, v in spectype_counts.items()}
        info['dominant_spectype'] = spectype_counts.index[0] if len(spectype_counts) > 0 else 'unknown'

        # Morphology type distribution
        morphtype_counts = subset['morphtype'].value_counts()
        info['morphtype_distribution'] = {str(k): int(v) for k, v in morphtype_counts.items()}
        info['dominant_morphtype'] = morphtype_counts.index[0] if len(morphtype_counts) > 0 else 'unknown'

        # Color distributions
        for color in ['gr_color', 'rz_color', 'w1w2_color']:
            vals = subset[color].dropna()
            if len(vals) > 0:
                info[f'{color}_mean'] = float(vals.mean())
                info[f'{color}_median'] = float(vals.median())
                info[f'{color}_std'] = float(vals.std())
            else:
                info[f'{color}_mean'] = None
                info[f'{color}_median'] = None
                info[f'{color}_std'] = None

        # Worst band distribution
        wb_counts = subset['worst_band'].value_counts()
        info['worst_band_distribution'] = {str(k): int(v) for k, v in wb_counts.items()}
        info['dominant_worst_band'] = wb_counts.index[0] if len(wb_counts) > 0 else 'unknown'

        # Point source fraction
        ps = subset['is_point_source']
        info['point_source_fraction'] = float(ps.sum() / n) if n > 0 else 0

        # Band residuals
        for band in ['rB', 'rR', 'rZ']:
            vals = subset[band].dropna()
            if len(vals) > 0:
                info[f'{band}_mean'] = float(vals.mean())
                info[f'{band}_median'] = float(vals.median())

        # deltachi2
        dc2 = subset['deltachi2'].dropna()
        if len(dc2) > 0:
            info['deltachi2_mean'] = float(dc2.mean())
            info['deltachi2_median'] = float(dc2.median())

        clusters_info[int(label)] = info

    return df, clusters_info


def step5_assign_labels(clusters_info, df):
    """Assign astrophysical labels based on cluster properties."""
    print("Step 5: Assigning astrophysical labels...")

    for cid, info in clusters_info.items():
        if cid == -1:
            info['astrophysical_label'] = 'Unclustered anomalies (diverse)'
            info['label_rationale'] = 'Objects not assigned to any cluster by HDBSCAN'
            continue

        label_parts = []
        rationale_parts = []

        z_med = info.get('z_median', 0) or 0
        dom_spec = info.get('dominant_spectype', '')
        gr = info.get('gr_color_median') or 0
        rz = info.get('rz_color_median') or 0
        w1w2 = info.get('w1w2_color_median') or 0
        ps_frac = info.get('point_source_fraction', 0)
        dom_line = info.get('dominant_line', '')
        dom_wb = info.get('dominant_worst_band', '')
        score_med = info.get('anomaly_score_median', 0)
        n = info.get('n_objects', 0)
        rest_peak = info.get('rest_frame_peak_mean') or 0

        # ---- Classification logic ----

        # High-z QSOs
        if z_med > 2.5 and dom_spec == 'QSO':
            label_parts.append('High-z QSO anomalies')
            rationale_parts.append(f'median z={z_med:.2f}, dominated by QSO spectype')
            if w1w2 > 0.5:
                label_parts.append('IR-bright')
                rationale_parts.append(f'w1-w2={w1w2:.2f}')

        # Moderate-z QSOs
        elif dom_spec == 'QSO' and z_med > 1.0:
            label_parts.append('Intermediate-z QSO anomalies')
            rationale_parts.append(f'median z={z_med:.2f}, QSO spectype')

        # Low-z QSOs
        elif dom_spec == 'QSO' and z_med <= 1.0:
            label_parts.append('Low-z QSO anomalies')
            rationale_parts.append(f'median z={z_med:.2f}, QSO spectype')

        # Stellar objects
        elif dom_spec == 'STAR' or (ps_frac > 0.7 and z_med < 0.01):
            label_parts.append('Unusual stellar spectra')
            rationale_parts.append(f'point source fraction={ps_frac:.2f}, z~0')
            if gr < 0.2:
                label_parts.append('(blue/hot)')
                rationale_parts.append(f'blue g-r={gr:.2f}')
            elif gr > 1.5:
                label_parts.append('(red/cool)')
                rationale_parts.append(f'red g-r={gr:.2f}')

        # Blue excess galaxies
        elif dom_spec == 'GALAXY' and gr < 0.5:
            label_parts.append('UV-excess galaxies')
            rationale_parts.append(f'blue g-r={gr:.2f}')
            if w1w2 > 0.8:
                label_parts.append('(AGN candidates)')
                rationale_parts.append(f'IR-bright w1-w2={w1w2:.2f}')
            else:
                label_parts.append('(possible starbursts)')
                rationale_parts.append('blue colors without IR AGN signature')

        # Red galaxies
        elif dom_spec == 'GALAXY' and gr > 1.2:
            label_parts.append('Red anomalous galaxies')
            rationale_parts.append(f'red g-r={gr:.2f}')
            # Check for post-starburst (E+A) indicators
            if dom_line in ['H-delta', 'H-gamma', 'H-beta', 'Ca II K', 'Ca II H']:
                label_parts.append('(post-starburst candidates)')
                rationale_parts.append(f'dominant line: {dom_line}')
            else:
                label_parts.append('(dusty/evolved)')
                rationale_parts.append(f'dominant line: {dom_line}')

        # IR-bright AGN
        elif w1w2 > 0.8:
            label_parts.append('IR-bright AGN candidates')
            rationale_parts.append(f'w1-w2={w1w2:.2f} (AGN wedge)')

        # Generic galaxies with specific spectral features
        elif dom_spec == 'GALAXY':
            if dom_line in ['Ly-alpha', 'C IV', 'C III]', 'Mg II'] and z_med > 1.0:
                label_parts.append(f'Emission-line galaxies ({dom_line})')
                rationale_parts.append(f'z={z_med:.2f}, dominant line {dom_line}')
            elif dom_line in ['[O III] 5007', '[O III] 4959', '[O II]']:
                label_parts.append(f'Strong [OIII]/[OII] emitters')
                rationale_parts.append(f'dominant line {dom_line}, possible AGN/starburst')
            elif dom_line in ['H-alpha', 'H-beta']:
                label_parts.append(f'Balmer-line anomalous galaxies')
                rationale_parts.append(f'dominant line {dom_line}')
            elif z_med > 1.5:
                label_parts.append(f'High-z galaxy anomalies')
                rationale_parts.append(f'z={z_med:.2f}')
            elif z_med < 0.3:
                label_parts.append(f'Nearby galaxy anomalies')
                rationale_parts.append(f'z={z_med:.2f}')
            else:
                label_parts.append(f'Galaxy anomalies (z~{z_med:.1f})')
                rationale_parts.append(f'z={z_med:.2f}')

        else:
            label_parts.append(f'Unclassified anomalies ({dom_spec})')
            rationale_parts.append(f'spectype={dom_spec}, z={z_med:.2f}')

        # Add worst-band info
        if dom_wb:
            rationale_parts.append(f'anomaly dominant in {dom_wb} band')

        # Add anomaly score context
        if score_med > 8:
            rationale_parts.append(f'very high anomaly score (median={score_med:.1f})')
        elif score_med > 5:
            rationale_parts.append(f'high anomaly score (median={score_med:.1f})')

        info['astrophysical_label'] = ' '.join(label_parts)
        info['label_rationale'] = '; '.join(rationale_parts)

    # Print summary
    print("\n  Taxonomy Summary:")
    print(f"  {'Cluster':<10} {'N':>5} {'Label':<50}")
    print(f"  {'-'*10} {'-'*5} {'-'*50}")
    for cid in sorted(clusters_info.keys()):
        info = clusters_info[cid]
        cname = 'noise' if cid == -1 else f'C{cid}'
        print(f"  {cname:<10} {info['n_objects']:>5} {info['astrophysical_label'][:50]}")

    return clusters_info


def step6_create_outputs(df, clusters_info, embedding):
    """Create taxonomy JSON, UMAP plot, and summary markdown."""
    print("\nStep 6: Creating outputs...")

    # --- taxonomy_results.json ---
    results = {
        'metadata': {
            'total_uncataloged': int(len(df)),
            'n_clusters': len([c for c in clusters_info if c != -1]),
            'n_noise': int(clusters_info.get(-1, {}).get('n_objects', 0)),
            'method': 'PCA(128->20) + UMAP(20->2, n_neighbors=15, min_dist=0.05) + HDBSCAN(min_cluster_size=20)',
            'data_source': 'DESI DR1 spectral autoencoder anomalies, cross-matched against SIMBAD+NED',
        },
        'clusters': clusters_info,
        'objects': []
    }

    # Add per-object records
    for _, row in df.iterrows():
        obj = {
            'targetid': int(row['targetid']),
            'target_ra': float(row['target_ra']),
            'target_dec': float(row['target_dec']),
            'z': float(row['z']) if not pd.isna(row['z']) else None,
            'spectype': str(row['spectype']),
            'morphtype': str(row.get('morphtype', '')),
            'anomaly_score': float(row['anomaly_score']),
            'cluster': int(row['cluster']),
            'astrophysical_label': clusters_info[int(row['cluster'])]['astrophysical_label'],
            'peak_residual_wavelength': float(row['peak_residual_wavelength']) if not pd.isna(row['peak_residual_wavelength']) else None,
            'rest_frame_line': str(row.get('rest_frame_line', '')),
            'gr_color': float(row['gr_color']) if not pd.isna(row['gr_color']) else None,
            'rz_color': float(row['rz_color']) if not pd.isna(row['rz_color']) else None,
            'w1w2_color': float(row['w1w2_color']) if not pd.isna(row['w1w2_color']) else None,
            'is_point_source': bool(row['is_point_source']),
            'umap_x': float(row['umap_x']),
            'umap_y': float(row['umap_y']),
        }
        results['objects'].append(obj)

    out_json = OUTPUT_DIR / 'taxonomy_results.json'
    with open(out_json, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"  Saved {out_json}")

    # --- UMAP plot ---
    create_umap_plot(df, clusters_info)

    # --- Summary markdown ---
    create_summary_markdown(clusters_info, len(df))


def create_umap_plot(df, clusters_info):
    """Create publication-quality UMAP plot colored by astrophysical family."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch

    fig, axes = plt.subplots(1, 2, figsize=(20, 9))

    # Build color map
    cluster_ids = sorted([c for c in clusters_info.keys() if c != -1])
    n_clusters = len(cluster_ids)

    # Use a perceptually distinct colormap
    if n_clusters <= 10:
        cmap = plt.cm.tab10
    elif n_clusters <= 20:
        cmap = plt.cm.tab20
    else:
        cmap = plt.cm.gist_ncar

    color_map = {}
    for i, cid in enumerate(cluster_ids):
        color_map[cid] = cmap(i / max(n_clusters - 1, 1))
    color_map[-1] = (0.8, 0.8, 0.8, 0.3)  # noise = light gray, transparent

    # Assign colors
    colors = [color_map[c] for c in df['cluster']]

    # --- Left panel: colored by cluster ---
    ax = axes[0]
    # Plot noise first (behind)
    noise_mask = df['cluster'] == -1
    ax.scatter(df.loc[noise_mask, 'umap_x'], df.loc[noise_mask, 'umap_y'],
               c=[(0.8, 0.8, 0.8, 0.3)], s=8, zorder=1)
    # Plot clusters
    for cid in cluster_ids:
        mask = df['cluster'] == cid
        label_str = clusters_info[cid]['astrophysical_label']
        n = clusters_info[cid]['n_objects']
        ax.scatter(df.loc[mask, 'umap_x'], df.loc[mask, 'umap_y'],
                   c=[color_map[cid]], s=15, label=f'C{cid}: {label_str} (n={n})',
                   zorder=2, alpha=0.7, edgecolors='none')

    ax.set_xlabel('UMAP 1', fontsize=12)
    ax.set_ylabel('UMAP 2', fontsize=12)
    ax.set_title('Uncataloged Anomaly Taxonomy\n1,127 objects not in SIMBAD or NED', fontsize=14)
    ax.legend(fontsize=7, loc='best', framealpha=0.9, markerscale=1.5)

    # --- Right panel: colored by spectype ---
    ax2 = axes[1]
    spectype_colors = {
        'GALAXY': '#2196F3',
        'QSO': '#FF5722',
        'STAR': '#4CAF50',
    }
    for stype, color in spectype_colors.items():
        mask = df['spectype'] == stype
        if mask.sum() > 0:
            ax2.scatter(df.loc[mask, 'umap_x'], df.loc[mask, 'umap_y'],
                        c=color, s=15, label=f'{stype} (n={mask.sum()})',
                        alpha=0.5, edgecolors='none')
    # Any other spectypes
    other_mask = ~df['spectype'].isin(spectype_colors.keys())
    if other_mask.sum() > 0:
        ax2.scatter(df.loc[other_mask, 'umap_x'], df.loc[other_mask, 'umap_y'],
                    c='gray', s=15, label=f'Other (n={other_mask.sum()})',
                    alpha=0.5, edgecolors='none')

    ax2.set_xlabel('UMAP 1', fontsize=12)
    ax2.set_ylabel('UMAP 2', fontsize=12)
    ax2.set_title('Colored by DESI Pipeline Spectype', fontsize=14)
    ax2.legend(fontsize=10, loc='best', framealpha=0.9)

    plt.tight_layout()
    out_path = OUTPUT_DIR / 'taxonomy_umap.png'
    plt.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  Saved {out_path}")

    # --- Additional plot: colored by redshift ---
    fig2, ax3 = plt.subplots(1, 1, figsize=(10, 9))
    z_vals = df['z'].clip(0, 5)
    sc = ax3.scatter(df['umap_x'], df['umap_y'], c=z_vals, cmap='plasma',
                     s=12, alpha=0.6, edgecolors='none')
    plt.colorbar(sc, ax=ax3, label='Redshift z')
    ax3.set_xlabel('UMAP 1', fontsize=12)
    ax3.set_ylabel('UMAP 2', fontsize=12)
    ax3.set_title('Uncataloged Anomalies: Redshift Distribution', fontsize=14)
    plt.tight_layout()
    out_path2 = OUTPUT_DIR / 'taxonomy_umap_redshift.png'
    plt.savefig(out_path2, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  Saved {out_path2}")

    # --- Plot: colored by anomaly score ---
    fig3, ax4 = plt.subplots(1, 1, figsize=(10, 9))
    sc2 = ax4.scatter(df['umap_x'], df['umap_y'], c=df['anomaly_score'],
                      cmap='hot_r', s=12, alpha=0.6, edgecolors='none',
                      vmin=3, vmax=df['anomaly_score'].quantile(0.95))
    plt.colorbar(sc2, ax=ax4, label='Anomaly Score')
    ax4.set_xlabel('UMAP 1', fontsize=12)
    ax4.set_ylabel('UMAP 2', fontsize=12)
    ax4.set_title('Uncataloged Anomalies: Anomaly Score', fontsize=14)
    plt.tight_layout()
    out_path3 = OUTPUT_DIR / 'taxonomy_umap_score.png'
    plt.savefig(out_path3, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  Saved {out_path3}")


def create_summary_markdown(clusters_info, total_objects):
    """Create human-readable summary of each family."""
    lines = []
    lines.append('# Uncataloged Anomaly Taxonomy')
    lines.append('')
    lines.append(f'**Total uncataloged objects:** {total_objects}')
    n_clusters = len([c for c in clusters_info if c != -1])
    n_noise = clusters_info.get(-1, {}).get('n_objects', 0)
    lines.append(f'**Clusters found:** {n_clusters}')
    lines.append(f'**Unclustered (noise):** {n_noise} ({n_noise/total_objects*100:.1f}%)')
    lines.append(f'**Method:** PCA(128->20) + UMAP(n_neighbors=15, min_dist=0.05) + HDBSCAN(min_cluster_size=20)')
    lines.append('')
    lines.append('---')
    lines.append('')

    # Summary table
    lines.append('## Taxonomy Summary')
    lines.append('')
    lines.append('| Family | N | z (median) | Score (median) | Dominant Type | Label |')
    lines.append('|--------|---|-----------|---------------|---------------|-------|')

    for cid in sorted(clusters_info.keys()):
        if cid == -1:
            continue
        info = clusters_info[cid]
        z_med = f"{info['z_median']:.3f}" if info.get('z_median') is not None else '--'
        score_med = f"{info['anomaly_score_median']:.1f}"
        lines.append(
            f"| C{cid} | {info['n_objects']} | {z_med} | {score_med} | "
            f"{info['dominant_spectype']} | {info['astrophysical_label']} |"
        )

    if -1 in clusters_info:
        info = clusters_info[-1]
        z_med = f"{info['z_median']:.3f}" if info.get('z_median') is not None else '--'
        score_med = f"{info['anomaly_score_median']:.1f}"
        lines.append(
            f"| noise | {info['n_objects']} | {z_med} | {score_med} | "
            f"{info['dominant_spectype']} | {info['astrophysical_label']} |"
        )

    lines.append('')
    lines.append('---')
    lines.append('')

    # Detailed cluster descriptions
    lines.append('## Detailed Cluster Profiles')
    lines.append('')

    for cid in sorted(clusters_info.keys()):
        info = clusters_info[cid]
        cname = 'Noise (unclustered)' if cid == -1 else f'Cluster {cid}'

        lines.append(f'### {cname}: {info["astrophysical_label"]}')
        lines.append('')
        lines.append(f'**N = {info["n_objects"]}** objects')
        lines.append('')

        if info.get('label_rationale'):
            lines.append(f'**Classification rationale:** {info["label_rationale"]}')
            lines.append('')

        # Redshift
        if info.get('z_median') is not None:
            lines.append(f'**Redshift:** median z = {info["z_median"]:.3f} '
                         f'(range {info.get("z_min", 0):.3f} -- {info.get("z_max", 0):.3f}, '
                         f'std = {info.get("z_std", 0):.3f})')

        # Anomaly score
        lines.append(f'**Anomaly score:** median = {info["anomaly_score_median"]:.1f}, '
                     f'mean = {info["anomaly_score_mean"]:.1f}')

        # Colors
        if info.get('gr_color_median') is not None:
            lines.append(f'**Colors:** g-r = {info["gr_color_median"]:.2f}, '
                         f'r-z = {info.get("rz_color_median", 0):.2f}, '
                         f'W1-W2 = {info.get("w1w2_color_median", 0):.2f}')

        # Spectype
        if info.get('spectype_distribution'):
            dist_str = ', '.join(f'{k}: {v}' for k, v in info['spectype_distribution'].items())
            lines.append(f'**Spectype distribution:** {dist_str}')

        # Morphology
        if info.get('morphtype_distribution'):
            dist_str = ', '.join(f'{k}: {v}' for k, v in info['morphtype_distribution'].items())
            lines.append(f'**Morphology:** {dist_str}')

        # Point source fraction
        lines.append(f'**Point source fraction:** {info["point_source_fraction"]:.1%}')

        # Worst band
        if info.get('worst_band_distribution'):
            dist_str = ', '.join(f'{k}: {v}' for k, v in info['worst_band_distribution'].items())
            lines.append(f'**Anomaly dominant band:** {dist_str}')

        # Rest-frame line
        if info.get('dominant_line'):
            lines.append(f'**Dominant spectral feature:** {info["dominant_line"]} '
                         f'({info.get("dominant_line_fraction", 0):.0%} of cluster)')
            if info.get('top_3_lines'):
                top3_str = ', '.join(f'{k}: {v}' for k, v in info['top_3_lines'].items())
                lines.append(f'**Top 3 lines:** {top3_str}')

        # Peak residual
        if info.get('peak_residual_mean') is not None:
            lines.append(f'**Peak residual wavelength:** {info["peak_residual_mean"]:.0f} A '
                         f'(std = {info.get("peak_residual_std", 0):.0f} A)')

        # Band residuals
        for band in ['rB', 'rR', 'rZ']:
            key = f'{band}_median'
            if info.get(key) is not None:
                lines.append(f'**{band} residual (median):** {info[key]:.3f}')

        # deltachi2
        if info.get('deltachi2_median') is not None:
            lines.append(f'**deltachi2 (median):** {info["deltachi2_median"]:.1f}')

        lines.append('')
        lines.append('---')
        lines.append('')

    # Interpretation
    lines.append('## Astrophysical Interpretation')
    lines.append('')
    lines.append('These 1,127 objects are spectral anomalies detected by a 128-dimensional ')
    lines.append('autoencoder trained on ~25K DESI DR1 spectra that have NO match in SIMBAD ')
    lines.append('or NED within 3 arcsec. The clustering reveals natural groupings based on ')
    lines.append('latent-space similarity, which we interpret using physical properties ')
    lines.append('(redshift, colors, spectral type, morphology, and the spectral feature ')
    lines.append('driving the anomaly).')
    lines.append('')
    lines.append('Key findings:')
    lines.append('')

    # Auto-generate key findings
    for cid in sorted(clusters_info.keys()):
        if cid == -1:
            continue
        info = clusters_info[cid]
        lines.append(f'- **C{cid} ({info["astrophysical_label"]}):** '
                     f'{info["n_objects"]} objects at median z={info.get("z_median", 0):.3f}. '
                     f'{info.get("label_rationale", "")}')

    lines.append('')

    out_path = OUTPUT_DIR / 'taxonomy_summary.md'
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"  Saved {out_path}")


def main():
    print("=" * 70)
    print("UNCATALOGED ANOMALY TAXONOMY PIPELINE")
    print("=" * 70)
    print()

    # Step 1: Load uncataloged IDs
    uncataloged_ids = step1_load_uncataloged_ids()

    # Step 2: Extract from parquet
    df = step2_extract_from_parquet(uncataloged_ids)

    # Step 3: Clustering
    embedding, labels, pca = step3_clustering(df)

    # Step 4: Characterize clusters
    df, clusters_info = step4_characterize_clusters(df, labels, embedding)

    # Step 5: Assign astrophysical labels
    clusters_info = step5_assign_labels(clusters_info, df)

    # Step 6: Create outputs
    step6_create_outputs(df, clusters_info, embedding)

    print()
    print("=" * 70)
    print("PIPELINE COMPLETE")
    print("=" * 70)
    print(f"\nOutputs saved to: {OUTPUT_DIR}")
    print(f"  - taxonomy_results.json")
    print(f"  - taxonomy_umap.png")
    print(f"  - taxonomy_umap_redshift.png")
    print(f"  - taxonomy_umap_score.png")
    print(f"  - taxonomy_summary.md")


if __name__ == '__main__':
    main()
