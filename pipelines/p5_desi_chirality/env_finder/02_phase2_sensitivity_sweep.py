#!/usr/bin/env python3
"""P5 env_finder Phase 2 sensitivity sweep.

Runs the V-Web Phase 1 pipeline across a grid of (R_s, N_grid, lambda_th)
configurations, joins each output with the matched chirality catalog, and
aggregates cw_fraction per environment class per config into a single CSV.

Per Houston 2026-05-21 drive-to-100 directive: this addresses
FINAL_TASK_LISTS.md P5 row 1 (Phase 2 sensitivity sweep).

Sweep grid (9 cells, ~16 min wall):
    R_s_mpc_h  ∈ {10, 25, 50}
    N_grid     ∈ {256}            (128 too coarse for 6 Gpc/h box; 512 OOM on 32GB)
    lambda_th  ∈ {0.0, 0.1, 0.3}

For each cell:
    1. Render config YAML to a temp directory with the cell parameters.
    2. Invoke 01_compute_vweb.py via subprocess with the temp config.
    3. Join the resulting env parquet with the matched chirality catalog.
    4. Compute per-env-class cw_fraction + sigma_from_half + n.
    5. Append a row per env class to the master CSV.

Output:
    pipelines/p5_desi_chirality/env_finder/reports/02_phase2_sweep.csv
    pipelines/p5_desi_chirality/env_finder/reports/02_phase2_sweep_summary.json
"""
from __future__ import annotations

import itertools
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
P5 = REPO / "pipelines/p5_desi_chirality"
ENV_FINDER = P5 / "env_finder"
SCRIPT = ENV_FINDER / "01_compute_vweb.py"
BASE_CONFIG = ENV_FINDER / "config.yaml"
SWEEP_DIR = P5 / "data/desi_env/phase2_sweep"
REPORTS = ENV_FINDER / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)
SWEEP_DIR.mkdir(parents=True, exist_ok=True)

# Matched chirality × DESI catalog (built in Phase 1 bootstrap)
MATCHED_PARQUET = P5 / "results/p5_matched_chirality_desi.parquet"

# Sweep axes
SWEEP_R_S = [10.0, 25.0, 50.0]
SWEEP_N_GRID = [256]
SWEEP_LAMBDA = [0.0, 0.1, 0.3]
ENV_CLASSES = ["void", "wall", "filament", "cluster"]


def _utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _load_base_config() -> dict:
    with BASE_CONFIG.open() as f:
        return yaml.safe_load(f)


def _render_cell_config(base: dict, r_s: float, n_grid: int, lambda_th: float, out_parquet: Path) -> Path:
    cfg = json.loads(json.dumps(base))
    cfg["smoothing"]["R_s_mpc_h"] = r_s
    cfg["grid"]["n"] = n_grid
    cfg["classify"]["lambda_th"] = lambda_th
    cfg["output"]["env_parquet"] = str(out_parquet.relative_to(REPO))
    cfg["output"]["volume_fractions_json"] = (
        f"pipelines/p5_desi_chirality/env_finder/reports/02_phase2_volfrac_R{r_s:g}_N{n_grid}_L{lambda_th:g}.json"
    )
    cfg_path = out_parquet.with_suffix(".cfg.yaml")
    with cfg_path.open("w") as f:
        yaml.safe_dump(cfg, f)
    return cfg_path


def _run_cell(cfg_path: Path) -> tuple[bool, str]:
    t0 = time.time()
    cmd = [sys.executable, str(SCRIPT), "--config", str(cfg_path)]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO), timeout=1800)
        wall = time.time() - t0
        ok = out.returncode == 0
        msg = f"rc={out.returncode} wall={wall:.1f}s"
        if not ok:
            msg += f" stderr-tail={out.stderr[-400:]}"
        return ok, msg
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT > 30min"


def _join_and_summarize(env_parquet: Path, label: str) -> pd.DataFrame | None:
    if not env_parquet.exists():
        return None
    if not MATCHED_PARQUET.exists():
        print(f"  SKIP join — matched catalog missing at {MATCHED_PARQUET}")
        return None
    env = pd.read_parquet(env_parquet)
    matched = pd.read_parquet(MATCHED_PARQUET)
    df = matched.merge(env[["TARGETID", "env_class"]], left_on="desi_targetid", right_on="TARGETID", how="inner")
    sp = df[df["match_class_eq"].isin(["CW", "CCW"])]
    rows = []
    for cls in ENV_CLASSES:
        sub = sp[sp["env_class"].astype(str) == cls]
        n = len(sub)
        n_cw = int((sub["match_class_eq"] == "CW").sum())
        f = n_cw / n if n else np.nan
        sigma = (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n > 0 else np.nan
        rows.append({
            "cell": label, "env_class": cls, "n": n, "n_cw": n_cw,
            "cw_fraction": float(f) if n else np.nan,
            "sigma_from_half": float(sigma) if n else np.nan,
        })
    return pd.DataFrame(rows)


def main() -> int:
    base = _load_base_config()
    sweep_rows = []
    run_log = []
    combos = list(itertools.product(SWEEP_R_S, SWEEP_N_GRID, SWEEP_LAMBDA))
    print(f"P5 Phase 2 sweep: {len(combos)} cells starting at {_utc()}")
    t_total = time.time()
    for r_s, n_grid, lambda_th in combos:
        label = f"R{r_s:g}_N{n_grid}_L{lambda_th:g}"
        out_parquet = SWEEP_DIR / f"desi_env_vweb_{label}.parquet"
        cfg_path = _render_cell_config(base, r_s, n_grid, lambda_th, out_parquet)
        print(f"\n[{_utc()}] cell {label} — running")
        ok, msg = _run_cell(cfg_path)
        print(f"  -> {msg}")
        run_log.append({"cell": label, "ok": ok, "msg": msg})
        if not ok:
            continue
        per_env = _join_and_summarize(out_parquet, label)
        if per_env is not None:
            for _, row in per_env.iterrows():
                d = row.to_dict()
                d["R_s_mpc_h"] = r_s
                d["N_grid"] = n_grid
                d["lambda_th"] = lambda_th
                sweep_rows.append(d)
    wall_total = time.time() - t_total
    df = pd.DataFrame(sweep_rows)
    out_csv = REPORTS / "02_phase2_sweep.csv"
    df.to_csv(out_csv, index=False)
    summary = {
        "sweep": {"R_s_mpc_h": SWEEP_R_S, "N_grid": SWEEP_N_GRID, "lambda_th": SWEEP_LAMBDA},
        "n_cells": len(combos),
        "n_cells_ok": sum(1 for r in run_log if r["ok"]),
        "wall_seconds_total": round(wall_total, 1),
        "headline": {
            "max_abs_sigma_across_sweep": float(df["sigma_from_half"].abs().max()) if len(df) else None,
            "cw_fraction_range_within_each_cell": (
                df.groupby("cell")["cw_fraction"].agg(lambda x: float(x.max() - x.min())).to_dict()
                if len(df) else None
            ),
        },
        "run_log": run_log,
        "generated_at_utc": _utc(),
    }
    out_json = REPORTS / "02_phase2_sweep_summary.json"
    out_json.write_text(json.dumps(summary, indent=2))
    print(f"\nDone. {summary['n_cells_ok']}/{summary['n_cells']} cells OK in {wall_total:.0f}s.")
    print(f"  CSV: {out_csv.relative_to(REPO)}")
    print(f"  JSON: {out_json.relative_to(REPO)}")
    return 0 if summary["n_cells_ok"] == summary["n_cells"] else 1


if __name__ == "__main__":
    sys.exit(main())
