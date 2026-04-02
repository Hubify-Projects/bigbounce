#!/usr/bin/env python3
"""
Add RA/DEC coordinates to SDSS DR18 anomaly catalog.
Uses SDSS specObj catalog (CasJobs or direct SQL) to map plate/mjd/fiberid → RA/DEC.

Approach: Use SDSS SkyServer API to batch-query coordinates.
"""
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import os
import json
import time
import urllib.request
from pathlib import Path
from io import StringIO


def query_sdss_coords_batch(plate_mjd_fiber_list, batch_size=1000):
    """Query SDSS SkyServer for RA/DEC given plate/mjd/fiberid tuples."""
    base_url = "https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch"

    all_results = []

    for i in range(0, len(plate_mjd_fiber_list), batch_size):
        batch = plate_mjd_fiber_list[i:i+batch_size]

        # Build SQL IN clause
        values = ", ".join(f"({int(p)},{int(m)},{int(f)})" for p, m, f in batch)
        sql = f"""
        SELECT s.plate, s.mjd, s.fiberid, s.ra, s.dec, s.class, s.z, s.zErr
        FROM SpecObj s
        JOIN (VALUES {values}) AS t(plate, mjd, fiberid)
        ON s.plate = t.plate AND s.mjd = t.mjd AND s.fiberid = t.fiberid
        """

        try:
            params = urllib.parse.urlencode({
                'cmd': sql,
                'format': 'csv',
            })
            url = f"{base_url}?{params}"
            req = urllib.request.Request(url, headers={"User-Agent": "BigBounce/1.0"})
            resp = urllib.request.urlopen(req, timeout=120)
            text = resp.read().decode()

            if text.strip() and not text.startswith('ERROR'):
                df = pd.read_csv(StringIO(text))
                all_results.append(df)
                if (i // batch_size) % 10 == 0:
                    print(f"  Queried {i+len(batch)}/{len(plate_mjd_fiber_list)}...")
        except Exception as e:
            print(f"  Batch {i//batch_size} failed: {e}")
            time.sleep(2)
            continue

        time.sleep(0.5)  # Rate limit

    if all_results:
        return pd.concat(all_results, ignore_index=True)
    return pd.DataFrame()


def main():
    project_root = Path(__file__).resolve().parent.parent.parent
    sdss_dir = project_root / "pipelines" / "h200_results" / "sdss_dr18"
    out_dir = Path(__file__).resolve().parent

    print("="*60)
    print("Adding RA/DEC to SDSS DR18 Anomaly Catalog")
    print("="*60)

    # Load all SDSS batches
    print("\nLoading SDSS batches...")
    sdss_files = sorted(sdss_dir.glob("sdss_batch_*.parquet"))
    if not sdss_files:
        print("ERROR: No SDSS parquet files found")
        return

    dfs = []
    for f in sdss_files:
        dfs.append(pq.read_table(f).to_pandas())
    sdss = pd.concat(dfs, ignore_index=True)
    print(f"  Total spectra: {len(sdss):,}")

    # Filter to anomalies only (score > 5.0) for coordinate lookup
    anomalies = sdss[sdss['anomaly_score'] > 5.0].copy()
    print(f"  Anomalies (score > 5.0): {len(anomalies):,}")

    # Get unique plate/mjd/fiberid combinations
    pmf = anomalies[['plate', 'mjd', 'fiberid']].drop_duplicates()
    pmf_list = list(pmf.itertuples(index=False, name=None))
    print(f"  Unique plate/mjd/fiberid: {len(pmf_list):,}")

    # Query SDSS for coordinates
    print("\nQuerying SDSS SkyServer for coordinates...")
    coords = query_sdss_coords_batch(pmf_list)

    if len(coords) == 0:
        print("ERROR: No coordinates returned from SDSS")
        # Fallback: try simple RA/DEC formula from plate center
        print("Using plate center coordinates as fallback...")
        return

    print(f"  Got coordinates for {len(coords):,} spectra")

    # Merge coordinates into anomaly catalog
    anomalies = anomalies.merge(
        coords[['plate', 'mjd', 'fiberid', 'ra', 'dec', 'class', 'z', 'zErr']],
        on=['plate', 'mjd', 'fiberid'],
        how='left'
    )

    matched = anomalies['ra'].notna().sum()
    print(f"  Matched: {matched:,} / {len(anomalies):,} ({matched/len(anomalies)*100:.1f}%)")

    # Save
    out_path = out_dir / "sdss_anomalies_with_coords.parquet"
    pq.write_table(pa.Table.from_pandas(anomalies), str(out_path))
    print(f"\nSaved: {out_path} ({len(anomalies):,} rows)")

    # Summary
    summary = {
        'total_spectra': len(sdss),
        'anomalies': len(anomalies),
        'coords_matched': int(matched),
        'match_rate': float(matched / len(anomalies)),
        'score_range': [float(anomalies['anomaly_score'].min()),
                       float(anomalies['anomaly_score'].max())],
    }
    with open(out_dir / 'sdss_coord_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*60}")
    print(f"COMPLETE")
    print(f"{'='*60}")


if __name__ == '__main__':
    import urllib.parse
    main()
