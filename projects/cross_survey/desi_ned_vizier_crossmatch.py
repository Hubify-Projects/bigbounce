#!/usr/bin/env python3
"""
P3-B-DESI-EXT — DESI DR1 top-1000 NED + VizieR cross-match sweep.

Follow-up to `ned_vizier_crossmatch_v2.py` (P3-B v2). That script found
100 % archival-ID rate in NED+VizieR on the SDSS-DR18 top-20 SIMBAD-novel
sample, calling the "SIMBAD-novel ≈ truly uncataloged" framing of Paper 3
§5.1 into question. This script answers the parallel question for DESI
DR1 — the survey Paper 3 leans on hardest (61 % of paper aggregate,
195,829 anomalies, 99 % SIMBAD-novel).

Sample: top-1000 DESI DR1 anomalies by `score` descending, drawn from
`pipelines/h200_results/pod_backup_20260408_full/dr1_all_anomalies.json`.

Stages:
1. NED 5-arcsec cone on each object (polite delay + retries + circuit
   breaker if NED is degraded).
2. VizieR all-catalogs 10-arcsec cone on every object (regardless of NED
   outcome). Total-budget cap so we terminate even if VizieR slows.

Stage 3 (Gaia-XP) is SKIPPED for this task — per the brief, we only need
it if residual-novel objects survive both stages, which is unlikely on
DESI if the v2 SDSS pattern holds.

Outputs:
- results/desi_ned_vizier_summary.json — per-object table + global counts
- results/P3-B-DESI-EXT_findings.md — findings + comparison to v2 SDSS
"""

import json
import sys
import time
from pathlib import Path
from collections import Counter

# Reuse query helpers from v2 (canonical NED + VizieR implementation)
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
import ned_vizier_crossmatch_v2 as v2  # noqa: E402  (sys.path hack above)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
RESULTS_DIR = BASE_DIR / "projects/cross_survey/results"
DESI_INPUT = (BASE_DIR / "pipelines/h200_results/pod_backup_20260408_full"
              / "dr1_all_anomalies.json")
OUTPUT_JSON = RESULTS_DIR / "desi_ned_vizier_summary.json"
FINDINGS_OUT = RESULTS_DIR / "P3-B-DESI-EXT_findings.md"

N_TOP = 1000

# NED: same params as v2 (slow + polite, circuit breaker if down)
NED_RADIUS_ARCSEC = v2.NED_RADIUS_ARCSEC          # 5.0"
NED_DELAY_SEC = max(v2.NED_DELAY_SEC, 5.0)        # >=5s per brief
NED_HEALTH_CHECK_N = v2.NED_HEALTH_CHECK_N        # 3 consecutive fails

# VizieR: same as v2 — 10" cone, 30s per-query, 4h total budget for top-1000
VIZIER_RADIUS_ARCSEC = v2.VIZIER_RADIUS_ARCSEC    # 10.0"
VIZIER_DELAY_SEC = v2.VIZIER_DELAY_SEC            # 2s between queries
VIZIER_TOTAL_BUDGET_SEC = 4 * 60 * 60             # 4h cap for 1000-row DESI run

service_status = {"NED": "unknown", "VizieR": "unknown"}


# ---------------------------------------------------------------------------
# Sample selection
# ---------------------------------------------------------------------------

def load_top_n(n):
    """Load DESI anomalies JSON, sort by score desc, return top n."""
    print(f"[desi] loading {DESI_INPUT.name}", flush=True)
    with DESI_INPUT.open() as f:
        data = json.load(f)
    print(f"[desi] {len(data)} DESI anomalies loaded", flush=True)
    data.sort(key=lambda o: float(o["score"]), reverse=True)
    top = data[:n]
    print(f"[desi] top {n} by score: max={top[0]['score']:.3f}  "
          f"min={top[-1]['score']:.3f}", flush=True)
    return top


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------

def write_snapshot(payload):
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))


def main():
    t0 = time.time()
    top = load_top_n(N_TOP)

    objs = []
    for o in top:
        objs.append({
            "survey": "DESI_DR1",
            "obj_id": str(o["tid"]),
            "ra": float(o["ra"]),
            "dec": float(o["dec"]),
            "anomaly_score": float(o["score"]),
            "worst_band": o.get("worst"),
            "rB": o.get("rB"),
            "rR": o.get("rR"),
            "rZ": o.get("rZ"),
        })

    # --- Stage 1: NED ---
    print("\n=== Stage 1: NED 5-arcsec cone on DESI top-1000 ===", flush=True)
    ned_ok = 0
    ned_fail = 0
    ned_novel = 0
    ned_skipped_degraded = 0
    ned_degraded = False
    health_fails = 0

    for i, o in enumerate(objs):
        if ned_degraded:
            ned_skipped_degraded += 1
            o["ned"] = {
                "matched": False, "n_matches": 0,
                "error": "skipped_service_degraded",
            }
            continue

        print(f"  [{i+1:>3}/{len(objs)}] tid={o['obj_id']:<12s} "
              f"ra={o['ra']:8.4f} dec={o['dec']:+8.4f}", flush=True, end=" -> ")
        res = v2.query_ned(o["ra"], o["dec"])
        o["ned"] = res
        if res.get("matched"):
            ned_ok += 1
            health_fails = 0
            tm = res.get("top_match") or {}
            tag = f"matched ({tm.get('name')})"
        elif "error" in res:
            ned_fail += 1
            health_fails += 1
            tag = f"error ({str(res.get('error'))[:50]})"
        else:
            ned_novel += 1
            health_fails = 0
            tag = "novel"
        print(tag, flush=True)

        # Polite delay
        time.sleep(NED_DELAY_SEC)

        # Circuit breaker: if the first few queries all error and 0 have
        # matched, bail on NED.
        if (health_fails >= NED_HEALTH_CHECK_N and ned_ok == 0):
            ned_degraded = True
            print(f"  [!!] NED circuit-breaker tripped after "
                  f"{health_fails} consecutive failures; skipping "
                  f"remaining NED queries", flush=True)

    if ned_degraded or (ned_fail > 0 and ned_ok == 0):
        service_status["NED"] = "degraded"
    elif ned_ok + ned_novel > 0:
        service_status["NED"] = "ok"
    else:
        service_status["NED"] = "skipped"

    for o in objs:
        n = o.get("ned", {})
        if n.get("matched"):
            o["ned_cls"] = "ned_matched"
        elif "error" in n:
            o["ned_cls"] = "error"
        else:
            o["ned_cls"] = "ned_novel"

    # Snapshot after stage 1
    write_snapshot({
        "meta": {"stage": "1_ned_done", "elapsed_sec": time.time() - t0},
        "objects": objs,
    })

    # --- Stage 2: VizieR on ALL objects (broader net than NED) ---
    print("\n=== Stage 2: VizieR 10-arcsec all-catalogs cone on all 100 ===",
          flush=True)
    viz_ok = 0
    viz_fail = 0
    viz_novel = 0
    viz_budget_skipped = 0
    vz_start = time.time()

    catalog_hits = Counter()  # catalogs that produce matches

    for i, o in enumerate(objs):
        if time.time() - vz_start > VIZIER_TOTAL_BUDGET_SEC:
            viz_budget_skipped += 1
            o["vizier"] = {"matched": False, "skipped": "budget_exhausted"}
            continue
        print(f"  [{i+1:>3}/{len(objs)}] tid={o['obj_id']:<12s} "
              f"ra={o['ra']:8.4f} dec={o['dec']:+8.4f}", flush=True, end=" -> ")
        res = v2.query_vizier(o["ra"], o["dec"])
        o["vizier"] = res
        if res.get("matched"):
            viz_ok += 1
            for c in res.get("catalogs", []):
                catalog_hits[c.get("catalog", "?")] += 1
            tag = f"matched ({res.get('n_catalogs', 0)} cats)"
        elif "error" in res:
            viz_fail += 1
            tag = f"error ({str(res.get('error'))[:50]})"
        else:
            viz_novel += 1
            tag = "novel"
        print(tag, flush=True)
        time.sleep(VIZIER_DELAY_SEC)

    for o in objs:
        vz = o.get("vizier", {}) or {}
        if vz.get("skipped"):
            viz_budget_skipped_tag = True  # noqa  (readability)
        # Final classification
        if o["ned_cls"] == "ned_matched":
            o["final_cls"] = "ned_matched"
        elif vz.get("matched"):
            o["final_cls"] = "vizier_matched"
        elif vz.get("skipped"):
            o["final_cls"] = "vizier_skipped_budget"
        elif "error" in vz:
            o["final_cls"] = "vizier_error_unresolved"
        elif o["ned_cls"] == "error":
            o["final_cls"] = "ned_error_unresolved"
        else:
            o["final_cls"] = "residual_novel"

    if viz_ok + viz_fail + viz_novel == 0:
        service_status["VizieR"] = "skipped"
    elif viz_fail > 0 and viz_ok == 0:
        service_status["VizieR"] = "degraded"
    else:
        service_status["VizieR"] = "ok"

    # --- Roll-up ---
    counts = Counter(o["final_cls"] for o in objs)
    resolved_keys = {"ned_matched", "vizier_matched", "residual_novel"}
    unresolved_keys = {"ned_error_unresolved", "vizier_error_unresolved",
                       "vizier_skipped_budget"}

    n_resolved = sum(counts.get(k, 0) for k in resolved_keys)
    n_matched = counts.get("ned_matched", 0) + counts.get("vizier_matched", 0)
    archival_id_rate = (n_matched / n_resolved) if n_resolved else None

    # --- Summary payload ---
    output = {
        "meta": {
            "task": "P3-B-DESI-EXT",
            "description": (
                "DESI DR1 top-1000 NED + VizieR cross-match sweep. "
                "Parallel to SDSS v2 sweep (ned_vizier_crossmatch_v2.py). "
                "Tests whether DESI's 99% SIMBAD-novel rate is supported by "
                "broader archival cross-checks."
            ),
            "input": str(DESI_INPUT.relative_to(BASE_DIR)),
            "n_sample": len(objs),
            "score_max": objs[0]["anomaly_score"],
            "score_min": objs[-1]["anomaly_score"],
            "ned_radius_arcsec": NED_RADIUS_ARCSEC,
            "vizier_radius_arcsec": VIZIER_RADIUS_ARCSEC,
            "ned_delay_sec": NED_DELAY_SEC,
            "vizier_total_budget_sec": VIZIER_TOTAL_BUDGET_SEC,
            "stage1_ned_ok": ned_ok,
            "stage1_ned_fail": ned_fail,
            "stage1_ned_novel": ned_novel,
            "stage1_ned_skipped_degraded": ned_skipped_degraded,
            "stage2_vizier_ok": viz_ok,
            "stage2_vizier_fail": viz_fail,
            "stage2_vizier_novel": viz_novel,
            "stage2_vizier_budget_skipped": viz_budget_skipped,
            "service_status": service_status,
            "archival_id_rate_resolved": archival_id_rate,
            "n_resolved": n_resolved,
            "n_matched": n_matched,
            "top_vizier_catalogs": catalog_hits.most_common(20),
            "elapsed_sec": time.time() - t0,
            "status": "complete",
        },
        "global_counts": dict(counts),
        "objects": objs,
    }
    write_snapshot(output)

    # --- Findings markdown ---
    lines = []
    lines.append("# P3-B-DESI-EXT — DESI DR1 top-1000 NED + VizieR findings\n")
    lines.append("**Date:** 2026-04-18 (drive-to-100 follow-up to v2 SDSS sweep)\n")
    lines.append("**Closes:** `P3-B-DESI-EXT`. "
                 "**Parallels:** `P3-B` v2 (`P3-B_findings_v2.md`).\n\n")

    lines.append("## Service status\n\n")
    for svc, st in service_status.items():
        lines.append(f"- **{svc}**: `{st}`\n")

    lines.append(f"\n## Sample\n\n")
    lines.append(f"- Source: `{DESI_INPUT.relative_to(BASE_DIR)}` "
                 f"(195,829 DESI DR1 anomalies)\n")
    lines.append(f"- Selection: top {N_TOP} by anomaly score (descending)\n")
    lines.append(f"- Score range: {objs[-1]['anomaly_score']:.3f} – "
                 f"{objs[0]['anomaly_score']:.3f}\n\n")

    lines.append(f"## Global counts ({len(objs)} objects)\n\n")
    lines.append("| Classification | Count |\n|---|---:|\n")
    for k in ("ned_matched", "vizier_matched", "residual_novel",
              "ned_error_unresolved", "vizier_error_unresolved",
              "vizier_skipped_budget"):
        lines.append(f"| `{k}` | {counts.get(k, 0)} |\n")

    lines.append("\n## Stage summary\n\n")
    lines.append(f"- Stage 1 NED: {ned_ok} matched / {ned_novel} novel / "
                 f"{ned_fail} errored / {ned_skipped_degraded} skipped "
                 f"(of {len(objs)})\n")
    lines.append(f"- Stage 2 VizieR: {viz_ok} matched / {viz_novel} novel / "
                 f"{viz_fail} errored / {viz_budget_skipped} budget-skipped "
                 f"(of {len(objs)})\n\n")

    lines.append("## Archival-ID rate\n\n")
    if archival_id_rate is not None:
        lines.append(f"- **DESI top-1000 archival-ID rate (resolved only):** "
                     f"**{100 * archival_id_rate:.1f} %** "
                     f"({n_matched} / {n_resolved}).\n")
    else:
        lines.append("- **DESI top-1000 archival-ID rate:** no resolved "
                     "objects — services degraded.\n")

    lines.append("\n## Comparison to SDSS v2 sweep\n\n")
    lines.append("| Sweep | Sample | Archival-ID rate |\n|---|---|---:|\n")
    lines.append("| SDSS-DR18 v2 (P3-B v2) | 20 / 20 resolved | **100.0 %** |\n")
    if archival_id_rate is not None:
        lines.append(f"| DESI-DR1 (this task)   | {n_matched} / "
                     f"{n_resolved} resolved | "
                     f"**{100 * archival_id_rate:.1f} %** |\n\n")
    else:
        lines.append("| DESI-DR1 (this task)   | services degraded | n/a |\n\n")

    lines.append("## Top VizieR catalogs driving DESI hits\n\n")
    if catalog_hits:
        lines.append("Catalogs responsible for the archival identifications "
                     "(top 20 by hit count):\n\n")
        lines.append("| Catalog | Hits |\n|---|---:|\n")
        for name, cnt in catalog_hits.most_common(20):
            safe = str(name).replace("|", "\\|")
            lines.append(f"| `{safe}` | {cnt} |\n")
        lines.append("\nThe catalog mix matters: a hit in a photometric "
                     "source table (e.g. Gaia DR3 source list, LS-DR10 "
                     "tractor, SDSS-photo) means the object appears in a "
                     "*position catalog* but may have no spectroscopic "
                     "characterisation. A hit in a spectroscopic or "
                     "classified-object catalog is a stronger claim of "
                     "archival identification.\n\n")
    else:
        lines.append("- (no VizieR hits recorded)\n\n")

    lines.append("## Recommendation for Paper 3 §5.1\n\n")
    if archival_id_rate is None:
        lines.append("Services degraded — no inference possible. Re-run "
                     "when NED and VizieR recover. Keep the current "
                     "SIMBAD-novel-as-upper-bound footnote (commit "
                     "`0364a5d`) until this sweep produces a number.\n\n")
    elif archival_id_rate >= 0.90:
        lines.append(f"DESI top-1000 shows an archival-ID rate of "
                     f"{100 * archival_id_rate:.1f} % in NED+VizieR — "
                     f"materially similar to the SDSS v2 result. The "
                     f"SIMBAD-novel framing in Paper 3 §5.1 is the same "
                     f"upper bound for DESI as it is for SDSS: most "
                     f"SIMBAD-novel DESI anomalies are present in at least "
                     f"one broader archival catalog. Paper 3 §5.1 DESI-"
                     f"specific novelty language should be softened with "
                     f"the same footnote already applied to the aggregate "
                     f"claim (commit `0364a5d`), and the distinction "
                     f"between *spectroscopic* novelty and *any-catalog* "
                     f"novelty should be made explicit. The scientific "
                     f"value of the anomalies is unchanged — they are still "
                     f"spectroscopically unusual — but the 'uncatalogued' "
                     f"framing cannot be supported.\n\n")
    else:
        lines.append(f"DESI top-1000 shows an archival-ID rate of only "
                     f"{100 * archival_id_rate:.1f} % in NED+VizieR — "
                     f"materially lower than the SDSS v2 result (100 %). "
                     f"DESI's anomaly scoring is reaching sources that "
                     f"broad photometric archives do not index, consistent "
                     f"with DESI going fainter/redder than all-sky "
                     f"photometry. Paper 3 §5.1 DESI-centred novelty "
                     f"claims hold with only the current upper-bound "
                     f"footnote caveat (commit `0364a5d`) — no further "
                     f"softening of DESI-specific language is required.\n\n")

    lines.append("## Files\n\n")
    lines.append(f"- `{OUTPUT_JSON.relative_to(BASE_DIR)}` — full per-object JSON\n")
    lines.append(f"- `{FINDINGS_OUT.relative_to(BASE_DIR)}` — this file\n")
    lines.append(f"- `{DESI_INPUT.relative_to(BASE_DIR)}` — DESI DR1 anomaly input\n")
    lines.append(f"- `projects/cross_survey/results/P3-B_findings_v2.md` — SDSS v2 parallel\n")

    FINDINGS_OUT.write_text("".join(lines))

    print(f"\n[desi] wrote {OUTPUT_JSON}")
    print(f"[desi] wrote {FINDINGS_OUT}")
    print(f"[desi] global counts: {dict(counts)}")
    print(f"[desi] service_status: {service_status}")
    print(f"[desi] archival-ID rate (resolved): "
          f"{archival_id_rate if archival_id_rate is None else f'{100*archival_id_rate:.1f} %'}")
    print(f"[desi] elapsed: {(time.time() - t0) / 60:.1f} min")
    return output


if __name__ == "__main__":
    main()
