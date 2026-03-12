"""
monte_carlo_sensitivity.py — Monte Carlo sensitivity analysis for WP5
=====================================================================

Samples the TTT and parity-odd model parameters, computes A_0 for
each realization, and produces:
  - CSV of all MC samples
  - Summary statistics (median A_0 per epsilon_PO bin)
  - Distribution of required epsilon_PO for A_0 = 0.003
  - Conservative upper bound (95th percentile)
  - Publication-quality figures

Usage:
  python monte_carlo_sensitivity.py --n_samples 100000 --output runs/RUN_ID/
  python monte_carlo_sensitivity.py --n_samples 1000 --output runs/test/
"""

import os
import sys
import argparse
import time

import numpy as np
from scipy import stats

# Local imports
from parity_bias_model import ParityBiasModel


def sample_parameters(n_samples, rng):
    """
    Draw Monte Carlo samples of the model parameters.

    Sampling distributions:
      lambda_mean      : log-normal, median 0.035, sigma = 0.01
      sigma_lnlambda   : uniform [0.4, 0.6]
      delta_rms         : uniform [0.5, 2.0]
      z_formation       : uniform [0.5, 3.0]
      epsilon_PO        : log-uniform [0.01, 1.0]

    Parameters
    ----------
    n_samples : int
        Number of MC samples.
    rng : numpy.random.Generator
        Random number generator.

    Returns
    -------
    params : dict of ndarray
        Dictionary with keys: lambda_mean, sigma_lnlambda, delta_rms,
        z_formation, epsilon_PO.
    """
    # lambda_mean: log-normal with mean 0.035, width sigma=0.01
    # For log-normal parametrization: mu = ln(0.035), s ~ 0.01/0.035
    lam_mu = np.log(0.035)
    lam_s = 0.01 / 0.035  # fractional width ~ 0.286
    lambda_mean = rng.lognormal(mean=lam_mu, sigma=lam_s, size=n_samples)

    # sigma_lnlambda: uniform [0.4, 0.6]
    sigma_lnlambda = rng.uniform(0.4, 0.6, size=n_samples)

    # delta_rms: uniform [0.5, 2.0]
    delta_rms = rng.uniform(0.5, 2.0, size=n_samples)

    # z_formation: uniform [0.5, 3.0]
    z_formation = rng.uniform(0.5, 3.0, size=n_samples)

    # epsilon_PO: log-uniform [0.01, 1.0]
    log_eps_min = np.log10(0.01)
    log_eps_max = np.log10(1.0)
    log_eps = rng.uniform(log_eps_min, log_eps_max, size=n_samples)
    epsilon_PO = 10.0 ** log_eps

    return {
        "lambda_mean": lambda_mean,
        "sigma_lnlambda": sigma_lnlambda,
        "delta_rms": delta_rms,
        "z_formation": z_formation,
        "epsilon_PO": epsilon_PO,
    }


def compute_A0_vectorized(params):
    """
    Compute A_0 for all MC samples (vectorized).

    A_0 = epsilon_PO * (2/pi) * (2/3) * lambda_mean / delta_rms  [Eq. 11]

    Parameters
    ----------
    params : dict of ndarray
        Sampled parameters.

    Returns
    -------
    A0 : ndarray
        Dipole amplitudes for all samples.
    """
    mean_cos = 2.0 / np.pi
    g = (2.0 / 3.0) * params["lambda_mean"] / params["delta_rms"]
    A0 = params["epsilon_PO"] * mean_cos * g
    return A0


def compute_required_epsilon(params, A0_target=0.003):
    """
    For each MC sample, compute the epsilon_PO needed for A_0 = A0_target.

    epsilon_PO_required = A0_target / (<|cos theta|> * g)        [Eq. 12]

    Parameters
    ----------
    params : dict of ndarray
        Sampled parameters (lambda_mean, delta_rms used).
    A0_target : float
        Target dipole amplitude.

    Returns
    -------
    eps_required : ndarray
        Required epsilon_PO for each parameter combination.
    """
    mean_cos = 2.0 / np.pi
    g = (2.0 / 3.0) * params["lambda_mean"] / params["delta_rms"]
    denominator = mean_cos * g
    eps_required = A0_target / denominator
    return eps_required


def compute_summary_statistics(params, A0, eps_required):
    """
    Compute summary statistics from MC run.

    Returns
    -------
    summary : dict
        Dictionary with summary statistics.
    """
    # Bin A_0 by epsilon_PO
    eps = params["epsilon_PO"]
    log_eps_bins = np.linspace(np.log10(0.01), np.log10(1.0), 21)
    eps_bin_centers = 10.0 ** (0.5 * (log_eps_bins[:-1] + log_eps_bins[1:]))
    log_eps_vals = np.log10(eps)
    bin_indices = np.digitize(log_eps_vals, log_eps_bins) - 1

    median_A0 = np.full(len(eps_bin_centers), np.nan)
    p16_A0 = np.full(len(eps_bin_centers), np.nan)
    p84_A0 = np.full(len(eps_bin_centers), np.nan)
    p05_A0 = np.full(len(eps_bin_centers), np.nan)
    p95_A0 = np.full(len(eps_bin_centers), np.nan)

    for i in range(len(eps_bin_centers)):
        mask = bin_indices == i
        if np.sum(mask) > 0:
            vals = A0[mask]
            median_A0[i] = np.median(vals)
            p16_A0[i] = np.percentile(vals, 16)
            p84_A0[i] = np.percentile(vals, 84)
            p05_A0[i] = np.percentile(vals, 2.5)
            p95_A0[i] = np.percentile(vals, 97.5)

    summary = {
        "eps_bin_centers": eps_bin_centers,
        "median_A0": median_A0,
        "p16_A0": p16_A0,
        "p84_A0": p84_A0,
        "p05_A0": p05_A0,
        "p95_A0": p95_A0,
        "eps_required_median": np.median(eps_required),
        "eps_required_p16": np.percentile(eps_required, 16),
        "eps_required_p84": np.percentile(eps_required, 84),
        "eps_required_p05": np.percentile(eps_required, 2.5),
        "eps_required_p95": np.percentile(eps_required, 97.5),
        "A0_95th_at_eps02": None,
    }

    # Conservative upper bound: 95th percentile of A_0 at epsilon_PO ~ 0.2
    mask_02 = (eps > 0.15) & (eps < 0.25)
    if np.sum(mask_02) > 0:
        summary["A0_95th_at_eps02"] = np.percentile(A0[mask_02], 95)

    return summary


def save_csv(output_dir, params, A0, eps_required):
    """Save all MC samples to CSV."""
    filepath = os.path.join(output_dir, "mc_samples.csv")
    header = "epsilon_PO,lambda_mean,sigma_lnlambda,delta_rms,z_formation,A0,eps_required"
    data = np.column_stack([
        params["epsilon_PO"],
        params["lambda_mean"],
        params["sigma_lnlambda"],
        params["delta_rms"],
        params["z_formation"],
        A0,
        eps_required,
    ])
    np.savetxt(filepath, data, delimiter=",", header=header, comments="",
               fmt="%.8e")
    print("  Saved: %s (%d rows)" % (filepath, len(A0)))


def save_summary(output_dir, summary, n_samples):
    """Save summary statistics to text file."""
    filepath = os.path.join(output_dir, "summary.txt")
    with open(filepath, "w") as f:
        f.write("WP5 Monte Carlo Sensitivity — Summary\n")
        f.write("=" * 50 + "\n")
        f.write("N samples: %d\n\n" % n_samples)

        f.write("Required epsilon_PO for A_0 = 0.003:\n")
        f.write("  Median: %.4f\n" % summary["eps_required_median"])
        f.write("  68%% CI: [%.4f, %.4f]\n" % (
            summary["eps_required_p16"], summary["eps_required_p84"]))
        f.write("  95%% CI: [%.4f, %.4f]\n" % (
            summary["eps_required_p05"], summary["eps_required_p95"]))
        f.write("\n")

        if summary["A0_95th_at_eps02"] is not None:
            f.write("Conservative upper bound at eps_PO ~ 0.2:\n")
            f.write("  A_0 (95th percentile): %.6f\n" % summary["A0_95th_at_eps02"])
        f.write("\n")

        f.write("Binned A_0 vs epsilon_PO:\n")
        f.write("%-12s  %-12s  %-12s  %-12s\n" % (
            "eps_PO", "A0_median", "A0_16th", "A0_84th"))
        for i in range(len(summary["eps_bin_centers"])):
            if not np.isnan(summary["median_A0"][i]):
                f.write("%-12.4f  %-12.6f  %-12.6f  %-12.6f\n" % (
                    summary["eps_bin_centers"][i],
                    summary["median_A0"][i],
                    summary["p16_A0"][i],
                    summary["p84_A0"][i]))

    print("  Saved: %s" % filepath)


def plot_scaling_curve(output_dir, summary):
    """
    Plot A_0 vs epsilon_PO with 1sigma/2sigma uncertainty bands.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    eps = summary["eps_bin_centers"]
    valid = ~np.isnan(summary["median_A0"])

    # 2-sigma band
    ax.fill_between(
        eps[valid], summary["p05_A0"][valid], summary["p95_A0"][valid],
        alpha=0.2, color="steelblue", label=r"$2\sigma$ band"
    )
    # 1-sigma band
    ax.fill_between(
        eps[valid], summary["p16_A0"][valid], summary["p84_A0"][valid],
        alpha=0.4, color="steelblue", label=r"$1\sigma$ band"
    )
    # Median
    ax.plot(eps[valid], summary["median_A0"][valid], "o-",
            color="navy", lw=2, ms=4, label="Median")

    # Observed A_0 line
    ax.axhline(y=0.003, color="crimson", ls="--", lw=1.5,
               label=r"$A_0 \approx 0.003$ (Shamir 2024)")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$\varepsilon_{\mathrm{PO}}$ (parity-odd coupling)", fontsize=13)
    ax.set_ylabel(r"$A_0$ (dipole amplitude)", fontsize=13)
    ax.set_title("Galaxy Spin Dipole Amplitude vs Parity-Odd Coupling", fontsize=14)
    ax.legend(fontsize=11, loc="upper left")
    ax.grid(True, alpha=0.3, which="both")
    ax.set_xlim(0.01, 1.0)

    plt.tight_layout()
    filepath = os.path.join(output_dir, "A0_vs_epsPO.png")
    fig.savefig(filepath, dpi=150)
    plt.close(fig)
    print("  Saved: %s" % filepath)


def plot_required_epsilon_histogram(output_dir, eps_required):
    """
    Histogram of required epsilon_PO for A_0 = 0.003.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    # Clip extreme values for visualization
    eps_clipped = np.clip(eps_required, 0.01, 10.0)
    log_eps = np.log10(eps_clipped)

    ax.hist(log_eps, bins=60, color="steelblue", edgecolor="navy",
            alpha=0.7, density=True)

    median_val = np.median(eps_required)
    ax.axvline(np.log10(median_val), color="crimson", ls="--", lw=2,
               label="Median = %.3f" % median_val)

    p16 = np.percentile(eps_required, 16)
    p84 = np.percentile(eps_required, 84)
    ax.axvline(np.log10(p16), color="orange", ls=":", lw=1.5,
               label="16th pctl = %.3f" % p16)
    ax.axvline(np.log10(p84), color="orange", ls=":", lw=1.5,
               label="84th pctl = %.3f" % p84)

    ax.set_xlabel(r"$\log_{10}(\varepsilon_{\mathrm{PO,\,required}})$",
                  fontsize=13)
    ax.set_ylabel("Probability density", fontsize=13)
    ax.set_title(r"Required $\varepsilon_{\mathrm{PO}}$ for $A_0 = 0.003$",
                 fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    filepath = os.path.join(output_dir, "required_epsPO_hist.png")
    fig.savefig(filepath, dpi=150)
    plt.close(fig)
    print("  Saved: %s" % filepath)


def plot_corner(output_dir, params, A0):
    """
    Corner-style plot of key parameter correlations.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    keys = ["epsilon_PO", "lambda_mean", "delta_rms", "z_formation"]
    labels = [
        r"$\varepsilon_{\mathrm{PO}}$",
        r"$\langle\lambda\rangle$",
        r"$\delta_{\mathrm{rms}}$",
        r"$z_{\mathrm{form}}$",
    ]
    n_params = len(keys)

    # Subsample for plotting efficiency
    n_plot = min(5000, len(A0))
    rng_plot = np.random.default_rng(42)
    idx = rng_plot.choice(len(A0), size=n_plot, replace=False)

    fig, axes = plt.subplots(n_params, n_params, figsize=(12, 12))

    for i in range(n_params):
        for j in range(n_params):
            ax = axes[i, j]
            if j > i:
                ax.set_visible(False)
                continue

            xi = params[keys[j]][idx]
            yi = params[keys[i]][idx]

            if i == j:
                # Diagonal: histogram
                ax.hist(xi, bins=40, color="steelblue", alpha=0.7,
                        edgecolor="navy")
            else:
                # Off-diagonal: scatter colored by A_0
                sc = ax.scatter(xi, yi, c=np.log10(A0[idx]), s=1,
                                alpha=0.3, cmap="viridis", rasterized=True)

            if i == n_params - 1:
                ax.set_xlabel(labels[j], fontsize=11)
            else:
                ax.set_xticklabels([])

            if j == 0 and i != 0:
                ax.set_ylabel(labels[i], fontsize=11)
            elif j != 0:
                ax.set_yticklabels([])

            ax.tick_params(labelsize=8)

    fig.suptitle("Parameter Correlations (color = log$_{10}$ $A_0$)",
                 fontsize=14, y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    filepath = os.path.join(output_dir, "corner_plot.png")
    fig.savefig(filepath, dpi=120)
    plt.close(fig)
    print("  Saved: %s" % filepath)


def main():
    parser = argparse.ArgumentParser(
        description="WP5 Monte Carlo sensitivity analysis for spin dipole amplitude"
    )
    parser.add_argument(
        "--n_samples", type=int, default=100000,
        help="Number of MC samples (default: 100000)"
    )
    parser.add_argument(
        "--output", type=str, required=True,
        help="Output directory (e.g., runs/RUN_ID/)"
    )
    parser.add_argument(
        "--seed", type=int, default=2026,
        help="Random seed (default: 2026)"
    )
    parser.add_argument(
        "--no_plots", action="store_true",
        help="Skip figure generation"
    )
    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    print("WP5 Monte Carlo Sensitivity Analysis")
    print("=" * 50)
    print("  N samples: %d" % args.n_samples)
    print("  Output:    %s" % args.output)
    print("  Seed:      %d" % args.seed)
    print()

    rng = np.random.default_rng(args.seed)

    # Step 1: Sample parameters
    t0 = time.time()
    print("Step 1: Sampling parameters...")
    params = sample_parameters(args.n_samples, rng)
    print("  Done in %.2f s" % (time.time() - t0))

    # Step 2: Compute A_0 for all samples
    t0 = time.time()
    print("Step 2: Computing A_0 (vectorized)...")
    A0 = compute_A0_vectorized(params)
    print("  Done in %.2f s" % (time.time() - t0))
    print("  A_0 range: [%.2e, %.2e]" % (A0.min(), A0.max()))
    print("  A_0 median: %.6f" % np.median(A0))

    # Step 3: Compute required epsilon_PO for A_0 = 0.003
    t0 = time.time()
    print("Step 3: Computing required epsilon_PO...")
    eps_required = compute_required_epsilon(params, A0_target=0.003)
    print("  Done in %.2f s" % (time.time() - t0))
    print("  eps_PO required median: %.4f" % np.median(eps_required))
    print("  eps_PO required 68%% CI: [%.4f, %.4f]" % (
        np.percentile(eps_required, 16), np.percentile(eps_required, 84)))

    # Step 4: Summary statistics
    t0 = time.time()
    print("Step 4: Computing summary statistics...")
    summary = compute_summary_statistics(params, A0, eps_required)
    print("  Done in %.2f s" % (time.time() - t0))

    # Step 5: Save outputs
    print("Step 5: Saving outputs...")
    save_csv(args.output, params, A0, eps_required)
    save_summary(args.output, summary, args.n_samples)

    # Step 6: Generate figures
    if not args.no_plots:
        print("Step 6: Generating figures...")
        plot_scaling_curve(args.output, summary)
        plot_required_epsilon_histogram(args.output, eps_required)
        plot_corner(args.output, params, A0)
    else:
        print("Step 6: Skipping figures (--no_plots)")

    print("\nDone. All outputs in: %s" % args.output)


if __name__ == "__main__":
    main()
