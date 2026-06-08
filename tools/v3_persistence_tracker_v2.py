#!/usr/bin/env python3
"""
v2 persistence-tracker — content-overlap fingerprinting instead of keyword overlap.

Fixes the failure mode of `v3_persistence_tracker.py` (the v1, with fixed
single-word keywords like `master`, `binomial`, `table_ii`):

  - v1 reported "0 NEW fingerprints" for fires 11+12+13 even though content
    audit of fire 13 revealed 12+ genuinely-new substantive findings, because
    every P4 finding mentioning "master" was tagged with the same fingerprint
    regardless of the actual issue. See AUTOLOOP_IMPROVEMENTS.md 2026-06-08
    fire-13 entry for the full failure mode.

v2 approach:
  - For each META finding across all rounds, extract problem text.
  - Build a 5-gram set (normalized, latex-stripped, lowercased).
  - For each finding, find its content cluster across all rounds by
    transitive Jaccard >= threshold (default 0.30).
  - Report:
      LOAD-BEARING: clusters with members in >=3 rounds (any paper).
      RECURRING: clusters with members in 2 rounds.
      NEW (this round): clusters with members in only the most recent round.

Compatible with the same input filenames as v1 (auto-*_<paper>_META_REVIEW.md).
Writes a v2 report to project-context/peer-reviews/PERSISTENT_FINDINGS_v2.md.

Usage:
    python tools/v3_persistence_tracker_v2.py [--threshold 0.30]

Exit code = number of clusters that are NEW-this-round AND severity ESSENTIAL
(0 = no new ESS, candidate for self-terminate counter advance).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS = REPO / "project-context" / "peer-reviews"
PAPERS = ["P1A", "P1B", "P2", "P3", "P4", "P5"]
OUT = REVIEWS / "PERSISTENT_FINDINGS_v2.md"

# Match both META format variants: "- Severity: X" and "Severity: X"
SEV_RE = re.compile(
    r"^[\s-]*Severity:\s*(ESSENTIAL|MAJOR|MINOR|NIT|FATAL|BLOCKER)\s*$",
    re.MULTILINE,
)


def find_rounds() -> list[str]:
    """Return sorted unique round labels from auto-*_META_REVIEW.md files."""
    rounds = set()
    for f in REVIEWS.glob("auto-*_META_REVIEW.md"):
        m = re.match(r"(auto-[\d_pt-]+)_P[\w\d]+_META_REVIEW\.md", f.name)
        if m:
            rounds.add(m.group(1))
    return sorted(rounds)


def extract_findings(text: str, round_label: str, paper: str) -> list[dict]:
    """Extract every Severity-tagged block. Returns list of dicts."""
    lines = text.splitlines()
    sev_indices = [(i, m) for i, ln in enumerate(lines)
                   if (m := SEV_RE.match(ln))]
    findings = []
    for k, (idx, m) in enumerate(sev_indices):
        sev = m.group(1).upper()
        end = sev_indices[k + 1][0] if k + 1 < len(sev_indices) else len(lines)
        block = lines[idx:end]
        id_str = ""
        for j in range(max(0, idx - 3), idx):
            l = lines[j].strip().lstrip("-").strip()
            mm = re.search(r"\b[PR]\d?[A-Z]?-?META-?[EBMNmn]\d+\b", l)
            if mm:
                id_str = mm.group(0)
                break
        problem = []
        in_prob = False
        for ln in block:
            l = ln.strip().lower().lstrip("-").strip()
            if l.startswith("problem") or l.startswith("specific problem"):
                in_prob = True
                after = ln.split(":", 1)[1].strip() if ":" in ln else ""
                if after:
                    problem.append(after)
                continue
            if in_prob and (l.startswith("required fix") or l.startswith("section") or l.startswith("location")):
                break
            if in_prob:
                problem.append(ln.strip())
        findings.append({
            "id": id_str,
            "severity": sev,
            "paper": paper,
            "round": round_label,
            "problem": " ".join(problem).strip(),
        })
    return findings


def normalize(text: str) -> str:
    t = text.lower()
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\\[a-z]+", " ", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def ngrams(text: str, n: int = 5) -> set:
    words = text.split()
    if len(words) < n:
        return set([" ".join(words)]) if words else set()
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def cluster_findings(findings: list[dict], threshold: float) -> list[list[int]]:
    n = len(findings)
    ng = [ngrams(normalize(f["problem"])) for f in findings]
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    by_paper = defaultdict(list)
    for i, f in enumerate(findings):
        by_paper[f["paper"]].append(i)

    for paper, idxs in by_paper.items():
        for ii in range(len(idxs)):
            for jj in range(ii + 1, len(idxs)):
                i, j = idxs[ii], idxs[jj]
                if jaccard(ng[i], ng[j]) >= threshold:
                    union(i, j)

    clusters_map = defaultdict(list)
    for i in range(n):
        clusters_map[find(i)].append(i)
    return list(clusters_map.values())


def main():
    threshold = 0.30
    if "--threshold" in sys.argv:
        idx = sys.argv.index("--threshold")
        if idx + 1 < len(sys.argv):
            threshold = float(sys.argv[idx + 1])

    rounds = find_rounds()
    print(f"[v2-tracker] {len(rounds)} round(s): {rounds}", file=sys.stderr)

    all_findings = []
    for r in rounds:
        for paper in PAPERS:
            f = REVIEWS / f"{r}_{paper}_META_REVIEW.md"
            if f.exists():
                all_findings.extend(extract_findings(f.read_text(), r, paper))

    print(f"[v2-tracker] {len(all_findings)} total META findings", file=sys.stderr)

    clusters = cluster_findings(all_findings, threshold)
    print(f"[v2-tracker] {len(clusters)} content-clusters at threshold {threshold}",
          file=sys.stderr)

    latest_round = rounds[-1] if rounds else ""
    cluster_meta = []
    for cl in clusters:
        members = [all_findings[i] for i in cl]
        rounds_in = sorted({m["round"] for m in members})
        papers_in = sorted({m["paper"] for m in members})
        severities = {m["severity"] for m in members}
        top_sev = "ESSENTIAL" if "ESSENTIAL" in severities else \
                  "MAJOR" if "MAJOR" in severities else \
                  "MINOR" if "MINOR" in severities else "NIT"
        cluster_meta.append({
            "members": members,
            "rounds": rounds_in,
            "papers": papers_in,
            "severity": top_sev,
            "is_new_this_round": rounds_in == [latest_round],
            "is_load_bearing": len(rounds_in) >= 3,
            "is_recurring": len(rounds_in) == 2,
        })

    cluster_meta.sort(key=lambda c: (-len(c["rounds"]), -len(c["members"])))

    out_lines = [
        "# Persistent Meta-Findings Tracker v2",
        "",
        f"Tracking META findings across {len(rounds)} autoloop fires using",
        f"content-overlap fingerprinting (5-gram Jaccard >= {threshold}).",
        "",
        f"Total META findings: {len(all_findings)}",
        f"Distinct content-clusters: {len(clusters)}",
        f"Latest round: {latest_round}",
        "",
        "## LOAD-BEARING (>=3 rounds)",
        "",
    ]

    lb = [c for c in cluster_meta if c["is_load_bearing"]]
    for c in lb:
        ex = c["members"][0]
        out_lines.append(f"### LB {c['severity']} {ex['paper']} - {len(c['rounds'])}/{len(rounds)} rounds")
        out_lines.append(f"Rounds: {c['rounds']}")
        out_lines.append(f"Member IDs: {[m['id'] for m in c['members'] if m['id']]}")
        out_lines.append(f"Example (round {ex['round']}, {ex['id']}):")
        out_lines.append(f"> {ex['problem'][:250]}...")
        out_lines.append("")

    out_lines.append("## RECURRING (2 rounds)\n")
    rec = [c for c in cluster_meta if c["is_recurring"]]
    for c in rec[:15]:
        ex = c["members"][0]
        out_lines.append(f"### REC {c['severity']} {ex['paper']} - 2/{len(rounds)} rounds")
        out_lines.append(f"Rounds: {c['rounds']}")
        out_lines.append(f"Example: {ex['problem'][:200]}...")
        out_lines.append("")

    new_this = [c for c in cluster_meta if c["is_new_this_round"]]
    new_ess = [c for c in new_this if c["severity"] == "ESSENTIAL"]
    out_lines.append(f"## NEW this round ({latest_round}) - {len(new_this)} clusters\n")
    out_lines.append(f"- NEW ESSENTIAL: **{len(new_ess)}**")
    out_lines.append(f"- NEW MAJOR: {sum(1 for c in new_this if c['severity']=='MAJOR')}")
    out_lines.append(f"- NEW MINOR/NIT: {sum(1 for c in new_this if c['severity'] in ('MINOR','NIT'))}\n")

    for c in new_ess:
        ex = c["members"][0]
        out_lines.append(f"### NEW ESS {ex['paper']} - {ex['id']}")
        out_lines.append(f"> {ex['problem'][:250]}...")
        out_lines.append("")

    OUT.write_text("\n".join(out_lines))
    print(f"-> {OUT}", file=sys.stderr)
    print("\n".join(out_lines[:60]))

    sys.exit(len(new_ess))


if __name__ == "__main__":
    main()
