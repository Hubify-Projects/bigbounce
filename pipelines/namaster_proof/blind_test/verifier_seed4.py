"""Batch-4 verifier-side randomness: commit before the batch, reveal after it.

    python verifier_seed4.py commit    # draws sigma, publishes sha256(sigma)
    python verifier_seed4.py reveal    # publishes sigma itself

The seed lives OUTSIDE the repository, under $NP_SEALED_DIR, for the whole
sealed window, so no automated commit can sweep it into git early.  Only the
commitment goes in first; the reveal is its own later commit.

Randomness source, declared in RULES_v4_FROZEN.md: preference (a) is the Bitcoin
block hash of a *confirmed* OpenTimestamps attestation of the batch receipt
digest -- randomness that did not exist when the runs were made and that nobody,
verifier included, controls.  Bitcoin confirmation of a stamp made after the
receipts are published takes hours, so preference (b), this commit-reveal seed,
is the operative source for this batch; (a) is a drop-in replacement for
`challenge_rows`' first argument.  The recorded source is carried into the
scorecard so no reader has to infer which was used.
"""

from __future__ import annotations

import hashlib
import json
import os
import secrets
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed4"))
PUBLIC = ROOT / "public4"
SOURCE = ("commit_reveal_verifier_seed_32B; "
          "bitcoin_ots_blockhash declared as the drop-in upgrade "
          "(no confirmed post-receipt attestation exists at challenge time)")


def main() -> int:
    action = sys.argv[1] if len(sys.argv) > 1 else "commit"
    PUBLIC.mkdir(exist_ok=True)
    SEALED.mkdir(parents=True, exist_ok=True)
    seed_file = SEALED / "verifier_seed.txt"
    if action == "commit":
        text = secrets.token_bytes(32).hex() + "\n"
        seed_file.write_text(text)
        (PUBLIC / "verifier_seed_commitment.json").write_text(json.dumps({
            "batch": 4,
            "purpose": "R8 post-commitment challenge randomness",
            "verifier_seed_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "randomness_source": SOURCE,
            "committed_before": ("the batch-4 seal, the batch-4 scripts' execution, "
                                 "and any batch-4 run output"),
            "revealed_after": "every run receipt and every bound receipt digest is committed",
        }, indent=2, sort_keys=True) + "\n")
        print("verifier seed committed")
    elif action == "reveal":
        text = seed_file.read_text()
        (PUBLIC / "verifier_seed_reveal.json").write_text(json.dumps({
            "batch": 4,
            "verifier_seed_hex": text.strip(),
            "opens_commitment_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "randomness_source": SOURCE,
        }, indent=2, sort_keys=True) + "\n")
        print("verifier seed revealed")
    else:
        raise SystemExit(f"unknown action {action!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
