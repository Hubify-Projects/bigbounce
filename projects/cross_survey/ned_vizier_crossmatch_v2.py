#!/usr/bin/env python3
"""
P3-B v2 — NED retry + VizieR + Gaia-XP cross-match sweep.

Follow-up to `ned_vizier_crossmatch.py` (fire #10) which rate-limited on
69/80 objects. This v2 script:

1. Re-reads the 80-sample target list from the fire #10 output
   (`results/ned_crossmatch_summary.json` — per-survey per_object lists).
2. For objects whose fire #10 classification was `error`: retries NED with
   a long inter-query delay + exponential backoff.
3. For every NED-novel object (fire #10 `still_uncatalogued` + any new
   NED-novel rows from step 2): VizieR all-catalogs cone search, budgeted.
4. For optically bright residual-novel objects (SDSS_DR18 + Gaia_DR3 only):
   Gaia DR3 source-level query flagging `has_xp_continuous` /
   `has_xp_sampled` — notes source IDs with XP spectra available. Does NOT
   download XP spectra (follow-up task).

Outputs:
- `results/ned_crossmatch_summary_v2.json` — full per-object table.
- `results/P3-B_findings_v2.md` — human-readable summary + SDSS
  archival-ID rate update + §7 honesty-footnote proposal (not applied).

Resilient to service outages: retries 3× with exponential backoff, writes
`service_degraded` note into findings if a whole service fails, and still
commits partial progress rather than crashing.
"""

import json
import math
import time
from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
RESULTS_DIR = BASE_DIR / "projects/cross_survey/results"
V1_INPUT = RESULTS_DIR / "ned_crossmatch_summary.json"
V2_OUTPUT = RESULTS_DIR / "ned_crossmatch_summary_v2.json"
FINDINGS_OUT = RESULTS_DIR / "P3-B_findings_v2.md"

NED_RADIUS_ARCSEC = 5.0
VIZIER_RADIUS_ARCSEC = 10.0
GAIA_MATCH_RADIUS_ARCSEC = 2.0

# NED: slow + polite
NED_DELAY_SEC = 8.0
NED_RETRIES = 3
NED_TIMEOUT_SEC = 15.0
# If the first N queries all fail, mark NED degraded and skip the rest
# (saves the remaining ~68 × 60 s = 68 min budget when NED is down).
NED_HEALTH_CHECK_N = 3

# VizieR: the 2-min per-query budget is generous; cap total budget.
VIZIER_TIMEOUT_SEC = 30.0
VIZIER_DELAY_SEC = 2.0
VIZIER_TOTAL_BUDGET_SEC = 25 * 60

# Gaia-XP brightness cut
G_MAG_MAX_GAIA = 19.0

# Service-health flags (set by run)
service_status = {
    "NED": "unknown",
    "VizieR": "unknown",
    "Gaia": "unknown",
}


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------

def _retry_with_backoff(fn, retries, label, base_sleep=2.0):
    """Retry fn() up to `retries` times with exponential backoff."""
    last_err = None
    for attempt in range(retries):
        try:
            return fn()
        except Exception as err:
            last_err = err
            sleep_s = base_sleep * (2 ** attempt)
            msg = str(err)[:160]
            print(f"    [{label}] attempt {attempt+1}/{retries} failed "
                  f"({msg}); sleeping {sleep_s:.1f}s", flush=True)
            time.sleep(sleep_s)
    return {"__error__": str(last_err)[:240] if last_err else "retry_exhausted"}


def query_ned(ra, dec):
    """NED cone search. Returns dict."""
    from astroquery.ipac.ned import Ned
    Ned.TIMEOUT = NED_TIMEOUT_SEC
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")

    def _do():
        tab = Ned.query_region(coord, radius=NED_RADIUS_ARCSEC * u.arcsec)
        if tab is None or len(tab) == 0:
            return {"matched": False, "n_matches": 0, "top_match": None}
        row = tab[0]

        def _s(k):
            try:
                v = row[k]
                return None if v is None else str(v)
            except Exception:
                return None

        return {
            "matched": True,
            "n_matches": int(len(tab)),
            "top_match": {
                "name": _s("Object Name"),
                "type": _s("Type"),
                "z": _s("Redshift"),
            },
        }

    res = _retry_with_backoff(_do, NED_RETRIES, "NED")
    if isinstance(res, dict) and "__error__" in res:
        return {"matched": False, "n_matches": 0, "error": res["__error__"]}
    return res


def query_vizier(ra, dec):
    """VizieR all-catalogs cone search."""
    from astroquery.vizier import Vizier
    V = Vizier(row_limit=5, timeout=VIZIER_TIMEOUT_SEC)
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")

    def _do():
        result = V.query_region(coord, radius=VIZIER_RADIUS_ARCSEC * u.arcsec)
        if result is None or len(result) == 0:
            return {"matched": False, "n_catalogs": 0, "catalogs": []}
        cats = []
        for tbl in result:
            nm = getattr(tbl.meta, "name", None) or tbl.meta.get("name", "?")
            cats.append({"catalog": str(nm), "n_rows": int(len(tbl))})
        return {
            "matched": True,
            "n_catalogs": len(cats),
            "catalogs": cats[:10],
        }

    res = _retry_with_backoff(_do, 2, "VizieR", base_sleep=3.0)
    if isinstance(res, dict) and "__error__" in res:
        return {"matched": False, "n_catalogs": 0, "error": res["__error__"]}
    return res


def query_gaia_xp(ra, dec):
    """Cone search Gaia DR3 for the closest source, report XP flags."""
    from astroquery.gaia import Gaia
    adql = f"""
        SELECT TOP 1
            source_id, ra, dec, phot_g_mean_mag,
            has_xp_continuous, has_xp_sampled,
            DISTANCE(
                POINT('ICRS', ra, dec),
                POINT('ICRS', {ra:.6f}, {dec:.6f})
            ) AS dist
        FROM gaiadr3.gaia_source
        WHERE 1=CONTAINS(
            POINT('ICRS', ra, dec),
            CIRCLE('ICRS', {ra:.6f}, {dec:.6f},
                   {GAIA_MATCH_RADIUS_ARCSEC / 3600.0})
        )
        ORDER BY dist ASC
    """

    def _do():
        job = Gaia.launch_job(adql)
        tab = job.get_results()
        if tab is None or len(tab) == 0:
            return {"matched": False}
        r = tab[0]

        def _num(k, cast=float):
            try:
                v = r[k]
                if v is None:
                    return None
                v = cast(v)
                if cast is float and (math.isnan(v) or math.isinf(v)):
                    return None
                return v
            except Exception:
                return None

        def _bool(k):
            try:
                v = r[k]
                return bool(v)
            except Exception:
                return None

        return {
            "matched": True,
            "source_id": str(r["source_id"]),
            "g_mag": _num("phot_g_mean_mag"),
            "has_xp_continuous": _bool("has_xp_continuous"),
            "has_xp_sampled": _bool("has_xp_sampled"),
            "dist_deg": _num("dist"),
        }

    res = _retry_with_backoff(_do, 2, "Gaia", base_sleep=3.0)
    if isinstance(res, dict) and "__error__" in res:
        return {"matched": False, "error": res["__error__"]}
    return res


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------

def load_v1_objects():
    """Load the 80-object table from v1 output; retain fire-#10 classification."""
    v1 = json.loads(V1_INPUT.read_text())
    out = []
    for survey, info in v1["per_survey"].items():
        for obj in info.get("per_object", []):
            out.append({
                "survey": survey,
                "obj_id": obj["obj_id"],
                "ra": float(obj["ra"]),
                "dec": float(obj["dec"]),
                "anomaly_score": obj.get("anomaly_score"),
                "v1_classification": obj["classification"],
                "v1_ned": obj.get("ned", {}),
            })
    return out


def write_snapshot(output):
    V2_OUTPUT.write_text(json.dumps(output, indent=2, default=str))


def main():
    t0 = time.time()
    print(f"[v2] loading {V1_INPUT.name}", flush=True)
    objs = load_v1_objects()
    print(f"[v2] {len(objs)} objects loaded", flush=True)

    # --- Stage 1: retry NED on v1-error objects ---
    print("\n=== Stage 1: NED retry on v1-error objects ===", flush=True)
    n_err = sum(1 for o in objs if o["v1_classification"] == "error")
    print(f"[v2] retrying NED on {n_err} rate-limit-errored objects", flush=True)

    ned_ok = 0
    ned_fail = 0
    ned_skipped_degraded = 0
    ned_degraded = False
    health_fails = 0
    for i, o in enumerate(objs):
        if o["v1_classification"] != "error":
            # Carry forward v1 NED result
            o["ned_v2"] = dict(o["v1_ned"])
            o["ned_v2"]["source"] = "v1"
            continue

        if ned_degraded:
            ned_skipped_degraded += 1
            o["ned_v2"] = {
                "matched": False,
                "n_matches": 0,
                "error": "skipped_service_degraded",
                "source": "v2",
            }
            continue

        print(f"  [{i+1:>2}/{len(objs)}] {o['survey']:<10s} "
              f"{o['obj_id'][:34]:<34s}", flush=True, end=" -> ")
        res = query_ned(o["ra"], o["dec"])
        res["source"] = "v2"
        o["ned_v2"] = res
        if res.get("matched"):
            ned_ok += 1
            health_fails = 0
            tag = f"matched ({res['top_match']['name']})"
        elif "error" in res:
            ned_fail += 1
            health_fails += 1
            tag = f"error ({res['error'][:50]})"
        else:
            health_fails = 0
            tag = "novel"
        print(tag, flush=True)
        time.sleep(NED_DELAY_SEC)

        # Health circuit breaker
        if health_fails >= NED_HEALTH_CHECK_N and ned_ok == 0:
            ned_degraded = True
            print(f"  [!!] NED circuit-breaker tripped after "
                  f"{health_fails} consecutive failures; skipping remaining "
                  f"v1-error objects", flush=True)

    # Service health inference
    if n_err > 0:
        if ned_degraded or (ned_fail > 0 and ned_ok == 0):
            service_status["NED"] = "degraded"
        else:
            service_status["NED"] = "ok"
    else:
        service_status["NED"] = "skipped"

    # --- Roll up per-object NED-v2 classification ---
    for o in objs:
        n = o["ned_v2"]
        if n.get("matched"):
            o["ned_v2_cls"] = "ned_matched"
        elif "error" in n:
            o["ned_v2_cls"] = "error"
        else:
            o["ned_v2_cls"] = "still_uncatalogued"

    # Snapshot after stage 1
    write_snapshot({
        "meta": {"stage": "1_ned_retry_done", "elapsed_sec": time.time() - t0},
        "objects": objs,
    })

    # --- Stage 2: VizieR on all NED-novel OR NED-error objects ---
    # If NED is degraded, a large pool of objects couldn't be resolved against
    # NED; the best we can do is ask VizieR independently and let it surface
    # archival identifications. Exclude only confirmed NED-matched objects.
    print("\n=== Stage 2: VizieR on NED-novel + NED-error objects ===",
          flush=True)
    novel = [o for o in objs if o["ned_v2_cls"] != "ned_matched"]
    print(f"[v2] {len(novel)} objects into VizieR stage "
          f"(NED-novel + NED-error)", flush=True)

    viz_ok = 0
    viz_fail = 0
    vz_start = time.time()
    for i, o in enumerate(novel):
        if time.time() - vz_start > VIZIER_TOTAL_BUDGET_SEC:
            print(f"  [{i+1}/{len(novel)}] VizieR budget exhausted, "
                  f"stopping stage 2", flush=True)
            for rem in novel[i:]:
                rem["vizier"] = {"matched": False, "skipped": "budget_exhausted"}
            break
        print(f"  [{i+1:>2}/{len(novel)}] {o['survey']:<10s} "
              f"{o['obj_id'][:34]:<34s}", flush=True, end=" -> ")
        res = query_vizier(o["ra"], o["dec"])
        o["vizier"] = res
        if res.get("matched"):
            viz_ok += 1
            tag = f"matched ({res['n_catalogs']} cats)"
        elif "error" in res:
            viz_fail += 1
            tag = f"error ({res['error'][:50]})"
        else:
            tag = "novel"
        print(tag, flush=True)
        time.sleep(VIZIER_DELAY_SEC)

    # Roll up per-object final novel/matched state
    for o in objs:
        vz = o.get("vizier", {})
        if o["ned_v2_cls"] == "ned_matched":
            o["final_cls"] = "ned_matched"
        elif vz.get("matched"):
            o["final_cls"] = "vizier_matched"
        elif vz.get("skipped"):
            o["final_cls"] = "vizier_skipped_budget"
        elif "error" in vz:
            o["final_cls"] = "vizier_error_unresolved"
        elif o["ned_v2_cls"] == "error":
            # NED couldn't resolve and VizieR also didn't match → unresolved
            o["final_cls"] = "ned_error_unresolved"
        else:
            o["final_cls"] = "residual_novel"

    # VizieR service status
    if len(novel) == 0:
        service_status["VizieR"] = "skipped"
    elif viz_ok + viz_fail > 0 and viz_fail == len([n for n in novel
                                                     if "vizier" in n]):
        service_status["VizieR"] = "degraded"
    else:
        service_status["VizieR"] = "ok"

    write_snapshot({
        "meta": {"stage": "2_vizier_done", "elapsed_sec": time.time() - t0},
        "objects": objs,
    })

    # --- Stage 3: Gaia-XP on residual-novel bright optical (SDSS + Gaia_DR3) ---
    print("\n=== Stage 3: Gaia-XP on residual-novel bright optical sources ===",
          flush=True)
    candidates = [o for o in objs
                  if o["final_cls"] == "residual_novel"
                  and o["survey"] in ("SDSS_DR18", "Gaia_DR3")]
    print(f"[v2] {len(candidates)} residual-novel SDSS+Gaia candidates", flush=True)

    gaia_ok = 0
    gaia_fail = 0
    xp_available = 0
    for i, o in enumerate(candidates):
        print(f"  [{i+1:>2}/{len(candidates)}] {o['survey']:<10s} "
              f"{o['obj_id'][:34]:<34s}", flush=True, end=" -> ")
        res = query_gaia_xp(o["ra"], o["dec"])
        o["gaia_xp"] = res
        if res.get("matched"):
            gaia_ok += 1
            g = res.get("g_mag")
            bright = g is not None and g <= G_MAG_MAX_GAIA
            o["gaia_xp_bright"] = bright
            has_xp = res.get("has_xp_continuous") or res.get("has_xp_sampled")
            if bright and has_xp:
                xp_available += 1
                tag = f"Gaia src {res['source_id']} G={g:.2f} XP=YES"
            else:
                tag = (f"Gaia src {res['source_id']} G="
                       f"{g if g is None else f'{g:.2f}'} XP=no")
        elif "error" in res:
            gaia_fail += 1
            tag = f"error ({res['error'][:50]})"
        else:
            tag = "no Gaia match"
        print(tag, flush=True)
        time.sleep(1.0)

    if len(candidates) == 0:
        service_status["Gaia"] = "skipped"
    elif gaia_fail == len(candidates):
        service_status["Gaia"] = "degraded"
    else:
        service_status["Gaia"] = "ok"

    # --- Summary ---
    counts = {
        "ned_matched": 0,
        "vizier_matched": 0,
        "residual_novel": 0,
        "ned_error_unresolved": 0,
        "vizier_error_unresolved": 0,
        "vizier_skipped_budget": 0,
    }
    per_survey = {}
    for o in objs:
        counts[o["final_cls"]] = counts.get(o["final_cls"], 0) + 1
        ps = per_survey.setdefault(o["survey"], {k: 0 for k in counts})
        ps[o["final_cls"]] += 1

    output = {
        "meta": {
            "description": (
                "P3-B v2 — NED retry + VizieR + Gaia-XP cross-match sweep. "
                "Builds on fire #10's ned_crossmatch_summary.json."
            ),
            "v1_input": str(V1_INPUT.relative_to(BASE_DIR)),
            "ned_radius_arcsec": NED_RADIUS_ARCSEC,
            "vizier_radius_arcsec": VIZIER_RADIUS_ARCSEC,
            "gaia_match_radius_arcsec": GAIA_MATCH_RADIUS_ARCSEC,
            "ned_delay_sec": NED_DELAY_SEC,
            "ned_retries": NED_RETRIES,
            "ned_timeout_sec": NED_TIMEOUT_SEC,
            "vizier_total_budget_sec": VIZIER_TOTAL_BUDGET_SEC,
            "g_mag_max_gaia": G_MAG_MAX_GAIA,
            "n_objects_total": len(objs),
            "stage1_ned_ok": ned_ok,
            "stage1_ned_fail": ned_fail,
            "stage2_vizier_ok": viz_ok,
            "stage2_vizier_fail": viz_fail,
            "stage3_gaia_ok": gaia_ok,
            "stage3_gaia_fail": gaia_fail,
            "stage3_xp_available": xp_available,
            "service_status": service_status,
            "elapsed_sec": time.time() - t0,
            "status": "complete",
        },
        "global_counts": counts,
        "per_survey": per_survey,
        "objects": objs,
    }
    write_snapshot(output)

    # --- SDSS sub-sample archival-ID rate (deterministic replay of first 11) ---
    sdss = [o for o in objs if o["survey"] == "SDSS_DR18"]
    sdss_ranked = sdss[:15]  # matches fire #10 "top-11 usable" (ranks 1-15 mod gaps)
    sdss_idrate_final = None
    # Closed definition: of SDSS objects whose final_cls is NOT an *unresolved
    # error*, fraction that are (ned_matched OR vizier_matched).
    resolved = [o for o in sdss
                if o["final_cls"] not in ("ned_error_unresolved",
                                           "vizier_error_unresolved",
                                           "vizier_skipped_budget")]
    resolved_matched = [o for o in resolved
                        if o["final_cls"] in ("ned_matched", "vizier_matched")]
    if resolved:
        sdss_idrate_final = len(resolved_matched) / len(resolved)

    # --- Findings file ---
    lines = []
    lines.append("# P3-B v2 — NED retry + VizieR + Gaia-XP findings\n")
    lines.append(f"**Date:** 2026-04-18 (drive-to-100 follow-up to fire #10)\n")
    lines.append("**Closes:** `P3-B-NED-RETRY`, `P3-B-VIZIER`. "
                 "**Advances:** `P3-B-GAIA-XP`.\n\n")
    lines.append("## Service status\n\n")
    for svc, st in service_status.items():
        lines.append(f"- **{svc}**: `{st}`\n")
    lines.append("\n## Global counts (80 objects)\n\n")
    lines.append("| Classification | Count |\n|---|---:|\n")
    for k, v in counts.items():
        lines.append(f"| `{k}` | {v} |\n")

    lines.append("\n## Per-survey breakdown\n\n")
    for survey, ps in per_survey.items():
        lines.append(f"### {survey}\n\n")
        for k, v in ps.items():
            if v > 0:
                lines.append(f"- `{k}`: {v}\n")
        lines.append("\n")

    lines.append("## Stage summary\n\n")
    lines.append(f"- Stage 1 NED retry: {ned_ok} matched / {ned_fail} errored "
                 f"(of {n_err} v1-errored)\n")
    lines.append(f"- Stage 2 VizieR: {viz_ok} matched / {viz_fail} errored "
                 f"(of {len(novel)} NED-novel)\n")
    lines.append(f"- Stage 3 Gaia-XP: {gaia_ok} Gaia matches, "
                 f"{xp_available} with XP spectra available "
                 f"(of {len(candidates)} residual-novel SDSS+Gaia)\n\n")

    lines.append("## SDSS archival-ID rate — updated\n\n")
    lines.append(f"- **Fire #10 headline:** 45 % (5 / 11) on usable SDSS sub-sample.\n")
    if sdss_idrate_final is not None:
        lines.append(f"- **v2 full-SDSS rate** (resolved only): "
                     f"**{100 * sdss_idrate_final:.1f} %** "
                     f"({len(resolved_matched)} / {len(resolved)}).\n")
    else:
        lines.append("- **v2 full-SDSS rate:** no resolved objects — service degraded.\n")

    lines.append("\n## Gaia-XP availability\n\n")
    xp_ids = [o for o in candidates
              if o.get("gaia_xp", {}).get("matched")
              and o.get("gaia_xp_bright")
              and (o["gaia_xp"].get("has_xp_continuous")
                   or o["gaia_xp"].get("has_xp_sampled"))]
    lines.append(f"- {xp_available} residual-novel optical sources have "
                 f"XP spectra available in Gaia DR3 (G ≤ {G_MAG_MAX_GAIA}).\n")
    if xp_ids:
        lines.append("- Source IDs to pull (follow-up task):\n\n")
        for o in xp_ids:
            gx = o["gaia_xp"]
            lines.append(f"  - `{gx['source_id']}` (obj `{o['obj_id']}`, "
                         f"G={gx.get('g_mag'):.2f}, "
                         f"XP_cont={gx.get('has_xp_continuous')}, "
                         f"XP_samp={gx.get('has_xp_sampled')})\n")

    lines.append("\n## Paper 3 §7 honesty-footnote — PROPOSED, not applied\n\n")
    lines.append("The fire #10 footnote pointed at `P3-B_findings.md` and the\n"
                 "preliminary 45 % NED-ID rate on an 11-object SDSS sub-sample.\n"
                 "Proposed update for §7 limitations (Houston's call to apply):\n\n")
    if sdss_idrate_final is not None:
        lines.append("> **Footnote update (proposed):** A v2 NED+VizieR sweep on\n"
                     f"> the full SDSS-DR18 top-20 novel sample yields an archival-\n"
                     f"> identification rate of {100 * sdss_idrate_final:.1f} %\n"
                     f"> ({len(resolved_matched)} / {len(resolved)} resolved). The\n"
                     "> program-wide 'novel' fraction quoted in Paper 3 §5 should\n"
                     "> therefore be read as an upper bound on true novelty: a\n"
                     "> non-trivial fraction of SIMBAD-uncatalogued anomalies are\n"
                     "> already identified in NED/VizieR. See\n"
                     "> `projects/cross_survey/results/P3-B_findings_v2.md` for the\n"
                     "> per-survey breakdown and Gaia-XP follow-up targets.\n\n")
    else:
        lines.append("> **Footnote update (proposed):** NED service was degraded\n"
                     "> during the v2 retry; keep the fire #10 45 % figure and\n"
                     "> re-run when services recover. No change to §7 wording.\n\n")

    lines.append("## Files\n\n")
    lines.append(f"- `{V2_OUTPUT.relative_to(BASE_DIR)}` — full per-object JSON\n")
    lines.append(f"- `{FINDINGS_OUT.relative_to(BASE_DIR)}` — this file\n")
    lines.append(f"- `{V1_INPUT.relative_to(BASE_DIR)}` — fire #10 v1 input\n")

    FINDINGS_OUT.write_text("".join(lines))

    print(f"\n[v2] wrote {V2_OUTPUT}")
    print(f"[v2] wrote {FINDINGS_OUT}")
    print(f"[v2] global counts: {counts}")
    print(f"[v2] service_status: {service_status}")
    print(f"[v2] elapsed: {(time.time() - t0) / 60:.1f} min")
    return output


if __name__ == "__main__":
    main()
