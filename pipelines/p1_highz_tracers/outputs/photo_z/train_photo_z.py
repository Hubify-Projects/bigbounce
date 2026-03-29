"""
Latent-space photo-z prediction: Can autoencoder embeddings predict spectroscopic redshift?

Trains HistGradientBoosting and MLP regressors on the 128-dim latent vectors
from the spectral autoencoder, predicting spectroscopic redshift z.

HistGradientBoosting is used instead of RandomForest for speed — it uses
histogram-based binning which is O(N) rather than O(N log N) per split,
making it 10-50x faster on large datasets while typically performing better.

This tests whether the autoencoder's internal representation encodes redshift
information — a novel ML contribution showing the latent space is
physically meaningful.
"""

import json
import sys
import time
import glob
import numpy as np
import pyarrow.parquet as pq
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

# ── Config ──────────────────────────────────────────────────────────────
DATA_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped"
OUT_DIR  = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/photo_z"
SAMPLE_N = 1_000_000
SEED     = 42

LAT_COLS = [f"lat_{i:03d}" for i in range(128)]
NEEDED   = LAT_COLS + ["z", "zwarn", "median_coadd_snr_r"]

# ── 1. Load & filter ───────────────────────────────────────────────────
print("=" * 60)
print("STEP 1: Loading and filtering data")
print("=" * 60)

files = sorted(glob.glob(f"{DATA_DIR}/desi_dr1_catalog_batch_*.parquet"))
print(f"  Found {len(files)} parquet files")

chunks = []
total_raw = 0
for i, f in enumerate(files):
    df = pq.read_table(f, columns=NEEDED).to_pandas()
    total_raw += len(df)
    # Quality filter: ZWARN=0, SNR_r > 2, valid z
    mask = (df["zwarn"] == 0) & (df["median_coadd_snr_r"] > 2) & (df["z"] > 0) & (df["z"].notna())
    df = df.loc[mask]
    chunks.append(df)
    if (i + 1) % 10 == 0:
        n_so_far = sum(len(c) for c in chunks)
        print(f"  ... processed {i+1}/{len(files)} files, {n_so_far:,} good objects so far")

data = pd.concat(chunks, ignore_index=True)
del chunks  # free memory
print(f"  Total raw objects scanned: {total_raw:,}")
print(f"  After quality filter (ZWARN=0, SNR_r>2, z>0): {len(data):,}")

# Drop any rows with NaN in latent columns
data = data.dropna(subset=LAT_COLS)
print(f"  After dropping NaN latents: {len(data):,}")

# Sample 1M
if len(data) > SAMPLE_N:
    data = data.sample(n=SAMPLE_N, random_state=SEED).reset_index(drop=True)
    print(f"  Sampled down to: {len(data):,}")
else:
    print(f"  Using all {len(data):,} objects (fewer than {SAMPLE_N:,})")

# ── 2. Prepare features ────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 2: Preparing features and splitting")
print("=" * 60)

X = data[LAT_COLS].values.astype(np.float32)
y = data["z"].values.astype(np.float64)
del data  # free memory

print(f"  Feature matrix: {X.shape}")
print(f"  Target z range: [{y.min():.4f}, {y.max():.4f}]")
print(f"  Target z mean:  {y.mean():.4f}")
print(f"  Target z median: {np.median(y):.4f}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)
print(f"  Train: {len(X_train):,}  |  Test: {len(X_test):,}")

# ── 3a. HistGradientBoosting ───────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3a: Training HistGradientBoostingRegressor")
print("=" * 60)

t0 = time.time()
hgb = HistGradientBoostingRegressor(
    max_iter=300,
    max_depth=15,
    learning_rate=0.05,
    min_samples_leaf=20,
    max_bins=255,
    validation_fraction=0.1,
    n_iter_no_change=15,
    early_stopping=True,
    random_state=SEED,
    verbose=1
)
hgb.fit(X_train, y_train)
hgb_time = time.time() - t0
print(f"  Training time: {hgb_time:.1f}s")
print(f"  Iterations used: {hgb.n_iter_}")

y_pred_hgb = hgb.predict(X_test)

# ── 3b. MLP Regressor ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3b: Training MLPRegressor (3 hidden layers)")
print("=" * 60)

t0 = time.time()
mlp = MLPRegressor(
    hidden_layer_sizes=(256, 128, 64),
    activation="relu",
    solver="adam",
    max_iter=200,
    early_stopping=True,
    validation_fraction=0.1,
    n_iter_no_change=15,
    random_state=SEED,
    verbose=True,
    batch_size=4096,
    learning_rate_init=0.001
)
mlp.fit(X_train, y_train)
mlp_time = time.time() - t0
print(f"  Training time: {mlp_time:.1f}s")
print(f"  Iterations used: {mlp.n_iter_}")

y_pred_mlp = mlp.predict(X_test)

# ── 4. Evaluate ────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 4: Evaluation")
print("=" * 60)

def evaluate(y_true, y_pred, name):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    # Normalized residual
    delta_z_norm = np.abs(y_pred - y_true) / (1.0 + y_true)
    outlier_frac = np.mean(delta_z_norm > 0.15)
    sigma_nmad = 1.4826 * np.median(np.abs(delta_z_norm - np.median(delta_z_norm)))
    bias = np.mean((y_pred - y_true) / (1.0 + y_true))

    print(f"\n  --- {name} ---")
    print(f"  MAE:            {mae:.5f}")
    print(f"  RMSE:           {rmse:.5f}")
    print(f"  R^2:            {r2:.5f}")
    print(f"  sigma_NMAD:     {sigma_nmad:.5f}")
    print(f"  bias:           {bias:.6f}")
    print(f"  Outlier frac:   {outlier_frac:.4f}  ({outlier_frac*100:.2f}%)")

    return {
        "mae": float(mae),
        "rmse": float(rmse),
        "r2": float(r2),
        "sigma_nmad": float(sigma_nmad),
        "bias": float(bias),
        "outlier_fraction_015": float(outlier_frac),
    }

hgb_metrics = evaluate(y_test, y_pred_hgb, "HistGradientBoosting")
mlp_metrics = evaluate(y_test, y_pred_mlp, "MLP (256-128-64)")

# ── 5. Plots ───────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 5: Generating plots")
print("=" * 60)

# Use whichever model is better for the main plots
best_name = "HistGradientBoosting" if hgb_metrics["rmse"] < mlp_metrics["rmse"] else "MLP"
y_pred_best = y_pred_hgb if best_name == "HistGradientBoosting" else y_pred_mlp
best_metrics = hgb_metrics if best_name == "HistGradientBoosting" else mlp_metrics

# --- Scatter plot: z_pred vs z_true ---
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

for ax, (name, yp, met) in zip(axes, [
    ("HistGradientBoosting", y_pred_hgb, hgb_metrics),
    ("MLP (256-128-64)", y_pred_mlp, mlp_metrics)
]):
    zmax = min(max(float(y_test.max()), float(np.max(yp)), 4), 6)
    h = ax.hist2d(y_test, yp, bins=200, cmap="inferno",
                  range=[[0, zmax], [0, zmax]],
                  norm=matplotlib.colors.LogNorm())
    ax.plot([0, zmax], [0, zmax], "w--", lw=1.5, alpha=0.8, label="Perfect prediction")
    ax.set_xlabel("Spectroscopic z (true)", fontsize=13)
    ax.set_ylabel("Predicted z", fontsize=13)
    ax.set_title(f"{name}\nMAE={met['mae']:.4f}  RMSE={met['rmse']:.4f}  "
                 f"R$^2$={met['r2']:.4f}  $\\eta_{{0.15}}$={met['outlier_fraction_015']:.3f}",
                 fontsize=11)
    ax.set_aspect("equal")
    ax.legend(fontsize=10)
    plt.colorbar(h[3], ax=ax, label="Count")

fig.suptitle("Autoencoder Latent Space $\\rightarrow$ Spectroscopic Redshift Prediction\n"
             "128-dim latent vectors from DESI DR1 spectral autoencoder (1M objects)",
             fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/photo_z_scatter.png", dpi=200, bbox_inches="tight")
print(f"  Saved: {OUT_DIR}/photo_z_scatter.png")
plt.close()

# --- Residual histogram ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

for ax, (name, yp, met) in zip(axes, [
    ("HistGradientBoosting", y_pred_hgb, hgb_metrics),
    ("MLP (256-128-64)", y_pred_mlp, mlp_metrics)
]):
    delta = (yp - y_test) / (1.0 + y_test)
    ax.hist(delta, bins=200, range=(-0.5, 0.5), density=True,
            alpha=0.8, color="#2563eb", edgecolor="none")
    ax.axvline(0, color="red", ls="--", lw=1.5)
    ax.axvline(-0.15, color="orange", ls=":", lw=1.2, label="Outlier threshold (0.15)")
    ax.axvline(0.15, color="orange", ls=":", lw=1.2)
    ax.set_xlabel("$\\Delta z / (1 + z_{\\rm true})$", fontsize=13)
    ax.set_ylabel("Density", fontsize=13)
    ax.set_title(f"{name}\n$\\sigma_{{NMAD}}$={met['sigma_nmad']:.5f}  "
                 f"bias={met['bias']:.5f}  "
                 f"$\\eta_{{0.15}}$={met['outlier_fraction_015']:.3f}",
                 fontsize=11)
    ax.legend(fontsize=10)

fig.suptitle("Normalized Redshift Residuals\n"
             "128-dim autoencoder latent space predictions",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/photo_z_residuals.png", dpi=200, bbox_inches="tight")
print(f"  Saved: {OUT_DIR}/photo_z_residuals.png")
plt.close()

# --- Feature importance (HGB permutation-based) ---
print("  Computing feature importances via permutation (sample)...")
from sklearn.inspection import permutation_importance
perm_result = permutation_importance(
    hgb, X_test[:50000], y_test[:50000],
    n_repeats=5, random_state=SEED, n_jobs=-1
)
importances = perm_result.importances_mean

fig, ax = plt.subplots(figsize=(14, 5))
top_k = 30
top_idx = np.argsort(importances)[-top_k:][::-1]
ax.bar(range(top_k), importances[top_idx], color="#2563eb", alpha=0.8)
ax.set_xticks(range(top_k))
ax.set_xticklabels([f"lat_{i:03d}" for i in top_idx], rotation=45, ha="right", fontsize=9)
ax.set_xlabel("Latent dimension", fontsize=12)
ax.set_ylabel("Permutation importance (MAE increase)", fontsize=12)
ax.set_title(f"Top {top_k} Latent Dimensions for Redshift Prediction (HistGradientBoosting)",
             fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/photo_z_feature_importance.png", dpi=200, bbox_inches="tight")
print(f"  Saved: {OUT_DIR}/photo_z_feature_importance.png")
plt.close()

# ── 6. Save metrics ────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 6: Saving metrics")
print("=" * 60)

metrics_out = {
    "description": "Predicting spectroscopic redshift from 128-dim autoencoder latent vectors",
    "data": {
        "source": DATA_DIR,
        "n_files": len(files),
        "total_raw": total_raw,
        "n_after_quality_filter": SAMPLE_N,
        "quality_cuts": "ZWARN=0, median_coadd_snr_r > 2, z > 0",
        "n_features": 128,
        "feature_columns": "lat_000 through lat_127",
        "train_size": int(len(X_train)),
        "test_size": int(len(X_test)),
        "z_range": [float(y.min()), float(y.max())],
        "z_mean": float(y.mean()),
        "z_median": float(np.median(y)),
    },
    "models": {
        "HistGradientBoosting": {
            "params": {"max_iter": 300, "max_depth": 15, "learning_rate": 0.05,
                       "min_samples_leaf": 20, "early_stopping": True},
            "training_time_s": round(hgb_time, 1),
            "n_iter": int(hgb.n_iter_),
            **hgb_metrics,
            "top_10_features": [
                {"dim": f"lat_{i:03d}", "importance": float(importances[i])}
                for i in np.argsort(importances)[-10:][::-1]
            ]
        },
        "MLP": {
            "params": {"hidden_layers": [256, 128, 64], "activation": "relu",
                       "max_iter": 200, "batch_size": 4096, "learning_rate_init": 0.001},
            "training_time_s": round(mlp_time, 1),
            "n_iter": int(mlp.n_iter_),
            **mlp_metrics
        }
    },
    "best_model": best_name,
    "plots": [
        f"{OUT_DIR}/photo_z_scatter.png",
        f"{OUT_DIR}/photo_z_residuals.png",
        f"{OUT_DIR}/photo_z_feature_importance.png"
    ]
}

with open(f"{OUT_DIR}/metrics.json", "w") as f:
    json.dump(metrics_out, f, indent=2)
print(f"  Saved: {OUT_DIR}/metrics.json")

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)
print(f"\n  Best model: {best_name}")
print(f"  MAE:  {best_metrics['mae']:.5f}")
print(f"  RMSE: {best_metrics['rmse']:.5f}")
print(f"  R^2:  {best_metrics['r2']:.5f}")
print(f"  sigma_NMAD: {best_metrics['sigma_nmad']:.5f}")
print(f"  Outlier fraction (|dz/(1+z)| > 0.15): {best_metrics['outlier_fraction_015']:.4f}")
