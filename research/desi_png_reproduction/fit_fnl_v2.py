#!/usr/bin/env python3
"""Ledger row 4 v2: cumulative re-fit removing v1's causes in order of
impact. CLI flags turn on each fix cumulatively; see RUN_LOG.md follow-up
section for the exact sequence run. Reuses fit_fnl.py's model/MCMC (same
formula, same b1-fixed simplification, same diagonal-covariance-calibration
technique) with three swappable pieces:
  --tk {eh,camb}       EH (v1) vs CAMB (fix 2) transfer function (camb_transfer.py)
  --nran N             randoms realisations used for P0/P2 (fix 3; reads
                        outputs/pk_qso_{cap}_nran{N}.json from a re-run of
                        the generalised pk_estimator_qso.py)
  --window-ic          apply the global integral constraint from
                        window_conv.py's shuffled-randoms window power
                        (fix 1) -- P0_obs(k) = P0_true(k) - W0n(k)*P0_true(k_min)
  --shotnoise-fixed     fix (4): instead of the free residual n_shot nuisance,
                        fix N_shot to the MEASURED shotnoise attribute from
                        pypower directly (poles.shotnoise from the nran run,
                        already the analytic 1/nbar FKP shot noise) with a
                        small residual prior around IT (not around 0) --
                        an "analytic Gaussian covariance ... with the
                        measured shot noise" as the task requests, still no
                        EZmocks/window mode-coupling in the covariance
                        (documented limitation, stated in the writeup).
"""
import argparse
import json
import numpy as np
import emcee

OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
DELTA_C = 1.686
Z_EFF = 1.491
B1_PUBLISHED = 0.237 * (1 + Z_EFF) ** 2 + 0.771


def get_cosmo_funcs(tk_source):
    from cosmoprimo.fiducial import DESI
    cosmo = DESI(engine="eisenstein_hu")
    H_ABS, C_KMS = cosmo.h, 299792.458
    H0, OMEGA_M = cosmo.H0, cosmo.Omega0_m
    D_ZEFF = cosmo.growth_factor(Z_EFF) / cosmo.growth_factor(0.0)
    F_ZEFF = cosmo.growth_rate(Z_EFF)
    fo = cosmo.get_fourier()
    pk0_eh = fo.pk_interpolator(of="delta_cb")
    NS = cosmo.n_s
    KREF = 1e-5

    if tk_source == "eh":
        def Tk(k):
            num = pk0_eh(k, z=0) / k ** NS
            den = pk0_eh(KREF, z=0) / KREF ** NS
            return np.sqrt(num / den)

        def plin_zeff(k):
            return D_ZEFF ** 2 * pk0_eh(k, z=0)
    else:
        import camb_transfer as ct

        def Tk(k):
            return ct.Tk_camb(k)

        def plin_zeff(k):
            # rescale CAMB's z=0 P(k) to z_eff via the SAME EH growth factor
            # (background/growth kept identical across tk_source -- only the
            # transfer function differs, per task scope "replace the EH T(k)
            # ... and the linear P(k) model")
            return D_ZEFF ** 2 * ct.pk_camb_z0(k)

    def alpha(k):
        k_abs = k * H_ABS
        return C_KMS ** 2 * k_abs ** 2 * Tk(k) * D_ZEFF / (OMEGA_M * H0 ** 2)

    return alpha, plin_zeff, F_ZEFF, D_ZEFF


def load_data(nran_suffix, apply_ic, ic_data=None):
    with open(f"{OUT}/pk_qso_NGC{nran_suffix}.json") as f:
        ngc = json.load(f)
    with open(f"{OUT}/pk_qso_SGC{nran_suffix}.json") as f:
        sgc = json.load(f)
    k = np.array(ngc["k"])
    good = ~np.isnan(k) & (k >= 0.003) & (k <= 0.08)
    k = k[good]
    p0_n, p2_n, nm_n = (np.array(ngc[x])[good] for x in ("power_0", "power_2", "nmodes"))
    p0_s, p2_s, nm_s = (np.array(sgc[x])[good] for x in ("power_0", "power_2", "nmodes"))
    wn, ws = ngc["n_data"], sgc["n_data"]
    p0 = (wn * p0_n + ws * p0_s) / (wn + ws)
    p2 = (wn * p2_n + ws * p2_s) / (wn + ws)
    nmodes = nm_n + nm_s
    shotnoise = (wn * ngc["shotnoise"] + ws * sgc["shotnoise"]) / (wn + ws)

    if apply_ic:
        # global IC (fix 1): subtract the window's own normalised monopole
        # shape times the OBSERVED P0 at k_min (data-side correction, the
        # standard direction for the classic global-IC formula since the
        # true P0 is unknown -- Beutler+2014 eq. 13-14 apply it this way
        # when only one field realisation is available).
        wN = json.load(open(f"{OUT}/window_qso_NGC.json"))
        wS = json.load(open(f"{OUT}/window_qso_SGC.json"))
        kw = np.array(wN["k"])
        w0_n = np.array(wN["w0"]) / np.array(wN["w0"])[~np.isnan(wN["w0"])][0]
        w0_s = np.array(wS["w0"]) / np.array(wS["w0"])[~np.isnan(wS["w0"])][0]
        w0comb = (wn * w0_n + ws * w0_s) / (wn + ws)
        w0comb_i = np.interp(k, kw, w0comb)
        p0 = p0 - w0comb_i * p0[0]
    return k, p0, p2, nmodes, shotnoise


def make_model(alpha_fn, plin_fn, f_zeff):
    def model_p0p2(k, f_nl, p, n_shot, b1=B1_PUBLISHED):
        db = 3.0 * f_nl * DELTA_C * (b1 - p) / alpha_fn(k)
        b = b1 + db
        pl = plin_fn(k)
        p0 = (b ** 2 + (2.0 / 3.0) * b * f_zeff + f_zeff ** 2 / 5.0) * pl + n_shot
        p2 = ((4.0 / 3.0) * b * f_zeff + (4.0 / 7.0) * f_zeff ** 2) * pl
        return p0, p2
    return model_p0p2


def run(args):
    alpha_fn, plin_fn, f_zeff, d_zeff = get_cosmo_funcs(args.tk)
    nran_suffix = f"_nran{args.nran}" if args.nran != 4 else ""
    K, P0_OBS, P2_OBS, NMODES, SHOTNOISE = load_data(nran_suffix, args.window_ic)
    model_p0p2 = make_model(alpha_fn, plin_fn, f_zeff)

    SIG_P0_RAW = np.sqrt(2.0 / NMODES) * (P0_OBS + SHOTNOISE)
    SIG_P2_RAW = np.sqrt(2.0 * 5.0 / NMODES) * (P0_OBS + SHOTNOISE)
    p0_null, p2_null = model_p0p2(K, 0.0, 1.6, 0.0)
    chi2_null = np.sum((P0_OBS - p0_null) ** 2 / SIG_P0_RAW ** 2) + \
                np.sum((P2_OBS - p2_null) ** 2 / SIG_P2_RAW ** 2)
    dof = 2 * len(K)
    cal = float(np.sqrt(chi2_null / dof))
    SIG_P0, SIG_P2 = SIG_P0_RAW * cal, SIG_P2_RAW * cal
    shot_prior_center = SHOTNOISE if args.shotnoise_fixed else 0.0
    shot_prior_width = 0.1 * SHOTNOISE

    def log_prior(theta, p_free):
        if p_free:
            f_nl, n_shot, p = theta
            if not (1.0 <= p <= 1.6):
                return -np.inf
        else:
            f_nl, n_shot = theta
        if not (-500 < f_nl < 500):
            return -np.inf
        return -0.5 * ((n_shot - shot_prior_center) / shot_prior_width) ** 2

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
        return lp + log_like(theta, p_free, p_fixed) if np.isfinite(lp) else -np.inf

    def run_mcmc(p_free, p_fixed=None, nwalkers=32, nsteps=3000):
        ndim = 3 if p_free else 2
        rng = np.random.default_rng(42)
        if p_free:
            p0 = np.column_stack([rng.normal(0, 5, nwalkers),
                                   rng.normal(shot_prior_center, shot_prior_width, nwalkers),
                                   rng.uniform(1.0, 1.6, nwalkers)])
        else:
            p0 = np.column_stack([rng.normal(0, 5, nwalkers),
                                   rng.normal(shot_prior_center, shot_prior_width, nwalkers)])
        sampler = emcee.EnsembleSampler(nwalkers, ndim, log_prob, args=(p_free, p_fixed))
        sampler.run_mcmc(p0, nsteps, progress=False)
        return sampler.get_chain(discard=nsteps // 3, thin=10, flat=True)

    results = {"tk": args.tk, "nran": args.nran, "window_ic": args.window_ic,
               "shotnoise_fixed": args.shotnoise_fixed, "cov_calibration_factor": cal,
               "chi2_null_over_dof_before_cal": float(chi2_null / dof),
               "k_range": [float(K.min()), float(K.max())], "n_kbins": int(len(K))}
    for p_fixed, label in [(1.6, "p1.6"), (1.0, "p1.0")]:
        chain = run_mcmc(False, p_fixed)[:, 0]
        results[label] = {"f_nl_median": float(np.median(chain)),
                           "f_nl_p16": float(np.percentile(chain, 16)),
                           "f_nl_p84": float(np.percentile(chain, 84)),
                           "f_nl_sigma": float(np.std(chain))}
    chain_m = run_mcmc(True)
    results["p_marg"] = {"f_nl_median": float(np.median(chain_m[:, 0])),
                          "f_nl_p16": float(np.percentile(chain_m[:, 0], 16)),
                          "f_nl_p84": float(np.percentile(chain_m[:, 0], 84)),
                          "f_nl_sigma": float(np.std(chain_m[:, 0]))}
    print(json.dumps(results, indent=2))
    with open(args.out, "w") as fh:
        json.dump(results, fh, indent=2)



def run_point(args):
    """Fast scipy.optimize point-estimate path (compute-budget fallback):
    MCMC posteriors under fit_fnl_v2.py's full emcee path proved too slow
    under this session's host contention (RUN_LOG.md follow-up section) --
    this reuses the same chi2 as run_mcmc's log_like but minimizes directly.
    Sigma is NOT recomputed here; v1's MCMC sigma (fnl_fit_results.json) is
    the canonical uncertainty reference for the v2 movement table."""
    from scipy.optimize import minimize
    alpha_fn, plin_fn, f_zeff, d_zeff = get_cosmo_funcs(args.tk)
    nran_suffix = f"_nran{args.nran}" if args.nran != 4 else ""
    K, P0_OBS, P2_OBS, NMODES, SHOTNOISE = load_data(nran_suffix, args.window_ic)
    model_p0p2 = make_model(alpha_fn, plin_fn, f_zeff)
    SIG_P0 = np.sqrt(2.0 / NMODES) * (P0_OBS + SHOTNOISE)
    SIG_P2 = np.sqrt(2.0 * 5.0 / NMODES) * (P0_OBS + SHOTNOISE)
    shot0 = SHOTNOISE if args.shotnoise_fixed else 0.0

    def chi2(theta, p_fixed):
        f_nl, n_shot = theta
        p0m, p2m = model_p0p2(K, f_nl, p_fixed, n_shot)
        return np.sum((P0_OBS - p0m) ** 2 / SIG_P0 ** 2) + np.sum((P2_OBS - p2m) ** 2 / SIG_P2 ** 2)

    results = {"tk": args.tk, "nran": args.nran, "window_ic": args.window_ic,
               "shotnoise_fixed": args.shotnoise_fixed, "method": "point_estimate"}
    for p_fixed, label in [(1.6, "p1.6"), (1.0, "p1.0")]:
        res = minimize(chi2, x0=[0.0, shot0], args=(p_fixed,), method="Nelder-Mead")
        results[label] = {"f_nl_point": float(res.x[0])}
        print(label, results[label])
    with open(args.out, "w") as fh:
        json.dump(results, fh, indent=2)
    print("SAVED", args.out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--tk", choices=["eh", "camb"], default="eh")
    ap.add_argument("--nran", type=int, default=4)
    ap.add_argument("--window-ic", action="store_true")
    ap.add_argument("--shotnoise-fixed", action="store_true")
    ap.add_argument("--out", required=True)
    ap.add_argument("--point", action="store_true",
                     help="fast scipy.optimize point estimate instead of full emcee MCMC")
    a = ap.parse_args()
    run_point(a) if a.point else run(a)
