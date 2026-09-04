#!/usr/bin/env python3
"""Ledger row 4 v3: joint (b1, f_NL, n_shot) fit against the OFFICIAL DESI
DR1 QSO GCcomb window matrix + measured P_ell + EZmock covariance (real
published products; see official_window_io.py). Removes v1/v2's window,
randoms-density, and covariance causes at once by using the real DESI
pipeline outputs instead of a homebrew reconstruction. CLI: --p {1.6,1.0}
--point (fast scipy) or default emcee.
"""
import argparse
import json
import numpy as np
from scipy.optimize import minimize
import emcee

import sys
sys.path.insert(0, "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction")
from fit_fnl_v2 import get_cosmo_funcs, DELTA_C, B1_PUBLISHED
import official_window_io as oio

OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
KMAX = 0.08
KMIN = 0.003


def build(alpha_fn, plin_fn, f_zeff, cap):
    W, theory_k, obs_k, obs_kedges = oio.load_window(cap)
    meas = oio.load_measured(cap)
    return W, theory_k, obs_k, meas


def model_obs_vec(params, alpha_fn, plin_fn, f_zeff, p, W, theory_k):
    b1, fnl, n_shot = params
    tvecs = []
    for ell in (0, 2, 4):
        k = theory_k[ell]
        db = 3.0 * fnl * DELTA_C * (b1 - p) / alpha_fn(k)
        b = b1 + db
        pl = plin_fn(k)
        if ell == 0:
            v = (b ** 2 + (2.0 / 3.0) * b * f_zeff + f_zeff ** 2 / 5.0) * pl + n_shot
        elif ell == 2:
            v = (4.0 / 3.0) * b * f_zeff * pl + (4.0 / 7.0) * f_zeff ** 2 * pl
        else:
            v = (8.0 / 35.0) * f_zeff ** 2 * pl
        tvecs.append(v)
    tvec = np.concatenate(tvecs)
    mvec = W @ tvec
    n0 = len(theory_k[0])
    # split back using OBSERVABLE lengths (rows of W partitioned 0,2,4)
    return mvec


def get_data_and_model_coarse(cap_list, alpha_fn, plin_fn, f_zeff, p):
    cov, cov_kedges, cov_kc = oio.load_covariance()
    data_c, model_fn_list, weight = {}, [], None
    # Combine caps (NGC+SGC) inverse-nmodes-weighted at fine grid before rebin,
    # matching v1/v2's approach; official GCcomb file already exists too.
    W_g, theory_k, obs_k, meas_g = build(alpha_fn, plin_fn, f_zeff, "GCcomb")
    obs_lens = [len(obs_k[ell]) for ell in (0, 2, 4)]

    def full_model(params):
        mvec = model_obs_vec(params, alpha_fn, plin_fn, f_zeff, p, W_g, theory_k)
        out = {}
        i0 = 0
        for ell, n in zip((0, 2, 4), obs_lens):
            fine = mvec[i0:i0 + n]
            out[ell] = oio.rebin_to_coarse(obs_k[ell], fine, meas_g[ell]["nmodes"], cov_kedges[ell])
            i0 += n
        return np.concatenate([out[0], out[2], out[4]])

    data_coarse = {}
    for ell in (0, 2, 4):
        data_coarse[ell] = oio.rebin_to_coarse(
            meas_g[ell]["k"], meas_g[ell]["value"], meas_g[ell]["nmodes"], cov_kedges[ell]
        )
    dvec = np.concatenate([data_coarse[0], data_coarse[2], data_coarse[4]])
    kc = np.concatenate([cov_kc[0], cov_kc[2], cov_kc[4]])
    mask = np.isfinite(dvec) & (kc >= KMIN) & (kc <= KMAX)
    return dvec, cov, mask, full_model, kc


def neg_log_like(params, dvec, cinv, mask, full_model):
    if params[0] < 0.5 or params[0] > 5 or params[2] < -5e4 or params[2] > 5e4:
        return 1e10
    mvec = full_model(params)
    r = (mvec - dvec)[mask]
    return 0.5 * r @ cinv @ r


def run(p_val, point_only, tag):
    alpha_fn, plin_fn, f_zeff, d_zeff = get_cosmo_funcs("camb")
    dvec, cov, mask, full_model, kc = get_data_and_model_coarse(None, alpha_fn, plin_fn, f_zeff, p_val)
    cinv_full = np.linalg.inv(cov[np.ix_(mask, mask)])

    def negll(params):
        return neg_log_like(params, dvec, cinv_full, mask, full_model)

    x0 = [B1_PUBLISHED, -5.0, 0.0]
    res = minimize(negll, x0, method="Nelder-Mead",
                    options={"xatol": 1e-3, "fatol": 1e-3, "maxiter": 4000})
    point = dict(b1=res.x[0], f_nl=res.x[1], n_shot=res.x[2], nll=res.fun,
                 n_data_bins=int(mask.sum()), success=bool(res.success))
    result = {"p": p_val, "point": point}

    if not point_only:
        ndim, nwalk = 3, 24
        p0 = res.x + 1e-3 * np.abs(res.x + 1e-6) * np.random.randn(nwalk, ndim)

        def log_prob(params):
            return -negll(params)

        sampler = emcee.EnsembleSampler(nwalk, ndim, log_prob)
        sampler.run_mcmc(p0, 1500, progress=False)
        chain = sampler.get_chain(discard=400, flat=True)
        fnl_chain = chain[:, 1]
        result["mcmc"] = dict(
            f_nl_median=float(np.median(fnl_chain)),
            f_nl_lo=float(np.percentile(fnl_chain, 16)),
            f_nl_hi=float(np.percentile(fnl_chain, 84)),
            b1_median=float(np.median(chain[:, 0])),
            n_shot_median=float(np.median(chain[:, 2])),
            n_samples=len(fnl_chain),
        )
        np.save(f"{OUT}/fnl_official_chain_{tag}.npy", chain)

    with open(f"{OUT}/fnl_official_{tag}.json", "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=float, required=True)
    ap.add_argument("--point", action="store_true")
    ap.add_argument("--tag", required=True)
    a = ap.parse_args()
    run(a.p, a.point, a.tag)
