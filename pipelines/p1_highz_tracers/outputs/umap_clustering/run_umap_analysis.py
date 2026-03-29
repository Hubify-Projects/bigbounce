#!/usr/bin/env python3
"""
Latent Space Population Structure Analysis
===========================================
UMAP embedding of 500K stratified sample from 22.5M DESI DR1 catalog,
with all 83 gold anomalies force-included.

Steps:
  1. Stratified random sample of 500K objects by spectype
  2. Force-include all 83 gold anomalies
  3. PCA: 128-dim latent -> 50-dim
  4. UMAP: 50-dim -> 2-dim  (n_neighbors=30, min_dist=0.1)
  5. Three plots: spectype, redshift, anomaly_score
  6. Save sample with UMAP coords to parquet
"""

import os
import sys
import json
import time
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from sklearn.decomposition import PCA
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ── paths ───────────────────────────────────────────────────────────────────
BASE = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs"
CATALOG_DIR = os.path.join(BASE, "enhanced_18M_deduped")
GOLD_FILE   = os.path.join(BASE, "gold_anomalies/gold_anomalies.json")
OUT_DIR     = os.path.join(BASE, "umap_clustering")

SAMPLE_SIZE = 500_000
LATENT_COLS = [f"lat_{i:03d}" for i in range(128)]
META_COLS   = ["targetid", "spectype", "z", "anomaly_score",
               "target_ra", "target_dec", "classification",
               "morphtype", "subtype"]

# ── 1. Load gold anomaly targetids ─────────────────────────────────────────
print("=" * 70)
print("LATENT SPACE POPULATION STRUCTURE — UMAP ANALYSIS")
print("=" * 70)
t0 = time.time()

with open(GOLD_FILE) as f:
    gold_list = json.load(f)
gold_ids = set(int(g["targetid"]) for g in gold_list)
print(f"\n[1/6] Gold anomalies loaded: {len(gold_ids)}")

# ── 2. Stream parquet files, collect metadata for stratified sampling ──────
print(f"\n[2/6] Scanning catalog for stratified sampling...")

parquet_files = sorted([
    os.path.join(CATALOG_DIR, f)
    for f in os.listdir(CATALOG_DIR)
    if f.endswith(".parquet")
])
print(f"  Found {len(parquet_files)} parquet files")

# First pass: count by spectype and find gold rows
spectype_counts = {}
gold_rows = []
total_rows = 0

for i, fpath in enumerate(parquet_files):
    table = pq.read_table(fpath, columns=["targetid", "spectype"])
    df_meta = table.to_pandas()
    total_rows += len(df_meta)

    for st in df_meta["spectype"].unique():
        spectype_counts[st] = spectype_counts.get(st, 0) + int((df_meta["spectype"] == st).sum())

    # Check for gold anomalies in this file
    gold_mask = df_meta["targetid"].isin(gold_ids)
    if gold_mask.any():
        gold_in_file = pq.read_table(fpath, columns=LATENT_COLS + META_COLS).to_pandas()
        gold_in_file = gold_in_file[gold_in_file["targetid"].isin(gold_ids)]
        gold_rows.append(gold_in_file)

    if (i + 1) % 10 == 0:
        print(f"  Scanned {i+1}/{len(parquet_files)} files ({total_rows:,} rows)...")

print(f"  Total catalog: {total_rows:,} rows")
print(f"  Spectype distribution:")
for st, ct in sorted(spectype_counts.items(), key=lambda x: -x[1]):
    print(f"    {st}: {ct:,} ({100*ct/total_rows:.1f}%)")

# Combine gold rows
if gold_rows:
    gold_df = pd.concat(gold_rows, ignore_index=True)
    gold_df["is_gold"] = True
    print(f"  Gold anomalies found in catalog: {len(gold_df)}")
else:
    gold_df = pd.DataFrame()
    print("  WARNING: No gold anomalies found in catalog!")

# ── 3. Stratified sampling ─────────────────────────────────────────────────
print(f"\n[3/6] Stratified sampling {SAMPLE_SIZE:,} objects...")

# Calculate per-spectype quotas (proportional)
non_gold_sample_size = SAMPLE_SIZE - len(gold_df)
quotas = {}
for st, ct in spectype_counts.items():
    quotas[st] = max(1, int(round(non_gold_sample_size * ct / total_rows)))

# Adjust to hit exact target
total_quota = sum(quotas.values())
if total_quota != non_gold_sample_size:
    # Add/remove from largest group
    largest = max(quotas, key=quotas.get)
    quotas[largest] += (non_gold_sample_size - total_quota)

print(f"  Sampling quotas (excluding {len(gold_df)} gold):")
for st, q in sorted(quotas.items(), key=lambda x: -x[1]):
    print(f"    {st}: {q:,}")

# Second pass: sample rows
np.random.seed(42)
sampled_chunks = []
sampled_per_type = {st: 0 for st in quotas}

# We need to do reservoir sampling per spectype across all files
# Strategy: read all files, sample proportionally from each
rows_seen_per_type = {st: 0 for st in quotas}

for i, fpath in enumerate(parquet_files):
    table = pq.read_table(fpath, columns=LATENT_COLS + META_COLS)
    df = table.to_pandas()

    # Remove gold anomalies (they're already included)
    if len(gold_df) > 0:
        df = df[~df["targetid"].isin(gold_ids)]

    for st in df["spectype"].unique():
        if st not in quotas:
            continue
        st_df = df[df["spectype"] == st]
        rows_seen_per_type[st] += len(st_df)

        # How many more do we need?
        remaining_quota = quotas[st] - sampled_per_type[st]
        if remaining_quota <= 0:
            continue

        # Sample proportionally from this chunk
        # Estimate remaining rows of this type
        remaining_files = len(parquet_files) - i - 1
        if remaining_files > 0:
            avg_per_file = rows_seen_per_type[st] / (i + 1)
            est_remaining = avg_per_file * remaining_files
            # Take proportional share from this file
            take = max(1, int(round(remaining_quota * len(st_df) / (len(st_df) + est_remaining))))
        else:
            take = remaining_quota

        take = min(take, remaining_quota, len(st_df))
        if take > 0:
            sampled = st_df.sample(n=take, random_state=42 + i)
            sampled_chunks.append(sampled)
            sampled_per_type[st] += take

    if (i + 1) % 10 == 0:
        total_sampled = sum(sampled_per_type.values())
        print(f"  Processed {i+1}/{len(parquet_files)} files, sampled {total_sampled:,} so far...")

# Combine all samples
sample_df = pd.concat(sampled_chunks, ignore_index=True)
sample_df["is_gold"] = False

# Add gold anomalies
if len(gold_df) > 0:
    full_df = pd.concat([sample_df, gold_df], ignore_index=True)
else:
    full_df = sample_df

print(f"  Final sample size: {len(full_df):,}")
print(f"    Non-gold: {len(sample_df):,}")
print(f"    Gold: {len(gold_df):,}")
print(f"  Spectype breakdown in sample:")
for st in sorted(full_df["spectype"].unique()):
    ct = (full_df["spectype"] == st).sum()
    print(f"    {st}: {ct:,}")

# ── 4. PCA: 128 → 50 ──────────────────────────────────────────────────────
print(f"\n[4/6] PCA dimensionality reduction (128 → 50)...")
t_pca = time.time()

latent_matrix = full_df[LATENT_COLS].values.astype(np.float32)

# Handle any NaN/Inf
nan_mask = np.isnan(latent_matrix).any(axis=1) | np.isinf(latent_matrix).any(axis=1)
if nan_mask.sum() > 0:
    print(f"  WARNING: {nan_mask.sum()} rows with NaN/Inf — replacing with 0")
    latent_matrix = np.nan_to_num(latent_matrix, nan=0.0, posinf=0.0, neginf=0.0)

pca = PCA(n_components=50, random_state=42)
pca_result = pca.fit_transform(latent_matrix)

var_explained = np.sum(pca.explained_variance_ratio_) * 100
print(f"  PCA complete in {time.time()-t_pca:.1f}s")
print(f"  Variance explained by 50 PCs: {var_explained:.1f}%")
print(f"  Top 5 PCs explain: {np.sum(pca.explained_variance_ratio_[:5])*100:.1f}%")

# ── 5. UMAP: 50 → 2 ──────────────────────────────────────────────────────
print(f"\n[5/6] UMAP embedding (50 → 2, n_neighbors=30, min_dist=0.1)...")
print(f"  This will take 10-20 minutes for {len(full_df):,} points...")
t_umap = time.time()

import umap

reducer = umap.UMAP(
    n_components=2,
    n_neighbors=30,
    min_dist=0.1,
    metric='euclidean',
    random_state=42,
    verbose=True,
    n_jobs=-1,
    low_memory=True
)
umap_result = reducer.fit_transform(pca_result)

print(f"  UMAP complete in {time.time()-t_umap:.1f}s")

# Add UMAP coords to dataframe
full_df["umap_x"] = umap_result[:, 0]
full_df["umap_y"] = umap_result[:, 1]

# ── 6. Plotting ───────────────────────────────────────────────────────────
print(f"\n[6/6] Creating plots...")

# Separate gold and non-gold for plotting
is_gold = full_df["is_gold"].values
not_gold = ~is_gold

# --- Plot A: by spectype ---
fig, ax = plt.subplots(1, 1, figsize=(14, 11))
spectype_colors = {"GALAXY": "#4285f4", "QSO": "#ea4335", "STAR": "#34a853"}
for st, color in spectype_colors.items():
    mask = (full_df["spectype"] == st).values & not_gold
    ax.scatter(
        umap_result[mask, 0], umap_result[mask, 1],
        c=color, s=0.3, alpha=0.15, label=f"{st} ({mask.sum():,})",
        rasterized=True
    )

# Gold anomalies on top
ax.scatter(
    umap_result[is_gold, 0], umap_result[is_gold, 1],
    c="gold", edgecolors="black", s=50, zorder=10,
    linewidths=0.8, marker="*", label=f"Gold Anomalies ({is_gold.sum()})"
)

ax.set_xlabel("UMAP 1", fontsize=13)
ax.set_ylabel("UMAP 2", fontsize=13)
ax.set_title("DESI DR1 Latent Space — Population Structure by Spectral Type\n"
             f"500K stratified sample + {is_gold.sum()} gold anomalies | PCA(128→50) → UMAP",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=11, markerscale=3, loc="upper right")
ax.set_facecolor("#0d1117")
fig.patch.set_facecolor("#0d1117")
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")
for spine in ax.spines.values():
    spine.set_color("white")
ax.legend(fontsize=11, markerscale=3, loc="upper right",
          facecolor="#161b22", edgecolor="white", labelcolor="white")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "umap_by_spectype.png"), dpi=200, facecolor=fig.get_facecolor())
plt.close()
print("  Saved umap_by_spectype.png")

# --- Plot B: by redshift ---
fig, ax = plt.subplots(1, 1, figsize=(14, 11))

z_vals = full_df["z"].values.copy()
# Clip redshift for visualization
z_clip = np.clip(z_vals, 0, 4.0)

sc = ax.scatter(
    umap_result[not_gold, 0], umap_result[not_gold, 1],
    c=z_clip[not_gold], cmap="plasma", s=0.3, alpha=0.2,
    vmin=0, vmax=4.0, rasterized=True
)

# Gold anomalies on top
ax.scatter(
    umap_result[is_gold, 0], umap_result[is_gold, 1],
    c="lime", edgecolors="white", s=50, zorder=10,
    linewidths=0.8, marker="*", label=f"Gold Anomalies ({is_gold.sum()})"
)

cbar = plt.colorbar(sc, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label("Redshift (z)", fontsize=12, color="white")
cbar.ax.yaxis.set_tick_params(color="white")
plt.setp(cbar.ax.yaxis.get_ticklabels(), color="white")

ax.set_xlabel("UMAP 1", fontsize=13)
ax.set_ylabel("UMAP 2", fontsize=13)
ax.set_title("DESI DR1 Latent Space — Redshift Distribution\n"
             f"500K stratified sample + {is_gold.sum()} gold anomalies | PCA(128→50) → UMAP",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=11, markerscale=3, loc="upper right",
          facecolor="#161b22", edgecolor="white", labelcolor="white")
ax.set_facecolor("#0d1117")
fig.patch.set_facecolor("#0d1117")
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")
for spine in ax.spines.values():
    spine.set_color("white")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "umap_by_redshift.png"), dpi=200, facecolor=fig.get_facecolor())
plt.close()
print("  Saved umap_by_redshift.png")

# --- Plot C: by anomaly score ---
fig, ax = plt.subplots(1, 1, figsize=(14, 11))

a_vals = full_df["anomaly_score"].values.copy()
# Use log scale for anomaly scores if they span many orders of magnitude
a_range = np.nanmax(a_vals) - np.nanmin(a_vals)
a_p99 = np.nanpercentile(a_vals[~np.isnan(a_vals)], 99)
a_p01 = np.nanpercentile(a_vals[~np.isnan(a_vals)], 1)

sc = ax.scatter(
    umap_result[not_gold, 0], umap_result[not_gold, 1],
    c=a_vals[not_gold], cmap="inferno", s=0.3, alpha=0.2,
    vmin=a_p01, vmax=a_p99, rasterized=True
)

# Gold anomalies with star markers
ax.scatter(
    umap_result[is_gold, 0], umap_result[is_gold, 1],
    c="cyan", edgecolors="white", s=80, zorder=10,
    linewidths=1.0, marker="*",
    label=f"Gold Anomalies ({is_gold.sum()})"
)

cbar = plt.colorbar(sc, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label("Anomaly Score", fontsize=12, color="white")
cbar.ax.yaxis.set_tick_params(color="white")
plt.setp(cbar.ax.yaxis.get_ticklabels(), color="white")

ax.set_xlabel("UMAP 1", fontsize=13)
ax.set_ylabel("UMAP 2", fontsize=13)
ax.set_title("DESI DR1 Latent Space — Anomaly Score Distribution\n"
             f"500K stratified sample + {is_gold.sum()} gold anomalies | PCA(128→50) → UMAP",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=11, markerscale=3, loc="upper right",
          facecolor="#161b22", edgecolor="white", labelcolor="white")
ax.set_facecolor("#0d1117")
fig.patch.set_facecolor("#0d1117")
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")
for spine in ax.spines.values():
    spine.set_color("white")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "umap_by_anomaly_score.png"), dpi=200, facecolor=fig.get_facecolor())
plt.close()
print("  Saved umap_by_anomaly_score.png")

# ── 7. Save parquet ───────────────────────────────────────────────────────
print(f"\n[7] Saving sample with UMAP coordinates...")

# Save the full sample with UMAP coordinates
output_cols = META_COLS + ["is_gold", "umap_x", "umap_y"] + LATENT_COLS
save_df = full_df[output_cols].copy()
save_df.to_parquet(os.path.join(OUT_DIR, "umap_sample_500k.parquet"), index=False)
print(f"  Saved umap_sample_500k.parquet ({len(save_df):,} rows)")

# ── Summary ───────────────────────────────────────────────────────────────
elapsed = time.time() - t0
print(f"\n{'='*70}")
print(f"ANALYSIS COMPLETE")
print(f"{'='*70}")
print(f"Total time: {elapsed/60:.1f} minutes")
print(f"Sample size: {len(full_df):,} objects")
print(f"  GALAXY: {(full_df['spectype']=='GALAXY').sum():,}")
print(f"  QSO:    {(full_df['spectype']=='QSO').sum():,}")
print(f"  STAR:   {(full_df['spectype']=='STAR').sum():,}")
print(f"Gold anomalies included: {is_gold.sum()}")
print(f"PCA variance explained (50 PCs): {var_explained:.1f}%")
print(f"UMAP range: x=[{umap_result[:,0].min():.1f}, {umap_result[:,0].max():.1f}], "
      f"y=[{umap_result[:,1].min():.1f}, {umap_result[:,1].max():.1f}]")
print(f"\nOutputs in {OUT_DIR}/:")
print(f"  umap_by_spectype.png")
print(f"  umap_by_redshift.png")
print(f"  umap_by_anomaly_score.png")
print(f"  umap_sample_500k.parquet")

# Gold anomaly positions summary
if is_gold.sum() > 0:
    gold_umap = umap_result[is_gold]
    print(f"\nGold anomaly UMAP positions:")
    print(f"  x range: [{gold_umap[:,0].min():.2f}, {gold_umap[:,0].max():.2f}]")
    print(f"  y range: [{gold_umap[:,1].min():.2f}, {gold_umap[:,1].max():.2f}]")

    # Check if gold anomalies cluster together or are spread out
    from scipy.spatial.distance import pdist
    gold_dists = pdist(gold_umap)
    all_dists = pdist(umap_result[np.random.choice(len(umap_result), 1000, replace=False)])
    print(f"  Mean pairwise distance (gold): {gold_dists.mean():.2f}")
    print(f"  Mean pairwise distance (random 1000): {all_dists.mean():.2f}")
    print(f"  Gold clustering ratio: {gold_dists.mean()/all_dists.mean():.2f} "
          f"({'clustered' if gold_dists.mean() < all_dists.mean() else 'spread out'})")
