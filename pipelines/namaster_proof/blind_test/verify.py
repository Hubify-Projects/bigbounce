"""Blind verifier: decides honest vs shortcut from receipts + contract alone.

Reads only public/ (the reference contract and the run directories).  It never
touches sealed/, and it never re-runs the expensive computation — that is the
whole point of the primitive.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[2] / "packages" / "namaster-proof" / "src"))

from namaster_proof.receipts import verify_json_receipt  # noqa: E402


def band_hash(bandpowers) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(np.asarray(bandpowers), dtype=np.float64).tobytes()
    ).hexdigest()


def judge(payload: dict, receipt: dict, contract: dict) -> list[str]:
    """Pre-declared primary rule set; returns the triggered rule names."""
    fired = []
    inter = receipt.get("intermediates", {})
    if receipt.get("code", {}).get("sha256") != contract["code_sha256"]:
        fired.append("R1_code_mismatch")
    if inter.get("ell_grid") != contract["ell_grid"]:
        fired.append("R2_grid_mismatch")
    if inter.get("n_wigner3j") != contract["n_wigner3j"]:
        fired.append("R3_3j_count_mismatch")
    if inter.get("coupling_shape") != contract["coupling_shape"] or \
       inter.get("coupling_support") != contract["coupling_support"]:
        fired.append("R4_operator_shape_mismatch")
    if receipt.get("inputs", {}).get("mask_sha256") != contract["mask_sha256"]:
        fired.append("R5_input_contract_mismatch")
    return fired


def main() -> int:
    # Non-rule plumbing only: batch 2 publishes under public2/.  judge() and the
    # R6 block below are byte-identical to the rule set frozen in
    # RULES_v2_FROZEN.md; this argument selects the directory, nothing else.
    public = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "public")
    contract = json.loads((public / "contract.json").read_text())
    verdicts, seen = {}, {}
    for directory in sorted((public / "runs").iterdir()):
        result = directory / "bandpowers.json"
        try:
            payload, receipt = verify_json_receipt(result)
        except Exception as exc:  # noqa: BLE001
            verdicts[directory.name] = {"call": "shortcut", "rules": [f"R0_receipt_invalid:{exc}"]}
            continue
        fired = judge(payload, receipt, contract)
        digest = band_hash(payload["bandpowers"])
        prior = seen.get(digest)
        if digest == contract["reference_bandpowers_sha256"] or (
            prior and prior != receipt.get("inputs", {}).get("map_sha256")
        ):
            fired.append("R6_result_reuse_across_inputs")
        seen.setdefault(digest, receipt.get("inputs", {}).get("map_sha256"))
        wall_flag = receipt.get("wall_s", 0.0) < contract["wall_floor_s"]
        verdicts[directory.name] = {
            "call": "shortcut" if fired else "honest",
            "rules": fired,
            "wall_rule_would_fire": bool(wall_flag),
        }
    (public / "verdicts.json").write_text(json.dumps(verdicts, indent=2, sort_keys=True) + "\n")
    n_short = sum(1 for v in verdicts.values() if v["call"] == "shortcut")
    print(f"{len(verdicts)} runs judged: {n_short} shortcut, {len(verdicts) - n_short} honest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
