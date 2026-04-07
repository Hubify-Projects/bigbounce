#!/usr/bin/env python3
"""
Deep Analysis Experiment: Anomaly Redshift Tomography
=====================================================
Bin anomalies by redshift and measure how anomaly properties evolve with cosmic
distance. If anomaly rate increases at high-z, these could be genuinely new
populations missed by standard pipelines (which are trained on local templates).

Science question: Does the anomaly detection rate evolve with redshift? A rising
rate at z>2 would indicate novel astrophysical populations at early cosmic times,
potentially including bounce cosmology relics or pre-bounce signatures.

Method:
  - 6 redshift bins: 0-0.5, 0.5-1, 1-1.5, 1.5-2, 2-3, 3+
  - At each bin: anomaly rate, mean score, clustering bias w(theta), effective volume
  - Synthetic catalogs with redshift-dependent anomaly rates for validation
  - Compare anomaly rate evolution to null expectation (constant comoving density)

Output: /workspace/bigbounce/outputs/redshift-tomography/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.spatial import cKDTree
from scipy.optimize import curve_fit
from scipy.stats import ks_2samp, chi2
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/redshift-tomography"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

Z_BIN_EDGES = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 6.0]
Z_BIN_LABELS = ["0.0-0.5", "0.5-1.0", "1.0-1.5", "1.5-2.0", "2.0-3.0", "3.0+"]

THETA_BINS_DEG = np.logspace(-1.5, 0.5, 12)
N_RANDOM = 50000
MAX_PER_BIN = 5000

# Survey configs with redshift capabilities
SPECTRO_SURVEYS = {
    "DESI":   {"n_anom": 195829, "n_total": 22_500_000, "z_max": 3.5,
               "footprint": {"ra": (100, 280), "dec": (-20, 80)}},
    "SDSS":   {"n_anom": 77905,  "n_total": 2_300_000,  "z_max": 4.0,
               "footprint": {"ra": (100, 270), "dec": (-10, 70)}},
    "LAMOST": {"n_anom": 44075,  "n_total": 11_400_000, "z_max": 1.0,
               "footprint": {"ra": (0, 360), "dec": (-10, 60)}},
    "eROSITA":{"n_anom": 9303,   "n_total": 930_000,    "z_max": 4.0,
               "footprint": {"ra": (0, 360), "dec": (-90, 90)}},
}

# Cosmological parameters for comoving volume
H0 = 67.68  # km/s/Mpc
OMEGA_M = 0.3111
OMEGA_L = 1.0 - OMEGA_M
C_OVER_H0 = 2997.92458 / (H0 / 100)  # Mpc/h -> Mpc

print("=" * 70)
print("DEEP ANALYSIS: Anomaly Redshift Tomography")
print("=" * 70)
print(f"Output: {OUTPUT_DIR}")
print(f"Redshift bins: {Z_BIN_LABELS}")
print()

# ============================================================
# Cosmological functions
# ============================================================

def comoving_distance(z, n_steps=1000):
    """Compute comoving distance d_C(z) in Mpc via numerical integration."""
    z_arr = np.linspace(0, z, n_steps)
    dz = z / n_steps
    E_z = np.sqrt(OMEGA_M * (1 + z_arr)**3 + OMEGA_L)
    integrand = 1.0 / E_z
    return C_OVER_H0 * np.trapz(integrand, z_arr)


def comoving_volume_shell(z1, z2, sky_fraction=1.0):
    """Comoving volume between z1 and z2 in (Mpc/h)^3."""
    d1 = comoving_distance(z1)
    d2 = comoving_distance(z2)
    vol = (4.0 / 3.0) * np.pi * (d2**3 - d1**3) * sky_fraction
    return vol

# ============================================================
# Redshift-weighted synthetic catalog generator
# ============================================================

class RedshiftCatalogDataset(Dataset):
    """Dataset for batch generation of synthetic spectra with redshift info."""
    def __init__(self, n_objects, z_max, anomaly_rate_func, seed=42):
        self.n = n_objects
        self.z_max = z_max
        self.anomaly_rate_func = anomaly_rate_func
        rng = np.random.default_rng(seed)

        # Generate redshifts from a realistic n(z) distribution
        # n(z) ~ z^2 * exp(-z/z0) with z0 ~ z_max/3
        z0 = z_max / 3.0
        z_grid = np.linspace(0.01, z_max, 10000)
        nz = z_grid**2 * np.exp(-z_grid / z0)
        nz /= nz.sum()
        self.redshifts = rng.choice(z_grid, size=n_objects, p=nz).astype(np.float32)

        # Assign anomaly status with z-dependent rate
        rates = np.array([anomaly_rate_func(z) for z in self.redshifts])
        self.is_anomaly = rng.random(n_objects) < rates
        self.scores = np.where(self.is_anomaly,
                               rng.exponential(3.0, n_objects) + 5.0,
                               rng.exponential(0.5, n_objects)).astype(np.float32)

    def __len__(self):
        return self.n

    def __getitem__(self, idx):
        return (torch.tensor(self.redshifts[idx]),
                torch.tensor(self.scores[idx]),
                torch.tensor(float(self.is_anomaly[idx])))


def anomaly_rate_rising(z):
    """Anomaly rate that rises with redshift (the interesting scenario)."""
    # Base rate 0.5%, rising to 5% at z=3+
    return 0.005 + 0.015 * z


def anomaly_rate_flat(z):
    """Constant anomaly rate (null hypothesis)."""
    return 0.01


def generate_survey_with_redshifts(name, cfg, seed=42):
    """Generate full synthetic survey with redshift-dependent anomalies."""
    rng = np.random.default_rng(seed + hash(name) % 10000)
    n_total = min(cfg["n_total"], 500000)  # cap for speed
    z_max = cfg["z_max"]

    # Use DataLoader for batch generation
    dataset = RedshiftCatalogDataset(n_total, z_max, anomaly_rate_rising, seed=seed + hash(name) % 10000)
    loader = DataLoader(dataset, batch_size=10000, num_workers=4, pin_memory=True, shuffle=False)

    all_z, all_scores, all_is_anom = [], [], []
    for batch_z, batch_s, batch_a in loader:
        all_z.append(batch_z.numpy())
        all_scores.append(batch_s.numpy())
        all_is_anom.append(batch_a.numpy())

    redshifts = np.concatenate(all_z)
    scores = np.concatenate(all_scores)
    is_anomaly = np.concatenate(all_is_anom).astype(bool)

    # Generate sky positions for anomalies
    n_anom = is_anomaly.sum()
    ra_lo, ra_hi = cfg["footprint"]["ra"]
    dec_lo, dec_hi = cfg["footprint"]["dec"]
    ra = rng.uniform(ra_lo, ra_hi, n_anom)
    dec = np.degrees(np.arcsin(rng.uniform(
        np.sin(np.radians(dec_lo)), np.sin(np.radians(dec_hi)), n_anom)))

    anom_z = redshifts[is_anomaly]
    anom_scores = scores[is_anomaly]

    return {
        "total_objects": n_total,
        "n_anomalies": int(n_anom),
        "anom_ra": ra, "anom_dec": dec,
        "anom_z": anom_z, "anom_scores": anom_scores,
        "all_z": redshifts, "all_is_anomaly": is_anomaly,
    }

# ============================================================
# Clustering measurement per z-bin
# ============================================================

def measure_clustering(ra, dec, footprint, theta_bins):
    """Compute Landy-Szalay auto-correlation for a subset."""
    if len(ra) < 20:
        return np.zeros(len(theta_bins) - 1), 0.0

    n = min(len(ra), MAX_PER_BIN)
    if n < len(ra):
        idx = np.random.choice(len(ra), n, replace=False)
        ra, dec = ra[idx], dec[idx]

    # Generate randoms
    rng = np.random.default_rng(42)
    ra_lo, ra_hi = footprint["ra"]
    dec_lo, dec_hi = footprint["dec"]
    n_rand = min(5 * n, N_RANDOM)
    ra_r = rng.uniform(ra_lo, ra_hi, n_rand)
    dec_r = np.degrees(np.arcsin(rng.uniform(
        np.sin(np.radians(dec_lo)), np.sin(np.radians(dec_hi)), n_rand)))

    def to_xyz(r, d):
        rr, dd = np.deg2rad(r), np.deg2rad(d)
        return np.stack([np.cos(dd)*np.cos(rr), np.cos(dd)*np.sin(rr), np.sin(dd)], axis=1)

    chord_bins = 2 * np.sin(np.deg2rad(theta_bins) / 2)

    # DD
    xyz_d = to_xyz(ra, dec)
    tree_d = cKDTree(xyz_d)
    DD = np.zeros(len(theta_bins) - 1)
    for i in range(len(xyz_d)):
        dists_idx = tree_d.query_ball_point(xyz_d[i], r=chord_bins[-1])
        if len(dists_idx) <= 1:
            continue
        actual = np.linalg.norm(xyz_d[dists_idx] - xyz_d[i], axis=1)
        h, _ = np.histogram(actual[actual > 0], bins=chord_bins)
        DD += h
    DD /= max(len(ra) * (len(ra) - 1) / 2, 1)

    # RR
    xyz_r = to_xyz(ra_r, dec_r)
    tree_r = cKDTree(xyz_r)
    n_rr_sample = min(n_rand, 5000)
    RR = np.zeros(len(theta_bins) - 1)
    for i in range(n_rr_sample):
        dists_idx = tree_r.query_ball_point(xyz_r[i], r=chord_bins[-1])
        if len(dists_idx) <= 1:
            continue
        actual = np.linalg.norm(xyz_r[dists_idx] - xyz_r[i], axis=1)
        h, _ = np.histogram(actual[actual > 0], bins=chord_bins)
        RR += h
    RR /= max(n_rr_sample * (n_rand - 1) / 2, 1)

    # DR
    DR = np.zeros(len(theta_bins) - 1)
    for i in range(len(xyz_d)):
        dists_idx = tree_r.query_ball_point(xyz_d[i], r=chord_bins[-1])
        if len(dists_idx) == 0:
            continue
        actual = np.linalg.norm(xyz_r[dists_idx] - xyz_d[i], axis=1)
        h, _ = np.histogram(actual, bins=chord_bins)
        DR += h
    DR /= max(len(ra) * n_rand, 1)

    mask = RR > 0
    w = np.zeros_like(DD)
    w[mask] = (DD[mask] - 2 * DR[mask] + RR[mask]) / RR[mask]

    # Effective bias ~ sqrt(mean w at ~1 degree)
    mid_idx = len(w) // 2
    w_ref = np.mean(w[max(0, mid_idx-2):mid_idx+2])
    bias_eff = np.sqrt(max(w_ref, 0)) * 10 + 1.0  # rough scaling

    return w, bias_eff

# ============================================================
# Main analysis loop
# ============================================================

t_start = time.time()
all_results = {}

for survey_name, cfg in SPECTRO_SURVEYS.items():
    print(f"\n{'='*70}")
    print(f"SURVEY: {survey_name}")
    print(f"{'='*70}")

    data = generate_survey_with_redshifts(survey_name, cfg)
    print(f"  Total objects: {data['total_objects']:,}")
    print(f"  Anomalies: {data['n_anomalies']:,} ({100*data['n_anomalies']/data['total_objects']:.2f}%)")

    survey_results = {
        "survey": survey_name,
        "total_objects": data["total_objects"],
        "n_anomalies": data["n_anomalies"],
        "global_anomaly_rate": data["n_anomalies"] / data["total_objects"],
        "z_bins": [],
    }

    # Sky fraction estimate
    ra_lo, ra_hi = cfg["footprint"]["ra"]
    dec_lo, dec_hi = cfg["footprint"]["dec"]
    sky_frac = ((ra_hi - ra_lo) / 360.0) * (
        np.sin(np.radians(dec_hi)) - np.sin(np.radians(dec_lo))) / 2.0

    print(f"\n  {'Bin':>10} | {'N_anom':>8} | {'N_total':>10} | {'Rate(%)':>8} | "
          f"{'<Score>':>8} | {'bias':>6} | {'Vol(Gpc3)':>10}")
    print(f"  {'-'*10}-+-{'-'*8}-+-{'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*6}-+-{'-'*10}")

    for b in range(len(Z_BIN_LABELS)):
        z_lo, z_hi = Z_BIN_EDGES[b], Z_BIN_EDGES[b + 1]
        label = Z_BIN_LABELS[b]

        # Skip bins beyond survey z_max
        if z_lo >= cfg["z_max"]:
            continue

        z_hi_eff = min(z_hi, cfg["z_max"])

        # Count anomalies and total in this z-bin
        mask_anom = (data["anom_z"] >= z_lo) & (data["anom_z"] < z_hi_eff)
        mask_all = (data["all_z"] >= z_lo) & (data["all_z"] < z_hi_eff)

        n_anom_bin = mask_anom.sum()
        n_total_bin = mask_all.sum()
        rate = n_anom_bin / max(n_total_bin, 1)
        mean_score = float(np.mean(data["anom_scores"][mask_anom])) if n_anom_bin > 0 else 0.0

        # Comoving volume
        vol = comoving_volume_shell(z_lo, z_hi_eff, sky_frac) / 1e9  # Gpc^3

        # Clustering
        w_theta = np.zeros(len(THETA_BINS_DEG) - 1)
        bias_eff = 1.0
        if n_anom_bin >= 20:
            w_theta, bias_eff = measure_clustering(
                data["anom_ra"][mask_anom], data["anom_dec"][mask_anom],
                cfg["footprint"], THETA_BINS_DEG)

        print(f"  {label:>10} | {n_anom_bin:>8,} | {n_total_bin:>10,} | "
              f"{100*rate:>7.3f}% | {mean_score:>8.2f} | {bias_eff:>6.2f} | {vol:>10.3f}")

        theta_centers = np.sqrt(THETA_BINS_DEG[:-1] * THETA_BINS_DEG[1:])

        survey_results["z_bins"].append({
            "z_range": [float(z_lo), float(z_hi_eff)],
            "label": label,
            "n_anomalies": int(n_anom_bin),
            "n_total": int(n_total_bin),
            "anomaly_rate": float(rate),
            "mean_anomaly_score": mean_score,
            "effective_bias": float(bias_eff),
            "comoving_volume_Gpc3": float(vol),
            "anomaly_density_per_Gpc3": float(n_anom_bin / max(vol, 1e-10)),
            "w_theta": w_theta.tolist(),
            "theta_centers_deg": theta_centers.tolist(),
        })

    # Test for redshift evolution: chi-squared vs flat rate
    if len(survey_results["z_bins"]) >= 3:
        rates = [b["anomaly_rate"] for b in survey_results["z_bins"]]
        mean_rate = np.mean(rates)
        n_totals = [b["n_total"] for b in survey_results["z_bins"]]
        n_anoms = [b["n_anomalies"] for b in survey_results["z_bins"]]

        # Chi-squared: observed vs expected under flat rate
        chi2_val = 0
        for n_a, n_t in zip(n_anoms, n_totals):
            expected = mean_rate * n_t
            if expected > 0:
                chi2_val += (n_a - expected)**2 / expected
        dof = len(rates) - 1
        p_flat = float(1 - chi2.cdf(chi2_val, dof)) if dof > 0 else 1.0

        # Linear fit: rate = a + b*z
        z_mids = [(b["z_range"][0] + b["z_range"][1]) / 2 for b in survey_results["z_bins"]]
        try:
            popt, pcov = curve_fit(lambda z, a, b: a + b * z, z_mids, rates)
            slope = popt[1]
            slope_err = np.sqrt(pcov[1, 1])
            slope_sigma = abs(slope) / max(slope_err, 1e-15)
        except Exception:
            slope, slope_err, slope_sigma = 0, 0, 0

        survey_results["evolution_test"] = {
            "chi2_vs_flat": float(chi2_val),
            "dof": dof,
            "p_value_flat": p_flat,
            "rejects_flat_at_3sigma": p_flat < 0.0027,
            "linear_slope": float(slope),
            "linear_slope_err": float(slope_err),
            "slope_significance_sigma": float(slope_sigma),
            "rate_increases_with_z": slope > 0,
        }

        verdict = "RISES" if slope > 0 and slope_sigma > 2 else "FLAT"
        print(f"\n  Evolution test: rate vs z slope = {slope:.6f} +/- {slope_err:.6f} "
              f"({slope_sigma:.1f} sigma) -> {verdict}")
        print(f"  Chi2 vs flat: {chi2_val:.2f} (dof={dof}, p={p_flat:.4f})")

    all_results[survey_name] = survey_results

elapsed = time.time() - t_start

# ============================================================
# Cross-survey comparison
# ============================================================

print("\n" + "=" * 70)
print("CROSS-SURVEY COMPARISON: Anomaly Rate Evolution")
print("=" * 70)

for name, res in all_results.items():
    if "evolution_test" in res:
        et = res["evolution_test"]
        print(f"  {name:>10}: slope={et['linear_slope']:.6f} ({et['slope_significance_sigma']:.1f} sigma), "
              f"chi2/dof={et['chi2_vs_flat']:.1f}/{et['dof']}, p_flat={et['p_value_flat']:.4f}")

# ============================================================
# Save results
# ============================================================

summary = {
    "experiment": "redshift_tomography",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": elapsed,
    "config": {
        "z_bin_edges": Z_BIN_EDGES,
        "z_bin_labels": Z_BIN_LABELS,
        "surveys": list(SPECTRO_SURVEYS.keys()),
        "theta_bins_deg": THETA_BINS_DEG.tolist(),
    },
    "surveys": all_results,
    "interpretation": {
        "question": "Does anomaly rate evolve with redshift?",
        "positive_scenario": "Rate rises at z>2 — genuinely new populations at high-z, "
                              "potentially including bounce cosmology relics",
        "null_scenario": "Rate flat — anomalies are distance-independent artifacts or "
                          "constant-fraction contaminants",
        "key_metric": "Linear slope of rate(z) and chi2 vs flat hypothesis",
    },
}

out_path = OUTPUT_DIR / "redshift_tomography_summary.json"
with open(out_path, "w") as f:
    json.dump(summary, f, cls=NumpyEncoder, indent=2)
print(f"\nSaved: {out_path}")

# Per-survey detailed outputs
for name, res in all_results.items():
    path = OUTPUT_DIR / f"{name.lower()}_tomography.json"
    with open(path, "w") as f:
        json.dump(res, f, cls=NumpyEncoder, indent=2)
    print(f"Saved: {path}")

print("\n" + "=" * 70)
print("COMPLETE")
print("=" * 70)
