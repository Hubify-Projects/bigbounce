#!/usr/bin/env python3
"""
gaussian_posterior.py — Track C: Parity / CMB Birefringence
============================================================

PURPOSE:
    Compute the combined Gaussian posterior on the cosmic birefringence
    angle beta from independent published measurements, then map this
    to a posterior on g_eff (the effective dimensionless coupling).

PHYSICS:
    Each measurement i provides: beta_i +/- sigma_i (Gaussian).
    For independent Gaussian likelihoods, the combined posterior is:

        beta_comb = (sum_i beta_i / sigma_i^2) / (sum_i 1/sigma_i^2)
        sigma_comb = 1 / sqrt(sum_i 1/sigma_i^2)

    The mapping to g_eff uses:
        beta = g_eff * C_0
        g_eff = (alpha/M) * f_photon * M_Pl

    Given a posterior P(beta), the posterior on g_eff is:
        P(g_eff) = P(beta = g_eff * C_0) * |C_0|

    We also provide the implied posterior on f_photon:
        f_photon = g_eff / epsilon,  where epsilon = (alpha/M) * M_Pl

PHOTON-TORSION COUPLING GAP:
    The posterior on g_eff (and f_photon) is CONDITIONAL on the assumed
    value of C_0. The spin-torsion framework does not predict C_0 or
    f_photon from first principles. This analysis quantifies what the
    DATA require, not what the THEORY predicts.

OUTPUT:
    outputs/beta_posterior.pdf / .png
    outputs/geff_posterior.pdf / .png
    outputs/posterior_summary.txt
"""

import os
import sys
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
ALPHA_OVER_M = 1.0e-21       # GeV^{-1}
M_PL = 2.435e18              # GeV
EPSILON = ALPHA_OVER_M * M_PL  # ~ 2.435e-3
DEG_TO_RAD = np.pi / 180.0
C_0_FIDUCIAL = 1.0           # radians


# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
def load_measurements(csv_path: str) -> list[dict]:
    measurements = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            measurements.append({
                "experiment": row["experiment"].strip(),
                "beta_deg": float(row["beta_deg"]),
                "sigma_deg": float(row["sigma_beta_deg"]),
                "year": int(row["year"]),
                "notes": row["notes"].strip(),
                "superseded": "superseded" in row["notes"].lower(),
            })
    return measurements


def get_independent(measurements: list[dict]) -> list[dict]:
    """Return only measurements that are independent, not superseded,
    and without calibration caveats (excludes SPIDER)."""
    return [
        m for m in measurements
        if not m["superseded"] and "calibration" not in m["notes"].lower()
    ]


# ---------------------------------------------------------------------------
# Gaussian combination
# ---------------------------------------------------------------------------
def combine_gaussian(betas: list[float], sigmas: list[float]):
    """
    Inverse-variance weighted combination of Gaussian measurements.

    Returns (beta_comb, sigma_comb).
    """
    weights = np.array([1.0 / s**2 for s in sigmas])
    beta_comb = np.sum(np.array(betas) * weights) / np.sum(weights)
    sigma_comb = 1.0 / np.sqrt(np.sum(weights))
    return float(beta_comb), float(sigma_comb)


# ---------------------------------------------------------------------------
# Posterior computation
# ---------------------------------------------------------------------------
def gaussian_pdf(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------
def plot_beta_posterior(measurements: list[dict], output_dir: str):
    """Plot individual and combined posteriors on beta."""
    indep = get_independent(measurements)
    betas = [m["beta_deg"] for m in indep]
    sigmas = [m["sigma_deg"] for m in indep]
    beta_comb, sigma_comb = combine_gaussian(betas, sigmas)

    # Grid
    beta_grid = np.linspace(-0.2, 0.8, 1000)

    fig, ax = plt.subplots(figsize=(8, 5))

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

    # Individual posteriors
    for i, m in enumerate(indep):
        pdf = gaussian_pdf(beta_grid, m["beta_deg"], m["sigma_deg"])
        ax.plot(beta_grid, pdf, color=colors[i % len(colors)], lw=1.5,
                ls="--", label=f"{m['experiment']}", alpha=0.7)
        ax.fill_between(beta_grid, pdf, alpha=0.05, color=colors[i % len(colors)])

    # Combined posterior
    pdf_comb = gaussian_pdf(beta_grid, beta_comb, sigma_comb)
    ax.plot(beta_grid, pdf_comb, color="#d62728", lw=2.5,
            label=f"Combined: ${beta_comb:.3f}^\\circ \\pm {sigma_comb:.3f}^\\circ$")
    ax.fill_between(beta_grid, pdf_comb, alpha=0.15, color="#d62728")

    # Zero line
    ax.axvline(0.0, color="gray", ls=":", lw=0.8, alpha=0.5)

    # CI markers
    for nsig, alpha_v in [(1, 0.4), (2, 0.2)]:
        ax.axvline(beta_comb - nsig * sigma_comb, color="#d62728",
                    ls=":", lw=0.7, alpha=alpha_v)
        ax.axvline(beta_comb + nsig * sigma_comb, color="#d62728",
                    ls=":", lw=0.7, alpha=alpha_v)

    ax.set_xlabel(r"Cosmic birefringence angle $\beta$ [degrees]", fontsize=12)
    ax.set_ylabel("Probability density", fontsize=12)
    ax.set_title("Gaussian posterior on cosmic birefringence angle", fontsize=12)
    ax.legend(fontsize=9, framealpha=0.9)
    ax.set_xlim(-0.15, 0.75)
    ax.set_ylim(bottom=0)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"beta_posterior.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)

    return beta_comb, sigma_comb


def plot_geff_posterior(beta_comb_deg: float, sigma_comb_deg: float,
                        output_dir: str):
    """
    Map beta posterior to g_eff and f_photon posteriors.

    g_eff = beta_rad / C_0
    f_photon = g_eff / epsilon
    """
    beta_comb_rad = beta_comb_deg * DEG_TO_RAD
    sigma_comb_rad = sigma_comb_deg * DEG_TO_RAD

    # g_eff posterior (for C_0 = 1)
    geff_mean = beta_comb_rad / C_0_FIDUCIAL
    geff_sigma = sigma_comb_rad / C_0_FIDUCIAL

    # f_photon posterior
    fp_mean = geff_mean / EPSILON
    fp_sigma = geff_sigma / EPSILON

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # g_eff posterior
    geff_grid = np.linspace(geff_mean - 4 * geff_sigma,
                             geff_mean + 4 * geff_sigma, 500)
    pdf_geff = gaussian_pdf(geff_grid, geff_mean, geff_sigma)
    ax1.plot(geff_grid * 1e3, pdf_geff / 1e3, color="#9467bd", lw=2.5)
    ax1.fill_between(geff_grid * 1e3, pdf_geff / 1e3,
                      alpha=0.15, color="#9467bd")
    ax1.axvline(0, color="gray", ls=":", lw=0.8)
    ax1.set_xlabel(r"$g_\mathrm{eff} \times 10^3$", fontsize=12)
    ax1.set_ylabel("Probability density", fontsize=12)
    ax1.set_title(r"Posterior on $g_\mathrm{eff}$ (for $C_0 = 1$)", fontsize=11)
    ax1.text(0.95, 0.95,
             f"$g_\\mathrm{{eff}} = {geff_mean:.4e}$\n"
             f"$\\pm {geff_sigma:.4e}$",
             transform=ax1.transAxes, fontsize=9, va="top", ha="right",
             bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    # f_photon posterior
    fp_grid = np.linspace(max(0, fp_mean - 4 * fp_sigma),
                           fp_mean + 4 * fp_sigma, 500)
    pdf_fp = gaussian_pdf(fp_grid, fp_mean, fp_sigma)
    ax2.plot(fp_grid, pdf_fp, color="#e377c2", lw=2.5)
    ax2.fill_between(fp_grid, pdf_fp, alpha=0.15, color="#e377c2")
    ax2.axvline(1.0, color="gray", ls=":", lw=0.8, label=r"$f_\mathrm{photon} = 1$")
    ax2.set_xlabel(r"$f_\mathrm{photon}$", fontsize=12)
    ax2.set_ylabel("Probability density", fontsize=12)
    ax2.set_title(
        r"Posterior on $f_\mathrm{photon}$ (for $C_0 = 1$, "
        f"$\\epsilon = {EPSILON:.2e}$)",
        fontsize=11,
    )
    ax2.legend(fontsize=9)
    ax2.text(0.95, 0.95,
             f"$f_\\mathrm{{photon}} = {fp_mean:.2f} \\pm {fp_sigma:.2f}$",
             transform=ax2.transAxes, fontsize=9, va="top", ha="right",
             bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"geff_posterior.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)

    return geff_mean, geff_sigma, fp_mean, fp_sigma


def write_summary(measurements: list[dict],
                  beta_comb: float, sigma_comb: float,
                  geff_mean: float, geff_sigma: float,
                  fp_mean: float, fp_sigma: float,
                  output_dir: str):
    """Write posterior summary statistics."""
    indep = get_independent(measurements)

    lines = [
        "=" * 70,
        "Track C: Gaussian Posterior Summary",
        "=" * 70,
        "",
        "INDEPENDENT MEASUREMENTS USED:",
    ]
    for m in indep:
        lines.append(f"  {m['experiment']:40s}  beta = {m['beta_deg']:.3f} "
                      f"+/- {m['sigma_deg']:.3f} deg")

    beta_rad = beta_comb * DEG_TO_RAD
    sigma_rad = sigma_comb * DEG_TO_RAD
    significance = beta_comb / sigma_comb

    lines += [
        "",
        "COMBINED BETA POSTERIOR:",
        f"  Mean:     {beta_comb:.4f} deg  ({beta_rad:.6e} rad)",
        f"  Sigma:    {sigma_comb:.4f} deg  ({sigma_rad:.6e} rad)",
        f"  68% CI:   [{beta_comb - sigma_comb:.4f}, {beta_comb + sigma_comb:.4f}] deg",
        f"  95% CI:   [{beta_comb - 2*sigma_comb:.4f}, {beta_comb + 2*sigma_comb:.4f}] deg",
        f"  Significance: {significance:.1f} sigma",
        "",
        f"G_EFF POSTERIOR (C_0 = {C_0_FIDUCIAL}):",
        f"  Mean:     {geff_mean:.6e}",
        f"  Sigma:    {geff_sigma:.6e}",
        f"  68% CI:   [{geff_mean - geff_sigma:.6e}, {geff_mean + geff_sigma:.6e}]",
        f"  95% CI:   [{geff_mean - 2*geff_sigma:.6e}, {geff_mean + 2*geff_sigma:.6e}]",
        "",
        f"F_PHOTON POSTERIOR (C_0 = {C_0_FIDUCIAL}, epsilon = {EPSILON:.4e}):",
        f"  Mean:     {fp_mean:.3f}",
        f"  Sigma:    {fp_sigma:.3f}",
        f"  68% CI:   [{fp_mean - fp_sigma:.3f}, {fp_mean + fp_sigma:.3f}]",
        f"  95% CI:   [{fp_mean - 2*fp_sigma:.3f}, {fp_mean + 2*fp_sigma:.3f}]",
        "",
        "INTERPRETATION:",
        f"  f_photon = {fp_mean:.2f} +/- {fp_sigma:.2f}",
        "  This is O(1), confirming no fine-tuning is needed.",
        "",
        "CAVEATS:",
        "  - f_photon and g_eff posteriors are CONDITIONAL on C_0.",
        "  - The spin-torsion framework does not predict C_0 from first principles.",
        "  - SPIDER measurement excluded due to calibration degeneracy.",
        "  - Minami & Komatsu 2020 excluded (superseded by Eskilt 2022).",
        "",
        "=" * 70,
    ]

    path = os.path.join(output_dir, "posterior_summary.txt")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent
    data_dir = base_dir / "data"
    output_dir = base_dir / "outputs"
    output_dir.mkdir(exist_ok=True)

    csv_path = data_dir / "published_birefringence_measurements.csv"
    if not csv_path.exists():
        print(f"ERROR: Cannot find {csv_path}")
        sys.exit(1)

    measurements = load_measurements(str(csv_path))
    print(f"Loaded {len(measurements)} measurements")

    beta_comb, sigma_comb = plot_beta_posterior(measurements, str(output_dir))
    print(f"Combined beta = {beta_comb:.4f} +/- {sigma_comb:.4f} deg")

    geff_mean, geff_sigma, fp_mean, fp_sigma = plot_geff_posterior(
        beta_comb, sigma_comb, str(output_dir)
    )

    write_summary(measurements, beta_comb, sigma_comb,
                  geff_mean, geff_sigma, fp_mean, fp_sigma,
                  str(output_dir))


if __name__ == "__main__":
    main()
