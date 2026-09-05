#!/usr/bin/env python3
"""Ledger row 4 v4, item (2) step C: fit f_NL (p=1.6, b1 free, n_shot=0
fixed per v3's degeneracy finding) for each imaging-systematics
high/low split, against the OFFICIAL DESI window matrix + OFFICIAL EZmock
covariance (fit_fnl_official.py machinery) -- v3 fidelity, not the ad-hoc
diagonal-sigma method used for the v2 galactic-latitude/WEIGHT_SYS splits.
Approximation, disclosed: the official window+covariance were built for
the FULL QSO GCcomb sample; applying them to a ~50%-of-sample split is an
approximation (no split-specific window/covariance exists), same caveat
class as v2's splits. Combines NGC+SGC per split via n_data-weighted mean
(combine_and_compare.py convention) before rebinning to the covariance's
coarse grid.
"""
import json
import numpy as np
from scipy.optimize import minimize
import sys
sys.path.insert(0, "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction")
from fit_fnl_v2 import get_cosmo_funcs, DELTA_C, B1_PUBLISHED
import official_window_io as oio

OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
KMIN, KMAX = 0.003, 0.08
P_VAL = 1.6


def combine_caps(prop, half):
    with open(f"{OUT}/pk_split_NGC_{prop}_{half}.json") as f:
        n = json.load(f)
    with open(f"{OUT}/pk_split_SGC_{prop}_{half}.json") as f:
        s = json.load(f)
    k = np.array(n["k"])
    wN, wS = n["n_data"], s["n_data"]
    out = {}
    for ell, key in ((0, "p0"), (2, "p2"), (4, "p4")):
        pn, ps = np.array(n[key]), np.array(s[key])
        out[ell] = (wN * pn + wS * ps) / (wN + wS)
    nmodes_n, nmodes_s = np.array(n["nmodes"]), np.array(s["nmodes"])
    out_nmodes = nmodes_n + nmodes_s  # combined fine-grid mode count for rebin weighting
    return k, out, out_nmodes, wN + wS


def model_obs_vec(params, alpha_fn, plin_fn, f_zeff, p, W, theory_k):
    b1, fnl = params
    tvecs = []
    for ell in (0, 2, 4):
        kk = theory_k[ell]
        db = 3.0 * fnl * DELTA_C * (b1 - p) / alpha_fn(kk)
        b = b1 + db
        pl = plin_fn(kk)
        if ell == 0:
            v = (b ** 2 + (2.0 / 3.0) * b * f_zeff + f_zeff ** 2 / 5.0) * pl
        elif ell == 2:
            v = (4.0 / 3.0) * b * f_zeff * pl + (4.0 / 7.0) * f_zeff ** 2 * pl
        else:
            v = (8.0 / 35.0) * f_zeff ** 2 * pl
        tvecs.append(v)
    return W @ np.concatenate(tvecs)


def fit_split(prop, half, alpha_fn, plin_fn, f_zeff):
    k, comb, nmodes, ntot = combine_caps(prop, half)
    W_g, theory_k, obs_k, obs_kedges = oio.load_window("GCcomb")
    cov, cov_kedges, cov_kc = oio.load_covariance()
    obs_lens = [len(obs_k[ell]) for ell in (0, 2, 4)]

    # data vector: rebin measured split P_ell (fine k, our own pypower grid)
    # onto the covariance coarse grid, using this split's own nmodes as weight
    data_c = {}
    for ell in (0, 2, 4):
        data_c[ell] = oio.rebin_to_coarse(k, comb[ell], nmodes, cov_kedges[ell])
    dvec = np.concatenate([data_c[0], data_c[2], data_c[4]])
    kc = np.concatenate([cov_kc[0], cov_kc[2], cov_kc[4]])
    mask = np.isfinite(dvec) & (kc >= KMIN) & (kc <= KMAX)
    cinv = np.linalg.inv(cov[np.ix_(mask, mask)])

    def full_model(params):
        mvec = model_obs_vec(params, alpha_fn, plin_fn, f_zeff, P_VAL, W_g, theory_k)
        out = {}
        i0 = 0
        for ell, n in zip((0, 2, 4), obs_lens):
            fine = mvec[i0:i0 + n]
            out[ell] = oio.rebin_to_coarse(obs_k[ell], fine, oio.load_measured("GCcomb")[ell]["nmodes"], cov_kedges[ell])
            i0 += n
        return np.concatenate([out[0], out[2], out[4]])

    def negll(params):
        if params[0] < 0.5 or params[0] > 5:
            return 1e10
        r = (full_model(params) - dvec)[mask]
        return 0.5 * r @ cinv @ r

    res = minimize(negll, [B1_PUBLISHED, -5.0], method="Nelder-Mead",
                    options={"xatol": 1e-3, "fatol": 1e-3, "maxiter": 3000})
    # profile-likelihood sigma on f_NL (1D scan, same technique as v3's headline)
    best = res.fun
    fnl0 = res.x[1]
    grid = fnl0 + np.linspace(-60, 60, 121)
    dchi2 = []
    for fv in grid:
        def negll_fixed(b1v):
            return negll([b1v[0], fv])
        r2 = minimize(negll_fixed, [res.x[0]], method="Nelder-Mead")
        dchi2.append(2 * (r2.fun - best))
    dchi2 = np.array(dchi2)
    lo = np.interp(1.0, dchi2[grid <= fnl0][::-1], grid[grid <= fnl0][::-1]) if np.any(dchi2[grid <= fnl0] > 1) else grid[0]
    hi = np.interp(1.0, dchi2[grid >= fnl0], grid[grid >= fnl0]) if np.any(dchi2[grid >= fnl0] > 1) else grid[-1]
    sigma = (hi - lo) / 2.0
    return dict(b1=float(res.x[0]), f_nl=float(fnl0), sigma_fnl=float(sigma),
                chi2=float(best * 2), n_dof=int(mask.sum()), n_data=int(ntot),
                success=bool(res.success))


if __name__ == "__main__":
    alpha_fn, plin_fn, f_zeff, d_zeff = get_cosmo_funcs("camb")
    props = ["EBV", "STARDENS", "GALDEPTH_Z"]
    results = {}
    for prop in props:
        results[prop] = {}
        for half in ("high", "low"):
            r = fit_split(prop, half, alpha_fn, plin_fn, f_zeff)
            results[prop][half] = r
            print(prop, half, r)
        dh, dl = results[prop]["high"]["f_nl"], results[prop]["low"]["f_nl"]
        sh, sl = results[prop]["high"]["sigma_fnl"], results[prop]["low"]["sigma_fnl"]
        delta = dh - dl
        sigma_delta = float(np.sqrt(sh ** 2 + sl ** 2))
        results[prop]["delta_fnl"] = delta
        results[prop]["sigma_delta"] = sigma_delta
        results[prop]["delta_over_sigma"] = delta / sigma_delta if sigma_delta > 0 else None
    with open(f"{OUT}/imaging_splits_fnl_v4.json", "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
