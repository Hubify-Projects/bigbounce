#!/usr/bin/env python3
"""
SIMBAD cross-match for top anomalies across all survey catalogs.

For each survey, takes the top 100 anomalies (by anomaly_score) and performs
a 3-arcsec cone search against SIMBAD via their TAP service. Reports known vs
novel fractions and object-type breakdowns.

Note: SIMBAD ADQL does NOT support UNION ALL. Each object is queried
individually; batches are used purely for rate-limiting (pause every
BATCH_SIZE queries).

Output: projects/cross_survey/results/simbad_crossmatch_summary.json
"""

import json
import time
import math
import requests
import pandas as pd
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2026/bigbounce")
RESULTS_DIR = BASE_DIR / "projects/cross_survey/results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

SIMBAD_TAP_URL = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"
RADIUS_ARCSEC = 3.0
RADIUS_DEG = RADIUS_ARCSEC / 3600.0
TOP_N = 100
BATCH_SIZE = 10          # pause after this many individual queries
BATCH_DELAY_SEC = 1.0    # polite delay between batches
REQUEST_TIMEOUT = 20     # seconds per HTTP request
RETRY_DELAY_SEC = 3.0    # delay before retrying a failed query
MAX_RETRIES = 2

# ---------------------------------------------------------------------------
# Survey catalogue definitions
# ---------------------------------------------------------------------------

def load_sdss():
    """SDSS DR18 — use the pre-merged coords file (77 905 objects)."""
    path = RESULTS_DIR / "sdss_anomalies_with_coords.parquet"
    df = pd.read_parquet(path)
    df = df.dropna(subset=["ra", "dec"])
    top = df.nlargest(TOP_N, "anomaly_score").reset_index(drop=True)
    top["obj_id"] = (
        "SDSS-"
        + top["plate"].astype(str)
        + "/"
        + top["mjd"].astype(str)
        + "/"
        + top["fiberid"].astype(str)
    )
    top["extra"] = top.apply(
        lambda r: {
            "class_sdss": r.get("class_sdss"),
            "z_sdss": float(r["z_sdss"]) if pd.notna(r.get("z_sdss")) else None,
        },
        axis=1,
    )
    return top[["obj_id", "ra", "dec", "anomaly_score", "extra"]]


def load_erosita():
    """eROSITA — full catalogue; take top 100 by anomaly score."""
    path = BASE_DIR / "pipelines/h200_results/erosita/erosita_anomalies.parquet"
    df = pd.read_parquet(path, columns=["iauname", "ra", "dec", "anomaly_score"])
    df = df.dropna(subset=["ra", "dec"])
    top = df.nlargest(TOP_N, "anomaly_score").reset_index(drop=True)
    top["obj_id"] = top["iauname"].fillna("eROSITA-unknown").astype(str)
    top["extra"] = [{}] * len(top)
    return top[["obj_id", "ra", "dec", "anomaly_score", "extra"]]


def load_neowise():
    """NEOWISE — 43 518 variable sources; take top 100 by score."""
    path = BASE_DIR / "pipelines/h200_results/neowise/neowise_anomalies.parquet"
    df = pd.read_parquet(path, columns=["source_id", "ra", "dec", "anomaly_score"])
    df = df.dropna(subset=["ra", "dec"])
    top = df.nlargest(TOP_N, "anomaly_score").reset_index(drop=True)
    top["obj_id"] = "NEOWISE-" + top["source_id"].astype(str)
    top["extra"] = [{}] * len(top)
    return top[["obj_id", "ra", "dec", "anomaly_score", "extra"]]


def load_gaia():
    """Gaia DR3 — 50 000 objects; take top 100 by score."""
    path = BASE_DIR / "pipelines/h200_results/gaia_dr3/gaia_anomalies.parquet"
    df = pd.read_parquet(path, columns=["source_id", "ra", "dec", "anomaly_score"])
    df = df.dropna(subset=["ra", "dec"])
    top = df.nlargest(TOP_N, "anomaly_score").reset_index(drop=True)
    top["obj_id"] = "Gaia-" + top["source_id"].astype(str)
    top["extra"] = [{}] * len(top)
    return top[["obj_id", "ra", "dec", "anomaly_score", "extra"]]


SURVEYS = {
    "SDSS_DR18": load_sdss,
    "eROSITA": load_erosita,
    "NEOWISE": load_neowise,
    "Gaia_DR3": load_gaia,
}

# LAMOST: still running (only checkpoint.json); skip with note.
SKIPPED_SURVEYS = {
    "LAMOST": "Pipeline still running — only checkpoint.json present (44 075 anomalies scored so far), no final anomaly parquet yet"
}

# ---------------------------------------------------------------------------
# SIMBAD TAP query helpers
# ---------------------------------------------------------------------------

def query_simbad_single(ra, dec):
    """
    Query SIMBAD TAP for a single (ra, dec) position at RADIUS_DEG.
    Returns list of dicts with keys: main_id, otype_txt, simbad_ra, simbad_dec.
    Returns empty list on failure (after retries).
    """
    adql = (
        f"SELECT main_id, otype_txt, ra, dec "
        f"FROM basic "
        f"WHERE CONTAINS("
        f"POINT('ICRS', ra, dec), "
        f"CIRCLE('ICRS', {ra:.6f}, {dec:.6f}, {RADIUS_DEG:.8f})"
        f") = 1"
    )
    params = {
        "REQUEST": "doQuery",
        "LANG": "ADQL",
        "FORMAT": "json",
        "QUERY": adql,
    }
    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.get(SIMBAD_TAP_URL, params=params, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            rows = data.get("data") or []
            meta = data.get("metadata", [])
            col_names = [m["name"] for m in meta] if meta else ["main_id", "otype_txt", "ra", "dec"]
            results = []
            for row in rows:
                rec = dict(zip(col_names, row))
                results.append({
                    "main_id": str(rec.get("main_id", "")),
                    "otype_txt": str(rec.get("otype_txt", "")),
                    "simbad_ra": float(rec["ra"]) if rec.get("ra") is not None else None,
                    "simbad_dec": float(rec["dec"]) if rec.get("dec") is not None else None,
                })
            return results
        except Exception as exc:
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY_SEC)
            else:
                print(f"    [WARN] SIMBAD query failed after {MAX_RETRIES+1} attempts: {exc}")
                return []
    return []


def angdist_arcsec(ra1, dec1, ra2, dec2):
    """Great-circle distance in arcsec (safe for < 1 deg separations)."""
    d2r = math.pi / 180.0
    cos_d = (
        math.sin(dec1 * d2r) * math.sin(dec2 * d2r)
        + math.cos(dec1 * d2r) * math.cos(dec2 * d2r) * math.cos((ra1 - ra2) * d2r)
    )
    cos_d = max(-1.0, min(1.0, cos_d))
    return math.degrees(math.acos(cos_d)) * 3600.0


# ---------------------------------------------------------------------------
# Per-survey crossmatch driver
# ---------------------------------------------------------------------------

def crossmatch_survey(name, df):
    """
    Cross-match top 100 rows of df against SIMBAD.
    Returns a result dict suitable for JSON serialisation.
    """
    print(f"\n{'='*60}")
    print(f"Survey: {name}  ({len(df)} objects to query)")
    print(f"{'='*60}")

    rows = df.to_dict("records")
    object_results = []

    for i, row in enumerate(rows):
        ra, dec = float(row["ra"]), float(row["dec"])
        matches = query_simbad_single(ra, dec)

        # Keep only the closest match within 3"
        best = None
        if matches:
            candidates = [
                m for m in matches
                if m["simbad_ra"] is not None and m["simbad_dec"] is not None
            ]
            if candidates:
                best = min(
                    candidates,
                    key=lambda h: angdist_arcsec(ra, dec, h["simbad_ra"], h["simbad_dec"]),
                )
            elif matches:
                best = matches[0]  # fallback: no coords returned

        entry = {
            "rank": i + 1,
            "obj_id": row["obj_id"],
            "ra": ra,
            "dec": dec,
            "anomaly_score": float(row["anomaly_score"]),
            "in_simbad": best is not None,
            "simbad_main_id": best["main_id"] if best else None,
            "simbad_otype": best["otype_txt"] if best else None,
            "simbad_sep_arcsec": (
                round(angdist_arcsec(ra, dec, best["simbad_ra"], best["simbad_dec"]), 2)
                if best and best["simbad_ra"] is not None else None
            ),
            "extra": row.get("extra", {}),
        }
        object_results.append(entry)

        # Progress and rate-limiting
        if (i + 1) % BATCH_SIZE == 0:
            matched_so_far = sum(1 for o in object_results if o["in_simbad"])
            print(f"  [{i+1:3d}/{len(rows)}] {matched_so_far} matched so far | "
                  f"last: {row['obj_id'][:35]} -> "
                  f"{'MATCHED: ' + best['main_id'][:25] if best else 'novel'}")
            time.sleep(BATCH_DELAY_SEC)

    # ---------- statistics ----------
    n_total = len(object_results)
    n_matched = sum(1 for o in object_results if o["in_simbad"])
    n_novel = n_total - n_matched

    otype_counts = {}
    for o in object_results:
        if o["in_simbad"] and o["simbad_otype"]:
            otype = o["simbad_otype"]
            otype_counts[otype] = otype_counts.get(otype, 0) + 1

    # Top novel objects (not in SIMBAD)
    novel_objects = [
        {
            "rank": o["rank"],
            "obj_id": o["obj_id"],
            "ra": o["ra"],
            "dec": o["dec"],
            "anomaly_score": o["anomaly_score"],
            "extra": o.get("extra", {}),
        }
        for o in object_results
        if not o["in_simbad"]
    ][:20]  # top 20 novel

    summary = {
        "survey": name,
        "n_queried": n_total,
        "n_matched_simbad": n_matched,
        "n_novel": n_novel,
        "match_fraction": round(n_matched / n_total, 4) if n_total else 0,
        "novel_fraction": round(n_novel / n_total, 4) if n_total else 0,
        "otype_breakdown": dict(sorted(otype_counts.items(), key=lambda x: -x[1])),
        "top_20_novel_objects": novel_objects,
        "all_results": object_results,
    }

    print(f"\n  Results: {n_matched}/{n_total} in SIMBAD "
          f"({summary['match_fraction']*100:.1f}%), "
          f"{n_novel} novel ({summary['novel_fraction']*100:.1f}%)")
    print(f"  Object types: {otype_counts}")

    return summary


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("SIMBAD cross-match: all survey anomaly catalogues")
    print(f"Top {TOP_N} objects per survey, {RADIUS_ARCSEC}\" cone radius")
    print(f"Individual queries, pause every {BATCH_SIZE} with {BATCH_DELAY_SEC}s delay\n")

    all_results = {}

    for survey_name, loader_fn in SURVEYS.items():
        try:
            df = loader_fn()
            print(f"Loaded {survey_name}: {len(df)} objects (after NaN-ra drop)")
        except Exception as exc:
            print(f"[ERROR] Could not load {survey_name}: {exc}")
            all_results[survey_name] = {"error": str(exc)}
            continue

        result = crossmatch_survey(survey_name, df)
        all_results[survey_name] = result

        # Save intermediate results after each survey
        _save_results(all_results)
        print(f"  Intermediate results saved.")

    # Add skipped surveys
    for survey_name, reason in SKIPPED_SURVEYS.items():
        all_results[survey_name] = {"skipped": True, "reason": reason}
        print(f"\nSkipped {survey_name}: {reason}")

    # ---------- cross-survey summary ----------
    print("\n" + "="*60)
    print("CROSS-SURVEY SUMMARY")
    print("="*60)

    completed = {k: v for k, v in all_results.items() if "n_queried" in v}
    total_queried = sum(v["n_queried"] for v in completed.values())
    total_matched = sum(v["n_matched_simbad"] for v in completed.values())
    total_novel = sum(v["n_novel"] for v in completed.values())

    for name, res in completed.items():
        print(f"  {name:15s}  {res['n_matched_simbad']:3d}/{res['n_queried']:3d} known "
              f"({res['match_fraction']*100:.0f}%)  "
              f"{res['n_novel']:3d} novel")

    if total_queried:
        print(f"\n  TOTAL: {total_matched}/{total_queried} known "
              f"({total_matched/total_queried*100:.1f}%)  "
              f"{total_novel} novel ({total_novel/total_queried*100:.1f}%)")

    # Aggregate otype breakdown
    global_otypes = {}
    for res in completed.values():
        for otype, cnt in res.get("otype_breakdown", {}).items():
            global_otypes[otype] = global_otypes.get(otype, 0) + cnt

    print(f"\n  Global object-type breakdown (SIMBAD matches):")
    for otype, cnt in sorted(global_otypes.items(), key=lambda x: -x[1])[:20]:
        print(f"    {otype:40s} {cnt:3d}")

    output = {
        "meta": {
            "description": "SIMBAD cross-match for top anomalies across survey catalogs",
            "top_n_per_survey": TOP_N,
            "radius_arcsec": RADIUS_ARCSEC,
            "surveys_completed": list(completed.keys()),
            "surveys_skipped": list(SKIPPED_SURVEYS.keys()),
            "date": "2026-04-02",
        },
        "global_summary": {
            "total_queried": total_queried,
            "total_matched_simbad": total_matched,
            "total_novel": total_novel,
            "overall_match_fraction": round(total_matched / total_queried, 4) if total_queried else 0,
            "overall_novel_fraction": round(total_novel / total_queried, 4) if total_queried else 0,
            "global_otype_breakdown": dict(
                sorted(global_otypes.items(), key=lambda x: -x[1])
            ),
        },
        "per_survey": all_results,
    }

    out_path = RESULTS_DIR / "simbad_crossmatch_summary.json"
    _write_json(output, out_path)
    print(f"\nFinal results saved to: {out_path}")
    return output


def _serialise(obj):
    """JSON serialiser that handles numpy scalars and non-finite floats."""
    if hasattr(obj, "item"):
        return obj.item()
    if isinstance(obj, float) and (math.isnan(obj) or math.isinf(obj)):
        return None
    raise TypeError(f"Not serialisable: {type(obj)}")


def _write_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=_serialise)


def _save_results(all_results):
    """Save intermediate results to disk."""
    out_path = RESULTS_DIR / "simbad_crossmatch_summary.json"
    # Build a partial output for intermediate saves
    completed = {k: v for k, v in all_results.items() if "n_queried" in v}
    total_queried = sum(v["n_queried"] for v in completed.values())
    total_matched = sum(v["n_matched_simbad"] for v in completed.values())
    total_novel = sum(v["n_novel"] for v in completed.values())
    global_otypes = {}
    for res in completed.values():
        for otype, cnt in res.get("otype_breakdown", {}).items():
            global_otypes[otype] = global_otypes.get(otype, 0) + cnt

    output = {
        "meta": {
            "description": "SIMBAD cross-match for top anomalies across survey catalogs (INTERMEDIATE)",
            "top_n_per_survey": TOP_N,
            "radius_arcsec": RADIUS_ARCSEC,
            "surveys_completed_so_far": list(completed.keys()),
            "date": "2026-04-02",
        },
        "global_summary": {
            "total_queried": total_queried,
            "total_matched_simbad": total_matched,
            "total_novel": total_novel,
            "overall_match_fraction": round(total_matched / total_queried, 4) if total_queried else 0,
            "overall_novel_fraction": round(total_novel / total_queried, 4) if total_queried else 0,
            "global_otype_breakdown": dict(sorted(global_otypes.items(), key=lambda x: -x[1])),
        },
        "per_survey": all_results,
    }
    _write_json(output, out_path)


if __name__ == "__main__":
    main()
