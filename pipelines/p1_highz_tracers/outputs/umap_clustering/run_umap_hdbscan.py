#!/usr/bin/env python3
"""
UMAP dimensionality reduction + HDBSCAN clustering on DESI DR1 anomalies.
Reads 46 parquet files, filters anomaly_score > 5.0, runs UMAP on 128-dim
latent vectors, clusters with HDBSCAN, saves results + scatter plot.
"""

import glob
import json
import time
import sys

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

# ── Step 1: Load anomalies from all 46 parquet files ──────────────────────

DATA_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M"
OUT_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/umap_clustering"

lat_cols = [f"lat_{i:03d}" for i in range(128)]
meta_cols = ["targetid", "anomaly_score", "z", "peak_residual_wavelength", "worst_band", "classification"]
all_cols = meta_cols + lat_cols

files = sorted(glob.glob(f"{DATA_DIR}/desi_dr1_catalog_batch_*.parquet"))
print(f"Found {len(files)} parquet files")

chunks = []
for i, f in enumerate(files):
    tbl = pq.read_table(f, columns=all_cols)
    df_chunk = tbl.to_pandas()
    df_chunk = df_chunk.loc[df_chunk["anomaly_score"] > 5.0]
    chunks.append(df_chunk)
    if (i + 1) % 10 == 0 or i == len(files) - 1:
        print(f"  Loaded {i+1}/{len(files)} files, anomalies so far: {sum(len(c) for c in chunks):,}")

df = pd.concat(chunks, ignore_index=True)
print(f"\nTotal anomalies (score > 5.0): {len(df):,}")
print(f"Columns: {len(df.columns)}")
sys.stdout.flush()

# ── Step 2: Extract latent vectors ────────────────────────────────────────

X = df[lat_cols].values.astype(np.float32)
print(f"Latent matrix shape: {X.shape}")

# Handle any NaN/inf
nan_mask = np.isnan(X).any(axis=1) | np.isinf(X).any(axis=1)
if nan_mask.sum() > 0:
    print(f"WARNING: {nan_mask.sum()} rows have NaN/inf in latent vectors, removing them")
    df = df[~nan_mask].reset_index(drop=True)
    X = df[lat_cols].values.astype(np.float32)
    print(f"After cleanup: {len(df):,} anomalies, latent shape {X.shape}")

sys.stdout.flush()

# ── Step 3: UMAP ─────────────────────────────────────────────────────────

print("\nRunning UMAP (n_components=2, n_neighbors=30, min_dist=0.1)...")
t0 = time.time()

import umap

reducer = umap.UMAP(
    n_components=2,
    n_neighbors=30,
    min_dist=0.1,
    metric="euclidean",
    random_state=42,
    low_memory=True,
    verbose=True,
)
embedding = reducer.fit_transform(X)

dt_umap = time.time() - t0
print(f"UMAP completed in {dt_umap:.1f}s")
print(f"Embedding shape: {embedding.shape}")
sys.stdout.flush()

df["umap_x"] = embedding[:, 0]
df["umap_y"] = embedding[:, 1]

# ── Step 4: HDBSCAN ──────────────────────────────────────────────────────

print("\nRunning HDBSCAN (min_cluster_size=50)...")
t0 = time.time()

import hdbscan

clusterer = hdbscan.HDBSCAN(
    min_cluster_size=50,
    min_samples=10,
    cluster_selection_method="eom",
    core_dist_n_jobs=-1,
)
labels = clusterer.fit_predict(embedding)

dt_hdb = time.time() - t0
print(f"HDBSCAN completed in {dt_hdb:.1f}s")
sys.stdout.flush()

df["cluster"] = labels

# ── Step 5: Cluster statistics ────────────────────────────────────────────

n_clusters = labels.max() + 1
n_noise = (labels == -1).sum()
n_clustered = (labels >= 0).sum()
frac_clustered = n_clustered / len(df)

print(f"\n{'='*60}")
print(f"CLUSTERING RESULTS")
print(f"{'='*60}")
print(f"Total anomalies:       {len(df):,}")
print(f"Clusters found:        {n_clusters}")
print(f"In clusters:           {n_clustered:,} ({frac_clustered:.1%})")
print(f"Noise (unclustered):   {n_noise:,} ({1-frac_clustered:.1%})")
print(f"UMAP time:             {dt_umap:.1f}s")
print(f"HDBSCAN time:          {dt_hdb:.1f}s")
print()

# Per-cluster stats
cluster_stats = []
print(f"{'Cluster':>8} {'Size':>8} {'Mean z':>8} {'Mean Score':>11} {'Mean Peak WL':>13} {'Top Class':>20}")
print("-" * 75)

for cid in range(n_clusters):
    mask = df["cluster"] == cid
    sub = df[mask]
    top_class = sub["classification"].value_counts().index[0] if len(sub) > 0 else "N/A"
    top_class_frac = sub["classification"].value_counts().iloc[0] / len(sub) if len(sub) > 0 else 0

    stats = {
        "cluster_id": int(cid),
        "size": int(mask.sum()),
        "mean_z": float(sub["z"].mean()),
        "std_z": float(sub["z"].std()),
        "mean_anomaly_score": float(sub["anomaly_score"].mean()),
        "std_anomaly_score": float(sub["anomaly_score"].std()),
        "mean_peak_wavelength": float(sub["peak_residual_wavelength"].mean()),
        "std_peak_wavelength": float(sub["peak_residual_wavelength"].std()),
        "top_classification": top_class,
        "top_classification_fraction": float(top_class_frac),
        "classification_counts": sub["classification"].value_counts().to_dict(),
        "worst_band_counts": sub["worst_band"].value_counts().to_dict(),
        "mean_umap_x": float(sub["umap_x"].mean()),
        "mean_umap_y": float(sub["umap_y"].mean()),
    }
    cluster_stats.append(stats)

    print(f"{cid:>8d} {mask.sum():>8,} {stats['mean_z']:>8.3f} {stats['mean_anomaly_score']:>11.2f} {stats['mean_peak_wavelength']:>13.1f} {top_class:>20} ({top_class_frac:.0%})")

# Noise stats
noise_sub = df[df["cluster"] == -1]
noise_stats = {
    "cluster_id": -1,
    "label": "noise",
    "size": int(n_noise),
    "mean_z": float(noise_sub["z"].mean()) if n_noise > 0 else None,
    "mean_anomaly_score": float(noise_sub["anomaly_score"].mean()) if n_noise > 0 else None,
    "mean_peak_wavelength": float(noise_sub["peak_residual_wavelength"].mean()) if n_noise > 0 else None,
}

print(f"\n{'Noise':>8} {n_noise:>8,} ", end="")
if n_noise > 0:
    print(f"{noise_stats['mean_z']:>8.3f} {noise_stats['mean_anomaly_score']:>11.2f} {noise_stats['mean_peak_wavelength']:>13.1f}")
else:
    print()

sys.stdout.flush()

# ── Step 6: Save results ─────────────────────────────────────────────────

# Save full anomaly table with UMAP coords + cluster labels
out_cols = meta_cols + ["umap_x", "umap_y", "cluster"]
df[out_cols].to_parquet(f"{OUT_DIR}/anomaly_umap.parquet", index=False)
print(f"\nSaved anomaly_umap.parquet ({len(df):,} rows)")

# Save cluster summary JSON
summary = {
    "total_anomalies": int(len(df)),
    "n_clusters": int(n_clusters),
    "n_clustered": int(n_clustered),
    "n_noise": int(n_noise),
    "fraction_clustered": float(frac_clustered),
    "umap_params": {"n_components": 2, "n_neighbors": 30, "min_dist": 0.1, "metric": "euclidean"},
    "hdbscan_params": {"min_cluster_size": 50, "min_samples": 10, "cluster_selection_method": "eom"},
    "umap_time_seconds": float(dt_umap),
    "hdbscan_time_seconds": float(dt_hdb),
    "clusters": cluster_stats,
    "noise": noise_stats,
}

with open(f"{OUT_DIR}/cluster_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
print(f"Saved cluster_summary.json")
sys.stdout.flush()

# ── Step 7: Scatter plot ──────────────────────────────────────────────────

print("\nGenerating scatter plot...")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

fig, ax = plt.subplots(figsize=(14, 10))

# Plot noise points first (gray, small)
noise_mask = df["cluster"] == -1
if noise_mask.sum() > 0:
    ax.scatter(
        df.loc[noise_mask, "umap_x"],
        df.loc[noise_mask, "umap_y"],
        c="#cccccc",
        s=0.5,
        alpha=0.15,
        label=f"Noise ({n_noise:,})",
        rasterized=True,
    )

# Plot clustered points with distinct colors
if n_clusters > 0:
    cmap = plt.cm.get_cmap("tab20", max(n_clusters, 1))
    clustered_mask = df["cluster"] >= 0
    sc = ax.scatter(
        df.loc[clustered_mask, "umap_x"],
        df.loc[clustered_mask, "umap_y"],
        c=df.loc[clustered_mask, "cluster"],
        cmap=cmap,
        s=1.5,
        alpha=0.5,
        vmin=-0.5,
        vmax=n_clusters - 0.5,
        rasterized=True,
    )
    cbar = plt.colorbar(sc, ax=ax, shrink=0.7, pad=0.02)
    cbar.set_label("Cluster ID", fontsize=12)
    cbar.set_ticks(range(n_clusters))

# Annotate cluster centers
for s in cluster_stats:
    ax.annotate(
        f"C{s['cluster_id']}",
        (s["mean_umap_x"], s["mean_umap_y"]),
        fontsize=7,
        fontweight="bold",
        ha="center",
        va="center",
        color="black",
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="gray", alpha=0.8),
    )

ax.set_xlabel("UMAP-1", fontsize=13)
ax.set_ylabel("UMAP-2", fontsize=13)
ax.set_title(
    f"DESI DR1 Spectral Anomalies — UMAP + HDBSCAN\n"
    f"{len(df):,} anomalies (score > 5), {n_clusters} clusters, "
    f"{frac_clustered:.1%} clustered",
    fontsize=14,
    fontweight="bold",
)
ax.legend(loc="upper right", fontsize=10, markerscale=5)

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/umap_clusters.png", dpi=200, bbox_inches="tight")
print(f"Saved umap_clusters.png")

print(f"\nAll outputs saved to {OUT_DIR}/")
print("Done.")
