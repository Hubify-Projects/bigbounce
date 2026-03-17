"""
Compute the smoothed density-contrast variance sigma^2(R) during
radiation domination.

  sigma_delta^2(R) = int d ln q  W_G^2(qR)  (16/81) (qR)^4  P_R(q)

with the Gaussian window  W_G(x) = exp(-x^2 / 2).

Also provides the horizon-mass <-> wavenumber mapping.
"""

import numpy as np
from scipy.integrate import quad

# ---- physical constants (CGS / natural) --------------------------------
G_CGS = 6.674e-8          # cm^3 g^{-1} s^{-2}
C_CGS = 2.998e10           # cm s^{-1}
M_SUN_G = 1.989e33         # g
MPC_CM = 3.086e24          # cm

# Equality-era quantities (standard cosmology)
M_H_EQ = 2.8e17 * M_SUN_G           # horizon mass at equality, in grams
K_EQ = 0.01                          # Mpc^{-1}, approximate equality scale
G_STAR_EQ = 3.36                      # effective relativistic dof at equality

# ---- horizon-mass <-> wavenumber mapping --------------------------------

def k_to_M_H(k, g_star=106.75):
    """Horizon mass at re-entry during radiation domination.

    M_H(k) = (3/2) M_{H,eq} (k_eq / k)^2 (g_{*,eq}/g_*)^{1/3}

    Parameters
    ----------
    k : float or array, comoving wavenumber in Mpc^{-1}
    g_star : float, effective relativistic dof at re-entry

    Returns
    -------
    M_H : float or array, horizon mass in grams
    """
    return 1.5 * M_H_EQ * (K_EQ / k) ** 2 * (G_STAR_EQ / g_star) ** (1.0 / 3)


def M_H_to_k(M_H, g_star=106.75):
    """Inverse: horizon mass → wavenumber."""
    return K_EQ * np.sqrt(1.5 * M_H_EQ / M_H * (G_STAR_EQ / g_star) ** (1.0 / 3))


def M_H_solar(M_H_grams):
    """Convert grams to solar masses."""
    return M_H_grams / M_SUN_G


# ---- smoothed variance -------------------------------------------------

def sigma2_gaussian(R, pr_func, k_min=1e-4, k_max=1e25, npts=4000):
    """Compute sigma_delta^2(R) using Gaussian window.

    sigma^2(R) = int d ln q  exp(-(qR)^2) (16/81)(qR)^4 P_R(q)

    Parameters
    ----------
    R : float, smoothing scale in Mpc (= 1/k_b for horizon crossing)
    pr_func : callable, P_R(k) taking array of k in Mpc^{-1}
    k_min, k_max : integration limits in Mpc^{-1}
    npts : number of log-spaced quadrature points

    Returns
    -------
    sigma2 : float
    """
    ln_q = np.linspace(np.log(k_min), np.log(k_max), npts)
    q = np.exp(ln_q)
    x = q * R
    # Gaussian window squared
    W2 = np.exp(-x ** 2)
    # radiation-era transfer: (16/81)(qR)^4
    transfer = (16.0 / 81.0) * x ** 4
    # integrand in d ln q
    integrand = W2 * transfer * pr_func(q)
    return np.trapezoid(integrand, ln_q)


def sigma_H(k_b, pr_func, **kwargs):
    """Convenience: sigma at horizon scale R_H = 1/k_b."""
    return np.sqrt(sigma2_gaussian(1.0 / k_b, pr_func, **kwargs))
