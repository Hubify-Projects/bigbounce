"""Wave 14-KKKK: high-confidence (Gold+Silver) restricted alpha re-measurement.

Closes R44-M5 Path B for P3. The 5,384 QSO_CANDIDATE sample is photometrically
selected (W1-W2 > 0.8 Stern+2012 cut applied at the candidate-selection stage,
median W1-W2 = 1.005); per-object spectroscopic redshifts are not available
for the full sample. The R44 reviewer flagged that the science-relevant
high-z regime for SPHEREx multi-tracer is z > 0.8, where the angular
two-point measurement at <z> of the 5,384 sample is an effective bias
enhancement averaged over a heterogeneous redshift distribution rather than
a measurement at the science regime.

The proper Path-B operationalization is therefore not a redshift cut on the
5,384 (since per-object z is unavailable), but a high-confidence cut: the
1,122-object Gold+Silver subset is the high-confidence end of the QSO
candidate distribution, and Wave 14-VVV's point-estimate result already
shows it is more strongly clustered (b_GS/b_full = 3.17 geomean over three
signal bins) than the full QSO-candidate sample. What was missing was the
jackknife covariance for the Gold+Silver target, which is what this wave
computes.

Output: pipelines/p1_highz_tracers/outputs/step6_alpha_empirical/
        alpha_highconfidence_results.json
"""

from __future__ import annotations
import json
import sys
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wave_14_vvv_alpha_empirical import (  # type: ignore
    radec_to_xyz,
    correlate_sample,
    make_anomaly_window_randoms,
    assign_jackknife_regions,
    bias_ratio_at_large_scales,
    jackknife_bias_ratio,
    THETA_EDGES_DEG,
    THETA_CENTERS_DEG,
    THETA_SIGNAL_MIN_DEG,
    THETA_SIGNAL_MAX_DEG,
    N_RANDOMS_MULTIPLIER,
    N_JACKKNIFE_REGIONS,
    SEED,
    SIGMA_FNL_BASELINE,
    ALPHA_FIDUCIAL_PAPER,
    IMPROVEMENT_AT_FIDUCIAL,
    LOCAL_INPUT,
    LOCAL_OUTPUT,
)


def main() -> None:
    print(f"[Wave 14-KKKK] Loading {LOCAL_INPUT}")
    df = pd.read_parquet(LOCAL_INPUT)
    full = df.dropna(subset=["ra", "dec"]).copy()
    print(f"  full anomaly: n = {len(full)}")

    qso_with_conf = full[full.get("classification", pd.Series([], dtype=str)) == "QSO_CANDIDATE"].copy()
    if "qso_confidence" not in qso_with_conf.columns:
        sys.exit("qso_confidence column missing -- cannot subset Gold+Silver")
    gs_mask = qso_with_conf["qso_confidence"].isin(["GOLD", "SILVER"])
    gs = qso_with_conf[gs_mask].copy()
    print(f"  Gold+Silver target: n = {len(gs)} "
          f"({(qso_with_conf['qso_confidence'] == 'GOLD').sum()} GOLD + "
          f"{(qso_with_conf['qso_confidence'] == 'SILVER').sum()} SILVER)")

    ra_full = full["ra"].to_numpy(dtype=np.float64)
    dec_full = full["dec"].to_numpy(dtype=np.float64)
    ra_gs = gs["ra"].to_numpy(dtype=np.float64)
    dec_gs = gs["dec"].to_numpy(dtype=np.float64)

    n_random = N_RANDOMS_MULTIPLIER * len(gs)
    print(f"[Wave 14-KKKK] Generating {n_random} anomaly-window-matched randoms")
    ra_r, dec_r = make_anomaly_window_randoms(ra_full, dec_full, n_random, SEED)

    regions_full = assign_jackknife_regions(ra_full, dec_full, N_JACKKNIFE_REGIONS, SEED)
    regions_gs = assign_jackknife_regions(ra_gs, dec_gs, N_JACKKNIFE_REGIONS, SEED + 1)
    regions_r = assign_jackknife_regions(ra_r, dec_r, N_JACKKNIFE_REGIONS, SEED + 7)

    print(f"[Wave 14-KKKK] Correlating Gold+Silver target")
    w_gs = correlate_sample(ra_gs, dec_gs, ra_r, dec_r, THETA_EDGES_DEG,
                            log_prefix="[GS]")
    print(f"[Wave 14-KKKK] Correlating full anomaly reference")
    w_full = correlate_sample(ra_full, dec_full, ra_r, dec_r, THETA_EDGES_DEG,
                              log_prefix="[full]")

    point_ratio = bias_ratio_at_large_scales(
        np.asarray(w_gs["w_theta"]),
        np.asarray(w_full["w_theta"]),
        THETA_CENTERS_DEG,
        THETA_SIGNAL_MIN_DEG,
        THETA_SIGNAL_MAX_DEG,
    )

    print(f"[Wave 14-KKKK] Running 30-region jackknife on bias ratio (GS-vs-full)")
    jk = jackknife_bias_ratio(
        ra_gs, dec_gs,
        ra_full, dec_full,
        ra_r, dec_r,
        regions_gs, regions_full, regions_r,
        THETA_EDGES_DEG, THETA_CENTERS_DEG,
        THETA_SIGNAL_MIN_DEG, THETA_SIGNAL_MAX_DEG,
        N_JACKKNIFE_REGIONS,
        log_prefix="[GS-jk]",
    )

    alpha_gs_jk = jk["alpha_internal"]
    alpha_gs_jk_std = jk["alpha_internal_std"]
    sigma_fnl_jk = SIGMA_FNL_BASELINE * (
        1.0 - (IMPROVEMENT_AT_FIDUCIAL / ALPHA_FIDUCIAL_PAPER) * alpha_gs_jk
    )
    sigma_fnl_jk_std = SIGMA_FNL_BASELINE * (
        IMPROVEMENT_AT_FIDUCIAL / ALPHA_FIDUCIAL_PAPER
    ) * alpha_gs_jk_std

    out = {
        "metadata": {
            "wave": "14-KKKK",
            "purpose": "High-confidence (Gold+Silver) restricted alpha re-measurement; closes R44-M5 Path B",
            "input_file": str(LOCAL_INPUT),
            "n_target_gs": int(len(gs)),
            "n_target_gold": int((qso_with_conf["qso_confidence"] == "GOLD").sum()),
            "n_target_silver": int((qso_with_conf["qso_confidence"] == "SILVER").sum()),
            "n_full_anomaly": int(len(full)),
            "n_random": int(n_random),
            "n_jackknife_regions": N_JACKKNIFE_REGIONS,
            "sigma_fnl_baseline": SIGMA_FNL_BASELINE,
            "alpha_fiducial_paper": ALPHA_FIDUCIAL_PAPER,
            "improvement_at_fiducial": IMPROVEMENT_AT_FIDUCIAL,
            "completed_at": datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
        },
        "point_estimate_gs_vs_full_signal": point_ratio,
        "jackknife_bias_ratio_gs_vs_full": jk,
        "alpha_gs_jk": alpha_gs_jk,
        "alpha_gs_jk_std": alpha_gs_jk_std,
        "sigma_fnl_gs_jk": sigma_fnl_jk,
        "sigma_fnl_gs_jk_std": sigma_fnl_jk_std,
    }

    out_path = LOCAL_OUTPUT / "alpha_highconfidence_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=lambda o: float(o) if hasattr(o, "__float__") else str(o)))
    print(f"[Wave 14-KKKK] DONE")
    print(f"  alpha_GS_jk = {alpha_gs_jk:+.4f} +/- {alpha_gs_jk_std:.4f} (1-sigma jackknife)")
    print(f"  sigma_fNL_GS_jk = {sigma_fnl_jk:.3f} +/- {sigma_fnl_jk_std:.3f}")
    print(f"  output: {out_path}")


if __name__ == "__main__":
    main()
