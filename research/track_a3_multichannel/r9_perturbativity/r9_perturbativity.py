#!/usr/bin/env python3
"""
R9 closure DA3M-R9-13: where does the tree-level in-in bispectrum lose
perturbative control along the c_s window of Sec. VIII?

Context. Sec. VIII tabulates f_NL^after(c_s) = T f_NL^pre(c_s) + Df^bounce(c_s)
and quotes 1.0-1.4e11 at the tensor-viable c_s = 1.5e-3. That number is
arithmetically correct but far outside the regime where a tree-level (leading
order in-in) bispectrum with a quadratic local map is meaningful. This script
states where control is actually lost, using THE PAPER'S OWN criterion from
Sec. V B: 1.2 |f_NL| sigma <~ 1.

Inputs (all already in the paper / its committed artifacts):
  A_s      = 2.1e-9   Planck amplitude at k_* = 0.05 Mpc^-1 (Sec. IV D)
  zeta_rms = sqrt(A_s)                 curvature rms at CMB scales
  f_NL^pre(c_s, L) = -245/16 + 105/(8 c_s^2) - 30 L      (row19_lambda)
  Df^bounce(c_s)   = -(5/24) rho_B (6 c_s^2 - 5)/c_s^4   (row18b_cs_bounce_cubic)
  T, rho_B = 1 - 2T per background      (Table III)

Outputs: results.json, and a printed summary.
No new physics is introduced here; this is a validity boundary for numbers the
paper already prints.
"""
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent

A_S = 2.1e-9
ZETA_RMS = np.sqrt(A_S)
PERT_COEFF = 1.2                     # Sec. V B criterion 1.2 |f_NL| sigma
FNL_MAX = 1.0 / (PERT_COEFF * ZETA_RMS)

# Table III: transfer coefficient per background, rho_B = 1 - 2T
BACKGROUNDS = {"quintin": 0.165, "lqc": 0.250, "poly": 0.196}


def fnl_pre(cs, L=0.0):
    return -245.0 / 16.0 + 105.0 / (8.0 * cs**2) - 30.0 * L


def fnl_pre_Xn(cs):
    """P ∝ X^n line, L = (1-cs^2)/(6 cs^2): Li+2016 Eq. (5.1)."""
    return -165.0 / 16.0 + 65.0 / (8.0 * cs**2)


def dfnl_bounce(cs, rho_b):
    return -(5.0 / 24.0) * rho_b * (6.0 * cs**2 - 5.0) / cs**4


def fnl_after(cs, T):
    return T * fnl_pre_Xn(cs) + dfnl_bounce(cs, 1.0 - 2.0 * T)


def main():
    out = {
        "criterion": {
            "form": "1.2 |f_NL| zeta_rms <= 1 (Sec. V B, applied at CMB scales)",
            "A_s": A_S,
            "zeta_rms": ZETA_RMS,
            "coefficient": PERT_COEFF,
            "fnl_max": FNL_MAX,
        },
        "backgrounds": {},
    }
    for name, T in BACKGROUNDS.items():
        # |f_NL^after| grows as 1/cs^4 toward small cs: find the cs where it
        # saturates the bound (bracket well below the sign-flip structure).
        f = lambda cs: abs(fnl_after(cs, T)) - FNL_MAX
        cs_pert = brentq(f, 1e-4, 0.3, xtol=1e-14, rtol=1e-12)
        out["backgrounds"][name] = {
            "T": T,
            "rho_B": 1.0 - 2.0 * T,
            "cs_perturbative_floor": cs_pert,
            "fnl_after_at_floor": fnl_after(cs_pert, T),
            "r_at_floor": 24.0 * cs_pert,
            "fnl_after_at_cs_1p5e-3": fnl_after(1.5e-3, T),
            "fnl_after_at_cs_0p624": fnl_after(0.624, T),
        }

    # DA3M-R9-19: the 95% Planck edge, not just the 68% one.
    # Planck 2018 local: f_NL = -0.9 +- 5.1 (68%) -> 68% [-6.0, +4.2],
    # 95% [-11.1, +9.3]. f_NL^after > 0 throughout this window, so the
    # upper edge binds.
    out["planck_edges"] = {"central": -0.9, "sigma": 5.1}
    for cl, nsig in (("68", 1.0), ("95", 2.0)):
        upper = -0.9 + nsig * 5.1
        edges = {}
        for name, T in BACKGROUNDS.items():
            g = lambda cs: fnl_after(cs, T) - upper
            cs_edge = brentq(g, 0.2, 0.999, xtol=1e-14, rtol=1e-12)
            edges[name] = {"cs_min": cs_edge, "r_min": 24.0 * cs_edge}
        out["planck_edges"][cl] = {"upper_fnl": upper, "per_background": edges}
        cmin = min(v["cs_min"] for v in edges.values())
        out["planck_edges"][cl]["cs_min_overall"] = cmin
        out["planck_edges"][cl]["r_min_overall"] = 24.0 * cmin
        out["planck_edges"][cl]["disjointness_factor_vs_tensor"] = cmin / 1.5e-3

    floors = [v["cs_perturbative_floor"] for v in out["backgrounds"].values()]
    out["summary"] = {
        "fnl_max": FNL_MAX,
        "cs_floor_min": min(floors),
        "cs_floor_max": max(floors),
        "r_at_floor_min": 24.0 * min(floors),
        "r_at_floor_max": 24.0 * max(floors),
        "cs_tensor_viable": 1.5e-3,
        "decades_past_control_at_tensor_viable": float(
            np.log10(
                abs(out["backgrounds"]["quintin"]["fnl_after_at_cs_1p5e-3"]) / FNL_MAX
            )
        ),
        "statement": (
            "Tree-level control is lost for c_s below ~the quoted floor; the "
            "tensor-viable c_s = 1.5e-3 sits many decades past it, so the "
            "10^11 figure is not a prediction of a controlled calculation. The "
            "no-go does not depend on it: r = 24 c_s alone excludes the window."
        ),
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out["summary"], indent=2))
    for k, v in out["backgrounds"].items():
        print(f"{k:8s} cs_floor={v['cs_perturbative_floor']:.4f} "
              f"r={v['r_at_floor']:.2f} |f|@floor={abs(v['fnl_after_at_floor']):.3e} "
              f"f@0.624={v['fnl_after_at_cs_0p624']:.3f}")


if __name__ == "__main__":
    main()
