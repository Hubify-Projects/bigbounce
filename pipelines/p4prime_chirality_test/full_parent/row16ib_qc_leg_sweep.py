#!/usr/bin/env python3
"""Row 16(i-b): graded QC sweep + per-imaging-leg/footprint systematics table
for the full-parent chirality dipole. Pre-registration:
ROW16IB_AXIS_SHIFT_2026-09-04.md (committed first). Estimator imported
verbatim from full_parent_estimator_lib (-> P4' strict-primary generator).
No tuning: every configured fit is reported with whatever it returns.
"""
from __future__ import annotations
import hashlib, json, time
from pathlib import Path
import healpy as hp
import numpy as np
import pyarrow as pa, pyarrow.compute as pc, pyarrow.parquet as pq
import full_parent_estimator_lib as lib

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parents[1] / "p2_chirality" / "apjs_release_v1.0.244" / "p4_catalog_primary_safe_v1.0.244.parquet"
OUT = HERE / "row16ib_axis_shift.json"
DEC_LEG_BOUNDARIES = (-20.0, 32.0)   # p2_chirality/c12b_wls_conditioning.py
N_DRAWS_MAIN, N_DRAWS_SUB, SEED = 10_000, 2_000, 20_260_906
ROW16II_BIAS = -0.0026
t0 = time.time()


def log(m): print(f"[{time.time()-t0:7.1f}s] {m}", flush=True)


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        while chunk := fh.read(8 << 20):
            h.update(chunk)
    return h.hexdigest()


def fit(name: str, ra, dec, is_cw, sel, n_draws, seed):
    """Full estimator + fixed-occupancy null on the sub-selection `sel`."""
    n_sel = int(sel.sum())
    if n_sel < 1000:
        return {"name": name, "n_selected": n_sel, "status": "SKIPPED_too_few"}
    total, cw = lib.maps_from_radec(ra[sel], dec[sel], is_cw[sel])
    support, capacities, projector, A_obs = lib.build_projector(total, cw)
    n_cw = int(cw[support].sum()); n_gal = int(capacities.sum())
    null = lib.fixed_occupancy_null(capacities, projector, n_cw, n_draws, seed)
    z = float((A_obs - null.mean()) / null.std(ddof=0))
    rank_p = (int(np.count_nonzero(null >= A_obs)) + 1) / (null.size + 1)
    m = np.where(support, (2.0 * cw - total) / np.maximum(total, 1), hp.UNSEEN)
    mono, dip = hp.fit_dipole(m, gal_cut=0)
    ra_d = float(np.degrees(np.arctan2(dip[1], dip[0])) % 360.0)
    dec_d = float(np.degrees(np.arcsin(np.clip(dip[2] / max(np.linalg.norm(dip), 1e-12), -1, 1))))
    log(f"{name:34s} N={n_gal:>9,} A={A_obs*100:6.3f}% z={z:+6.2f} p={rank_p:.4f} axis=({ra_d:6.1f},{dec_d:+6.1f})")
    return {"name": name, "n_selected": n_sel, "n_pixels_support": int(support.sum()),
            "n_galaxies_in_support": n_gal, "n_cw_in_support": n_cw,
            "A_obs_pct": A_obs * 100, "A_obs_pct_row16ii_corrected": (A_obs + ROW16II_BIAS) * 100,
            "monopole": float(mono), "axis_ra_deg": ra_d, "axis_dec_deg": dec_d,
            "null": {"n_draws": int(n_draws), "seed": int(seed), "mean": float(null.mean()),
                     "std_ddof0": float(null.std(ddof=0))},
            "z": z, "rank_p_one_sided": rank_p, "status": "OK"}


def angsep(ra1, dec1, ra2, dec2):
    v = [hp.ang2vec(np.radians(90 - d), np.radians(r)) for r, d in ((ra1, dec1), (ra2, dec2))]
    return float(np.degrees(np.arccos(np.clip(np.dot(v[0], v[1]), -1, 1))))


def monopole_leakage(capacities, projector, p_global, deltas, n_real, seed):
    """Pure-monopole (no dipole) injections -> dipole amplitude leaked by the mask."""
    rng = np.random.default_rng(seed)
    capf = capacities.astype(np.float64)
    out = {}
    for d in deltas:
        p = np.clip(p_global + 0.5 * d, 1e-6, 1 - 1e-6)
        amps = np.empty(n_real)
        for i in range(n_real):
            n_cw = rng.binomial(capacities, p)
            amps[i] = np.linalg.norm((projector @ ((2.0 * n_cw - capf) / capf))[1:4])
        out[f"delta_{d:+.4f}"] = {"mean_leaked_A_pct": float(amps.mean() * 100),
                                  "p99_leaked_A_pct": float(np.percentile(amps, 99) * 100)}
        log(f"  monopole-leak delta={d:+.4f}: mean A_leak={amps.mean()*100:.4f}%")
    return out


def main() -> int:
    cat_sha = sha256_file(CATALOG)
    tb = pq.read_table(CATALOG, columns=["ra_deg", "dec_deg", "class_eq", "primary_hc", "raw_flip_qc_unsafe"])
    tb = tb.filter(pc.is_in(tb["class_eq"], value_set=pa.array(["CW", "CCW"])))
    ra = tb["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = tb["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    is_cw = np.asarray(tb["class_eq"].combine_chunks().to_pylist(), dtype=object) == "CW"
    hc = tb["primary_hc"].combine_chunks().to_numpy(zero_copy_only=False).astype(bool)
    unsafe = tb["raw_flip_qc_unsafe"].combine_chunks().to_numpy(zero_copy_only=False).astype(bool)
    n = ra.size
    log(f"spirals loaded: {n:,}  primary_hc={hc.sum():,}  raw_flip_qc_unsafe={unsafe.sum():,}")

    gl, gb = hp.Rotator(coord=["C", "G"])(np.radians(90 - dec), np.radians(ra % 360))
    b = 90 - np.degrees(gl)
    lo, hi = DEC_LEG_BOUNDARIES
    legs = {"BASS+MzLS": dec > hi, "DECaLS": (dec > lo) & (dec <= hi), "DES": dec <= lo}

    res = {"schema": "p4p-row16ib-axis-shift/v1", "catalog_sha256": cat_sha,
           "prereg": "ROW16IB_AXIS_SHIFT_2026-09-04.md", "n_spirals_full_parent": int(n),
           "dec_leg_boundaries": list(DEC_LEG_BOUNDARIES),
           "row16ii_bias_full_amp_reported_not_subtracted": ROW16II_BIAS,
           "qc_sweep": {}, "legs": {}, "galactic_cuts": {}}

    sels = {"C0_full_parent": np.ones(n, bool), "C1_relax_primary_hc": ~unsafe,
            "C2_relax_rawflip": hc, "C3_strict": hc & ~unsafe}
    for i, (k, s) in enumerate(sels.items()):
        res["qc_sweep"][k] = fit(k, ra, dec, is_cw, s, N_DRAWS_MAIN if k in ("C0_full_parent", "C3_strict") else N_DRAWS_SUB, SEED + i)

    for j, (leg, lm) in enumerate(legs.items()):
        for base in ("C0_full_parent", "C3_strict"):
            bm = sels[base]
            res["legs"][f"{base}|only_{leg}"] = fit(f"{base}|only_{leg}", ra, dec, is_cw, bm & lm, N_DRAWS_SUB, SEED + 100 + j)
            res["legs"][f"{base}|drop_{leg}"] = fit(f"{base}|drop_{leg}", ra, dec, is_cw, bm & ~lm, N_DRAWS_SUB, SEED + 200 + j)

    for k, cut in (("C0|abs_b_gt_20", np.abs(b) > 20), ("C0|abs_b_gt_30", np.abs(b) > 30)):
        res["galactic_cuts"][k] = fit(k, ra, dec, is_cw, cut, N_DRAWS_SUB, SEED + 300)

    total, cw = lib.maps_from_radec(ra, dec, is_cw)
    support, capacities, projector, _ = lib.build_projector(total, cw)
    p_g = float(cw[support].sum() / capacities.sum())
    res["monopole_mask_leakage_null"] = monopole_leakage(
        capacities, projector, p_g,
        [2 * (p_g - 0.5), ROW16II_BIAS, -ROW16II_BIAS], 1000, SEED + 400)

    c0, c3 = res["qc_sweep"]["C0_full_parent"], res["qc_sweep"]["C3_strict"]
    res["axis_separations_deg"] = {
        "C0_vs_C3": angsep(c0["axis_ra_deg"], c0["axis_dec_deg"], c3["axis_ra_deg"], c3["axis_dec_deg"]),
        **{k: angsep(c0["axis_ra_deg"], c0["axis_dec_deg"], v["axis_ra_deg"], v["axis_dec_deg"])
           for k, v in res["legs"].items() if v.get("status") == "OK" and k.startswith("C0_full_parent|drop_")},
    }
    res["systematics_legs_not_run"] = ["dr8_brick_quality", "psf_depth", "psf_seeing", "ebv"]
    res["systematics_legs_not_run_reason"] = (
        "immutable release parquet carries no per-object depth/seeing/EBV/brick columns; "
        "the DR8 sweep join used by wave_14_qq_systematics_regression.py lives on a retired "
        "pod path (/workspace/dr8_sweep_fetch). Proxied by imaging leg + |b| cuts only.")
    res["wall_clock_s"] = time.time() - t0
    OUT.write_text(json.dumps(res, indent=2) + "\n")
    log(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
