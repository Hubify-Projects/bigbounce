"""Sealed random assignment of opaque run ids to honest/shortcut arms.

The assignment is drawn from a random 32-byte key, written under sealed/ (which
the verifier must not read), and *committed* before any run executes by
publishing only sha256(assignment JSON) to public/sealed_digest.json.  Revealing
the key afterwards lets anyone recompute the digest and confirm the assignment
was fixed in advance.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import secrets
from pathlib import Path

from variants import VARIANTS

REPLICATES = 3


def derive(key: bytes, n_replicates: int = REPLICATES) -> dict[str, dict]:
    arms = [v for v in VARIANTS for _ in range(n_replicates)]
    order = sorted(
        range(len(arms)),
        key=lambda i: hmac.new(key, f"perm{i}".encode(), hashlib.sha256).hexdigest(),
    )
    assignment = {}
    for slot, idx in enumerate(order):
        run_id = f"run_{slot:03d}"
        seed_hex = hmac.new(key, f"seed{run_id}".encode(), hashlib.sha256).hexdigest()
        assignment[run_id] = {"variant": arms[idx], "map_seed": int(seed_hex[:8], 16) % 100000}
    return assignment


def digest(assignment: dict) -> str:
    encoded = json.dumps(assignment, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parent
    sealed, public = root / "sealed", root / "public"
    sealed.mkdir(exist_ok=True)
    public.mkdir(exist_ok=True)
    key = secrets.token_bytes(32)
    assignment = derive(key)
    (sealed / "key.txt").write_text(key.hex() + "\n")
    (sealed / "assignment.json").write_text(json.dumps(assignment, indent=2, sort_keys=True) + "\n")
    (public / "sealed_digest.json").write_text(
        json.dumps({"n_runs": len(assignment), "assignment_sha256": digest(assignment)},
                   indent=2, sort_keys=True) + "\n"
    )
    print(f"sealed {len(assignment)} runs; digest {digest(assignment)[:16]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
