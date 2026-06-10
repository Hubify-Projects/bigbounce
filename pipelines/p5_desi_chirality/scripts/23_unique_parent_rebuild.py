#!/usr/bin/env python3
"""R24conf QUEUE-15 (P5 META-E1) — T-Web density field rebuilt on the
unique-TARGETID parent.

The production V-Web field (env_finder/01_compute_vweb.py) CIC-deposits every
row of the filtered DESI DR1 zall sample; TARGETIDs observed in multiple
coadds therefore deposit multiple times, weighting the density field by
n_coadd. This script rebuilds the full field (CIC -> footprint mask ->
Gaussian smoothing -> tidal eigenvalues -> classification) twice on the SAME
grid geometry (origin/box/cell from the row-level parent, replicating the
production cell size 25.9127 Mpc/h):

  build "row_level"        : all filtered rows (production replication)
  build "unique_targetid"  : deduped by TARGETID (keep='first') before CIC

and reports Delta(class volume fractions), cell-level class agreement, and
Delta(f_CW by class) on the identical unique-TARGETID matched-spiral set
(env class NN-interpolated at spiral positions in both fields, so the delta
isolates the field-construction change). Published row-level references
(env_finder/reports/01_volume_fractions.json and
results/analysis_cosmic_web/p4_monopole_residual_analysis.json) are quoted
alongside.

Output: pipelines/p5_desi_chirality/outputs/23_unique_parent_rebuild.json
Run:    nice -n 5 python3 pipelines/p5_desi_chirality/scripts/23_unique_parent_rebuild.py
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
PUB_VOLFRAC = P5 / "env_finder/reports/01_volume_fractions.json"
PUB_FCW = P5 / "results/analysis_cosmic_web/p4_monopole_residual_analysis.json"
OUT = P5 / "outputs/23_unique_parent_rebuild.json"


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


def build_field(pos, origin, cell_size, N, R_s, t0, tag):
    """Full V-Web pipeline (identical to 01_compute_vweb.py stages 5-10)."""
    from scipy.ndimage import binary_dilation
    count = cic_deposit(pos, origin, cell_size, N, t0)
    occupied = count > 0
    dilate = int(np.ceil(R_s / cell_size)) + 1
    mask = binary_dilation(occupied, iterations=dilate)
    n_mask = int(mask.sum())
    rho_mean = float(count[mask].mean())
    delta = np.zeros_like(count, dtype=np.float32)
    delta[mask] = (count[mask] / rho_mean - 1.0).astype(np.float32)
    del count
    step(t0, f"[{tag}] mask cells {n_mask:,}; rho_mean {rho_mean:.4f}")
    delta_s, KX, KY, KZ, k2 = gaussian_smooth_fft(delta, cell_size, R_s, t0)
    del delta
    l1, l2, l3 = tidal_eigenvalues(delta_s, KX, KY, KZ, k2, t0)
    del delta_s, KX, KY, KZ, k2
    cell_class = classify_vweb(l1, l2, l3, 0.0)
    del l1, l2, l3
    fracs = {ENV_CLASSES[i]: float(((cell_class == i) & mask).sum()) / n_mask
             for i in range(4)}
    step(t0, f"[{tag}] vol fracs: " + " ".join(f"{k}={v:.4f}" for k, v in fracs.items()))
    return cell_class, mask, n_mask, rho_mean, fracs


def main():
    t0 = time.time()
    cfg = yaml.safe_load(open(CONFIG_PATH))
    N = int(cfg["grid"]["n"])
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])
    R_s = float(cfg["smoothing"]["R_s_mpc_h"])

    step(t0, "Loading filtered zall ...")
    p = REPO_ROOT / cfg["input"]["zall_path"]
    cols = ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z", "ZWARN", "SPECTYPE"]
    df = pq.read_table(str(p), columns=cols).to_pandas()
    f = cfg["input"]["filter"]
    sel = ((df["ZWARN"] == f["zwarn_max"])
           & (df["SPECTYPE"].astype(str).str.strip() == f["spectype"])
           & (df["Z"] > f["z_min"]) & (df["Z"] < f["z_max"]))
    df = df.loc[sel, ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z"]].reset_index(drop=True)
    n_rows = len(df)
    step(t0, f"filtered rows: {n_rows:,}")

    pos_all = positions(df["Z"].values, df["TARGET_RA"].values, df["TARGET_DEC"].values)
    # fixed grid geometry from the row-level parent (production replication)
    mins = pos_all.min(axis=0) - pad
    maxs = pos_all.max(axis=0) + pad
    box_side = float(np.max(maxs - mins))
    origin = mins.astype(np.float32)
    cell_size = box_side / N
    step(t0, f"grid: N={N}, cell={cell_size:.4f} Mpc/h (production: 25.9127)")

    uniq_idx = (~df["TARGETID"].duplicated(keep="first")).to_numpy()
    n_unique = int(uniq_idx.sum())
    step(t0, f"unique TARGETIDs: {n_unique:,} ({n_rows - n_unique:,} duplicate rows, "
             f"{100*(n_rows-n_unique)/n_rows:.2f}%)")

    # matched-spiral parent (identical to script 22): primary-deduped CW/CCW,
    # then deduped by desi_targetid (keep='first')
    sp = pd.read_parquet(MATCHED, columns=["desi_targetid", "match_class_eq",
                                           "desi_z", "desi_ra", "desi_dec",
                                           "matched_primary_deduped"])
    sp = sp[sp["matched_primary_deduped"]
            & sp["match_class_eq"].isin(["CW", "CCW"])]
    sp = sp.drop_duplicates(subset="desi_targetid", keep="first").reset_index(drop=True)
    sp_pos = positions(sp["desi_z"].values, sp["desi_ra"].values, sp["desi_dec"].values)
    sp_cw = (sp["match_class_eq"] == "CW").to_numpy()
    step(t0, f"matched spirals (unique TARGETID): {len(sp):,}")

    def spiral_classes(cell_class):
        u = (sp_pos - origin) / cell_size
        idx = np.clip(np.floor(u + 0.5).astype(np.int64), 0, N - 1)
        return cell_class[idx[:, 0], idx[:, 1], idx[:, 2]]

    results = {}
    classes = {}
    sp_cls = {}
    masks = {}
    for tag, posv in [("row_level", pos_all), ("unique_targetid", pos_all[uniq_idx])]:
        cell_class, mask, n_mask, rho_mean, fracs = build_field(
            posv, origin, cell_size, N, R_s, t0, tag)
        scls = spiral_classes(cell_class)
        per_class = {}
        for i, cname in enumerate(ENV_CLASSES):
            m = scls == i
            nn = int(m.sum())
            ncw = int(sp_cw[m].sum())
            per_class[cname] = {"n": nn, "n_cw": ncw,
                                "cw_fraction": (ncw / nn) if nn else None,
                                "sigma_from_half": _sig(ncw, nn)}
        results[tag] = {"n_deposited": int(len(posv)), "n_mask_cells": n_mask,
                        "rho_mean_gal_per_cell": rho_mean,
                        "volume_fractions_in_footprint": fracs,
                        "spiral_f_cw_by_class": per_class}
        classes[tag] = cell_class
        sp_cls[tag] = scls
        masks[tag] = mask

    # ---- deltas -------------------------------------------------------------
    vf_row = results["row_level"]["volume_fractions_in_footprint"]
    vf_uni = results["unique_targetid"]["volume_fractions_in_footprint"]
    d_vf = {k: float(vf_uni[k] - vf_row[k]) for k in ENV_CLASSES}
    both = masks["row_level"] & masks["unique_targetid"]
    agree = float((classes["row_level"][both] == classes["unique_targetid"][both]).mean())
    sp_agree = float((sp_cls["row_level"] == sp_cls["unique_targetid"]).mean())
    d_fcw = {}
    for cname in ENV_CLASSES:
        a = results["row_level"]["spiral_f_cw_by_class"][cname]
        b = results["unique_targetid"]["spiral_f_cw_by_class"][cname]
        d_fcw[cname] = {
            "delta_f_cw_pp": (None if (a["cw_fraction"] is None or b["cw_fraction"] is None)
                              else float((b["cw_fraction"] - a["cw_fraction"]) * 100)),
            "delta_n": int(b["n"] - a["n"]),
        }

    pub_vf = json.loads(PUB_VOLFRAC.read_text())["volume_fractions_in_footprint"]
    pub_fcw = json.loads(PUB_FCW.read_text())["per_class_residual_vs_p5_monopole"]

    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/23_unique_parent_rebuild.py",
        "closes": "QUEUE-15 / META-E1 (R24CONF_COMPUTE_QUEUE.md)",
        "method": {
            "grid_n": N, "cell_size_mpc_h": cell_size, "box_side_mpc_h": box_side,
            "R_s_mpc_h": R_s, "lambda_th": 0.0,
            "geometry_note": ("identical origin/box/cell for both builds (set from the "
                              "row-level parent) so the delta isolates the dedupe; "
                              "dedupe = drop_duplicates(TARGETID, keep='first') before CIC"),
            "spiral_join_note": ("env classes NN-interpolated at the unique-TARGETID "
                                 "matched-spiral positions in BOTH fields (same spiral set); "
                                 "the published per-class f_CW values come from the row-level "
                                 "env-parquet TARGETID join (812,793 rows incl. duplicates) "
                                 "and are quoted for reference"),
        },
        "parent_counts": {"n_rows": n_rows, "n_unique_targetid": n_unique,
                          "n_duplicate_rows": n_rows - n_unique,
                          "duplicate_row_fraction": (n_rows - n_unique) / n_rows},
        "builds": results,
        "deltas_unique_minus_row_level": {
            "volume_fractions_pp": {k: v * 100 for k, v in d_vf.items()},
            "max_abs_volume_fraction_shift_pp": float(max(abs(v) for v in d_vf.values()) * 100),
            "cell_class_agreement_on_common_mask": agree,
            "spiral_class_assignment_agreement": sp_agree,
            "f_cw_by_class": d_fcw,
            "max_abs_f_cw_shift_pp": float(max(abs(v["delta_f_cw_pp"]) for v in d_fcw.values()
                                               if v["delta_f_cw_pp"] is not None)),
        },
        "published_references": {
            "volume_fractions_in_footprint_row_level": pub_vf,
            "f_cw_by_class_row_level_env_join": {
                k: {"n": v["n"], "cw_fraction": v["cw_fraction"]}
                for k, v in pub_fcw.items()},
        },
    }
    OUT.write_text(json.dumps(out, indent=2))
    step(t0, f"wrote {OUT}")


if __name__ == "__main__":
    main()
