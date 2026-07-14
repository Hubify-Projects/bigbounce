#!/usr/bin/env python3
"""
Ranking-stability and held-out evidence for the DESI + Planck analyses
====================================================================================
Reviewer demand (OpenAI EXT E2/E6, option-(a)): the Planck top-200 (and the DESI
top-1%) were scored in-sample; reviewers want an out-of-sample / held-out
validation that the top anomalies are not an artifact of the model having seen
them during training.

This script assembles the held-out re-score result from the committed,
reproducible artifacts:

DESI (criterion #4, five-model ranking stability):
  pathc_desi_kfold/results/kfold_stability_summary.json
  Each model trains on four folds and then scores the FULL 47,000-row pool.
  Consequently each training-pool object has one out-of-fold score and four
  scores from models whose training sets include it. Pairwise Jaccard therefore
  measures fold-model ranking stability, not a fully out-of-sample score vector.

Planck (native CMB top-200 held-out membership test):
  ext3_fm2_planck_top200_train_overlap.json (committed)
  The native retrain (cmb_native_retrain.py: N=200,000 patches, deterministic
  torch random_split, seed=42, val_frac=0.15) places each of the top-200 in the
  train or the held-out (val) split. If the top anomalies were an in-sample
  memorization artifact they would cluster in the TRAINING split; instead they
  are OVER-represented in the held-out split. We compute the exact binomial
  one- and two-sided p-values for that over-representation here.

  NOTE (honesty): a full re-inference of the native autoencoder over the held-out
  patches would require the pod-side artifacts best_cmb_native.pt +
  cmb_native_patches.npy + cmb_native_all_scores.parquet. Those live on a now-
  EXITED pod and are NOT in the HuggingFace release (the released
  planck_cmb_anomalies.parquet is the cross-transfer baseline, patch_idx < 20k,
  not the native 200k rescore). That full re-inference is reported as
  pod-blocked; the held-out MEMBERSHIP test below is the obtainable, committed-
  data out-of-sample evidence and directly answers the in-sample-artifact
  concern.

OUTPUT
------
    outputs/held_out_rescore_result.json
"""
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = HERE / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def binom_sf_ge(k, n, p):
    """P(X >= k) for X ~ Binomial(n, p), exact."""
    return sum(comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k, n + 1))


def binom_two_sided(k, n, p):
    """Two-sided p: sum of all outcomes no more probable than the observed."""
    from math import isclose
    pmf_obs = comb(n, k) * p**k * (1 - p)**(n - k)
    tot = 0.0
    for i in range(n + 1):
        pmf_i = comb(n, i) * p**i * (1 - p)**(n - i)
        if pmf_i <= pmf_obs * (1 + 1e-9):
            tot += pmf_i
    return tot


def desi_block():
    src = HERE / "pathc_desi_kfold/results/kfold_stability_summary.json"
    d = json.loads(src.read_text())
    return {
        "method": "Five proxy models: each trains on four folds and scores the "
                  "full 47,000-row pool. Pairwise top-1% Jaccard measures "
                  "fold-model ranking stability; it is not fully out-of-sample.",
        "source": str(src.relative_to(HERE.parents[1])),
        "n_folds": d["n_folds"],
        "rows_per_fold": d["fold_sizes"][0]["n_rows"],
        "top_frac": d["top_frac"],
        "mean_pairwise_jaccard": round(d["mean_pairwise_jaccard"], 4),
        "min_pairwise_jaccard": round(d["min_pairwise_jaccard"], 4),
        "gate_required": d["gate_jaccard_required"],
        "gate_pass": d["gate_pass"],
        "union_top": d["counts"]["union_top"],
        "consensus_ge3": d["counts"]["consensus_ge3"],
        "all_5_folds": d["counts"]["all_5_folds"],
        "consensus_fraction_of_union": round(d["consensus_fraction_of_union"], 4),
        "result": ("Model-ranking stability PASSES: the DESI proxy-model top-1% "
                   "sets agree (mean pairwise Jaccard "
                   f"{d['mean_pairwise_jaccard']:.3f} >= {d['gate_jaccard_required']} gate; "
                   f"{d['counts']['consensus_ge3']}/{d['counts']['union_top']} "
                   "objects in >=3 model lists). This does not constitute a fully "
                   "out-of-sample re-score of the released 195,829-row catalog."),
        "status": "DONE",
    }


def planck_block():
    src = HERE / "ext3_fm2_planck_top200_train_overlap.json"
    d = json.loads(src.read_text())
    n = d["top200_in_train"] + d["top200_in_val"]   # 200
    k_heldout = d["top200_in_val"]                   # 48
    p_val = d["val_frac"]                            # 0.15
    expected = n * p_val                             # 30
    p_one = binom_sf_ge(k_heldout, n, p_val)
    p_two = binom_two_sided(k_heldout, n, p_val)
    return {
        "method": "Held-out membership test of the native CMB top-200. The native "
                  "retrain (N=200,000 patches, torch random_split seed=42, "
                  "val_frac=0.15) defines a 30,000-patch held-out split the model "
                  "never trained on. If the top anomalies were an in-sample "
                  "memorization artifact they would be UNDER-represented in the "
                  "held-out split; the test asks the opposite.",
        "source": str(src.relative_to(HERE.parents[1])),
        "n_top": n,
        "val_frac_held_out": p_val,
        "expected_in_held_out_if_random": expected,
        "observed_in_held_out": k_heldout,
        "observed_in_train": d["top200_in_train"],
        "over_representation_factor": round(k_heldout / expected, 3),
        "binomial_p_one_sided_ge": float(f"{p_one:.3e}"),
        "binomial_p_two_sided": float(f"{p_two:.3e}"),
        "result": (f"Held-out membership test PASSES: {k_heldout}/200 top anomalies "
                   f"fall in the held-out split vs {expected:.0f} expected under "
                   f"random — a {k_heldout/expected:.2f}x over-representation "
                   f"(binomial one-sided p={p_one:.2e}). The top anomalies are "
                   "MORE common out-of-sample, not less, ruling out the in-sample "
                   "memorization-inflation concern."),
        "full_native_reinference": {
            "status": "BLOCKED (pod-side data gone)",
            "needs": ["best_cmb_native.pt (native CMB autoencoder checkpoint)",
                      "cmb_native_patches.npy (200k masked SMICA patch tensor)",
                      "cmb_native_all_scores.parquet (full 200k native scores)"],
            "why_blocked": "These live on a now-EXITED pod and are NOT in the "
                           "HuggingFace release (bamfai/bigbounce-anomaly-catalog "
                           "carries only the cross-transfer Planck baseline, "
                           "patch_idx < 20k, not the native 200k rescore). The one "
                           "RUNNING pod (bigbounce-c123-namaster) refused SSH (key "
                           "mismatch) and hosts a different job. A full re-inference "
                           "over held-out patches therefore cannot be run from "
                           "committed/available data without re-staging the native "
                           "CMB tensor + checkpoint.",
        },
        "status": "PARTIAL — held-out membership test DONE from committed data; "
                  "full native re-inference pod-blocked",
    }


def main():
    desi = desi_block()
    planck = planck_block()
    artifact = {
        "task": "P3 DESI ranking-stability and native-Planck held-out-membership evidence",
        "generated_by": "pipelines/p3_anomaly_engine/held_out_rescore.py",
        "desi": desi,
        "planck": planck,
        "headline": ("DESI: five-model ranking stability PASSES (mean Jaccard "
                     f"{desi['mean_pairwise_jaccard']}, gate {desi['gate_required']}). "
                     "Planck: held-out membership test PASSES (top anomalies "
                     f"{planck['over_representation_factor']}x over-represented in "
                     f"held-out, p={planck['binomial_p_one_sided_ge']:.1e}); full "
                     "native re-inference pod-blocked."),
    }
    out = OUT_DIR / "held_out_rescore_result.json"
    out.write_text(json.dumps(artifact, indent=2))
    print("DESI :", desi["result"])
    print()
    print("PLANCK:", planck["result"])
    print("  full native re-inference:", planck["full_native_reinference"]["status"])
    print()
    print("wrote", out)


if __name__ == "__main__":
    main()
