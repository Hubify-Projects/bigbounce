"""Batch-3 seal: sealed random assignment + public commitment, drawn AFTER the
rules were frozen (RULES_v3_FROZEN.md, its own commit) and BEFORE any run.

The sealed material (key + assignment) is written OUTSIDE the repository, to
$NP_SEALED_DIR, so that no automated commit can sweep it into git during the
sealed window.  Only the commitment goes into the repo:

  public3/sealed_digest.json      n_runs, assignment_sha256, key_file_sha256
  public3/frozen_rules_digest.json sha256 of the frozen rules + every script

Reveal (reveal3.py) copies the sealed material in afterwards, in its own commit.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
from pathlib import Path

from variants3 import VARIANTS_V3

REPLICATES = 6
ROOT = Path(__file__).resolve().parent
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed3"))
FROZEN_FILES = ("RULES_v3_FROZEN.md", "verify.py", "variants.py", "variants2.py",
                "pcl.py", "wigner.py", "variants3.py", "verify3.py", "seal3.py", "run_blind3.py")


def derive(key: bytes, n_replicates: int = REPLICATES) -> dict[str, dict]:
    arms = [v for v in VARIANTS_V3 for _ in range(n_replicates)]
    order = sorted(range(len(arms)),
                   key=lambda i: hmac.new(key, f"perm{i}".encode(), hashlib.sha256).hexdigest())
    assignment = {}
    for slot, idx in enumerate(order):
        run_id = f"run_{slot:03d}"
        seed_hex = hmac.new(key, f"seed{run_id}".encode(), hashlib.sha256).hexdigest()
        assignment[run_id] = {"variant": arms[idx], "map_seed": int(seed_hex[:8], 16) % 100000}
    return assignment


def digest(assignment: dict) -> str:
    return hashlib.sha256(json.dumps(assignment, sort_keys=True).encode()).hexdigest()


def main() -> int:
    public = ROOT / "public3"
    public.mkdir(exist_ok=True)
    SEALED.mkdir(parents=True, exist_ok=True)
    key = secrets.token_bytes(32)
    assignment = derive(key)
    key_text = key.hex() + "\n"
    (SEALED / "key.txt").write_text(key_text)
    (SEALED / "assignment.json").write_text(json.dumps(assignment, indent=2, sort_keys=True) + "\n")
    (public / "sealed_digest.json").write_text(json.dumps({
        "batch": 3,
        "n_runs": len(assignment),
        "n_arms": len(VARIANTS_V3),
        "replicates_per_arm": REPLICATES,
        "arms": list(VARIANTS_V3),
        "assignment_sha256": digest(assignment),
        "key_file_sha256": hashlib.sha256(key_text.encode()).hexdigest(),
    }, indent=2, sort_keys=True) + "\n")
    (public / "frozen_rules_digest.json").write_text(json.dumps(
        {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in FROZEN_FILES},
        indent=2, sort_keys=True) + "\n")
    print(f"sealed {len(assignment)} runs; digest {digest(assignment)[:16]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
