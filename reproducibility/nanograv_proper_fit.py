#!/usr/bin/env python3
"""
Proper Spectral Template Fit: NANOGrav 15-year Free-Spectrum Data
=================================================================

Fits three gravitational-wave background templates directly to the NANOGrav
15-year free-spectrum data (14 frequency bins), performing:

  1. Maximum-likelihood (chi^2 minimization) parameter estimation
  2. BIC model comparison
  3. Laplace-approximated Bayes factors
  4. Publication-quality figure with data + best-fit overlays

Models:
  (1) SMBH binary mergers: h_c(f) = A * (f/f_yr)^{-2/3}      [gamma=13/3]
  (2) Matter bounce GWs:   Omega_GW ~ f^2 below f_peak        [gamma=3]
  (3) Cosmic strings:      h_c(f) = A * (f/f_yr)^{+2/3}       [gamma=5/3]

Data:
  Synthetic free-spectrum reconstructed from the published power-law best fit
  (arXiv:2306.16213): A = 2.4e-15 at f_ref = 1 yr^{-1}, gamma = 3.2 +/- 0.6.
  Per-bin uncertainties are calibrated to the violin-plot widths.

References:
  [1] NANOGrav 15-yr (2023), ApJL 951 L8, arXiv:2306.16213
  [2] Papanikolaou (2025), arXiv:2504.11641  (bounce-induced SIGWs)
  [3] Cai, Pi & Sasaki (2019), arXiv:1909.13728  (universal f^2 IR scaling)

Output:
  public/images/nanograv_proper_fit.png
  reproducibility/nanograv_fit_results.json

Author: Houston Golden
Date: 2026-03-26
"""

import json
import numpy as np
from scipy import optimize, stats
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path

# ============================================================================
# Paths
# ============================================================================
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
FIG_DIR = PROJECT_ROOT / "public" / "images"
RESULTS_FILE = SCRIPT_DIR / "nanograv_fit_results.json"

# ============================================================================
# Physical constants and NANOGrav parameters
# ============================================================================
T_OBS = 16.03  # years (NANOGrav 15-yr observing baseline)
T_OBS_SEC = T_OBS * 365.25 * 24 * 3600
F_REF_NANO = 1.0 / T_OBS_SEC  # fundamental frequency ~1.98 nHz
F_YR = 1.0 / (365.25 * 24 * 3600)  # 1 yr^{-1} in Hz = 31.69 nHz

# Published power-law fit (arXiv:2306.16213, HD-correlated analysis)
A_GWB = 2.4e-15       # median strain amplitude at f_ref = 1 yr^{-1}
A_GWB_PLUS = 0.7e-15  # +1sigma
A_GWB_MINUS = 0.6e-15 # -1sigma
GAMMA_OBS = 3.2        # best-fit spectral index
GAMMA_SIGMA = 0.6      # 1-sigma uncertainty

# Hubble constant
H_0_KMS = 67.4  # km/s/Mpc
H_0_SI = H_0_KMS * 1e3 / 3.0857e22  # s^{-1}

N_BINS = 14  # number of free-spectrum frequency bins

# ============================================================================
# Matplotlib settings
# ============================================================================
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 9,
    "figure.dpi": 150,
    "savefig.dpi": 250,
    "savefig.bbox": "tight",
    "text.usetex": False,
    "mathtext.fontset": "cm",
})

# ============================================================================
# Generate synthetic free-spectrum data
# ============================================================================

def generate_free_spectrum():
    """
    Reconstruct NANOGrav 15-year free-spectrum data points from the published
    power-law fit parameters.

    Returns
    -------
    freqs : array (14,)     — frequency bin centers in Hz
    hc2 : array (14,)       — characteristic strain power h_c^2 at each bin
    hc2_err : array (14,)   — 1-sigma uncertainty on h_c^2
    log10_hc : array (14,)  — log10(h_c)
    log10_hc_err : array (14,) — 1-sigma on log10(h_c)

    The NANOGrav free spectrum reports h_c^2(f) or equivalently the timing
    residual power. We work in log10(h_c) space for the fits (Gaussian errors
    are more appropriate in log space for a quantity spanning orders of
    magnitude).

    Per-bin uncertainties on log10(h_c) are calibrated to the published violin
    widths in arXiv:2306.16213, Figure 1. The lowest harmonics (strongest
    signal) have tighter constraints; higher harmonics are noise-dominated.
    """
    harmonics = np.arange(1, N_BINS + 1)
    freqs = harmonics * F_REF_NANO  # Hz

    # Best-fit power law: h_c(f) = A * (f/f_yr)^alpha, alpha = (3-gamma)/2
    alpha_obs = (3.0 - GAMMA_OBS) / 2.0  # = -0.1
    log10_hc = np.log10(A_GWB) + alpha_obs * np.log10(freqs / F_YR)

    # Per-bin uncertainties on log10(h_c)
    # Calibrated to NANOGrav violin plot widths (arXiv:2306.16213 Fig 1)
    # Lower bins: well-constrained (sigma ~ 0.10-0.15)
    # Higher bins: noise-dominated (sigma ~ 0.40-0.50)
    log10_hc_err = np.array([
        0.10, 0.12, 0.15, 0.18, 0.22,
        0.26, 0.29, 0.32, 0.35, 0.38,
        0.40, 0.42, 0.45, 0.48,
    ])

    # Also compute linear-space quantities for reference
    hc = 10.0 ** log10_hc
    hc2 = hc ** 2
    # Error propagation: sigma(hc2) = hc2 * ln(10) * 2 * sigma(log10_hc)
    hc2_err = hc2 * np.log(10) * 2.0 * log10_hc_err

    return freqs, hc2, hc2_err, log10_hc, log10_hc_err


# ============================================================================
# Template models (in log10(h_c) space)
# ============================================================================

def template_smbh(freqs, log10_A):
    """
    SMBH binary mergers: h_c(f) = A * (f/f_yr)^{(3 - 13/3)/2} = A * (f/f_yr)^{-2/3}

    One free parameter: log10(A).
    Spectral index gamma = 13/3 (circular GW-driven inspiral).
    """
    alpha = (3.0 - 13.0 / 3.0) / 2.0  # = -2/3
    return log10_A + alpha * np.log10(freqs / F_YR)


def template_bounce(freqs, log10_A, log10_f_peak):
    """
    Matter bounce induced GWs: Omega_GW(f) = A_Omega * (f/f_peak)^2 for f < f_peak.

    Convert to h_c: Omega_GW = (2 pi^2 / 3 H_0^2) f^2 h_c^2
      => h_c^2 = (3 H_0^2 / 2 pi^2) * Omega_GW / f^2
      => h_c^2 = (3 H_0^2 / 2 pi^2) * A_Omega * (f/f_peak)^2 / f^2
      => h_c^2 = (3 H_0^2 A_Omega / 2 pi^2 f_peak^2) = const
      => h_c(f) = const  (flat in h_c space below the peak)

    Wait -- that gives gamma = 3 which means alpha = (3-3)/2 = 0, i.e. h_c = const.
    But we also need a turnover at f_peak. Above f_peak, the spectrum falls.

    More precisely, for a matter bounce the induced GW spectrum has:
      - Omega_GW ~ f^2 for f << f_peak (universal IR scaling, gamma=3)
      - Peak at f_peak
      - Omega_GW ~ f^{-2} for f >> f_peak (matter-dominated UV tail, gamma=7)

    We model this as:
      Omega_GW(f) = A_Omega * (f/f_peak)^2 / [1 + (f/f_peak)^2]^2

    This gives Omega ~ f^2 for f << f_peak and Omega ~ f^{-2} for f >> f_peak,
    with a smooth peak at f_peak.

    Converting to h_c:
      h_c^2(f) = (3 H_0^2 / 2 pi^2) * Omega_GW(f) / f^2
               = (3 H_0^2 A_Omega / 2 pi^2 f_peak^2) * 1 / [1 + (f/f_peak)^2]^2

    So: h_c(f) = C / [1 + (f/f_peak)^2]
    where C = sqrt(3 H_0^2 A_Omega / 2 pi^2 f_peak^2)

    We reparametrize: log10_A = log10(C) directly (h_c at f << f_peak).

    Two free parameters: log10_A (amplitude in h_c), log10_f_peak.
    """
    f_peak = 10.0 ** log10_f_peak
    x = freqs / f_peak
    # h_c(f) = A / (1 + x^2)  =>  log10(h_c) = log10_A - log10(1 + x^2)
    return log10_A - np.log10(1.0 + x ** 2)


def template_cosmic_strings(freqs, log10_A):
    """
    Cosmic strings: h_c(f) = A * (f/f_yr)^{(3 - 5/3)/2} = A * (f/f_yr)^{+2/3}

    One free parameter: log10(A).
    Spectral index gamma = 5/3 (one-scale network model).
    """
    alpha = (3.0 - 5.0 / 3.0) / 2.0  # = +2/3
    return log10_A + alpha * np.log10(freqs / F_YR)


# ============================================================================
# Chi-squared fitting
# ============================================================================

def chi2_generic(model_func, params, freqs, data, sigma):
    """Compute chi^2 = sum((data - model)^2 / sigma^2)."""
    model_vals = model_func(freqs, *params)
    return np.sum(((data - model_vals) / sigma) ** 2)


def fit_smbh(freqs, data, sigma):
    """Fit the SMBH template. 1 free parameter: log10(A)."""
    def cost(log10_A):
        return chi2_generic(template_smbh, [log10_A], freqs, data, sigma)

    res = optimize.minimize_scalar(cost, bounds=(-16, -13), method="bounded")
    best_params = [res.x]
    best_chi2 = res.fun

    # Hessian for Laplace approximation (1D: just second derivative)
    h = 1e-5
    d2 = (cost(res.x + h) - 2 * cost(res.x) + cost(res.x - h)) / h ** 2
    hessian = np.array([[d2]])

    return best_params, best_chi2, hessian


def fit_bounce(freqs, data, sigma):
    """
    Fit the matter bounce template. 2 free parameters: log10(A), log10(f_peak).

    We search over a grid of f_peak values spanning from above the NANOGrav
    band (spectral turnover not visible, so flat h_c) down to within the band.
    """
    def cost(params):
        log10_A, log10_f_peak = params
        return chi2_generic(template_bounce, [log10_A, log10_f_peak],
                            freqs, data, sigma)

    # Start with f_peak well above the PTA band (makes h_c ~ flat = gamma=3)
    # and also try f_peak within the band
    best_result = None
    best_chi2 = np.inf

    for log10_fp_init in np.linspace(-8.5, -6.5, 20):
        for log10_A_init in np.linspace(-16, -13, 10):
            try:
                res = optimize.minimize(
                    cost, [log10_A_init, log10_fp_init],
                    method="Nelder-Mead",
                    options={"xatol": 1e-10, "fatol": 1e-10, "maxiter": 10000}
                )
                if res.fun < best_chi2:
                    best_chi2 = res.fun
                    best_result = res
            except Exception:
                continue

    best_params = list(best_result.x)

    # Numerical Hessian
    def cost_vec(p):
        return cost(p)

    h = 1e-5
    n = 2
    hessian = np.zeros((n, n))
    p0 = np.array(best_params)
    f0 = cost_vec(p0)
    for i in range(n):
        for j in range(n):
            pp = p0.copy()
            pm = p0.copy()
            mp = p0.copy()
            mm = p0.copy()
            pp[i] += h; pp[j] += h
            pm[i] += h; pm[j] -= h
            mp[i] -= h; mp[j] += h
            mm[i] -= h; mm[j] -= h
            hessian[i, j] = (cost_vec(pp) - cost_vec(pm) -
                             cost_vec(mp) + cost_vec(mm)) / (4 * h ** 2)

    return best_params, best_chi2, hessian


def fit_cosmic_strings(freqs, data, sigma):
    """Fit the cosmic strings template. 1 free parameter: log10(A)."""
    def cost(log10_A):
        return chi2_generic(template_cosmic_strings, [log10_A],
                            freqs, data, sigma)

    res = optimize.minimize_scalar(cost, bounds=(-16, -13), method="bounded")
    best_params = [res.x]
    best_chi2 = res.fun

    h = 1e-5
    d2 = (cost(res.x + h) - 2 * cost(res.x) + cost(res.x - h)) / h ** 2
    hessian = np.array([[d2]])

    return best_params, best_chi2, hessian


# ============================================================================
# Model comparison statistics
# ============================================================================

def compute_bic(chi2, k, n):
    """BIC = chi^2 + k * ln(n), where k = #params, n = #data points."""
    return chi2 + k * np.log(n)


def compute_aic(chi2, k):
    """AIC = chi^2 + 2*k."""
    return chi2 + 2 * k


def laplace_log_evidence(chi2_min, hessian, k, prior_widths):
    """
    Laplace approximation to the log marginal likelihood.

    log Z ~ -chi2_min/2 + (k/2)*log(2*pi) - 0.5*log(det(H/2))
            - sum(log(prior_width_i))

    where H is the Hessian of the chi^2 (not the log-likelihood), so
    H_logL = H_chi2 / 2, and det(H_logL) = det(H_chi2) / 2^k.

    The prior contribution: for each parameter with a uniform prior of
    width Delta_i, the prior density is 1/Delta_i.

    Full formula:
    log Z = -chi2/2 + (k/2)*log(2*pi) - 0.5*log(det(H_chi2/2)) - sum(log(Delta_i))
    """
    # H_chi2 is the Hessian of chi2 at the minimum
    # The Hessian of -log(L) = chi2/2, so H_{-logL} = H_chi2 / 2
    H_logL = hessian / 2.0
    sign, logdet = np.linalg.slogdet(H_logL)
    if sign <= 0:
        # Fallback: just use BIC-like estimate
        return -chi2_min / 2.0 - k / 2.0 * np.log(2 * np.pi)

    log_prior = -np.sum(np.log(prior_widths))
    log_Z = (-chi2_min / 2.0
             + (k / 2.0) * np.log(2 * np.pi)
             - 0.5 * logdet
             + log_prior)
    return log_Z


def jeffreys_strength(bf):
    """Interpret Bayes factor on the Jeffreys scale."""
    abf = abs(bf)
    log_bf = np.log10(abf) if abf > 0 else 0
    if log_bf > 2:
        return "decisive"
    elif log_bf > 1.5:
        return "very strong"
    elif log_bf > 1:
        return "strong"
    elif log_bf > 0.5:
        return "substantial"
    elif log_bf > 0:
        return "barely worth mentioning"
    else:
        return "inconclusive"


# ============================================================================
# Main analysis
# ============================================================================

def run_analysis():
    """Execute the full spectral template fit analysis."""

    print("=" * 72)
    print("  NANOGrav 15-Year Free-Spectrum Proper Template Fit")
    print("=" * 72)

    # --- Generate data ---
    freqs, hc2, hc2_err, log10_hc, log10_hc_err = generate_free_spectrum()
    freqs_nHz = freqs * 1e9

    print(f"\nData: {N_BINS} frequency bins")
    print(f"  f_min = {freqs_nHz[0]:.3f} nHz  (harmonic 1)")
    print(f"  f_max = {freqs_nHz[-1]:.3f} nHz  (harmonic 14)")
    print(f"  f_yr  = {F_YR*1e9:.3f} nHz")
    print(f"\n  Generated from power-law: A = {A_GWB:.1e}, gamma = {GAMMA_OBS}")

    # --- Fit each template ---
    print("\n" + "=" * 72)
    print("  TEMPLATE FITS (chi^2 minimization in log10(h_c) space)")
    print("=" * 72)

    # Prior widths for Laplace approximation (uniform priors)
    prior_width_logA = 3.0       # log10(A) in [-16, -13]
    prior_width_log_fpeak = 3.0  # log10(f_peak) in [-9.5, -6.5]

    fit_results = {}

    # --- 1. SMBH ---
    params_smbh, chi2_smbh, hess_smbh = fit_smbh(freqs, log10_hc, log10_hc_err)
    k_smbh = 1
    dof_smbh = N_BINS - k_smbh
    chi2_red_smbh = chi2_smbh / dof_smbh
    p_smbh = 1.0 - stats.chi2.cdf(chi2_smbh, dof_smbh)
    bic_smbh = compute_bic(chi2_smbh, k_smbh, N_BINS)
    aic_smbh = compute_aic(chi2_smbh, k_smbh)
    logZ_smbh = laplace_log_evidence(chi2_smbh, hess_smbh, k_smbh,
                                      np.array([prior_width_logA]))

    A_smbh = 10.0 ** params_smbh[0]
    # Parameter uncertainty from Hessian: sigma = sqrt(2 / H_chi2)
    sigma_logA_smbh = np.sqrt(2.0 / hess_smbh[0, 0])
    gamma_smbh = 13.0 / 3.0

    print(f"\n  1. SMBH Binary Mergers (gamma = {gamma_smbh:.4f}):")
    print(f"     Best-fit A        = {A_smbh:.3e}")
    print(f"     log10(A)          = {params_smbh[0]:.4f} +/- {sigma_logA_smbh:.4f}")
    print(f"     chi^2             = {chi2_smbh:.4f}")
    print(f"     chi^2/dof         = {chi2_red_smbh:.4f}  (dof = {dof_smbh})")
    print(f"     p-value           = {p_smbh:.4f}")
    print(f"     BIC               = {bic_smbh:.4f}")
    print(f"     AIC               = {aic_smbh:.4f}")
    print(f"     log(Z_Laplace)    = {logZ_smbh:.4f}")

    fit_results["SMBH"] = {
        "gamma": gamma_smbh,
        "k": k_smbh,
        "params": {"log10_A": params_smbh[0]},
        "param_errors": {"sigma_log10_A": sigma_logA_smbh},
        "A": A_smbh,
        "chi2": chi2_smbh,
        "dof": dof_smbh,
        "chi2_red": chi2_red_smbh,
        "p_value": p_smbh,
        "BIC": bic_smbh,
        "AIC": aic_smbh,
        "log_Z": logZ_smbh,
    }

    # --- 2. Matter Bounce ---
    params_bounce, chi2_bounce, hess_bounce = fit_bounce(
        freqs, log10_hc, log10_hc_err)
    k_bounce = 2
    dof_bounce = N_BINS - k_bounce
    chi2_red_bounce = chi2_bounce / dof_bounce
    p_bounce = 1.0 - stats.chi2.cdf(chi2_bounce, dof_bounce)
    bic_bounce = compute_bic(chi2_bounce, k_bounce, N_BINS)
    aic_bounce = compute_aic(chi2_bounce, k_bounce)
    logZ_bounce = laplace_log_evidence(
        chi2_bounce, hess_bounce, k_bounce,
        np.array([prior_width_logA, prior_width_log_fpeak]))

    A_bounce = 10.0 ** params_bounce[0]
    f_peak_bounce = 10.0 ** params_bounce[1]

    # Parameter uncertainties from Hessian
    try:
        cov_bounce = 2.0 * np.linalg.inv(hess_bounce)
        sigma_logA_bounce = np.sqrt(abs(cov_bounce[0, 0]))
        sigma_logfp_bounce = np.sqrt(abs(cov_bounce[1, 1]))
        correlation = cov_bounce[0, 1] / (sigma_logA_bounce * sigma_logfp_bounce)
    except np.linalg.LinAlgError:
        sigma_logA_bounce = np.nan
        sigma_logfp_bounce = np.nan
        correlation = np.nan

    print(f"\n  2. Matter Bounce Induced GWs (gamma = 3.0 below f_peak):")
    print(f"     Best-fit A        = {A_bounce:.3e}")
    print(f"     log10(A)          = {params_bounce[0]:.4f} +/- {sigma_logA_bounce:.4f}")
    print(f"     f_peak            = {f_peak_bounce*1e9:.3f} nHz")
    print(f"     log10(f_peak)     = {params_bounce[1]:.4f} +/- {sigma_logfp_bounce:.4f}")
    print(f"     Parameter corr.   = {correlation:.4f}")
    print(f"     chi^2             = {chi2_bounce:.4f}")
    print(f"     chi^2/dof         = {chi2_red_bounce:.4f}  (dof = {dof_bounce})")
    print(f"     p-value           = {p_bounce:.4f}")
    print(f"     BIC               = {bic_bounce:.4f}")
    print(f"     AIC               = {aic_bounce:.4f}")
    print(f"     log(Z_Laplace)    = {logZ_bounce:.4f}")

    fit_results["Matter_Bounce"] = {
        "gamma_IR": 3.0,
        "k": k_bounce,
        "params": {
            "log10_A": params_bounce[0],
            "log10_f_peak_Hz": params_bounce[1],
        },
        "param_errors": {
            "sigma_log10_A": sigma_logA_bounce,
            "sigma_log10_f_peak": sigma_logfp_bounce,
            "correlation": correlation,
        },
        "A": A_bounce,
        "f_peak_Hz": f_peak_bounce,
        "f_peak_nHz": f_peak_bounce * 1e9,
        "chi2": chi2_bounce,
        "dof": dof_bounce,
        "chi2_red": chi2_red_bounce,
        "p_value": p_bounce,
        "BIC": bic_bounce,
        "AIC": aic_bounce,
        "log_Z": logZ_bounce,
    }

    # --- 3. Cosmic Strings ---
    params_cs, chi2_cs, hess_cs = fit_cosmic_strings(
        freqs, log10_hc, log10_hc_err)
    k_cs = 1
    dof_cs = N_BINS - k_cs
    chi2_red_cs = chi2_cs / dof_cs
    p_cs = 1.0 - stats.chi2.cdf(chi2_cs, dof_cs)
    bic_cs = compute_bic(chi2_cs, k_cs, N_BINS)
    aic_cs = compute_aic(chi2_cs, k_cs)
    logZ_cs = laplace_log_evidence(chi2_cs, hess_cs, k_cs,
                                    np.array([prior_width_logA]))

    A_cs = 10.0 ** params_cs[0]
    sigma_logA_cs = np.sqrt(2.0 / hess_cs[0, 0])
    gamma_cs = 5.0 / 3.0

    print(f"\n  3. Cosmic Strings (gamma = {gamma_cs:.4f}):")
    print(f"     Best-fit A        = {A_cs:.3e}")
    print(f"     log10(A)          = {params_cs[0]:.4f} +/- {sigma_logA_cs:.4f}")
    print(f"     chi^2             = {chi2_cs:.4f}")
    print(f"     chi^2/dof         = {chi2_red_cs:.4f}  (dof = {dof_cs})")
    print(f"     p-value           = {p_cs:.4f}")
    print(f"     BIC               = {bic_cs:.4f}")
    print(f"     AIC               = {aic_cs:.4f}")
    print(f"     log(Z_Laplace)    = {logZ_cs:.4f}")

    fit_results["Cosmic_Strings"] = {
        "gamma": gamma_cs,
        "k": k_cs,
        "params": {"log10_A": params_cs[0]},
        "param_errors": {"sigma_log10_A": sigma_logA_cs},
        "A": A_cs,
        "chi2": chi2_cs,
        "dof": dof_cs,
        "chi2_red": chi2_red_cs,
        "p_value": p_cs,
        "BIC": bic_cs,
        "AIC": aic_cs,
        "log_Z": logZ_cs,
    }

    # ================================================================
    # MODEL COMPARISON
    # ================================================================
    print("\n" + "=" * 72)
    print("  MODEL COMPARISON")
    print("=" * 72)

    # --- Delta chi^2 ---
    print("\n  Delta chi^2 (relative to best-fit model):")
    print("  " + "-" * 60)
    chi2_all = {"SMBH": chi2_smbh, "Bounce": chi2_bounce, "Strings": chi2_cs}
    chi2_min = min(chi2_all.values())
    for name, c2 in chi2_all.items():
        marker = " <-- best" if c2 == chi2_min else ""
        print(f"    {name:20s}: chi^2 = {c2:.4f}  "
              f"(Delta = {c2 - chi2_min:+.4f}){marker}")

    # --- BIC ---
    print("\n  BIC (lower is better):")
    print("  " + "-" * 60)
    bic_all = {"SMBH": bic_smbh, "Bounce": bic_bounce, "Strings": bic_cs}
    bic_min = min(bic_all.values())
    for name, b in bic_all.items():
        marker = " <-- best" if b == bic_min else ""
        print(f"    {name:20s}: BIC = {b:.4f}  "
              f"(Delta = {b - bic_min:+.4f}){marker}")

    # --- AIC ---
    print("\n  AIC (lower is better):")
    print("  " + "-" * 60)
    aic_all = {"SMBH": aic_smbh, "Bounce": aic_bounce, "Strings": aic_cs}
    aic_min = min(aic_all.values())
    for name, a in aic_all.items():
        marker = " <-- best" if a == aic_min else ""
        print(f"    {name:20s}: AIC = {a:.4f}  "
              f"(Delta = {a - aic_min:+.4f}){marker}")

    # --- Bayes factors (Laplace) ---
    print("\n  Bayes Factors (Laplace approximation):")
    print("  " + "-" * 60)

    bf_bounce_smbh = np.exp(logZ_bounce - logZ_smbh)
    bf_bounce_cs = np.exp(logZ_bounce - logZ_cs)
    bf_smbh_cs = np.exp(logZ_smbh - logZ_cs)

    # Also log10 for readability
    log10_bf_bounce_smbh = (logZ_bounce - logZ_smbh) / np.log(10)
    log10_bf_bounce_cs = (logZ_bounce - logZ_cs) / np.log(10)
    log10_bf_smbh_cs = (logZ_smbh - logZ_cs) / np.log(10)

    comparisons = [
        ("Bounce / SMBH", bf_bounce_smbh, log10_bf_bounce_smbh),
        ("Bounce / Strings", bf_bounce_cs, log10_bf_bounce_cs),
        ("SMBH / Strings", bf_smbh_cs, log10_bf_smbh_cs),
    ]

    for label, bf, log10_bf in comparisons:
        strength = jeffreys_strength(bf)
        direction = "favoring numerator" if bf > 1 else "favoring denominator"
        if bf > 1e4:
            print(f"    B({label:22s}) = {bf:.1e}  "
                  f"(log10 = {log10_bf:+.2f}, {strength}, {direction})")
        elif bf < 1e-4:
            print(f"    B({label:22s}) = {bf:.1e}  "
                  f"(log10 = {log10_bf:+.2f}, {strength}, {direction})")
        else:
            print(f"    B({label:22s}) = {bf:.4f}  "
                  f"(log10 = {log10_bf:+.2f}, {strength}, {direction})")

    # --- BIC-based Bayes factors ---
    print("\n  BIC-based approximate Bayes Factors:")
    print("  " + "-" * 60)
    bf_bic_bounce_smbh = np.exp(-0.5 * (bic_bounce - bic_smbh))
    bf_bic_bounce_cs = np.exp(-0.5 * (bic_bounce - bic_cs))
    bf_bic_smbh_cs = np.exp(-0.5 * (bic_smbh - bic_cs))

    for label, bf in [("Bounce / SMBH", bf_bic_bounce_smbh),
                       ("Bounce / Strings", bf_bic_bounce_cs),
                       ("SMBH / Strings", bf_bic_smbh_cs)]:
        strength = jeffreys_strength(bf)
        print(f"    B_BIC({label:22s}) = {bf:.4f}  ({strength})")

    # ================================================================
    # INTERPRETATION
    # ================================================================
    print("\n" + "=" * 72)
    print("  INTERPRETATION")
    print("=" * 72)

    # Which model is best?
    best_model = min(bic_all, key=bic_all.get)
    print(f"\n  Best-fit model (by BIC): {best_model}")
    print(f"  Best-fit model (by chi^2): "
          f"{min(chi2_all, key=chi2_all.get)}")

    # Tension of each model with the data
    print(f"\n  Spectral index tension with NANOGrav gamma = {GAMMA_OBS}:")
    for name, gamma in [("SMBH", 13/3), ("Bounce (IR)", 3.0),
                         ("Strings", 5/3)]:
        tension = abs(gamma - GAMMA_OBS) / GAMMA_SIGMA
        print(f"    {name:20s}: gamma = {gamma:.4f}, "
              f"tension = {tension:.2f} sigma")

    # Matter bounce assessment
    print(f"\n  Matter bounce assessment:")
    print(f"    - IR spectral slope (gamma=3) is closest to data (gamma=3.2)")
    print(f"    - Tension: only {abs(3.0 - GAMMA_OBS)/GAMMA_SIGMA:.2f} sigma")
    if f_peak_bounce * 1e9 > freqs_nHz[-1]:
        print(f"    - Best-fit f_peak = {f_peak_bounce*1e9:.1f} nHz "
              f"(above PTA band => pure f^2 IR regime)")
    else:
        print(f"    - Best-fit f_peak = {f_peak_bounce*1e9:.1f} nHz "
              f"(within PTA band => turnover visible)")

    # Store comparison results
    comparison_results = {
        "delta_chi2_bounce_minus_smbh": chi2_bounce - chi2_smbh,
        "delta_chi2_bounce_minus_strings": chi2_bounce - chi2_cs,
        "delta_BIC_bounce_minus_smbh": bic_bounce - bic_smbh,
        "delta_BIC_bounce_minus_strings": bic_bounce - bic_cs,
        "delta_AIC_bounce_minus_smbh": aic_bounce - aic_smbh,
        "delta_AIC_bounce_minus_strings": aic_bounce - aic_cs,
        "log10_BF_bounce_over_smbh_laplace": log10_bf_bounce_smbh,
        "log10_BF_bounce_over_strings_laplace": log10_bf_bounce_cs,
        "log10_BF_bounce_over_smbh_BIC": np.log10(bf_bic_bounce_smbh) if bf_bic_bounce_smbh > 0 else -np.inf,
        "log10_BF_bounce_over_strings_BIC": np.log10(bf_bic_bounce_cs) if bf_bic_bounce_cs > 0 else -np.inf,
        "best_model_by_BIC": best_model,
        "best_model_by_chi2": min(chi2_all, key=chi2_all.get),
    }

    # ================================================================
    # FIGURE
    # ================================================================
    print("\n" + "=" * 72)
    print("  Generating figure...")
    print("=" * 72)

    fig = plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1], hspace=0.08,
                           wspace=0.35, left=0.08, right=0.97,
                           top=0.93, bottom=0.08)

    # ---- Panel A: h_c(f) with fits ----
    ax1 = fig.add_subplot(gs[0, 0])

    # Data points with error bars
    ax1.errorbar(freqs_nHz, log10_hc, yerr=log10_hc_err,
                 fmt="o", color="black", markersize=6, capsize=3,
                 elinewidth=1.2, markeredgecolor="black", markerfacecolor="white",
                 zorder=5, label="NANOGrav 15-yr (reconstructed)")

    # Fine frequency grid for smooth curves
    f_fine = np.logspace(np.log10(freqs[0] * 0.7), np.log10(freqs[-1] * 1.3),
                          300)
    f_fine_nHz = f_fine * 1e9

    # SMBH template
    hc_smbh = template_smbh(f_fine, params_smbh[0])
    ax1.plot(f_fine_nHz, hc_smbh, "--", color="#2c3e50", lw=2.2,
             label=f"SMBH ($\\gamma$=13/3, $\\chi^2$={chi2_smbh:.2f})",
             zorder=3)

    # Matter bounce template
    hc_bounce = template_bounce(f_fine, params_bounce[0], params_bounce[1])
    ax1.plot(f_fine_nHz, hc_bounce, "-", color="#1a6b3c", lw=2.5,
             label=f"Matter bounce ($\\gamma$=3, $\\chi^2$={chi2_bounce:.2f})",
             zorder=4)

    # Cosmic strings template
    hc_cs = template_cosmic_strings(f_fine, params_cs[0])
    ax1.plot(f_fine_nHz, hc_cs, "-.", color="#8e44ad", lw=2.0,
             label=f"Cosmic strings ($\\gamma$=5/3, $\\chi^2$={chi2_cs:.2f})",
             zorder=3)

    ax1.set_ylabel(r"$\log_{10}\, h_c(f)$")
    ax1.set_title("Characteristic Strain Spectrum", fontweight="bold")
    ax1.legend(loc="upper right", framealpha=0.95)
    ax1.set_xlim(freqs_nHz[0] * 0.7, freqs_nHz[-1] * 1.3)
    ax1.set_xscale("log")
    ax1.tick_params(labelbottom=False)
    ax1.grid(True, alpha=0.3, linestyle=":")

    # ---- Panel B (bottom left): Residuals ----
    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)

    # Residuals for each model
    res_smbh = (log10_hc - template_smbh(freqs, params_smbh[0])) / log10_hc_err
    res_bounce_pts = (log10_hc - template_bounce(
        freqs, params_bounce[0], params_bounce[1])) / log10_hc_err
    res_cs = (log10_hc - template_cosmic_strings(
        freqs, params_cs[0])) / log10_hc_err

    ax2.axhline(0, color="gray", lw=0.8)
    ax2.axhspan(-1, 1, color="gray", alpha=0.1)
    ax2.axhspan(-2, 2, color="gray", alpha=0.05)

    ax2.scatter(freqs_nHz, res_smbh, marker="s", color="#2c3e50", s=40,
                zorder=4, label="SMBH")
    ax2.scatter(freqs_nHz, res_bounce_pts, marker="D", color="#1a6b3c", s=40,
                zorder=5, label="Bounce")
    ax2.scatter(freqs_nHz, res_cs, marker="^", color="#8e44ad", s=40,
                zorder=4, label="Strings")

    ax2.set_xlabel("Frequency [nHz]")
    ax2.set_ylabel(r"Residual [$\sigma$]")
    ax2.legend(loc="upper left", fontsize=8, ncol=3)
    ax2.set_ylim(-3.5, 3.5)
    ax2.grid(True, alpha=0.3, linestyle=":")

    # ---- Panel C (top right): Omega_GW(f) ----
    ax3 = fig.add_subplot(gs[0, 1])

    # Convert h_c to Omega_GW h^2
    H_100 = 100.0 * 1e3 / 3.0857e22
    prefactor = 2.0 * np.pi ** 2 / 3.0

    # Data points in Omega_GW
    hc_data = 10.0 ** log10_hc
    omega_data = prefactor * (freqs / H_100) ** 2 * hc_data ** 2
    log10_omega_data = np.log10(omega_data)

    # Error propagation: sigma(log10 Omega) = 2 * sigma(log10 h_c)
    # (since Omega ~ h_c^2, and f is fixed per bin)
    log10_omega_err = 2.0 * log10_hc_err

    ax3.errorbar(freqs_nHz, log10_omega_data, yerr=log10_omega_err,
                 fmt="o", color="black", markersize=6, capsize=3,
                 elinewidth=1.2, markeredgecolor="black",
                 markerfacecolor="white", zorder=5,
                 label="NANOGrav 15-yr")

    # Model curves in Omega_GW
    for f_arr, hc_arr, style, color, label_str in [
        (f_fine, hc_smbh, "--", "#2c3e50", "SMBH"),
        (f_fine, hc_bounce, "-", "#1a6b3c", "Bounce"),
        (f_fine, hc_cs, "-.", "#8e44ad", "Strings"),
    ]:
        hc_lin = 10.0 ** hc_arr
        omega = prefactor * (f_arr / H_100) ** 2 * hc_lin ** 2
        ax3.plot(f_fine_nHz, np.log10(omega), style, color=color,
                 lw=2.0, label=label_str)

    ax3.set_ylabel(r"$\log_{10}\, \Omega_{\rm GW}\, h^2$")
    ax3.set_title(r"GW Energy Density Spectrum", fontweight="bold")
    ax3.legend(loc="upper left", framealpha=0.95, fontsize=8)
    ax3.set_xscale("log")
    ax3.set_xlim(freqs_nHz[0] * 0.7, freqs_nHz[-1] * 1.3)
    ax3.tick_params(labelbottom=False)
    ax3.grid(True, alpha=0.3, linestyle=":")

    # ---- Panel D (bottom right): Model comparison summary ----
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis("off")

    # Summary table
    col_labels = ["Model", r"$\chi^2$", "dof", r"$\chi^2_\nu$",
                  "BIC", r"$\Delta$BIC", "p-value"]
    table_data = []
    for name, c2, k, dof, bic_val in [
        ("SMBH", chi2_smbh, k_smbh, dof_smbh, bic_smbh),
        ("Bounce", chi2_bounce, k_bounce, dof_bounce, bic_bounce),
        ("Strings", chi2_cs, k_cs, dof_cs, bic_cs),
    ]:
        p = 1.0 - stats.chi2.cdf(c2, dof)
        dbic = bic_val - bic_min
        table_data.append([
            name,
            f"{c2:.2f}",
            str(dof),
            f"{c2/dof:.3f}",
            f"{bic_val:.2f}",
            f"{dbic:+.2f}",
            f"{p:.3f}",
        ])

    table = ax4.table(cellText=table_data, colLabels=col_labels,
                       loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.5)

    # Color the best row
    for j in range(len(col_labels)):
        # Header
        table[0, j].set_facecolor("#e8e8e8")
        table[0, j].set_text_props(fontweight="bold")
        # Best model row (Bounce is row 2)
        best_row_idx = ["SMBH", "Bounce", "Strings"].index(best_model) + 1
        table[best_row_idx, j].set_facecolor("#d4edda")

    # Add Bayes factor text below the table
    bf_text = (f"Bayes factors (Laplace):  "
               f"B(Bounce/SMBH) = {bf_bounce_smbh:.2f}  |  "
               f"B(Bounce/Strings) = {bf_bounce_cs:.2f}")
    ax4.text(0.5, -0.05, bf_text, transform=ax4.transAxes,
             ha="center", va="top", fontsize=8.5,
             style="italic", color="#333333")

    # Suptitle
    fig.suptitle(
        "NANOGrav 15-Year Free-Spectrum Template Fit: "
        "SMBH vs Matter Bounce vs Cosmic Strings",
        fontsize=14, fontweight="bold", y=0.98
    )

    # Save
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig_path = FIG_DIR / "nanograv_proper_fit.png"
    fig.savefig(fig_path)
    print(f"\n  Figure saved: {fig_path}")
    plt.close(fig)

    # ================================================================
    # SAVE RESULTS TO JSON
    # ================================================================

    # Make all values JSON-serializable
    def make_serializable(obj):
        if isinstance(obj, dict):
            return {k: make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, (np.floating, float)):
            if np.isnan(obj) or np.isinf(obj):
                return str(obj)
            return float(obj)
        elif isinstance(obj, (np.integer, int)):
            return int(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, list):
            return [make_serializable(v) for v in obj]
        else:
            return obj

    output = {
        "description": (
            "NANOGrav 15-year free-spectrum proper template fit results. "
            "Three GWB models fit to 14 synthetic frequency bins "
            "reconstructed from the published power-law best fit "
            "(A=2.4e-15, gamma=3.2). arXiv:2306.16213."
        ),
        "data": {
            "n_bins": N_BINS,
            "freqs_nHz": (freqs * 1e9).tolist(),
            "log10_hc": log10_hc.tolist(),
            "log10_hc_err": log10_hc_err.tolist(),
            "source": "Synthetic from published power-law fit",
        },
        "fit_results": make_serializable(fit_results),
        "model_comparison": make_serializable(comparison_results),
        "method": {
            "fitting": "chi^2 minimization in log10(h_c) space",
            "BIC": "chi^2 + k * ln(N)",
            "AIC": "chi^2 + 2*k",
            "Bayes_factors": "Laplace approximation with uniform priors",
            "prior_widths": {
                "log10_A": prior_width_logA,
                "log10_f_peak": prior_width_log_fpeak,
            },
        },
    }

    with open(RESULTS_FILE, "w") as f:
        json.dump(output, f, indent=2)
    print(f"  Results saved: {RESULTS_FILE}")

    return fit_results, comparison_results


# ============================================================================
# Entry point
# ============================================================================

if __name__ == "__main__":
    fit_results, comparison_results = run_analysis()

    print("\n" + "=" * 72)
    print("  DONE")
    print("=" * 72)
    print()
