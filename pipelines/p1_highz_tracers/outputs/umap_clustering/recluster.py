#!/usr/bin/env python3
"""
Re-run HDBSCAN with tuned parameters on the already-computed UMAP embedding
to find finer subclusters within the main blob.
"""

import json
import time
import sys

import numpy as np
import pandas as pd
import hdbscan

OUT_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/umap_clustering"

# Load the UMAP-embedded anomalies
print("Loading anomaly_umap.parquet...")
df = pd.read_parquet(f"{OUT_DIR}/anomaly_umap.parquet")
print(f"Loaded {len(df):,} anomalies")

embedding = df[["umap_x", "umap_y"]].values

# ── HDBSCAN with higher min_cluster_size to break subclusters ──
# min_cluster_size=500 requires denser concentrations to form clusters
# leaf method tends to find more granular clusters than eom
min_cs = 500
min_samp = 25

print(f"\nRunning HDBSCAN (min_cluster_size={min_cs}, min_samples={min_samp}, method=leaf)...")
t0 = time.time()

clusterer = hdbscan.HDBSCAN(
    min_cluster_size=min_cs,
    min_samples=min_samp,
    cluster_selection_method="leaf",
    core_dist_n_jobs=-1,
)
labels = clusterer.fit_predict(embedding)

dt_hdb = time.time() - t0
print(f"HDBSCAN completed in {dt_hdb:.1f}s")

df["cluster"] = labels

n_clusters = labels.max() + 1
n_noise = (labels == -1).sum()
n_clustered = (labels >= 0).sum()
frac_clustered = n_clustered / len(df)

print(f"\n{'='*70}")
print(f"CLUSTERING RESULTS (min_cluster_size={min_cs}, leaf method)")
print(f"{'='*70}")
print(f"Total anomalies:       {len(df):,}")
print(f"Clusters found:        {n_clusters}")
print(f"In clusters:           {n_clustered:,} ({frac_clustered:.1%})")
print(f"Noise (unclustered):   {n_noise:,} ({1-frac_clustered:.1%})")
print()

# Per-cluster stats
cluster_stats = []
print(f"{'Cluster':>8} {'Size':>8} {'Mean z':>8} {'Std z':>7} {'Mean Score':>11} {'Mean Peak WL':>13} {'Worst Band':>12} {'Top Class':>20}")
print("-" * 102)

for cid in range(n_clusters):
    mask = df["cluster"] == cid
    sub = df[mask]
    top_class = sub["classification"].value_counts().index[0] if len(sub) > 0 else "N/A"
    top_class_frac = sub["classification"].value_counts().iloc[0] / len(sub) if len(sub) > 0 else 0
    top_band = sub["worst_band"].value_counts().index[0] if len(sub) > 0 else "N/A"
    top_band_frac = sub["worst_band"].value_counts().iloc[0] / len(sub) if len(sub) > 0 else 0

    stats = {
        "cluster_id": int(cid),
        "size": int(mask.sum()),
        "mean_z": float(sub["z"].mean()),
        "std_z": float(sub["z"].std()),
        "median_z": float(sub["z"].median()),
        "mean_anomaly_score": float(sub["anomaly_score"].mean()),
        "std_anomaly_score": float(sub["anomaly_score"].std()),
        "max_anomaly_score": float(sub["anomaly_score"].max()),
        "mean_peak_wavelength": float(sub["peak_residual_wavelength"].mean()),
        "std_peak_wavelength": float(sub["peak_residual_wavelength"].std()),
        "top_classification": top_class,
        "top_classification_fraction": float(top_class_frac),
        "classification_counts": {k: int(v) for k, v in sub["classification"].value_counts().to_dict().items()},
        "worst_band_counts": {k: int(v) for k, v in sub["worst_band"].value_counts().to_dict().items()},
        "top_worst_band": top_band,
        "mean_umap_x": float(sub["umap_x"].mean()),
        "mean_umap_y": float(sub["umap_y"].mean()),
    }
    cluster_stats.append(stats)

    print(f"{cid:>8d} {mask.sum():>8,} {stats['mean_z']:>8.3f} {stats['std_z']:>7.3f} {stats['mean_anomaly_score']:>11.2f} {stats['mean_peak_wavelength']:>13.1f} {top_band:>8}({top_band_frac:.0%}) {top_class:>16}({top_class_frac:.0%})")

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

print(f"\n{'Noise':>8} {n_noise:>8,}", end="")
if n_noise > 0:
    print(f" {noise_stats['mean_z']:>8.3f}         {noise_stats['mean_anomaly_score']:>11.2f} {noise_stats['mean_peak_wavelength']:>13.1f}")
else:
    print()

sys.stdout.flush()

# ── Save results ──────────────────────────────────────────────────────────

# Overwrite parquet with new cluster labels
df.to_parquet(f"{OUT_DIR}/anomaly_umap.parquet", index=False)
print(f"\nUpdated anomaly_umap.parquet ({len(df):,} rows)")

# Save cluster summary
summary = {
    "total_anomalies": int(len(df)),
    "n_clusters": int(n_clusters),
    "n_clustered": int(n_clustered),
    "n_noise": int(n_noise),
    "fraction_clustered": float(frac_clustered),
    "umap_params": {"n_components": 2, "n_neighbors": 30, "min_dist": 0.1, "metric": "euclidean"},
    "hdbscan_params": {"min_cluster_size": min_cs, "min_samples": min_samp, "cluster_selection_method": "leaf"},
    "hdbscan_time_seconds": float(dt_hdb),
    "clusters": cluster_stats,
    "noise": noise_stats,
}

with open(f"{OUT_DIR}/cluster_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
print(f"Updated cluster_summary.json")

# ── Scatter plot ──────────────────────────────────────────────────────────

print("\nGenerating scatter plot...")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(24, 10))

# Left panel: colored by cluster
ax = axes[0]
noise_mask = df["cluster"] == -1
if noise_mask.sum() > 0:
    ax.scatter(
        df.loc[noise_mask, "umap_x"],
        df.loc[noise_mask, "umap_y"],
        c="#dddddd",
        s=0.3,
        alpha=0.1,
        rasterized=True,
    )

if n_clusters > 0:
    cmap = plt.colormaps.get_cmap("tab20")
    clustered_mask = df["cluster"] >= 0
    sc = ax.scatter(
        df.loc[clustered_mask, "umap_x"],
        df.loc[clustered_mask, "umap_y"],
        c=df.loc[clustered_mask, "cluster"],
        cmap=cmap,
        s=0.8,
        alpha=0.4,
        vmin=-0.5,
        vmax=max(n_clusters - 0.5, 0.5),
        rasterized=True,
    )
    cbar = plt.colorbar(sc, ax=ax, shrink=0.7, pad=0.02)
    cbar.set_label("Cluster ID", fontsize=12)
    if n_clusters <= 20:
        cbar.set_ticks(range(n_clusters))

# Annotate cluster centers
for s in cluster_stats:
    ax.annotate(
        f"C{s['cluster_id']}\n({s['size']:,})",
        (s["mean_umap_x"], s["mean_umap_y"]),
        fontsize=6,
        fontweight="bold",
        ha="center",
        va="center",
        color="black",
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="gray", alpha=0.85),
    )

ax.set_xlabel("UMAP-1", fontsize=13)
ax.set_ylabel("UMAP-2", fontsize=13)
ax.set_title(
    f"DESI DR1 Anomalies -- UMAP + HDBSCAN\n"
    f"{len(df):,} anomalies, {n_clusters} clusters, "
    f"{frac_clustered:.1%} clustered, {n_noise:,} noise",
    fontsize=13,
    fontweight="bold",
)

# Right panel: colored by anomaly score
ax2 = axes[1]
sc2 = ax2.scatter(
    df["umap_x"],
    df["umap_y"],
    c=df["anomaly_score"],
    cmap="inferno",
    s=0.5,
    alpha=0.3,
    vmin=5,
    vmax=df["anomaly_score"].quantile(0.99),
    rasterized=True,
)
cbar2 = plt.colorbar(sc2, ax=ax2, shrink=0.7, pad=0.02)
cbar2.set_label("Anomaly Score", fontsize=12)
ax2.set_xlabel("UMAP-1", fontsize=13)
ax2.set_ylabel("UMAP-2", fontsize=13)
ax2.set_title("Colored by Anomaly Score", fontsize=13, fontweight="bold")

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/umap_clusters.png", dpi=200, bbox_inches="tight")
print(f"Saved umap_clusters.png")

print(f"\nAll outputs saved to {OUT_DIR}/")
print("Done.")
