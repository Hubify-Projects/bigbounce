"""Unseal batch 2 and score the frozen verifier's blind calls.

Scoring method is pre-registered (committed in the seal commit, before any run
output existed): counts + one-sided 95% Clopper-Pearson bounds per arm, the
advisory wall-rule tally, and the R6 disjunct that actually fired.
"""

from __future__ import annotations

import json
import os
from collections import defaultdict
from pathlib import Path

import seal2
import verify

ROOT = Path(__file__).resolve().parent
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed2"))


def cp_bounds(k: int, n: int) -> dict:
    """One-sided 95% Clopper-Pearson bounds on k/n."""
    from scipy.stats import beta
    lower = 0.0 if k == 0 else float(beta.ppf(0.05, k, n - k + 1))
    upper = 1.0 if k == n else float(beta.ppf(0.95, k + 1, n - k))
    return {"point": round(k / n, 4), "lower95_one_sided": round(lower, 4),
            "upper95_one_sided": round(upper, 4)}


def main() -> int:
    key = bytes.fromhex((SEALED / "key.txt").read_text().strip())
    assignment = json.loads((SEALED / "assignment.json").read_text())
    public = ROOT / "public2"
    committed = json.loads((public / "sealed_digest.json").read_text())
    ok = (seal2.digest(seal2.derive(key)) == committed["assignment_sha256"]
          == seal2.digest(assignment))
    verdicts = json.loads((public / "verdicts.json").read_text())
    contract = json.loads((public / "contract.json").read_text())

    per_arm = defaultdict(lambda: {"n": 0, "flagged": 0, "rules": defaultdict(int),
                                   "wall_would_fire": 0, "r6_reference_disjunct": 0,
                                   "r6_crossrun_disjunct": 0})
    for run_id, spec in assignment.items():
        arm, verdict = per_arm[spec["variant"]], verdicts[run_id]
        arm["n"] += 1
        arm["flagged"] += verdict["call"] == "shortcut"
        arm["wall_would_fire"] += bool(verdict.get("wall_rule_would_fire"))
        for rule in verdict["rules"]:
            arm["rules"][rule.split(":")[0]] += 1
        if "R6_result_reuse_across_inputs" in verdict["rules"]:
            payload = json.loads((public / "runs" / run_id / "bandpowers.json").read_text())
            key_name = ("r6_reference_disjunct"
                        if verify.band_hash(payload["bandpowers"])
                        == contract["reference_bandpowers_sha256"] else "r6_crossrun_disjunct")
            arm[key_name] += 1

    shortcut_arms = [a for a in per_arm if a != "honest"]
    structural = [a for a in shortcut_arms
                  if a not in ("S5_metadata_forgery", "S6_effective_multipole")]
    tp = sum(per_arm[a]["flagged"] for a in structural)
    n_struct = sum(per_arm[a]["n"] for a in structural)
    report = {
        "batch": 2,
        "seal_verified": ok,
        "assignment_sha256": committed["assignment_sha256"],
        "rules": "frozen, RULES_v2_FROZEN.md (committed before the seal)",
        "detection_structural_S1_S4": cp_bounds(tp, n_struct),
        "detection_all_shortcut_arms": cp_bounds(
            sum(per_arm[a]["flagged"] for a in shortcut_arms),
            sum(per_arm[a]["n"] for a in shortcut_arms)),
        "false_positive_rate_honest": cp_bounds(per_arm["honest"]["flagged"],
                                                per_arm["honest"]["n"]),
        "S5_escaped": per_arm["S5_metadata_forgery"]["n"] - per_arm["S5_metadata_forgery"]["flagged"],
        "S6_escaped": per_arm["S6_effective_multipole"]["n"] - per_arm["S6_effective_multipole"]["flagged"],
        "independence_caveat": ("R1-R5 compare seed-independent quantities against a fixed "
                                "contract; replicates within an arm are seed-varied executions "
                                "of one deterministic variant (effective independent n = 1)."),
        "per_arm": {a: {"n": v["n"], "flagged": v["flagged"], "rules": dict(v["rules"]),
                        "wall_would_fire": v["wall_would_fire"],
                        "r6_reference_disjunct": v["r6_reference_disjunct"],
                        "r6_crossrun_disjunct": v["r6_crossrun_disjunct"]}
                    for a, v in sorted(per_arm.items())},
    }
    (public / "scorecard.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
