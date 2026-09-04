#!/usr/bin/env python3
"""Ledger row 4 v2, fix (5): point-estimate f_NL(p=1.6) for the NGC-only
galactic-latitude split (systest_gal_lat_fast.py, reduced scope: NGC cap
only, nmesh=256 vs the headline 512, after the full NGC+SGC/nmesh=512
version repeatedly failed to complete under host contention -- see
RUN_LOG.md). Self-consistent differential test: same model/covariance
recipe for both halves, EH transfer (matches v1's systematics baseline),
no window-IC (systematics test isolates the imaging/geometry lever, not
compounded with the window fix). Delta_fNL is the informative quantity;
absolute NGC-only values are not the headline constraint.
"""
import json
import numpy as np
from scipy.optimize import minimize
from cosmoprimo.fiducial import DESI

OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
DELTA_C, Z_EFF = 1.686, 1.491
B1 = 0.237 * (1 + Z_EFF) ** 2 + 0.771
cosmo = DESI(engine="eisenstein_hu")
fo = cosmo.get_fourier()
pk0 = fo.pk_interpolator(of="delta_cb")
NS, KREF, H_ABS, C_KMS = cosmo.n_s, 1e-5, cosmo.h, 299792.458
H0, OM = cosmo.H0, cosmo.Omega0_m
D_ZEFF = cosmo.growth_factor(Z_EFF) / cosmo.growth_factor(0.0)
F_ZEFF = cosmo.growth_rate(Z_EFF)


def Tk(k):
    return np.sqrt((pk0(k, z=0) / k ** NS) / (pk0(KREF, z=0) / KREF ** NS))


def alpha(k):
    return C_KMS ** 2 * (k * H_ABS) ** 2 * Tk(k) * D_ZEFF / (OM * H0 ** 2)


def model(k, f_nl, p, n_shot):
    db = 3.0 * f_nl * DELTA_C * (B1 - p) / alpha(k)
    b = B1 + db
    pl = D_ZEFF ** 2 * pk0(k, z=0)
    p0 = (b ** 2 + (2 / 3) * b * F_ZEFF + F_ZEFF ** 2 / 5) * pl + n_shot
    p2 = ((4 / 3) * b * F_ZEFF + (4 / 7) * F_ZEFF ** 2) * pl
    return p0, p2


def fit_one(entry, p_fixed=1.6):
    k = np.array(entry["k"])
    good = (k >= 0.003) & (k <= 0.08)
    k = k[good]
    p0 = np.array(entry["p0"])[good]
    p2 = np.array(entry["p2"])[good]
    sig0 = np.abs(p0) * 0.1 + 1.0  # simple relative+floor sigma (differential test)
    sig2 = np.abs(p2) * 0.15 + 1.0

    def chi2(theta):
        f_nl, n_shot = theta
        m0, m2 = model(k, f_nl, p_fixed, n_shot)
        return np.sum((p0 - m0) ** 2 / sig0 ** 2) + np.sum((p2 - m2) ** 2 / sig2 ** 2)

    res = minimize(chi2, x0=[0.0, 0.0], method="Nelder-Mead")
    return float(res.x[0])


if __name__ == "__main__":
    with open(f"{OUT}/systest_splits_pk.json") as f:
        data = json.load(f)
    fh = fit_one(data["NGC_gallat_high"])
    fl = fit_one(data["NGC_gallat_low"])
    out = {"NGC_gallat_high_fnl": fh, "NGC_gallat_low_fnl": fl,
           "delta_fnl_gallat_high_minus_low": fh - fl}
    print(out)
    with open(f"{OUT}/systest_splits_fnl_v2.json", "w") as fo_:
        json.dump(out, fo_, indent=2)
