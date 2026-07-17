#!/usr/bin/env python3
"""
G3 (open-compute gate) — JOINT covariance across the four chirality estimators.

The reviewers' standing gate M4 ("all residuals are systematics" asserted
without a joint statistical framework) asks for a single covariance/likelihood
that ties the estimators together, rather than four separately-reported nulls.
This script computes the JOINT sampling covariance of the paper's committed
estimators under one shared block-bootstrap, so their correlation structure is
measured on the SAME resamples (the object a joint framework requires).

Estimators evaluated per resample (all on the primary HC sample, canonical mask):
  1. A_dipole_realspace  — uniform-pixel-weight real-space dipole amplitude
                            |a| from the fit A_p = m + a . n_hat (the paper's
                            PRIMARY z_mom estimator family; unit pixel weights).
  2. A_dipole_WLS        — nuisance-marginalized WLS dipole amplitude from the
                            design {dipole_xyz, leg_BASS, leg_DECaLS, leg_DES,
                            density, density^2, const}, weighted by n_total
                            (matches scripts/joint_nuisance_bootstrap_sigma.py).
  3. monopole            — global CW-fraction offset f_CW - 0.5 (the -9.47 sigma
                            monopole), spiral-count weighted over the mask.
  4. Cl1_pseudo          — mask-coupled harmonic l=1 pseudo-power C_1 of the
                            monopole-subtracted A_p map via healpy.anafast.
                            NaMaster-free proxy for the MASTER l=1 leg (see NOTE).

NOTE on the MASTER leg: a fully MASTER-decoupled l=1 (mode-coupling matrix
inverse) requires NaMaster/pymaster, which is NOT installed in this local
environment. Estimator 4 here is the mask-COUPLED pseudo-C_1 (anafast), which
is a legitimate harmonic estimator and co-varies with the others under the same
resampling. The MASTER-decoupled refinement (identical bootstrap, C_decoupled =
M^{-1} pseudo_C) is a pod-bound extension (resume A4000 + install NaMaster) and
is flagged in COMPUTE_CAMPAIGN. The joint 3x3 sub-block over estimators 1-3 is
NaMaster-independent and fully final.

Sample: primary HC = (class_eq in {CW,CCW}) & (confidence_eq > 0.6) = 949,584
(reproduces the canonical HC count exactly). The strict primary (890,069, which
additionally removes the 59,515 raw_flip_qc_unsafe rows) needs the quarantine
flag from the separate payload and is a documented refinement, not a blocker.

Inputs (committed / locally cached, offline):
  HF dataset bamfai/galaxy-chirality-catalog :: catalog_production.parquet
  (cached under ~/.cache/huggingface; 8,474,531 rows; cols ra/dec/class_eq/
  confidence_eq). No network needed if the snapshot is cached.

Output:
  outputs/canonical_provenance/g3_joint_estimator_covariance.json  (final)
  outputs/canonical_provenance/g3_joint_estimator_covariance.partial.json
      (checkpoint written every CHECKPOINT_EVERY iters so a future session can
       monitor / resume-decide without re-reading the log)

Run:
  python3 scripts/g3_joint_estimator_covariance.py            # full N=2000
  python3 scripts/g3_joint_estimator_covariance.py --smoke    # N=20 quick test
"""
from __future__ import annotations

import glob
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import healpy as hp
import pandas as pd

# ---------------------------------------------------------------- config
NSIDE_DATA = 64
NSIDE_BLOCK = 8
LMAX = 3 * NSIDE_DATA - 1  # 191
N_BOOTSTRAP = 2000
SEED = 42
CONF_THRESH = 0.6
CHECKPOINT_EVERY = 100
DEC_LEG_BOUNDARIES = (-20.0, 32.0)
GAL_LAT_CUT_DEG = 15.0
ESTIMATOR_NAMES = ["A_dipole_realspace", "A_dipole_WLS", "monopole", "Cl1_pseudo"]

REPO = Path(__file__).resolve().parents[1]  # pipelines/p2_chirality
OUT = REPO / "outputs" / "canonical_provenance" / "g3_joint_estimator_covariance.json"
OUT_PARTIAL = OUT.with_suffix(".partial.json")

SMOKE = "--smoke" in sys.argv
if SMOKE:
    N_BOOTSTRAP = 20
    CHECKPOINT_EVERY = 5

t0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time()-t0:7.1f}s] {msg}", flush=True)


def find_catalog() -> str:
    cands = sorted(
        glob.glob(
            os.path.expanduser(
                "~/.cache/huggingface/hub/datasets--bamfai--galaxy-chirality-catalog/"
                "snapshots/*/catalog_production.parquet"
            )
        )
    )
    if not cands:
        raise SystemExit(
            "catalog_production.parquet not found in HF cache. "
            "Run with HF_TOKEN set to download bamfai/galaxy-chirality-catalog, "
            "or point this script at a local copy."
        )
    return cands[-1]


def galactic_lat_mask(nside: int) -> np.ndarray:
    """Canonical mask: |b_gal| > 15 deg (float 1/0 per pixel)."""
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    rot = hp.Rotator(coord=["C", "G"])
    theta_g, _ = rot(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > GAL_LAT_CUT_DEG).astype(float)


def build_static():
    """Load catalog, select primary HC, precompute per-galaxy pixel/superpixel/leg."""
    cat = find_catalog()
    log(f"loading catalog {cat.split('snapshots/')[1][:12]} ...")
    df = pd.read_parquet(cat, columns=["ra", "dec", "class_eq", "confidence_eq"])
    hc = df["class_eq"].isin(["CW", "CCW"]) & (df["confidence_eq"] > CONF_THRESH)
    df = df.loc[hc].reset_index(drop=True)
    n_gal = len(df)
    log(f"primary HC spirals: {n_gal:,} (expect 949,584)")

    ra = df["ra"].values.astype(np.float64)
    dec = df["dec"].values.astype(np.float64)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)

    theta = np.deg2rad(90.0 - dec)
    phi = np.deg2rad(ra)
    pix = hp.ang2pix(NSIDE_DATA, theta, phi).astype(np.int64)
    superpix = hp.ang2pix(NSIDE_BLOCK, theta, phi).astype(np.int64)

    dec_lo, dec_hi = DEC_LEG_BOUNDARIES
    leg = np.full(n_gal, 1, np.int8)  # 0=BASS,1=DECaLS,2=DES
    leg[dec > dec_hi] = 0
    leg[dec < dec_lo] = 2

    # group galaxy indices by superpixel (block-bootstrap unit)
    order = np.argsort(superpix, kind="stable")
    sp_sorted = superpix[order]
    uniq_sp, starts = np.unique(sp_sorted, return_index=True)
    ends = np.append(starts[1:], len(sp_sorted))
    sp_to_idx = {int(sp): order[s:e] for sp, s, e in zip(uniq_sp, starts, ends)}
    log(f"HC sample spans {uniq_sp.size} superpixels (NSIDE={NSIDE_BLOCK})")

    npix = hp.nside2npix(NSIDE_DATA)
    mask = galactic_lat_mask(NSIDE_DATA)  # 1/0 per pixel, geometry only
    thp, php = hp.pix2ang(NSIDE_DATA, np.arange(npix))
    n_hat = np.column_stack(
        [np.sin(thp) * np.cos(php), np.sin(thp) * np.sin(php), np.cos(thp)]
    )
    return dict(
        pix=pix, superpix=superpix, is_cw=is_cw, leg=leg,
        uniq_sp=uniq_sp, sp_to_idx=sp_to_idx, npix=npix, mask=mask,
        n_hat=n_hat, n_gal=n_gal, catalog=cat,
    )


def estimators_from_indices(idx, S) -> np.ndarray:
    """Compute the 4-estimator vector from a set of galaxy indices."""
    npix = S["npix"]
    pix = S["pix"][idx]
    is_cw = S["is_cw"][idx]
    leg = S["leg"][idx]

    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw = np.bincount(pix[is_cw == 1], minlength=npix).astype(np.float64)
    n_BASS = np.bincount(pix[leg == 0], minlength=npix).astype(np.float64)
    n_DECaLS = np.bincount(pix[leg == 1], minlength=npix).astype(np.float64)
    n_DES = np.bincount(pix[leg == 2], minlength=npix).astype(np.float64)

    in_mask = (S["mask"] > 0) & (n_total > 0)
    ip = np.where(in_mask)[0]
    if ip.size < 50:
        return np.full(4, np.nan)

    A_p = np.zeros(npix)
    A_p[ip] = 2.0 * (n_cw[ip] / n_total[ip]) - 1.0

    w_spiral = n_total[ip]
    # ---- 3. monopole: global CW-fraction offset (spiral-count weighted)
    f_cw_global = n_cw[ip].sum() / n_total[ip].sum()
    monopole = f_cw_global - 0.5

    # center A_p on its spiral-weighted mask mean (monopole removed for dipole/harmonic)
    A_bar = np.average(A_p[ip], weights=w_spiral)
    A_p_c = A_p.copy()
    A_p_c[ip] = A_p[ip] - A_bar

    nh = S["n_hat"][ip]
    # ---- 1. real-space dipole: uniform-pixel-weight LS fit A_p = m + a.n_hat
    M1 = np.column_stack([np.ones(ip.size), nh[:, 0], nh[:, 1], nh[:, 2]])
    try:
        c1, *_ = np.linalg.lstsq(M1, A_p[ip], rcond=None)
        A_dipole_rs = float(np.linalg.norm(c1[1:4]))
    except np.linalg.LinAlgError:
        A_dipole_rs = np.nan

    # ---- 2. WLS nuisance-marginalized dipole (n_total-weighted, full design)
    safe = np.maximum(n_total, 1.0)
    f_B = (n_BASS / safe)[ip]
    f_D = (n_DECaLS / safe)[ip]
    f_S = (n_DES / safe)[ip]
    rho = (n_total / max(n_total[ip].mean(), 1.0))[ip]
    for col in (f_B, f_D, f_S, rho):
        col -= np.average(col, weights=w_spiral)
    rho2 = rho ** 2
    rho2 -= np.average(rho2, weights=w_spiral)
    M2 = np.column_stack(
        [nh[:, 0], nh[:, 1], nh[:, 2], f_B, f_D, f_S, rho, rho2, np.ones(ip.size)]
    )
    sw = np.sqrt(w_spiral)
    try:
        a2 = np.linalg.solve((M2 * sw[:, None]).T @ (M2 * sw[:, None]),
                             (M2 * sw[:, None]).T @ (A_p_c[ip] * sw))
        A_dipole_wls = float(np.linalg.norm(a2[:3]))
    except np.linalg.LinAlgError:
        A_dipole_wls = np.nan

    # ---- 4. mask-coupled harmonic l=1 pseudo-power (anafast; NaMaster-free)
    masked = np.zeros(npix)
    masked[ip] = A_p_c[ip]
    cl = hp.anafast(masked, lmax=LMAX)
    Cl1 = float(cl[1])

    return np.array([A_dipole_rs, A_dipole_wls, monopole, Cl1])


def write_partial(state: dict) -> None:
    OUT_PARTIAL.parent.mkdir(parents=True, exist_ok=True)
    OUT_PARTIAL.write_text(json.dumps(state, indent=2))


def main() -> None:
    rng = np.random.default_rng(SEED)
    S = build_static()

    all_idx = np.arange(S["n_gal"])
    full_vec = estimators_from_indices(all_idx, S)
    log("full-sample estimators: " + ", ".join(
        f"{n}={v:.6g}" for n, v in zip(ESTIMATOR_NAMES, full_vec)))

    uniq_sp = S["uniq_sp"]
    n_sp = uniq_sp.size
    sp_to_idx = S["sp_to_idx"]

    boots = np.full((N_BOOTSTRAP, 4), np.nan)
    log(f"running {N_BOOTSTRAP} block-bootstrap resamples "
        f"({'SMOKE' if SMOKE else 'FULL'}) ...")
    for b in range(N_BOOTSTRAP):
        chosen = rng.choice(uniq_sp, size=n_sp, replace=True)
        idx = np.concatenate([sp_to_idx[int(sp)] for sp in chosen])
        boots[b] = estimators_from_indices(idx, S)
        if (b + 1) % CHECKPOINT_EVERY == 0:
            valid = ~np.isnan(boots[:, 0])
            nv = int(valid.sum())
            log(f"  {b+1}/{N_BOOTSTRAP}  (valid={nv})")
            write_partial({
                "status": "running",
                "completed": b + 1,
                "n_bootstrap": N_BOOTSTRAP,
                "n_valid": nv,
                "estimator_names": ESTIMATOR_NAMES,
                "full_sample": {n: (None if np.isnan(v) else float(v))
                                for n, v in zip(ESTIMATOR_NAMES, full_vec)},
                "elapsed_s": round(time.time() - t0, 1),
            })

    valid = ~np.isnan(boots).any(axis=1)
    B = boots[valid]
    nv = int(valid.sum())
    log(f"valid resamples: {nv}/{N_BOOTSTRAP}")

    cov = np.cov(B.T, ddof=1)
    corr = np.corrcoef(B.T)
    sigma = B.std(axis=0, ddof=1)
    mean = B.mean(axis=0)
    # z of the full-sample statistic under its own bootstrap sigma
    z_self = [(float(full_vec[i]) / sigma[i]) if sigma[i] > 0 else None
              for i in range(4)]

    result = {
        "script": "scripts/g3_joint_estimator_covariance.py",
        "gate": "G3 — joint covariance across estimators",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "catalog_snapshot": S["catalog"].split("snapshots/")[1][:40],
        "sample": f"primary HC (class_eq in CW/CCW & confidence_eq>{CONF_THRESH})",
        "n_galaxies": int(S["n_gal"]),
        "mask": f"|b_gal| > {GAL_LAT_CUT_DEG} deg & n_total>0",
        "nside_data": NSIDE_DATA,
        "nside_block": NSIDE_BLOCK,
        "lmax": LMAX,
        "n_bootstrap": N_BOOTSTRAP,
        "n_valid": nv,
        "seed": SEED,
        "smoke": SMOKE,
        "estimator_names": ESTIMATOR_NAMES,
        "full_sample": {n: float(v) for n, v in zip(ESTIMATOR_NAMES, full_vec)},
        "bootstrap_mean": {n: float(v) for n, v in zip(ESTIMATOR_NAMES, mean)},
        "bootstrap_sigma": {n: float(v) for n, v in zip(ESTIMATOR_NAMES, sigma)},
        "z_full_over_bootstrap_sigma": {n: z for n, z in zip(ESTIMATOR_NAMES, z_self)},
        "joint_covariance": cov.tolist(),
        "joint_correlation": corr.tolist(),
        "master_leg_note": (
            "Cl1_pseudo is the mask-COUPLED anafast l=1 (NaMaster absent locally). "
            "MASTER-decoupled refinement is pod-bound; the 3x3 sub-block over "
            "estimators 1-3 (A_dipole_realspace, A_dipole_WLS, monopole) is "
            "NaMaster-independent and final."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    write_partial({"status": "done", "completed": N_BOOTSTRAP, "n_valid": nv,
                   "output": str(OUT), "elapsed_s": round(time.time() - t0, 1)})
    log(f"wrote {OUT}")
    print("\n=== JOINT CORRELATION MATRIX ===", flush=True)
    print("            " + "".join(f"{n[:10]:>12}" for n in ESTIMATOR_NAMES))
    for i, n in enumerate(ESTIMATOR_NAMES):
        print(f"{n[:10]:>10}  " + "".join(f"{corr[i, j]:+12.3f}" for j in range(4)))
    print("\n=== bootstrap sigma / z(full/sigma) ===")
    for i, n in enumerate(ESTIMATOR_NAMES):
        zz = z_self[i]
        print(f"  {n:>20}: full={full_vec[i]:+.5g}  sigma={sigma[i]:.5g}  "
              f"z={'nan' if zz is None else f'{zz:+.2f}'}")


if __name__ == "__main__":
    main()
