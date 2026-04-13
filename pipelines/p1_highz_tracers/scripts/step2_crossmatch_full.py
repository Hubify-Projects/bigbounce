#!/usr/bin/env python3
"""
Pipeline 1 — Step 2: Cross-match 195,829 DESI DR1 anomalies with photometric catalogs.

Extracts:
  - Legacy Survey DR10: g/r/z optical photometry + morphology type
  - AllWISE: W1/W2 IR photometry (for W1-W2 color selection)
  - Gaia DR3: proper motions + parallax (to identify stars)
  - CatWISE2020: deeper W1/W2 (if AllWISE fails)

Uses multiple services with fallbacks:
  1. CDS xMatch (bulk, fastest when it works)
  2. VizieR TAP + ADQL (reliable, handles uploads)
  3. IRSA TAP (for WISE catalogs)
  4. ESA Gaia Archive TAP (for Gaia DR3)

Output: anomaly_crossmatch.csv with all photometric/astrometric properties.

Run on H200 pod (has astroquery + fast network) or locally if astroquery is installed.
"""

import json
import os
import sys
import time
import csv
import io
import logging
from pathlib import Path

# Try imports, report what's available
HAVE_ASTROQUERY = False
HAVE_ASTROPY = False
HAVE_PANDAS = False

try:
    import numpy as np
    HAVE_NUMPY = True
except ImportError:
    HAVE_NUMPY = False
    print("WARNING: numpy not available")

try:
    import pandas as pd
    HAVE_PANDAS = True
except ImportError:
    print("WARNING: pandas not available, will use CSV")

try:
    from astropy.coordinates import SkyCoord
    from astropy import units as u
    from astropy.table import Table
    HAVE_ASTROPY = True
except ImportError:
    print("WARNING: astropy not available, using raw HTTP")

try:
    from astroquery.xmatch import XMatch
    from astroquery.vizier import Vizier
    HAVE_ASTROQUERY = True
except ImportError:
    print("WARNING: astroquery not available, using raw HTTP")

try:
    import requests
    HAVE_REQUESTS = True
except ImportError:
    import urllib.request
    HAVE_REQUESTS = False

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger(__name__)

# ============================================================
# Configuration
# ============================================================

# Detect environment
if os.path.exists('/workspace'):
    # Running on H200 pod
    BASE_DIR = '/workspace/bigbounce/pipelines/p1_highz_tracers'
    ANOMALY_FILE = '/workspace/desi_dr1/outputs/dr1_all_anomalies.json'
    if not os.path.exists(ANOMALY_FILE):
        ANOMALY_FILE = '/workspace/dr1_all_anomalies.json'
else:
    # Running locally
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(SCRIPT_DIR)
    ANOMALY_FILE = os.path.join(BASE_DIR, 'outputs/desi_dr1/dr1_all_anomalies.json')

OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs/step2_crossmatch')
os.makedirs(OUTPUT_DIR, exist_ok=True)

MATCH_RADIUS_ARCSEC = 3.0  # Standard for spectroscopic-photometric matching
CHUNK_SIZE = 10000  # Objects per CDS xMatch request
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds

# Catalog definitions
CATALOGS = {
    'allwise': {
        'cds_id': 'vizier:II/328/allwise',
        'label': 'AllWISE',
        'key_columns': ['W1mag', 'W2mag', 'W3mag', 'W4mag', 'e_W1mag', 'e_W2mag',
                        'ccf', 'ex', 'var'],
        'purpose': 'W1-W2 IR color for QSO/AGN selection',
    },
    'gaiadr3': {
        'cds_id': 'vizier:I/355/gaiadr3',
        'label': 'Gaia DR3',
        'key_columns': ['Plx', 'e_Plx', 'pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag',
                        'RUWE', 'Dist'],
        'purpose': 'Proper motion + parallax to identify stars',
    },
    'catwise2020': {
        'cds_id': 'vizier:II/365/catwise',
        'label': 'CatWISE2020',
        'key_columns': ['W1mproPM', 'W2mproPM', 'e_W1mproPM', 'e_W2mproPM',
                        'pmRA', 'pmDE'],
        'purpose': 'Deeper W1/W2 with proper motions',
    },
    'ls_dr10': {
        'cds_id': 'vizier:II/371/des_dr2',  # Closest available on VizieR
        'label': 'Legacy Survey DR10 (via NOIRLab)',
        'key_columns': ['flux_g', 'flux_r', 'flux_z', 'type', 'shape_r'],
        'purpose': 'Optical photometry + morphology',
        'tap_url': 'https://datalab.noirlab.edu/tap',
        'tap_table': 'ls_dr10.tractor',
    },
    'sdss_dr16': {
        'cds_id': 'vizier:V/154/sdss16',
        'label': 'SDSS DR16 Photometric',
        'key_columns': ['umag', 'gmag', 'rmag', 'imag', 'zmag', 'cl'],
        'purpose': 'ugriz photometry + star/galaxy classification',
    },
    'milliquas': {
        'cds_id': 'vizier:VII/290/catalog',
        'label': 'Milliquas v8',
        'key_columns': ['Name', 'Type', 'Rmag', 'Bmag', 'z'],
        'purpose': 'Known QSO identification',
    },
}


# ============================================================
# Loading
# ============================================================

def load_anomalies(path):
    """Load anomaly catalog."""
    log.info(f"Loading anomalies from {path}")
    with open(path) as f:
        data = json.load(f)
    log.info(f"Loaded {len(data):,} anomalies")
    log.info(f"Fields: {list(data[0].keys())}")
    log.info(f"RA range: {min(d['ra'] for d in data):.2f} - {max(d['ra'] for d in data):.2f}")
    log.info(f"DEC range: {min(d['dec'] for d in data):.2f} - {max(d['dec'] for d in data):.2f}")
    log.info(f"Score range: {min(d['score'] for d in data):.2f} - {max(d['score'] for d in data):.2f}")
    return data


def anomalies_to_csv(anomalies):
    """Convert anomalies to CSV string for CDS upload."""
    lines = ['ra,dec,tid,score']
    for a in anomalies:
        lines.append(f'{a["ra"]:.6f},{a["dec"]:.6f},{a["tid"]},{a["score"]:.2f}')
    return '\n'.join(lines)


# ============================================================
# CDS xMatch (primary method)
# ============================================================

def cds_xmatch_chunk(csv_content, catalog_id, match_radius=3.0, timeout=300):
    """Cross-match a CSV chunk against a CDS catalog."""
    url = 'http://cdsxmatch.cds.unistra.fr/xmatch/api/v1/sync'

    if HAVE_REQUESTS:
        files = {'cat1': ('chunk.csv', csv_content, 'text/csv')}
        data = {
            'request': 'xmatch',
            'distMaxArcsec': str(match_radius),
            'RESPONSEFORMAT': 'csv',
            'cat2': catalog_id,
            'colRA1': 'ra',
            'colDec1': 'dec',
        }
        r = requests.post(url, data=data, files=files, timeout=timeout,
                         headers={'User-Agent': 'BigBounce-P1-Step2/2.0'})
        r.raise_for_status()
        return r.text
    else:
        # Fallback to urllib
        import urllib.request
        boundary = '----BigBounceStep2'
        params = {
            'request': 'xmatch',
            'distMaxArcsec': str(match_radius),
            'RESPONSEFORMAT': 'csv',
            'cat2': catalog_id,
            'colRA1': 'ra',
            'colDec1': 'dec',
        }
        body_parts = []
        for k, v in params.items():
            body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}')
        body_parts.append(
            f'--{boundary}\r\nContent-Disposition: form-data; name="cat1"; filename="chunk.csv"\r\n'
            f'Content-Type: text/csv\r\n\r\n{csv_content}'
        )
        body_parts.append(f'--{boundary}--')
        body = '\r\n'.join(body_parts).encode('utf-8')
        req = urllib.request.Request(url, data=body,
            headers={
                'Content-Type': f'multipart/form-data; boundary={boundary}',
                'User-Agent': 'BigBounce-P1-Step2/2.0',
            })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')


def cds_xmatch_bulk(anomalies, catalog_id, catalog_label, match_radius=3.0):
    """
    Bulk cross-match via CDS xMatch with chunking and retry logic.
    Returns dict mapping tid -> match_row.
    """
    log.info(f"CDS xMatch: {catalog_label} ({catalog_id}), {len(anomalies):,} objects, {match_radius}\" radius")

    all_matches = {}
    total = len(anomalies)
    n_chunks = (total + CHUNK_SIZE - 1) // CHUNK_SIZE

    for chunk_idx in range(n_chunks):
        start = chunk_idx * CHUNK_SIZE
        end = min(start + CHUNK_SIZE, total)
        chunk = anomalies[start:end]

        chunk_csv = anomalies_to_csv(chunk)
        chunk_label = f"chunk {chunk_idx+1}/{n_chunks} ({len(chunk)} objects)"

        for attempt in range(MAX_RETRIES):
            try:
                log.info(f"  {chunk_label}, attempt {attempt+1}...")
                result_csv = cds_xmatch_chunk(chunk_csv, catalog_id, match_radius)

                # Parse CSV result
                lines = result_csv.strip().splitlines()
                if len(lines) <= 1:
                    log.info(f"    {chunk_label}: 0 matches")
                    break

                reader = csv.DictReader(io.StringIO(result_csv))
                chunk_matches = {}
                for row in reader:
                    tid = row.get('tid', '')
                    if tid:
                        chunk_matches[tid] = row

                log.info(f"    {chunk_label}: {len(chunk_matches)} matches")
                all_matches.update(chunk_matches)
                break  # Success

            except Exception as e:
                log.warning(f"    {chunk_label} attempt {attempt+1} failed: {e}")
                if attempt < MAX_RETRIES - 1:
                    log.info(f"    Retrying in {RETRY_DELAY}s...")
                    time.sleep(RETRY_DELAY)
                else:
                    log.error(f"    {chunk_label} FAILED after {MAX_RETRIES} attempts")

        # Rate limit between chunks
        if chunk_idx < n_chunks - 1:
            time.sleep(2)

    log.info(f"  TOTAL {catalog_label}: {len(all_matches)} matches out of {total} ({len(all_matches)/total*100:.1f}%)")
    return all_matches


# ============================================================
# Astroquery xMatch (alternative method)
# ============================================================

def astroquery_xmatch(anomalies, catalog_id, catalog_label, match_radius=3.0):
    """Cross-match using astroquery.xmatch (wraps CDS)."""
    if not HAVE_ASTROQUERY or not HAVE_ASTROPY:
        return None

    log.info(f"astroquery XMatch: {catalog_label}")

    try:
        # Build astropy Table
        t = Table()
        t['ra'] = [a['ra'] for a in anomalies]
        t['dec'] = [a['dec'] for a in anomalies]
        t['tid'] = [str(a['tid']) for a in anomalies]

        result = XMatch.query(
            cat1=t,
            cat2=catalog_id,
            max_distance=match_radius * u.arcsec,
            colRA1='ra',
            colDec1='dec',
        )

        log.info(f"  {catalog_label}: {len(result)} matches")

        # Convert to dict keyed by tid
        matches = {}
        for row in result:
            tid = str(row['tid'])
            matches[tid] = {col: str(row[col]) for col in result.colnames}

        return matches

    except Exception as e:
        log.warning(f"astroquery XMatch failed for {catalog_label}: {e}")
        return None


# ============================================================
# NOIRLab DataLab TAP (for Legacy Survey DR10)
# ============================================================

def noirlab_tap_crossmatch(anomalies, batch_size=1000):
    """
    Cross-match against Legacy Survey DR10 via NOIRLab DataLab TAP.
    Uses ADQL cone search in batches (no table upload needed).
    """
    log.info(f"NOIRLab TAP: Legacy Survey DR10, {len(anomalies):,} objects")

    tap_url = 'https://datalab.noirlab.edu/tap/sync'
    all_matches = {}
    total = len(anomalies)
    n_batches = (total + batch_size - 1) // batch_size

    for batch_idx in range(n_batches):
        start = batch_idx * batch_size
        end = min(start + batch_size, total)
        batch = anomalies[start:end]

        # Build ADQL with UNION of point-in-circle conditions
        # For large batches, use a simulated upload via VALUES
        # NOIRLab TAP supports async queries for large results

        # Build coordinate list for CONTAINS query
        conditions = []
        for a in batch:
            conditions.append(
                f"CONTAINS(POINT('ICRS', t.ra, t.dec), "
                f"CIRCLE('ICRS', {a['ra']:.6f}, {a['dec']:.6f}, {MATCH_RADIUS_ARCSEC/3600.0:.8f})) = 1"
            )

        # For batches > 50, use a different approach: query a box and filter
        if len(batch) > 50:
            ra_min = min(a['ra'] for a in batch)
            ra_max = max(a['ra'] for a in batch)
            dec_min = min(a['dec'] for a in batch)
            dec_max = max(a['dec'] for a in batch)

            # Add margin
            margin = MATCH_RADIUS_ARCSEC / 3600.0 + 0.01
            dec_min -= margin
            dec_max += margin

            adql = f"""
            SELECT t.ls_id, t.ra, t.dec, t.type,
                   t.flux_g, t.flux_r, t.flux_z,
                   t.flux_ivar_g, t.flux_ivar_r, t.flux_ivar_z,
                   t.shape_r, t.shape_e1, t.shape_e2,
                   t.ref_cat, t.ref_id, t.maskbits
            FROM ls_dr10.tractor AS t
            WHERE t.dec BETWEEN {dec_min:.6f} AND {dec_max:.6f}
              AND t.ra BETWEEN {ra_min:.6f} AND {ra_max:.6f}
            """

            try:
                if HAVE_REQUESTS:
                    r = requests.get(tap_url, params={
                        'REQUEST': 'doQuery',
                        'LANG': 'ADQL',
                        'FORMAT': 'csv',
                        'QUERY': adql,
                    }, timeout=120)
                    r.raise_for_status()
                    result_csv = r.text
                else:
                    import urllib.request, urllib.parse
                    params = urllib.parse.urlencode({
                        'REQUEST': 'doQuery',
                        'LANG': 'ADQL',
                        'FORMAT': 'csv',
                        'QUERY': adql,
                    })
                    req = urllib.request.Request(f'{tap_url}?{params}')
                    with urllib.request.urlopen(req, timeout=120) as resp:
                        result_csv = resp.read().decode('utf-8')

                lines = result_csv.strip().splitlines()
                if len(lines) > 1:
                    # Parse and do local cross-match
                    reader = csv.DictReader(io.StringIO(result_csv))
                    ls_objects = list(reader)

                    # Match each anomaly to closest LS object
                    for a in batch:
                        best_dist = float('inf')
                        best_match = None
                        for ls_obj in ls_objects:
                            try:
                                dra = (float(ls_obj['ra']) - a['ra']) * \
                                      3600.0 * abs(cos_deg(a['dec']))
                                ddec = (float(ls_obj['dec']) - a['dec']) * 3600.0
                                dist = (dra**2 + ddec**2)**0.5
                                if dist < MATCH_RADIUS_ARCSEC and dist < best_dist:
                                    best_dist = dist
                                    best_match = ls_obj
                            except (ValueError, KeyError):
                                continue
                        if best_match:
                            all_matches[str(a['tid'])] = best_match

                    log.info(f"  batch {batch_idx+1}/{n_batches}: "
                             f"{sum(1 for a in batch if str(a['tid']) in all_matches)} matches "
                             f"from {len(ls_objects)} LS objects")
                else:
                    log.info(f"  batch {batch_idx+1}/{n_batches}: 0 LS objects in region")

            except Exception as e:
                log.warning(f"  batch {batch_idx+1}/{n_batches} failed: {e}")

        else:
            # Small batch: individual CONTAINS queries
            or_clause = ' OR '.join(conditions)
            adql = f"""
            SELECT t.ls_id, t.ra, t.dec, t.type,
                   t.flux_g, t.flux_r, t.flux_z,
                   t.shape_r
            FROM ls_dr10.tractor AS t
            WHERE {or_clause}
            """
            try:
                if HAVE_REQUESTS:
                    r = requests.get(tap_url, params={
                        'REQUEST': 'doQuery',
                        'LANG': 'ADQL',
                        'FORMAT': 'csv',
                        'QUERY': adql,
                    }, timeout=60)
                    r.raise_for_status()
                    lines = r.text.strip().splitlines()
                    log.info(f"  batch {batch_idx+1}/{n_batches}: {max(0, len(lines)-1)} LS objects")
                    if len(lines) > 1:
                        reader = csv.DictReader(io.StringIO(r.text))
                        for row in reader:
                            # Find closest anomaly
                            for a in batch:
                                try:
                                    dra = (float(row['ra']) - a['ra']) * \
                                          3600.0 * abs(cos_deg(a['dec']))
                                    ddec = (float(row['dec']) - a['dec']) * 3600.0
                                    dist = (dra**2 + ddec**2)**0.5
                                    if dist < MATCH_RADIUS_ARCSEC:
                                        all_matches[str(a['tid'])] = row
                                        break
                                except (ValueError, KeyError):
                                    continue
            except Exception as e:
                log.warning(f"  batch {batch_idx+1} failed: {e}")

        if batch_idx < n_batches - 1 and batch_idx % 10 == 9:
            time.sleep(1)  # Rate limit

    log.info(f"  TOTAL LS DR10: {len(all_matches)} matches out of {total} ({len(all_matches)/total*100:.1f}%)")
    return all_matches


def cos_deg(deg):
    """Cosine of angle in degrees."""
    import math
    return math.cos(math.radians(deg))


# ============================================================
# DESI redshift lookup via NOIRLab DataLab
# ============================================================

def query_desi_redshifts(anomalies, batch_size=5000):
    """
    Query DESI DR1 spectroscopic catalog for redshifts via NOIRLab DataLab.
    Uses TARGETID join.
    """
    log.info(f"Querying DESI DR1 redshifts for {len(anomalies):,} objects")

    tap_url = 'https://datalab.noirlab.edu/tap/sync'
    all_redshifts = {}
    total = len(anomalies)
    n_batches = (total + batch_size - 1) // batch_size

    for batch_idx in range(n_batches):
        start = batch_idx * batch_size
        end = min(start + batch_size, total)
        batch = anomalies[start:end]

        tids = ','.join(str(a['tid']) for a in batch)

        adql = f"""
        SELECT z.targetid, z.z AS redshift, z.zerr, z.zwarn, z.spectype, z.subtype,
               z.deltachi2, z.tsnr2_lrg, z.tsnr2_elg, z.tsnr2_qso
        FROM desi_dr1.zpix AS z
        WHERE z.targetid IN ({tids})
          AND z.zcat_primary = True
        """

        try:
            if HAVE_REQUESTS:
                r = requests.get(tap_url, params={
                    'REQUEST': 'doQuery',
                    'LANG': 'ADQL',
                    'FORMAT': 'csv',
                    'QUERY': adql,
                }, timeout=120)
                r.raise_for_status()
                result_csv = r.text
            else:
                import urllib.request, urllib.parse
                params = urllib.parse.urlencode({
                    'REQUEST': 'doQuery',
                    'LANG': 'ADQL',
                    'FORMAT': 'csv',
                    'QUERY': adql,
                })
                req = urllib.request.Request(f'{tap_url}?{params}')
                with urllib.request.urlopen(req, timeout=120) as resp:
                    result_csv = resp.read().decode('utf-8')

            lines = result_csv.strip().splitlines()
            if len(lines) > 1:
                reader = csv.DictReader(io.StringIO(result_csv))
                batch_matches = 0
                for row in reader:
                    tid = row.get('targetid', '')
                    if tid:
                        all_redshifts[tid] = row
                        batch_matches += 1
                log.info(f"  redshift batch {batch_idx+1}/{n_batches}: {batch_matches} matches")
            else:
                log.info(f"  redshift batch {batch_idx+1}/{n_batches}: 0 matches")

        except Exception as e:
            log.warning(f"  redshift batch {batch_idx+1} failed: {e}")

        if batch_idx < n_batches - 1 and batch_idx % 5 == 4:
            time.sleep(1)

    log.info(f"  TOTAL redshifts: {len(all_redshifts)} out of {total} ({len(all_redshifts)/total*100:.1f}%)")
    return all_redshifts


# ============================================================
# Verification
# ============================================================

def verify_service(catalog_id, label):
    """Quick test with 5 known objects to verify a CDS service works."""
    log.info(f"Verifying {label}...")

    # Use M31 center + Vega + Polaris (known bright objects with AllWISE/Gaia entries)
    test_csv = 'ra,dec,tid,score\n10.684,41.269,test_m31,99\n279.235,38.783,test_vega,99\n37.954,89.264,test_polaris,99'

    try:
        result = cds_xmatch_chunk(test_csv, catalog_id, match_radius=10.0, timeout=30)
        lines = result.strip().splitlines()
        n_matches = max(0, len(lines) - 1)
        log.info(f"  {label} verification: {n_matches}/3 matches")
        return n_matches > 0
    except Exception as e:
        log.warning(f"  {label} verification FAILED: {e}")
        return False


# ============================================================
# Main pipeline
# ============================================================

def merge_results(anomalies, allwise_matches, gaia_matches, catwise_matches,
                  ls_matches, sdss_matches, milliquas_matches, redshift_matches):
    """Merge all cross-match results into a single table."""
    log.info("Merging all cross-match results...")

    rows = []
    for a in anomalies:
        tid = str(a['tid'])
        row = {
            'tid': a['tid'],
            'ra': a['ra'],
            'dec': a['dec'],
            'anomaly_score': a['score'],
            'worst_band': a['worst'],
            'residual_B': a['rB'],
            'residual_R': a['rR'],
            'residual_Z': a['rZ'],
        }

        # Redshift
        if tid in redshift_matches:
            z = redshift_matches[tid]
            row['redshift'] = z.get('redshift', '')
            row['redshift_err'] = z.get('zerr', '')
            row['zwarn'] = z.get('zwarn', '')
            row['spectype'] = z.get('spectype', '')
            row['subtype'] = z.get('subtype', '')
            row['deltachi2'] = z.get('deltachi2', '')

        # AllWISE
        if tid in allwise_matches:
            w = allwise_matches[tid]
            row['W1mag'] = w.get('W1mag', '')
            row['W2mag'] = w.get('W2mag', '')
            row['W3mag'] = w.get('W3mag', '')
            row['W4mag'] = w.get('W4mag', '')
            row['e_W1mag'] = w.get('e_W1mag', '')
            row['e_W2mag'] = w.get('e_W2mag', '')
            row['allwise_dist_arcsec'] = w.get('angDist', '')
            # Compute W1-W2 color
            try:
                w1 = float(w.get('W1mag', ''))
                w2 = float(w.get('W2mag', ''))
                row['W1_W2_color'] = round(w1 - w2, 3)
            except (ValueError, TypeError):
                row['W1_W2_color'] = ''
        elif tid in catwise_matches:
            # Fallback to CatWISE2020
            c = catwise_matches[tid]
            row['W1mag'] = c.get('W1mproPM', '')
            row['W2mag'] = c.get('W2mproPM', '')
            row['e_W1mag'] = c.get('e_W1mproPM', '')
            row['e_W2mag'] = c.get('e_W2mproPM', '')
            row['allwise_dist_arcsec'] = c.get('angDist', '')
            try:
                w1 = float(c.get('W1mproPM', ''))
                w2 = float(c.get('W2mproPM', ''))
                row['W1_W2_color'] = round(w1 - w2, 3)
            except (ValueError, TypeError):
                row['W1_W2_color'] = ''

        # Gaia DR3
        if tid in gaia_matches:
            g = gaia_matches[tid]
            row['gaia_pmra'] = g.get('pmRA', '')
            row['gaia_pmdec'] = g.get('pmDE', '')
            row['gaia_parallax'] = g.get('Plx', '')
            row['gaia_parallax_err'] = g.get('e_Plx', '')
            row['gaia_gmag'] = g.get('Gmag', '')
            row['gaia_bpmag'] = g.get('BPmag', '')
            row['gaia_rpmag'] = g.get('RPmag', '')
            row['gaia_dist_arcsec'] = g.get('angDist', '')
            # Flag as stellar if significant parallax
            try:
                plx = float(g.get('Plx', '0'))
                plx_err = float(g.get('e_Plx', '1'))
                row['likely_star'] = 1 if (plx > 0 and plx / plx_err > 3) else 0
            except (ValueError, TypeError):
                row['likely_star'] = ''

        # Legacy Survey DR10
        if tid in ls_matches:
            ls = ls_matches[tid]
            row['ls_type'] = ls.get('type', '')
            row['ls_shape_r'] = ls.get('shape_r', '')
            # Convert fluxes to magnitudes (nanomaggies)
            import math
            for band in ['g', 'r', 'z']:
                flux_key = f'flux_{band}'
                try:
                    flux = float(ls.get(flux_key, '0'))
                    if flux > 0:
                        row[f'ls_{band}mag'] = round(22.5 - 2.5 * math.log10(flux), 3)
                    else:
                        row[f'ls_{band}mag'] = ''
                except (ValueError, TypeError):
                    row[f'ls_{band}mag'] = ''
            # Compute g-r, r-z colors
            try:
                g_mag = float(row.get('ls_gmag', ''))
                r_mag = float(row.get('ls_rmag', ''))
                row['g_r_color'] = round(g_mag - r_mag, 3)
            except (ValueError, TypeError):
                row['g_r_color'] = ''
            try:
                r_mag = float(row.get('ls_rmag', ''))
                z_mag = float(row.get('ls_zmag', ''))
                row['r_z_color'] = round(r_mag - z_mag, 3)
            except (ValueError, TypeError):
                row['r_z_color'] = ''

        # SDSS
        if tid in sdss_matches:
            s = sdss_matches[tid]
            row['sdss_gmag'] = s.get('gmag', '')
            row['sdss_rmag'] = s.get('rmag', '')
            row['sdss_class'] = s.get('cl', '')

        # Milliquas
        if tid in milliquas_matches:
            m = milliquas_matches[tid]
            row['known_qso'] = 1
            row['qso_type'] = m.get('Type', '')
            row['qso_name'] = m.get('Name', '')
            row['qso_z'] = m.get('z', '')
        else:
            row['known_qso'] = 0

        # Classification flags
        row['has_allwise'] = 1 if (tid in allwise_matches or tid in catwise_matches) else 0
        row['has_gaia'] = 1 if tid in gaia_matches else 0
        row['has_redshift'] = 1 if tid in redshift_matches else 0
        row['in_any_catalog'] = 1 if any(tid in m for m in
            [allwise_matches, gaia_matches, sdss_matches, milliquas_matches]) else 0

        rows.append(row)

    return rows


def save_results(rows, output_dir):
    """Save merged cross-match results."""
    # Define column order
    columns = [
        'tid', 'ra', 'dec', 'anomaly_score', 'worst_band',
        'residual_B', 'residual_R', 'residual_Z',
        'redshift', 'redshift_err', 'zwarn', 'spectype', 'subtype', 'deltachi2',
        'W1mag', 'W2mag', 'W3mag', 'W4mag', 'e_W1mag', 'e_W2mag',
        'W1_W2_color', 'allwise_dist_arcsec',
        'gaia_pmra', 'gaia_pmdec', 'gaia_parallax', 'gaia_parallax_err',
        'gaia_gmag', 'gaia_bpmag', 'gaia_rpmag', 'gaia_dist_arcsec', 'likely_star',
        'ls_type', 'ls_gmag', 'ls_rmag', 'ls_zmag', 'ls_shape_r',
        'g_r_color', 'r_z_color',
        'sdss_gmag', 'sdss_rmag', 'sdss_class',
        'known_qso', 'qso_type', 'qso_name', 'qso_z',
        'has_allwise', 'has_gaia', 'has_redshift', 'in_any_catalog',
    ]

    # CSV output
    csv_path = os.path.join(output_dir, 'anomaly_crossmatch.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    log.info(f"Saved: {csv_path} ({os.path.getsize(csv_path) / 1024 / 1024:.1f} MB)")

    # Also save as JSON for easy loading
    json_path = os.path.join(output_dir, 'anomaly_crossmatch.json')
    with open(json_path, 'w') as f:
        json.dump(rows, f, default=str)
    log.info(f"Saved: {json_path} ({os.path.getsize(json_path) / 1024 / 1024:.1f} MB)")

    # Summary statistics
    n_total = len(rows)
    n_with_allwise = sum(1 for r in rows if r.get('has_allwise'))
    n_with_gaia = sum(1 for r in rows if r.get('has_gaia'))
    n_with_redshift = sum(1 for r in rows if r.get('has_redshift'))
    n_likely_star = sum(1 for r in rows if r.get('likely_star') == 1)
    n_known_qso = sum(1 for r in rows if r.get('known_qso') == 1)
    n_in_any = sum(1 for r in rows if r.get('in_any_catalog'))
    n_genuinely_new = n_total - n_in_any

    # W1-W2 color distribution
    w12_values = [float(r['W1_W2_color']) for r in rows
                  if r.get('W1_W2_color') not in ('', None)]
    n_qso_color = sum(1 for w in w12_values if w > 0.8) if w12_values else 0

    summary = {
        'total_anomalies': n_total,
        'match_radius_arcsec': MATCH_RADIUS_ARCSEC,
        'with_allwise': n_with_allwise,
        'with_gaia': n_with_gaia,
        'with_redshift': n_with_redshift,
        'likely_stars': n_likely_star,
        'known_qsos': n_known_qso,
        'in_any_catalog': n_in_any,
        'genuinely_new': n_genuinely_new,
        'w1_w2_gt_0.8_qso_candidates': n_qso_color,
        'w1_w2_values_available': len(w12_values),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
    }

    summary_path = os.path.join(output_dir, 'crossmatch_summary.json')
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    log.info(f"Saved: {summary_path}")

    # Print summary
    log.info("=" * 60)
    log.info("CROSS-MATCH SUMMARY")
    log.info("=" * 60)
    log.info(f"Total anomalies:        {n_total:>8,}")
    log.info(f"With AllWISE/CatWISE:   {n_with_allwise:>8,} ({n_with_allwise/n_total*100:.1f}%)")
    log.info(f"With Gaia DR3:          {n_with_gaia:>8,} ({n_with_gaia/n_total*100:.1f}%)")
    log.info(f"With DESI redshift:     {n_with_redshift:>8,} ({n_with_redshift/n_total*100:.1f}%)")
    log.info(f"Likely stars (parallax):{n_likely_star:>8,} ({n_likely_star/n_total*100:.1f}%)")
    log.info(f"Known QSOs (Milliquas): {n_known_qso:>8,} ({n_known_qso/n_total*100:.1f}%)")
    log.info(f"In ANY catalog:         {n_in_any:>8,} ({n_in_any/n_total*100:.1f}%)")
    log.info(f"Genuinely new:          {n_genuinely_new:>8,} ({n_genuinely_new/n_total*100:.1f}%)")
    if w12_values:
        log.info(f"W1-W2 > 0.8 (QSO-like):{n_qso_color:>8,}")
    log.info("=" * 60)

    return summary


def main():
    t_start = time.time()

    # Load anomalies
    anomalies = load_anomalies(ANOMALY_FILE)

    # Verify CDS is up
    cds_ok = verify_service('vizier:II/328/allwise', 'AllWISE via CDS')

    # Cross-match against each catalog
    allwise_matches = {}
    gaia_matches = {}
    catwise_matches = {}
    sdss_matches = {}
    milliquas_matches = {}
    ls_matches = {}
    redshift_matches = {}

    if cds_ok:
        log.info("\n" + "=" * 60)
        log.info("PHASE 1: CDS xMatch bulk cross-matching")
        log.info("=" * 60)

        # AllWISE (most important for W1-W2 color)
        allwise_matches = cds_xmatch_bulk(anomalies, 'vizier:II/328/allwise', 'AllWISE')

        # Gaia DR3 (proper motions)
        gaia_matches = cds_xmatch_bulk(anomalies, 'vizier:I/355/gaiadr3', 'Gaia DR3')

        # CatWISE2020 (deeper, fill in AllWISE gaps)
        if len(allwise_matches) < len(anomalies) * 0.5:
            log.info("AllWISE coverage < 50%, trying CatWISE2020...")
            catwise_matches = cds_xmatch_bulk(anomalies, 'vizier:II/365/catwise', 'CatWISE2020')

        # SDSS DR16
        sdss_matches = cds_xmatch_bulk(anomalies, 'vizier:V/154/sdss16', 'SDSS DR16')

        # Milliquas v8
        milliquas_matches = cds_xmatch_bulk(anomalies, 'vizier:VII/290/catalog', 'Milliquas v8')

    elif HAVE_ASTROQUERY:
        log.info("\n" + "=" * 60)
        log.info("PHASE 1: astroquery xMatch (CDS fallback)")
        log.info("=" * 60)

        allwise_matches = astroquery_xmatch(anomalies, 'vizier:II/328/allwise', 'AllWISE') or {}
        gaia_matches = astroquery_xmatch(anomalies, 'vizier:I/355/gaiadr3', 'Gaia DR3') or {}
        milliquas_matches = astroquery_xmatch(anomalies, 'vizier:VII/290/catalog', 'Milliquas v8') or {}

    else:
        log.error("CDS is down and astroquery not available. Cannot proceed with CDS-based matching.")
        log.error("Install astroquery: pip install astroquery")

    # PHASE 2: NOIRLab DataLab for Legacy Survey + DESI redshifts
    log.info("\n" + "=" * 60)
    log.info("PHASE 2: NOIRLab DataLab (Legacy Survey + DESI redshifts)")
    log.info("=" * 60)

    try:
        redshift_matches = query_desi_redshifts(anomalies)
    except Exception as e:
        log.error(f"DESI redshift query failed: {e}")

    try:
        ls_matches = noirlab_tap_crossmatch(anomalies)
    except Exception as e:
        log.error(f"Legacy Survey cross-match failed: {e}")

    # PHASE 3: Merge and save
    log.info("\n" + "=" * 60)
    log.info("PHASE 3: Merging results")
    log.info("=" * 60)

    rows = merge_results(anomalies, allwise_matches, gaia_matches, catwise_matches,
                         ls_matches, sdss_matches, milliquas_matches, redshift_matches)

    summary = save_results(rows, OUTPUT_DIR)

    elapsed = time.time() - t_start
    log.info(f"\nTotal time: {elapsed/60:.1f} minutes")

    # Save checkpoint
    checkpoint = {
        'status': 'COMPLETE',
        'elapsed_seconds': round(elapsed),
        'summary': summary,
        'services_used': {
            'cds_xmatch': cds_ok,
            'noirlab_tap': len(redshift_matches) > 0 or len(ls_matches) > 0,
        },
    }
    with open(os.path.join(OUTPUT_DIR, 'checkpoint.json'), 'w') as f:
        json.dump(checkpoint, f, indent=2)

    return summary


if __name__ == '__main__':
    main()
