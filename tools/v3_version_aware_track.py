#!/usr/bin/env python3
"""
v3 version-aware tracker — ties review findings to specific paper versions.

For each autoloop fire, identify:
  - What paperVersion the PDF was reviewed at
  - What changed between version N and N+1
  - Which findings were CLOSED across the version bump

Output: project-context/peer-reviews/PAPER_VERSION_TIMELINE.md

Usage:
    python tools/v3_version_aware_track.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from v3_persistence_tracker import discover_rounds, parse_meta_findings, fingerprint
from v3_cross_round_diff import parse_round_findings

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"

PAPER_TEX_PATHS = {
    "P1A": "arxiv/paper1a_ech_nogo.tex",
    "P1B": "arxiv/paper1b_mcmc_companion.tex",
    "P2": "research/focused_paper_source_integration/02_full_draft.tex",
    "P3": "pipelines/p3_anomaly_engine/paper3_draft.tex",
    "P4": "pipelines/p2_chirality/chirality_catalog_paper.tex",
    "P5": "pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex",
}

PAPERS = list(PAPER_TEX_PATHS.keys())


def parse_paper_version(tex_path: Path) -> str:
    """Extract \\paperVersion{...} value."""
    if not tex_path.exists():
        return "?"
    text = tex_path.read_text(errors="replace")
    m = re.search(r"\\newcommand\{\\paperVersion\}\{([^}]+)\}", text)
    return m.group(1) if m else "?"


def round_timestamp(round_label: str) -> str:
    """Convert auto-2026-06-05_1418pt → 2026-06-05 14:18."""
    m = re.match(r"auto-(\d{4}-\d{2}-\d{2})_(\d{2})(\d{2})pt", round_label)
    if m:
        return f"{m.group(1)} {m.group(2)}:{m.group(3)}"
    return round_label


def git_log_for_paper_between(tex_rel: str, from_round: str, to_round: str) -> list[dict]:
    """List commits touching the .tex file between two rounds.

    Approximation: use the round timestamps as proxies for commit-time bounds.
    """
    m1 = re.match(r"auto-(\d{4}-\d{2}-\d{2})_(\d{2})(\d{2})pt", from_round)
    m2 = re.match(r"auto-(\d{4}-\d{2}-\d{2})_(\d{2})(\d{2})pt", to_round)
    if not m1 or not m2:
        return []
    since = f"{m1.group(1)} {m1.group(2)}:{m1.group(3)}"
    until = f"{m2.group(1)} {m2.group(2)}:{m2.group(3)}"
    try:
        result = subprocess.run(
            ["git", "log", f"--since={since}", f"--until={until}", "--oneline", "--", tex_rel],
            capture_output=True, text=True, cwd=REPO, timeout=30,
        )
        if result.returncode != 0:
            return []
        commits = []
        for line in result.stdout.strip().splitlines():
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                commits.append({"sha": parts[0], "subject": parts[1]})
        return commits
    except Exception:
        return []


def build_report() -> str:
    rounds = discover_rounds()
    if not rounds:
        return "# No autoloop rounds yet\n"

    out = ["# Paper Version Timeline", ""]
    out.append("Cross-fire view of which paper versions were reviewed, what changed")
    out.append("between rounds, and which findings closed across each bump.")
    out.append("")

    # Current version per paper
    out.append("## Current paper versions")
    out.append("")
    out.append("| Paper | Version | .tex path |")
    out.append("|---|---|---|")
    for paper, rel in PAPER_TEX_PATHS.items():
        tex = REPO / rel
        version = parse_paper_version(tex)
        out.append(f"| {paper} | `{version}` | `{rel}` |")
    out.append("")

    # Round-over-round diff
    out.append("## Round-over-round changes per paper")
    out.append("")
    for paper in PAPERS:
        out.append(f"### {paper}")
        out.append("")
        out.append("| Round | Time | Closed | Commits since prev round |")
        out.append("|---|---|---|---|")
        prev_round = None
        for r in rounds:
            ts = round_timestamp(r)
            closed_count = 0
            commits_str = ""
            if prev_round is not None:
                prev_keys = set(parse_round_findings(prev_round, paper).keys()) - {"other"}
                new_keys = set(parse_round_findings(r, paper).keys()) - {"other"}
                closed_count = len(prev_keys - new_keys)
                commits = git_log_for_paper_between(PAPER_TEX_PATHS[paper], prev_round, r)
                if commits:
                    commits_str = "; ".join(
                        f"`{c['sha']}` {c['subject'][:60]}" for c in commits[:3]
                    )
                else:
                    commits_str = "(no .tex commits in window)"
            out.append(f"| `{r}` | {ts} | {closed_count} | {commits_str} |")
            prev_round = r
        out.append("")

    return "\n".join(out)


def main() -> int:
    report = build_report()
    out_path = REVIEWS_DIR / "PAPER_VERSION_TIMELINE.md"
    out_path.write_text(report)
    print(f"→ {out_path}", file=sys.stderr)
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
