"""Unseal batch 4 and score the frozen verifier's blind calls.

Scoring is pre-registered in RULES_v4_FROZEN.md (its own commit, before the
verifier-seed commitment, before the seal, before any run output): **class-level
counts only**.  No Clopper-Pearson interval and no per-run detection probability
is computed here, deliberately -- the R2/R3 audits are right that within-arm
replicates are seed-varied executions of one deterministic variant, so the
inferential unit is the class, not the run.
"""

from __future__ import annotations

import json
import os
from collections import defaultdict
from pathlib import Path

import seal4

ROOT = Path(__file__).resolve().parent
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed4"))


def main() -> int:
    key = bytes.fromhex((SEALED / "key.txt").read_text().strip())
    assignment = json.loads((SEALED / "assignment.json").read_text())
    public = ROOT / "public4"
    committed = json.loads((public / "sealed_digest.json").read_text())
    commitment = json.loads((public / "verifier_seed_commitment.json").read_text())
    reveal = json.loads((public / "verifier_seed_reveal.json").read_text())
    verdicts = json.loads((public / "verdicts.json").read_text())

    per_arm = defaultdict(lambda: {"n": 0, "flagged": 0, "rules": defaultdict(int),
                                   "r7_fired": 0, "r8_fired": 0, "suspect": 0,
                                   "r7_res": [], "r8_res": []})
    for run_id, spec in assignment.items():
        arm, v = per_arm[spec["variant"]], verdicts[run_id]
        arm["n"] += 1
        arm["flagged"] += v["call"] == "shortcut"
        arm["suspect"] += v.get("tag") == "SHORTCUT-SUSPECT"
        for rule in v["rules"]:
            name = rule.split(":")[0]
            arm["rules"][name] += 1
            arm["r7_fired"] += name == "R7_operator_consistency_residual"
            arm["r8_fired"] += name == "R8_post_commitment_challenge"
        for src, dst in (("r7_relative_residual", "r7_res"), ("r8_relative_residual", "r8_res")):
            if v.get(src) is not None:
                arm[dst].append(v[src])

    report = {
        "batch": 4,
        "seal_verified": seal4.digest(seal4.derive(key)) == committed["assignment_sha256"]
        == seal4.digest(assignment),
        "verifier_seed_commitment_opened": reveal["opens_commitment_sha256"]
        == commitment["verifier_seed_sha256"],
        "randomness_source": commitment["randomness_source"],
        "assignment_sha256": committed["assignment_sha256"],
        "rules": "frozen, RULES_v4_FROZEN.md (committed before the seed commitment and the seal)",
        "reporting": ("class-level counts only; no run-level Clopper-Pearson interval "
                      "and no per-run detection probability is computed or claimed"),
        "headline": {
            "S7_r7_aware_effective": {
                "r7_fired": per_arm["S7_r7_aware_effective"]["r7_fired"],
                "r8_fired": per_arm["S7_r7_aware_effective"]["r8_fired"],
                "flagged": per_arm["S7_r7_aware_effective"]["flagged"],
                "n": per_arm["S7_r7_aware_effective"]["n"]},
            "S8_omit_pseudo_cl": {
                "r7_fired": per_arm["S8_omit_pseudo_cl"]["r7_fired"],
                "r8_fired": per_arm["S8_omit_pseudo_cl"]["r8_fired"],
                "flagged": per_arm["S8_omit_pseudo_cl"]["flagged"],
                "suspect": per_arm["S8_omit_pseudo_cl"]["suspect"],
                "n": per_arm["S8_omit_pseudo_cl"]["n"]},
        },
        "false_positives_honest": f'{per_arm["honest"]["flagged"]}/{per_arm["honest"]["n"]}',
        "per_arm": {a: {"n": v["n"], "flagged": v["flagged"], "rules": dict(v["rules"]),
                        "r7_fired": v["r7_fired"], "r8_fired": v["r8_fired"],
                        "shortcut_suspect": v["suspect"],
                        "r7_residual_max": max(v["r7_res"]) if v["r7_res"] else None,
                        "r8_residual_max": max(v["r8_res"]) if v["r8_res"] else None,
                        "r8_residual_min": min(v["r8_res"]) if v["r8_res"] else None}
                    for a, v in sorted(per_arm.items())},
    }
    (public / "scorecard.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
