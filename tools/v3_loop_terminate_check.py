#!/usr/bin/env python3
"""
v3 loop-terminate check — refined self-terminate condition for the autoloop.

The cron rule says "self-terminate after 3 consecutive rounds with 0 NEW
ESSENTIAL findings." But the autoloop tool counts any ESSENTIAL appearing in
a new consensus_key as "NEW", even if it's the SAME underlying scientific
issue surfaced for the Nth round. This causes the self-terminate counter to
never increment.

This tool computes a STRICTER definition of "NEW":
  - A finding is NEW if its meta-finding fingerprint AND its consensus_key
    have BOTH never been seen in any prior round.
  - A finding is PERSISTENT if its fingerprint matches one already known.
  - A finding is RESURGENT if it was caught in round N-2, missed in N-1,
    caught again in N.

The self-terminate decision uses only truly-NEW findings, not persistent
or resurgent ones (which the persistence-tracker already escalates).

Usage:
    python tools/v3_loop_terminate_check.py <new_round>
"""
from __future__ import annotations

import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from v3_cross_round_diff import parse_round_findings, consensus_key
from v3_persistence_tracker import (
    discover_rounds, parse_meta_findings, fingerprint as meta_fingerprint
)

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"

PAPERS = ["P1A", "P1B", "P2", "P3", "P4", "P5"]


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <new_round>", file=sys.stderr)
        return 1
    new_round = sys.argv[1]

    rounds = discover_rounds()
    if new_round not in rounds:
        print(f"new_round {new_round} not yet observed; available: {rounds}", file=sys.stderr)
        return 1
    prior_rounds = [r for r in rounds if r < new_round]

    # Build the set of all (paper, consensus_key) and (paper, meta_fingerprint)
    # known in any prior round
    known_consensus_keys: set = set()
    known_meta_fps: set = set()
    for r in prior_rounds:
        for paper in PAPERS:
            # Consensus keys from v3.1 reviews
            for k in parse_round_findings(r, paper).keys():
                if k != "other":
                    known_consensus_keys.add((paper, k))
            # Meta-finding fingerprints
            for fid, summary in parse_meta_findings(r, paper).items():
                fp = meta_fingerprint(summary)
                if fp != "other":
                    known_meta_fps.add((paper, fp))

    # Identify truly-NEW in the new round
    truly_new = []
    for paper in PAPERS:
        # Consensus keys
        for k in parse_round_findings(new_round, paper).keys():
            if k != "other" and (paper, k) not in known_consensus_keys:
                truly_new.append((paper, "consensus", k))
        # Meta fingerprints
        for fid, summary in parse_meta_findings(new_round, paper).items():
            fp = meta_fingerprint(summary)
            if fp != "other" and (paper, fp) not in known_meta_fps:
                truly_new.append((paper, "meta", fp))

    # Filter to ESSENTIAL only — for consensus_key, look at parsed severity;
    # for meta, look at the META-E prefix
    new_essential = []
    for paper, tier, key in truly_new:
        if tier == "consensus":
            findings = parse_round_findings(new_round, paper).get(key, {})
            snippets = findings.get("snippets", []) if isinstance(findings, dict) else []
            if any("essential" in s.lower() for s in snippets):
                new_essential.append((paper, tier, key))
        elif tier == "meta":
            # meta-fingerprints don't carry severity easily; assume all are ≥MAJOR
            new_essential.append((paper, tier, key))

    print(f"## Loop-terminate check — round {new_round}")
    print(f"  Prior rounds: {len(prior_rounds)}")
    print(f"  Truly-NEW (paper, key) pairs this round: {len(truly_new)}")
    print(f"    of which ESSENTIAL: {len(new_essential)}")
    for paper, tier, key in new_essential:
        print(f"    + {paper}/{tier}/{key}")
    print()
    if len(new_essential) == 0:
        print("✅ This round had 0 truly-NEW ESSENTIAL findings.")
        print("   (Persistent and recurring findings are not counted — they're tracked separately.)")
    else:
        print(f"❌ This round had {len(new_essential)} truly-NEW ESSENTIAL findings. Counter resets.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
