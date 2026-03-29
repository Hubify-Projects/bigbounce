#!/usr/bin/env python3
"""
Complete cross-match: finish NED queries for objects 41-83,
then do all SIMBAD queries via Harvard mirror.
Merges everything into crossmatch_results.json.
"""

import json
import time
import urllib.request
import urllib.parse
import urllib.error
import ssl
import os
import sys
import xml.etree.ElementTree as ET

DIR = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(DIR, "gold_anomalies.json")
EXISTING = os.path.join(DIR, "crossmatch_results.json")
OUTPUT = os.path.join(DIR, "crossmatch_results.json")

SEARCH_RADIUS_ARCSEC = 5
RATE_LIMIT_SEC = 1.0

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE


# ──────────────────────────── NED ────────────────────────────

def query_ned(ra_deg, dec_deg, radius_arcsec=5.0):
    """Query NED for objects near (ra, dec)."""
    url = (
        f"https://ned.ipac.caltech.edu/cgi-bin/nph-objsearch?"
        f"search_type=Near+Position+Search"
        f"&in_csys=Equatorial&in_equinox=J2000.0"
        f"&lon={ra_deg:.6f}d&lat={dec_deg:.6f}d"
        f"&radius={radius_arcsec:.1f}"
        f"&hconst=67.8&omegam=0.308&omegav=0.692&wmap=4&corr_z=1"
        f"&z_constraint=Unconstrained"
        f"&ot_include=ANY&nmp_op=ANY"
        f"&out_csys=Equatorial&out_equinox=J2000.0"
        f"&obj_sort=Distance+to+search+center"
        f"&of=xml_main&zv_breaker=30000.0&list_limit=5&img_stamp=NO"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BigBounce-Crossmatch/1.0"})
        with urllib.request.urlopen(req, timeout=30, context=ssl_ctx) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            if "No object" in raw or "<TABLEDATA />" in raw or "<TABLEDATA/>" in raw:
                return {"found": False, "objects": [], "n_matches": 0, "error": None}
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
            return {"found": False, "objects": [], "n_matches": 0, "error": None}
    except Exception as e:
        return {"found": False, "objects": [], "n_matches": 0, "error": str(e)}


def parse_ned_xml(xml_text):
    """Parse NED VOTable XML."""
    objects = []
    try:
        root = ET.fromstring(xml_text)
        ns = ""
        if root.tag.startswith("{"):
            ns = root.tag.split("}")[0] + "}"
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
                    if len(tds) > 6 and tds[6].strip():
                        try:
                            obj["redshift"] = float(tds[6].strip())
                        except ValueError:
                            obj["redshift"] = None
                    else:
                        obj["redshift"] = None
                    objects.append(obj)
    except ET.ParseError:
        pass
    return objects


# ──────────────────────────── SIMBAD (Harvard) ────────────────────────────

def query_simbad_harvard(ra_deg, dec_deg, radius_arcsec=5, max_retries=2):
    """Query SIMBAD via Harvard mirror."""
    url = (
        f"https://simbad.harvard.edu/simbad/sim-coo?"
        f"Coord={ra_deg}+{dec_deg}"
        f"&CooFrame=FK5&CooEpoch=2000&CooEqui=2000"
        f"&Radius={radius_arcsec}&Radius.unit=arcsec"
        f"&output.format=votable&output.max=5"
    )
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "BigBounce-Crossmatch/1.0"})
            with urllib.request.urlopen(req, timeout=20, context=ssl_ctx) as resp:
                raw = resp.read().decode("utf-8")
                return parse_simbad_votable(raw)
        except Exception as e:
            if attempt < max_retries:
                time.sleep(2)
                continue
            return {"found": False, "main_id": None, "otype": None, "error": str(e)}


def parse_simbad_votable(xml_text):
    """Parse SIMBAD VOTable XML response."""
    try:
        if 'name="Error"' in xml_text or "No astronomical object found" in xml_text:
            return {"found": False, "main_id": None, "otype": None, "error": None}

        root = ET.fromstring(xml_text)
        ns = root.tag.split("}")[0] + "}" if root.tag.startswith("{") else ""

        fields = []
        for field in root.iter(f"{ns}FIELD"):
            fields.append(field.get("ID", field.get("name", "")))

        idx = {}
        for i, f in enumerate(fields):
            if f in ("MAIN_ID", "OTYPE_S", "RA_d", "DEC_d", "ANG_DIST"):
                idx[f] = i

        all_matches = []
        for tabledata in root.iter(f"{ns}TABLEDATA"):
            for tr in tabledata.iter(f"{ns}TR"):
                tds = [td.text.strip() if td.text else "" for td in tr.iter(f"{ns}TD")]
                match = {}
                if "MAIN_ID" in idx and idx["MAIN_ID"] < len(tds):
                    match["main_id"] = tds[idx["MAIN_ID"]]
                if "OTYPE_S" in idx and idx["OTYPE_S"] < len(tds):
                    match["otype"] = tds[idx["OTYPE_S"]]
                if "RA_d" in idx and idx["RA_d"] < len(tds):
                    try:
                        match["simbad_ra"] = float(tds[idx["RA_d"]])
                    except (ValueError, TypeError):
                        pass
                if "DEC_d" in idx and idx["DEC_d"] < len(tds):
                    try:
                        match["simbad_dec"] = float(tds[idx["DEC_d"]])
                    except (ValueError, TypeError):
                        pass
                if "ANG_DIST" in idx and idx["ANG_DIST"] < len(tds):
                    try:
                        match["ang_dist_arcsec"] = float(tds[idx["ANG_DIST"]])
                    except (ValueError, TypeError):
                        pass
                if match.get("main_id"):
                    all_matches.append(match)

        if all_matches:
            best = all_matches[0]
            return {
                "found": True,
                "main_id": best.get("main_id"),
                "otype": best.get("otype"),
                "simbad_ra": best.get("simbad_ra"),
                "simbad_dec": best.get("simbad_dec"),
                "ang_dist_arcsec": best.get("ang_dist_arcsec"),
                "n_matches": len(all_matches),
                "all_matches": all_matches if len(all_matches) > 1 else None,
                "error": None,
            }
        return {"found": False, "main_id": None, "otype": None, "error": None}
    except ET.ParseError as e:
        return {"found": False, "main_id": None, "otype": None, "error": f"XML parse: {e}"}


# ──────────────────────────── MAIN ────────────────────────────

def main():
    with open(INPUT) as f:
        anomalies = json.load(f)

    # Load existing partial results (first 40 have NED data)
    existing = {}
    if os.path.exists(EXISTING):
        with open(EXISTING) as f:
            data = json.load(f)
            if "results" in data:
                for r in data["results"]:
                    existing[r["targetid"]] = r
        print(f"Loaded {len(existing)} existing results (NED data for first batch)")

    print(f"\n{'='*70}")
    print(f"PHASE 1: Finish NED queries for remaining objects")
    print(f"{'='*70}")

    ned_total_found = 0
    ned_errors = 0

    # Process NED for objects that don't have NED results yet
    for i, obj in enumerate(anomalies):
        tid = obj["targetid"]
        ra, dec = obj["ra"], obj["dec"]

        if tid in existing and existing[tid].get("ned", {}).get("found") is not None and existing[tid]["ned"].get("error") is None:
            # Already have valid NED result
            if existing[tid]["ned"]["found"]:
                ned_total_found += 1
            continue

        print(f"  NED [{i+1}/{len(anomalies)}] tid={tid} RA={ra:.4f} Dec={dec:.4f}", end="", flush=True)
        ned = query_ned(ra, dec, SEARCH_RADIUS_ARCSEC)

        if ned["error"]:
            print(f"  ERROR: {ned['error'][:40]}")
            ned_errors += 1
        elif ned["found"]:
            ned_total_found += 1
            print(f"  FOUND: {ned.get('primary_name','?')} [{ned.get('primary_type','?')}]")
        else:
            print(f"  --")

        # Store/update
        if tid not in existing:
            existing[tid] = {
                "targetid": tid, "ra": ra, "dec": dec,
                "z": obj["z"], "spectype": obj["spectype"],
                "anomaly_score": obj["anomaly_score"],
            }
        existing[tid]["ned"] = {
            "found": ned["found"],
            "primary_name": ned.get("primary_name"),
            "primary_type": ned.get("primary_type"),
            "primary_redshift": ned.get("primary_redshift"),
            "n_matches": ned.get("n_matches", 0),
            "objects": ned.get("objects", []) if ned["found"] else [],
            "error": ned.get("error"),
        }
        existing[tid]["in_ned"] = ned["found"]

        time.sleep(RATE_LIMIT_SEC)

    # Count NED found from existing
    for tid, r in existing.items():
        if r.get("ned", {}).get("found") and tid not in [obj["targetid"] for obj in anomalies[len(existing):]]:
            pass  # already counted

    ned_total_found = sum(1 for r in existing.values() if r.get("ned", {}).get("found", False))
    print(f"\nNED phase complete: {ned_total_found}/{len(anomalies)} found")

    print(f"\n{'='*70}")
    print(f"PHASE 2: SIMBAD queries via Harvard mirror (all 83 objects)")
    print(f"{'='*70}")

    simbad_found = 0
    simbad_errors = 0

    for i, obj in enumerate(anomalies):
        tid = obj["targetid"]
        ra, dec = obj["ra"], obj["dec"]

        print(f"  SIMBAD [{i+1}/{len(anomalies)}] tid={tid} RA={ra:.4f} Dec={dec:.4f} z={obj['z']:.3f} {obj['spectype']}", end="", flush=True)

        simbad = query_simbad_harvard(ra, dec, SEARCH_RADIUS_ARCSEC)

        if simbad["error"]:
            print(f"  ERROR: {simbad['error'][:40]}")
            simbad_errors += 1
        elif simbad["found"]:
            simbad_found += 1
            print(f"  FOUND: {simbad['main_id']} [{simbad['otype']}]")
        else:
            print(f"  --")

        if tid not in existing:
            existing[tid] = {
                "targetid": tid, "ra": ra, "dec": dec,
                "z": obj["z"], "spectype": obj["spectype"],
                "anomaly_score": obj["anomaly_score"],
                "ned": {"found": False, "objects": [], "n_matches": 0, "error": "not queried"},
                "in_ned": False,
            }
        existing[tid]["simbad"] = {
            "found": simbad["found"],
            "main_id": simbad.get("main_id"),
            "object_type": simbad.get("otype"),
            "simbad_ra": simbad.get("simbad_ra"),
            "simbad_dec": simbad.get("simbad_dec"),
            "ang_dist_arcsec": simbad.get("ang_dist_arcsec"),
            "n_matches": simbad.get("n_matches", 0),
            "all_matches": simbad.get("all_matches"),
            "error": simbad.get("error"),
        }
        existing[tid]["in_simbad"] = simbad["found"]
        existing[tid]["in_any_database"] = simbad["found"] or existing[tid].get("in_ned", False)
        existing[tid]["uncataloged"] = not existing[tid]["in_any_database"]

        time.sleep(RATE_LIMIT_SEC)

        # Save every 20
        if (i + 1) % 20 == 0:
            save_output(anomalies, existing)
            print(f"  [checkpoint saved at {i+1}/83]")

    # Final save
    save_output(anomalies, existing)

    # Summary
    results_list = [existing[obj["targetid"]] for obj in anomalies if obj["targetid"] in existing]
    simbad_found = sum(1 for r in results_list if r.get("in_simbad", False))
    ned_found = sum(1 for r in results_list if r.get("in_ned", False))
    both = sum(1 for r in results_list if r.get("in_simbad", False) and r.get("in_ned", False))
    either = sum(1 for r in results_list if r.get("in_any_database", False))
    neither = sum(1 for r in results_list if r.get("uncataloged", False))

    print(f"\n{'='*70}")
    print("CROSS-MATCH SUMMARY")
    print(f"{'='*70}")
    print(f"Total anomalies:          {len(anomalies)}")
    print(f"Found in SIMBAD:          {simbad_found}/{len(anomalies)} ({100*simbad_found/len(anomalies):.1f}%)")
    print(f"Found in NED:             {ned_found}/{len(anomalies)} ({100*ned_found/len(anomalies):.1f}%)")
    print(f"Found in BOTH:            {both}/{len(anomalies)} ({100*both/len(anomalies):.1f}%)")
    print(f"Found in EITHER:          {either}/{len(anomalies)} ({100*either/len(anomalies):.1f}%)")
    print(f"UNCATALOGED (novel):      {neither}/{len(anomalies)} ({100*neither/len(anomalies):.1f}%)")
    print(f"SIMBAD errors:            {simbad_errors}")
    print(f"NED errors:               {ned_errors}")

    # Print uncataloged objects
    uncataloged = [r for r in results_list if r.get("uncataloged", False)]
    if uncataloged:
        print(f"\nUNCATALOGED OBJECTS ({len(uncataloged)}):")
        for r in uncataloged:
            print(f"  tid={r['targetid']}  RA={r['ra']:.4f}  Dec={r['dec']:.4f}  z={r['z']:.3f}  {r['spectype']}  score={r['anomaly_score']:.3f}")

    print(f"\nResults saved to: {OUTPUT}")


def save_output(anomalies, existing):
    """Save merged results."""
    results_list = [existing[obj["targetid"]] for obj in anomalies if obj["targetid"] in existing]
    simbad_found = sum(1 for r in results_list if r.get("in_simbad", False))
    ned_found = sum(1 for r in results_list if r.get("in_ned", False))
    both = sum(1 for r in results_list if r.get("in_simbad", False) and r.get("in_ned", False))
    either = sum(1 for r in results_list if r.get("in_any_database", False))
    neither = sum(1 for r in results_list if r.get("uncataloged", False))
    simbad_errors = sum(1 for r in results_list if r.get("simbad", {}).get("error"))
    ned_errors = sum(1 for r in results_list if r.get("ned", {}).get("error"))

    output = {
        "metadata": {
            "description": "Cross-match of 83 gold anomalies against SIMBAD and NED",
            "search_radius_arcsec": SEARCH_RADIUS_ARCSEC,
            "simbad_mirror": "simbad.harvard.edu",
            "ned_api": "ned.ipac.caltech.edu",
            "processed": len(results_list),
            "total": len(anomalies),
            "complete": len(results_list) == len(anomalies),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "summary": {
            "total_anomalies": len(anomalies),
            "in_simbad": simbad_found,
            "in_ned": ned_found,
            "in_both": both,
            "in_either": either,
            "uncataloged": neither,
            "simbad_errors": simbad_errors,
            "ned_errors": ned_errors,
            "pct_simbad": round(100 * simbad_found / max(len(results_list), 1), 1),
            "pct_ned": round(100 * ned_found / max(len(results_list), 1), 1),
            "pct_uncataloged": round(100 * neither / max(len(results_list), 1), 1),
        },
        "results": results_list,
    }

    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2)


if __name__ == "__main__":
    main()
