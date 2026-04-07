#!/usr/bin/env python3
"""
Deep Analysis Experiment: Galaxy Bias Evolution b(z) from Anomaly Clustering
============================================================================
Extend the f_NL bias validation to measure how anomaly bias evolves with
redshift. At each z-bin, compute w(theta), fit for b(z), and compare with the
standard DESI QSO bias curve. If anomaly bias increases faster than standard
tracers, the multi-tracer f_NL improvement grows with survey volume.

Science question: Can anomalies serve as a high-bias tracer population for
improved f_NL constraints? The scale-dependent bias from f_NL is:
  Delta_b(k, z) = (b(z) - 1) * f_NL * delta_c / (alpha(k, z) * k^2)
Higher b(z) means stronger scale-dependent signal.

Method:
  - Generate synthetic anomaly + standard tracer catalogs at 6 z-bins
  - Measure w(theta) for anomalies and standard tracers at each z
  - Fit effective bias b_eff from w(theta) amplitude
  - Compute Delta_b(k) and forecast sigma(f_NL) improvement at each z
  - Compare anomaly b(z) vs standard DESI QSO bias: b_QSO(z) = 0.53 + 0.29*(1+z)^2

Output: /workspace/bigbounce/outputs/bias-evolution/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.spatial import cKDTree
from scipy.optimize import minimize_scalar, curve_fit
from scipy.interpolate import interp1d
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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/bias-evolution"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

Z_BIN_EDGES = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
Z_BIN_LABELS = ["0.0-0.5", "0.5-1.0", "1.0-1.5", "1.5-2.0", "2.0-3.0", "3.0+"]

THETA_BINS_DEG = np.logspace(-1.5, 0.5, 15)
N_RANDOM = 50000
N_ANOMALIES_PER_BIN = 3000
N_STANDARD_PER_BIN = 20000

# Cosmological constants
H0 = 67.68
OMEGA_M = 0.3111
OMEGA_L = 1 - OMEGA_M
C_KMS = 299792.458
DELTA_C = 1.686  # critical collapse density
FNL_FIDUCIAL = -4.375  # matter bounce prediction

# k values for scale-dependent bias
K_MODES = np.logspace(-3, -1, 30)  # h/Mpc

# Footprint (DESI-like)
FOOTPRINT = {"ra": (100, 280), "dec": (-20, 80)}

print("=" * 70)
print("DEEP ANALYSIS: Galaxy Bias Evolution b(z) from Anomaly Clustering")
print("=" * 70)
print(f"Output: {OUTPUT_DIR}")
print(f"f_NL fiducial (matter bounce): {FNL_FIDUCIAL}")
print()

# ============================================================
# Cosmological functions
# ============================================================

def E_z(z):
    return np.sqrt(OMEGA_M * (1 + z)**3 + OMEGA_L)


def comoving_distance(z, n_steps=500):
    z_arr = np.linspace(0, z, n_steps)
    integrand = 1.0 / E_z(z_arr)
    return (C_KMS / H0) * np.trapz(integrand, z_arr)


def growth_factor_approx(z):
    """Approximate growth factor D(z) normalized to D(0)=1."""
    a = 1.0 / (1.0 + z)
    omega_m_z = OMEGA_M * (1 + z)**3 / E_z(z)**2
    return a * (omega_m_z**0.6) / (OMEGA_M**0.6)


def transfer_function_approx(k):
    """Approximate matter transfer function T(k) — Eisenstein & Hu shape."""
    # Simplified BBKS-like
    q = k / (OMEGA_M * (H0 / 100)**2)  # scale in Mpc^-1 units
    T = np.log(1 + 2.34 * q) / (2.34 * q) * (
        1 + 3.89 * q + (16.1 * q)**2 + (5.46 * q)**3 + (6.71 * q)**4)**(-0.25)
    return T


def alpha_k_z(k, z):
    """Scale factor alpha(k,z) for scale-dependent bias."""
    D_z = growth_factor_approx(z)
    T_k = transfer_function_approx(k)
    # alpha(k,z) = 2 * k^2 * T(k) * D(z) / (3 * Omega_m * H0^2)
    # In natural units with c=1, H0 in km/s/Mpc
    return 2.0 * k**2 * T_k * D_z / (3.0 * OMEGA_M)

# ============================================================
# Standard bias models
# ============================================================

def bias_desi_qso(z):
    """DESI QSO bias: b(z) = 0.53 + 0.29*(1+z)^2 (Laurent+2017)."""
    return 0.53 + 0.29 * (1 + z)**2


def bias_desi_lrg(z):
    """DESI LRG bias: b(z) ~ 1.7 * D(0)/D(z)."""
    return 1.7 / growth_factor_approx(z)


def bias_anomaly_model(z):
    """Hypothesized anomaly bias: steeper than QSO, representing rare objects."""
    # Anomalies are high-score outliers -> expect high bias
    # Model: b(z) = 2.0 + 0.8*(1+z)^2 (steeper than QSO)
    return 2.0 + 0.8 * (1 + z)**2

# ============================================================
# Synthetic catalog generation with bias
# ============================================================

class BiasedCatalogDataset(Dataset):
    """Generate positions with known bias (clustered proportional to bias)."""
    def __init__(self, n_objects, bias, footprint, seed=42):
        self.n = n_objects
        rng = np.random.default_rng(seed)

        ra_lo, ra_hi = footprint["ra"]
        dec_lo, dec_hi = footprint["dec"]

        # Higher bias -> more clustering: use more cluster spots, tighter scatter
        n_clusters = max(3, int(bias * 2))
        scatter = max(0.5, 3.0 / bias)  # degrees
        frac_clustered = min(0.8, 0.15 * bias)

        n_clust = int(frac_clustered * n_objects)
        n_unif = n_objects - n_clust

        # Uniform component
        ra_u = rng.uniform(ra_lo, ra_hi, n_unif).astype(np.float32)
        dec_u = np.degrees(np.arcsin(rng.uniform(
            np.sin(np.radians(dec_lo)), np.sin(np.radians(dec_hi)), n_unif))).astype(np.float32)

        # Clustered component
        spot_ra = rng.uniform(ra_lo + 10, ra_hi - 10, n_clusters)
        spot_dec = rng.uniform(max(dec_lo + 10, -80), min(dec_hi - 10, 80), n_clusters)
        assigns = rng.integers(0, n_clusters, n_clust)
        ra_c = (spot_ra[assigns] + rng.normal(0, scatter, n_clust)).astype(np.float32)
        dec_c = (spot_dec[assigns] + rng.normal(0, scatter, n_clust)).astype(np.float32)

        self.ra = np.concatenate([ra_u, ra_c])
        self.dec = np.concatenate([dec_u, dec_c])
        self.ra = np.clip(self.ra, ra_lo, ra_hi)
        self.dec = np.clip(self.dec, dec_lo, dec_hi)

    def __len__(self):
        return self.n

    def __getitem__(self, idx):
        return torch.tensor(self.ra[idx]), torch.tensor(self.dec[idx])

# ============================================================
# Clustering measurement
# ============================================================

def measure_w_theta(ra, dec, footprint, theta_bins, max_n=5000):
    """Measure angular auto-correlation w(theta) with Landy-Szalay."""
    if len(ra) < 30:
        return np.zeros(len(theta_bins) - 1)

    n = min(len(ra), max_n)
    if n < len(ra):
        idx = np.random.choice(len(ra), n, replace=False)
        ra, dec = ra[idx], dec[idx]

    rng = np.random.default_rng(12345)
    ra_lo, ra_hi = footprint["ra"]
    dec_lo, dec_hi = footprint["dec"]
    n_rand = min(5 * n, N_RANDOM)
    ra_r = rng.uniform(ra_lo, ra_hi, n_rand).astype(np.float64)
    dec_r = np.degrees(np.arcsin(rng.uniform(
        np.sin(np.radians(dec_lo)), np.sin(np.radians(dec_hi)), n_rand))).astype(np.float64)

    def to_xyz(r, d):
        rr, dd = np.deg2rad(r), np.deg2rad(d)
        return np.stack([np.cos(dd)*np.cos(rr), np.cos(dd)*np.sin(rr), np.sin(dd)], axis=1)

    chord_bins = 2 * np.sin(np.deg2rad(theta_bins) / 2)
    xyz_d = to_xyz(ra, dec)
    xyz_r = to_xyz(ra_r, dec_r)
    tree_d = cKDTree(xyz_d)
    tree_r = cKDTree(xyz_r)

    # DD
    DD = np.zeros(len(theta_bins) - 1)
    for i in range(len(xyz_d)):
        hits = tree_d.query_ball_point(xyz_d[i], r=chord_bins[-1])
        if len(hits) <= 1:
            continue
        dists = np.linalg.norm(xyz_d[hits] - xyz_d[i], axis=1)
        h, _ = np.histogram(dists[dists > 0], bins=chord_bins)
        DD += h
    n_dd = len(ra) * (len(ra) - 1) / 2
    DD /= max(n_dd, 1)

    # RR (subsample)
    n_rr = min(n_rand, 5000)
    RR = np.zeros(len(theta_bins) - 1)
    for i in range(n_rr):
        hits = tree_r.query_ball_point(xyz_r[i], r=chord_bins[-1])
        if len(hits) <= 1:
            continue
        dists = np.linalg.norm(xyz_r[hits] - xyz_r[i], axis=1)
        h, _ = np.histogram(dists[dists > 0], bins=chord_bins)
        RR += h
    RR /= max(n_rr * (n_rand - 1) / 2, 1)

    # DR
    DR = np.zeros(len(theta_bins) - 1)
    for i in range(len(xyz_d)):
        hits = tree_r.query_ball_point(xyz_d[i], r=chord_bins[-1])
        if len(hits) == 0:
            continue
        dists = np.linalg.norm(xyz_r[hits] - xyz_d[i], axis=1)
        h, _ = np.histogram(dists, bins=chord_bins)
        DR += h
    DR /= max(len(ra) * n_rand, 1)

    mask = RR > 0
    w = np.zeros_like(DD)
    w[mask] = (DD[mask] - 2 * DR[mask] + RR[mask]) / RR[mask]
    return w


def fit_bias_from_w(w_theta, w_theta_reference):
    """Fit effective bias: w_obs = b_eff^2 * w_ref, so b_eff = sqrt(w_obs/w_ref)."""
    mask = (w_theta_reference > 0) & (w_theta > 0)
    if mask.sum() < 3:
        return 1.0, 0.5

    ratios = w_theta[mask] / w_theta_reference[mask]
    b_eff = np.sqrt(np.median(ratios))
    b_err = np.std(np.sqrt(ratios)) / np.sqrt(mask.sum())
    return float(max(b_eff, 0.1)), float(b_err)

# ============================================================
# Main analysis
# ============================================================

t_start = time.time()
theta_centers = np.sqrt(THETA_BINS_DEG[:-1] * THETA_BINS_DEG[1:])
results_by_z = []

# First, compute reference w(theta) from a large uniform random catalog
# (this represents b=1 matter field)
print("Computing reference w(theta) for b=1 matter field...")
rng_ref = np.random.default_rng(9999)
ra_ref = rng_ref.uniform(FOOTPRINT["ra"][0], FOOTPRINT["ra"][1], 20000).astype(np.float64)
dec_ref = np.degrees(np.arcsin(rng_ref.uniform(
    np.sin(np.radians(FOOTPRINT["dec"][0])),
    np.sin(np.radians(FOOTPRINT["dec"][1])), 20000))).astype(np.float64)

# Add mild clustering for b=1 reference
n_spots = 20
spot_ra = rng_ref.uniform(120, 260, n_spots)
spot_dec = rng_ref.uniform(-10, 70, n_spots)
n_clust = 4000
assigns = rng_ref.integers(0, n_spots, n_clust)
ra_c = spot_ra[assigns] + rng_ref.normal(0, 3.0, n_clust)
dec_c = spot_dec[assigns] + rng_ref.normal(0, 3.0, n_clust)
ra_ref = np.concatenate([ra_ref[:16000], ra_c]).astype(np.float64)
dec_ref = np.concatenate([dec_ref[:16000], dec_c]).astype(np.float64)

w_reference = measure_w_theta(ra_ref, dec_ref, FOOTPRINT, THETA_BINS_DEG)
print(f"  Reference w(theta) range: [{w_reference.min():.6f}, {w_reference.max():.6f}]")

print(f"\n{'='*70}")
print("BIAS MEASUREMENT BY REDSHIFT BIN")
print(f"{'='*70}")
print(f"\n  {'z-bin':>10} | {'b_anom':>8} | {'b_std':>8} | {'b_QSO':>8} | "
      f"{'ratio':>8} | {'Delta_b/b':>10} | {'sigma_fNL':>10}")
print(f"  {'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*10}-+-{'-'*10}")

for b in range(len(Z_BIN_LABELS)):
    z_lo, z_hi = Z_BIN_EDGES[b], Z_BIN_EDGES[b + 1]
    z_mid = (z_lo + z_hi) / 2
    label = Z_BIN_LABELS[b]

    # Generate anomaly catalog with model bias
    b_model = bias_anomaly_model(z_mid)
    anom_dataset = BiasedCatalogDataset(
        N_ANOMALIES_PER_BIN, b_model, FOOTPRINT,
        seed=42 + b * 1000)
    anom_loader = DataLoader(anom_dataset, batch_size=5000, num_workers=4,
                              pin_memory=True, shuffle=False)
    ra_anom, dec_anom = [], []
    for batch_ra, batch_dec in anom_loader:
        ra_anom.append(batch_ra.numpy())
        dec_anom.append(batch_dec.numpy())
    ra_anom = np.concatenate(ra_anom).astype(np.float64)
    dec_anom = np.concatenate(dec_anom).astype(np.float64)

    # Generate standard tracer catalog with QSO bias
    b_qso = bias_desi_qso(z_mid)
    std_dataset = BiasedCatalogDataset(
        N_STANDARD_PER_BIN, b_qso, FOOTPRINT,
        seed=99 + b * 1000)
    std_loader = DataLoader(std_dataset, batch_size=10000, num_workers=4,
                             pin_memory=True, shuffle=False)
    ra_std, dec_std = [], []
    for batch_ra, batch_dec in std_loader:
        ra_std.append(batch_ra.numpy())
        dec_std.append(batch_dec.numpy())
    ra_std = np.concatenate(ra_std).astype(np.float64)
    dec_std = np.concatenate(dec_std).astype(np.float64)

    # Measure clustering
    w_anom = measure_w_theta(ra_anom, dec_anom, FOOTPRINT, THETA_BINS_DEG)
    w_std = measure_w_theta(ra_std, dec_std, FOOTPRINT, THETA_BINS_DEG)

    # Fit bias
    b_anom_fit, b_anom_err = fit_bias_from_w(w_anom, w_reference)
    b_std_fit, b_std_err = fit_bias_from_w(w_std, w_reference)

    # Scale-dependent bias: Delta_b(k) = (b-1) * f_NL * delta_c / alpha(k,z)
    delta_b_anom = np.array([(b_anom_fit - 1) * FNL_FIDUCIAL * DELTA_C / alpha_k_z(k, z_mid)
                              for k in K_MODES])
    delta_b_std = np.array([(b_std_fit - 1) * FNL_FIDUCIAL * DELTA_C / alpha_k_z(k, z_mid)
                             for k in K_MODES])

    # Fractional scale-dependent bias enhancement
    frac_delta_b = abs(np.mean(delta_b_anom)) / max(abs(np.mean(delta_b_std)), 1e-10)

    # Fisher forecast: sigma(f_NL) ~ 1 / sqrt(integral of (db/df_NL)^2 * n_eff * V)
    # Relative improvement from multi-tracer
    D_z = growth_factor_approx(z_mid)
    chi = comoving_distance(z_mid)
    vol_eff = 4 * np.pi * chi**2 * (C_KMS / H0 / E_z(z_mid)) / 3  # rough
    n_eff_anom = N_ANOMALIES_PER_BIN / max(vol_eff, 1e-10) * 1e9  # per Gpc^3
    n_eff_std = N_STANDARD_PER_BIN / max(vol_eff, 1e-10) * 1e9

    # sigma(f_NL) single-tracer ~ 1/(b-1) * const
    sigma_fnl_single = 8.98 / max(b_std_fit - 1, 0.1)  # scaled from our Fisher result
    # Multi-tracer improvement: sigma_multi ~ sigma_single / sqrt(1 + n_anom/n_std * ((b_a-1)/(b_s-1))^2)
    improvement_factor = np.sqrt(1 + (n_eff_anom / max(n_eff_std, 1e-10)) *
                                  ((b_anom_fit - 1) / max(b_std_fit - 1, 0.1))**2)
    sigma_fnl_multi = sigma_fnl_single / improvement_factor

    ratio = b_anom_fit / max(b_std_fit, 0.1)
    print(f"  {label:>10} | {b_anom_fit:>8.2f} | {b_std_fit:>8.2f} | {b_qso:>8.2f} | "
          f"{ratio:>8.2f} | {frac_delta_b:>10.2f} | {sigma_fnl_multi:>10.2f}")

    results_by_z.append({
        "z_range": [float(z_lo), float(z_hi)],
        "z_mid": float(z_mid),
        "label": label,
        "bias_anomaly_measured": float(b_anom_fit),
        "bias_anomaly_error": float(b_anom_err),
        "bias_anomaly_model": float(b_model),
        "bias_standard_measured": float(b_std_fit),
        "bias_standard_error": float(b_std_err),
        "bias_qso_model": float(b_qso),
        "bias_ratio_anom_over_std": float(ratio),
        "w_theta_anomaly": w_anom.tolist(),
        "w_theta_standard": w_std.tolist(),
        "theta_centers_deg": theta_centers.tolist(),
        "scale_dependent_bias_anomaly": delta_b_anom.tolist(),
        "scale_dependent_bias_standard": delta_b_std.tolist(),
        "k_modes_hMpc": K_MODES.tolist(),
        "fractional_delta_b_enhancement": float(frac_delta_b),
        "sigma_fnl_single_tracer": float(sigma_fnl_single),
        "sigma_fnl_multi_tracer": float(sigma_fnl_multi),
        "multi_tracer_improvement_pct": float((1 - sigma_fnl_multi / sigma_fnl_single) * 100),
        "growth_factor": float(D_z),
    })

elapsed = time.time() - t_start

# ============================================================
# Summary statistics
# ============================================================

print(f"\n{'='*70}")
print("SUMMARY")
print(f"{'='*70}")

z_mids = [r["z_mid"] for r in results_by_z]
b_anoms = [r["bias_anomaly_measured"] for r in results_by_z]
b_stds = [r["bias_standard_measured"] for r in results_by_z]
improvements = [r["multi_tracer_improvement_pct"] for r in results_by_z]

print(f"\n  Anomaly bias range: {min(b_anoms):.2f} - {max(b_anoms):.2f}")
print(f"  Standard bias range: {min(b_stds):.2f} - {max(b_stds):.2f}")
print(f"  Mean bias ratio (anom/std): {np.mean([r['bias_ratio_anom_over_std'] for r in results_by_z]):.2f}")
print(f"  Multi-tracer improvement range: {min(improvements):.1f}% - {max(improvements):.1f}%")

# Fit b(z) evolution: b = a + c*(1+z)^2
try:
    popt_anom, _ = curve_fit(lambda z, a, c: a + c * (1 + z)**2, z_mids, b_anoms)
    popt_std, _ = curve_fit(lambda z, a, c: a + c * (1 + z)**2, z_mids, b_stds)
    print(f"\n  Anomaly bias fit: b(z) = {popt_anom[0]:.2f} + {popt_anom[1]:.3f}*(1+z)^2")
    print(f"  Standard bias fit: b(z) = {popt_std[0]:.2f} + {popt_std[1]:.3f}*(1+z)^2")
    print(f"  (QSO model: b(z) = 0.53 + 0.290*(1+z)^2)")

    steeper = popt_anom[1] > popt_std[1]
    print(f"\n  Anomaly bias evolution is {'STEEPER' if steeper else 'SHALLOWER'} than standard tracers")
    if steeper:
        print(f"  -> Multi-tracer f_NL improvement GROWS with redshift")
        print(f"  -> Optimal strategy: use anomalies as high-z complement to standard tracers")
except Exception as e:
    print(f"  Bias fit failed: {e}")
    popt_anom = [0, 0]
    popt_std = [0, 0]

# ============================================================
# Save results
# ============================================================

summary = {
    "experiment": "bias_evolution",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": elapsed,
    "config": {
        "z_bin_edges": Z_BIN_EDGES,
        "z_bin_labels": Z_BIN_LABELS,
        "theta_bins_deg": THETA_BINS_DEG.tolist(),
        "n_anomalies_per_bin": N_ANOMALIES_PER_BIN,
        "n_standard_per_bin": N_STANDARD_PER_BIN,
        "fnl_fiducial": FNL_FIDUCIAL,
        "delta_c": DELTA_C,
        "k_modes_hMpc": K_MODES.tolist(),
    },
    "redshift_bins": results_by_z,
    "global_summary": {
        "anomaly_bias_range": [float(min(b_anoms)), float(max(b_anoms))],
        "standard_bias_range": [float(min(b_stds)), float(max(b_stds))],
        "mean_bias_ratio": float(np.mean([r["bias_ratio_anom_over_std"] for r in results_by_z])),
        "multi_tracer_improvement_range_pct": [float(min(improvements)), float(max(improvements))],
        "anomaly_bias_fit_coeffs": {"a": float(popt_anom[0]), "c": float(popt_anom[1])},
        "standard_bias_fit_coeffs": {"a": float(popt_std[0]), "c": float(popt_std[1])},
        "anomaly_bias_steeper_than_standard": bool(popt_anom[1] > popt_std[1]),
    },
    "interpretation": {
        "question": "Does anomaly bias grow faster with z than standard tracers?",
        "if_yes": "Anomalies are increasingly rare/massive at high-z -> ideal multi-tracer "
                   "complement for f_NL measurement. The scale-dependent bias signal "
                   "Delta_b = (b-1)*f_NL*delta_c/alpha(k,z) grows with b.",
        "if_no": "Anomaly bias tracks standard populations -> limited additional f_NL leverage "
                  "from multi-tracer technique.",
        "connection_to_bounce": "Matter bounce predicts f_NL = -4.375. Higher anomaly bias "
                                 "at z>2 would make this detectable at >5 sigma with SPHEREx.",
    },
}

out_path = OUTPUT_DIR / "bias_evolution_summary.json"
with open(out_path, "w") as f:
    json.dump(summary, f, cls=NumpyEncoder, indent=2)
print(f"\nSaved: {out_path}")

print("\n" + "=" * 70)
print("COMPLETE")
print("=" * 70)
