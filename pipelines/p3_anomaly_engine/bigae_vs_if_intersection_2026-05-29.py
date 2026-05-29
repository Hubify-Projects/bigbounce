"""
P3 §pathc_caveats item (f) closure — BigAE vs IsolationForest intersection on eROSITA.

Multi-round-deferred item from R3/R4 Gemini-M1 + R7 GEM-M3: the eROSITA
"high overlap" claim between the canonical-S (BigAE autoencoder) anomaly set
and the IsolationForest baseline needs an exact intersection count.

Per the §pathc_caveats item (f) text: "the exact empirical intersection
count (number of objects in both the canonical-S top-298 and the
IsolationForest top-9,303)" — straightforward intersection of two sorted
index lists.

Data:
  pipelines/p3_anomaly_engine/pod_runs/erosita_dr1_raw/erosita_anomalies.parquet
    Full eROSITA DR1 BigAE scoring: 930,203 sources × 26 cols
    Columns: iauname, ra, dec, anomaly_score (BigAE reconstruction MSE),
              ml_flux_1, ml_rate_1, det_like_1, ext, ext_like, pos_err,
              lat_00..lat_15 (16-d BigAE latent space)

Strategy:
  1. BigAE-top-298: sort by anomaly_score descending, take top 298.
     (The 298 is the v3.1.x P3 Path-C-native eROSITA headline count
     after the strict 5σ injection-recovery gate.)
  2. IF-top-9303: fit IsolationForest on the 16-d BigAE latent space,
     take top 9,303 by IF score. (The 9,303 is the eROSITA summary's
     top-1% threshold under either scoring axis.)
  3. Intersect by iauname. Report intersection count + p-value under
     null of independent random samples.

Output:
  pipelines/p3_anomaly_engine/r42_results/bigae_vs_if_intersection_2026-05-29.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

PARQ = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/pod_runs/erosita_dr1_raw/erosita_anomalies.parquet")
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/r42_results/bigae_vs_if_intersection_2026-05-29.json")

N_BIGAE_TOP = 298    # Path-C native eROSITA headline (after 5σ injection-recovery)
N_IF_TOP = 9303      # eROSITA top-1% under either scoring axis
SEED = 42


def hypergeom_p(intersect: int, n_bigae: int, n_if: int, n_total: int) -> tuple[float, float]:
    """Two-sided p-value + expected-under-null for hypergeometric intersection."""
    from scipy.stats import hypergeom

    rv = hypergeom(n_total, n_bigae, n_if)
    expected = n_bigae * n_if / n_total
    # Two-sided: probability of seeing |k - E| as large or larger
    sf = rv.sf(intersect - 1)  # P(X >= intersect)
    cdf = rv.cdf(intersect)
    p_upper = sf
    p_lower = cdf - (intersect != 0) * rv.pmf(intersect)  # P(X <= intersect-1)
    # Symmetric two-sided around expectation:
    if intersect >= expected:
        p_two_sided = 2 * min(p_upper, 0.5)
    else:
        p_two_sided = 2 * min(cdf, 0.5)
    return float(p_two_sided), float(expected)


def main():
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] loading {PARQ.name} ...", flush=True)
    df = pd.read_parquet(PARQ)
    n_total = len(df)
    print(f"  rows: {n_total:,}", flush=True)

    # ============================================================
    # (1) BigAE top-298 by anomaly_score
    # ============================================================
    df_bigae_sorted = df.sort_values("anomaly_score", ascending=False).reset_index(drop=True)
    bigae_top = df_bigae_sorted.head(N_BIGAE_TOP)
    bigae_top_names = set(bigae_top["iauname"].tolist())
    bigae_score_threshold = float(bigae_top["anomaly_score"].iloc[-1])
    print(f"\n[BigAE] top-{N_BIGAE_TOP} threshold score = {bigae_score_threshold:.4e}", flush=True)

    # ============================================================
    # (2) IsolationForest on 16-d BigAE latent space
    # ============================================================
    lat_cols = [c for c in df.columns if c.startswith("lat_")]
    assert len(lat_cols) == 16, f"expected 16 lat_NN cols, got {len(lat_cols)}: {lat_cols}"
    X = df[lat_cols].to_numpy()
    print(f"\n[IF] fitting IsolationForest on {X.shape[0]:,} x {X.shape[1]} latents ...", flush=True)
    iso = IsolationForest(
        n_estimators=200,
        contamination="auto",
        random_state=SEED,
        n_jobs=-1,
    )
    iso.fit(X)
    # decision_function: higher = more normal. So -decision_function = anomaly score.
    if_scores = -iso.decision_function(X)
    df["if_score"] = if_scores
    print(f"[{time.time()-t0:.1f}s] IF fit done. IF score: mean={if_scores.mean():.4f} std={if_scores.std():.4f}", flush=True)

    df_if_sorted = df.sort_values("if_score", ascending=False).reset_index(drop=True)
    if_top = df_if_sorted.head(N_IF_TOP)
    if_top_names = set(if_top["iauname"].tolist())
    if_score_threshold = float(if_top["if_score"].iloc[-1])
    print(f"[IF] top-{N_IF_TOP} threshold IF-score = {if_score_threshold:.4e}", flush=True)

    # ============================================================
    # (3) Intersection
    # ============================================================
    intersect = bigae_top_names & if_top_names
    n_intersect = len(intersect)

    bigae_in_if_frac = n_intersect / N_BIGAE_TOP
    if_in_bigae_frac = n_intersect / N_IF_TOP

    # Null hypothesis: BigAE-top-298 and IF-top-9303 are independent random subsets.
    p_two_sided, expected = hypergeom_p(n_intersect, N_BIGAE_TOP, N_IF_TOP, n_total)
    enrichment = n_intersect / expected if expected > 0 else float("inf")

    print(f"\n=== INTERSECTION ===")
    print(f"  BigAE top-{N_BIGAE_TOP} ∩ IF top-{N_IF_TOP} = {n_intersect}")
    print(f"  {n_intersect}/{N_BIGAE_TOP} = {100*bigae_in_if_frac:.1f}% of BigAE-top-{N_BIGAE_TOP} are in IF-top-{N_IF_TOP}")
    print(f"  {n_intersect}/{N_IF_TOP} = {100*if_in_bigae_frac:.2f}% of IF-top-{N_IF_TOP} are in BigAE-top-{N_BIGAE_TOP}")
    print(f"  Expected under independence: {expected:.2f}")
    print(f"  Enrichment vs random: {enrichment:.1f}x")
    print(f"  Two-sided hypergeometric p-value: {p_two_sided:.3e}")

    # ============================================================
    # Output
    # ============================================================
    result = {
        "script": "pipelines/p3_anomaly_engine/bigae_vs_if_intersection_2026-05-29.py",
        "purpose": "Closes P3 §sec:pathc_caveats item (f) — BigAE-vs-IsolationForest 'high overlap' verification (R3+R4 Gemini-M1, R7 GEM-M3 multi-round deferral).",
        "data_source": str(PARQ),
        "n_total_sources": int(n_total),
        "n_bigae_top": N_BIGAE_TOP,
        "n_if_top": N_IF_TOP,
        "bigae_top_score_threshold": bigae_score_threshold,
        "if_top_score_threshold": if_score_threshold,
        "if_n_estimators": 200,
        "if_random_state": SEED,
        "if_features": lat_cols,
        "intersection": {
            "count": int(n_intersect),
            "frac_of_bigae_top": float(bigae_in_if_frac),
            "frac_of_if_top": float(if_in_bigae_frac),
            "expected_under_independence": float(expected),
            "enrichment_vs_random": float(enrichment),
            "hypergeometric_p_two_sided": float(p_two_sided),
        },
        "interpretation": (
            f"BigAE-top-{N_BIGAE_TOP} ∩ IF-top-{N_IF_TOP} = {n_intersect} "
            f"({100*bigae_in_if_frac:.1f}% of BigAE-top-{N_BIGAE_TOP} are also IF-top-{N_IF_TOP}); "
            f"expected under random-independence null = {expected:.2f}; "
            f"enrichment {enrichment:.1f}x; hypergeometric two-sided p = {p_two_sided:.3e}. "
            f"This quantifies the §3.4 'high overlap' qualitative claim with a real empirical "
            f"intersection number and statistical significance against the random-independence null."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
