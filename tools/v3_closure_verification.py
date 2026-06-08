#!/usr/bin/env python3
"""
v3 closure-verification — for each shipped paper-fix, check whether the
META finding that motivated the fix re-fires in subsequent rounds.

If a closure was effective: the META finding shouldn't re-fire (its content
shouldn't appear in subsequent rounds' META files).

If a closure was insufficient: the META finding re-fires → we know the .tex
edit didn't actually resolve the underlying issue.

Tracks named closures by anchor-text (a short distinctive phrase from the
original META finding). For each closure, scans all rounds AFTER the closure
fire and reports re-firings.

Input: a JSON ledger of closure entries, each with:
  - closure_id (e.g., "P3-META-E4-fire-14-closure")
  - closure_commit (git short hash)
  - closure_fire_round (the round the closure was committed FROM)
  - paper (P1A/P1B/P2/P3/P4/P5)
  - anchor_phrases (list of distinctive phrases — closure considered "leaked"
    if any anchor appears in a META finding in a subsequent round)

Usage:
    python tools/v3_closure_verification.py [--ledger PATH]

Default ledger: project-context/peer-reviews/CLOSURE_LEDGER.json
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS = REPO / "project-context" / "peer-reviews"
DEFAULT_LEDGER = REVIEWS / "CLOSURE_LEDGER.json"


def find_rounds_after(closure_round: str) -> list[str]:
    """Return sorted round labels strictly after `closure_round`."""
    rounds = set()
    for f in REVIEWS.glob("auto-*_META_REVIEW.md"):
        m = re.match(r"(auto-[\d_pt-]+)_P[\w\d]+_META_REVIEW\.md", f.name)
        if m:
            rounds.add(m.group(1))
    return sorted(r for r in rounds if r > closure_round)


def check_anchor_in_round(anchor: str, paper: str, round_label: str) -> bool:
    """Return True if `anchor` substring (case-insensitive) appears in the
    META file for `paper` in `round_label`."""
    f = REVIEWS / f"{round_label}_{paper}_META_REVIEW.md"
    if not f.exists():
        return False
    text = f.read_text().lower()
    return anchor.lower() in text


def main():
    ledger_path = DEFAULT_LEDGER
    for i, a in enumerate(sys.argv):
        if a == "--ledger" and i + 1 < len(sys.argv):
            ledger_path = Path(sys.argv[i + 1])

    if not ledger_path.exists():
        # Bootstrap with the 3 TIER A2 closures from fire 14
        bootstrap = [
            {
                "closure_id": "P3-META-E4-fire-14",
                "closure_commit": "b90f0c8d",
                "closure_fire_round": "auto-2026-06-08_1424pt",
                "paper": "P3",
                "anchor_phrases": [
                    "Gaussian summary is inconsistent with the quoted 68% interval width",
                    "0.382",
                    "CI width is 0.578",
                ],
                "description": "γ ± 0.382 vs CI [2.304, 2.882] arithmetic inconsistency",
            },
            {
                "closure_id": "P5-META-E1-fire-14",
                "closure_commit": "b90f0c8d",
                "closure_fire_round": "auto-2026-06-08_1424pt",
                "paper": "P5",
                "anchor_phrases": [
                    "two incompatible",
                    "1.98 percentage points",
                    "range",
                ],
                "description": "P5 canonical-config range cross-section contradiction",
            },
            {
                "closure_id": "P1B-META-E1-fire-14",
                "closure_commit": "b90f0c8d",
                "closure_fire_round": "auto-2026-06-08_1424pt",
                "paper": "P1B",
                "anchor_phrases": [
                    "0.336",
                    "Caγ = 8",
                    "much less than 0.336",
                ],
                "description": "βALP=0.336° exceeds formula bound at fixed C_aγ=8",
            },
        ]
        ledger_path.write_text(json.dumps(bootstrap, indent=2))
        print(f"Bootstrapped ledger with 3 TIER A2 closures at {ledger_path}",
              file=sys.stderr)

    ledger = json.loads(ledger_path.read_text())
    print(f"## Closure verification — {len(ledger)} tracked closures\n")

    re_fired_count = 0
    for c in ledger:
        rounds_after = find_rounds_after(c["closure_fire_round"])
        print(f"### {c['closure_id']}: {c['description']}")
        print(f"  closure_commit: {c['closure_commit']}; closed_after: {c['closure_fire_round']}")
        print(f"  paper: {c['paper']}; rounds since closure: {len(rounds_after)}")

        re_firings = []
        for r in rounds_after:
            for anchor in c["anchor_phrases"]:
                if check_anchor_in_round(anchor, c["paper"], r):
                    re_firings.append((r, anchor))
                    break  # one anchor hit per round is enough
        if re_firings:
            re_fired_count += 1
            print(f"  ⚠️  RE-FIRED in {len(re_firings)} round(s):")
            for r, a in re_firings:
                print(f"      {r}: anchor '{a[:60]}'")
        else:
            print(f"  ✅ STUCK — anchors not present in any round after closure.")
        print()

    print(f"--- SUMMARY ---")
    print(f"Total closures tracked: {len(ledger)}")
    print(f"Closures that RE-FIRED: {re_fired_count}")
    print(f"Closures STUCK: {len(ledger) - re_fired_count}")
    sys.exit(re_fired_count)


if __name__ == "__main__":
    main()
