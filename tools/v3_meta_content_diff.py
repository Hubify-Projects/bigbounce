#!/usr/bin/env python3
"""
Detect NEW ESSENTIAL META findings between two autoloop rounds, based on
problem-text content overlap rather than coarse keyword fingerprinting.

This addresses the failure mode caught in fire 13 (2026-06-08): persistence_tracker
uses a fixed single-word keyword set, so two completely unrelated P4 findings
that both mention "master" get fingerprinted identically and the tracker
reports false "0 NEW" results.

This script extracts the actual problem text per ESS finding and compares
across rounds via 5-gram Jaccard similarity. Two findings are "same issue"
iff their 5-gram Jaccard ≥ 0.30 on the normalized problem prose. Findings
in the new round with no near-match in the old round are flagged NEW.

Usage:
    python tools/v3_meta_content_diff.py <old_round> <new_round> [--threshold 0.30]

Example:
    python tools/v3_meta_content_diff.py auto-2026-06-08_1354pt auto-2026-06-08_1517pt

Output (stdout):
    Per-paper:
      - count of ESS in old + new
      - list of NEW ESS findings (with truncated quote)
      - list of CLOSED ESS findings (in old but not new)
      - list of RECURRING ESS findings (matched across rounds)

Exit code: number of papers with NEW ESS findings (0 = all matched =
autoloop converged for self-terminate purposes).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS = REPO / "project-context" / "peer-reviews"
PAPERS = ["P1A", "P1B", "P2", "P3", "P4", "P5"]

# Match BOTH formats: "- Severity: ESSENTIAL" and "Severity: ESSENTIAL"
SEV_RE = re.compile(r"^[\s-]*Severity:\s*ESSENTIAL\s*$", re.MULTILINE)

# A finding "block" starts at a Severity: ESSENTIAL line and ends at
# the next blank-line-then-non-blank or at the next Severity/Required-fix
# boundary. We collect lines until the next Severity: line OR until the
# blank-line-followed-by-empty-line transition.
def extract_ess_findings(text: str) -> list[dict]:
    """
    Return a list of {id, section, problem, fix} dicts for every
    Severity: ESSENTIAL block in the META file.
    """
    findings = []
    lines = text.splitlines()
    cur = None
    # Identify ESS block boundaries by Severity: lines
    sev_indices = [i for i, ln in enumerate(lines)
                   if SEV_RE.match(ln) or re.match(r"^[\s-]*Severity:\s*(ESSENTIAL|MAJOR|MINOR|NIT|FATAL|BLOCKER)\s*$", ln)]
    for k, idx in enumerate(sev_indices):
        sev_line = lines[idx].strip().rstrip(":").lower()
        if "essential" not in sev_line:
            continue
        # Block end: next Severity line OR EOF
        end = sev_indices[k + 1] if k + 1 < len(sev_indices) else len(lines)
        # ID candidate: line above the Severity (usually a header line with the ID)
        id_line = ""
        for j in range(max(0, idx - 3), idx):
            l = lines[j].strip().lstrip("-").strip()
            if re.search(r"\b[PR]\d?[A-Z]?-?META-?[EBMNm]\d+\b", l):
                id_line = re.search(r"\b[PR]\d?[A-Z]?-?META-?[EBMNm]\d+\b", l).group(0)
                break
        # Problem text: everything from "Problem" line down to "Required fix"
        block = lines[idx:end]
        problem = []
        in_prob = False
        for ln in block:
            ln_lower = ln.strip().lower().lstrip("-").strip()
            if ln_lower.startswith("problem") or ln_lower.startswith("specific problem"):
                in_prob = True
                # collect text after the colon
                after = ln.split(":", 1)[1].strip() if ":" in ln else ""
                if after:
                    problem.append(after)
                continue
            if in_prob and (ln_lower.startswith("required fix") or ln_lower.startswith("section") or ln_lower.startswith("location")):
                break
            if in_prob:
                problem.append(ln.strip())
        findings.append({
            "id": id_line,
            "problem": " ".join(problem).strip(),
            "raw_block": "\n".join(block[:25]),
        })
    return findings


def normalize(text: str) -> str:
    """Lowercase + strip latex/markdown symbols + collapse whitespace."""
    t = text.lower()
    # Strip latex/markdown noise that distracts from semantic match
    t = re.sub(r"\$[^$]*\$", " ", t)  # inline math
    t = re.sub(r"\\[a-z]+", " ", t)    # latex commands
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def ngrams(text: str, n: int = 5) -> set:
    """Return word-level n-gram set."""
    words = text.split()
    if len(words) < n:
        return set([" ".join(words)])
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def match_findings(old: list[dict], new: list[dict], threshold: float) -> tuple:
    """
    For each new finding, find the best-match old finding by 5-gram Jaccard.
    Return (matched, new_only, closed).
    """
    new_ngrams = [ngrams(normalize(f["problem"])) for f in new]
    old_ngrams = [ngrams(normalize(f["problem"])) for f in old]

    matched = []
    new_only = []
    matched_old_idxs = set()

    for ni, nf in enumerate(new):
        best_sim = 0.0
        best_oi = -1
        for oi, of in enumerate(old):
            sim = jaccard(new_ngrams[ni], old_ngrams[oi])
            if sim > best_sim:
                best_sim = sim
                best_oi = oi
        if best_sim >= threshold and best_oi >= 0:
            matched.append((nf, old[best_oi], best_sim))
            matched_old_idxs.add(best_oi)
        else:
            new_only.append((nf, best_sim))

    closed = [old[oi] for oi in range(len(old)) if oi not in matched_old_idxs]
    return matched, new_only, closed


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    old_round = sys.argv[1]
    new_round = sys.argv[2]
    threshold = 0.30
    for a in sys.argv[3:]:
        if a.startswith("--threshold"):
            threshold = float(a.split("=", 1)[1]) if "=" in a else float(sys.argv[sys.argv.index(a) + 1])

    papers_with_new = 0
    overall_summary = []

    for paper in PAPERS:
        old_file = REVIEWS / f"{old_round}_{paper}_META_REVIEW.md"
        new_file = REVIEWS / f"{new_round}_{paper}_META_REVIEW.md"
        if not old_file.exists():
            print(f"[{paper}] missing old META file: {old_file.name}")
            continue
        if not new_file.exists():
            print(f"[{paper}] missing new META file: {new_file.name}")
            continue
        old_ess = extract_ess_findings(old_file.read_text())
        new_ess = extract_ess_findings(new_file.read_text())
        matched, new_only, closed = match_findings(old_ess, new_ess, threshold)
        if new_only:
            papers_with_new += 1
        overall_summary.append((paper, len(old_ess), len(new_ess), len(matched), len(new_only), len(closed)))

        print(f"\n## {paper}: old={len(old_ess)} ESS / new={len(new_ess)} ESS")
        print(f"  matched (recurring): {len(matched)}")
        print(f"  NEW in this round:   {len(new_only)}")
        print(f"  closed (in old only): {len(closed)}")
        for nf, sim in new_only:
            preview = nf["problem"][:200].replace("\n", " ")
            print(f"  🔴 NEW [{nf['id'] or '?'}] (best_sim={sim:.2f}): {preview}")
        for of in closed:
            preview = of["problem"][:120].replace("\n", " ")
            print(f"  🟢 CLOSED [{of['id'] or '?'}]: {preview}")

    print(f"\n=== TOTAL ===")
    total_old = sum(s[1] for s in overall_summary)
    total_new = sum(s[2] for s in overall_summary)
    total_new_only = sum(s[4] for s in overall_summary)
    total_closed = sum(s[5] for s in overall_summary)
    print(f"  old ESS = {total_old}, new ESS = {total_new}")
    print(f"  NEW = {total_new_only}, RECURRING = {sum(s[3] for s in overall_summary)}, CLOSED = {total_closed}")
    print(f"  papers with NEW ESS findings: {papers_with_new} / 6")

    # exit code = papers with new findings (0 = converged)
    sys.exit(papers_with_new)


if __name__ == "__main__":
    main()
