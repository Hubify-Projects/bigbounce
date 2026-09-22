#!/usr/bin/env python3
"""Two independently-computed checks added in response to the 2026-09-22
exact-vAF.0.5 confirmation board (Grok AF-N2; Claude-opus AF-E3): (1) the
blue-arm camera's OWN univariate R^2 against mean_mse, distinct from the
already-committed full three-camera regression in
blue_arm_diagnostics_2026-09-19.py -- the summary locations (abstract, Sec I,
Sec XI) had conflated "dropping r_B collapses the full-model R^2 to 0.01"
with "r_B alone accounts for R^2=0.78", which is a different, previously
uncomputed number; (2) the Spearman correlation of anomaly score against
pipeline redshift for the ZWARN=0 subset, supporting the prose claim "no
visible trend of score with redshift" with a real statistic instead of a
visual read of Fig. 8.

Outputs pipelines/p1_highz_tracers/anomaly_flagship_draft/outputs_blue_arm/
confirm_round_2026-09-22.json, consumed by main.tex (vAF.0.6).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

PHASE3 = Path(__file__).resolve().parents[2] / "clean_rerun" / "results_2026-08-07" / "phase3_v2"
OUT = Path(__file__).resolve().parents[2] / "anomaly_flagship_draft" / "outputs_blue_arm"
OUT.mkdir(parents=True, exist_ok=True)


def r2_univariate(y: np.ndarray, x: np.ndarray) -> float:
    X1 = np.column_stack([np.ones(len(x)), x])
    beta, *_ = np.linalg.lstsq(X1, y, rcond=None)
    pred = X1 @ beta
    ss_res = ((y - pred) ** 2).sum()
    ss_tot = ((y - y.mean()) ** 2).sum()
    return float(1 - ss_res / ss_tot)


def main() -> None:
    base = pd.read_parquet(PHASE3 / "flagship_sample_v2.parquet")[["targetid", "zwarn", "z"]]
    base = base.rename(columns={"zwarn": "zwarn_real", "z": "z_real"})
    enr = pd.read_parquet(PHASE3 / "flagship_sample_v2_enriched.parquet")
    df = base.merge(enr, on="targetid", how="inner")
    assert len(df) == 1244, f"expected 1244 rows, got {len(df)}"

    out: dict = {}

    # 1. Blue-arm camera's own univariate R^2 (distinct from the full
    #    3-regressor R^2=0.777 already reported in Sec. V C).
    y = df["mean_mse"].to_numpy(dtype=float)
    out["mean_mse_r2_univariate_rB"] = r2_univariate(y, df["rB"].to_numpy(dtype=float))
    out["mean_mse_r2_univariate_rR"] = r2_univariate(y, df["rR"].to_numpy(dtype=float))
    out["mean_mse_r2_univariate_rZ"] = r2_univariate(y, df["rZ"].to_numpy(dtype=float))

    # 2. Score vs. redshift, ZWARN=0 subset (n should be 502, matching the
    #    same subset already used in Sec. V C's wavelength-concentration test).
    sub = df[df["zwarn_real"] == 0]
    out["n_zwarn0"] = int(len(sub))
    rho, p = stats.spearmanr(sub["anomaly_score"], sub["z_real"])
    out["score_vs_z_zwarn0_rho"] = float(rho)
    out["score_vs_z_zwarn0_p"] = float(p)

    path = OUT / "confirm_round_2026-09-22.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
