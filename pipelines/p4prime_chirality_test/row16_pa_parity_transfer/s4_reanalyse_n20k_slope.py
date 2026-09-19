#!/usr/bin/env python3
"""Row 16(ii-b) statistic S4 — re-analysis of the committed N=20,000
row 16(ii) injection slope (no new inference).

Pre-registration: PREREGISTRATION_2026-09-19.md sec. 5 (S4), committed 12248d70
BEFORE this script was run.

Section 1 of the pre-registration proves that for the production Z2 flip-TTA the
pre-mirror injection is an exact CW<->CCW relabelling, so for the paper's hard
statistic A_cls = 2 N_CW/(N_CW+N_CCW) - 1 the injection curve obeys
E[A(f)] = A0 (1-2f) identically, i.e. dA/df = -2 A0 with no dependence on the
network. The committed analysis quoted a slope without the error bar of that
estimator. This script builds that error bar by Monte-Carlo over injection-seed
realisations of exactly the committed design, places the committed slope in it,
and reports the sample size at which the design would first reach 3-sigma power.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
PAIRS = HERE.parent / "injection_pilot" / "scale20k_pairs.parquet"
COMMITTED = HERE.parent / "injection_pilot" / "scale20k_injection_results.json"
FRACTIONS = [0.0, 0.005, 0.01, 0.02, 0.05]
N_SEEDS_COMMITTED = 10          # the committed design: 5 fractions x 10 seeds
N_REPLICAS = 2000               # pre-registered
OUT = HERE / "s4_n20k_slope_reanalysis.json"


def slopes_for_design(cls_normal, soft_cw, soft_ccw, n_replicas, rng, n_seeds):
    """Replicate the committed 5-fraction x n_seeds design n_replicas times and
    return the fitted slope of each replica, for both statistics."""
    n = len(cls_normal)
    cls_pre = np.where(cls_normal == 0, 1, np.where(cls_normal == 1, 0, 2))
    n_spi = int(((cls_normal == 0) | (cls_normal == 1)).sum())
    is_cw, is_ccw = cls_normal == 0, cls_normal == 1
    n_cw0 = int(is_cw.sum())
    A0_cls = 2.0 * n_cw0 / n_spi - 1.0
    A0_soft = float(2.0 * soft_cw.mean() - 1.0)

    xs = np.repeat(FRACTIONS, n_seeds).astype(float)
    xc = xs - xs.mean()
    denom = (xc ** 2).sum()

    out_cls = np.empty(n_replicas)
    out_soft = np.empty(n_replicas)
    for r in range(n_replicas):
        ys_cls = np.empty(len(xs))
        ys_soft = np.empty(len(xs))
        k = 0
        for f in FRACTIONS:
            n_flip = int(round(f * n))
            for _ in range(n_seeds):
                if n_flip == 0:
                    ys_cls[k] = A0_cls
                    ys_soft[k] = A0_soft
                else:
                    S = rng.choice(n, size=n_flip, replace=False)
                    # hard statistic: CW<->CCW swap on S, NS unchanged, so the
                    # spiral denominator is invariant
                    d = int(is_ccw[S].sum()) - int(is_cw[S].sum())
                    ys_cls[k] = 2.0 * (n_cw0 + d) / n_spi - 1.0
                    # soft statistic: mean over ALL galaxies of eq_cw
                    m = soft_cw.sum() - soft_cw[S].sum() + soft_ccw[S].sum()
                    ys_soft[k] = 2.0 * m / n - 1.0
                k += 1
        out_cls[r] = ((xc * (ys_cls - ys_cls.mean())).sum()) / denom
        out_soft[r] = ((xc * (ys_soft - ys_soft.mean())).sum()) / denom
    return out_cls, out_soft, A0_cls, A0_soft, n_spi


def main():
    df = pd.read_parquet(PAIRS)
    n = len(df)
    eq_cw = (df["p_cw_orig"].values + df["p_ccw_flip"].values) / 2.0
    eq_ccw = (df["p_ccw_orig"].values + df["p_cw_flip"].values) / 2.0
    eq_ns = (df["p_ns_orig"].values + df["p_ns_flip"].values) / 2.0
    cls = np.argmax(np.stack([eq_cw, eq_ccw, eq_ns], axis=1), axis=1)

    rng = np.random.default_rng(20260919)
    s_cls, s_soft, A0_cls, A0_soft, n_spi = slopes_for_design(
        cls, eq_cw, eq_ccw, N_REPLICAS, rng, N_SEEDS_COMMITTED)

    committed = json.loads(COMMITTED.read_text())
    c_cls = committed["slope_dA_df_pixel_level_TTA_spiral_classified"]
    c_soft = committed["slope_dA_df_pixel_level_TTA"]
    id_cls = -2.0 * A0_cls
    id_soft = committed["slope_dA_df_label_level_analytic"]   # mixture identity

    se_cls, se_soft = float(s_cls.std(ddof=1)), float(s_soft.std(ddof=1))
    z_cls = (c_cls - id_cls) / se_cls
    z_soft = (c_soft - id_soft) / se_soft

    # N at which 3*SE(slope) = |2 A0_cls|, i.e. the first N with 3-sigma power
    # for this design. The scaling of SE with N is MEASURED (not assumed) by
    # re-running the same MC on random sub-samples, then fitted in log-log.
    sizes = [2500, 5000, 10000, n]
    ses = []
    for m in sizes:
        if m == n:
            ses.append(se_cls)
            continue
        sub = rng.choice(n, size=m, replace=False)
        s_m, _, _, _, _ = slopes_for_design(
            cls[sub], eq_cw[sub], eq_ccw[sub], 800, rng, N_SEEDS_COMMITTED)
        ses.append(float(s_m.std(ddof=1)))
    p_fit, logc = np.polyfit(np.log(sizes), np.log(ses), 1)
    scaling_exponent = float(p_fit)
    # solve 3 * SE_20k * (N/n)^p = |identity slope|
    target = abs(id_cls) / (3.0 * se_cls)
    n_req = float(n * target ** (1.0 / scaling_exponent))
    n_req_sqrtn = float(n * (3.0 * se_cls / abs(id_cls)) ** 2)   # p = -1/2 reference

    res = {
        "preregistration": "PREREGISTRATION_2026-09-19.md sec.5 S4 (commit 12248d70)",
        "input_pairs": str(PAIRS.relative_to(HERE.parent.parent.parent)),
        "n_galaxies": int(n), "n_spiral_classified": int(n_spi),
        "A0_spiral_classified": float(A0_cls),
        "A0_soft_all_classes": float(A0_soft),
        "exact_identity_slope_spiral_classified": float(id_cls),
        "mixture_identity_slope_soft": float(id_soft),
        "committed_slope_spiral_classified": float(c_cls),
        "committed_slope_soft": float(c_soft),
        "mc_replicas": N_REPLICAS,
        "mc_mean_slope_spiral_classified": float(s_cls.mean()),
        "mc_se_slope_spiral_classified": se_cls,
        "mc_mean_slope_soft": float(s_soft.mean()),
        "mc_se_slope_soft": se_soft,
        "z_committed_vs_identity_spiral_classified": float(z_cls),
        "z_committed_vs_identity_soft": float(z_soft),
        "se_vs_N_sizes": sizes,
        "se_vs_N_values": ses,
        "se_scaling_exponent_measured": scaling_exponent,
        "n_required_for_3sigma_power_spiral_classified": n_req,
        "n_required_for_3sigma_power_sqrtN_reference": n_req_sqrtn,
        "naive_identity_used_in_committed_headline": -2.0 * A0_soft,
        "verdict": (
            "CONSISTENT WITH NOISE FLOOR" if max(abs(z_cls), abs(z_soft)) < 3
            else "DEVIATION ABOVE 3 SIGMA"),
    }
    OUT.write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
