#!/usr/bin/env python3
"""Recompute the P3 spatial-uniformity chi^2 on the post-excision 377,482 set.

Closure of the pod-gated item in
project-context/peer-reviews/INT_v3/P3_erosita_closure_2026-07-07.md:
the shipped chi^2 (376,713) was computed on the full inclusive 378,280 set that
still folded in the now-excised 500 Gaia synthetic + 298 eROSITA singletons. The
paper states the exact recompute for the 377,482 headline set was not possible
"here without fabricating" because the pod-side LAMOST positions (~113k) were not
committed locally.

They ARE reachable: the HuggingFace dataset bamfai/bigbounce-anomaly-catalog ships
pathc_unique_objects.parquet with per-object ra_mean/dec_mean AND survey provenance
(survey_list / best_survey), including all 108,963 lamost_dr10 positions. This script
reproduces the pod chi^2 method EXACTLY (NSIDE=64 HEALPix; uniform mean over occupied
pixels; chi^2 = sum (n-nbar)^2/nbar) and:

  1. VALIDATES against the pod reference: reconstruct the 7way_headline no-ACT set
     (378,280 = 8-way-incl-ACT 378,480 minus 200 ACT) and confirm chi^2 == 376,713.
  2. RECOMPUTES on the excised headline set (377,482 = 378,280 minus 500 Gaia
     minus 298 eROSITA).

No value is invented; the number falls out of the exact committed arithmetic.
"""
import json
import sys
from pathlib import Path
from glob import glob

import numpy as np
import pandas as pd
import healpy as hp

NSIDE = 64

# Locate the HF-cached Path-C unique-objects parquet (8-way incl ACT).
cands = sorted(glob(str(Path.home() /
    ".cache/huggingface/hub/datasets--bamfai--bigbounce-anomaly-catalog/"
    "snapshots/*/pathc_unique_objects.parquet")))
if not cands:
    sys.exit("FATAL: HF-cached pathc_unique_objects.parquet not found.")
PARQUET = cands[-1]

df = pd.read_parquet(PARQUET, columns=["ra_mean", "dec_mean", "survey_list", "best_survey"])
print(f"loaded {len(df):,} rows from {PARQUET}")


def chi2_of(sub, tag):
    """Exact pod method: NSIDE=64, uniform mean over occupied pixels, Poisson var."""
    pix = hp.ang2pix(NSIDE, sub["ra_mean"].to_numpy(),
                     sub["dec_mean"].to_numpy(), lonlat=True)
    counts = np.bincount(pix, minlength=hp.nside2npix(NSIDE))
    occ = counts[counts > 0]
    nbar = occ.mean()
    chi2 = float(((occ - nbar) ** 2 / nbar).sum())
    dof = int(len(occ) - 1)
    res = {
        "n_objects": int(len(sub)),
        "n_occupied_pixels": int(len(occ)),
        "n_total_pixels": int(hp.nside2npix(NSIDE)),
        "nbar_per_occupied_pixel": float(nbar),
        "chi2": chi2,
        "dof": dof,
        "chi2_reduced": float(chi2 / dof),
    }
    print(f"  {tag:22s} n={len(sub):>7,} occ={len(occ):>6,} "
          f"chi2={chi2:>12,.2f} chi2_nu={chi2/dof:6.3f}")
    return res


# survey membership is by best_survey (each cluster's dominant survey); the
# singletons excised (Gaia 500, eROSITA 298) are pure single-survey clusters,
# so best_survey == survey_list for them (verified: survey_list value_counts).
is_act = df["best_survey"].eq("act_dr6")
is_gaia = df["best_survey"].eq("gaia_dr3")
is_ero = df["best_survey"].eq("erosita_dr1")

print(f"\ncounts by best_survey: ACT={is_act.sum()}, "
      f"Gaia={is_gaia.sum()}, eROSITA={is_ero.sum()}")

# 1. Reproduce the 7way_headline no-ACT reference set (378,280).
no_act = df[~is_act]
print("\n== VALIDATION: reproduce pod 7way_headline (no-ACT, expect chi2=376,713) ==")
ref = chi2_of(no_act, "7way_headline_no_act")
POD_REF_CHI2 = 376713.1413133129
POD_REF_N = 378280
ok_n = len(no_act) == POD_REF_N
ok_chi2 = abs(ref["chi2"] - POD_REF_CHI2) < 1.0
print(f"  match n_objects=={POD_REF_N}: {ok_n}  (got {len(no_act):,})")
print(f"  match chi2=={POD_REF_CHI2:.4f}: {ok_chi2}  "
      f"(delta={ref['chi2']-POD_REF_CHI2:+.4f})")

# 2. Recompute on the excised headline set (377,482 = no-ACT minus Gaia minus eROSITA).
excised = df[~is_act & ~is_gaia & ~is_ero]
print("\n== RECOMPUTE: excised headline set (expect n=377,482) ==")
new = chi2_of(excised, "377482_excised")
ok_excised_n = len(excised) == 377482
print(f"  match n_objects==377,482: {ok_excised_n}  (got {len(excised):,})")

validated = ok_n and ok_chi2 and ok_excised_n
out = {
    "script": "scripts/recompute_spatial_chi2_excised.py",
    "purpose": "Exact spatial-uniformity chi^2 on the 377,482 post-excision "
               "(Gaia-500 + eROSITA-298 removed) headline set, closing the "
               "pod-gated item in INT_v3/P3_erosita_closure_2026-07-07.md.",
    "data_source": PARQUET,
    "data_source_note": "HuggingFace bamfai/bigbounce-anomaly-catalog "
                        "pathc_unique_objects.parquet; per-object ra_mean/dec_mean "
                        "+ survey provenance incl. all LAMOST DR10 positions. "
                        "NOT fabricated; positions are the committed catalog.",
    "method": "NSIDE=64 HEALPix; uniform mean over OCCUPIED pixels; "
              "chi^2 = sum (n-nbar)^2/nbar (Poisson variance). "
              "Identical to r24conf_pod_session_batch.py item #35.",
    "validation_against_pod": {
        "reference": "r24conf_pod_session_batch.json item35 7way_headline",
        "pod_chi2": POD_REF_CHI2,
        "pod_n_objects": POD_REF_N,
        "reproduced_chi2": ref["chi2"],
        "reproduced_n_objects": ref["n_objects"],
        "n_match": ok_n,
        "chi2_match_within_1": ok_chi2,
    },
    "excised_set_377482": new,
    "prior_shipped_chi2_on_inclusive_378280": POD_REF_CHI2,
    "delta_chi2_vs_inclusive": new["chi2"] - POD_REF_CHI2,
    "validated": validated,
}
outp = Path(__file__).resolve().parents[1] / "outputs" / "spatial_chi2_excised_377482.json"
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2))
print(f"\nwrote {outp}")
print(f"VALIDATED={validated}")
