"""
P3 §pathc_caveats item (b) closure — explicit DESI OOD MSE threshold-in-OOD-units.

Multi-round-deferred item (R3/R4 GPT-B1 + R7 carry, ~2-3 weeks since first
flagged) asks: at what threshold would the canonical 0.87% headline anomaly
rate be preserved if applied to the OOD random-sweep sample rather than to
the curated 22.5M production catalog?

0.87% of N = 100,000 OOD spectra = 870 sources → top-870 cut → 99.13th percentile
of the OOD MSE distribution.

Read the existing B10 OOD summary at
pipelines/p3_anomaly_engine/r42_results/B10_ood_results_100k.json,
log-interpolate between p99 (=44.85) and p99.9 (=344.93) to get p99.13,
and convert to the equivalent canonical-S value.

The canonical-S↔MSE relationship: per §sec:method body, S=5 ↔ MSE≈0.143
in standardized units (= 5 × training_val_loss_ref = 5 × 0.0287). So:
  S = MSE / 0.0287

Output:
  pipelines/p3_anomaly_engine/r42_results/ood_threshold_2026-05-29.json
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

INP = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/r42_results/B10_ood_results_100k.json")
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/r42_results/ood_threshold_2026-05-29.json")
HEADLINE_RATE = 0.0087   # 0.87% DESI canonical headline rate
CANONICAL_S_CUT = 5.0
CANONICAL_MSE_CUT = 0.143

def main():
    d = json.loads(INP.read_text())
    n = d["n_spectra"]                  # 100,000
    val_ref = d["training_val_loss_ref"]  # 0.0287
    p99 = d["mse_p99"]                  # 44.849
    p99_9 = d["mse_p99_9"]              # 344.928
    median = d["mse_median"]            # 0.178

    # Target percentile to preserve 0.87% rate on OOD sample:
    # Top 0.87% of OOD = top-870 sources → percentile = 1 - 0.0087 = 0.9913
    target_pct = 1.0 - HEADLINE_RATE  # 0.9913
    target_pct_pp = target_pct * 100.0  # 99.13

    # Log-interpolate between p99 and p99.9 in (percentile, log10(MSE)) space.
    # The OOD MSE distribution tail is approximately power-law / log-linear;
    # linear interpolation in log-MSE between bracketing percentiles is the
    # natural estimator with only the summary statistics on disk.
    frac_along = (target_pct_pp - 99.0) / (99.9 - 99.0)  # 0.13 / 0.9 = 0.1444
    log_p99 = np.log10(p99)
    log_p99_9 = np.log10(p99_9)
    log_interp = log_p99 + frac_along * (log_p99_9 - log_p99)
    mse_at_target = 10.0 ** log_interp

    # Equivalent canonical-S value on OOD distribution:
    s_at_target_via_val = mse_at_target / val_ref
    s_at_target_via_canonical_cut = mse_at_target * (CANONICAL_S_CUT / CANONICAL_MSE_CUT)

    # Ratio to the curated-catalog S>5 cut:
    s_inflation = s_at_target_via_val / CANONICAL_S_CUT
    mse_inflation = mse_at_target / CANONICAL_MSE_CUT

    # What fraction of the OOD sample is flagged by the curated S>5 (MSE>0.143)?
    # Already in the JSON via fraction_above_5x_val (5x val_loss = 5 * 0.0287 = 0.1435 = same as MSE>0.143):
    frac_at_curated_cut = d["fraction_above_5x_val"]  # 0.52815

    result = {
        "script": "pipelines/p3_anomaly_engine/ood_threshold_2026-05-29.py",
        "purpose": "Closes P3 §pathc_caveats item (b) — explicit DESI OOD MSE threshold-in-OOD-units (R3/R4 GPT-B1 multi-round deferral).",
        "input_artifact": str(INP),
        "n_ood_spectra": int(n),
        "headline_rate_target": HEADLINE_RATE,
        "target_percentile": float(target_pct),
        "target_percentile_pct": float(target_pct_pp),
        "ood_percentiles_from_b10": {
            "median": median,
            "p99": p99,
            "p99_9": p99_9,
        },
        "interpolation_method": "linear in (percentile, log10(MSE)) between p99 and p99.9",
        "ood_threshold_at_0pct87_rate": {
            "MSE_standardized": float(mse_at_target),
            "S_via_training_val_ref": float(s_at_target_via_val),
            "S_via_canonical_cut_ratio": float(s_at_target_via_canonical_cut),
        },
        "inflation_vs_curated_cut": {
            "mse_at_0pct87_OOD_over_canonical_MSE_cut": float(mse_inflation),
            "S_at_0pct87_OOD_over_canonical_S_cut": float(s_inflation),
        },
        "curated_cut_applied_to_ood_sample": {
            "MSE_cut": float(CANONICAL_MSE_CUT),
            "fraction_of_OOD_flagged": float(frac_at_curated_cut),
            "fraction_pct": float(frac_at_curated_cut * 100.0),
            "ratio_to_0pct87_headline": float(frac_at_curated_cut / HEADLINE_RATE),
        },
        "interpretation": (
            f"To preserve the 0.87% headline anomaly rate on a representative random "
            f"SPARCL OOD sample, the per-sample cut should be the OOD 99.13th percentile, "
            f"which is MSE ≈ {mse_at_target:.2f} in standardized units (equivalently "
            f"S ≈ {s_at_target_via_val:.0f} relative to the training-pool reference, "
            f"i.e. ~{s_inflation:.0f}× the curated-catalog S>5 cut). Conversely, "
            f"applying the curated S>5 (MSE>0.143) cut as-is to the OOD sample flags "
            f"{frac_at_curated_cut*100:.1f}% of OOD spectra ({frac_at_curated_cut/HEADLINE_RATE:.0f}× "
            f"the headline rate), confirming the curation-not-threshold reconciliation."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    print(f"\n=== HEADLINE ===")
    print(f"  Target percentile to preserve 0.87% rate: {target_pct_pp:.2f}th")
    print(f"  Log-interp MSE_p99.13 = {mse_at_target:.2f}")
    print(f"  Equivalent S threshold ≈ {s_at_target_via_val:.0f}σ_train (= {s_inflation:.0f}× canonical S>5)")
    print(f"  Curated cut MSE>0.143 applied to OOD: {frac_at_curated_cut*100:.1f}% flagged ({frac_at_curated_cut/HEADLINE_RATE:.0f}× headline)")


if __name__ == "__main__":
    main()
