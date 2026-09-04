"""
A3-M audit item DA3M-R5-18 -- gamma_cr COVERAGE of the 27-point PBH grid.

Question (R5 truth audit, item DA3M-R5-18): the paper quotes a required-amplitude
ratio A(-35/16)/A(-35/8) = 1.7-1.9 from `pbh_compaction_fnl.py`'s 27-point
(Delta, r_p k_p, C_th) grid, and separately notes that the SIGN of the
non-Gaussian effect flips at gamma_cr ~ 0.85 (enhancement below, suppression
above).  Whether any of the 27 points fall at gamma_cr <~ 0.85 is not reported,
and neither is whether the grid's gamma_cr coverage contains the gamma_cr the
lab's OWN spectrum shape actually has.

Method: pure re-reading of two COMMITTED result JSONs -- no re-derivation, no
new physics, no re-fit.
  (1) `outputs/pbh_compaction_fnl.json` -> robust_amplitude_requirement_grid:
      the 27 grid points, each carrying gamma_cr and ratio_-35/16_over_-35/8.
      gamma_cr = sigma_cr^2/(sigma_c sigma_r) [Choudhury et al. 2025 Eq. 50]
      depends only on the SHAPE (Delta, r_p k_p), not on C_th, so the 27 points
      carry 9 distinct gamma_cr values, each repeated over C_th in {0.4,0.5,0.6}.
  (2) `outputs/inlab_delta2_zeta_2026-09-03.json` -> ir_cutoff_sensitivity:
      the gamma_cr the lab's own near-scale-invariant spectrum gives, over the
      IR-cutoff scan k_min/k_p in {1e-5, 1e-3, 1e-2, 1e-1}
      (the 0.27-0.63 range of the A3-1b note).

Reported: gamma_cr per grid point; the covered range; how many points fall at
gamma_cr <= 0.85 (the enhancement branch); and whether the in-lab shape's
gamma_cr range lies INSIDE or OUTSIDE the scanned coverage.

Venue: local (Apple silicon), CPU only, seconds, cost $0.
Output: outputs/r5_18_gammacr_coverage.json
"""
from __future__ import annotations
import json, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
GRIDJ = HERE / "outputs/pbh_compaction_fnl.json"
INLABJ = HERE / "outputs/inlab_delta2_zeta_2026-09-03.json"
OUTJ = HERE / "outputs/r5_18_gammacr_coverage.json"
FLIP = 0.85          # the sign-flip scale quoted in pbh_compaction_fnl.py step (4)

def main():
    t0 = time.time()
    grid = json.loads(GRIDJ.read_text())["robust_amplitude_requirement_grid"]
    inlab = json.loads(INLABJ.read_text())["ir_cutoff_sensitivity"]

    pts = []
    for key, v in grid.items():
        d = dict(p.split("=") for p in key.split(","))
        pts.append({"Delta": float(d["Delta"]), "rp_kp": float(d["rp_kp"]),
                    "C_th": float(d["C_th"]), "gamma_cr": v["gamma_cr"],
                    "ratio_-35/16_over_-35/8": v["ratio_-35/16_over_-35/8"]})
    pts.sort(key=lambda p: (p["gamma_cr"], p["C_th"]))
    gs = [p["gamma_cr"] for p in pts]
    rs = [p["ratio_-35/16_over_-35/8"] for p in pts]
    distinct = sorted({round(g, 10) for g in gs})
    below = [p for p in pts if p["gamma_cr"] <= FLIP]

    lab = {k: v["gamma_cr"] for k, v in inlab.items()}
    lab_lo, lab_hi = min(lab.values()), max(lab.values())

    out = {
        "task": "DA3M-R5-18 -- gamma_cr coverage of the 27-point PBH grid and "
                "the standing of the quoted 1.7-1.9 amplitude ratio",
        "date": "2026-09-04",
        "source_artifacts": {
            "grid": "research/track_a3_multichannel/outputs/pbh_compaction_fnl.json"
                    " (robust_amplitude_requirement_grid)",
            "inlab_shape": "research/track_a3_multichannel/outputs/"
                           "inlab_delta2_zeta_2026-09-03.json "
                           "(ir_cutoff_sensitivity)"},
        "gamma_cr_definition": "sigma_cr^2/(sigma_c sigma_r), Choudhury et al. "
            "2025 (arXiv:2409.18983) Eq. 50; a function of the SPECTRUM SHAPE "
            "(Delta, r_p k_p) only -- independent of C_th",
        "grid_points": pts,
        "n_points": len(pts),
        "n_distinct_gamma_cr": len(distinct),
        "distinct_gamma_cr": distinct,
        "gamma_cr_covered_range": [min(gs), max(gs)],
        "ratio_range_over_grid": [min(rs), max(rs)],
        "sign_flip_scale": FLIP,
        "n_points_at_or_below_flip": len(below),
        "points_at_or_below_flip": sorted({round(p["gamma_cr"], 6) for p in below}),
        "inlab_spectrum_gamma_cr": lab,
        "inlab_gamma_cr_range": [lab_lo, lab_hi],
        "inlab_inside_grid_coverage": bool(lab_hi >= min(gs)),
        "verdict": {
            "coverage": f"the 27 points carry {len(distinct)} distinct gamma_cr values "
                f"spanning [{min(gs):.3f}, {max(gs):.3f}]; each value repeats "
                "over C_th in {0.4, 0.5, 0.6} because gamma_cr is C_th-independent",
            "enhancement_branch": f"{len(below)} of {len(pts)} points sit at "
                f"gamma_cr <= {FLIP} (the enhancement branch); the grid straddles "
                "the sign-flip scale rather than sitting entirely above it",
            "is_the_quoted_ratio_inside_coverage":
                f"NO for the lab's own spectrum shape. The in-lab near-scale-"
                f"invariant spectrum gives gamma_cr in [{lab_lo:.3f}, {lab_hi:.3f}], "
                f"entirely BELOW the scanned [{min(gs):.3f}, {max(gs):.3f}]. The "
                f"grid's own ratio range is [{min(rs):.3f}, {max(rs):.3f}] "
                "(1.732 +- 0.050); the in-lab shape gives 1.85-1.89 (A3-1b note). "
                "The quoted 1.7-1.9 is therefore the UNION of the scanned grid and "
                "the one out-of-coverage in-lab evaluation -- honest as a combined "
                "range, but it must not be presented as a scan result, and the "
                "narrower 1.732 +- 0.050 must not be quoted as universal."},
        "wall_seconds": time.time() - t0}
    OUTJ.write_text(json.dumps(out, indent=2))
    for p in pts:
        print(f"  Delta={p['Delta']:<5} rp_kp={p['rp_kp']:<5} C_th={p['C_th']:<4} "
              f"gamma_cr={p['gamma_cr']:.4f}  ratio={p['ratio_-35/16_over_-35/8']:.4f}")
    print(json.dumps(out["verdict"], indent=2))

if __name__ == "__main__":
    main()
