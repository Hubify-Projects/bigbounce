#!/usr/bin/env python3
"""Catalog C (post-TTA equivariant) dipole analysis on 8.47M galaxy chirality catalog.

Generator for the canonical inclusive-mask post-TTA dipole result cited in
`chirality_catalog_paper.tex` §V.B / Tables I-III.

Pipeline (mirrors run_dipole_8M.py for Catalog A/B — same HEALPix NSIDE=64,
same min-pixel-count mask, same hp.fit_dipole, same MC-null methodology — only
the input catalog and the class column differ):

  1. Load Catalog C parquet produced by `run_eq_fast.py`
     (`catalog_production.parquet`, with the post-TTA `class_eq` column).
  2. Filter to high-confidence spirals using `class_eq in {CW, CCW}` and
     `p_cw_eq > 0.6` (the equivariant confidence threshold).
  3. Pixelize to HEALPix NSIDE = 64 (49,152 pixels, 0.92 deg^2 each);
     retain pixels with N_spiral >= 10 (inclusive, matching the paper contract).
  4. Fit dipole via healpy.fit_dipole on the per-pixel CW asymmetry.
  5. Monte Carlo null: 10,000 shuffled realizations of the per-pixel labels,
     with the exact array retained for rank and moment reproducibility.
  6. Angular power spectrum C_ell for ell = 1..5, reported as excess
     over the shot-noise floor.
  7. Save the primary JSON and exact 10,000-element pixel-permutation null
     array to `outputs/dipole/catalog_c_summary.json` and
     `outputs/canonical_provenance/c12_queue2_null_amps_10k.npy`.

Expected result:
  - dipole amplitude ~ 10x smaller than Catalog A (raw)
  - significance = +0.549 sigma; one-sided upper-tail rank p = 0.26517
  - consistent with equivariant-TTA residual bias ~ 0.005% per pixel,
    far below the ~1% classifier CW bias that produced Catalog A's
    2.31-sigma pre-TTA signal.

Usage (pod; parquet lives at /workspace/chirality/):

    python run_dipole_catalog_c.py

Or with custom path:

    CAT_C_PATH=/path/to/catalog_production.parquet python run_dipole_catalog_c.py

This script closes the primary audit trail: given the committed Catalog C
parquet (produced
deterministically by `run_eq_fast.py` from the Catalog A v2 inference
outputs + equivariant flip-averaging per `equivariant_postprocess.py`),
this script reproduces the paper's inclusive-mask headline.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd

DATASET_REPO_ID = "bamfai/galaxy-chirality-catalog"
DATASET_REPO_TYPE = "dataset"
DATASET_FILENAME = "catalog_production.parquet"
DATASET_REVISION = "a21eb596fd10edb9af9e7a1bcefb04f87327a724"
DATASET_SHA256 = "e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563"
DATASET_BYTES = 952_115_239
NULL_ARTIFACT = (
    "pipelines/p2_chirality/outputs/canonical_provenance/"
    "c12_queue2_null_amps_10k.npy"
)

WORK = os.environ.get("WORK", "/workspace/chirality")


def _default_cat_c() -> str:
    pod = f"{WORK}/catalog_production.parquet"
    if Path(pod).exists():
        return pod
    try:
        from huggingface_hub import hf_hub_download
        return hf_hub_download(
            DATASET_REPO_ID,
            DATASET_FILENAME,
            repo_type=DATASET_REPO_TYPE,
            revision=DATASET_REVISION,
        )
    except Exception:
        return pod


CAT_C_PATH = os.environ.get("CAT_C_PATH") or _default_cat_c()
OUT_PATH = os.environ.get(
    "OUT_PATH",
    str(Path(__file__).parent / "outputs" / "dipole" / "catalog_c_summary.json"),
)
NULL_PATH = os.environ.get(
    "NULL_PATH",
    str(
        Path(__file__).parent
        / "outputs"
        / "canonical_provenance"
        / "c12_queue2_null_amps_10k.npy"
    ),
)
NSIDE = 64
MIN_PIX_COUNT = 10
N_MC = 10000  # upgraded from 1,000 at the 2026-06-09 regeneration (R23conf)
MC_SEED = 20260418
SECONDARY_N_MC = int(os.environ.get("SECONDARY_N_MC", "0"))


def sha256_file(path: str | Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        while chunk := fh.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    print("=" * 70, flush=True)
    print("CATALOG C (POST-TTA) DIPOLE ANALYSIS", flush=True)
    print("=" * 70, flush=True)

    print(f"Loading Catalog C from {CAT_C_PATH}...", flush=True)
    if not Path(CAT_C_PATH).exists():
        print(f"ERROR: {CAT_C_PATH} not found", flush=True)
        print(
            "This script is pod-runnable — the parquet is produced by "
            "`run_eq_fast.py` from the 8.47M v2 inference catalog. "
            "Expected columns: class_eq (CW/CCW/NOT_SPIRAL), p_cw_eq, ra, dec.",
            flush=True,
        )
        return 1

    source_sha256 = sha256_file(CAT_C_PATH)
    if source_sha256 != DATASET_SHA256:
        raise ValueError(
            "Catalog content hash mismatch: "
            f"expected {DATASET_SHA256}, got {source_sha256}"
        )
    if Path(CAT_C_PATH).stat().st_size != DATASET_BYTES:
        raise ValueError(
            "Catalog byte-count mismatch: "
            f"expected {DATASET_BYTES}, got {Path(CAT_C_PATH).stat().st_size}"
        )

    # Project only the five columns used by the primary estimator.  This keeps
    # the exact calculation local and avoids materializing unrelated catalog
    # columns from the 8,474,531-row Parquet release.
    df = pd.read_parquet(
        CAT_C_PATH,
        columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"],
    )
    n_total = len(df)
    print(f"  {n_total:,} galaxies loaded", flush=True)

    # High-confidence equivariant spirals
    # SELECTION FIX (2026-06-09, R23conf META-E1 closure): the previous filter
    # `df["p_cw_eq"].abs() > 0.6` selected only CW-confident galaxies (a
    # degenerate all-CW sample, 471,049 rows on the released parquet) and could
    # not have produced a meaningful dipole. The high-confidence cut is on the
    # WINNING class probability:
    if "p_cw_eq" in df.columns and "p_ccw_eq" in df.columns:
        conf = np.maximum(df["p_cw_eq"].values, df["p_ccw_eq"].values) > 0.6
    else:
        conf = df.get("confidence", pd.Series(np.ones(n_total, dtype=bool))) > 0.6

    spirals = df[
        (df["class_eq"].isin(["CW", "CCW"]))
        & conf
        & (df["ra"].notna())
    ]
    n_spirals = len(spirals)
    cw_eq_frac = (spirals["class_eq"] == "CW").mean()
    print(f"  High-conf equivariant spirals: {n_spirals:,}", flush=True)
    print(f"  CW fraction (post-TTA): {cw_eq_frac:.4f}", flush=True)

    # HEALPix binning
    npix = hp.nside2npix(NSIDE)
    cw_map = np.zeros(npix)
    ccw_map = np.zeros(npix)
    theta = np.radians(90 - spirals["dec"].values)
    phi = np.radians(spirals["ra"].values % 360)
    pix = hp.ang2pix(NSIDE, theta, phi)
    is_cw = (spirals["class_eq"] == "CW").values
    np.add.at(cw_map, pix, is_cw.astype(float))
    np.add.at(ccw_map, pix, (~is_cw).astype(float))

    tot = cw_map + ccw_map
    # Canonical primary contract: inclusive N_spiral(p) >= 10.  Versions
    # through v1.0.242 accidentally executed the strict >10 mask; that result
    # is retained only in the explicitly historical sensitivity artifacts.
    mask = tot >= MIN_PIX_COUNT
    asym = np.zeros(npix)
    asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot[mask]
    n_pix = int(mask.sum())
    f_sky = n_pix / npix
    print(f"  Pixels used: {n_pix}/{npix} (f_sky = {f_sky:.4f})", flush=True)

    # Dipole fit
    asym_full = np.full(npix, hp.UNSEEN)
    asym_full[mask] = asym[mask]
    mono, dip = hp.fit_dipole(asym_full, gal_cut=0)
    amp = float(np.sqrt(np.sum(dip ** 2)))
    ra_deg = float(np.degrees(np.arctan2(dip[1], dip[0])) % 360)
    dec_deg = float(np.degrees(np.arcsin(dip[2] / amp))) if amp > 0 else 0.0
    print(f"  Monopole: {mono:.6f}", flush=True)
    print(f"  Dipole amplitude: {amp:.6f}", flush=True)
    print(
        f"  Equatorial direction: (RA, Dec) = ({ra_deg:.1f}, {dec_deg:.1f}) deg",
        flush=True,
    )

    # MC null (shuffle per-pixel labels, re-fit dipole)
    reuse_primary_null = os.environ.get("REUSE_PRIMARY_NULL", "0") == "1"
    print(f"  Running {N_MC:,} MC null realizations...", flush=True)
    t0 = time.time()
    valid = asym[mask].copy()
    if reuse_primary_null:
        boots = np.load(NULL_PATH)
        if boots.shape != (N_MC,):
            raise ValueError(
                f"Reusable primary null has shape {boots.shape}; expected {(N_MC,)}"
            )
        print(f"  Reused completed exact primary null: {NULL_PATH}", flush=True)
    else:
        boots = np.empty(N_MC)
        rng = np.random.default_rng(MC_SEED)
        for i in range(N_MC):
            rng.shuffle(valid)
            asym_shuf = np.full(npix, hp.UNSEEN)
            asym_shuf[mask] = valid
            _, d = hp.fit_dipole(asym_shuf, gal_cut=0)
            boots[i] = np.sqrt(np.sum(d ** 2))
    mc_mean = float(np.mean(boots))
    mc_std = float(np.std(boots))
    sigma = (amp - mc_mean) / mc_std if mc_std > 0 else 0.0
    rank_k = int((boots >= amp).sum())
    pval = float((rank_k + 1) / (N_MC + 1))

    Path(NULL_PATH).parent.mkdir(parents=True, exist_ok=True)
    np.save(NULL_PATH, boots)
    null_sha256 = sha256_file(NULL_PATH)

    # Second null (R23conf META-E1): per-galaxy label shuffle — binomial draw
    # of per-pixel CW counts at the global CW rate, preserving N_spiral(p).
    shuffle_null = {
        "status": "not_run_in_v1.0.243_bounded_primary_regeneration",
        "reason": "Secondary diagnostic; not part of the requested canonical pixel-permutation primary.",
    }
    if SECONDARY_N_MC > 0:
        print(
            f"  Running {SECONDARY_N_MC:,} per-galaxy label-shuffle nulls...",
            flush=True,
        )
        rng2 = np.random.default_rng(MC_SEED)
        p_glob = cw_map[mask].sum() / tot[mask].sum()
        n_tot_pix = tot[mask].astype(int)
        boots2 = np.empty(SECONDARY_N_MC)
        for i in range(SECONDARY_N_MC):
            cws = rng2.binomial(n_tot_pix, p_glob)
            asym_shuf = np.full(npix, hp.UNSEEN)
            asym_shuf[mask] = (2.0 * cws - n_tot_pix) / n_tot_pix
            _, d = hp.fit_dipole(asym_shuf, gal_cut=0)
            boots2[i] = np.sqrt(np.sum(d ** 2))
        mc2_mean = float(np.mean(boots2)); mc2_std = float(np.std(boots2))
        sigma2 = (amp - mc2_mean) / mc2_std if mc2_std > 0 else 0.0
        pval2 = float(
            ((boots2 >= amp).sum() + 1) / (SECONDARY_N_MC + 1)
        )
        shuffle_null = {
            "status": "diagnostic",
            "description": "per-galaxy label shuffle (binomial per pixel at the global CW rate)",
            "n_realizations": SECONDARY_N_MC,
            "seed": MC_SEED,
            "significance_sigma": float(sigma2),
            "rank_p": pval2,
            "mc_mean": mc2_mean,
            "mc_std": mc2_std,
        }
        print(
            f"  shuffle null: {sigma2:.2f}sigma (rank-p = {pval2:.4f})",
            flush=True,
        )
    print(
        f"  MC null ({time.time()-t0:.0f}s): {sigma:.2f}sigma "
        f"(p = {pval:.4f}, mean = {mc_mean:.6f}, std = {mc_std:.6f})",
        flush=True,
    )

    # Angular power spectrum C_ell for ell = 1..5
    print("  Computing C_ell (lmax = 5)...", flush=True)
    cl = hp.anafast(asym_full, lmax=5)
    shot_noise = 1.0 / np.mean(tot[mask]) if mask.any() else 0.0
    multipoles = [
        {
            "l": int(ll),
            "Cl": float(cl[ll]),
            "excess_over_shot_noise": float(max(0.0, cl[ll] - shot_noise)),
        }
        for ll in range(len(cl))
    ]

    # Save
    out: dict = {
        "experiment": "Paper 4 Catalog C Dipolar Analysis (post-TTA)",
        "generator": "pipelines/p2_chirality/run_dipole_catalog_c.py",
        "regeneration_note_2026_06_09": (
            "Anchor regenerated during R23conf after the selection-filter "
            "defect above was found; the values in dipole_fit/mc_null below "
            "supersede the previously printed 0.43-sigma/p=0.30 pair and the "
            "later strict-mask +0.41-sigma result, whose "
            "generator could not be reproduced as committed."
        ),
        "paper_claim": {
            "role": "single primary observed-label estimator",
            "significance_sigma": float(sigma),
            "rank_p_one_sided_upper_tail": pval,
            "note": (
                "Canonical inclusive-mask values for P4 v1.0.243. Reproduce "
                "by running this generator against the exact catalog release."
            ),
        },
        "catalog_c": {
            "source": {
                "provider": "huggingface",
                "repo_id": DATASET_REPO_ID,
                "repo_type": DATASET_REPO_TYPE,
                "filename": DATASET_FILENAME,
                "revision": DATASET_REVISION,
                "sha256": source_sha256,
                "bytes": DATASET_BYTES,
            },
            "n_total": int(n_total),
            "n_spirals_highconf": int(n_spirals),
            "cw_eq_fraction": float(cw_eq_frac),
            "nside": NSIDE,
            "npix": int(npix),
            "min_pix_count": MIN_PIX_COUNT,
            "min_pix_count_operator": ">=",
            "n_valid_pixels": n_pix,
            "f_sky": f_sky,
        },
        "dipole": {
            "amplitude": amp,
            "direction_frame": "equatorial (catalog RA/Dec basis)",
            "equatorial_ra_deg": ra_deg,
            "equatorial_dec_deg": dec_deg,
            "monopole": float(mono),
            "significance_sigma": float(sigma),
            "rank_p_one_sided_upper_tail": pval,
            "rank_formula": "(k+1)/(N+1), k = count(A_null >= A_data)",
            "rank_k": rank_k,
            "rank_N": N_MC,
            "mc_n_realizations": N_MC,
            "mc_seed": MC_SEED,
            "mc_mean": mc_mean,
            "mc_std": mc_std,
            "mc_std_ddof": 0,
            "null_array": NULL_ARTIFACT,
            "null_array_sha256": null_sha256,
            "consistent_with_null": bool(sigma < 2.0),
            "post_tta": True,
            "shuffle_null": shuffle_null,
        },
        "multipole_decomposition": {
            "shot_noise_cl": float(shot_noise),
            "lmax": 5,
            "multipoles": multipoles,
        },
        "methodology": {
            "healpix_nside": NSIDE,
            "min_galaxies_per_pixel": MIN_PIX_COUNT,
            "min_galaxies_per_pixel_operator": ">=",
            "dipole_estimator": "healpy.fit_dipole (gal_cut = 0)",
            "null_model": (
                "Per-pixel label shuffle (preserves mask + footprint geometry); "
                "significance = (amp - mean(boots)) / std(boots)"
            ),
            "n_mc_realizations": N_MC,
            "rng": "numpy.random.default_rng",
            "rng_seed": MC_SEED,
            "n_mc_rationale": (
                "Exact 10,000-realization primary array retained for rank and "
                "moment reproducibility; the result is far from a discovery tail."
            ),
        },
    }
    Path(OUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"\nSaved: {OUT_PATH}", flush=True)

    print("\n" + "=" * 70, flush=True)
    print("CATALOG C DIPOLE SUMMARY (post-TTA)", flush=True)
    print("=" * 70, flush=True)
    print(
        f"  Cat C (equivariant): {sigma:.2f}sigma, "
        f"amp = {amp:.6f}, equatorial (RA,Dec) = "
        f"({ra_deg:.1f}, {dec_deg:.1f}) deg",
        flush=True,
    )
    if sigma > 3:
        print("  *** SIGNIFICANT DIPOLE (post-TTA) — ", flush=True)
        print("      Investigate: equivariance correction failed", flush=True)
    elif sigma > 2:
        print("  ** Marginal post-TTA signal", flush=True)
    else:
        print(
            "  No significant post-TTA dipole — "
            "equivariance correction successful; "
            "result consistent with the canonical inclusive-mask null",
            flush=True,
        )
    print("=" * 70, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
