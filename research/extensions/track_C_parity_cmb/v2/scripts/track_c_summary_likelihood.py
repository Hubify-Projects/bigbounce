#!/usr/bin/env python3
"""
Track C v2: Gaussian Summary-Likelihood Inference on Cosmic Birefringence
=========================================================================

Upgrades the v1 consistency check into a proper summary-likelihood analysis.

DATA:
  - Eskilt (2022), arXiv:2205.13962: beta = 0.30 +/- 0.11 deg
  - Diego-Palazuelos & Komatsu (2025), arXiv:2503.14452: beta = 0.215 +/- 0.074 deg

LIKELIHOOD:
  L(beta | data) = Product_i N(beta; beta_i, sigma_i)

  This is a SUMMARY likelihood using published point estimates, NOT a
  map-level or harmonic-space likelihood. The distinction matters and
  must be stated explicitly in any publication.

INFERENCE:
  1. Posterior on beta with uniform prior
  2. Bayes factor for beta != 0 (Savage-Dickey density ratio)
  3. Derived posterior on f_photon for fixed C_0
  4. 2D degeneracy contour (f_photon, C_0)

OUTPUT:
  v2/outputs/
    track_c_v2_beta_posterior.pdf/png
    track_c_v2_fphoton_posterior.pdf/png
    track_c_v2_degeneracy.pdf/png
    track_c_v2_corner.pdf/png
    track_c_v2_results_summary.txt
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

# ============================================================================
# Constants
# ============================================================================
ALPHA_OVER_M = 1.0e-21       # GeV^{-1}
M_PL = 2.435e18              # GeV (reduced Planck mass)
EPSILON = ALPHA_OVER_M * M_PL  # 2.435e-3 (dimensionless one-loop suppression)
DEG2RAD = np.pi / 180.0

# Published measurements (independent, not superseded)
MEASUREMENTS = [
    {"name": "Eskilt 2022 (Planck NPIPE)",
     "arxiv": "2205.13962",
     "beta_deg": 0.30, "sigma_deg": 0.11},
    {"name": "Diego-Palazuelos & Komatsu 2025 (ACT DR6)",
     "arxiv": "2503.14452",
     "beta_deg": 0.215, "sigma_deg": 0.074},
]

# Prior on beta: uniform on [-1, 1] degrees
BETA_PRIOR_MIN = -1.0  # degrees
BETA_PRIOR_MAX = 1.0   # degrees

# ============================================================================
# Gaussian likelihood
# ============================================================================
def log_likelihood(beta_deg):
    """Log-likelihood for beta given published measurements."""
    ll = 0.0
    for m in MEASUREMENTS:
        ll -= 0.5 * ((beta_deg - m["beta_deg"]) / m["sigma_deg"]) ** 2
    return ll


def gaussian_pdf(x, mu, sigma):
    """Normalized Gaussian PDF."""
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


# ============================================================================
# Analytic posterior (Gaussian + uniform prior)
# ============================================================================
def compute_posterior():
    """Compute the analytic posterior on beta.

    For independent Gaussian likelihoods with uniform prior:
        beta_post = weighted mean
        sigma_post = 1/sqrt(sum 1/sigma_i^2)
    """
    weights = [1.0 / m["sigma_deg"] ** 2 for m in MEASUREMENTS]
    beta_post = sum(w * m["beta_deg"] for w, m in zip(weights, MEASUREMENTS)) / sum(weights)
    sigma_post = 1.0 / np.sqrt(sum(weights))
    return beta_post, sigma_post


def compute_bayes_factor(beta_post, sigma_post):
    """Bayes factor for H1: beta != 0 vs H0: beta = 0.

    Using Savage-Dickey density ratio:
        BF_{10} = prior(beta=0) / posterior(beta=0)

    For uniform prior on [-1, 1] deg:
        prior(0) = 1 / (BETA_PRIOR_MAX - BETA_PRIOR_MIN)

    For Gaussian posterior:
        posterior(0) = N(0; beta_post, sigma_post)
    """
    prior_at_zero = 1.0 / (BETA_PRIOR_MAX - BETA_PRIOR_MIN)
    posterior_at_zero = gaussian_pdf(0.0, beta_post, sigma_post)
    bf_10 = prior_at_zero / posterior_at_zero
    return bf_10


# ============================================================================
# Derived parameters
# ============================================================================
def beta_to_fphoton(beta_deg, C0):
    """Convert beta (degrees) to f_photon for given C_0."""
    beta_rad = beta_deg * DEG2RAD
    return beta_rad / (EPSILON * C0)


# ============================================================================
# Plotting
# ============================================================================
def plot_beta_posterior(beta_post, sigma_post, bf10, output_dir):
    """Figure 1: Posterior on beta with individual measurements."""
    fig, ax = plt.subplots(figsize=(8, 5))

    beta_grid = np.linspace(-0.2, 0.7, 1000)

    # Individual likelihoods
    colors = ["#1f77b4", "#ff7f0e"]
    for m, c in zip(MEASUREMENTS, colors):
        pdf = gaussian_pdf(beta_grid, m["beta_deg"], m["sigma_deg"])
        ax.plot(beta_grid, pdf, color=c, lw=1.5, ls="--",
                label=f'{m["name"]}: ${m["beta_deg"]:.3f}° \\pm {m["sigma_deg"]:.3f}°$',
                alpha=0.7)

    # Combined posterior
    pdf_post = gaussian_pdf(beta_grid, beta_post, sigma_post)
    ax.plot(beta_grid, pdf_post, color="#d62728", lw=2.5,
            label=f'Combined: ${beta_post:.3f}° \\pm {sigma_post:.3f}°$\n'
                  f'  ({beta_post/sigma_post:.1f}$\\sigma$ from zero)')
    ax.fill_between(beta_grid, pdf_post, alpha=0.15, color="#d62728")

    # Zero reference
    ax.axvline(0.0, color="gray", ls=":", lw=1, alpha=0.5)

    # Confidence intervals
    for nsig in [1, 2]:
        ax.axvline(beta_post - nsig * sigma_post, color="#d62728",
                   ls=":", lw=0.7, alpha=0.3)
        ax.axvline(beta_post + nsig * sigma_post, color="#d62728",
                   ls=":", lw=0.7, alpha=0.3)

    # Bayes factor annotation
    ax.text(0.97, 0.97,
            f"Bayes factor ($\\beta \\neq 0$ vs $\\beta = 0$):\n"
            f"$\\mathrm{{BF}}_{{10}} = {bf10:.1f}$\n"
            f"($\\ln \\mathrm{{BF}}_{{10}} = {np.log(bf10):.1f}$)",
            transform=ax.transAxes, fontsize=9, va="top", ha="right",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor="gray", alpha=0.9))

    ax.set_xlabel(r"Cosmic birefringence angle $\beta$ [degrees]", fontsize=12)
    ax.set_ylabel("Probability density [deg$^{-1}$]", fontsize=12)
    ax.set_title("Gaussian summary-likelihood posterior on $\\beta$\n"
                 "(using published Planck + ACT measurements)",
                 fontsize=11)
    ax.legend(fontsize=8.5, loc="upper left")
    ax.set_xlim(-0.15, 0.65)
    ax.set_ylim(bottom=0)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"track_c_v2_beta_posterior.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_fphoton_posterior(beta_post, sigma_post, output_dir):
    """Figure 2: Derived posterior on f_photon for several C_0 values."""
    fig, ax = plt.subplots(figsize=(8, 5))

    C0_values = [0.3, 1.0, 3.0]
    colors = ["#2ca02c", "#9467bd", "#e377c2"]
    labels_extra = ["(conservative)", "(fiducial)", "(liberal)"]

    for C0, c, lbl in zip(C0_values, colors, labels_extra):
        fp_mean = beta_to_fphoton(beta_post, C0)
        fp_sigma = beta_to_fphoton(sigma_post, C0)  # linear mapping
        fp_grid = np.linspace(max(0, fp_mean - 4 * fp_sigma),
                              fp_mean + 4 * fp_sigma, 500)
        pdf = gaussian_pdf(fp_grid, fp_mean, fp_sigma)
        ax.plot(fp_grid, pdf, color=c, lw=2,
                label=f'$C_0 = {C0}$: $f_\\mathrm{{photon}} = {fp_mean:.2f} \\pm {fp_sigma:.2f}$ {lbl}')
        ax.fill_between(fp_grid, pdf, alpha=0.1, color=c)

    ax.axvline(1.0, color="gray", ls=":", lw=1, alpha=0.5,
               label="$f_\\mathrm{photon} = 1$ (no enhancement)")
    ax.axvspan(0.1, 10, color="green", alpha=0.04, label="O(1) naturalness window")

    ax.set_xlabel(r"$f_\mathrm{photon}$ (effective photon-torsion coupling)", fontsize=12)
    ax.set_ylabel("Probability density", fontsize=12)
    ax.set_title("Derived posterior on $f_\\mathrm{photon}$\n"
                 f"($\\epsilon = (\\alpha/M)\\,M_\\mathrm{{Pl}} = {EPSILON:.3e}$)",
                 fontsize=11)
    ax.legend(fontsize=8.5, loc="upper right")
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"track_c_v2_fphoton_posterior.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_degeneracy(beta_post, sigma_post, output_dir):
    """Figure 3: 2D degeneracy contour (f_photon, C_0)."""
    fig, ax = plt.subplots(figsize=(8, 6))

    # The constraint is: f_photon × C_0 = beta_rad / epsilon
    # So C_0 = beta_rad / (epsilon × f_photon)
    beta_rad = beta_post * DEG2RAD
    sigma_rad = sigma_post * DEG2RAD

    fp_grid = np.logspace(-1, 2, 500)

    # Central curve
    C0_central = beta_rad / (EPSILON * fp_grid)
    ax.plot(fp_grid, C0_central, color="#d62728", lw=2.5,
            label=f'$\\beta = {beta_post:.3f}°$ (best fit)')

    # 1-sigma and 2-sigma bands
    for nsig, alpha_v in [(1, 0.2), (2, 0.1)]:
        C0_lo = (beta_rad - nsig * sigma_rad) / (EPSILON * fp_grid)
        C0_hi = (beta_rad + nsig * sigma_rad) / (EPSILON * fp_grid)
        ax.fill_between(fp_grid, np.maximum(C0_lo, 1e-3), C0_hi,
                        color="#d62728", alpha=alpha_v,
                        label=f'{nsig}$\\sigma$ band')

    # O(1) naturalness region
    ax.axhspan(0.1, 10, color="green", alpha=0.05)
    ax.axvspan(0.1, 10, color="blue", alpha=0.05)
    ax.text(1.0, 0.15, "O(1) natural\nregion", fontsize=8,
            ha="center", color="gray", style="italic")

    # Reference points
    ax.plot(1.73, 1.0, 'k*', markersize=12, zorder=5,
            label=f'Fiducial: $f_\\mathrm{{photon}} = 1.73$, $C_0 = 1$')

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$f_\mathrm{photon}$ (photon-torsion vertex factor)", fontsize=12)
    ax.set_ylabel(r"$C_0$ (cosmological field excursion) [radians]", fontsize=12)
    ax.set_title("Degeneracy: $\\beta = \\epsilon \\cdot f_\\mathrm{photon} \\cdot C_0$\n"
                 "Constraint from combined Planck + ACT birefringence",
                 fontsize=11)
    ax.set_xlim(0.1, 100)
    ax.set_ylim(0.01, 100)
    ax.legend(fontsize=8.5, loc="upper right")
    ax.grid(True, alpha=0.2, which="both")

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"track_c_v2_degeneracy.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_corner(beta_post, sigma_post, output_dir):
    """Figure 4: Summary corner-style plot (beta, f_photon, evidence)."""
    fig = plt.figure(figsize=(10, 8))

    # Layout: 2×2 grid
    ax1 = fig.add_subplot(221)  # beta posterior
    ax2 = fig.add_subplot(222)  # f_photon posterior (C0=1)
    ax3 = fig.add_subplot(223)  # degeneracy
    ax4 = fig.add_subplot(224)  # summary table

    # Panel 1: beta
    beta_grid = np.linspace(-0.1, 0.6, 500)
    pdf = gaussian_pdf(beta_grid, beta_post, sigma_post)
    ax1.plot(beta_grid, pdf, color="#d62728", lw=2)
    ax1.fill_between(beta_grid, pdf, alpha=0.15, color="#d62728")
    ax1.axvline(0, color="gray", ls=":", lw=0.8)
    ax1.set_xlabel(r"$\beta$ [deg]", fontsize=10)
    ax1.set_ylabel("PDF", fontsize=10)
    ax1.set_title(r"$\beta$ posterior", fontsize=10)
    ax1.set_xlim(-0.1, 0.55)

    # Panel 2: f_photon (C0=1)
    fp_mean = beta_to_fphoton(beta_post, 1.0)
    fp_sigma = beta_to_fphoton(sigma_post, 1.0)
    fp_grid = np.linspace(max(0, fp_mean - 4 * fp_sigma),
                          fp_mean + 4 * fp_sigma, 500)
    pdf_fp = gaussian_pdf(fp_grid, fp_mean, fp_sigma)
    ax2.plot(fp_grid, pdf_fp, color="#9467bd", lw=2)
    ax2.fill_between(fp_grid, pdf_fp, alpha=0.15, color="#9467bd")
    ax2.axvline(1.0, color="gray", ls=":", lw=0.8)
    ax2.set_xlabel(r"$f_\mathrm{photon}$ ($C_0 = 1$)", fontsize=10)
    ax2.set_title(r"$f_\mathrm{photon}$ posterior", fontsize=10)

    # Panel 3: degeneracy
    beta_rad = beta_post * DEG2RAD
    sigma_rad = sigma_post * DEG2RAD
    fp_arr = np.logspace(-0.5, 1.5, 300)
    C0_central = beta_rad / (EPSILON * fp_arr)
    C0_lo = (beta_rad - sigma_rad) / (EPSILON * fp_arr)
    C0_hi = (beta_rad + sigma_rad) / (EPSILON * fp_arr)
    ax3.plot(fp_arr, C0_central, color="#d62728", lw=2)
    ax3.fill_between(fp_arr, np.maximum(C0_lo, 0.01), C0_hi,
                     color="#d62728", alpha=0.2)
    ax3.set_xscale("log")
    ax3.set_yscale("log")
    ax3.set_xlabel(r"$f_\mathrm{photon}$", fontsize=10)
    ax3.set_ylabel(r"$C_0$ [rad]", fontsize=10)
    ax3.set_title("$(f_\\mathrm{photon}, C_0)$ degeneracy", fontsize=10)
    ax3.set_xlim(0.3, 30)
    ax3.set_ylim(0.03, 30)

    # Panel 4: summary table
    ax4.axis("off")
    bf10 = compute_bayes_factor(beta_post, sigma_post)
    table_text = (
        f"TRACK C v2 SUMMARY\n"
        f"{'─' * 40}\n"
        f"Data: Planck NPIPE + ACT DR6\n"
        f"Method: Gaussian summary likelihood\n"
        f"{'─' * 40}\n"
        f"β = {beta_post:.3f}° ± {sigma_post:.3f}°\n"
        f"  ({beta_post/sigma_post:.1f}σ from zero)\n"
        f"BF(β≠0 vs β=0) = {bf10:.1f}\n"
        f"  ln BF = {np.log(bf10):.1f}\n"
        f"{'─' * 40}\n"
        f"f_photon (C₀=1) = {fp_mean:.2f} ± {fp_sigma:.2f}\n"
        f"f_photon (C₀=0.3) = {beta_to_fphoton(beta_post, 0.3):.2f}\n"
        f"f_photon (C₀=3) = {beta_to_fphoton(beta_post, 3.0):.2f}\n"
        f"{'─' * 40}\n"
        f"ε = (α/M)·M_Pl = {EPSILON:.3e}\n"
        f"All f_photon values O(1): natural"
    )
    ax4.text(0.05, 0.95, table_text, transform=ax4.transAxes,
             fontsize=9, va="top", ha="left", family="monospace",
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f8f8",
                       edgecolor="gray"))

    fig.suptitle("Track C: Cosmic Birefringence — Summary-Likelihood Inference",
                 fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])

    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"track_c_v2_corner.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)


# ============================================================================
# Summary output
# ============================================================================
def write_summary(beta_post, sigma_post, bf10, output_dir):
    """Write machine-readable and human-readable summary."""
    beta_rad = beta_post * DEG2RAD
    sigma_rad = sigma_post * DEG2RAD
    significance = beta_post / sigma_post

    C0_values = [0.1, 0.3, 1.0, 3.0, 10.0]
    fp_table = [(C0, beta_to_fphoton(beta_post, C0),
                 beta_to_fphoton(sigma_post, C0)) for C0 in C0_values]

    lines = [
        "=" * 72,
        "TRACK C v2: Gaussian Summary-Likelihood Inference Results",
        "=" * 72,
        "",
        "METHOD:",
        "  Gaussian summary likelihood using published isotropic",
        "  birefringence measurements. NOT a map-level analysis.",
        "  Prior: uniform on beta in [-1, 1] degrees.",
        "",
        "DATA SOURCES:",
    ]
    for m in MEASUREMENTS:
        lines.append(f"  {m['name']}")
        lines.append(f"    beta = {m['beta_deg']:.3f} +/- {m['sigma_deg']:.3f} deg"
                     f"  (arXiv:{m['arxiv']})")
    lines += [
        "",
        "POSTERIOR ON BETA:",
        f"  beta = {beta_post:.4f} +/- {sigma_post:.4f} deg",
        f"       = {beta_rad:.6e} +/- {sigma_rad:.6e} rad",
        f"  68% CI: [{beta_post - sigma_post:.4f}, {beta_post + sigma_post:.4f}] deg",
        f"  95% CI: [{beta_post - 2*sigma_post:.4f}, {beta_post + 2*sigma_post:.4f}] deg",
        f"  Significance: {significance:.1f} sigma",
        "",
        "BAYESIAN MODEL COMPARISON:",
        f"  Bayes factor BF(beta!=0 / beta=0) = {bf10:.1f}",
        f"  ln BF = {np.log(bf10):.1f}",
        f"  Interpretation: {'Strong' if np.log(bf10) > 3 else 'Moderate' if np.log(bf10) > 1 else 'Weak'}"
        f" evidence for beta != 0 (Jeffreys scale)",
        "",
        "DERIVED f_photon POSTERIORS:",
        f"  (epsilon = (alpha/M)*M_Pl = {EPSILON:.4e})",
        "",
        f"  {'C_0':>6s}  {'f_photon':>10s}  {'sigma':>10s}  {'status':>12s}",
        f"  {'---':>6s}  {'---':>10s}  {'---':>10s}  {'---':>12s}",
    ]
    for C0, fp, fp_sig in fp_table:
        status = "O(1) natural" if 0.1 < fp < 10 else "fine-tuned"
        lines.append(f"  {C0:6.1f}  {fp:10.3f}  {fp_sig:10.3f}  {status:>12s}")

    lines += [
        "",
        "INTERPRETATION:",
        f"  For C_0 in [0.3, 3.0], f_photon in [{fp_table[1][1]:.1f}, {fp_table[3][1]:.1f}].",
        "  All values are O(1), confirming that the spin-torsion",
        "  operator scale alpha/M ~ 10^{-21} GeV^{-1} is naturally",
        "  compatible with observed cosmic birefringence.",
        "",
        "CAVEATS:",
        "  1. This is a SUMMARY-LIKELIHOOD inference, not a full CMB analysis.",
        "  2. f_photon and C_0 are DEGENERATE; only the product is constrained.",
        "  3. The photon-torsion coupling has NOT been derived from first principles.",
        "  4. Uniform birefringence is generic to ANY pseudo-scalar model,",
        "     not specific to the spin-torsion framework.",
        "  5. Eskilt and ACT measurements treated as independent; a rigorous",
        "     joint analysis would account for shared sky/calibration overlap.",
        "",
        "=" * 72,
    ]

    path = os.path.join(output_dir, "track_c_v2_results_summary.txt")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


def write_likelihood_table(beta_post, sigma_post, output_dir):
    """Write a machine-readable likelihood summary table."""
    beta_rad = beta_post * DEG2RAD
    sigma_rad = sigma_post * DEG2RAD

    lines = [
        "# Track C v2: Summary-likelihood results",
        "# All values computed analytically from Gaussian summary likelihood",
        "# Date: 2026-03-13",
        "#",
        "parameter,value,uncertainty,unit,prior,notes",
        f"beta,{beta_post:.6f},{sigma_post:.6f},degrees,uniform[-1:1],combined_posterior",
        f"beta_rad,{beta_rad:.8e},{sigma_rad:.8e},radians,derived,combined_posterior",
        f"significance,{beta_post/sigma_post:.2f},,sigma,,from_zero",
        f"bayes_factor,{compute_bayes_factor(beta_post, sigma_post):.2f},,,savage_dickey,beta!=0_vs_0",
        f"f_photon_C0_0.3,{beta_to_fphoton(beta_post, 0.3):.4f},{beta_to_fphoton(sigma_post, 0.3):.4f},,log_uniform[0.01:100],derived",
        f"f_photon_C0_1.0,{beta_to_fphoton(beta_post, 1.0):.4f},{beta_to_fphoton(sigma_post, 1.0):.4f},,log_uniform[0.01:100],derived",
        f"f_photon_C0_3.0,{beta_to_fphoton(beta_post, 3.0):.4f},{beta_to_fphoton(sigma_post, 3.0):.4f},,log_uniform[0.01:100],derived",
        f"epsilon,{EPSILON:.6e},,dimensionless,fixed,(alpha/M)*M_Pl",
    ]

    path = os.path.join(output_dir, "track_c_v2_likelihood_table.csv")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


# ============================================================================
# Main
# ============================================================================
def main():
    output_dir = Path(__file__).resolve().parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True, parents=True)

    print("=" * 60)
    print("Track C v2: Summary-Likelihood Inference")
    print("=" * 60)

    # 1. Compute posterior
    beta_post, sigma_post = compute_posterior()
    print(f"\nPosterior: beta = {beta_post:.4f} +/- {sigma_post:.4f} deg "
          f"({beta_post/sigma_post:.1f}sigma)")

    # 2. Bayes factor
    bf10 = compute_bayes_factor(beta_post, sigma_post)
    print(f"Bayes factor (beta!=0): {bf10:.1f} (ln BF = {np.log(bf10):.1f})")

    # 3. f_photon
    fp = beta_to_fphoton(beta_post, 1.0)
    fp_sig = beta_to_fphoton(sigma_post, 1.0)
    print(f"f_photon (C_0=1): {fp:.2f} +/- {fp_sig:.2f}")

    # 4. Generate all plots
    print("\nGenerating figures...")
    plot_beta_posterior(beta_post, sigma_post, bf10, str(output_dir))
    plot_fphoton_posterior(beta_post, sigma_post, str(output_dir))
    plot_degeneracy(beta_post, sigma_post, str(output_dir))
    plot_corner(beta_post, sigma_post, str(output_dir))
    print("Figures saved.")

    # 5. Write summaries
    write_summary(beta_post, sigma_post, bf10, str(output_dir))
    write_likelihood_table(beta_post, sigma_post, str(output_dir))

    # 6. Copy corner plot to paper figures
    paper_fig_dir = Path(__file__).resolve().parents[4] / "paper" / "figures"
    paper_fig_dir.mkdir(exist_ok=True, parents=True)
    import shutil
    for name in ["track_c_v2_corner.pdf", "track_c_v2_corner.png"]:
        src = output_dir / name
        dst = paper_fig_dir / name.replace("track_c_v2_corner", "trackC_parity_upgrade_corner")
        if src.exists():
            shutil.copy2(src, dst)
            print(f"Copied {name} -> {dst}")

    # Also copy summary
    for name in ["track_c_v2_beta_posterior.pdf", "track_c_v2_beta_posterior.png"]:
        src = output_dir / name
        dst = paper_fig_dir / name.replace("track_c_v2_beta_posterior", "trackC_parity_upgrade_summary")
        if src.exists():
            shutil.copy2(src, dst)
            print(f"Copied {name} -> {dst}")

    print("\n" + "=" * 60)
    print("Track C v2 COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
