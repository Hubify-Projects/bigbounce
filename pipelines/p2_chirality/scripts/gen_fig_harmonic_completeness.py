#!/usr/bin/env python3
"""Generate fig_harmonic_completeness.png from c9b real injection-recovery data.

Source artifact:
  outputs/canonical_provenance/c9/c9b_injection_completeness.json
    -- 1000 injections / amplitude / axis on label-shuffle backgrounds through
       the apodized-footprint MASTER ell=1 channel; 500-MC null per realization;
       seed 42. Real, version-controlled completeness measurement (not
       interpolation).

Plots the axis-averaged P(detect >= 3sigma) as a function of injected
amplitude A_p for the 4 sampled amplitudes (0.5%, 0.75%, 1.7%, 3.0%) plus the
3 per-axis (x, y, z_fiducial) curves. Horizontal reference lines mark the
50% and 95% recovery thresholds; the 92% completeness at A_p = 0.5%
(headline result cited in the Conclusions text + Table tab:harmonic_completeness)
is annotated explicitly.

Output: pipelines/p2_chirality/fig_harmonic_completeness.png (paper root,
co-located with other figures the .tex \\includegraphics calls expect).
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "outputs" / "canonical_provenance" / "c9" / "c9b_injection_completeness.json"
OUT_PNG = ROOT / "fig_harmonic_completeness.png"
OUT_PDF = ROOT / "fig_harmonic_completeness.pdf"


def load_curves():
    with ARTIFACT.open() as f:
        data = json.load(f)
    comp = data["completeness"]
    keys = sorted(comp.keys(), key=lambda k: comp[k]["amplitude_Ap"])
    A = np.array([comp[k]["amplitude_Ap"] for k in keys])
    avg = np.array([comp[k]["axis_averaged"]["p_detect_3sigma"] for k in keys])
    per_axis = {
        ax: np.array([comp[k]["per_axis"][ax]["p_detect_3sigma"] for k in keys])
        for ax in ("x", "y", "z_fiducial")
    }
    null = data["null"]
    return A, avg, per_axis, null, data


def main():
    A, avg, per_axis, null, data = load_curves()

    # Convert to percent for plotting (paper convention: A_p in %).
    A_pct = A * 100.0

    fig, ax = plt.subplots(figsize=(6.0, 4.4), dpi=200)

    # Per-axis curves (thin, gray-shaded family).
    axis_styles = {
        "x":          dict(color="#1f77b4", marker="s", ls="--", label=r"axis $\hat x$"),
        "y":          dict(color="#2ca02c", marker="^", ls="--", label=r"axis $\hat y$"),
        "z_fiducial": dict(color="#d62728", marker="D", ls="--", label=r"axis $\hat z$ (fiducial)"),
    }
    for ax_name, vec in per_axis.items():
        style = axis_styles[ax_name]
        ax.plot(A_pct, vec, lw=1.0, alpha=0.75, markersize=5, **style)

    # Axis-averaged curve (heavy, black).
    ax.plot(A_pct, avg, color="black", marker="o", lw=2.0, markersize=7,
            label=r"axis-averaged $P(\geq 3\sigma)$")

    # Thresholds.
    ax.axhline(0.50, color="gray", ls=":", lw=1.0)
    ax.axhline(0.95, color="gray", ls=":", lw=1.0)
    ax.text(2.95, 0.50 + 0.012, "50% recovery", ha="right", va="bottom",
            fontsize=8, color="gray")
    ax.text(2.95, 0.95 + 0.012, "95% recovery", ha="right", va="bottom",
            fontsize=8, color="gray")

    # Annotate the headline 92% at 0.5%.
    ax.annotate(
        r"$P(\geq 3\sigma)=0.92$ at $A_p=0.5\%$",
        xy=(0.5, 0.916), xytext=(0.95, 0.62),
        fontsize=8.5,
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
    )
    # A_95 boundary lives below the smallest tested amplitude (0.5% gives
    # 0.916 axis-avg, already above 0.95 floor at 0.75%); record the
    # bracket explicitly.
    ax.annotate(
        r"$A_{95,\mathrm{harm}} \in (0.5\%, 0.75\%]$",
        xy=(0.75, 0.9997), xytext=(1.5, 0.78),
        fontsize=8.5,
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
    )

    ax.set_xscale("log")
    ax.set_xlabel(r"Injected dipole amplitude $A_p$ [%]")
    ax.set_ylabel(r"Recovery probability $P(\sigma_{\rm inj} \geq 3)$")
    ax.set_xlim(0.4, 3.4)
    ax.set_ylim(0.45, 1.03)
    ax.grid(True, which="both", alpha=0.25, lw=0.5)
    ax.legend(loc="lower right", fontsize=8, frameon=True, framealpha=0.92)

    sigma_data = null.get("sigma_data", null.get("c3_reference_sigma"))
    ax.set_title(
        r"Harmonic-channel completeness: MASTER $\ell\!=\!1$, $C^2$ $2^\circ$ apodization"
        + "\n"
        + rf"$10^3$ inj./amp./axis on label-shuffle null; obs.\ $\sigma={sigma_data:.2f}$",
        fontsize=9.5,
    )

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    fig.savefig(OUT_PDF, bbox_inches="tight")
    print(f"wrote {OUT_PNG}")
    print(f"wrote {OUT_PDF}")


if __name__ == "__main__":
    main()
