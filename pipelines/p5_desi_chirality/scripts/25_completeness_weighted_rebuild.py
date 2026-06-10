#!/usr/bin/env python3
"""R24conf QUEUE-16 (P5 META-M1) + R26conf META-M1/META-M4 residue —
completeness-weighted density rebuild with the DESI DR1 BGS_BRIGHT randoms
as the mean-density tracer, plus the cube-connected/3-iteration
mask-dilation rerun.

Data: pipelines/p5_desi_chirality/data/randoms/
      BGS_BRIGHT_{NGC,SGC}_{0..3}_clustering.ran.fits  (8 files, ~74.7M rows,
      RA/DEC/Z/WEIGHT; v1.5 LSS clustering randoms, z in [0.01, 0.50]).

Geometry-matching disclosure (pattern-036): the published field deposits the
filtered zall parent (ZWARN==0, SPECTYPE==GALAXY, 0.01<z<2.0). The clustering
randoms trace the BGS_BRIGHT *target* selection over 0.01<z<0.50 — the
GALAXY-spectype cut has no randoms analog, and dark-program (LRG/ELG) galaxies
in the parent have no BGS randoms. The weighted rebuild is therefore run on
the z-window 0.01<z<0.50 (which contains 99.3% of the matched CW/CCW spirals)
against an identically-windowed unweighted control build, so the reported
delta isolates the completeness weighting, not the z-cut.

Builds (identical grid geometry, set from the full row-level parent as in
scripts/23_unique_parent_rebuild.py; production cell 25.9127 Mpc/h):

  D "row_level"               : full parent, production replication
                                (cross-structure dilation, 2 iter)
  C "dilation_cube3"          : full parent, SAME count grid, mask =
                                binary_dilation(occupied, np.ones((3,3,3)),
                                iterations=3)  [R26conf META-M1]
  A "unweighted_window"       : parent restricted to 0.01<z<0.50,
                                production-style build (control)
  B "randoms_weighted_window" : same windowed galaxies; delta_w =
                                (n_g/N_g)/(n_rw/N_rw) - 1 on cells with raw
                                random CIC count >= NR_MIN (low-random cells
                                excluded); randoms deposited with their
                                catalog WEIGHT column; delta=0 outside
                                support; the n_r_w-WEIGHTED mean of delta_w
                                over the support is 0 by construction (alpha
                                normalization), addressing the zero-padding
                                integral-constraint family, R26conf META-M4
                                (the unweighted per-cell mean is positive —
                                radial zall-vs-BGS profile mismatch — and is
                                reported; k=0 is zeroed in the Poisson
                                inversion so it does not enter classification)

Reports Delta(class volume fractions), cell-class agreement, per-class
Delta f_CW on the identical matched-spiral set for B-vs-A and C-vs-D.

Output: pipelines/p5_desi_chirality/outputs/25_completeness_weighted_rebuild.json
Run:    nice -n 5 python3 pipelines/p5_desi_chirality/scripts/25_completeness_weighted_rebuild.py
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
from _compute_vweb_lib import (classify_vweb, gaussian_smooth_fft,  # noqa: E402
                               step, tidal_eigenvalues, ENV_CLASSES)

CONFIG_PATH = P5 / "env_finder/config.yaml"
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
RANDOMS_DIR = P5 / "data/randoms"
RANDOM_FILES = [RANDOMS_DIR / f"BGS_BRIGHT_{cap}_{i}_clustering.ran.fits"
                for cap in ("NGC", "SGC") for i in range(4)]
OUT = P5 / "outputs/25_completeness_weighted_rebuild.json"

Z_WIN = (0.01, 0.50)   # randoms support window (full files span [0.0100, 0.5000])
NR_MIN = 5.0           # min raw-random CIC count per supported cell


def _sig(n_cw, n):
    return float((n_cw - 0.5 * n) / (0.5 * np.sqrt(n))) if n else float("nan")


def positions(z, ra_deg, dec_deg):
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


def cic_weighted(pos, weights, origin, cell_size, N, grids, t0, tag):
    """CIC deposit into one or more accumulator grids (one per weight array;
    weights entry None = unit weights). Same kernel as _compute_vweb_lib."""
    u = (pos - origin) / cell_size
    in_bounds = np.all((u >= 0.0) & (u < N - 1), axis=1)
    n_out = len(pos) - int(in_bounds.sum())
    if n_out > 0:
        step(t0, f"  [{tag}] WARNING: {n_out:,} of {len(pos):,} outside grid (dropped)")
    u = u[in_bounds]
    weights = [None if w is None else w[in_bounds].astype(np.float32) for w in weights]
    i0 = np.floor(u).astype(np.int64)
    f = (u - i0).astype(np.float32)
    i1 = i0 + 1
    for dx in (0, 1):
        for dy in (0, 1):
            for dz in (0, 1):
                wx = (1 - f[:, 0]) if dx == 0 else f[:, 0]
                wy = (1 - f[:, 1]) if dy == 0 else f[:, 1]
                wz = (1 - f[:, 2]) if dz == 0 else f[:, 2]
                w = (wx * wy * wz).astype(np.float32)
                ix = i0[:, 0] if dx == 0 else i1[:, 0]
                iy = i0[:, 1] if dy == 0 else i1[:, 1]
                iz = i0[:, 2] if dz == 0 else i1[:, 2]
                for grid, wt in zip(grids, weights):
                    np.add.at(grid, (ix, iy, iz),
                              w if wt is None else (w * wt).astype(np.float32))
    return int(in_bounds.sum())


def classify_field(delta, cell_size, R_s, t0, tag):
    delta_s, KX, KY, KZ, k2 = gaussian_smooth_fft(delta, cell_size, R_s, t0)
    l1, l2, l3 = tidal_eigenvalues(delta_s, KX, KY, KZ, k2, t0)
    del delta_s, KX, KY, KZ, k2
    cell_class = classify_vweb(l1, l2, l3, 0.0)
    del l1, l2, l3
    step(t0, f"[{tag}] classified")
    return cell_class


def tabulate(cell_class, mask, sp_cls, sp_cw, tag, t0, extra=None):
    n_mask = int(mask.sum())
    fracs = {ENV_CLASSES[i]: float(((cell_class == i) & mask).sum()) / n_mask
             for i in range(4)}
    per_class = {}
    for i, cname in enumerate(ENV_CLASSES):
        m = sp_cls == i
        nn = int(m.sum())
        ncw = int(sp_cw[m].sum())
        per_class[cname] = {"n": nn, "n_cw": ncw,
                            "cw_fraction": (ncw / nn) if nn else None,
                            "sigma_from_half": _sig(ncw, nn)}
    step(t0, f"[{tag}] vol fracs: " + " ".join(f"{k}={v:.4f}" for k, v in fracs.items()))
    out = {"n_mask_cells": n_mask, "volume_fractions_in_footprint": fracs,
           "spiral_f_cw_by_class": per_class}
    if extra:
        out.update(extra)
    return out


def compare(res_a, res_b, cls_a, cls_b, mask_a, mask_b, scls_a, scls_b):
    vf_a = res_a["volume_fractions_in_footprint"]
    vf_b = res_b["volume_fractions_in_footprint"]
    d_vf = {k: float((vf_b[k] - vf_a[k]) * 100) for k in ENV_CLASSES}
    both = mask_a & mask_b
    agree = float((cls_a[both] == cls_b[both]).mean())
    sp_agree = float((scls_a == scls_b).mean())
    d_fcw = {}
    for cname in ENV_CLASSES:
        a = res_a["spiral_f_cw_by_class"][cname]
        b = res_b["spiral_f_cw_by_class"][cname]
        d_fcw[cname] = {
            "delta_f_cw_pp": (None if (a["cw_fraction"] is None or b["cw_fraction"] is None)
                              else float((b["cw_fraction"] - a["cw_fraction"]) * 100)),
            "delta_n": int(b["n"] - a["n"]),
        }
    return {
        "volume_fractions_pp": d_vf,
        "max_abs_volume_fraction_shift_pp": float(max(abs(v) for v in d_vf.values())),
        "n_common_mask_cells": int(both.sum()),
        "cell_class_agreement_on_common_mask": agree,
        "spiral_class_assignment_agreement": sp_agree,
        "f_cw_by_class": d_fcw,
        "max_abs_f_cw_shift_pp": float(max(abs(v["delta_f_cw_pp"]) for v in d_fcw.values()
                                           if v["delta_f_cw_pp"] is not None)),
    }


def main():
    from scipy.ndimage import binary_dilation
    t0 = time.time()
    cfg = yaml.safe_load(open(CONFIG_PATH))
    N = int(cfg["grid"]["n"])
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])
    R_s = float(cfg["smoothing"]["R_s_mpc_h"])

    # ---- galaxies (identical filter to production / 23-series) -------------
    step(t0, "Loading filtered zall ...")
    p = REPO_ROOT / cfg["input"]["zall_path"]
    cols = ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z", "ZWARN", "SPECTYPE"]
    df = pq.read_table(str(p), columns=cols).to_pandas()
    f = cfg["input"]["filter"]
    sel = ((df["ZWARN"] == f["zwarn_max"])
           & (df["SPECTYPE"].astype(str).str.strip() == f["spectype"])
           & (df["Z"] > f["z_min"]) & (df["Z"] < f["z_max"]))
    df = df.loc[sel, ["TARGET_RA", "TARGET_DEC", "Z"]].reset_index(drop=True)
    n_rows = len(df)
    step(t0, f"filtered rows: {n_rows:,}")

    pos_all = positions(df["Z"].values, df["TARGET_RA"].values, df["TARGET_DEC"].values)
    mins = pos_all.min(axis=0) - pad
    maxs = pos_all.max(axis=0) + pad
    box_side = float(np.max(maxs - mins))
    origin = mins.astype(np.float32)
    cell_size = box_side / N
    step(t0, f"grid: N={N}, cell={cell_size:.4f} Mpc/h (production: 25.9127)")

    in_win = ((df["Z"].values > Z_WIN[0]) & (df["Z"].values < Z_WIN[1]))
    n_win = int(in_win.sum())
    step(t0, f"galaxies in z-window {Z_WIN}: {n_win:,} ({100*n_win/n_rows:.1f}%)")
    del df

    # ---- spirals (identical to 23-series; full + windowed sets) ------------
    sp = pd.read_parquet(MATCHED, columns=["desi_targetid", "match_class_eq",
                                           "desi_z", "desi_ra", "desi_dec",
                                           "matched_primary_deduped"])
    sp = sp[sp["matched_primary_deduped"]
            & sp["match_class_eq"].isin(["CW", "CCW"])]
    sp = sp.drop_duplicates(subset="desi_targetid", keep="first").reset_index(drop=True)
    sp_pos_full = positions(sp["desi_z"].values, sp["desi_ra"].values, sp["desi_dec"].values)
    sp_cw_full = (sp["match_class_eq"] == "CW").to_numpy()
    sp_win = ((sp["desi_z"].values > Z_WIN[0]) & (sp["desi_z"].values < Z_WIN[1]))
    sp_pos_win = sp_pos_full[sp_win]
    sp_cw_win = sp_cw_full[sp_win]
    step(t0, f"matched spirals: {len(sp):,} total, {int(sp_win.sum()):,} "
             f"({100*sp_win.mean():.1f}%) in z-window")

    def spiral_classes(cell_class, sp_pos):
        u = (sp_pos - origin) / cell_size
        idx = np.clip(np.floor(u + 0.5).astype(np.int64), 0, N - 1)
        return cell_class[idx[:, 0], idx[:, 1], idx[:, 2]]

    def spiral_cells(sp_pos):
        u = (sp_pos - origin) / cell_size
        return np.clip(np.floor(u + 0.5).astype(np.int64), 0, N - 1)

    # ---- galaxy count grids (full + windowed) -------------------------------
    step(t0, "CIC: full parent + windowed parent ...")
    ng_full = np.zeros((N, N, N), dtype=np.float32)
    cic_weighted(pos_all, [None], origin, cell_size, N, [ng_full], t0, "gal_full")
    ng_win = np.zeros((N, N, N), dtype=np.float32)
    cic_weighted(pos_all[in_win], [None], origin, cell_size, N, [ng_win], t0, "gal_win")
    del pos_all

    # ---- randoms: raw + WEIGHT-weighted CIC, per-file streaming ------------
    from astropy.io import fits
    nr_raw = np.zeros((N, N, N), dtype=np.float32)
    nr_w = np.zeros((N, N, N), dtype=np.float32)
    n_rand_total = 0
    w_sum = 0.0
    for fn in RANDOM_FILES:
        with fits.open(fn, memmap=True) as hd:
            d = hd[1].data
            z = np.asarray(d["Z"], dtype=np.float64)
            keep = (z > Z_WIN[0]) & (z < Z_WIN[1])
            rpos = positions(z[keep], np.asarray(d["RA"])[keep],
                             np.asarray(d["DEC"])[keep])
            rw = np.asarray(d["WEIGHT"], dtype=np.float32)[keep]
        n_in = cic_weighted(rpos, [None, rw], origin, cell_size, N,
                            [nr_raw, nr_w], t0, fn.name)
        n_rand_total += n_in
        w_sum += float(rw.sum())
        step(t0, f"  randoms {fn.name}: {n_in:,} deposited (running {n_rand_total:,})")
        del rpos, rw, z, keep
    step(t0, f"randoms total: {n_rand_total:,}; sum(WEIGHT) = {w_sum:,.0f}")

    builds, classes, masks = {}, {}, {}
    sp_cls = {}

    # ---- build D: production replication (full parent) ---------------------
    occupied = ng_full > 0
    dilate_n = int(np.ceil(R_s / cell_size)) + 1
    mask_d = binary_dilation(occupied, iterations=dilate_n)
    rho_mean_d = float(ng_full[mask_d].mean())
    delta = np.zeros_like(ng_full)
    delta[mask_d] = ng_full[mask_d] / rho_mean_d - 1.0
    cls_d = classify_field(delta, cell_size, R_s, t0, "D_row_level")
    del delta
    sp_cls["D"] = spiral_classes(cls_d, sp_pos_full)
    builds["D_row_level"] = tabulate(
        cls_d, mask_d, sp_cls["D"], sp_cw_full, "D_row_level", t0,
        extra={"n_deposited": n_rows, "rho_mean_gal_per_cell": rho_mean_d,
               "dilation": f"cross-structure, {dilate_n} iterations (production)"})
    classes["D"], masks["D"] = cls_d, mask_d

    # ---- build C: cube-connected 3-iteration dilation (R26conf META-M1) ----
    mask_c = binary_dilation(occupied, structure=np.ones((3, 3, 3), dtype=bool),
                             iterations=3)
    rho_mean_c = float(ng_full[mask_c].mean())
    delta = np.zeros_like(ng_full)
    delta[mask_c] = ng_full[mask_c] / rho_mean_c - 1.0
    cls_c = classify_field(delta, cell_size, R_s, t0, "C_dilation_cube3")
    del delta, occupied
    sp_cls["C"] = spiral_classes(cls_c, sp_pos_full)
    builds["C_dilation_cube3"] = tabulate(
        cls_c, mask_c, sp_cls["C"], sp_cw_full, "C_dilation_cube3", t0,
        extra={"n_deposited": n_rows, "rho_mean_gal_per_cell": rho_mean_c,
               "dilation": "cube-connected np.ones((3,3,3)), 3 iterations"})
    classes["C"], masks["C"] = cls_c, mask_c
    del ng_full

    # ---- build A: unweighted windowed control -------------------------------
    occ_w = ng_win > 0
    mask_a = binary_dilation(occ_w, iterations=dilate_n)
    rho_mean_a = float(ng_win[mask_a].mean())
    delta = np.zeros_like(ng_win)
    delta[mask_a] = ng_win[mask_a] / rho_mean_a - 1.0
    cls_a = classify_field(delta, cell_size, R_s, t0, "A_unweighted_window")
    del delta, occ_w
    sp_cls["A"] = spiral_classes(cls_a, sp_pos_win)
    builds["A_unweighted_window"] = tabulate(
        cls_a, mask_a, sp_cls["A"], sp_cw_win, "A_unweighted_window", t0,
        extra={"n_deposited": n_win, "rho_mean_gal_per_cell": rho_mean_a,
               "z_window": list(Z_WIN)})
    classes["A"], masks["A"] = cls_a, mask_a

    # ---- build B: randoms-weighted windowed ---------------------------------
    support = nr_raw >= NR_MIN
    n_support = int(support.sum())
    alpha = float(ng_win[support].sum() / nr_w[support].sum())
    delta = np.zeros_like(ng_win)
    delta[support] = ng_win[support] / (alpha * nr_w[support]) - 1.0
    mean_delta_support = float(delta[support].mean())
    # diagnostics: galaxies / spirals on unsupported cells
    gal_unsupported = float(ng_win[~support].sum() / ng_win.sum())
    sp_idx = spiral_cells(sp_pos_win)
    sp_unsupported = float((~support[sp_idx[:, 0], sp_idx[:, 1], sp_idx[:, 2]]).mean())
    step(t0, f"[B] support cells (n_r_raw >= {NR_MIN}): {n_support:,}; alpha = {alpha:.5f}; "
             f"<delta>_support = {mean_delta_support:.2e}; "
             f"gal mass on unsupported cells {100*gal_unsupported:.3f}%; "
             f"spirals on unsupported cells {100*sp_unsupported:.3f}%")
    cls_b = classify_field(delta, cell_size, R_s, t0, "B_randoms_weighted_window")
    del delta
    sp_cls["B"] = spiral_classes(cls_b, sp_pos_win)
    builds["B_randoms_weighted_window"] = tabulate(
        cls_b, support, sp_cls["B"], sp_cw_win, "B_randoms_weighted_window", t0,
        extra={"n_deposited": n_win, "n_randoms_deposited": n_rand_total,
               "z_window": list(Z_WIN), "nr_min_raw_cic": NR_MIN,
               "alpha_Ng_over_Nrw": alpha,
               "mean_raw_randoms_per_support_cell": float(nr_raw[support].mean()),
               "mean_delta_on_support": mean_delta_support,
               "frac_gal_mass_on_unsupported_cells": gal_unsupported,
               "frac_spirals_on_unsupported_cells": sp_unsupported})
    classes["B"], masks["B"] = cls_b, support
    del ng_win, nr_raw, nr_w

    # ---- deltas -------------------------------------------------------------
    d_BA = compare(builds["A_unweighted_window"], builds["B_randoms_weighted_window"],
                   classes["A"], classes["B"], masks["A"], masks["B"],
                   sp_cls["A"], sp_cls["B"])
    d_CD = compare(builds["D_row_level"], builds["C_dilation_cube3"],
                   classes["D"], classes["C"], masks["D"], masks["C"],
                   sp_cls["D"], sp_cls["C"])
    d_AD_vf = {k: float((builds["A_unweighted_window"]["volume_fractions_in_footprint"][k]
                         - builds["D_row_level"]["volume_fractions_in_footprint"][k]) * 100)
               for k in ENV_CLASSES}

    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/25_completeness_weighted_rebuild.py",
        "closes": ("QUEUE-16 / R24conf META-M1 (randoms-weighted rebuild) + "
                   "R26conf META-M1 (cube-connected/3-iter dilation) + "
                   "R26conf META-M4 (integral constraint via randoms-based alpha)"),
        "randoms": {
            "files": [f.name for f in RANDOM_FILES],
            "source": ("DESI DR1 LSS iron v1.5 BGS_BRIGHT clustering randoms "
                       "(RA/DEC/Z/WEIGHT)"),
            "n_deposited": n_rand_total,
            "z_range_used": list(Z_WIN),
            "weighting": "catalog WEIGHT column (raw counts used for the support cut)",
        },
        "geometry_matching_disclosure": (
            "Pattern-036: the published parent applies ZWARN==0 + SPECTYPE==GALAXY + "
            "0.01<z<2.0 to the zall table; the BGS_BRIGHT clustering randoms trace the "
            "BGS_BRIGHT target selection over 0.01<z<0.50 only — the GALAXY-spectype cut "
            "has no randoms analog and dark-program (LRG/ELG) parent galaxies have no BGS "
            "randoms. The weighted build is therefore restricted to the 0.01<z<0.50 window "
            "(99.3% of matched CW/CCW spirals) and compared against an identically-windowed "
            "unweighted control build on the same grid, so the delta isolates the "
            "completeness weighting."),
        "method": {
            "grid_n": N, "cell_size_mpc_h": cell_size, "box_side_mpc_h": box_side,
            "R_s_mpc_h": R_s, "lambda_th": 0.0,
            "delta_w_definition": ("delta_w = n_g / (alpha * n_r_w) - 1 on cells with raw "
                                   "random CIC count >= NR_MIN; alpha = "
                                   "sum(n_g)/sum(n_r_w) over supported cells; delta_w = 0 "
                                   "elsewhere (zero-padding). The n_r_w-weighted mean of "
                                   "delta_w over the support is 0 by construction (alpha "
                                   "normalization), addressing the integral-constraint "
                                   "family; the UNWEIGHTED per-cell mean is positive "
                                   "(measured, reported as mean_delta_on_support), "
                                   "reflecting the radial-profile mismatch between the zall "
                                   "GALAXY parent and the BGS_BRIGHT clustering selection. "
                                   "The k=0 mode is zeroed in the Poisson inversion, so the "
                                   "offset does not enter the tidal classification."),
            "spiral_join_note": ("env classes NN-interpolated at the unique-TARGETID "
                                 "matched-spiral positions; B-vs-A uses the identical "
                                 "in-window spiral set, C-vs-D the identical full set"),
        },
        "parent_counts": {"n_rows_full": n_rows, "n_rows_window": n_win,
                          "n_spirals_full": int(len(sp)),
                          "n_spirals_window": int(sp_win.sum())},
        "builds": builds,
        "deltas_weighted_minus_unweighted_window": d_BA,
        "deltas_cube3_minus_production_dilation": d_CD,
        "context_window_minus_full_volume_fractions_pp": d_AD_vf,
    }
    OUT.write_text(json.dumps(out, indent=2))
    step(t0, f"wrote {OUT}")


if __name__ == "__main__":
    main()
