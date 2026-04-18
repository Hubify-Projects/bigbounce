#!/usr/bin/env python3
"""
P3-B-DESI-EXT — DESI DR1 top-1000 cross-match via CDS X-Match.

Purpose-built replacement for both the cone-by-cone VizieR script and
the VizieR-TAP upload approach. CDS X-Match (astroquery.xmatch.XMatch)
is optimized for "upload N-row sample, cross-match against large VizieR
catalog" — seconds per catalog even against Gaia DR3 (1.8B rows).

Usage: python3 desi_xmatch_crossmatch.py

Curated catalog list spans the major all-sky surveys covered by Paper 3:
Gaia DR3, SDSS DR16, Pan-STARRS1 DR2, AllWISE, CatWISE2020, 2MASS PSC,
unWISE, GALEX AIS, ROSAT 2RXS, NVSS, VLASS, USNO-B1, UCAC5, APASS9.
"""

import json
import time
import tempfile
from pathlib import Path
from collections import defaultdict

from astropy import units as u
from astropy.table import Table
from astroquery.xmatch import XMatch

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
RESULTS_DIR = BASE_DIR / "projects/cross_survey/results"
DESI_INPUT = (BASE_DIR / "pipelines/h200_results/pod_backup_20260408_full"
              / "dr1_all_anomalies.json")
OUTPUT_JSON = RESULTS_DIR / "desi_xmatch_summary.json"
FINDINGS_OUT = RESULTS_DIR / "P3-B-DESI-EXT_findings.md"

N_TOP = 1000
RADIUS_ARCSEC = 10.0

# Curated high-coverage catalogs (CDS VizieR names)
CATALOGS = [
    ("Gaia_DR3",          "vizier:I/355/gaiadr3"),
    ("SDSS_DR16",         "vizier:V/154/sdss16"),
    ("SDSS_DR12",         "vizier:V/147/sdss12"),
    ("DESI_LS_DR9_N",     "vizier:VII/292/north"),
    ("DESI_LS_DR9_S",     "vizier:VII/292/south"),
    ("DES_DR2",           "vizier:II/371/des_dr2"),
    ("Pan-STARRS1_DR2",   "vizier:II/349/ps1"),
    ("AllWISE",           "vizier:II/328/allwise"),
    ("CatWISE2020",       "vizier:II/365/catwise"),
    ("2MASS_PSC",         "vizier:II/246/out"),
    ("unWISE",            "vizier:II/363/unwise"),
    ("GALEX_AIS_DR5",     "vizier:II/312/ais"),
    ("GALEX_AIS_v2",      "vizier:II/335/galex_ais"),
    ("Chandra_CSC",       "vizier:B/chandra/chandra"),
    ("XMM_4XMM-DR13",     "vizier:IX/69/xmm4d13s"),
    ("NVSS",              "vizier:VIII/65/nvss"),
    ("VLASS_QL",          "vizier:J/ApJS/255/30/comp"),
    ("USNO-B1",           "vizier:I/284/out"),
    ("UCAC5",             "vizier:I/340/ucac5"),
    ("APASS9",            "vizier:II/336/apass9"),
]


def load_top_n(n):
    print(f"[desi] loading {DESI_INPUT.name}", flush=True)
    with DESI_INPUT.open() as f:
        data = json.load(f)
    print(f"[desi] {len(data)} anomalies loaded", flush=True)
    data.sort(key=lambda o: float(o["score"]), reverse=True)
    top = data[:n]
    print(f"[desi] top {n}: score max={top[0]['score']:.3f}  "
          f"min={top[-1]['score']:.3f}", flush=True)
    return top


def build_sample_csv(objs, path):
    tab = Table({
        "tid": [str(o["tid"]) for o in objs],
        "ra":  [float(o["ra"]) for o in objs],
        "dec": [float(o["dec"]) for o in objs],
    })
    tab.write(path, format="csv", overwrite=True)
    return tab


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[desi-xmatch] start  N={N_TOP}  radius={RADIUS_ARCSEC}\"  "
          f"{len(CATALOGS)} catalogs", flush=True)

    objs = load_top_n(N_TOP)
    tids_all = [str(o["tid"]) for o in objs]

    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        sample_path = f.name
    build_sample_csv(objs, sample_path)
    print(f"[desi-xmatch] uploaded sample CSV: {sample_path}", flush=True)

    per_catalog_matches = {}
    per_catalog_errors = []

    t_start = time.time()
    for (label, cat) in CATALOGS:
        t0 = time.time()
        try:
            result = XMatch.query(
                cat1=open(sample_path),
                cat2=cat,
                max_distance=RADIUS_ARCSEC * u.arcsec,
                colRA1="ra",
                colDec1="dec",
            )
        except Exception as e:
            dt = time.time() - t0
            print(f"[{label:18s}] ERROR after {dt:5.1f}s: "
                  f"{type(e).__name__}: {e}", flush=True)
            per_catalog_errors.append(label)
            continue
        dt = time.time() - t0
        n_rows = len(result)
        matched = set(str(t) for t in result["tid"])
        print(f"[{label:18s}] {n_rows:6d} rows  "
              f"{len(matched):4d} unique tids  ({dt:5.1f}s)", flush=True)
        per_catalog_matches[label] = matched

    t_total = time.time() - t_start
    print(f"[desi-xmatch] done  {t_total:.1f}s total  "
          f"{len(per_catalog_errors)} errors: {per_catalog_errors}",
          flush=True)

    # ---- Aggregate ----------------------------------------------------
    tid_to_cats = defaultdict(list)
    for label, tids in per_catalog_matches.items():
        for tid in tids:
            tid_to_cats[tid].append(label)

    n_matched_any = sum(1 for tid in tids_all if tid_to_cats[tid])
    n_unmatched = N_TOP - n_matched_any
    archival_id_rate = n_matched_any / N_TOP
    per_cat_counts = {label: len(tids)
                      for label, tids in per_catalog_matches.items()}

    summary = {
        "sample": {
            "survey": "DESI_DR1",
            "n_top": N_TOP,
            "ordering": "score desc",
            "score_max": float(objs[0]["score"]),
            "score_min": float(objs[-1]["score"]),
            "caveat": ("Top-1000 by DESI anomaly score, not explicitly "
                       "filtered to SIMBAD-novel. DESI is ~99 % "
                       "SIMBAD-novel at top 10K, so overlap is ~99 %."),
        },
        "config": {
            "method": "CDS X-Match (astroquery.xmatch)",
            "radius_arcsec": RADIUS_ARCSEC,
            "catalogs": [c[0] for c in CATALOGS],
            "catalog_errors": per_catalog_errors,
        },
        "counts": {
            "n_sample": N_TOP,
            "n_matched_any_catalog": n_matched_any,
            "n_unmatched": n_unmatched,
            "archival_id_rate": archival_id_rate,
        },
        "per_catalog_match_counts": per_cat_counts,
        "per_object": [
            {
                "tid": tid,
                "ra": float(o["ra"]),
                "dec": float(o["dec"]),
                "score": float(o["score"]),
                "matched_catalogs": sorted(tid_to_cats[tid]),
                "n_catalogs": len(tid_to_cats[tid]),
            }
            for tid, o in zip(tids_all, objs)
        ],
        "wall_time_sec": t_total,
    }
    with OUTPUT_JSON.open("w") as f:
        json.dump(summary, f, indent=2)
    print(f"[desi-xmatch] wrote {OUTPUT_JSON}", flush=True)

    # ---- Write findings MD -------------------------------------------
    md = []
    md.append("# P3-B-DESI-EXT findings — DESI DR1 top-1000 "
              "CDS-XMatch sweep")
    md.append(f"**Date:** {time.strftime('%Y-%m-%d')}")
    md.append("**Method:** CDS X-Match (astroquery.xmatch.XMatch), "
              f"{len(CATALOGS)} curated catalogs, "
              f"{RADIUS_ARCSEC}\" radius.")
    md.append("**Closes:** P3-B-DESI-EXT.")
    md.append("")
    md.append("## Sample")
    md.append(f"- Top {N_TOP} DESI DR1 anomalies by score desc")
    md.append(f"- Score range: [{objs[-1]['score']:.3f}, "
              f"{objs[0]['score']:.3f}]")
    md.append("- Ordering caveat: top-by-score, not top-SIMBAD-novel "
              "(DESI is ~99 % SIMBAD-novel at top 10K)")
    md.append("")
    md.append("## Headline")
    md.append(f"- **Archival-ID rate: {archival_id_rate*100:.1f} %** "
              f"({n_matched_any}/{N_TOP})")
    md.append(f"- Unmatched (not in any of {len(CATALOGS)} curated "
              f"catalogs): {n_unmatched}")
    md.append(f"- Wall time: {t_total:.1f} s ({t_total/60:.1f} min)")
    md.append("")
    md.append("## Per-catalog match counts")
    md.append("| Catalog | Matched tids |")
    md.append("|---|---:|")
    for label in [c[0] for c in CATALOGS]:
        n = per_cat_counts.get(label, "ERR")
        md.append(f"| {label} | {n} |")
    if per_catalog_errors:
        md.append("")
        md.append(f"**Catalog errors:** {per_catalog_errors}")
    md.append("")
    md.append("## Comparison to v2 SDSS")
    md.append("- v2 SDSS DR18 top-20 SIMBAD-novel → 100 % (20/20) "
              "via VizieR all-catalogs web API")
    md.append(f"- This run DESI DR1 top-{N_TOP} → "
              f"{archival_id_rate*100:.1f} % via {len(CATALOGS)}-catalog "
              "curated X-Match")
    md.append("- Methodological note: curated list is a subset of "
              "VizieR's ~25 k tables. A curated match is sufficient "
              "proof the anomaly is NOT uncataloged; a curated "
              "non-match is NOT proof of true novelty (could still be "
              "in a long-tail catalog).")
    md.append("")
    md.append("## Paper 3 §5.1 implication")
    md.append("- The §5.1 honesty footnote (committed `0364a5d`) "
              "already reframes SIMBAD-novel as an upper bound on true "
              "novelty. This DESI-scale result operationalizes it on "
              "Paper 3's largest survey.")
    md.append(f"- Recommend the footnote cite the DESI rate "
              f"({archival_id_rate*100:.0f} % on top-{N_TOP}) alongside "
              "the SDSS rate (100 %).")
    md.append("")
    md.append("## Files")
    md.append(f"- `{OUTPUT_JSON.relative_to(BASE_DIR)}` — per-object JSON")
    md.append(f"- `{FINDINGS_OUT.relative_to(BASE_DIR)}` — this file")
    md.append("- `projects/cross_survey/desi_xmatch_crossmatch.py` "
              "— script")

    FINDINGS_OUT.write_text("\n".join(md) + "\n")
    print(f"[desi-xmatch] wrote {FINDINGS_OUT}", flush=True)

    print("")
    print(f"=== HEADLINE: archival-ID rate = "
          f"{archival_id_rate*100:.1f} % ({n_matched_any}/{N_TOP}) ===")
    print(f"=== wall time: {t_total:.1f} s ===")


if __name__ == "__main__":
    main()
