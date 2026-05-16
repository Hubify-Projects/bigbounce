#!/usr/bin/env python3
"""Analysis C — chirality vs cosmic-web environment.

Requires an environmental VAC (filament / void / cluster / wall labels per
DESI TARGETID). This script defines the join interface and runs the
chirality-by-environment test once the input is wired in.

Until the environment VAC is resolved, this script is a *contract*: it
writes a placeholder summary marking the blocker explicitly so downstream
plotting and the paper skeleton can reference a stable schema.

Expected input (when ready):
    data/desi_env/desi_env_<vac_name>.parquet
    Schema:
        TARGETID  : int64    (DESI TARGETID; foreign key)
        env_class : category {void, wall, filament, cluster}
        env_density : float  (optional auxiliary density estimator)
        vac_provenance : str
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

ENV_CLASSES = ["void", "wall", "filament", "cluster"]


def _env_join_table(matched: pd.DataFrame, env: pd.DataFrame) -> pd.DataFrame:
    df = matched.merge(env, left_on="desi_targetid", right_on="TARGETID", how="inner")
    sp = df[df["match_class_eq"].isin(["CW", "CCW"])]
    rows = []
    for cls, sub in sp.groupby("env_class"):
        n = len(sub)
        n_cw = int((sub["match_class_eq"] == "CW").sum())
        f = n_cw / n if n else np.nan
        sigma = (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n > 0 else np.nan
        rows.append({
            "env_class": str(cls),
            "n": int(n), "n_cw": n_cw, "n_ccw": int(n - n_cw),
            "cw_fraction": float(f),
            "sigma_from_half": float(sigma),
        })
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    parser.add_argument("--env", default=None,
                        help="Path to env VAC parquet (overrides default search).")
    args = parser.parse_args()
    cfg = load_config(args.config)

    matched_path = resolve_p5_path(cfg["paths"]["out_matched"])
    out_dir = ensure_dir(resolve_p5_path("results/analysis_cosmic_web"))

    env_dir = resolve_p5_path("data/desi_env")
    env_files = []
    if args.env:
        env_files = [Path(args.env)]
    elif env_dir.exists():
        env_files = sorted(env_dir.glob("desi_env_*.parquet"))

    if not env_files:
        blocker = {
            "status": "blocked",
            "blocker": "DESI environmental VAC missing",
            "expected_path": str(env_dir / "desi_env_<vac>.parquet"),
            "expected_schema": [
                {"col": "TARGETID", "dtype": "int64"},
                {"col": "env_class", "dtype": "category", "values": ENV_CLASSES},
                {"col": "env_density", "dtype": "float64", "optional": True},
                {"col": "vac_provenance", "dtype": "str"},
            ],
            "candidate_sources": [
                "DESI DR1 LSS VAC (BGS/LRG/ELG/QSO) — pending VAC release",
                "External void/filament catalogs (Bisigello et al. 2025; Tempel et al. 2018) — would need DESI ID resolution",
                "The '187 DESI-derived attributes' catalog mentioned by Houston — currently MISSING from repo, see reports/00_audit.md",
            ],
            "written_utc": utc_now(),
        }
        (out_dir / "summary.json").write_text(json.dumps(blocker, indent=2))
        print("[blocked] no env VAC found — wrote schema contract")
        return 0

    if not matched_path.exists():
        print(f"ERROR: matched catalog missing.")
        return 2

    matched = pd.read_parquet(matched_path)
    matched = matched[matched.get("matched_primary_deduped", matched["matched_primary"])]
    out_tables = []
    for ef in env_files:
        env = pd.read_parquet(ef)
        t = _env_join_table(matched, env)
        t["env_vac"] = ef.stem
        out_tables.append(t)
        t.to_csv(out_dir / f"cw_fraction_by_env__{ef.stem}.csv", index=False)
    full = pd.concat(out_tables, ignore_index=True)

    (out_dir / "summary.json").write_text(json.dumps({
        "written_utc": utc_now(),
        "config_version": cfg["version"],
        "env_vacs": [str(p.name) for p in env_files],
        "rows_total": int(len(full)),
    }, indent=2))
    print(f"[done] wrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
