#!/usr/bin/env python3
"""Fail-closed RunPod REST v1 launcher for the frozen P1B production job."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shlex
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import prepare_runpod_production as prep
import generate_remote_bootstrap as bootstrap
import verify_runpod_s3_retention as s3verify
import retain_remote_production as retention


API_BASE = "https://rest.runpod.io/v1"
GITHUB_API_BASE = "https://api.github.com"
GITHUB_REPOSITORY = "Hubify-Projects/bigbounce"
WATCHDOG_INTENT_VARIABLE = "P1B_RUNPOD_INTENT"
CONFIRMATION = "LAUNCH-P1B-500MC-WITH-BUDGET-GUARD"
POD_NAME_PREFIX = "p1b-physical-spectrum-500mc"
CONTAINER_TIMEOUT_KILL_AFTER_SECONDS = 60


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


class GitHubActionsVariables:
    """Publish non-secret durable watchdog intent outside the launching host."""

    def __init__(self, token: str, repository: str = GITHUB_REPOSITORY,
                 base: str = GITHUB_API_BASE):
        if repository.count("/") != 1:
            raise ValueError("GitHub repository must be OWNER/REPO")
        self.token = token
        self.repository = repository
        self.base = base.rstrip("/")

    def request(self, method: str, path: str, payload: dict | None = None):
        body = None if payload is None else json.dumps(payload).encode()
        request = urllib.request.Request(
            self.base + path, data=body, method=method,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
        except urllib.error.HTTPError as error:
            raise ValueError(f"GitHub REST {method} {path} failed with HTTP {error.code}") from None
        return json.loads(raw) if raw else {}

    @property
    def variable_path(self) -> str:
        return f"/repos/{self.repository}/actions/variables/{WATCHDOG_INTENT_VARIABLE}"

    def publish_and_verify(self, intent: dict) -> None:
        encoded = json.dumps(intent, sort_keys=True, separators=(",", ":"))
        try:
            self.request("GET", self.variable_path)
        except ValueError as error:
            if "HTTP 404" not in str(error):
                raise
            self.request("POST", f"/repos/{self.repository}/actions/variables", {
                "name": WATCHDOG_INTENT_VARIABLE, "value": encoded,
            })
        else:
            self.request("PATCH", self.variable_path, {"name": WATCHDOG_INTENT_VARIABLE, "value": encoded})
        observed = self.request("GET", self.variable_path)
        if observed.get("name") != WATCHDOG_INTENT_VARIABLE or observed.get("value") != encoded:
            raise ValueError("durable GitHub watchdog intent read-back mismatch")


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


def watchdog_intent(*, commit: str, created_not_before: dt.datetime,
                    max_runtime_minutes: int, max_hourly_rate: float,
                    max_total_budget: float) -> dict:
    if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit):
        raise ValueError("watchdog intent requires a lowercase full commit SHA")
    if created_not_before.tzinfo is None:
        raise ValueError("watchdog intent creation time must include a timezone")
    if min(max_runtime_minutes, max_hourly_rate, max_total_budget) <= 0:
        raise ValueError("watchdog intent ceilings must be positive")
    started = created_not_before.astimezone(dt.timezone.utc)
    return {
        "schema": "p1b-runpod-watchdog-intent/v1",
        "active": True,
        "git_commit": commit,
        "pod_name": pod_name(commit),
        "created_not_before": started.isoformat(),
        "deadline": (started + dt.timedelta(minutes=max_runtime_minutes)).isoformat(),
        "max_hourly_rate_usd": max_hourly_rate,
        "max_total_budget_usd": max_total_budget,
    }


def container_timeout_command(remote_argv: list[str], *, runtime_seconds: int,
                              status_path: Path, commit: str) -> str:
    """Wrap the complete bootstrap in a hard deadline with an atomic status record."""
    if remote_argv[:2] != ["bash", "-lc"] or len(remote_argv) != 3:
        raise ValueError("bound bootstrap did not produce exact bash entrypoint/start command")
    if not isinstance(runtime_seconds, int) or isinstance(runtime_seconds, bool) or runtime_seconds <= 0:
        raise ValueError("container runtime ceiling must be a positive integer number of seconds")
    if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit):
        raise ValueError("container timeout status requires a lowercase full commit SHA")
    if not status_path.is_absolute():
        raise ValueError("container timeout status path must be absolute")
    status_dir = status_path.parent
    inner = shlex.join(remote_argv)
    # GNU timeout returns 124 when its deadline fires, including when the TERM
    # grace period escalates to KILL. Preserve every other bootstrap exit code.
    return f"""set -euo pipefail
mkdir -p {shlex.quote(str(status_dir))}
status_path={shlex.quote(str(status_path))}
status_tmp="$status_path.tmp.$$"
started_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
set +e
timeout --foreground --signal=TERM --kill-after={CONTAINER_TIMEOUT_KILL_AFTER_SECONDS}s {runtime_seconds}s {inner}
exit_code=$?
set -e
if [ "$exit_code" -eq 0 ]; then
  state=completed
elif [ "$exit_code" -eq 124 ]; then
  state=timed_out
else
  state=failed
fi
finished_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf '{{"schema":"p1b-container-runtime/v1","git_commit":"%s","state":"%s","exit_code":%s,"runtime_ceiling_seconds":%s,"term_grace_seconds":%s,"started_at":"%s","finished_at":"%s"}}\n' {shlex.quote(commit)} "$state" "$exit_code" {runtime_seconds} {CONTAINER_TIMEOUT_KILL_AFTER_SECONDS} "$started_at" "$finished_at" > "$status_tmp"
sync "$status_tmp"
mv "$status_tmp" "$status_path"
sync {shlex.quote(str(status_dir))}
exit "$exit_code"
"""


def field(pod: dict, *names):
    for name in names:
        if name in pod:
            return pod[name]
    return None


def write_recovery(path: Path, value: dict) -> None:
    safe = {key: val for key, val in value.items()
            if "key" not in key.lower() and "authorization" not in key.lower()}
    path.parent.mkdir(parents=True, exist_ok=True)
    retention.atomic_json(path, safe)


def terminate_confirmed(client, pod_id: str, *, attempts: int = 3,
                        sleep_fn=time.sleep) -> bool:
    """Best-effort delete with retry, stop fallback, and terminal confirmation."""
    for attempt in range(attempts):
        try:
            client.delete_pod(pod_id)
        except Exception:
            if attempt == 0:
                try:
                    client.stop_pod(pod_id)
                except Exception:
                    pass
        try:
            pod = client.get_pod(pod_id)
        except Exception as error:
            # REST 404 is represented without response secrets by RunPodREST.
            if "HTTP 404" in str(error):
                return True
        else:
            if str(field(pod, "status", "desiredStatus") or "").upper() in {"TERMINATED", "DELETED"}:
                return True
        if attempt + 1 < attempts:
            sleep_fn(1)
    return False


def launch(*, client, manifest: dict, expected_commit: str, contract: dict, balance_path: Path,
           balance_max_age_minutes: int, max_hourly_rate: float, max_total_budget: float,
           max_runtime_minutes: int, gpu_type_id: str, receipt_path: Path,
           network_volume_id: str | None = None, datacenter_id: str | None = None,
           s3_client=None, retention_staging: Path | None = None,
           retention_receipt: Path | None = None, poll_seconds: int = 30,
           recovery_path: Path | None = None, github_variables=None,
           now_fn=utcnow, sleep_fn=time.sleep) -> dict:
    validate_manifest(manifest, expected_commit, contract)
    if contract.get("provider_mutation_ready") is not True:
        raise ValueError("contract provider_mutation_ready is false; refusing before RunPod HTTP")
    if not network_volume_id:
        raise ValueError("networkVolumeId is required before RunPod HTTP")
    if datacenter_id not in s3verify.RUNPOD_S3_ENDPOINTS:
        raise ValueError("supported network-volume datacenter is required before RunPod HTTP")
    if retention_staging is None or retention_receipt is None or s3_client is None:
        raise ValueError("S3 client, local staging, and verification receipt are required before RunPod HTTP")
    if min(max_hourly_rate, max_total_budget, max_runtime_minutes) <= 0:
        raise ValueError("hourly rate, total budget, and runtime ceilings must be positive")
    runtime_budget = max_hourly_rate * max_runtime_minutes / 60
    if runtime_budget > max_total_budget + 1e-9:
        raise ValueError("hourly-rate × runtime exceeds --max-total-budget-usd")
    balance = validate_balance(balance_path, max_total_budget, balance_max_age_minutes, now_fn())
    name = pod_name(expected_commit)
    if any(field(pod, "name") == name for pod in pod_rows(client.list_pods())):
        raise ValueError(f"refusing duplicate deterministic pod name: {name}")
    if github_variables is None:
        raise ValueError("independent GitHub watchdog intent publisher is required before RunPod HTTP")
    intent_started = now_fn()
    github_variables.publish_and_verify(watchdog_intent(
        commit=expected_commit, created_not_before=intent_started,
        max_runtime_minutes=max_runtime_minutes, max_hourly_rate=max_hourly_rate,
        max_total_budget=max_total_budget,
    ))
    image = manifest["container"]["image"]
    remote_argv = bootstrap.generate(
        manifest, Path("/tmp/bound-production-manifest.json"), Path("/tmp/p1b-work"),
        Path("/tmp/p1b-state"), Path("/workspace/p1b-retention"),
    )
    container_command = container_timeout_command(
        remote_argv, runtime_seconds=max_runtime_minutes * 60,
        status_path=Path("/workspace/p1b-container-status") / f"{expected_commit}.json",
        commit=expected_commit,
    )
    payload = {
        "name": name,
        "imageName": image,
        "gpuTypeIds": [gpu_type_id],
        "gpuCount": 1,
        "containerDiskInGb": 40,
        "networkVolumeId": network_volume_id,
        "dataCenterIds": [datacenter_id],
        "cloudType": "SECURE",
        "volumeMountPath": "/workspace",
        "dockerEntrypoint": remote_argv[:2],
        "dockerStartCmd": [container_command],
        "env": {"P1B_GIT_COMMIT": expected_commit, "P1B_MAX_RUNTIME_MINUTES": str(max_runtime_minutes)},
    }
    pod = client.create_pod(payload)
    pod_id = str(field(pod, "id", "podId") or "")
    if not pod_id:
        raise ValueError("create response omitted pod id")
    recovery_path = recovery_path or receipt_path.with_suffix(".recovery.json")
    cleanup_required = True
    try:
        # First post-create write is an atomic recovery ledger. If it fails,
        # the enclosing exception path immediately attempts confirmed cleanup.
        write_recovery(recovery_path, {
            "schema": "p1b-runpod-recovery/v1", "state": "owns_live_pod",
            "at": now_fn().isoformat(), "pod_id": pod_id, "git_commit": expected_commit,
            "network_volume_id": network_volume_id, "datacenter_id": datacenter_id,
        })
        cost = field(pod, "costPerHr", "desiredCostPerHr", "costPerHour")
        returned_image = field(pod, "imageName", "image")
        gpu_count = field(pod, "gpuCount")
        returned_gpu = field(pod, "gpuTypeId", "gpuType")
        returned_volume = field(pod, "networkVolume") or {}
        status = str(field(pod, "status", "desiredStatus") or "").upper()
        if not isinstance(cost, (int, float)) or cost > max_hourly_rate:
            raise ValueError("create response exceeds hourly-rate ceiling")
        if (returned_image != image or gpu_count != 1 or returned_gpu != gpu_type_id
                or returned_volume.get("id") != network_volume_id
                or returned_volume.get("dataCenterId") != datacenter_id
                or status not in {"CREATED", "RUNNING", "STARTING", "PENDING"}):
            raise ValueError("create response image/GPU/volume/status mismatch")
        deadline = now_fn() + dt.timedelta(minutes=max_runtime_minutes)
        event = {"at": now_fn().isoformat(), "event": "created", "pod_id": pod_id, "pod_name": name,
                 "git_commit": expected_commit, "image": image, "gpu_count": 1,
                 "gpu_type_id": gpu_type_id, "network_volume_id": network_volume_id,
                 "cost_per_hour_usd": cost, "max_total_budget_usd": max_total_budget,
                 "deadline": deadline.isoformat(), "balance_receipt": balance}
        append_receipt(receipt_path, event)
        result = supervise(
            client=client, s3_client=s3_client, pod_id=pod_id, manifest=manifest,
            network_volume_id=network_volume_id, datacenter_id=datacenter_id,
            retention_staging=retention_staging, retention_receipt=retention_receipt,
            receipt_path=receipt_path, created_at=now_fn(), deadline=deadline,
            max_total_budget=max_total_budget, max_hourly_rate=max_hourly_rate,
            cost_per_hour=cost, poll_seconds=poll_seconds, now_fn=now_fn, sleep_fn=sleep_fn,
        )
        cleanup_required = False  # supervisor owns every normal terminal outcome
        try:
            write_recovery(recovery_path, {"schema": "p1b-runpod-recovery/v1", "state": result,
                                           "at": now_fn().isoformat(), "pod_id": pod_id})
        except Exception:
            # Never turn a terminal-unverified/manual-review outcome into an
            # automatic deletion merely because the final ledger update failed.
            pass
        return {**event, "supervision_result": result}
    except Exception as error:
        confirmed = terminate_confirmed(client, pod_id, sleep_fn=sleep_fn)
        cleanup_required = False
        try:
            append_receipt(receipt_path, {
                "at": now_fn().isoformat(), "event": "post_create_exception_cleanup",
                "pod_id": pod_id, "error_class": type(error).__name__,
                "delete_confirmed": confirmed,
            })
        except Exception:
            pass
        try:
            write_recovery(recovery_path, {
                "schema": "p1b-runpod-recovery/v1",
                "state": "exception_cleanup_confirmed" if confirmed else "manual_cleanup_required",
                "at": now_fn().isoformat(), "pod_id": pod_id,
                "error_class": type(error).__name__,
            })
        except Exception:
            pass
        raise
    finally:
        if cleanup_required:
            terminate_confirmed(client, pod_id, sleep_fn=sleep_fn)


def retention_prefix(manifest: dict) -> str:
    return f"p1b-retention/{manifest['contract_id']}--{manifest['git_commit']}"


def supervise(*, client, s3_client, pod_id: str, manifest: dict,
              network_volume_id: str, datacenter_id: str,
              retention_staging: Path, retention_receipt: Path, receipt_path: Path,
              created_at: dt.datetime, deadline: dt.datetime, max_total_budget: float,
              max_hourly_rate: float, cost_per_hour: float, poll_seconds=30,
              now_fn=utcnow, sleep_fn=time.sleep) -> str:
    """Continuously supervise cost and independently verify S3 before deletion."""
    while True:
        now = now_fn()
        accrued = cost_per_hour * max(0, (now - created_at).total_seconds()) / 3600
        if now >= deadline or accrued >= max_total_budget:
            confirmed = terminate_confirmed(client, pod_id, sleep_fn=sleep_fn)
            reason = "deadline" if now >= deadline else "budget"
            append_receipt(receipt_path, {"at": now.isoformat(), "event": "supervisor_cost_deleted_unverified",
                                         "pod_id": pod_id, "reason": reason,
                                         "delete_confirmed": confirmed})
            return reason

        try:
            pod = client.get_pod(pod_id)
        except Exception:
            append_receipt(receipt_path, {"at": now.isoformat(), "event": "supervisor_get_ambiguous",
                                         "pod_id": pod_id})
            sleep_fn(poll_seconds)
            continue
        live_cost = field(pod, "costPerHr", "desiredCostPerHr", "costPerHour")
        if not isinstance(live_cost, (int, float)) or live_cost > max_hourly_rate:
            confirmed = terminate_confirmed(client, pod_id, sleep_fn=sleep_fn)
            append_receipt(receipt_path, {"at": now.isoformat(), "event": "supervisor_price_deleted_unverified",
                                         "pod_id": pod_id, "reason": "hourly_rate_ambiguous_or_exceeded",
                                         "delete_confirmed": confirmed})
            return "hourly_rate"

        ambiguity = None
        try:
            s3verify.download_and_verify(
                client=s3_client, network_volume_id=network_volume_id,
                datacenter_id=datacenter_id, prefix=retention_prefix(manifest),
                staging_root=retention_staging, manifest=manifest,
                receipt_path=retention_receipt,
            )
        except Exception as error:
            # Provider exceptions can contain request metadata; persist only a
            # non-sensitive classification, never exception text or credentials.
            ambiguity = type(error).__name__
        else:
            confirmed = terminate_confirmed(client, pod_id, sleep_fn=sleep_fn)
            append_receipt(receipt_path, {"at": now.isoformat(), "event": "verified_retention_then_deleted",
                                         "pod_id": pod_id, "verification_receipt": str(retention_receipt),
                                         "delete_confirmed": confirmed})
            if not confirmed:
                raise ValueError("verified retention but pod deletion could not be confirmed")
            return "verified"

        status = str(field(pod, "status", "desiredStatus") or "").upper()
        if status in {"EXITED", "TERMINATED", "STOPPED"}:
            append_receipt(receipt_path, {"at": now.isoformat(), "event": "terminal_retained_for_manual_review",
                                         "pod_id": pod_id, "s3_ambiguity": ambiguity})
            return "terminal_unverified"
        sleep_fn(poll_seconds)


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
    parser.add_argument("--network-volume-id")
    parser.add_argument("--datacenter-id", choices=sorted(s3verify.RUNPOD_S3_ENDPOINTS))
    parser.add_argument("--retention-staging", type=Path)
    parser.add_argument("--retention-verification-receipt", type=Path)
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
    github_token = os.environ.get("P1B_WATCHDOG_GITHUB_TOKEN")
    if not github_token:
        raise ValueError("P1B_WATCHDOG_GITHUB_TOKEN is required for durable pre-create intent")
    required = (args.balance_receipt, args.max_hourly_rate_usd, args.max_total_budget_usd,
                args.max_runtime_minutes, args.gpu_type_id, args.network_volume_id,
                args.datacenter_id, args.retention_staging, args.retention_verification_receipt)
    if any(value is None for value in required):
        raise ValueError("launch requires balance, rate, budget, runtime, and GPU type ceilings")
    launch(client=client, manifest=manifest, expected_commit=args.expected_commit, contract=contract,
           balance_path=args.balance_receipt, balance_max_age_minutes=args.balance_max_age_minutes,
           max_hourly_rate=args.max_hourly_rate_usd, max_total_budget=args.max_total_budget_usd,
           max_runtime_minutes=args.max_runtime_minutes, gpu_type_id=args.gpu_type_id,
           receipt_path=args.receipt, network_volume_id=args.network_volume_id,
           datacenter_id=args.datacenter_id, s3_client=s3verify.s3_client(args.datacenter_id),
           retention_staging=args.retention_staging,
           retention_receipt=args.retention_verification_receipt,
           github_variables=GitHubActionsVariables(github_token))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"launcher failed: {error}", file=sys.stderr)
        raise SystemExit(2)
