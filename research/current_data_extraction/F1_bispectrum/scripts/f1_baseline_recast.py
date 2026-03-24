#!/usr/bin/env python3
"""
F1.1 — Baseline Local f_NL Reproduction (TRIAGE_RECAST level)

Reproduces the Planck 2018 local f_NL constraint and recasts it onto
the matter-bounce template using the verified shape overlap factor.

This is Path A (Fisher recast), not Path B (map-level estimator).
Level: TRIAGE_RECAST until validated by injection/recovery.

References:
  Planck 2018 results IX (arXiv:1905.05697):
    f_NL^local = -0.9 ± 5.1 (T+E, KSW estimator)
    f_NL^local = -0.9 ± 5.0 (T+E, binned estimator)
    f_NL^local = -1.0 ± 5.1 (T+E, modal estimator)

  Template overlap: r = 0.84 ± 0.02 (Phase 1 robustness audit)
  Canonical target: f_NL = -35/8 = -4.375

WHAT THIS SCRIPT DOES:
  1. Documents the published Planck constraint
  2. Applies the template-overlap correction
  3. Computes the bounce-template constraint
  4. Computes consistency with the canonical prediction
  5. Outputs reproducible JSON + summary table

WHAT THIS SCRIPT DOES NOT DO:
  - Does not process any map-level data
  - Does not run a bispectrum estimator
  - Does not claim to improve on Planck
  - Does not claim map-level validation
"""

import json
import numpy as np
from pathlib import Path

OUTDIR = Path(__file__).parent.parent / "outputs"
OUTDIR.mkdir(exist_ok=True)

# ═══════════════════════════════════════════════════════
# PUBLISHED CONSTRAINTS (Planck 2018 IX, Table 4)
# ═══════════════════════════════════════════════════════

PLANCK_LOCAL = {
    "source": "Planck 2018 IX (arXiv:1905.05697), Table 4",
    "estimator": "KSW",
    "data": "T+E",
    "f_NL": -0.9,
    "sigma": 5.1,
    "convention": "Planck (zeta = zeta_G + 3/5 f_NL zeta_G^2)",
}

# Additional published constraints for cross-check
PLANCK_VARIANTS = [
    {"estimator": "Binned", "data": "T+E", "f_NL": -0.9, "sigma": 5.0},
    {"estimator": "Modal", "data": "T+E", "f_NL": -1.0, "sigma": 5.1},
    {"estimator": "KSW", "data": "T-only", "f_NL": -0.6, "sigma": 5.7},
]

# DESI DR1 (Mueller et al. 2024, approximate)
DESI_SDB = {
    "source": "DESI DR1 (approximate, from published forecasts and early results)",
    "method": "Scale-dependent bias",
    "f_NL": -3.6,
    "sigma": 9.2,
    "tracer": "QSO",
    "note": "APPROXIMATE — exact published value may differ",
}

DESI_PB = {
    "source": "DESI DR1 power+bispectrum (approximate)",
    "method": "P+B combined",
    "f_NL": -0.1,
    "sigma": 7.4,
    "note": "APPROXIMATE",
}

# ═══════════════════════════════════════════════════════
# TEMPLATE OVERLAP (from Phase 1 robustness audit)
# ═══════════════════════════════════════════════════════

OVERLAP = {
    "r_cmb_fisher": 0.876,
    "r_lss_sdb": 0.829,
    "r_generic": 0.84,
    "r_uncertainty": 0.02,
    "source": "Phase 1 robustness audit, 10 weighting schemes",
    "polynomial_systematic": 0.01,
}

# Canonical prediction
CANONICAL = {
    "f_NL": -35/8,  # = -4.375
    "alternative": -35/16,  # = -2.1875
    "confidence_canonical": 0.92,
}

# ═══════════════════════════════════════════════════════
# RECAST COMPUTATION
# ═══════════════════════════════════════════════════════

def recast_constraint(f_NL_local, sigma_local, r, r_err=0.0):
    """
    Recast a local-template constraint onto the bounce template.

    A local estimator measures:
        f_NL^measured = r × f_NL^bounce

    So:
        f_NL^bounce = f_NL^measured / r
        sigma^bounce = sigma^local / r

    Propagating r uncertainty:
        sigma^bounce = sigma^local / r × sqrt(1 + (r_err/r)^2 × (f_NL/sigma)^2)
        ≈ sigma^local / r  (since r_err/r << 1 and f_NL/sigma < 1)
    """
    f_NL_bounce = f_NL_local / r
    sigma_bounce = sigma_local / r

    # Propagate r uncertainty (small correction)
    if r_err > 0 and abs(f_NL_local) > 0:
        sigma_bounce = sigma_local / r * np.sqrt(1 + (r_err/r)**2 * (f_NL_local/sigma_local)**2)

    return f_NL_bounce, sigma_bounce


def compute_tension(f_NL, sigma, prediction):
    """Compute tension between measurement and prediction in sigma."""
    return abs(f_NL - prediction) / sigma


# ═══════════════════════════════════════════════════════
# MAIN COMPUTATION
# ═══════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("F1.1 — BASELINE PLANCK f_NL REPRODUCTION + BOUNCE RECAST")
    print("Level: TRIAGE_RECAST")
    print("=" * 70)

    # Step 1: Reproduce the published constraint
    print(f"\n  STEP 1: Published Planck 2018 constraint")
    print(f"    f_NL^local = {PLANCK_LOCAL['f_NL']} ± {PLANCK_LOCAL['sigma']}")
    print(f"    Estimator: {PLANCK_LOCAL['estimator']}, Data: {PLANCK_LOCAL['data']}")
    print(f"    Source: {PLANCK_LOCAL['source']}")

    print(f"\n    Cross-check with other estimators:")
    for v in PLANCK_VARIANTS:
        print(f"      {v['estimator']:>8s} ({v['data']:>6s}): {v['f_NL']:+.1f} ± {v['sigma']:.1f}")

    # Step 2: Apply template overlap
    r_cmb = OVERLAP["r_cmb_fisher"]
    r_err = OVERLAP["r_uncertainty"]
    print(f"\n  STEP 2: Template overlap correction")
    print(f"    r (CMB Fisher) = {r_cmb} ± {r_err}")
    print(f"    Source: {OVERLAP['source']}")

    f_bounce, sigma_bounce = recast_constraint(
        PLANCK_LOCAL["f_NL"], PLANCK_LOCAL["sigma"], r_cmb, r_err
    )

    print(f"\n    Recast result:")
    print(f"      f_NL^bounce = {PLANCK_LOCAL['f_NL']}/{r_cmb} = {f_bounce:+.2f}")
    print(f"      σ^bounce = {PLANCK_LOCAL['sigma']}/{r_cmb} = {sigma_bounce:.2f}")

    # Step 3: Consistency with prediction
    f_pred = CANONICAL["f_NL"]
    tension_pred = compute_tension(f_bounce, sigma_bounce, f_pred)
    tension_zero = compute_tension(f_bounce, sigma_bounce, 0)

    print(f"\n  STEP 3: Consistency assessment")
    print(f"    Canonical prediction: {f_pred}")
    print(f"    Tension with prediction: {tension_pred:.2f}σ")
    print(f"    Tension with zero: {tension_zero:.2f}σ")

    # Step 4: DESI combination
    print(f"\n  STEP 4: DESI combination (approximate)")
    r_lss = OVERLAP["r_lss_sdb"]

    constraints = [
        ("Planck 2018 T+E", PLANCK_LOCAL["f_NL"], PLANCK_LOCAL["sigma"], r_cmb),
        ("DESI DR1 QSO SDB", DESI_SDB["f_NL"], DESI_SDB["sigma"], r_lss),
        ("DESI DR1 P+B", DESI_PB["f_NL"], DESI_PB["sigma"], r_lss),
    ]

    print(f"\n    {'Constraint':<25s} {'f^local':>8s} {'σ^local':>8s} {'r':>6s} "
          f"{'f^bounce':>10s} {'σ^bounce':>9s}")
    print("    " + "-" * 70)

    combined_inv_var = 0.0
    combined_weighted = 0.0

    for name, f_loc, sig_loc, r in constraints:
        f_b, sig_b = recast_constraint(f_loc, sig_loc, r)
        print(f"    {name:<25s} {f_loc:>+8.1f} {sig_loc:>8.1f} {r:>6.3f} "
              f"{f_b:>+10.2f} {sig_b:>9.2f}")
        inv_var = 1.0 / sig_b**2
        combined_inv_var += inv_var
        combined_weighted += f_b * inv_var

    sigma_comb = 1.0 / np.sqrt(combined_inv_var)
    f_comb = combined_weighted / combined_inv_var
    t_pred_comb = compute_tension(f_comb, sigma_comb, f_pred)
    t_zero_comb = compute_tension(f_comb, sigma_comb, 0)

    print(f"    {'':25s} {'':>8s} {'':>8s} {'':>6s} {'──────────':>10s} {'─────────':>9s}")
    print(f"    {'COMBINED':<25s} {'':>8s} {'':>8s} {'':>6s} {f_comb:>+10.2f} {sigma_comb:>9.2f}")
    print(f"\n    Combined tension with prediction: {t_pred_comb:.2f}σ")
    print(f"    Combined tension with zero: {t_zero_comb:.2f}σ")

    # Step 5: Summary
    print(f"\n  " + "=" * 66)
    print(f"  SUMMARY")
    print(f"  " + "=" * 66)
    print(f"""
    PLANCK ALONE (bounce template):
      f_NL = {f_bounce:+.1f} ± {sigma_bounce:.1f}
      vs prediction ({f_pred}): {tension_pred:.1f}σ
      vs zero: {tension_zero:.1f}σ

    PLANCK + DESI COMBINED (bounce template):
      f_NL = {f_comb:+.1f} ± {sigma_comb:.1f}
      vs prediction: {t_pred_comb:.1f}σ
      vs zero: {t_zero_comb:.1f}σ

    VERDICT: Current data are consistent with both the bounce
    prediction AND zero. No discrimination yet.

    LEVEL: TRIAGE_RECAST
    This is a published-number recast, not a map-level extraction.
    Upgrade requires: injection/recovery validation on simulations.
    """)

    # Step 6: Output JSON
    result = {
        "pipeline": "F1",
        "stage": "F1.1",
        "level": "TRIAGE_RECAST",
        "planck_local": {
            "f_NL": PLANCK_LOCAL["f_NL"],
            "sigma": PLANCK_LOCAL["sigma"],
            "source": PLANCK_LOCAL["source"],
        },
        "template_overlap": {
            "r_cmb": r_cmb,
            "r_lss": r_lss,
            "r_uncertainty": r_err,
        },
        "planck_bounce": {
            "f_NL": float(f_bounce),
            "sigma": float(sigma_bounce),
            "tension_vs_prediction": float(tension_pred),
            "tension_vs_zero": float(tension_zero),
        },
        "combined_bounce": {
            "f_NL": float(f_comb),
            "sigma": float(sigma_comb),
            "tension_vs_prediction": float(t_pred_comb),
            "tension_vs_zero": float(t_zero_comb),
            "note": "APPROXIMATE — DESI values are estimated, not from official publication",
        },
        "canonical_prediction": {
            "f_NL": float(f_pred),
            "confidence": CANONICAL["confidence_canonical"],
        },
        "caveats": [
            "TRIAGE_RECAST: uses published numbers, not map-level data",
            "Template overlap r assumed constant (survey-weighted average)",
            "DESI values are approximate and may not match official publication",
            "Independence of Planck bispectrum and DESI SDB assumed but not rigorously verified",
            "No injection/recovery validation performed at this level",
        ],
    }

    outfile = OUTDIR / "F1_baseline_recast.json"
    with open(outfile, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  Output saved: {outfile}")


if __name__ == "__main__":
    main()
