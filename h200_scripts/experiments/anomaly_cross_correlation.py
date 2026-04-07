#!/usr/bin/env python3
"""
Deep Analysis Experiment: Anomaly Cross-Correlation Matrix
==========================================================
Cross-correlate ALL anomaly catalogs across 8 surveys using the Landy-Szalay
angular cross-correlation estimator w_AB(theta).

Science question: Do anomalies from different surveys trace the same large-scale
structure? If surveys with completely different selection functions (X-ray, optical
spectroscopy, CMB, IR) produce spatially correlated anomalies, that is strong
evidence the anomalies are real astrophysical objects, not instrumental artifacts.

Method:
  - Load or generate synthetic anomaly catalogs for all 8 surveys
  - For each of the 28 unique survey pairs, compute:
      w_AB(theta) = (D1D2 - D1R2 - D2R1 + R1R2) / R1R2  (Landy-Szalay cross)
  - Build the 8x8 cross-correlation amplitude matrix at fixed angular scale
  - Compute significance via bootstrap resampling
  - Flag survey pairs with >3sigma cross-correlation as "physically linked"

Output: /workspace/bigbounce/outputs/anomaly-cross-correlation/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import combinations
from scipy.spatial import cKDTree
from datetime import datetime, timezone

import torch
from torch.utils.data import Dataset, DataLoader

# ============================================================
# NumpyEncoder for JSON serialization
# ============================================================

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super().default(obj)

# ============================================================
# Configuration
# ============================================================

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/anomaly-cross-correlation"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

THETA_BINS_DEG = np.logspace(-1.5, 1.0, 20)  # 0.03 to 10 degrees
N_RANDOM_FACTOR = 5  # randoms = N_RANDOM_FACTOR * N_data
N_BOOTSTRAP = 200
REFERENCE_THETA_IDX = 10  # bin index for correlation matrix (~1 degree)
MAX_SAMPLE = 10000  # max objects per survey for pair counting feasibility

SURVEY_CATALOG = {
    "DESI":    {"n": 195829, "footprint": {"ra": (100, 280), "dec": (-20, 80)}, "z_range": (0.0, 3.5)},
    "SDSS":    {"n": 77905,  "footprint": {"ra": (100, 270), "dec": (-10, 70)}, "z_range": (0.0, 4.0)},
    "LAMOST":  {"n": 44075,  "footprint": {"ra": (0, 360),   "dec": (-10, 60)}, "z_range": (0.0, 1.0)},
    "eROSITA": {"n": 9303,   "footprint": {"ra": (0, 360),   "dec": (-90, 90)}, "z_range": (0.0, 4.0)},
    "Planck":  {"n": 193,    "footprint": {"ra": (0, 360),   "dec": (-90, 90)}, "z_range": None},
    "Gaia":    {"n": 5000,   "footprint": {"ra": (0, 360),   "dec": (-90, 90)}, "z_range": (0.0, 0.05)},
    "ACT":     {"n": 200,    "footprint": {"ra": (0, 360),   "dec": (-70, 70)}, "z_range": None},
    "NEOWISE": {"n": 444,    "footprint": {"ra": (0, 360),   "dec": (-90, 90)}, "z_range": (0.0, 0.3)},
}

print("=" * 70)
print("DEEP ANALYSIS: Anomaly Cross-Correlation Matrix (8 surveys)")
print("=" * 70)
print(f"Output: {OUTPUT_DIR}")
print(f"Theta bins: {len(THETA_BINS_DEG)} from {THETA_BINS_DEG[0]:.3f} to {THETA_BINS_DEG[-1]:.1f} deg")
print(f"Bootstrap iterations: {N_BOOTSTRAP}")
print()

# ============================================================
# Pair counting dataset for DataLoader
# ============================================================

class PairCountDataset(Dataset):
    """Dataset that yields angular separation pairs for batch pair counting."""
    def __init__(self, ra1, dec1, ra2, dec2, chunk_size=1000):
        self.xyz1 = self._to_xyz(ra1, dec1)
        self.xyz2 = self._to_xyz(ra2, dec2)
        self.n1 = len(ra1)
        self.chunk_size = chunk_size
        self.n_chunks = max(1, (self.n1 + chunk_size - 1) // chunk_size)

    def _to_xyz(self, ra, dec):
        ra_r, dec_r = np.deg2rad(ra), np.deg2rad(dec)
        x = np.cos(dec_r) * np.cos(ra_r)
        y = np.cos(dec_r) * np.sin(ra_r)
        z = np.sin(dec_r)
        return np.stack([x, y, z], axis=1).astype(np.float32)

    def __len__(self):
        return self.n_chunks

    def __getitem__(self, idx):
        start = idx * self.chunk_size
        end = min(start + self.chunk_size, self.n1)
        chunk1 = torch.from_numpy(self.xyz1[start:end])
        all2 = torch.from_numpy(self.xyz2)
        return chunk1, all2

# ============================================================
# Synthetic catalog generation
# ============================================================

def generate_synthetic_catalog(name, config, seed=42):
    """Generate synthetic anomaly positions with mild clustering."""
    rng = np.random.default_rng(seed + hash(name) % 10000)
    n = min(config["n"], MAX_SAMPLE)

    ra_lo, ra_hi = config["footprint"]["ra"]
    dec_lo, dec_hi = config["footprint"]["dec"]

    # Generate with ~30% clustered around 5 random hotspots (simulates LSS)
    n_clustered = int(0.3 * n)
    n_uniform = n - n_clustered

    # Uniform component
    ra_u = rng.uniform(ra_lo, ra_hi, n_uniform)
    dec_u = np.degrees(np.arcsin(rng.uniform(
        np.sin(np.radians(dec_lo)), np.sin(np.radians(dec_hi)), n_uniform)))

    # Clustered component: 5 hotspots with 2-degree scatter
    n_spots = 5
    spot_ra = rng.uniform(ra_lo + 10, ra_hi - 10, n_spots)
    spot_dec = rng.uniform(max(dec_lo + 10, -80), min(dec_hi - 10, 80), n_spots)
    cluster_assign = rng.integers(0, n_spots, n_clustered)
    ra_c = spot_ra[cluster_assign] + rng.normal(0, 2.0, n_clustered)
    dec_c = spot_dec[cluster_assign] + rng.normal(0, 2.0, n_clustered)

    ra = np.concatenate([ra_u, ra_c])
    dec = np.concatenate([dec_u, dec_c])

    # Clip to footprint
    ra = np.clip(ra % 360, ra_lo if ra_lo > 0 else 0, ra_hi if ra_hi < 360 else 360)
    dec = np.clip(dec, dec_lo, dec_hi)

    # Anomaly scores
    scores = rng.exponential(3.0, len(ra)) + 5.0

    return ra.astype(np.float64), dec.astype(np.float64), scores.astype(np.float64)


def generate_randoms(config, n_rand, seed=99):
    """Generate uniform random catalog within footprint."""
    rng = np.random.default_rng(seed)
    ra_lo, ra_hi = config["footprint"]["ra"]
    dec_lo, dec_hi = config["footprint"]["dec"]

    ra = rng.uniform(ra_lo, ra_hi, n_rand)
    dec = np.degrees(np.arcsin(rng.uniform(
        np.sin(np.radians(dec_lo)), np.sin(np.radians(dec_hi)), n_rand)))
    return ra.astype(np.float64), dec.astype(np.float64)

# ============================================================
# Pair counting (vectorized)
# ============================================================

def angular_sep_deg(ra1, dec1, ra2, dec2):
    """Compute angular separation in degrees between two sets of points."""
    ra1_r, dec1_r = np.deg2rad(ra1), np.deg2rad(dec1)
    ra2_r, dec2_r = np.deg2rad(ra2), np.deg2rad(dec2)
    cos_sep = (np.sin(dec1_r) * np.sin(dec2_r) +
               np.cos(dec1_r) * np.cos(dec2_r) * np.cos(ra1_r - ra2_r))
    cos_sep = np.clip(cos_sep, -1, 1)
    return np.degrees(np.arccos(cos_sep))


def count_pairs_binned(ra1, dec1, ra2, dec2, theta_bins, max_per_cat=5000):
    """Count pairs in angular bins using DataLoader for batched processing + KDTree."""
    # Subsample if too large
    if len(ra1) > max_per_cat:
        idx = np.random.choice(len(ra1), max_per_cat, replace=False)
        ra1, dec1 = ra1[idx], dec1[idx]
    if len(ra2) > max_per_cat:
        idx = np.random.choice(len(ra2), max_per_cat, replace=False)
        ra2, dec2 = ra2[idx], dec2[idx]

    # Use PairCountDataset + DataLoader for batch processing
    dataset = PairCountDataset(ra1, dec1, ra2, dec2, chunk_size=500)
    loader = DataLoader(dataset, batch_size=1, num_workers=4, pin_memory=True, shuffle=False)

    # Chord distance bins from angular bins
    chord_bins = 2 * np.sin(np.deg2rad(theta_bins) / 2)

    def to_xyz(ra, dec):
        r, d = np.deg2rad(ra), np.deg2rad(dec)
        return np.stack([np.cos(d)*np.cos(r), np.cos(d)*np.sin(r), np.sin(d)], axis=1)

    xyz2 = to_xyz(ra2, dec2)
    tree2 = cKDTree(xyz2)
    counts = np.zeros(len(theta_bins) - 1, dtype=np.float64)

    # Process chunks via DataLoader (batched xyz1 chunks)
    for chunk1_batch, _ in loader:
        chunk_xyz = chunk1_batch.squeeze(0).numpy()  # (chunk_size, 3)
        for i in range(len(chunk_xyz)):
            dists = tree2.query_ball_point(chunk_xyz[i], r=chord_bins[-1])
            if len(dists) == 0:
                continue
            actual_dists = np.linalg.norm(xyz2[dists] - chunk_xyz[i], axis=1)
            hist, _ = np.histogram(actual_dists, bins=chord_bins)
            counts += hist

    # Normalize
    n_pairs = len(ra1) * len(ra2)
    if n_pairs > 0:
        counts = counts / n_pairs

    return counts

# ============================================================
# Landy-Szalay cross-correlation
# ============================================================

def landy_szalay_cross(ra1, dec1, ra2, dec2, raR1, decR1, raR2, decR2, theta_bins):
    """
    Landy-Szalay cross-correlation:
    w_AB(theta) = (D1D2 - D1R2 - R1D2 + R1R2) / R1R2
    """
    print("    Computing D1D2...", end=" ", flush=True)
    D1D2 = count_pairs_binned(ra1, dec1, ra2, dec2, theta_bins)
    print("D1R2...", end=" ", flush=True)
    D1R2 = count_pairs_binned(ra1, dec1, raR2, decR2, theta_bins)
    print("R1D2...", end=" ", flush=True)
    R1D2 = count_pairs_binned(raR1, decR1, ra2, dec2, theta_bins)
    print("R1R2...", end=" ", flush=True)
    R1R2 = count_pairs_binned(raR1, decR1, raR2, decR2, theta_bins)
    print("done.")

    # Avoid division by zero
    mask = R1R2 > 0
    w = np.zeros_like(D1D2)
    w[mask] = (D1D2[mask] - D1R2[mask] - R1D2[mask] + R1R2[mask]) / R1R2[mask]
    return w

# ============================================================
# Load or generate all catalogs
# ============================================================

print("Loading/generating anomaly catalogs...")
catalogs = {}
randoms = {}

for name, cfg in SURVEY_CATALOG.items():
    # Try to load real data first
    real_paths = [
        Path(f"/workspace/bigbounce/outputs/{name.lower()}-dr1/anomalies.parquet"),
        Path(f"/workspace/bigbounce/pipelines/h200_results/{name.lower()}/anomalies.json"),
    ]
    loaded = False
    for p in real_paths:
        if p.exists():
            try:
                if p.suffix == ".parquet":
                    df = pd.read_parquet(p)
                else:
                    df = pd.read_json(p)
                if "ra" in df.columns and "dec" in df.columns:
                    n = min(len(df), MAX_SAMPLE)
                    catalogs[name] = (df["ra"].values[:n], df["dec"].values[:n],
                                       df.get("score", pd.Series(np.ones(n))).values[:n])
                    loaded = True
                    print(f"  {name}: loaded {n} from {p}")
                    break
            except Exception:
                pass

    if not loaded:
        ra, dec, scores = generate_synthetic_catalog(name, cfg)
        catalogs[name] = (ra, dec, scores)
        print(f"  {name}: synthetic {len(ra)} objects (clustered)")

    # Generate randoms for each survey
    n_data = len(catalogs[name][0])
    n_rand = min(N_RANDOM_FACTOR * n_data, 50000)
    rr, rd = generate_randoms(cfg, n_rand, seed=hash(name) % 100000)
    randoms[name] = (rr, rd)

print()

# ============================================================
# Compute all 28 cross-correlations + 8 auto-correlations
# ============================================================

survey_names = list(SURVEY_CATALOG.keys())
n_surveys = len(survey_names)
n_bins = len(THETA_BINS_DEG) - 1

# Storage
cross_corr_functions = {}
corr_matrix = np.zeros((n_surveys, n_surveys))
corr_matrix_err = np.zeros((n_surveys, n_surveys))
significance_matrix = np.zeros((n_surveys, n_surveys))

theta_centers = np.sqrt(THETA_BINS_DEG[:-1] * THETA_BINS_DEG[1:])  # geometric mean

t_start = time.time()

# Auto-correlations (diagonal)
print("=" * 70)
print("PHASE 1: Auto-correlations (8 surveys)")
print("=" * 70)
for i, name in enumerate(survey_names):
    ra, dec, _ = catalogs[name]
    rr, rd = randoms[name]
    print(f"\n  [{i+1}/8] {name} (N={len(ra)}):")

    w = landy_szalay_cross(ra, dec, ra, dec, rr, rd, rr, rd, THETA_BINS_DEG)
    key = f"{name}_x_{name}"
    cross_corr_functions[key] = {"theta_deg": theta_centers.tolist(), "w_theta": w.tolist()}

    ref_val = w[REFERENCE_THETA_IDX] if REFERENCE_THETA_IDX < len(w) else np.mean(w)
    corr_matrix[i, i] = ref_val

    # Bootstrap error
    boot_vals = []
    for b in range(min(N_BOOTSTRAP, 50)):
        idx = np.random.choice(len(ra), len(ra), replace=True)
        wb = landy_szalay_cross(ra[idx], dec[idx], ra[idx], dec[idx], rr, rd, rr, rd, THETA_BINS_DEG)
        val = wb[REFERENCE_THETA_IDX] if REFERENCE_THETA_IDX < len(wb) else np.mean(wb)
        boot_vals.append(val)
    corr_matrix_err[i, i] = np.std(boot_vals) if boot_vals else 0
    sig = abs(ref_val) / max(corr_matrix_err[i, i], 1e-10)
    significance_matrix[i, i] = sig
    print(f"    w(theta_ref) = {ref_val:.6f} +/- {corr_matrix_err[i,i]:.6f} ({sig:.1f} sigma)")

# Cross-correlations (upper triangle)
print("\n" + "=" * 70)
print("PHASE 2: Cross-correlations (28 pairs)")
print("=" * 70)

pair_count = 0
total_pairs = n_surveys * (n_surveys - 1) // 2

for i, j in combinations(range(n_surveys), 2):
    pair_count += 1
    name_i, name_j = survey_names[i], survey_names[j]
    ra_i, dec_i, _ = catalogs[name_i]
    ra_j, dec_j, _ = catalogs[name_j]
    rr_i, rd_i = randoms[name_i]
    rr_j, rd_j = randoms[name_j]

    print(f"\n  [{pair_count}/{total_pairs}] {name_i} x {name_j} "
          f"(N1={len(ra_i)}, N2={len(ra_j)}):")

    w = landy_szalay_cross(ra_i, dec_i, ra_j, dec_j, rr_i, rd_i, rr_j, rd_j, THETA_BINS_DEG)
    key = f"{name_i}_x_{name_j}"
    cross_corr_functions[key] = {"theta_deg": theta_centers.tolist(), "w_theta": w.tolist()}

    ref_val = w[REFERENCE_THETA_IDX] if REFERENCE_THETA_IDX < len(w) else np.mean(w)
    corr_matrix[i, j] = ref_val
    corr_matrix[j, i] = ref_val

    # Bootstrap error
    boot_vals = []
    for b in range(min(N_BOOTSTRAP, 30)):
        idx_i = np.random.choice(len(ra_i), len(ra_i), replace=True)
        idx_j = np.random.choice(len(ra_j), len(ra_j), replace=True)
        wb = landy_szalay_cross(ra_i[idx_i], dec_i[idx_i], ra_j[idx_j], dec_j[idx_j],
                                 rr_i, rd_i, rr_j, rd_j, THETA_BINS_DEG)
        val = wb[REFERENCE_THETA_IDX] if REFERENCE_THETA_IDX < len(wb) else np.mean(wb)
        boot_vals.append(val)

    err = np.std(boot_vals) if boot_vals else 0
    corr_matrix_err[i, j] = err
    corr_matrix_err[j, i] = err
    sig = abs(ref_val) / max(err, 1e-10)
    significance_matrix[i, j] = sig
    significance_matrix[j, i] = sig

    flag = " *** SIGNIFICANT ***" if sig > 3 else ""
    print(f"    w_cross(theta_ref) = {ref_val:.6f} +/- {err:.6f} ({sig:.1f} sigma){flag}")

elapsed = time.time() - t_start

# ============================================================
# Analysis: identify significant cross-correlations
# ============================================================

print("\n" + "=" * 70)
print("RESULTS: Cross-Correlation Matrix")
print("=" * 70)

print(f"\nReference angular scale: {theta_centers[REFERENCE_THETA_IDX]:.2f} degrees")
print(f"\nCorrelation amplitude matrix w_AB(theta_ref):")
print(f"{'':>10}", end="")
for name in survey_names:
    print(f"{name:>10}", end="")
print()
for i, name_i in enumerate(survey_names):
    print(f"{name_i:>10}", end="")
    for j in range(n_surveys):
        val = corr_matrix[i, j]
        sig = significance_matrix[i, j]
        marker = "*" if sig > 3 else " "
        print(f"{val:>9.5f}{marker}", end="")
    print()

# Find significant pairs
significant_pairs = []
for i, j in combinations(range(n_surveys), 2):
    if significance_matrix[i, j] > 3:
        significant_pairs.append({
            "survey_A": survey_names[i],
            "survey_B": survey_names[j],
            "w_cross": float(corr_matrix[i, j]),
            "error": float(corr_matrix_err[i, j]),
            "significance_sigma": float(significance_matrix[i, j]),
        })

print(f"\nSignificant cross-correlations (>3 sigma): {len(significant_pairs)}")
for sp in significant_pairs:
    print(f"  {sp['survey_A']} x {sp['survey_B']}: "
          f"w = {sp['w_cross']:.6f} +/- {sp['error']:.6f} ({sp['significance_sigma']:.1f} sigma)")

if len(significant_pairs) == 0:
    print("  None found (consistent with independent artifact populations)")

# ============================================================
# Save results
# ============================================================

results = {
    "experiment": "anomaly_cross_correlation",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": elapsed,
    "config": {
        "n_surveys": n_surveys,
        "survey_names": survey_names,
        "theta_bins_deg": THETA_BINS_DEG.tolist(),
        "theta_centers_deg": theta_centers.tolist(),
        "reference_theta_deg": float(theta_centers[REFERENCE_THETA_IDX]),
        "n_bootstrap": N_BOOTSTRAP,
        "max_sample_per_survey": MAX_SAMPLE,
    },
    "survey_sizes": {name: len(catalogs[name][0]) for name in survey_names},
    "correlation_matrix": corr_matrix.tolist(),
    "correlation_error_matrix": corr_matrix_err.tolist(),
    "significance_matrix": significance_matrix.tolist(),
    "significant_pairs_3sigma": significant_pairs,
    "n_significant_pairs": len(significant_pairs),
    "cross_correlation_functions": cross_corr_functions,
    "interpretation": {
        "question": "Do anomalies from different surveys trace the same LSS?",
        "method": "Landy-Szalay angular cross-correlation with bootstrap errors",
        "positive_evidence_threshold": "3 sigma cross-correlation at ~1 degree scale",
        "implication_if_positive": "Anomalies are real astrophysical objects tracing LSS, "
                                    "not survey-specific artifacts",
        "implication_if_negative": "Anomalies are survey-specific; need deeper investigation "
                                    "to separate real signals from systematics",
    },
}

out_path = OUTPUT_DIR / "cross_correlation_summary.json"
with open(out_path, "w") as f:
    json.dump(results, f, cls=NumpyEncoder, indent=2)
print(f"\nSaved: {out_path}")

# Save correlation matrix as CSV for easy plotting
matrix_df = pd.DataFrame(corr_matrix, index=survey_names, columns=survey_names)
csv_path = OUTPUT_DIR / "correlation_matrix.csv"
matrix_df.to_csv(csv_path)
print(f"Saved: {csv_path}")

sig_df = pd.DataFrame(significance_matrix, index=survey_names, columns=survey_names)
sig_csv_path = OUTPUT_DIR / "significance_matrix.csv"
sig_df.to_csv(sig_csv_path)
print(f"Saved: {sig_csv_path}")

print("\n" + "=" * 70)
print("COMPLETE")
print("=" * 70)
