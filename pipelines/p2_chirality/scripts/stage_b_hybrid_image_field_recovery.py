#!/usr/bin/env python3
"""Stage-B hybrid paired-image -> field injection/recovery for P4.

This is deliberately *not* a continuous morphology transform and not an
unconditional physical calibration.  It uses the two already-inferred members
of each Stage-A original/mirror pair as a discrete intervention.  A latent
CW/CCW population dipole is drawn on deterministic isotropic axes; for each
Stage-A spiral the original or mirror member is selected to realize the drawn
handedness, after which the stored production Z2-TTA class/probability is
passed through hard-label selection, NS triage, p_eq cuts, HEALPix map making,
and the canonical real-space dipole estimator.

The missing ingredient for an unconditional physical calibration is an
independent per-object true chirality label (and a validated continuous image
transformation).  The JSON output says this explicitly.
"""
from __future__ import annotations

import hashlib
import json
import math
import time
import urllib.request
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow.compute as pc
import pyarrow.parquet as pq
from astropy.io import fits
from huggingface_hub import hf_hub_download


ROOT = Path(__file__).resolve().parents[3]
P4 = ROOT / "pipelines" / "p2_chirality"
STAGE_A = P4 / "outputs" / "canonical_provenance" / "e2e_fullrun" / "e2e_shards"
MORPH = P4 / "outputs" / "spiral_morphology_dr8.parquet"
OUT = P4 / "outputs" / "canonical_provenance" / "stage_b_hybrid_image_field_recovery.json"
BRICK_CACHE = Path("/tmp/p4_stage_b_bricks")
BRICK_CACHE.mkdir(exist_ok=True)

NSIDE = 64
NPIX = hp.nside2npix(NSIDE)
MIN_PIX_COUNT = 10
SEED = 20260714
N_AXES = 20
N_NULL = 500
AMPLITUDES = np.array([0.005, 0.0075, 0.010, 0.015, 0.020])
CUTS = [0.0, 0.6, 0.7, 0.8, 0.9]
URLS = {
    "north": "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr8/north/survey-bricks-dr8-north.fits.gz",
    "south": "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr8/south/survey-bricks-dr8-south.fits.gz",
}


def log(msg: str, t0: float) -> None:
    print(f"[{time.time() - t0:7.1f}s] {msg}", flush=True)


def seq_hash(values) -> str:
    h = hashlib.sha256()
    for v in values:
        h.update(str(v).encode("utf-8"))
        h.update(b"\0")
    return h.hexdigest()


def class_code(col) -> np.ndarray:
    # Stage-A uses NS; production parquet uses NOT_SPIRAL.  Codes: 1=CW,
    # -1=CCW, 0=NS/other.
    a = np.zeros(len(col), dtype=np.int8)
    a[np.asarray(pc.equal(col, "CW"))] = 1
    a[np.asarray(pc.equal(col, "CCW"))] = -1
    return a


def fibonacci_axes(n: int) -> np.ndarray:
    i = np.arange(n, dtype=float)
    z = 1.0 - 2.0 * (i + 0.5) / n
    phi = 2.0 * np.pi * i / ((1.0 + np.sqrt(5.0)) / 2.0)
    r = np.sqrt(np.maximum(0.0, 1.0 - z * z))
    return np.column_stack([r * np.cos(phi), r * np.sin(phi), z])


def fit_dipole(n_total: np.ndarray, n_cw: np.ndarray) -> dict:
    # Exact primary-mask convention: retain pixels with N_spiral >= 10.
    keep = n_total >= MIN_PIX_COUNT
    if int(keep.sum()) < 10:
        return {"ok": False, "n_pix": int(keep.sum())}
    m = np.full(NPIX, hp.UNSEEN, dtype=np.float64)
    m[keep] = (2.0 * n_cw[keep] - n_total[keep]) / n_total[keep]
    mono, dip = hp.fit_dipole(m, gal_cut=0)
    amp = float(np.linalg.norm(dip))
    return {
        "ok": True,
        "n_pix": int(keep.sum()),
        "monopole": float(mono),
        "vector": [float(x) for x in dip],
        "amplitude": amp,
    }


def null_calibration(n_total: np.ndarray, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    vals = np.empty(N_NULL, dtype=np.float64)
    for k in range(N_NULL):
        n_cw = rng.binomial(n_total.astype(np.int64), 0.5)
        vals[k] = fit_dipole(n_total, n_cw).get("amplitude", np.nan)
    vals = vals[np.isfinite(vals)]
    return {
        "n": int(len(vals)),
        "mean": float(vals.mean()),
        "std_ddof1": float(vals.std(ddof=1)),
        "q95": float(np.quantile(vals, 0.95)),
        "q99": float(np.quantile(vals, 0.99)),
    }


def parse_keys(ids: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    brick = np.fromiter((int(x.split("_", 1)[0]) for x in ids), dtype=np.int64, count=len(ids))
    obj = np.fromiter((int(x.split("_", 1)[1]) for x in ids), dtype=np.int64, count=len(ids))
    return brick, obj


def match_sorted(query: np.ndarray, reference: np.ndarray) -> np.ndarray:
    order = np.argsort(reference)
    ref = reference[order]
    pos = np.searchsorted(ref, query)
    ok = (pos < len(ref)) & (ref[np.minimum(pos, len(ref) - 1)] == query)
    out = np.full(len(query), -1, dtype=np.int64)
    out[ok] = order[pos[ok]]
    return out


def load_brick_metrics(t0: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rows = []
    for tag, url in URLS.items():
        path = BRICK_CACHE / Path(url).name
        if not path.exists():
            log(f"downloading official DR8 {tag} brick table", t0)
            urllib.request.urlretrieve(url, path)
        with fits.open(path, memmap=True) as hdul:
            d = hdul[1].data
            names = {x.lower(): x for x in d.columns.names}
            bra = np.asarray(d[names["ra"]], dtype=np.float64)
            bdec = np.asarray(d[names["dec"]], dtype=np.float64)
            psfcols = [v for k, v in names.items() if k.startswith("psfsize_")]
            depcols = [v for k, v in names.items() if k.startswith("psfdepth_")]
            psf = np.nanmean(np.column_stack([d[c] for c in psfcols]), axis=1).astype(np.float32)
            depth = np.nanmean(np.column_stack([d[c] for c in depcols]), axis=1).astype(np.float32)
            rows.append((bra, bdec, psf, depth))
    return tuple(np.concatenate([r[i] for r in rows]) for i in range(4))


def quantile_group(values: np.ndarray, labels: list[str]) -> tuple[np.ndarray, list[float]]:
    finite = np.isfinite(values)
    edges = np.quantile(values[finite], [0.25, 0.5, 0.75])
    group = np.full(len(values), -1, dtype=np.int8)
    group[finite] = np.digitize(values[finite], edges, right=True).astype(np.int8)
    return group, [float(x) for x in edges]


def main() -> int:
    t0 = time.time()
    log("loading production catalog coordinates", t0)
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset"
    )
    cat = pq.read_table(
        cat_path, columns=["dr8_id", "ra", "dec", "class_eq", "confidence_eq"]
    )
    cat_ids = np.asarray(cat["dr8_id"].to_pylist(), dtype=object)
    ra_all = np.asarray(cat["ra"], dtype=np.float64)
    dec_all = np.asarray(cat["dec"], dtype=np.float64)
    production_class = class_code(cat["class_eq"])
    production_conf = np.asarray(cat["confidence_eq"], dtype=np.float32)

    ids_parts, o_parts, m_parts, pcw_parts, pccw_parts = [], [], [], [], []
    log("loading 192 Stage-A shards", t0)
    for p in sorted(STAGE_A.glob("e2e_*.parquet")):
        tab = pq.read_table(
            p,
            columns=["dr8_id", "class_eq", "class_eq_mirror", "p_cw_eq", "p_ccw_eq"],
        )
        ids_parts.extend(tab["dr8_id"].to_pylist())
        o_parts.append(class_code(tab["class_eq"]))
        m_parts.append(class_code(tab["class_eq_mirror"]))
        pcw_parts.append(np.asarray(tab["p_cw_eq"], dtype=np.float32))
        pccw_parts.append(np.asarray(tab["p_ccw_eq"], dtype=np.float32))
    stage_ids = np.asarray(ids_parts, dtype=object)
    if len(stage_ids) != len(cat_ids):
        raise RuntimeError(f"row-count mismatch Stage A={len(stage_ids)} catalog={len(cat_ids)}")
    h_stage, h_cat = seq_hash(stage_ids), seq_hash(cat_ids)
    if h_stage != h_cat:
        raise RuntimeError("Stage-A/catalog row-order hash mismatch; refusing positional join")
    stage_orig = np.concatenate(o_parts)
    mirror = np.concatenate(m_parts)
    stage_conf = np.maximum(np.concatenate(pcw_parts), np.concatenate(pccw_parts))
    del ids_parts, o_parts, m_parts, pcw_parts, pccw_parts

    # The production catalog, not the Stage-A shard export, defines the
    # science-sample hard label and confidence.  Stage A supplies the paired
    # mirror outcome.  Preserve and report their tiny disagreement explicitly.
    stage_production_disagreement = stage_orig != production_class
    stage_hc_all = (stage_orig != 0) & (stage_conf > 0.6)
    production_hc_all = (production_class != 0) & (production_conf > 0.6)
    base = production_class != 0
    ids = cat_ids[base]
    ra = ra_all[base]
    dec = dec_all[base]
    orig = production_class[base]
    stage_orig = stage_orig[base]
    stage_conf = stage_conf[base]
    mirror = mirror[base]
    conf = production_conf[base]
    pair_concordant = stage_orig == orig
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0))
    xyz = np.column_stack([
        np.cos(np.radians(dec)) * np.cos(np.radians(ra)),
        np.cos(np.radians(dec)) * np.sin(np.radians(ra)),
        np.sin(np.radians(dec)),
    ]).astype(np.float32)
    log(f"Stage-B base pool: {len(ids):,} released-production EQ spirals", t0)

    # Static strata.
    leg = np.full(len(ids), 1, dtype=np.int8)  # 0 BASS, 1 DECaLS, 2 DES
    leg[dec > 32.375] = 0
    des = (dec < -10.0) & (((ra >= 0) & (ra <= 60)) | ((ra >= 300) & (ra <= 360)))
    leg[des] = 2

    brick, obj = parse_keys(ids)
    morph = pq.read_table(MORPH)
    mbrick = np.asarray(morph["BRICKID"], dtype=np.int64)
    mobj = np.asarray(morph["OBJID"], dtype=np.int64)
    # DR8 OBJID is well below 1e7; composite integer is collision-free here.
    mi = match_sorted(brick * 10_000_000 + obj, mbrick * 10_000_000 + mobj)
    mok = mi >= 0
    ba = np.full(len(ids), np.nan, dtype=np.float32)
    fracdev = np.full(len(ids), np.nan, dtype=np.float32)
    shape_r = np.full(len(ids), np.nan, dtype=np.float32)
    if mok.any():
        typ = np.asarray(morph["TYPE"].to_pylist(), dtype=object)[mi[mok]]
        fd = np.asarray(morph["FRACDEV"], dtype=np.float32)[mi[mok]]
        use_dev = np.isin(typ, ["DEV", "COMP", "SER"]) | (fd >= 0.5)
        de1 = np.asarray(morph["SHAPEDEV_E1"], dtype=np.float32)[mi[mok]]
        de2 = np.asarray(morph["SHAPEDEV_E2"], dtype=np.float32)[mi[mok]]
        ee1 = np.asarray(morph["SHAPEEXP_E1"], dtype=np.float32)[mi[mok]]
        ee2 = np.asarray(morph["SHAPEEXP_E2"], dtype=np.float32)[mi[mok]]
        er = np.asarray(morph["SHAPEEXP_R"], dtype=np.float32)[mi[mok]]
        dr = np.asarray(morph["SHAPEDEV_R"], dtype=np.float32)[mi[mok]]
        emag = np.sqrt(np.where(use_dev, de1, ee1) ** 2 + np.where(use_dev, de2, ee2) ** 2)
        ba[mok] = (1.0 - emag) / (1.0 + emag)
        fracdev[mok] = fd
        shape_r[mok] = np.where(use_dev, dr, er)

    b_ra, b_dec, b_psf, b_depth = load_brick_metrics(t0)
    from scipy.spatial import cKDTree
    def sphere_xyz(r, d):
        rr, dd = np.radians(r), np.radians(d)
        cd = np.cos(dd)
        return np.column_stack([np.cos(rr) * cd, np.sin(rr) * cd, np.sin(dd)])
    tree = cKDTree(sphere_xyz(b_ra, b_dec))
    _, bi = tree.query(sphere_xyz(ra, dec), k=1, workers=-1)
    bok = np.ones(len(ids), dtype=bool)
    psf = b_psf[bi].astype(np.float32)
    depth = b_depth[bi].astype(np.float32)
    depth_q, depth_edges = quantile_group(depth, ["Q1", "Q2", "Q3", "Q4"])
    psf_q, psf_edges = quantile_group(psf, ["Q1", "Q2", "Q3", "Q4"])

    groups: dict[str, np.ndarray] = {}
    for cut in CUTS:
        groups[f"all_peq_gt_{cut:.1f}"] = (conf > cut) & pair_concordant
    # All canonical HC rows are pair-concordant.  Lower-confidence/full-pool
    # summaries exclude the small export seam instead of silently combining a
    # production original label with a discordant Stage-A mirror label.
    hc = (conf > 0.6) & pair_concordant
    for idx, name in enumerate(["BASS+MzLS", "DECaLS", "DES"]):
        groups[f"leg_{name}"] = hc & (leg == idx)
    groups["morph_edge_ba_lt_0.3"] = hc & np.isfinite(ba) & (ba < 0.3)
    groups["morph_face_ba_ge_0.5"] = hc & np.isfinite(ba) & (ba >= 0.5)
    groups["morph_fracdev_ge_0.5"] = hc & np.isfinite(fracdev) & (fracdev >= 0.5)
    groups["morph_fracdev_lt_0.5"] = hc & np.isfinite(fracdev) & (fracdev < 0.5)
    for q in range(4):
        groups[f"depth_Q{q+1}"] = hc & (depth_q == q)
        groups[f"psf_Q{q+1}"] = hc & (psf_q == q)

    # Reference counts and nulls use the original production-EQ spiral pool.
    refs, nulls = {}, {}
    for gi, (name, g) in enumerate(groups.items()):
        nt = np.bincount(pix[g], minlength=NPIX).astype(np.int64)
        refs[name] = nt
        nulls[name] = null_calibration(nt, SEED + 10_000 + gi)
    log(f"built {len(groups)} reference/null strata", t0)

    axes = fibonacci_axes(N_AXES)
    records = []
    for ai, axis in enumerate(axes):
        cosang = xyz @ axis.astype(np.float32)
        for aj, amp in enumerate(AMPLITUDES):
            rng = np.random.default_rng(SEED + ai * 1009 + aj * 9176)
            want = np.where(rng.random(len(ids)) < (0.5 + 0.5 * amp * cosang), 1, -1).astype(np.int8)
            choose_orig = want == orig
            out_class = np.where(choose_orig, orig, mirror)
            out_spiral = out_class != 0  # production NS triage
            out_cw = out_class == 1      # production hard argmax
            row = {"axis_index": ai, "axis_xyz": [float(x) for x in axis], "amplitude_injected": float(amp), "groups": {}}
            for name, g in groups.items():
                use = g & out_spiral
                nt = np.bincount(pix[use], minlength=NPIX).astype(np.int64)
                nc = np.bincount(pix[use & out_cw], minlength=NPIX).astype(np.int64)
                fit = fit_dipole(nt, nc)
                if fit.get("ok"):
                    vec = np.asarray(fit["vector"])
                    fit["projection_on_injected_axis"] = float(vec @ axis)
                    fit["amplitude_ratio"] = float(fit["amplitude"] / amp)
                    fit["angular_separation_deg"] = float(
                        np.degrees(np.arccos(np.clip((vec @ axis) / max(np.linalg.norm(vec), 1e-30), -1, 1)))
                    )
                    ncal = nulls[name]
                    fit["z_vs_reference_binomial_null"] = float((fit["amplitude"] - ncal["mean"]) / ncal["std_ddof1"])
                    fit["detected_gt_3sigma"] = bool(fit["z_vs_reference_binomial_null"] > 3.0)
                fit["n_selected"] = int(use.sum())
                fit["n_triaged_to_NS"] = int((g & ~out_spiral).sum())
                row["groups"][name] = fit
            records.append(row)
        log(f"axis {ai+1}/{N_AXES} complete", t0)

    # Aggregate every group over the deterministic axis battery.
    aggregates = {}
    for name in groups:
        by_amp = []
        for amp in AMPLITUDES:
            vals = [r["groups"][name] for r in records if r["amplitude_injected"] == float(amp)]
            z = np.array([v.get("z_vs_reference_binomial_null", np.nan) for v in vals])
            rec = np.array([v.get("amplitude", np.nan) for v in vals])
            proj = np.array([v.get("projection_on_injected_axis", np.nan) for v in vals])
            det = np.array([v.get("detected_gt_3sigma", False) for v in vals], dtype=float)
            by_amp.append({
                "amplitude_injected": float(amp),
                "n_axes": N_AXES,
                "detection_fraction_gt_3sigma": float(det.mean()),
                "recovered_amplitude_p16_p50_p84": [float(x) for x in np.nanquantile(rec, [0.16, 0.5, 0.84])],
                "signed_projection_p16_p50_p84": [float(x) for x in np.nanquantile(proj, [0.16, 0.5, 0.84])],
                "z_p16_p50_p84": [float(x) for x in np.nanquantile(z, [0.16, 0.5, 0.84])],
                "median_recovered_over_injected": float(np.nanmedian(rec / amp)),
            })
        def crossing(level: float):
            hit = [x["amplitude_injected"] for x in by_amp if x["detection_fraction_gt_3sigma"] >= level]
            return min(hit) if hit else None
        per_axis_cross = []
        for ai in range(N_AXES):
            hit = [r["amplitude_injected"] for r in records if r["axis_index"] == ai and r["groups"][name].get("detected_gt_3sigma")]
            per_axis_cross.append(min(hit) if hit else np.nan)
        finite = np.asarray(per_axis_cross, dtype=float)
        finite = finite[np.isfinite(finite)]
        aggregates[name] = {
            "reference_n": int(groups[name].sum()),
            "reference_null": nulls[name],
            "by_amplitude": by_amp,
            "A50_grid": crossing(0.50),
            "A95_grid": crossing(0.95),
            "per_axis_first_3sigma_crossing_p16_p50_p84": ([float(x) for x in np.quantile(finite, [0.16, 0.5, 0.84])] if len(finite) else None),
            "axes_without_3sigma_crossing": int(N_AXES - len(finite)),
        }

    payload = {
        "stage": "B-hybrid-paired-image-surrogate",
        "status": "complete",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "generator": "pipelines/p2_chirality/scripts/stage_b_hybrid_image_field_recovery.py",
        "scope": (
            "Discrete original-vs-mirror paired-image population intervention using precomputed Stage-A mirror outcomes; "
            "propagates the production catalog's EQ hard label and confidence through paired-member selection, NS triage, "
            "p_eq cuts, map making, and the canonical real-space estimator."
        ),
        "not_claimed": (
            "Not a continuous image transformation, not independently ground-truthed physical chirality, and not an unconditional physical calibration. "
            "The intervention conditions on the Stage-A EQ spiral label to identify the CW/CCW member of each mirror pair."
        ),
        "missing_inputs_for_unconditional_calibration": [
            "independent per-object true physical CW/CCW labels at full-catalog scale",
            "validated continuous morphology transform spanning realistic pitch angle/inclination/PSF/noise",
            "truth labels for Stage-A NS/NS pairs, so physical-spiral recall through NS triage cannot be measured",
        ],
        "config": {
            "nside": NSIDE,
            "min_pix_count_rule": f">= {MIN_PIX_COUNT}",
            "n_axes": N_AXES,
            "axis_rule": "deterministic Fibonacci sphere",
            "amplitudes": [float(x) for x in AMPLITUDES],
            "seed": SEED,
            "n_null_per_stratum": N_NULL,
            "p_eq_cuts": CUTS,
        },
        "integrity": {
            "n_catalog": int(len(cat_ids)),
            "n_stage_a": int(len(stage_ids)),
            "sequence_sha256_catalog": h_cat,
            "sequence_sha256_stage_a": h_stage,
            "sequence_match": True,
            "n_production_eq_spirals": int(base.sum()),
            "n_stage_a_vs_production_class_disagreements": int(stage_production_disagreement.sum()),
            "n_stage_a_vs_production_class_disagreements_within_production_spirals": int(
                (stage_orig != orig).sum()
            ),
            "n_pair_concordant_production_spirals_used": int(pair_concordant.sum()),
            "pair_concordant_fraction_of_production_spirals": float(pair_concordant.mean()),
            "n_stage_a_vs_production_class_disagreements_within_canonical_hc": int(
                ((stage_orig != orig) & (conf > 0.6)).sum()
            ),
            "n_pair_concordant_canonical_hc": int(((stage_orig == orig) & (conf > 0.6)).sum()),
            "discordant_pair_policy": (
                "Excluded from paired intervention aggregates; a forced production-orig/Stage-A-mirror "
                "mapping is not reported because its pair semantics are not defensible. Canonical HC has zero discordant rows."
            ),
            "hc_membership_seam": {
                "released_production_class_and_confidence_gt_0.6_canonical": int(production_hc_all.sum()),
                "stage_a_fresh_class_and_probability_gt_0.6_noncanonical": int(stage_hc_all.sum()),
                "noncanonical_minus_canonical": int(stage_hc_all.sum() - production_hc_all.sum()),
                "symmetric_difference_rows": int(np.logical_xor(stage_hc_all, production_hc_all).sum()),
                "adopted_for_all_stage_b_aggregates": "released production membership (canonical)",
            },
            "n_morphology_matched": int(mok.sum()),
            "n_brick_depth_psf_matched": int(bok.sum()),
        },
        "strata": {
            "imaging_leg_rule": "BASS+MzLS dec>32.375; DES dec<-10 and RA in [0,60] or [300,360]; else DECaLS",
            "depth_quartile_edges": depth_edges,
            "psf_quartile_edges": psf_edges,
            "morphology_available": ["b/a", "FRACDEV", "type-selected SHAPE_R"],
            "unavailable": ["per-object seeing/noise realization", "spectroscopic redshift", "independent physical chirality truth"],
        },
        "aggregates": aggregates,
        "trial_records": records,
        "failure_modes": [
            "Pair member is selected using the EQ output-defined handedness, so classifier correctness relative to nature is not tested.",
            "The Stage-A/released-production hard-label export seam is excluded from paired aggregates; no forced full-pool sensitivity is claimed.",
            "Mirror pairing is discrete; it does not test arbitrary physical morphology perturbations.",
            "Z2-TTA makes CW/CCW probability swapping nearly exact by construction, so the main value is testing selection/triage/footprint/estimator propagation.",
            "Twenty axes give detection fractions in increments of 0.05; A50/A95 are grid-level values, not smooth confidence limits.",
            "Null calibration is a fixed-count per-pixel p=0.5 binomial battery, not a label permutation and not a joint spatial nuisance likelihood.",
        ],
    }
    OUT.write_text(json.dumps(payload, indent=2))
    log(f"wrote {OUT}", t0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
