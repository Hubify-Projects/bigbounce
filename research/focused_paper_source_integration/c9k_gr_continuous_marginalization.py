#!/usr/bin/env python3
"""c9k — continuous GR marginalization check for Table III (tab:gr).

R24conf Grok P2-M2: the GR-contamination scenarios in Table III are evaluated
only at the discrete grid sigma_GR in {0, 0.5, 1.0}; the reviewer asks for a
proper marginal-likelihood integral over sigma_GR in [0, 1] (uniform prior) or
a demonstration that the discrete sampling is converged to < 0.1 in
log-evidence.

This script does both, reusing the exact model conventions of the committed
c9g_bf_table_recompute.py:

  likelihood width: sigma_eff(sigma_GR) = sqrt(0.7^2 + sigma_GR^2)
  bounce-delta:  L_b = N(fhat; -35/8, sigma_eff)
  SSFSR point:   L_s = N(fhat;  0.015, sigma_eff)
  tuned narrow:  L_t = (1/10) * int_{-5}^{+5} N(fhat; f, sigma_eff) df

Marginal evidence per model under uniform prior sigma_GR ~ U[0,1]:
  Z_m = int_0^1 L_m(fhat | sigma_eff(sigma_GR)) d sigma_GR
evaluated at the central mock detection fhat = -35/8 (same evaluation point
as the Table III closed-form cells).

Outputs:
  outputs/c9k_gr_continuous_marginalization.json
"""
import json
import math

SQRT2 = math.sqrt(2.0)
F0 = -35.0 / 16.0  # -2.1875 (H17 correction: was the superseded -35/8 center;
# realigned to the corrected -35/16 center used by c9g and the tab:gr cells)
SSFSR = 0.015
FHAT = F0  # central mock detection, same as Table III closed-form cells


def phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def Phi(x):
    return 0.5 * (1 + math.erf(x / SQRT2))


def sigma_eff(sigma_gr):
    return math.sqrt(0.7 ** 2 + sigma_gr ** 2)


def L_bounce(fhat, s):
    return phi((fhat - F0) / s) / s


def L_ssfsr(fhat, s):
    return phi((fhat - SSFSR) / s) / s


def L_tuned(fhat, s, lo=-5.0, hi=5.0):
    return (Phi((hi - fhat) / s) - Phi((lo - fhat) / s)) / (hi - lo)


def marginal_evidence(L, n_grid):
    """Trapezoid integral of L(fhat | sigma_eff(sigma_gr)) over sigma_gr in [0,1]."""
    total = 0.0
    h = 1.0 / (n_grid - 1)
    for i in range(n_grid):
        sg = i * h
        w = 0.5 if i in (0, n_grid - 1) else 1.0
        total += w * L(FHAT, sigma_eff(sg))
    return total * h


def main():
    # --- continuous marginalization (fine grid, convergence-checked) ---
    grids = [3, 11, 101, 1001, 10001]
    rows = {}
    for n in grids:
        zb = marginal_evidence(L_bounce, n)
        zs = marginal_evidence(L_ssfsr, n)
        zt = marginal_evidence(L_tuned, n)
        rows[n] = {
            "BF_vs_SSFSR": zb / zs,
            "BF_vs_tuned_narrow": zb / zt,
            "log10_BF_vs_SSFSR": math.log10(zb / zs),
        }
    fine = rows[10001]
    coarse3 = rows[3]  # the paper's 3-point grid {0, 0.5, 1.0} as a trapezoid
    dlog_ssfsr = abs(math.log(coarse3["BF_vs_SSFSR"]) - math.log(fine["BF_vs_SSFSR"]))
    dlog_tuned = abs(math.log(coarse3["BF_vs_tuned_narrow"]) - math.log(fine["BF_vs_tuned_narrow"]))

    # --- discrete Table III cells for reference ---
    discrete = {}
    for sg in (0.0, 0.5, 1.0):
        s = sigma_eff(sg)
        discrete["sigma_GR=%.1f" % sg] = {
            "sigma_eff": round(s, 4),
            "BF_vs_SSFSR": "%.3e" % (L_bounce(FHAT, s) / L_ssfsr(FHAT, s)),
            "BF_vs_tuned_narrow": round(L_bounce(FHAT, s) / L_tuned(FHAT, s), 3),
        }

    out = {
        "script": "research/focused_paper_source_integration/c9k_gr_continuous_marginalization.py",
        "purpose": "R24conf Grok P2-M2: continuous sigma_GR in [0,1] uniform-prior marginal-likelihood "
                   "Bayes factors vs the discrete {0, 0.5, 1.0} grid of Table III (tab:gr).",
        "conventions": "identical to committed c9g_bf_table_recompute.py; evaluated at central "
                       "mock detection fhat = -35/8",
        "discrete_grid_cells": discrete,
        "continuous_marginal": {
            "BF_vs_SSFSR": "%.3e" % fine["BF_vs_SSFSR"],
            "BF_vs_tuned_narrow": round(fine["BF_vs_tuned_narrow"], 3),
            "grid_convergence": {str(n): {
                "BF_vs_SSFSR": "%.4e" % rows[n]["BF_vs_SSFSR"],
                "BF_vs_tuned_narrow": round(rows[n]["BF_vs_tuned_narrow"], 4)} for n in grids},
        },
        "three_point_vs_fine_log_evidence_gap": {
            "delta_logBF_vs_SSFSR": round(dlog_ssfsr, 4),
            "delta_logBF_vs_tuned": round(dlog_tuned, 4),
            "note": "gap between the paper's 3-point trapezoid and the 10001-point fine grid; "
                    "< 0.1 in log-evidence satisfies the Grok P2-M2 convergence criterion "
                    "(applies to the smooth BF_vs_tuned column; the SSFSR column is "
                    "exponentially sigma-sensitive and is reported via the continuous value directly)",
        },
    }
    with open("outputs/c9k_gr_continuous_marginalization.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
