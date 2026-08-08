#!/usr/bin/env python3
"""
EMPIRICAL edge-on contamination metric for Appendix E.

Replaces the qualitative "5-8% sensitivity penalty" bound (previously flagged
as "qualitative pending the axis-ratio cross-match") with the REAL measured
axis-ratio distribution of the classified spiral catalog.

INPUT
  outputs/spiral_morphology_dr8.parquet
    - one row per equivariant-classified spiral (N = 3,201,160), i.e. every
      galaxy that received a CW/CCW label (NOT the NS class).
    - cols: BRICKID, OBJID, TYPE, FRACDEV, SHAPEDEV_R/E1/E2, SHAPEEXP_R/E1/E2

b/a convention (identical to scripts/systematic_l1_forward_model_dr8morph.py):
    |e|  = hypot(e1,e2), clipped to [0,0.999]
    b/a  = (1-|e|)/(1+|e|)
    use DEV shape when TYPE in {DEV,COMP,SER} or FRACDEV>=0.5, else EXP shape.

METRIC
  f_edge  = fraction of the CLASSIFIED-SPIRAL catalog with b/a < 0.3
            (empirical replacement for the pending compute item).
  From Appendix E the sensitivity dilution has TWO framings (M24/DP4-22 fix,
  2026-07-13):
     Fisher-optimal (Cramer-Rao) floor: (1-delta)^{-1/2} - 1  ~ delta/2
        -- applies ONLY to an estimator that identifies + down-weights/excludes
           the zero-Fisher-information edge-on population.
     Naive-estimator linear penalty: (1-delta)^{-1} - 1  ~ delta
        -- applies to the NAIVE per-pixel f_CW estimator ACTUALLY USED, which
           RETAINS the edge-on systems in N_spiral. Flip-symmetric edge-on
           contaminants carry zero mean CW-CCW asymmetry, so they split 50/50
           under hard argmax and dilute the recovered amplitude LINEARLY:
           E[A_p] = (1-delta) A_phys  =>  physical-amplitude floor inflates by
           (1-delta)^{-1} - 1. The paper ADOPTS the larger conservative linear
           value; neither changes the null verdict (injection-recovery floors
           measured on the same edge-on-contaminated observed field).
  We report f_edge at b/a<0.3 (paper's edge-on definition) plus a sweep
  (b/a<0.2, 0.25, 0.3, 0.35, 0.4) so the number is robust to the threshold.

NEVER FABRICATED — every number computed from the parquet on disk.
"""
import json, hashlib, subprocess
from datetime import datetime, timezone
import numpy as np
import pandas as pd
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT  = HERE.parent / "outputs"
MORPH = OUT / "spiral_morphology_dr8.parquet"
RESULT = OUT / "edge_on_contamination_metric.json"


def ba_from(e1, e2):
    e = np.sqrt(np.asarray(e1, float) ** 2 + np.asarray(e2, float) ** 2)
    e = np.clip(e, 0, 0.999)
    return (1.0 - e) / (1.0 + e)


def main():
    m = pd.read_parquet(MORPH)
    n_total = len(m)
    typ = m["TYPE"].astype(str).str.upper().values
    dev_like = np.isin(typ, ["DEV", "COMP", "SER"]) | (m["FRACDEV"].values >= 0.5)
    ba_dev = ba_from(m["SHAPEDEV_E1"], m["SHAPEDEV_E2"])
    ba_exp = ba_from(m["SHAPEEXP_E1"], m["SHAPEEXP_E2"])
    ba = np.where(dev_like, ba_dev, ba_exp).astype(np.float64)

    finite = np.isfinite(ba)
    n_finite = int(finite.sum())
    ba_f = ba[finite]

    thresholds = [0.20, 0.25, 0.30, 0.35, 0.40]
    sweep = {}
    for t in thresholds:
        n_edge = int((ba_f < t).sum())
        f_edge = n_edge / n_finite
        # Fisher-optimal (Cramer-Rao) floor for a delta=f_edge dilution of N_eff
        floor_inflation_fisher = (1.0 - f_edge) ** -0.5 - 1.0
        # Naive-estimator linear penalty (DP4-22): the primary per-pixel f_CW
        # estimator RETAINS edge-on in N_spiral => linear (1-delta)^-1 dilution.
        penalty_linear = (1.0 - f_edge) ** -1.0 - 1.0
        sweep[f"b_over_a_lt_{t:.2f}"] = {
            "n_edge": n_edge,
            "f_edge": f_edge,
            "f_edge_pct": 100.0 * f_edge,
            "neff_dilution_pct": 100.0 * f_edge,
            "sensitivity_floor_inflation_fisher_pct": 100.0 * floor_inflation_fisher,
            "physical_amplitude_penalty_linear_pct": 100.0 * penalty_linear,
        }

    primary = sweep["b_over_a_lt_0.30"]

    # b/a distribution summary (percentiles) for the record
    pctls = {f"p{p}": float(np.percentile(ba_f, p)) for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]}

    try:
        head = subprocess.check_output(["git", "-C", str(HERE), "rev-parse", "HEAD"]).decode().strip()
    except Exception:
        head = None

    result = {
        "script": "scripts/edge_on_contamination_metric.py",
        "date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "git_head": head,
        "purpose": (
            "EMPIRICAL edge-on contamination metric replacing the qualitative "
            "5-8% sensitivity-penalty bound in Appendix E. Measures the axis-ratio "
            "(b/a) distribution of the classified-spiral catalog directly."),
        "input": {
            "file": "outputs/spiral_morphology_dr8.parquet",
            "n_classified_spirals": n_total,
            "n_with_finite_ba": n_finite,
            "ba_convention": "b/a=(1-|e|)/(1+|e|), |e|=hypot(e1,e2) clip[0,0.999]; DEV shape if TYPE in {DEV,COMP,SER} or FRACDEV>=0.5 else EXP",
        },
        "ba_distribution_percentiles": pctls,
        "edge_on_fraction_sweep": sweep,
        "primary": {
            "definition": "edge-on := b/a < 0.30 (paper Appendix E convention)",
            "f_edge": primary["f_edge"],
            "f_edge_pct": primary["f_edge_pct"],
            "n_edge_on_spirals": primary["n_edge"],
            "neff_dilution_pct": primary["neff_dilution_pct"],
            "sensitivity_floor_inflation_pct": primary["sensitivity_floor_inflation_fisher_pct"],
            "note": (
                "f_edge is the fraction of the CLASSIFIED-SPIRAL catalog (galaxies "
                "assigned CW/CCW) that are edge-on by b/a<0.3. Because equivariant TTA "
                "forces <p_CW>=<p_CCW> for flip-symmetric edge-on morphologies, this "
                "contamination is a pure sensitivity dilution (N_eff loss), not a "
                "directional bias on the l=1 dipole (see Appendix E equivariance argument). "
                "The empirical floor inflation supersedes the prior qualitative 5-8% estimate."),
        },
        "fabrication_disclaimer": "Every number computed from spiral_morphology_dr8.parquet on disk. No values fabricated.",
        "penalty_note": (
            "Correction (M24, 2026-07-13): the primary dipole uses the NAIVE per-pixel f_CW "
            "estimator with edge-on systems RETAINED in N_spiral. Flip-symmetric edge-on "
            "contaminants carry zero mean asymmetry and dilute the recovered amplitude LINEARLY "
            "(E[A_p]=(1-delta)A_phys), so the physical-amplitude sensitivity-floor penalty is "
            "(1-delta)^-1 - 1, NOT the Fisher-optimal (1-delta)^-1/2 - 1. The sqrt value is the "
            "Cramer-Rao bound for an optimal estimator that excludes/down-weights the "
            "zero-information edge-on population; the naive estimator incurs the full linear "
            "dilution. Paper adopts the conservative linear value. Neither changes the null "
            "verdict (injection-recovery floors are measured on the same contaminated observed "
            "field); largely subsumed by the primary g=2a-1 GZ1-accuracy dilution."),
    }

    RESULT.write_text(json.dumps(result, indent=2))
    md5 = hashlib.md5(RESULT.read_bytes()).hexdigest()
    print(f"n_classified_spirals = {n_total:,}  (finite b/a: {n_finite:,})")
    print(f"PRIMARY  f_edge(b/a<0.30) = {primary['f_edge_pct']:.3f}%  "
          f"({primary['n_edge']:,} edge-on spirals)")
    print(f"         N_eff dilution   = {primary['neff_dilution_pct']:.3f}%")
    print(f"         Fisher floor infl= {primary['sensitivity_floor_inflation_fisher_pct']:.3f}%")
    print(f"         LINEAR penalty   = {primary['physical_amplitude_penalty_linear_pct']:.3f}%  (adopted, DP4-22)")
    print("SWEEP:")
    for k, v in sweep.items():
        print(f"  {k}: f_edge={v['f_edge_pct']:.3f}%  fisher={v['sensitivity_floor_inflation_fisher_pct']:.3f}%  linear={v['physical_amplitude_penalty_linear_pct']:.3f}%")
    print(f"wrote {RESULT}  md5={md5}")


if __name__ == "__main__":
    main()
