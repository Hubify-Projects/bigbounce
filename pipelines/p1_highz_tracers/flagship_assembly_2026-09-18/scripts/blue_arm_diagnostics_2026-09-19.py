#!/usr/bin/env python3
"""Within-catalogue instrumental-vs-astrophysical diagnostics for the blue-arm
result (Sec. V C / OT-3), run against already-released columns only -- no
network access, no new scan. Added in response to the R1 INT board (Claude
opus MAJOR-3/4/5; Grok AF-E1/E8; Gemini AF-E3), which found the paper's own
released columns already carry decisive evidence the manuscript did not use.

Outputs pipelines/p1_highz_tracers/anomaly_flagship_draft/outputs_blue_arm/
blue_arm_diagnostics.json, consumed by main.tex Sec. V C (vAF.0.4).
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


def r2(y: np.ndarray, X: np.ndarray) -> float:
    X1 = np.column_stack([np.ones(len(X)), X])
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

    # 1. worst_band census (which camera dominates the loss, per object)
    vc = df["worst_band"].value_counts()
    out["worst_band_census"] = {k: int(v) for k, v in vc.items()}
    out["worst_band_b_fraction"] = float(vc.get("B", 0) / len(df))

    # 2. variance decomposition: mean_mse ~ rB + rR + rZ
    y = df["mean_mse"].to_numpy(dtype=float)
    out["mean_mse_r2_full"] = r2(y, df[["rB", "rR", "rZ"]].to_numpy(dtype=float))
    out["mean_mse_r2_drop_rB"] = r2(y, df[["rR", "rZ"]].to_numpy(dtype=float))
    out["mean_mse_r2_drop_rR"] = r2(y, df[["rB", "rZ"]].to_numpy(dtype=float))
    out["mean_mse_r2_drop_rZ"] = r2(y, df[["rB", "rR"]].to_numpy(dtype=float))

    # 3. per-camera residual vs per-camera coadd S/N (tests the "noisier fibre
    #    reconstructs worse" instrumental reading directly)
    snr_corr = {}
    for band in ("B", "R", "Z"):
        r = stats.spearmanr(df[f"r{band}"], df[f"median_coadd_snr_{band.lower()}"])
        snr_corr[band] = {"rho": float(r.statistic), "p": float(r.pvalue), "n": int(len(df))}
    out["residual_vs_snr_spearman"] = snr_corr

    # 4. rest-frame vs observed-frame peak_residual_wavelength concentration,
    #    ZWARN=0 subset only (real, trusted pipeline redshift). A genuine
    #    rest-frame spectral feature should concentrate in the REST frame; a
    #    fixed-wavelength calibration/sky-subtraction artefact should
    #    concentrate in the OBSERVED frame.
    z0 = df[df["zwarn_real"] == 0].copy()
    obs = z0["peak_residual_wavelength"].to_numpy(dtype=float)
    rest = obs / (1 + z0["z_real"].to_numpy(dtype=float))
    out["restframe_test"] = {
        "n_zwarn0": int(len(z0)),
        "observed_median_A": float(np.median(obs)),
        "observed_iqr_over_median": float((np.percentile(obs, 75) - np.percentile(obs, 25)) / np.median(obs)),
        "restframe_median_A": float(np.median(rest)),
        "restframe_iqr_over_median": float((np.percentile(rest, 75) - np.percentile(rest, 25)) / np.median(rest)),
        "interpretation": (
            "observed-frame IQR/median < rest-frame IQR/median => the residual "
            "concentrates in the OBSERVED frame, not the rest frame -- favours "
            "a fixed-wavelength (instrumental/calibration) origin over a "
            "rest-frame spectral feature"
        ),
    }

    OUT.joinpath("blue_arm_diagnostics.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
