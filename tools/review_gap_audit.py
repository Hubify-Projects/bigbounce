#!/usr/bin/env python3
"""
Quantify the internal/external review-gap closure.

Counts ESSENTIAL/MAJOR/MINOR/NIT findings per reviewer per round, and produces
a side-by-side diff between an old pdftotext-based round and a new native-PDF
round, so we can prove the gap is actually closing.

Usage:
    python tools/review_gap_audit.py <old_round_label> <new_round_label> <paper_tag>

Example:
    python tools/review_gap_audit.py R9 R10v3 P4
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"

SEVERITY_PATTERNS = {
    "ESSENTIAL": re.compile(r"\b(?:ESSENTIAL|BLOCKER|E\d+|B\d+)\b"),
    "MAJOR": re.compile(r"\bMAJOR\b|\bM\d+\b"),
    "MINOR": re.compile(r"\bMINOR\b|\bm\d+\b"),
    "NIT": re.compile(r"\bNIT\b|\bN\d+\b|\bn\d+\b"),
}

FINDING_ID_RE = re.compile(r"\b([PR]?\d?[A-Z]?\d?-?[EBMmNn]\d+)\b")


def count_findings(text: str) -> dict:
    counts = {k: 0 for k in SEVERITY_PATTERNS}
    section = None
    for line in text.splitlines():
        line_strip = line.strip()
        upper = line_strip.upper()
        for sev in SEVERITY_PATTERNS:
            if upper.startswith(("####", "###", "##")) and sev in upper:
                section = sev
                break
        if section and FINDING_ID_RE.search(line_strip):
            counts[section] += 1
    return counts


def find_review_files(round_label: str, paper_tag: str) -> list[Path]:
    """Match files like R9_P4_Grok_brutal.md or 2026-06-04_1814pt_P4_Grok_brutal.md."""
    pattern = f"{round_label}_{paper_tag}_*.md"
    return sorted(REVIEWS_DIR.glob(pattern))


def extract_recommendation(text: str) -> str:
    m = re.search(
        r"(?:Summary recommendation|recommendation)\s*\n+\**\s*"
        r"(REJECT|MAJOR REVISIONS|MINOR REVISIONS|ACCEPT WITH MINOR CORRECTIONS|ACCEPT)",
        text, re.IGNORECASE,
    )
    return m.group(1).upper() if m else "UNKNOWN"


def reviewer_from_filename(p: Path) -> str:
    stem = p.stem
    parts = stem.split("_", 2)
    return parts[2] if len(parts) >= 3 else stem


def audit_round(round_label: str, paper_tag: str) -> dict:
    files = find_review_files(round_label, paper_tag)
    out: dict = {"round": round_label, "paper": paper_tag, "reviewers": {}}
    for p in files:
        name = p.name.lower()
        if "external" in name or "synthesis" in name or "meta_review" in name:
            continue
        text = p.read_text(errors="replace")
        out["reviewers"][reviewer_from_filename(p)] = {
            "file": p.name,
            "size_chars": len(text),
            "counts": count_findings(text),
            "recommendation": extract_recommendation(text),
        }
    return out


def total_findings(audit: dict, sev: str) -> int:
    return sum(r["counts"].get(sev, 0) for r in audit["reviewers"].values())


def print_audit(audit: dict) -> None:
    print(f"\n## {audit['round']} — {audit['paper']}")
    print(f"  reviewers: {len(audit['reviewers'])}")
    if not audit["reviewers"]:
        print("  (no files found)")
        return
    headers = ("Reviewer", "ESS", "MAJ", "MIN", "NIT", "Chars", "Rec")
    print(f"  {headers[0]:24s} {headers[1]:>4s} {headers[2]:>4s} {headers[3]:>4s} {headers[4]:>4s} {headers[5]:>7s}  {headers[6]}")
    for name, info in audit["reviewers"].items():
        c = info["counts"]
        print(f"  {name:24s} {c.get('ESSENTIAL',0):>4d} {c.get('MAJOR',0):>4d} {c.get('MINOR',0):>4d} {c.get('NIT',0):>4d} {info['size_chars']:>7d}  {info['recommendation']}")
    print(f"  {'TOTAL':24s} {total_findings(audit,'ESSENTIAL'):>4d} {total_findings(audit,'MAJOR'):>4d} {total_findings(audit,'MINOR'):>4d} {total_findings(audit,'NIT'):>4d}")


def gap_delta(old: dict, new: dict) -> None:
    print(f"\n## GAP DELTA: {new['round']} vs {old['round']}")
    for sev in ["ESSENTIAL", "MAJOR", "MINOR", "NIT"]:
        old_n = total_findings(old, sev)
        new_n = total_findings(new, sev)
        delta = new_n - old_n
        arrow = "▲" if delta > 0 else ("▼" if delta < 0 else "=")
        print(f"  {sev:10s}: old={old_n:>3d}  new={new_n:>3d}  {arrow} {delta:+d}")

    new_only = set(new["reviewers"].keys()) - set(old["reviewers"].keys())
    if new_only:
        print(f"  reviewers added in new round: {sorted(new_only)}")
    chars_old = sum(r["size_chars"] for r in old["reviewers"].values())
    chars_new = sum(r["size_chars"] for r in new["reviewers"].values())
    print(f"  total report chars: old={chars_old:,}  new={chars_new:,}  ({(chars_new/chars_old-1)*100:+.1f}%)")


def main() -> int:
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <old_round> <new_round> <paper_tag>", file=sys.stderr)
        return 1
    old_round, new_round, paper = sys.argv[1], sys.argv[2], sys.argv[3]
    old_audit = audit_round(old_round, paper)
    new_audit = audit_round(new_round, paper)
    print_audit(old_audit)
    print_audit(new_audit)
    gap_delta(old_audit, new_audit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
