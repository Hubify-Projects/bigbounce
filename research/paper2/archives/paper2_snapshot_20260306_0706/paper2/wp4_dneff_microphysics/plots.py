#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WP4: Delta-Neff Publication Figures
=====================================

Generates publication-quality figures from parameter scan results:

  Fig 1: Delta-Neff contour plot for reheating model (Br_dr vs g_star_hidden)
  Fig 2: Delta-Neff contour plot for decay model (m_X vs tau_X)
  Fig 3: Allowed parameter region (all constraints + target)
  Fig 4: Comparison of both models with Paper 1 posterior band

Usage:
    python plots.py --input runs/reheat_001/ --output figures/
    python plots.py --input runs/decay_001/ --output figures/
    python plots.py --input runs/reheat_001/ --input-decay runs/decay_001/ --output figures/

Author: Houston Golden (2026)
"""

from __future__ import division, print_function
import argparse
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for SSH compatibility
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.patches import Patch
import matplotlib.ticker as ticker

from dneff_models import DNEFF_BBN_MAX, DNEFF_CMB_MAX, DNEFF_TARGET_LO, DNEFF_TARGET_HI


# ===========================================================================
# Style configuration
# ===========================================================================

def setup_style():
    """Set up publication-quality matplotlib style."""
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Computer Modern Roman", "Times New Roman", "DejaVu Serif"],
        "font.size": 11,
        "axes.labelsize": 13,
        "axes.titlesize": 14,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.figsize": (7, 5.5),
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.minor.width": 0.4,
        "ytick.minor.width": 0.4,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
    })


# ===========================================================================
# Figure 1: Reheating model contour plot
# ===========================================================================

def fig1_reheating_contours(input_dir, output_dir):
    """
    Delta-Neff(Br_dr, g_star_hidden) contour plot for the reheating model,
    with BBN and CMB constraint bands overlaid.
    """
    print("Generating Fig 1: Reheating model contours...")

    Br_dr = np.load(os.path.join(input_dir, "param_Br_dr.npy"))
    g_hidden = np.load(os.path.join(input_dir, "param_g_hidden.npy"))

    # Use Treh = 1e9 GeV as fiducial
    tag = "Treh_1e+09"
    dneff_file = os.path.join(input_dir, "dneff_grid_%s.npy" % tag)
    if not os.path.exists(dneff_file):
        # Try alternative formatting
        for candidate in os.listdir(input_dir):
            if candidate.startswith("dneff_grid_Treh") and "9" in candidate:
                dneff_file = os.path.join(input_dir, candidate)
                break

    dneff = np.load(dneff_file)

    fig, ax = plt.subplots(1, 1, figsize=(7, 5.5))

    # Contour levels
    levels = [0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.34, 0.50, 1.0, 2.0, 5.0]

    # Filled contours
    cf = ax.contourf(
        Br_dr, g_hidden, dneff.T,
        levels=np.logspace(-3, 1, 50),
        norm=LogNorm(vmin=1e-3, vmax=10),
        cmap="viridis",
    )
    cbar = fig.colorbar(cf, ax=ax, label=r"$\Delta N_{\rm eff}$", pad=0.02)

    # Line contours at key values
    cs = ax.contour(
        Br_dr, g_hidden, dneff.T,
        levels=[DNEFF_TARGET_LO, DNEFF_TARGET_HI, DNEFF_CMB_MAX, DNEFF_BBN_MAX],
        colors=["#2196F3", "#2196F3", "#FF5722", "#F44336"],
        linewidths=[1.5, 1.5, 1.5, 1.5],
        linestyles=["--", "--", "-.", ":"],
    )

    # Label the contours
    fmt = {
        DNEFF_TARGET_LO: r"$0.10$",
        DNEFF_TARGET_HI: r"$0.20$",
        DNEFF_CMB_MAX: r"CMB $2\sigma$",
        DNEFF_BBN_MAX: r"BBN $2\sigma$",
    }
    ax.clabel(cs, fmt=fmt, fontsize=9, inline=True)

    # Shade the target region
    ax.contourf(
        Br_dr, g_hidden, dneff.T,
        levels=[DNEFF_TARGET_LO, DNEFF_TARGET_HI],
        colors=["none"],
        hatches=["///"],
        alpha=0.0,
    )
    # Draw hatching border manually via contour
    ax.contour(
        Br_dr, g_hidden, dneff.T,
        levels=[DNEFF_TARGET_LO, DNEFF_TARGET_HI],
        colors=["#1565C0"],
        linewidths=[2.0, 2.0],
        linestyles=["--", "--"],
    )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Branching fraction $\mathrm{Br}_{\rm dr}$")
    ax.set_ylabel(r"Hidden sector d.o.f. $g_{*,\rm hidden}$")
    ax.set_title(r"Model A: Reheating Branching ($T_{\rm reh} = 10^9\,\mathrm{GeV}$)")

    # Legend
    legend_elements = [
        Patch(facecolor="none", edgecolor="#1565C0", linestyle="--",
              label=r"Target: $0.10 \leq \Delta N_{\rm eff} \leq 0.20$"),
        Patch(facecolor="none", edgecolor="#FF5722", linestyle="-.",
              label=r"CMB $2\sigma$: $\Delta N_{\rm eff} < 0.34$"),
        Patch(facecolor="none", edgecolor="#F44336", linestyle=":",
              label=r"BBN $2\sigma$: $\Delta N_{\rm eff} < 0.50$"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", framealpha=0.9)

    # Save
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, "fig1_reheating_contours.%s" % ext)
        fig.savefig(path)
        print("  Saved: %s" % path)
    plt.close(fig)


# ===========================================================================
# Figure 2: Decay model contour plot
# ===========================================================================

def fig2_decay_contours(input_dir, output_dir):
    """
    Delta-Neff(m_X, tau_X) contour plot for the decay model,
    with BBN and CMB constraint bands overlaid.
    """
    print("Generating Fig 2: Decay model contours...")

    m_X = np.load(os.path.join(input_dir, "param_m_X.npy"))
    tau_X = np.load(os.path.join(input_dir, "param_tau_X.npy"))

    # Use fiducial config
    dneff = np.load(os.path.join(input_dir, "dneff_grid_fiducial.npy"))

    fig, ax = plt.subplots(1, 1, figsize=(7, 5.5))

    # Clip very small values for log colorscale
    dneff_plot = np.clip(dneff, 1e-6, None)

    # Filled contours
    cf = ax.contourf(
        m_X, tau_X, dneff_plot.T,
        levels=np.logspace(-6, 2, 50),
        norm=LogNorm(vmin=1e-6, vmax=100),
        cmap="inferno",
    )
    cbar = fig.colorbar(cf, ax=ax, label=r"$\Delta N_{\rm eff}$", pad=0.02)

    # Key contour lines
    cs = ax.contour(
        m_X, tau_X, dneff_plot.T,
        levels=[DNEFF_TARGET_LO, DNEFF_TARGET_HI, DNEFF_CMB_MAX, DNEFF_BBN_MAX],
        colors=["#4FC3F7", "#4FC3F7", "#FF8A65", "#EF5350"],
        linewidths=[1.5, 1.5, 1.5, 1.5],
        linestyles=["--", "--", "-.", ":"],
    )

    fmt = {
        DNEFF_TARGET_LO: r"$0.10$",
        DNEFF_TARGET_HI: r"$0.20$",
        DNEFF_CMB_MAX: r"CMB",
        DNEFF_BBN_MAX: r"BBN",
    }
    ax.clabel(cs, fmt=fmt, fontsize=9, inline=True)

    # Mark neutrino decoupling line (tau ~ 1 sec => T ~ 1 MeV)
    ax.axhline(y=1.0, color="white", linewidth=0.8, linestyle=":",
               alpha=0.7, label=r"$\tau_X = 1\,\mathrm{s}$ ($T \sim 1\,\mathrm{MeV}$)")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Particle mass $m_X$ [GeV]")
    ax.set_ylabel(r"Lifetime $\tau_X$ [seconds]")
    ax.set_title(r"Model B: Heavy Particle Decay ($\mathrm{Br}_{\rm dark}=1,\; Y_X = 10^{-10}$)")

    # Legend
    legend_elements = [
        Patch(facecolor="none", edgecolor="#4FC3F7", linestyle="--",
              label=r"Target: $0.10 \leq \Delta N_{\rm eff} \leq 0.20$"),
        Patch(facecolor="none", edgecolor="#FF8A65", linestyle="-.",
              label=r"CMB $2\sigma$"),
        Patch(facecolor="none", edgecolor="#EF5350", linestyle=":",
              label=r"BBN $2\sigma$"),
        Patch(facecolor="none", edgecolor="white", linestyle=":",
              label=r"$\nu$ decoupling ($\tau_X = 1\,$s)"),
    ]
    ax.legend(handles=legend_elements, loc="lower left", framealpha=0.9)

    # Save
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, "fig2_decay_contours.%s" % ext)
        fig.savefig(path)
        print("  Saved: %s" % path)
    plt.close(fig)


# ===========================================================================
# Figure 3: Allowed parameter region
# ===========================================================================

def fig3_allowed_regions(input_dir_reheat, input_dir_decay, output_dir):
    """
    Allowed parameter regions (intersection of all constraints + target)
    for both models side by side.
    """
    print("Generating Fig 3: Allowed parameter regions...")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # --- Panel A: Reheating ---
    ax = axes[0]
    Br_dr = np.load(os.path.join(input_dir_reheat, "param_Br_dr.npy"))
    g_hidden = np.load(os.path.join(input_dir_reheat, "param_g_hidden.npy"))

    # Load masks for all Treh values
    colors_treh = {"1e+06": "#4CAF50", "1e+09": "#2196F3", "1e+12": "#9C27B0"}
    labels_treh = {"1e+06": r"$T_{\rm reh}=10^6\,$GeV",
                   "1e+09": r"$T_{\rm reh}=10^9\,$GeV",
                   "1e+12": r"$T_{\rm reh}=10^{12}\,$GeV"}

    for fname in sorted(os.listdir(input_dir_reheat)):
        if not fname.startswith("mask_allowed_Treh"):
            continue
        # Extract Treh tag
        tag = fname.replace("mask_allowed_Treh_", "").replace(".npy", "")
        mask = np.load(os.path.join(input_dir_reheat, fname))

        color = colors_treh.get(tag, "#888888")
        label = labels_treh.get(tag, tag)

        # Plot allowed region as filled contour at level 0.5
        ax.contourf(
            Br_dr, g_hidden, mask.astype(float).T,
            levels=[0.5, 1.5],
            colors=[color],
            alpha=0.3,
        )
        ax.contour(
            Br_dr, g_hidden, mask.astype(float).T,
            levels=[0.5],
            colors=[color],
            linewidths=[1.5],
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Branching fraction $\mathrm{Br}_{\rm dr}$")
    ax.set_ylabel(r"$g_{*,\rm hidden}$")
    ax.set_title("(a) Reheating Model — Allowed Region")

    # Manual legend
    legend_a = []
    for tag in ["1e+06", "1e+09", "1e+12"]:
        legend_a.append(Patch(
            facecolor=colors_treh[tag], alpha=0.3,
            edgecolor=colors_treh[tag], label=labels_treh[tag]
        ))
    ax.legend(handles=legend_a, loc="upper left", framealpha=0.9)

    # --- Panel B: Decay ---
    ax = axes[1]
    if input_dir_decay is not None:
        m_X = np.load(os.path.join(input_dir_decay, "param_m_X.npy"))
        tau_X = np.load(os.path.join(input_dir_decay, "param_tau_X.npy"))

        config_colors = {
            "fiducial": "#2196F3",
            "Br01": "#4CAF50",
            "YX1e8": "#FF9800",
            "Br05_YX1e9": "#9C27B0",
        }
        config_labels = {
            "fiducial": r"$\mathrm{Br}=1,\; Y_X=10^{-10}$",
            "Br01": r"$\mathrm{Br}=0.1,\; Y_X=10^{-10}$",
            "YX1e8": r"$\mathrm{Br}=1,\; Y_X=10^{-8}$",
            "Br05_YX1e9": r"$\mathrm{Br}=0.5,\; Y_X=10^{-9}$",
        }

        for fname in sorted(os.listdir(input_dir_decay)):
            if not fname.startswith("mask_allowed_"):
                continue
            tag = fname.replace("mask_allowed_", "").replace(".npy", "")
            if tag not in config_colors:
                continue

            mask = np.load(os.path.join(input_dir_decay, fname))
            color = config_colors[tag]

            ax.contourf(
                m_X, tau_X, mask.astype(float).T,
                levels=[0.5, 1.5],
                colors=[color],
                alpha=0.25,
            )
            ax.contour(
                m_X, tau_X, mask.astype(float).T,
                levels=[0.5],
                colors=[color],
                linewidths=[1.5],
            )

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel(r"$m_X$ [GeV]")
        ax.set_ylabel(r"$\tau_X$ [seconds]")
        ax.set_title("(b) Decay Model — Allowed Region")

        legend_b = []
        for tag in ["fiducial", "Br01", "YX1e8", "Br05_YX1e9"]:
            if tag in config_colors:
                legend_b.append(Patch(
                    facecolor=config_colors[tag], alpha=0.25,
                    edgecolor=config_colors[tag], label=config_labels[tag]
                ))
        ax.legend(handles=legend_b, loc="upper left", framealpha=0.9, fontsize=9)
    else:
        ax.text(0.5, 0.5, "Decay scan not provided",
                transform=ax.transAxes, ha="center", va="center",
                fontsize=12, color="gray")
        ax.set_title("(b) Decay Model — No Data")

    fig.tight_layout(w_pad=3.0)

    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, "fig3_allowed_regions.%s" % ext)
        fig.savefig(path)
        print("  Saved: %s" % path)
    plt.close(fig)


# ===========================================================================
# Figure 4: Comparison with Paper 1 posteriors
# ===========================================================================

def fig4_model_comparison(input_dir_reheat, input_dir_decay, output_dir):
    """
    Comparison of both models' Delta-Neff predictions with Paper 1
    posterior band shown as a horizontal shaded region.
    """
    print("Generating Fig 4: Model comparison with Paper 1 posterior...")

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    # Paper 1 posterior band
    ax.axhspan(DNEFF_TARGET_LO, DNEFF_TARGET_HI, alpha=0.2, color="#1565C0",
               label=r"Paper 1 MCMC: $\Delta N_{\rm eff} = 0.14$-$0.18$")
    ax.axhline(y=0.15, color="#1565C0", linewidth=1.0, linestyle="--", alpha=0.5)

    # Constraint lines
    ax.axhline(y=DNEFF_CMB_MAX, color="#FF5722", linewidth=1.0, linestyle="-.",
               label=r"Planck 2018 $2\sigma$ ($\Delta N_{\rm eff} < 0.34$)")
    ax.axhline(y=DNEFF_BBN_MAX, color="#F44336", linewidth=1.0, linestyle=":",
               label=r"BBN $2\sigma$ ($\Delta N_{\rm eff} < 0.50$)")

    x_positions = []
    x_labels = []
    x_idx = 0

    # --- Reheating model points ---
    if input_dir_reheat is not None:
        summary_path = os.path.join(input_dir_reheat, "summary.json")
        if os.path.exists(summary_path):
            with open(summary_path, "r") as f:
                summary = json.load(f)
            bf = summary.get("best_fit", {})
            if bf.get("dneff") is not None:
                ax.errorbar(
                    x_idx, bf["dneff"], yerr=0.03,
                    fmt="s", color="#4CAF50", markersize=10,
                    capsize=5, capthick=1.5, linewidth=1.5,
                    label="Model A best fit (Br=%.1e, g*=%.1f)" % (
                        bf["Br_dr"], bf["g_star_hidden"])
                )
                x_positions.append(x_idx)
                x_labels.append("Model A\n(reheating)")
                x_idx += 1

        # Show range from allowed region
        for fname in sorted(os.listdir(input_dir_reheat)):
            if fname.startswith("dneff_grid_Treh") and fname.endswith(".npy"):
                tag = fname.replace("dneff_grid_", "").replace(".npy", "")
                mask_file = os.path.join(input_dir_reheat,
                                         "mask_allowed_%s.npy" % tag)
                if not os.path.exists(mask_file):
                    continue
                dneff = np.load(os.path.join(input_dir_reheat, fname))
                mask = np.load(mask_file)
                if np.any(mask):
                    allowed_vals = dneff[mask]
                    lo = np.min(allowed_vals)
                    hi = np.max(allowed_vals)
                    mid = np.median(allowed_vals)
                    ax.plot(
                        [x_idx, x_idx], [lo, hi],
                        color="#81C784", linewidth=3, alpha=0.6,
                        solid_capstyle="round"
                    )
                    ax.plot(x_idx, mid, "o", color="#388E3C", markersize=6)
                    x_positions.append(x_idx)
                    treh_label = tag.replace("Treh_", "T=")
                    x_labels.append("A: %s" % treh_label)
                    x_idx += 1

    # --- Decay model points ---
    if input_dir_decay is not None:
        summary_path = os.path.join(input_dir_decay, "summary.json")
        if os.path.exists(summary_path):
            with open(summary_path, "r") as f:
                summary = json.load(f)
            bf = summary.get("best_fit", {})
            if bf.get("dneff") is not None:
                ax.errorbar(
                    x_idx, bf["dneff"], yerr=0.03,
                    fmt="D", color="#FF9800", markersize=10,
                    capsize=5, capthick=1.5, linewidth=1.5,
                    label="Model B best fit (m=%.1e, tau=%.1e)" % (
                        bf["m_X_GeV"], bf["tau_X_sec"])
                )
                x_positions.append(x_idx)
                x_labels.append("Model B\n(decay)")
                x_idx += 1

        # Show range from allowed region for each config
        config_colors = {
            "fiducial": "#FFB74D",
            "Br01": "#A5D6A7",
            "YX1e8": "#90CAF9",
            "Br05_YX1e9": "#CE93D8",
        }
        for fname in sorted(os.listdir(input_dir_decay)):
            if fname.startswith("dneff_grid_") and fname.endswith(".npy"):
                tag = fname.replace("dneff_grid_", "").replace(".npy", "")
                if tag not in config_colors:
                    continue
                mask_file = os.path.join(input_dir_decay,
                                         "mask_allowed_%s.npy" % tag)
                if not os.path.exists(mask_file):
                    continue
                dneff = np.load(os.path.join(input_dir_decay, fname))
                mask = np.load(mask_file)
                if np.any(mask):
                    allowed_vals = dneff[mask]
                    lo = np.min(allowed_vals)
                    hi = np.max(allowed_vals)
                    mid = np.median(allowed_vals)
                    color = config_colors[tag]
                    ax.plot(
                        [x_idx, x_idx], [lo, hi],
                        color=color, linewidth=3, alpha=0.6,
                        solid_capstyle="round"
                    )
                    ax.plot(x_idx, mid, "o", color=color, markersize=6)
                    x_positions.append(x_idx)
                    x_labels.append("B: %s" % tag)
                    x_idx += 1

    # Formatting
    if x_positions:
        ax.set_xticks(x_positions)
        ax.set_xticklabels(x_labels, fontsize=8, rotation=30, ha="right")
        ax.set_xlim(-0.5, max(x_positions) + 0.5)
    else:
        ax.text(0.5, 0.5, "No scan data found",
                transform=ax.transAxes, ha="center", fontsize=14, color="gray")

    ax.set_ylabel(r"$\Delta N_{\rm eff}$")
    ax.set_ylim(0, 0.7)
    ax.set_title(r"$\Delta N_{\rm eff}$ Model Predictions vs. Observational Constraints")
    ax.legend(loc="upper right", framealpha=0.9, fontsize=9)
    ax.grid(axis="y", alpha=0.3, linewidth=0.5)

    fig.tight_layout()

    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, "fig4_model_comparison.%s" % ext)
        fig.savefig(path)
        print("  Saved: %s" % path)
    plt.close(fig)


# ===========================================================================
# Detect model type from scan directory
# ===========================================================================

def detect_model(input_dir):
    """Detect whether a scan directory contains reheating or decay results."""
    summary_path = os.path.join(input_dir, "summary.json")
    if os.path.exists(summary_path):
        with open(summary_path, "r") as f:
            summary = json.load(f)
        return summary.get("model", "unknown")

    # Fallback: check for characteristic files
    if os.path.exists(os.path.join(input_dir, "param_Br_dr.npy")):
        return "reheating"
    if os.path.exists(os.path.join(input_dir, "param_m_X.npy")):
        return "decay"
    return "unknown"


# ===========================================================================
# Main
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(
        description="WP4 Delta-Neff publication figure generation"
    )
    parser.add_argument(
        "--input", required=True,
        help="Input directory with scan results (primary model)"
    )
    parser.add_argument(
        "--input-decay", default=None,
        help="Input directory with decay scan results (for comparison plots)"
    )
    parser.add_argument(
        "--output", required=True,
        help="Output directory for figures"
    )
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)
        print("Created output directory: %s" % args.output)

    setup_style()

    # Detect model type
    model_type = detect_model(args.input)
    print("Detected primary model type: %s" % model_type)

    input_reheat = None
    input_decay = None

    if model_type == "reheating":
        input_reheat = args.input
        input_decay = args.input_decay
    elif model_type == "decay":
        input_decay = args.input
        # Check if --input-decay was actually the reheating one
        if args.input_decay is not None:
            other_type = detect_model(args.input_decay)
            if other_type == "reheating":
                input_reheat = args.input_decay
    else:
        print("WARNING: Could not detect model type from %s" % args.input)
        print("Trying to generate whatever plots are possible...")
        input_reheat = args.input if os.path.exists(
            os.path.join(args.input, "param_Br_dr.npy")) else None
        input_decay = args.input if os.path.exists(
            os.path.join(args.input, "param_m_X.npy")) else None

    # Generate figures
    if input_reheat is not None:
        fig1_reheating_contours(input_reheat, args.output)

    if input_decay is not None:
        fig2_decay_contours(input_decay, args.output)

    # Fig 3 needs at least one model
    if input_reheat is not None or input_decay is not None:
        fig3_allowed_regions(
            input_reheat if input_reheat else input_decay,
            input_decay,
            args.output
        )

    # Fig 4: comparison (works with either or both)
    fig4_model_comparison(input_reheat, input_decay, args.output)

    print("\nAll figures saved to: %s" % os.path.abspath(args.output))


if __name__ == "__main__":
    main()
