#!/usr/bin/env python3
"""R24conf local-batch closures — P5 queue items 20, 21, 22, 23, 25, 27.

QUEUE-20 / META-M7   : MC validation of the ASTRA entropy-weighted variance
                       using the actual per-object {P_class} probabilities
                       (10^4 Bernoulli(0.5)-null draws on the 25,186 overlap).
QUEUE-21 / OpenAI-M8 : Sec. VIII.F per-pixel sigma_vs_monopole distribution +
                       void-count correlations recomputed on the
                       unique-TARGETID env-joined parent (dedupe by TARGETID
                       BEFORE the per-pixel pass).
QUEUE-22 / OpenAI-M9 : per-shell N table for the 21 z-shells + in-mask
                       cell-level mean/var of delta BEFORE (global-mean) and
                       AFTER (shell-mean) the selection correction, from a
                       rerun of the script-16 grid stage (CIC + mask + shells;
                       no smoothing needed).
QUEUE-23 / OpenAI-m9 : EDGE/DEPTH flag inclusion test in the V2 GALZONE
                       catalog-native void cut (baseline OUT=0 & ZONE>=0 &
                       VOID0>=0; variants + EDGE=0, + DEPTH>=1, + DEPTH>=2).
                       SIDE FINDING: the published catalog-native numbers in
                       results/analysis_cosmic_web/desivast_catalog_native_
                       void_chirality.json (REVOLVER 86,276 / VIDE 64,514)
                       reproduce EXACTLY (n, f_CW, sigma) only under a
                       zone-indexing defect: concatenating NGC+SGC ZONEVOID
                       without per-cap zone-id offsets and deduping the
                       zone->VOID0 map with keep='last' (SGC rows overwrite
                       NGC zone ids). The correct per-cap join yields
                       REVOLVER 104,912 / VIDE 74,111. Both reproductions are
                       recorded below; the corrected values supersede.
QUEUE-25 / OpenAI-m14: fraction of in-mask grid cells within R_s = 25 Mpc/h
                       of the occupancy-footprint boundary (same buffer
                       definition as script 16).
QUEUE-27 / META-m1   : kNN (k=5) density-quintile recompute with a HEALPix
                       NSIDE-64 mask-edge angular buffer; Fig. 5
                       quintile-assignment invariance + max per-quintile
                       f_CW shift.

Output: pipelines/p5_desi_chirality/outputs/22_r24conf_local_batch.json
Run:    nice -n 5 python3 pipelines/p5_desi_chirality/scripts/22_r24conf_local_batch.py
"""
from __future__ import annotations

import glob
import json
import sys
import time
import traceback
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import yaml

P5 = Path(__file__).resolve().parents[1]
REPO_ROOT = P5.parents[1]
sys.path.insert(0, str(P5 / "env_finder"))
from _compute_vweb_lib import cic_deposit, step  # noqa: E402

MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
ENV_VWEB = P5 / "data/desi_env/desi_env_vweb.parquet"
ASTRA_PROBS_DIR = P5 / "data/desi_env/astra_edr/probabilities"
DESIVAST_DIR = P5 / "data/desivast"
CONFIG_PATH = P5 / "env_finder/config.yaml"
ZSHELL_JSON = P5 / "outputs/16_cosmic_web_zshell_corrected.json"
OUT = P5 / "outputs/22_r24conf_local_batch.json"

ENV_ORDER = ["void", "wall", "filament", "cluster"]
ASTRA_TO_VWEB = {"PVOID": "void", "PSHEET": "wall",
                 "PFILAMENT": "filament", "PKNOT": "cluster"}
SEED = 20260610
Z_DESIVAST_MAX = 0.24

# script-16 shell scheme (identical)
Z_EDGES = np.concatenate([
    np.array([0.01]),
    np.arange(0.05, 0.50 + 1e-9, 0.05),
    np.arange(0.60, 1.50 + 1e-9, 0.10),
    np.array([1.70]),
])


def _sig(n_cw: int, n: int) -> float:
    return float((n_cw - 0.5 * n) / (0.5 * np.sqrt(n))) if n else float("nan")


def _cls_row(sub: pd.DataFrame) -> dict:
    n = int(len(sub))
    n_cw = int((sub["match_class_eq"] == "CW").sum())
    return {"n": n, "n_cw": n_cw, "cw_fraction": (n_cw / n) if n else None,
            "sigma_from_half": _sig(n_cw, n)}


def load_spirals() -> pd.DataFrame:
    cols = ["desi_targetid", "match_class_eq", "desi_z", "desi_ra", "desi_dec",
            "matched_primary_deduped"]
    m = pd.read_parquet(MATCHED, columns=cols)
    sp = m[m["matched_primary_deduped"]
           & m["match_class_eq"].isin(["CW", "CCW"])].copy()
    return sp.reset_index(drop=True)


# --------------------------------------------------------------------------
# QUEUE-22 + QUEUE-25 — grid pass (CIC + mask + shells + EDT buffer)
# --------------------------------------------------------------------------
def grid_pass(t0) -> dict:
    from astropy.cosmology import Planck18
    from scipy.ndimage import binary_dilation, distance_transform_edt

    cfg = yaml.safe_load(open(CONFIG_PATH))
    N = int(cfg["grid"]["n"])
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])
    R_s = float(cfg["smoothing"]["R_s_mpc_h"])

    step(t0, "Loading filtered zall (grid pass) ...")
    p = REPO_ROOT / cfg["input"]["zall_path"]
    cols = ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z", "ZWARN", "SPECTYPE"]
    df = pq.read_table(str(p), columns=cols).to_pandas()
    f = cfg["input"]["filter"]
    sel = ((df["ZWARN"] == f["zwarn_max"])
           & (df["SPECTYPE"].astype(str).str.strip() == f["spectype"])
           & (df["Z"] > f["z_min"]) & (df["Z"] < f["z_max"]))
    df = df.loc[sel, ["TARGET_RA", "TARGET_DEC", "Z"]].reset_index(drop=True)
    step(t0, f"  filtered rows: {len(df):,}")

    chi = (Planck18.comoving_distance(df["Z"].values).value
           * (Planck18.H0.value / 100.0)).astype(np.float32)
    ra = np.deg2rad(df["TARGET_RA"].values).astype(np.float32)
    dec = np.deg2rad(df["TARGET_DEC"].values).astype(np.float32)
    cd = np.cos(dec)
    pos = np.empty((len(df), 3), dtype=np.float32)
    pos[:, 0] = chi * cd * np.cos(ra)
    pos[:, 1] = chi * cd * np.sin(ra)
    pos[:, 2] = chi * np.sin(dec)
    del chi, ra, dec, cd, df

    mins = pos.min(axis=0) - pad
    maxs = pos.max(axis=0) + pad
    box_side = float(np.max(maxs - mins))
    origin = mins.astype(np.float32)
    cell_size = box_side / N
    count = cic_deposit(pos, origin, cell_size, N, t0)
    del pos
    occupied = count > 0
    dilate_radius_cells = int(np.ceil(R_s / cell_size)) + 1
    mask = binary_dilation(occupied, iterations=dilate_radius_cells)
    n_mask = int(mask.sum())
    rho_mean_global = float(count[mask].mean())
    step(t0, f"  mask cells {n_mask:,}; global rho_mean {rho_mean_global:.4f}")

    # shell index per cell (identical to script 16)
    ax = (origin[:, None] + np.arange(N, dtype=np.float32)[None, :]
          * np.float32(cell_size))
    chi_cell = np.sqrt((ax[0] ** 2)[:, None, None]
                       + (ax[1] ** 2)[None, :, None]
                       + (ax[2] ** 2)[None, None, :]).astype(np.float32)
    h = Planck18.H0.value / 100.0
    chi_edges = (Planck18.comoving_distance(Z_EDGES).value * h).astype(np.float64)
    n_shells = len(Z_EDGES) - 1
    shell_idx = np.clip(np.digitize(chi_cell, chi_edges) - 1, 0,
                        n_shells - 1).astype(np.int16)
    del chi_cell

    # QUEUE-22: per-shell N table + mean/var delta before/after correction
    art16 = json.loads(ZSHELL_JSON.read_text())
    n_gal_16 = {s["shell"]: s["n_galaxies"] for s in art16["shells"]}
    shells = []
    for s in range(n_shells):
        selc = mask & (shell_idx == s)
        n_cells = int(selc.sum())
        if n_cells == 0:
            continue
        c = count[selc].astype(np.float64)
        nbar = float(c.mean())
        d_glob = c / rho_mean_global - 1.0
        d_shell = c / nbar - 1.0
        shells.append({
            "shell": s, "z_lo": float(Z_EDGES[s]), "z_hi": float(Z_EDGES[s + 1]),
            "n_galaxies": int(n_gal_16.get(s, -1)),
            "n_mask_cells": n_cells, "nbar_shell_gal_per_cell": nbar,
            "delta_globalmean_mean": float(d_glob.mean()),
            "delta_globalmean_var": float(d_glob.var()),
            "delta_shellmean_mean": float(d_shell.mean()),
            "delta_shellmean_var": float(d_shell.var()),
        })
    del count, shell_idx

    # QUEUE-25: in-mask cells within R_s of the occupancy-footprint boundary
    edt_cells = distance_transform_edt(mask).astype(np.float32)
    buffer_thresh = dilate_radius_cells * cell_size + R_s
    cell_buffer = (edt_cells * np.float32(cell_size)) <= np.float32(buffer_thresh)
    n_buf = int((cell_buffer & mask).sum())
    del edt_cells, cell_buffer, mask, occupied
    return {
        "method": {"grid_n": N, "cell_size_mpc_h": cell_size,
                   "box_side_mpc_h": box_side, "R_s_mpc_h": R_s,
                   "dilate_radius_cells": dilate_radius_cells,
                   "rho_mean_global_gal_per_cell": rho_mean_global,
                   "buffer_threshold_mpc_h": float(buffer_thresh),
                   "buffer_definition": ("in-mask cell within (dilation + R_s) "
                                         "of mask exterior == within R_s of "
                                         "true occupancy-footprint boundary "
                                         "(identical to script 16)"),
                   "note": ("delta means/vars are raw cell-level (pre-"
                            "smoothing) over in-mask cells per shell; the "
                            "shell-mean delta has zero mean per shell by "
                            "construction")},
        "QUEUE22_per_shell_table": shells,
        "QUEUE25_boundary_buffer_fraction": {
            "n_in_mask_cells": n_mask, "n_in_mask_cells_within_Rs_of_boundary": n_buf,
            "fraction": n_buf / n_mask,
        },
    }


# --------------------------------------------------------------------------
# QUEUE-21 — per-pixel pass on the unique-TARGETID env parent
# --------------------------------------------------------------------------
def queue21(sp: pd.DataFrame, t0) -> dict:
    import healpy as hp
    from astropy.io import fits
    from scipy import stats

    step(t0, "QUEUE-21: env join + unique-TARGETID dedupe ...")
    env = pd.read_parquet(ENV_VWEB, columns=["TARGETID", "env_class"])
    j = sp.merge(env, left_on="desi_targetid", right_on="TARGETID", how="inner")
    n_rows_parent = int(len(j))
    ju = j.drop_duplicates(subset="desi_targetid", keep="first").copy()
    del j, env
    n_cw = int((ju["match_class_eq"] == "CW").sum())
    f_mono = n_cw / len(ju)

    pix = hp.ang2pix(32, ju["desi_ra"].to_numpy(), ju["desi_dec"].to_numpy(),
                     lonlat=True)
    g = pd.DataFrame({"pix": pix, "cw": (ju["match_class_eq"] == "CW")})
    agg = g.groupby("pix")["cw"].agg(["size", "sum"])
    agg = agg[agg["size"] >= 200]
    sig_pix = (agg["sum"] - f_mono * agg["size"]) / (0.5 * np.sqrt(agg["size"]))
    dist = {"nside": 32, "min_spirals_per_pixel": 200,
            "n_valid_pixels": int(len(agg)), "monopole_f_cw": float(f_mono),
            "mean": float(sig_pix.mean()), "std": float(sig_pix.std(ddof=0)),
            "skew": float(stats.skew(sig_pix)),
            "excess_kurtosis": float(stats.kurtosis(sig_pix))}

    # void-count correlations on the unique-TARGETID parent, z<=0.24
    zcut = ju[ju["desi_z"] <= Z_DESIVAST_MAX]
    pix2 = hp.ang2pix(32, zcut["desi_ra"].to_numpy(), zcut["desi_dec"].to_numpy(),
                      lonlat=True)
    g2 = pd.DataFrame({"pix": pix2, "cw": (zcut["match_class_eq"] == "CW")})
    per = g2.groupby("pix")["cw"].agg(n="size", n_cw="sum")
    per["sigma"] = (per["n_cw"] - 0.5 * per["n"]) / (0.5 * np.sqrt(per["n"]))
    ras, decs = [], []
    for gc in ["NGC", "SGC"]:
        with fits.open(DESIVAST_DIR / f"DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits") as fh:
            mx = fh["MAXIMALS"].data
            ras.append(np.asarray(mx["RA"], dtype=float))
            decs.append(np.asarray(mx["DEC"], dtype=float))
    vpix = hp.ang2pix(32, np.concatenate(ras), np.concatenate(decs), lonlat=True)
    per["n_voids"] = pd.Series(vpix).value_counts().reindex(per.index).fillna(0).astype(int)
    sel = per[(per["n"] >= 200) & (per["n_voids"] >= 1)]
    x = sel["n_voids"].values.astype(float)
    y = sel["sigma"].values
    w = sel["n"].values.astype(float)
    r_unw, p_unw = stats.pearsonr(x, y)
    rho_sp, p_sp = stats.spearmanr(x, y)
    wn = w / w.sum()
    mx_, my_ = np.sum(wn * x), np.sum(wn * y)
    cov = np.sum(wn * (x - mx_) * (y - my_))
    r_w = cov / (np.sqrt(np.sum(wn * (x - mx_) ** 2))
                 * np.sqrt(np.sum(wn * (y - my_) ** 2)))
    neff = 1.0 / np.sum(wn ** 2)
    t = r_w * np.sqrt(max(neff - 2, 1) / max(1 - r_w ** 2, 1e-12))
    p_w = 2 * stats.t.sf(abs(t), max(neff - 2, 1))
    return {
        "parent": ("env-joined matched spirals deduped by TARGETID before the "
                   "per-pixel pass (keep=first)"),
        "n_rows_env_parent": n_rows_parent,
        "n_unique_targetid": int(len(ju)),
        "sigma_vs_monopole_distribution": dist,
        "void_count_correlation_z_leq_0p24": {
            "n_spirals_zcut": int(len(zcut)), "n_valid_pixels": int(len(sel)),
            "pearson_unweighted": {"r": float(r_unw), "p": float(p_unw)},
            "pearson_weighted_Npix": {"r": float(r_w), "p": float(p_w),
                                      "n_eff": float(neff)},
            "spearman": {"rho": float(rho_sp), "p": float(p_sp)},
        },
    }


# --------------------------------------------------------------------------
# QUEUE-23 — EDGE/DEPTH flag variants of the V2 GALZONE catalog-native cut
# --------------------------------------------------------------------------
def queue23(sp: pd.DataFrame, t0) -> dict:
    from astropy.io import fits

    step(t0, "QUEUE-23: V2 GALZONE EDGE/DEPTH variants ...")
    lz = sp[sp["desi_z"] <= Z_DESIVAST_MAX][["desi_targetid", "match_class_eq"]]
    out = {"matched_spirals_z_leq_0p24": int(len(lz)), "by_algorithm": {}}
    for algo in ["V2_REVOLVER", "V2_VIDE"]:
        gzs, zvs, zvs_raw = [], [], []
        zone_offset = 0
        for gc in ["NGC", "SGC"]:
            with fits.open(DESIVAST_DIR / f"DESIVAST_BGS_VOLLIM_{algo}_{gc}.fits") as fh:
                gz = fh["GALZONE"].data
                zv = fh["ZONEVOID"].data
                gd = pd.DataFrame({
                    "TARGET": np.asarray(gz["TARGET"], dtype=np.int64),
                    "ZONE": np.asarray(gz["ZONE"], dtype=np.int64),
                    "DEPTH": np.asarray(gz["DEPTH"], dtype=np.int64),
                    "EDGE": np.asarray(gz["EDGE"], dtype=np.int64),
                    "OUT": np.asarray(gz["OUT"], dtype=np.int64),
                })
                zd = pd.DataFrame({
                    "ZONE": np.asarray(zv["ZONE"], dtype=np.int64),
                    "VOID0": np.asarray(zv["VOID0"], dtype=np.int64),
                })
                zvs_raw.append(zd.copy())  # raw (non-offset) for bug repro
                # offset ZONE ids so NGC/SGC zone tables don't collide
                gd.loc[gd["ZONE"] >= 0, "ZONE"] += zone_offset
                zd["ZONE"] += zone_offset
                zone_offset += int(zd["ZONE"].max()) + 1
                gzs.append(gd)
                zvs.append(zd)
        gal = pd.concat(gzs, ignore_index=True)
        zone = pd.concat(zvs, ignore_index=True)
        gal = gal.merge(zone, on="ZONE", how="left")
        gal["VOID0"] = gal["VOID0"].fillna(-1).astype(np.int64)
        j = lz.merge(gal, left_on="desi_targetid", right_on="TARGET", how="inner")
        base = (j["OUT"] == 0) & (j["ZONE"] >= 0) & (j["VOID0"] >= 0)
        variants = {
            "baseline_OUT0_VOID0ge0": base,
            "plus_EDGE0": base & (j["EDGE"] == 0),
            "plus_DEPTH_ge1": base & (j["DEPTH"] >= 1),
            "plus_DEPTH_ge2": base & (j["DEPTH"] >= 2),
        }
        res = {"n_joined_galzone_rows": int(len(j))}
        f_base = None
        for name, m in variants.items():
            sub = j[m]
            row = _cls_row(sub)
            if name == "baseline_OUT0_VOID0ge0":
                f_base = row["cw_fraction"]
            row["f_cw_shift_pp_vs_baseline"] = (
                (row["cw_fraction"] - f_base) * 100
                if (row["cw_fraction"] is not None and f_base is not None) else None)
            res[name] = row
        # reproduce the published (buggy) numbers: non-offset zone map with
        # keep='last' dedupe (SGC ZONEVOID rows overwrite NGC zone ids)
        gzs_raw = []
        for gc in ["NGC", "SGC"]:
            from astropy.io import fits as _fits
            with _fits.open(DESIVAST_DIR / f"DESIVAST_BGS_VOLLIM_{algo}_{gc}.fits") as fh:
                gz = fh["GALZONE"].data
                gzs_raw.append(pd.DataFrame({
                    "TARGET": np.asarray(gz["TARGET"], dtype=np.int64),
                    "ZONE": np.asarray(gz["ZONE"], dtype=np.int64),
                    "OUT": np.asarray(gz["OUT"], dtype=np.int64),
                }))
        graw = pd.concat(gzs_raw, ignore_index=True)
        zraw = pd.concat(zvs_raw, ignore_index=True).drop_duplicates(
            "ZONE", keep="last")
        graw = graw.merge(zraw, on="ZONE", how="left")
        graw["VOID0"] = graw["VOID0"].fillna(-9).astype(np.int64)
        jraw = lz.merge(graw, left_on="desi_targetid", right_on="TARGET",
                        how="inner")
        mraw = (jraw["OUT"] == 0) & (jraw["ZONE"] >= 0) & (jraw["VOID0"] >= 0)
        res["published_value_reproduction_via_zone_offset_bug"] = {
            **_cls_row(jraw[mraw]),
            "note": ("non-offset NGC+SGC ZONEVOID concat deduped keep='last' "
                     "reproduces the published desivast_catalog_native_void_"
                     "chirality.json numbers exactly; diagnosis of the "
                     "published-artifact defect, superseded by the corrected "
                     "per-cap baseline above"),
        }
        out["by_algorithm"][algo] = res
    return out


# --------------------------------------------------------------------------
# QUEUE-27 — kNN density quintiles with mask-edge angular buffer
# --------------------------------------------------------------------------
def queue27(sp: pd.DataFrame, t0) -> dict:
    import healpy as hp
    from sklearn.neighbors import BallTree

    K = 5
    NSIDE_BUF = 64
    qs = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    ra = sp["desi_ra"].to_numpy()
    dec = sp["desi_dec"].to_numpy()
    is_cw = (sp["match_class_eq"] == "CW").to_numpy()

    def knn_density(ra_d, dec_d):
        coords = np.column_stack([np.deg2rad(dec_d), np.deg2rad(ra_d)])
        tree = BallTree(coords, metric="haversine")
        dist, _ = tree.query(coords, k=K + 1)
        kth = dist[:, K]
        kth = np.where(kth <= 0, np.nan, kth)
        return 1.0 / (kth ** 2)

    def quintiles(density):
        edges = np.quantile(density[np.isfinite(density)], qs)
        b = np.clip(np.digitize(density, edges) - 1, 0, len(qs) - 2)
        return b

    def per_q(bins, cw):
        rows = []
        for i in range(5):
            m = bins == i
            n = int(m.sum())
            ncw = int(cw[m].sum())
            rows.append({"quintile": i + 1, "n": n, "n_cw": ncw,
                         "cw_fraction": ncw / n if n else None,
                         "sigma_from_half": _sig(ncw, n)})
        return rows

    step(t0, "QUEUE-27: baseline kNN density (k=5) ...")
    d0 = knn_density(ra, dec)
    b0 = quintiles(d0)
    base_rows = per_q(b0, is_cw)

    # mask-edge angular buffer: NSIDE-64 occupancy; drop spirals in occupied
    # pixels that have >=1 unoccupied neighbor pixel (~0.9 deg buffer)
    step(t0, "QUEUE-27: NSIDE-64 mask-edge buffer ...")
    pix = hp.ang2pix(NSIDE_BUF, ra, dec, lonlat=True)
    occ = np.zeros(hp.nside2npix(NSIDE_BUF), dtype=bool)
    occ[np.unique(pix)] = True
    occ_pix = np.where(occ)[0]
    neigh = hp.get_all_neighbours(NSIDE_BUF, occ_pix)  # (8, n_occ)
    has_empty_neighbor = np.zeros_like(occ)
    valid = neigh >= 0
    empty_n = np.zeros(neigh.shape[1], dtype=bool)
    for r in range(neigh.shape[0]):
        row = neigh[r]
        bad = (~valid[r]) | (~occ[np.clip(row, 0, None)])
        empty_n |= bad
    has_empty_neighbor[occ_pix[empty_n]] = True
    keep = ~has_empty_neighbor[pix]
    n_removed = int((~keep).sum())

    step(t0, f"QUEUE-27: buffered kNN density on {int(keep.sum()):,} spirals ...")
    d1 = knn_density(ra[keep], dec[keep])
    b1 = quintiles(d1)
    buf_rows = per_q(b1, is_cw[keep])

    same = float((b0[keep] == b1).mean())
    shifts = [abs(buf_rows[i]["cw_fraction"] - base_rows[i]["cw_fraction"]) * 100
              for i in range(5)]
    return {
        "knn_k": K, "buffer": f"HEALPix NSIDE={NSIDE_BUF} occupied pixels with "
                              ">=1 unoccupied neighbor excluded (~0.9 deg edge buffer)",
        "n_spirals_total": int(len(sp)), "n_spirals_removed_by_buffer": n_removed,
        "baseline_quintiles": base_rows,
        "buffered_quintiles": buf_rows,
        "quintile_assignment_agreement_retained": same,
        "max_per_quintile_f_cw_shift_pp": float(max(shifts)),
        "per_quintile_f_cw_shift_pp": [float(s) for s in shifts],
    }


# --------------------------------------------------------------------------
# QUEUE-20 — MC validation of the ASTRA entropy-weighted variance
# --------------------------------------------------------------------------
def queue20(sp: pd.DataFrame, t0) -> dict:
    from astropy.io import fits

    step(t0, "QUEUE-20: loading ASTRA per-object probabilities ...")
    rows = []
    for f in sorted(glob.glob(str(ASTRA_PROBS_DIR / "zone_*_probability.fits.gz"))):
        with fits.open(f) as h:
            d = h[1].data
            rows.append(pd.DataFrame({
                "TARGETID": d["TARGETID"].astype(np.int64),
                "PVOID": d["PVOID"].astype(np.float64),
                "PSHEET": d["PSHEET"].astype(np.float64),
                "PFILAMENT": d["PFILAMENT"].astype(np.float64),
                "PKNOT": d["PKNOT"].astype(np.float64),
            }))
    astra = pd.concat(rows, ignore_index=True)
    astra = astra.groupby("TARGETID", as_index=False).mean()
    s = astra[["PVOID", "PSHEET", "PFILAMENT", "PKNOT"]].sum(axis=1)
    for c in ["PVOID", "PSHEET", "PFILAMENT", "PKNOT"]:
        astra[c] = astra[c] / s

    p5 = sp[["desi_targetid", "match_class_eq"]].copy()
    p5["TARGETID"] = p5["desi_targetid"].astype(np.int64)
    j = p5.merge(astra, on="TARGETID", how="inner")
    # restrict to the published 25,186-spiral overlap (all three labels:
    # chirality x ASTRA x V-Web), identical to script 15
    vweb_ids = pd.read_parquet(ENV_VWEB, columns=["TARGETID"])
    vweb_ids = vweb_ids.drop_duplicates("TARGETID")
    j = j.merge(vweb_ids, on="TARGETID", how="inner")
    n = len(j)
    step(t0, f"QUEUE-20: overlap = {n:,} spirals (expect 25,186)")

    prob_cols = ["PVOID", "PSHEET", "PFILAMENT", "PKNOT"]
    P = j[prob_cols].to_numpy()  # (n, 4)
    is_cw = (j["match_class_eq"] == "CW").to_numpy(float)
    n_eff = P.sum(axis=0)
    obs_ncw_eff = (P * is_cw[:, None]).sum(axis=0)
    analytic_sd = np.sqrt(0.25 * (P ** 2).sum(axis=0))

    n_mc = 10_000
    rng = np.random.default_rng(SEED)
    sums = np.empty((n_mc, 4))
    chunk = 500
    for i0 in range(0, n_mc, chunk):
        m = min(chunk, n_mc - i0)
        X = rng.random((m, n)) < 0.5
        sums[i0:i0 + m] = X @ P
    centered = sums - 0.5 * n_eff
    mc_sd = centered.std(axis=0, ddof=1)
    mc_cov = np.cov(centered.T)
    obs_dev = obs_ncw_eff - 0.5 * n_eff
    p_two = ((np.abs(centered) >= np.abs(obs_dev)).sum(axis=0) + 1) / (n_mc + 1)
    per_class = {}
    for k, (pcol, cls) in enumerate(ASTRA_TO_VWEB.items()):
        per_class[cls] = {
            "n_eff": float(n_eff[k]),
            "obs_n_cw_eff": float(obs_ncw_eff[k]),
            "analytic_sd": float(analytic_sd[k]),
            "mc_sd": float(mc_sd[k]),
            "mc_over_analytic_sd_ratio": float(mc_sd[k] / analytic_sd[k]),
            "sigma_analytic": float(obs_dev[k] / analytic_sd[k]),
            "sigma_mc": float(obs_dev[k] / mc_sd[k]),
            "p_two_sided_mc": float(p_two[k]),
        }
    corr = mc_cov / np.outer(mc_sd, mc_sd)
    return {
        "n_overlap": int(n), "n_mc": n_mc, "seed": SEED,
        "null": "independent per-object Bernoulli(0.5) CW labels",
        "per_class": per_class,
        "max_abs_sd_ratio_deviation_pct": float(
            np.max(np.abs(mc_sd / analytic_sd - 1.0)) * 100),
        "mc_between_class_correlation": {
            "classes": list(ASTRA_TO_VWEB.values()),
            "matrix": [[float(corr[a, b]) for b in range(4)] for a in range(4)],
            "note": ("non-zero off-diagonals quantify the within-object "
                     "negative correlation among class weights that the "
                     "analytic per-class variance neglects"),
        },
    }


def main() -> int:
    t0 = time.time()
    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/22_r24conf_local_batch.py",
        "closes": ["QUEUE-20/META-M7", "QUEUE-21/OpenAI-M8", "QUEUE-22/OpenAI-M9",
                   "QUEUE-23/OpenAI-m9", "QUEUE-25/OpenAI-m14", "QUEUE-27/META-m1"],
    }
    sp = load_spirals()
    out["parent_catalog_matched_n"] = int(len(sp))

    items = [
        ("QUEUE22_QUEUE25_grid_pass", lambda: grid_pass(t0)),
        ("QUEUE21_unique_targetid_perpixel", lambda: queue21(sp, t0)),
        ("QUEUE23_v2_galzone_flag_variants", lambda: queue23(sp, t0)),
        ("QUEUE27_density_quintile_edge_buffer", lambda: queue27(sp, t0)),
        ("QUEUE20_astra_entropy_mc", lambda: queue20(sp, t0)),
    ]
    for name, fn in items:
        try:
            out[name] = fn()
            step(t0, f"{name}: OK")
        except Exception:
            out[name] = {"FAILED": traceback.format_exc()}
            step(t0, f"{name}: FAILED")
        OUT.write_text(json.dumps(out, indent=2))
    out["runtime_seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=2))
    print(f"[done] wrote {OUT} in {out['runtime_seconds']}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
