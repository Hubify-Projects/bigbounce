#!/usr/bin/env python3
"""
Reproduce the P3 VALIDATED catalog-grade headline count (5" positional dedup).
=============================================================================
Reviewer demand (RS22, Grok + Gemini): the validated catalog-grade headline
must be RECOMPUTABLE end-to-end from the committed per-survey validated lists —
not stated as an asserted lower bound obtained by subtraction.

This script takes the committed per-survey VALIDATED lists, applies the exact
5-arcsec positional deduplication used throughout the paper, and emits the
exact validated headline count. It is the validated-tier analogue of the
recommended-tier reproducer sixway_dedup.py.

VALIDATED TIER MEMBERSHIP (RS22 directives 1, 2, 4)
---------------------------------------------------
The validated catalog-grade subset is the set of surveys that pass, or (for
NEOWISE) supply the geometry-QA analogue of, an injection-recovery /
detector-sensitivity gate:

    DESI DR1   195,829   (S > 5 fixed canonical-S cut)
    SDSS DR18   77,905   (fixed-size continuity slice)
    Planck CMB     200   (top-1% map patches)
    NEOWISE        419   (top-1%, Path-C ecliptic-pole masked)

EXCLUDED from the validated tier, and therefore from this count:
  * Gaia DR3   (directive 1) — the committed output is a synthetic-placeholder
    fallback (generate_synthetic_gaia(); see gaia_provenance_audit.py). It is
    non-reproducible against real Gaia DR3 and is DROPPED entirely. A real Gaia
    tier is deferred to future work.
  * eROSITA DR1 (directive 2) — demoted to a reproducible top-298 MEMBERSHIP
    list only (erosita_membership_reproduce.py). Its per-object S_BigAE score
    axis is non-reproducible (Spearman rho <= -0.10 across rescalings), so it
    contributes NO score-dependent statistics and is NOT in the validated
    headline count. Membership is reproducible; the score axis is not.
  * LAMOST DR10 (directive 4) — 98% blue-excess training-bias artifact,
    injection-recovery gate FAIL. Reported only as a methodological lesson;
    excluded from the validated total. This script never loads it.
  * ACT DR6 — cross-transfer quarantine; contributes zero objects.

ALGORITHM (identical to sixway_dedup.py)
----------------------------------------
1. Load the 4 validated surveys, normalize to (survey, source_id, ra, dec).
2. Apply the NEOWISE Path-C ecliptic-pole mask inline (|ecliptic_lat| < 80 deg)
   so the 419 is reproduced from the 436-row raw block, not assumed.
3. Build astropy SkyCoord, search_around_sky(self, self, 5") -> pairs <= 5".
4. Union-find (friends-of-friends) -> clusters = unique physical objects.
5. Emit the exact validated headline count + per-survey / per-pair breakdown.

The headline reported in the paper is this exact recomputed unique count.
NO subtraction bound; NO synthetic data; NO score-axis dependence.

DATA SOURCE (canonical, reproducible)
-------------------------------------
Per-object catalogs are the released HuggingFace dataset
    bamfai/bigbounce-anomaly-catalog
staged into ../hf_staging/ (gitignored) on first run (HF_TOKEN from
repo-root .env.local). DESI falls back to the committed in-repo CSV
    pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.csv
if HF is unreachable.

OUTPUT
------
    ../outputs/reproduce_headline_dedup.json

Deterministic: no randomness. Re-runnable.

Run
---
    python3 pipelines/p3_anomaly_engine/scripts/reproduce_headline_dedup.py
"""
import json
import os
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord, search_around_sky
import astropy.units as u

HERE = Path(__file__).resolve().parent
P3 = HERE.parent
REPO = P3.parents[1]
STAGE = P3 / "hf_staging"
OUT_DIR = P3 / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MATCH_RADIUS_ARCSEC = 5.0
NEOWISE_ELAT_CUT_DEG = 80.0  # reject |ecliptic_lat| >= 80 (Path-C pole mask)

HF_REPO = "bamfai/bigbounce-anomaly-catalog"

# VALIDATED-tier surveys ONLY. Gaia + eROSITA + LAMOST + ACT are excluded.
# (survey, hf_filename, local_staging_name, id_col)
SURVEYS = [
    ("desi_dr1",  "desi_dr1_anomalies.parquet",      "desi_dr1_anomalies.parquet",     "tid"),
    ("sdss_dr18", "sdss_dr18_pathc_native.parquet",  "sdss_dr18_pathc_native.parquet", None),
    ("planck_cmb", "planck_cmb_anomalies.parquet",   "planck_cmb_anomalies.parquet",   "patch_idx"),
    ("neowise",   "neowise_anomalies.parquet",       "neowise_anomalies.parquet",      "source_id"),
]

# Per-survey validated input the paper states (pre-dedup).
EXPECTED_INPUT = {
    "desi_dr1": 195829, "sdss_dr18": 77905, "planck_cmb": 200, "neowise_pathc": 419,
}


class UnionFind:
    def __init__(self, n):
        self.p = np.arange(n)
        self.r = np.zeros(n, dtype=np.int32)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1


def _ensure_staged(hf_filename, local_name):
    STAGE.mkdir(parents=True, exist_ok=True)
    local = STAGE / local_name
    if local.exists():
        return local
    try:
        from huggingface_hub import hf_hub_download
        import shutil
        tok = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
        p = hf_hub_download(repo_id=HF_REPO, repo_type="dataset",
                            filename=hf_filename, token=tok)
        shutil.copy(p, local)
        return local
    except Exception as e:
        print(f"    HF download failed for {hf_filename}: {type(e).__name__}: {e}")
        return None


def _load_desi_fallback():
    csv = REPO / "pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.csv"
    if not csv.exists():
        return None
    df = pd.read_csv(csv, usecols=["tid", "ra", "dec", "anomaly_score"])
    return pd.DataFrame({
        "survey": "desi_dr1",
        "source_id": df["tid"].astype(str).values,
        "ra": df["ra"].astype("float64").values,
        "dec": df["dec"].astype("float64").values,
    })


def _neowise_mask(df):
    """Path-C ecliptic-pole mask: keep |ecliptic_lat| < 80 deg."""
    sc = SkyCoord(ra=df["ra"].values * u.deg, dec=df["dec"].values * u.deg, frame="icrs")
    elat = sc.barycentrictrueecliptic.lat.deg
    keep = np.abs(elat) < NEOWISE_ELAT_CUT_DEG
    return df.loc[keep].reset_index(drop=True), int((~keep).sum())


def load_survey(name, hf_filename, local_name, id_col):
    local = _ensure_staged(hf_filename, local_name)
    if local is None:
        if name == "desi_dr1":
            fb = _load_desi_fallback()
            if fb is not None:
                return fb, f"loaded {len(fb)} rows (DESI committed-CSV fallback)"
        return None, f"FAILED (no HF, no fallback) {hf_filename}"
    df = pd.read_parquet(local)
    out = pd.DataFrame({
        "survey": name,
        "source_id": (df[id_col].astype(str).values if id_col and id_col in df.columns
                      else [f"{name}_{i}" for i in range(len(df))]),
        "ra": df["ra"].astype("float64").values,
        "dec": df["dec"].astype("float64").values,
    })
    ok = np.isfinite(out["ra"]) & np.isfinite(out["dec"])
    out = out.loc[ok].reset_index(drop=True)
    msg = f"loaded {len(out)} rows"
    if name == "neowise":
        out, n_rej = _neowise_mask(out)
        out["survey"] = "neowise_pathc"
        msg = f"loaded {len(out)+n_rej} raw -> {len(out)} after ecliptic-pole mask ({n_rej} rejected)"
    return out, msg


def main():
    parts, status = [], {}
    for name, hf_f, loc, idc in SURVEYS:
        part, msg = load_survey(name, hf_f, loc, idc)
        status[name] = msg
        print(f"  {name:12s}  {msg}")
        if part is None:
            raise SystemExit(f"ABORT: survey {name} could not be loaded — cannot fabricate.")
        parts.append(part)

    cat = pd.concat(parts, ignore_index=True)
    n_total = len(cat)
    per_survey_input = cat["survey"].value_counts().to_dict()
    print(f"\n  total validated survey-level detections (4-way input): {n_total:,}")

    sc = SkyCoord(ra=cat["ra"].values * u.deg, dec=cat["dec"].values * u.deg, frame="icrs")
    print(f"  search_around_sky at {MATCH_RADIUS_ARCSEC}\" ...")
    i1, i2, sep, _ = search_around_sky(sc, sc, MATCH_RADIUS_ARCSEC * u.arcsec)
    m = i1 < i2
    i1, i2 = i1[m], i2[m]
    n_pairs = len(i1)
    print(f"  {n_pairs:,} off-diagonal pairs within {MATCH_RADIUS_ARCSEC}\"")

    surv = cat["survey"].values
    pair_counter = Counter()
    for a, b in zip(surv[i1], surv[i2]):
        pair_counter[tuple(sorted((a, b)))] += 1
    pair_table = {f"{a}|{b}": int(c) for (a, b), c in sorted(pair_counter.items())}

    uf = UnionFind(n_total)
    for a, b in zip(i1, i2):
        uf.union(int(a), int(b))
    labels = np.array([uf.find(i) for i in range(n_total)])
    uniq, inv = np.unique(labels, return_inverse=True)
    cat["cluster_id"] = inv
    n_unique = len(uniq)
    n_collapsed = n_total - n_unique
    print(f"  VALIDATED unique physical objects: {n_unique:,}  "
          f"(collapsed {n_collapsed:,}, {100*n_collapsed/n_total:.4f}%)")

    # Point-source subset = drop the 200 Planck CMB map patches.
    n_planck = int(per_survey_input.get("planck_cmb", 0))
    n_unique_pointsource = n_unique - n_planck

    g = cat.groupby("cluster_id")
    nsurv = g["survey"].nunique()
    k_hist = Counter(nsurv.values.tolist())
    n_multi = int((nsurv >= 2).sum())

    input_ok = {
        s: int(per_survey_input.get(s, 0)) == EXPECTED_INPUT[s]
        for s in EXPECTED_INPUT
    }

    artifact = {
        "task": "P3 VALIDATED catalog-grade headline dedup (RS22 directives 1-4)",
        "generated_by": "pipelines/p3_anomaly_engine/scripts/reproduce_headline_dedup.py",
        "data_source": f"HuggingFace {HF_REPO} (per-object released validated catalogs)",
        "match_radius_arcsec": MATCH_RADIUS_ARCSEC,
        "neowise_ecliptic_pole_mask_deg": NEOWISE_ELAT_CUT_DEG,
        "validated_surveys": ["desi_dr1", "sdss_dr18", "planck_cmb", "neowise_pathc"],
        "excluded": {
            "gaia_dr3": "DROPPED — synthetic-placeholder fallback (directive 1)",
            "erosita_dr1": "membership-only, no score-axis statistics, not in headline (directive 2)",
            "lamost_dr10": "blue-excess artifact, injection-recovery FAIL, methodological lesson only (directive 4)",
            "act_dr6": "cross-transfer quarantine, zero objects",
        },
        "survey_load_status": status,
        "per_survey_input_detections": {k: int(v) for k, v in sorted(per_survey_input.items())},
        "per_survey_input_matches_paper": input_ok,
        "total_validated_survey_level_detections": int(n_total),
        "pairs_within_radius": int(n_pairs),
        "per_survey_pair_match_counts": pair_table,
        "n_collapsed_detections": int(n_collapsed),
        "compression_pct": round(100 * n_collapsed / n_total, 4),
        "clusters_in_k_surveys": {str(k): int(v) for k, v in sorted(k_hist.items())},
        "n_multi_survey_clusters_ge2": n_multi,
        "VALIDATED_HEADLINE_unique": int(n_unique),
        "VALIDATED_HEADLINE_pointsource": int(n_unique_pointsource),
        "note": ("This is the EXACT validated-tier count — a direct 4-way 5\" dedup of the "
                 "committed validated per-survey lists, NOT a subtraction lower bound. "
                 "Gaia dropped, eROSITA membership-only, LAMOST excluded."),
    }
    with open(OUT_DIR / "reproduce_headline_dedup.json", "w") as f:
        json.dump(artifact, f, indent=2)

    print("\n=== VALIDATED HEADLINE ===")
    print(f"  unique validated anomalies       : {n_unique:,}")
    print(f"  unique validated (point-source)  : {n_unique_pointsource:,}")
    print(f"  wrote {OUT_DIR/'reproduce_headline_dedup.json'}")


if __name__ == "__main__":
    main()
