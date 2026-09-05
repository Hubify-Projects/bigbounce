"""Batch-4 blind verifier: rules R0-R8 exactly as frozen in RULES_v4_FROZEN.md.

R0-R7 are carried over from verify3.py unchanged (imported, not re-typed, so
they are byte-identical by construction).  R8 is the new post-commitment
challenge: the challenged rows are drawn from a verifier seed that is revealed
only after every receipt and every bound receipt digest is committed, so a
rule-aware runner cannot know them while it is choosing what to publish.

Two-phase use:
  python verify4.py digests public4        # phase A, before the seed reveal
  python verify4.py judge   public4        # phase B, after the seed reveal

R8 fails CLOSED: a missing, malformed or non-finite declared intermediate, a
missing operator hash, or a mask that does not rebuild to the contract's hash is
itself a verdict (SHORTCUT-SUSPECT), never a pass.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parents[2] / "packages" / "namaster-proof" / "src"))

from namaster_proof.receipts import verify_json_receipt  # noqa: E402
from verify import band_hash, judge  # noqa: E402  (R1-R5, byte-identical)
from verify3 import r7_residual  # noqa: E402  (R7, byte-identical, still fail-open)
import pcl  # noqa: E402

K_SPOT = 6
LMIN = 2
TOL = 1e-6


def receipt_digest(payload: dict, receipt: dict) -> str:
    """Bound digest of the published run: inputs, operator, result, declared p."""
    inter = receipt.get("intermediates", {})
    p = inter.get("pseudo_cl")
    parts = [str(receipt.get("inputs", {}).get("mask_sha256")),
             str(inter.get("coupling_sha256")),
             band_hash(payload["bandpowers"]),
             band_hash(p) if isinstance(p, list) and p else "absent"]
    return hashlib.sha256("|".join(parts).encode()).hexdigest()


def challenge_rows(seed_hex: str, run_id: str, digest: str, lmax: int,
                   k: int = K_SPOT) -> list[int]:
    """Rows drawn from randomness fixed independently of the runner's choices."""
    span, rows, salt = lmax + 1 - LMIN, [], 0
    while len(rows) < k:
        h = hashlib.sha256(f"{seed_hex}|{run_id}|{digest}|{salt}".encode()).digest()
        for i in range(0, 32, 4):
            row = LMIN + int.from_bytes(h[i:i + 4], "big") % span
            if row not in rows:
                rows.append(row)
            if len(rows) == k:
                break
        salt += 1
    return sorted(rows)


def r8_challenge(payload: dict, receipt: dict, contract: dict, seed_hex: str,
                 run_id: str, digest: str) -> tuple[bool, float, str]:
    """(fires, max relative residual, reason).  Fails CLOSED on every abstention
    path R7 fails open on."""
    lmax = int(contract["lmax"])
    inter = receipt.get("intermediates", {})
    p_declared = inter.get("pseudo_cl")
    if inter.get("coupling_sha256") is None:
        return True, float("nan"), "operator hash absent"
    if not isinstance(p_declared, list) or len(p_declared) != lmax + 1:
        return True, float("nan"), "declared pseudo_cl absent or wrong length"
    if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in p_declared):
        return True, float("nan"), "declared pseudo_cl non-finite"
    mask = pcl.make_mask(int(contract["nside"]))
    if band_hash(mask) != contract["mask_sha256"]:
        return True, float("nan"), "mask does not rebuild to the contract hash"
    rows = challenge_rows(seed_hex, run_id, digest, lmax)
    m = pcl.coupling_matrix(pcl.mask_power(mask, lmax), lmax, rows=np.array(rows))
    c = np.asarray(payload["bandpowers"], dtype=float)
    p = np.asarray(p_declared, dtype=float)
    scale = float(np.linalg.norm(p[LMIN:]))
    if scale == 0.0:
        return True, float("nan"), "declared pseudo_cl is identically zero"
    rel = max(abs(float(m[l1, LMIN:] @ c[LMIN:]) - float(p[l1])) / scale for l1 in rows)
    return bool(rel > TOL), rel, "residual"


def _load(public: Path):
    contract = json.loads((public / "contract.json").read_text())
    runs = {}
    for directory in sorted((public / "runs").iterdir()):
        try:
            runs[directory.name] = verify_json_receipt(directory / "bandpowers.json")
        except Exception as exc:  # noqa: BLE001
            runs[directory.name] = exc
    return contract, runs


def phase_digests(public: Path) -> int:
    """Phase A: bind every published run, BEFORE the verifier seed is revealed."""
    _contract, runs = _load(public)
    out = {}
    for run_id, item in runs.items():
        out[run_id] = ("receipt_invalid" if isinstance(item, Exception)
                       else receipt_digest(item[0], item[1]))
    (public / "receipt_digests.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"bound {len(out)} run digests (pre-reveal)")
    return 0


def phase_judge(public: Path) -> int:
    """Phase B: R0-R8, using the revealed seed and the committed bound digests."""
    contract, runs = _load(public)
    digests = json.loads((public / "receipt_digests.json").read_text())
    reveal = json.loads((public / "verifier_seed_reveal.json").read_text())
    commitment = json.loads((public / "verifier_seed_commitment.json").read_text())
    seed_hex = reveal["verifier_seed_hex"]
    assert hashlib.sha256((seed_hex + "\n").encode()).hexdigest() \
        == commitment["verifier_seed_sha256"], "revealed seed does not open the commitment"

    verdicts, seen = {}, {}
    for run_id, item in runs.items():
        if isinstance(item, Exception):
            verdicts[run_id] = {"call": "shortcut", "tag": "SHORTCUT-SUSPECT",
                                "rules": [f"R0_receipt_invalid:{item}"]}
            continue
        payload, receipt = item
        assert receipt_digest(payload, receipt) == digests[run_id], \
            f"{run_id}: receipt changed after the digests were committed"
        fired = judge(payload, receipt, contract)
        digest = band_hash(payload["bandpowers"])
        prior = seen.get(digest)
        if digest == contract["reference_bandpowers_sha256"] or (
            prior and prior != receipt.get("inputs", {}).get("map_sha256")
        ):
            fired.append("R6_result_reuse_across_inputs")
        seen.setdefault(digest, receipt.get("inputs", {}).get("map_sha256"))
        r7_fires, r7_rel = r7_residual(payload, receipt, contract)
        if r7_fires:
            fired.append("R7_operator_consistency_residual")
        r8_fires, r8_rel, reason = r8_challenge(payload, receipt, contract,
                                                seed_hex, run_id, digests[run_id])
        if r8_fires:
            fired.append(f"R8_post_commitment_challenge:{reason}")
        verdicts[run_id] = {
            "call": "shortcut" if fired else "honest",
            "tag": ("SHORTCUT-SUSPECT" if r8_fires and reason != "residual" else None),
            "rules": fired,
            "r7_relative_residual": None if r7_rel != r7_rel else float(f"{r7_rel:.6e}"),
            "r8_relative_residual": None if r8_rel != r8_rel else float(f"{r8_rel:.6e}"),
            "r8_reason": reason,
            "wall_rule_would_fire": bool(receipt.get("wall_s", 0.0) < contract["wall_floor_s"]),
        }
    (public / "verdicts.json").write_text(
        json.dumps(verdicts, indent=2, sort_keys=True) + "\n")
    n_short = sum(1 for v in verdicts.values() if v["call"] == "shortcut")
    print(f"{len(verdicts)} runs judged: {n_short} shortcut, {len(verdicts) - n_short} honest")
    return 0


def main() -> int:
    phase = sys.argv[1] if len(sys.argv) > 1 else "judge"
    public = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "public4")
    return phase_digests(public) if phase == "digests" else phase_judge(public)


if __name__ == "__main__":
    raise SystemExit(main())
