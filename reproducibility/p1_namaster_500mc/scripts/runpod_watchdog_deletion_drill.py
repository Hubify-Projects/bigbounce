#!/usr/bin/env python3
"""One-purpose, fail-closed live drill for the independent RunPod watchdog."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import signal
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import prepare_runpod_production as prep
import runpod_budget_launcher as launcher


CONFIRMATION = "CRASH-P1B-WATCHDOG-DELETION-DRILL"
MAX_DRILL_BUDGET_USD = 0.10
MAX_DRILL_RUNTIME_MINUTES = 10
TERMINAL = {"TERMINATED", "DELETED"}
GITHUB_RECEIPT_SCHEMA = "p1b-watchdog-deletion-drill-github-run/v1"
MAX_SCHEDULE_DELAY_SECONDS = 600


def _positive_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a positive finite number")
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{label} must be a positive finite number")
    return number


def _validate_commit(commit: str) -> None:
    if len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit):
        raise ValueError("expected commit must be a full lowercase SHA-1")
    if prep.git("rev-parse", "HEAD") != commit:
        raise ValueError("expected commit must equal current HEAD")


def _production_image(contract: dict) -> str:
    image = contract.get("container", {}).get("image")
    if (not isinstance(image, str) or "@sha256:" not in image or
            len(image.rsplit("@sha256:", 1)[1]) != 64):
        raise ValueError("existing production image must be pinned by SHA-256 digest")
    return image


def _ceilings(*, hourly: float, total: float, runtime_minutes: int) -> tuple[float, float, int]:
    hourly = _positive_number(hourly, "max hourly rate")
    total = _positive_number(total, "max total budget")
    if total > MAX_DRILL_BUDGET_USD:
        raise ValueError("drill total budget must not exceed $0.10")
    if (isinstance(runtime_minutes, bool) or not isinstance(runtime_minutes, int) or
            runtime_minutes <= 0 or runtime_minutes > MAX_DRILL_RUNTIME_MINUTES):
        raise ValueError("drill runtime must be an integer from 1 through 10 minutes")
    if hourly * runtime_minutes / 60 > total + 1e-12:
        raise ValueError("hourly-rate × runtime exceeds total drill budget")
    return hourly, total, runtime_minutes


def _create_payload(*, commit: str, image: str, gpu_type_id: str,
                    runtime_minutes: int) -> dict:
    if not gpu_type_id:
        raise ValueError("exactly one GPU type id is required")
    harmless = ["bash", "-lc", f"exec sleep {runtime_minutes * 60}"]
    command = launcher.container_timeout_command(
        harmless, runtime_seconds=runtime_minutes * 60,
        status_path=Path("/tmp/p1b-watchdog-drill-status.json"), commit=commit,
    )
    return {
        "name": launcher.pod_name(commit),
        "imageName": image,
        "gpuTypeIds": [gpu_type_id],
        "gpuCount": 1,
        "containerDiskInGb": 20,
        "cloudType": "SECURE",
        "dockerEntrypoint": ["bash", "-lc"],
        "dockerStartCmd": [command],
        "env": {"P1B_GIT_COMMIT": commit, "P1B_WATCHDOG_DRILL": "1"},
    }


def _validate_create_response(pod: object, *, payload: dict, max_hourly_rate: float) -> str:
    if not isinstance(pod, dict):
        raise ValueError("create response must be an object")
    pod_id = launcher.field(pod, "id", "podId")
    cost = launcher.field(pod, "costPerHr", "desiredCostPerHr", "costPerHour")
    status = str(launcher.field(pod, "status", "desiredStatus") or "").upper()
    returned_image = launcher.field(pod, "imageName", "image")
    returned_gpu = launcher.field(pod, "gpuTypeId", "gpuType")
    volume = launcher.field(pod, "networkVolume", "networkVolumeId")
    if not isinstance(pod_id, str) or not pod_id:
        raise ValueError("create response omitted pod id")
    if (_positive_number(cost, "create response hourly cost") > max_hourly_rate or
            returned_image != payload["imageName"] or
            launcher.field(pod, "gpuCount") != 1 or
            returned_gpu != payload["gpuTypeIds"][0] or volume not in (None, "", {}) or
            status not in {"CREATED", "RUNNING", "STARTING", "PENDING"}):
        raise ValueError("create response image/GPU/no-volume/status/cost mismatch")
    return pod_id


def crash_after_create(*, client, github_variables, contract: dict, expected_commit: str,
                       balance_path: Path, balance_max_age_minutes: int,
                       max_hourly_rate: float, max_total_budget: float,
                       max_runtime_minutes: int, gpu_type_id: str,
                       confirmation: str, now_fn=launcher.utcnow,
                       kill_fn=os.kill) -> None:
    """Publish durable intent, create a harmless pod, then deliberately lose the host."""
    if confirmation != CONFIRMATION:
        raise ValueError(f"drill requires exact confirmation: {CONFIRMATION}")
    _validate_commit(expected_commit)
    hourly, total, runtime = _ceilings(
        hourly=max_hourly_rate, total=max_total_budget, runtime_minutes=max_runtime_minutes,
    )
    launcher.validate_balance(balance_path, total, balance_max_age_minutes, now_fn())
    image = _production_image(contract)
    name = launcher.pod_name(expected_commit)
    # Construct and fully validate the inert payload before activating the
    # durable intent. Publication is the final operation before provider POST.
    payload = _create_payload(
        commit=expected_commit, image=image, gpu_type_id=gpu_type_id,
        runtime_minutes=runtime,
    )
    if any(launcher.field(pod, "name") == name for pod in launcher.pod_rows(client.list_pods())):
        raise ValueError(f"refusing existing deterministic production pod name: {name}")
    started = now_fn()
    github_variables.publish_and_verify(launcher.watchdog_intent(
        commit=expected_commit, created_not_before=started,
        max_runtime_minutes=runtime, max_hourly_rate=hourly,
        max_total_budget=total,
    ))
    pod = client.create_pod(payload)
    _validate_create_response(pod, payload=payload, max_hourly_rate=hourly)
    # Deliberately do not persist the pod id. The externally stored intent must
    # be sufficient for the independent watchdog to discover and delete it.
    kill_fn(os.getpid(), signal.SIGKILL)
    raise RuntimeError("SIGKILL unexpectedly returned")


def _validate_github_receipt(path: Path, *, commit: str, pod_name: str) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    required = {"schema", "run_id", "event_name", "conclusion", "git_commit", "pod_name",
                "action", "deleted_pod_id", "deadline", "watchdog_observed_at", "completed_at"}
    if not isinstance(value, dict) or set(value) != required:
        raise ValueError("GitHub run receipt must contain exactly the drill receipt fields")
    if (value["schema"] != GITHUB_RECEIPT_SCHEMA or
            isinstance(value["run_id"], bool) or not isinstance(value["run_id"], int) or
            value["run_id"] <= 0 or value["conclusion"] != "success" or
            value["event_name"] != "schedule" or
            value["git_commit"] != commit or value["pod_name"] != pod_name or
            value["action"] != "delete_confirmed" or
            not isinstance(value["deleted_pod_id"], str) or not value["deleted_pod_id"]):
        raise ValueError("GitHub run receipt does not prove successful watchdog deletion")
    deadline = launcher.parse_instant(value["deadline"])
    observed = launcher.parse_instant(value["watchdog_observed_at"])
    completed = launcher.parse_instant(value["completed_at"])
    delay = (observed - deadline).total_seconds()
    if delay < 0 or delay > MAX_SCHEDULE_DELAY_SECONDS or completed < observed:
        raise ValueError("scheduled watchdog proof is early, delayed, or temporally ambiguous")
    return value


def _inactive_intent(github_variables, *, commit: str, name: str) -> None:
    observed = github_variables.request("GET", github_variables.variable_path)
    if observed.get("name") != launcher.WATCHDOG_INTENT_VARIABLE:
        raise ValueError("durable watchdog intent read-back name mismatch")
    try:
        intent = json.loads(observed.get("value", ""))
    except json.JSONDecodeError:
        raise ValueError("durable watchdog intent read-back is not JSON") from None
    if (intent.get("active") is not False or intent.get("git_commit") != commit or
            intent.get("pod_name") != name):
        raise ValueError("commit-bound durable watchdog intent was not restored inactive")


def verify(*, client, github_variables, expected_commit: str, github_run_receipt: Path,
           initial_balance_path: Path, final_balance_path: Path, max_total_budget: float,
           balance_max_age_minutes: int = 15,
           now_fn=launcher.utcnow) -> dict:
    _validate_commit(expected_commit)
    name = launcher.pod_name(expected_commit)
    receipt = _validate_github_receipt(github_run_receipt, commit=expected_commit, pod_name=name)
    matches = [pod for pod in launcher.pod_rows(client.list_pods())
               if launcher.field(pod, "name") == name]
    if matches:
        raise ValueError("matching drill pod still exists; deletion is not proven")
    budget = _positive_number(max_total_budget, "max total budget")
    if budget > MAX_DRILL_BUDGET_USD:
        raise ValueError("verification budget must not exceed $0.10")
    initial_balance = launcher.validate_balance(
        initial_balance_path, 0, balance_max_age_minutes, now_fn(),
    )
    final_balance = launcher.validate_balance(
        final_balance_path, 0, balance_max_age_minutes, now_fn(),
    )
    spent = float(initial_balance["amount_usd"]) - float(final_balance["amount_usd"])
    if spent < 0 or spent > budget + 1e-9:
        raise ValueError("final balance delta is negative, ambiguous, or exceeds drill budget")
    _inactive_intent(github_variables, commit=expected_commit, name=name)
    return {
        "schema": "p1b-watchdog-deletion-drill-verification/v1",
        "verified": True,
        "git_commit": expected_commit,
        "pod_name": name,
        "provider_state": "absent",
        "github_run_id": receipt["run_id"],
        "final_balance_receipt": final_balance,
        "observed_spend_usd": spent,
        "durable_intent_active": False,
        "contract_auto_enabled": False,
    }


def parse_args(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--crash-after-create", action="store_true")
    mode.add_argument("--verify", action="store_true")
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--balance-receipt", type=Path)
    parser.add_argument("--balance-max-age-minutes", type=int, default=15)
    parser.add_argument("--max-hourly-rate-usd", type=float)
    parser.add_argument("--max-total-budget-usd", type=float)
    parser.add_argument("--max-runtime-minutes", type=int)
    parser.add_argument("--gpu-type-id")
    parser.add_argument("--confirm")
    parser.add_argument("--github-run-receipt", type=Path)
    parser.add_argument("--final-balance-receipt", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    key = os.environ.get("RUNPOD_API_KEY")
    if not key:
        raise ValueError("RUNPOD_API_KEY is required (never printed or stored)")
    client = launcher.RunPodREST(key)
    if args.verify:
        if (args.github_run_receipt is None or args.balance_receipt is None or
                args.final_balance_receipt is None or args.max_total_budget_usd is None):
            raise ValueError("--verify requires GitHub-run, initial/final-balance, and budget evidence")
        github_token = os.environ.get("P1B_WATCHDOG_GITHUB_TOKEN")
        if not github_token:
            raise ValueError("P1B_WATCHDOG_GITHUB_TOKEN is required to verify inactive intent")
        print(json.dumps(verify(
            client=client, github_variables=launcher.GitHubActionsVariables(github_token),
            expected_commit=args.expected_commit, github_run_receipt=args.github_run_receipt,
            initial_balance_path=args.balance_receipt, final_balance_path=args.final_balance_receipt,
            max_total_budget=args.max_total_budget_usd,
            balance_max_age_minutes=args.balance_max_age_minutes,
        ), sort_keys=True))
        return 0
    github_token = os.environ.get("P1B_WATCHDOG_GITHUB_TOKEN")
    if not github_token:
        raise ValueError("P1B_WATCHDOG_GITHUB_TOKEN is required for durable intent")
    required = (args.balance_receipt, args.max_hourly_rate_usd, args.max_total_budget_usd,
                args.max_runtime_minutes, args.gpu_type_id)
    if any(value is None for value in required):
        raise ValueError("drill requires balance, rate, budget, runtime, and GPU ceilings")
    contract = json.loads(prep.DEFAULT_CONTRACT.read_text(encoding="utf-8"))
    crash_after_create(
        client=client, github_variables=launcher.GitHubActionsVariables(github_token),
        contract=contract, expected_commit=args.expected_commit,
        balance_path=args.balance_receipt,
        balance_max_age_minutes=args.balance_max_age_minutes,
        max_hourly_rate=args.max_hourly_rate_usd,
        max_total_budget=args.max_total_budget_usd,
        max_runtime_minutes=args.max_runtime_minutes,
        gpu_type_id=args.gpu_type_id, confirmation=args.confirm,
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"deletion drill failed: {error}", file=sys.stderr)
        raise SystemExit(2)
