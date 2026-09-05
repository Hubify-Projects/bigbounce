#!/usr/bin/env python3
"""Row 13 Part A at scale: analyze the N~5000 production-equivariant
(Z2 flip-TTA) forward-pass pairs to build the pixel-level injected-f vs
recovered-A curve, with 5 random seeds per fraction (noise floor) and
bootstrap errors, and compare the slope dA/df against the exact
label-level analytic identity.

Uses the exact swap identity proven in run_injection_scale.py's docstring:
    eq_cw(flip(img)) = eq_ccw(img)
so injecting a mirror-flip on a subset S of galaxies (simulating a
"real" parity effect hitting the images before the production pipeline
ever sees them) is applied by swapping eq_cw<->eq_ccw for i in S, with
NO new inference needed — the f/seed grid is evaluated in closed form
over the one-time N-galaxy forward-pass pairs.

Label-level comparison: flipping fraction f of BINARY CW/CCW labels
(the idealized/label-level operation, as opposed to flipping raw pixels
through the real classifier) changes the mean CW-fraction analytically:
    A_label(f) = (1-f)*A0 + f*(-A0) = A0*(1 - 2f)   [exact, no noise]
This is the closed-form "label-level" curve Row 13 compares against —
distinct from (and not the same axis as) the paper's committed
full_catalog_injection_recovery.py / gen_fig_injection_recovery.py
detection-probability-vs-amplitude curve, which measures MASTER ell=1
sky-map recovery, not global-asymmetry-vs-flip-fraction. That
distinction is disclosed explicitly in the ledger row writeup.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
FRACTIONS = [0.0, 0.005, 0.01, 0.02, 0.05]
SEEDS = [1, 2, 3, 4, 5]
N_BOOTSTRAP = 500


def main():
    df = pd.read_parquet(HERE / "scale_pairs.parquet")
    n = len(df)
    p_cw_o = df["p_cw_orig"].values
    p_ccw_o = df["p_ccw_orig"].values
    p_ns_o = df["p_ns_orig"].values
    p_cw_f = df["p_cw_flip"].values
    p_ccw_f = df["p_ccw_flip"].values
    p_ns_f = df["p_ns_flip"].values

    # Production Z2-TTA equivariant probabilities (matches
    # equivariant_postprocess.py exactly): eq_cw = (p_cw_orig + p_ccw_flip)/2
    eq_cw_normal = (p_cw_o + p_ccw_f) / 2.0
    eq_ccw_normal = (p_ccw_o + p_cw_f) / 2.0
    eq_ns_normal = (p_ns_o + p_ns_f) / 2.0
    # Exact swap for a pre-flipped image (proven identity, no re-inference)
    eq_cw_preflipped = eq_ccw_normal
    eq_ccw_preflipped = eq_cw_normal

    A0_full = float(2.0 * eq_cw_normal.mean() - 1.0)
    M_cw = float(eq_cw_normal.mean())
    M_ccw = float(eq_ccw_normal.mean())
    M_ns = float(eq_ns_normal.mean())
    A0_ccw = float(2.0 * M_ccw - 1.0)

    # Hard-argmax classification (the paper's actual asymmetry statistic:
    # A = 2*f_CW - 1 among CLASSIFIED SPIRALS only, not mean(p_cw) over all
    # images -- fixes the mean(p_cw)-over-all-classes normalization mismatch
    # that made the N=500 pilot's raw-pass baseline (-0.396) not comparable
    # to the paper's f_CW-restricted-to-spirals statistic).
    class_normal = np.argmax(np.stack([eq_cw_normal, eq_ccw_normal, eq_ns_normal], axis=1), axis=1)
    # 0=CW, 1=CCW, 2=NS. Under a pre-flip, eq_ns is unchanged and eq_cw/eq_ccw
    # swap, so a CW-classified galaxy becomes CCW-classified and vice versa;
    # an NS-classified galaxy stays NS (proven identity, no re-inference).
    class_preflipped = np.where(class_normal == 0, 1, np.where(class_normal == 1, 0, 2))

    rows = []
    for f in FRACTIONS:
        n_flip = int(round(f * n))
        seed_As, seed_As_cls = [], []
        for seed in SEEDS:
            rng = np.random.default_rng(1000 * seed + n_flip)
            flip_idx = rng.choice(n, size=n_flip, replace=False) if n_flip > 0 else np.array([], dtype=int)
            eq_cw_realized = eq_cw_normal.copy()
            eq_cw_realized[flip_idx] = eq_cw_preflipped[flip_idx]
            A = float(2.0 * eq_cw_realized.mean() - 1.0)
            seed_As.append(A)

            class_realized = class_normal.copy()
            class_realized[flip_idx] = class_preflipped[flip_idx]
            n_cw_cls = int((class_realized == 0).sum())
            n_ccw_cls = int((class_realized == 1).sum())
            n_spi = n_cw_cls + n_ccw_cls
            A_cls = float(2.0 * n_cw_cls / n_spi - 1.0) if n_spi > 0 else float("nan")
            seed_As_cls.append(A_cls)

            # bootstrap error on THIS realization (resample galaxies with replacement)
            boot = np.empty(N_BOOTSTRAP)
            boot_cls = np.empty(N_BOOTSTRAP)
            brng = np.random.default_rng(2000 * seed + n_flip)
            for b in range(N_BOOTSTRAP):
                samp = brng.integers(0, n, size=n)
                boot[b] = 2.0 * eq_cw_realized[samp].mean() - 1.0
                cr = class_realized[samp]
                nb_cw, nb_ccw = (cr == 0).sum(), (cr == 1).sum()
                boot_cls[b] = 2.0 * nb_cw / (nb_cw + nb_ccw) - 1.0 if (nb_cw + nb_ccw) > 0 else np.nan
            boot_se = float(boot.std())
            boot_se_cls = float(np.nanstd(boot_cls))

            rows.append({
                "f_injected": f, "seed": seed, "n_flipped": n_flip,
                "A_recovered": A, "bootstrap_se": boot_se,
                "A_recovered_spiral_classified": A_cls, "n_spiral_classified": n_spi,
                "bootstrap_se_spiral_classified": boot_se_cls,
            })

        mean_A = float(np.mean(seed_As))
        std_A = float(np.std(seed_As, ddof=1)) if len(seed_As) > 1 else 0.0
        mean_A_cls = float(np.mean(seed_As_cls))
        std_A_cls = float(np.std(seed_As_cls, ddof=1)) if len(seed_As) > 1 else 0.0
        print(f"f={f:.3f}  n_flip={n_flip:5d}  A_mean(5 seeds)={mean_A:+.6f} (noise={std_A:.6f})  "
              f"A_cls_mean={mean_A_cls:+.6f} (noise={std_A_cls:.6f})")

    per_seed = pd.DataFrame(rows)

    # Slope dA/df via linear regression on per-seed points (pixel-level, TTA)
    slope_pix, intercept_pix = np.polyfit(per_seed["f_injected"], per_seed["A_recovered"], 1)
    slope_pix_cls, intercept_pix_cls = np.polyfit(per_seed["f_injected"], per_seed["A_recovered_spiral_classified"], 1)

    n_cw_cls0 = int((class_normal == 0).sum())
    n_ccw_cls0 = int((class_normal == 1).sum())
    A0_cls = float(2.0 * n_cw_cls0 / (n_cw_cls0 + n_ccw_cls0) - 1.0)
    # For the hard-count statistic (denominator = fixed CW+CCW count, NS
    # excluded from both numerator and denominator), swapping a random
    # fraction f of CW<->CCW labels gives the EXACT identity A(f)=A0*(1-2f)
    # (no NS-mass correction needed here, unlike the soft-probability mean
    # statistic above, since NS drops out of both terms of the ratio).
    slope_label_cls = -2.0 * A0_cls
    label_curve_cls = [{"f_injected": f, "A_label_cls": A0_cls * (1 - 2 * f)} for f in FRACTIONS]

    # Label-level analytic curve, exact expectation for swapping a RANDOM
    # fraction f of galaxies' eq_cw<->eq_ccw values (accounts for the
    # NOT_SPIRAL mass M_ns, which a naive A0*(1-2f) identity omits):
    #   E[A(f)] = (1-f)*A0 + f*A0_ccw   where A0_ccw = 2*M_ccw - 1
    label_curve = [{"f_injected": f, "A_label": (1 - f) * A0_full + f * A0_ccw} for f in FRACTIONS]
    slope_label = A0_ccw - A0_full  # exact dA/df for the mixture identity above

    summary = {
        "n_total": int(n),
        "pipeline": "production equivariant Z2 (2-fold horizontal-flip) TTA, matching "
                    "pipelines/p2_chirality/equivariant_postprocess.py exactly "
                    "(NOT raw single-pass, NOT full D4 8-way)",
        "model": "bamfai/galaxy-chirality-v2 chirality_model_v2_best.pt "
                 "rev 237d021c451d75cf86a875e86d4de498b74e2f12",
        "A0_baseline_pixel_level": A0_full,
        "M_cw_mean_eq": M_cw, "M_ccw_mean_eq": M_ccw, "M_ns_mean_eq": M_ns, "A0_ccw": A0_ccw,
        "paper_residual_bias_postprocess": -0.0026,
        "fractions": FRACTIONS,
        "seeds": SEEDS,
        "per_seed_results": rows,
        "per_fraction_mean_A": [
            {"f_injected": f,
             "A_mean": float(per_seed.loc[per_seed.f_injected == f, "A_recovered"].mean()),
             "A_std_across_seeds": float(per_seed.loc[per_seed.f_injected == f, "A_recovered"].std(ddof=1)) if len(SEEDS) > 1 else 0.0,
             "A_spiral_classified_mean": float(per_seed.loc[per_seed.f_injected == f, "A_recovered_spiral_classified"].mean()),
             "A_spiral_classified_std_across_seeds": float(per_seed.loc[per_seed.f_injected == f, "A_recovered_spiral_classified"].std(ddof=1)) if len(SEEDS) > 1 else 0.0}
            for f in FRACTIONS
        ],
        "slope_dA_df_pixel_level_TTA": float(slope_pix),
        "intercept_pixel_level_TTA": float(intercept_pix),
        "label_level_analytic_curve": label_curve,
        "slope_dA_df_label_level_analytic": float(slope_label),
        "slope_ratio_pixel_over_label": float(slope_pix / slope_label) if slope_label != 0 else None,
        "A0_spiral_classified": A0_cls,
        "slope_dA_df_pixel_level_TTA_spiral_classified": float(slope_pix_cls),
        "label_level_analytic_curve_spiral_classified": label_curve_cls,
        "slope_dA_df_label_level_analytic_spiral_classified": float(slope_label_cls),
        "slope_ratio_pixel_over_label_spiral_classified": float(slope_pix_cls / slope_label_cls) if slope_label_cls != 0 else None,
        "note_on_comparison_scope": (
            "The 'label-level curve' here is the exact closed-form mixture "
            "identity E[A(f)]=(1-f)*A0+f*A0_ccw for swapping eq_cw<->eq_ccw on "
            "a random fraction f of galaxies (A0_ccw=2*mean(eq_ccw)-1; this "
            "properly accounts for the NOT_SPIRAL probability mass, which a "
            "naive A(f)=A0*(1-2f) identity omits) -- NOT the paper's committed "
            "full_catalog_injection_recovery.py / "
            "gen_fig_injection_recovery.py detection-probability-vs-amplitude "
            "curve, which measures MASTER ell=1 sky-map dipole recovery under a "
            "physically-motivated cos(theta) dipole injection, a different "
            "statistic on a different axis (amplitude A, not flip-fraction f). "
            "Both are disclosed; conflating them would misstate the comparison."
        ),
    }
    (HERE / "scale_injection_results.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps({k: v for k, v in summary.items() if k not in ("per_seed_results",)}, indent=2))


if __name__ == "__main__":
    main()
