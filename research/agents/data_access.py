#!/usr/bin/env python3
"""
Astronomical Data Access Agent

Unified interface to MAST (JWST/HST/TESS), Gaia DR3, SDSS, VizieR, and NED.
Uses astroquery for all archive access.

JWST data access methods:
  1. MAST Portal API (astroquery.mast) — query metadata, download files
  2. AWS S3 public bucket (s3://stpubdata) — direct file access, no auth
  3. MAST REST API — programmatic metadata queries

Usage:
    from research.agents.data_access import search_jwst, search_gaia, query_catalog
    jwst = search_jwst("NGC 1365", radius_arcmin=5)
    gaia = search_gaia(ra=53.23, dec=-36.14, radius_deg=0.1)
"""

import os
import json
from typing import Optional, Union
from datetime import datetime

from . import OUTPUT_DIR


def _ensure_astroquery():
    """Check astroquery is installed."""
    try:
        import astroquery
        return True
    except ImportError:
        raise ImportError(
            "astroquery is required. Install with: pip install astroquery"
        )


# ── MAST / JWST / HST ────────────────────────────────────────────────

def search_jwst(target: str = None, ra: float = None, dec: float = None,
                radius_arcmin: float = 3, filters: dict = None,
                max_results: int = 50) -> list[dict]:
    """
    Search JWST observations in MAST.

    Args:
        target: Target name (resolved by MAST) OR provide ra/dec
        ra, dec: Coordinates in degrees (J2000)
        radius_arcmin: Search radius in arcminutes
        filters: Additional MAST filters (e.g., {"instrument_name": "NIRCAM"})
        max_results: Maximum results to return
    """
    _ensure_astroquery()
    from astroquery.mast import Observations
    from astropy.coordinates import SkyCoord
    import astropy.units as u

    criteria = {"obs_collection": "JWST"}
    if filters:
        criteria.update(filters)

    if target:
        results = Observations.query_criteria(
            objectname=target, radius=f"{radius_arcmin} arcmin",
            **criteria,
        )
    elif ra is not None and dec is not None:
        coord = SkyCoord(ra=ra, dec=dec, unit="deg")
        results = Observations.query_criteria(
            coordinates=coord, radius=f"{radius_arcmin} arcmin",
            **criteria,
        )
    else:
        raise ValueError("Provide either target name or ra/dec coordinates")

    # Convert to list of dicts
    rows = []
    for i, row in enumerate(results[:max_results]):
        rows.append({
            "obs_id": str(row.get("obs_id", "")),
            "target_name": str(row.get("target_name", "")),
            "instrument": str(row.get("instrument_name", "")),
            "filters": str(row.get("filters", "")),
            "proposal_id": str(row.get("proposal_id", "")),
            "obs_date": str(row.get("t_min", "")),
            "exposure_time": float(row.get("t_exptime", 0)),
            "ra": float(row.get("s_ra", 0)),
            "dec": float(row.get("s_dec", 0)),
            "dataproduct_type": str(row.get("dataproduct_type", "")),
        })
    return rows


def search_mast(target: str = None, ra: float = None, dec: float = None,
                radius_arcmin: float = 3, collection: str = None,
                max_results: int = 50) -> list[dict]:
    """
    General MAST search (HST, JWST, TESS, Kepler, etc.).

    Args:
        collection: Mission name (e.g., "JWST", "HST", "TESS")
    """
    _ensure_astroquery()
    from astroquery.mast import Observations

    kwargs = {}
    if collection:
        kwargs["obs_collection"] = collection

    if target:
        results = Observations.query_criteria(
            objectname=target, radius=f"{radius_arcmin} arcmin", **kwargs,
        )
    elif ra is not None and dec is not None:
        from astropy.coordinates import SkyCoord
        coord = SkyCoord(ra=ra, dec=dec, unit="deg")
        results = Observations.query_criteria(
            coordinates=coord, radius=f"{radius_arcmin} arcmin", **kwargs,
        )
    else:
        results = Observations.query_criteria(**kwargs)

    return [dict(zip(results.colnames, row)) for row in results[:max_results]]


def jwst_s3_uri(obs_id: str) -> str:
    """
    Get the AWS S3 URI for a JWST observation (public, no auth needed).
    Bucket: s3://stpubdata/jwst/public/
    """
    return f"s3://stpubdata/jwst/public/{obs_id}/"


def mast_api_query(service: str, params: dict) -> dict:
    """
    Direct MAST REST API query.

    Args:
        service: MAST service (e.g., "Mast.Caom.Cone", "Mast.Catalogs.Filtered.Tic")
        params: Service-specific parameters
    """
    import urllib.request

    body = json.dumps({
        "service": service,
        "format": "json",
        "params": params,
    }).encode()

    req = urllib.request.Request(
        "https://mast.stsci.edu/api/v0/invoke",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


# ── Gaia DR3 ─────────────────────────────────────────────────────────

def search_gaia(ra: float, dec: float, radius_deg: float = 0.1,
                max_results: int = 100, columns: str = None) -> list[dict]:
    """
    Query Gaia DR3 catalog.

    Args:
        ra, dec: Center coordinates in degrees (J2000)
        radius_deg: Search radius in degrees
        max_results: Max rows
        columns: Specific columns (default: essential astrometry)
    """
    _ensure_astroquery()
    from astroquery.gaia import Gaia

    if columns is None:
        columns = "source_id, ra, dec, parallax, pmra, pmdec, phot_g_mean_mag, bp_rp, radial_velocity"

    query = f"""
    SELECT TOP {max_results} {columns}
    FROM gaiadr3.gaia_source
    WHERE CONTAINS(
        POINT('ICRS', ra, dec),
        CIRCLE('ICRS', {ra}, {dec}, {radius_deg})
    ) = 1
    ORDER BY phot_g_mean_mag ASC
    """

    job = Gaia.launch_job(query)
    table = job.get_results()
    return [dict(zip(table.colnames, row)) for row in table]


def gaia_adql(query: str, async_mode: bool = False) -> list[dict]:
    """
    Run arbitrary ADQL query against Gaia DR3.

    Args:
        query: Full ADQL query string
        async_mode: Use async for large queries (no row limit)
    """
    _ensure_astroquery()
    from astroquery.gaia import Gaia

    if async_mode:
        job = Gaia.launch_job_async(query)
    else:
        job = Gaia.launch_job(query)

    table = job.get_results()
    return [dict(zip(table.colnames, row)) for row in table]


# ── VizieR Catalogs ──────────────────────────────────────────────────

def query_catalog(catalog_id: str, target: str = None,
                  ra: float = None, dec: float = None,
                  radius_arcmin: float = 5,
                  max_results: int = 100) -> list[dict]:
    """
    Query any VizieR catalog.

    Args:
        catalog_id: VizieR catalog ID (e.g., "II/246" for 2MASS, "V/147" for SDSS DR12)
        target: Target name or ra/dec coordinates
    """
    _ensure_astroquery()
    from astroquery.vizier import Vizier
    from astropy.coordinates import SkyCoord
    import astropy.units as u

    v = Vizier(row_limit=max_results)

    if target:
        tables = v.query_object(target, catalog=catalog_id,
                                radius=radius_arcmin * u.arcmin)
    elif ra is not None and dec is not None:
        coord = SkyCoord(ra=ra, dec=dec, unit="deg")
        tables = v.query_region(coord, catalog=catalog_id,
                                radius=radius_arcmin * u.arcmin)
    else:
        raise ValueError("Provide either target or ra/dec")

    if not tables:
        return []

    table = tables[0]
    return [dict(zip(table.colnames, row)) for row in table]


# ── NED (Extragalactic Database) ─────────────────────────────────────

def search_ned(target: str) -> list[dict]:
    """
    Query NASA/IPAC Extragalactic Database for an object.
    Returns basic object data including redshift and classifications.
    """
    _ensure_astroquery()
    from astroquery.ned import Ned

    table = Ned.query_object(target)
    return [dict(zip(table.colnames, row)) for row in table]


# ── Utility ──────────────────────────────────────────────────────────

def save_data(data: Union[list, dict], filename: str = None) -> str:
    """Save query results to JSON in outputs directory."""
    if filename is None:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data_{ts}.json"
    path = OUTPUT_DIR / filename
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    return str(path)


if __name__ == "__main__":
    print("BigBounce Data Access Agent")
    print("=" * 40)
    print("\nAvailable data sources:")
    print("  JWST/HST/TESS  — search_jwst(), search_mast()")
    print("  JWST S3         — jwst_s3_uri() (AWS public bucket)")
    print("  MAST REST API   — mast_api_query()")
    print("  Gaia DR3        — search_gaia(), gaia_adql()")
    print("  VizieR          — query_catalog()")
    print("  NED             — search_ned()")
    print("\nAll sources are free. No API keys required.")
    print("\nRequires: pip install astroquery astropy")
