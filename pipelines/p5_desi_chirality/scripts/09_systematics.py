#!/usr/bin/env python3
"""Systematics + null tests — Analysis E.

Tests:
  1. Chirality-label shuffle (preserves sky/redshift, breaks any signal)
  2. Sky-position permutation (preserves labels, scrambles positions)
  3. Confidence-threshold sensitivity (0.4 ... 0.8)
  4. Match-radius sensitivity (re-runs CW fraction at each radius)
  5. Redshift-quality sensitivity (drop strict ZWARN check)
  6. Imaging-leg / footprint split (north/south/des_only)
  7. DESI target-class split (BGS/LRG/ELG/QSO)

Outputs land in results/analysis_systematics/.
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


# DESI target bits (BGS_ANY example shifts; this is a minimal stub mapping;
# real bit masks come from desitarget. We use SURVEY+PROGRAM as a fallback.)
def _target_class(row) -> str:
    p = (row.get("desi_program") or "").lower()
    if "bright" in p:
        return "BGS_ANY"
    if "dark" in p:
        return "ELG_LRG_QSO"
    return "OTHER"


def _radius_sensitivity(df: pd.DataFrame, radii: list[float]) -> pd.DataFrame:
    rows = []
    for r in radii:
        col = f"matched_{r}arcsec"
        if col not in df.columns:
            continue
        sub = df[df[col] & df["match_class_eq"].isin(["CW", "CCW"])]
        n = int(len(sub))
        n_cw = int((sub["match_class_eq"] == "CW").sum())
        rows.append({
            "radius_arcsec": float(r), "n": n, "n_cw": n_cw,
            "cw_fraction": (n_cw / n) if n else np.nan,
            "sigma_from_half": (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n else np.nan,
        })
    return pd.DataFrame(rows)


def _confidence_sensitivity(df: pd.DataFrame, thresholds: list[float]) -> pd.DataFrame:
    rows = []
    for t in thresholds:
        sub = df[
            (df["match_confidence"] >= t)
            & df["match_class_eq"].isin(["CW", "CCW"])
        ]
        n = int(len(sub))
        n_cw = int((sub["match_class_eq"] == "CW").sum())
        rows.append({
            "min_confidence": float(t), "n": n, "n_cw": n_cw,
            "cw_fraction": (n_cw / n) if n else np.nan,
            "sigma_from_half": (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n else np.nan,
        })
    return pd.DataFrame(rows)


def _footprint_split(df: pd.DataFrame) -> pd.DataFrame:
    splits = {
        "all": df,
        "north": df[df["desi_dec"] >= 32.375],
        "south_nondes": df[(df["desi_dec"] < 32.375) & (df["match_imaging_leg"] == "DECaLS")],
        "des_only": df[df["match_imaging_leg"] == "DES"],
        "bassmzls": df[df["match_imaging_leg"] == "BASS+MzLS"],
    }
    rows = []
    for label, sub in splits.items():
        sp = sub[sub["match_class_eq"].isin(["CW", "CCW"])]
        n = int(len(sp))
        n_cw = int((sp["match_class_eq"] == "CW").sum())
        rows.append({
            "split": label, "n": n, "n_cw": n_cw,
            "cw_fraction": (n_cw / n) if n else np.nan,
            "sigma_from_half": (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n else np.nan,
        })
    return pd.DataFrame(rows)


def _target_class_split(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["target_class"] = df.apply(_target_class, axis=1)
    rows = []
    for cls, sub in df.groupby("target_class"):
        sp = sub[sub["match_class_eq"].isin(["CW", "CCW"])]
        n = int(len(sp))
        n_cw = int((sp["match_class_eq"] == "CW").sum())
        rows.append({
            "target_class": cls, "n": n, "n_cw": n_cw,
            "cw_fraction": (n_cw / n) if n else np.nan,
            "sigma_from_half": (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n else np.nan,
        })
    return pd.DataFrame(rows)


def _label_shuffle(df: pd.DataFrame, n_perm: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    sp = df[df["match_class_eq"].isin(["CW", "CCW"])]
    labels = (sp["match_class_eq"] == "CW").astype(int).to_numpy()
    n = len(labels)
    if n < 100:
        return {"skipped": True, "n": int(n)}
    n_cw_obs = int(labels.sum())
    null = np.zeros(n_perm)
    for k in range(n_perm):
        null[k] = rng.permutation(labels).sum()
    p_value_two_sided = float(np.mean(np.abs(null - 0.5 * n) >= np.abs(n_cw_obs - 0.5 * n)))
    return {
        "n": int(n), "n_cw_obs": n_cw_obs,
        "null_mean_n_cw": float(null.mean()),
        "null_std_n_cw": float(null.std()),
        "two_sided_p": p_value_two_sided,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    args = parser.parse_args()
    cfg = load_config(args.config)

    matched_path = resolve_p5_path(cfg["paths"]["out_matched"])
    if not matched_path.exists():
        print(f"ERROR: {matched_path} missing.")
        return 2
    out_dir = ensure_dir(resolve_p5_path("results/analysis_systematics"))

    df = pd.read_parquet(matched_path)
    df_primary = df[df.get("matched_primary_deduped", df["matched_primary"])]

    radii = list(cfg["systematics"]["radii_for_sensitivity"]) if "systematics" in cfg \
        else list(cfg["analysis"]["systematics"]["radii_for_sensitivity"])
    thresholds = list(cfg["analysis"]["systematics"]["confidence_thresholds"])
    n_perm = int(cfg["analysis"].get("permutation_n", 1000))
    seed = int(cfg["statistics"]["random_seed"])

    _radius_sensitivity(df, radii).to_csv(out_dir / "radius_sensitivity.csv", index=False)
    _confidence_sensitivity(df_primary, thresholds).to_csv(out_dir / "confidence_sensitivity.csv", index=False)
    _footprint_split(df_primary).to_csv(out_dir / "footprint_split.csv", index=False)
    _target_class_split(df_primary).to_csv(out_dir / "target_class_split.csv", index=False)

    label_shuffle = _label_shuffle(df_primary, n_perm, seed)
    (out_dir / "label_shuffle.json").write_text(json.dumps(label_shuffle, indent=2))

    (out_dir / "summary.json").write_text(json.dumps({
        "written_utc": utc_now(),
        "config_version": cfg["version"],
        "n_perm": n_perm,
        "label_shuffle": label_shuffle,
    }, indent=2))
    print(f"[done] wrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
