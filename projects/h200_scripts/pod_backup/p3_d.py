#!/usr/bin/env python3
"""
P3-D — ensemble anomaly detection on DESI DR1 latents (or feature-space fallback).

Inputs:
  /workspace/bigbounce_scan/inputs/dr1_all_anomalies.json (195,829 DESI DR1 anomalies)

Approach:
  The JSON has no explicit 16-D latents — only {tid, ra, dec, score, worst,
  rB, rR, rZ}. We build an 8-D feature vector per object from:
    [score, rB, rR, rZ, log10(|rB|+1), log10(|rR|+1), log10(|rZ|+1),
     worst_encoded]
  Train 3 estimators (IsolationForest, LOF-novelty, OCSVM) on the full
  set; rank each object by each method; take rank-sum agreement.

Outputs:
  /workspace/bigbounce_scan/outputs/p3_d/ensemble_top100.parquet
  /workspace/bigbounce_scan/outputs/p3_d/ensemble_results.json

Runtime expectation on A100 host CPU: ~3-8 min for 195k points at 8D.
No GPU needed — scikit-learn CPU implementations are fine at this scale.
"""

import json
import time
import pathlib
import sys
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

INPUT_JSON = "/workspace/bigbounce_scan/inputs/dr1_all_anomalies.json"
OUT_DIR = pathlib.Path("/workspace/bigbounce_scan/outputs/p3_d")
OUT_DIR.mkdir(parents=True, exist_ok=True)

t0 = time.time()
print(f"[P3-D] Loading {INPUT_JSON}")
with open(INPUT_JSON) as fh:
    data = json.load(fh)
print(f"[P3-D] Loaded {len(data):,} anomalies in {time.time()-t0:.1f}s")

df = pd.DataFrame(data)
print(f"[P3-D] Columns: {list(df.columns)}")
print(f"[P3-D] dtypes:\n{df.dtypes}")

# Check for latents
latent_cols = [c for c in df.columns if c.startswith(("z_", "latent_", "feat_"))]
if latent_cols and len(latent_cols) >= 8:
    print(f"[P3-D] Found {len(latent_cols)} latent cols, using latents")
    X = df[latent_cols].to_numpy(dtype=np.float32)
else:
    print("[P3-D] No latents present — building 8-D feature vector from "
          "{score, rB, rR, rZ, log10 transforms, worst-encoded}")
    worst_map = {w: i for i, w in enumerate(sorted(df["worst"].unique()))}
    df["worst_enc"] = df["worst"].map(worst_map)
    feats = np.column_stack([
        df["score"].to_numpy(dtype=np.float32),
        df["rB"].to_numpy(dtype=np.float32),
        df["rR"].to_numpy(dtype=np.float32),
        df["rZ"].to_numpy(dtype=np.float32),
        np.log10(np.abs(df["rB"]) + 1.0),
        np.log10(np.abs(df["rR"]) + 1.0),
        np.log10(np.abs(df["rZ"]) + 1.0),
        df["worst_enc"].to_numpy(dtype=np.float32),
    ]).astype(np.float32)
    X = feats

scaler = StandardScaler()
Xs = scaler.fit_transform(X)
print(f"[P3-D] Feature matrix shape: {Xs.shape}")

# Subsample for LOF/OCSVM training (they scale poorly); score all.
N = Xs.shape[0]
rng = np.random.default_rng(42)
if N > 20000:
    train_idx = rng.choice(N, 20000, replace=False)
    X_train = Xs[train_idx]
else:
    X_train = Xs

# 1) Isolation Forest — full fit on all 195k
t = time.time()
print("[P3-D] Training IsolationForest …")
iso = IsolationForest(n_estimators=200, contamination="auto",
                      random_state=42, n_jobs=-1)
iso.fit(Xs)
iso_scores = -iso.score_samples(Xs)  # higher = more anomalous
print(f"[P3-D]   done in {time.time()-t:.1f}s")

# 2) LOF novelty mode
t = time.time()
print("[P3-D] Training LOF (novelty=True) …")
lof = LocalOutlierFactor(n_neighbors=35, novelty=True, n_jobs=-1)
lof.fit(X_train)
lof_scores = -lof.score_samples(Xs)
print(f"[P3-D]   done in {time.time()-t:.1f}s")

# 3) OCSVM
t = time.time()
print("[P3-D] Training OneClassSVM (RBF, nu=0.05) …")
ocsvm = OneClassSVM(kernel="rbf", gamma="scale", nu=0.05)
ocsvm.fit(X_train)
ocsvm_scores = -ocsvm.score_samples(Xs)
print(f"[P3-D]   done in {time.time()-t:.1f}s")

# Rank-based agreement
print("[P3-D] Computing rank-sum agreement …")
def ranks(a):
    return np.argsort(np.argsort(-a))  # 0 = most anomalous
r_iso = ranks(iso_scores)
r_lof = ranks(lof_scores)
r_ocsvm = ranks(ocsvm_scores)
rank_sum = r_iso + r_lof + r_ocsvm

# Spearman correlations for method diversity
from scipy.stats import spearmanr
corr_iso_lof = spearmanr(iso_scores, lof_scores).correlation
corr_iso_svm = spearmanr(iso_scores, ocsvm_scores).correlation
corr_lof_svm = spearmanr(lof_scores, ocsvm_scores).correlation
print(f"[P3-D]   iso vs lof  = {corr_iso_lof:.3f}")
print(f"[P3-D]   iso vs svm  = {corr_iso_svm:.3f}")
print(f"[P3-D]   lof vs svm  = {corr_lof_svm:.3f}")

# Top-100 by rank-sum
df["iso_score"] = iso_scores
df["lof_score"] = lof_scores
df["ocsvm_score"] = ocsvm_scores
df["iso_rank"] = r_iso
df["lof_rank"] = r_lof
df["ocsvm_rank"] = r_ocsvm
df["rank_sum"] = rank_sum

top100 = df.nsmallest(100, "rank_sum").copy()
top100.to_parquet(OUT_DIR / "ensemble_top100.parquet", index=False)
print(f"[P3-D] Wrote {OUT_DIR / 'ensemble_top100.parquet'}")

# Intersection of top-500 across methods (stronger agreement signal)
top500_iso = set(np.argsort(-iso_scores)[:500])
top500_lof = set(np.argsort(-lof_scores)[:500])
top500_svm = set(np.argsort(-ocsvm_scores)[:500])
triple_intersect = top500_iso & top500_lof & top500_svm
print(f"[P3-D] |top500 ∩ (all 3 methods)| = {len(triple_intersect)}")

results = {
    "task": "P3-D",
    "input": INPUT_JSON,
    "n_anomalies": int(N),
    "feature_source": "latents" if latent_cols and len(latent_cols) >= 8 else "derived_8d",
    "feature_dims": int(Xs.shape[1]),
    "methods": ["IsolationForest", "LocalOutlierFactor(novelty)", "OneClassSVM"],
    "spearman_rho": {
        "iso_lof": float(corr_iso_lof),
        "iso_ocsvm": float(corr_iso_svm),
        "lof_ocsvm": float(corr_lof_svm),
    },
    "top500_triple_intersection_count": len(triple_intersect),
    "top100_rank_sum_range": [int(top100["rank_sum"].min()),
                              int(top100["rank_sum"].max())],
    "top100_score_range": [float(top100["score"].min()),
                           float(top100["score"].max())],
    "auc_note": "no ground-truth column in input; AUC not computed",
    "runtime_s": round(time.time() - t0, 1),
    "completed_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

with open(OUT_DIR / "ensemble_results.json", "w") as fh:
    json.dump(results, fh, indent=2)
print(f"[P3-D] Wrote {OUT_DIR / 'ensemble_results.json'}")
print(f"[P3-D] TOTAL runtime {time.time()-t0:.1f}s")
print("[P3-D] DONE")
