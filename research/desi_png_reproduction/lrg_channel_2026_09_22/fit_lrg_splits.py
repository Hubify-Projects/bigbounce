#!/usr/bin/env python3
"""Ledger row 4 LRG channel: fit f_NL for each pre-registered systematics
split half and build the 5-row table -- the LRG analogue of v5's
../fit_fnl_splits_v5.py, on the same convention.

Machinery identical to ../fit_fnl_splits.py: b1 free, n_shot fixed = 0,
OFFICIAL window matrix + OFFICIAL EZmock covariance, NGC+SGC combined by
n_data-weighted mean before rebinning onto the covariance's coarse grid,
KMIN/KMAX = 0.003/0.08, profile-likelihood sigma. Same disclosed
covariance-reuse caveat as v4/v5: no split-specific official covariance
exists, so the full-sample covariance is reused for each ~50% half, which
under-estimates sigma_Delta by roughly sqrt(2); both raw and sqrt(2)-
corrected Delta/sigma are tabulated.

Emitted at p = 1.0 (the LRG default, matching this channel's headline) and
at p = 1.6 (so the table is directly comparable with v5's QSO table).
"""
import json
import os
import sys
import time

import numpy as np

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction"
sys.path.insert(0, HERE)
sys.path.insert(0, f"{HERE}/lrg_channel_2026_09_22")

import lrg_fit_core as core
import lrg_official_io as lio
from fit_lrg_headline import cosmo_at

OUT = f"{HERE}/lrg_channel_2026_09_22/outputs"
PK = f"{OUT}/pk"
PROPS = ["EBV", "STARDENS", "GALDEPTH_Z", "WEIGHTSYS", "GALLAT"]
FLAG, WATCH = 2.0, 1.0
KMIN, KMAX = 0.003, 0.08
GRID = np.linspace(-400, 400, 801)      # 1.0 spacing, then parabolic vertex


def combine_caps(zb, prop, half):
    """n_data-weighted NGC+SGC mean -- ../fit_fnl_splits.py convention."""
    parts = {}
    for cap in ("NGC", "SGC"):
        p = f"{PK}/pk_LRG_z{zb}_{cap}_{prop}_{half}.json"
        if not os.path.exists(p):
            return None
        parts[cap] = json.load(open(p))
    n, s = parts["NGC"], parts["SGC"]
    k = np.array(n["k"])
    wN, wS = n["n_data"], s["n_data"]
    comb = {ell: (wN * np.array(n[key]) + wS * np.array(s[key])) / (wN + wS)
            for ell, key in ((0, "p0"), (2, "p2"), (4, "p4"))}
    nmodes = np.array(n["nmodes"]) + np.array(s["nmodes"])
    return k, comb, nmodes, wN + wS


def verdict(dsig):
    a = abs(dsig)
    return ("FLAGS" if a >= FLAG else
            "MARGINAL WATCH ITEM" if a >= WATCH else
            "no detectable sensitivity")


def main():
    zbins = sys.argv[1].split(",") if len(sys.argv) > 1 else list(lio.ZBINS)
    table = {}
    outpath = f"{OUT}/systematics_table_lrg.json"
    if os.path.exists(outpath):
        table = json.load(open(outpath))
    for zb in zbins:
        t0 = time.time()
        W, theory_k, obs_k, obs_kedges = lio.load_window(zb)
        meas = lio.load_measured(zb)
        cov, cov_kedges, cov_kc = lio.load_covariance(zb)
        nmodes = {ell: meas[ell]["nmodes"] for ell in (0, 2, 4)}
        mg = core.ModelGrid(W, theory_k, obs_k, nmodes, cov_kedges)
        kc = np.concatenate([cov_kc[ell] for ell in (0, 2, 4)])
        krange = (kc >= KMIN) & (kc <= KMAX)
        table.setdefault(zb, {})
        for p in (1.0, 1.6):
            a_fn, pl_fn, f_g, _ = cosmo_at(meas["zeff"])
            basis = mg.basis(a_fn, pl_fn, f_g, GRID, p)
            print(f"[basis] z{zb} p={p} in {time.time()-t0:.0f}s", flush=True)
            tp = {}
            for prop in PROPS:
                halves, ok = {}, True
                for half in ("high", "low"):
                    c = combine_caps(zb, prop, half)
                    if c is None:
                        ok = False
                        break
                    k, comb, nm, ntot = c
                    dvec = np.concatenate([
                        core.rebin(k, comb[ell], nm, cov_kedges[ell])
                        for ell in (0, 2, 4)])
                    mask = np.isfinite(dvec) & krange
                    cinv = np.linalg.inv(cov[np.ix_(mask, mask)])
                    chi2, b1s = core.profile_from_basis(basis, dvec, cinv, mask)
                    best, lo, hi, sig = core.interval(GRID, chi2)
                    i = int(np.argmin(chi2))
                    halves[half] = dict(f_nl=best, sigma=sig, b1=float(b1s[i]),
                                        chi2=float(chi2[i]),
                                        n_bins=int(mask.sum()),
                                        chi2_per_dof=float(chi2[i] / (mask.sum() - 2)),
                                        n_data=int(ntot))
                if not ok:
                    tp[prop] = {"status": "NOT RUN -- P(k) measurement missing"}
                    print(f"z{zb} p={p} {prop}: NOT RUN", flush=True)
                    continue
                dh, dl = halves["high"]["f_nl"], halves["low"]["f_nl"]
                sh, sl = halves["high"]["sigma"], halves["low"]["sigma"]
                delta = dh - dl
                sd = float(np.sqrt(sh ** 2 + sl ** 2))
                raw = delta / sd if sd > 0 else None
                corr = raw / np.sqrt(2.0) if raw is not None else None
                tp[prop] = dict(high=halves["high"], low=halves["low"],
                                delta_fnl=delta, sigma_delta=sd,
                                delta_over_sigma=raw,
                                delta_over_sigma_sqrt2corrected=corr,
                                verdict=verdict(corr) if corr is not None else None)
                print(f"z{zb} p={p} {prop}: high={dh:+.2f}+/-{sh:.2f} "
                      f"low={dl:+.2f}+/-{sl:.2f} d={delta:+.2f} sd={sd:.2f} "
                      f"raw={raw:+.2f} corr={corr:+.2f} -> {tp[prop]['verdict']}",
                      flush=True)
            table[zb][str(p)] = tp
            json.dump(table, open(outpath, "w"), indent=2)
        del W, basis, mg
    print("DONE")


if __name__ == "__main__":
    main()
