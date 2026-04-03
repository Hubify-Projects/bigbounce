#!/usr/bin/env python3
"""
Spectral Anomaly Taxonomy — UMAP + HDBSCAN clustering of SDSS anomalies.

Loads anomaly parquet files from the multi-survey sweep, extracts 128-dim
latent vectors, reduces to 2D via UMAP, and clusters with HDBSCAN.  Each
cluster is characterized by mean anomaly score, size, centroid latent
vector, and representative member spectra.

GPU acceleration: uses cuml UMAP/HDBSCAN if available (rapids), otherwise
falls back to CPU (umap-learn + hdbscan).  50K points runs in ~2 min on
CPU, ~10 s on GPU.

Output (all in /workspace/bigbounce/outputs/taxonomy/):
  taxonomy_clusters.parquet  — per-object cluster assignment + UMAP coords
  taxonomy_summary.json      — cluster stats, centroids, representatives
  checkpoint.json            — run metadata for resumability
"""

import os, sys, json, time, glob, subprocess
import numpy as np

# ─── Dependency bootstrap ────────────────────────────────────────────────────

def _ensure(pkg, pip_name=None):
    try:
        __import__(pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install",
                               pip_name or pkg, "-q"])

_ensure("pyarrow")
_ensure("umap", "umap-learn")
_ensure("hdbscan")
_ensure("pandas")

import pandas as pd
import pyarrow.parquet as pq

# ─── Configuration ───────────────────────────────────────────────────────────

BASE       = "/workspace/bigbounce"
PARQ_GLOB  = os.path.join(BASE, "outputs", "sdss_batch_*.parquet")
OUT_DIR    = os.path.join(BASE, "outputs", "taxonomy")
TOP_K      = 50_000          # max anomalies to cluster
MIN_CLUSTER = 15             # HDBSCAN min_cluster_size
UMAP_N     = 15              # UMAP n_neighbors
UMAP_DIST  = 0.1             # UMAP min_dist
SEED       = 42
LAT_COLS   = [f"lat_{i:03d}" for i in range(128)]

os.makedirs(OUT_DIR, exist_ok=True)

# ─── 1. Load all anomaly parquet files ───────────────────────────────────────

def load_anomalies():
    files = sorted(glob.glob(PARQ_GLOB))
    if not files:
        sys.exit(f"ERROR: no parquet files matching {PARQ_GLOB}")
    print(f"Found {len(files)} parquet files")

    frames = []
    for f in files:
        df = pd.read_parquet(f)
        frames.append(df)
        print(f"  {os.path.basename(f)}: {len(df):,} rows")

    df = pd.concat(frames, ignore_index=True)
    print(f"Total rows: {len(df):,}")
    return df

# ─── 2. Filter to top anomalies ─────────────────────────────────────────────

def filter_top(df):
    missing = [c for c in LAT_COLS if c not in df.columns]
    if missing:
        sys.exit(f"ERROR: missing latent columns: {missing[:5]}...")

    if "anomaly_score" not in df.columns:
        sys.exit("ERROR: no anomaly_score column found")

    df = df.dropna(subset=["anomaly_score"])
    df = df.sort_values("anomaly_score", ascending=False).head(TOP_K)
    df = df.reset_index(drop=True)
    print(f"Filtered to top {len(df):,} anomalies "
          f"(score range {df['anomaly_score'].min():.4f} – "
          f"{df['anomaly_score'].max():.4f})")
    return df

# ─── 3. UMAP dimensionality reduction ───────────────────────────────────────

def run_umap(X):
    """Try cuml GPU UMAP first, fall back to umap-learn CPU."""
    try:
        from cuml.manifold import UMAP as cuUMAP
        print("Using cuML GPU UMAP")
        reducer = cuUMAP(n_neighbors=UMAP_N, min_dist=UMAP_DIST,
                         n_components=2, random_state=SEED, verbose=True)
    except ImportError:
        import umap
        print("Using umap-learn (CPU)")
        reducer = umap.UMAP(n_neighbors=UMAP_N, min_dist=UMAP_DIST,
                            n_components=2, random_state=SEED, verbose=True)

    t0 = time.time()
    embedding = reducer.fit_transform(X)
    dt = time.time() - t0
    print(f"UMAP done in {dt:.1f}s — shape {embedding.shape}")
    return np.asarray(embedding, dtype=np.float32)

# ─── 4. HDBSCAN clustering ──────────────────────────────────────────────────

def run_hdbscan(embedding):
    """Try cuml GPU HDBSCAN first, fall back to CPU hdbscan."""
    try:
        from cuml.cluster import HDBSCAN as cuHDBSCAN
        print("Using cuML GPU HDBSCAN")
        clusterer = cuHDBSCAN(min_cluster_size=MIN_CLUSTER,
                              min_samples=5, prediction_data=True)
    except ImportError:
        import hdbscan
        print("Using hdbscan (CPU)")
        clusterer = hdbscan.HDBSCAN(min_cluster_size=MIN_CLUSTER,
                                     min_samples=5, prediction_data=True)

    t0 = time.time()
    labels = clusterer.fit_predict(embedding)
    dt = time.time() - t0
    labels = np.asarray(labels)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = int(np.sum(labels == -1))
    print(f"HDBSCAN done in {dt:.1f}s — {n_clusters} clusters, "
          f"{n_noise} noise points")
    return labels, clusterer

# ─── 5. Characterize clusters ───────────────────────────────────────────────

def characterize(df, X_lat, embedding, labels):
    unique_labels = sorted(set(labels))
    clusters = []

    for lab in unique_labels:
        mask = labels == lab
        idxs = np.where(mask)[0]
        scores = df.loc[idxs, "anomaly_score"].values
        centroid = X_lat[idxs].mean(axis=0).tolist()
        umap_center = embedding[idxs].mean(axis=0).tolist()

        # Pick 5 most anomalous members as representatives
        top5 = idxs[np.argsort(-scores)[:5]]
        reps = []
        for i in top5:
            row = {"index": int(i), "anomaly_score": float(scores[np.where(idxs == i)[0][0]])}
            for col in ["objid", "specobjid", "plate", "mjd", "fiberid",
                        "class", "subclass", "z", "ra", "dec"]:
                if col in df.columns:
                    val = df.loc[i, col]
                    row[col] = val.item() if hasattr(val, "item") else val
            reps.append(row)

        info = {
            "cluster_id":        int(lab),
            "is_noise":          lab == -1,
            "size":              int(mask.sum()),
            "mean_anomaly_score": float(scores.mean()),
            "std_anomaly_score":  float(scores.std()),
            "min_anomaly_score":  float(scores.min()),
            "max_anomaly_score":  float(scores.max()),
            "umap_center":       umap_center,
            "latent_centroid":   centroid,
            "representatives":   reps,
        }
        clusters.append(info)

    clusters.sort(key=lambda c: c["mean_anomaly_score"], reverse=True)
    return clusters

# ─── 6. Save outputs ────────────────────────────────────────────────────────

def save(df, embedding, labels, clusters, t_total):
    # Parquet with cluster assignments
    out = df.copy()
    out["umap_x"] = embedding[:, 0]
    out["umap_y"] = embedding[:, 1]
    out["cluster_id"] = labels
    pq_path = os.path.join(OUT_DIR, "taxonomy_clusters.parquet")
    out.to_parquet(pq_path, index=False)
    print(f"Saved {pq_path} ({len(out):,} rows)")

    # Summary JSON
    summary = {
        "n_objects":   len(df),
        "n_clusters":  sum(1 for c in clusters if not c["is_noise"]),
        "n_noise":     sum(c["size"] for c in clusters if c["is_noise"]),
        "top_k":       TOP_K,
        "umap_params": {"n_neighbors": UMAP_N, "min_dist": UMAP_DIST},
        "hdbscan_params": {"min_cluster_size": MIN_CLUSTER, "min_samples": 5},
        "clusters":    clusters,
    }
    js_path = os.path.join(OUT_DIR, "taxonomy_summary.json")
    with open(js_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"Saved {js_path}")

    # Checkpoint
    ckpt = {
        "status":      "complete",
        "timestamp":   time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "runtime_s":   round(t_total, 1),
        "n_objects":   len(df),
        "n_clusters":  summary["n_clusters"],
        "n_noise":     summary["n_noise"],
        "parquet":     pq_path,
        "summary":     js_path,
    }
    ck_path = os.path.join(OUT_DIR, "checkpoint.json")
    with open(ck_path, "w") as f:
        json.dump(ckpt, f, indent=2)
    print(f"Saved {ck_path}")

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    t0 = time.time()
    print("=" * 60)
    print("Spectral Anomaly Taxonomy — UMAP + HDBSCAN")
    print("=" * 60)

    df = load_anomalies()
    df = filter_top(df)

    X_lat = df[LAT_COLS].values.astype(np.float32)
    print(f"Latent matrix: {X_lat.shape}")

    embedding = run_umap(X_lat)
    labels, _ = run_hdbscan(embedding)

    clusters = characterize(df, X_lat, embedding, labels)

    t_total = time.time() - t0
    save(df, embedding, labels, clusters, t_total)

    print(f"\nDone in {t_total:.1f}s")
    print(f"Clusters found: {sum(1 for c in clusters if not c['is_noise'])}")
    for c in clusters[:10]:
        tag = "NOISE" if c["is_noise"] else f"C{c['cluster_id']}"
        print(f"  {tag:>6s}: {c['size']:>6,} objects, "
              f"mean score {c['mean_anomaly_score']:.4f}")

if __name__ == "__main__":
    main()
