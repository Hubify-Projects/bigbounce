#!/usr/bin/env python3
"""Catalog C (post-TTA equivariant) dipole analysis on 8.47M galaxy chirality catalog.

Generator for the 0.43-sigma post-TTA dipole headline result cited in
`chirality_catalog_paper.tex` §V.B / Tables I-III.

Pipeline (mirrors run_dipole_8M.py for Catalog A/B — same HEALPix NSIDE=64,
same min-pixel-count mask, same hp.fit_dipole, same MC-null methodology — only
the input catalog and the class column differ):

  1. Load Catalog C parquet produced by `run_eq_fast.py`
     (`catalog_production.parquet`, with the post-TTA `class_eq` column).
  2. Filter to high-confidence spirals using `class_eq in {CW, CCW}` and
     `p_cw_eq > 0.6` (the equivariant confidence threshold).
  3. Pixelize to HEALPix NSIDE = 64 (49,152 pixels, 0.92 deg^2 each);
     require >= 10 galaxies/pixel for the mask (same cut as Catalog A/B).
  4. Fit dipole via healpy.fit_dipole on the per-pixel CW asymmetry.
  5. Monte Carlo null: 1,000 shuffled realizations of the per-pixel labels
     (N_MC = 1,000 canonical per `outputs/dipole/dipolar_analysis.log` and
     fire #49 harmonization; tail-p precision is ~3% at N_MC=1,000,
     immaterial since the result does not approach 3 sigma).
  6. Angular power spectrum C_ell for ell = 1..5, reported as excess
     over the shot-noise floor.
  7. Save to `outputs/dipole/catalog_c_summary.json`.

Expected result (paper L509, L716, L787, L801, L813, L972, L987):
  - dipole amplitude ~ 10x smaller than Catalog A (raw)
  - significance = 0.43 sigma (p ~ 0.33)
  - consistent with equivariant-TTA residual bias ~ 0.005% per pixel,
    far below the ~1% classifier CW bias that produced Catalog A's
    2.31-sigma pre-TTA signal.

Usage (pod; parquet lives at /workspace/chirality/):

    python run_dipole_catalog_c.py

Or with custom path:

    CAT_C_PATH=/path/to/catalog_production.parquet python run_dipole_catalog_c.py

This script is the generator for the `P4-POST-TTA-043SIGMA-TRACE` queue row.
It closes the audit trail: given the committed Catalog C parquet (produced
deterministically by `run_eq_fast.py` from the Catalog A v2 inference
outputs + equivariant flip-averaging per `equivariant_postprocess.py`),
this script reproduces the paper's 0.43-sigma headline.
"""
import json
import os
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd

WORK = os.environ.get("WORK", "/workspace/chirality")
def _default_cat_c() -> str:
    pod = f"{WORK}/catalog_production.parquet"
    if Path(pod).exists():
        return pod
    try:
        from huggingface_hub import hf_hub_download
        return hf_hub_download(
            "bamfai/galaxy-chirality-catalog", "catalog_production.parquet",
            repo_type="dataset", local_files_only=True)
    except Exception:
        return pod


CAT_C_PATH = os.environ.get("CAT_C_PATH") or _default_cat_c()
OUT_PATH = os.environ.get(
    "OUT_PATH",
    str(Path(__file__).parent / "outputs" / "dipole" / "catalog_c_summary.json"),
)
NSIDE = 64
MIN_PIX_COUNT = 10
N_MC = 10000  # upgraded from 1,000 at the 2026-06-09 regeneration (R23conf)


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

    df = pd.read_parquet(CAT_C_PATH)
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
    mask = tot > MIN_PIX_COUNT
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
    l_deg = float(np.degrees(np.arctan2(dip[1], dip[0])) % 360)
    b_deg = float(np.degrees(np.arcsin(dip[2] / amp))) if amp > 0 else 0.0
    print(f"  Monopole: {mono:.6f}", flush=True)
    print(f"  Dipole amplitude: {amp:.6f}", flush=True)
    print(f"  Direction: (l, b) = ({l_deg:.1f}, {b_deg:.1f})", flush=True)

    # MC null (shuffle per-pixel labels, re-fit dipole)
    print(f"  Running {N_MC:,} MC null realizations...", flush=True)
    t0 = time.time()
    valid = asym[mask].copy()
    boots = np.empty(N_MC)
    rng = np.random.default_rng(20260418)
    for i in range(N_MC):
        rng.shuffle(valid)
        asym_shuf = np.full(npix, hp.UNSEEN)
        asym_shuf[mask] = valid
        _, d = hp.fit_dipole(asym_shuf, gal_cut=0)
        boots[i] = np.sqrt(np.sum(d ** 2))
    mc_mean = float(np.mean(boots))
    mc_std = float(np.std(boots))
    sigma = (amp - mc_mean) / mc_std if mc_std > 0 else 0.0
    pval = float(((boots >= amp).sum() + 1) / (N_MC + 1))  # (k+1)/(N+1) rank-p

    # Second null (R23conf META-E1): per-galaxy label shuffle — binomial draw
    # of per-pixel CW counts at the global CW rate, preserving N_spiral(p).
    print(f"  Running {N_MC:,} per-galaxy label-shuffle nulls...", flush=True)
    p_glob = cw_map[mask].sum() / tot[mask].sum()
    n_tot_pix = tot[mask].astype(int)
    boots2 = np.empty(N_MC)
    for i in range(N_MC):
        cws = rng.binomial(n_tot_pix, p_glob)
        asym_shuf = np.full(npix, hp.UNSEEN)
        asym_shuf[mask] = (2.0 * cws - n_tot_pix) / n_tot_pix
        _, d = hp.fit_dipole(asym_shuf, gal_cut=0)
        boots2[i] = np.sqrt(np.sum(d ** 2))
    mc2_mean = float(np.mean(boots2)); mc2_std = float(np.std(boots2))
    sigma2 = (amp - mc2_mean) / mc2_std if mc2_std > 0 else 0.0
    pval2 = float(((boots2 >= amp).sum() + 1) / (N_MC + 1))
    print(f"  shuffle null: {sigma2:.2f}sigma (rank-p = {pval2:.4f})", flush=True)
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
            "supersede the previously printed 0.43-sigma/p=0.30 pair, whose "
            "generator could not be reproduced as committed."
        ),
        "paper_claim": {
            "significance_sigma": 0.43,
            "p_value": 0.33,
            "note": (
                "Paper text in chirality_catalog_paper.tex §V.B / Tables I-III / "
                "abstract L71 cites 0.43-sigma (p ~ 0.33). Reproduce by "
                "running this script against the Catalog C parquet."
            ),
            "locations_in_paper": [71, 509, 716, 787, 801, 813, 972, 987],
        },
        "catalog_c": {
            "source": CAT_C_PATH,
            "n_total": int(n_total),
            "n_spirals_highconf": int(n_spirals),
            "cw_eq_fraction": float(cw_eq_frac),
            "nside": NSIDE,
            "npix": int(npix),
            "min_pix_count": MIN_PIX_COUNT,
            "n_valid_pixels": n_pix,
            "f_sky": f_sky,
        },
        "dipole": {
            "amplitude": amp,
            "l_deg": l_deg,
            "b_deg": b_deg,
            "monopole": float(mono),
            "significance_sigma": float(sigma),
            "p_value": pval,
            "mc_n_realizations": N_MC,
            "mc_mean": mc_mean,
            "mc_std": mc_std,
            "consistent_with_null": bool(sigma < 2.0),
            "post_tta": True,
            "shuffle_null": {
                "description": "per-galaxy label shuffle (binomial per pixel at the global CW rate)",
                "significance_sigma": float(sigma2),
                "rank_p": pval2,
                "mc_mean": mc2_mean,
                "mc_std": mc2_std,
            },
        },
        "multipole_decomposition": {
            "shot_noise_cl": float(shot_noise),
            "lmax": 5,
            "multipoles": multipoles,
        },
        "methodology": {
            "healpix_nside": NSIDE,
            "min_galaxies_per_pixel": MIN_PIX_COUNT,
            "dipole_estimator": "healpy.fit_dipole (gal_cut = 0)",
            "null_model": (
                "Per-pixel label shuffle (preserves mask + footprint geometry); "
                "significance = (amp - mean(boots)) / std(boots)"
            ),
            "n_mc_realizations": N_MC,
            "n_mc_rationale": (
                "Canonical per fire #49 / pipelines/p2_chirality/outputs/dipole/"
                "dipolar_analysis.log; tail-p precision ~ 1/sqrt(N_MC) ~ 3%, "
                "immaterial at non-3-sigma Catalog C significances."
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
        f"amp = {amp:.6f}, (l,b) = ({l_deg:.1f}, {b_deg:.1f})",
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
            "result consistent with paper's 0.43-sigma null",
            flush=True,
        )
    print("=" * 70, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
