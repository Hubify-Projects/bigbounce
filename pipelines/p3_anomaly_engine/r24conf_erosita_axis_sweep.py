#!/usr/bin/env python3
"""R24conf QUEUE-33 (P3 META-E1 + OpenAI-M2/M7 + META-m1) — eROSITA
production-threshold (0.259, n=298) axis re-derivation sweep.

Goal: determine on which axis/convention of the COMMITTED per-object score
artifacts the published top-298 threshold 0.259 (and the Table III S_BigAE
values 0.439-1.084) is reproducible. Prior audit excluded raw (rank-298 =
3.4119), full-sample z (0.218) and IF -decision_function 200-tree/seed-42
(0.301).

Committed artifacts used:
  pod_runs/erosita_dr1_raw/erosita_anomalies.parquet   (930,203 raw scores + 16-d latents)
  hf_staging_pod/erosita_dr1_anomalies.parquet         (298-row released selection)

Two tests:
  A. Monotone-axis sweep: every candidate axis that is a monotone per-object
     transform of the committed raw reconstruction score preserves rank
     ordering, so its rank-298 threshold is the transform of 3.4119. We
     tabulate that value for {raw, z, robust-z, log10, ln, z(log10),
     robust-z(log10), min-max, min-max(log10), /mean, /p99, ECDF, probit,
     sigmoid(z)} and for IsolationForest variants retrained on the committed
     16-d latents (100/200 trees, seeds 0/42).
  B. Monotonicity test against Table III: the production S_BigAE values for
     the 5 named top sources are compared in rank order against the committed
     raw scores. If the orderings disagree, NO monotone transform of the
     committed raw axis can reproduce the production scores — decisive for
     the membership-is-canonical framing.

Output: pipelines/p3_anomaly_engine/r24conf_erosita_axis_sweep.json
Run:    nice -n 5 python3 pipelines/p3_anomaly_engine/r24conf_erosita_axis_sweep.py
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

P3 = Path(__file__).resolve().parent
RAW = P3 / "pod_runs/erosita_dr1_raw/erosita_anomalies.parquet"
REL = P3 / "hf_staging_pod/erosita_dr1_anomalies.parquet"
OUT = P3 / "r24conf_erosita_axis_sweep.json"

TARGET = 0.259
N_SEL = 298

# Table III (paper3_draft.tex, tab:erosita_top) production S_BigAE values
TABLE3 = {
    "1eRASS J053856.1-640457": 1.084,
    "1eRASS J053544.3-660159": 0.815,
    "1eRASS J170249.4-484724": 0.591,
    "1eRASS J062619.8-694546": 0.498,
    "1eRASS J152039.9-570955": 0.439,
}

t0 = time.time()


def log(m):
    print(f"[{time.time()-t0:7.1f}s] {m}", flush=True)


def main():
    log("loading committed 930K raw-score artifact ...")
    lat_cols = [f"lat_{i:02d}" for i in range(16)]
    df = pd.read_parquet(RAW, columns=["iauname", "anomaly_score"] + lat_cols)
    s = df["anomaly_score"].to_numpy(np.float64)
    n = len(s)
    order = np.argsort(s)[::-1]
    thr_raw = float(s[order[N_SEL - 1]])
    log(f"n = {n:,}; rank-{N_SEL} raw threshold = {thr_raw:.6f}")

    # membership check: released 298 == raw top-298?
    rel = pd.read_parquet(REL, columns=["iauname", "anomaly_score"])
    top298_names = set(df["iauname"].to_numpy()[order[:N_SEL]])
    rel_names = set(rel["iauname"])
    membership_match = top298_names == rel_names
    log(f"released 298 == committed-raw top-298: {membership_match}")

    # ---- A. monotone-axis sweep -------------------------------------------
    mean, std = float(s.mean()), float(s.std(ddof=0))
    med = float(np.median(s))
    mad = float(np.median(np.abs(s - med)))
    s_pos = np.maximum(s, 1e-300)
    l10 = np.log10(s_pos)
    l10_mean, l10_std = float(l10.mean()), float(l10.std(ddof=0))
    l10_med = float(np.median(l10))
    l10_mad = float(np.median(np.abs(l10 - l10_med)))
    p99 = float(np.percentile(s, 99))
    smin, smax = float(s.min()), float(s.max())
    l10min, l10max = float(l10.min()), float(l10.max())
    z_thr = (thr_raw - mean) / std
    ecdf = 1.0 - (N_SEL - 1) / n  # fraction <= threshold (upper tail rank)

    axes = {
        "raw_reconstruction_score": thr_raw,
        "z_full_sample": z_thr,
        "robust_z_median_MAD": (thr_raw - med) / (1.4826 * mad),
        "log10": float(np.log10(thr_raw)),
        "ln": float(np.log(thr_raw)),
        "z_of_log10": (np.log10(thr_raw) - l10_mean) / l10_std,
        "robust_z_of_log10": (np.log10(thr_raw) - l10_med) / (1.4826 * l10_mad),
        "minmax_raw": (thr_raw - smin) / (smax - smin),
        "minmax_log10": (np.log10(thr_raw) - l10min) / (l10max - l10min),
        "raw_over_mean": thr_raw / mean,
        "raw_over_p99": thr_raw / p99,
        "ecdf_percentile": ecdf,
        "one_minus_ecdf": 1.0 - ecdf,
        "probit_of_ecdf": float(stats.norm.ppf(ecdf)),
        "sigmoid_of_z": float(1.0 / (1.0 + np.exp(-z_thr))),
        "sqrt_raw": float(np.sqrt(thr_raw)),
    }

    # IsolationForest variants on the committed 16-d latents
    try:
        from sklearn.ensemble import IsolationForest
        X = df[lat_cols].to_numpy(np.float32)
        for n_est, seed in [(100, 42), (200, 42), (100, 0)]:
            log(f"IF n_estimators={n_est} seed={seed} fit+score ...")
            iforest = IsolationForest(n_estimators=n_est, random_state=seed, n_jobs=-1)
            iforest.fit(X)
            d = -iforest.decision_function(X)  # higher = more anomalous
            axes[f"IF_neg_decision_function_{n_est}tree_seed{seed}"] = float(
                np.sort(d)[::-1][N_SEL - 1])
    except Exception as e:  # pragma: no cover
        axes["IF_variants_error"] = repr(e)

    sweep = []
    for name, val in axes.items():
        if isinstance(val, str):
            continue
        sweep.append({"axis": name, "rank_298_threshold": float(val),
                      "abs_delta_vs_0.259": float(abs(val - TARGET)),
                      "matches_0.259_at_3dp": bool(round(val, 3) == TARGET)})
    sweep.sort(key=lambda r: r["abs_delta_vs_0.259"])
    any_match = any(r["matches_0.259_at_3dp"] for r in sweep)
    for r in sweep[:6]:
        log(f"  {r['axis']:42s} thr = {r['rank_298_threshold']:.4f}")

    # ---- B. Table III monotonicity test ------------------------------------
    raw_by_name = dict(zip(df["iauname"], s))
    t3 = []
    for nm, sb in TABLE3.items():
        t3.append({"iauname": nm, "S_BigAE_production": sb,
                   "raw_committed": float(raw_by_name.get(nm, np.nan))})
    sb_v = np.array([r["S_BigAE_production"] for r in t3])
    rw_v = np.array([r["raw_committed"] for r in t3])
    rho, p_rho = stats.spearmanr(sb_v, rw_v)
    monotone = bool(abs(rho) == 1.0 and rho > 0)
    log(f"Table III Spearman(S_BigAE, committed raw) = {rho:+.3f} -> monotone with raw: {monotone}")

    out = {
        "job": "R24conf-P3-QUEUE33-erosita-axis-sweep",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "generator": "pipelines/p3_anomaly_engine/r24conf_erosita_axis_sweep.py",
        "committed_artifacts": [str(RAW.relative_to(P3.parents[1])),
                                str(REL.relative_to(P3.parents[1]))],
        "published_threshold": TARGET,
        "n_selected": N_SEL,
        "membership_check": {
            "released_298_equals_committed_raw_top298": membership_match,
            "released_min_score": float(rel["anomaly_score"].min()),
            "rank_298_raw_threshold": thr_raw,
        },
        "axis_sweep_rank298_thresholds": sweep,
        "any_axis_reproduces_0.259": any_match,
        "table3_monotonicity_test": {
            "rows": t3,
            "spearman_rho": float(rho),
            "production_axis_monotone_in_committed_raw": monotone,
            "implication": (
                "The production S_BigAE ordering of the Table III top-5 disagrees with the "
                "committed raw-score ordering (e.g. the committed-raw rank-1 source "
                "J062619.8-694546 carries production S_BigAE = 0.498 while the committed-raw "
                "rank-2 source J053856.1-640457 carries 1.084). Therefore NO monotone "
                "per-object transform of the committed raw axis (normalization, log, "
                "z-scoring, calibration) can reproduce the production scores or the 0.259 "
                "threshold." if not monotone else
                "Production ordering is consistent with a monotone transform of raw."),
        },
        "conclusion": (
            "No committed score axis reproduces the production threshold 0.259: the "
            "monotone sweep brackets it on no axis, and the Table III production scores "
            "are non-monotone in the committed raw artifact, ruling out the entire class "
            "of per-object monotone rescalings. The released 298-source membership list "
            "is, however, exactly the committed-raw top-298 (min released score = rank-298 "
            "raw threshold 3.4119): the n=298 membership itself is the committed, "
            "reproducible selection (membership-is-canonical)." if (not any_match and membership_match)
            else "See axis_sweep / membership_check."),
    }
    OUT.write_text(json.dumps(out, indent=1))
    log(f"wrote {OUT}")


if __name__ == "__main__":
    main()
