#!/usr/bin/env python3
"""
Verify P4 canonical numbers + emit reproducible-provenance JSON artifacts.

Closes the on-record DeepSeek-B1 / DeepSeek-M3 deferrals from the
2026-05-14 real-cross-vendor R-round on P4 v1.0.51 (OpenRouter).

Inputs (canonical on-disk source of truth):
    pipelines/p2_chirality/r42_results/wave_14_oo_bin_flatness.json
        — produced by the wave-14-OO bin-flatness sweep on Pod 3 H200,
        2026-04-29 (29.3s wall, full-spiral n=3,201,160 + high-confidence
        n=949,584). Contains canonical N_input, N_CW, N_CCW, and
        catalog-wide CW fraction for both denominator tiers.

Outputs:
    pipelines/p2_chirality/outputs/canonical_provenance/
        global_cw_fraction.json
            — exact N_CW, N_CCW, N_spiral, computed p, sigma_binomial,
            and the n-sigma deviation from parity, with the formula and
            source-of-truth file referenced inline.
        spiral_count_verification.json
            — verification that the N_spiral = 3,201,160 figure used as
            the canonical denominator across abstract / Sec. V / Table II
            is consistent across all wave-14 result files that report it.

Run:
    python3 pipelines/p2_chirality/scripts/verify_canonical_numbers.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
P4 = REPO / "pipelines" / "p2_chirality"
R42 = P4 / "r42_results"
OUT = P4 / "outputs" / "canonical_provenance"

WAVE_14_OO = R42 / "wave_14_oo_bin_flatness.json"


def compute_global_cw() -> dict:
    """Read canonical numbers from wave_14_oo_bin_flatness.json and emit the
    exact global-CW-fraction provenance JSON."""
    d = json.load(WAVE_14_OO.open())
    full = d["denominators"]["full_spiral"]
    n_cw = full["n_cw"]
    n_ccw = full["n_ccw"]
    n_input = full["n_input"]
    p = n_cw / (n_cw + n_ccw)
    sigma = math.sqrt(p * (1 - p) / (n_cw + n_ccw))
    n_sigma = (0.5 - p) / sigma  # signed (negative = CCW-leaning)

    return {
        "source_of_truth": str(WAVE_14_OO.relative_to(REPO)),
        "tier": "full_spiral (Catalog C canonical)",
        "N_CW": n_cw,
        "N_CCW": n_ccw,
        "N_spiral": n_cw + n_ccw,
        "N_input_self_consistency_check": n_input == (n_cw + n_ccw),
        "p_CW": p,
        "sigma_binomial": sigma,
        "deviation_from_parity_sigma": n_sigma,
        "interpretation": (
            "p_CW = N_CW / (N_CW + N_CCW); sigma_binomial = "
            "sqrt(p * (1 - p) / (N_CW + N_CCW)); the deviation is "
            "(0.5 - p) / sigma_binomial. The sign is positive when the "
            "catalog is CW-deficit (CCW-leaning); the canonical Catalog C "
            "deviation is positive, i.e. ~9.5 sigma in the CCW-leaning "
            "direction (equivalently a 0.26 percent CW deficit)."
        ),
        "rounded_for_paper": {
            "p_CW_4sig": round(p, 4),
            "sigma_binomial_6sig": float(f"{sigma:.4e}"),
            "deviation_1sig": float(f"{n_sigma:.2f}"),
        },
    }


def verify_n_spiral_consistency() -> dict:
    """Cross-check that N_spiral = 3,201,160 is consistent across all
    wave-14 result files that report it."""
    targets = [
        ("wave_14_oo_bin_flatness.json", ["denominators", "full_spiral", "n_input"]),
        ("wave_14_qq_systematics_regression.json", ["n_spirals_used"]),
        ("wave_14_pp_namaster_verification.json", ["n_spiral"]),
        ("wave_14_jj_psf_xcorr_results.json", ["n_spirals"]),
    ]
    report = {}
    canonical = 3_201_160
    for fname, path in targets:
        fpath = R42 / fname
        if not fpath.exists():
            report[fname] = {"status": "missing"}
            continue
        d = json.load(fpath.open())
        cur = d
        try:
            for k in path:
                cur = cur[k]
            report[fname] = {
                "value": cur,
                "matches_canonical": cur == canonical,
                "path": ".".join(path),
            }
        except (KeyError, TypeError) as e:
            report[fname] = {"status": f"path-error: {e}", "path": ".".join(path)}
    return {
        "canonical_N_spiral": canonical,
        "all_match": all(r.get("matches_canonical", False) for r in report.values()),
        "per_file": report,
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    g = compute_global_cw()
    s = verify_n_spiral_consistency()

    json.dump(g, (OUT / "global_cw_fraction.json").open("w"), indent=2)
    json.dump(s, (OUT / "spiral_count_verification.json").open("w"), indent=2)

    print("[canonical-verify] N_spiral = N_CW + N_CCW =",
          g["N_CW"], "+", g["N_CCW"], "=", g["N_spiral"])
    print("[canonical-verify] N_spiral consistency across 4 wave-14 files:",
          "PASS" if s["all_match"] else "FAIL")
    print("[canonical-verify] p_CW =", g["p_CW"])
    print("[canonical-verify] sigma_binomial =", g["sigma_binomial"])
    print("[canonical-verify] deviation =", g["deviation_from_parity_sigma"], "sigma")
    print("[canonical-verify] wrote", OUT / "global_cw_fraction.json")
    print("[canonical-verify] wrote", OUT / "spiral_count_verification.json")
    return 0 if s["all_match"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
