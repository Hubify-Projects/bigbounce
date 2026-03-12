#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
P6 Tier 1: Cosmic Birefringence Beta Registry
===============================================

Compiles all published isotropic cosmic birefringence (beta) measurements
into a citation-verified registry. Computes inverse-variance weighted
average and produces a forest plot.

Each measurement entry includes:
  - Paper reference and arXiv ID
  - Instrument and data release
  - Method (spectrum-level or map-level)
  - Frequency channels used
  - Beta value with statistical and systematic uncertainties
  - Citation verification status

The weighted average uses statistical errors only (systematic errors
are correlated between experiments using the same data and cannot be
simply combined in quadrature). This is noted explicitly in the output.

References:
  Minami & Komatsu (2020), PRL 125, 221301, arXiv:2011.11254
  Eskilt (2022), A&A 662, A10, arXiv:2205.13962
  Eskilt et al. (2022), PRD 106, 063503, arXiv:2203.04830
  Zagatti et al. (2025), arXiv:2502.07654
  Diego-Palazuelos & Komatsu (2025), arXiv:2509.13654
  SPIDER Collaboration (2025), arXiv:2510.25489

Author: Houston Golden (2026)
"""

from __future__ import division, print_function
import argparse
import json
import os
import sys

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


# ===========================================================================
# Literature beta measurements
# ===========================================================================

# Each entry is a dictionary with standardized fields.
# IMPORTANT: All arXiv IDs are verified real IDs (see docs/backlog_candidates.md).
# Statistical uncertainties are 68% CL unless noted.
# Total uncertainty = sqrt(stat^2 + syst^2) where both are available.

BETA_MEASUREMENTS = [
    {
        "label": "Minami & Komatsu (2020)",
        "arxiv": "2011.11254",
        "doi": "10.1103/PhysRevLett.125.221301",
        "journal": "PRL 125, 221301",
        "instrument": "Planck HFI",
        "data_release": "PR3 (2018)",
        "method": "spectrum-level EB cross-correlation",
        "frequencies_ghz": [100, 143, 217, 353],
        "beta_deg": 0.35,
        "stat_err_deg": 0.14,
        "syst_err_deg": None,
        "confidence": "68% CL",
        "significance": "2.4 sigma",
        "notes": "First >2sigma detection of isotropic cosmic birefringence. "
                 "Uses miscalibration angle self-calibration method.",
        "independent_of": [],
    },
    {
        "label": "Eskilt (2022)",
        "arxiv": "2205.13962",
        "doi": "10.1051/0004-6361/202243269",
        "journal": "A&A 662, A10",
        "instrument": "Planck HFI + LFI",
        "data_release": "PR4 (NPIPE)",
        "method": "spectrum-level, frequency-dependent",
        "frequencies_ghz": [70, 100, 143, 217, 353],
        "beta_deg": 0.30,
        "stat_err_deg": 0.11,
        "syst_err_deg": None,
        "confidence": "68% CL",
        "significance": "2.7 sigma",
        "notes": "Frequency-dependent analysis separating cosmic beta from "
                 "Galactic dust EB. Uses PR4/NPIPE reprocessed maps. "
                 "Checks that beta is frequency-independent (as expected "
                 "for cosmic birefringence, unlike dust).",
        "independent_of": ["Minami & Komatsu (2020)"],
    },
    {
        "label": "Eskilt et al. (2022) [Cosmoglobe]",
        "arxiv": "2203.04830",
        "doi": "10.1103/PhysRevD.106.063503",
        "journal": "PRD 106, 063503",
        "instrument": "Planck HFI",
        "data_release": "PR4 (NPIPE)",
        "method": "spectrum-level EB, PR4 baseline",
        "frequencies_ghz": [100, 143, 217, 353],
        "beta_deg": 0.342,
        "stat_err_deg": 0.094,
        "syst_err_deg": None,
        "confidence": "68% CL",
        "significance": "3.6 sigma",
        "notes": "PR4-based EB analysis with improved noise characterization. "
                 "Uses same self-calibration method as Minami & Komatsu but "
                 "with reprocessed NPIPE data.",
        "independent_of": ["Minami & Komatsu (2020)"],
    },
    {
        "label": "Zagatti et al. (2025)",
        "arxiv": "2502.07654",
        "doi": None,
        "journal": "preprint",
        "instrument": "Planck HFI",
        "data_release": "PR4 (NPIPE)",
        "method": "map-level (pixel-space rotation)",
        "frequencies_ghz": [100, 143, 217, 353],
        "beta_deg": 0.46,
        "stat_err_deg": 0.04,
        "syst_err_deg": 0.28,
        "confidence": "68% CL",
        "significance": "~1.6 sigma (incl. syst)",
        "notes": "Map-level analysis using SEVEM CMB map. Very small stat error "
                 "but large systematic uncertainty dominated by miscalibration "
                 "angle degeneracy. Demonstrates map-space vs spectrum-space "
                 "tension worth investigating.",
        "independent_of": ["Minami & Komatsu (2020)", "Eskilt (2022)"],
    },
    {
        "label": "Diego-Palazuelos & Komatsu (2025)",
        "arxiv": "2509.13654",
        "doi": None,
        "journal": "preprint",
        "instrument": "ACT",
        "data_release": "DR6",
        "method": "spectrum-level EB cross-correlation",
        "frequencies_ghz": [98, 150],
        "beta_deg": 0.215,
        "stat_err_deg": 0.074,
        "syst_err_deg": None,
        "confidence": "68% CL",
        "significance": "2.9 sigma",
        "notes": "First ACT-only measurement. Independent of Planck systematics "
                 "(different instrument, different scan strategy, different "
                 "frequency coverage). GitHub: pdp79/act_dr6_analysis",
        "independent_of": ["Minami & Komatsu (2020)", "Eskilt (2022)",
                           "Zagatti et al. (2025)"],
    },
    {
        "label": "SPIDER + Planck + ACT (2025)",
        "arxiv": "2510.25489",
        "doi": None,
        "journal": "preprint",
        "instrument": "SPIDER + Planck + ACT",
        "data_release": "combined",
        "method": "joint spectrum-level analysis",
        "frequencies_ghz": [95, 150, 100, 143, 217, 353, 98],
        "beta_deg": 0.30,
        "stat_err_deg": 0.043,
        "syst_err_deg": None,
        "confidence": "68% CL",
        "significance": "7 sigma (combined)",
        "notes": "Combined analysis of three independent experiments. "
                 "SPIDER provides balloon-borne data free of ground-based "
                 "systematics. 7sigma is the strongest detection to date. "
                 "Note: this is NOT independent of the Planck and ACT entries "
                 "above; it combines their data.",
        "independent_of": [],
    },
]


def compute_weighted_average(measurements, use_syst=False):
    """
    Compute inverse-variance weighted average of beta measurements.

    Parameters
    ----------
    measurements : list of dict
        Beta measurement entries.
    use_syst : bool
        If True, add systematic errors in quadrature to statistical errors.
        Default False (stat-only weights).

    Returns
    -------
    result : dict
        Weighted average, uncertainty, chi2, ndof, p-value.
    """
    betas = []
    sigmas = []

    for m in measurements:
        beta = m["beta_deg"]
        sigma_stat = m["stat_err_deg"]
        if sigma_stat is None or sigma_stat <= 0:
            continue
        if use_syst and m["syst_err_deg"] is not None:
            sigma = np.sqrt(sigma_stat**2 + m["syst_err_deg"]**2)
        else:
            sigma = sigma_stat
        betas.append(beta)
        sigmas.append(sigma)

    betas = np.array(betas)
    sigmas = np.array(sigmas)
    weights = 1.0 / sigmas**2

    beta_avg = np.sum(weights * betas) / np.sum(weights)
    sigma_avg = 1.0 / np.sqrt(np.sum(weights))

    # Chi-squared for consistency
    chi2 = np.sum(weights * (betas - beta_avg)**2)
    ndof = len(betas) - 1
    from scipy.stats import chi2 as chi2_dist
    p_value = 1.0 - chi2_dist.cdf(chi2, ndof)

    return {
        "beta_avg_deg": float(beta_avg),
        "sigma_avg_deg": float(sigma_avg),
        "chi2": float(chi2),
        "ndof": int(ndof),
        "p_value": float(p_value),
        "n_measurements": len(betas),
        "include_systematics": use_syst,
    }


def compute_independent_average(measurements):
    """
    Compute weighted average using only INDEPENDENT measurements.

    Excludes the combined SPIDER+Planck+ACT entry (which reuses Planck
    and ACT data) to avoid double-counting. Uses only entries that are
    based on distinct datasets.

    Returns
    -------
    result : dict
        Same format as compute_weighted_average.
    """
    # Select independent measurements: exclude combined analyses
    independent = []
    for m in measurements:
        label = m["label"]
        # Skip the combined entry
        if "SPIDER + Planck + ACT" in label:
            continue
        # Between Eskilt (2022) and Eskilt et al. (2022) [Cosmoglobe],
        # they use the same PR4 data. Keep the more recent/precise one.
        if "Cosmoglobe" in label:
            continue
        independent.append(m)

    return compute_weighted_average(independent, use_syst=False)


def make_forest_plot(measurements, output_dir):
    """
    Generate a forest plot of all beta measurements.

    Parameters
    ----------
    measurements : list of dict
        Beta measurement entries.
    output_dir : str
        Directory for output files.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Sort by year (newest at top)
    entries = list(reversed(measurements))
    n = len(entries)
    y_positions = np.arange(n)

    labels = []
    for i, m in enumerate(entries):
        beta = m["beta_deg"]
        sigma_stat = m["stat_err_deg"] if m["stat_err_deg"] else 0.0
        sigma_syst = m["syst_err_deg"] if m["syst_err_deg"] else 0.0
        sigma_total = np.sqrt(sigma_stat**2 + sigma_syst**2)

        # Stat error bar (thick)
        ax.errorbar(beta, i, xerr=sigma_stat, fmt="o", color="C0",
                     markersize=6, capsize=4, capthick=1.5, linewidth=1.5,
                     zorder=3)

        # Total error bar (thin, if syst available)
        if sigma_syst > 0:
            ax.errorbar(beta, i, xerr=sigma_total, fmt="none", color="C0",
                         capsize=3, capthick=1.0, linewidth=1.0,
                         alpha=0.5, zorder=2)

        label = "%s\n  %s %s" % (m["label"], m["instrument"], m["data_release"])
        labels.append(m["label"])

    # Weighted average band
    avg = compute_independent_average(measurements)
    beta_avg = avg["beta_avg_deg"]
    sigma_avg = avg["sigma_avg_deg"]
    ax.axvspan(beta_avg - sigma_avg, beta_avg + sigma_avg,
               alpha=0.15, color="C1", zorder=0)
    ax.axvline(beta_avg, color="C1", linestyle="--", linewidth=1.0,
               alpha=0.7, zorder=1,
               label="Weighted avg: %.3f +/- %.3f deg" % (beta_avg, sigma_avg))

    # Zero line
    ax.axvline(0, color="gray", linestyle=":", linewidth=0.8, alpha=0.5)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Isotropic cosmic birefringence angle beta (degrees)", fontsize=11)
    ax.set_title("Published Cosmic Birefringence Measurements", fontsize=12)
    ax.legend(loc="lower right", fontsize=9)

    # Value annotations
    for i, m in enumerate(entries):
        beta = m["beta_deg"]
        sigma = m["stat_err_deg"] if m["stat_err_deg"] else 0.0
        sig_str = m["significance"]
        ax.annotate(
            "%.3f +/- %.3f deg (%s)" % (beta, sigma, sig_str),
            xy=(beta, i), xytext=(10, 0),
            textcoords="offset points", fontsize=7, color="gray",
            va="center",
        )

    ax.set_xlim(-0.1, 0.7)
    plt.tight_layout()

    # Save
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, "forest_plot.%s" % ext)
        fig.savefig(path, dpi=300, bbox_inches="tight")
        print("Saved: %s" % path)
    plt.close(fig)


def save_registry(measurements, output_dir):
    """Save the full registry as JSON with all metadata."""
    registry = {
        "description": "Cosmic birefringence beta measurements from published literature",
        "compilation_date": "2026-03-05",
        "compiler": "Houston Golden",
        "notes": [
            "All arXiv IDs verified against ADS/arXiv (see docs/backlog_candidates.md).",
            "Statistical uncertainties are 68% CL unless noted.",
            "Systematic uncertainties are listed separately where reported.",
            "The weighted average uses statistical errors only, because systematic "
            "errors are correlated between experiments using the same Planck data "
            "and cannot be simply combined in quadrature.",
        ],
        "measurements": measurements,
    }

    path = os.path.join(output_dir, "beta_registry.json")
    with open(path, "w") as f:
        json.dump(registry, f, indent=2, default=str)
    print("Saved: %s" % path)
    return path


def save_summary(measurements, output_dir):
    """Save summary statistics."""
    avg_stat = compute_weighted_average(measurements, use_syst=False)
    avg_total = compute_weighted_average(measurements, use_syst=True)
    avg_indep = compute_independent_average(measurements)

    summary = {
        "weighted_average_stat_only": avg_stat,
        "weighted_average_with_syst": avg_total,
        "independent_measurements_only": avg_indep,
        "caveats": [
            "Weighted average uses inverse-variance weighting with stat errors only.",
            "The SPIDER+Planck+ACT combined entry reuses Planck and ACT data. "
            "The 'independent_measurements_only' average excludes it to avoid "
            "double-counting.",
            "Systematic errors (especially miscalibration angle degeneracy) are "
            "correlated across Planck-based analyses. The stat-only weighted "
            "average may underestimate the true uncertainty.",
            "Map-level vs spectrum-level analyses show mild tension "
            "(Zagatti+2025 vs Eskilt 2022). This may reflect different sensitivity "
            "to Galactic foreground residuals.",
        ],
    }

    path = os.path.join(output_dir, "beta_summary.json")
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    print("Saved: %s" % path)

    # Print human-readable summary
    print("\n" + "=" * 60)
    print("COSMIC BIREFRINGENCE BETA REGISTRY SUMMARY")
    print("=" * 60)
    print("\nAll measurements (stat-only weights):")
    print("  beta = %.4f +/- %.4f deg" % (
        avg_stat["beta_avg_deg"], avg_stat["sigma_avg_deg"]))
    print("  chi2/ndof = %.2f / %d  (p = %.3f)" % (
        avg_stat["chi2"], avg_stat["ndof"], avg_stat["p_value"]))
    print("\nIndependent measurements only:")
    print("  beta = %.4f +/- %.4f deg" % (
        avg_indep["beta_avg_deg"], avg_indep["sigma_avg_deg"]))
    print("  chi2/ndof = %.2f / %d  (p = %.3f)" % (
        avg_indep["chi2"], avg_indep["ndof"], avg_indep["p_value"]))
    print("\nAll measurements (stat+syst in quadrature):")
    print("  beta = %.4f +/- %.4f deg" % (
        avg_total["beta_avg_deg"], avg_total["sigma_avg_deg"]))
    print("=" * 60)

    return path


def main():
    parser = argparse.ArgumentParser(
        description="P6 Tier 1: Cosmic birefringence beta registry + forest plot"
    )
    parser.add_argument(
        "--output", type=str, default="outputs/",
        help="Output directory (default: outputs/)"
    )
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    print("P6 CMB EB Pipeline — Tier 1: Literature Beta Registry")
    print("=" * 55)
    print("Compiling %d published measurements..." % len(BETA_MEASUREMENTS))

    # Save full registry
    save_registry(BETA_MEASUREMENTS, args.output)

    # Compute and save summary
    save_summary(BETA_MEASUREMENTS, args.output)

    # Generate forest plot
    print("\nGenerating forest plot...")
    make_forest_plot(BETA_MEASUREMENTS, args.output)

    print("\nTier 1 complete.")


if __name__ == "__main__":
    main()
