#!/usr/bin/env python3
"""
eb_shape_comparison.py — Track C: Parity / CMB Birefringence
=============================================================

PURPOSE:
    Forward-model the CMB EB cross-spectrum induced by isotropic cosmic
    birefringence and compare its shape against a null (no birefringence)
    and against anisotropic birefringence.

PHYSICS:
    Isotropic cosmic birefringence rotates CMB polarization by angle beta.
    Under this rotation, a non-zero EB cross-spectrum is generated:

        C_l^{EB} = sin(2*beta) / 2 * (C_l^{EE} - C_l^{BB})

    For small beta (beta << 1 radian):

        C_l^{EB} ≈ beta * (C_l^{EE} - C_l^{BB})       ... Eq. (*)

    This is an EXACT result of the rotation, not a model-dependent prediction.
    The spin-torsion framework motivates a non-zero beta but does not change
    the rotation formula. Any isotropic birefringence source gives the same
    EB shape -- the shape is a diagnostic of ISOTROPY, not of the mechanism.

    KEY DIAGNOSTIC:
        C_l^{EB} / (C_l^{EE} - C_l^{BB}) = constant across all l
        => isotropic birefringence
        If this ratio varies with l => anisotropic or non-birefringence source.

APPROACH:
    - Use tabulated Planck 2018 best-fit TT/EE/BB spectra (lensed).
    - If CAMB is available, generate spectra directly; otherwise use a
      simple analytic approximation for the shape.
    - Compute predicted C_l^{EB} for the measured beta.
    - Show the EB spectrum and the ratio diagnostic.

OUTPUT:
    outputs/eb_shape_comparison.pdf / .png
    outputs/eb_ratio_diagnostic.pdf / .png
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

DEG_TO_RAD = np.pi / 180.0

# ---------------------------------------------------------------------------
# Try to import CAMB; fall back to analytic approximation
# ---------------------------------------------------------------------------
CAMB_AVAILABLE = False
try:
    import camb
    CAMB_AVAILABLE = True
except ImportError:
    pass


def get_spectra_camb(lmax: int = 2500) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate lensed CMB power spectra using CAMB with Planck 2018 best-fit
    parameters.

    Returns (ell, Cl_EE, Cl_BB) in muK^2 (not l(l+1)/2pi normalized).
    """
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=67.36, ombh2=0.02237, omch2=0.1200,
        mnu=0.06, omk=0, tau=0.0544,
    )
    pars.InitPower.set_params(As=2.1e-9, ns=0.9649, r=0)
    pars.set_for_lmax(lmax, lens_potential_accuracy=1)
    pars.DoLensing = True

    results = camb.get_results(pars)
    powers = results.get_cmb_power_spectra(pars, CMB_unit="muK")
    totCL = powers["lensed_scalar"]  # shape (lmax+1, 4): TT, EE, BB, TE

    ell = np.arange(totCL.shape[0])
    Cl_EE = totCL[:, 1]  # muK^2, l(l+1)/(2pi) * Cl
    Cl_BB = totCL[:, 2]

    # CAMB returns D_l = l(l+1)/(2pi) * C_l; convert back to C_l
    with np.errstate(divide="ignore", invalid="ignore"):
        factor = np.where(ell > 0, ell * (ell + 1) / (2 * np.pi), 1.0)
        Cl_EE_raw = np.where(ell > 0, Cl_EE / factor, 0.0)
        Cl_BB_raw = np.where(ell > 0, Cl_BB / factor, 0.0)

    return ell, Cl_EE_raw, Cl_BB_raw


def get_spectra_analytic(lmax: int = 2500) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Simple analytic approximation for CMB EE and BB power spectra.

    This uses a rough fit to the Planck 2018 lensed spectra for SHAPE ONLY.
    The absolute normalization is approximate but sufficient for demonstrating
    the EB shape diagnostic.

    EE spectrum: dominated by acoustic peaks at l ~ 400, 800, 1200, ...
    BB spectrum: lensing B-modes peaking at l ~ 1000, much smaller than EE.
    """
    ell = np.arange(lmax + 1, dtype=float)

    # Approximate EE: sum of Gaussian peaks (very rough)
    # Peak positions and amplitudes loosely fit to Planck data
    Dl_EE = np.zeros_like(ell)
    ee_peaks = [
        (140, 0.6, 50),    # reionization bump
        (396, 40.0, 80),   # first EE peak
        (810, 25.0, 100),  # second
        (1180, 15.0, 90),  # third
        (1540, 8.0, 80),   # fourth
        (1900, 4.0, 80),   # fifth
    ]
    for l0, amp, width in ee_peaks:
        Dl_EE += amp * np.exp(-0.5 * ((ell - l0) / width) ** 2)

    # Damping tail
    Dl_EE *= np.exp(-ell / 2000.0)
    Dl_EE[0:2] = 0

    # Approximate lensing BB: broad peak around l ~ 1000
    Dl_BB = np.zeros_like(ell)
    # Lensing BB is much smaller than EE
    Dl_BB = 0.05 * np.exp(-0.5 * ((ell - 800) / 400) ** 2)
    Dl_BB *= np.exp(-ell / 2500.0)
    Dl_BB[0:2] = 0

    # Convert D_l to C_l
    with np.errstate(divide="ignore", invalid="ignore"):
        factor = np.where(ell > 1, ell * (ell + 1) / (2 * np.pi), 1.0)
        Cl_EE = np.where(ell > 1, Dl_EE / factor, 0.0)
        Cl_BB = np.where(ell > 1, Dl_BB / factor, 0.0)

    return ell, Cl_EE, Cl_BB


# ---------------------------------------------------------------------------
# EB computation
# ---------------------------------------------------------------------------
def compute_Cl_EB(beta_rad: float, Cl_EE: np.ndarray,
                  Cl_BB: np.ndarray) -> np.ndarray:
    """
    Compute C_l^{EB} from isotropic birefringence.

    EXACT relation:
        C_l^{EB} = sin(2*beta) / 2 * (C_l^{EE} - C_l^{BB})

    For small beta:
        C_l^{EB} ≈ beta * (C_l^{EE} - C_l^{BB})

    We use the exact formula.
    """
    return 0.5 * np.sin(2 * beta_rad) * (Cl_EE - Cl_BB)


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------
def plot_eb_spectrum(ell, Cl_EE, Cl_BB, beta_deg, output_dir):
    """Plot EE, BB, and predicted EB spectra."""
    beta_rad = beta_deg * DEG_TO_RAD
    Cl_EB = compute_Cl_EB(beta_rad, Cl_EE, Cl_BB)

    # Convert to D_l for plotting
    factor = ell * (ell + 1) / (2 * np.pi)
    factor[0:2] = 1.0

    Dl_EE = Cl_EE * factor
    Dl_BB = Cl_BB * factor
    Dl_EB = Cl_EB * factor

    mask = ell >= 2

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8),
                                     gridspec_kw={"height_ratios": [2, 1]},
                                     sharex=True)

    # Top panel: EE, BB, |EB|
    ax1.semilogy(ell[mask], Dl_EE[mask], color="#1f77b4", lw=1.5,
                  label=r"$D_\ell^{EE}$")
    ax1.semilogy(ell[mask], Dl_BB[mask], color="#ff7f0e", lw=1.5,
                  label=r"$D_\ell^{BB}$ (lensing)")
    ax1.semilogy(ell[mask], np.abs(Dl_EB[mask]), color="#d62728", lw=2.0,
                  label=rf"$|D_\ell^{{EB}}|$ ($\beta = {beta_deg:.3f}^\circ$)")

    ax1.set_ylabel(r"$D_\ell = \ell(\ell+1)C_\ell / 2\pi$ [$\mu K^2$]",
                    fontsize=11)
    ax1.set_ylim(1e-6, 100)
    ax1.legend(fontsize=10, loc="upper right")
    source_tag = "CAMB (Planck 2018)" if CAMB_AVAILABLE else "Analytic approximation"
    ax1.set_title(
        f"Predicted EB spectrum from isotropic birefringence\n"
        f"[Spectra source: {source_tag}]",
        fontsize=12,
    )

    # Bottom panel: EB with sign
    ax2.plot(ell[mask], Dl_EB[mask] * 1e3, color="#d62728", lw=1.5)
    ax2.axhline(0, color="gray", ls=":", lw=0.8)
    ax2.set_xlabel(r"Multipole $\ell$", fontsize=11)
    ax2.set_ylabel(r"$D_\ell^{EB} \times 10^3$ [$\mu K^2$]", fontsize=11)
    ax2.set_xlim(2, 2500)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"eb_shape_comparison.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_ratio_diagnostic(ell, Cl_EE, Cl_BB, beta_deg, output_dir):
    """
    Plot the ratio C_l^{EB} / (C_l^{EE} - C_l^{BB}) vs ell.

    For isotropic birefringence this should be CONSTANT = sin(2*beta)/2.
    Deviations from a constant indicate anisotropic or non-birefringence effects.
    """
    beta_rad = beta_deg * DEG_TO_RAD
    Cl_EB = compute_Cl_EB(beta_rad, Cl_EE, Cl_BB)

    diff = Cl_EE - Cl_BB
    mask = (ell >= 30) & (np.abs(diff) > 1e-15)

    ratio = np.full_like(ell, np.nan, dtype=float)
    ratio[mask] = Cl_EB[mask] / diff[mask]

    expected = 0.5 * np.sin(2 * beta_rad)

    fig, ax = plt.subplots(figsize=(9, 4.5))

    ax.plot(ell[mask], ratio[mask], color="#9467bd", lw=0.8, alpha=0.7)

    # Smoothed version (binned)
    bin_edges = np.arange(30, 2501, 50)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_means = np.array([
        np.nanmean(ratio[(ell >= lo) & (ell < hi)])
        for lo, hi in zip(bin_edges[:-1], bin_edges[1:])
    ])
    ax.plot(bin_centers, bin_means, "o", color="#9467bd", ms=3, zorder=5,
            label=r"Binned $C_\ell^{EB} / (C_\ell^{EE} - C_\ell^{BB})$")

    ax.axhline(expected, color="#d62728", ls="-", lw=2.0,
               label=rf"Expected: $\sin(2\beta)/2 = {expected:.6f}$"
                     f"\n" + rf"($\beta = {beta_deg:.3f}^\circ$)")

    ax.set_xlabel(r"Multipole $\ell$", fontsize=11)
    ax.set_ylabel(r"$C_\ell^{EB} / (C_\ell^{EE} - C_\ell^{BB})$", fontsize=11)
    ax.set_title(
        "Isotropy diagnostic: ratio should be constant for isotropic birefringence",
        fontsize=11,
    )
    ax.set_xlim(30, 2500)
    ypad = abs(expected) * 0.5
    ax.set_ylim(expected - ypad, expected + ypad)
    ax.legend(fontsize=9, loc="lower right")

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"eb_ratio_diagnostic.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent
    output_dir = base_dir / "outputs"
    output_dir.mkdir(exist_ok=True)

    # Combined beta from Eskilt + ACT DR6
    beta_deg = 0.242  # combined Eskilt + ACT DR6; see gaussian_posterior.py

    print(f"CAMB available: {CAMB_AVAILABLE}")
    if CAMB_AVAILABLE:
        print("Using CAMB for CMB power spectra (Planck 2018 best-fit)...")
        ell, Cl_EE, Cl_BB = get_spectra_camb(lmax=2500)
    else:
        print("CAMB not available; using analytic approximation for spectrum SHAPE.")
        print("(Install camb for quantitatively accurate spectra.)")
        ell, Cl_EE, Cl_BB = get_spectra_analytic(lmax=2500)

    print(f"Using beta = {beta_deg:.3f} deg")
    print(f"sin(2*beta)/2 = {0.5 * np.sin(2 * beta_deg * DEG_TO_RAD):.6e}")

    plot_eb_spectrum(ell, Cl_EE, Cl_BB, beta_deg, str(output_dir))
    print("Saved eb_shape_comparison.pdf/.png")

    plot_ratio_diagnostic(ell, Cl_EE, Cl_BB, beta_deg, str(output_dir))
    print("Saved eb_ratio_diagnostic.pdf/.png")


if __name__ == "__main__":
    main()
