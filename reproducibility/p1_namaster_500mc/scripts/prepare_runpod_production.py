#!/usr/bin/env python3
"""Generate a zero-spend P1B RunPod production manifest; never create a pod."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONTRACT = ROOT / "reproducibility/p1_namaster_500mc/runpod_production_contract.json"
CONFIRMATION = "LAUNCH-P1B-500MC"


def build_execution(contract: dict) -> dict:
    """Derive all executable semantics solely from the checked-out contract."""
    if len(contract.get("robustness_commands", [])) != 8:
        raise ValueError("contract must define exactly eight robustness commands")
    output_root = contract["output_root"]
    outputs = contract.get("execution_outputs", {})
    robustness_outputs = outputs.get("robustness", [])
    robustness_receipts = outputs.get("robustness_receipts", [])
    if len(robustness_outputs) != 8 or len(robustness_receipts) != 8:
        raise ValueError("contract must define exactly eight robustness output/receipt pairs")

    def rooted(paths: list[str]) -> list[str]:
        return [str(Path(output_root) / path) for path in paths]

    jobs = [{
        "name": "canonical", "kind": "canonical",
        "command": contract["canonical_command"],
        "outputs": rooted(outputs.get("canonical", [])),
    }]
    jobs.extend({
        "name": f"robustness-{index + 1:02d}", "kind": "robustness",
        "command": command,
        "outputs": rooted([robustness_outputs[index], robustness_receipts[index]]),
    } for index, command in enumerate(contract["robustness_commands"]))
    return {
        "contract_id": contract["contract_id"],
        "container": contract["container"],
        "output_root": output_root,
        "acceptance": contract["acceptance"],
        "execution_jobs": jobs,
        "merge_job": {
            "name": "strict-merge", "kind": "merge",
            "command": contract["merge_command"],
            "outputs": rooted(outputs.get("merged", []) + outputs.get("merged_receipts", [])),
        },
    }


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode:
        raise ValueError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def preflight(contract: dict, expected_commit: str) -> dict:
    head = git("rev-parse", "HEAD")
    if expected_commit != head or len(expected_commit) != 40:
        raise ValueError(f"--expected-commit must exactly equal current HEAD {head}")
    if not os.environ.get("RUNPOD_API_KEY"):
        raise ValueError("RUNPOD_API_KEY is required (value is never printed or stored)")

    inputs = contract["required_tracked_inputs"]
    if not inputs:
        raise ValueError("contract has no required tracked inputs")
    for relative in inputs:
        if git("ls-files", "--error-unmatch", "--", relative) != relative:
            raise ValueError(f"required input is not tracked: {relative}")
        if not (ROOT / relative).is_file():
            raise ValueError(f"required input is missing: {relative}")
    dirty = git("status", "--porcelain", "--untracked-files=all", "--", *inputs)
    if dirty:
        raise ValueError(f"required tracked inputs are not clean:\n{dirty}")
    execution = build_execution(contract)

    return {
        "contract_id": contract["contract_id"],
        "git_commit": head,
        "required_inputs_clean": True,
        "runpod_api_key_present": True,
        "provider_mutation_performed": False,
        "input_sha256": {relative: sha256(ROOT / relative) for relative in inputs},
        "container": contract["container"],
        "output_root": contract["output_root"],
        "canonical_command": contract["canonical_command"],
        "robustness_commands": contract["robustness_commands"],
        "merge_command": contract["merge_command"],
        "acceptance": contract["acceptance"],
        "execution_jobs": execution["execution_jobs"],
        "merge_job": execution["merge_job"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--launch", action="store_true")
    parser.add_argument("--max-budget-usd", type=float)
    parser.add_argument("--confirm")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    contract = json.loads(args.contract.read_text())
    manifest = preflight(contract, args.expected_commit)

    if args.launch:
        if args.max_budget_usd is None or args.max_budget_usd <= 0:
            raise ValueError("--launch requires a positive --max-budget-usd ceiling")
        if args.confirm != CONFIRMATION:
            raise ValueError(f"--launch requires --confirm {CONFIRMATION}")
        raise ValueError(
            "provider mutation is intentionally not implemented; use this validated "
            "manifest with an independently reviewed budget-enforcing launcher"
        )

    rendered = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(rendered)
        print(f"validated zero-spend manifest written: {args.manifest}")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"preflight failed: {error}", file=sys.stderr)
        raise SystemExit(2)
