#!/usr/bin/env python3
"""
v3 review synthesis — aggregate all 5 reviewer outputs into one consolidated report.

For each paper + round, finds all reviewer .md files, parses findings, dedupes
across reviewers (when 2+ reviewers flag the same issue, label it CONSENSUS),
and emits a single MASTER findings list ordered by severity then consensus count.

This is what closes the loop for Houston: one report per paper showing the union
of what all 5 vendors found, with consensus weighting so we know what's most
important to fix first.

Usage:
    python tools/v3_review_synthesis.py <round_label> <paper_tag>

Example:
    python tools/v3_review_synthesis.py R10v3 P4
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"

# Severity-level header detection (matches "ESSENTIAL", "MAJOR", "MINOR", "NIT")
SEV_HEADER_RE = re.compile(
    r"^#{0,4}\s*\**\s*(ESSENTIAL|MAJOR|MINOR|NIT|FATAL|BLOCKER)\b",
    re.IGNORECASE,
)

# Finding marker — broad pattern matching across all vendor formats:
#   P4-E1, P4-M3, P4-m1, P4-N1, P4-NIT1, GRO-B1, P4-META-E1
# Used at the start of a line (optionally with markdown bold) to indicate
# a new finding. We allow both upper-case and lower-case severities.
FINDING_ID_RE = re.compile(
    r"\b([Pp]?\d?[A-Z]?-?(?:META-)?[EBMmNnFf]\d+|B\d+|NIT\d+|N\d+)\b"
)


def reviewer_from_filename(p: Path) -> str:
    """Extract reviewer name from filename like R10v3_P4_Grok_brutal.md."""
    parts = p.stem.split("_", 2)
    return parts[2] if len(parts) >= 3 else p.stem


def parse_findings(md_text: str, reviewer: str) -> list[dict]:
    """Split a single reviewer .md into individual findings.
    Handles multiple ID conventions:
      P4-E1, P4-M3, P4-m1, P4-N1, P4-NIT1
      **P4-E7** (Claude format with bold)
      P4-META-E1 (meta-reviewer format)
    Infers severity from the ID letter when no section header is present.
    """
    findings: list[dict] = []
    cur_sev = None
    cur_block: list[str] = []
    cur_id = None

    LEADING_ID_RE = re.compile(
        r"^(?:#{1,4}\s*)?\**\s*[Pp]?\d?[A-Z]?-?(?:META-)?([EBMmNnFf])(\d+)\b"
    )

    def infer_severity_from_id(fid: str) -> str:
        """Map ID letter to severity. E/B → ESSENTIAL; M (upper) → MAJOR;
        m (lower) → MINOR; N (upper) → NIT; n (lower) → NIT; F → FATAL."""
        # Strip prefix like "P4-" or "P4-META-"
        tail = fid.split("-")[-1]
        if not tail:
            return "UNKNOWN"
        letter = tail[0]
        if letter in ("E", "B", "F"):
            return "ESSENTIAL"
        elif letter == "M":
            return "MAJOR"
        elif letter == "m":
            return "MINOR"
        elif letter in ("N", "n"):
            return "NIT"
        return "UNKNOWN"

    def flush():
        nonlocal cur_block, cur_id
        if cur_id and cur_block:
            sev = cur_sev or infer_severity_from_id(cur_id)
            findings.append({
                "reviewer": reviewer,
                "severity": sev,
                "id": cur_id,
                "text": "\n".join(cur_block).strip(),
            })
        cur_block = []
        cur_id = None

    for line in md_text.splitlines():
        s = line.strip()

        # severity-section header
        m_sev = SEV_HEADER_RE.match(s)
        if m_sev:
            flush()
            cur_sev = m_sev.group(1).upper()
            continue

        # finding id marker at line start (with optional ** wrap)
        m_lead = LEADING_ID_RE.match(s)
        if m_lead:
            flush()
            # capture the full ID from the line
            full_id_match = FINDING_ID_RE.search(s)
            cur_id = full_id_match.group(1) if full_id_match else m_lead.group(0).strip(" *")

        if cur_id:
            cur_block.append(line)

    flush()
    return findings


def normalize_id(fid: str) -> str:
    """P4-E1 → e1, GRO-B1 → b1, etc. for cross-reviewer dedup."""
    return fid.lower().split("-")[-1]


def consensus_key(text: str) -> str:
    """Build a coarse consensus key from finding text — words like 'N_MC=500',
    'σ values', 'Table II', 'Iye', 'Shamir', 'companion'..."""
    keywords = []
    for kw_re, label in [
        (r"\bN[_ ]?MC\b.*\b500\b", "n_mc_500"),
        (r"\bsigma values?\b|\bσ values?\b", "sigma_mixing"),
        (r"\b[Tt]able\s+I[I]+\b", "table_ii"),
        (r"\b[Tt]able\s+IV\b", "table_iv"),
        (r"\b[Ii]ye\b", "iye_citation"),
        (r"\b[Ss]hamir\b", "shamir_citation"),
        (r"\bcompanion\b", "companion"),
        (r"\b[Cc]osmic variance\b", "cosmic_variance"),
        (r"\bNmap\b|\bN_map\b", "nmap_weighting"),
        (r"\b28\.8\b|\b28\.32\b", "table_ii_sigma_arithmetic"),
        (r"\b3\.86\b|\b3\.0\b.*suppression", "asymmetry_factor"),
        (r"\bFisher\b.*0\.29|\bFisher\b.*0\.167", "fisher_floor"),
        (r"\bz.*1\.68\b|\bz.*1\.57\b", "table_iv_z"),
        (r"\b67\.6%?\b.*CE-?ResNet|\blabel noise\b", "label_noise"),
        (r"\bpage count\b|\btoo long\b|\bcondense\b|\bshorten\b", "length"),
        (r"\bversion[- ]history\b|\bsuperseded\b|\bR\d+\b", "audit_artifact"),
        (r"\bcanonical canonical\b|\bduplicate phrase\b", "duplicate_phrase"),
        (r"\bfuture date\b|\b2026\b.*date", "future_date"),
    ]:
        if re.search(kw_re, text, re.IGNORECASE):
            keywords.append(label)
    return ",".join(keywords) if keywords else "other"


def synthesize(round_label: str, paper_tag: str) -> str:
    pattern = f"{round_label}_{paper_tag}_*.md"
    files = sorted(REVIEWS_DIR.glob(pattern))
    if not files:
        return f"# No reviews found for {round_label} {paper_tag}\n"

    all_findings: list[dict] = []
    per_reviewer: dict[str, list[dict]] = {}
    failed_reviewers: list[str] = []

    for p in files:
        reviewer = reviewer_from_filename(p)
        if "synthesis" in reviewer.lower():
            continue
        _txt = p.read_text(errors="replace")
        findings = parse_findings(_txt, reviewer)
        per_reviewer[reviewer] = findings
        all_findings.extend(findings)
        if "Reviewer call FAILED" in _txt or "[FALLBACK" in _txt.split("---")[0]:
            failed_reviewers.append(reviewer)

    # Group by consensus key
    grouped: dict[str, list[dict]] = defaultdict(list)
    for f in all_findings:
        key = consensus_key(f["text"])
        grouped[key].append(f)

    # Build report
    sev_order = ["ESSENTIAL", "FATAL", "BLOCKER", "MAJOR", "MINOR", "NIT", "UNKNOWN"]
    sev_rank = {s: i for i, s in enumerate(sev_order)}

    lines: list[str] = [
        f"# {paper_tag} {round_label} — v3 native-PDF cross-vendor SYNTHESIS",
        "",
        f"**Reviewers**: {', '.join(sorted(per_reviewer.keys()))}",
    ]
    if failed_reviewers:
        lines += [
            "",
            f"## ⛔ ROUND DEGRADED — reviewer leg(s) FAILED: {', '.join(failed_reviewers)}",
            "Failed legs are API errors, NOT zero-finding clean reviews. This round",
            "MUST NOT count toward any clean-round counter; re-run after the failure",
            "(e.g. API credit top-up) is resolved.",
        ]
    lines += [
        f"**Total findings (across all reviewers)**: {len(all_findings)}",
        f"**Distinct consensus groups**: {sum(1 for k in grouped if k != 'other') + (1 if 'other' in grouped else 0)}",
        "",
        "## Per-reviewer finding counts",
        "",
        "| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |",
        "|----------|-----------|-------|-------|-----|",
    ]
    for rv, fs in sorted(per_reviewer.items()):
        cnt: dict[str, int] = defaultdict(int)
        for f in fs:
            cnt[f["severity"]] += 1
        lines.append(
            f"| {rv} | {cnt.get('ESSENTIAL', 0) + cnt.get('FATAL', 0) + cnt.get('BLOCKER', 0)} | "
            f"{cnt.get('MAJOR', 0)} | {cnt.get('MINOR', 0)} | {cnt.get('NIT', 0)} |"
        )
    lines.extend(["", "---", ""])

    # Consensus-weighted findings
    lines.append("## Consensus-grouped findings (most reviewers first)")
    lines.append("")
    sorted_groups = sorted(
        grouped.items(),
        key=lambda kv: (
            -len({f["reviewer"] for f in kv[1]}),  # more reviewers = higher
            min((sev_rank.get(f["severity"], 99) for f in kv[1]), default=99),  # higher severity first
            kv[0],
        ),
    )
    for key, fs in sorted_groups:
        if key == "other":
            continue
        reviewers = sorted({f["reviewer"] for f in fs})
        max_sev = sev_order[min((sev_rank.get(f["severity"], 99) for f in fs))]
        consensus_tag = "**CONSENSUS**" if len(reviewers) >= 2 else "_single-reviewer_"
        lines.append(f"### `{key}` — {max_sev} — {consensus_tag} ({len(reviewers)} reviewer{'s' if len(reviewers) > 1 else ''})")
        lines.append("")
        lines.append(f"Reviewers: {', '.join(reviewers)}")
        lines.append("")
        for f in fs:
            snippet = f["text"][:600].replace("\n", " ")
            lines.append(f"- **[{f['reviewer']}/{f['id']}/{f['severity']}]**: {snippet}{'…' if len(f['text']) > 600 else ''}")
        lines.append("")

    if "other" in grouped:
        lines.append(f"## Other findings ({len(grouped['other'])})")
        lines.append("")
        for f in grouped["other"]:
            snippet = f["text"][:400].replace("\n", " ")
            lines.append(f"- **[{f['reviewer']}/{f['id']}/{f['severity']}]**: {snippet}{'…' if len(f['text']) > 400 else ''}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <round_label> <paper_tag>", file=sys.stderr)
        return 1
    round_label, paper_tag = sys.argv[1], sys.argv[2]
    report = synthesize(round_label, paper_tag)
    out = REVIEWS_DIR / f"{round_label}_{paper_tag}_SYNTHESIS.md"
    out.write_text(report)
    print(f"→ {out}", file=sys.stderr)
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
