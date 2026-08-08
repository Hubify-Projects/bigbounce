#!/usr/bin/env python3
"""A_95^obs — coverage-calibrated OBSERVED-LABEL 95% upper limit on the primary
high-confidence (HC) real-space chirality dipole amplitude for P4.

Closes truth-audit finding M3-(a) (GENUINELY-NEW-REAL) from
``project-context/peer-reviews/INT_v3/ROUND_2026-07-17-P4-v1.0.264-EXACTPDF-
325b7ced-CLAUDESTACK-CONFIRM/P4_v1.0.264_truth_audit.md``.

WHAT THIS IS.  A coverage-calibrated observed-label upper limit: the injected
real-space dipole amplitude at which the EXACT committed primary estimator,
tested against the EXACT committed fixed-occupancy null, is detected (one-sided
add-one rank p < 0.05) in >= 95% of random-axis injections.  It is the
amplitude the primary channel is demonstrably sensitive to at 95% coverage.

WHAT THIS IS **NOT**.  It is NOT a physical parity-amplitude bound.  Converting
A_95^obs -> A_95^phys requires the spatially resolved morphology transfer
function (the scalar g=0.398 is illustrative only); that remains the tracked
transfer-function gate and is NOT claimed here.  This is an observed-label
sensitivity floor only, in the same A_p full-amplitude convention as the
committed headline observed amplitude A_dip = 0.00466520.

EXACTNESS.  The estimator, catalog, strict-primary selection
(primary_hc && !raw_flip_qc_unsafe -> 890,069 rows; 887,472 in the 23,633-pixel
N_spiral>=10 support), and the fixed-occupancy multivariate-hypergeometric null
are reused verbatim from the committed generator
``generate_p4_primary_label_shuffle_strict_v1_0_257.py`` (imported here so the
estimator is byte-identical).  The committed 10^4-draw null array
``p4_primary_hc_safe_label_shuffle_10k_v1_0_257.npy`` (SHA-256 3a03ca4b...) is
the detection reference.  The reproduction of A_dip=0.00466520 / z_mom=+0.63465
/ p=0.23768 is asserted as a hard gate before any injection runs.

INJECTION MODEL (observed-label).  For random isotropic axis u and full
amplitude A, per-support-pixel CW probability p_pix = p_CW_global + (A/2)(n_hat.u)
(clipped), and injected per-pixel CW counts are drawn Binomial(capacity, p_pix)
at FIXED pixel occupancy (capacities held to the observed values).  This is the
same p_CW = p_global + (A/2)cos(theta) observed-label injection convention as
the committed ``scripts/injection_sweep_extended.py`` row-(vii) sweep, upgraded
to the primary uniform-pixel estimator, the committed fixed-occupancy detection
null, >=1000 random axes/amplitude, and inversion for the 95% coverage crossing.
No ViT, no confidence cut re-inference, no transfer function, no pod.

Run:
  python3 analysis/a95_observed_label_upper_limit_v1_0_265.py           # full
  python3 analysis/a95_observed_label_upper_limit_v1_0_265.py --smoke   # fast

Output: analysis/a95_observed_label_upper_limit_v1_0_265.json (+ .partial.json)
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow.compute as pc
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
P4 = HERE.parent                       # pipelines/p2_chirality
ROOT = P4.parents[1]                   # repo root

# ---- import the committed strict-primary generator verbatim (exact estimator/null)
GEN_PATH = P4 / "generate_p4_primary_label_shuffle_strict_v1_0_257.py"
_spec = importlib.util.spec_from_file_location("p4_strict_gen", GEN_PATH)
gen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gen)

CATALOG = gen.DEFAULT_CATALOG
NULL_ARRAY = P4 / "outputs/canonical_provenance/p4_primary_hc_safe_label_shuffle_10k_v1_0_257.npy"
NULL_RECEIPT = P4 / "outputs/canonical_provenance/p4_primary_hc_safe_label_shuffle_10k_v1_0_257.json"
OUT = HERE / "a95_observed_label_upper_limit_v1_0_265.json"
OUT_PARTIAL = OUT.with_suffix(".partial.json")

NSIDE = gen.NSIDE                      # 64
# ----------------------------------------------------------------- config
SMOKE = "--smoke" in sys.argv
N_AXES = 2000                          # random isotropic axes per amplitude (>=1000 required)
DETECTION_ALPHA = 0.05                 # one-sided add-one rank p threshold
INJECTION_SEED = 20_260_717            # distinct from the null seed (20260715)
AXIS_CHUNK = 250                       # axis batch for vectorized memory control
# amplitude grid in the A_p full-amplitude convention (matches A_dip=0.004665)
COARSE_GRID = np.array(
    [0.0040, 0.0050, 0.0060, 0.0070, 0.0080, 0.0090, 0.0100,
     0.0110, 0.0120, 0.0130, 0.0140, 0.0150, 0.0175, 0.0200]
)
if SMOKE:
    N_AXES = 200
    COARSE_GRID = np.array([0.0060, 0.0090, 0.0120, 0.0150])

t0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - t0:8.1f}s] {msg}", flush=True)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while chunk := fh.read(8 * 1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def build_static() -> dict:
    """Reproduce the committed strict-primary support/estimator EXACTLY."""
    cat_sha = sha256_file(CATALOG)
    if cat_sha != gen.CATALOG_SHA256:
        raise RuntimeError(f"catalog SHA {cat_sha} != committed {gen.CATALOG_SHA256}")
    log("catalog SHA-256 matches committed generator")

    table = pq.read_table(
        CATALOG,
        columns=["ra_deg", "dec_deg", "class_eq", "primary_hc", "raw_flip_qc_unsafe"],
    )
    strict = gen.select_strict_primary(table)
    if strict.num_rows != gen.EXPECTED_SELECTED_ROWS:
        raise RuntimeError(f"strict rows {strict.num_rows} != {gen.EXPECTED_SELECTED_ROWS}")

    ra = strict["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = strict["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    labels = np.asarray(strict["class_eq"].combine_chunks().to_pylist(), dtype=object)
    is_cw = labels == "CW"
    if not np.all(np.logical_or(is_cw, labels == "CCW")):
        raise RuntimeError("strict primary selection contains a non-spiral label")

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0))
    total = np.bincount(pix, minlength=npix).astype(np.int64)
    cw = np.bincount(pix[is_cw], minlength=npix).astype(np.int64)

    # EXACT committed estimator machinery (support, capacities, projector, A_obs)
    support, capacities, projector, observed_amplitude = gen.build_projector(total, cw)
    n_cw = int(cw[support].sum())
    n_gal = int(capacities.sum())
    p_cw_global = n_cw / n_gal

    # per-support-pixel unit vectors (same order as build_projector's design matrix)
    support_idx = np.flatnonzero(support)
    theta, phi = hp.pix2ang(NSIDE, support_idx)
    n_hat = np.column_stack([
        np.sin(theta) * np.cos(phi),
        np.sin(theta) * np.sin(phi),
        np.cos(theta),
    ]).astype(np.float64)                     # (Ns, 3)

    log(f"support {support_idx.size} px | {n_gal:,} gal | n_cw {n_cw:,} | "
        f"p_CW_global {p_cw_global:.6f} | A_obs {observed_amplitude:.8f}")
    return dict(
        catalog_sha256=cat_sha,
        support_idx=support_idx,
        capacities=capacities.astype(np.int64),
        projector=projector,
        n_hat=n_hat,
        n_cw=n_cw,
        n_gal=n_gal,
        p_cw_global=p_cw_global,
        observed_amplitude=observed_amplitude,
    )


def verify_headline(S: dict, null: np.ndarray) -> dict:
    """Hard gate: committed A_obs / z_mom / rank-p reproduced exactly."""
    A_obs = S["observed_amplitude"]
    null_mean = float(null.mean())
    null_std0 = float(null.std(ddof=0))
    z_mom = (A_obs - null_mean) / null_std0
    rank_k = int(np.count_nonzero(null >= A_obs))
    rank_p = (rank_k + 1) / (null.size + 1)
    rec = json.loads(NULL_RECEIPT.read_text())
    checks = {
        "A_obs_committed": rec["observed_amplitude"],
        "A_obs_recomputed": A_obs,
        "z_mom_committed": rec["significance_sigma_ddof0"],
        "z_mom_recomputed": z_mom,
        "rank_p_committed": rec["rank_p_one_sided_upper_tail"],
        "rank_p_recomputed": rank_p,
    }
    ok = (
        abs(A_obs - rec["observed_amplitude"]) < 1e-12
        and abs(z_mom - rec["significance_sigma_ddof0"]) < 1e-6
        and rank_k == rec["rank_k"]
    )
    if not ok:
        raise RuntimeError(f"headline reproduction gate FAILED: {checks}")
    log(f"headline gate PASS  A_obs={A_obs:.8f}  z_mom={z_mom:+.5f}  p={rank_p:.5f}")
    checks["passed"] = True
    return checks


def detection_fraction(A: float, S: dict, null_sorted: np.ndarray,
                       rng: np.random.Generator) -> tuple[float, np.ndarray]:
    """Fraction of N_AXES random-axis injections detected at add-one rank p<alpha.

    Vectorized over axis chunks.  Injection is observed-label:
    p_pix = p_global + (A/2) (n_hat . u); n_cw ~ Binomial(capacity, p_pix) at
    fixed occupancy; estimator = ||projector @ ((2 n_cw - cap)/cap)||[1:4].
    Detection uses the committed fixed-occupancy null array (add-one rank).
    """
    cap = S["capacities"]                 # (Ns,)
    capf = cap.astype(np.float64)
    n_hat = S["n_hat"]                    # (Ns, 3)
    proj = S["projector"]                 # (4, Ns)
    pg = S["p_cw_global"]
    Nnull = null_sorted.size
    detected = np.zeros(N_AXES, dtype=bool)
    amps = np.empty(N_AXES, dtype=np.float64)

    done = 0
    while done < N_AXES:
        m = min(AXIS_CHUNK, N_AXES - done)
        # isotropic axes: unit-normalized standard normals
        u = rng.standard_normal((3, m))
        u /= np.linalg.norm(u, axis=0, keepdims=True)
        cos = n_hat @ u                                   # (Ns, m)
        p = pg + 0.5 * A * cos
        np.clip(p, 1e-6, 1.0 - 1e-6, out=p)
        n_cw = rng.binomial(cap[:, None], p)              # (Ns, m) fixed occupancy
        mapvals = (2.0 * n_cw - capf[:, None]) / capf[:, None]
        coef = proj @ mapvals                             # (4, m)
        amp = np.linalg.norm(coef[1:4, :], axis=0)        # (m,)
        # add-one one-sided upper-tail rank p = (#null>=amp + 1)/(Nnull+1)
        ge = Nnull - np.searchsorted(null_sorted, amp, side="left")
        rank_p = (ge + 1.0) / (Nnull + 1.0)
        detected[done:done + m] = rank_p < DETECTION_ALPHA
        amps[done:done + m] = amp
        done += m
    return float(detected.mean()), amps


def invert_A95(grid: np.ndarray, pdet: np.ndarray) -> dict:
    """Linear-interpolate the P_det=0.95 crossing; also logistic fit for a
    smooth estimate. Returns both plus the bracketing grid points."""
    target = 0.95
    order = np.argsort(grid)
    g = grid[order]
    pv = pdet[order]
    # linear interpolation of first upward crossing
    a_lin = None
    bracket = None
    for i in range(len(g) - 1):
        if pv[i] < target <= pv[i + 1] and pv[i + 1] > pv[i]:
            frac = (target - pv[i]) / (pv[i + 1] - pv[i])
            a_lin = float(g[i] + frac * (g[i + 1] - g[i]))
            bracket = [float(g[i]), float(g[i + 1]), float(pv[i]), float(pv[i + 1])]
            break
    if a_lin is None and pv[-1] >= target:
        a_lin = float(g[np.argmax(pv >= target)])
    # logistic fit P = 1/(1+exp(-k(A-A0))) on interior points (0<p<1)
    a_log = None
    interior = (pv > 1e-3) & (pv < 1 - 1e-3)
    if interior.sum() >= 3:
        y = np.clip(pv[interior], 1e-3, 1 - 1e-3)
        z = np.log(y / (1.0 - y))                 # logit
        k, b = np.polyfit(g[interior], z, 1)       # z = k*A + b
        if k > 0:
            z_target = np.log(target / (1.0 - target))
            a_log = float((z_target - b) / k)
    return {
        "target_coverage": target,
        "A95_obs_linear_interp": a_lin,
        "A95_obs_logistic_fit": a_log,
        "bracket_[A_lo,A_hi,P_lo,P_hi]": bracket,
    }


def write_partial(state: dict) -> None:
    OUT_PARTIAL.write_text(json.dumps(state, indent=2))


def run_grid(grid: np.ndarray, S: dict, null_sorted: np.ndarray,
             rng: np.random.Generator, per_amp: list, tag: str) -> np.ndarray:
    pdet = np.empty(len(grid))
    for i, A in enumerate(grid):
        f, amps = detection_fraction(float(A), S, null_sorted, rng)
        pdet[i] = f
        per_amp.append({
            "phase": tag,
            "A_injected_full_amp": float(A),
            "A_injected_pct": float(A * 100.0),
            "n_axes": N_AXES,
            "detection_fraction": f,
            "recovered_amp_p16_p50_p84": [float(x) for x in np.quantile(amps, [0.16, 0.5, 0.84])],
        })
        log(f"[{tag}] A={A*100:.3f}%  P_det={f:.4f}")
        write_partial({
            "status": "running", "phase": tag,
            "completed_amplitudes": i + 1, "n_amplitudes": len(grid),
            "n_axes": N_AXES, "detection_alpha": DETECTION_ALPHA,
            "per_amplitude": per_amp, "elapsed_s": round(time.time() - t0, 1),
        })
    return pdet


def main() -> int:
    log(f"A_95^obs upper-limit computation ({'SMOKE' if SMOKE else 'FULL'})")
    S = build_static()
    null = np.load(NULL_ARRAY)
    null_sha = sha256_file(NULL_ARRAY)
    log(f"committed null array: {null.size} draws, SHA-256 {null_sha[:16]}...")
    headline = verify_headline(S, null)
    null_sorted = np.sort(null)

    rng = np.random.default_rng(INJECTION_SEED)
    per_amp: list = []

    # ---- coarse pass
    pdet_coarse = run_grid(COARSE_GRID, S, null_sorted, rng, per_amp, "coarse")
    inv = invert_A95(COARSE_GRID, pdet_coarse)

    # ---- adaptive refinement around the 0.95 crossing
    grid_all = list(COARSE_GRID)
    pdet_all = list(pdet_coarse)
    if inv["bracket_[A_lo,A_hi,P_lo,P_hi]"] is not None and not SMOKE:
        lo, hi = inv["bracket_[A_lo,A_hi,P_lo,P_hi]"][0], inv["bracket_[A_lo,A_hi,P_lo,P_hi]"][1]
        refine = np.linspace(lo, hi, 6)[1:-1]     # 4 interior points
        refine = np.array([a for a in refine if a not in COARSE_GRID])
        if refine.size:
            log(f"refining {refine.size} points in [{lo*100:.3f}%, {hi*100:.3f}%]")
            pdet_ref = run_grid(refine, S, null_sorted, rng, per_amp, "refine")
            grid_all.extend(refine)
            pdet_all.extend(pdet_ref)

    grid_all = np.array(grid_all)
    pdet_all = np.array(pdet_all)
    inv_final = invert_A95(grid_all, pdet_all)

    A95 = inv_final["A95_obs_linear_interp"] or inv_final["A95_obs_logistic_fit"]
    result = {
        "artifact": "A_95^obs — coverage-calibrated observed-label 95% upper limit "
                    "on the primary HC real-space chirality dipole amplitude",
        "closes": "P4 v1.0.264 truth-audit finding M3-(a) (GENUINELY-NEW-REAL)",
        "audit_ref": "project-context/peer-reviews/INT_v3/ROUND_2026-07-17-P4-"
                     "v1.0.264-EXACTPDF-325b7ced-CLAUDESTACK-CONFIRM/"
                     "P4_v1.0.264_truth_audit.md",
        "status": "complete",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "generator": "pipelines/p2_chirality/analysis/"
                     "a95_observed_label_upper_limit_v1_0_265.py",
        "label_class": "OBSERVED-LABEL (NOT a physical parity-amplitude bound)",
        "A95_obs_full_amplitude": A95,
        "A95_obs_pct": (A95 * 100.0 if A95 is not None else None),
        "A95_obs_linear_interp": inv_final["A95_obs_linear_interp"],
        "A95_obs_logistic_fit": inv_final["A95_obs_logistic_fit"],
        "coverage_bracket": inv_final["bracket_[A_lo,A_hi,P_lo,P_hi]"],
        "detection_definition": (
            f"one-sided add-one empirical rank p<{DETECTION_ALPHA} of the primary "
            "uniform-pixel fit_dipole amplitude against the committed fixed-occupancy "
            "10^4-draw null (p=(#null>=A_rec + 1)/(N_null+1))"
        ),
        "injection_model": (
            "observed-label: p_pix = p_CW_global + (A/2)(n_hat.u); "
            "n_cw ~ Binomial(capacity, p_pix) at fixed pixel occupancy; "
            "A is the A_p full-amplitude dipole (same convention as A_obs)"
        ),
        "estimator": "EXACT committed primary uniform-pixel healpy.fit_dipole amplitude "
                     "(imported from generate_p4_primary_label_shuffle_strict_v1_0_257.py)",
        "null_reference": "EXACT committed fixed-occupancy multivariate-hypergeometric "
                          "10^4-draw null array (label-randomization)",
        "headline_reproduction_gate": headline,
        "sample": {
            "selection": "primary_hc && !raw_flip_qc_unsafe",
            "n_selected_rows": gen.EXPECTED_SELECTED_ROWS,
            "n_galaxies_in_support": S["n_gal"],
            "n_pixels_support": int(S["support_idx"].size),
            "n_cw_in_support": S["n_cw"],
            "p_cw_global": S["p_cw_global"],
            "nside": NSIDE,
            "min_pixel_count": gen.MIN_PIXEL_COUNT,
            "observed_amplitude_A_obs": S["observed_amplitude"],
        },
        "config": {
            "n_axes_per_amplitude": N_AXES,
            "detection_alpha": DETECTION_ALPHA,
            "injection_seed": INJECTION_SEED,
            "axis_rule": "random isotropic (unit-normalized Gaussian)",
            "amplitude_grid_full_amp": [float(x) for x in np.sort(grid_all)],
            "smoke": SMOKE,
        },
        "per_amplitude": sorted(per_amp, key=lambda r: r["A_injected_full_amp"]),
        "inputs_hashed": {
            "catalog": {"path": gen.repo_relative(CATALOG), "sha256": S["catalog_sha256"]},
            "committed_null_array": {
                "path": str(NULL_ARRAY.resolve().relative_to(ROOT.resolve())),
                "sha256": null_sha,
            },
            "committed_generator": {
                "path": str(GEN_PATH.resolve().relative_to(ROOT.resolve())),
                "sha256": sha256_file(GEN_PATH),
            },
        },
        "runtime_versions": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "healpy": hp.__version__,
        },
        "interpretation_limits": [
            "OBSERVED-LABEL coverage floor only; not a physical/primordial amplitude bound",
            "A_obs->A_phys requires the spatially resolved morphology transfer function "
            "(tracked transfer-function gate; scalar g=0.398 is illustrative only)",
            "detection null is the committed fixed-occupancy label randomization; it is not "
            "a joint spatial-nuisance likelihood",
            "changes no existing science number; the primary null (z_mom=+0.635, p=0.23768) "
            "is unchanged and additive",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2))
    write_partial({"status": "done", "output": str(OUT),
                   "A95_obs_full_amplitude": A95,
                   "elapsed_s": round(time.time() - t0, 1)})
    log(f"WROTE {OUT}")
    if A95 is not None:
        log(f"A_95^obs = {A95:.6f}  ({A95*100:.4f}% full-amplitude, OBSERVED-LABEL)")
    else:
        log("A_95^obs crossing NOT bracketed on this grid — extend the grid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
