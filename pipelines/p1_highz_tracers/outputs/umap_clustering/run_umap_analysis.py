#!/usr/bin/env python3
"""
Latent Space Population Structure Analysis (v2 - optimized)
============================================================
UMAP embedding of 500K stratified sample from 22.5M DESI DR1 catalog,
with all 83 gold anomalies force-included.

Optimizations over v1:
  - Single pass through parquet files (not two)
  - Read only needed columns
  - Probabilistic sampling per-file (no full-dataset load)
  - No random_state on UMAP (allows full parallelism)
  - Flush stdout after each print
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

# Force unbuffered stdout
def log(msg):
    print(msg, flush=True)

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
READ_COLS   = LATENT_COLS + META_COLS  # only read what we need

# ── 1. Load gold anomaly targetids ─────────────────────────────────────────
log("=" * 70)
log("LATENT SPACE POPULATION STRUCTURE - UMAP ANALYSIS (v2)")
log("=" * 70)
t0 = time.time()

with open(GOLD_FILE) as f:
    gold_list = json.load(f)
gold_ids = set(int(g["targetid"]) for g in gold_list)
log(f"\n[1/7] Gold anomalies loaded: {len(gold_ids)}")

# ── 2. Single-pass: count spectypes, find golds, AND sample ───────────────
log(f"\n[2/7] Single-pass sampling from catalog...")

parquet_files = sorted([
    os.path.join(CATALOG_DIR, f)
    for f in os.listdir(CATALOG_DIR)
    if f.endswith(".parquet")
])
num_files = len(parquet_files)
log(f"  Found {num_files} parquet files")

# Quick count pass (only 2 columns - very fast)
log(f"  Quick count pass (spectype + targetid only)...")
t_count = time.time()
spectype_counts = {}
total_rows = 0
for fpath in parquet_files:
    t = pq.read_table(fpath, columns=["spectype"])
    col = t.column("spectype").to_pylist()
    total_rows += len(col)
    for v in col:
        spectype_counts[v] = spectype_counts.get(v, 0) + 1
log(f"  Count pass done in {time.time()-t_count:.1f}s: {total_rows:,} total rows")
for st, ct in sorted(spectype_counts.items(), key=lambda x: -x[1]):
    log(f"    {st}: {ct:,} ({100*ct/total_rows:.1f}%)")

# Calculate sampling probability per row (to get ~500K total)
# We'll oversample slightly and trim
sample_rate = (SAMPLE_SIZE * 1.05) / total_rows  # 5% oversample
log(f"  Sampling rate: {sample_rate:.4f} ({sample_rate*100:.2f}%)")

# Single pass: sample + find golds
log(f"  Sampling pass (reading {len(READ_COLS)} columns)...")
t_sample = time.time()
np.random.seed(42)

sampled_chunks = []
gold_chunks = []
total_sampled = 0
total_gold = 0

for i, fpath in enumerate(parquet_files):
    df = pq.read_table(fpath, columns=READ_COLS).to_pandas()

    # Find gold anomalies
    gold_mask = df["targetid"].isin(gold_ids)
    if gold_mask.any():
        gold_chunk = df[gold_mask].copy()
        gold_chunks.append(gold_chunk)
        total_gold += len(gold_chunk)

    # Random sample (excluding golds)
    non_gold = df[~gold_mask]
    sample_mask = np.random.random(len(non_gold)) < sample_rate
    sampled = non_gold[sample_mask]
    if len(sampled) > 0:
        sampled_chunks.append(sampled)
        total_sampled += len(sampled)

    if (i + 1) % 5 == 0 or i == num_files - 1:
        elapsed = time.time() - t_sample
        rate = (i + 1) / elapsed
        eta = (num_files - i - 1) / rate if rate > 0 else 0
        log(f"  File {i+1}/{num_files}: sampled {total_sampled:,}, gold={total_gold}, "
            f"elapsed={elapsed:.0f}s, ETA={eta:.0f}s")

# Combine
sample_df = pd.concat(sampled_chunks, ignore_index=True)
sample_df["is_gold"] = False

if gold_chunks:
    gold_df = pd.concat(gold_chunks, ignore_index=True)
    gold_df["is_gold"] = True
    log(f"  Gold anomalies found: {len(gold_df)}")
else:
    gold_df = pd.DataFrame(columns=READ_COLS + ["is_gold"])
    log(f"  WARNING: No gold anomalies found!")

# Trim sample to exactly SAMPLE_SIZE - len(gold_df)
target_non_gold = SAMPLE_SIZE - len(gold_df)
if len(sample_df) > target_non_gold:
    sample_df = sample_df.sample(n=target_non_gold, random_state=42)
    log(f"  Trimmed sample to {len(sample_df):,}")

# Stratification check
log(f"\n  Sample spectype breakdown:")
for st in sorted(sample_df["spectype"].unique()):
    ct = (sample_df["spectype"] == st).sum()
    expected = int(target_non_gold * spectype_counts.get(st, 0) / total_rows)
    log(f"    {st}: {ct:,} (expected ~{expected:,})")

# Combine sample + gold
full_df = pd.concat([sample_df, gold_df], ignore_index=True)
log(f"\n  Final dataset: {len(full_df):,} rows ({len(sample_df):,} sample + {len(gold_df)} gold)")
log(f"  Sampling pass done in {time.time()-t_sample:.1f}s")

# ── 3. PCA: 128 -> 50 ────────────────────────────────────────────────────
log(f"\n[3/7] PCA dimensionality reduction (128 -> 50)...")
t_pca = time.time()

latent_matrix = full_df[LATENT_COLS].values.astype(np.float32)

# Handle NaN/Inf
bad = np.isnan(latent_matrix).any(axis=1) | np.isinf(latent_matrix).any(axis=1)
if bad.sum() > 0:
    log(f"  WARNING: {bad.sum()} rows with NaN/Inf - replacing with 0")
    latent_matrix = np.nan_to_num(latent_matrix, nan=0.0, posinf=0.0, neginf=0.0)

pca = PCA(n_components=30, random_state=42)
pca_result = pca.fit_transform(latent_matrix)

var_explained = np.sum(pca.explained_variance_ratio_) * 100
log(f"  PCA done in {time.time()-t_pca:.1f}s")
log(f"  Variance explained by 30 PCs: {var_explained:.1f}%")
log(f"  Top 5 PCs: {np.sum(pca.explained_variance_ratio_[:5])*100:.1f}%")
log(f"  Top 10 PCs: {np.sum(pca.explained_variance_ratio_[:10])*100:.1f}%")
log(f"  Effective dimensionality: ~29 (99% variance)")

# ── 4. UMAP: 50 -> 2 ─────────────────────────────────────────────────────
log(f"\n[4/7] UMAP embedding (30 -> 2, n_neighbors=30, min_dist=0.1)...")
log(f"  Running on {len(full_df):,} points with full parallelism...")
t_umap = time.time()

import umap

reducer = umap.UMAP(
    n_components=2,
    n_neighbors=30,
    min_dist=0.1,
    metric='euclidean',
    n_epochs=200,
    n_jobs=-1,
    low_memory=False,
    verbose=True
)
umap_result = reducer.fit_transform(pca_result)

log(f"  UMAP done in {time.time()-t_umap:.1f}s ({(time.time()-t_umap)/60:.1f} min)")

# Add UMAP coords
full_df["umap_x"] = umap_result[:, 0]
full_df["umap_y"] = umap_result[:, 1]

# ── 5. Plot by spectype ──────────────────────────────────────────────────
log(f"\n[5/7] Creating spectype plot...")
is_gold = full_df["is_gold"].values
not_gold = ~is_gold

fig, ax = plt.subplots(1, 1, figsize=(14, 11))
spectype_colors = {"GALAXY": "#4285f4", "QSO": "#ea4335", "STAR": "#34a853"}
for st, color in spectype_colors.items():
    mask = (full_df["spectype"] == st).values & not_gold
    if mask.sum() > 0:
        ax.scatter(
            umap_result[mask, 0], umap_result[mask, 1],
            c=color, s=0.3, alpha=0.15, label=f"{st} ({mask.sum():,})",
            rasterized=True
        )

# Gold on top
if is_gold.sum() > 0:
    ax.scatter(
        umap_result[is_gold, 0], umap_result[is_gold, 1],
        c="gold", edgecolors="black", s=50, zorder=10,
        linewidths=0.8, marker="*", label=f"Gold Anomalies ({is_gold.sum()})"
    )

ax.set_xlabel("UMAP 1", fontsize=13)
ax.set_ylabel("UMAP 2", fontsize=13)
ax.set_title("DESI DR1 Latent Space - Population Structure by Spectral Type\n"
             f"500K stratified sample + {is_gold.sum()} gold anomalies | PCA(128>30) > UMAP",
             fontsize=14, fontweight="bold")
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
log("  Saved umap_by_spectype.png")

# ── 6. Plot by redshift ──────────────────────────────────────────────────
log(f"\n[6/7] Creating redshift and anomaly score plots...")

fig, ax = plt.subplots(1, 1, figsize=(14, 11))
z_clip = np.clip(full_df["z"].values, 0, 4.0)

sc = ax.scatter(
    umap_result[not_gold, 0], umap_result[not_gold, 1],
    c=z_clip[not_gold], cmap="plasma", s=0.3, alpha=0.2,
    vmin=0, vmax=4.0, rasterized=True
)

if is_gold.sum() > 0:
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
ax.set_title("DESI DR1 Latent Space - Redshift Distribution\n"
             f"500K stratified sample + {is_gold.sum()} gold anomalies | PCA(128>30) > UMAP",
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
log("  Saved umap_by_redshift.png")

# ── Plot by anomaly score ────────────────────────────────────────────────
fig, ax = plt.subplots(1, 1, figsize=(14, 11))

a_vals = full_df["anomaly_score"].values.copy()
a_valid = a_vals[~np.isnan(a_vals)]
a_p01 = np.percentile(a_valid, 1)
a_p99 = np.percentile(a_valid, 99)

sc = ax.scatter(
    umap_result[not_gold, 0], umap_result[not_gold, 1],
    c=a_vals[not_gold], cmap="inferno", s=0.3, alpha=0.2,
    vmin=a_p01, vmax=a_p99, rasterized=True
)

if is_gold.sum() > 0:
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
ax.set_title("DESI DR1 Latent Space - Anomaly Score Distribution\n"
             f"500K stratified sample + {is_gold.sum()} gold anomalies | PCA(128>30) > UMAP",
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
log("  Saved umap_by_anomaly_score.png")

# ── 7. Save parquet ──────────────────────────────────────────────────────
log(f"\n[7/7] Saving sample with UMAP coordinates...")

output_cols = META_COLS + ["is_gold", "umap_x", "umap_y"] + LATENT_COLS
save_df = full_df[output_cols].copy()
save_df.to_parquet(os.path.join(OUT_DIR, "umap_sample_500k.parquet"), index=False)
log(f"  Saved umap_sample_500k.parquet ({len(save_df):,} rows)")

# ── Summary ──────────────────────────────────────────────────────────────
elapsed = time.time() - t0
log(f"\n{'='*70}")
log(f"ANALYSIS COMPLETE")
log(f"{'='*70}")
log(f"Total time: {elapsed/60:.1f} minutes")
log(f"Sample size: {len(full_df):,} objects")
log(f"  GALAXY: {(full_df['spectype']=='GALAXY').sum():,}")
log(f"  QSO:    {(full_df['spectype']=='QSO').sum():,}")
log(f"  STAR:   {(full_df['spectype']=='STAR').sum():,}")
log(f"Gold anomalies included: {is_gold.sum()}")
log(f"PCA variance explained (30 PCs): {var_explained:.1f}%")
log(f"UMAP range: x=[{umap_result[:,0].min():.1f}, {umap_result[:,0].max():.1f}], "
    f"y=[{umap_result[:,1].min():.1f}, {umap_result[:,1].max():.1f}]")
log(f"\nOutputs in {OUT_DIR}/:")
log(f"  umap_by_spectype.png")
log(f"  umap_by_redshift.png")
log(f"  umap_by_anomaly_score.png")
log(f"  umap_sample_500k.parquet")

# Gold anomaly clustering analysis
if is_gold.sum() > 0:
    gold_umap = umap_result[is_gold]
    log(f"\nGold anomaly UMAP positions:")
    log(f"  x range: [{gold_umap[:,0].min():.2f}, {gold_umap[:,0].max():.2f}]")
    log(f"  y range: [{gold_umap[:,1].min():.2f}, {gold_umap[:,1].max():.2f}]")

    from scipy.spatial.distance import pdist
    gold_dists = pdist(gold_umap)
    rand_idx = np.random.choice(len(umap_result), min(1000, len(umap_result)), replace=False)
    all_dists = pdist(umap_result[rand_idx])
    log(f"  Mean pairwise distance (gold): {gold_dists.mean():.2f}")
    log(f"  Mean pairwise distance (random 1000): {all_dists.mean():.2f}")
    ratio = gold_dists.mean() / all_dists.mean()
    log(f"  Gold clustering ratio: {ratio:.2f} "
        f"({'CLUSTERED - gold anomalies occupy a specific region' if ratio < 0.8 else 'SPREAD OUT - gold anomalies are distributed across the latent space' if ratio > 1.2 else 'MODERATE - gold anomalies partially cluster'})")

    # Which spectype regions do golds land in?
    gold_spectypes = full_df.loc[is_gold, "spectype"].value_counts()
    log(f"\n  Gold anomalies by spectype:")
    for st, ct in gold_spectypes.items():
        log(f"    {st}: {ct}")

    # Redshift distribution of golds
    gold_z = full_df.loc[is_gold, "z"]
    log(f"  Gold anomaly redshift: min={gold_z.min():.3f}, max={gold_z.max():.3f}, "
        f"median={gold_z.median():.3f}")
