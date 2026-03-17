"""
Build the primordial curvature power spectrum P_R(k).

Model: CMB power-law + Gaussian bump

  P_R(k) = A_cmb (k/k_*)^{n_s - 1}  +  A_b exp[ -ln^2(k/k_b) / (2 s_k^2) ]

For PBH formation scales the CMB term is negligible, so the bump
dominates.  Chain 1A samples {log10(A_b), log10(M_b/g), s_k}.
"""

import numpy as np

# CMB baseline
A_CMB = 2.1e-9
N_S = 0.965
K_PIVOT = 0.05  # Mpc^{-1}


def pr_spectrum(k, A_b, k_b, s_k):
    """Full P_R(k) = CMB baseline + Gaussian bump.

    Parameters
    ----------
    k : array, comoving wavenumber in Mpc^{-1}
    A_b : float, bump amplitude
    k_b : float, bump centre in Mpc^{-1}
    s_k : float, bump width in ln(k)

    Returns
    -------
    P_R : array, same shape as k
    """
    cmb = A_CMB * (k / K_PIVOT) ** (N_S - 1)
    bump = A_b * np.exp(-np.log(k / k_b) ** 2 / (2 * s_k ** 2))
    return cmb + bump
