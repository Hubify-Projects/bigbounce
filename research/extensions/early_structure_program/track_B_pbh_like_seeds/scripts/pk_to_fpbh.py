#!/usr/bin/env python3
"""
Track B (optional): P(k) -> beta(M) -> f_PBH Mapping
======================================================

Shows how a primordial power spectrum enhancement maps to PBH abundance:

1. Collapse fraction:
       beta(M) ~ erfc(delta_c / (sqrt(2) * sigma(M)))

2. For radiation domination with a delta-function P(k) bump:
       sigma^2(M) ~ (4/9) * A_bump

3. PBH dark matter fraction:
       f_PBH(M) ~ beta(M) * (M_eq / M)^{1/2}

   where M_eq ~ 2.8e17 M_sun is the horizon mass at matter-radiation equality.

This script computes and plots the required power spectrum amplitude A_bump
as a function of PBH mass M for target f_PBH levels.

References
----------
- Press & Schechter 1974
- Carr et al. 2021, arXiv: 2002.12778
- Green & Kavanagh 2021, arXiv: 2007.10722
"""

import os
import numpy as np
from scipy.special import erfcinv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------
DELTA_C = 0.45          # critical overdensity for PBH formation (rad. dom.)
M_EQ = 2.8e17           # horizon mass at equality [M_sun]

# Horizon mass as function of scale: M_H ~ M_sun * (k / 7e13 Mpc^{-1})^{-2}
# at radiation domination entry
# Equivalently: k ~ 7e13 * (M / M_sun)^{-1/2} Mpc^{-1}


def beta_from_sigma(sigma):
    """
    Press-Schechter collapse fraction.

    beta = erfc(delta_c / (sqrt(2) * sigma))

    Parameters
    ----------
    sigma : float or array
        RMS density fluctuation on mass scale M.

    Returns
    -------
    beta : float or array
        Collapse fraction.
    """
    from scipy.special import erfc
    arg = DELTA_C / (np.sqrt(2.0) * sigma)
    return erfc(arg)


def fpbh_from_beta(beta, M):
    """
    Convert collapse fraction to present-day DM fraction.

    f_PBH ~ beta * (M_eq / M)^{1/2}

    This is an order-of-magnitude relation valid for radiation-domination
    formation.

    Parameters
    ----------
    beta : float or array
        Collapse fraction at formation.
    M : float or array
        PBH mass [M_sun].

    Returns
    -------
    f_PBH : float or array
    """
    return beta * np.sqrt(M_EQ / M)


def sigma_from_A_bump(A_bump):
    """
    RMS fluctuation from delta-function P(k) enhancement.

    sigma^2 = (4/9) * A_bump  (radiation domination, delta-function limit)

    Parameters
    ----------
    A_bump : float or array
        Amplitude of the P(k) enhancement.

    Returns
    -------
    sigma : float or array
    """
    return np.sqrt((4.0 / 9.0) * A_bump)


def required_A_bump(f_target, M):
    """
    Compute the required P(k) amplitude A_bump to achieve f_PBH = f_target
    at mass M.

    Inverts: f_PBH = erfc(delta_c / (sqrt(2) sigma)) * sqrt(M_eq/M)
             sigma = sqrt(4/9 * A_bump)

    Parameters
    ----------
    f_target : float
        Target PBH DM fraction.
    M : float or array
        PBH mass [M_sun].

    Returns
    -------
    A_bump : float or array
        Required power spectrum amplitude.
    """
    from scipy.special import erfcinv as erfinvc
    # beta needed
    beta_needed = f_target / np.sqrt(M_EQ / M)
    # Clip to valid range for erfcinv
    beta_needed = np.clip(beta_needed, 1e-300, 2.0 - 1e-15)
    # sigma needed: erfc(delta_c / (sqrt(2)*sigma)) = beta
    # => delta_c / (sqrt(2)*sigma) = erfcinv(beta)
    # => sigma = delta_c / (sqrt(2) * erfcinv(beta))
    ei = erfinvc(beta_needed)
    # Guard against erfcinv returning 0 or negative
    ei = np.maximum(ei, 1e-30)
    sigma_needed = DELTA_C / (np.sqrt(2.0) * ei)
    # A_bump = (9/4) * sigma^2
    return (9.0 / 4.0) * sigma_needed**2


def plot_pk_to_fpbh():
    """Plot required A_bump vs M_PBH for several f_PBH target levels."""
    M_arr = np.logspace(-18, 6, 500)  # M_sun
    f_targets = [1e-3, 1e-5, 1.0]
    colors = ["#F44336", "#2196F3", "#4CAF50"]
    labels = ["$f_{\\rm PBH} = 10^{-3}$",
              "$f_{\\rm PBH} = 10^{-5}$",
              "$f_{\\rm PBH} = 1$"]

    fig, ax = plt.subplots(figsize=(10, 6))

    for ft, color, label in zip(f_targets, colors, labels):
        A = required_A_bump(ft, M_arr)
        # Filter out unphysical values
        valid = (A > 1e-10) & (A < 1e2) & np.isfinite(A)
        ax.loglog(M_arr[valid], A[valid], lw=2.5, color=color, label=label)

    # SMBH seed window
    ax.axvspan(1e3, 1e6, color="#FFD700", alpha=0.2, zorder=0,
               label="SMBH seed window")

    # CMB normalization reference
    ax.axhline(2.1e-9, color="gray", ls=":", lw=1.5, alpha=0.7)
    ax.text(1e-17, 3e-9, "CMB normalization $A_s \\approx 2.1 \\times 10^{-9}$",
            fontsize=9, color="gray")

    # Formatting
    ax.set_xlabel("PBH mass $M$ [$M_\\odot$]", fontsize=13)
    ax.set_ylabel("Required $\\mathcal{P}(k)$ amplitude $A_{\\rm bump}$",
                  fontsize=13)
    ax.set_title("Primordial Power Spectrum Enhancement for PBH Production",
                 fontsize=14, fontweight="bold")
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(1e-4, 1e1)
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    ax.grid(True, alpha=0.2, which="both")

    fig.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, "pk_to_fpbh_mapping.pdf")
    fig.savefig(outpath, bbox_inches="tight", dpi=200)
    fig.savefig(outpath.replace(".pdf", ".png"), bbox_inches="tight", dpi=200)
    print(f"  Saved: {outpath}")
    plt.close(fig)


def main():
    print("Track B (optional): P(k) -> f_PBH Mapping")
    print("=" * 50)
    print("\nGenerating P(k) amplitude plot ...")
    plot_pk_to_fpbh()
    print("\nDone. Outputs in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
