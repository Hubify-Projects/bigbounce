#!/usr/bin/env python3
"""Analysis A — chirality vs redshift.

Per-bin CW fraction with binomial uncertainties, logistic regression
chirality ~ redshift + sky controls + confidence, and a permutation null.
All outputs land under results/analysis_redshift/.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, resolve_p5_path, ensure_dir, utc_now


def _binomial_ci(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    if n == 0:
        return (np.nan, np.nan)
    from scipy.stats import beta
    lo = beta.ppf(alpha / 2, k, n - k + 1) if k > 0 else 0.0
    hi = beta.ppf(1 - alpha / 2, k + 1, n - k) if k < n else 1.0
    return (lo, hi)


def _bin_table(df: pd.DataFrame, edges: list[float]) -> pd.DataFrame:
    df = df[df["match_class_eq"].isin(["CW", "CCW"])].copy()
    df["z_bin"] = pd.cut(df["desi_z"], bins=edges, include_lowest=True)
    rows = []
    for z_bin, sub in df.groupby("z_bin"):
        n_cw = int((sub["match_class_eq"] == "CW").sum())
        n = int(len(sub))
        if n == 0:
            continue
        f = n_cw / n
        lo, hi = _binomial_ci(n_cw, n)
        sigma = (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n > 0 else np.nan
        rows.append({
            "z_low": float(z_bin.left), "z_high": float(z_bin.right),
            "n": n, "n_cw": n_cw, "n_ccw": n - n_cw,
            "cw_fraction": f, "ci95_low": lo, "ci95_high": hi,
            "sigma_from_half": sigma,
        })
    return pd.DataFrame(rows)


def _logistic(df: pd.DataFrame) -> dict:
    """chirality ~ z + |sin(dec)| + cos(ra) + confidence (no statsmodels dep)."""
    from sklearn.linear_model import LogisticRegression
    spirals = df[df["match_class_eq"].isin(["CW", "CCW"])].copy()
    if len(spirals) < 100:
        return {"skipped": True, "n": int(len(spirals))}
    y = (spirals["match_class_eq"] == "CW").astype(int).to_numpy()
    X = np.column_stack([
        spirals["desi_z"].to_numpy(),
        np.abs(np.sin(np.deg2rad(spirals["desi_dec"].to_numpy()))),
        np.cos(np.deg2rad(spirals["desi_ra"].to_numpy())),
        spirals["match_confidence"].to_numpy(),
    ])
    keep = np.isfinite(X).all(axis=1) & np.isfinite(y)
    X, y = X[keep], y[keep]
    model = LogisticRegression(penalty=None, solver="lbfgs", max_iter=2000)
    model.fit(X, y)
    return {
        "skipped": False,
        "n": int(len(y)),
        "intercept": float(model.intercept_[0]),
        "coef": dict(zip(
            ["z", "abs_sin_dec", "cos_ra", "confidence"],
            [float(c) for c in model.coef_[0]],
        )),
    }


def _permutation_null(df: pd.DataFrame, edges: list[float], n_perm: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    spirals = df[df["match_class_eq"].isin(["CW", "CCW"])].copy()
    labels = (spirals["match_class_eq"] == "CW").to_numpy().astype(int)
    z = spirals["desi_z"].to_numpy()
    bin_idx = np.digitize(z, edges) - 1
    n_bins = len(edges) - 1
    obs = np.array([
        labels[bin_idx == i].mean() if (bin_idx == i).sum() else np.nan
        for i in range(n_bins)
    ])
    null_max_abs = np.zeros(n_perm)
    for k in range(n_perm):
        perm = rng.permutation(labels)
        null = np.array([
            perm[bin_idx == i].mean() if (bin_idx == i).sum() else np.nan
            for i in range(n_bins)
        ])
        null_max_abs[k] = np.nanmax(np.abs(null - 0.5))
    obs_max = float(np.nanmax(np.abs(obs - 0.5)))
    p_value = float((null_max_abs >= obs_max).mean())
    return {
        "n_permutations": int(n_perm),
        "obs_max_abs_deviation_from_half": obs_max,
        "p_value": p_value,
        "null_p99": float(np.quantile(null_max_abs, 0.99)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    args = parser.parse_args()
    cfg = load_config(args.config)

    matched_path = resolve_p5_path(cfg["paths"]["out_matched"])
    if not matched_path.exists():
        print(f"ERROR: {matched_path} missing. Run 03_crossmatch.py first.")
        return 2

    out_dir = ensure_dir(resolve_p5_path("results/analysis_redshift"))
    df = pd.read_parquet(matched_path)
    df = df[df.get("matched_primary_deduped", df["matched_primary"])].copy()

    edges = list(cfg["analysis"]["redshift_bins"]["edges"])
    table = _bin_table(df, edges)
    table.to_csv(out_dir / "cw_fraction_by_z.csv", index=False)

    logit = _logistic(df)
    (out_dir / "logistic.json").write_text(json.dumps(logit, indent=2))

    perm = _permutation_null(
        df, edges,
        n_perm=int(cfg["analysis"].get("permutation_n", 1000)),
        seed=int(cfg["statistics"]["random_seed"]),
    )
    (out_dir / "permutation_null.json").write_text(json.dumps(perm, indent=2))

    summary = {
        "written_utc": utc_now(),
        "config_version": cfg["version"],
        "n_spirals_total": int((df["match_class_eq"].isin(["CW", "CCW"])).sum()),
        "redshift_table_path": "cw_fraction_by_z.csv",
        "logistic_summary": logit,
        "permutation_summary": perm,
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    print(f"[done] wrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
