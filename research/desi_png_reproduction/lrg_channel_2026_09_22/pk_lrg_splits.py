#!/usr/bin/env python3
"""Ledger row 4 LRG channel: the five pre-registered systematics splits,
measured with pypower at IDENTICAL settings to v5's QSO runs
(../pk_estimator_qso_weightsys_v5.py, ../pk_estimator_qso_gallat_v5.py,
../pk_estimator_qso_splits.py): nmesh=256, N_RAN=4, ells (0,2,4),
edges arange(0, 0.31, 0.001), los="firstpoint", tsc, interlacing=2, f8.

Inputs come from the derived column cache built by stream_lrg_cache.py --
no catalogue is read from disk, because none was ever written there.
Splits are per z-bin (the official window/covariance products are per
z-bin), NGC and SGC separately, combined later by fit_lrg_splits.py's
n_data-weighted mean exactly as ../fit_fnl_splits.py does.

Resumable: an existing output json for a (zbin, cap, prop, half) is skipped.
"""
import json
import os
import sys
import time

import numpy as np
from cosmoprimo.fiducial import DESI
from pypower import CatalogFFTPower

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction"
CACHE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/lrg_stream_cache"
OUT = f"{HERE}/lrg_channel_2026_09_22/outputs/pk"
ZBINS = {"0.4-0.6": (0.4, 0.6), "0.6-0.8": (0.6, 0.8), "0.8-1.1": (0.8, 1.1)}
PROPS = ["EBV", "STARDENS", "GALDEPTH_Z", "WEIGHTSYS", "GALLAT"]
N_RAN = 4
NMESH = 256
cosmo = DESI(engine="eisenstein_hu")
_MEM = {}


def load(name):
    if name not in _MEM:
        while len(_MEM) >= 5:      # one cap's data + its 4 randoms resident
            _MEM.pop(next(iter(_MEM)))
        _MEM[name] = dict(np.load(f"{CACHE}/{name}.npz"))
    return _MEM[name]


def zmask(d, zb):
    lo, hi = ZBINS[zb]
    return (d["Z"] > lo) & (d["Z"] < hi)


def medians(zb):
    path = f"{HERE}/lrg_channel_2026_09_22/outputs/split_medians.json"
    if os.path.exists(path):
        allm = json.load(open(path))
        if zb in allm:
            return allm[zb]
    else:
        allm = {}
    vals = {p: [] for p in ("EBV", "STARDENS", "GALDEPTH_Z")}
    n = 0
    for cap in ("NGC", "SGC"):
        d = load(f"LRG_{cap}_data")
        m = zmask(d, zb)
        n += int(m.sum())
        for p in vals:
            vals[p].append(d[p][m])
    out = {p: float(np.median(np.concatenate(v)[np.isfinite(np.concatenate(v))]))
           for p, v in vals.items()}
    out["_n_data"] = n
    allm[zb] = out
    json.dump(allm, open(path, "w"), indent=2)
    return out


def split_mask(arr, prop, half, med):
    if prop == "GALLAT":
        return np.abs(arr["GALB"]) > 40 if half == "high" else np.abs(arr["GALB"]) <= 40
    if prop == "WEIGHTSYS":
        return np.ones(len(arr["RA"]), dtype=bool)
    v = arr[prop]
    ok = np.isfinite(v)
    return ok & (v > med[prop]) if half == "high" else ok & (v <= med[prop])


def weights(arr, m, prop, half):
    w = arr["WEIGHT"][m].astype(np.float64)
    if prop == "WEIGHTSYS" and half == "low":
        w = w / arr["WEIGHT_SYS"][m].astype(np.float64)
    return w * arr["WEIGHT_FKP"][m].astype(np.float64)


def xyz(arr, m):
    ra = np.deg2rad(arr["RA"][m].astype(np.float64))
    dec = np.deg2rad(arr["DEC"][m].astype(np.float64))
    dist = cosmo.comoving_radial_distance(arr["Z"][m].astype(np.float64))
    return np.array([dist * np.cos(dec) * np.cos(ra),
                     dist * np.cos(dec) * np.sin(ra),
                     dist * np.sin(dec)])


def run_one(zb, cap, prop, half, med):
    tag = f"pk_LRG_z{zb}_{cap}_{prop}_{half}"
    path = f"{OUT}/{tag}.json"
    if os.path.exists(path):
        print(f"[skip] {tag}", flush=True)
        return
    t0 = time.time()
    d = load(f"LRG_{cap}_data")
    md = zmask(d, zb) & split_mask(d, prop, half, med)
    dpos, dw = xyz(d, md), weights(d, md, prop, half)
    n_data = int(md.sum())
    rpos_l, rw_l = [], []
    for i in range(N_RAN):
        r = load(f"LRG_{cap}_ran{i}")
        mr = zmask(r, zb) & split_mask(r, prop, half, med)
        rpos_l.append(xyz(r, mr))
        rw_l.append(weights(r, mr, prop, half))
    rpos = np.concatenate(rpos_l, axis=1)
    rw = np.concatenate(rw_l)
    del rpos_l, rw_l
    edges = np.arange(0.0, 0.31, 0.001)
    res = CatalogFFTPower(
        data_positions1=dpos, data_weights1=dw,
        randoms_positions1=rpos, randoms_weights1=rw,
        edges=edges, ells=(0, 2, 4), los="firstpoint",
        nmesh=NMESH, resampler="tsc", interlacing=2,
        position_type="xyz", dtype="f8")
    poles = res.poles
    out = dict(k=poles.k.tolist(), p0=poles(ell=0).real.tolist(),
               p2=poles(ell=2).real.tolist(), p4=poles(ell=4).real.tolist(),
               nmodes=poles.nmodes.tolist(), n_data=n_data, n_ran=int(len(rw)),
               zbin=zb, cap=cap, prop=prop, half=half,
               seconds=round(time.time() - t0, 1))
    os.makedirs(OUT, exist_ok=True)
    json.dump(out, open(path, "w"))
    print(f"[{tag}] N={n_data} Nran={len(rw)} {time.time()-t0:.0f}s", flush=True)
    del dpos, dw, rpos, rw, res


def main():
    os.makedirs(OUT, exist_ok=True)
    order = sys.argv[1].split(",") if len(sys.argv) > 1 else ["0.8-1.1", "0.6-0.8", "0.4-0.6"]
    props = sys.argv[2].split(",") if len(sys.argv) > 2 else PROPS
    for zb in order:                     # pre-registered order: descending volume
        med = medians(zb)
        print(f"== z{zb} medians {med}", flush=True)
        for prop in props:
            for cap in ("NGC", "SGC"):
                for half in ("high", "low"):
                    run_one(zb, cap, prop, half, med)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
