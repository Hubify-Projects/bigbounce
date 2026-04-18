#!/usr/bin/env python3
"""Cross-match TIC 374313355 against SIMBAD + Gaia DR3.

Target: RA=160.148889 deg, Dec=+5.091599 deg (ICRS), Tmag=18.52,
P=13.782 d Lomb-Scargle peak (FAP~4e-263).
"""

from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord

TARGET_RA = 160.148889  # deg
TARGET_DEC = 5.091599   # deg
TMAG = 18.517
PERIOD_D = 13.782472
OUTDIR = Path(__file__).parent


def retry(fn, label, tries=3, backoff=5.0):
    last_err = None
    for i in range(tries):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            last_err = e
            print(f"[{label}] attempt {i+1}/{tries} failed: {e}", file=sys.stderr)
            if i < tries - 1:
                time.sleep(backoff * (i + 1))
    raise RuntimeError(f"{label} failed after {tries} tries: {last_err}")


def run_simbad(coord: SkyCoord) -> dict:
    from astroquery.simbad import Simbad

    custom = Simbad()
    # Default fields plus otype/sptype/flux info
    try:
        custom.add_votable_fields("otype", "sp_type", "flux(V)", "flux(G)", "ids")
    except Exception as e:  # noqa: BLE001
        print(f"[simbad] could not add all extended fields: {e}", file=sys.stderr)

    out: dict = {
        "queries": [],
        "target": {"ra_deg": TARGET_RA, "dec_deg": TARGET_DEC},
    }

    for radius_arcsec in (5.0, 30.0):
        def do_query(r=radius_arcsec):
            return custom.query_region(coord, radius=r * u.arcsec)

        tbl = retry(do_query, f"simbad_{radius_arcsec}arcsec")
        entry: dict = {"radius_arcsec": radius_arcsec}
        if tbl is None or len(tbl) == 0:
            entry["n_hits"] = 0
            entry["hits"] = []
        else:
            entry["n_hits"] = int(len(tbl))
            entry["columns"] = [str(c) for c in tbl.colnames]
            hits: list[dict] = []
            # compute distance to target for each hit
            for row in tbl:
                h: dict = {}
                for col in tbl.colnames:
                    v = row[col]
                    try:
                        if hasattr(v, "mask") and bool(v.mask):
                            v = None
                        else:
                            v = v.item() if hasattr(v, "item") else v
                    except Exception:
                        try:
                            v = str(v)
                        except Exception:
                            v = None
                    if isinstance(v, bytes):
                        v = v.decode("utf-8", errors="replace")
                    h[col] = v
                # Try to compute angular distance
                try:
                    from astropy.coordinates import SkyCoord as SC

                    ra_val = h.get("ra") or h.get("RA")
                    dec_val = h.get("dec") or h.get("DEC")
                    if ra_val is not None and dec_val is not None:
                        if isinstance(ra_val, (int, float)) and isinstance(
                            dec_val, (int, float)
                        ):
                            sc = SC(ra=ra_val * u.deg, dec=dec_val * u.deg)
                        else:
                            sc = SC(f"{ra_val} {dec_val}", unit=(u.hourangle, u.deg))
                        h["_dist_arcsec"] = float(coord.separation(sc).arcsec)
                except Exception as e:  # noqa: BLE001
                    h["_dist_arcsec_error"] = str(e)
                hits.append(h)
            entry["hits"] = hits
        out["queries"].append(entry)

    return out


def run_gaia(coord: SkyCoord) -> dict:
    from astroquery.gaia import Gaia

    Gaia.MAIN_GAIA_TABLE = "gaiadr3.gaia_source"
    Gaia.ROW_LIMIT = 50

    out: dict = {
        "queries": [],
        "target": {"ra_deg": TARGET_RA, "dec_deg": TARGET_DEC},
    }

    for radius_arcsec in (5.0, 30.0):
        def do_query(r=radius_arcsec):
            job = Gaia.cone_search_async(coord, radius=r * u.arcsec)
            return job.get_results()

        tbl = retry(do_query, f"gaia_{radius_arcsec}arcsec")
        entry: dict = {"radius_arcsec": radius_arcsec}
        if tbl is None or len(tbl) == 0:
            entry["n_hits"] = 0
            entry["hits"] = []
        else:
            entry["n_hits"] = int(len(tbl))
            keep_cols = [
                "source_id",
                "ra",
                "dec",
                "parallax",
                "parallax_error",
                "pmra",
                "pmdec",
                "phot_g_mean_mag",
                "phot_bp_mean_mag",
                "phot_rp_mean_mag",
                "bp_rp",
                "ruwe",
                "phot_variable_flag",
                "dist",  # returned by cone_search_async in deg
                "in_qso_candidates",
                "in_galaxy_candidates",
                "non_single_star",
                "has_xp_continuous",
                "has_xp_sampled",
                "teff_gspphot",
            ]
            cols = [c for c in keep_cols if c in tbl.colnames]
            entry["columns_returned"] = cols
            hits: list[dict] = []
            for row in tbl:
                h: dict = {}
                for col in cols:
                    v = row[col]
                    try:
                        if hasattr(v, "mask") and bool(v.mask):
                            v = None
                        else:
                            v = v.item() if hasattr(v, "item") else v
                    except Exception:
                        v = None
                    if isinstance(v, bytes):
                        v = v.decode("utf-8", errors="replace")
                    h[col] = v
                # cone_search_async returns `dist` in degrees
                dist_deg = h.get("dist")
                if isinstance(dist_deg, (int, float)):
                    h["_dist_arcsec"] = dist_deg * 3600.0
                hits.append(h)
            # sort by distance ascending
            hits.sort(key=lambda r: r.get("_dist_arcsec", math.inf))
            entry["hits"] = hits
        out["queries"].append(entry)

    return out


def derive_params(gaia_hit: dict) -> dict:
    """Given the nearest Gaia DR3 hit, derive distance, abs G, quality flags."""
    d: dict = {}
    G = gaia_hit.get("phot_g_mean_mag")
    BP = gaia_hit.get("phot_bp_mean_mag")
    RP = gaia_hit.get("phot_rp_mean_mag")
    bp_rp = gaia_hit.get("bp_rp")
    plx = gaia_hit.get("parallax")
    plx_err = gaia_hit.get("parallax_error")
    ruwe = gaia_hit.get("ruwe")
    varflag = gaia_hit.get("phot_variable_flag")

    d["G"] = G
    d["BP"] = BP
    d["RP"] = RP
    d["bp_rp"] = bp_rp if bp_rp is not None else (
        BP - RP if (isinstance(BP, (int, float)) and isinstance(RP, (int, float))) else None
    )
    d["parallax_mas"] = plx
    d["parallax_error_mas"] = plx_err
    d["ruwe"] = ruwe
    d["phot_variable_flag"] = varflag

    if isinstance(plx, (int, float)) and isinstance(plx_err, (int, float)) and plx_err > 0:
        d["parallax_snr"] = plx / plx_err
        if plx > 0:
            dist_pc = 1000.0 / plx  # mas → pc
            d["distance_pc_naive"] = dist_pc
            if isinstance(G, (int, float)):
                # Absolute mag: M = m - 5 log10(d/10pc) = m + 5 - 5log10(d)
                d["abs_G_naive"] = G - 5.0 * math.log10(dist_pc) + 5.0
        else:
            d["distance_pc_naive"] = None
            d["abs_G_naive"] = None
    else:
        d["parallax_snr"] = None
        d["distance_pc_naive"] = None
        d["abs_G_naive"] = None

    return d


def main() -> int:
    coord = SkyCoord(ra=TARGET_RA * u.deg, dec=TARGET_DEC * u.deg, frame="icrs")
    print(f"Target: {coord.to_string('hmsdms')} (Tmag={TMAG}, P={PERIOD_D} d)")

    # SIMBAD
    try:
        simbad_result = run_simbad(coord)
    except Exception as e:  # noqa: BLE001
        simbad_result = {"service_unavailable": True, "error": str(e)}
    with open(OUTDIR / "simbad_hit.json", "w") as f:
        json.dump(simbad_result, f, indent=2, default=str)
    print(f"SIMBAD: wrote simbad_hit.json")

    # Gaia
    try:
        gaia_result = run_gaia(coord)
    except Exception as e:  # noqa: BLE001
        gaia_result = {"service_unavailable": True, "error": str(e)}
    with open(OUTDIR / "gaia_dr3_hit.json", "w") as f:
        json.dump(gaia_result, f, indent=2, default=str)
    print(f"Gaia DR3: wrote gaia_dr3_hit.json")

    # Derive params for the nearest Gaia hit (if any)
    derived = None
    if not gaia_result.get("service_unavailable"):
        for q in gaia_result["queries"]:
            if q["n_hits"] > 0:
                derived = derive_params(q["hits"][0])
                derived["nearest_hit_radius_query_arcsec"] = q["radius_arcsec"]
                derived["nearest_hit_source_id"] = q["hits"][0].get("source_id")
                derived["nearest_hit_dist_arcsec"] = q["hits"][0].get("_dist_arcsec")
                break
    if derived is not None:
        with open(OUTDIR / "derived_params.json", "w") as f:
            json.dump(derived, f, indent=2, default=str)
        print(f"Derived: {json.dumps(derived, indent=2, default=str)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
