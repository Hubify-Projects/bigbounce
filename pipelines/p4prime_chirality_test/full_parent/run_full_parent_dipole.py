#!/usr/bin/env python3
"""Row 16(i): FULL-PARENT dipole/A_95 fit on all 8,474,531 DESI Legacy DR8
galaxies (production equivariant Z2-TTA classifier outputs already committed
in the immutable catalog — REUSED, no re-inference), using the exact P4'
primary estimator (see full_parent_estimator_lib.py). Selection here is ALL
class_eq in {CW, CCW} rows (no primary_hc / raw_flip_qc_unsafe restriction) —
the full parent, not the 887,472-row strict-primary HC subset.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

import full_parent_estimator_lib as lib

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parents[1] / "p2_chirality" / "apjs_release_v1.0.244" / "p4_catalog_primary_safe_v1.0.244.parquet"
OUT = HERE / "row16i_full_parent_dipole.json"
N_DRAWS = 10_000
NULL_SEED = 20_260_904
N_AXES = 2000
INJ_SEED = 20_260_905
GRID = np.array([0.0040, 0.0050, 0.0060, 0.0070, 0.0080, 0.0090, 0.0100,
                  0.0110, 0.0120, 0.0130, 0.0140, 0.0150, 0.0175, 0.0200])


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        while chunk := fh.read(8 * 1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    t0 = time.time()
    cat_sha = sha256_file(CATALOG)
    table = pq.read_table(CATALOG, columns=["ra_deg", "dec_deg", "class_eq"])
    n_total_parent = table.num_rows
    spiral_mask = pc.is_in(table["class_eq"], value_set=pa.array(["CW", "CCW"]))
    spirals = table.filter(spiral_mask)
    n_spiral = spirals.num_rows
    ra = spirals["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = spirals["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    labels = np.asarray(spirals["class_eq"].combine_chunks().to_pylist(), dtype=object)
    is_cw = labels == "CW"

    total, cw = lib.maps_from_radec(ra, dec, is_cw)
    support, capacities, projector, A_obs = lib.build_projector(total, cw)
    support_idx = np.flatnonzero(support)
    n_cw_support = int(cw[support].sum())
    n_gal_support = int(capacities.sum())
    p_global = n_cw_support / n_gal_support
    theta, phi = hp.pix2ang(lib.NSIDE, support_idx)
    n_hat = np.column_stack([np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)])

    print(f"[{time.time()-t0:.0f}s] support={support_idx.size} px, N_support={n_gal_support:,}, A_obs={A_obs:.6f}")
    null = lib.fixed_occupancy_null(capacities, projector, n_cw_support, N_DRAWS, NULL_SEED)
    null_sorted = np.sort(null)
    z_mom = float((A_obs - null.mean()) / null.std(ddof=0))
    rank_k = int(np.count_nonzero(null >= A_obs))
    rank_p = (rank_k + 1) / (null.size + 1)
    print(f"[{time.time()-t0:.0f}s] null done: z_mom={z_mom:+.4f} rank_p={rank_p:.4f}")

    rng = np.random.default_rng(INJ_SEED)
    pdet = np.array([
        lib.detection_fraction(A, capacities, n_hat, projector, p_global, null_sorted, N_AXES, rng)
        for A in GRID
    ])
    a95_lin, bracket = lib.invert_a95(GRID, pdet)
    print(f"[{time.time()-t0:.0f}s] A_95(full-parent) = {a95_lin}")

    mono, dip = hp.fit_dipole(np.where(support, (2.0 * cw - total) / np.maximum(total, 1), hp.UNSEEN), gal_cut=0)
    ra_dip = float(np.degrees(np.arctan2(dip[1], dip[0])) % 360.0)
    dec_dip = float(np.degrees(np.arcsin(dip[2] / A_obs)))

    result = {
        "schema": "p4p-row16i-full-parent-dipole/v1",
        "estimator_source": "pipelines/p2_chirality/generate_p4_primary_label_shuffle_strict_v1_0_257.py:build_projector (imported verbatim)",
        "catalog_path": str(CATALOG.relative_to(HERE.parents[2])),
        "catalog_sha256": cat_sha,
        "n_total_parent_rows": int(n_total_parent),
        "n_spiral_full_parent": int(n_spiral),
        "selection": "class_eq in (CW, CCW); NO primary_hc / raw_flip_qc_unsafe restriction (full parent, not the 887,472-row strict-primary subset)",
        "nside": lib.NSIDE, "min_pixel_count": lib.MIN_PIXEL_COUNT,
        "n_pixels_support": int(support_idx.size),
        "n_galaxies_in_support": n_gal_support,
        "n_cw_in_support": n_cw_support,
        "p_cw_global": p_global,
        "monopole": float(mono),
        "observed_amplitude_A_obs": A_obs,
        "dipole_ra_deg": ra_dip, "dipole_dec_deg": dec_dip,
        "null": {"n_draws": N_DRAWS, "seed": NULL_SEED, "mean": float(null.mean()),
                  "std_ddof0": float(null.std(ddof=0)), "z_moment": z_mom,
                  "rank_k": rank_k, "rank_p_one_sided_upper_tail": rank_p},
        "injection_recovery": {"n_axes_per_amplitude": N_AXES, "seed": INJ_SEED,
                                 "grid_full_amp": GRID.tolist(), "detection_fraction": pdet.tolist(),
                                 "A95_obs_full_amp": a95_lin, "A95_obs_pct": (a95_lin * 100 if a95_lin else None),
                                 "bracket": bracket},
        "comparison_887k_strict_primary": {"A95_obs_pct": 0.98, "A95_CL_pct": 0.75, "N_support": 887472},
        "row16ii_injection_calibrated_systematic": {
            "source": "pipelines/p4prime_chirality_test/injection_pilot/scale20k_injection_results.json",
            "paper_residual_bias_postprocess_full_amp": -0.0026,
            "note": "pixel-level equivariant-postprocess residual bias measured on the N=20,000 label-injection pilot; reported for context, NOT subtracted from A_obs/A_95 above (no tuning)."
        },
        "wall_clock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=False) + "\n")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
