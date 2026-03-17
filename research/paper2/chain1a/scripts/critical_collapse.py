"""
PBH mass spectrum from Gaussian Press-Schechter + critical collapse.

Fixed-time approximation valid for narrow spectral bumps.

Collapse fraction (formation rate):
  beta(M_H) = (1/2) erfc(delta_c / (sqrt(2) sigma_H))

Critical-collapse mass relation:
  M_PBH = K_c  M_H  (delta - delta_c)^{gamma_c}

=> differential mass spectrum (change of variables from delta to M):
  d beta / d ln M  =  (K_c / (gamma_c sqrt(2 pi) sigma_H))
      * (M / (K_c M_H))^{1 + 1/gamma_c}
      * exp[ -(delta_c + (M/(K_c M_H))^{1/gamma_c})^2 / (2 sigma_H^2) ]

Present-day abundance:
  f_PBH = (1/Omega_CDM) int d ln M  (M_eq/M)^{1/2} beta(M)
"""

import numpy as np
from scipy.special import erfc

# ---- benchmark parameters (Chain 1A: fixed) ----------------------------
DELTA_C = 0.45     # collapse threshold, radiation domination
K_C = 3.0          # critical-collapse mass prefactor
GAMMA_C = 0.36     # critical-collapse exponent

# ---- cosmological constants --------------------------------------------
OMEGA_CDM = 0.265
M_EQ_GRAMS = 2.8e17 * 1.989e33  # horizon mass at equality in grams


def beta_total(sigma_H, delta_c=DELTA_C):
    """Total collapse fraction (integrated over all delta > delta_c)."""
    if sigma_H <= 0:
        return 0.0
    arg = delta_c / (np.sqrt(2) * sigma_H)
    if arg > 8:
        return 0.0
    return 0.5 * erfc(arg)


def dbeta_dlnM(M, M_H, sigma_H, delta_c=DELTA_C, K_c=K_C, gamma_c=GAMMA_C):
    """Differential collapse rate d beta / d ln M.

    Parameters
    ----------
    M : array, PBH mass in grams
    M_H : float, horizon mass in grams (sets the scale)
    sigma_H : float, smoothed variance at horizon scale
    delta_c, K_c, gamma_c : collapse parameters

    Returns
    -------
    dbdlnM : array, same shape as M
    """
    x = M / (K_c * M_H)
    # Only masses M < K_c * M_H * (some large delta) make sense
    # but we compute everywhere and let the exponential kill large M
    delta_of_M = delta_c + x ** (1.0 / gamma_c)
    prefactor = K_c / (gamma_c * np.sqrt(2 * np.pi) * sigma_H)
    power_term = x ** (1.0 + 1.0 / gamma_c)
    exp_term = np.exp(-delta_of_M ** 2 / (2 * sigma_H ** 2))
    return prefactor * power_term * exp_term


def fpbh_total(M_H, sigma_H, delta_c=DELTA_C, K_c=K_C, gamma_c=GAMMA_C,
               npts=500):
    """Total dark matter fraction f_PBH = Omega_PBH / Omega_CDM.

    f_PBH = (1/Omega_CDM) int d ln M  (M_eq/M)^{1/2}  d beta/d ln M

    Parameters
    ----------
    M_H : float, horizon mass in grams
    sigma_H : float, smoothed variance at horizon scale
    npts : int, quadrature points

    Returns
    -------
    f_pbh : float
    psi : callable, normalized mass function psi(M)
    """
    # Mass range: from very small to K_c * M_H * (generous upper delta)
    ln_M_min = np.log(1e-5 * K_c * M_H)
    ln_M_max = np.log(K_c * M_H * 100)  # well above delta_c
    ln_M = np.linspace(ln_M_min, ln_M_max, npts)
    M = np.exp(ln_M)

    db = dbeta_dlnM(M, M_H, sigma_H, delta_c, K_c, gamma_c)
    # redshift factor: (M_eq/M)^{1/2}
    redshift_factor = np.sqrt(M_EQ_GRAMS / M)

    integrand = redshift_factor * db
    f_pbh = np.trapezoid(integrand, ln_M) / OMEGA_CDM

    # Normalized mass function
    psi_unnorm = db  # d beta / d ln M
    norm = np.trapezoid(psi_unnorm, ln_M)
    if norm > 0:
        def psi_func(m):
            return np.interp(np.log(m), ln_M, psi_unnorm / norm)
    else:
        def psi_func(m):
            return np.zeros_like(m)

    return f_pbh, psi_func, M, db


def fpbh_density(M_arr, M_H, sigma_H, delta_c=DELTA_C, K_c=K_C,
                 gamma_c=GAMMA_C):
    """Compute f_PBH(M) per log mass bin (for constraint comparison).

    Returns d f_PBH / d ln M evaluated at each M in M_arr.
    """
    db = dbeta_dlnM(M_arr, M_H, sigma_H, delta_c, K_c, gamma_c)
    redshift_factor = np.sqrt(M_EQ_GRAMS / M_arr)
    return redshift_factor * db / OMEGA_CDM
