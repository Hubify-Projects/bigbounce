"""
Prior-predictive check for the spectator-ALP cosmic-birefringence
consistency check in Paper 1B (arxiv/paper1b_mcmc_companion.tex,
Sec. VI "Cosmic Birefringence: Spectator ALP Consistency Check").

MOTIVATION (rebuttal to ChatGPT-B2 "tautological fit" concern)
--------------------------------------------------------------
The ALP MCMC uses a Gaussian summary likelihood centred on the single
published datum beta_obs = 0.342 +/- 0.094 deg (Eskilt & Komatsu 2022).
The reviewer's concern: because the likelihood is centred on the datum,
"agreement within 1 sigma" is guaranteed by construction and therefore
carries no evidential weight -- the fit could be tautological.

The honest quantitative rebuttal is a PRIOR-PREDICTIVE fraction: sample
the ALP nuisance parameters from their STATED priors (NOT the posterior),
push each draw through the SAME committed forward model
beta(theta_i, m, C_agamma) = (C_agamma * alpha_EM / 4pi) * [theta(z_rec)-theta(0)],
and ask what fraction of prior draws lands within sigma_beta (and 2 sigma_beta)
of beta_obs WITHOUT ANY LIKELIHOOD.

  - Large fraction => the signal sits in a generic region of prior space:
    natural accommodation, the "fit" is cheap, concern is mild.
  - Tiny fraction  => the model only reaches beta_obs in a fine-tuned
    corner: the accommodation IS prior-/tuning-dependent and MUST be
    disclosed (the fit is not evidentially free).

Either way, the REAL number goes in the paper. No fabrication.

FORWARD MODEL: reuses the committed EOM integrator
research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py
(the exact same code the paper's beta prediction comes from).

STATED PRIORS (read directly from
arxiv/paper1b_mcmc_companion.tex App. "ALP-MCMC Sampled Parameters"):

  Continuous-prior headline config (c5_continuous):
    C_agamma       ~ Uniform[4, 60]
    theta_i        ~ Uniform[0.01, pi]
    log10(m_a/eV)  ~ Uniform[-35, -30]
    f_a            = M_Pl (fixed)

  Fixed-coupling config (run1_full):
    C_agamma       = 8 (fixed)
    theta_i        ~ Uniform[0.01, pi]
    log10(m_a/eV)  ~ Uniform[-35, -30]
    f_a            = M_Pl (fixed)

OBSERVED:  beta_obs = 0.342 deg,  sigma_beta = 0.094 deg (Eskilt & Komatsu 2022).

Usage:
    python3 alp_prior_predictive.py            # 1e5 draws (default)
    python3 alp_prior_predictive.py 200000     # custom N
"""
import os
import sys
import json
import numpy as np
from scipy.integrate import solve_ivp

# Import the committed forward model (same EOM the paper's beta comes from).
_HERE = os.path.dirname(os.path.abspath(__file__))
_ALP_DIR = os.path.normpath(os.path.join(
    _HERE, "..", "..", "research", "branch_R_alp_birefringence", "phase2_mcmc"))
sys.path.insert(0, _ALP_DIR)
import alp_ode as _A  # noqa: E402
from alp_ode import compute_alp_birefringence  # noqa: E402  (reference integrator)


def beta_deg_fast(theta_i, log10_m_eV, C_agamma=8.0, Omega_m=0.315):
    """Birefringence via the SAME committed EOM (alp_ode._ode_rhs_lna) but with
    DOP853 adaptive stepping at rtol=1e-7 and no max_step cap.

    Verified to agree with the committed compute_alp_birefringence integrator
    (rtol=1e-10, max_step=0.05) to < 3e-8 deg over the full prior box -- i.e.
    ~7 orders of magnitude below sigma_beta=0.094 deg -- so the MC uses the
    identical physical model, just a faster tolerance. This equivalence is
    re-checked by verify_equivalence() and reported at run time.
    """
    m = 10.0 ** log10_m_eV
    la0 = -np.log(1 + 3000.0)
    lar = -np.log(1 + _A.Z_REC)
    sol = solve_ivp(_A._ode_rhs_lna, [la0, 0.0], [theta_i, 0.0],
                    args=(m, _A.H0_EV, Omega_m), method="DOP853",
                    rtol=1e-7, atol=1e-10, dense_output=True)
    if not sol.success:
        return np.nan
    dtheta = sol.sol(lar)[0] - sol.sol(0.0)[0]
    return float(np.degrees(C_agamma * _A.ALPHA_EM * dtheta / (4.0 * np.pi)))


def verify_equivalence(n=40, seed=0):
    """Max |beta_fast - beta_committed| over n random prior-box points (deg)."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(n):
        ti = rng.uniform(0.01, np.pi)
        lm = rng.uniform(-35.0, -30.0)
        cg = rng.uniform(4.0, 60.0)
        b0 = compute_alp_birefringence(ti, lm, C_agamma=cg)["beta_deg"]
        worst = max(worst, abs(beta_deg_fast(ti, lm, cg) - b0))
    return worst

# ---- Observed datum (Eskilt & Komatsu 2022, joint WMAP+Planck) ----
BETA_OBS = 0.342     # deg
SIGMA_BETA = 0.094   # deg

# ---- Stated priors ----
THETA_I_LO, THETA_I_HI = 0.01, np.pi
LOG10M_LO, LOG10M_HI = -35.0, -30.0
CAG_LO, CAG_HI = 4.0, 60.0


def _eval_star(args):
    """Picklable worker for ProcessPoolExecutor: (theta_i, log10m, C) -> beta."""
    ti, lm, cg = args
    try:
        return beta_deg_fast(ti, lm, cg)
    except Exception:
        return np.nan


def prior_predictive(n_draws, sample_coupling, seed=1234):
    """Monte-Carlo the STATED priors through the committed beta() forward model.

    sample_coupling=True  -> c5_continuous headline config (C_agamma~U[4,60]).
    sample_coupling=False -> run1_full fixed-coupling config (C_agamma=8).
    Uses beta_deg_fast (verified equivalent to the committed integrator). Runs
    serially -- deterministic, no multiprocessing to be reaped mid-run.
    Returns dict of summary statistics.
    """
    rng = np.random.default_rng(seed)
    theta_i = rng.uniform(THETA_I_LO, THETA_I_HI, n_draws)
    log10m = rng.uniform(LOG10M_LO, LOG10M_HI, n_draws)
    if sample_coupling:
        c_ag = rng.uniform(CAG_LO, CAG_HI, n_draws)
    else:
        c_ag = np.full(n_draws, 8.0)

    nproc = int(os.environ.get("ALP_NPROC", "1"))
    if nproc > 1:
        from concurrent.futures import ProcessPoolExecutor
        tasks = list(zip(theta_i.tolist(), log10m.tolist(), c_ag.tolist()))
        with ProcessPoolExecutor(max_workers=nproc) as ex:
            beta = np.array(list(ex.map(_eval_star, tasks, chunksize=100)))
    else:
        beta = np.empty(n_draws)
        for i in range(n_draws):
            try:
                beta[i] = beta_deg_fast(float(theta_i[i]), float(log10m[i]),
                                        float(c_ag[i]))
            except Exception:
                beta[i] = np.nan
    failed = int(np.sum(~np.isfinite(beta)))

    ok = np.isfinite(beta)
    beta_ok = beta[ok]
    absdiff = np.abs(beta_ok - BETA_OBS)

    frac_1sig = float(np.mean(absdiff < SIGMA_BETA))
    frac_2sig = float(np.mean(absdiff < 2 * SIGMA_BETA))
    # sign-agnostic: birefringence sign is a convention; also report |beta| match
    absbeta = np.abs(beta_ok)
    frac_1sig_absmag = float(np.mean(np.abs(absbeta - BETA_OBS) < SIGMA_BETA))
    frac_2sig_absmag = float(np.mean(np.abs(absbeta - BETA_OBS) < 2 * SIGMA_BETA))

    return {
        "config": "c5_continuous (C_agamma~U[4,60])" if sample_coupling
        else "run1_full (C_agamma=8 fixed)",
        "n_draws": int(n_draws),
        "n_failed": int(failed),
        "beta_obs_deg": BETA_OBS,
        "sigma_beta_deg": SIGMA_BETA,
        "frac_within_1sigma": frac_1sig,
        "frac_within_2sigma": frac_2sig,
        "frac_within_1sigma_absmag": frac_1sig_absmag,
        "frac_within_2sigma_absmag": frac_2sig_absmag,
        "median_abs_beta_deg": float(np.median(absbeta)),
        "beta_16_50_84_deg": [float(np.percentile(beta_ok, 16)),
                              float(np.percentile(beta_ok, 50)),
                              float(np.percentile(beta_ok, 84))],
        "absbeta_16_50_84_deg": [float(np.percentile(absbeta, 16)),
                                 float(np.percentile(absbeta, 50)),
                                 float(np.percentile(absbeta, 84))],
        "frac_absbeta_exceeds_obs": float(np.mean(absbeta > BETA_OBS)),
    }


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000
    print(f"# Prior-predictive ALP birefringence check  (N={n:,} draws each)\n")
    worst = verify_equivalence(40)
    print(f"# integrator-equivalence check: max |beta_fast - beta_committed| "
          f"= {worst:.2e} deg  (<< sigma_beta={SIGMA_BETA})\n")
    out = os.path.join(_HERE, "alp_prior_predictive_result.json")
    results = []
    for sample_coupling in (True, False):
        res = prior_predictive(n, sample_coupling)
        res["integrator_equiv_max_deg"] = float(worst)
        results.append(res)
        # write incrementally so a partial run still leaves a usable artifact
        with open(out, "w") as f:
            json.dump(results, f, indent=2)
        print(f"## {res['config']}")
        print(f"  draws                : {res['n_draws']:,}  (failed: {res['n_failed']})")
        print(f"  beta_obs             : {res['beta_obs_deg']} +/- {res['sigma_beta_deg']} deg")
        print(f"  median |beta|        : {res['median_abs_beta_deg']:.4f} deg")
        print(f"  |beta| 16/50/84 pct  : {res['absbeta_16_50_84_deg']}")
        print(f"  frac within 1 sigma  : {res['frac_within_1sigma']*100:.2f}%  (signed)")
        print(f"  frac within 2 sigma  : {res['frac_within_2sigma']*100:.2f}%  (signed)")
        print(f"  frac |beta| w/in 1sig: {res['frac_within_1sigma_absmag']*100:.2f}%")
        print(f"  frac |beta| w/in 2sig: {res['frac_within_2sigma_absmag']*100:.2f}%")
        print(f"  frac |beta| > obs    : {res['frac_absbeta_exceeds_obs']*100:.2f}%")
        print()

    print(f"# wrote {out}")


if __name__ == "__main__":
    main()
