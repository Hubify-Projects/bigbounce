"""
PBH exclusion pseudo-likelihood for Chain 1A.

These are exclusion curves, NOT Gaussian measurements.

For each compiled monochromatic upper bound f^mono_{i,max}(M),
compute the integrated constraint test:

  I_i(theta) = int d ln M  f_PBH(theta) * psi(M; theta) / f^mono_{i,max}(M)

Require I_i <= 1.  Soften into a hinge penalty:

  -2 ln L_PBH = sum_i [ max(0, I_i - 1) / epsilon ]^2

with epsilon ~ 0.05-0.1 so the sampler doesn't bounce off hard walls.
"""

import numpy as np
from bounds_loader import load_all_bounds

EPSILON = 0.05  # softening scale for hinge penalty


def integrated_constraint(f_pbh, M_arr, psi_arr, log10_M_bound, log10_f_bound):
    """Compute I_i for a single constraint channel.

    Parameters
    ----------
    f_pbh : float, total f_PBH = Omega_PBH / Omega_CDM
    M_arr : array, PBH mass grid in grams
    psi_arr : array, normalized mass function evaluated on M_arr
    log10_M_bound : array, constraint mass points (log10 grams)
    log10_f_bound : array, constraint f_max points (log10)

    Returns
    -------
    I : float, integrated constraint ratio
    """
    ln_M = np.log(M_arr)

    # Interpolate the monochromatic bound onto our mass grid
    log10_M_grid = np.log10(M_arr)
    log10_f_max = np.interp(log10_M_grid, log10_M_bound, log10_f_bound,
                            left=0.0, right=0.0)
    f_max = 10.0 ** log10_f_max

    # Avoid division by zero
    f_max = np.maximum(f_max, 1e-30)

    # Integrand: f_PBH * psi(M) / f_max(M)
    integrand = f_pbh * psi_arr / f_max

    return np.trapezoid(integrand, ln_M)


def log_likelihood_pbh(f_pbh, M_arr, psi_arr, epsilon=EPSILON):
    """Compute -2 ln L_PBH from all constraint channels.

    Parameters
    ----------
    f_pbh : float, total f_PBH
    M_arr : array, PBH mass grid in grams
    psi_arr : array, normalized mass function on M_arr
    epsilon : float, softening scale

    Returns
    -------
    neg2lnL : float, -2 ln L (0 if all constraints satisfied)
    violations : dict, {label: I_i} for each channel
    """
    bounds = load_all_bounds()
    neg2lnL = 0.0
    violations = {}

    for log_M, log_f, label in bounds:
        I_i = integrated_constraint(f_pbh, M_arr, psi_arr, log_M, log_f)
        violations[label] = I_i
        if I_i > 1.0:
            neg2lnL += ((I_i - 1.0) / epsilon) ** 2

    return neg2lnL, violations


def is_viable(f_pbh, M_arr, psi_arr):
    """Quick check: does this point satisfy all constraints?

    Returns True if all I_i <= 1.
    """
    _, violations = log_likelihood_pbh(f_pbh, M_arr, psi_arr)
    return all(v <= 1.0 for v in violations.values())
