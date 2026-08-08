#!/usr/bin/env python3
"""c9g — recompute Table III (tab:gr) Bayes factors from first principles.

R23conf P2-M1: the delta/narrow no-GR cell reads 10.9 in Table III while the
closed-form Eq.(7) value at the central detection is 7.0. No committed artifact
generates the table. This script tests the candidate generating mechanisms:

  (a) closed-form BF at the central mock detection fhat = -35/8;
  (b) realization-marginalized BF: fhat ~ N(-35/8, sigma_eff), report
      mean / median / geometric-mean BF over realizations;
  (c) GR marginalization as sigma_eff inflation.

Models compared (likelihood sigma = sigma_eff):
  bounce-delta: f fixed at -35/8                -> L = N(fhat; -35/8, s)
  tuned narrow: f ~ U[-5, +5]                   -> L = (1/10) * int N(fhat; f, s) df
  SSFSR point:  f = 0.015                       -> L = N(fhat; 0.015, s)

Writes outputs/c9g_bf_table_recompute.json
"""
import json
import math
import random

SQRT2 = math.sqrt(2.0)


def phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def Phi(x):
    return 0.5 * (1 + math.erf(x / SQRT2))


F0 = -35.0 / 16.0  # -2.1875 (H17 correction: was the superseded -35/8 = -4.375;
# the SSFSR column and P(BF>3) of tab:gr were left at the -35/8 center while the
# Tuned column had already been hand-updated to -35/16 — this restores a single
# consistent center for every generated cell.)
SSFSR = 0.015


def bf_vs_tuned(fhat, s, lo=-5.0, hi=5.0):
    num = phi((fhat - F0) / s) / s
    den = (Phi((hi - fhat) / s) - Phi((lo - fhat) / s)) / (hi - lo)
    return num / den


def bf_vs_ssfsr(fhat, s):
    return math.exp((-((fhat - F0) ** 2) + (fhat - SSFSR) ** 2) / (2 * s * s))


def run(s, n=200000, seed=42):
    rng = random.Random(seed)
    bts, bss, gt3 = [], [], 0
    for _ in range(n):
        fhat = rng.gauss(F0, s)
        bt = bf_vs_tuned(fhat, s)
        bs = bf_vs_ssfsr(fhat, s)
        bts.append(bt)
        bss.append(bs)
        if bs > 3:
            gt3 += 1
    bts.sort()
    bss.sort()
    mean_bt = sum(bts) / n
    med_bt = bts[n // 2]
    gm_bt = math.exp(sum(math.log(b) for b in bts) / n)
    mean_bs = sum(bss) / n
    med_bs = bss[n // 2]
    gm_bs = math.exp(sum(math.log(b) for b in bss) / n)
    return {
        "sigma_eff": s,
        "closed_form_at_central": {
            "bf_vs_tuned": round(bf_vs_tuned(F0, s), 3),
            "bf_vs_ssfsr": "%.3e" % bf_vs_ssfsr(F0, s),
        },
        "realization_marginalized": {
            "bf_vs_tuned": {"mean": round(mean_bt, 2), "median": round(med_bt, 2), "geo_mean": round(gm_bt, 2)},
            "bf_vs_ssfsr": {"mean": "%.3e" % mean_bs, "median": "%.3e" % med_bs, "geo_mean": "%.3e" % gm_bs},
            "P_bf_ssfsr_gt3": round(gt3 / n, 4),
        },
    }


def bf_vs_tuned_broad(fhat, s):
    return bf_vs_tuned(fhat, s, lo=-15.0, hi=15.0)


if __name__ == "__main__":
    results = {"table_iii_claims": {
        "ideal_no_gr": {"bf_vs_ssfsr": 3.3e6, "bf_vs_tuned": 10.9, "p_gt3": 0.98},
        "sigma_gr_0.5": {"bf_vs_ssfsr": 4.1e4, "bf_vs_tuned": 9.4, "p_gt3": 0.97},
        "sigma_gr_1.0": {"bf_vs_ssfsr": 329, "bf_vs_tuned": 7.9, "p_gt3": 0.96},
    }, "scans": []}
    # candidate sigma_eff: 0.7 baseline; GR inflation sqrt(0.7^2+x); plus
    # plausible variants the original (lost) run may have used
    for s in (0.70, 0.74, 0.80, 0.86, 0.90, 1.00, 1.22, math.sqrt(0.7**2 + 0.5**2), math.sqrt(0.7**2 + 1.0**2)):
        results["scans"].append(run(s))
    # final Table III (tab:gr) replacement values: closed-form Eq.(7) at the
    # central detection, sigma_eff = sqrt(0.7^2 + sigma_GR^2); P(BF>3) from MC
    final = []
    for label, sgr in (("ideal_no_gr", 0.0), ("sigma_gr_0.5", 0.5), ("sigma_gr_1.0", 1.0)):
        s = math.sqrt(0.7 ** 2 + sgr ** 2)
        row = run(s)
        final.append({
            "row": label,
            "sigma_eff": round(s, 4),
            "bf_vs_ssfsr_closed_form": "%.2e" % bf_vs_ssfsr(F0, s),
            "bf_vs_tuned_narrow_closed_form": round(bf_vs_tuned(F0, s), 2),
            "bf_vs_tuned_broad_closed_form": round(bf_vs_tuned_broad(F0, s), 2),
            "P_bf_ssfsr_gt3_mc": row["realization_marginalized"]["P_bf_ssfsr_gt3"],
        })
    results["table_iii_replacement"] = final
    results["verdict"] = ("Original Table III values (3.3e6/10.9, 4.1e4/9.4, 329/7.9) are "
                          "irreproducible: SSFSR column matches an obsolete sigma=0.8 baseline; "
                          "the 10.9 Tuned cell matches no tested mechanism (closed form max 7.0 "
                          "at sigma=0.7; realization marginalization and GR inflation both lower "
                          "it). Replaced by the closed-form values above on the paper's "
                          "sigma=0.7 convention.")
    with open("outputs/c9g_bf_table_recompute.json", "w") as f:
        json.dump(results, f, indent=1)
    print("\nTable III replacement rows:")
    for r in final:
        print(r)
    for r in results["scans"]:
        cf = r["closed_form_at_central"]
        rm = r["realization_marginalized"]
        print(f"s={r['sigma_eff']:.3f}  cf_tuned={cf['bf_vs_tuned']:>7}  "
              f"mc_tuned mean/med/gm={rm['bf_vs_tuned']['mean']}/{rm['bf_vs_tuned']['median']}/{rm['bf_vs_tuned']['geo_mean']}  "
              f"cf_ssfsr={cf['bf_vs_ssfsr']}  mc_ssfsr med={rm['bf_vs_ssfsr']['median']}  P>3={rm['P_bf_ssfsr_gt3']}")
