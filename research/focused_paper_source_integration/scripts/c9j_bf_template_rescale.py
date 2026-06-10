#!/usr/bin/env python3
"""c9j — R23conf META-E2 closure: template-mismatch rescaling of the four-corner
Bayes-factor grid.

The Bayes-factor section evaluates the closed-form Eq. (bf) grid at the survey
local-template sigma = 0.7 with the mock detection placed at the bounce
prediction f0 = -35/8 (the r -> 1, no-template-mismatch bookkeeping endpoint).
META-E2 asks what happens under the Eq. (5) bookkeeping in bounce-amplitude
space, sigma_eff = sigma(local)/r with the noise-weighted r = 0.84
(sigma_eff ~= 0.833), and under the alternative fully-measured-space
bookkeeping (prediction and detection at r*f0 = -3.675, sigma = 0.7).

Same closed-form formulas as c9g_bf_table_recompute.py (validated: reproduces
the printed 17.10 / 7.00 / 9.80 / 4.01 at sigma = 0.7 exactly).

Writes outputs/c9j_bf_template_rescale.json
"""
import json
import math

SQRT2 = math.sqrt(2.0)
F0 = -35.0 / 8.0
R_NOISE = 0.84


def phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def Phi(x):
    return 0.5 * (1 + math.erf(x / SQRT2))


def bf_delta_vs_uniform(fhat, pred, s, lo, hi):
    num = phi((fhat - pred) / s) / s
    den = (Phi((hi - fhat) / s) - Phi((lo - fhat) / s)) / (hi - lo)
    return num / den


def bf_gauss_vs_uniform(fhat, pred, s, sth, lo, hi):
    seff = math.sqrt(s * s + sth * sth)
    num = phi((fhat - pred) / seff) / seff
    den = (Phi((hi - fhat) / s) - Phi((lo - fhat) / s)) / (hi - lo)
    return num / den


def four_corner(fhat, pred, s, sth=1.0):
    return {
        "delta_narrow_[-5,5]": round(bf_delta_vs_uniform(fhat, pred, s, -5, 5), 2),
        "delta_broad_[-15,15]": round(bf_delta_vs_uniform(fhat, pred, s, -15, 15), 2),
        "gauss_sth1.0_narrow_[-5,5]": round(bf_gauss_vs_uniform(fhat, pred, s, sth, -5, 5), 2),
        "gauss_sth1.0_broad_[-15,15]": round(bf_gauss_vs_uniform(fhat, pred, s, sth, -15, 15), 2),
    }


if __name__ == "__main__":
    s_local = 0.7
    s_bounce = s_local / R_NOISE  # Eq.(5) rescaling, ~0.833
    results = {
        "paper_bookkeeping_r_to_1": {
            "description": "detection and prediction at f0=-35/8, sigma=0.7 "
                           "(the no-template-mismatch endpoint quoted in the tables)",
            "grid": four_corner(F0, F0, s_local),
        },
        "bounce_amplitude_bookkeeping": {
            "description": "META-E2 requested rescaling: sigma_eff = 0.7/r = %.4f "
                           "at r = 0.84, detection and prediction at -35/8" % s_bounce,
            "grid": four_corner(F0, F0, s_bounce),
        },
        "measured_space_bookkeeping": {
            "description": "fully measured-space alternative: prediction and "
                           "detection at r*f0 = %.4f, sigma = 0.7; competitor "
                           "priors unrescaled (multifield is local-shaped, r=1)" % (R_NOISE * F0),
            "grid": four_corner(R_NOISE * F0, R_NOISE * F0, s_local),
        },
    }
    with open("outputs/c9j_bf_template_rescale.json", "w") as f:
        json.dump(results, f, indent=1)
    for k, v in results.items():
        print(k, v["grid"])
