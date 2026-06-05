#!/usr/bin/env python3
"""
v3 cross-round diff — find NEW findings between two rounds of the same paper.

For each paper, compare the consensus-grouped findings between an old round
and a new round, identifying:
  - findings that appear in the new round but were not in the old
  - findings that disappeared (likely closed by fixes between rounds)
  - findings where consensus weight changed

Usage:
    python tools/v3_cross_round_diff.py <old_round> <new_round> <paper_tag>
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"


# Re-use synthesis parser logic
SEV_HEADER_RE = re.compile(
    r"^#{0,4}\s*\**\s*(ESSENTIAL|MAJOR|MINOR|NIT|FATAL|BLOCKER)\b",
    re.IGNORECASE,
)
LEADING_ID_RE = re.compile(
    r"^(?:#{1,4}\s*)?\**\s*[Pp]?\d?[A-Z]?-?(?:META-)?([EBMmNnFf])(\d+)\b"
)
FINDING_ID_RE = re.compile(
    r"\b([Pp]?\d?[A-Z]?-?(?:META-)?[EBMmNnFf]\d+|B\d+|NIT\d+|N\d+)\b"
)


def consensus_key(text: str) -> str:
    """Heuristic key for cross-round identification."""
    keywords = []
    patterns = [
        (r"\bN[_ ]?MC\b.*\b500\b", "n_mc_500"),
        (r"\bsigma values?\b|\bσ values?\b", "sigma_mixing"),
        (r"\b[Tt]able\s+I[I]+\b", "table_ii"),
        (r"\b[Tt]able\s+IV\b", "table_iv"),
        (r"\b[Ii]ye\b", "iye_citation"),
        (r"\b[Ss]hamir\b", "shamir_citation"),
        (r"\bcompanion\b", "companion"),
        (r"\b[Cc]osmic variance\b", "cosmic_variance"),
        (r"\bNmap\b|\bN_map\b|\b[Ff]_sky\b", "weighting"),
        (r"\b28\.8\b|\b28\.32\b", "table_ii_sigma_arithmetic"),
        (r"\bFisher\b.*0\.29|\bFisher\b.*0\.167", "fisher_floor"),
        (r"\bz.*1\.68\b|\bz.*1\.57\b", "table_iv_z"),
        (r"\b67\.6%?\b.*CE-?ResNet|\blabel noise\b", "label_noise"),
        (r"\bpage count\b|\btoo long\b|\bcondense\b|\bshorten\b", "length"),
        (r"\bversion[- ]history\b|\bsuperseded\b", "audit_artifact"),
        (r"\bcanonical canonical\b|\bduplicate phrase\b", "duplicate_phrase"),
        (r"\bfuture date\b|\bDated.*202\d", "future_date"),
        (r"\bT-Web\b|\bV-Web\b", "tweb_vweb"),
        (r"\b234,?282\b|\b240,?919\b", "gz1_stale_n"),
        (r"\b0\.398\b|\b0\.63\b.*[Dd]ilution|\b2a-1\b", "dilution_factor"),
        (r"\bfsky\b.*\bnon-?binary\b|\bfsky.*weighted\b|\beffective fsky\b", "fsky_effective"),
        (r"\bdeduplication\b|\bdedup\b|\bduplicat\w+\s+catalog", "dedup_audit"),
    ]
    for kw_re, label in patterns:
        if re.search(kw_re, text, re.IGNORECASE):
            keywords.append(label)
    return ",".join(keywords) if keywords else "other"


def parse_round_findings(round_label: str, paper_tag: str) -> dict:
    """Parse all reviewer files for (round, paper) → consensus-keyed findings."""
    pattern = f"{round_label}_{paper_tag}_*.md"
    files = sorted(REVIEWS_DIR.glob(pattern))
    by_key: dict = defaultdict(lambda: {"reviewers": set(), "ids": set(), "snippets": []})
    for p in files:
        name = p.name.lower()
        if "synthesis" in name or "meta_review" in name:
            continue
        reviewer = p.stem.split("_", 2)[2] if "_" in p.stem else p.stem
        text = p.read_text(errors="replace")
        cur_id = None
        cur_block: list[str] = []
        for line in text.splitlines():
            s = line.strip()
            m_lead = LEADING_ID_RE.match(s)
            if m_lead:
                if cur_id and cur_block:
                    block_text = "\n".join(cur_block)
                    key = consensus_key(block_text)
                    by_key[key]["reviewers"].add(reviewer)
                    by_key[key]["ids"].add(f"{reviewer}/{cur_id}")
                    by_key[key]["snippets"].append(block_text[:500])
                cur_block = []
                cur_id = None
                full_id = FINDING_ID_RE.search(s)
                if full_id:
                    cur_id = full_id.group(1)
            if cur_id:
                cur_block.append(line)
        if cur_id and cur_block:
            block_text = "\n".join(cur_block)
            key = consensus_key(block_text)
            by_key[key]["reviewers"].add(reviewer)
            by_key[key]["ids"].add(f"{reviewer}/{cur_id}")
            by_key[key]["snippets"].append(block_text[:500])
    return dict(by_key)


def main() -> int:
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <old_round> <new_round> <paper_tag>", file=sys.stderr)
        return 1
    old_round, new_round, paper = sys.argv[1], sys.argv[2], sys.argv[3]
    old = parse_round_findings(old_round, paper)
    new = parse_round_findings(new_round, paper)

    old_keys = set(old.keys()) - {"other"}
    new_keys = set(new.keys()) - {"other"}

    appeared = new_keys - old_keys
    disappeared = old_keys - new_keys
    persisted = old_keys & new_keys

    print(f"# {paper} cross-round diff: {old_round} → {new_round}")
    print(f"  old non-other keys: {len(old_keys)}")
    print(f"  new non-other keys: {len(new_keys)}")
    print(f"  APPEARED (new round, not in old): {len(appeared)}")
    for k in sorted(appeared):
        n_rev = len(new[k]["reviewers"])
        print(f"    + {k}  ({n_rev} reviewer{'s' if n_rev > 1 else ''})")
    print(f"  DISAPPEARED (in old, not in new — likely closed): {len(disappeared)}")
    for k in sorted(disappeared):
        n_rev = len(old[k]["reviewers"])
        print(f"    - {k}  (was caught by {n_rev} reviewer{'s' if n_rev > 1 else ''})")
    print(f"  PERSISTED (in both rounds): {len(persisted)}")
    for k in sorted(persisted):
        old_n = len(old[k]["reviewers"])
        new_n = len(new[k]["reviewers"])
        delta = new_n - old_n
        arrow = "▲" if delta > 0 else ("▼" if delta < 0 else "=")
        print(f"    {arrow} {k}  {old_n} → {new_n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
