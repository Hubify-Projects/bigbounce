#!/usr/bin/env python3
"""
R23conf META-REVIEW closure audits — P3-META-M1 / P3-META-M4 / P3-META-M7
=========================================================================
Three local recomputes on the same seven Path-C survey parquets used by
pathc_positional_dedup.py (ACT excluded, canonical 7-way configuration):

  (1) META-M1  FoF chain audit: per-cluster maximum pairwise separation at
      the canonical 5" link length; counts clusters whose max pairwise
      separation exceeds 5" (transitive "chain bridging").
  (2) META-M4  SDSS-threshold robustness: re-run the identical 7-way
      union-find dedup with the SDSS tier replaced by (a) the native
      top-1% score-knee set (top-19,253) and (b) the S>5 set (12),
      instead of the 77,905-row continuity slice.
  (3) META-M7  DESI x SDSS 3" coincidence denominator: observed pair-matched
      count at 3" between the full DESI (195,829) and SDSS continuity-slice
      (77,905) anomaly catalogs, with the random-coincidence expectation
      measured empirically by RA-shifted controls (+/-0.5 deg, +/-1.0 deg).

Output: pipelines/p3_anomaly_engine/pathc_dedup/r23conf_dedup_audits.json
Run:    python3 pipelines/p3_anomaly_engine/pathc_dedup/r23conf_dedup_audits.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord, search_around_sky
import astropy.units as u

REPO = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / 'r23conf_dedup_audits.json'

SURVEYS = [
    ('desi_dr1', 'pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.parquet'),
    ('erosita_dr1', 'pipelines/p3_anomaly_engine/hf_staging_pod/erosita_dr1_anomalies.parquet'),
    ('planck_cmb', 'pipelines/p3_anomaly_engine/hf_staging/planck_cmb_anomalies.parquet'),
    ('gaia_dr3', 'pipelines/p3_anomaly_engine/hf_staging/gaia_dr3_anomalies.parquet'),
    ('neowise_pathc', 'pipelines/p3_anomaly_engine/pathc_neowise_ecliptic/neowise_pathc_masked_anomalies.parquet'),
    ('sdss_dr18', 'pipelines/p3_anomaly_engine/hf_staging/sdss_dr18_pathc_native.parquet'),
    ('lamost_dr10', 'pipelines/p3_anomaly_engine/hf_staging/lamost_dr10_pathc_native.parquet'),
]

RADIUS = 5.0  # arcsec, canonical


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


def load(name, path):
    df = pd.read_parquet(REPO / path)
    out = pd.DataFrame({
        'survey': name,
        'ra': df['ra'].astype('float64').values,
        'dec': df['dec'].astype('float64').values,
    })
    ok = np.isfinite(out['ra']) & np.isfinite(out['dec'])
    return out.loc[ok].reset_index(drop=True)


def dedup(cat, radius=RADIUS):
    sc = SkyCoord(ra=cat['ra'].values * u.deg, dec=cat['dec'].values * u.deg, frame='icrs')
    i1, i2, sep, _ = search_around_sky(sc, sc, radius * u.arcsec)
    m = i1 < i2
    i1, i2, sep = i1[m], i2[m], sep[m]
    uf = UnionFind(len(cat))
    for a, b in zip(i1, i2):
        uf.union(a, b)
    labels = np.array([uf.find(i) for i in range(len(cat))])
    uniq, inv = np.unique(labels, return_inverse=True)
    return inv, sc, (i1, i2, sep)


def main():
    parts = {name: load(name, path) for name, path in SURVEYS}
    results = {'task': 'R23conf P3 META-M1/M4/M7 dedup audits', 'radius_arcsec': RADIUS}

    # ---------- canonical 7-way run + META-M1 chain audit ----------
    cat = pd.concat(parts.values(), ignore_index=True)
    inv, sc, _ = dedup(cat)
    cat['cluster_id'] = inv
    n_unique = int(cat['cluster_id'].nunique())
    g = cat.groupby('cluster_id')
    sizes = g.size()
    multi_ids = sizes[sizes >= 2].index
    max_seps, over_link = [], 0
    size_hist = sizes[sizes >= 2].value_counts().sort_index().to_dict()
    for cid in multi_ids:
        idx = np.where(inv == cid)[0]
        sub = sc[idx]
        seps = sub[:, None].separation(sub[None, :]).arcsec
        mx = float(seps.max())
        max_seps.append(mx)
        if mx > RADIUS:
            over_link += 1
    max_seps = np.array(max_seps)
    results['canonical_7way'] = {
        'n_input': int(len(cat)),
        'n_unique': n_unique,
        'n_clusters_ge2_members': int(len(multi_ids)),
        'cluster_size_histogram_ge2': {int(k): int(v) for k, v in size_hist.items()},
        'meta_m1_chain_audit': {
            'max_intra_cluster_pairwise_separation_arcsec': float(max_seps.max()) if len(max_seps) else 0.0,
            'n_clusters_max_sep_gt_link_5as': int(over_link),
            'fraction_clusters_chained': float(over_link / len(multi_ids)) if len(multi_ids) else 0.0,
        },
    }
    print('canonical:', results['canonical_7way'])

    # ---------- META-M4: SDSS-threshold variants ----------
    sdss_full = pd.read_parquet(REPO / 'pipelines/p3_anomaly_engine/hf_staging/sdss_dr18_pathc_native.parquet')
    variants = {
        'sdss_top1pct_19253': sdss_full.nlargest(19253, 'anomaly_score'),
        'sdss_sgt5_12': sdss_full[sdss_full['anomaly_score'] > 5.0],
    }
    results['meta_m4_sdss_threshold_variants'] = {}
    for vname, vdf in variants.items():
        p2 = dict(parts)
        p2['sdss_dr18'] = pd.DataFrame({
            'survey': 'sdss_dr18',
            'ra': vdf['ra'].astype('float64').values,
            'dec': vdf['dec'].astype('float64').values,
        }).reset_index(drop=True)
        cat2 = pd.concat(p2.values(), ignore_index=True)
        inv2, sc2, _ = dedup(cat2)
        cat2['cluster_id'] = inv2
        g2 = cat2.groupby('cluster_id')
        nsurv = g2['survey'].nunique()
        results['meta_m4_sdss_threshold_variants'][vname] = {
            'sdss_rows': int(len(vdf)),
            'n_input': int(len(cat2)),
            'n_unique': int(cat2['cluster_id'].nunique()),
            'n_multi_survey_clusters': int((nsurv >= 2).sum()),
            'compression_pct': float(100 * (len(cat2) - cat2['cluster_id'].nunique()) / len(cat2)),
        }
        print(vname, results['meta_m4_sdss_threshold_variants'][vname])

    # ---------- META-M7: DESI x SDSS 3" coincidence denominator ----------
    desi = parts['desi_dr1']
    sdss = parts['sdss_dr18']
    c_desi = SkyCoord(ra=desi['ra'].values * u.deg, dec=desi['dec'].values * u.deg)

    def n_matches(sdss_ra_shift_deg):
        c_s = SkyCoord(ra=(sdss['ra'].values + sdss_ra_shift_deg) % 360.0 * u.deg,
                       dec=sdss['dec'].values * u.deg)
        idx, sep, _ = c_desi.match_to_catalog_sky(c_s)
        return int((sep.arcsec < 3.0).sum())

    observed = n_matches(0.0)
    shifts = [0.5, -0.5, 1.0, -1.0]
    controls = [n_matches(s) for s in shifts]
    results['meta_m7_desi_x_sdss_3as'] = {
        'n_desi': int(len(desi)),
        'n_sdss_continuity_slice': int(len(sdss)),
        'observed_matches_3as': observed,
        'ra_shift_controls_deg': shifts,
        'control_match_counts': controls,
        'expected_random_mean': float(np.mean(controls)),
        'note': ('Observed = DESI anomalies with an SDSS continuity-slice anomaly within 3"; '
                 'expectation measured empirically by RA-shifting the SDSS catalog '
                 '(preserves footprint overlap and local density to first order).'),
    }
    print('meta_m7:', results['meta_m7_desi_x_sdss_3as'])

    with open(OUT, 'w') as f:
        json.dump(results, f, indent=2)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
