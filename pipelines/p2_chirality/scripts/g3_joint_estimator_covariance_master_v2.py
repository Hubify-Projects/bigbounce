#!/usr/bin/env python3
"""
G3 MASTER-leg refinement — JOINT covariance with the NaMaster MASTER-DECOUPLED
l=1 estimator as the 4th channel.

This is the pod-bound refinement flagged in COMPUTE_CAMPAIGN_2026-07-17.md
("MASTER-leg refinement (pod-bound, flagged not blocked)"). It reruns the
IDENTICAL block-bootstrap as the committed
scripts/g3_joint_estimator_covariance.py (same NSIDE=8 superpixel blocks, same
N=2000 resamples, same seed=42, same rng call sequence -> byte-identical
resample index sets), swapping estimator 4 from the mask-coupled anafast
pseudo-C_1 proxy to the MASTER-decoupled C_1:

    C_decoupled = M^{-1} C_pseudo

with the mode-coupling matrix M computed once by NaMaster on the FIXED
canonical effective mask (|b_gal| > 15 deg AND n_total_fullsample > 0, binary),
single-ell bandpowers starting at ell=1 (bin 0 == ell 1), following the
coupling-matrix path of scripts/master_decoupled_monopole_null.py.

Convention (recorded honestly): the workspace/mask is FIXED at the full-sample
effective mask; each bootstrap resample's centered CW-asymmetry map A_p_c is
laid onto that fixed mask (pixels empty in the resample carry 0, exactly the
convention the committed anafast leg uses). The decoupled C_1 is therefore a
well-defined estimator whose sampling covariance the bootstrap measures.

Per resample we evaluate FIVE quantities:
  1. A_dipole_realspace   (identical to committed g3)
  2. A_dipole_WLS         (identical to committed g3)
  3. monopole             (identical to committed g3)
  4. Cl1_master           (NEW: MASTER-decoupled l=1)
  5. Cl1_pseudo           (the committed anafast proxy, kept as cross-check)

Primary output: the 4x4 covariance/correlation over channels 1-4 (with
Cl1_master as the 4th channel), plus the 5x5 including the pseudo proxy and
the scalar corr(Cl1_master, Cl1_pseudo) as the proxy-validity readout.

Output:
  outputs/canonical_provenance/g3_joint_estimator_covariance_master_v2.json
  (+ .partial.json checkpoints)

Run:
  python3 g3_joint_estimator_covariance_master_v2.py            # full N=2000
  python3 g3_joint_estimator_covariance_master_v2.py --smoke    # N=20
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
import pymaster as nmt

# ---------------------------------------------------------------- config
# (identical to the committed g3_joint_estimator_covariance.py)
NSIDE_DATA = 64
NSIDE_BLOCK = 8
LMAX = 3 * NSIDE_DATA - 1  # 191
N_BOOTSTRAP = 2000
SEED = 42
CONF_THRESH = 0.6
CHECKPOINT_EVERY = 100
DEC_LEG_BOUNDARIES = (-20.0, 32.0)
GAL_LAT_CUT_DEG = 15.0
ESTIMATOR_NAMES = ["A_dipole_realspace", "A_dipole_WLS", "monopole", "Cl1_master"]
ALL_NAMES = ESTIMATOR_NAMES + ["Cl1_pseudo"]

HERE = Path(__file__).resolve().parent
# on the pod this runs from /workspace/g3; locally from scripts/. Output goes
# next to the script unless the repo layout is present.
_repo_out = HERE.parent / "outputs" / "canonical_provenance"
OUT_DIR = _repo_out if _repo_out.is_dir() else HERE / "out"
OUT = OUT_DIR / "g3_joint_estimator_covariance_master_v2.json"
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
            "Run with HF_TOKEN set to download bamfai/galaxy-chirality-catalog."
        )
    return cands[-1]


def galactic_lat_mask(nside: int) -> np.ndarray:
    """Canonical mask: |b_gal| > 15 deg (float 1/0 per pixel). Identical to g3."""
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    rot = hp.Rotator(coord=["C", "G"])
    theta_g, _ = rot(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > GAL_LAT_CUT_DEG).astype(float)


def build_master_workspace(mask_fixed: np.ndarray):
    """Coupling matrix on the fixed canonical mask, single-ell bins, bin0=ell1.

    Follows scripts/master_decoupled_monopole_null.py; NmtBin.from_edges with
    edges starting at ell=1 gives single-ell bandpowers whose bin 0 is ell=1.
    API-compat across pymaster 2.x / 3.x.
    """
    b = nmt.NmtBin.from_edges(np.arange(1, LMAX + 1), np.arange(2, LMAX + 2))
    eff = b.get_effective_ells()
    assert abs(float(eff[0]) - 1.0) < 1e-9, f"bin0 ell != 1 (got {eff[0]})"
    zeros = np.zeros(mask_fixed.size)
    f_dummy = nmt.NmtField(mask_fixed, [zeros], lmax=LMAX)
    try:  # pymaster >= 3.0
        w = nmt.NmtWorkspace.from_fields(f_dummy, f_dummy, b)
    except AttributeError:  # pymaster 2.x
        w = nmt.NmtWorkspace()
        w.compute_coupling_matrix(f_dummy, f_dummy, b)
    return b, w


def build_static():
    """Load catalog, select primary HC, precompute per-galaxy pixel/superpixel/leg.
    Identical to committed g3, plus the fixed MASTER workspace."""
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

    order = np.argsort(superpix, kind="stable")
    sp_sorted = superpix[order]
    uniq_sp, starts = np.unique(sp_sorted, return_index=True)
    ends = np.append(starts[1:], len(sp_sorted))
    sp_to_idx = {int(sp): order[s:e] for sp, s, e in zip(uniq_sp, starts, ends)}
    log(f"HC sample spans {uniq_sp.size} superpixels (NSIDE={NSIDE_BLOCK})")

    npix = hp.nside2npix(NSIDE_DATA)
    mask = galactic_lat_mask(NSIDE_DATA)
    thp, php = hp.pix2ang(NSIDE_DATA, np.arange(npix))
    n_hat = np.column_stack(
        [np.sin(thp) * np.cos(php), np.sin(thp) * np.sin(php), np.cos(thp)]
    )

    # FIXED canonical effective mask for the MASTER workspace:
    # galactic cut AND full-sample n_total > 0 (binary).
    n_total_full = np.bincount(pix, minlength=npix).astype(np.float64)
    mask_fixed = ((mask > 0) & (n_total_full > 0)).astype(np.float64)
    f_sky = float(mask_fixed.mean())
    log(f"fixed MASTER mask: f_sky = {f_sky:.5f} "
        f"({int(mask_fixed.sum())}/{npix} px)")
    log("computing MASTER coupling matrix (single-ell bins, bin0=ell1) ...")
    bins, wsp = build_master_workspace(mask_fixed)
    log("coupling matrix done")

    return dict(
        pix=pix, superpix=superpix, is_cw=is_cw, leg=leg,
        uniq_sp=uniq_sp, sp_to_idx=sp_to_idx, npix=npix, mask=mask,
        mask_fixed=mask_fixed, f_sky=f_sky, bins=bins, wsp=wsp,
        n_hat=n_hat, n_gal=n_gal, catalog=cat,
    )


def estimators_from_indices(idx, S) -> np.ndarray:
    """5-vector: [A_dipole_rs, A_dipole_WLS, monopole, Cl1_master, Cl1_pseudo].
    Channels 1-3 and 5 are code-identical to the committed g3."""
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
        return np.full(5, np.nan)

    A_p = np.zeros(npix)
    A_p[ip] = 2.0 * (n_cw[ip] / n_total[ip]) - 1.0

    w_spiral = n_total[ip]
    f_cw_global = n_cw[ip].sum() / n_total[ip].sum()
    monopole = f_cw_global - 0.5

    A_bar = np.average(A_p[ip], weights=w_spiral)
    A_p_c = A_p.copy()
    A_p_c[ip] = A_p[ip] - A_bar

    nh = S["n_hat"][ip]
    # ---- 1. real-space dipole
    M1 = np.column_stack([np.ones(ip.size), nh[:, 0], nh[:, 1], nh[:, 2]])
    try:
        c1, *_ = np.linalg.lstsq(M1, A_p[ip], rcond=None)
        A_dipole_rs = float(np.linalg.norm(c1[1:4]))
    except np.linalg.LinAlgError:
        A_dipole_rs = np.nan

    # ---- 2. WLS nuisance-marginalized dipole
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

    # shared masked map for both harmonic legs
    masked = np.zeros(npix)
    masked[ip] = A_p_c[ip]

    # ---- 5. mask-coupled anafast pseudo-C_1 (committed g3 channel 4)
    cl = hp.anafast(masked, lmax=LMAX)
    Cl1_pseudo = float(cl[1])

    # ---- 4. MASTER-decoupled C_1 (fixed canonical workspace)
    try:
        f0 = nmt.NmtField(S["mask_fixed"], [masked], lmax=LMAX, lite=True)
        cl_coupled = nmt.compute_coupled_cell(f0, f0)
        cl_dec = S["wsp"].decouple_cell(cl_coupled)
        Cl1_master = float(cl_dec[0][0])  # bin 0 == ell 1
    except Exception:
        Cl1_master = np.nan

    return np.array([A_dipole_rs, A_dipole_wls, monopole, Cl1_master, Cl1_pseudo])


def write_partial(state: dict) -> None:
    OUT_PARTIAL.parent.mkdir(parents=True, exist_ok=True)
    OUT_PARTIAL.write_text(json.dumps(state, indent=2))


def main() -> None:
    rng = np.random.default_rng(SEED)
    S = build_static()

    all_idx = np.arange(S["n_gal"])
    full_vec = estimators_from_indices(all_idx, S)
    log("full-sample estimators: " + ", ".join(
        f"{n}={v:.6g}" for n, v in zip(ALL_NAMES, full_vec)))

    uniq_sp = S["uniq_sp"]
    n_sp = uniq_sp.size
    sp_to_idx = S["sp_to_idx"]

    boots = np.full((N_BOOTSTRAP, 5), np.nan)
    log(f"running {N_BOOTSTRAP} block-bootstrap resamples "
        f"({'SMOKE' if SMOKE else 'FULL'}; identical rng sequence to g3) ...")
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
                "estimator_names": ALL_NAMES,
                "full_sample": {n: (None if np.isnan(v) else float(v))
                                for n, v in zip(ALL_NAMES, full_vec)},
                "elapsed_s": round(time.time() - t0, 1),
            })

    valid = ~np.isnan(boots).any(axis=1)
    B = boots[valid]
    nv = int(valid.sum())
    log(f"valid resamples: {nv}/{N_BOOTSTRAP}")

    # primary 4x4 over [rs, WLS, monopole, Cl1_master]
    B4 = B[:, :4]
    cov4 = np.cov(B4.T, ddof=1)
    corr4 = np.corrcoef(B4.T)
    # full 5x5 including the pseudo proxy
    cov5 = np.cov(B.T, ddof=1)
    corr5 = np.corrcoef(B.T)
    sigma = B.std(axis=0, ddof=1)
    mean = B.mean(axis=0)
    z_self = [(float(full_vec[i]) / sigma[i]) if sigma[i] > 0 else None
              for i in range(5)]
    corr_master_pseudo = float(corr5[3, 4])

    result = {
        "script": "scripts/g3_joint_estimator_covariance_master_v2.py",
        "gate": "G3 MASTER-leg refinement — joint covariance w/ MASTER-decoupled l=1",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "catalog_snapshot": S["catalog"].split("snapshots/")[1][:40],
        "sample": f"primary HC (class_eq in CW/CCW & confidence_eq>{CONF_THRESH})",
        "n_galaxies": int(S["n_gal"]),
        "mask": f"|b_gal| > {GAL_LAT_CUT_DEG} deg & n_total>0 (per-resample, chs 1-3,5)",
        "master_mask": ("FIXED canonical effective mask: |b_gal|>15 deg AND "
                        "n_total_fullsample>0 (binary); workspace computed once"),
        "master_f_sky": S["f_sky"],
        "master_binning": "NmtBin.from_edges(arange(1,192), arange(2,193)); bin0=ell1",
        "pymaster_version": nmt.__version__,
        "nside_data": NSIDE_DATA,
        "nside_block": NSIDE_BLOCK,
        "lmax": LMAX,
        "n_bootstrap": N_BOOTSTRAP,
        "n_valid": nv,
        "seed": SEED,
        "rng_note": ("identical np.random.default_rng(42) call sequence as the "
                     "committed g3_joint_estimator_covariance.py -> identical "
                     "resample index sets"),
        "smoke": SMOKE,
        "estimator_names": ESTIMATOR_NAMES,
        "all_names": ALL_NAMES,
        "full_sample": {n: float(v) for n, v in zip(ALL_NAMES, full_vec)},
        "bootstrap_mean": {n: float(v) for n, v in zip(ALL_NAMES, mean)},
        "bootstrap_sigma": {n: float(v) for n, v in zip(ALL_NAMES, sigma)},
        "z_full_over_bootstrap_sigma": {n: z for n, z in zip(ALL_NAMES, z_self)},
        "joint_covariance_4x4": cov4.tolist(),
        "joint_correlation_4x4": corr4.tolist(),
        "joint_covariance_5x5_incl_pseudo": cov5.tolist(),
        "joint_correlation_5x5_incl_pseudo": corr5.tolist(),
        "corr_Cl1_master_vs_Cl1_pseudo": corr_master_pseudo,
        "note": ("4th channel is the MASTER-decoupled C_1 (M^-1 C_pseudo, fixed "
                 "canonical workspace). Cl1_pseudo retained as 5th tracked "
                 "quantity purely to validate the committed anafast proxy."),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    write_partial({"status": "done", "completed": N_BOOTSTRAP, "n_valid": nv,
                   "output": str(OUT), "elapsed_s": round(time.time() - t0, 1)})
    log(f"wrote {OUT}")
    print("\n=== JOINT 4x4 CORRELATION (MASTER-decoupled 4th channel) ===", flush=True)
    print("            " + "".join(f"{n[:10]:>12}" for n in ESTIMATOR_NAMES))
    for i, n in enumerate(ESTIMATOR_NAMES):
        print(f"{n[:10]:>10}  " + "".join(f"{corr4[i, j]:+12.3f}" for j in range(4)))
    print(f"\ncorr(Cl1_master, Cl1_pseudo) = {corr_master_pseudo:+.4f}")
    print("\n=== bootstrap sigma / z(full/sigma) ===")
    for i, n in enumerate(ALL_NAMES):
        zz = z_self[i]
        print(f"  {n:>20}: full={full_vec[i]:+.5g}  sigma={sigma[i]:.5g}  "
              f"z={'nan' if zz is None else f'{zz:+.2f}'}")


if __name__ == "__main__":
    main()
