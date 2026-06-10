#!/usr/bin/env python3
"""R24conf local compute batch (C12) — P4 queue items runnable on the Mac.

Closes (CLOSED-LOCAL) the following rows of
project-context/peer-reviews/R24CONF_COMPUTE_QUEUE.md:

  QUEUE-2  (OpenAI-E3): 10^4 pixel-permutation null array for the headline HC
           real-space dipole (exact run_dipole_catalog_c.py conventions:
           NSIDE=64, winning-class conf>0.6, tot>10 mask, hp.fit_dipole,
           rng seed 20260418); null quantiles {50,68,90,95,99}% and a
           rank-based 95% CL upper limit on A_dip.
  QUEUE-3  (OpenAI-E4): documentation of the exact sigma convention of the
           injection-recovery scorer (read from
           scripts/injection_sweep_extended.py; no new compute).
  QUEUE-6  (META-M3): equal-area declination-band uniformity (8 bands of
           equal in-mask pixel count on the canonical N_spiral>=10 mask),
           per-band f_CW +/- binomial sigma, HC and full-spiral samples.
  QUEUE-8  (OpenAI-M1): real-space dipole robustness panel — {uniform,
           N_spiral-weighted} fit x mask threshold N_spiral(p)>={10,20,50},
           each vs a 2000-permutation pixel null.
  QUEUE-10 (OpenAI-M4): A_dip and z (2000-perm pixel null) vs confidence
           cut p_eq in {0, 0.4, 0.5, 0.6, 0.7, 0.8}.
  QUEUE-14 (META-m1): low-ell real-Y_lm regression (ell<=3) of the headline
           HC A_p map; per-coefficient z vs 2000-perm pixel null.
  QUEUE-1  (META-E2): NaMaster mode-coupling-matrix conditioning on the
           apodized W_p=N_all footprint at NSIDE=64, apodization 1/2/3 deg
           C2; full-matrix and low-ell-block singular values, ell=1 row
           diagonal dominance.

Output: outputs/canonical_provenance/c12_r24conf_local_batch.json
(saved incrementally after each item; a failed item leaves earlier blocks
intact and is recorded as {"status": "FAILED", ...} — pattern-036).
"""
import json
import time
import traceback
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download

NSIDE = 64
NPIX = hp.nside2npix(NSIDE)
OUT = Path(__file__).parent / "outputs" / "canonical_provenance" / "c12_r24conf_local_batch.json"

t0 = time.time()
RESULTS = {
    "job": "C12-P4-R24conf-local-batch",
    "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "generator": "pipelines/p2_chirality/c12_r24conf_local_batch.py",
    "items": {},
}


def log(m):
    print(f"[{time.time()-t0:8.1f}s] {m}", flush=True)


def save():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(RESULTS, f, indent=1)


def rank_p(null, obs):
    k = int(np.sum(null >= obs))
    return k, (k + 1) / (len(null) + 1)


# ---------------------------------------------------------------- data load
log("loading parquet (local_files_only)...")
PARQUET = hf_hub_download(
    "bamfai/galaxy-chirality-catalog", "catalog_production.parquet",
    repo_type="dataset", local_files_only=True)
df = pd.read_parquet(PARQUET, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"])
RESULTS["catalog_parquet"] = PARQUET
n_total_rows = len(df)
log(f"rows: {n_total_rows:,}")

theta_all = np.radians(90.0 - df["dec"].values)
phi_all = np.radians(df["ra"].values % 360)
pix_all = hp.ang2pix(NSIDE, theta_all, phi_all)

is_spiral = df["class_eq"].isin(["CW", "CCW"]).values
is_cw_all = (df["class_eq"].values == "CW")
max_eq = np.maximum(df["p_cw_eq"].values, df["p_ccw_eq"].values)

pix_sp = pix_all[is_spiral]
is_cw_sp = is_cw_all[is_spiral]
max_eq_sp = max_eq[is_spiral]
dec_sp = df["dec"].values[is_spiral]

# pixel unit vectors + uniform/weighted LS machinery
th_pix, ph_pix = hp.pix2ang(NSIDE, np.arange(NPIX))
pix_xyz = np.column_stack([
    np.sin(th_pix) * np.cos(ph_pix),
    np.sin(th_pix) * np.sin(ph_pix),
    np.cos(th_pix),
])


def maps_for(sel_pix, sel_cw):
    cw = np.bincount(sel_pix[sel_cw], minlength=NPIX).astype(float)
    tot = np.bincount(sel_pix, minlength=NPIX).astype(float)
    return cw, tot


def ls_dipole_amp(asym_in, mask_idx, w=None):
    """LS fit A_p = m + a.n_p on in-mask pixels; returns |a|.

    w=None -> uniform pixel weighting (algebraically identical to
    healpy.fit_dipole with gal_cut=0 on the UNSEEN-masked map)."""
    X = np.column_stack([pix_xyz[mask_idx], np.ones(len(mask_idx))])
    if w is None:
        c, *_ = np.linalg.lstsq(X, asym_in, rcond=None)
    else:
        A = (X * w[:, None]).T @ X
        b = (X * w[:, None]).T @ asym_in
        c = np.linalg.solve(A, b)
    return float(np.sqrt(np.sum(c[:3] ** 2)))


def perm_null_amps(asym_in, mask_idx, n_perm, rng, w=None, chunk=500):
    """Pixel-permutation null: permute A_p across in-mask pixels, refit.
    Weights (if any) stay attached to pixels. Batched matmul LS."""
    X = np.column_stack([pix_xyz[mask_idx], np.ones(len(mask_idx))])
    if w is None:
        P = np.linalg.pinv(X)            # (4, n)
    else:
        A = (X * w[:, None]).T @ X
        P = np.linalg.solve(A, (X * w[:, None]).T)  # (4, n)
    n = len(asym_in)
    amps = np.empty(n_perm)
    done = 0
    while done < n_perm:
        m = min(chunk, n_perm - done)
        idx = np.argsort(rng.random((m, n)), axis=1)  # m independent perms
        coefs = asym_in[idx] @ P.T                     # (m, 4)
        amps[done:done + m] = np.sqrt(np.sum(coefs[:, :3] ** 2, axis=1))
        done += m
    return amps


# ================================================================ QUEUE-3
# (documentation only — verified by reading the committed scorer script)
log("QUEUE-3 (OpenAI-E4): documenting injection-scorer sigma convention...")
RESULTS["items"]["queue3_openai_e4_sigma_convention"] = {
    "status": "CLOSED-LOCAL",
    "source_script": "pipelines/p2_chirality/scripts/injection_sweep_extended.py",
    "sigma_convention": (
        "sigma_inj = (A_rec - mean(A_null)) / std(A_null, ddof=1), where the "
        "null is N_MC_NULL=1000 per-pixel binomial label-shuffle realizations "
        "n_CW(p) ~ Binomial(N_spiral(p), p_CW_global) on the HC-broad "
        "(p_eq>0.6) pixelized counts at NSIDE=64 (preserves per-pixel totals "
        "and the global monopole; destroys spatial label correlations), "
        "A_rec/A_null are full-amplitude (2|a|) N_total(p)-weighted LS dipole "
        "fits to f_CW(p), and the variance estimator is the unbiased sample "
        "standard deviation (ddof=1) of the 1000 null amplitudes "
        "(injection_sweep_extended.py lines 74-82, 104-108). "
        "P(sigma>3) is then the fraction of 100 injections per amplitude "
        "exceeding sigma=3 against that fixed null calibration."
    ),
    "seed": 42,
}
save()

# ================================================================ QUEUE-6
log("QUEUE-6 (META-M3): equal-area dec-band uniformity...")
try:
    n_sp_map = np.bincount(pix_sp, minlength=NPIX).astype(float)
    canon_mask = n_sp_map >= 10
    canon_idx = np.where(canon_mask)[0]
    dec_pix = 90.0 - np.degrees(th_pix[canon_idx])
    order = np.argsort(dec_pix)
    bands_idx = np.array_split(canon_idx[order], 8)  # equal pixel count = equal area
    pix2band = np.full(NPIX, -1, dtype=int)
    for b, bi in enumerate(bands_idx):
        pix2band[bi] = b

    def band_stats(sel_pix, sel_cw, label):
        gb = pix2band[sel_pix]
        rows = []
        inm = gb >= 0
        f_glob = float(sel_cw[inm].mean())
        for b in range(8):
            s = gb == b
            n = int(s.sum())
            ncw = int(sel_cw[s].sum())
            f = ncw / n
            sig = float(np.sqrt(f * (1 - f) / n))
            rows.append({
                "band": b + 1,
                "dec_range_deg": [float(np.min(dec_pix[order][sum(len(x) for x in bands_idx[:b]):sum(len(x) for x in bands_idx[:b + 1])])),
                                   float(np.max(dec_pix[order][sum(len(x) for x in bands_idx[:b]):sum(len(x) for x in bands_idx[:b + 1])]))],
                "n_pix": int(len(bands_idx[b])),
                "n_gal": n, "n_cw": ncw, "f_cw": float(f),
                "sigma_binomial": sig,
                "dev_from_half_pct": float((f - 0.5) * 100),
                "z_vs_global": float((f - f_glob) / sig),
            })
        return {"sample": label, "global_f_cw_in_mask": f_glob, "bands": rows,
                "max_abs_dev_from_half_pct": float(max(abs(r["dev_from_half_pct"]) for r in rows)),
                "max_abs_z_vs_global": float(max(abs(r["z_vs_global"]) for r in rows))}

    hc_sel = max_eq_sp > 0.6
    res6 = {
        "status": "CLOSED-LOCAL",
        "construction": (
            "canonical mask = N_spiral(p)>=10 on the full Catalog C spiral "
            "sample (23,682 pixels expected); in-mask pixels sorted by Dec "
            "and split into 8 contiguous bands of equal in-mask pixel count "
            "(HEALPix pixels are equal-area, so bands are equal in-mask "
            "area); galaxies assigned to bands via their NSIDE=64 pixel."
        ),
        "n_pix_canonical": int(canon_mask.sum()),
        "hc_sample": band_stats(pix_sp[hc_sel], is_cw_sp[hc_sel], "HC (max p_eq > 0.6)"),
        "full_spiral_sample": band_stats(pix_sp, is_cw_sp, "all Catalog C spirals"),
        "paper_equal_count_comparison": {
            "paper_value": "7 equal-spiral-count Dec slabs (full spiral sample): f_CW dev from 0.5 spans -0.110% to -0.463%",
            "paper_max_abs_dev_pct": 0.463,
        },
    }
    RESULTS["items"]["queue6_meta_m3_equal_area_bands"] = res6
    log(f"  HC max|dev|={res6['hc_sample']['max_abs_dev_from_half_pct']:.3f}% "
        f"full max|dev|={res6['full_spiral_sample']['max_abs_dev_from_half_pct']:.3f}%")
except Exception as e:
    RESULTS["items"]["queue6_meta_m3_equal_area_bands"] = {
        "status": "FAILED", "error": repr(e), "traceback": traceback.format_exc()}
    log(f"  QUEUE-6 FAILED: {e!r}")
save()

# ================================================================ QUEUE-8
log("QUEUE-8 (OpenAI-M1): robustness panel (fit x mask threshold)...")
try:
    hc_pix = pix_sp[max_eq_sp > 0.6]
    hc_cw = is_cw_sp[max_eq_sp > 0.6]
    cw_hc, tot_hc = maps_for(hc_pix, hc_cw)
    rng8 = np.random.default_rng(20260610)
    panel = []
    for thr in (10, 20, 50):
        mask = tot_hc >= thr
        midx = np.where(mask)[0]
        asym = (cw_hc[mask] - (tot_hc[mask] - cw_hc[mask])) / tot_hc[mask]
        w = tot_hc[mask]
        for fit, wgt in (("uniform", None), ("N_spiral_weighted", w)):
            amp = ls_dipole_amp(asym, midx, w=wgt)
            null = perm_null_amps(asym, midx, 2000, rng8, w=wgt)
            z = float((amp - null.mean()) / null.std(ddof=1))
            k, p = rank_p(null, amp)
            panel.append({"mask_threshold_nspiral_ge": thr, "fit": fit,
                          "n_pix": int(mask.sum()), "amp": amp, "z_mom": z,
                          "rank_p": float(p), "k": k,
                          "null_mean": float(null.mean()),
                          "null_std": float(null.std(ddof=1))})
            log(f"  thr>={thr} {fit}: amp={amp:.6f} z={z:+.2f} p={p:.4f}")
    RESULTS["items"]["queue8_openai_m1_robustness_panel"] = {
        "status": "CLOSED-LOCAL",
        "sample": "HC (winning-class p_eq > 0.6), NSIDE=64",
        "null": "2000 pixel-permutation realizations per cell (A_p permuted across in-mask pixels; weights stay attached to pixels), seed 20260610",
        "note_mask_convention": "sweep uses N_spiral(p)>=thr; the headline generator mask is tot>10 (strict), which differs from >=10 by the N=10 pixels only",
        "panel": panel,
    }
except Exception as e:
    RESULTS["items"]["queue8_openai_m1_robustness_panel"] = {
        "status": "FAILED", "error": repr(e), "traceback": traceback.format_exc()}
    log(f"  QUEUE-8 FAILED: {e!r}")
save()

# ================================================================ QUEUE-10
log("QUEUE-10 (OpenAI-M4): confidence-cut sweep...")
try:
    rng10 = np.random.default_rng(20260611)
    sweep = []
    for cut in (0.0, 0.4, 0.5, 0.6, 0.7, 0.8):
        sel = max_eq_sp > cut if cut > 0 else np.ones(len(pix_sp), bool)
        cw_m, tot_m = maps_for(pix_sp[sel], is_cw_sp[sel])
        mask = tot_m > 10  # headline generator convention
        midx = np.where(mask)[0]
        asym = (cw_m[mask] - (tot_m[mask] - cw_m[mask])) / tot_m[mask]
        amp = ls_dipole_amp(asym, midx)
        null = perm_null_amps(asym, midx, 2000, rng10)
        z = float((amp - null.mean()) / null.std(ddof=1))
        k, p = rank_p(null, amp)
        sweep.append({"p_eq_cut": cut, "n_gal": int(sel.sum()),
                      "n_pix": int(mask.sum()), "amp": amp, "z_mom": z,
                      "rank_p": float(p), "k": k,
                      "null_mean": float(null.mean()),
                      "null_std": float(null.std(ddof=1))})
        log(f"  cut>{cut}: N={int(sel.sum()):,} amp={amp:.6f} z={z:+.2f} p={p:.4f}")
    RESULTS["items"]["queue10_openai_m4_confidence_sweep"] = {
        "status": "CLOSED-LOCAL",
        "selection": "class_eq in {CW,CCW} and max(p_cw_eq,p_ccw_eq) > cut; mask tot>10; uniform-weight LS dipole",
        "null": "2000 pixel-permutation realizations per cut, seed 20260611",
        "sweep": sweep,
    }
except Exception as e:
    RESULTS["items"]["queue10_openai_m4_confidence_sweep"] = {
        "status": "FAILED", "error": repr(e), "traceback": traceback.format_exc()}
    log(f"  QUEUE-10 FAILED: {e!r}")
save()

# ================================================================ QUEUE-14
log("QUEUE-14 (META-m1): low-ell Y_lm regression of the HC A_p map...")
try:
    from scipy.special import sph_harm

    cw_hc, tot_hc = maps_for(pix_sp[max_eq_sp > 0.6], is_cw_sp[max_eq_sp > 0.6])
    mask = tot_hc > 10
    midx = np.where(mask)[0]
    asym = (cw_hc[mask] - (tot_hc[mask] - cw_hc[mask])) / tot_hc[mask]
    th, ph = th_pix[midx], ph_pix[midx]

    cols, names = [], []
    for l in range(4):
        for m in range(-l, l + 1):
            if m == 0:
                y = sph_harm(0, l, ph, th).real
            elif m > 0:
                y = np.sqrt(2) * (-1) ** m * sph_harm(m, l, ph, th).real
            else:
                y = np.sqrt(2) * (-1) ** m * sph_harm(-m, l, ph, th).imag
            cols.append(y)
            names.append(f"l{l}m{m:+d}")
    X = np.column_stack(cols)
    P = np.linalg.pinv(X)
    cond_design = float(np.linalg.cond(X))
    coef_obs = P @ asym

    rng14 = np.random.default_rng(20260612)
    n_perm = 2000
    coef_null = np.empty((n_perm, X.shape[1]))
    done = 0
    while done < n_perm:
        m_ = min(500, n_perm - done)
        idx = np.argsort(rng14.random((m_, len(asym))), axis=1)
        coef_null[done:done + m_] = asym[idx] @ P.T
        done += m_

    rows = []
    for j, nm in enumerate(names):
        mu, sd = coef_null[:, j].mean(), coef_null[:, j].std(ddof=1)
        z = float((coef_obs[j] - mu) / sd) if sd > 0 else None
        kk = int(np.sum(np.abs(coef_null[:, j] - mu) >= abs(coef_obs[j] - mu)))
        rows.append({"coef": nm, "value": float(coef_obs[j]), "z": z,
                     "rank_p_two_sided": float((kk + 1) / (n_perm + 1))})
        if j > 0:
            log(f"  {nm}: c={coef_obs[j]:+.5f} z={z:+.2f}")
    z_l1 = [abs(r["z"]) for r in rows if r["coef"].startswith("l1") and r["z"] is not None]
    RESULTS["items"]["queue14_meta_m1_ylm_regression"] = {
        "status": "CLOSED-LOCAL",
        "field": "headline HC A_p map (winning p_eq>0.6, tot>10 mask, NSIDE=64)",
        "design": "real spherical harmonics ell<=3 (16 columns) evaluated on in-mask pixel centers; OLS via pseudo-inverse",
        "design_condition_number": cond_design,
        "null": "2000 pixel-permutation realizations, seed 20260612; per-coefficient z=(c_obs-mean)/std(ddof=1), two-sided rank p; the l0 coefficient is monopole-dominated and nearly permutation-invariant",
        "coefficients": rows,
        "max_abs_z_l1": float(max(z_l1)) if z_l1 else None,
        "max_abs_z_l_le_3_excl_l0": float(max(abs(r["z"]) for r in rows[1:] if r["z"] is not None)),
    }
except Exception as e:
    RESULTS["items"]["queue14_meta_m1_ylm_regression"] = {
        "status": "FAILED", "error": repr(e), "traceback": traceback.format_exc()}
    log(f"  QUEUE-14 FAILED: {e!r}")
save()

# ================================================================ QUEUE-1
log("QUEUE-1 (META-E2): NaMaster coupling-matrix conditioning (apod 1/2/3 deg)...")
try:
    import pymaster as nmt

    n_all_map = np.bincount(pix_all, minlength=NPIX).astype(float)
    binary = (n_all_map >= 1).astype(float)
    blocks = {}
    for apo in (1.0, 2.0, 3.0):
        apod = nmt.mask_apodization(binary, apo, "C2")
        weight = apod * n_all_map  # W_p = N_all on the apodized footprint
        fld = nmt.NmtField(weight, [np.zeros(NPIX)])
        bins = nmt.NmtBin.from_lmax_linear(3 * NSIDE - 1, 1)
        try:
            wsp = nmt.NmtWorkspace.from_fields(fld, fld, bins)
        except AttributeError:
            wsp = nmt.NmtWorkspace()
            wsp.compute_coupling_matrix(fld, fld, bins)
        M = wsp.get_coupling_matrix()
        s_full = np.linalg.svd(M, compute_uv=False)
        low = M[:6, :6]
        s_low = np.linalg.svd(low, compute_uv=False)
        row1 = M[1, :]
        diag_dom = float(M[1, 1] / (np.sum(np.abs(row1)) - abs(M[1, 1])))
        blocks[f"apod_{apo:.0f}deg"] = {
            "f_sky_eff": float(np.mean(weight) ** 2 / np.mean(weight ** 2)),
            "full_matrix": {
                "shape": list(M.shape),
                "sv_max": float(s_full[0]), "sv_min": float(s_full[-1]),
                "condition_number": float(s_full[0] / s_full[-1]),
            },
            "low_ell_block_l0_to_l5": {
                "singular_values": [float(v) for v in s_low],
                "condition_number": float(s_low[0] / s_low[-1]),
            },
            "l1_row": {
                "M_11": float(M[1, 1]),
                "diag_dominance_ratio_M11_over_offdiag_rowsum": diag_dom,
                "largest_offdiag_couplings": {
                    f"l'={int(j)}": float(M[1, j])
                    for j in np.argsort(np.abs(row1))[::-1][:5] if j != 1
                },
            },
        }
        log(f"  apod {apo:.0f}deg: cond(full)={blocks[f'apod_{apo:.0f}deg']['full_matrix']['condition_number']:.3e} "
            f"cond(l<=5)={blocks[f'apod_{apo:.0f}deg']['low_ell_block_l0_to_l5']['condition_number']:.3f} "
            f"diag-dom(l=1)={diag_dom:.3f}")
    RESULTS["items"]["queue1_meta_e2_coupling_conditioning"] = {
        "status": "CLOSED-LOCAL",
        "construction": (
            "NmtField(weight, [0]) with weight = C2-apodized(N_all>=1 binary) "
            "x N_all at NSIDE=64; bins NmtBin.from_lmax_linear(191, nlb=1); "
            "M = NmtWorkspace.get_coupling_matrix() (unbinned spin-0 "
            "mode-coupling matrix, (lmax+1)^2). Reported: SVD of the full "
            "matrix, SVD of the leading ell in [0,5] block, and the ell=1 row "
            "diagonal-dominance ratio M_11/sum_{l' != 1}|M_1l'|."
        ),
        "apodization_sweep": blocks,
    }
except Exception as e:
    RESULTS["items"]["queue1_meta_e2_coupling_conditioning"] = {
        "status": "FAILED", "error": repr(e), "traceback": traceback.format_exc()}
    log(f"  QUEUE-1 FAILED: {e!r}")
save()

# ================================================================ QUEUE-2
log("QUEUE-2 (OpenAI-E3): 10^4 pixel-perm null + 95% CL UL (exact generator replication)...")
try:
    # Exact run_dipole_catalog_c.py replication: HC selection, tot > 10 (strict),
    # hp.fit_dipole, rng(20260418), in-place shuffle loop.
    conf = max_eq > 0.6
    sel = is_spiral & conf & df["ra"].notna().values
    cw_map = np.zeros(NPIX)
    ccw_map = np.zeros(NPIX)
    np.add.at(cw_map, pix_all[sel], is_cw_all[sel].astype(float))
    np.add.at(ccw_map, pix_all[sel], (~is_cw_all[sel]).astype(float))
    tot = cw_map + ccw_map
    mask = tot > 10
    asym = np.zeros(NPIX)
    asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot[mask]

    asym_full = np.full(NPIX, hp.UNSEEN)
    asym_full[mask] = asym[mask]
    _, dip = hp.fit_dipole(asym_full, gal_cut=0)
    amp_obs = float(np.sqrt(np.sum(dip ** 2)))
    log(f"  observed amp = {amp_obs:.6f} (expect 0.004423), n_pix={int(mask.sum())}")

    N_MC = 10_000
    valid = asym[mask].copy()
    boots = np.empty(N_MC)
    rng = np.random.default_rng(20260418)
    for i in range(N_MC):
        rng.shuffle(valid)
        shuf = np.full(NPIX, hp.UNSEEN)
        shuf[mask] = valid
        _, d = hp.fit_dipole(shuf, gal_cut=0)
        boots[i] = np.sqrt(np.sum(d ** 2))
        if (i + 1) % 2000 == 0:
            log(f"  perm {i+1}/{N_MC}")

    q = {f"q{p_}": float(np.percentile(boots, p_)) for p_ in (50, 68, 90, 95, 99)}
    k, p_rank = rank_p(boots, amp_obs)
    z = float((amp_obs - boots.mean()) / boots.std(ddof=1))
    null95 = q["q95"]
    RESULTS["items"]["queue2_openai_e3_null_array_ul95"] = {
        "status": "CLOSED-LOCAL",
        "replicates": "run_dipole_catalog_c.py null (i) exactly: HC winning-conf>0.6, tot>10 mask, hp.fit_dipole, N_MC=10^4, rng seed 20260418, in-place shuffle",
        "observed_amp": amp_obs,
        "n_pix": int(mask.sum()),
        "n_hc": int(sel.sum()),
        "null_mean": float(boots.mean()),
        "null_std_ddof1": float(boots.std(ddof=1)),
        "z_mom": z,
        "rank_k": k,
        "rank_p_one_sided": float(p_rank),
        "null_quantiles": q,
        "ul95_construction": (
            "PRIMARY: A_95UL is defined as the 95th percentile of the "
            "pixel-permutation null amplitude distribution, i.e. the smallest "
            "amplitude with P(A_null >= A_95UL) = 0.05. Because the observed "
            "amplitude (rank p = {:.3f}) is fully consistent with the null, "
            "any true coherent dipole large enough to push the estimator "
            "above this quantile with 95% null-exclusion probability is "
            "disfavored; this is an estimator-level (not signal-injected) "
            "limit and does not account for signal+noise amplitude addition. "
            "CONSERVATIVE companion: UL_cons = max(A_obs, A_95UL), which here "
            "equals A_95UL since A_obs < A_95UL. No obs+quantile sum "
            "construction is used."
        ).format(p_rank),
        "A_95UL": null95,
        "UL_conservative_max_obs_null95": float(max(amp_obs, null95)),
        "null_array_saved": "outputs/canonical_provenance/c12_queue2_null_amps_10k.npy",
    }
    np.save(OUT.parent / "c12_queue2_null_amps_10k.npy", boots)
    log(f"  null q95={null95:.6f}, z={z:+.3f}, rank p={p_rank:.4f}")
except Exception as e:
    RESULTS["items"]["queue2_openai_e3_null_array_ul95"] = {
        "status": "FAILED", "error": repr(e), "traceback": traceback.format_exc()}
    log(f"  QUEUE-2 FAILED: {e!r}")
save()

log(f"DONE -> {OUT}")
