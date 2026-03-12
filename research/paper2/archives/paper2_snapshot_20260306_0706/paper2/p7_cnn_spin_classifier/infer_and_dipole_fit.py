#!/usr/bin/env python
"""
BigBounce P7 — Inference + Toy Dipole Fit.

Runs the trained CNN on the test set, bins CW fraction across the sky,
and fits a simple dipole model: f_CW(theta, phi) = 0.5 + A0 * cos(angle_from_axis).
Bootstrap uncertainty on A0 and dipole direction.

DISCLAIMER: This is a pipeline development exercise. The dipole fit is a
technical demonstration, not a cosmological measurement. Systematic biases
have not been fully characterized.

Usage:
    python infer_and_dipole_fit.py \\
        --model_path runs/dev/model.pt \\
        --data_dir data/ \\
        --output_dir runs/dev/dipole/
"""

from __future__ import print_function, division

import argparse
import json
import logging
import os
import sys
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from scipy.optimize import minimize

warnings.filterwarnings("ignore")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("dipole_fit")

LABEL_TO_IDX = {"cw": 0, "ccw": 1}
IDX_TO_LABEL = {0: "cw", 1: "ccw"}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run inference and fit toy dipole model"
    )
    parser.add_argument("--model_path", type=str, required=True,
                        help="Path to trained model checkpoint")
    parser.add_argument("--data_dir", type=str, default="data/",
                        help="Path to dataset directory")
    parser.add_argument("--output_dir", type=str, default="runs/dev/dipole/",
                        help="Output directory for dipole fit results")
    parser.add_argument("--n_bootstrap", type=int, default=1000,
                        help="Number of bootstrap resamples (default: 1000)")
    parser.add_argument("--n_bins", type=int, default=12,
                        help="Number of angular bins for sky map (default: 12)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed (default: 42)")
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Model loading and inference
# ---------------------------------------------------------------------------

def load_model(model_path, device):
    """Load trained ResNet-18 model."""
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)

    checkpoint = torch.load(model_path, map_location=device, weights_only=False)
    if "model_state_dict" in checkpoint:
        model.load_state_dict(checkpoint["model_state_dict"])
    else:
        model.load_state_dict(checkpoint)

    model = model.to(device)
    model.eval()
    return model


def get_eval_transform(img_size=128):
    """Standard evaluation transform."""
    return transforms.Compose([
        transforms.Resize(img_size),
        transforms.CenterCrop(img_size),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])


def run_inference(model, catalog, data_dir, transform, device):
    """
    Run inference on test set galaxies.

    Returns list of dicts with objid, ra, dec, true_label, pred_label, prob_cw.
    """
    test_df = catalog[catalog["split"] == "test"].reset_index(drop=True)
    results = []

    for _, row in test_df.iterrows():
        objid = str(row["objid"])
        label = row["label"]
        ra = float(row["ra"])
        dec = float(row["dec"])
        img_path = os.path.join(data_dir, "images", label, "{}.jpg".format(objid))

        if not os.path.exists(img_path):
            continue

        try:
            img = Image.open(img_path).convert("RGB")
        except Exception:
            continue

        tensor = transform(img).unsqueeze(0).to(device)
        with torch.no_grad():
            output = model(tensor)
            probs = torch.softmax(output, dim=1).cpu().numpy()[0]

        pred_idx = int(np.argmax(probs))
        results.append({
            "objid": objid,
            "ra": ra,
            "dec": dec,
            "true_label": label,
            "pred_label": IDX_TO_LABEL[pred_idx],
            "prob_cw": float(probs[0]),
            "prob_ccw": float(probs[1]),
        })

    return results


# ---------------------------------------------------------------------------
# Coordinate transforms
# ---------------------------------------------------------------------------

def equatorial_to_galactic(ra_deg, dec_deg):
    """
    Convert equatorial (ra, dec) in degrees to galactic (l, b) in degrees.
    Uses the standard IAU transformation.
    """
    # Reference direction: Galactic center at (ra, dec) = (192.85948, 27.12825) J2000
    # North galactic pole: (ra, dec) = (192.85948, 27.12825) — simplified
    ra_ngp = np.radians(192.85948)
    dec_ngp = np.radians(27.12825)
    l_ncp = np.radians(122.93192)

    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)

    sin_b = (np.sin(dec) * np.sin(dec_ngp)
             + np.cos(dec) * np.cos(dec_ngp) * np.cos(ra - ra_ngp))
    b = np.arcsin(np.clip(sin_b, -1, 1))

    num = np.cos(dec) * np.sin(ra - ra_ngp)
    den = (np.sin(dec) * np.cos(dec_ngp)
           - np.cos(dec) * np.sin(dec_ngp) * np.cos(ra - ra_ngp))
    l = l_ncp - np.arctan2(num, den)

    l = np.degrees(l) % 360
    b = np.degrees(b)
    return l, b


def angular_separation(l1, b1, l2, b2):
    """
    Angular separation between two sky positions in degrees.
    All inputs and output in degrees.
    """
    l1_r, b1_r = np.radians(l1), np.radians(b1)
    l2_r, b2_r = np.radians(l2), np.radians(b2)

    cos_sep = (np.sin(b1_r) * np.sin(b2_r)
               + np.cos(b1_r) * np.cos(b2_r) * np.cos(l1_r - l2_r))
    return np.degrees(np.arccos(np.clip(cos_sep, -1, 1)))


# ---------------------------------------------------------------------------
# Dipole model
# ---------------------------------------------------------------------------

def dipole_model(params, l_gal, b_gal):
    """
    Simple dipole model for CW fraction:
      f_CW = 0.5 + A0 * cos(angle from dipole axis)

    params: [A0, l_dipole, b_dipole]
    l_gal, b_gal: galactic coordinates in degrees (arrays)

    Returns predicted f_CW for each galaxy.
    """
    A0, l_d, b_d = params
    sep = angular_separation(l_gal, b_gal, l_d, b_d)
    return 0.5 + A0 * np.cos(np.radians(sep))


def dipole_cost(params, l_gal, b_gal, is_cw):
    """
    Negative log-likelihood for binomial model.
    is_cw: boolean array (1 if predicted CW, 0 if CCW)
    """
    f_cw = dipole_model(params, l_gal, b_gal)
    # Clip to avoid log(0)
    f_cw = np.clip(f_cw, 1e-6, 1 - 1e-6)
    # Binomial log-likelihood
    ll = np.sum(is_cw * np.log(f_cw) + (1 - is_cw) * np.log(1 - f_cw))
    return -ll


def fit_dipole(l_gal, b_gal, is_cw, rng):
    """
    Fit dipole model to data using scipy.optimize.
    Returns best-fit (A0, l_dipole, b_dipole) and cost.
    """
    best_result = None
    best_cost = np.inf

    # Try multiple random starting points
    for _ in range(20):
        x0 = [
            rng.uniform(-0.05, 0.05),  # A0
            rng.uniform(0, 360),         # l
            rng.uniform(-90, 90),        # b
        ]
        bounds = [(-0.5, 0.5), (0, 360), (-90, 90)]

        try:
            result = minimize(
                dipole_cost, x0, args=(l_gal, b_gal, is_cw),
                method="L-BFGS-B", bounds=bounds,
                options={"maxiter": 1000, "ftol": 1e-10},
            )
            if result.fun < best_cost:
                best_cost = result.fun
                best_result = result
        except Exception:
            continue

    if best_result is None:
        return None

    return {
        "A0": float(best_result.x[0]),
        "l_dipole": float(best_result.x[1]),
        "b_dipole": float(best_result.x[2]),
        "neg_loglik": float(best_result.fun),
        "success": bool(best_result.success),
    }


def bootstrap_dipole(l_gal, b_gal, is_cw, n_bootstrap, rng):
    """
    Bootstrap uncertainty on dipole fit parameters.
    Returns arrays of (A0, l, b) from bootstrap resamples.
    """
    n = len(l_gal)
    A0_samples = []
    l_samples = []
    b_samples = []

    logger.info("Running %d bootstrap resamples...", n_bootstrap)

    for i in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        l_boot = l_gal[idx]
        b_boot = b_gal[idx]
        is_cw_boot = is_cw[idx]

        result = fit_dipole(l_boot, b_boot, is_cw_boot, rng)
        if result is not None:
            A0_samples.append(result["A0"])
            l_samples.append(result["l_dipole"])
            b_samples.append(result["b_dipole"])

        if (i + 1) % 100 == 0:
            logger.info("  Bootstrap %d/%d", i + 1, n_bootstrap)

    return np.array(A0_samples), np.array(l_samples), np.array(b_samples)


# ---------------------------------------------------------------------------
# Sky binning
# ---------------------------------------------------------------------------

def bin_cw_fraction_sky(ra, dec, is_cw, n_ra_bins=12, n_dec_bins=6):
    """
    Bin CW fraction across the sky in RA/Dec bins.

    Returns: ra_centers, dec_centers, cw_frac_grid, count_grid
    """
    ra_edges = np.linspace(0, 360, n_ra_bins + 1)
    dec_edges = np.linspace(-90, 90, n_dec_bins + 1)

    cw_frac_grid = np.full((n_dec_bins, n_ra_bins), np.nan)
    count_grid = np.zeros((n_dec_bins, n_ra_bins), dtype=int)

    for i in range(n_dec_bins):
        for j in range(n_ra_bins):
            mask = (
                (ra >= ra_edges[j]) & (ra < ra_edges[j + 1])
                & (dec >= dec_edges[i]) & (dec < dec_edges[i + 1])
            )
            count = np.sum(mask)
            if count > 0:
                cw_frac_grid[i, j] = np.mean(is_cw[mask])
                count_grid[i, j] = count

    ra_centers = 0.5 * (ra_edges[:-1] + ra_edges[1:])
    dec_centers = 0.5 * (dec_edges[:-1] + dec_edges[1:])

    return ra_centers, dec_centers, cw_frac_grid, count_grid


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_sky_map_scatter(ra, dec, prob_cw, output_dir):
    """
    Scatter plot of P(CW) across the sky on a Mollweide projection.
    """
    # Convert RA to range [-180, 180] for Mollweide
    ra_centered = np.where(ra > 180, ra - 360, ra)
    ra_rad = np.radians(ra_centered)
    dec_rad = np.radians(dec)

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection="mollweide")

    sc = ax.scatter(
        ra_rad, dec_rad, c=prob_cw, cmap="RdBu_r",
        s=8, alpha=0.6, vmin=0, vmax=1, edgecolors="none",
    )
    cbar = plt.colorbar(sc, ax=ax, shrink=0.6, label="P(CW)")
    ax.set_title("Galaxy Spin P(CW) — Sky Map (Mollweide)", fontsize=14)
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, "skymap_pcw_mollweide.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Sky map (Mollweide) saved to %s", path)


def plot_sky_map_binned(ra_centers, dec_centers, cw_frac_grid, output_dir):
    """
    Binned CW fraction map using imshow.
    """
    fig, ax = plt.subplots(figsize=(12, 5))

    im = ax.imshow(
        cw_frac_grid, origin="lower", cmap="RdBu_r",
        extent=[0, 360, -90, 90], aspect="auto",
        vmin=0.3, vmax=0.7,
    )
    plt.colorbar(im, ax=ax, label="CW fraction", shrink=0.8)
    ax.set_xlabel("RA (deg)")
    ax.set_ylabel("Dec (deg)")
    ax.set_title("Binned CW Fraction Across Sky")
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, "skymap_binned.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Binned sky map saved to %s", path)


def plot_dipole_bootstrap(A0_samples, output_dir):
    """Histogram of bootstrap A0 values."""
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(A0_samples, bins=50, color="steelblue", edgecolor="black", linewidth=0.5, alpha=0.8)
    ax.axvline(0, color="red", linestyle="--", alpha=0.7, label="A0 = 0 (no dipole)")

    median = np.median(A0_samples)
    ci_low = np.percentile(A0_samples, 2.5)
    ci_high = np.percentile(A0_samples, 97.5)
    ax.axvline(median, color="orange", linestyle="-", alpha=0.8,
               label="Median = %.4f" % median)
    ax.axvspan(ci_low, ci_high, alpha=0.15, color="orange",
               label="95%% CI: [%.4f, %.4f]" % (ci_low, ci_high))

    ax.set_xlabel("Dipole Amplitude A0")
    ax.set_ylabel("Count")
    ax.set_title("Bootstrap Distribution of Dipole Amplitude")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, "dipole_A0_bootstrap.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Dipole bootstrap histogram saved to %s", path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    rng = np.random.RandomState(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info("=" * 60)
    logger.info("BigBounce P7 — Inference + Dipole Fit")
    logger.info("Model: %s", args.model_path)
    logger.info("Data dir: %s", args.data_dir)
    logger.info("Output dir: %s", args.output_dir)
    logger.info("Bootstrap: %d resamples", args.n_bootstrap)
    logger.info("Device: %s", device)
    logger.info("=" * 60)

    print("")
    print("DISCLAIMER: This is a pipeline development exercise.")
    print("The dipole fit is a technical demonstration, not a cosmological measurement.")
    print("Systematic biases have not been fully characterized.")
    print("")

    # Load model
    if not os.path.exists(args.model_path):
        logger.error("Model not found: %s", args.model_path)
        sys.exit(1)

    model = load_model(args.model_path, device)
    transform = get_eval_transform()

    # Load catalog
    catalog_path = os.path.join(args.data_dir, "catalog.csv")
    if not os.path.exists(catalog_path):
        logger.error("Catalog not found: %s", catalog_path)
        sys.exit(1)

    catalog = pd.read_csv(catalog_path)

    # Run inference
    logger.info("Running inference on test set...")
    results = run_inference(model, catalog, args.data_dir, transform, device)
    logger.info("Inference complete: %d galaxies", len(results))

    if len(results) < 10:
        logger.error("Too few test galaxies (%d) for dipole fit.", len(results))
        sys.exit(1)

    # Extract arrays
    ra = np.array([r["ra"] for r in results])
    dec = np.array([r["dec"] for r in results])
    prob_cw = np.array([r["prob_cw"] for r in results])
    is_cw = np.array([1.0 if r["pred_label"] == "cw" else 0.0 for r in results])

    # Convert to galactic coordinates
    l_gal, b_gal = equatorial_to_galactic(ra, dec)

    # Compute overall CW fraction
    overall_cw_frac = np.mean(is_cw)
    logger.info("Overall CW fraction: %.4f", overall_cw_frac)
    logger.info("Overall mean P(CW): %.4f", np.mean(prob_cw))

    # Bin CW fraction across sky
    ra_centers, dec_centers, cw_frac_grid, count_grid = bin_cw_fraction_sky(
        ra, dec, is_cw, n_ra_bins=args.n_bins, n_dec_bins=args.n_bins // 2,
    )

    # Fit dipole
    logger.info("Fitting dipole model...")
    fit_result = fit_dipole(l_gal, b_gal, is_cw, rng)

    if fit_result is None:
        logger.error("Dipole fit failed.")
        fit_result = {
            "A0": 0.0,
            "l_dipole": 0.0,
            "b_dipole": 0.0,
            "neg_loglik": float("inf"),
            "success": False,
        }

    logger.info("Best-fit dipole:")
    logger.info("  A0 = %.6f", fit_result["A0"])
    logger.info("  (l, b) = (%.2f, %.2f) deg", fit_result["l_dipole"], fit_result["b_dipole"])

    # Bootstrap
    A0_boot, l_boot, b_boot = bootstrap_dipole(
        l_gal, b_gal, is_cw, args.n_bootstrap, rng
    )

    if len(A0_boot) > 0:
        A0_median = float(np.median(A0_boot))
        A0_ci_low = float(np.percentile(A0_boot, 2.5))
        A0_ci_high = float(np.percentile(A0_boot, 97.5))
        A0_std = float(np.std(A0_boot))

        l_median = float(np.median(l_boot))
        b_median = float(np.median(b_boot))

        logger.info("Bootstrap results (%d successful):", len(A0_boot))
        logger.info("  A0: %.6f +/- %.6f", A0_median, A0_std)
        logger.info("  A0 95%% CI: [%.6f, %.6f]", A0_ci_low, A0_ci_high)
        logger.info("  Dipole direction median: (l, b) = (%.1f, %.1f)", l_median, b_median)

        # Check if A0 is consistent with zero
        a0_consistent_zero = A0_ci_low <= 0 <= A0_ci_high
        logger.info("  A0 consistent with zero: %s", "YES" if a0_consistent_zero else "NO")
    else:
        A0_median = 0.0
        A0_ci_low = 0.0
        A0_ci_high = 0.0
        A0_std = 0.0
        l_median = 0.0
        b_median = 0.0
        a0_consistent_zero = True
        logger.warning("All bootstrap fits failed.")

    # -----------------------------------------------------------------------
    # Save results
    # -----------------------------------------------------------------------

    dipole_output = {
        "disclaimer": (
            "This is a pipeline development exercise. "
            "The dipole fit is a technical demonstration, not a cosmological measurement. "
            "Systematic biases have not been fully characterized."
        ),
        "n_galaxies": len(results),
        "overall_cw_fraction": float(overall_cw_frac),
        "overall_mean_prob_cw": float(np.mean(prob_cw)),
        "best_fit": fit_result,
        "bootstrap": {
            "n_resamples": args.n_bootstrap,
            "n_successful": len(A0_boot),
            "A0_median": A0_median,
            "A0_std": A0_std,
            "A0_ci_95_low": A0_ci_low,
            "A0_ci_95_high": A0_ci_high,
            "l_dipole_median": l_median,
            "b_dipole_median": b_median,
            "A0_consistent_with_zero": bool(a0_consistent_zero),
        },
    }

    json_path = os.path.join(args.output_dir, "dipole_fit.json")
    with open(json_path, "w") as f:
        json.dump(dipole_output, f, indent=2)
    logger.info("Dipole fit results saved to %s", json_path)

    # Save inference results
    infer_path = os.path.join(args.output_dir, "test_inference.json")
    with open(infer_path, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Inference results saved to %s", infer_path)

    # -----------------------------------------------------------------------
    # Plots
    # -----------------------------------------------------------------------

    # Sky map (Mollweide scatter)
    plot_sky_map_scatter(ra, dec, prob_cw, args.output_dir)

    # Sky map (binned)
    plot_sky_map_binned(ra_centers, dec_centers, cw_frac_grid, args.output_dir)

    # Bootstrap A0 histogram
    if len(A0_boot) > 0:
        plot_dipole_bootstrap(A0_boot, args.output_dir)

    logger.info("=" * 60)
    logger.info("Dipole fit pipeline complete. All outputs in %s", args.output_dir)
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
