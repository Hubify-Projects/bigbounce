#!/usr/bin/env python3
"""
analyze_w0wa_quintom.py — Post-processing for w0-wa quintom MCMC chains.

Analyzes the CPL dark energy posterior from Planck+BAO+SN to test whether
the data independently confirms the DESI DR2 quintom-B signal:
  - w0 > -1 (phantom divide not crossed at z=0)
  - w0 + wa < -1 (phantom divide crossed at higher z)

This is the signature of quintom-B behavior, which the bounce cosmology
framework predicts via the effective equation of state of the torsion
scalar field traversing the bounce.

Usage:
    python analyze_w0wa_quintom.py [--chain-dir CHAIN_DIR] [--burn-in 0.3]

Requirements:
    pip install getdist matplotlib numpy scipy

Author: Houston Golden (2026)
"""

import argparse
import os
import sys
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

try:
    from getdist import MCSamples, loadMCSamples
    from getdist import plots as gdplots
    HAS_GETDIST = True
except ImportError:
    HAS_GETDIST = False
    print("WARNING: getdist not installed. Install with: pip install getdist")
    print("         Will use manual chain loading instead.")

from scipy import stats


# ---------------------------------------------------------------------------
# DESI DR2 reference values (DESI Collaboration 2025, arXiv:2503.14738)
# ---------------------------------------------------------------------------
DESI_W0 = -0.752
DESI_W0_ERR = 0.070
DESI_WA = -1.01
DESI_WA_ERR = 0.30

# LCDM reference
LCDM_W0 = -1.0
LCDM_WA = 0.0


def load_chains_getdist(chain_dir, burn_in=0.3):
    """Load MCMC chains using getdist."""
    # Find the chain root by looking for .txt files
    chain_files = sorted([
        f for f in os.listdir(chain_dir)
        if f.endswith(".txt") and not f.endswith(".input.txt")
        and not f.endswith(".updated.txt") and not f.endswith(".progress.txt")
    ])

    if not chain_files:
        raise FileNotFoundError(f"No chain .txt files found in {chain_dir}")

    # Determine the root name
    root = chain_files[0].rsplit(".", 1)[0]
    if root.endswith(".1") or root.endswith(".2"):
        root = root.rsplit(".", 1)[0]

    chain_path = os.path.join(chain_dir, root)
    print(f"Loading chains from: {chain_path}")

    samples = loadMCSamples(chain_path, settings={"ignore_rows": burn_in})
    return samples


def load_chains_manual(chain_dir, burn_in=0.3):
    """Load MCMC chains manually from text files (fallback without getdist)."""
    chain_files = sorted([
        os.path.join(chain_dir, f) for f in os.listdir(chain_dir)
        if f.endswith(".txt") and "spin_torsion" in f
        and not f.endswith(".input.txt") and not f.endswith(".updated.txt")
        and not f.endswith(".progress.txt") and not f.endswith(".paramnames")
    ])

    if not chain_files:
        raise FileNotFoundError(f"No chain files found in {chain_dir}")

    # Read paramnames
    paramnames_file = None
    for f in os.listdir(chain_dir):
        if f.endswith(".paramnames"):
            paramnames_file = os.path.join(chain_dir, f)
            break

    param_names = []
    if paramnames_file and os.path.exists(paramnames_file):
        with open(paramnames_file) as pf:
            for line in pf:
                line = line.strip()
                if line and not line.startswith("#"):
                    param_names.append(line.split()[0])

    # Load and concatenate chains
    all_data = []
    for cf in chain_files:
        print(f"  Loading: {cf}")
        try:
            data = np.loadtxt(cf)
            # Apply burn-in
            n_burn = int(burn_in * len(data))
            all_data.append(data[n_burn:])
        except Exception as e:
            print(f"  Warning: Could not load {cf}: {e}")

    if not all_data:
        raise ValueError("No valid chain data loaded")

    combined = np.vstack(all_data)
    # Column 0 = weight, column 1 = -loglike, columns 2+ = parameters
    weights = combined[:, 0]
    params_data = combined[:, 2:]

    return weights, params_data, param_names


def find_param_index(param_names, target):
    """Find the index of a parameter by name (case-insensitive, partial match)."""
    target_lower = target.lower()
    for i, name in enumerate(param_names):
        if name.lower() == target_lower:
            return i
        if name.lower().replace("_", "") == target_lower.replace("_", ""):
            return i
    # Try partial match
    for i, name in enumerate(param_names):
        if target_lower in name.lower():
            return i
    return None


def compute_quintom_statistics(w0_samples, wa_samples, weights=None):
    """Compute quintom-B diagnostic statistics from posterior samples."""
    results = {}

    if weights is not None:
        w_norm = weights / weights.sum()
    else:
        w_norm = np.ones(len(w0_samples)) / len(w0_samples)

    # Basic statistics
    w0_mean = np.average(w0_samples, weights=w_norm)
    wa_mean = np.average(wa_samples, weights=w_norm)
    w0_std = np.sqrt(np.average((w0_samples - w0_mean)**2, weights=w_norm))
    wa_std = np.sqrt(np.average((wa_samples - wa_mean)**2, weights=w_norm))

    results["w0_mean"] = w0_mean
    results["w0_std"] = w0_std
    results["wa_mean"] = wa_mean
    results["wa_std"] = wa_std

    # Weighted percentiles (approximate via resampling)
    n_resample = min(100000, len(w0_samples) * 10)
    indices = np.random.choice(len(w0_samples), size=n_resample, p=w_norm)
    w0_resampled = w0_samples[indices]
    wa_resampled = wa_samples[indices]

    results["w0_median"] = np.median(w0_resampled)
    results["w0_16"] = np.percentile(w0_resampled, 16)
    results["w0_84"] = np.percentile(w0_resampled, 84)
    results["wa_median"] = np.median(wa_resampled)
    results["wa_16"] = np.percentile(wa_resampled, 16)
    results["wa_84"] = np.percentile(wa_resampled, 84)

    # --- Quintom-B diagnostics ---

    # 1. Probability that w0 > -1 (quintessence-like at z=0)
    prob_w0_gt_minus1 = np.sum(w_norm[w0_samples > -1.0])
    results["P(w0 > -1)"] = prob_w0_gt_minus1

    # 2. Probability that w0 + wa < -1 (phantom-like in the past)
    w0_plus_wa = w0_samples + wa_samples
    prob_sum_lt_minus1 = np.sum(w_norm[w0_plus_wa < -1.0])
    results["P(w0+wa < -1)"] = prob_sum_lt_minus1

    # 3. Probability of quintom-B: BOTH conditions simultaneously
    quintom_b_mask = (w0_samples > -1.0) & (w0_plus_wa < -1.0)
    prob_quintom_b = np.sum(w_norm[quintom_b_mask])
    results["P(quintom-B)"] = prob_quintom_b

    # 4. Crossing redshift z_c where w(z_c) = -1
    #    w(z) = w0 + wa * z/(1+z) = -1
    #    => z_c = -(1+w0) / (wa + 1 + w0) = -(1+w0) / (1 + w0 + wa)
    w0_plus_1 = w0_samples + 1.0
    denom = 1.0 + w0_samples + wa_samples  # = 1 + w0 + wa
    # Crossing only valid when z_c > 0 and denominator != 0
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        z_cross = np.where(
            (np.abs(denom) > 1e-10),
            -w0_plus_1 / denom,
            np.nan
        )
    # Only keep valid crossings (positive z, physical)
    valid_crossing = (z_cross > 0) & (z_cross < 10) & np.isfinite(z_cross)
    z_cross_valid = z_cross[valid_crossing]
    w_cross_valid = w_norm[valid_crossing]

    if len(z_cross_valid) > 0 and w_cross_valid.sum() > 0:
        w_cv_norm = w_cross_valid / w_cross_valid.sum()
        results["z_cross_mean"] = np.average(z_cross_valid, weights=w_cv_norm)
        results["z_cross_median"] = np.median(
            np.random.choice(z_cross_valid, size=50000,
                             p=w_cv_norm)
        )
        results["z_cross_16"] = np.percentile(
            np.random.choice(z_cross_valid, size=50000, p=w_cv_norm), 16
        )
        results["z_cross_84"] = np.percentile(
            np.random.choice(z_cross_valid, size=50000, p=w_cv_norm), 84
        )
        results["P(crossing exists)"] = np.sum(w_norm[valid_crossing])
    else:
        results["z_cross_mean"] = np.nan
        results["z_cross_median"] = np.nan
        results["z_cross_16"] = np.nan
        results["z_cross_84"] = np.nan
        results["P(crossing exists)"] = 0.0

    # 5. Distance from LCDM (w0=-1, wa=0) in sigma
    dw0 = w0_mean - LCDM_W0
    dwa = wa_mean - LCDM_WA
    # Approximate 2D distance using covariance
    cov = np.cov(w0_resampled, wa_resampled)
    delta = np.array([dw0, dwa])
    try:
        chi2 = delta @ np.linalg.inv(cov) @ delta
        results["sigma_from_LCDM"] = np.sqrt(chi2)
    except np.linalg.LinAlgError:
        results["sigma_from_LCDM"] = np.nan

    # 6. Consistency with DESI DR2
    dw0_desi = w0_mean - DESI_W0
    dwa_desi = wa_mean - DESI_WA
    # Combined sigma distance (treating our posterior and DESI as independent)
    cov_desi = np.array([
        [DESI_W0_ERR**2, 0],
        [0, DESI_WA_ERR**2]
    ])
    cov_combined = cov + cov_desi
    delta_desi = np.array([dw0_desi, dwa_desi])
    try:
        chi2_desi = delta_desi @ np.linalg.inv(cov_combined) @ delta_desi
        results["sigma_from_DESI"] = np.sqrt(chi2_desi)
    except np.linalg.LinAlgError:
        results["sigma_from_DESI"] = np.nan

    return results


def plot_w0wa_contours(w0_samples, wa_samples, weights, output_dir):
    """Plot w0-wa posterior contours with DESI DR2 and LCDM reference."""
    fig, ax = plt.subplots(1, 1, figsize=(8, 7))

    # Resampled for 2D histogram
    w_norm = weights / weights.sum()
    n_resample = min(200000, len(w0_samples) * 10)
    indices = np.random.choice(len(w0_samples), size=n_resample, p=w_norm)
    w0_r = w0_samples[indices]
    wa_r = wa_samples[indices]

    # 2D histogram contours
    H, xedges, yedges = np.histogram2d(w0_r, wa_r, bins=80,
                                        range=[[-2.0, 0.0], [-3.0, 2.0]])
    H = H.T
    # Smooth
    from scipy.ndimage import gaussian_filter
    H_smooth = gaussian_filter(H, sigma=1.5)

    # Normalize to find contour levels
    H_flat = H_smooth.flatten()
    H_flat.sort()
    H_cumsum = np.cumsum(H_flat[::-1])
    H_cumsum /= H_cumsum[-1]

    # Find 1-sigma (68%) and 2-sigma (95%) levels
    level_68 = H_flat[::-1][np.searchsorted(H_cumsum, 0.68)]
    level_95 = H_flat[::-1][np.searchsorted(H_cumsum, 0.95)]

    x_centers = 0.5 * (xedges[:-1] + xedges[1:])
    y_centers = 0.5 * (yedges[:-1] + yedges[1:])

    # Plot contours
    ax.contourf(x_centers, y_centers, H_smooth,
                levels=[level_95, level_68, H_smooth.max()],
                colors=["#c6dbef", "#3182bd"], alpha=0.7)
    ax.contour(x_centers, y_centers, H_smooth,
               levels=[level_95, level_68],
               colors=["#2171b5", "#08519c"], linewidths=[1, 1.5])

    # LCDM point
    ax.plot(LCDM_W0, LCDM_WA, "k+", markersize=15, markeredgewidth=2.5,
            label=r"$\Lambda$CDM ($w_0=-1, w_a=0$)", zorder=10)

    # DESI DR2 point with error ellipse
    ax.errorbar(DESI_W0, DESI_WA, xerr=DESI_W0_ERR, yerr=DESI_WA_ERR,
                fmt="s", color="#e31a1c", markersize=8, capsize=4,
                label=f"DESI DR2 ($w_0={DESI_W0}$, $w_a={DESI_WA}$)",
                zorder=10)

    # Quintom-B region shading
    # w0 > -1 AND w0+wa < -1 => wa < -1-w0
    w0_line = np.linspace(-2.5, -0.3, 200)
    wa_boundary = -1.0 - w0_line  # wa = -1 - w0
    ax.fill_between(w0_line, wa_boundary, -3.0,
                     where=(w0_line > -1.0),
                     alpha=0.08, color="green",
                     label="Quintom-B region")

    # Phantom divide lines
    ax.axvline(x=-1.0, color="gray", linestyle="--", alpha=0.5, linewidth=0.8)
    ax.plot(w0_line, -1.0 - w0_line, "g--", alpha=0.4, linewidth=0.8,
            label=r"$w_0 + w_a = -1$")

    ax.set_xlabel(r"$w_0$", fontsize=14)
    ax.set_ylabel(r"$w_a$", fontsize=14)
    ax.set_title("CPL Dark Energy: Quintom-B Test\n"
                 r"Planck NPIPE + SDSS DR16 BAO + Pantheon+", fontsize=13)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.9)
    ax.set_xlim(-2.0, 0.0)
    ax.set_ylim(-3.0, 2.0)
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    outpath = os.path.join(output_dir, "w0wa_quintom_contours.png")
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    print(f"Saved: {outpath}")
    plt.close(fig)


def plot_wz_reconstruction(w0_samples, wa_samples, weights, output_dir):
    """Plot w(z) reconstruction from posterior samples."""
    fig, ax = plt.subplots(1, 1, figsize=(9, 5.5))

    z_arr = np.linspace(0, 2.5, 300)
    a_arr = 1.0 / (1.0 + z_arr)

    # Resample
    w_norm = weights / weights.sum()
    n_curves = 5000
    indices = np.random.choice(len(w0_samples), size=n_curves, p=w_norm)

    # Compute w(z) for each sample
    wz_all = np.zeros((n_curves, len(z_arr)))
    for i, idx in enumerate(indices):
        wz_all[i] = w0_samples[idx] + wa_samples[idx] * (1.0 - a_arr)

    # Percentiles
    wz_median = np.median(wz_all, axis=0)
    wz_16 = np.percentile(wz_all, 16, axis=0)
    wz_84 = np.percentile(wz_all, 84, axis=0)
    wz_2p5 = np.percentile(wz_all, 2.5, axis=0)
    wz_97p5 = np.percentile(wz_all, 97.5, axis=0)

    # Plot bands
    ax.fill_between(z_arr, wz_2p5, wz_97p5, alpha=0.15, color="#3182bd",
                     label=r"95\% CL")
    ax.fill_between(z_arr, wz_16, wz_84, alpha=0.35, color="#3182bd",
                     label=r"68\% CL")
    ax.plot(z_arr, wz_median, "-", color="#08519c", linewidth=2,
            label=r"Median $w(z)$")

    # LCDM reference
    ax.axhline(y=-1.0, color="black", linestyle="--", linewidth=1.5,
               alpha=0.7, label=r"$\Lambda$CDM ($w=-1$)")

    # DESI DR2 best fit
    wz_desi = DESI_W0 + DESI_WA * (1.0 - a_arr)
    ax.plot(z_arr, wz_desi, ":", color="#e31a1c", linewidth=2,
            label=f"DESI DR2 best fit")

    # Mark crossing region
    crossing_mask = (wz_16 < -1.0) & (wz_84 > -1.0)
    if np.any(crossing_mask):
        z_cross_region = z_arr[crossing_mask]
        if len(z_cross_region) > 0:
            ax.axvspan(z_cross_region[0], z_cross_region[-1],
                       alpha=0.08, color="green",
                       label="Crossing region (68% CL)")

    ax.set_xlabel(r"Redshift $z$", fontsize=14)
    ax.set_ylabel(r"$w(z) = w_0 + w_a \frac{z}{1+z}$", fontsize=14)
    ax.set_title("Dark Energy Equation of State Reconstruction\n"
                 r"Planck NPIPE + SDSS DR16 BAO + Pantheon+", fontsize=13)
    ax.legend(loc="lower left", fontsize=10, framealpha=0.9)
    ax.set_xlim(0, 2.5)
    ax.set_ylim(-2.5, 0.0)
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    outpath = os.path.join(output_dir, "wz_reconstruction.png")
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    print(f"Saved: {outpath}")
    plt.close(fig)


def plot_crossing_redshift(w0_samples, wa_samples, weights, output_dir):
    """Plot the posterior distribution of the phantom-divide crossing redshift."""
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))

    # Compute crossing redshift for each sample
    # w(z_c) = -1  =>  z_c = -(1+w0) / (1+w0+wa)
    w0_plus_1 = w0_samples + 1.0
    denom = 1.0 + w0_samples + wa_samples

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        z_cross = np.where(np.abs(denom) > 1e-10, -w0_plus_1 / denom, np.nan)

    # Filter to physical crossings
    valid = (z_cross > 0) & (z_cross < 5) & np.isfinite(z_cross)
    z_valid = z_cross[valid]
    w_valid = weights[valid]

    if len(z_valid) == 0:
        print("No valid crossing redshifts found. Skipping crossing plot.")
        plt.close(fig)
        return

    # Weighted histogram
    ax.hist(z_valid, bins=80, weights=w_valid, density=True,
            color="#3182bd", alpha=0.6, edgecolor="#08519c", linewidth=0.5)

    # Summary stats
    w_v_norm = w_valid / w_valid.sum()
    z_mean = np.average(z_valid, weights=w_v_norm)
    n_resample = min(100000, len(z_valid) * 10)
    z_resampled = np.random.choice(z_valid, size=n_resample, p=w_v_norm)
    z_med = np.median(z_resampled)
    z_16 = np.percentile(z_resampled, 16)
    z_84 = np.percentile(z_resampled, 84)

    ax.axvline(z_med, color="#e31a1c", linewidth=2,
               label=rf"$z_c = {z_med:.2f}^{{+{z_84-z_med:.2f}}}_{{-{z_med-z_16:.2f}}}$")
    ax.axvspan(z_16, z_84, alpha=0.15, color="#e31a1c")

    frac_valid = np.sum(weights[valid]) / np.sum(weights)
    ax.set_xlabel(r"Crossing redshift $z_c$ where $w(z_c) = -1$", fontsize=13)
    ax.set_ylabel("Posterior density", fontsize=13)
    ax.set_title(f"Phantom-Divide Crossing Redshift\n"
                 f"P(crossing exists) = {frac_valid:.1%}", fontsize=13)
    ax.legend(fontsize=12, framealpha=0.9)
    ax.set_xlim(0, 4)
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    outpath = os.path.join(output_dir, "crossing_redshift.png")
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    print(f"Saved: {outpath}")
    plt.close(fig)


def plot_getdist_triangle(samples, output_dir):
    """Generate a triangle plot using getdist (if available)."""
    if not HAS_GETDIST:
        print("Skipping getdist triangle plot (getdist not installed).")
        return

    g = gdplots.get_subplot_plotter()
    g.settings.figure_legend_frame = True
    g.settings.alpha_filled_add = 0.7

    params_to_plot = ["w", "wa", "H0", "omegam", "sigma8", "S8"]
    # Filter to only params that exist in the samples
    available = [p for p in params_to_plot if samples.paramNames.parWithName(p)]

    if len(available) < 2:
        print("Not enough parameters for triangle plot.")
        return

    g.triangle_plot(samples, available, filled=True,
                    title_limit=1,
                    markers={"w": -1.0, "wa": 0.0})

    outpath = os.path.join(output_dir, "w0wa_triangle.png")
    g.export(outpath)
    print(f"Saved: {outpath}")


def print_summary(results):
    """Print a formatted summary of quintom-B diagnostics."""
    print("\n" + "=" * 70)
    print("  QUINTOM-B DIAGNOSTIC SUMMARY")
    print("  CPL Dark Energy: w(z) = w0 + wa * z/(1+z)")
    print("=" * 70)

    print(f"\n  w0  = {results['w0_mean']:.4f} +/- {results['w0_std']:.4f}")
    print(f"        (median: {results['w0_median']:.4f}, "
          f"68%: [{results['w0_16']:.4f}, {results['w0_84']:.4f}])")
    print(f"  wa  = {results['wa_mean']:.4f} +/- {results['wa_std']:.4f}")
    print(f"        (median: {results['wa_median']:.4f}, "
          f"68%: [{results['wa_16']:.4f}, {results['wa_84']:.4f}])")

    print(f"\n  --- Quintom-B Diagnostics ---")
    print(f"  P(w0 > -1)          = {results['P(w0 > -1)']:.4f}  "
          f"({results['P(w0 > -1)']*100:.1f}%)")
    print(f"  P(w0 + wa < -1)     = {results['P(w0+wa < -1)']:.4f}  "
          f"({results['P(w0+wa < -1)']*100:.1f}%)")
    print(f"  P(quintom-B)        = {results['P(quintom-B)']:.4f}  "
          f"({results['P(quintom-B)']*100:.1f}%)")

    if not np.isnan(results.get("z_cross_mean", np.nan)):
        print(f"\n  Crossing redshift z_c = {results['z_cross_mean']:.3f}")
        print(f"        (median: {results['z_cross_median']:.3f}, "
              f"68%: [{results['z_cross_16']:.3f}, {results['z_cross_84']:.3f}])")
        print(f"  P(crossing exists)   = {results['P(crossing exists)']:.4f}  "
              f"({results['P(crossing exists)']*100:.1f}%)")
    else:
        print(f"\n  Crossing redshift: No valid crossings in posterior")

    print(f"\n  --- Comparison ---")
    print(f"  Distance from LCDM:   {results['sigma_from_LCDM']:.2f} sigma")
    print(f"  Distance from DESI:   {results['sigma_from_DESI']:.2f} sigma")

    print(f"\n  DESI DR2 reference:   w0 = {DESI_W0} +/- {DESI_W0_ERR}, "
          f"wa = {DESI_WA} +/- {DESI_WA_ERR}")
    print(f"  LCDM reference:       w0 = {LCDM_W0}, wa = {LCDM_WA}")

    # Interpretation
    print(f"\n  --- Interpretation ---")
    if results["P(quintom-B)"] > 0.68:
        print("  STRONG quintom-B signal: >68% posterior probability")
        print("  The data independently confirm phantom-divide crossing!")
    elif results["P(quintom-B)"] > 0.50:
        print("  MODERATE quintom-B signal: >50% posterior probability")
        print("  Data favor quintom-B over LCDM, but not decisively.")
    elif results["P(quintom-B)"] > 0.30:
        print("  WEAK quintom-B hint: 30-50% posterior probability")
        print("  Some tension with LCDM but not statistically significant.")
    else:
        print("  NO quintom-B signal: <30% posterior probability")
        print("  Data are consistent with LCDM (w=-1 fixed).")

    if results["sigma_from_DESI"] < 1.0:
        print(f"\n  Our posterior is CONSISTENT with DESI DR2 "
              f"({results['sigma_from_DESI']:.1f} sigma).")
    elif results["sigma_from_DESI"] < 2.0:
        print(f"\n  Our posterior shows MILD tension with DESI DR2 "
              f"({results['sigma_from_DESI']:.1f} sigma).")
    else:
        print(f"\n  Our posterior is IN TENSION with DESI DR2 "
              f"({results['sigma_from_DESI']:.1f} sigma).")

    print("=" * 70)


def save_results(results, output_dir):
    """Save results to a text file and CSV."""
    # Text summary
    txt_path = os.path.join(output_dir, "quintom_results.txt")
    with open(txt_path, "w") as f:
        f.write("Quintom-B Analysis Results\n")
        f.write("=" * 50 + "\n")
        for key, val in results.items():
            f.write(f"{key}: {val}\n")
    print(f"Saved: {txt_path}")

    # CSV for data explorer embedding
    csv_path = os.path.join(output_dir, "quintom_results.csv")
    with open(csv_path, "w") as f:
        f.write("parameter,value\n")
        for key, val in results.items():
            f.write(f"{key},{val}\n")
    print(f"Saved: {csv_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze w0-wa MCMC chains for quintom-B crossing behavior"
    )
    parser.add_argument(
        "--chain-dir",
        default="chains/w0wa_quintom",
        help="Directory containing MCMC chain files (default: chains/w0wa_quintom)"
    )
    parser.add_argument(
        "--burn-in",
        type=float,
        default=0.3,
        help="Fraction of chain to discard as burn-in (default: 0.3)"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory for output plots (default: same as chain-dir)"
    )
    args = parser.parse_args()

    chain_dir = args.chain_dir
    if not os.path.isabs(chain_dir):
        chain_dir = os.path.join(os.path.dirname(__file__), chain_dir)

    output_dir = args.output_dir or chain_dir
    os.makedirs(output_dir, exist_ok=True)

    print(f"Chain directory: {chain_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Burn-in fraction: {args.burn_in}")

    # Load chains
    w0_samples = None
    wa_samples = None
    weights = None

    if HAS_GETDIST:
        try:
            samples = load_chains_getdist(chain_dir, burn_in=args.burn_in)
            print(f"Loaded {samples.numrows} samples via getdist")

            # Extract w0 and wa
            w0_par = samples.paramNames.parWithName("w")
            wa_par = samples.paramNames.parWithName("wa")

            if w0_par is None or wa_par is None:
                print("ERROR: Could not find 'w' and/or 'wa' parameters in chain.")
                print(f"Available parameters: {[p.name for p in samples.paramNames.names]}")
                sys.exit(1)

            w0_samples = samples.getParams().w
            wa_samples = samples.getParams().wa
            weights = samples.weights

            # Triangle plot
            plot_getdist_triangle(samples, output_dir)

        except Exception as e:
            print(f"getdist loading failed: {e}")
            print("Falling back to manual loading...")
            HAS_GETDIST_local = False
    else:
        HAS_GETDIST_local = False

    if w0_samples is None:
        # Manual loading
        weights_raw, params_data, param_names = load_chains_manual(
            chain_dir, burn_in=args.burn_in
        )
        print(f"Loaded {len(weights_raw)} samples manually")
        print(f"Parameters: {param_names}")

        w0_idx = find_param_index(param_names, "w")
        wa_idx = find_param_index(param_names, "wa")

        if w0_idx is None or wa_idx is None:
            print(f"ERROR: Could not find w0 (idx={w0_idx}) or wa (idx={wa_idx})")
            print(f"Available: {param_names}")
            sys.exit(1)

        w0_samples = params_data[:, w0_idx]
        wa_samples = params_data[:, wa_idx]
        weights = weights_raw

    print(f"\nAnalyzing {len(w0_samples)} posterior samples...")
    print(f"  w0 range: [{w0_samples.min():.3f}, {w0_samples.max():.3f}]")
    print(f"  wa range: [{wa_samples.min():.3f}, {wa_samples.max():.3f}]")

    # Compute diagnostics
    results = compute_quintom_statistics(w0_samples, wa_samples, weights)

    # Print summary
    print_summary(results)

    # Save results
    save_results(results, output_dir)

    # Generate plots
    print("\nGenerating plots...")
    plot_w0wa_contours(w0_samples, wa_samples, weights, output_dir)
    plot_wz_reconstruction(w0_samples, wa_samples, weights, output_dir)
    plot_crossing_redshift(w0_samples, wa_samples, weights, output_dir)

    print("\nAnalysis complete. All outputs saved to:", output_dir)


if __name__ == "__main__":
    main()
