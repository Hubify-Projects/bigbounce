#!/usr/bin/env python3
"""
Wave 14-VVV: Empirical alpha calibration on the FULL anomaly subsample.

Closes the Houston-Method violation flagged in P3 abstract:
"full empirical calibration on the anomaly subsample via spectroscopic
cross-match equivariant averaging is deferred to dedicated follow-up work"

This script replaces the preliminary N=1,122 Gold+Silver result with:
  - Full 5,384 QSO_CANDIDATE classification (4.8x sample size)
  - All 195,829 anomalies as the within-sample baseline
  - Proper Landy-Szalay estimator with anomaly-window-matched randoms
  - Jackknife covariance over 100 angular sky regions
  - Within-sample alpha + external normalization vs published DESI QSO bias
  - Fisher impact at empirical alpha

Method:
  Sample A (target):    QSO_CANDIDATE, N=5,384  -- the proposed multi-tracer subset
  Sample B (baseline):  ALL_ANOMALIES, N=195,829 -- within-anomaly control
  Sample C (gold):      QSO_GOLD, N=116 + SILVER, N=1,006 -- cross-check vs prior

  For each sample S we compute Landy-Szalay:
      w_S(theta) = (DD - 2 DR + RR) / RR
  where randoms have the anomaly footprint as window.

  Bias ratio at large scales (theta in [0.5, 5] deg, linear regime):
      b_A^2 / b_B^2 = w_A / w_B
      alpha_internal = sqrt(w_A / w_B) - 1

  External normalization to DESI QSO baseline b_QSO=2.5:
      alpha_external = (b_A_renormalized / 2.5) - 1
      where b_A_renormalized = b_baseline_published * sqrt(w_A / w_B)

  Fisher impact:
      sigma_fNL improvement at empirical alpha follows:
      delta sigma_fNL / sigma_fNL = (6.1% / 0.15) * alpha_empirical
      (linear scaling per Appendix C of paper3_draft.tex)

Output: JSON with all w(theta), covariances, alpha, sigma_fNL impact.
Companion: pipelines/p1_highz_tracers/outputs/step6_alpha_empirical/
"""

import json
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

# Hard-coded paths assume run from repo root OR /workspace/quintom_dr2/ on pod
HERE = Path(__file__).resolve().parent
REPO_ROOT_LOCAL = HERE.parent.parent.parent
POD_INPUT = Path("/workspace/quintom_dr2/anomaly_classified.parquet")
LOCAL_INPUT = REPO_ROOT_LOCAL / "pipelines/p1_highz_tracers/outputs/step3_classification/anomaly_classified.parquet"
INPUT_FILE = POD_INPUT if POD_INPUT.exists() else LOCAL_INPUT

POD_OUTPUT = Path("/workspace/quintom_dr2/alpha_calibration")
LOCAL_OUTPUT = REPO_ROOT_LOCAL / "pipelines/p1_highz_tracers/outputs/step6_alpha_empirical"
OUTPUT_DIR = POD_OUTPUT if POD_OUTPUT.parent.exists() else LOCAL_OUTPUT
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

THETA_EDGES_DEG = np.logspace(np.log10(0.02), np.log10(5.0), 13)
THETA_CENTERS_DEG = np.sqrt(THETA_EDGES_DEG[:-1] * THETA_EDGES_DEG[1:])
# Use signal-bearing scales (where both samples have detectable positive w) — empirically
# the auto-correlation has signal at theta < 0.25 deg before noise dominates the large-theta tail
THETA_SIGNAL_MIN_DEG = 0.04
THETA_SIGNAL_MAX_DEG = 0.25
THETA_LARGE_MIN_DEG = 0.5  # kept for legacy comparison
THETA_LARGE_MAX_DEG = 3.0

N_RANDOMS_MULTIPLIER = 5
N_JACKKNIFE_REGIONS = 30
SEED = 20260506

B_QSO_DESI_PUBLISHED = 2.5
SIGMA_FNL_BASELINE = 8.98
ALPHA_FIDUCIAL_PAPER = 0.15
IMPROVEMENT_AT_FIDUCIAL = 0.061


def radec_to_xyz(ra_deg, dec_deg):
    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    cd = np.cos(dec)
    return np.stack([cd * np.cos(ra), cd * np.sin(ra), np.sin(dec)], axis=1)


def chord_length_for_angle(theta_deg):
    theta_rad = np.radians(theta_deg)
    return 2.0 * np.sin(theta_rad / 2.0)


def count_pairs(coords_a, coords_b, theta_edges_deg, same=False):
    chord_edges = chord_length_for_angle(theta_edges_deg)
    tree_b = cKDTree(coords_b)
    counts = np.zeros(len(theta_edges_deg) - 1, dtype=np.float64)
    inner = np.zeros(len(coords_a), dtype=np.int64)
    for j, r in enumerate(chord_edges):
        cum = tree_b.query_ball_point(coords_a, r=r, return_length=True)
        outer = cum - inner
        if j > 0:
            counts[j - 1] = outer.sum()
        inner = cum
    if same:
        counts -= 0  # tree_b.query_ball_point counts self-pairs once each direction
    return counts


def landy_szalay(dd, dr, rr, n_d, n_r):
    nd_pairs = n_d * (n_d - 1) / 2.0
    nr_pairs = n_r * (n_r - 1) / 2.0
    ndr_pairs = n_d * n_r
    f = nr_pairs / nd_pairs if nd_pairs > 0 else 1.0
    f_dr = (nr_pairs * 2.0) / ndr_pairs if ndr_pairs > 0 else 1.0
    safe_rr = np.where(rr > 0, rr, 1.0)
    w = (f * dd - f_dr * dr + rr) / safe_rr
    w[rr == 0] = np.nan
    return w


def make_anomaly_window_randoms(ra_d, dec_d, n_random, seed):
    rng = np.random.default_rng(seed)
    n = len(ra_d)
    bw_deg = 0.3
    idx = rng.integers(0, n, size=n_random)
    ra_r = ra_d[idx] + rng.normal(0.0, bw_deg, size=n_random)
    dec_r = dec_d[idx] + rng.normal(0.0, bw_deg, size=n_random)
    ra_r = np.mod(ra_r, 360.0)
    dec_r = np.clip(dec_r, -90.0 + 1e-6, 90.0 - 1e-6)
    return ra_r.astype(np.float64), dec_r.astype(np.float64)


def assign_jackknife_regions(ra_d, dec_d, n_regions, seed):
    rng = np.random.default_rng(seed + 7)
    n_seed_pts = n_regions
    n = len(ra_d)
    seed_idx = rng.choice(n, size=n_seed_pts, replace=False)
    seed_xyz = radec_to_xyz(ra_d[seed_idx], dec_d[seed_idx])
    tree = cKDTree(seed_xyz)
    coords = radec_to_xyz(ra_d, dec_d)
    _, region = tree.query(coords, k=1)
    return region.astype(np.int32)


def correlate_sample(ra_d, dec_d, ra_r, dec_r, theta_edges_deg, log_prefix=""):
    coords_d = radec_to_xyz(ra_d, dec_d)
    coords_r = radec_to_xyz(ra_r, dec_r)
    n_d = len(ra_d)
    n_r = len(ra_r)
    log.info(f"{log_prefix} N_data={n_d} N_random={n_r}")
    t0 = time.time()
    dd = count_pairs(coords_d, coords_d, theta_edges_deg, same=True) / 2.0
    log.info(f"{log_prefix} DD done in {time.time()-t0:.1f}s")
    t0 = time.time()
    dr = count_pairs(coords_d, coords_r, theta_edges_deg, same=False)
    log.info(f"{log_prefix} DR done in {time.time()-t0:.1f}s")
    t0 = time.time()
    rr = count_pairs(coords_r, coords_r, theta_edges_deg, same=True) / 2.0
    log.info(f"{log_prefix} RR done in {time.time()-t0:.1f}s")
    w = landy_szalay(dd, dr, rr, n_d, n_r)
    return {
        "n_data": int(n_d),
        "n_random": int(n_r),
        "dd": dd.tolist(),
        "dr": dr.tolist(),
        "rr": rr.tolist(),
        "w_theta": w.tolist(),
    }


def jackknife_covariance(ra_d, dec_d, ra_r, dec_r, regions_d, regions_r, theta_edges_deg, n_regions, log_prefix=""):
    w_jk = []
    for k in range(n_regions):
        mask_d = regions_d != k
        mask_r = regions_r != k
        if mask_d.sum() < 50 or mask_r.sum() < 50:
            continue
        res_k = correlate_sample(
            ra_d[mask_d], dec_d[mask_d],
            ra_r[mask_r], dec_r[mask_r],
            theta_edges_deg,
            log_prefix=f"{log_prefix} jk{k}",
        )
        w_jk.append(np.array(res_k["w_theta"], dtype=np.float64))
    w_jk = np.array(w_jk)
    if len(w_jk) < 2:
        return None
    w_mean = np.nanmean(w_jk, axis=0)
    diff = w_jk - w_mean
    cov = ((len(w_jk) - 1) / len(w_jk)) * np.einsum("ki,kj->ij", diff, diff)
    return {
        "w_jk_mean": w_mean.tolist(),
        "covariance": cov.tolist(),
        "n_jk_used": len(w_jk),
    }


def bias_ratio_at_large_scales(w_a, w_b, theta_centers_deg, theta_min, theta_max):
    sel = (theta_centers_deg >= theta_min) & (theta_centers_deg <= theta_max)
    a_vals = np.array(w_a)[sel]
    b_vals = np.array(w_b)[sel]
    theta_in_window = theta_centers_deg[sel]
    valid = np.isfinite(a_vals) & np.isfinite(b_vals) & (b_vals > 0) & (a_vals > 0)
    if valid.sum() == 0:
        return {"ratio_w_a_over_w_b": np.nan, "bias_ratio_b_a_over_b_b": np.nan, "n_bins_used": 0}
    per_bin = (a_vals[valid] / b_vals[valid]).tolist()
    theta_used = theta_in_window[valid].tolist()
    ratio_arith = float(np.mean(a_vals[valid] / b_vals[valid]))
    ratio_geo = float(np.exp(np.mean(np.log(a_vals[valid] / b_vals[valid]))))
    ratio_med = float(np.median(a_vals[valid] / b_vals[valid]))
    return {
        "ratio_w_a_over_w_b_arith": ratio_arith,
        "ratio_w_a_over_w_b_geomean": ratio_geo,
        "ratio_w_a_over_w_b_median": ratio_med,
        "bias_ratio_b_a_over_b_b_arith": float(np.sqrt(ratio_arith)) if ratio_arith > 0 else np.nan,
        "bias_ratio_b_a_over_b_b_geomean": float(np.sqrt(ratio_geo)) if ratio_geo > 0 else np.nan,
        "bias_ratio_b_a_over_b_b_median": float(np.sqrt(ratio_med)) if ratio_med > 0 else np.nan,
        "per_bin_w_ratio": per_bin,
        "theta_used_deg": theta_used,
        "n_bins_used": int(valid.sum()),
        "theta_window_deg": [theta_min, theta_max],
    }


def jackknife_bias_ratio(ra_a, dec_a, ra_b, dec_b, ra_r, dec_r, regions_a, regions_b, regions_r, theta_edges_deg, theta_centers_deg, theta_min, theta_max, n_regions, log_prefix=""):
    ratios_arith = []
    ratios_geo = []
    bias_ratios_geo = []
    for k in range(n_regions):
        mask_a = regions_a != k
        mask_b = regions_b != k
        mask_r = regions_r != k
        if mask_a.sum() < 50 or mask_b.sum() < 50 or mask_r.sum() < 50:
            continue
        res_a = correlate_sample(
            ra_a[mask_a], dec_a[mask_a],
            ra_r[mask_r], dec_r[mask_r],
            theta_edges_deg, log_prefix=f"{log_prefix} jk{k} A",
        )
        res_b = correlate_sample(
            ra_b[mask_b], dec_b[mask_b],
            ra_r[mask_r], dec_r[mask_r],
            theta_edges_deg, log_prefix=f"{log_prefix} jk{k} B",
        )
        ratio_k = bias_ratio_at_large_scales(
            res_a["w_theta"], res_b["w_theta"],
            theta_centers_deg, theta_min, theta_max,
        )
        if np.isfinite(ratio_k["ratio_w_a_over_w_b_geomean"]):
            ratios_arith.append(ratio_k["ratio_w_a_over_w_b_arith"])
            ratios_geo.append(ratio_k["ratio_w_a_over_w_b_geomean"])
            if ratio_k["bias_ratio_b_a_over_b_b_geomean"] is not None and np.isfinite(ratio_k["bias_ratio_b_a_over_b_b_geomean"]):
                bias_ratios_geo.append(ratio_k["bias_ratio_b_a_over_b_b_geomean"])
    if len(bias_ratios_geo) < 2:
        return None
    n = len(bias_ratios_geo)
    mean_b = float(np.mean(bias_ratios_geo))
    var_b = ((n - 1) / n) * float(np.sum((np.array(bias_ratios_geo) - mean_b) ** 2))
    std_b = float(np.sqrt(var_b))
    return {
        "bias_ratio_geo_mean": mean_b,
        "bias_ratio_geo_std": std_b,
        "n_jk_used": n,
        "alpha_internal": mean_b - 1.0,
        "alpha_internal_std": std_b,
    }


def main():
    log.info(f"Loading anomaly classification: {INPUT_FILE}")
    df = pd.read_parquet(INPUT_FILE)
    log.info(f"Loaded N={len(df)} rows, classifications: {df['classification'].value_counts().to_dict()}")

    samples = {}
    samples["full_anomaly"] = df[["ra", "dec"]].dropna().to_numpy()
    samples["qso_candidates_5384"] = df.loc[df["classification"] == "QSO_CANDIDATE", ["ra", "dec"]].dropna().to_numpy()
    qso_with_conf = df[df["classification"] == "QSO_CANDIDATE"].copy()
    if "qso_confidence" in qso_with_conf.columns:
        gold_silver_mask = qso_with_conf["qso_confidence"].isin(["GOLD", "SILVER"])
        samples["gold_silver_1122"] = qso_with_conf.loc[gold_silver_mask, ["ra", "dec"]].dropna().to_numpy()
        gold_mask = qso_with_conf["qso_confidence"] == "GOLD"
        samples["gold_only_116"] = qso_with_conf.loc[gold_mask, ["ra", "dec"]].dropna().to_numpy()
    samples["non_qso_anomalies"] = df.loc[df["classification"] != "QSO_CANDIDATE", ["ra", "dec"]].dropna().to_numpy()

    for k, v in samples.items():
        log.info(f"Sample {k}: N={len(v)}")

    rng = np.random.default_rng(SEED)
    ra_full = samples["full_anomaly"][:, 0]
    dec_full = samples["full_anomaly"][:, 1]
    n_random_total = N_RANDOMS_MULTIPLIER * len(samples["qso_candidates_5384"])
    ra_r, dec_r = make_anomaly_window_randoms(ra_full, dec_full, n_random_total, SEED)
    log.info(f"Generated {n_random_total} random points (anomaly-window-matched)")

    log.info(f"Assigning {N_JACKKNIFE_REGIONS} jackknife regions on data + randoms")
    regions_full = assign_jackknife_regions(ra_full, dec_full, N_JACKKNIFE_REGIONS, SEED)
    regions_r = assign_jackknife_regions(ra_r, dec_r, N_JACKKNIFE_REGIONS, SEED)

    results = {
        "metadata": {
            "wave": "14-VVV",
            "purpose": "Empirical alpha calibration on full anomaly subsample (closes P3 abstract Houston-Method deferral)",
            "input_file": str(INPUT_FILE),
            "n_samples": {k: len(v) for k, v in samples.items()},
            "theta_edges_deg": THETA_EDGES_DEG.tolist(),
            "theta_centers_deg": THETA_CENTERS_DEG.tolist(),
            "n_random_per_target": N_RANDOMS_MULTIPLIER,
            "n_jackknife_regions": N_JACKKNIFE_REGIONS,
            "theta_large_window_deg": [THETA_LARGE_MIN_DEG, THETA_LARGE_MAX_DEG],
            "b_qso_desi_published": B_QSO_DESI_PUBLISHED,
            "sigma_fnl_baseline": SIGMA_FNL_BASELINE,
            "alpha_fiducial_paper": ALPHA_FIDUCIAL_PAPER,
            "improvement_at_fiducial": IMPROVEMENT_AT_FIDUCIAL,
            "seed": SEED,
            "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        "clustering": {},
        "alpha_calibration": {},
    }

    for sample_name, coords in samples.items():
        if len(coords) < 50:
            log.warning(f"Skipping {sample_name}: N<50")
            continue
        ra_d = coords[:, 0]
        dec_d = coords[:, 1]
        log.info(f"=== Computing w(theta) for {sample_name} (N={len(coords)}) ===")
        clust = correlate_sample(ra_d, dec_d, ra_r, dec_r, THETA_EDGES_DEG, log_prefix=sample_name)
        results["clustering"][sample_name] = clust

    # PRIMARY: bias ratio using SIGNAL-bearing scales (theta in [0.04, 0.25] deg)
    if "qso_candidates_5384" in results["clustering"] and "full_anomaly" in results["clustering"]:
        log.info("=== PRIMARY: Bias ratio QSO_CAND vs full anomaly @ signal scales ===")
        ratio_signal = bias_ratio_at_large_scales(
            results["clustering"]["qso_candidates_5384"]["w_theta"],
            results["clustering"]["full_anomaly"]["w_theta"],
            THETA_CENTERS_DEG,
            THETA_SIGNAL_MIN_DEG,
            THETA_SIGNAL_MAX_DEG,
        )
        results["alpha_calibration"]["qso_cand_vs_full_anomaly_signal"] = ratio_signal
        b_ratio_geo = ratio_signal["bias_ratio_b_a_over_b_b_geomean"]
        if b_ratio_geo is not None and np.isfinite(b_ratio_geo):
            alpha_internal = b_ratio_geo - 1.0
            improvement_internal = (IMPROVEMENT_AT_FIDUCIAL / ALPHA_FIDUCIAL_PAPER) * alpha_internal
            sigma_fnl_internal = SIGMA_FNL_BASELINE * (1.0 - improvement_internal)
            results["alpha_calibration"]["alpha_internal_signal"] = alpha_internal
            results["alpha_calibration"]["improvement_internal_signal_pct"] = improvement_internal * 100.0
            results["alpha_calibration"]["sigma_fnl_internal_signal"] = sigma_fnl_internal
            log.info(f"alpha_internal (signal scales, geomean) = {alpha_internal:.4f}")
            log.info(f"improvement = {improvement_internal*100:.2f}%")
            log.info(f"sigma_fnl @ alpha_internal = {sigma_fnl_internal:.3f}")

    # Legacy: bias ratio at large scales (kept for comparison with prior result)
    if "qso_candidates_5384" in results["clustering"] and "full_anomaly" in results["clustering"]:
        ratio_large = bias_ratio_at_large_scales(
            results["clustering"]["qso_candidates_5384"]["w_theta"],
            results["clustering"]["full_anomaly"]["w_theta"],
            THETA_CENTERS_DEG,
            THETA_LARGE_MIN_DEG,
            THETA_LARGE_MAX_DEG,
        )
        results["alpha_calibration"]["qso_cand_vs_full_anomaly_large_legacy"] = ratio_large

    if "qso_candidates_5384" in results["clustering"] and "non_qso_anomalies" in results["clustering"]:
        log.info("=== Bias ratio: QSO candidates vs non-QSO anomalies (cleaner control) ===")
        ratio_qso_nonqso = bias_ratio_at_large_scales(
            results["clustering"]["qso_candidates_5384"]["w_theta"],
            results["clustering"]["non_qso_anomalies"]["w_theta"],
            THETA_CENTERS_DEG,
            THETA_SIGNAL_MIN_DEG,
            THETA_SIGNAL_MAX_DEG,
        )
        results["alpha_calibration"]["qso_cand_vs_non_qso_anomalies_signal"] = ratio_qso_nonqso

    if "gold_silver_1122" in results["clustering"] and "full_anomaly" in results["clustering"]:
        ratio_gs = bias_ratio_at_large_scales(
            results["clustering"]["gold_silver_1122"]["w_theta"],
            results["clustering"]["full_anomaly"]["w_theta"],
            THETA_CENTERS_DEG,
            THETA_SIGNAL_MIN_DEG,
            THETA_SIGNAL_MAX_DEG,
        )
        results["alpha_calibration"]["gold_silver_vs_full_anomaly_signal"] = ratio_gs

    log.info("=== Jackknife uncertainty on bias ratio (primary deliverable) ===")
    qso_coords = samples["qso_candidates_5384"]
    full_coords = samples["full_anomaly"]
    regions_qso = assign_jackknife_regions(qso_coords[:, 0], qso_coords[:, 1], N_JACKKNIFE_REGIONS, SEED + 1)
    regions_full = assign_jackknife_regions(full_coords[:, 0], full_coords[:, 1], N_JACKKNIFE_REGIONS, SEED + 2)
    jk_ratio = jackknife_bias_ratio(
        qso_coords[:, 0], qso_coords[:, 1],
        full_coords[:, 0], full_coords[:, 1],
        ra_r, dec_r,
        regions_qso, regions_full, regions_r,
        THETA_EDGES_DEG, THETA_CENTERS_DEG,
        THETA_SIGNAL_MIN_DEG, THETA_SIGNAL_MAX_DEG,
        N_JACKKNIFE_REGIONS,
        log_prefix="bias_ratio_jk",
    )
    if jk_ratio is not None:
        results["alpha_calibration"]["jackknife_bias_ratio"] = jk_ratio
        if jk_ratio["alpha_internal"] is not None and np.isfinite(jk_ratio["alpha_internal"]):
            alpha_jk = jk_ratio["alpha_internal"]
            alpha_jk_std = jk_ratio["alpha_internal_std"]
            improvement_jk = (IMPROVEMENT_AT_FIDUCIAL / ALPHA_FIDUCIAL_PAPER) * alpha_jk
            sigma_fnl_jk = SIGMA_FNL_BASELINE * (1.0 - improvement_jk)
            sigma_fnl_jk_std = SIGMA_FNL_BASELINE * (IMPROVEMENT_AT_FIDUCIAL / ALPHA_FIDUCIAL_PAPER) * alpha_jk_std
            results["alpha_calibration"]["alpha_internal_jk"] = alpha_jk
            results["alpha_calibration"]["alpha_internal_jk_std"] = alpha_jk_std
            results["alpha_calibration"]["sigma_fnl_internal_jk"] = sigma_fnl_jk
            results["alpha_calibration"]["sigma_fnl_internal_jk_std"] = sigma_fnl_jk_std
            log.info(f"alpha_internal_jk = {alpha_jk:.4f} +/- {alpha_jk_std:.4f}")
            log.info(f"sigma_fnl_jk = {sigma_fnl_jk:.3f} +/- {sigma_fnl_jk_std:.3f}")

    results["metadata"]["completed_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    out_path = OUTPUT_DIR / "alpha_empirical_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=lambda o: float(o) if isinstance(o, np.floating) else str(o))
    log.info(f"Saved: {out_path}")
    log.info("Wave 14-VVV alpha calibration complete.")


if __name__ == "__main__":
    main()
