#!/usr/bin/env python3
"""Regression: the LRG channel's fast exact profile core must reproduce v5's
PUBLISHED QSO headline numbers (LEDGER4_RESULT_v5 section 4 /
outputs/fnl_official_nshot0_summary.json) when fed the same official QSO
products. If this does not match, no LRG number is reported.
"""
import json
import sys

import numpy as np

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction"
sys.path.insert(0, HERE)
sys.path.insert(0, f"{HERE}/lrg_channel_2026_09_22")

import official_window_io as oio
from fit_fnl_v2 import get_cosmo_funcs
import lrg_fit_core as core

EXPECT = json.load(open(f"{HERE}/outputs/fnl_official_nshot0_summary.json"))


def build():
    W, theory_k, obs_k, obs_kedges = oio.load_window("GCcomb")
    meas = oio.load_measured("GCcomb")
    cov, cov_kedges, cov_kc = oio.load_covariance()
    nmodes = {ell: meas[ell]["nmodes"] for ell in (0, 2, 4)}
    dvec = np.concatenate([
        core.rebin(meas[ell]["k"], meas[ell]["value"], meas[ell]["nmodes"],
                   cov_kedges[ell]) for ell in (0, 2, 4)])
    return core.Binned(W, theory_k, obs_k, nmodes, cov, cov_kedges, cov_kc, dvec)


def main():
    alpha_fn, plin_fn, f_g, d_g = get_cosmo_funcs("camb")
    b = build()
    q = core.verify_quadratic(b.theory_k, alpha_fn, plin_fn, f_g, 1.6)
    print(f"quadratic-vs-direct max rel diff = {q:.3e}")
    assert q < 1e-9, q  # float64 roundoff only; see verify_quadratic docstring
    print(f"n_data_bins = {b.n_bins} (v5: 48; n_dof = 46)")
    out = {}
    for p, key in ((1.6, "p16"), (1.0, "p10")):
        grid = np.linspace(-150, 150, 601)
        c, _ = b.profile(alpha_fn, plin_fn, f_g, grid, p)
        g2, c2, b2 = core.refine(grid, c, alpha_fn, plin_fn, f_g, b, p, npts=801)
        best, lo, hi, sig = core.interval(g2, c2)
        i = int(np.argmin(c2))
        got = dict(f_nl=best, sigma=sig, b1=float(b2[i]), chi2=float(c2[i]),
                   n_bins=b.n_bins)
        exp = EXPECT[key]
        print(f"p={p}: f_NL {got['f_nl']:+.4f} (v5 {exp['f_nl']:+.4f})  "
              f"sigma {got['sigma']:.4f} (v5 {exp['sigma_fnl']:.4f})  "
              f"b1 {got['b1']:.5f} (v5 {exp['b1']:.5f})  "
              f"chi2 {got['chi2']:.4f} (v5 {exp['chi2']:.4f})")
        # tolerances: v5 located its minimum with a 121-point Nelder-Mead
        # scan, this core with a fine grid + parabolic vertex; agreement is
        # required to be far inside the measurement's own sigma
        assert abs(got["f_nl"] - exp["f_nl"]) < 0.02 * exp["sigma_fnl"], (got, exp)
        assert abs(got["sigma"] - exp["sigma_fnl"]) < 0.02 * exp["sigma_fnl"], (got, exp)
        assert abs(got["b1"] - exp["b1"]) < 1e-3, (got, exp)
        assert abs(got["chi2"] - exp["chi2"]) < 0.05, (got, exp)
        got["delta_f_nl_vs_v5"] = got["f_nl"] - exp["f_nl"]
        got["delta_f_nl_in_v5_sigma"] = (got["f_nl"] - exp["f_nl"]) / exp["sigma_fnl"]
        got["sigma_ratio_vs_v5"] = got["sigma"] / exp["sigma_fnl"]
        out[key] = dict(got=got, v5=exp)
    out["quadratic_max_rel_diff"] = q
    json.dump(out, open(f"{HERE}/lrg_channel_2026_09_22/outputs/regress_qso.json", "w"),
              indent=2)
    print("REGRESSION PASS -- core reproduces the v5 QSO headline")


if __name__ == "__main__":
    main()
