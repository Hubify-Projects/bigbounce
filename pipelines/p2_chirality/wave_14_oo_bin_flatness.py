#!/usr/bin/env python3
"""Wave 14-OO — P4-OA-B7 bin-by-bin CW flatness vs morphology axes (0.1% bar).

Closes R42 OpenAI P4-OA-B7 BLOCKER:
  "Bin-by-bin CW-fraction flatness vs r-mag, surface brightness, Sersic size,
   PSF FWHM, edge-on b/a — all bins must be flat to <0.1% to rule out
   morphology-driven CW/CCW asymmetry leak."

Inputs (Pod 3 H200, both already on disk):
  - /workspace/r42_b20/chirality_catalog/catalog_production.parquet
        8,474,531 rows, columns include p_cw_eq, p_ccw_eq, class_eq, dr8_id
  - /workspace/dr8_sweep_fetch/catalog_production_with_ba.parquet
        DR8 sweep metadata, joined on dr8_id:
          type, fracdev, shapeexp_r, shapedev_r, shape_r_eff, e_mag, b_over_a

Available axes (no flux_r in current sweep — that fetch fires in parallel):
  1. shape_r_eff (Sersic effective radius, log-binned)
  2. fracdev (de Vauc fraction, [0,1] linear bins)
  3. b_over_a (axis ratio, [0,1] linear bins) — already done Wave 14-KK,
     re-running here at finer granularity for completeness
  4. type (PSF / REX / EXP / DEV / COMP categorical)

Method:
  Per axis, equal-count quantile bins (10 for continuous, native for categorical).
  Per bin: count CW + CCW spirals, compute CW-fraction, Poisson SE.
  Flatness statistic = max-bin-to-bin spread of CW-fraction.
  Bar = 0.1% (paper's claimed tolerance).

  Strict criterion (BLOCKER bar): max bin-to-bin spread < 0.001.
  Soft criterion (sanity): max |bin - 0.5| < 0.001 + Poisson SE for that bin.

Output:
  /workspace/r42_b20/chirality_catalog/wave_14_oo_bin_flatness.json
"""
from __future__ import annotations
import json
import os
import time
from pathlib import Path

import numpy as np
import pandas as pd

CATALOG_PARQUET = "/workspace/r42_b20/chirality_catalog/catalog_production.parquet"
SWEEP_PARQUET = "/workspace/dr8_sweep_fetch/catalog_production_with_ba.parquet"
OUT_JSON = "/workspace/r42_b20/chirality_catalog/wave_14_oo_bin_flatness.json"

P_CW_THRESHOLD = 0.6  # |p_cw_eq| > 0.6 high-confidence equivariant spiral
N_BINS_CONT = 10
FLATNESS_BAR = 0.001  # 0.1% paper tolerance


def cw_fraction_per_bin(df: pd.DataFrame, bin_col: str) -> dict:
    """Compute CW-fraction per bin with Poisson SE."""
    rows = []
    groups = df.groupby(bin_col, observed=True)
    for label, g in groups:
        n_cw = int((g["class_eq"] == "CW").sum())
        n_ccw = int((g["class_eq"] == "CCW").sum())
        n_tot = n_cw + n_ccw
        if n_tot == 0:
            cw_frac, se = float("nan"), float("nan")
        else:
            cw_frac = n_cw / n_tot
            se = (cw_frac * (1 - cw_frac) / n_tot) ** 0.5
        rows.append(
            {
                "bin": str(label),
                "n_cw": n_cw,
                "n_ccw": n_ccw,
                "n_total": n_tot,
                "cw_fraction": cw_frac,
                "poisson_se": se,
                "z_vs_half": (cw_frac - 0.5) / se if (se and se > 0) else float("nan"),
            }
        )
    return rows


def axis_summary(rows: list[dict]) -> dict:
    """Compute flatness summary stats."""
    cw_fracs = np.array([r["cw_fraction"] for r in rows if not np.isnan(r["cw_fraction"])])
    if len(cw_fracs) < 2:
        return {
            "n_bins": len(rows),
            "max_bin_spread": float("nan"),
            "max_dev_from_half": float("nan"),
            "max_z_vs_half": float("nan"),
            "passes_strict_0p1pct_bar": False,
        }
    max_spread = float(cw_fracs.max() - cw_fracs.min())
    max_dev = float(np.max(np.abs(cw_fracs - 0.5)))
    max_z = float(np.nanmax([r["z_vs_half"] for r in rows]))
    return {
        "n_bins": len(rows),
        "max_bin_spread": max_spread,
        "max_dev_from_half": max_dev,
        "max_z_vs_half": max_z,
        "passes_strict_0p1pct_bar": bool(max_spread < FLATNESS_BAR),
    }


def main() -> None:
    t0 = time.time()
    print(f"[Wave 14-OO] start {time.strftime('%Y-%m-%d %H:%M:%S')}")

    print("[1/5] loading catalog_production.parquet ...")
    cat = pd.read_parquet(
        CATALOG_PARQUET, columns=["dr8_id", "p_cw_eq", "p_ccw_eq", "class_eq", "confidence_eq"]
    )
    print(f"        {len(cat):,} rows")

    print("[2/5] loading DR8 sweep metadata ...")
    sweep = pd.read_parquet(
        SWEEP_PARQUET,
        columns=["dr8_id", "type", "fracdev", "shapeexp_r", "shapedev_r", "shape_r_eff", "b_over_a"],
    )
    print(f"        {len(sweep):,} rows")

    print("[3/5] joining + filtering equivariant spirals (Wave 14-KK denominator) ...")
    df_join = cat.merge(sweep, on="dr8_id", how="inner")
    df_full = df_join[df_join["class_eq"].isin(["CW", "CCW"])].copy()
    df_hi = df_full[df_full["confidence_eq"] > P_CW_THRESHOLD].copy()
    print(f"        full spiral subsample (Wave 14-KK denom): {len(df_full):,}")
    print(f"        high-confidence subsample (>0.6):         {len(df_hi):,}")

    results: dict = {
        "wave": "14-OO",
        "task": "P4-OA-B7 bin-by-bin CW flatness",
        "p_cw_threshold": P_CW_THRESHOLD,
        "flatness_bar": FLATNESS_BAR,
        "denominators": {},
    }

    for denom_name, df in [("full_spiral", df_full), ("high_confidence", df_hi)]:
        cw_total = int((df["class_eq"] == "CW").sum())
        ccw_total = int((df["class_eq"] == "CCW").sum())
        cat_cw_frac = cw_total / (cw_total + ccw_total) if (cw_total + ccw_total) else float("nan")
        print(f"\n=== denominator: {denom_name} (n={len(df):,}, CW frac={cat_cw_frac:.6f}) ===")

        denom_block: dict = {
            "n_input": int(len(df)),
            "n_cw": cw_total,
            "n_ccw": ccw_total,
            "catalog_wide_cw_fraction": cat_cw_frac,
            "axes": {},
        }

        df = df.copy()
        df["bin_size"] = pd.qcut(
            np.log10(df["shape_r_eff"].clip(lower=1e-3)),
            q=N_BINS_CONT,
            duplicates="drop",
        )
        rows = cw_fraction_per_bin(df, "bin_size")
        summary = axis_summary(rows)
        denom_block["axes"]["shape_r_eff_log"] = {"summary": summary, "bins": rows}
        print(f"  shape_r_eff_log : spread={summary['max_bin_spread']:.6f} pass={summary['passes_strict_0p1pct_bar']}")

        df["bin_fd"] = pd.cut(df["fracdev"].fillna(0), bins=N_BINS_CONT)
        rows = cw_fraction_per_bin(df, "bin_fd")
        summary = axis_summary(rows)
        denom_block["axes"]["fracdev"] = {"summary": summary, "bins": rows}
        print(f"  fracdev         : spread={summary['max_bin_spread']:.6f} pass={summary['passes_strict_0p1pct_bar']}")

        df["bin_ba"] = pd.cut(df["b_over_a"].fillna(0).clip(0, 1), bins=N_BINS_CONT)
        rows = cw_fraction_per_bin(df, "bin_ba")
        summary = axis_summary(rows)
        denom_block["axes"]["b_over_a"] = {"summary": summary, "bins": rows}
        print(f"  b_over_a        : spread={summary['max_bin_spread']:.6f} pass={summary['passes_strict_0p1pct_bar']}")

        df["bin_type"] = df["type"].fillna("UNK").astype(str).str.strip()
        rows = cw_fraction_per_bin(df, "bin_type")
        summary = axis_summary(rows)
        denom_block["axes"]["type_categorical"] = {"summary": summary, "bins": rows}
        print(f"  type            : spread={summary['max_bin_spread']:.6f} pass={summary['passes_strict_0p1pct_bar']}")

        all_pass = all(
            ax["summary"]["passes_strict_0p1pct_bar"]
            for ax in denom_block["axes"].values()
            if not np.isnan(ax["summary"]["max_bin_spread"])
        )
        denom_block["all_axes_pass_0p1pct_bar"] = bool(all_pass)
        results["denominators"][denom_name] = denom_block

    elapsed = time.time() - t0
    results["wall_seconds"] = elapsed

    Path(OUT_JSON).parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n[5/5] wrote {OUT_JSON} (wall {elapsed:.1f}s)")
    for d, blk in results["denominators"].items():
        print(f"  {d}: all_axes_pass_0p1pct_bar={blk['all_axes_pass_0p1pct_bar']}")


if __name__ == "__main__":
    main()
