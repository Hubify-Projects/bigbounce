#!/usr/bin/env python3
"""
NED deep cross-match for Paper 3 novel anomalies (P3-B, NED pass).

Extends the SIMBAD-only cross-match (projects/cross_survey/results/
simbad_crossmatch_summary.json) by re-querying the SIMBAD-novel objects
against NED. Goal: reclassify SIMBAD-"uncatalogued" into
"ned_archival_identified" vs "still_uncatalogued".

VizieR is intentionally deferred to a follow-up fire — the VizieR TAP
service was hanging during the first attempt (no response after 13 min).
Filed as `P3-B-VIZIER` in queue.md for a clean-retry slot.

Input:  projects/cross_survey/results/simbad_crossmatch_summary.json
        (top_20_novel_objects per survey — 80 objects total across
         SDSS_DR18, eROSITA, NEOWISE, Gaia_DR3)

Output: projects/cross_survey/results/ned_crossmatch_summary.json
        Written incrementally after each object so progress is recoverable.

Each object is classified:
  - "ned_matched"           (SIMBAD-novel, NED-found)
  - "still_uncatalogued"    (SIMBAD-novel, NED-novel)
  - "error"                 (query failed after retries)
"""

import json
import time
from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.ipac.ned import Ned

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
RESULTS_DIR = BASE_DIR / "projects/cross_survey/results"
INPUT = RESULTS_DIR / "simbad_crossmatch_summary.json"
OUTPUT = RESULTS_DIR / "ned_crossmatch_summary.json"

RADIUS_ARCSEC = 5.0
QUERY_DELAY_SEC = 0.3
MAX_RETRIES = 2

# Per-query watchdog: if NED doesn't respond in this many seconds, mark
# error and move on.
PER_QUERY_TIMEOUT_SEC = 8.0

Ned.TIMEOUT = PER_QUERY_TIMEOUT_SEC


def query_ned(ra, dec):
    """Cone search NED around (ra, dec). Return dict."""
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")
    for attempt in range(MAX_RETRIES):
        try:
            table = Ned.query_region(coord, radius=RADIUS_ARCSEC * u.arcsec)
            if table is None or len(table) == 0:
                return {"matched": False, "n_matches": 0, "top_match": None}
            row = table[0]

            def _safe(key):
                try:
                    v = row[key]
                    return None if v is None else str(v)
                except Exception:
                    return None

            return {
                "matched": True,
                "n_matches": int(len(table)),
                "top_match": {
                    "name": _safe("Object Name"),
                    "type": _safe("Type"),
                    "z": _safe("Redshift"),
                },
            }
        except Exception as err:
            if attempt == MAX_RETRIES - 1:
                return {"matched": False, "n_matches": 0, "error": str(err)[:200]}
            time.sleep(0.8 + attempt)
    return {"matched": False, "n_matches": 0, "error": "retry_exhausted"}


def write_snapshot(output):
    OUTPUT.write_text(json.dumps(output, indent=2, default=str))


def main():
    print(f"Loading SIMBAD-novel exemplars from {INPUT.name}", flush=True)
    simbad = json.loads(INPUT.read_text())

    per_survey_out = {}
    global_counts = {"ned_matched": 0, "still_uncatalogued": 0, "error": 0}
    total = 0

    output = {
        "meta": {
            "description": (
                "NED cross-match of SIMBAD-novel anomalies (P3-B, NED pass). "
                "Reclassifies SIMBAD-'uncatalogued' into NED-archival-identified "
                "vs still-uncatalogued. VizieR pass deferred (hung TAP)."
            ),
            "parent_simbad_file": str(INPUT.relative_to(BASE_DIR)),
            "radius_arcsec": RADIUS_ARCSEC,
            "per_query_timeout_sec": PER_QUERY_TIMEOUT_SEC,
            "surveys_queried": [],
            "n_objects_total": 0,
            "status": "in_progress",
        },
        "global_counts": global_counts,
        "per_survey": per_survey_out,
    }

    for survey, info in simbad["per_survey"].items():
        novel = info.get("top_20_novel_objects", [])
        if not novel:
            per_survey_out[survey] = {
                "n_queried": 0,
                "per_object": [],
                "counts": {"ned_matched": 0, "still_uncatalogued": 0, "error": 0},
            }
            continue

        print(f"\n=== {survey}: {len(novel)} SIMBAD-novel objects ===", flush=True)
        per_obj = []
        counts = {"ned_matched": 0, "still_uncatalogued": 0, "error": 0}

        for obj in novel:
            ra = float(obj["ra"])
            dec = float(obj["dec"])
            ned = query_ned(ra, dec)
            time.sleep(QUERY_DELAY_SEC)

            if "error" in ned and not ned.get("matched"):
                cls = "error"
            elif ned.get("matched"):
                cls = "ned_matched"
            else:
                cls = "still_uncatalogued"

            counts[cls] += 1
            global_counts[cls] += 1
            total += 1

            per_obj.append({
                "obj_id": obj["obj_id"],
                "ra": ra,
                "dec": dec,
                "anomaly_score": obj.get("anomaly_score"),
                "classification": cls,
                "ned": ned,
            })

            print(f"  [{obj['rank']:>2}] {obj['obj_id'][:38]:<38s} -> {cls}",
                  flush=True)

            per_survey_out[survey] = {
                "n_queried": len(per_obj),
                "per_object": per_obj,
                "counts": counts,
            }
            output["meta"]["surveys_queried"] = list(per_survey_out.keys())
            output["meta"]["n_objects_total"] = total
            write_snapshot(output)

    output["meta"]["status"] = "complete"
    output["global_fractions"] = {
        k: (v / total if total else 0.0) for k, v in global_counts.items()
    }
    write_snapshot(output)
    print(f"\nWrote {OUTPUT}")
    print(f"Global: {global_counts}")
    print(f"Fractions: {output['global_fractions']}")
    return output


if __name__ == "__main__":
    main()
