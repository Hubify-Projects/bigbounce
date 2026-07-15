#!/usr/bin/env python3
"""Fail-closed RunPod REST v1 launcher for the frozen P1B production job."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import prepare_runpod_production as prep


API_BASE = "https://rest.runpod.io/v1"
CONFIRMATION = "LAUNCH-P1B-500MC-WITH-BUDGET-GUARD"
POD_NAME_PREFIX = "p1b-physical-spectrum-500mc"


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_instant(value: str) -> dt.datetime:
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("balance observed_at must include an ISO-8601 timezone")
    return parsed.astimezone(dt.timezone.utc)


class RunPodREST:
    def __init__(self, api_key: str, base: str = API_BASE):
        self.api_key = api_key
        self.base = base.rstrip("/")

    def request(self, method: str, path: str, payload: dict | None = None):
        body = None if payload is None else json.dumps(payload).encode()
        request = urllib.request.Request(
            self.base + path,
            data=body,
            method=method,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
        except urllib.error.HTTPError as error:
            # Never include headers or the API key in an exception/receipt.
            raise ValueError(f"RunPod REST {method} {path} failed with HTTP {error.code}") from None
        return json.loads(raw) if raw else {}

    def list_pods(self):
        return self.request("GET", "/pods")

    def create_pod(self, payload: dict):
        return self.request("POST", "/pods", payload)

    def get_pod(self, pod_id: str):
        return self.request("GET", f"/pods/{pod_id}")

    def delete_pod(self, pod_id: str):
        return self.request("DELETE", f"/pods/{pod_id}")

    def stop_pod(self, pod_id: str):
        return self.request("POST", f"/pods/{pod_id}/stop", {})


def pod_rows(response) -> list[dict]:
    if isinstance(response, list):
        return response
    for key in ("pods", "data"):
        if isinstance(response, dict) and isinstance(response.get(key), list):
            return response[key]
    raise ValueError("unexpected RunPod pod-list response")


def validate_manifest(manifest: dict, expected_commit: str, contract: dict) -> None:
    head = prep.git("rev-parse", "HEAD")
    if expected_commit != head or manifest.get("git_commit") != head:
        raise ValueError("manifest, --expected-commit, and current HEAD must match exactly")
    if manifest.get("contract_id") != contract.get("contract_id"):
        raise ValueError("manifest contract_id mismatch")
    hashes = manifest.get("input_sha256")
    if not isinstance(hashes, dict) or set(hashes) != set(contract["required_tracked_inputs"]):
        raise ValueError("manifest input hash set does not match the contract")
    dirty = prep.git("status", "--porcelain", "--untracked-files=all", "--", *hashes)
    if dirty:
        raise ValueError("manifest inputs are not clean")
    for relative, expected in hashes.items():
        if prep.sha256(prep.ROOT / relative) != expected:
            raise ValueError(f"manifest hash mismatch: {relative}")
    image = manifest.get("container", {}).get("image", "")
    if "@sha256:" not in image or len(image.rsplit("@sha256:", 1)[1]) != 64:
        raise ValueError("container image is not pinned by immutable SHA-256 digest")


def validate_balance(path: Path, required_usd: float, max_age_minutes: int, now: dt.datetime) -> dict:
    receipt = json.loads(path.read_text())
    if receipt.get("source") != "runpod-console":
        raise ValueError("balance receipt source must be runpod-console")
    amount = receipt.get("amount_usd")
    if not isinstance(amount, (int, float)) or amount < required_usd:
        raise ValueError("recent RunPod balance receipt is insufficient")
    age = now - parse_instant(receipt.get("observed_at", ""))
    if age < dt.timedelta(0) or age > dt.timedelta(minutes=max_age_minutes):
        raise ValueError("RunPod balance receipt is stale or future-dated")
    return {"source": "runpod-console", "amount_usd": amount, "observed_at": receipt["observed_at"]}


def append_receipt(path: Path, event: dict) -> None:
    try:
        path.resolve().relative_to(prep.ROOT.resolve())
    except ValueError:
        pass
    else:
        ignored = prep.git("check-ignore", "-q", "--", str(path.relative_to(prep.ROOT)))
        # git check-ignore emits no output; git() raises when not ignored.
        del ignored
    path.parent.mkdir(parents=True, exist_ok=True)
    safe = {key: value for key, value in event.items() if "key" not in key.lower() and "authorization" not in key.lower()}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(safe, sort_keys=True) + "\n")


def pod_name(commit: str) -> str:
    return f"{POD_NAME_PREFIX}-{commit[:12]}"


def field(pod: dict, *names):
    for name in names:
        if name in pod:
            return pod[name]
    return None


def launch(*, client, manifest: dict, expected_commit: str, contract: dict, balance_path: Path,
           balance_max_age_minutes: int, max_hourly_rate: float, max_total_budget: float,
           max_runtime_minutes: int, gpu_type_id: str, receipt_path: Path,
           now_fn=utcnow) -> dict:
    validate_manifest(manifest, expected_commit, contract)
    if contract.get("provider_mutation_ready") is not True:
        raise ValueError("contract provider_mutation_ready is false; refusing before RunPod HTTP")
    if min(max_hourly_rate, max_total_budget, max_runtime_minutes) <= 0:
        raise ValueError("hourly rate, total budget, and runtime ceilings must be positive")
    runtime_budget = max_hourly_rate * max_runtime_minutes / 60
    if runtime_budget > max_total_budget + 1e-9:
        raise ValueError("hourly-rate × runtime exceeds --max-total-budget-usd")
    balance = validate_balance(balance_path, max_total_budget, balance_max_age_minutes, now_fn())
    name = pod_name(expected_commit)
    if any(field(pod, "name") == name for pod in pod_rows(client.list_pods())):
        raise ValueError(f"refusing duplicate deterministic pod name: {name}")
    image = manifest["container"]["image"]
    payload = {
        "name": name,
        "imageName": image,
        "gpuTypeIds": [gpu_type_id],
        "gpuCount": 1,
        "containerDiskInGb": 40,
        "volumeInGb": 40,
        "env": {"P1B_GIT_COMMIT": expected_commit, "P1B_MAX_RUNTIME_MINUTES": str(max_runtime_minutes)},
    }
    pod = client.create_pod(payload)
    pod_id = str(field(pod, "id", "podId") or "")
    cleanup_reason = None
    try:
        if not pod_id:
            raise ValueError("create response omitted pod id")
        cost = field(pod, "costPerHr", "desiredCostPerHr", "costPerHour")
        returned_image = field(pod, "imageName", "image")
        gpu_count = field(pod, "gpuCount")
        returned_gpu = field(pod, "gpuTypeId", "gpuType")
        status = str(field(pod, "status", "desiredStatus") or "").upper()
        if not isinstance(cost, (int, float)) or cost > max_hourly_rate:
            raise ValueError("create response exceeds hourly-rate ceiling")
        if (returned_image != image or gpu_count != 1 or returned_gpu != gpu_type_id
                or status not in {"CREATED", "RUNNING", "STARTING", "PENDING"}):
            raise ValueError("create response image/GPU/status mismatch")
    except Exception as error:
        cleanup_reason = str(error)
        if pod_id:
            client.delete_pod(pod_id)
        append_receipt(receipt_path, {"at": now_fn().isoformat(), "event": "create_mismatch_deleted",
                                     "pod_id": pod_id, "reason": cleanup_reason})
        raise
    deadline = now_fn() + dt.timedelta(minutes=max_runtime_minutes)
    event = {"at": now_fn().isoformat(), "event": "created", "pod_id": pod_id, "pod_name": name,
             "git_commit": expected_commit, "image": image, "gpu_count": 1,
             "gpu_type_id": gpu_type_id,
             "cost_per_hour_usd": cost, "max_total_budget_usd": max_total_budget,
             "deadline": deadline.isoformat(), "balance_receipt": balance}
    append_receipt(receipt_path, event)
    return event


def watchdog(client, pod_id: str, created_at: dt.datetime, deadline: dt.datetime, max_total_budget: float,
             cost_per_hour: float, receipt_path: Path, *, poll_seconds=30, now_fn=utcnow, sleep_fn=time.sleep):
    if created_at > deadline:
        raise ValueError("watchdog created_at must not be later than deadline")
    while True:
        now = now_fn()
        accrued = cost_per_hour * max(0, (now - created_at).total_seconds()) / 3600
        if now >= deadline or accrued >= max_total_budget:
            client.delete_pod(pod_id)
            reason = "deadline" if now >= deadline else "budget"
            append_receipt(receipt_path, {"at": now.isoformat(), "event": "watchdog_deleted",
                                         "pod_id": pod_id, "reason": reason})
            return reason
        pod = client.get_pod(pod_id)
        if str(field(pod, "status", "desiredStatus") or "").upper() in {"EXITED", "TERMINATED", "STOPPED"}:
            append_receipt(receipt_path, {"at": now.isoformat(), "event": "watchdog_observed_terminal",
                                         "pod_id": pod_id})
            return "terminal"
        sleep_fn(poll_seconds)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--balance-receipt", type=Path)
    parser.add_argument("--balance-max-age-minutes", type=int, default=15)
    parser.add_argument("--max-hourly-rate-usd", type=float)
    parser.add_argument("--max-total-budget-usd", type=float)
    parser.add_argument("--max-runtime-minutes", type=int)
    parser.add_argument("--gpu-type-id")
    parser.add_argument("--launch", action="store_true")
    parser.add_argument("--confirm")
    parser.add_argument("--watchdog", action="store_true")
    parser.add_argument("--pod-id")
    parser.add_argument("--deadline")
    parser.add_argument("--created-at")
    parser.add_argument("--cost-per-hour-usd", type=float)
    parser.add_argument("--terminate", action="store_true")
    parser.add_argument("--stop", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    key = os.environ.get("RUNPOD_API_KEY")
    if not key:
        raise ValueError("RUNPOD_API_KEY is required (never printed or stored)")
    client = RunPodREST(key)
    if args.stop:
        if not args.pod_id or args.confirm != "STOP-P1B-POD":
            raise ValueError("stop requires --pod-id and --confirm STOP-P1B-POD")
        client.stop_pod(args.pod_id)
        append_receipt(args.receipt, {"at": utcnow().isoformat(), "event": "operator_stopped", "pod_id": args.pod_id})
        return 0
    if args.terminate:
        if not args.pod_id or args.confirm != "TERMINATE-P1B-POD":
            raise ValueError("termination requires --pod-id and --confirm TERMINATE-P1B-POD")
        client.delete_pod(args.pod_id)
        append_receipt(args.receipt, {"at": utcnow().isoformat(), "event": "operator_deleted", "pod_id": args.pod_id})
        return 0
    if args.watchdog:
        if not all((args.pod_id, args.created_at, args.deadline, args.cost_per_hour_usd, args.max_total_budget_usd)):
            raise ValueError("watchdog requires pod id, created-at, deadline, hourly cost, and total budget")
        watchdog(client, args.pod_id, parse_instant(args.created_at), parse_instant(args.deadline), args.max_total_budget_usd,
                 args.cost_per_hour_usd, args.receipt)
        return 0
    manifest = json.loads(args.manifest.read_text())
    contract = json.loads(prep.DEFAULT_CONTRACT.read_text())
    validate_manifest(manifest, args.expected_commit, contract)
    if not args.launch:
        print("dry-run validated; no RunPod mutation performed")
        return 0
    if args.confirm != CONFIRMATION:
        raise ValueError(f"--launch requires --confirm {CONFIRMATION}")
    if contract.get("provider_mutation_ready") is not True:
        raise ValueError("contract provider_mutation_ready is false; refusing before RunPod HTTP")
    required = (args.balance_receipt, args.max_hourly_rate_usd, args.max_total_budget_usd,
                args.max_runtime_minutes, args.gpu_type_id)
    if any(value is None for value in required):
        raise ValueError("launch requires balance, rate, budget, runtime, and GPU type ceilings")
    launch(client=client, manifest=manifest, expected_commit=args.expected_commit, contract=contract,
           balance_path=args.balance_receipt, balance_max_age_minutes=args.balance_max_age_minutes,
           max_hourly_rate=args.max_hourly_rate_usd, max_total_budget=args.max_total_budget_usd,
           max_runtime_minutes=args.max_runtime_minutes, gpu_type_id=args.gpu_type_id,
           receipt_path=args.receipt)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"launcher failed: {error}", file=sys.stderr)
        raise SystemExit(2)
