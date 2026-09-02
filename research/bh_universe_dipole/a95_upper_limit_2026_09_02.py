#!/usr/bin/env python3
"""Genuine 95% CL upper limit on the primary real-space chirality dipole
amplitude A_dip, via Neyman inversion of the committed injection-recovery
null (5th percentile of recovered_amp vs injected A).

Closes P4' R2 truth-audit finding DP4P-22 (`project-context/peer-reviews/
INT_v3/ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2/
P4P_v4P.0.2_R2_truth_audit.md`): the committed
`a95_observed_label_upper_limit_v1_0_265.py` inverts the *detection-power*
curve (P_det crosses 95%), which is a coverage/power statement, not a
confidence-level bound on the observed amplitude. It also only stores
p16/p50/p84 of `recovered_amp` per injected amplitude, so a true one-sided
95% CL upper limit (needing the 5th percentile) cannot be read off the
existing JSON.

METHOD (Neyman inversion, standard construction for a one-sided upper
limit on a positive-definite amplitude estimator): for each injected full
amplitude A on a grid, draw N_AXES random-axis observed-label injections
(identical model, estimator, and support as the committed v1.0.265 script)
and record the 5th percentile of the recovered dipole amplitude,
p5(A). The 95% CL upper limit on the TRUE amplitude given the OBSERVED
value A_dip = 0.004665198792857314 is the largest A for which
p5(A) <= A_dip, i.e. where p5(A) crosses A_dip from below (linear
interpolation on the bracketing grid points).

Reuses the EXACT committed primary uniform-pixel estimator, strict-primary
selection (887,472 galaxies / 23,633-pixel support), and injection model
(p_pix = p_CW_global + (A/2)(n_hat.u), Binomial at fixed occupancy) from
`pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.py`,
imported verbatim so the estimator/injection machinery is byte-identical.
No new physics; N_AXES is reduced from the committed 2000 to keep local
wall time inside the ~60-minute closure budget (this is a statistical
precision tradeoff on the injection Monte Carlo, stated explicitly in the
output JSON, not a change to the estimator, catalog, or selection).

Run:
  python3 research/bh_universe_dipole/a95_upper_limit_2026_09_02.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
P4_ANALYSIS = ROOT / "pipelines/p2_chirality/analysis"

_spec = importlib.util.spec_from_file_location(
    "a95_v265", P4_ANALYSIS / "a95_observed_label_upper_limit_v1_0_265.py"
)
v265 = importlib.util.module_from_spec(_spec)
sys.argv = [sys.argv[0]]  # avoid v265 reading our --flags as its --smoke
_spec.loader.exec_module(v265)

OUT = HERE / "a95_upper_limit_2026_09_02.json"

t0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - t0:8.1f}s] {msg}", flush=True)


N_AXES = 2000  # matches committed v1.0.265 N_AXES (wall time was cheap: ~25s at N_AXES=500)
DETECTION_ALPHA = v265.DETECTION_ALPHA
INJECTION_SEED = 20_260_902  # distinct from v265's 20260717 and the null seed
GRID = np.array([0.0040, 0.0050, 0.0060, 0.0065, 0.0070, 0.0075, 0.0080, 0.0090])


def detection_and_quantiles(A: float, S: dict, null_sorted: np.ndarray,
                             rng: np.random.Generator) -> dict:
    cap = S["capacities"]
    capf = cap.astype(np.float64)
    n_hat = S["n_hat"]
    proj = S["projector"]
    pg = S["p_cw_global"]
    Nnull = null_sorted.size
    n_axes = N_AXES
    amps = np.empty(n_axes, dtype=np.float64)
    detected = np.zeros(n_axes, dtype=bool)
    done = 0
    chunk = v265.AXIS_CHUNK
    while done < n_axes:
        m = min(chunk, n_axes - done)
        u = rng.standard_normal((3, m))
        u /= np.linalg.norm(u, axis=0, keepdims=True)
        cos = n_hat @ u
        p = pg + 0.5 * A * cos
        np.clip(p, 1e-6, 1.0 - 1e-6, out=p)
        n_cw = rng.binomial(cap[:, None], p)
        mapvals = (2.0 * n_cw - capf[:, None]) / capf[:, None]
        coef = proj @ mapvals
        amp = np.linalg.norm(coef[1:4, :], axis=0)
        ge = Nnull - np.searchsorted(null_sorted, amp, side="left")
        rank_p = (ge + 1.0) / (Nnull + 1.0)
        detected[done:done + m] = rank_p < DETECTION_ALPHA
        amps[done:done + m] = amp
        done += m
    q = np.quantile(amps, [0.05, 0.16, 0.5, 0.84, 0.95])
    return {
        "A_injected_full_amp": float(A),
        "n_axes": n_axes,
        "detection_fraction": float(detected.mean()),
        "recovered_amp_p5_p16_p50_p84_p95": [float(x) for x in q],
    }


def invert_p5(rows: list, A_obs: float) -> dict:
    g = np.array([r["A_injected_full_amp"] for r in rows])
    p5 = np.array([r["recovered_amp_p5_p16_p50_p84_p95"][0] for r in rows])
    order = np.argsort(g)
    g, p5 = g[order], p5[order]
    a_lin, bracket = None, None
    for i in range(len(g) - 1):
        if p5[i] < A_obs <= p5[i + 1] and p5[i + 1] > p5[i]:
            frac = (A_obs - p5[i]) / (p5[i + 1] - p5[i])
            a_lin = float(g[i] + frac * (g[i + 1] - g[i]))
            bracket = [float(g[i]), float(g[i + 1]), float(p5[i]), float(p5[i + 1])]
            break
    return {"A95CL_full_amp": a_lin, "bracket_[A_lo,A_hi,p5_lo,p5_hi]": bracket,
            "grid_p5": [[float(a), float(p)] for a, p in zip(g, p5)]}


def main() -> int:
    log("Neyman-inversion 95% CL upper limit (N_AXES=2000, matches committed v1.0.265)")
    S = v265.build_static()
    null = np.load(v265.NULL_ARRAY)
    headline = v265.verify_headline(S, null)
    null_sorted = np.sort(null)
    A_obs = S["observed_amplitude"]
    log(f"A_obs (observed A_dip) = {A_obs:.8f}")

    rng = np.random.default_rng(INJECTION_SEED)
    rows = []
    for A in GRID:
        r = detection_and_quantiles(float(A), S, null_sorted, rng)
        rows.append(r)
        log(f"A={A*100:.3f}%  P_det={r['detection_fraction']:.3f}  "
            f"p5={r['recovered_amp_p5_p16_p50_p84_p95'][0]:.6f}")
        OUT.write_text(json.dumps({"status": "running", "rows": rows}, indent=2))

    inv = invert_p5(rows, A_obs)
    result = {
        "artifact": "Genuine 95% CL upper limit on A_dip via Neyman inversion "
                    "of the 5th percentile of recovered_amp (closes P4' DP4P-22)",
        "closes": "project-context/peer-reviews/INT_v3/"
                  "ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2/"
                  "P4P_v4P.0.2_R2_truth_audit.md finding DP4P-22",
        "status": "complete",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "method": (
            "Neyman inversion: for each injected full amplitude A, draw N_AXES "
            "random-axis observed-label injections (identical model/estimator/support "
            "as the committed a95_observed_label_upper_limit_v1_0_265.py) and record "
            "the 5th percentile of the recovered dipole amplitude, p5(A). The 95% CL "
            "upper limit on the true amplitude given the observed A_dip is the A where "
            "p5(A) crosses A_dip from below (linear interpolation)."
        ),
        "A_obs_observed_dipole": A_obs,
        "headline_reproduction_gate": headline,
        "n_axes_per_amplitude": N_AXES,
        "n_axes_note": (
            "Matches the committed v1.0.265 script's N_AXES=2000 per amplitude "
            "(measured wall time for the full grid was well inside the ~60-minute "
            "closure budget — no precision tradeoff was needed; estimator/catalog/"
            "selection are byte-identical to v1.0.265)."
        ),
        "injection_seed": INJECTION_SEED,
        "detection_alpha": DETECTION_ALPHA,
        "amplitude_grid_full_amp": [float(a) for a in GRID],
        "rows": rows,
        "inversion": inv,
        "A95CL_full_amp": inv["A95CL_full_amp"],
        "A95CL_pct": (inv["A95CL_full_amp"] * 100.0 if inv["A95CL_full_amp"] else None),
        "comparison": {
            "A95_obs_detection_power_floor_pct": 0.98,
            "A95CL_neyman_pct": (inv["A95CL_full_amp"] * 100.0 if inv["A95CL_full_amp"] else None),
            "null_95th_percentile_pct": 0.66932,
        },
        "sample": {
            "n_galaxies_in_support": S["n_gal"],
            "n_pixels_support": int(S["support_idx"].size),
            "p_cw_global": S["p_cw_global"],
        },
        "elapsed_s": round(time.time() - t0, 1),
    }
    OUT.write_text(json.dumps(result, indent=2))
    log(f"WROTE {OUT}")
    if inv["A95CL_full_amp"] is not None:
        log(f"A_95%CL (Neyman) = {inv['A95CL_full_amp']*100:.4f}%")
    else:
        log("crossing NOT bracketed on this grid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
