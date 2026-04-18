#!/usr/bin/env python3
"""Wider Gaia DR3 search — 60" radius — since nothing within 5"."""
import json
from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

Gaia.MAIN_GAIA_TABLE = "gaiadr3.gaia_source"
Gaia.ROW_LIMIT = 200

coord = SkyCoord(ra=160.148889 * u.deg, dec=5.091599 * u.deg, frame="icrs")

job = Gaia.cone_search_async(coord, radius=60.0 * u.arcsec)
tbl = job.get_results()
print(f"n hits within 60 arcsec: {len(tbl)}")

hits = []
for row in tbl:
    h = {
        "source_id": int(row["source_id"]),
        "ra": float(row["ra"]),
        "dec": float(row["dec"]),
        "G": float(row["phot_g_mean_mag"]) if row["phot_g_mean_mag"] is not None else None,
        "bp_rp": float(row["bp_rp"]) if row["bp_rp"] is not None else None,
        "parallax": float(row["parallax"]) if row["parallax"] is not None else None,
        "parallax_error": float(row["parallax_error"]) if row["parallax_error"] is not None else None,
        "pmra": float(row["pmra"]) if row["pmra"] is not None else None,
        "pmdec": float(row["pmdec"]) if row["pmdec"] is not None else None,
        "dist_arcsec": float(row["dist"]) * 3600.0,
    }
    hits.append(h)

hits.sort(key=lambda r: r["dist_arcsec"])
for h in hits[:10]:
    print(h)

out_path = Path(__file__).parent / "gaia_dr3_wide.json"
with open(out_path, "w") as f:
    json.dump({"radius_arcsec": 60.0, "n_hits": len(hits), "hits": hits}, f, indent=2)
print(f"wrote {out_path}")
