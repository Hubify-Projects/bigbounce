#!/usr/bin/env python3
"""
FW-6 Hyperparameter Stability Test for Paper 3
================================================
Addresses the deferred claim at line 274:
  "Hyperparameter stability testing across a range of n_neighbors in [15, 50]
   and min_cluster_size in [15, 100] is deferred to follow-up work."

Performs a 7x5 grid search:
  UMAP  n_neighbors    = [15, 20, 25, 30, 35, 40, 50]
  HDBSCAN min_cluster_size = [15, 25, 50, 75, 100]

Uses the DESI BigAE second-level latent embeddings (16D, 195,829 anomalies).

OPTIMIZATION: UMAP only depends on n_neighbors, so we run 7 UMAP fits (not 35),
then sweep 5 HDBSCAN min_cluster_size values over each 2D embedding.

For each (n_neighbors, min_cluster_size) pair, records:
  - Number of clusters found
  - Noise fraction
  - Largest cluster fraction
  - Jaccard similarity of top-cluster membership vs fiducial (n_neighbors=30, min_cluster_size=50)

The fiducial configuration matches what is used in the paper's DESI taxonomy.

Output: JSON results + heatmap figure.
"""

import json
import time
import os
import numpy as np

# ---------- configuration ----------
LATENT_PATH = (
    "/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/h200_results/"
    "pod_backup_20260408_full/outputs/second-level-anomalies/second_level_latents_16d.npy"
)
OUT_DIR = "/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/fw6_stability"

N_NEIGHBORS_GRID = [15, 20, 25, 30, 35, 40, 50]
MIN_CLUSTER_SIZE_GRID = [15, 25, 50, 75, 100]

# UMAP constants (matching paper fiducial)
UMAP_MIN_DIST = 0.1
UMAP_N_COMPONENTS = 2
UMAP_RANDOM_STATE = 42

# HDBSCAN constant
HDBSCAN_MIN_SAMPLES = 10

# Fiducial for Jaccard reference
FIDUCIAL_NN = 30
FIDUCIAL_MCS = 50

os.makedirs(OUT_DIR, exist_ok=True)

# ---------- load data ----------
print(f"Loading latent embeddings from {LATENT_PATH} ...")
latents = np.load(LATENT_PATH)
print(f"  Shape: {latents.shape}, dtype: {latents.dtype}")
N = latents.shape[0]

# ---------- imports ----------
import umap
import hdbscan


def jaccard(set_a, set_b):
    """Jaccard similarity between two sets."""
    if len(set_a) == 0 and len(set_b) == 0:
        return 1.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union > 0 else 0.0


# ---------- Phase 1: Run UMAP once per n_neighbors ----------
print(f"\nPhase 1: Running {len(N_NEIGHBORS_GRID)} UMAP embeddings on {N:,} objects ...")
umap_embeddings = {}  # nn -> 2D embedding array

for i, nn in enumerate(N_NEIGHBORS_GRID):
    t0 = time.time()
    print(f"  [{i+1}/{len(N_NEIGHBORS_GRID)}] UMAP n_neighbors={nn} ...", end="", flush=True)
    reducer = umap.UMAP(
        n_neighbors=nn,
        min_dist=UMAP_MIN_DIST,
        n_components=UMAP_N_COMPONENTS,
        random_state=UMAP_RANDOM_STATE,
        verbose=False,
    )
    embedding_2d = reducer.fit_transform(latents)
    elapsed = time.time() - t0
    umap_embeddings[nn] = embedding_2d
    print(f" done in {elapsed:.0f}s")

# ---------- Phase 2: Run HDBSCAN over each embedding ----------
print(f"\nPhase 2: Running {len(N_NEIGHBORS_GRID)*len(MIN_CLUSTER_SIZE_GRID)} HDBSCAN clusterings ...")

results = {}
all_labels = {}
count = 0

for nn in N_NEIGHBORS_GRID:
    emb = umap_embeddings[nn]
    for mcs in MIN_CLUSTER_SIZE_GRID:
        count += 1
        key = f"nn{nn}_mcs{mcs}"
        print(f"  [{count:2d}/35] nn={nn:2d}, mcs={mcs:3d} ...", end="", flush=True)

        t0 = time.time()
        clusterer = hdbscan.HDBSCAN(
            min_cluster_size=mcs,
            min_samples=HDBSCAN_MIN_SAMPLES,
            core_dist_n_jobs=-1,
        )
        labels = clusterer.fit_predict(emb)
        elapsed = time.time() - t0

        n_clusters = len(set(labels) - {-1})
        noise_mask = labels == -1
        noise_frac = noise_mask.sum() / len(labels)

        if n_clusters > 0:
            cluster_ids, counts = np.unique(labels[~noise_mask], return_counts=True)
            largest_frac = counts.max() / len(labels)
            largest_id = int(cluster_ids[counts.argmax()])
        else:
            largest_frac = 0.0
            largest_id = -1

        all_labels[key] = labels
        results[key] = {
            "n_neighbors": nn,
            "min_cluster_size": mcs,
            "n_clusters": n_clusters,
            "noise_fraction": round(float(noise_frac), 6),
            "largest_cluster_fraction": round(float(largest_frac), 6),
            "largest_cluster_id": largest_id,
            "hdbscan_elapsed_s": round(elapsed, 1),
        }
        print(f"  {n_clusters:2d} clusters, noise={noise_frac:.4f}, "
              f"largest={largest_frac:.3f}, {elapsed:.1f}s")

# ---------- Jaccard stability vs fiducial ----------
print("\nPhase 3: Computing Jaccard stability vs fiducial "
      f"(nn={FIDUCIAL_NN}, mcs={FIDUCIAL_MCS}) ...")

fid_key = f"nn{FIDUCIAL_NN}_mcs{FIDUCIAL_MCS}"
fid_labels = all_labels[fid_key]

fid_clusters = set(fid_labels) - {-1}
fid_largest_id = results[fid_key]["largest_cluster_id"]
fid_largest_set = set(np.where(fid_labels == fid_largest_id)[0])

# Pre-compute fiducial cluster sets
fid_cluster_sets = {}
for fc in fid_clusters:
    fid_cluster_sets[fc] = set(np.where(fid_labels == fc)[0])

for key, labels in all_labels.items():
    # Top-cluster Jaccard
    this_largest_id = results[key]["largest_cluster_id"]
    if this_largest_id >= 0:
        this_largest_set = set(np.where(labels == this_largest_id)[0])
        j_top = jaccard(fid_largest_set, this_largest_set)
    else:
        j_top = 0.0

    # Pre-compute this config's cluster sets
    this_clusters = set(labels) - {-1}
    this_cluster_sets = {}
    for tc in this_clusters:
        this_cluster_sets[tc] = set(np.where(labels == tc)[0])

    # Mean best-match Jaccard across all fiducial clusters
    j_per_fid = []
    for fc in fid_clusters:
        fc_set = fid_cluster_sets[fc]
        best_j = 0.0
        for tc in this_clusters:
            tc_set = this_cluster_sets[tc]
            best_j = max(best_j, jaccard(fc_set, tc_set))
        j_per_fid.append(best_j)

    j_mean_bestmatch = float(np.mean(j_per_fid)) if j_per_fid else 0.0

    # Non-noise Jaccard
    fid_nonnoise = set(np.where(fid_labels >= 0)[0])
    this_nonnoise = set(np.where(labels >= 0)[0])
    j_nonnoise = jaccard(fid_nonnoise, this_nonnoise)

    results[key]["jaccard_top_cluster_vs_fiducial"] = round(j_top, 6)
    results[key]["jaccard_mean_bestmatch_vs_fiducial"] = round(j_mean_bestmatch, 6)
    results[key]["jaccard_nonnoise_vs_fiducial"] = round(j_nonnoise, 6)

# ---------- pairwise Jaccard between all configs (top cluster) ----------
print("Computing pairwise top-cluster Jaccard matrix ...")
keys = sorted(results.keys())
n_configs = len(keys)
pw_jaccard = np.zeros((n_configs, n_configs))

# Pre-compute largest-cluster sets
largest_sets = {}
for k in keys:
    lid = results[k]["largest_cluster_id"]
    largest_sets[k] = set(np.where(all_labels[k] == lid)[0]) if lid >= 0 else set()

for a_idx, a_key in enumerate(keys):
    a_set = largest_sets[a_key]
    for b_idx in range(a_idx + 1, n_configs):
        b_key = keys[b_idx]
        b_set = largest_sets[b_key]
        j = jaccard(a_set, b_set)
        pw_jaccard[a_idx, b_idx] = j
        pw_jaccard[b_idx, a_idx] = j
    pw_jaccard[a_idx, a_idx] = 1.0

# Upper-triangle pairwise stats (excluding self)
pw_upper = []
for a in range(n_configs):
    for b in range(a + 1, n_configs):
        pw_upper.append(pw_jaccard[a, b])
pw_upper = np.array(pw_upper)

# ---------- summary ----------
summary = {
    "experiment": "FW-6 Hyperparameter Stability (UMAP + HDBSCAN)",
    "data_source": LATENT_PATH,
    "n_objects": int(N),
    "latent_dim": int(latents.shape[1]),
    "umap_fixed": {"min_dist": UMAP_MIN_DIST, "n_components": UMAP_N_COMPONENTS, "random_state": UMAP_RANDOM_STATE},
    "hdbscan_fixed": {"min_samples": HDBSCAN_MIN_SAMPLES},
    "grid": {
        "n_neighbors": N_NEIGHBORS_GRID,
        "min_cluster_size": MIN_CLUSTER_SIZE_GRID,
        "n_configs": n_configs,
    },
    "fiducial": {"n_neighbors": FIDUCIAL_NN, "min_cluster_size": FIDUCIAL_MCS},
    "pairwise_top_cluster_jaccard": {
        "mean": round(float(pw_upper.mean()), 6),
        "std": round(float(pw_upper.std()), 6),
        "min": round(float(pw_upper.min()), 6),
        "max": round(float(pw_upper.max()), 6),
        "median": round(float(np.median(pw_upper)), 6),
    },
    "results_per_config": results,
}

# n_clusters range
nc_vals = [r["n_clusters"] for r in results.values()]
summary["n_clusters_range"] = {"min": min(nc_vals), "max": max(nc_vals), "values": nc_vals}

# Jaccard vs fiducial summary
j_top_vals = [r["jaccard_top_cluster_vs_fiducial"] for r in results.values()]
j_mean_vals = [r["jaccard_mean_bestmatch_vs_fiducial"] for r in results.values()]
j_nn_vals = [r["jaccard_nonnoise_vs_fiducial"] for r in results.values()]
summary["jaccard_vs_fiducial_summary"] = {
    "top_cluster": {
        "mean": round(float(np.mean(j_top_vals)), 6),
        "std": round(float(np.std(j_top_vals)), 6),
        "min": round(float(np.min(j_top_vals)), 6),
        "max": round(float(np.max(j_top_vals)), 6),
    },
    "mean_bestmatch": {
        "mean": round(float(np.mean(j_mean_vals)), 6),
        "std": round(float(np.std(j_mean_vals)), 6),
        "min": round(float(np.min(j_mean_vals)), 6),
        "max": round(float(np.max(j_mean_vals)), 6),
    },
    "nonnoise": {
        "mean": round(float(np.mean(j_nn_vals)), 6),
        "std": round(float(np.std(j_nn_vals)), 6),
        "min": round(float(np.min(j_nn_vals)), 6),
        "max": round(float(np.max(j_nn_vals)), 6),
    },
}

# Stability verdict
j_mean_bm = summary["jaccard_vs_fiducial_summary"]["mean_bestmatch"]["mean"]
if j_mean_bm >= 0.7:
    verdict = "STABLE"
    verdict_detail = (
        f"Mean best-match Jaccard = {j_mean_bm:.3f} >= 0.70 threshold. "
        "Cluster assignments are robust across the tested hyperparameter range."
    )
elif j_mean_bm >= 0.5:
    verdict = "MODERATE"
    verdict_detail = (
        f"Mean best-match Jaccard = {j_mean_bm:.3f} (0.50-0.70 range). "
        "Some cluster reassignment occurs; paper should note this."
    )
else:
    verdict = "UNSTABLE"
    verdict_detail = (
        f"Mean best-match Jaccard = {j_mean_bm:.3f} < 0.50. "
        "Cluster assignments are sensitive to hyperparameters."
    )
summary["stability_verdict"] = verdict
summary["stability_detail"] = verdict_detail

# Save JSON
json_path = os.path.join(OUT_DIR, "fw6_stability_results.json")
with open(json_path, "w") as f:
    json.dump(summary, f, indent=2)
print(f"\nResults saved to {json_path}")

# ---------- heatmap figure ----------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    nn_vals = N_NEIGHBORS_GRID
    mcs_vals = MIN_CLUSTER_SIZE_GRID

    def build_grid(metric_key):
        grid = np.zeros((len(mcs_vals), len(nn_vals)))
        for i, nn in enumerate(nn_vals):
            for j, mcs in enumerate(mcs_vals):
                key = f"nn{nn}_mcs{mcs}"
                grid[j, i] = results[key][metric_key]
        return grid

    # Panel 1: n_clusters
    grid_nc = build_grid("n_clusters")
    im0 = axes[0].imshow(grid_nc, aspect="auto", cmap="viridis")
    axes[0].set_xticks(range(len(nn_vals)))
    axes[0].set_xticklabels(nn_vals)
    axes[0].set_yticks(range(len(mcs_vals)))
    axes[0].set_yticklabels(mcs_vals)
    axes[0].set_xlabel("n_neighbors")
    axes[0].set_ylabel("min_cluster_size")
    axes[0].set_title("Number of clusters")
    for i in range(len(mcs_vals)):
        for j in range(len(nn_vals)):
            axes[0].text(j, i, f"{int(grid_nc[i, j])}", ha="center", va="center",
                        color="white" if grid_nc[i, j] < grid_nc.max()*0.6 else "black", fontsize=9)
    plt.colorbar(im0, ax=axes[0], shrink=0.8)

    # Panel 2: Jaccard top-cluster vs fiducial
    grid_jt = build_grid("jaccard_top_cluster_vs_fiducial")
    im1 = axes[1].imshow(grid_jt, aspect="auto", cmap="RdYlGn", vmin=0, vmax=1)
    axes[1].set_xticks(range(len(nn_vals)))
    axes[1].set_xticklabels(nn_vals)
    axes[1].set_yticks(range(len(mcs_vals)))
    axes[1].set_yticklabels(mcs_vals)
    axes[1].set_xlabel("n_neighbors")
    axes[1].set_ylabel("min_cluster_size")
    axes[1].set_title("Jaccard (top cluster vs fiducial)")
    for i in range(len(mcs_vals)):
        for j in range(len(nn_vals)):
            axes[1].text(j, i, f"{grid_jt[i, j]:.2f}", ha="center", va="center",
                        color="black", fontsize=8)
    plt.colorbar(im1, ax=axes[1], shrink=0.8)

    # Panel 3: Jaccard mean best-match vs fiducial
    grid_jm = build_grid("jaccard_mean_bestmatch_vs_fiducial")
    im2 = axes[2].imshow(grid_jm, aspect="auto", cmap="RdYlGn", vmin=0, vmax=1)
    axes[2].set_xticks(range(len(nn_vals)))
    axes[2].set_xticklabels(nn_vals)
    axes[2].set_yticks(range(len(mcs_vals)))
    axes[2].set_yticklabels(mcs_vals)
    axes[2].set_xlabel("n_neighbors")
    axes[2].set_ylabel("min_cluster_size")
    axes[2].set_title("Jaccard (mean best-match vs fiducial)")
    for i in range(len(mcs_vals)):
        for j in range(len(nn_vals)):
            axes[2].text(j, i, f"{grid_jm[i, j]:.2f}", ha="center", va="center",
                        color="black", fontsize=8)
    plt.colorbar(im2, ax=axes[2], shrink=0.8)

    fig.suptitle(
        f"FW-6: UMAP + HDBSCAN Hyperparameter Stability ({N:,} DESI anomalies, 16D latent)\n"
        f"Verdict: {verdict} | Mean best-match Jaccard = {j_mean_bm:.3f}",
        fontsize=12, fontweight="bold"
    )
    plt.tight_layout()
    fig_path = os.path.join(OUT_DIR, "fw6_stability_heatmap.png")
    plt.savefig(fig_path, dpi=150, bbox_inches="tight")
    print(f"Heatmap saved to {fig_path}")
    plt.close()

except ImportError as e:
    print(f"matplotlib not available, skipping figure: {e}")

# ---------- print summary ----------
print("\n" + "=" * 70)
print("FW-6 HYPERPARAMETER STABILITY -- SUMMARY")
print("=" * 70)
print(f"Objects:      {N:,}")
print(f"Latent dim:   {latents.shape[1]}")
print(f"Grid:         {len(N_NEIGHBORS_GRID)} x {len(MIN_CLUSTER_SIZE_GRID)} = {n_configs} configs")
print(f"Fiducial:     n_neighbors={FIDUCIAL_NN}, min_cluster_size={FIDUCIAL_MCS}")
print(f"N clusters:   {min(nc_vals)} - {max(nc_vals)}")
print()
print("Jaccard vs fiducial (top cluster):")
s = summary["jaccard_vs_fiducial_summary"]["top_cluster"]
print(f"  mean={s['mean']:.3f}, std={s['std']:.3f}, min={s['min']:.3f}, max={s['max']:.3f}")
print()
print("Jaccard vs fiducial (mean best-match across all clusters):")
s = summary["jaccard_vs_fiducial_summary"]["mean_bestmatch"]
print(f"  mean={s['mean']:.3f}, std={s['std']:.3f}, min={s['min']:.3f}, max={s['max']:.3f}")
print()
print("Jaccard vs fiducial (non-noise membership):")
s = summary["jaccard_vs_fiducial_summary"]["nonnoise"]
print(f"  mean={s['mean']:.3f}, std={s['std']:.3f}, min={s['min']:.3f}, max={s['max']:.3f}")
print()
print(f"Pairwise top-cluster Jaccard (all {n_configs}C2 = {len(pw_upper)} pairs):")
pw = summary["pairwise_top_cluster_jaccard"]
print(f"  mean={pw['mean']:.3f}, std={pw['std']:.3f}, min={pw['min']:.3f}, max={pw['max']:.3f}")
print()
print(f"VERDICT: {verdict}")
print(f"  {verdict_detail}")
print("=" * 70)
