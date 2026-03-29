#!/usr/bin/env python3
"""
Final HDBSCAN clustering: try eom method with min_cluster_size=200 to see if
there's an intermediate level of structure between 2 and 35 clusters.
Also generate a 4-panel diagnostic figure.
"""

import json
import time
import sys

import numpy as np
import pandas as pd
import hdbscan

OUT_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/umap_clustering"

# Load the UMAP-embedded anomalies (reload fresh, without old cluster labels)
print("Loading anomaly_umap.parquet...")
df = pd.read_parquet(f"{OUT_DIR}/anomaly_umap.parquet")
# Drop old cluster col
if "cluster" in df.columns:
    df = df.drop(columns=["cluster"])
print(f"Loaded {len(df):,} anomalies")

embedding = df[["umap_x", "umap_y"]].values

# ── Try multiple HDBSCAN settings ────────────────────────────────────────

configs = [
    {"min_cluster_size": 50, "min_samples": 10, "method": "eom", "label": "eom_50"},
    {"min_cluster_size": 200, "min_samples": 15, "method": "eom", "label": "eom_200"},
    {"min_cluster_size": 500, "min_samples": 25, "method": "eom", "label": "eom_500"},
    {"min_cluster_size": 100, "min_samples": 5, "method": "leaf", "label": "leaf_100"},
]

results = {}
for cfg in configs:
    t0 = time.time()
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=cfg["min_cluster_size"],
        min_samples=cfg["min_samples"],
        cluster_selection_method=cfg["method"],
        core_dist_n_jobs=-1,
    )
    labels = clusterer.fit_predict(embedding)
    dt = time.time() - t0

    n_cl = labels.max() + 1
    n_noise = (labels == -1).sum()
    n_in = (labels >= 0).sum()

    results[cfg["label"]] = {
        "labels": labels,
        "n_clusters": n_cl,
        "n_noise": n_noise,
        "n_clustered": n_in,
        "frac_clustered": n_in / len(df),
        "time": dt,
        "config": cfg,
    }

    print(f"{cfg['label']:>12}: {n_cl:>3} clusters, {n_in:>7,} clustered ({n_in/len(df):.1%}), {n_noise:>7,} noise, {dt:.1f}s")

sys.stdout.flush()

# ── Pick best: eom_200 should give intermediate result ────────────────────

# Use eom_50 as the primary (most physically meaningful — fewest, largest clusters)
# But show all four in the diagnostic figure
best_key = "eom_50"
best = results[best_key]
df["cluster"] = best["labels"]

n_clusters = best["n_clusters"]
n_noise = best["n_noise"]
n_clustered = best["n_clustered"]
frac_clustered = best["frac_clustered"]

print(f"\n{'='*70}")
print(f"PRIMARY RESULT: {best_key}")
print(f"{'='*70}")
print(f"Total anomalies:       {len(df):,}")
print(f"Clusters found:        {n_clusters}")
print(f"In clusters:           {n_clustered:,} ({frac_clustered:.1%})")
print(f"Noise (unclustered):   {n_noise:,} ({1-frac_clustered:.1%})")
print()

# Per-cluster stats
cluster_stats = []
print(f"{'Cluster':>8} {'Size':>8} {'Mean z':>8} {'Std z':>7} {'Mean Score':>11} {'Mean Peak WL':>13} {'Worst Band':>12}")
print("-" * 80)

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
        "top_worst_band_fraction": float(top_band_frac),
        "mean_umap_x": float(sub["umap_x"].mean()),
        "mean_umap_y": float(sub["umap_y"].mean()),
    }
    cluster_stats.append(stats)
    print(f"{cid:>8d} {mask.sum():>8,} {stats['mean_z']:>8.3f} {stats['std_z']:>7.3f} {stats['mean_anomaly_score']:>11.2f} {stats['mean_peak_wavelength']:>13.1f} {top_band:>8}({top_band_frac:.0%})")

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
sys.stdout.flush()

# ── Save parquet + JSON ───────────────────────────────────────────────────

df.to_parquet(f"{OUT_DIR}/anomaly_umap.parquet", index=False)
print(f"\nSaved anomaly_umap.parquet ({len(df):,} rows)")

summary = {
    "total_anomalies": int(len(df)),
    "n_clusters": int(n_clusters),
    "n_clustered": int(n_clustered),
    "n_noise": int(n_noise),
    "fraction_clustered": float(frac_clustered),
    "umap_params": {"n_components": 2, "n_neighbors": 30, "min_dist": 0.1, "metric": "euclidean"},
    "hdbscan_params": {"min_cluster_size": 50, "min_samples": 10, "cluster_selection_method": "eom"},
    "clusters": cluster_stats,
    "noise": noise_stats,
    "sensitivity_analysis": {
        k: {
            "n_clusters": int(v["n_clusters"]),
            "n_clustered": int(v["n_clustered"]),
            "n_noise": int(v["n_noise"]),
            "fraction_clustered": float(v["frac_clustered"]),
            "config": {ck: (int(cv) if isinstance(cv, (int, np.integer)) else cv) for ck, cv in v["config"].items()},
        }
        for k, v in results.items()
    },
}
with open(f"{OUT_DIR}/cluster_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
print("Saved cluster_summary.json")

# ── 4-panel diagnostic figure ─────────────────────────────────────────────

print("\nGenerating 4-panel diagnostic figure...")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(22, 18))

panels = [
    ("eom_50", "EOM (min_cluster_size=50)"),
    ("eom_200", "EOM (min_cluster_size=200)"),
    ("eom_500", "EOM (min_cluster_size=500)"),
    ("leaf_100", "Leaf (min_cluster_size=100)"),
]

for ax, (key, title) in zip(axes.flat, panels):
    r = results[key]
    labs = r["labels"]
    n_cl = r["n_clusters"]
    n_ns = r["n_noise"]
    n_in = r["n_clustered"]

    # Noise
    nm = labs == -1
    if nm.sum() > 0:
        ax.scatter(embedding[nm, 0], embedding[nm, 1], c="#dddddd", s=0.3, alpha=0.1, rasterized=True)

    # Clusters
    if n_cl > 0:
        cm = labs >= 0
        cmap = plt.colormaps.get_cmap("tab20")
        ax.scatter(
            embedding[cm, 0], embedding[cm, 1],
            c=labs[cm], cmap=cmap, s=0.6, alpha=0.4,
            vmin=-0.5, vmax=max(n_cl - 0.5, 0.5),
            rasterized=True,
        )

    ax.set_title(f"{title}\n{n_cl} clusters, {n_in:,} in ({n_in/len(df):.1%}), {n_ns:,} noise", fontsize=11, fontweight="bold")
    ax.set_xlabel("UMAP-1", fontsize=10)
    ax.set_ylabel("UMAP-2", fontsize=10)

fig.suptitle("DESI DR1 Anomaly Clustering: HDBSCAN Parameter Sensitivity", fontsize=15, fontweight="bold", y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{OUT_DIR}/umap_clusters_diagnostic.png", dpi=150, bbox_inches="tight")
print("Saved umap_clusters_diagnostic.png")

# ── Main publication figure (2-panel) ─────────────────────────────────────

print("Generating publication figure...")
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 10))

# Left: clusters
noise_mask = df["cluster"] == -1
if noise_mask.sum() > 0:
    ax1.scatter(df.loc[noise_mask, "umap_x"], df.loc[noise_mask, "umap_y"],
                c="#dddddd", s=0.3, alpha=0.1, rasterized=True)
if n_clusters > 0:
    cm = df["cluster"] >= 0
    cmap = plt.colormaps.get_cmap("tab20")
    sc = ax1.scatter(df.loc[cm, "umap_x"], df.loc[cm, "umap_y"],
                     c=df.loc[cm, "cluster"], cmap=cmap, s=1.0, alpha=0.5,
                     vmin=-0.5, vmax=max(n_clusters - 0.5, 0.5), rasterized=True)
    cbar = plt.colorbar(sc, ax=ax1, shrink=0.7, pad=0.02)
    cbar.set_label("Cluster ID", fontsize=12)
    if n_clusters <= 20:
        cbar.set_ticks(range(n_clusters))

for s in cluster_stats:
    ax1.annotate(
        f"C{s['cluster_id']}\n(n={s['size']:,})\nz={s['mean_z']:.2f}",
        (s["mean_umap_x"], s["mean_umap_y"]),
        fontsize=7, fontweight="bold", ha="center", va="center", color="black",
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.9),
    )

ax1.set_xlabel("UMAP-1", fontsize=13)
ax1.set_ylabel("UMAP-2", fontsize=13)
ax1.set_title(
    f"DESI DR1 Spectral Anomalies -- UMAP + HDBSCAN\n"
    f"{len(df):,} anomalies (score > 5), {n_clusters} clusters, "
    f"{frac_clustered:.1%} clustered",
    fontsize=13, fontweight="bold",
)

# Right: anomaly score
sc2 = ax2.scatter(df["umap_x"], df["umap_y"], c=df["anomaly_score"],
                  cmap="inferno", s=0.5, alpha=0.3, vmin=5,
                  vmax=df["anomaly_score"].quantile(0.99), rasterized=True)
cbar2 = plt.colorbar(sc2, ax=ax2, shrink=0.7, pad=0.02)
cbar2.set_label("Anomaly Score", fontsize=12)
ax2.set_xlabel("UMAP-1", fontsize=13)
ax2.set_ylabel("UMAP-2", fontsize=13)
ax2.set_title("Colored by Anomaly Score", fontsize=13, fontweight="bold")

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/umap_clusters.png", dpi=200, bbox_inches="tight")
print("Saved umap_clusters.png")

print(f"\nAll outputs saved to {OUT_DIR}/")
print("Done.")
