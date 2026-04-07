#!/usr/bin/env python3
"""
Deep Spectral Taxonomy — UMAP + HDBSCAN + Full Characterization
================================================================
Run deep dimensionality reduction (UMAP → 2D) on 195K anomaly latent
vectors, cluster with HDBSCAN, then characterize each cluster with:
  - Mean spectrum/feature profile
  - Redshift distribution
  - Anomaly score distribution
  - Spatial distribution (RA/Dec)
  - Cluster purity metrics

The "noise" objects (HDBSCAN cluster = -1) are the most scientifically
interesting — they don't fit ANY known anomaly population.

If real data unavailable, generates 195K synthetic 128-dim objects with
15 distinct planted populations. Computes ARI, NMI, silhouette scores.

Output: spectral-taxonomy-deep/
"""

import json
import os
import sys
import time
import warnings
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path
from scipy.spatial.distance import cdist

import torch
from torch.utils.data import DataLoader, TensorDataset

warnings.filterwarnings("ignore", category=FutureWarning)

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/spectral-taxonomy-deep"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)


# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

SEARCH_PATHS = [
    Path("/workspace/bigbounce/outputs/desi-dr1"),
    Path("/workspace/bigbounce/pipelines/h200_results/desi_dr1"),
    Path("/workspace/bigbounce/outputs/desi_anomalies"),
    Path("/workspace/bigbounce/pipelines/p3_anomaly_engine/outputs"),
    Path("/workspace/bigbounce/outputs"),
]


def load_real_data():
    """Attempt to load real anomaly latent vectors + metadata."""
    print("  Searching for anomaly data...")

    for search_path in SEARCH_PATHS:
        if not search_path.exists():
            continue
        for pattern in ["*latent*.npy", "*latent*.npz", "*embeddings*.npy"]:
            for f in sorted(search_path.glob(pattern)):
                try:
                    if f.suffix == ".npy":
                        data = np.load(f)
                    else:
                        npz = np.load(f)
                        data = npz[list(npz.keys())[0]]
                    print(f"  Found: {f} shape={data.shape}")
                    return data.astype(np.float32), str(f), None
                except Exception as e:
                    print(f"  Error: {e}")

        for pattern in ["*anomal*.csv", "*anomal*.parquet"]:
            for f in sorted(search_path.glob(pattern)):
                try:
                    df = pd.read_parquet(f) if f.suffix == ".parquet" else pd.read_csv(f, nrows=200000)
                    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
                    if len(num_cols) >= 10:
                        print(f"  Found: {f} ({len(df)} rows, {len(num_cols)} features)")
                        return df[num_cols].values.astype(np.float32), str(f), df
                except Exception:
                    continue

    return None, None, None


def generate_synthetic_data(n_objects=195000, latent_dim=128, n_populations=15):
    """Generate synthetic data with 15 distinct planted populations."""
    print(f"  Generating synthetic: {n_objects} objects, {n_populations} populations")
    np.random.seed(42)

    pop_config = [
        ("BAL_QSO", 0.12, 2.0, 2.2),
        ("type2_AGN", 0.09, 1.8, 1.0),
        ("ELG_strong", 0.10, 1.5, 0.8),
        ("ELG_weak", 0.08, 2.5, 0.5),
        ("star_forming", 0.07, 2.2, 0.3),
        ("high_z_QSO", 0.05, 1.2, 3.5),
        ("FeLoBAL", 0.03, 1.0, 1.8),
        ("DLA_absorber", 0.04, 1.5, 2.5),
        ("stellar_M", 0.06, 1.0, 0.01),
        ("stellar_WD", 0.03, 0.8, 0.02),
        ("compact_group", 0.04, 2.0, 0.15),
        ("post_starburst", 0.05, 1.8, 0.6),
        ("LINER", 0.04, 1.5, 0.1),
        ("green_valley", 0.06, 2.0, 0.4),
        ("ultra_rare", 0.02, 8.0, 2.0),  # wide scatter — hardest to cluster
    ]

    vectors = []
    labels = []
    redshifts = []
    scores = []
    ras = []
    decs = []

    remaining = n_objects
    for i, (name, frac, spread, z_center) in enumerate(pop_config):
        n_pop = int(n_objects * frac) if i < len(pop_config) - 1 else remaining
        n_pop = min(n_pop, remaining)
        remaining -= n_pop
        if n_pop <= 0:
            continue

        center = np.random.randn(latent_dim) * 4.0
        vecs = center + np.random.randn(n_pop, latent_dim).astype(np.float32) * spread
        vectors.append(vecs)
        labels.extend([name] * n_pop)
        redshifts.extend(np.abs(np.random.normal(z_center, 0.3, n_pop)).tolist())
        scores.extend(np.exp(np.random.normal(3 + spread, 1.0, n_pop)).tolist())
        # Spatial: some populations are localized
        ra_center = np.random.uniform(120, 260)
        dec_center = np.random.uniform(-10, 60)
        ra_spread = np.random.uniform(20, 80)
        dec_spread = np.random.uniform(10, 40)
        ras.extend(np.random.normal(ra_center, ra_spread, n_pop).tolist())
        decs.extend(np.random.normal(dec_center, dec_spread, n_pop).tolist())

    # Fill any remainder with background noise
    if remaining > 0:
        vecs = np.random.randn(remaining, latent_dim).astype(np.float32) * 3.0
        vectors.append(vecs)
        labels.extend(["background"] * remaining)
        redshifts.extend(np.random.uniform(0, 4, remaining).tolist())
        scores.extend(np.exp(np.random.normal(2, 1, remaining)).tolist())
        ras.extend(np.random.uniform(100, 280, remaining).tolist())
        decs.extend(np.random.uniform(-20, 80, remaining).tolist())

    all_vectors = np.vstack(vectors).astype(np.float32)
    n_total = len(all_vectors)

    metadata = pd.DataFrame({
        "object_id": [f"TAX_{i:06d}" for i in range(n_total)],
        "ra": np.clip(ras[:n_total], 0, 360),
        "dec": np.clip(decs[:n_total], -90, 90),
        "redshift": redshifts[:n_total],
        "anomaly_score": scores[:n_total],
        "true_label": labels[:n_total],
    })

    idx = np.random.permutation(n_total)
    return all_vectors[idx], metadata.iloc[idx].reset_index(drop=True)


# ═══════════════════════════════════════════════════════
# UMAP via PyTorch (parametric approximation)
# ═══════════════════════════════════════════════════════

def gpu_pca_reduce(vectors, n_components=50, device=None):
    """GPU-accelerated PCA as pre-UMAP step."""
    print(f"  PCA: {vectors.shape[1]}D → {n_components}D")
    t = torch.tensor(vectors, dtype=torch.float32, device=device)
    t = t - t.mean(dim=0)
    U, S, V = torch.pca_lowrank(t, q=n_components)
    reduced = (t @ V).cpu().numpy()
    explained = (S ** 2).cpu().numpy()
    explained_ratio = explained / explained.sum()
    print(f"  Top-5 explained variance: {explained_ratio[:5].sum():.3f}")
    return reduced, explained_ratio


def umap_embed(vectors, n_neighbors=30, min_dist=0.1, n_components=2):
    """Run UMAP embedding. Falls back to PCA+t-SNE approximation if umap not installed."""
    try:
        import umap
        print(f"  UMAP: n_neighbors={n_neighbors}, min_dist={min_dist}")
        reducer = umap.UMAP(
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            n_components=n_components,
            metric="euclidean",
            random_state=42,
            n_jobs=-1,
        )
        embedding = reducer.fit_transform(vectors)
        return embedding, "umap"
    except ImportError:
        print("  UMAP not available — using PCA+t-SNE fallback")
        from sklearn.manifold import TSNE
        # PCA to 50D first
        from sklearn.decomposition import PCA
        pca = PCA(n_components=min(50, vectors.shape[1]), random_state=42)
        reduced = pca.fit_transform(vectors)
        tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_jobs=-1)
        embedding = tsne.fit_transform(reduced)
        return embedding, "pca+tsne"


def hdbscan_cluster(embedding, min_cluster_size=500, min_samples=50):
    """Run HDBSCAN clustering. Falls back to DBSCAN if hdbscan not installed."""
    try:
        import hdbscan
        print(f"  HDBSCAN: min_cluster_size={min_cluster_size}, min_samples={min_samples}")
        clusterer = hdbscan.HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
            cluster_selection_method="eom",
            core_dist_n_jobs=-1,
        )
        labels = clusterer.fit_predict(embedding)
        probs = clusterer.probabilities_
        return labels, probs, "hdbscan"
    except ImportError:
        print("  HDBSCAN not available — using DBSCAN fallback")
        from sklearn.cluster import DBSCAN
        # Estimate eps from k-nearest neighbor distances
        from sklearn.neighbors import NearestNeighbors
        nn = NearestNeighbors(n_neighbors=min_samples)
        nn.fit(embedding)
        distances, _ = nn.kneighbors(embedding)
        eps = np.percentile(distances[:, -1], 90)
        print(f"  DBSCAN: eps={eps:.3f}, min_samples={min_samples}")
        db = DBSCAN(eps=eps, min_samples=min_samples, n_jobs=-1)
        labels = db.fit_predict(embedding)
        probs = np.ones(len(labels), dtype=np.float64)
        probs[labels == -1] = 0.0
        return labels, probs, "dbscan"


# ═══════════════════════════════════════════════════════
# Cluster Characterization
# ═══════════════════════════════════════════════════════

def characterize_clusters(vectors, embedding, labels, metadata):
    """Full characterization of each cluster."""
    unique_labels = sorted(set(labels))
    n_clusters = len([l for l in unique_labels if l >= 0])
    n_noise = int((labels == -1).sum())
    print(f"\n  Found {n_clusters} clusters + {n_noise} noise objects")

    cluster_info = []
    for cl in unique_labels:
        mask = labels == cl
        n_members = int(mask.sum())
        cl_vectors = vectors[mask]
        cl_embed = embedding[mask]

        info = {
            "cluster_id": int(cl),
            "n_members": n_members,
            "fraction": float(n_members / len(labels)),
            "is_noise": cl == -1,
            "embedding_centroid": cl_embed.mean(axis=0).tolist(),
            "embedding_spread": float(cl_embed.std()),
            "mean_feature_profile": cl_vectors.mean(axis=0).tolist()[:10],  # first 10 dims
            "feature_std": float(cl_vectors.std()),
        }

        if metadata is not None:
            cl_meta = metadata[mask]
            if "redshift" in cl_meta.columns:
                z = cl_meta["redshift"].values
                info["redshift_stats"] = {
                    "mean": float(np.mean(z)),
                    "median": float(np.median(z)),
                    "std": float(np.std(z)),
                    "min": float(np.min(z)),
                    "max": float(np.max(z)),
                }
            if "anomaly_score" in cl_meta.columns:
                s = cl_meta["anomaly_score"].values
                info["score_stats"] = {
                    "mean": float(np.mean(s)),
                    "median": float(np.median(s)),
                    "std": float(np.std(s)),
                    "p95": float(np.percentile(s, 95)),
                }
            if "ra" in cl_meta.columns and "dec" in cl_meta.columns:
                info["spatial"] = {
                    "ra_mean": float(cl_meta["ra"].mean()),
                    "ra_std": float(cl_meta["ra"].std()),
                    "dec_mean": float(cl_meta["dec"].mean()),
                    "dec_std": float(cl_meta["dec"].std()),
                }
            if "true_label" in cl_meta.columns:
                label_counts = cl_meta["true_label"].value_counts()
                info["composition"] = {
                    str(k): int(v) for k, v in label_counts.head(5).items()
                }
                info["dominant_type"] = str(label_counts.index[0])
                info["purity"] = float(label_counts.iloc[0] / n_members)

        cluster_info.append(info)

    return cluster_info


# ═══════════════════════════════════════════════════════
# Clustering Metrics
# ═══════════════════════════════════════════════════════

def compute_metrics(labels_pred, labels_true=None, embedding=None):
    """Compute clustering quality metrics."""
    from sklearn.metrics import silhouette_score

    metrics = {}

    # Silhouette (on clustered points only)
    clustered_mask = labels_pred >= 0
    if clustered_mask.sum() > 100 and len(set(labels_pred[clustered_mask])) > 1:
        # Subsample for speed
        n_sample = min(10000, clustered_mask.sum())
        idx = np.random.choice(np.where(clustered_mask)[0], n_sample, replace=False)
        metrics["silhouette_score"] = float(
            silhouette_score(embedding[idx], labels_pred[idx])
        )

    if labels_true is not None:
        from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
        metrics["ARI"] = float(adjusted_rand_score(labels_true, labels_pred))
        metrics["NMI"] = float(normalized_mutual_info_score(labels_true, labels_pred))

    metrics["n_clusters"] = int(len(set(labels_pred)) - (1 if -1 in labels_pred else 0))
    metrics["n_noise"] = int((labels_pred == -1).sum())
    metrics["noise_fraction"] = float((labels_pred == -1).sum() / len(labels_pred))

    return metrics


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("DEEP SPECTRAL TAXONOMY — UMAP + HDBSCAN + Characterization")
    print("=" * 70)
    t_start = time.time()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n  Device: {device}")

    # Load data
    print("\n[1/6] Loading data...")
    vectors, source, raw_df = load_real_data()
    metadata = None
    data_source = "real"

    if vectors is None:
        print("  No real data — generating synthetic")
        vectors, metadata = generate_synthetic_data(n_objects=195000, latent_dim=128)
        source = "synthetic"
        data_source = "synthetic"
    else:
        if vectors.shape[1] < 128:
            vectors = np.hstack([vectors, np.zeros((vectors.shape[0], 128 - vectors.shape[1]), dtype=np.float32)])
        elif vectors.shape[1] > 128:
            vectors = vectors[:, :128]
        vectors = vectors.astype(np.float32)
        if raw_df is not None:
            metadata = raw_df

    print(f"  Shape: {vectors.shape}, Source: {source}")

    # PCA pre-reduction (GPU)
    print("\n[2/6] PCA dimensionality reduction...")
    pca_vectors, explained_ratio = gpu_pca_reduce(vectors, n_components=50, device=device)

    # UMAP embedding
    print("\n[3/6] UMAP embedding → 2D...")
    t_umap = time.time()
    embedding, embed_method = umap_embed(pca_vectors, n_neighbors=30, min_dist=0.1)
    umap_time = time.time() - t_umap
    print(f"  Embedding method: {embed_method}, time: {umap_time:.1f}s")
    print(f"  Embedding range: x=[{embedding[:,0].min():.1f}, {embedding[:,0].max():.1f}], "
          f"y=[{embedding[:,1].min():.1f}, {embedding[:,1].max():.1f}]")

    # HDBSCAN clustering
    print("\n[4/6] HDBSCAN clustering...")
    t_hdb = time.time()
    cluster_labels, cluster_probs, cluster_method = hdbscan_cluster(
        embedding, min_cluster_size=500, min_samples=50
    )
    hdb_time = time.time() - t_hdb
    print(f"  Clustering method: {cluster_method}, time: {hdb_time:.1f}s")

    # Characterize clusters
    print("\n[5/6] Characterizing clusters...")
    cluster_info = characterize_clusters(vectors, embedding, cluster_labels, metadata)

    for ci in cluster_info:
        label = "NOISE" if ci["is_noise"] else f"C{ci['cluster_id']}"
        dom = ci.get("dominant_type", "?")
        pur = ci.get("purity", 0)
        print(f"    {label}: {ci['n_members']:6d} objects ({ci['fraction']:.1%})"
              f"  dominant={dom}  purity={pur:.2f}")

    # Metrics
    print("\n[6/6] Computing quality metrics...")
    true_labels = None
    if metadata is not None and "true_label" in metadata.columns:
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        true_labels = le.fit_transform(metadata["true_label"].values)

    metrics = compute_metrics(cluster_labels, true_labels, embedding)
    print(f"  Silhouette: {metrics.get('silhouette_score', 'N/A')}")
    print(f"  ARI: {metrics.get('ARI', 'N/A')}")
    print(f"  NMI: {metrics.get('NMI', 'N/A')}")
    print(f"  Clusters: {metrics['n_clusters']}, Noise: {metrics['n_noise']} ({metrics['noise_fraction']:.1%})")

    # Identify most interesting noise objects
    noise_mask = cluster_labels == -1
    noise_indices = np.where(noise_mask)[0]
    interesting_noise = []
    if len(noise_indices) > 0 and metadata is not None:
        # Rank noise by anomaly score
        noise_scores = metadata.iloc[noise_indices]["anomaly_score"].values if "anomaly_score" in metadata.columns else np.zeros(len(noise_indices))
        top_noise_idx = noise_indices[np.argsort(noise_scores)[-50:][::-1]]
        for rank, idx in enumerate(top_noise_idx):
            row = metadata.iloc[idx]
            interesting_noise.append({
                "rank": rank + 1,
                "index": int(idx),
                "object_id": str(row.get("object_id", f"IDX_{idx}")),
                "anomaly_score": float(row.get("anomaly_score", 0)),
                "redshift": float(row.get("redshift", 0)),
                "ra": float(row.get("ra", 0)),
                "dec": float(row.get("dec", 0)),
                "true_label": str(row.get("true_label", "unknown")),
                "umap_x": float(embedding[idx, 0]),
                "umap_y": float(embedding[idx, 1]),
            })

    # Save
    total_time = time.time() - t_start

    summary = {
        "experiment": "spectral_taxonomy_deep",
        "description": "UMAP + HDBSCAN deep taxonomy of anomaly population",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data_source": data_source,
        "source_path": str(source),
        "n_objects": int(vectors.shape[0]),
        "input_dim": int(vectors.shape[1]),
        "embedding_method": embed_method,
        "clustering_method": cluster_method,
        "params": {
            "pca_components": 50,
            "umap_n_neighbors": 30,
            "umap_min_dist": 0.1,
            "hdbscan_min_cluster_size": 500,
            "hdbscan_min_samples": 50,
        },
        "metrics": metrics,
        "clusters": cluster_info,
        "top_50_noise_objects": interesting_noise,
        "timing": {
            "pca_s": float(0),
            "umap_s": float(umap_time),
            "hdbscan_s": float(hdb_time),
            "total_s": float(total_time),
        },
        "device": str(device),
    }

    with open(OUTPUT_DIR / "taxonomy_deep_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    np.save(OUTPUT_DIR / "umap_embedding.npy", embedding)
    np.save(OUTPUT_DIR / "cluster_labels.npy", cluster_labels)
    np.save(OUTPUT_DIR / "cluster_probs.npy", cluster_probs)

    embed_df = pd.DataFrame({
        "umap_x": embedding[:, 0],
        "umap_y": embedding[:, 1],
        "cluster": cluster_labels,
        "cluster_prob": cluster_probs,
    })
    if metadata is not None:
        for col in ["object_id", "ra", "dec", "redshift", "anomaly_score", "true_label"]:
            if col in metadata.columns:
                embed_df[col] = metadata[col].values
    embed_df.to_csv(OUTPUT_DIR / "taxonomy_full.csv", index=False)

    if interesting_noise:
        pd.DataFrame(interesting_noise).to_csv(OUTPUT_DIR / "top50_noise.csv", index=False)

    print(f"\n  Saved to: {OUTPUT_DIR}")
    print(f"  Total time: {total_time:.1f}s")

    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
