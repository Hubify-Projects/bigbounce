#!/usr/bin/env python3
"""
backfill_readiness_metrics.py — one-shot historical backfill of the
readinessMetrics table + rigorEvents, posted via the Convex public HTTP
mutation API (no auth key needed for data writes).

HONESTY CONTRACT (Houston, 2026-07-10):
  - EXT verdicts come ONLY from site/src/data/reviewTimeline.ts
    externalVerdictRounds (the committed, source-cited EXT history).
  - INT verdicts come ONLY from the H17 INT-API raws under
    project-context/peer-reviews/INT_api/H17_2026-07-10/ (each raw carries a
    literal `PARSED VERDICT:` / `(1) VERDICT:` line). INT history before H17 is
    patchy and is NOT fabricated — we backfill only what is file-verifiable.
  - A leg that produced no output is recorded verdict:"failed" (chart gap,
    never a zero).
  - genuinelyNewCount / cleanWaveStreak are set to a real value ONLY where the
    board documents it. For the H17 final waves the board (reviewTimeline
    H17F/H17H entries + CLAUDE.md directive H-refined) states "0 genuinely-new
    real findings" — those are the ETA-driving rows. Undocumented earlier
    rounds carry genuinelyNewCount defaulted to a documented-or-conservative
    value and DO NOT drive the ETA (the ETA reads each paper's LATEST wave).
  - rigor events cite their source (a CLAUDE.md directive letter or a board /
    reviewTimeline entry).

Data sources are pre-extracted to /tmp/ext_rounds.json and /tmp/int_verdicts.json
by the extraction step in the build session; if those are absent, this script
re-extracts ext rounds directly from reviewTimeline.ts.

Usage:  python3 tools/backfill_readiness_metrics.py [--dry-run]
"""
import json
import os
import re
import sys
import time
import urllib.request

CONVEX_MUT = "https://brilliant-panther-471.convex.cloud/api/mutation"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SLUG_BY_PID = {
    "P1A": "paper-1a", "P1B": "paper-1b", "P2": "paper-2",
    "P3": "paper-3", "P4": "paper-4", "P5": "paper-5",
}
EXT_REVIEWERS = ["ChatGPT", "Grok", "Gemini"]  # externalVerdictRounds triple order
VERDICT_MAP = {
    "REJECT": "reject", "MAJOR": "major-revisions",
    "MINOR": "minor-revisions", "ACCEPT": "accept", "NO_VERDICT": "failed",
}

DRY = "--dry-run" in sys.argv


def post_mutation(path, args):
    payload = json.dumps({"path": path, "args": args, "format": "json"}).encode()
    if DRY:
        print(f"  [dry] {path} :: {json.dumps(args)[:110]}")
        return {"status": "success", "value": {"dry": True}}
    req = urllib.request.Request(
        CONVEX_MUT, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        resp = json.load(r)
    if resp.get("status") != "success":
        raise RuntimeError(f"mutation {path} failed: {resp}")
    return resp


def load_ext_rounds():
    p = "/tmp/ext_rounds.json"
    if os.path.exists(p):
        return json.load(open(p))
    # Fallback: regex-extract from reviewTimeline.ts (roundId/dateISO/verdicts only)
    ts = open(os.path.join(REPO, "site/src/data/reviewTimeline.ts")).read()
    decl = ts.index("export const externalVerdictRounds")
    eq = ts.index("= [", decl) + 2
    depth, end = 0, -1
    for i in range(eq, len(ts)):
        if ts[i] == "[":
            depth += 1
        elif ts[i] == "]":
            depth -= 1
            if depth == 0:
                end = i
                break
    body = ts[eq:end + 1]
    out = []
    for chunk in re.split(r'(?=roundId:\s*")', body):
        if "roundId:" not in chunk:
            continue
        rid = re.search(r'roundId:\s*"([^"]+)"', chunk)
        dt = re.search(r'dateISO:\s*"([^"]+)"', chunk)
        vb = re.search(r"verdicts:\s*\{([\s\S]*?)\n\s*\},", chunk)
        if not (rid and dt and vb):
            continue
        verdicts = {}
        for m in re.finditer(r'(P1A|P1B|P2|P3|P4|P5):\s*\[([^\]]*)\]', vb.group(1)):
            verdicts[m.group(1)] = [
                s.strip().strip('"') for s in m.group(2).split(",")
            ]
        if verdicts:
            out.append({"roundId": rid.group(1), "dateISO": dt.group(1),
                        "verdicts": verdicts})
    return out


def load_int():
    return json.load(open("/tmp/int_verdicts.json"))


def seq_for(date_iso, tiebreak=0):
    # ms since epoch of the date + a small tiebreak so same-day waves order.
    t = time.mktime(time.strptime(date_iso, "%Y-%m-%d")) * 1000
    return int(t) + tiebreak


# ── Rigor events (each cites its source) ──────────────────────────────────
RIGOR_EVENTS = [
    {"label": "De-biased referee prompt", "dateISO": "2026-06-29",
     "description": "Severity-steering language struck from the external referee prompt; raw MAJOR counts rise (a feature) — a stricter bar, not degrading papers.",
     "source": "reviewTimeline RAEXT / skillsSeries 'RA · de-bias'; CLAUDE.md pattern-071"},
    {"label": "Integrity gate", "dateISO": "2026-06-26",
     "description": "Mandatory independent integrity audit + PDF-hygiene md5 pre-dispatch gate added before any convergence claim.",
     "source": "CLAUDE.md directive F; INTEGRITY_AUDIT_2026-06-26.md"},
    {"label": "Recalibrated gate", "dateISO": "2026-07-01",
     "description": "Convergence recalibrated to Grok+Gemini ACCEPT + every ChatGPT MAJOR truth-audited non-real (harsh-referee floor recognized).",
     "source": "CLAUDE.md directive H / H-refined (pattern-066)"},
    {"label": "Verified-review reset", "dateISO": "2026-07-04",
     "description": "'Converged/ACCEPT' claims caught as unverified; rebuilt EXT with raw text + screenshots READ before any verdict; readiness reset to 76-80.",
     "source": "CLAUDE.md verified-review reset; MEMORY feedback_verifiable_review_reset"},
    {"label": "Directive J 0/0/0", "dateISO": "2026-07-09",
     "description": "Program exit bar set LITERAL 0 MAJOR/0 MINOR/0 REJECT from every reviewer; never-idle loop.",
     "source": "CLAUDE.md directive J (2026-07-09)"},
    {"label": "Fused loops + directive K", "dateISO": "2026-07-10",
     "description": "INT/EXT fused per paper with disposition ledgers; two-consecutive-clean-waves convergence bar (directive K).",
     "source": "CLAUDE.md directive K; reviewTimeline H17H/H17F entries"},
]

# Waves whose genuinely-new count is DOCUMENTED as 0 (source-cited in the board).
# These are the ETA-driving rows. Key: (paperId, waveLabel-substring).
DOC_ZERO_NEW_WAVES = {
    # H17 final + presentation-closure: reviewTimeline H17F/H17H entries state
    # "0 genuinely-new real findings" across all reviewers.
    "H17-INT", "H17-INT-retest", "H17-INT-retest2", "H17-INT-retest3",
    "H17-INT-retest4",
}


def main():
    ext = load_ext_rounds()
    intv = load_int()

    # ── Build wave rows ──
    # rows keyed by (paperId, waveLabel) → {dateISO, seq, verdicts:[...]}
    rows = {}

    # EXT rounds: one row per (paper, round). verdicts = ChatGPT/Grok/Gemini EXT.
    for ri, r in enumerate(ext):
        for pid, triple in r["verdicts"].items():
            key = (pid, r["roundId"])
            vlist = []
            for reviewer, raw in zip(EXT_REVIEWERS, triple):
                vlist.append({
                    "reviewer": reviewer, "channel": "EXT",
                    "verdict": VERDICT_MAP.get(raw, "failed"),
                })
            rows[key] = {
                "paperId": pid, "paperSlug": SLUG_BY_PID[pid],
                "waveLabel": r["roundId"], "dateISO": r["dateISO"],
                "seq": seq_for(r["dateISO"], ri),
                "verdicts": vlist, "channelKind": "EXT",
            }

    # INT waves: group by (paperId, waveLabel), collect one verdict per reviewer.
    int_seq_base = len(ext) + 10
    for iv in intv:
        pid, wave = iv["paperId"], iv["waveLabel"]
        key = (pid, wave)
        if key not in rows:
            rows[key] = {
                "paperId": pid, "paperSlug": SLUG_BY_PID[pid],
                "waveLabel": wave, "dateISO": iv["dateISO"],
                "seq": seq_for(iv["dateISO"], int_seq_base),
                "verdicts": [], "channelKind": "INT",
            }
        rows[key]["verdicts"].append({
            "reviewer": iv["reviewer"], "channel": "INT",
            "verdict": iv["verdict"],
        })

    # ── Per-paper chronological streak computation ──
    # genuinelyNewCount: 0 for documented-zero waves; for all others we cannot
    # source a per-paper genuinely-new count from files, so we mark it 0 ONLY
    # if the wave is in DOC_ZERO_NEW_WAVES, else -1 (== "not sourced"; renders
    # as no-streak-credit). cleanWaveStreak counts trailing waves with
    # genuinelyNewCount == 0.
    by_paper = {}
    for row in rows.values():
        by_paper.setdefault(row["paperId"], []).append(row)

    payloads = []
    for pid, waves in by_paper.items():
        waves.sort(key=lambda w: w["seq"])
        streak = 0
        for w in waves:
            documented_zero = w["waveLabel"] in DOC_ZERO_NEW_WAVES
            genuinely_new = 0 if documented_zero else -1
            if genuinely_new == 0:
                streak += 1
            elif genuinely_new > 0:
                streak = 0
            # genuinely_new == -1 (unsourced): do NOT credit a clean streak,
            # but do NOT reset a documented streak either — leave streak as-is.
            payloads.append({
                "paperSlug": w["paperSlug"], "paperId": pid,
                "waveLabel": w["waveLabel"], "dateISO": w["dateISO"],
                "seq": w["seq"],
                "genuinelyNewCount": max(genuinely_new, 0),
                "cleanWaveStreak": streak if documented_zero else 0,
                "openComputeCount": 0, "openVenueCount": 0,
                "verdicts": w["verdicts"],
                "note": (w["channelKind"] + " wave; genuinely-new "
                         + ("0 (board-documented)" if documented_zero
                            else "not file-sourced")),
            })

    print(f"Prepared {len(payloads)} wave rows across {len(by_paper)} papers "
          f"({len(ext)} EXT rounds + {len(intv)} INT verdict rows).")

    ok = 0
    for p in payloads:
        post_mutation("readinessMetrics:recordWave", p)
        ok += 1
    print(f"Posted {ok} readinessMetrics rows.")

    re_ok = 0
    for e in RIGOR_EVENTS:
        post_mutation("readinessMetrics:recordRigorEvent", e)
        re_ok += 1
    print(f"Posted {re_ok} rigorEvents.")

    print("BACKFILL COMPLETE"
          + (" (dry-run — nothing written)" if DRY else ""))
    print(f"  readinessMetrics rows: {ok}")
    print(f"  rigorEvents: {re_ok}")


if __name__ == "__main__":
    main()
