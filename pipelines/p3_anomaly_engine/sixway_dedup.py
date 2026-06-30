#!/usr/bin/env python3
"""
Independent 6-way positional dedup artifact — P3 OpenAI-E1 ("most critical")
============================================================================
Reviewer demand (OpenAI EXT E1): Paper 3 quotes a deduplicated catalog count
for the *recommended-tier* (catalog-grade) surveys.  Reviewers asked for the
ACTUAL dedup table to be produced and committed — a reproducible positional
cross-match at 5 arcsec showing the per-survey input counts, the per-survey-pair
collapse, and the final unique count — not just a stated number.

This script reproduces, from the canonical released per-object catalogs, the
6-way recommended-tier chain stated in the paper (footnote spadesuit / §III):

    input  = 195,829 (DESI) + 77,905 (SDSS) + 298 (eROSITA) + 200 (Planck)
             + 500 (Gaia) + 419 (NEOWISE, ecliptic-masked)  = 275,151
    unique = 269,317   (5,834 detections collapsed; 2.12% compression)

The six surveys are the recommended/exploratory tiers that enter the catalog
headline. LAMOST DR10 (113,342) and ACT DR6 (cross-transfer) are NOT part of
this 6-way set — they are the additional surveys that take the *7-way* count
to 378,280 (see pathc_positional_dedup.py for the full N-way run). The reviewer
asked specifically for the 6-way recommended-tier artifact, which is this file.

DATA SOURCE (canonical, reproducible)
-------------------------------------
Per-object catalogs are the released HuggingFace dataset
    bamfai/bigbounce-anomaly-catalog
The script downloads the parquet blocks into ./hf_staging/ (gitignored) on
first run (HF_TOKEN from repo-root .env.local), then runs entirely locally.
DESI is also committed in-repo as a CSV
    pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.csv
and the script falls back to it if HF is unreachable.

NEOWISE: the released block is the 436-row raw top-1% set; the paper's 419
is that set after the Path-C ecliptic-pole mask (|ecliptic_lat| < 80 deg,
neowise_pathc_ecliptic_mask.py). This script applies that exact cut inline so
the 419 is reproduced from first principles, not assumed.

ALGORITHM
---------
1. Load 6 surveys, normalize schema to (survey, source_id, ra, dec, score).
2. Apply NEOWISE ecliptic-pole mask inline -> 419.
3. Build astropy SkyCoord, search_around_sky(self, self, 5") -> all pairs <=5".
4. Union-find (friends-of-friends) -> clusters = unique physical objects.
5. Emit: per-survey input counts, per-survey-pair match counts, per-survey
   "absorbed" (detections that merged into a cluster owned by an earlier
   survey), total collapse, final unique count, and the k-survey histogram.

OUTPUT
------
    outputs/sixway_dedup_artifact.json   # full machine-readable artifact
    outputs/sixway_dedup_artifact.csv    # one row per unique physical object

Deterministic: no randomness. Re-runnable. Numbers must match (or honestly
correct) the paper's 275,151-input / 269,317-unique / 5,834-collapse chain.
"""
import itertools
import json
import os
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord, search_around_sky
import astropy.units as u

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
STAGE = HERE / "hf_staging"
OUT_DIR = HERE / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MATCH_RADIUS_ARCSEC = 5.0
NEOWISE_ELAT_CUT_DEG = 80.0  # reject |ecliptic_lat| >= 80 (Path-C pole mask)

HF_REPO = "bamfai/bigbounce-anomaly-catalog"

# (survey, hf_filename, local_staging_name, id_col)
SURVEYS = [
    ("desi_dr1",    "desi_dr1_anomalies.parquet",                 "desi_dr1_anomalies.parquet",      "tid"),
    ("sdss_dr18",   "sdss_dr18_pathc_native.parquet",             "sdss_dr18_pathc_native.parquet",  None),
    ("erosita_dr1", "blocks/erosita_dr1/erosita_dr1_anomalies.parquet", "erosita_dr1_anomalies.parquet", "iauname"),
    ("planck_cmb",  "planck_cmb_anomalies.parquet",               "planck_cmb_anomalies.parquet",    "patch_idx"),
    ("gaia_dr3",    "gaia_dr3_anomalies.parquet",                 "gaia_dr3_anomalies.parquet",      "source_id"),
    ("neowise",     "neowise_anomalies.parquet",                  "neowise_anomalies.parquet",       "source_id"),
]

PAPER_CLAIM = {
    "input_sum": 275151,
    "unique": 269317,
    "collapsed": 5834,
    "compression_pct": 2.12,
    "per_survey_input": {
        "desi_dr1": 195829, "sdss_dr18": 77905, "erosita_dr1": 298,
        "planck_cmb": 200, "gaia_dr3": 500, "neowise": 419,
    },
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
    """Return local path to a survey parquet, downloading from HF if absent."""
    STAGE.mkdir(parents=True, exist_ok=True)
    local = STAGE / local_name
    if local.exists():
        return local
    try:
        from huggingface_hub import hf_hub_download
        tok = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
        p = hf_hub_download(repo_id=HF_REPO, repo_type="dataset",
                            filename=hf_filename, token=tok)
        # copy into staging under the flat local name
        import shutil
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
        "score": df["anomaly_score"].astype("float64").values,
    })


def _neowise_mask(df):
    """Apply Path-C ecliptic-pole mask: keep |ecliptic_lat| < 80 deg."""
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
    score_col = next((c for c in ("anomaly_score", "score", "S_BigAE") if c in df.columns), None)
    out = pd.DataFrame({
        "survey": name,
        "source_id": (df[id_col].astype(str).values if id_col and id_col in df.columns
                      else [f"{name}_{i}" for i in range(len(df))]),
        "ra": df["ra"].astype("float64").values,
        "dec": df["dec"].astype("float64").values,
        "score": (df[score_col].astype("float64").values if score_col
                  else np.full(len(df), np.nan)),
    })
    ok = np.isfinite(out["ra"]) & np.isfinite(out["dec"])
    out = out.loc[ok].reset_index(drop=True)
    msg = f"loaded {len(out)} rows"
    if name == "neowise":
        out, n_rej = _neowise_mask(out)
        out["survey"] = "neowise_pathc"   # rename to masked label
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
    cat["row"] = np.arange(len(cat))
    n_total = len(cat)
    per_survey_input = cat["survey"].value_counts().to_dict()
    print(f"\n  total survey-level detections (6-way input): {n_total:,}")

    sc = SkyCoord(ra=cat["ra"].values * u.deg, dec=cat["dec"].values * u.deg, frame="icrs")
    print(f"  search_around_sky at {MATCH_RADIUS_ARCSEC}\" ...")
    i1, i2, sep, _ = search_around_sky(sc, sc, MATCH_RADIUS_ARCSEC * u.arcsec)
    m = i1 < i2          # drop self-pairs + symmetric duplicates
    i1, i2, sep = i1[m], i2[m], sep[m]
    n_pairs = len(i1)
    print(f"  {n_pairs:,} off-diagonal pairs within {MATCH_RADIUS_ARCSEC}\"")

    # Per-survey-pair match table (how many 5" matches link each survey pair)
    surv = cat["survey"].values
    pair_counter = Counter()
    for a, b in zip(surv[i1], surv[i2]):
        pair_counter[tuple(sorted((a, b)))] += 1
    pair_table = {f"{a}|{b}": int(c) for (a, b), c in sorted(pair_counter.items())}

    # Union-find -> clusters
    uf = UnionFind(n_total)
    for a, b in zip(i1, i2):
        uf.union(int(a), int(b))
    labels = np.array([uf.find(i) for i in range(n_total)])
    uniq, inv = np.unique(labels, return_inverse=True)
    cat["cluster_id"] = inv
    n_unique = len(uniq)
    n_collapsed = n_total - n_unique
    print(f"  unique physical objects: {n_unique:,}  "
          f"(collapsed {n_collapsed:,}, {100*n_collapsed/n_total:.4f}%)")

    # k-survey histogram + multi-survey clusters
    g = cat.groupby("cluster_id")
    nsurv = g["survey"].nunique()
    ndet = g["survey"].size
    k_hist = Counter(nsurv.values.tolist())
    n_multi = int((nsurv >= 2).sum())

    # Per-survey "absorbed" detections (members beyond the first per cluster,
    # attributed to the survey of each absorbed detection)
    absorbed = Counter()
    for cid, sub in cat.groupby("cluster_id"):
        if len(sub) == 1:
            continue
        # the cluster keeps one representative; the rest are "absorbed"
        svs = sub["survey"].tolist()
        for s in svs[1:]:
            absorbed[s] += 1

    # Build per-unique-object output table
    clusters = g.agg(
        n_detections=("survey", "size"),
        n_surveys=("survey", "nunique"),
        survey_list=("survey", lambda s: ",".join(sorted(set(s)))),
        ra_mean=("ra", "mean"),
        dec_mean=("dec", "mean"),
        best_score=("score", "max"),
        member_ids=("source_id", lambda s: "|".join(s.astype(str))),
    ).reset_index()
    clusters.to_csv(OUT_DIR / "sixway_dedup_artifact.csv", index=False)

    # Consistency check vs paper claim
    chk = {
        "input_sum_matches": n_total == PAPER_CLAIM["input_sum"],
        "unique_matches": n_unique == PAPER_CLAIM["unique"],
        "collapsed_matches": n_collapsed == PAPER_CLAIM["collapsed"],
        "per_survey_input_matches": {
            s: int(per_survey_input.get(s if s != "neowise" else "neowise_pathc",
                                        per_survey_input.get(s, 0)))
               == PAPER_CLAIM["per_survey_input"][s]
            for s in PAPER_CLAIM["per_survey_input"]
        },
    }

    artifact = {
        "task": "P3 independent 6-way recommended-tier positional dedup (OpenAI E1)",
        "generated_by": "pipelines/p3_anomaly_engine/sixway_dedup.py",
        "data_source": f"HuggingFace {HF_REPO} (per-object released catalogs)",
        "match_radius_arcsec": MATCH_RADIUS_ARCSEC,
        "neowise_ecliptic_pole_mask_deg": NEOWISE_ELAT_CUT_DEG,
        "surveys": ["desi_dr1", "sdss_dr18", "erosita_dr1", "planck_cmb",
                    "gaia_dr3", "neowise_pathc"],
        "survey_load_status": status,
        "per_survey_input_detections": {k: int(v) for k, v in sorted(per_survey_input.items())},
        "total_survey_level_detections": int(n_total),
        "pairs_within_radius": int(n_pairs),
        "per_survey_pair_match_counts": pair_table,
        "per_survey_absorbed_in_dedup": {k: int(v) for k, v in sorted(absorbed.items())},
        "n_unique_physical_objects": int(n_unique),
        "n_collapsed_detections": int(n_collapsed),
        "compression_pct": round(100 * n_collapsed / n_total, 4),
        "clusters_in_k_surveys": {str(k): int(v) for k, v in sorted(k_hist.items())},
        "n_multi_survey_clusters_ge2": n_multi,
        "paper_claim": PAPER_CLAIM,
        "consistency_check": chk,
        "verdict": ("EXACT-MATCH to paper claim"
                    if (chk["input_sum_matches"] and chk["unique_matches"]
                        and chk["collapsed_matches"])
                    else "MISMATCH — see consistency_check; paper number must be corrected"),
    }
    with open(OUT_DIR / "sixway_dedup_artifact.json", "w") as f:
        json.dump(artifact, f, indent=2)

    print("\n=== CONSISTENCY vs paper (275,151 input / 269,317 unique / 5,834 collapse) ===")
    print(f"  input  : got {n_total:,}   paper 275,151   match={chk['input_sum_matches']}")
    print(f"  unique : got {n_unique:,}   paper 269,317   match={chk['unique_matches']}")
    print(f"  collapse: got {n_collapsed:,}   paper 5,834   match={chk['collapsed_matches']}")
    print(f"  VERDICT: {artifact['verdict']}")
    print(f"\n  wrote {OUT_DIR/'sixway_dedup_artifact.json'}")
    print(f"  wrote {OUT_DIR/'sixway_dedup_artifact.csv'}")


if __name__ == "__main__":
    main()
