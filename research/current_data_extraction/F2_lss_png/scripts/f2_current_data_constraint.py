#!/usr/bin/env python3
"""
Task 2: F2 Current-Data PNG Constraint

Builds the best honest current-data f_NL constraint using Planck + LSS,
answering: does adding LSS information materially improve the picture?

This uses PUBLISHED constraints (not raw data) because:
1. DESI DR1 f_NL results are not yet in a final public catalog
2. The LSS f_NL constraint comes from scale-dependent bias papers
3. We can still assess whether the COMBINATION improves things

Method: Fisher-combination of independent constraints,
corrected for bounce-template mismatch.
"""

import numpy as np
import json
from pathlib import Path

OUTDIR = Path(__file__).parent.parent / "outputs"
OUTDIR.mkdir(exist_ok=True)

# ═══════════════════════════════════════
# Published / estimated f_NL constraints
# ═══════════════════════════════════════

# Template overlap factors
R_CMB = 0.878   # ℓ-space Fisher (validated)
R_LSS = 0.83    # LSS SDB weighting (conservative)
R_INJ = 0.90    # Injection-validated

constraints = {
    "planck_TplusE": {
        "source": "Planck 2018 IX, Table 4, KSW T+E",
        "f_NL_local": -0.9, "sigma_local": 5.1,
        "type": "CMB_bispectrum", "r": R_CMB,
        "direct": True,
    },
    "planck_T_only": {
        "source": "Planck 2018 IX, Table 4, KSW T-only",
        "f_NL_local": -0.6, "sigma_local": 5.7,
        "type": "CMB_bispectrum", "r": R_CMB,
        "direct": True,
    },
    "desi_qso_sdb": {
        "source": "DESI DR1 QSO SDB (Mueller et al., approximate)",
        "f_NL_local": -3.6, "sigma_local": 9.2,
        "type": "LSS_SDB", "r": R_LSS,
        "direct": False, "note": "approximate value from early analysis",
    },
    "desi_pb_combined": {
        "source": "DESI DR1 P+B (approximate)",
        "f_NL_local": -0.1, "sigma_local": 7.4,
        "type": "LSS_bispectrum", "r": R_LSS,
        "direct": False, "note": "approximate",
    },
    "euclid_forecast": {
        "source": "Euclid photometric forecast (Amendola et al.)",
        "f_NL_local": 0.0, "sigma_local": 3.0,
        "type": "LSS_photometric", "r": R_LSS,
        "direct": False, "note": "FORECAST, not measurement",
    },
    "cmbs4_forecast": {
        "source": "CMB-S4 forecast (bispectrum)",
        "f_NL_local": 0.0, "sigma_local": 2.5,
        "type": "CMB_bispectrum", "r": R_CMB,
        "direct": False, "note": "FORECAST, not measurement",
    },
}

# Canonical prediction
F_NL_PRED = -35/8  # = -4.375

print("=" * 70)
print("F2: CURRENT-DATA PNG CONSTRAINT SUMMARY")
print("=" * 70)

# ═══════════════════════════════════════
# Compute bounce-template constraints
# ═══════════════════════════════════════

def recast(f_local, sigma_local, r):
    return f_local / r, sigma_local / r

results = {}

print("\n  INDIVIDUAL CONSTRAINTS (bounce template):")
print("  %-25s %8s %8s %10s %10s %8s %s" % (
    "Constraint", "f_local", "σ_local", "f_bounce", "σ_bounce", "vs pred", "Type"))
print("  " + "-" * 85)

for name, c in constraints.items():
    f_b, sig_b = recast(c["f_NL_local"], c["sigma_local"], c["r"])
    tension = abs(f_b - F_NL_PRED) / sig_b
    dtype = "DIRECT" if c["direct"] else ("FORECAST" if "forecast" in name else "APPROX")

    results[name] = {
        **c,
        "f_NL_bounce": float(f_b),
        "sigma_bounce": float(sig_b),
        "tension_vs_pred": float(tension),
        "data_type": dtype,
    }

    print("  %-25s %+8.1f %8.1f %+10.2f %10.2f %7.2fσ %s" % (
        name[:25], c["f_NL_local"], c["sigma_local"], f_b, sig_b, tension, dtype))

# ═══════════════════════════════════════
# Combinations
# ═══════════════════════════════════════

combos = {
    "Planck T+E only": ["planck_TplusE"],
    "Planck + DESI QSO": ["planck_TplusE", "desi_qso_sdb"],
    "Planck + DESI P+B": ["planck_TplusE", "desi_pb_combined"],
    "Planck + all DESI": ["planck_TplusE", "desi_qso_sdb", "desi_pb_combined"],
    "All current (direct+approx)": ["planck_TplusE", "desi_qso_sdb", "desi_pb_combined"],
    "Future: +Euclid +CMB-S4": ["planck_TplusE", "desi_qso_sdb", "desi_pb_combined", "euclid_forecast", "cmbs4_forecast"],
}

print("\n  COMBINATIONS:")
print("  %-30s %10s %10s %8s %8s %s" % (
    "Combination", "f_bounce", "σ_bounce", "vs pred", "vs zero", "Improvement"))
print("  " + "-" * 80)

combo_results = {}
planck_only_sigma = results["planck_TplusE"]["sigma_bounce"]

for combo_name, members in combos.items():
    inv_var = 0
    weighted = 0
    all_direct = True

    for m in members:
        r = results[m]
        s = r["sigma_bounce"]
        f = r["f_NL_bounce"]
        inv_var += 1.0 / s**2
        weighted += f / s**2
        if not r.get("direct", False):
            all_direct = False

    sigma_comb = 1.0 / np.sqrt(inv_var)
    f_comb = weighted / inv_var
    tension_pred = abs(f_comb - F_NL_PRED) / sigma_comb
    tension_zero = abs(f_comb) / sigma_comb
    improvement = (1 - sigma_comb / planck_only_sigma) * 100

    combo_results[combo_name] = {
        "f_NL_bounce": float(f_comb),
        "sigma_bounce": float(sigma_comb),
        "tension_pred": float(tension_pred),
        "tension_zero": float(tension_zero),
        "improvement_pct": float(improvement),
        "all_direct": all_direct,
        "members": members,
    }

    dtype = "DIRECT" if all_direct else "MIXED"
    print("  %-30s %+10.2f %10.2f %7.2fσ %7.2fσ %+6.1f%% (%s)" % (
        combo_name[:30], f_comb, sigma_comb, tension_pred, tension_zero, improvement, dtype))

# ═══════════════════════════════════════
# Verdict
# ═══════════════════════════════════════

planck_desi = combo_results["Planck + all DESI"]
planck_only = combo_results["Planck T+E only"]

improvement = planck_desi["improvement_pct"]
materially_better = improvement > 10

print("\n" + "=" * 70)
print("VERDICT")
print("=" * 70)
print("""
  Planck alone:        f_NL = %+.1f ± %.1f (bounce template)
  Planck + DESI:       f_NL = %+.1f ± %.1f (bounce template)
  Improvement:         %.1f%% reduction in sigma

  Does DESI materially improve? %s
  Reason: DESI SDB has σ ≈ 9-11 on bounce template, much wider than
  Planck's σ ≈ 5.8. The combination helps modestly but Planck
  bispectrum dominates.

  Current data vs prediction (-4.375): %.1fσ away
  Current data vs zero: %.1fσ away
  Status: CANNOT DISCRIMINATE
""" % (planck_only["f_NL_bounce"], planck_only["sigma_bounce"],
       planck_desi["f_NL_bounce"], planck_desi["sigma_bounce"],
       improvement,
       "YES" if materially_better else "NO — DESI adds < 10%% improvement",
       planck_desi["tension_pred"], planck_desi["tension_zero"]))

# Save
output = {
    "individual": results,
    "combinations": combo_results,
    "canonical_prediction": F_NL_PRED,
    "template_overlap": {"r_cmb": R_CMB, "r_lss": R_LSS, "r_injection": R_INJ},
    "verdict": {
        "desi_materially_improves": materially_better,
        "improvement_pct": float(improvement),
        "best_current_sigma": float(planck_desi["sigma_bounce"]),
        "best_current_fnl": float(planck_desi["f_NL_bounce"]),
    },
}

outfile = OUTDIR / "F2_current_data_constraint.json"
with open(outfile, "w") as f:
    json.dump(output, f, indent=2)
print("Saved:", outfile)
