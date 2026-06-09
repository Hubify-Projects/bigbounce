#!/usr/bin/env python3
"""
v3 autoloop-log-entry — auto-generate the AUTOLOOP_LOG.md closure entry
for a given fire, pulling per-paper findings, content-diff results,
closure-verification status, and pattern-040 sweep state.

Usage:
    python tools/v3_autoloop_log_entry.py <new_round> [<prev_round>]

Outputs the entry to stdout. Pipe to >> AUTOLOOP_LOG.md to append.

Example:
    python tools/v3_autoloop_log_entry.py auto-2026-06-08_1737pt > /tmp/entry.md

Avoids the 80-line manual entry that I've been writing for every fire.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS = REPO / "project-context" / "peer-reviews"
PAPERS = ["P1A", "P1B", "P2", "P3", "P4", "P5"]


def find_prev_round(new_round: str) -> str:
    rounds = set()
    for f in REVIEWS.glob("auto-*_META_REVIEW.md"):
        m = re.match(r"(auto-[\d_pt-]+)_P[\w\d]+_META_REVIEW\.md", f.name)
        if m:
            rounds.add(m.group(1))
    rounds = sorted(rounds)
    if new_round in rounds:
        idx = rounds.index(new_round)
        if idx > 0:
            return rounds[idx - 1]
    if rounds:
        return rounds[-2] if len(rounds) >= 2 else rounds[-1]
    return ""


def per_paper_findings(round_label: str) -> dict:
    log = REVIEWS / "AUTOLOOP_LOG.md"
    counts = {}
    if not log.exists():
        return counts
    text = log.read_text()
    pattern = re.compile(
        rf"## {re.escape(round_label.replace('auto-', ''))}.*?(?=## |\Z)",
        re.DOTALL,
    )
    m = pattern.search(text)
    block = m.group(0) if m else ""
    for paper in PAPERS:
        line_pat = re.compile(rf"-\s+{paper}:\s+(\d+)\s+findings,\s+(\d+)\s+consensus")
        line_m = line_pat.search(block)
        if line_m:
            counts[paper] = (int(line_m.group(1)), int(line_m.group(2)))
    return counts


def content_diff_summary(prev: str, new: str) -> dict:
    if not prev:
        return {"new_ess": 0, "recurring": 0, "closed": 0, "papers_with_new": 0}
    # Note: v3_meta_content_diff.py exits with code = papers_with_new (non-zero
    # on any new finding), so we must use check=False to avoid raising.
    try:
        r = subprocess.run(
            ["python3", str(REPO / "tools" / "v3_meta_content_diff.py"), prev, new],
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            timeout=60,
            check=False,
        )
        out = r.stdout.decode()
    except Exception as e:
        return {"new_ess": 0, "recurring": 0, "closed": 0, "papers_with_new": 0,
                "error": str(e)[:200]}
    result = {"new_ess": 0, "recurring": 0, "closed": 0, "papers_with_new": 0}
    for line in out.splitlines():
        # Match: "  NEW = 14, RECURRING = 0, CLOSED = 18"
        m = re.search(r"NEW\s*=\s*(\d+)\s*,?\s*RECURRING\s*=\s*(\d+)\s*,?\s*CLOSED\s*=\s*(\d+)", line)
        if m:
            result["new_ess"] = int(m.group(1))
            result["recurring"] = int(m.group(2))
            result["closed"] = int(m.group(3))
        # Match: "  papers with NEW ESS findings: 6 / 6"
        m = re.search(r"papers with NEW ESS.*?:\s*(\d+)\s*/", line)
        if m:
            result["papers_with_new"] = int(m.group(1))
    return result


def closure_verif_summary() -> dict:
    # v3_closure_verification.py exits with code = closures_re_fired
    try:
        r = subprocess.run(
            ["python3", str(REPO / "tools" / "v3_closure_verification.py")],
            stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
            timeout=30, check=False,
        )
        out = r.stdout.decode()
    except Exception as e:
        return {"tracked": 0, "re_fired": 0, "stuck": 0, "error": str(e)[:200]}
    result = {"tracked": 0, "re_fired": 0, "stuck": 0}
    for line in out.splitlines():
        m = re.search(r"Total closures tracked:\s*(\d+)", line)
        if m:
            result["tracked"] = int(m.group(1))
        m = re.search(r"Closures that RE-FIRED:\s*(\d+)", line)
        if m:
            result["re_fired"] = int(m.group(1))
        m = re.search(r"Closures STUCK:\s*(\d+)", line)
        if m:
            result["stuck"] = int(m.group(1))
    return result


def pattern040_sweep() -> int:
    try:
        r = subprocess.run(
            ["bash", str(REPO / "tools" / "v3_pattern040_all_papers.sh")],
            stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
            timeout=60, check=False,
        )
        out = r.stdout.decode()
    except Exception:
        return -1
    m = re.search(r"OVERALL TOTAL:\s*(\d+)\s+flagged", out)
    return int(m.group(1)) if m else -1


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    new_round = sys.argv[1]
    prev_round = sys.argv[2] if len(sys.argv) > 2 else find_prev_round(new_round)

    findings = per_paper_findings(new_round)
    diff = content_diff_summary(prev_round, new_round)
    closures = closure_verif_summary()
    p040 = pattern040_sweep()

    ts_m = re.match(r"auto-(\d{4}-\d{2}-\d{2})_(\d{4})pt", new_round)
    date_str = ts_m.group(1) if ts_m else "?"
    time_str = (ts_m.group(2)[:2] + ":" + ts_m.group(2)[2:]) if ts_m else "?"

    print(f"\n### Fire closure ({date_str} {time_str}pt -- round {new_round})")
    print(f"")
    print(f"Auto-generated by tools/v3_autoloop_log_entry.py.")
    print(f"")
    print(f"Per-paper findings:")
    for paper in PAPERS:
        if paper in findings:
            f, c = findings[paper]
            print(f"  {paper}: {f} findings, {c} consensus")
        else:
            print(f"  {paper}: (not found in AUTOLOOP_LOG summary)")
    print(f"")
    print(f"### Content-diff {prev_round} -> {new_round}")
    print(f"")
    print(f"- NEW: {diff.get('new_ess', '?')}, RECURRING: {diff.get('recurring', '?')}, CLOSED: {diff.get('closed', '?')}")
    print(f"- Papers with NEW ESS: {diff.get('papers_with_new', '?')} / 6")
    print(f"")
    print(f"### Closure ledger verification")
    print(f"")
    print(f"- Total closures tracked: {closures.get('tracked', '?')}")
    print(f"- RE-FIRED: {closures.get('re_fired', '?')}")
    print(f"- STUCK: {closures.get('stuck', '?')}")
    print(f"")
    print(f"### Pattern-040 sweep")
    print(f"")
    print(f"- Cross-section contradictions across all 6 papers: {p040}")
    print(f"")
    print(f"### Self-terminate counter recommendation")
    print(f"")
    if diff.get("new_ess", 1) == 0 and closures.get("re_fired", 1) == 0:
        print(f"ADVANCE counter (this fire is clean -- 0 NEW ESS, 0 RE-FIRED)")
    else:
        print(f"RESET / HOLD counter (NEW ESS = {diff.get('new_ess', '?')}, "
              f"RE-FIRED = {closures.get('re_fired', '?')})")
    print(f"")


if __name__ == "__main__":
    main()
