#!/usr/bin/env python3
"""
UMAP + HDBSCAN classification of 77,905 SDSS DR18 spectral anomalies.

Mirrors the DESI DR1 pipeline at:
  pipelines/p1_highz_tracers/outputs/umap_clustering/run_umap_hdbscan.py

Schema differences from DESI:
  - SDSS has: plate, mjd, fiberid, anomaly_score, rB, rR, rZ, lat_000..lat_127
  - SDSS does NOT have: z (redshift), classification, peak_residual_wavelength, worst_band
  - rB/rR/rZ are per-band residuals used to infer spectral character

Anomaly threshold: score > 5.0 → exactly 77,905 objects across 46 files.

Category heuristics (applied after clustering, per cluster medians):
  - HIGH_Z_CANDIDATE  : rZ dominates (rZ >> rB) — z-band excess, high-z galaxy likely
  - BLUE_EXCESS       : rB dominates (rB >> rR, rB >> rZ) — blue continuum, possible QSO
  - BROAD_EXCESS      : all three bands high roughly equally — broad spectral feature
  - AGN_CANDIDATE     : high score + blue excess + moderately high rR — AGN/Seyfert signature
  - EMISSION_LINE     : very high rR (optical emission peak), rB modest — emission galaxy
  - ARTIFACT          : extremely high score outlier with unbalanced residuals — CCD/pipeline glitch
  - UNCATEGORIZED     : noise or residuals too balanced to classify

Usage:
  pip install umap-learn hdbscan pyarrow pandas matplotlib numpy
  python3 classify_sdss_anomalies.py
"""

import glob
import json
import time
import sys

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

# ── Paths ──────────────────────────────────────────────────────────────────

DATA_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/h200_results/sdss_dr18"
OUT_DIR  = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/anomaly_classification"

ANOMALY_THRESHOLD = 5.0    # score > 5.0  → 77,905 objects
UMAP_N_NEIGHBORS  = 30
UMAP_MIN_DIST     = 0.1
HDBSCAN_MIN_CLUSTER  = 50
HDBSCAN_MIN_SAMPLES  = 10

# ── Step 1: Load all 46 SDSS parquet batches ──────────────────────────────

lat_cols  = [f"lat_{i:03d}" for i in range(128)]
band_cols = ["rB", "rR", "rZ"]
id_cols   = ["plate", "mjd", "fiberid"]
all_cols  = id_cols + ["anomaly_score"] + band_cols + lat_cols

files = sorted(glob.glob(f"{DATA_DIR}/sdss_batch_*.parquet"))
print(f"Found {len(files)} parquet files in {DATA_DIR}")
if not files:
    sys.exit("ERROR: no sdss_batch_*.parquet files found — check DATA_DIR")

chunks = []
for i, f in enumerate(files):
    tbl = pq.read_table(f, columns=all_cols)
    df_chunk = tbl.to_pandas()
    df_chunk = df_chunk.loc[df_chunk["anomaly_score"] > ANOMALY_THRESHOLD]
    chunks.append(df_chunk)
    if (i + 1) % 10 == 0 or i == len(files) - 1:
        print(f"  Loaded {i+1}/{len(files)} files | anomalies so far: "
              f"{sum(len(c) for c in chunks):,}")

df = pd.concat(chunks, ignore_index=True)
print(f"\nTotal anomalies (score > {ANOMALY_THRESHOLD}): {len(df):,}")
print(f"Columns: {list(df.columns)}")
sys.stdout.flush()

# ── Step 2: Extract latent vectors and clean NaN/inf ──────────────────────

X = df[lat_cols].values.astype(np.float32)
print(f"\nLatent matrix shape: {X.shape}")

bad_mask = np.isnan(X).any(axis=1) | np.isinf(X).any(axis=1)
if bad_mask.sum() > 0:
    print(f"WARNING: {bad_mask.sum()} rows have NaN/inf in latent vectors — removing")
    df = df[~bad_mask].reset_index(drop=True)
    X  = df[lat_cols].values.astype(np.float32)
    print(f"After cleanup: {len(df):,} rows, latent shape {X.shape}")

# Also sanitise band columns used later for heuristics
for col in band_cols:
    df[col] = df[col].replace([np.inf, -np.inf], np.nan).fillna(0.0)

sys.stdout.flush()

# ── Step 3: UMAP 2-D embedding ────────────────────────────────────────────

print(f"\nRunning UMAP (n_components=2, n_neighbors={UMAP_N_NEIGHBORS}, "
      f"min_dist={UMAP_MIN_DIST})...")
t0 = time.time()

import umap

reducer = umap.UMAP(
    n_components  = 2,
    n_neighbors   = UMAP_N_NEIGHBORS,
    min_dist      = UMAP_MIN_DIST,
    metric        = "euclidean",
    random_state  = 42,
    low_memory    = True,
    verbose       = True,
)
embedding = reducer.fit_transform(X)

dt_umap = time.time() - t0
print(f"UMAP done in {dt_umap:.1f}s — embedding shape: {embedding.shape}")
sys.stdout.flush()

df["umap_x"] = embedding[:, 0]
df["umap_y"] = embedding[:, 1]

# ── Step 4: HDBSCAN clustering ────────────────────────────────────────────

print(f"\nRunning HDBSCAN (min_cluster_size={HDBSCAN_MIN_CLUSTER}, "
      f"min_samples={HDBSCAN_MIN_SAMPLES})...")
t0 = time.time()

import hdbscan

clusterer = hdbscan.HDBSCAN(
    min_cluster_size      = HDBSCAN_MIN_CLUSTER,
    min_samples           = HDBSCAN_MIN_SAMPLES,
    cluster_selection_method = "eom",
    core_dist_n_jobs      = -1,
)
labels = clusterer.fit_predict(embedding)

dt_hdbscan = time.time() - t0
print(f"HDBSCAN done in {dt_hdbscan:.1f}s")
sys.stdout.flush()

df["cluster"] = labels

n_clusters  = int(labels.max()) + 1
n_noise     = int((labels == -1).sum())
n_clustered = int((labels >= 0).sum())
frac_clustered = n_clustered / len(df)

print(f"\n{'='*65}")
print(f"CLUSTERING RESULTS")
print(f"{'='*65}")
print(f"Total anomalies:     {len(df):,}")
print(f"Clusters found:      {n_clusters}")
print(f"In clusters:         {n_clustered:,} ({frac_clustered:.1%})")
print(f"Noise (unclustered): {n_noise:,} ({1-frac_clustered:.1%})")
print(f"UMAP time:           {dt_umap:.1f}s")
print(f"HDBSCAN time:        {dt_hdbscan:.1f}s")
sys.stdout.flush()

# ── Step 5: Per-cluster statistics and category heuristics ────────────────

def infer_category(med_score, med_rB, med_rR, med_rZ):
    """
    Rule-based category assignment using median band residuals.

    Band semantics (SDSS spectrograph):
      rB ~ 3800–6000 Å  (blue optical)
      rR ~ 5600–9200 Å  (red optical)
      rZ ~ 8400–9200 Å  (far red / near-IR)

    A galaxy at z ~ 1 shifts Lyman-break into optical; its spectrum
    is faint in blue → rB excess relative to rR.
    A QSO/AGN has strong blue continuum → rB high.
    Emission-line galaxies peak in rR.
    CCD artifacts tend to produce extreme single-band spikes.
    """
    # Normalise to avoid log(0): add a floor
    rB = max(med_rB, 1e-6)
    rR = max(med_rR, 1e-6)
    rZ = max(med_rZ, 1e-6)

    total  = rB + rR + rZ
    fB = rB / total
    fR = rR / total
    fZ = rZ / total

    # Artifact: any single band is >80 % of total AND score is extremely high
    if med_score > 1e5 and (fB > 0.80 or fR > 0.80 or fZ > 0.80):
        return "ARTIFACT"

    # Emission-line galaxy: red band dominates strongly, blue modest
    if fR > 0.55 and fB < 0.30:
        return "EMISSION_LINE_GALAXY"

    # High-z candidate: z-band (far red) dominates
    if fZ > 0.45 and fZ > fB * 2.0:
        return "HIGH_Z_CANDIDATE"

    # Blue excess / QSO / AGN
    if fB > 0.45:
        if med_score > 500 or fR > 0.25:
            return "AGN_CANDIDATE"
        return "BLUE_EXCESS_QSO"

    # Broad excess: all three bands elevated roughly equally
    if abs(fB - fR) < 0.12 and abs(fR - fZ) < 0.12:
        return "BROAD_SPECTRAL_EXCESS"

    return "UNCATEGORIZED"


cluster_stats = []

header = (f"{'Clust':>6} {'Size':>7} {'Med Score':>12} "
          f"{'Med rB':>9} {'Med rR':>9} {'Med rZ':>9} {'Category':<26}")
print(f"\n{header}")
print("-" * 85)

for cid in range(n_clusters):
    mask = df["cluster"] == cid
    sub  = mask.pipe(lambda m: df[m])

    med_score = float(sub["anomaly_score"].median())
    med_rB    = float(sub["rB"].median())
    med_rR    = float(sub["rR"].median())
    med_rZ    = float(sub["rZ"].median())

    category  = infer_category(med_score, med_rB, med_rR, med_rZ)

    stats = {
        "cluster_id"             : cid,
        "size"                   : int(mask.sum()),
        "fraction_of_anomalies"  : round(mask.sum() / len(df), 5),
        "median_anomaly_score"   : med_score,
        "mean_anomaly_score"     : float(sub["anomaly_score"].mean()),
        "std_anomaly_score"      : float(sub["anomaly_score"].std()),
        "median_rB"              : med_rB,
        "median_rR"              : med_rR,
        "median_rZ"              : med_rZ,
        "mean_umap_x"            : float(sub["umap_x"].mean()),
        "mean_umap_y"            : float(sub["umap_y"].mean()),
        "inferred_category"      : category,
    }
    cluster_stats.append(stats)

    print(f"{cid:>6d} {mask.sum():>7,} {med_score:>12.2f} "
          f"{med_rB:>9.3f} {med_rR:>9.3f} {med_rZ:>9.3f} {category:<26}")

# Noise row
noise_sub = df[df["cluster"] == -1]
noise_stats = {
    "cluster_id"           : -1,
    "label"                : "noise",
    "size"                 : n_noise,
    "fraction_of_anomalies": round(n_noise / len(df), 5),
    "median_anomaly_score" : float(noise_sub["anomaly_score"].median()) if n_noise > 0 else None,
    "median_rB"            : float(noise_sub["rB"].median()) if n_noise > 0 else None,
    "median_rR"            : float(noise_sub["rR"].median()) if n_noise > 0 else None,
    "median_rZ"            : float(noise_sub["rZ"].median()) if n_noise > 0 else None,
    "inferred_category"    : "NOISE",
}
if n_noise > 0:
    print(f"{'noise':>6} {n_noise:>7,} "
          f"{noise_stats['median_anomaly_score']:>12.2f} "
          f"{noise_stats['median_rB']:>9.3f} "
          f"{noise_stats['median_rR']:>9.3f} "
          f"{noise_stats['median_rZ']:>9.3f} {'NOISE':<26}")

sys.stdout.flush()

# ── Category count summary ─────────────────────────────────────────────────

category_counts = {}
for s in cluster_stats:
    cat = s["inferred_category"]
    category_counts[cat] = category_counts.get(cat, 0) + s["size"]
category_counts["NOISE"] = n_noise

print(f"\n{'CATEGORY SUMMARY':}")
print("-" * 45)
for cat, cnt in sorted(category_counts.items(), key=lambda x: -x[1]):
    print(f"  {cat:<30} {cnt:>8,}  ({cnt/len(df):.1%})")
sys.stdout.flush()

# ── Step 6: Save outputs ──────────────────────────────────────────────────

# 6a. Clustered dataframe (with UMAP coords + cluster label)
out_df_cols = id_cols + ["anomaly_score"] + band_cols + ["umap_x", "umap_y", "cluster"]
out_parquet = f"{OUT_DIR}/sdss_anomaly_umap.parquet"
df[out_df_cols].to_parquet(out_parquet, index=False)
print(f"\nSaved clustered dataframe → {out_parquet} ({len(df):,} rows)")

# 6b. Cluster summary JSON
summary = {
    "survey"               : "SDSS DR18",
    "input_files"          : len(files),
    "anomaly_threshold"    : ANOMALY_THRESHOLD,
    "total_anomalies"      : len(df),
    "n_clusters"           : n_clusters,
    "n_clustered"          : n_clustered,
    "n_noise"              : n_noise,
    "fraction_clustered"   : round(frac_clustered, 5),
    "umap_params"          : {
        "n_components"     : 2,
        "n_neighbors"      : UMAP_N_NEIGHBORS,
        "min_dist"         : UMAP_MIN_DIST,
        "metric"           : "euclidean",
        "random_state"     : 42,
    },
    "hdbscan_params"       : {
        "min_cluster_size" : HDBSCAN_MIN_CLUSTER,
        "min_samples"      : HDBSCAN_MIN_SAMPLES,
        "cluster_selection_method": "eom",
    },
    "timing_seconds"       : {
        "umap"             : round(dt_umap, 2),
        "hdbscan"          : round(dt_hdbscan, 2),
    },
    "category_totals"      : category_counts,
    "clusters"             : cluster_stats,
    "noise"                : noise_stats,
}

out_json = f"{OUT_DIR}/sdss_cluster_summary.json"
with open(out_json, "w") as fh:
    json.dump(summary, fh, indent=2)
print(f"Saved cluster summary   → {out_json}")
sys.stdout.flush()

# ── Step 7: UMAP scatter plot ─────────────────────────────────────────────

print("\nGenerating scatter plot...")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Map each inferred category to a colour for annotation boxes
CATEGORY_COLORS = {
    "HIGH_Z_CANDIDATE"     : "#e74c3c",   # red
    "AGN_CANDIDATE"        : "#e67e22",   # orange
    "BLUE_EXCESS_QSO"      : "#3498db",   # blue
    "EMISSION_LINE_GALAXY" : "#2ecc71",   # green
    "BROAD_SPECTRAL_EXCESS": "#9b59b6",   # purple
    "ARTIFACT"             : "#95a5a6",   # gray
    "UNCATEGORIZED"        : "#bdc3c7",   # light gray
    "NOISE"                : "#dddddd",
}

fig, axes = plt.subplots(1, 2, figsize=(20, 9))

# --- Left panel: coloured by cluster ID ---
ax = axes[0]
noise_mask = df["cluster"] == -1
if noise_mask.sum() > 0:
    ax.scatter(
        df.loc[noise_mask, "umap_x"],
        df.loc[noise_mask, "umap_y"],
        c="#dddddd", s=0.3, alpha=0.12, rasterized=True, label=f"Noise ({n_noise:,})"
    )
if n_clusters > 0:
    cmap = plt.cm.get_cmap("tab20", max(n_clusters, 1))
    cm = df["cluster"] >= 0
    sc = ax.scatter(
        df.loc[cm, "umap_x"],
        df.loc[cm, "umap_y"],
        c=df.loc[cm, "cluster"],
        cmap=cmap,
        s=0.8,
        alpha=0.5,
        vmin=-0.5,
        vmax=n_clusters - 0.5,
        rasterized=True,
    )
    cbar = plt.colorbar(sc, ax=ax, shrink=0.7, pad=0.02)
    cbar.set_label("Cluster ID", fontsize=11)
    cbar.set_ticks(range(n_clusters))

# Annotate cluster centres
for s in cluster_stats:
    ax.annotate(
        f"C{s['cluster_id']}",
        (s["mean_umap_x"], s["mean_umap_y"]),
        fontsize=6,
        fontweight="bold",
        ha="center",
        va="center",
        color="black",
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="gray", alpha=0.85),
    )

ax.set_xlabel("UMAP-1", fontsize=12)
ax.set_ylabel("UMAP-2", fontsize=12)
ax.set_title(
    f"SDSS DR18 Spectral Anomalies — UMAP + HDBSCAN\n"
    f"{len(df):,} anomalies (score > {ANOMALY_THRESHOLD}), "
    f"{n_clusters} clusters, {frac_clustered:.1%} clustered",
    fontsize=12, fontweight="bold"
)
ax.legend(loc="upper right", fontsize=9, markerscale=6)

# --- Right panel: coloured by inferred category ---
ax2 = axes[1]

# Build per-point category array
point_categories = np.array(["NOISE"] * len(df), dtype=object)
for s in cluster_stats:
    mask = df["cluster"] == s["cluster_id"]
    point_categories[mask.values] = s["inferred_category"]

# Plot each category separately
for cat, col in CATEGORY_COLORS.items():
    m = point_categories == cat
    if m.sum() == 0:
        continue
    size  = 0.3 if cat == "NOISE" else 1.2
    alpha = 0.10 if cat == "NOISE" else 0.55
    ax2.scatter(
        df.loc[m, "umap_x"],
        df.loc[m, "umap_y"],
        c=col,
        s=size,
        alpha=alpha,
        rasterized=True,
        label=f"{cat} ({m.sum():,})",
    )

# Annotate cluster centres with category label
for s in cluster_stats:
    short = s["inferred_category"].replace("_", "\n")
    ax2.annotate(
        f"C{s['cluster_id']}\n{short}",
        (s["mean_umap_x"], s["mean_umap_y"]),
        fontsize=5,
        ha="center",
        va="center",
        color="black",
        bbox=dict(
            boxstyle="round,pad=0.15",
            fc=CATEGORY_COLORS.get(s["inferred_category"], "white"),
            ec="gray",
            alpha=0.85,
        ),
    )

ax2.set_xlabel("UMAP-1", fontsize=12)
ax2.set_ylabel("UMAP-2", fontsize=12)
ax2.set_title(
    f"SDSS DR18 — Inferred Physical Categories",
    fontsize=12, fontweight="bold"
)
leg = ax2.legend(loc="upper right", fontsize=7, markerscale=8,
                  framealpha=0.9, title="Category")
leg.get_title().set_fontsize(8)

plt.tight_layout()
out_png = f"{OUT_DIR}/sdss_umap_clusters.png"
plt.savefig(out_png, dpi=200, bbox_inches="tight")
print(f"Saved scatter plot       → {out_png}")

# ── Done ──────────────────────────────────────────────────────────────────

print(f"\n{'='*65}")
print(f"ALL OUTPUTS SAVED TO: {OUT_DIR}/")
print(f"{'='*65}")
print(f"  sdss_anomaly_umap.parquet   — clustered anomaly table ({len(df):,} rows)")
print(f"  sdss_cluster_summary.json   — cluster stats + categories")
print(f"  sdss_umap_clusters.png      — dual-panel scatter plot")
print(f"\nClusters: {n_clusters}  |  Clustered: {n_clustered:,} ({frac_clustered:.1%})"
      f"  |  Noise: {n_noise:,}")
print("\nTop categories:")
for cat, cnt in sorted(category_counts.items(), key=lambda x: -x[1])[:5]:
    print(f"  {cat:<30} {cnt:>8,}")
print("\nDone.")
