#!/usr/bin/env python3
"""Ledger row 4 LRG channel HEADLINE fit -- exactly as pre-registered
(PRE_REGISTRATION.md sections 2-3, committed 2026-09-22 before any statistic).

Official DESI DR1 LRG window matrix + measured P_ell + EZmock covariance,
all three z-bins, streamed by HTTP range read (nothing on disk). n_shot
fixed = 0, b1 free, KMIN/KMAX = 0.003/0.08, ells 0/2/4, profile-likelihood
Delta chi2 = 1. p = 1.0 headline (LRG default), p = 1.6 alternate,
p-marginalised midpoint -- the same three-row presentation v3/v5 used for QSO.
"""
import json
import sys
import time

import numpy as np

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction"
sys.path.insert(0, HERE)
sys.path.insert(0, f"{HERE}/lrg_channel_2026_09_22")

import fit_fnl_v2
import lrg_fit_core as core
import lrg_official_io as lio
import http_stream as hs

OUT = f"{HERE}/lrg_channel_2026_09_22/outputs"
QSO_ZEFF = 1.491


def cosmo_at(z_eff):
    """The SAME fit_fnl_v2.get_cosmo_funcs (it reads module-level Z_EFF at
    call time), evaluated at z_eff -- not a re-implementation."""
    saved = fit_fnl_v2.Z_EFF
    try:
        fit_fnl_v2.Z_EFF = z_eff
        return fit_fnl_v2.get_cosmo_funcs("camb")
    finally:
        fit_fnl_v2.Z_EFF = saved


def assert_same_code_path():
    a0, p0, f0, d0 = fit_fnl_v2.get_cosmo_funcs("camb")
    a1, p1, f1, d1 = cosmo_at(QSO_ZEFF)
    k = np.logspace(-3.5, -0.8, 64)
    assert np.array_equal(a0(k), a1(k))
    assert np.array_equal(p0(k), p1(k))
    assert f0 == f1 and d0 == d1
    assert fit_fnl_v2.Z_EFF == QSO_ZEFF
    return dict(check="z_eff parameterisation is the same code path as the QSO fits",
                at_z_eff=QSO_ZEFF, alpha_bitwise_equal=True,
                plin_bitwise_equal=True, f_zeff=float(f0), D_zeff=float(d0))


def build(zbin):
    W, theory_k, obs_k, obs_kedges = lio.load_window(zbin)
    meas = lio.load_measured(zbin)
    cov, cov_kedges, cov_kc = lio.load_covariance(zbin)
    nmodes = {ell: meas[ell]["nmodes"] for ell in (0, 2, 4)}
    dvec = np.concatenate([
        core.rebin(meas[ell]["k"], meas[ell]["value"], meas[ell]["nmodes"],
                   cov_kedges[ell]) for ell in (0, 2, 4)])
    b = core.Binned(W, theory_k, obs_k, nmodes, cov, cov_kedges, cov_kc, dvec)
    return b, meas["zeff"]


def main():
    t0 = time.time()
    check = assert_same_code_path()
    bins, zeffs = {}, {}
    for zb in lio.ZBINS:
        bins[zb], zeffs[zb] = build(zb)
        print(f"[stream] LRG z{zb} zeff={zeffs[zb]:.5f} n_bins={bins[zb].n_bins} "
              f"cum {hs.BYTES_STREAMED['n']/1e6:.0f} MB", flush=True)

    res = {"code_path_check": check, "zeff": zeffs, "p": {}}
    grid = np.linspace(-400, 400, 1601)
    for p in (1.0, 1.6):
        pres = {"bins": {}}
        total = None
        for zb in lio.ZBINS:
            b = bins[zb]
            a_fn, pl_fn, f_g, d_g = cosmo_at(zeffs[zb])
            if p == 1.0 and zb == lio.ZBINS[0]:
                res["quadratic_max_rel_diff"] = core.verify_quadratic(
                    b.theory_k, a_fn, pl_fn, f_g, p)
            c, b1 = b.profile(a_fn, pl_fn, f_g, grid, p)
            best, lo, hi, sig = core.interval(grid, c)
            span = max(4 * sig, 8.0)
            g2 = np.linspace(best - span, best + span, 1201)
            c2, b12 = b.profile(a_fn, pl_fn, f_g, g2, p)
            best, lo, hi, sig = core.interval(g2, c2)
            i = int(np.argmin(c2))
            pres["bins"][zb] = dict(
                zeff=zeffs[zb], f_nl=best, lo_68=lo, hi_68=hi, sigma=sig,
                b1=float(b12[i]), b1_over_D=float(b12[i] * d_g),
                chi2_min=float(c2[i]), n_bins=b.n_bins,
                chi2_per_dof=float(c2[i] / (b.n_bins - 2)))
            np.save(f"{OUT}/profile_LRG_p{p}_{zb}.npy", np.vstack([grid, c]))
            total = c if total is None else total + c
            print(f"  p={p} z{zb}: f_NL={best:+.3f} +/- {sig:.3f}  b1={b12[i]:.4f} "
                  f"chi2/dof={c2[i]/(b.n_bins-2):.3f}", flush=True)
        best, lo, hi, sig = core.interval(grid, total)
        # refine the combination on a narrow shared grid
        span = max(4 * sig, 8.0)
        g2 = np.linspace(best - span, best + span, 1201)
        tot2 = None
        for zb in lio.ZBINS:
            a_fn, pl_fn, f_g, _ = cosmo_at(zeffs[zb])
            c2, _ = bins[zb].profile(a_fn, pl_fn, f_g, g2, p)
            tot2 = c2 if tot2 is None else tot2 + c2
        best, lo, hi, sig = core.interval(g2, tot2)
        pres["combined"] = dict(
            f_nl=best, lo_68=lo, hi_68=hi, sigma=sig,
            chi2_min=float(tot2.min()),
            n_bins=sum(bins[zb].n_bins for zb in lio.ZBINS),
            note="three z-bins combined by summing the b1-profiled chi2 curves "
                 "(independent b1 per bin, one shared f_NL). Bins treated as "
                 "independent: no cross-bin official covariance product exists. "
                 "Disclosed approximation, same class as the v4/v5 split "
                 "covariance reuse.")
        np.save(f"{OUT}/profile_LRG_p{p}_combined.npy", np.vstack([g2, tot2]))
        res["p"][str(p)] = pres
        print(f"  p={p} COMBINED: f_NL={best:+.3f} +/- {sig:.3f}", flush=True)

    a, bq = res["p"]["1.0"]["combined"], res["p"]["1.6"]["combined"]
    res["p_marginalised_midpoint"] = dict(
        f_nl=0.5 * (a["f_nl"] + bq["f_nl"]),
        sigma=0.5 * (a["sigma"] + bq["sigma"]),
        note="midpoint of the p=1.0 and p=1.6 results, the same "
             "p-marginalisation presentation v3/v5 used for QSO")
    res["streamed_bytes"] = hs.BYTES_STREAMED["n"]
    res["sha256"] = lio.SHA256
    res["wall_seconds"] = round(time.time() - t0, 1)
    with open(f"{OUT}/fnl_lrg_headline.json", "w") as f:
        json.dump(res, f, indent=2)
    print(json.dumps({k: res["p"][k]["combined"] for k in res["p"]}, indent=2))
    print(f"streamed {res['streamed_bytes']/1e6:.0f} MB, {res['wall_seconds']:.0f}s")


if __name__ == "__main__":
    main()
