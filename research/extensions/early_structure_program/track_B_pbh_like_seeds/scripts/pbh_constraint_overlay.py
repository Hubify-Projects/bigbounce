#!/usr/bin/env python3
"""
Track B: PBH Constraint Overlay
================================

Plots approximate upper limits on the primordial black hole (PBH) dark matter
fraction f_PBH as a function of PBH mass from six major observational
constraint channels. The SMBH seed mass window (10^3 -- 10^6 M_sun) is
highlighted to show where PBH-seeded SMBHs could form.

Constraint curves are ILLUSTRATIVE -- approximate piecewise/power-law fits
to published bounds, not exact digitizations. They capture the correct
orders of magnitude and mass ranges from:

- Microlensing (EROS/OGLE): Tisserand et al. 2007, Niikura et al. 2019
- CMB accretion: Ali-Haimoud & Kamionkowski 2017, Serpico et al. 2020
- GW merger rates: LIGO/Virgo/KAGRA O3, Hutsi et al. 2021
- Hawking evaporation: Carr et al. 2010, 2021
- Wide binary disruption: Monroy-Rodriguez & Allen 2014
- Ultra-faint dwarf heating: Brandt 2016, Lu et al. 2021
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Solar mass in grams
M_SUN_G = 1.989e33


def constraint_microlensing():
    """
    Microlensing (EROS + OGLE + Subaru/HSC combined).
    f < ~0.1 for M ~ 10^{-7} to 10 M_sun, weakening at edges.
    """
    log_m = np.array([-8, -7, -6, -4, -2, -1, 0, 0.5, 1, 1.5, 2])
    log_f = np.array([0, -0.3, -0.7, -1.0, -1.0, -1.0, -1.0, -0.8, -0.5, -0.2, 0])
    return 10.0**log_m, 10.0**log_f


def constraint_cmb_accretion():
    """
    CMB spectral distortions / accretion constraints.
    f < ~10^{-3} for M ~ 1 to 10^4 M_sun.
    """
    log_m = np.array([-0.5, 0, 1, 2, 3, 4, 4.5, 5])
    log_f = np.array([0, -1.5, -2.5, -3.0, -3.0, -2.5, -1.5, 0])
    return 10.0**log_m, 10.0**log_f


def constraint_gw_mergers():
    """
    Gravitational wave merger rate constraints (LIGO/Virgo O3).
    f < ~10^{-3} for M ~ 1 to 100 M_sun.
    """
    log_m = np.array([-0.5, 0, 0.5, 1, 1.5, 2, 2.5])
    log_f = np.array([0, -1.0, -2.5, -3.0, -2.5, -1.5, 0])
    return 10.0**log_m, 10.0**log_f


def constraint_hawking():
    """
    Hawking evaporation constraints.
    f < ~10^{-8} for M < 10^{15} g ~ 10^{-18} M_sun.
    Constraint weakens rapidly above this mass.
    """
    # In M_sun
    log_m = np.array([-20, -19, -18, -17.5, -17, -16])
    log_f = np.array([-8, -8, -6, -3, -1, 0])
    return 10.0**log_m, 10.0**log_f


def constraint_wide_binaries():
    """
    Wide binary disruption constraints.
    f < ~0.1 for M ~ 1 to 10^3 M_sun.
    """
    log_m = np.array([0, 0.5, 1, 2, 3, 3.5])
    log_f = np.array([0, -0.5, -1.0, -1.0, -0.5, 0])
    return 10.0**log_m, 10.0**log_f


def constraint_ufd_heating():
    """
    Ultra-faint dwarf galaxy dynamical heating.
    f < ~0.01 for M ~ 10 to 10^5 M_sun.
    """
    log_m = np.array([0.5, 1, 2, 3, 4, 5, 5.5])
    log_f = np.array([0, -1.0, -2.0, -2.0, -2.0, -1.0, 0])
    return 10.0**log_m, 10.0**log_f


def plot_constraint_overlay():
    """Generate the PBH constraint overlay plot."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Define constraints
    constraints = [
        ("Hawking evaporation",  constraint_hawking,       "#9C27B0", "-"),
        ("Microlensing",         constraint_microlensing,   "#2196F3", "-"),
        ("GW mergers",           constraint_gw_mergers,     "#4CAF50", "--"),
        ("Wide binaries",        constraint_wide_binaries,  "#FF9800", "-."),
        ("CMB accretion",        constraint_cmb_accretion,  "#F44336", "-"),
        ("UFD heating",          constraint_ufd_heating,    "#795548", "--"),
    ]

    for label, func, color, ls in constraints:
        m_arr, f_arr = func()
        # Interpolate for smooth curves
        log_m_fine = np.linspace(np.log10(m_arr[0]), np.log10(m_arr[-1]), 300)
        log_f_fine = np.interp(log_m_fine, np.log10(m_arr), np.log10(f_arr))
        ax.plot(10.0**log_m_fine, 10.0**log_f_fine, lw=2.5, color=color,
                ls=ls, label=label, zorder=3)
        # Fill excluded region (above the curve)
        ax.fill_between(10.0**log_m_fine, 10.0**log_f_fine, 1e1,
                        color=color, alpha=0.06, zorder=1)

    # SMBH seed window
    ax.axvspan(1e3, 1e6, color="#FFD700", alpha=0.25, zorder=0,
               label="SMBH seed window")
    ax.text(3e4, 3e-9, "SMBH seed\nwindow", fontsize=11, ha="center",
            va="center", fontweight="bold", color="#B8860B",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF8DC",
                      edgecolor="#B8860B", alpha=0.8))

    # Formatting
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-20, 1e7)
    ax.set_ylim(1e-10, 2)
    ax.set_xlabel("PBH mass $M$ [$M_\\odot$]", fontsize=13)
    ax.set_ylabel("Dark matter fraction $f_{\\rm PBH}$", fontsize=13)
    ax.set_title("PBH Observational Constraints with SMBH Seed Window",
                 fontsize=14, fontweight="bold")
    ax.legend(fontsize=9, loc="lower left", framealpha=0.9)
    ax.grid(True, alpha=0.2, which="both")

    # Reference line
    ax.axhline(1.0, color="gray", ls=":", lw=1, alpha=0.5)
    ax.text(1e-19, 1.2, "$f_{\\rm PBH} = 1$ (all DM)", fontsize=8,
            color="gray")

    fig.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, "pbh_constraint_overlay.pdf")
    fig.savefig(outpath, bbox_inches="tight", dpi=200)
    fig.savefig(outpath.replace(".pdf", ".png"), bbox_inches="tight", dpi=200)
    print(f"  Saved: {outpath}")
    plt.close(fig)


def main():
    print("Track B: PBH Constraint Overlay")
    print("=" * 50)
    print("\nGenerating constraint overlay plot ...")
    plot_constraint_overlay()
    print("\nDone. Outputs in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
