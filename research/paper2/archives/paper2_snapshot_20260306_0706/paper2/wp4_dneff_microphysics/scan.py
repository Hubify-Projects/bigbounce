#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WP4: Delta-Neff Parameter Scan
================================

Runs parameter scans over the reheating branching model (Model A)
or the heavy particle decay model (Model B), computes Delta-Neff grids,
applies BBN/CMB constraint masks, and identifies the allowed parameter
region that produces Delta-Neff in the Paper 1 target range (0.10-0.20).

Usage:
    python scan.py --model reheating --output runs/reheat_001/
    python scan.py --model decay --output runs/decay_001/

Outputs:
    - dneff_grid.npy          : 2D (or 3D) Delta-Neff array
    - param_axis_*.npy        : Parameter axis arrays
    - allowed_mask.npy        : Boolean mask for BBN+CMB+target allowed region
    - scan_results.csv        : Flattened parameter + Delta-Neff table
    - summary.json            : Best-fit parameters, constraint counts, metadata

Author: Houston Golden (2026)
"""

from __future__ import division, print_function
import argparse
import json
import os
import sys
import time

import numpy as np

from dneff_models import (
    ReheatingModel, DecayModel,
    DNEFF_BBN_MAX, DNEFF_CMB_MAX, DNEFF_TARGET_LO, DNEFF_TARGET_HI
)


# ===========================================================================
# Reheating model scan
# ===========================================================================

def scan_reheating(output_dir, n_br=100, n_gh=80):
    """
    Scan the reheating branching model over (Br_dr, g_star_hidden)
    at several fixed reheating temperatures.

    Parameters
    ----------
    output_dir : str
        Directory to write results into.
    n_br : int
        Number of points along Br_dr axis (log-spaced).
    n_gh : int
        Number of points along g_star_hidden axis (log-spaced).

    Returns
    -------
    dict
        Summary dictionary with best-fit parameters and metadata.
    """
    print("Running reheating model scan...")
    print("  Br_dr: %d points in [1e-4, 1]" % n_br)
    print("  g_star_hidden: %d points in [1, 106.75]" % n_gh)

    # Parameter axes
    Br_dr_arr = np.logspace(-4, 0, n_br)
    # Clip upper end slightly below 1 to avoid numerical issues
    Br_dr_arr = np.clip(Br_dr_arr, 1.0e-4, 0.999)
    g_hidden_arr = np.logspace(0, np.log10(106.75), n_gh)

    # Reheating temperatures to scan
    Treh_values = [1.0e6, 1.0e9, 1.0e12]

    # Save parameter axes
    np.save(os.path.join(output_dir, "param_Br_dr.npy"), Br_dr_arr)
    np.save(os.path.join(output_dir, "param_g_hidden.npy"), g_hidden_arr)

    # Create 2D meshgrid
    Br_grid, gh_grid = np.meshgrid(Br_dr_arr, g_hidden_arr, indexing="ij")

    all_csv_rows = []
    best_fit = {"dneff": None, "distance": 1.0e10}
    target_center = 0.5 * (DNEFF_TARGET_LO + DNEFF_TARGET_HI)  # 0.15

    for Treh in Treh_values:
        print("  Treh = %.1e GeV ..." % Treh)
        model = ReheatingModel(Treh=Treh)
        dneff_grid = model.compute_dneff(Br_grid, gh_grid)

        # Constraint masks
        mask_bbn = model.allowed_bbn(dneff_grid)
        mask_cmb = model.allowed_cmb(dneff_grid)
        mask_target = model.in_target(dneff_grid)
        mask_all = mask_bbn & mask_cmb & mask_target

        # Save per-Treh results
        tag = "Treh_%.0e" % Treh
        np.save(os.path.join(output_dir, "dneff_grid_%s.npy" % tag), dneff_grid)
        np.save(os.path.join(output_dir, "mask_allowed_%s.npy" % tag), mask_all)

        n_allowed = int(np.sum(mask_all))
        n_total = dneff_grid.size
        print("    Allowed+target points: %d / %d (%.1f%%)" % (
            n_allowed, n_total, 100.0 * n_allowed / n_total
        ))

        # Find best-fit (closest to target_center = 0.15)
        if n_allowed > 0:
            allowed_dneff = dneff_grid[mask_all]
            allowed_br = Br_grid[mask_all]
            allowed_gh = gh_grid[mask_all]
            distances = np.abs(allowed_dneff - target_center)
            idx_best = np.argmin(distances)
            if distances[idx_best] < best_fit["distance"]:
                best_fit = {
                    "dneff": float(allowed_dneff[idx_best]),
                    "Br_dr": float(allowed_br[idx_best]),
                    "g_star_hidden": float(allowed_gh[idx_best]),
                    "Treh_GeV": Treh,
                    "distance": float(distances[idx_best]),
                }

        # Build CSV rows
        for i in range(n_br):
            for j in range(n_gh):
                all_csv_rows.append((
                    Br_dr_arr[i],
                    g_hidden_arr[j],
                    Treh,
                    dneff_grid[i, j],
                    bool(mask_bbn[i, j]),
                    bool(mask_cmb[i, j]),
                    bool(mask_target[i, j]),
                    bool(mask_all[i, j]),
                ))

    # Write CSV
    csv_path = os.path.join(output_dir, "scan_results.csv")
    with open(csv_path, "w") as f:
        f.write("Br_dr,g_star_hidden,Treh_GeV,Delta_Neff,BBN_OK,CMB_OK,Target,Allowed\n")
        for row in all_csv_rows:
            f.write("%.6e,%.6e,%.6e,%.6e,%s,%s,%s,%s\n" % (
                row[0], row[1], row[2], row[3],
                row[4], row[5], row[6], row[7]
            ))
    print("  CSV written: %s (%d rows)" % (csv_path, len(all_csv_rows)))

    # Summary
    summary = {
        "model": "reheating",
        "n_Br_dr": n_br,
        "n_g_hidden": n_gh,
        "Treh_values_GeV": Treh_values,
        "total_points": len(all_csv_rows),
        "constraints": {
            "BBN_max": DNEFF_BBN_MAX,
            "CMB_max": DNEFF_CMB_MAX,
            "target_lo": DNEFF_TARGET_LO,
            "target_hi": DNEFF_TARGET_HI,
        },
        "best_fit": best_fit,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }

    summary_path = os.path.join(output_dir, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print("  Summary written: %s" % summary_path)

    if best_fit["dneff"] is not None:
        print("\n  Best fit for Delta-Neff ~ 0.15:")
        print("    Br_dr          = %.4e" % best_fit["Br_dr"])
        print("    g_star_hidden  = %.2f" % best_fit["g_star_hidden"])
        print("    Treh           = %.1e GeV" % best_fit["Treh_GeV"])
        print("    Delta-Neff     = %.4f" % best_fit["dneff"])
    else:
        print("\n  WARNING: No parameter point found in target range!")

    return summary


# ===========================================================================
# Decay model scan
# ===========================================================================

def scan_decay(output_dir, n_mx=100, n_tau=100):
    """
    Scan the heavy particle decay model over (m_X, tau_X)
    at fixed (Br_dark, Y_X), then vary those.

    Parameters
    ----------
    output_dir : str
        Directory to write results into.
    n_mx : int
        Number of points along m_X axis (log-spaced).
    n_tau : int
        Number of points along tau_X axis (log-spaced).

    Returns
    -------
    dict
        Summary dictionary with best-fit parameters and metadata.
    """
    print("Running decay model scan...")
    print("  m_X: %d points in [1, 1e12] GeV" % n_mx)
    print("  tau_X: %d points in [1e-6, 1e6] seconds" % n_tau)

    # Parameter axes
    m_X_arr = np.logspace(0, 12, n_mx)      # 1 GeV to 1e12 GeV
    tau_X_arr = np.logspace(-6, 6, n_tau)    # 1e-6 to 1e6 seconds

    # Save parameter axes
    np.save(os.path.join(output_dir, "param_m_X.npy"), m_X_arr)
    np.save(os.path.join(output_dir, "param_tau_X.npy"), tau_X_arr)

    model = DecayModel()

    # Create meshgrid
    mx_grid, tau_grid = np.meshgrid(m_X_arr, tau_X_arr, indexing="ij")

    # --- Fiducial scan: Br_dark=1, Y_X=1e-10 ---
    fiducial_configs = [
        {"Br_dark": 1.0, "Y_X": 1.0e-10, "tag": "fiducial"},
        {"Br_dark": 0.1, "Y_X": 1.0e-10, "tag": "Br01"},
        {"Br_dark": 1.0, "Y_X": 1.0e-8,  "tag": "YX1e8"},
        {"Br_dark": 0.5, "Y_X": 1.0e-9,  "tag": "Br05_YX1e9"},
    ]

    all_csv_rows = []
    best_fit = {"dneff": None, "distance": 1.0e10}
    target_center = 0.5 * (DNEFF_TARGET_LO + DNEFF_TARGET_HI)

    for config in fiducial_configs:
        Br_dark = config["Br_dark"]
        Y_X = config["Y_X"]
        tag = config["tag"]

        print("  Config: Br_dark=%.2f, Y_X=%.1e (%s) ..." % (Br_dark, Y_X, tag))

        dneff_grid = model.compute_dneff(mx_grid, tau_grid, Br_dark, Y_X)

        # Constraint masks
        mask_bbn = model.allowed_bbn(dneff_grid)
        mask_cmb = model.allowed_cmb(dneff_grid)
        mask_target = model.in_target(dneff_grid)
        mask_all = mask_bbn & mask_cmb & mask_target

        # Save per-config results
        np.save(os.path.join(output_dir, "dneff_grid_%s.npy" % tag), dneff_grid)
        np.save(os.path.join(output_dir, "mask_allowed_%s.npy" % tag), mask_all)

        n_allowed = int(np.sum(mask_all))
        n_total = dneff_grid.size
        print("    Allowed+target points: %d / %d (%.1f%%)" % (
            n_allowed, n_total, 100.0 * n_allowed / n_total
        ))

        # Best fit
        if n_allowed > 0:
            allowed_dneff = dneff_grid[mask_all]
            allowed_mx = mx_grid[mask_all]
            allowed_tau = tau_grid[mask_all]
            distances = np.abs(allowed_dneff - target_center)
            idx_best = np.argmin(distances)
            if distances[idx_best] < best_fit["distance"]:
                best_fit = {
                    "dneff": float(allowed_dneff[idx_best]),
                    "m_X_GeV": float(allowed_mx[idx_best]),
                    "tau_X_sec": float(allowed_tau[idx_best]),
                    "Br_dark": Br_dark,
                    "Y_X": Y_X,
                    "config": tag,
                    "distance": float(distances[idx_best]),
                }

        # Build CSV rows
        for i in range(n_mx):
            for j in range(n_tau):
                all_csv_rows.append((
                    m_X_arr[i],
                    tau_X_arr[j],
                    Br_dark,
                    Y_X,
                    dneff_grid[i, j],
                    bool(mask_bbn[i, j]),
                    bool(mask_cmb[i, j]),
                    bool(mask_target[i, j]),
                    bool(mask_all[i, j]),
                ))

    # Write CSV
    csv_path = os.path.join(output_dir, "scan_results.csv")
    with open(csv_path, "w") as f:
        f.write("m_X_GeV,tau_X_sec,Br_dark,Y_X,Delta_Neff,BBN_OK,CMB_OK,Target,Allowed\n")
        for row in all_csv_rows:
            f.write("%.6e,%.6e,%.6e,%.6e,%.6e,%s,%s,%s,%s\n" % (
                row[0], row[1], row[2], row[3], row[4],
                row[5], row[6], row[7], row[8]
            ))
    print("  CSV written: %s (%d rows)" % (csv_path, len(all_csv_rows)))

    # Summary
    summary = {
        "model": "decay",
        "n_m_X": n_mx,
        "n_tau_X": n_tau,
        "configs": fiducial_configs,
        "total_points": len(all_csv_rows),
        "constraints": {
            "BBN_max": DNEFF_BBN_MAX,
            "CMB_max": DNEFF_CMB_MAX,
            "target_lo": DNEFF_TARGET_LO,
            "target_hi": DNEFF_TARGET_HI,
        },
        "best_fit": best_fit,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }

    summary_path = os.path.join(output_dir, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print("  Summary written: %s" % summary_path)

    if best_fit["dneff"] is not None:
        print("\n  Best fit for Delta-Neff ~ 0.15:")
        print("    m_X    = %.4e GeV" % best_fit["m_X_GeV"])
        print("    tau_X  = %.4e sec" % best_fit["tau_X_sec"])
        print("    Br_dark = %.2f" % best_fit["Br_dark"])
        print("    Y_X    = %.1e" % best_fit["Y_X"])
        print("    Delta-Neff = %.4f" % best_fit["dneff"])
    else:
        print("\n  WARNING: No parameter point found in target range!")

    return summary


# ===========================================================================
# Main
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(
        description="WP4 Delta-Neff parameter scan"
    )
    parser.add_argument(
        "--model", required=True, choices=["reheating", "decay"],
        help="Which model to scan: 'reheating' (Model A) or 'decay' (Model B)"
    )
    parser.add_argument(
        "--output", required=True,
        help="Output directory for results (will be created if needed)"
    )
    parser.add_argument(
        "--n-primary", type=int, default=100,
        help="Number of grid points along primary axis (default: 100)"
    )
    parser.add_argument(
        "--n-secondary", type=int, default=80,
        help="Number of grid points along secondary axis (default: 80)"
    )
    args = parser.parse_args()

    # Create output directory
    if not os.path.exists(args.output):
        os.makedirs(args.output)
        print("Created output directory: %s" % args.output)

    t_start = time.time()

    if args.model == "reheating":
        summary = scan_reheating(args.output, n_br=args.n_primary, n_gh=args.n_secondary)
    elif args.model == "decay":
        summary = scan_decay(args.output, n_mx=args.n_primary, n_tau=args.n_secondary)
    else:
        print("ERROR: Unknown model '%s'" % args.model)
        sys.exit(1)

    elapsed = time.time() - t_start
    print("\nScan completed in %.1f seconds." % elapsed)
    print("Results in: %s" % os.path.abspath(args.output))

    return summary


if __name__ == "__main__":
    main()
