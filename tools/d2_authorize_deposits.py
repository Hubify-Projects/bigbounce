#!/usr/bin/env python3
"""Apply Houston's D2 license decision to the fail-closed deposit configs.

Usage:
    python3 tools/d2_authorize_deposits.py cc-by-4.0 \
        --authorized-by "Houston, 2026-07-2X, chat" [--papers P1A,P1B,P5]

For each gated paper this sets ``metadata.license`` and rewrites the
fail-closed blocker to only the conditions that remain AFTER the license
decision:

- P1A: license was the only blocker -> metadata_complete becomes true.
- P1B: still requires the namaster-proof 0.1.7 software archive DOI. Pass
  ``--p1b-software-doi 10.5281/zenodo.XXXX`` once minted to clear it and
  record the DOI as a related identifier.
- P5:  still gated on the Paper-IV (P4 arXiv ID) back-patch; the blocker is
  reduced to that condition only.

Dry-run by default; ``--write`` edits tools/paper_deposit_config.json.
This script never contacts Zenodo. It refuses to run without
``--authorized-by`` naming Houston and a date, because the license choice is
his decision (D2), not the agent's.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CONFIG = Path(__file__).with_name("paper_deposit_config.json")
KNOWN_LICENSES = {"cc-by-4.0", "cc-by-sa-4.0", "cc-by-nc-4.0", "cc0-1.0", "mit", "arxiv-nonexclusive"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("license", help="Zenodo license id, e.g. cc-by-4.0")
    ap.add_argument("--papers", default="P1A,P1B,P5")
    ap.add_argument("--authorized-by", required=True,
                    help='provenance stamp, e.g. "Houston, 2026-07-21, chat"')
    ap.add_argument("--p1b-software-doi", default="",
                    help="namaster-proof 0.1.7 Zenodo DOI once minted")
    ap.add_argument("--write", action="store_true", help="apply (default: dry-run)")
    args = ap.parse_args()

    lic = args.license.strip().lower()
    if lic not in KNOWN_LICENSES:
        print(f"FAIL: unrecognized license id '{lic}' (known: {sorted(KNOWN_LICENSES)})",
              file=sys.stderr)
        return 1
    if "houston" not in args.authorized_by.lower():
        print("FAIL: --authorized-by must record Houston's authorization", file=sys.stderr)
        return 1

    cfg = json.loads(CONFIG.read_text())
    papers = cfg["papers"]
    for pid in [p.strip() for p in args.papers.split(",") if p.strip()]:
        if pid not in papers:
            print(f"FAIL: unknown paper {pid}", file=sys.stderr)
            return 1
        entry = papers[pid]
        entry["metadata"]["license"] = lic
        entry["license_authorization"] = args.authorized_by
        if pid == "P1A":
            entry["metadata_complete"] = True
            entry.pop("metadata_blocker", None)
            print(f"{pid}: license={lic}; fully unblocked (license was the only gate)")
        elif pid == "P1B":
            doi = args.p1b_software_doi.strip()
            if doi:
                entry["metadata_complete"] = True
                entry.pop("metadata_blocker", None)
                rel = entry["metadata"].setdefault("related_identifiers", [])
                if not any(r.get("identifier") == doi for r in rel):
                    rel.append({"identifier": doi, "relation": "describes", "scheme": "doi"})
                print(f"{pid}: license={lic}; software DOI {doi} recorded; fully unblocked")
            else:
                entry["metadata_complete"] = False
                entry["metadata_blocker"] = (
                    "License authorized; remaining gate: mint the namaster-proof 0.1.7 "
                    "software archive DOI on Zenodo, then re-run d2_authorize_deposits.py "
                    "with --p1b-software-doi")
                print(f"{pid}: license={lic}; still gated on software DOI")
        elif pid == "P5":
            entry["metadata_complete"] = False
            entry["metadata_blocker"] = (
                "License authorized; remaining gate: Paper-IV (P4) arXiv ID back-patch "
                "into the P5 manuscript and rebuilt tarball/proof")
            print(f"{pid}: license={lic}; still gated on Paper-IV back-patch")
        else:
            print(f"{pid}: license={lic} set (no blocker logic defined for this paper)")

    if args.write:
        CONFIG.write_text(json.dumps(cfg, indent=1, sort_keys=False) + "\n")
        print(f"WROTE {CONFIG}")
    else:
        print("dry-run only; re-run with --write to apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
