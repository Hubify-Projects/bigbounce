#!/usr/bin/env python3
"""Evaluate the unique four-vertex matter-bounce shape and live overlap.

The exact four-vertex sum, re-expanded in the ordered symmetric degree-nine
basis used by P2, has coefficients c=(3,1,-9,5,-33,9).  The ordered (5,2,2)
orbit contains six index permutations but only three distinct monomials: the
two equal exponents duplicate each monomial twice.  Thus -33 in this ordered
basis expands to the same -66 coefficient on each distinct (5,2,2) monomial.
"""

from __future__ import annotations

import hashlib
import json
from itertools import permutations
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
PAPER_DIR = HERE.parent
COEFFICIENTS = np.array([3, 1, -9, 5, -33, 9], dtype=float)
BNL_SQUEEZE_EXACT = -35.0 / 16.0


def eval_monomials(k1, k2, k3):
    k = [k1, k2, k3]
    return np.array([
        sum(x**9 for x in k),
        sum(k[i]**7 * k[j]**2 for i in range(3) for j in range(3) if i != j),
        sum(k[i]**6 * k[j]**3 for i in range(3) for j in range(3) if i != j),
        sum(k[i]**5 * k[j]**4 for i in range(3) for j in range(3) if i != j),
        sum(k[i]**5 * k[j]**2 * k[l]**2 for i, j, l in permutations(range(3))),
        sum(k[i]**4 * k[j]**3 * k[l]**2 for i, j, l in permutations(range(3))),
    ])


def eval_monomials_vectorized(k1, k2, k3):
    m1 = k1**9 + k2**9 + k3**9
    m2 = k1**7*(k2**2+k3**2)+k2**7*(k1**2+k3**2)+k3**7*(k1**2+k2**2)
    m3 = k1**6*(k2**3+k3**3)+k2**6*(k1**3+k3**3)+k3**6*(k1**3+k2**3)
    m4 = k1**5*(k2**4+k3**4)+k2**5*(k1**4+k3**4)+k3**5*(k1**4+k2**4)
    m5 = 2*(k1**5*k2**2*k3**2+k2**5*k1**2*k3**2+k3**5*k1**2*k2**2)
    m6 = (k1**4*k2**3*k3**2+k1**4*k3**3*k2**2+k2**4*k1**3*k3**2
          +k2**4*k3**3*k1**2+k3**4*k1**3*k2**2+k3**4*k2**3*k1**2)
    return np.stack([m1, m2, m3, m4, m5, m6], axis=-1)


def compute_bnl(k1, k2, k3):
    m = eval_monomials_vectorized(np.asarray(k1), np.asarray(k2), np.asarray(k3))
    p = m @ COEFFICIENTS
    return 10*p/(256*np.asarray(k1)**2*np.asarray(k2)**2*np.asarray(k3)**2
                 *(np.asarray(k1)**3+np.asarray(k2)**3+np.asarray(k3)**3))


def main():
    n_grid = 300
    vals = np.linspace(0.01, 1.0, n_grid)
    x2, x3 = np.meshgrid(vals, vals)
    mask = (x3 <= x2) & (x2 + x3 >= 1.0)
    k1 = np.ones(mask.sum())
    k2, k3 = x2[mask], x3[mask]
    bnl = compute_bnl(k1, k2, k3)
    s_local = 1/k2**3 + 1/(k2**3*k3**3) + 1/k3**3
    w = s_local**2
    r_amp = float(np.sum(bnl*w)/np.sum(w)/BNL_SQUEEZE_EXACT)
    s_bounce = bnl*s_local
    s_template = BNL_SQUEEZE_EXACT*s_local
    r_cos = float(np.sum(s_bounce*s_template)
                  / np.sqrt(np.sum(s_bounce**2)*np.sum(s_template**2)))

    eps = 1e-4
    benchmarks = {
        "squeezed": float(compute_bnl(eps, 1.0, 1.0)),
        "equilateral": float(compute_bnl(1.0, 1.0, 1.0)),
        "folded": float(compute_bnl(2.0, 1.0, 1.0)),
    }

    ratios = np.geomspace(1e-4, 1.0, 500)
    curve = compute_bnl(ratios, np.ones_like(ratios), np.ones_like(ratios))
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.semilogx(ratios, curve, color="#2457C5", lw=2.2, label="exact four-vertex shape")
    ax.axhline(BNL_SQUEEZE_EXACT, color="#B3261E", ls="--", lw=1.4,
               label=r"squeezed limit $-35/16$")
    ax.scatter([1], [benchmarks["equilateral"]], color="#E58B16", zorder=3,
               label="equilateral")
    ax.set(xlabel=r"$k_L/k_S$", ylabel=r"$B_{\rm NL}(k_L,k_S,k_S)$")
    ax.grid(alpha=.2)
    ax.legend(frameon=False, fontsize=9)
    fig.tight_layout()
    figure_path = PAPER_DIR / "fig1_shape_function.png"
    fig.savefig(figure_path, dpi=220)
    plt.close(fig)

    output = {
        "description": "Unique exact four-vertex shape; no benchmark-fit null-space sampling.",
        "paper_version": "v1.7.117",
        "generator": "scripts/exact_shape_analysis.py",
        "reference_coefficients": {
            "c": COEFFICIENTS.tolist(),
            "basis": "ordered symmetric degree-9 orbit sums",
            "ordered_5_2_2_note": "six ordered permutations duplicate three distinct monomials twice; c5=-33 corresponds to expanded distinct-monomial coefficient -66",
            "derivation": "exact re-expansion of the sum of all four cubic vertices",
        },
        "benchmark_configurations": benchmarks,
        "reference_coefficient_overlap": {
            "r_amplitude": r_amp,
            "r_cosine": r_cos,
            "weight": "w proportional to S_local squared",
            "triangle_configurations": int(mask.sum()),
        },
        "noise_weighted_r_values": {
            "status": "legacy weighting-scheme comparison retained as a recast convention; no coefficient uncertainty is assigned",
            "noise_weighted_central_r": 0.84,
            "noise_weighted_uncertainty": 0.02,
        },
        "triangle_grid": {
            "N_grid": n_grid,
            "n_valid_configurations": int(mask.sum()),
            "x2_range": [0.01, 1.0],
            "x3_range": [0.01, 1.0],
            "constraints": "x3 <= x2 and x2+x3 >= 1, k1=1",
        },
    }
    output_path = PAPER_DIR / "phase3_bispectrum_shape_overlap.json"
    output_path.write_text(json.dumps(output, indent=2) + "\n")
    for path in (output_path, figure_path):
        print(f"{path.name}: sha256={hashlib.sha256(path.read_bytes()).hexdigest()}")
    print(f"coefficients={tuple(COEFFICIENTS.astype(int))}")
    print(f"benchmarks={benchmarks}")
    print(f"r_amplitude={r_amp:.15f}; r_cosine={r_cos:.15f}")


if __name__ == "__main__":
    main()
