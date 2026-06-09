#!/usr/bin/env python3
"""
Path-C dedup-radius sensitivity sweep {3", 5", 7"} — P3 v3.1.80 closure
(R22prov OpenAI-E9/M6, Perplexity-E21, Grok-M3).

Re-runs the canonical 7-way positional dedup (NO ACT — the canonical
catalog configuration that yields 378,280 at 5") at three matching radii
using the exact same survey inputs and union-find FoF algorithm as
pathc_positional_dedup.py, and reports the unique-object count, the
point-source-tier count, the multi-survey cluster count, and the
compression fraction at each radius.

The paper's v3.1.79 claim "robust at the ≲0.1% level" was asserted but
not measured; this script replaces the assertion with measured numbers.

Output: pipelines/p3_anomaly_engine/pathc_dedup/radius_sweep_results.json
Run from repo root:  python3 pipelines/p3_anomaly_engine/pathc_dedup_radius_sweep.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord, search_around_sky
import astropy.units as u

OUT = Path('pipelines/p3_anomaly_engine/pathc_dedup/radius_sweep_results.json')

RADII_ARCSEC = [3.0, 5.0, 7.0]

# Canonical 7-way inputs (identical registry to pathc_positional_dedup.py,
# minus ACT DR6 which is quarantined and excluded from the canonical headline).
SURVEYS = [
    ('desi_dr1',
     'pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.parquet'),
    ('erosita_dr1',
     'pipelines/p3_anomaly_engine/hf_staging_pod/erosita_dr1_anomalies.parquet'),
    ('planck_cmb',
     'pipelines/p3_anomaly_engine/hf_staging/planck_cmb_anomalies.parquet'),
    ('gaia_dr3',
     'pipelines/p3_anomaly_engine/hf_staging/gaia_dr3_anomalies.parquet'),
    ('neowise_pathc',
     'pipelines/p3_anomaly_engine/pathc_neowise_ecliptic/neowise_pathc_masked_anomalies.parquet'),
    ('sdss_dr18',
     'pipelines/p3_anomaly_engine/hf_staging/sdss_dr18_pathc_native.parquet'),
    ('lamost_dr10',
     'pipelines/p3_anomaly_engine/hf_staging/lamost_dr10_pathc_native.parquet'),
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


def main():
    parts = []
    for name, path in SURVEYS:
        df = pd.read_parquet(path)
        ra = df['ra'].astype('float64').values
        dec = df['dec'].astype('float64').values
        ok = np.isfinite(ra) & np.isfinite(dec)
        parts.append(pd.DataFrame({'survey': name, 'ra': ra[ok], 'dec': dec[ok]}))
        print(f'  {name:14s} loaded {ok.sum():,} rows')
    cat = pd.concat(parts, ignore_index=True)
    n_total = len(cat)
    print(f'Total survey-level detections (7-way, no ACT): {n_total:,}')

    sc = SkyCoord(ra=cat['ra'].values * u.deg, dec=cat['dec'].values * u.deg,
                  frame='icrs')
    is_planck = (cat['survey'] == 'planck_cmb').values

    results = {}
    for radius in RADII_ARCSEC:
        idx1, idx2, _, _ = search_around_sky(sc, sc, radius * u.arcsec)
        m = idx1 < idx2
        idx1, idx2 = idx1[m], idx2[m]
        uf = UnionFind(n_total)
        for a, b in zip(idx1, idx2):
            uf.union(a, b)
        labels = np.array([uf.find(i) for i in range(n_total)])
        uniq, inv = np.unique(labels, return_inverse=True)
        n_unique = len(uniq)
        # multi-survey clusters
        tmp = pd.DataFrame({'cluster': inv, 'survey': cat['survey'].values})
        nsurv = tmp.groupby('cluster')['survey'].nunique()
        n_multi = int((nsurv >= 2).sum())
        # point-source tier = unique clusters containing no planck member
        planck_clusters = set(inv[is_planck])
        n_point = n_unique - len(planck_clusters)
        results[f'{radius:.0f}arcsec'] = {
            'radius_arcsec': radius,
            'pairs_within_radius': int(len(idx1)),
            'n_unique_objects': int(n_unique),
            'n_point_source_tier': int(n_point),
            'n_planck_patch_clusters': int(len(planck_clusters)),
            'n_multi_survey_clusters_ge2': n_multi,
            'n_collapsed': int(n_total - n_unique),
            'compression_pct': round(100.0 * (n_total - n_unique) / n_total, 4),
        }
        print(f'  r={radius:.0f}":  unique={n_unique:,}  multi-survey={n_multi}  '
              f'compression={results[f"{radius:.0f}arcsec"]["compression_pct"]:.4f}%')

    r3 = results['3arcsec']['n_unique_objects']
    r5 = results['5arcsec']['n_unique_objects']
    r7 = results['7arcsec']['n_unique_objects']
    summary = {
        'task': 'P3 v3.1.80 dedup-radius sensitivity sweep (canonical 7-way, no ACT)',
        'total_survey_level_detections': int(n_total),
        'results': results,
        'variation_vs_5arcsec_pct': {
            '3arcsec': round(100.0 * (r3 - r5) / r5, 4),
            '7arcsec': round(100.0 * (r7 - r5) / r5, 4),
        },
        'max_abs_variation_pct': round(
            max(abs(100.0 * (r3 - r5) / r5), abs(100.0 * (r7 - r5) / r5)), 4),
    }
    OUT.write_text(json.dumps(summary, indent=2))
    print(f'wrote {OUT}')
    print(json.dumps(summary['variation_vs_5arcsec_pct'], indent=2))


if __name__ == '__main__':
    main()
