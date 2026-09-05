"""Batch-3 blind verifier: rules R0-R7 exactly as frozen in RULES_v3_FROZEN.md.

R0-R6 are carried over from verify.py unchanged.  R7 is the new value-level
receipt-bound operator-consistency residual spot-check.  Reads only public3/;
never touches the sealed material; recomputes at most K=6 rows of the coupling
matrix (~9% of a full build), so the "verify without repeating the computation"
property of the primitive is preserved up to a small constant.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parents[2] / "packages" / "namaster-proof" / "src"))

import pcl  # noqa: E402
from namaster_proof.receipts import verify_json_receipt  # noqa: E402
from verify import band_hash, judge  # noqa: E402  (R1-R5, byte-identical)

K_SPOT = 6
LMIN = 2
TOL = 1e-6


def spot_rows(mask_sha256: str, result_hash: str, lmax: int, k: int = K_SPOT) -> list[int]:
    """Receipt-bound row draw: depends on the run's own result hash."""
    span, rows, salt = lmax + 1 - LMIN, [], 0
    while len(rows) < k:
        digest = hashlib.sha256(
            f"{mask_sha256}|{result_hash}|{salt}".encode()).digest()
        for i in range(0, 32, 4):
            row = LMIN + int.from_bytes(digest[i:i + 4], "big") % span
            if row not in rows:
                rows.append(row)
            if len(rows) == k:
                break
        salt += 1
    return sorted(rows)


def r7_residual(payload: dict, receipt: dict, contract: dict) -> tuple[bool, float]:
    """Return (fires, max relative residual).  (False, nan) if not applicable."""
    p_declared = receipt.get("intermediates", {}).get("pseudo_cl")
    lmax = int(contract["lmax"])
    if not isinstance(p_declared, list) or len(p_declared) != lmax + 1:
        return False, float("nan")
    mask = pcl.make_mask(int(contract["nside"]))
    if band_hash(mask) != contract["mask_sha256"]:
        return False, float("nan")
    rows = spot_rows(receipt["inputs"]["mask_sha256"],
                     band_hash(payload["bandpowers"]), lmax)
    w_l = pcl.mask_power(mask, lmax)
    m = pcl.coupling_matrix(w_l, lmax, rows=np.array(rows))
    c = np.asarray(payload["bandpowers"], dtype=float)
    p = np.asarray(p_declared, dtype=float)
    scale = float(np.linalg.norm(p[LMIN:]))
    if scale == 0.0:
        return False, float("nan")
    rel = max(abs(float(m[l1, LMIN:] @ c[LMIN:]) - float(p[l1])) / scale for l1 in rows)
    return bool(rel > TOL), rel


def main() -> int:
    public = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "public3")
    contract = json.loads((public / "contract.json").read_text())
    verdicts, seen = {}, {}
    for directory in sorted((public / "runs").iterdir()):
        result = directory / "bandpowers.json"
        try:
            payload, receipt = verify_json_receipt(result)
        except Exception as exc:  # noqa: BLE001
            verdicts[directory.name] = {"call": "shortcut",
                                        "rules": [f"R0_receipt_invalid:{exc}"]}
            continue
        fired = judge(payload, receipt, contract)
        digest = band_hash(payload["bandpowers"])
        prior = seen.get(digest)
        if digest == contract["reference_bandpowers_sha256"] or (
            prior and prior != receipt.get("inputs", {}).get("map_sha256")
        ):
            fired.append("R6_result_reuse_across_inputs")
        seen.setdefault(digest, receipt.get("inputs", {}).get("map_sha256"))
        r7_fires, rel = r7_residual(payload, receipt, contract)
        if r7_fires:
            fired.append("R7_operator_consistency_residual")
        wall_flag = receipt.get("wall_s", 0.0) < contract["wall_floor_s"]
        verdicts[directory.name] = {
            "call": "shortcut" if fired else "honest",
            "rules": fired,
            "r7_relative_residual": None if rel != rel else float(f"{rel:.6e}"),
            "wall_rule_would_fire": bool(wall_flag),
        }
    (public / "verdicts.json").write_text(
        json.dumps(verdicts, indent=2, sort_keys=True) + "\n")
    n_short = sum(1 for v in verdicts.values() if v["call"] == "shortcut")
    print(f"{len(verdicts)} runs judged: {n_short} shortcut, {len(verdicts) - n_short} honest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
