#!/usr/bin/env python3
"""
Extract physical paper-ready parameter values from a frozen artifact pack.

Usage:
    python extract_physical_parameters.py <frozen_pack_dir>

Reads chain files from frozen_pack_dir/chains/chain_*/spin_torsion.1.txt
Outputs physical values with validated column mapping.
"""
import numpy as np
import json
import os
import sys
from datetime import datetime, timezone


def parse_chain_header(filepath):
    """Parse chain file header, correctly handling the '#' prefix."""
    with open(filepath) as f:
        tokens = f.readline().strip().split()
    if tokens[0] == '#':
        return tokens[1:]
    elif tokens[0].startswith('#'):
        tokens[0] = tokens[0].lstrip('#')
        return tokens
    return tokens


def validate_column_mapping(col_idx, first_row):
    """Validate that column mapping produces physically sensible values."""
    checks = {
        "weight":       (0.5, 1e4,    "MCMC weight"),
        "minuslogpost": (100, 1e6,    "-log(posterior)"),
        "H0":           (40, 100,     "km/s/Mpc"),
        "nnu":          (2, 6,        "N_eff"),
        "ns":           (0.8, 1.2,    "spectral index"),
        "ombh2":        (0.005, 0.1,  "Omega_b h^2"),
        "omch2":        (0.001, 0.99, "Omega_c h^2"),
        "tau":          (0.01, 0.8,   "optical depth"),
        "sigma8":       (0.1, 2.0,    "sigma_8"),
        "omegam":       (0.05, 1.0,   "Omega_m"),
        "delta_neff":   (-2, 3,       "Delta N_eff"),
        "age":          (10, 20,      "Gyr"),
    }
    errors = []
    for param, (lo, hi, desc) in checks.items():
        if param not in col_idx:
            continue
        val = first_row[col_idx[param]]
        if not (lo <= val <= hi):
            errors.append(
                "  {} = {:.6f} NOT in [{}, {}] ({})".format(param, val, lo, hi, desc)
            )
    return errors


def weighted_stats(x, w):
    """Compute weighted mean, std, and 68% CI."""
    wsum = np.sum(w)
    mean = np.sum(w * x) / wsum
    var = np.sum(w * (x - mean)**2) / wsum
    std = np.sqrt(var)

    # 68% CI from weighted quantiles
    sorted_idx = np.argsort(x)
    x_sorted = x[sorted_idx]
    w_sorted = w[sorted_idx]
    cumw = np.cumsum(w_sorted) / wsum
    lo_68 = x_sorted[np.searchsorted(cumw, 0.16)]
    hi_68 = x_sorted[np.searchsorted(cumw, 0.84)]

    return mean, std, lo_68, hi_68


def compute_rhat(chains, pidx, widx, burn_frac=0.3):
    """Compute Gelman-Rubin R-hat for a parameter."""
    chain_means = []
    chain_vars = []
    for d in chains:
        start = int(d.shape[0] * burn_frac)
        x = d[start:, pidx]
        w = d[start:, widx]
        wsum = np.sum(w)
        mean = np.sum(w * x) / wsum
        var = np.sum(w * (x - mean)**2) / wsum
        chain_means.append(mean)
        chain_vars.append(var)
    m = len(chains)
    gm = np.mean(chain_means)
    B = np.sum([(cm - gm)**2 for cm in chain_means]) / (m - 1)
    W = np.mean(chain_vars)
    if W == 0:
        return float("inf")
    return np.sqrt((W + B) / W) - 1


def compute_ess(chains, pidx, burn_frac=0.3):
    """Compute autocorrelation-based ESS."""
    total_ess = 0
    for d in chains:
        start = int(d.shape[0] * burn_frac)
        x = d[start:, pidx]
        n = len(x)
        if n < 50:
            continue
        x_c = x - np.mean(x)
        fft = np.fft.fft(x_c, n=2*n)
        acf = np.fft.ifft(fft * np.conj(fft))[:n].real
        acf = acf / acf[0] if acf[0] != 0 else acf
        tau_int = 1.0
        for lag in range(1, n // 2):
            if acf[lag] < 0.05:
                break
            tau_int += 2 * acf[lag]
        total_ess += n / max(tau_int, 1.0)
    return total_ess


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_physical_parameters.py <frozen_pack_dir>")
        sys.exit(1)

    pack_dir = sys.argv[1]
    chains_dir = os.path.join(pack_dir, "chains")

    if not os.path.isdir(chains_dir):
        print("ERROR: No chains/ directory in {}".format(pack_dir))
        sys.exit(1)

    # Find chain directories
    chain_dirs = sorted([
        d for d in os.listdir(chains_dir)
        if os.path.isdir(os.path.join(chains_dir, d)) and d.startswith("chain_")
    ])

    if not chain_dirs:
        print("ERROR: No chain_* directories found")
        sys.exit(1)

    # Load chains
    col_idx = None
    chains = []
    for cd in chain_dirs:
        fpath = os.path.join(chains_dir, cd, "spin_torsion.1.txt")
        if not os.path.exists(fpath):
            print("WARNING: {} not found, skipping".format(fpath))
            continue
        header = parse_chain_header(fpath)
        if col_idx is None:
            col_idx = {name: i for i, name in enumerate(header)}
        d = np.loadtxt(fpath)
        chains.append(d)

    print("Loaded {} chains from {}".format(len(chains), pack_dir))

    # Validate column mapping
    errors = validate_column_mapping(col_idx, chains[0][0])
    if errors:
        print("\nFATAL: Column mapping validation failed!")
        for e in errors:
            print(e)
        sys.exit(1)
    print("Column mapping validated OK")

    w_idx = col_idx["weight"]
    burn_frac = 0.3

    # Physical parameters to extract
    PARAMS = [
        ("H0",         "Hubble constant",                   "km/s/Mpc",      0.01, 2000),
        ("delta_neff", "Extra effective neutrino species",   "dimensionless", 0.01, 2000),
        ("tau",        "Optical depth to reionization",     "dimensionless", 0.02, 1000),
        ("sigma8",     "RMS matter fluctuations (8 Mpc/h)", "dimensionless", None, None),
        ("omegam",     "Total matter density",              "dimensionless", None, None),
        ("ns",         "Scalar spectral index",             "dimensionless", None, None),
        ("S8",         "sigma8 * sqrt(Omega_m/0.3)",        "dimensionless", None, None),
        ("nnu",        "Effective number of neutrino species", "dimensionless", None, None),
        ("ombh2",      "Baryon density",                    "dimensionless", None, None),
        ("omch2",      "CDM density",                       "dimensionless", None, None),
        ("logA",       "log(10^10 A_s)",                    "dimensionless", None, None),
        ("age",        "Age of the universe",               "Gyr",           None, None),
    ]

    # Compute statistics
    results = {}
    print("\n" + "=" * 90)
    print("PHYSICAL PARAMETER EXTRACTION")
    print("=" * 90)
    print("{:>14} {:>12} {:>10} {:>12} {:>12} {:>10} {:>10}".format(
        "Parameter", "Mean", "Std", "68% lo", "68% hi", "R-1", "ESS"))
    print("-" * 90)

    for pname, desc, unit, rhat_tgt, ess_tgt in PARAMS:
        if pname not in col_idx:
            print("{:>14} — column not found".format(pname))
            continue

        pidx = col_idx[pname]

        # Pool post-burn-in data
        all_x = []
        all_w = []
        for d in chains:
            start = int(d.shape[0] * burn_frac)
            all_x.extend(d[start:, pidx])
            all_w.extend(d[start:, w_idx])
        all_x = np.array(all_x)
        all_w = np.array(all_w)

        mean, std, lo68, hi68 = weighted_stats(all_x, all_w)
        r1 = compute_rhat(chains, pidx, w_idx, burn_frac)
        ess = compute_ess(chains, pidx, burn_frac)

        results[pname] = {
            "mean": float(mean),
            "std": float(std),
            "lo68": float(lo68),
            "hi68": float(hi68),
            "rhat_minus_1": float(r1),
            "ess": float(ess),
            "description": desc,
            "unit": unit,
        }

        rhat_str = "{:.4f}".format(r1)
        ess_str = "{:.0f}".format(ess)
        print("{:>14} {:>12.6f} {:>10.6f} {:>12.6f} {:>12.6f} {:>10} {:>10}".format(
            pname, mean, std, lo68, hi68, rhat_str, ess_str))

    # Output
    output = {
        "source": pack_dir,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "n_chains": len(chains),
        "burn_fraction": burn_frac,
        "total_samples": sum(d.shape[0] for d in chains),
        "column_mapping_validated": True,
        "parameters": results,
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "full_tension_physical_parameters.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print("\nSaved to {}".format(out_path))

    return output


if __name__ == "__main__":
    main()
