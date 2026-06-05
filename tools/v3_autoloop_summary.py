#!/usr/bin/env python3
"""
v3 autoloop summary — produces the AUTOLOOP_LOG.md entry for one fire.

For each paper, computes:
  - Total findings in the new round
  - Consensus issues
  - NEW issues (appeared in new round, not in prev round)
  - DISAPPEARED (closed between rounds)

Aggregates cross-paper patterns: a "pattern candidate" is a consensus_key that
appears in 2+ papers in this round. Logged for Houston review.

Usage:
    python tools/v3_autoloop_summary.py <prev_round> <new_round>
"""
from __future__ import annotations

import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from v3_cross_round_diff import parse_round_findings, consensus_key

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"
LOG = REVIEWS_DIR / "AUTOLOOP_LOG.md"

PAPERS = ["P1A", "P1B", "P2", "P3", "P4", "P5"]


def main() -> int:
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <prev_round> <new_round>", file=sys.stderr)
        return 1

    prev_round = sys.argv[1]
    new_round = sys.argv[2]

    print(f"[autoloop-summary] {prev_round} → {new_round}", file=sys.stderr)

    cross_paper_patterns: dict = defaultdict(list)
    lines: list[str] = []
    lines.append("")
    lines.append(f"## Cross-round diff: `{prev_round}` → `{new_round}`")
    lines.append("")

    total_new_ess = 0
    for paper in PAPERS:
        prev = parse_round_findings(prev_round, paper)
        new = parse_round_findings(new_round, paper)
        prev_keys = set(prev.keys()) - {"other"}
        new_keys = set(new.keys()) - {"other"}
        appeared = new_keys - prev_keys
        disappeared = prev_keys - new_keys
        synth_path = REVIEWS_DIR / f"{new_round}_{paper}_SYNTHESIS.md"
        total_findings = 0
        consensus = 0
        if synth_path.exists():
            text = synth_path.read_text(errors="replace")
            for line in text.splitlines():
                if "Total findings" in line:
                    nums = [int(x) for x in line.split() if x.isdigit()]
                    if nums:
                        total_findings = nums[0]
            consensus = text.count("CONSENSUS")
        new_essentials = [k for k in appeared if any(
            "essential" in s.lower() for s in new[k]["snippets"]
        )]
        total_new_ess += len(new_essentials)
        lines.append(f"- **{paper}**: {total_findings} findings, {consensus} consensus | "
                     f"appeared={len(appeared)}, disappeared={len(disappeared)}, "
                     f"new ESSENTIAL={len(new_essentials)}")
        for k in sorted(new_essentials):
            lines.append(f"    + NEW ESS [{k}] caught by {len(new[k]['reviewers'])} reviewer(s)")
        for k in sorted(disappeared):
            lines.append(f"    - CLOSED [{k}] (was caught by {len(prev[k]['reviewers'])} prev)")
        # Add to cross-paper accumulator
        for k in new_keys:
            cross_paper_patterns[k].append(paper)

    lines.append("")
    lines.append("### Cross-paper pattern candidates (consensus key appearing in 2+ papers)")
    lines.append("")
    multi_paper_patterns = {k: papers for k, papers in cross_paper_patterns.items()
                            if len(papers) >= 2 and k != "other"}
    if multi_paper_patterns:
        for k, papers in sorted(multi_paper_patterns.items()):
            lines.append(f"- `{k}` → in {len(papers)} papers: {sorted(papers)}")
    else:
        lines.append("(none this round)")

    lines.append("")
    lines.append(f"**Total NEW ESSENTIAL across all 6 papers this round: {total_new_ess}**")
    lines.append("")
    lines.append("**Self-terminate condition**: 3 consecutive rounds with 0 new ESSENTIAL.")
    lines.append("")
    lines.append("---")

    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write("\n".join(lines))

    print("\n".join(lines))
    return 0 if total_new_ess == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
