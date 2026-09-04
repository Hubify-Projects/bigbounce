#!/usr/bin/env python3
"""Ledger row 4 v2, fix (5): point-estimate f_NL(p=1.6) for the galactic-
latitude and PHOTSYS splits from systest_gal_lat.py, same point-fit pattern
as systest_fit.py. Reports Delta f_NL for each split vs the statistical
sigma from the main fit (fnl_fit_results.json, p=1.6 row).
"""
import json
import numpy as np
from scipy.optimize import minimize
import fit_fnl as ff

OUT = ff.OUT
with open(f"{OUT}/systest_splits_pk.json") as f:
    data = json.load(f)
with open(f"{OUT}/fnl_fit_results.json") as f:
    main_sigma = json.load(f)["p1.6_QSO_merger"]["f_nl_sigma_approx"]


def combined(pair):
    ngc, sgc = data.get(f"NGC_{pair}"), data.get(f"SGC_{pair}")
    if ngc is None or sgc is None:
        return None
    k = np.array(ngc["k"])
    good = (k >= 0.003) & (k <= 0.08)
    k = k[good]
    p0 = (ngc["n_data"] * np.array(ngc["p0"])[good] + sgc["n_data"] * np.array(sgc["p0"])[good]) / (ngc["n_data"] + sgc["n_data"])
    p2 = (ngc["n_data"] * np.array(ngc["p2"])[good] + sgc["n_data"] * np.array(sgc["p2"])[good]) / (ngc["n_data"] + sgc["n_data"])
    return k, p0, p2


def point_fit(k, p0, p2, p_fixed=1.6):
    sig_p0, sig_p2 = ff.SIG_P0, ff.SIG_P2

    def chi2(theta):
        f_nl, n_shot = theta
        p0m, p2m = ff.model_p0p2(k, f_nl, p_fixed, n_shot)
        return np.sum((p0 - p0m) ** 2 / sig_p0 ** 2) + np.sum((p2 - p2m) ** 2 / sig_p2 ** 2)

    res = minimize(chi2, x0=[0.0, 0.0], method="Nelder-Mead")
    return res.x[0]


results = {"main_fit_sigma_p1.6": main_sigma}
pairs = [("gallat_high", "gallat_low"), ("photsys_N", "photsys_S")]
for a, b in pairs:
    ca, cb = combined(a), combined(b)
    if ca is None or cb is None:
        results[f"{a}_vs_{b}"] = "MISSING"
        continue
    fa, fb = point_fit(*ca), point_fit(*cb)
    results[a] = float(fa)
    results[b] = float(fb)
    results[f"delta_{a}_vs_{b}"] = float(fa - fb)
    print(a, fa, b, fb, "delta=", fa - fb)

with open(f"{OUT}/systest_splits_fnl.json", "w") as fh:
    json.dump(results, fh, indent=2)
print("SAVED systest_splits_fnl.json")
