#!/usr/bin/env python3
"""c9l — R25conf Grok P2-M1: continuous marginalization over the bounce-prior
width hyperparameter sigma_theory, vs the discrete {delta, 0.5, 1.0, 2.0} grid
of Sec. VI (and Table tab:bayes).

Conventions identical to committed c9g_bf_table_recompute.py / c9k:
  likelihood sigma = 0.7 (SPHEREx baseline), mock detection fhat = -35/8.
  Gaussian bounce prior N(-35/8, sigma_theory):
      Z_bounce(st) = N(fhat; -35/8, sqrt(0.7^2 + st^2))   [exact convolution]
  competitor: flat U[lo, hi], Z_comp = (Phi((hi-fhat)/s) - Phi((lo-fhat)/s))/(hi-lo)
  hyperprior: sigma_theory ~ U[0.5, 2.0] (uniform, spanning the reported grid).

Writes outputs/c9l_sigma_theory_continuous_marginalization.json
"""
import json
import math

SQRT2 = math.sqrt(2.0)
F0 = -35.0 / 8.0
S = 0.7


def phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def Phi(x):
    return 0.5 * (1 + math.erf(x / SQRT2))


def z_bounce(st, fhat=F0, s=S):
    seff = math.sqrt(s * s + st * st)
    return phi((fhat - F0) / seff) / seff


def z_comp(lo, hi, fhat=F0, s=S):
    return (Phi((hi - fhat) / s) - Phi((lo - fhat) / s)) / (hi - lo)


def marginal_bf(lo, hi, st_lo=0.5, st_hi=2.0, n=10001):
    h = (st_hi - st_lo) / (n - 1)
    vals = [z_bounce(st_lo + i * h) for i in range(n)]
    integral = h * (sum(vals) - 0.5 * (vals[0] + vals[-1]))
    zb = integral / (st_hi - st_lo)
    return zb / z_comp(lo, hi)


if __name__ == "__main__":
    out = {
        "script": "research/focused_paper_source_integration/c9l_sigma_theory_continuous_marginalization.py",
        "purpose": ("R25conf Grok P2-M1: continuous uniform-hyperprior marginalization over "
                    "sigma_theory in [0.5, 2.0] vs the discrete grid of Sec. VI / tab:bayes."),
        "conventions": "identical to committed c9g/c9k; fhat = -35/8, sigma = 0.7",
        "discrete_grid": {},
        "continuous_marginal": {},
    }
    for label, st in (("delta", 0.0), ("0.5", 0.5), ("1.0", 1.0), ("2.0", 2.0)):
        out["discrete_grid"][f"sigma_theory={label}"] = {
            "BF_broad_[-15,15]": round(z_bounce(st) / z_comp(-15, 15), 3),
            "BF_narrow_[-5,5]": round(z_bounce(st) / z_comp(-5, 5), 3),
        }
    conv = {}
    for n in (3, 11, 101, 1001, 10001):
        conv[str(n)] = {
            "BF_broad": round(marginal_bf(-15, 15, n=n), 4),
            "BF_narrow": round(marginal_bf(-5, 5, n=n), 4),
        }
    out["continuous_marginal"] = {
        "hyperprior": "sigma_theory ~ U[0.5, 2.0]",
        "BF_broad_[-15,15]": round(marginal_bf(-15, 15), 3),
        "BF_narrow_[-5,5]": round(marginal_bf(-5, 5), 3),
        "grid_convergence": conv,
        "note": ("Marginal BF (broad 8.84, narrow 3.62) lies between the discrete sigma_theory = 0.5 "
                 "and 2.0 endpoints (broad 13.91/5.65) and close to the recommended sigma_theory = 1.0 "
                 "values (broad 9.80, narrow 4.01); BF > 1 (bounce over tuned multifield) holds across "
                 "the entire hyperprior support, so the ranking is stable under continuous prior-width "
                 "variation. 3-point grid converged to < 0.03 in log-evidence vs the 10001-point grid."),
    }
    # log-evidence gap of the 3-point grid vs fine grid
    out["three_point_vs_fine_log_gap"] = {
        "delta_logBF_broad": round(abs(math.log(conv["3"]["BF_broad"]) - math.log(conv["10001"]["BF_broad"])), 4),
        "delta_logBF_narrow": round(abs(math.log(conv["3"]["BF_narrow"]) - math.log(conv["10001"]["BF_narrow"])), 4),
    }
    with open("outputs/c9l_sigma_theory_continuous_marginalization.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))
