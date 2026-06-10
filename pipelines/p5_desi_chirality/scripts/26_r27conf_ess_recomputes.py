#!/usr/bin/env python3
"""R27conf ESSENTIAL recompute items Q1 + Q2 (queue:
project-context/peer-reviews/R27conf_P5_TRUTH_AUDIT.md).

Q1 (META-E1) — per-Rs mask-dilation Phase-2 rerun.
    Reviewer concern: the Phase-2 sweep's footprint-mask dilation is
    Rs=25-tuned (2 cross iterations) and under-masks at Rs=50 (which needs
    ceil(50/25.91)+1 = 3). This script rebuilds the full V-Web chain
    (CIC -> mask -> smooth -> tidal classify -> spiral NN-join) at each
    sweep Rs in {10, 25, 50} (lambda_th = 0, N = 256^3, production grid
    geometry) TWICE where the iteration counts differ:
        "scaled"  : iterations = ceil(Rs/cell) + 1   (10->2, 25->2, 50->3)
        "fixed2"  : iterations = 2                   (the Rs=25-tuned value)
    At Rs in {10, 25} scaled == fixed2 (both 2), so one build serves both.
    Reports per-Rs volume fractions + per-class spiral f_CW for each build,
    the scaled-minus-fixed2 deltas at Rs=50, and a bit-level check of the
    scaled builds against the PUBLISHED Phase-2 sweep reports
    (env_finder/reports/02_phase2_volfrac_R*_N256_L0.json). Note the
    published Rs=50 report already carries n_mask_cells = 3,416,329 >
    3,150,086 (the 2-iteration mask), i.e. production 01_compute_vweb.py
    scales dilation per Rs by construction; this run verifies that
    empirically and quantifies the counterfactual fixed-2 build anyway.

Q2 (META-E2) — FoG-compressed DESIVAST hole-membership stability.
    Reviewer concern: the DESIVAST void-membership null lacks an explicit
    membership-flip stability test under line-of-sight Finger-of-God
    displacements. The audit row demands a "FoG-compressed rerun" but
    specifies no compression scale; we use the standard sigma_v/(aH) ~
    5 Mpc/h LOS scale quoted in the paper's RSD paragraph (disclosed
    choice). Since a deterministic per-galaxy FoG compression requires a
    group catalog (not available), we implement the LOS-displacement
    Monte Carlo bound: each matched spiral's comoving distance is
    perturbed chi -> chi + eps with eps ~ N(0, 5 Mpc/h) (200 realizations,
    fixed seed), plus coherent +/-5 Mpc/h worst-case shifts, and the
    VoidFinder any-hole membership test (scripts/24 item18 defA
    conventions) is recomputed exactly per realization. Reports n_void,
    f_CW(void), Delta f_CW(void - nonvoid), two-sample z, and flip counts
    vs the uncompressed baseline (exact-rerun n_void = 57,081; published
    k=20-guard headline 56,981).

Output: pipelines/p5_desi_chirality/outputs/26_r27conf_ess_recomputes.json
Run:    nice -n 5 python3 pipelines/p5_desi_chirality/scripts/26_r27conf_ess_recomputes.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import yaml

P5 = Path(__file__).resolve().parents[1]
REPO_ROOT = P5.parents[1]
sys.path.insert(0, str(P5 / "env_finder"))
from _compute_vweb_lib import (cic_deposit, classify_vweb, gaussian_smooth_fft,  # noqa: E402
                               step, tidal_eigenvalues, ENV_CLASSES)

CONFIG_PATH = P5 / "env_finder/config.yaml"
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
DESIVAST_DIR = P5 / "data/desivast"
SWEEP_CSV = P5 / "env_finder/reports/02_phase2_sweep.csv"
PUB_VOLFRAC_TPL = "env_finder/reports/02_phase2_volfrac_R{r}_N256_L0.json"
OUT = P5 / "outputs/26_r27conf_ess_recomputes.json"

SWEEP_RS = [10.0, 25.0, 50.0]
FIXED_ITERS = 2                       # the Rs=25-tuned production value
FOG_SIGMA_MPC_H = 5.0                 # sigma_v/(aH) LOS scale (see paper RSD para)
FOG_N_MC = 200
SEED = 20260611
H0, OM0, LITTLE_H = 67.66, 0.315, 0.6766
Z_DESIVAST_MAX = 0.24
T0 = time.time()


def _sig(n_cw, n):
    return float((n_cw - 0.5 * n) / (0.5 * np.sqrt(n))) if n else float("nan")


def _cls_row(n, n_cw):
    return {"n": int(n), "n_cw": int(n_cw),
            "cw_fraction": (n_cw / n) if n else None,
            "sigma_from_half": _sig(n_cw, n) if n else None}


def positions_planck18(z, ra_deg, dec_deg):
    from astropy.cosmology import Planck18
    chi = (Planck18.comoving_distance(z).value
           * (Planck18.H0.value / 100.0)).astype(np.float32)
    ra = np.deg2rad(ra_deg).astype(np.float32)
    dec = np.deg2rad(dec_deg).astype(np.float32)
    cd = np.cos(dec)
    pos = np.empty((len(z), 3), dtype=np.float32)
    pos[:, 0] = chi * cd * np.cos(ra)
    pos[:, 1] = chi * cd * np.sin(ra)
    pos[:, 2] = chi * np.sin(dec)
    return pos


def build_field(pos, origin, cell_size, N, R_s, n_dilate, tag):
    """Full V-Web chain (01_compute_vweb.py stages 5-10), explicit dilation."""
    from scipy.ndimage import binary_dilation
    count = cic_deposit(pos, origin, cell_size, N, T0)
    occupied = count > 0
    mask = binary_dilation(occupied, iterations=n_dilate)
    n_mask = int(mask.sum())
    rho_mean = float(count[mask].mean())
    delta = np.zeros_like(count, dtype=np.float32)
    delta[mask] = (count[mask] / rho_mean - 1.0).astype(np.float32)
    del count
    step(T0, f"[{tag}] dilate={n_dilate}; mask {n_mask:,}; rho_mean {rho_mean:.4f}")
    delta_s, KX, KY, KZ, k2 = gaussian_smooth_fft(delta, cell_size, R_s, T0)
    del delta
    l1, l2, l3 = tidal_eigenvalues(delta_s, KX, KY, KZ, k2, T0)
    del delta_s, KX, KY, KZ, k2
    cell_class = classify_vweb(l1, l2, l3, 0.0)
    del l1, l2, l3
    fracs = {ENV_CLASSES[i]: float(((cell_class == i) & mask).sum()) / n_mask
             for i in range(4)}
    step(T0, f"[{tag}] vol fracs: " + " ".join(f"{k}={v:.4f}" for k, v in fracs.items()))
    return cell_class, mask, n_mask, rho_mean, fracs


# ---------------------------------------------------------------------------
def q1_per_rs_dilation():
    cfg = yaml.safe_load(open(CONFIG_PATH))
    N = int(cfg["grid"]["n"])
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])

    step(T0, "Q1: loading filtered zall ...")
    p = REPO_ROOT / cfg["input"]["zall_path"]
    cols = ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z", "ZWARN", "SPECTYPE"]
    df = pq.read_table(str(p), columns=cols).to_pandas()
    f = cfg["input"]["filter"]
    sel = ((df["ZWARN"] == f["zwarn_max"])
           & (df["SPECTYPE"].astype(str).str.strip() == f["spectype"])
           & (df["Z"] > f["z_min"]) & (df["Z"] < f["z_max"]))
    df = df.loc[sel, ["TARGET_RA", "TARGET_DEC", "Z"]].reset_index(drop=True)
    n_rows = len(df)
    step(T0, f"Q1: filtered rows {n_rows:,}")

    pos = positions_planck18(df["Z"].values, df["TARGET_RA"].values,
                             df["TARGET_DEC"].values)
    del df
    mins = pos.min(axis=0) - pad
    maxs = pos.max(axis=0) + pad
    box_side = float(np.max(maxs - mins))
    origin = mins.astype(np.float32)
    cell_size = box_side / N
    step(T0, f"Q1: grid N={N}, cell={cell_size:.4f} Mpc/h")

    # matched-spiral set (scripts/23 conventions: primary-deduped CW/CCW,
    # deduped by desi_targetid keep='first')
    sp = pd.read_parquet(MATCHED, columns=["desi_targetid", "match_class_eq",
                                           "desi_z", "desi_ra", "desi_dec",
                                           "matched_primary_deduped"])
    sp = sp[sp["matched_primary_deduped"]
            & sp["match_class_eq"].isin(["CW", "CCW"])]
    sp = sp.drop_duplicates(subset="desi_targetid", keep="first").reset_index(drop=True)
    sp_pos = positions_planck18(sp["desi_z"].values, sp["desi_ra"].values,
                                sp["desi_dec"].values)
    sp_cw = (sp["match_class_eq"] == "CW").to_numpy()
    n_spirals = len(sp)
    step(T0, f"Q1: matched spirals (unique TARGETID) {n_spirals:,}")
    del sp

    def spiral_classes(cell_class):
        u = (sp_pos - origin) / cell_size
        idx = np.clip(np.floor(u + 0.5).astype(np.int64), 0, N - 1)
        return cell_class[idx[:, 0], idx[:, 1], idx[:, 2]]

    def per_class(scls):
        d = {}
        for i, cname in enumerate(ENV_CLASSES):
            m = scls == i
            d[cname] = _cls_row(int(m.sum()), int(sp_cw[m].sum()))
        return d

    builds = {}
    scls_store = {}
    for R_s in SWEEP_RS:
        scaled_iters = int(np.ceil(R_s / cell_size)) + 1
        variants = [("scaled", scaled_iters)]
        if scaled_iters != FIXED_ITERS:
            variants.append(("fixed2", FIXED_ITERS))
        for vtag, n_dil in variants:
            tag = f"R{int(R_s)}_{vtag}"
            cell_class, mask, n_mask, rho_mean, fracs = build_field(
                pos, origin, cell_size, N, R_s, n_dil, tag)
            scls = spiral_classes(cell_class)
            builds[tag] = {
                "R_s_mpc_h": R_s, "dilation_iterations": n_dil,
                "n_mask_cells": n_mask, "rho_mean_gal_per_cell": rho_mean,
                "volume_fractions_in_footprint": fracs,
                "spiral_f_cw_by_class": per_class(scls),
            }
            scls_store[tag] = scls
            del cell_class, mask
        if scaled_iters == FIXED_ITERS:
            builds[f"R{int(R_s)}_scaled"]["note"] = (
                f"scaled iterations == fixed-2 at Rs={R_s:g} "
                f"(ceil({R_s:g}/{cell_size:.2f})+1 = 2); single build serves "
                "both variants")

    # Rs=50 scaled-vs-fixed2 deltas
    a, b = builds["R50_fixed2"], builds["R50_scaled"]
    d_vf = {k: float(b["volume_fractions_in_footprint"][k]
                     - a["volume_fractions_in_footprint"][k]) for k in ENV_CLASSES}
    agree = float((scls_store["R50_scaled"] == scls_store["R50_fixed2"]).mean())
    d_fcw = {}
    for cname in ENV_CLASSES:
        fa = a["spiral_f_cw_by_class"][cname]
        fb = b["spiral_f_cw_by_class"][cname]
        d_fcw[cname] = {
            "delta_f_cw_pp": (None if (fa["cw_fraction"] is None
                                       or fb["cw_fraction"] is None)
                              else float((fb["cw_fraction"] - fa["cw_fraction"]) * 100)),
            "delta_n": int(fb["n"] - fa["n"]),
        }

    # bit-level check of the scaled builds against the published sweep reports
    published_check = {}
    for R_s in SWEEP_RS:
        pub = json.loads((P5 / PUB_VOLFRAC_TPL.format(r=int(R_s))).read_text())
        mine = builds[f"R{int(R_s)}_scaled"]
        published_check[f"R{int(R_s)}"] = {
            "published_n_mask_cells": pub["n_mask_cells"],
            "rebuilt_scaled_n_mask_cells": mine["n_mask_cells"],
            "n_mask_match": pub["n_mask_cells"] == mine["n_mask_cells"],
            "max_abs_volfrac_diff": float(max(
                abs(pub["volume_fractions_in_footprint"][k]
                    - mine["volume_fractions_in_footprint"][k])
                for k in ENV_CLASSES)),
        }

    # published per-class f_CW at lambda_th=0 (TARGETID-join convention) for ref
    sw = pd.read_csv(SWEEP_CSV)
    sw = sw[sw["lambda_th"] == 0.0]
    pub_fcw = {f"R{int(r)}": {
        row["env_class"]: {"n": int(row["n"]), "cw_fraction": float(row["cw_fraction"])}
        for _, row in sw[sw["R_s_mpc_h"] == r].iterrows()} for r in SWEEP_RS}

    return {
        "closes": "R27conf-Q1 / META-E1 (per-Rs mask-dilation Phase-2 rerun)",
        "method": {
            "grid_n": N, "cell_size_mpc_h": cell_size, "box_side_mpc_h": box_side,
            "lambda_th": 0.0, "n_deposited": n_rows, "n_spirals": n_spirals,
            "dilation_rule_scaled": "iterations = ceil(R_s/cell) + 1 (10->2, 25->2, 50->3)",
            "dilation_rule_fixed2": "iterations = 2 (the Rs=25-tuned value the reviewer "
                                    "presumed was applied at all Rs)",
            "spiral_join_note": ("env classes NN-interpolated at unique-TARGETID "
                                 "matched-spiral positions (scripts/23 conventions); "
                                 "published sweep f_CW values use the row-level "
                                 "TARGETID join and are quoted for reference"),
        },
        "builds": builds,
        "deltas_R50_scaled3_minus_fixed2": {
            "volume_fractions_pp": {k: v * 100 for k, v in d_vf.items()},
            "max_abs_volume_fraction_shift_pp": float(max(abs(v) for v in d_vf.values()) * 100),
            "spiral_class_assignment_agreement": agree,
            "f_cw_by_class": d_fcw,
            "max_abs_f_cw_shift_pp": float(max(abs(v["delta_f_cw_pp"]) for v in d_fcw.values()
                                               if v["delta_f_cw_pp"] is not None)),
        },
        "published_sweep_check": published_check,
        "published_sweep_f_cw_lambda0_reference": pub_fcw,
        "finding": ("Production 01_compute_vweb.py computes dilation as "
                    "ceil(R_s/cell)+1 from each sweep cell's own R_s, so the "
                    "published Rs=50 cells already used 3 iterations (see "
                    "published_sweep_check n_mask match); the reviewer's "
                    "fixed-2 premise is the counterfactual, quantified in "
                    "deltas_R50_scaled3_minus_fixed2."),
    }


# ---------------------------------------------------------------------------
def q2_fog_membership():
    from astropy.io import fits
    from astropy.cosmology import FlatLambdaCDM
    from scipy.spatial import cKDTree

    step(T0, "Q2: loading matched z<=0.24 sample + VoidFinder holes ...")
    sp = pd.read_parquet(MATCHED, columns=["desi_targetid", "match_class_eq",
                                           "desi_z", "desi_ra", "desi_dec",
                                           "matched_primary_deduped"])
    sp = sp[sp["matched_primary_deduped"]
            & sp["match_class_eq"].isin(["CW", "CCW"])]
    lz = sp[sp["desi_z"] <= Z_DESIVAST_MAX].reset_index(drop=True)
    del sp
    cosmo = FlatLambdaCDM(H0=H0, Om0=OM0)
    chi = cosmo.comoving_distance(lz["desi_z"].to_numpy()).value * LITTLE_H
    ra = np.radians(lz["desi_ra"].to_numpy())
    dec = np.radians(lz["desi_dec"].to_numpy())
    unit = np.column_stack([np.cos(dec) * np.cos(ra),
                            np.cos(dec) * np.sin(ra),
                            np.sin(dec)])
    y = (lz["match_class_eq"] == "CW").to_numpy()
    n_gal = len(lz)
    holes = []
    for gc in ["NGC", "SGC"]:
        with fits.open(DESIVAST_DIR / f"DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits") as h:
            d = h["HOLES"].data
            holes.append(np.column_stack([d["X"], d["Y"], d["Z"], d["RADIUS"]]))
    holes = np.vstack(holes)
    step(T0, f"Q2: n_gal {n_gal:,}, n_holes {len(holes):,}")

    def membership(chi_v):
        gal = unit * chi_v[:, None]
        kd = cKDTree(gal)
        mem = np.zeros(n_gal, dtype=bool)
        for idx in kd.query_ball_point(holes[:, :3], r=holes[:, 3]):
            mem[idx] = True
        return mem

    def two_sample_z(nA, kA, nB, kB):
        fA, fB = kA / nA, kB / nB
        pp = (kA + kB) / (nA + nB)
        se = np.sqrt(pp * (1 - pp) * (1 / nA + 1 / nB))
        return float((fA - fB) / se)

    def summarize(mem):
        nv, kv = int(mem.sum()), int(y[mem].sum())
        nn, kn = int((~mem).sum()), int(y[~mem].sum())
        return {"void": _cls_row(nv, kv), "nonvoid": _cls_row(nn, kn),
                "delta_fcw_pp": float((kv / nv - kn / nn) * 100) if nv and nn else None,
                "two_sample_z_void_minus_nonvoid":
                    two_sample_z(nv, kv, nn, kn) if nv and nn else None}

    mem0 = membership(chi)
    base = summarize(mem0)
    step(T0, f"Q2: baseline n_void {int(mem0.sum()):,} (exact-rerun ref 57,081)")

    rng = np.random.default_rng(SEED)
    mc_rows = []
    for k in range(FOG_N_MC):
        eps = rng.normal(0.0, FOG_SIGMA_MPC_H, size=n_gal)
        mem = membership(chi + eps)
        s = summarize(mem)
        mc_rows.append({
            "n_void": s["void"]["n"],
            "f_cw_void": s["void"]["cw_fraction"],
            "delta_fcw_pp": s["delta_fcw_pp"],
            "z2": s["two_sample_z_void_minus_nonvoid"],
            "n_flip_out": int((mem0 & ~mem).sum()),
            "n_flip_in": int((~mem0 & mem).sum()),
        })
        if (k + 1) % 50 == 0:
            step(T0, f"Q2: MC {k+1}/{FOG_N_MC}")
    mc = pd.DataFrame(mc_rows)

    def stats(col):
        v = mc[col].to_numpy(dtype=float)
        return {"mean": float(v.mean()), "std": float(v.std(ddof=1)),
                "min": float(v.min()), "max": float(v.max())}

    coherent = {}
    for lbl, shift in [("plus_5", +FOG_SIGMA_MPC_H), ("minus_5", -FOG_SIGMA_MPC_H)]:
        mem = membership(chi + shift)
        s = summarize(mem)
        s["n_flip_out"] = int((mem0 & ~mem).sum())
        s["n_flip_in"] = int((~mem0 & mem).sum())
        coherent[lbl] = s

    return {
        "closes": "R27conf-Q2 / META-E2 (FoG-compressed DESIVAST membership rerun)",
        "method": {
            "sample": f"z<={Z_DESIVAST_MAX} matched primary deduped CW/CCW spirals "
                      f"(n={n_gal:,}); VoidFinder NGC+SGC any-hole membership "
                      "(scripts/24 item18 defA conventions, Mpc/h)",
            "fog_model": (f"LOS comoving-distance perturbation chi -> chi + eps, "
                          f"eps ~ N(0, {FOG_SIGMA_MPC_H:g} Mpc/h), {FOG_N_MC} "
                          f"realizations, seed {SEED}; plus coherent "
                          f"+/-{FOG_SIGMA_MPC_H:g} Mpc/h worst-case shifts. "
                          "DISCLOSED CHOICE: the audit row specifies no "
                          "compression scale, so we use the sigma_v/(aH) ~ "
                          "5 Mpc/h FoG displacement scale already quoted in the "
                          "paper's RSD paragraph; a deterministic per-galaxy "
                          "FoG compression would require a group catalog, which "
                          "is not part of the P5 data set, so the MC "
                          "displacement bound (which brackets compression of "
                          "either sign) is used instead."),
            "published_headline_n_void": 56981,
            "published_headline_note": "k=20-guard catalog-anchored value; the "
                                       "exact-rerun baseline is 57,081 "
                                       "(outputs/24 item18 defA)",
        },
        "uncompressed_baseline": base,
        "fog_mc": {
            "n_void": stats("n_void"),
            "f_cw_void": stats("f_cw_void"),
            "delta_fcw_pp": stats("delta_fcw_pp"),
            "two_sample_z": stats("z2"),
            "n_flip_out": stats("n_flip_out"),
            "n_flip_in": stats("n_flip_in"),
        },
        "coherent_shifts": coherent,
    }


def main():
    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/26_r27conf_ess_recomputes.py",
        "closes": "R27conf-Q1 (META-E1) + R27conf-Q2 (META-E2)",
    }
    out["q2_fog_membership"] = q2_fog_membership()
    OUT.write_text(json.dumps(out, indent=2))
    step(T0, "Q2 written")
    out["q1_per_rs_dilation"] = q1_per_rs_dilation()
    OUT.write_text(json.dumps(out, indent=2))
    step(T0, f"wrote {OUT}")


if __name__ == "__main__":
    main()
