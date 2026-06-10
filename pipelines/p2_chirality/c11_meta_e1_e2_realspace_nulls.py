#!/usr/bin/env python3
"""R23conf closures P4-META-E1 + P4-META-E2 (real-space channel).

META-E1: recompute the headline real-space dipole significance under
  (i)   the published per-pixel permutation null (reproduction check),
  (ii)  a per-galaxy label-shuffle null (multivariate hypergeometric draw
        preserving N_spiral(p) and the global CW count exactly), and
  (iii) a variance-aware (N_spiral(p)-weighted) LS dipole fit, with its own
        per-galaxy label-shuffle null.
  All on the canonical mask (N_spiral(p) >= 10), full Catalog C spirals,
  NSIDE=64, uniform pixel weighting for (i)-(ii) per Sec. IV C.a.

META-E2: axis-resolved spot check of the Table V real-space injection-
  recovery at A = 0.75% (HC-broad, p_eq > 0.6): 10 fixed axes drawn
  uniformly on the sphere, 100 injections each, against the same
  binomial per-pixel-shuffle null calibration as injection_sweep_extended.py.

Output: outputs/canonical_provenance/c11_meta_e1_e2_realspace_nulls.json
"""
import json
import time

import healpy as hp
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download

NSIDE = 64
MIN_SPIRALS = 10          # canonical mask: N_spiral(p) >= 10
N_MC = 10_000             # null realizations for META-E1 legs
SEED = 42
N_AXES = 10               # META-E2 spot check
N_INJ_PER_AXIS = 100
N_NULL_INJ = 1000
A_INJ_PCT = 0.75          # full amplitude, percent
OUT = "outputs/canonical_provenance/c11_meta_e1_e2_realspace_nulls.json"

t0 = time.time()


def log(msg):
    print(f"[{time.time()-t0:7.1f}s] {msg}", flush=True)


def rank_p(null_amps, data_amp):
    """(k+1)/(N+1) one-sided empirical rank (paper convention)."""
    k = int(np.sum(null_amps >= data_amp))
    return k, (k + 1) / (len(null_amps) + 1)


def fit_dipole_uniform(asym_in_mask, mask_idx, npix):
    m = np.full(npix, hp.UNSEEN)
    m[mask_idx] = asym_in_mask
    _, dip = hp.fit_dipole(m, gal_cut=0)
    return float(np.sqrt(np.sum(dip ** 2)))


def fit_dipole_weighted(asym, w, X):
    """Weighted LS fit of A_p = m + a.n_p; returns |a|."""
    A = (X * w[:, None]).T @ X
    b = (X * w[:, None]).T @ asym
    c = np.linalg.solve(A, b)
    return float(np.sqrt(np.sum(c[:3] ** 2)))


def main():
    log("Resolving cached catalog parquet (local_files_only)...")
    path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet",
        repo_type="dataset", local_files_only=True,
    )
    log(f"parquet: {path}")
    df = pd.read_parquet(path, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    n_spiral_total = len(spirals)
    log(f"Catalog C spirals (full, no confidence cut): {n_spiral_total:,}")

    npix = hp.nside2npix(NSIDE)
    theta = np.radians(90.0 - spirals["dec"].values)
    phi = np.radians(spirals["ra"].values % 360)
    pix = hp.ang2pix(NSIDE, theta, phi)
    is_cw = (spirals["class_eq"].values == "CW")
    n_cw_map = np.bincount(pix[is_cw], minlength=npix).astype(float)
    n_sp_map = np.bincount(pix, minlength=npix).astype(float)

    mask = n_sp_map >= MIN_SPIRALS
    mask_idx = np.where(mask)[0]
    n_pix_used = int(mask.sum())
    f_sky = n_pix_used / npix
    n_sp_in = n_sp_map[mask]
    n_cw_in = n_cw_map[mask]
    n_cw_tot_in = int(n_cw_in.sum())
    n_sp_tot_in = int(n_sp_in.sum())
    log(f"canonical mask: n_pix={n_pix_used}, f_sky={f_sky:.5f}, "
        f"spirals in mask={n_sp_tot_in:,}, CW in mask={n_cw_tot_in:,}")

    asym_obs = (2.0 * n_cw_in - n_sp_in) / n_sp_in  # A_p
    amp_obs = fit_dipole_uniform(asym_obs, mask_idx, npix)
    log(f"observed uniform-weight dipole amplitude |a| = {amp_obs:.6e}")

    # direction vectors for weighted fit
    th_p, ph_p = hp.pix2ang(NSIDE, mask_idx)
    X = np.column_stack([
        np.sin(th_p) * np.cos(ph_p),
        np.sin(th_p) * np.sin(ph_p),
        np.cos(th_p),
        np.ones(n_pix_used),
    ])
    w_var = n_sp_in.copy()  # inverse-variance ~ N_spiral(p)
    amp_obs_w = fit_dipole_weighted(asym_obs, w_var, X)
    log(f"observed N_spiral-weighted dipole amplitude |a| = {amp_obs_w:.6e}")

    rng = np.random.default_rng(SEED)

    # ---- (i) per-pixel permutation null (published convention) ----
    log(f"null (i): per-pixel permutation x {N_MC} ...")
    vals = asym_obs.copy()
    amps_perm = np.empty(N_MC)
    for k in range(N_MC):
        rng.shuffle(vals)
        amps_perm[k] = fit_dipole_uniform(vals, mask_idx, npix)
        if (k + 1) % 2000 == 0:
            log(f"  perm {k+1}/{N_MC}")
    z_perm = (amp_obs - amps_perm.mean()) / amps_perm.std(ddof=1)
    k_perm, p_perm = rank_p(amps_perm, amp_obs)
    log(f"  (i) z_mom={z_perm:+.3f}, rank p={p_perm:.4f} (k={k_perm})")

    # ---- (ii) per-galaxy label-shuffle null (hypergeometric) ----
    log(f"null (ii): per-galaxy label shuffle x {N_MC} ...")
    colors = n_sp_in.astype(np.int64)
    amps_pg = np.empty(N_MC)
    amps_pg_w = np.empty(N_MC)
    for k in range(N_MC):
        ncw = rng.multivariate_hypergeometric(colors, n_cw_tot_in, method="marginals")
        a_null = (2.0 * ncw - n_sp_in) / n_sp_in
        amps_pg[k] = fit_dipole_uniform(a_null, mask_idx, npix)
        amps_pg_w[k] = fit_dipole_weighted(a_null, w_var, X)
        if (k + 1) % 2000 == 0:
            log(f"  pg-shuffle {k+1}/{N_MC}")
    z_pg = (amp_obs - amps_pg.mean()) / amps_pg.std(ddof=1)
    k_pg, p_pg = rank_p(amps_pg, amp_obs)
    z_pg_w = (amp_obs_w - amps_pg_w.mean()) / amps_pg_w.std(ddof=1)
    k_pg_w, p_pg_w = rank_p(amps_pg_w, amp_obs_w)
    log(f"  (ii) uniform-weight fit vs per-galaxy null: z_mom={z_pg:+.3f}, p={p_pg:.4f} (k={k_pg})")
    log(f"  (iii) N_spiral-weighted fit vs per-galaxy null: z_mom={z_pg_w:+.3f}, p={p_pg_w:.4f} (k={k_pg_w})")

    # ---- META-E2: axis-resolved injection spot check (HC-broad) ----
    log("META-E2: HC-broad (p_eq>0.6) axis-resolved injection at A=0.75% ...")
    max_eq = np.maximum(spirals["p_cw_eq"].values, spirals["p_ccw_eq"].values)
    hc = max_eq > 0.6
    pix_hc = pix[hc]
    is_cw_hc = is_cw[hc]
    n_tot_hc = np.bincount(pix_hc, minlength=npix)
    n_cw_hc = np.bincount(pix_hc[is_cw_hc], minlength=npix)
    p_cw_global_hc = n_cw_hc.sum() / n_tot_hc.sum()
    log(f"  HC spirals: {int(hc.sum()):,}; p_cw_global={p_cw_global_hc:.5f}")

    nz = n_tot_hc > 0
    nz_idx = np.where(nz)[0]
    th_a, ph_a = hp.pix2ang(NSIDE, nz_idx)
    Xa = np.column_stack([
        np.sin(th_a) * np.cos(ph_a),
        np.sin(th_a) * np.sin(ph_a),
        np.cos(th_a),
        np.ones(len(nz_idx)),
    ])
    w_hc = n_tot_hc[nz].astype(float)

    def dip_amp_counts(ncw_arr):
        # injection_sweep_extended.py convention: weighted fit on f_CW, amp = 2|a|
        p_arr = ncw_arr / w_hc
        A = (Xa * w_hc[:, None]).T @ Xa
        b = (Xa * w_hc[:, None]).T @ p_arr
        c = np.linalg.solve(A, b)
        return float(2.0 * np.sqrt(np.sum(c[:3] ** 2)))

    rng2 = np.random.default_rng(SEED)
    log(f"  null calibration ({N_NULL_INJ} binomial draws)...")
    null_amps = np.empty(N_NULL_INJ)
    for k in range(N_NULL_INJ):
        ncw_null = rng2.binomial(n_tot_hc[nz], p_cw_global_hc)
        null_amps[k] = dip_amp_counts(ncw_null)
    null_mean, null_std = null_amps.mean(), null_amps.std(ddof=1)
    log(f"  null amp: mean={null_mean*100:.4f}%, std={null_std*100:.4f}%")

    # 10 fixed axes, uniform on the sphere (area-uniform; cos(theta)~U)
    rng3 = np.random.default_rng(20260609)
    cos_t = rng3.uniform(-1, 1, N_AXES)
    phis = rng3.uniform(0, 2 * np.pi, N_AXES)
    sin_t = np.sqrt(1 - cos_t ** 2)
    axes = np.column_stack([sin_t * np.cos(phis), sin_t * np.sin(phis), cos_t])

    pix_xyz = np.column_stack([
        np.sin(th_a) * np.cos(ph_a),
        np.sin(th_a) * np.sin(ph_a),
        np.cos(th_a),
    ])
    A_full = A_INJ_PCT / 100.0
    per_axis = []
    for ax_i, ax in enumerate(axes):
        cos_ax = pix_xyz @ ax
        p_inj = np.clip(p_cw_global_hc + 0.5 * A_full * cos_ax, 0.001, 0.999)
        sigmas = np.empty(N_INJ_PER_AXIS)
        for j in range(N_INJ_PER_AXIS):
            ncw_inj = rng2.binomial(n_tot_hc[nz], p_inj)
            sigmas[j] = (dip_amp_counts(ncw_inj) - null_mean) / null_std
        per_axis.append({
            "axis_xyz_equatorial": [float(v) for v in ax],
            "P_sigma_gt_3": float(np.mean(sigmas > 3)),
            "median_sigma": float(np.median(sigmas)),
        })
        log(f"  axis {ax_i+1}/{N_AXES}: P(s>3)={per_axis[-1]['P_sigma_gt_3']:.2f}, "
            f"med sigma={per_axis[-1]['median_sigma']:.2f}")

    p3 = np.array([a["P_sigma_gt_3"] for a in per_axis])
    e2_summary = {
        "amplitude_full_pct": A_INJ_PCT,
        "n_axes": N_AXES,
        "n_inj_per_axis": N_INJ_PER_AXIS,
        "axis_sampling": "uniform on the sphere (cos(theta)~U(-1,1)), seed 20260609",
        "P3_axis_mean": float(p3.mean()),
        "P3_min": float(p3.min()),
        "P3_max": float(p3.max()),
        "P3_p16": float(np.percentile(p3, 16)),
        "P3_p84": float(np.percentile(p3, 84)),
        "published_table_v_value_at_0p75": 0.55,
        "published_axis_protocol": "injection_sweep_extended.py draws a NEW random axis per injection (theta~U(0,pi), phi~U(0,2pi)); Table V P values are therefore averages over that random-axis ensemble",
    }

    out = {
        "job": "C11-P4-R23conf-META-E1-E2-realspace-nulls",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "closes": ["P4-META-E1", "P4-META-E2"],
        "config": {
            "nside": NSIDE, "min_spirals_per_pix": MIN_SPIRALS,
            "n_mc": N_MC, "seed": SEED,
            "catalog_parquet": path,
            "rank_p_convention": "(k+1)/(N+1), one-sided",
        },
        "catalog": {
            "n_spiral_total": n_spiral_total,
            "n_pix_canonical": n_pix_used,
            "f_sky_canonical": f_sky,
            "n_spiral_in_mask": n_sp_tot_in,
            "n_cw_in_mask": n_cw_tot_in,
        },
        "meta_e1": {
            "observed_amp_uniform": amp_obs,
            "observed_amp_nspiral_weighted": amp_obs_w,
            "null_i_pixel_permutation": {
                "z_mom": float(z_perm), "k": k_perm, "rank_p": float(p_perm),
                "null_mean": float(amps_perm.mean()), "null_std": float(amps_perm.std(ddof=1)),
            },
            "null_ii_per_galaxy_label_shuffle_uniform_fit": {
                "z_mom": float(z_pg), "k": k_pg, "rank_p": float(p_pg),
                "null_mean": float(amps_pg.mean()), "null_std": float(amps_pg.std(ddof=1)),
            },
            "null_iii_per_galaxy_label_shuffle_weighted_fit": {
                "z_mom": float(z_pg_w), "k": k_pg_w, "rank_p": float(p_pg_w),
                "null_mean": float(amps_pg_w.mean()), "null_std": float(amps_pg_w.std(ddof=1)),
            },
        },
        "meta_e2": {"per_axis": per_axis, "summary": e2_summary,
                     "hc_subsample": {"n_hc": int(hc.sum()),
                                       "p_cw_global": float(p_cw_global_hc),
                                       "null_mean_amp_pct": float(null_mean * 100),
                                       "null_std_amp_pct": float(null_std * 100)}},
    }
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    log(f"saved {OUT}")


if __name__ == "__main__":
    main()
