"""Batch-4 seal: sealed random assignment + public commitment, drawn AFTER the
rules were frozen (RULES_v4_FROZEN.md, its own commit) and AFTER the verifier
seed was committed (its own commit), and BEFORE any run.

Same construction as seal3.py; only the variant table and the frozen-file list
change.  Sealed material stays outside the repository under $NP_SEALED_DIR.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
from pathlib import Path

from variants4 import VARIANTS_V4

REPLICATES = 6
ROOT = Path(__file__).resolve().parent
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed4"))
FROZEN_FILES = ("RULES_v4_FROZEN.md", "verify.py", "variants.py", "variants2.py",
                "pcl.py", "wigner.py", "variants3.py", "verify3.py",
                "variants4.py", "verify4.py", "seal4.py", "run_blind4.py",
                "verifier_seed4.py")


def derive(key: bytes, n_replicates: int = REPLICATES) -> dict[str, dict]:
    arms = [v for v in VARIANTS_V4 for _ in range(n_replicates)]
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
    public = ROOT / "public4"
    public.mkdir(exist_ok=True)
    SEALED.mkdir(parents=True, exist_ok=True)
    key = secrets.token_bytes(32)
    assignment = derive(key)
    key_text = key.hex() + "\n"
    (SEALED / "key.txt").write_text(key_text)
    (SEALED / "assignment.json").write_text(json.dumps(assignment, indent=2, sort_keys=True) + "\n")
    (public / "sealed_digest.json").write_text(json.dumps({
        "batch": 4,
        "n_runs": len(assignment),
        "n_arms": len(VARIANTS_V4),
        "replicates_per_arm": REPLICATES,
        "arms": list(VARIANTS_V4),
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
