#!/usr/bin/env python3
"""
consistency_window.py — Track C: Parity / CMB Birefringence
============================================================

PURPOSE:
    Given the spin-torsion operator scale alpha/M ~ 10^{-21} GeV^{-1} and
    the observed cosmic birefringence beta ~ 0.30 deg, determine what range
    of the effective photon-torsion vertex factor f_photon is required for
    consistency.

PHYSICS:
    The spin-torsion framework contains a parity-odd operator:
        L_PV = (alpha/M) * epsilon^{abcd} K_{ab} R_{cd}

    This operator does NOT directly couple to photons. A photon-torsion
    coupling must arise through some mechanism (e.g., loop-induced vertex,
    axion-like mixing, or an explicit Chern-Simons coupling to the
    electromagnetic field). We parameterize this unknown coupling as f_photon.

    The resulting birefringence angle is:
        beta = g_eff * C_0
    where:
        g_eff = (alpha/M) * f_photon * M_Pl   [dimensionless]
        C_0   = geometric/cosmological integral [radians]

    For a pseudo-scalar field excursion Delta_phi ~ M_Pl over cosmic history,
    C_0 ~ O(1) radian is a natural scale.

    The KEY QUESTION this script answers:
        What value of f_photon makes alpha/M ~ 10^{-21} GeV^{-1} consistent
        with beta ~ 0.30 deg, given C_0 ~ O(1)?

    ANSWER: f_photon ~ O(1), meaning no fine-tuning is required.

PHOTON-TORSION COUPLING GAP:
    The spin-torsion framework QUALITATIVELY motivates birefringence
    (it contains a parity-odd gravitational operator) but CANNOT predict
    the birefringence angle beta without specifying the photon-torsion
    coupling f_photon. This script maps out the consistency window —
    it does NOT derive f_photon from first principles.

OUTPUT:
    outputs/consistency_window.pdf
    outputs/consistency_window.png
    outputs/consistency_window_summary.txt
"""

import os
import sys
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
ALPHA_OVER_M = 1.0e-21       # GeV^{-1}
M_PL = 2.435e18              # GeV (reduced Planck mass)
DEG_TO_RAD = np.pi / 180.0

# Dimensionless one-loop suppression
EPSILON = ALPHA_OVER_M * M_PL  # ~ 2.435e-3

# ---------------------------------------------------------------------------
# Load published measurements
# ---------------------------------------------------------------------------
def load_measurements(csv_path: str) -> list[dict]:
    """Load birefringence measurements from CSV, excluding superseded ones."""
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


def get_independent_measurements(measurements: list[dict]) -> list[dict]:
    """Return only measurements that are independent, not superseded,
    and without calibration caveats (excludes SPIDER)."""
    return [
        m for m in measurements
        if not m["superseded"] and "calibration" not in m["notes"].lower()
    ]


# ---------------------------------------------------------------------------
# Core physics: consistency window
# ---------------------------------------------------------------------------
def required_f_photon(beta_rad: float, C_0: float) -> float:
    """
    Compute required f_photon given observed beta and assumed C_0.

    beta = g_eff * C_0
    g_eff = (alpha/M) * f_photon * M_Pl = EPSILON * f_photon

    Therefore: f_photon = beta / (EPSILON * C_0)
    """
    return beta_rad / (EPSILON * C_0)


def beta_from_f_photon(f_photon: float, C_0: float) -> float:
    """
    Compute predicted beta [radians] given f_photon and C_0.

    beta = EPSILON * f_photon * C_0
    """
    return EPSILON * f_photon * C_0


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------
def make_consistency_plot(measurements: list[dict], output_dir: str):
    """
    Main plot: f_photon vs beta, showing where observations land.
    """
    fig, ax = plt.subplots(figsize=(9, 6.5))

    # f_photon scan
    f_photon_arr = np.logspace(-2, 3, 500)

    # Plot theory curves for different C_0 values
    C0_values = [0.1, 0.3, 1.0, 3.0, 10.0]
    colors_C0 = ["#bdbdbd", "#969696", "#252525", "#969696", "#bdbdbd"]
    styles_C0 = ["--", "-.", "-", "-.", "--"]

    for C0, color, ls in zip(C0_values, colors_C0, styles_C0):
        beta_theory = np.array([
            beta_from_f_photon(fp, C0) / DEG_TO_RAD for fp in f_photon_arr
        ])
        label = f"$C_0 = {C0}$" if C0 in [0.1, 1.0, 10.0] else None
        lw = 2.5 if C0 == 1.0 else 1.2
        ax.plot(f_photon_arr, beta_theory, color=color, ls=ls, lw=lw,
                label=label, zorder=2)

    # Fiducial curve (C_0 = 1) highlighted
    beta_fiducial = np.array([
        beta_from_f_photon(fp, 1.0) / DEG_TO_RAD for fp in f_photon_arr
    ])
    ax.plot(f_photon_arr, beta_fiducial, color="#9467bd", lw=2.5,
            label=r"$C_0 = 1$ (fiducial)", zorder=3)

    # Observational constraint bands (horizontal)
    obs_colors = {"Eskilt 2022": "#1f77b4",
                  "Diego-Palazuelos & Komatsu 2025": "#ff7f0e",
                  "SPIDER 2025": "#2ca02c"}

    indep = get_independent_measurements(measurements)

    for m in measurements:
        if m["superseded"]:
            continue
        c = obs_colors.get(m["experiment"], "gray")
        beta_c = m["beta_deg"]
        sig = m["sigma_deg"]
        is_spider = "SPIDER" in m["experiment"]
        alpha_fill = 0.08 if is_spider else 0.15

        # 2-sigma band
        ax.axhspan(beta_c - 2 * sig, beta_c + 2 * sig,
                    color=c, alpha=alpha_fill, zorder=0)
        # 1-sigma band
        ax.axhspan(beta_c - sig, beta_c + sig,
                    color=c, alpha=alpha_fill + 0.08, zorder=1)
        # Central value
        ls = ":" if is_spider else "-"
        ax.axhline(beta_c, color=c, ls=ls, lw=1.0, zorder=1,
                    label=f"{m['experiment']}: "
                          f"${beta_c:.3f}^\\circ \\pm {sig:.3f}^\\circ$")

    # Combined Gaussian (Eskilt + ACT DR6 only)
    if len(indep) >= 2:
        weights = [1.0 / m["sigma_deg"] ** 2 for m in indep]
        beta_comb = sum(w * m["beta_deg"] for w, m in zip(weights, indep)) / sum(weights)
        sigma_comb = 1.0 / np.sqrt(sum(weights))
        ax.axhline(beta_comb, color="#d62728", ls="-", lw=1.5, zorder=4,
                    label=f"Combined (Eskilt + ACT): "
                          f"${beta_comb:.3f}^\\circ \\pm {sigma_comb:.3f}^\\circ$")
        ax.axhspan(beta_comb - sigma_comb, beta_comb + sigma_comb,
                    color="#d62728", alpha=0.12, zorder=1)

    # Mark f_photon = 1 line
    ax.axvline(1.0, color="gray", ls=":", lw=1.0, alpha=0.5)
    ax.text(1.05, 0.015, r"$f_\mathrm{photon} = 1$",
            fontsize=9, color="gray", rotation=90, va="bottom")

    # Formatting
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$f_\mathrm{photon}$ (effective photon-torsion vertex factor)",
                  fontsize=12)
    ax.set_ylabel(r"Birefringence angle $\beta$ [degrees]", fontsize=12)
    ax.set_title(
        r"Consistency window: $\beta = \epsilon \cdot f_\mathrm{photon} \cdot C_0$"
        f"\n"
        r"where $\epsilon = (\alpha/M)\,M_\mathrm{{Pl}}$"
        f" = {EPSILON:.3e}",
        fontsize=12,
    )
    ax.set_xlim(1e-2, 1e3)
    ax.set_ylim(0.01, 10)
    ax.legend(fontsize=8, loc="upper left", framealpha=0.9)
    ax.tick_params(which="both", direction="in")

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(output_dir, f"consistency_window.{ext}"),
                    dpi=150, bbox_inches="tight")
    plt.close(fig)


def write_summary(measurements: list[dict], output_dir: str):
    """Write a plain-text summary of the consistency window analysis."""
    indep = get_independent_measurements(measurements)

    # Combined constraint
    weights = [1.0 / m["sigma_deg"] ** 2 for m in indep]
    beta_comb = sum(w * m["beta_deg"] for w, m in zip(weights, indep)) / sum(weights)
    sigma_comb = 1.0 / np.sqrt(sum(weights))

    beta_comb_rad = beta_comb * DEG_TO_RAD

    lines = [
        "=" * 70,
        "Track C: Consistency Window Summary",
        "=" * 70,
        "",
        "SPIN-TORSION PARAMETERS:",
        f"  alpha/M           = {ALPHA_OVER_M:.1e} GeV^{{-1}}",
        f"  M_Pl (reduced)    = {M_PL:.3e} GeV",
        f"  epsilon = (a/M)*M = {EPSILON:.4e}  (dimensionless one-loop suppression)",
        "",
        "PUBLISHED BIREFRINGENCE MEASUREMENTS:",
    ]

    for m in measurements:
        tag = " [SUPERSEDED]" if m["superseded"] else ""
        tag += " [CALIBRATION CAVEAT]" if "SPIDER" in m["experiment"] else ""
        lines.append(
            f"  {m['experiment']:40s}  beta = {m['beta_deg']:.3f} +/- "
            f"{m['sigma_deg']:.3f} deg  ({m['year']}){tag}"
        )

    lines += [
        "",
        "COMBINED INDEPENDENT CONSTRAINT (Eskilt 2022 + ACT DR6):",
        f"  beta_combined     = {beta_comb:.4f} +/- {sigma_comb:.4f} deg",
        f"                    = {beta_comb_rad:.6e} +/- {sigma_comb * DEG_TO_RAD:.6e} rad",
        f"  Detection significance: {beta_comb / sigma_comb:.1f} sigma",
        "",
        "REQUIRED f_photon (for C_0 = 1 radian):",
        f"  f_photon = beta / (epsilon * C_0)",
        f"           = {beta_comb_rad:.4e} / ({EPSILON:.4e} * 1.0)",
        f"           = {required_f_photon(beta_comb_rad, 1.0):.3f}",
        "",
        "INTERPRETATION:",
        f"  For C_0 ~ O(1), the required f_photon ~ {required_f_photon(beta_comb_rad, 1.0):.1f}",
        "  This is an O(1) number, meaning NO FINE-TUNING is required.",
        "  The spin-torsion scale alpha/M ~ 10^{-21} GeV^{-1} is naturally",
        "  consistent with observed cosmic birefringence.",
        "",
        "PHOTON-TORSION COUPLING GAP:",
        "  The spin-torsion framework contains a parity-odd gravitational",
        "  operator but does NOT directly couple to photons. The parameter",
        "  f_photon encodes the unknown photon-torsion coupling vertex.",
        "  This analysis shows the REQUIRED VALUE is O(1), not that it",
        "  has been DERIVED from the theory.",
        "",
        "SENSITIVITY TABLE (f_photon for different C_0):",
    ]

    for C0 in [0.1, 0.3, 1.0, 3.0, 10.0]:
        fp = required_f_photon(beta_comb_rad, C0)
        lines.append(f"  C_0 = {C0:5.1f}  =>  f_photon = {fp:8.3f}")

    lines += ["", "=" * 70]

    with open(os.path.join(output_dir, "consistency_window_summary.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")

    # Also print
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
    print(f"Loaded {len(measurements)} measurements from {csv_path.name}")

    make_consistency_plot(measurements, str(output_dir))
    print(f"Saved consistency_window.pdf and .png to {output_dir}")

    write_summary(measurements, str(output_dir))


if __name__ == "__main__":
    main()
