#!/usr/bin/env python3
"""
Cross-match 83 gold anomalies against SIMBAD and NED astronomical databases.
Uses 5 arcsecond search radius with 1-second rate limiting.
"""

import json
import time
import urllib.request
import urllib.parse
import urllib.error
import ssl
import sys
import os

# Paths
INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gold_anomalies.json")
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crossmatch_results.json")

SEARCH_RADIUS_ARCSEC = 5.0
RATE_LIMIT_SEC = 1.0

# Allow unverified SSL for TAP queries (some observatory certs are outdated)
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE


def query_simbad(ra_deg, dec_deg, radius_arcsec=5.0):
    """
    Query SIMBAD TAP service for objects within radius of (ra, dec).
    Returns dict with 'found', 'main_id', 'otype', 'otype_longname', 'ra', 'dec', 'error'.
    """
    # SIMBAD TAP uses ADQL
    # Convert radius from arcsec to degrees for CONTAINS/CIRCLE
    radius_deg = radius_arcsec / 3600.0

    adql = (
        f"SELECT TOP 5 main_id, otype, otypes, ra, dec "
        f"FROM basic "
        f"WHERE CONTAINS(POINT('ICRS', ra, dec), "
        f"CIRCLE('ICRS', {ra_deg}, {dec_deg}, {radius_deg})) = 1 "
        f"ORDER BY DISTANCE(POINT('ICRS', ra, dec), POINT('ICRS', {ra_deg}, {dec_deg}))"
    )

    params = urllib.parse.urlencode({
        "request": "doQuery",
        "lang": "adql",
        "format": "json",
        "query": adql,
    })

    url = f"https://simbad.u-strasbg.fr/simbad/sim-tap/sync?{params}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BigBounce-Crossmatch/1.0"})
        with urllib.request.urlopen(req, timeout=30, context=ssl_ctx) as resp:
            raw = resp.read().decode("utf-8")
            data = json.loads(raw)

            # TAP JSON format: {"metadata": [...], "data": [[...], ...]}
            if "data" in data and len(data["data"]) > 0:
                # columns: main_id, otype, otypes, ra, dec
                row = data["data"][0]
                all_matches = []
                for r in data["data"]:
                    all_matches.append({
                        "main_id": r[0],
                        "otype": r[1],
                        "otypes": r[2] if len(r) > 2 else None,
                    })
                return {
                    "found": True,
                    "main_id": row[0],
                    "otype": row[1],
                    "otypes": row[2] if len(row) > 2 else None,
                    "simbad_ra": row[3] if len(row) > 3 else None,
                    "simbad_dec": row[4] if len(row) > 4 else None,
                    "n_matches": len(data["data"]),
                    "all_matches": all_matches if len(data["data"]) > 1 else None,
                    "error": None,
                }
            else:
                return {"found": False, "main_id": None, "otype": None, "error": None}
    except Exception as e:
        return {"found": False, "main_id": None, "otype": None, "error": str(e)}


def query_ned(ra_deg, dec_deg, radius_arcsec=5.0):
    """
    Query NED for objects near (ra, dec) using the object search API.
    Returns dict with 'found', 'object_name', 'object_type', 'redshift', 'error'.
    """
    # NED has a cone search via their VO interface
    # Use the NED TAP or simple cone search
    radius_deg = radius_arcsec / 3600.0

    params = urllib.parse.urlencode({
        "search_type": "Near Position Search",
        "RA": f"{ra_deg:.6f}d",
        "DEC": f"{dec_deg:.6f}d",
        "SR": f"{radius_arcsec}",
        "of": "xml_main",
        "in_csys": "Equatorial",
        "in_equinox": "J2000",
    })

    # Use NED's VO cone search instead (more reliable for scripting)
    vo_url = (
        f"https://ned.ipac.caltech.edu/cgi-bin/nph-objsearch?"
        f"search_type=Near+Position+Search"
        f"&in_csys=Equatorial&in_equinox=J2000.0"
        f"&lon={ra_deg:.6f}d&lat={dec_deg:.6f}d"
        f"&radius={radius_arcsec:.1f}"
        f"&hconst=67.8&omegam=0.308&omegav=0.692&wmap=4&corr_z=1"
        f"&z_constraint=Unconstrained"
        f"&ot_include=ANY"
        f"&nmp_op=ANY"
        f"&out_csys=Equatorial&out_equinox=J2000.0"
        f"&obj_sort=Distance+to+search+center"
        f"&of=xml_main"
        f"&zv_breaker=30000.0"
        f"&list_limit=5"
        f"&img_stamp=NO"
    )

    try:
        req = urllib.request.Request(vo_url, headers={"User-Agent": "BigBounce-Crossmatch/1.0"})
        with urllib.request.urlopen(req, timeout=30, context=ssl_ctx) as resp:
            raw = resp.read().decode("utf-8", errors="replace")

            # Parse the XML response - look for TABLEDATA
            # NED XML uses VOTable format
            if "No object" in raw or "<TABLEDATA />" in raw or "<TABLEDATA/>" in raw:
                return {"found": False, "objects": [], "n_matches": 0, "error": None}

            # Try to extract objects from NED XML
            objects = parse_ned_xml(raw)
            if objects:
                return {
                    "found": True,
                    "objects": objects,
                    "n_matches": len(objects),
                    "primary_name": objects[0].get("name", "unknown"),
                    "primary_type": objects[0].get("type", "unknown"),
                    "primary_redshift": objects[0].get("redshift"),
                    "error": None,
                }
            else:
                return {"found": False, "objects": [], "n_matches": 0, "error": None}

    except Exception as e:
        return {"found": False, "objects": [], "n_matches": 0, "error": str(e)}


def parse_ned_xml(xml_text):
    """Parse NED VOTable XML to extract object info."""
    import xml.etree.ElementTree as ET

    objects = []
    try:
        # Clean up potential issues
        root = ET.fromstring(xml_text)

        # Handle namespaced VOTable
        ns = ""
        if root.tag.startswith("{"):
            ns = root.tag.split("}")[0] + "}"

        # Find TABLEDATA
        for tabledata in root.iter(f"{ns}TABLEDATA"):
            for tr in tabledata.iter(f"{ns}TR"):
                tds = [td.text if td.text else "" for td in tr.iter(f"{ns}TD")]
                if len(tds) >= 4:
                    obj = {
                        "name": tds[1].strip() if len(tds) > 1 else "",
                        "ra_ned": tds[2].strip() if len(tds) > 2 else "",
                        "dec_ned": tds[3].strip() if len(tds) > 3 else "",
                        "type": tds[4].strip() if len(tds) > 4 else "",
                    }
                    # Try to get redshift - it's typically in column index 6 or 7
                    if len(tds) > 6 and tds[6].strip():
                        try:
                            obj["redshift"] = float(tds[6].strip())
                        except ValueError:
                            obj["redshift"] = None
                    else:
                        obj["redshift"] = None
                    objects.append(obj)
    except ET.ParseError:
        # Fallback: regex extraction
        import re
        # Try to find object names in the raw text
        names = re.findall(r'<TD>([^<]+)</TD>', xml_text)
        if names:
            # Group into rows (NED typically has ~10 columns)
            pass

    return objects


def main():
    with open(INPUT, "r") as f:
        anomalies = json.load(f)

    print(f"Loaded {len(anomalies)} gold anomalies")
    print(f"Search radius: {SEARCH_RADIUS_ARCSEC} arcsec")
    print(f"Rate limit: {RATE_LIMIT_SEC}s between queries")
    print("=" * 70)

    results = []
    simbad_found = 0
    ned_found = 0
    simbad_errors = 0
    ned_errors = 0

    for i, obj in enumerate(anomalies):
        ra = obj["ra"]
        dec = obj["dec"]
        targetid = obj["targetid"]
        z = obj["z"]
        spectype = obj["spectype"]
        score = obj["anomaly_score"]

        print(f"\n[{i+1}/{len(anomalies)}] targetid={targetid}  RA={ra:.5f}  Dec={dec:.5f}  z={z:.4f}  type={spectype}  score={score:.3f}")

        # Query SIMBAD
        print(f"  Querying SIMBAD...", end="", flush=True)
        simbad_result = query_simbad(ra, dec, SEARCH_RADIUS_ARCSEC)
        if simbad_result["error"]:
            print(f" ERROR: {simbad_result['error'][:60]}")
            simbad_errors += 1
        elif simbad_result["found"]:
            simbad_found += 1
            print(f" FOUND: {simbad_result['main_id']} (type={simbad_result['otype']}, n={simbad_result.get('n_matches',1)})")
        else:
            print(f" NOT FOUND")

        time.sleep(RATE_LIMIT_SEC)

        # Query NED
        print(f"  Querying NED...", end="", flush=True)
        ned_result = query_ned(ra, dec, SEARCH_RADIUS_ARCSEC)
        if ned_result["error"]:
            print(f" ERROR: {ned_result['error'][:60]}")
            ned_errors += 1
        elif ned_result["found"]:
            ned_found += 1
            print(f" FOUND: {ned_result.get('primary_name','?')} (type={ned_result.get('primary_type','?')}, n={ned_result['n_matches']})")
        else:
            print(f" NOT FOUND")

        time.sleep(RATE_LIMIT_SEC)

        # Combine results
        entry = {
            "targetid": targetid,
            "ra": ra,
            "dec": dec,
            "z": z,
            "spectype": spectype,
            "anomaly_score": score,
            "simbad": {
                "found": simbad_result["found"],
                "main_id": simbad_result.get("main_id"),
                "object_type": simbad_result.get("otype"),
                "all_object_types": simbad_result.get("otypes"),
                "n_matches": simbad_result.get("n_matches", 0),
                "all_matches": simbad_result.get("all_matches"),
                "error": simbad_result.get("error"),
            },
            "ned": {
                "found": ned_result["found"],
                "primary_name": ned_result.get("primary_name"),
                "primary_type": ned_result.get("primary_type"),
                "primary_redshift": ned_result.get("primary_redshift"),
                "n_matches": ned_result.get("n_matches", 0),
                "objects": ned_result.get("objects", []) if ned_result["found"] else [],
                "error": ned_result.get("error"),
            },
            "in_simbad": simbad_result["found"],
            "in_ned": ned_result["found"],
            "in_any_database": simbad_result["found"] or ned_result["found"],
            "uncataloged": not (simbad_result["found"] or ned_result["found"]),
        }
        results.append(entry)

        # Save intermediate results every 10 objects
        if (i + 1) % 10 == 0:
            save_results(results, simbad_found, ned_found, simbad_errors, ned_errors, i + 1, len(anomalies))

    # Final save
    save_results(results, simbad_found, ned_found, simbad_errors, ned_errors, len(anomalies), len(anomalies))

    # Print summary
    print("\n" + "=" * 70)
    print("CROSS-MATCH SUMMARY")
    print("=" * 70)
    print(f"Total anomalies:          {len(anomalies)}")
    print(f"Found in SIMBAD:          {simbad_found}/{len(anomalies)} ({100*simbad_found/len(anomalies):.1f}%)")
    print(f"Found in NED:             {ned_found}/{len(anomalies)} ({100*ned_found/len(anomalies):.1f}%)")
    both = sum(1 for r in results if r["in_simbad"] and r["in_ned"])
    either = sum(1 for r in results if r["in_any_database"])
    neither = sum(1 for r in results if r["uncataloged"])
    print(f"Found in BOTH:            {both}/{len(anomalies)} ({100*both/len(anomalies):.1f}%)")
    print(f"Found in EITHER:          {either}/{len(anomalies)} ({100*either/len(anomalies):.1f}%)")
    print(f"UNCATALOGED (novel):      {neither}/{len(anomalies)} ({100*neither/len(anomalies):.1f}%)")
    print(f"SIMBAD errors:            {simbad_errors}")
    print(f"NED errors:               {ned_errors}")
    print(f"\nResults saved to: {OUTPUT}")


def save_results(results, simbad_found, ned_found, simbad_errors, ned_errors, processed, total):
    """Save results with summary metadata."""
    both = sum(1 for r in results if r["in_simbad"] and r["in_ned"])
    either = sum(1 for r in results if r["in_any_database"])
    neither = sum(1 for r in results if r["uncataloged"])

    output = {
        "metadata": {
            "description": "Cross-match of 83 gold anomalies against SIMBAD and NED",
            "search_radius_arcsec": SEARCH_RADIUS_ARCSEC,
            "processed": processed,
            "total": total,
            "complete": processed == total,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "summary": {
            "total_anomalies": total,
            "in_simbad": simbad_found,
            "in_ned": ned_found,
            "in_both": both,
            "in_either": either,
            "uncataloged": neither,
            "simbad_errors": simbad_errors,
            "ned_errors": ned_errors,
            "pct_simbad": round(100 * simbad_found / max(processed, 1), 1),
            "pct_ned": round(100 * ned_found / max(processed, 1), 1),
            "pct_uncataloged": round(100 * neither / max(processed, 1), 1),
        },
        "results": results,
    }

    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2)
    print(f"  [Saved {processed}/{total} results to {OUTPUT}]")


if __name__ == "__main__":
    main()
