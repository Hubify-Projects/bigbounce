#!/usr/bin/env python3
"""Ledger row 4 step 5: fit f_NL (p=1.6 fixed, point-estimate only -- no
full MCMC, for speed) on the WEIGHT_SYS on/off variants from
systest_weight_sys.py, reusing fit_fnl.py's model/covariance machinery.
Reports Delta f_NL = f_NL(sys off) - f_NL(sys on), the plan's headline
systematic (sec 3.4 test 1).
"""
import json
import numpy as np
from scipy.optimize import minimize
import fit_fnl as ff

OUT = ff.OUT

with open(f"{OUT}/systest_weight_sys_pk.json") as f:
    data = json.load(f)


def combined(variant):
    ngc, sgc = data[f"NGC_{variant}"], data[f"SGC_{variant}"]
    k = np.array(ngc["k"])
    good = (k >= 0.003) & (k <= 0.08)
    k = k[good]
    p0 = (ngc["n_data"] * np.array(ngc["p0"])[good] + sgc["n_data"] * np.array(sgc["p0"])[good]) / (ngc["n_data"] + sgc["n_data"])
    p2 = (ngc["n_data"] * np.array(ngc["p2"])[good] + sgc["n_data"] * np.array(sgc["p2"])[good]) / (ngc["n_data"] + sgc["n_data"])
    return k, p0, p2


def point_fit(k, p0, p2, p_fixed=1.6):
    # reuse ff's sigma shape (Nmodes not recomputed here; use ff's NMODES/
    # calibration factor from the main run as a reasonable proxy since
    # binning/mesh are identical) -- point-estimate chi2 minimisation only.
    sig_p0 = ff.SIG_P0
    sig_p2 = ff.SIG_P2

    def chi2(theta):
        f_nl, n_shot = theta
        p0m, p2m = ff.model_p0p2(k, f_nl, p_fixed, n_shot)
        return np.sum((p0 - p0m) ** 2 / sig_p0 ** 2) + np.sum((p2 - p2m) ** 2 / sig_p2 ** 2)

    res = minimize(chi2, x0=[0.0, 0.0], method="Nelder-Mead")
    return res.x[0]


results = {}
for variant in ["sys", "nosys"]:
    k, p0, p2 = combined(variant)
    fnl = point_fit(k, p0, p2, p_fixed=1.6)
    results[variant] = float(fnl)
    print(variant, "f_NL (point est, p=1.6) =", fnl)

results["delta_fnl_sys_off_minus_on"] = results["nosys"] - results["sys"]
print("Delta f_NL (WEIGHT_SYS off - on) =", results["delta_fnl_sys_off_minus_on"])
with open(f"{OUT}/systest_weight_sys_fnl.json", "w") as fh:
    json.dump(results, fh, indent=2)
