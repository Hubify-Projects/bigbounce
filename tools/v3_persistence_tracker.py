#!/usr/bin/env python3
"""
v3 persistence-tracker — identifies findings that recur across N consecutive fires.

A finding that the meta-reviewer surfaces in 3+ consecutive rounds is no longer
"new" — it's a confirmed scientific issue requiring Houston decision. The autoloop
needs to ESCALATE these from "fire log noise" to "TRIAGE_QUEUE priority".

Usage:
    python tools/v3_persistence_tracker.py [--rounds N] [--min-rounds-persistent K]

Reads:
    project-context/peer-reviews/auto-*_*_META_REVIEW.md  (cross-fire meta findings)
    project-context/peer-reviews/auto-*_*_SYNTHESIS.md   (cross-fire reviewer consensus)

Outputs:
    project-context/peer-reviews/PERSISTENT_FINDINGS.md  (markdown report)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from collections import defaultdict, OrderedDict

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"

PAPERS = ["P1A", "P1B", "P2", "P3", "P4", "P5"]


def discover_rounds() -> list[str]:
    """Find all autoloop rounds in chronological order."""
    rounds = set()
    for p in REVIEWS_DIR.glob("auto-*_P*_SYNTHESIS.md"):
        # Format: auto-2026-06-05_1418pt_P4_SYNTHESIS.md
        parts = p.stem.split("_")
        # Round label is everything before the paper tag
        for i, part in enumerate(parts):
            if part in PAPERS:
                round_label = "_".join(parts[:i])
                rounds.add(round_label)
                break
    return sorted(rounds)


def parse_meta_findings(round_label: str, paper: str) -> dict:
    """Parse {paper}-META-E# / -M# IDs out of the meta-review .md."""
    meta_path = REVIEWS_DIR / f"{round_label}_{paper}_META_REVIEW.md"
    if not meta_path.exists():
        return {}
    text = meta_path.read_text(errors="replace")
    findings: dict = {}
    pat = re.compile(rf"^{re.escape(paper)}-META-(E\d+|M\d+|m\d+|N\d+|n\d+)\b", re.MULTILINE)
    # Capture each finding + its short summary (the "Specific problem" line)
    for m in pat.finditer(text):
        fid = m.group(1)
        start = m.end()
        # Find next finding header or end-of-text
        next_match = pat.search(text, pos=start)
        block_end = next_match.start() if next_match else len(text)
        block = text[start:block_end]
        # Extract a short summary — first line containing "Problem" or first 200 chars
        summary_match = re.search(r"(?:Specific problem|Problem)[^\n]*?:\s*([^\n]+)", block)
        summary = summary_match.group(1) if summary_match else block.strip()[:200]
        findings[fid] = summary.strip()[:300]
    return findings


def fingerprint(summary: str) -> str:
    """Crude signature for cross-round identity matching."""
    s = summary.lower()
    # Strip punctuation
    s = re.sub(r"[^a-z0-9]+", " ", s)
    # Keep top-tier keywords
    tokens = []
    keywords = [
        "binomial", "n_total", "n_spiral", "fsky", "non-binary", "weighted mask",
        "monopole", "leakage", "post-master", "pre-master", "master",
        "t-web", "v-web", "tidal tensor", "velocity shear",
        "dedup", "deduplication", "cross-match", "astrometric",
        "selection function", "random catalog", "n(z)", "radial",
        "label noise", "ce-resnet", "gz1",
        "double correction", "lee", "look-elsewhere", "bonferroni",
        "ap definition", "asymmetry definition", "denominator",
        "shamir", "iye", "tadaki",
        "table ii", "table iv", "abstract",
        "future date", "sigma values", "qualifier",
    ]
    for kw in keywords:
        if kw in s:
            tokens.append(kw.replace(" ", "_"))
    return "|".join(sorted(set(tokens))) if tokens else "other"


def main() -> int:
    rounds = discover_rounds()
    if not rounds:
        print("No autoloop rounds found", file=sys.stderr)
        return 1
    print(f"[persistence-tracker] {len(rounds)} round(s): {rounds}", file=sys.stderr)

    # Build round-by-round META findings: round → paper → {fingerprint: [(fid, summary)]}
    rounds_data = OrderedDict()
    for r in rounds:
        rounds_data[r] = {}
        for paper in PAPERS:
            findings = parse_meta_findings(r, paper)
            rounds_data[r][paper] = defaultdict(list)
            for fid, summary in findings.items():
                fp = fingerprint(summary)
                if fp == "other":
                    continue
                rounds_data[r][paper][fp].append((fid, summary))

    # For each (paper, fingerprint), count consecutive rounds it appears in
    persistence: dict = defaultdict(list)  # (paper, fp) → [round_label, ...]
    for r in rounds:
        for paper in PAPERS:
            for fp in rounds_data[r][paper]:
                persistence[(paper, fp)].append(r)

    # Build report
    out_lines: list[str] = []
    out_lines.append("# Persistent Meta-Findings Tracker")
    out_lines.append("")
    out_lines.append(f"Tracking META findings across {len(rounds)} autoloop fires.")
    out_lines.append(f"Rounds: {rounds}")
    out_lines.append("")
    out_lines.append("## Findings that persist ≥2 rounds (escalation candidates for Houston decision)")
    out_lines.append("")
    out_lines.append("Persistent META findings indicate scientific issues that the v3.2 meta-reviewer")
    out_lines.append("consistently surfaces. They are NOT mechanical bugs — they require Houston's")
    out_lines.append("judgment on which fix to apply (mechanical text edit vs analysis rerun vs")
    out_lines.append("text relabel).")
    out_lines.append("")

    escalations: list[tuple] = []
    for (paper, fp), seen in sorted(persistence.items(), key=lambda kv: -len(kv[1])):
        if len(seen) >= 2:
            escalations.append((paper, fp, seen))

    if not escalations:
        out_lines.append("(none — autoloop has not yet seen 2+ rounds of the same finding)")
    else:
        for paper, fp, seen in escalations:
            ratio = f"{len(seen)}/{len(rounds)}"
            tag = "🔴 LOAD-BEARING" if len(seen) >= 3 else "🟡 RECURRING"
            out_lines.append(f"### {tag} {paper} — `{fp}` ({ratio} rounds)")
            out_lines.append("")
            out_lines.append(f"Seen in rounds: {seen}")
            out_lines.append("")
            # Cite the first finding example
            r0 = seen[0]
            findings = rounds_data[r0][paper][fp]
            if findings:
                fid, summary = findings[0]
                out_lines.append(f"Example (round {r0}, finding {paper}-META-{fid}):")
                out_lines.append("")
                out_lines.append(f"> {summary}")
                out_lines.append("")

    out = REVIEWS_DIR / "PERSISTENT_FINDINGS.md"
    out.write_text("\n".join(out_lines))
    print(f"→ {out}", file=sys.stderr)
    print("\n".join(out_lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
