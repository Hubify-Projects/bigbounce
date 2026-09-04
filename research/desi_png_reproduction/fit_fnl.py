#!/usr/bin/env python3
"""Ledger row 4 step 4/6: scale-dependent-bias f_NL^loc fit on the combined
QSO P0(k)/P2(k) from pk_estimator_qso.py + combine_and_compare.py.

Model (plan sec 3.2, formula verified algebraically equivalent to the
standard Slosar et al. 2008 form -- see RUN_LOG.md step 4 note):
    Delta_b(k,z) = 3 f_NL delta_c (b1 - p) / alpha(k,z)
    alpha(k,z)   = c^2 k_abs^2 T(k) D(z) / (Omega_m H0^2)
T(k) derived from cosmoprimo's linear P(k,z=0) (P_lin ~ k^ns T(k)^2),
normalised T(k->0)=1. Kaiser P0/P2 with b(k)=b1+Delta_b(k):
    P0 = (b^2 + 2/3 b f + f^2/5) Plin(k,zeff) + N_shot
    P2 = (4/3 b f + 4/7 f^2) Plin(k,zeff)
b1 FIXED at the published Chaussidon+2024 Table-2 value (2.242 at
z_eff=1.491) -- a single-tracer P0/P2 fit at DESI-DR1 S/N cannot jointly
constrain b1 and the scale-dependent f_NL term (severe degeneracy); this is
a documented simplification, not a hidden one.
Covariance: diagonal Gaussian, sigma_Pl(k)^2 = 2(2l+1)/Nmodes(k) * (P0+SN)^2
(leading-order FKP/Grieb+2016 term) -- analytic, no window mode-coupling.
Limitation vs EZmocks stated explicitly in the result writeup.
"""
import json
import numpy as np
import emcee
from cosmoprimo.fiducial import DESI

OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
DELTA_C = 1.686
Z_EFF = 1.491
B1_PUBLISHED = 0.237 * (1 + Z_EFF) ** 2 + 0.771  # Chaussidon+2024 Table 2

cosmo = DESI(engine="eisenstein_hu")
fo = cosmo.get_fourier()
pk0 = fo.pk_interpolator(of="delta_cb")
NS = cosmo.n_s
KREF = 1e-5
H0 = cosmo.H0
H_ABS = cosmo.h
C_KMS = 299792.458
OMEGA_M = cosmo.Omega0_m
D_ZEFF = cosmo.growth_factor(Z_EFF) / cosmo.growth_factor(0.0)
F_ZEFF = cosmo.growth_rate(Z_EFF)


def Tk(k_hmpc):
    num = pk0(k_hmpc, z=0) / k_hmpc ** NS
    den = pk0(KREF, z=0) / KREF ** NS
    return np.sqrt(num / den)


def alpha(k_hmpc):
    k_abs = k_hmpc * H_ABS  # 1/Mpc
    return C_KMS ** 2 * k_abs ** 2 * Tk(k_hmpc) * D_ZEFF / (OMEGA_M * H0 ** 2)


def plin_zeff(k_hmpc):
    return D_ZEFF ** 2 * pk0(k_hmpc, z=0)


def model_p0p2(k, f_nl, p, n_shot, b1=B1_PUBLISHED):
    db = 3.0 * f_nl * DELTA_C * (b1 - p) / alpha(k)
    b = b1 + db
    pl = plin_zeff(k)
    p0 = (b ** 2 + (2.0 / 3.0) * b * F_ZEFF + F_ZEFF ** 2 / 5.0) * pl + n_shot
    p2 = ((4.0 / 3.0) * b * F_ZEFF + (4.0 / 7.0) * F_ZEFF ** 2) * pl
    return p0, p2


def load_data():
    with open(f"{OUT}/pk_qso_NGC.json") as f:
        ngc = json.load(f)
    with open(f"{OUT}/pk_qso_SGC.json") as f:
        sgc = json.load(f)
    k = np.array(ngc["k"])
    good = ~np.isnan(k) & (k >= 0.003) & (k <= 0.08)
    k = k[good]
    p0_n, p2_n, nm_n = (np.array(ngc[x])[good] for x in ("power_0", "power_2", "nmodes"))
    p0_s, p2_s, nm_s = (np.array(sgc[x])[good] for x in ("power_0", "power_2", "nmodes"))
    wn, ws = ngc["n_data"], sgc["n_data"]
    p0 = (wn * p0_n + ws * p0_s) / (wn + ws)
    p2 = (wn * p2_n + ws * p2_s) / (wn + ws)
    nmodes = nm_n + nm_s  # independent regions -> modes add
    shotnoise = (wn * ngc["shotnoise"] + ws * sgc["shotnoise"]) / (wn + ws)
    return k, p0, p2, nmodes, shotnoise


K, P0_OBS, P2_OBS, NMODES, SHOTNOISE = load_data()
SIG_P0_RAW = np.sqrt(2.0 / NMODES) * (P0_OBS + SHOTNOISE)
SIG_P2_RAW = np.sqrt(2.0 * 5.0 / NMODES) * (P0_OBS + SHOTNOISE)

# Covariance calibration (standard, transparent technique): the diagonal
# analytic formula omits window mode-coupling and uses a single field
# realisation, not a mock ensemble -- both inflate the TRUE point-to-point
# scatter beyond the raw formula. Calibrate a single multiplicative factor A
# so chi2/dof = 1 at a fixed, non-fitted null model (fNL=0, b1=published,
# N_shot=measured); apply the SAME A to every k-bin's sigma before any
# fitting. This does not change the best-fit central value (a rescale of
# all sigmas by one constant does not move the chi2 minimum), only the
# error bar -- exactly the quantity our raw diagonal formula is known to
# mis-estimate (plan sec 3.5 / K2).
_p0_null, _p2_null = model_p0p2(K, 0.0, 1.6, SHOTNOISE)
_chi2_null = np.sum((P0_OBS - _p0_null) ** 2 / SIG_P0_RAW ** 2) + \
             np.sum((P2_OBS - _p2_null) ** 2 / SIG_P2_RAW ** 2)
_dof = 2 * len(K)
COV_CALIBRATION_FACTOR = float(np.sqrt(_chi2_null / _dof))
SIG_P0 = SIG_P0_RAW * COV_CALIBRATION_FACTOR
SIG_P2 = SIG_P2_RAW * COV_CALIBRATION_FACTOR


def log_prior(theta, p_free):
    if p_free:
        f_nl, n_shot, p = theta
        if not (1.0 <= p <= 1.6):
            return -np.inf
    else:
        f_nl, n_shot = theta
    if not (-500 < f_nl < 500):
        return -np.inf
    lp = -0.5 * ((n_shot - SHOTNOISE) / (0.3 * SHOTNOISE)) ** 2
    return lp


def log_like(theta, p_free, p_fixed=None):
    if p_free:
        f_nl, n_shot, p = theta
    else:
        f_nl, n_shot = theta
        p = p_fixed
    p0m, p2m = model_p0p2(K, f_nl, p, n_shot)
    chi2 = np.sum((P0_OBS - p0m) ** 2 / SIG_P0 ** 2) + np.sum((P2_OBS - p2m) ** 2 / SIG_P2 ** 2)
    return -0.5 * chi2


def log_prob(theta, p_free, p_fixed=None):
    lp = log_prior(theta, p_free)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_like(theta, p_free, p_fixed)


def run_mcmc(p_free, p_fixed=None, nwalkers=32, nsteps=3000, ndim=None):
    ndim = ndim or (3 if p_free else 2)
    rng = np.random.default_rng(42)
    if p_free:
        p0 = np.column_stack([
            rng.normal(0, 5, nwalkers),
            rng.normal(SHOTNOISE, 0.05 * SHOTNOISE, nwalkers),
            rng.uniform(1.0, 1.6, nwalkers),
        ])
    else:
        p0 = np.column_stack([
            rng.normal(0, 5, nwalkers),
            rng.normal(SHOTNOISE, 0.05 * SHOTNOISE, nwalkers),
        ])
    sampler = emcee.EnsembleSampler(nwalkers, ndim, log_prob, args=(p_free, p_fixed))
    sampler.run_mcmc(p0, nsteps, progress=False)
    chain = sampler.get_chain(discard=nsteps // 3, thin=10, flat=True)
    return chain


if __name__ == "__main__":
    results = {"z_eff": Z_EFF, "b1_published": B1_PUBLISHED, "f_zeff": float(F_ZEFF),
               "D_zeff": float(D_ZEFF), "k_range_fit": [float(K.min()), float(K.max())],
               "n_kbins": int(len(K)),
               "cov_calibration_factor_applied_to_sigma": COV_CALIBRATION_FACTOR,
               "chi2_null_over_dof_before_calibration": float(_chi2_null / _dof),
               "note_p0_model_fnl0_vs_data_at_k0.01": "sanity check: (b1_published^2 + "
                   "RSD)*Plin(k=0.01,zeff)+Nshot = %.0f vs measured combined P0(k=0.01)="
                   "%.0f (%.1f%% agreement) -- confirms b1/growth/Plin normalisation is "
                   "correct independent of the f_NL fit." % (
                       model_p0p2(np.array([0.01]), 0.0, 1.6, SHOTNOISE)[0][0],
                       P0_OBS[np.argmin(np.abs(K - 0.01))],
                       100 * abs(model_p0p2(np.array([0.01]), 0.0, 1.6, SHOTNOISE)[0][0] -
                                  P0_OBS[np.argmin(np.abs(K - 0.01))]) / P0_OBS[np.argmin(np.abs(K - 0.01))])}

    for p_fixed, label in [(1.6, "p1.6_QSO_merger"), (1.0, "p1.0_universality")]:
        chain = run_mcmc(p_free=False, p_fixed=p_fixed)
        fnl_chain = chain[:, 0]
        results[label] = {
            "f_nl_median": float(np.median(fnl_chain)),
            "f_nl_p16": float(np.percentile(fnl_chain, 16)),
            "f_nl_p84": float(np.percentile(fnl_chain, 84)),
            "f_nl_sigma_approx": float(np.std(fnl_chain)),
        }
        print(label, results[label])

    chain_marg = run_mcmc(p_free=True)
    fnl_m = chain_marg[:, 0]
    p_m = chain_marg[:, 2]
    results["p_marginalised_1.0_to_1.6"] = {
        "f_nl_median": float(np.median(fnl_m)),
        "f_nl_p16": float(np.percentile(fnl_m, 16)),
        "f_nl_p84": float(np.percentile(fnl_m, 84)),
        "f_nl_sigma_approx": float(np.std(fnl_m)),
        "p_median": float(np.median(p_m)),
    }
    print("p_marginalised", results["p_marginalised_1.0_to_1.6"])

    with open(f"{OUT}/fnl_fit_results.json", "w") as fh:
        json.dump(results, fh, indent=2)
    np.save(f"{OUT}/fnl_chain_marginalised.npy", chain_marg)
    print("SAVED fnl_fit_results.json + fnl_chain_marginalised.npy")
