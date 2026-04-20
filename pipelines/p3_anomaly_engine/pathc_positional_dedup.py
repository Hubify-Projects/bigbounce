#!/usr/bin/env python3
"""
Path-C 8-way positional dedup at 5 arcsec — P3-PATHC-DEDUP-LOCAL
================================================================
Computes unique-physical-object count across the per-survey Paper 3
anomaly catalogs by friends-of-friends union-find at 5" angular
separation.

Path-C exit criterion #7 asks Paper 3 Table 1 + abstract to quote BOTH
  "N survey-level detections"   (the sum of per-survey top-cut counts)
  "M unique physical objects"   (after positional dedup)

Current surveys available LOCALLY (this fire, no pod):
  DESI DR1  top-1%  195,829 rows   (pipelines/p1_highz_tracers/outputs/step2_crossmatch/)
  eROSITA   top-cut   298 rows   (hf_staging_pod/)
  Planck CMB           200 rows   (hf_staging/)
  Gaia DR3             500 rows   (hf_staging/)
  NEOWISE Path-C masked 419 rows (pathc_neowise_ecliptic/, fire #84)

Surveys still pending the running native retrains (will be added after the
pod re-scores finish):
  SDSS DR18 native  ~77,905 top rows   (rescore ETA 50 h)
  LAMOST DR10 native ~44,075 top rows (rescore ETA 33 h)
  ACT DR6 native      ~200 rows       (post-retrain, if retained)

The script writes `pending` survey rows with zero contribution and is
designed to be re-run after each retrain finishes — it takes the surveys
it finds on disk and logs which ones are still pending, so the pipeline
output keeps improving across fires.

Algorithm:
  1. Load N surveys + normalize schema to (survey, source_id, ra, dec,
     anomaly_score).
  2. Concatenate, build astropy SkyCoord.
  3. `search_around_sky(cat, cat, 5 arcsec)` -> all pair matches within 5".
  4. Union-find on those pairs -> cluster labels.
  5. Per-cluster output row: (cluster_id, n_detections, n_surveys,
     survey_list, best_survey, best_score, ra_mean, dec_mean, member_ids).
  6. Summary JSON: per-survey detection counts, M unique objects, number
     of multi-survey matches (clusters with n_surveys >= 2), tabular
     "how many objects appear in exactly k surveys".

Outputs:
  pipelines/p3_anomaly_engine/pathc_dedup/
    unique_objects.parquet     # one row per unique physical object
    multi_survey_matches.parquet   # subset: clusters with >=2 surveys
    pathc_dedup_summary.json       # headline counts for Paper 3 §2.X / Table 1
"""
import json
import os
from pathlib import Path
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord, search_around_sky
import astropy.units as u

OUT_DIR = Path('pipelines/p3_anomaly_engine/pathc_dedup')
OUT_DIR.mkdir(parents=True, exist_ok=True)

MATCH_RADIUS_ARCSEC = 5.0

# -- Survey catalog registry ------------------------------------------------
# Each entry: (name, parquet_path, id_col). Path-C criterion #7 is 8-way,
# but SDSS / LAMOST / ACT are still being produced by the pod retrains.
# The script degrades gracefully: missing catalogs are logged as pending.
SURVEYS = [
    ('desi_dr1',
     'pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.parquet',
     None),
    ('erosita_dr1',
     'pipelines/p3_anomaly_engine/hf_staging_pod/erosita_dr1_anomalies.parquet',
     'iauname'),
    ('planck_cmb',
     'pipelines/p3_anomaly_engine/hf_staging/planck_cmb_anomalies.parquet',
     'patch_idx'),
    ('gaia_dr3',
     'pipelines/p3_anomaly_engine/hf_staging/gaia_dr3_anomalies.parquet',
     'source_id'),
    ('neowise_pathc',
     'pipelines/p3_anomaly_engine/pathc_neowise_ecliptic/neowise_pathc_masked_anomalies.parquet',
     'source_id'),
    ('sdss_dr18',
     'pipelines/p3_anomaly_engine/hf_staging/sdss_native_anomalies.parquet',     # <- will appear post-rescore
     None),
    ('lamost_dr10',
     'pipelines/p3_anomaly_engine/hf_staging/lamost_native_anomalies.parquet',   # <- will appear post-rescore
     'obsid'),
    ('act_dr6',
     'pipelines/p3_anomaly_engine/hf_staging/act_native_anomalies.parquet',      # <- will appear post-retrain
     None),
]


class UnionFind:
    def __init__(self, n):
        self.p = np.arange(n)
        self.r = np.zeros(n, dtype=np.int32)
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.r[rx] < self.r[ry]:
            rx, ry = ry, rx
        self.p[ry] = rx
        if self.r[rx] == self.r[ry]:
            self.r[rx] += 1


def load_survey(name, path, id_col):
    p = Path(path)
    if not p.exists():
        return None, f'pending (file not on disk: {path})'
    df = pd.read_parquet(path)
    # Normalize schema
    keep = {}
    keep['survey'] = name
    if id_col is None:
        keep['source_id'] = [f'{name}_{i}' for i in range(len(df))]
    else:
        keep['source_id'] = df[id_col].astype(str).values
    keep['ra'] = df['ra'].astype('float64').values
    keep['dec'] = df['dec'].astype('float64').values
    if 'anomaly_score' in df.columns:
        keep['anomaly_score'] = df['anomaly_score'].astype('float64').values
    else:
        keep['anomaly_score'] = np.full(len(df), np.nan)
    out = pd.DataFrame(keep)
    # Sanity filter: drop rows with non-finite coords
    ok = np.isfinite(out['ra']) & np.isfinite(out['dec'])
    dropped = int((~ok).sum())
    out = out.loc[ok].reset_index(drop=True)
    return out, f'loaded {len(out)} rows (dropped {dropped} non-finite)'


def main():
    loaded_parts = []
    status = {}
    for name, path, idc in SURVEYS:
        part, msg = load_survey(name, path, idc)
        status[name] = msg
        print(f'  {name:14s}  {msg}')
        if part is not None:
            loaded_parts.append(part)
    if not loaded_parts:
        print('NO surveys loaded — aborting.')
        return

    cat = pd.concat(loaded_parts, ignore_index=True)
    n_total = len(cat)
    print(f'\nTotal detections across {len(loaded_parts)} loaded surveys: {n_total:,}')

    sc = SkyCoord(ra=cat['ra'].values * u.deg, dec=cat['dec'].values * u.deg, frame='icrs')
    print(f'  running search_around_sky at {MATCH_RADIUS_ARCSEC}" ...')
    idx1, idx2, sep, _ = search_around_sky(sc, sc, MATCH_RADIUS_ARCSEC * u.arcsec)
    # search_around_sky is symmetric and includes self-pairs; drop self + duplicates
    mask = idx1 < idx2
    idx1 = idx1[mask]
    idx2 = idx2[mask]
    print(f'  {len(idx1):,} within-{MATCH_RADIUS_ARCSEC}"  (off-diagonal, unordered)')

    uf = UnionFind(n_total)
    for a, b in zip(idx1, idx2):
        uf.union(a, b)
    labels = np.array([uf.find(i) for i in range(n_total)])
    # Re-label contiguous cluster IDs
    uniq, inv = np.unique(labels, return_inverse=True)
    cat['cluster_id'] = inv

    n_unique = len(uniq)
    print(f'  {n_unique:,} unique physical objects after 5" dedup '
          f'(compression {100*(n_total-n_unique)/n_total:.3f}%)')

    # Per-cluster aggregation
    g = cat.groupby('cluster_id')
    clusters = g.agg(
        n_detections=('survey', 'size'),
        n_surveys=('survey', 'nunique'),
        survey_list=('survey', lambda s: ','.join(sorted(set(s)))),
        ra_mean=('ra', 'mean'),
        dec_mean=('dec', 'mean'),
        best_score=('anomaly_score', 'max'),
        member_ids=('source_id', lambda s: '|'.join(s.astype(str))),
    ).reset_index()
    # "best_survey" = the survey owning the max-score member (NaN-safe)
    def best_survey(sub):
        s = sub.dropna(subset=['anomaly_score'])
        if len(s) == 0:
            return sub['survey'].iloc[0]
        return s.loc[s['anomaly_score'].idxmax(), 'survey']
    clusters['best_survey'] = g.apply(best_survey).values

    out_path = OUT_DIR / 'unique_objects.parquet'
    clusters.to_parquet(out_path)
    print(f'  wrote {out_path}  ({len(clusters):,} rows)')

    multi = clusters[clusters['n_surveys'] >= 2].sort_values('n_surveys', ascending=False).reset_index(drop=True)
    multi_path = OUT_DIR / 'multi_survey_matches.parquet'
    multi.to_parquet(multi_path)
    print(f'  wrote {multi_path}  ({len(multi):,} multi-survey clusters)')

    # Per-survey detection breakdown
    per_survey = cat['survey'].value_counts().to_dict()
    # "How many objects appear in exactly k surveys"
    k_hist = clusters['n_surveys'].value_counts().sort_index().to_dict()
    k_hist = {int(k): int(v) for k, v in k_hist.items()}

    summary = {
        'task': 'P3-PATHC-DEDUP-LOCAL (8-way-aspirational, N-way actual)',
        'match_radius_arcsec': MATCH_RADIUS_ARCSEC,
        'surveys_planned': [name for name, _, _ in SURVEYS],
        'surveys_loaded': list(per_survey.keys()),
        'surveys_pending': [k for k, v in status.items() if v.startswith('pending')],
        'survey_load_status': status,
        'per_survey_detections': {k: int(v) for k, v in per_survey.items()},
        'total_survey_detections_loaded': int(n_total),
        'n_unique_objects': int(n_unique),
        'compression_fraction': float((n_total - n_unique) / n_total),
        'n_multi_survey_matches_ge2': int(len(multi)),
        'clusters_in_k_surveys': k_hist,
        'paper3_table1_numbers_now': {
            'survey_level_detections': int(n_total),
            'unique_physical_objects': int(n_unique),
            'note': (
                f'Reported across {len(loaded_parts)} of {len(SURVEYS)} planned surveys. '
                'SDSS DR18 + LAMOST DR10 native re-scores are in flight on pod '
                '`ktds4mkmzb7ven` (ETA 50 / 33 h); ACT DR6 is deferred. Re-run this '
                'script after each rescore completes — it degrades gracefully and '
                'picks up new survey parquets automatically.'
            ),
        },
        'note_multi_survey_meaning': (
            'A multi-survey match at 5" is rare and scientifically valuable: the same '
            'physical position flagged as anomalous by two independent pipelines is '
            'strong evidence of a genuine astrophysical feature rather than a '
            'survey-specific systematic.'
        ),
    }
    summary_path = OUT_DIR / 'pathc_dedup_summary.json'
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'  wrote {summary_path}')

    print(f'\nHEADLINE: {n_total:,} survey-level detections  ->  {n_unique:,} unique physical objects')
    if len(multi) > 0:
        print(f'          {len(multi):,} multi-survey matches (same position in >=2 surveys)')
        top_multi = multi.head(10)
        print(f'  top {len(top_multi)} multi-survey clusters:')
        for _, r in top_multi.iterrows():
            print(f'    cluster {int(r.cluster_id):6d}  n_surveys={r.n_surveys}  '
                  f'surveys={r.survey_list}  score={r.best_score:.4g}  '
                  f'ra={r.ra_mean:.4f}  dec={r.dec_mean:.4f}')


if __name__ == '__main__':
    main()
