#!/usr/bin/env python3
"""Independent fail-closed watchdog for a durable P1B RunPod launch intent."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

import runpod_budget_launcher as launcher


SCHEMA = "p1b-runpod-watchdog-intent/v1"
REQUIRED_KEYS = {
    "schema", "active", "git_commit", "pod_name", "created_not_before", "deadline",
    "max_hourly_rate_usd", "max_total_budget_usd",
}
TERMINAL = {"EXITED", "TERMINATED", "STOPPED", "DELETED"}


def _instant(value: object, label: str) -> dt.datetime:
    if not isinstance(value, str):
        raise ValueError(f"intent {label} must be an ISO-8601 string")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise ValueError(f"intent {label} is not valid ISO-8601") from None
    if parsed.tzinfo is None:
        raise ValueError(f"intent {label} must include a timezone")
    return parsed.astimezone(dt.timezone.utc)


def validate_intent(value: object) -> dict:
    if not isinstance(value, dict) or set(value) != REQUIRED_KEYS:
        raise ValueError("intent must contain exactly the watchdog v1 fields")
    if value["schema"] != SCHEMA:
        raise ValueError("intent schema mismatch")
    if not isinstance(value["active"], bool):
        raise ValueError("intent active must be boolean")
    commit = value["git_commit"]
    if (not isinstance(commit, str) or len(commit) != 40 or
            any(c not in "0123456789abcdef" for c in commit)):
        raise ValueError("intent git_commit must be a full lowercase SHA-1")
    if value["pod_name"] != launcher.pod_name(commit):
        raise ValueError("intent pod_name is not deterministic for git_commit")
    created = _instant(value["created_not_before"], "created_not_before")
    deadline = _instant(value["deadline"], "deadline")
    if deadline <= created:
        raise ValueError("intent deadline must be after created_not_before")
    for key in ("max_hourly_rate_usd", "max_total_budget_usd"):
        number = value[key]
        if isinstance(number, bool) or not isinstance(number, (int, float)) or number <= 0:
            raise ValueError(f"intent {key} must be a positive finite number")
        if not float(number) < float("inf"):
            raise ValueError(f"intent {key} must be a positive finite number")
    return {**value, "created_not_before": created, "deadline": deadline}


def load_intent(path: Path | None, env: dict[str, str] | None = None) -> dict:
    environ = os.environ if env is None else env
    if path is not None:
        raw = path.read_text(encoding="utf-8")
    else:
        raw = environ.get("P1B_RUNPOD_WATCHDOG_INTENT_JSON", "")
        if not raw:
            raise ValueError("--intent or P1B_RUNPOD_WATCHDOG_INTENT_JSON is required")
    return validate_intent(json.loads(raw))


def _metadata_commit(pod: dict) -> str | None:
    """Return advertised full commit metadata, if the provider exposes it."""
    found: set[str] = set()

    def walk(value: object) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                normalized = str(key).lower().replace("-", "_")
                if normalized in {"git_commit", "p1b_git_commit", "commit_sha"} and isinstance(child, str):
                    found.add(child)
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(pod)
    if not found:
        return None
    if len(found) != 1:
        return "AMBIGUOUS"
    return next(iter(found))


def _price(pod: dict) -> float | None:
    value = launcher.field(pod, "costPerHr", "costPerHour", "hourlyCost", "costPerHourUsd")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if 0 < number < float("inf") else None


def _pod_id(pod: dict) -> str:
    value = launcher.field(pod, "id", "podId")
    if not isinstance(value, str) or not value:
        raise ValueError("matching pod has no usable id")
    return value


def run_once(client, intent: dict, *, now: dt.datetime | None = None,
             terminate_fn=launcher.terminate_confirmed) -> dict:
    intent = validate_intent({
        **intent,
        "created_not_before": (intent["created_not_before"].isoformat()
                               if isinstance(intent.get("created_not_before"), dt.datetime)
                               else intent.get("created_not_before")),
        "deadline": (intent["deadline"].isoformat()
                     if isinstance(intent.get("deadline"), dt.datetime) else intent.get("deadline")),
    })
    observed = (now or launcher.utcnow()).astimezone(dt.timezone.utc)
    if not intent["active"]:
        return {"schema": "p1b-runpod-watchdog-result/v1", "action": "none", "reason": "inactive_intent"}
    matches = [pod for pod in launcher.pod_rows(client.list_pods())
               if launcher.field(pod, "name") == intent["pod_name"]]
    if not matches:
        return {"schema": "p1b-runpod-watchdog-result/v1", "action": "none", "reason": "no_matching_pod"}

    actionable: list[tuple[dict, str]] = []
    terminal_count = 0
    elapsed_hours = max(0.0, (observed - intent["created_not_before"]).total_seconds()) / 3600
    accrued = elapsed_hours * float(intent["max_hourly_rate_usd"])
    for pod in matches:
        metadata = _metadata_commit(pod)
        if metadata is not None and metadata != intent["git_commit"]:
            raise ValueError("matching pod name has conflicting or ambiguous full-commit metadata")
        status = str(launcher.field(pod, "status", "desiredStatus") or "").upper()
        if status in TERMINAL:
            terminal_count += 1
            continue
        price = _price(pod)
        if len(matches) > 1:
            reason = "duplicate_matches"
        elif observed >= intent["deadline"]:
            reason = "deadline"
        elif accrued >= float(intent["max_total_budget_usd"]):
            reason = "budget"
        elif price is None:
            reason = "hourly_price_ambiguous"
        elif price > float(intent["max_hourly_rate_usd"]):
            reason = "hourly_price_exceeded"
        else:
            continue
        actionable.append((pod, reason))

    if not actionable:
        reason = "already_terminal" if terminal_count == len(matches) else "within_limits"
        return {"schema": "p1b-runpod-watchdog-result/v1", "action": "none", "reason": reason,
                "matching_pods": len(matches), "terminal_pods": terminal_count}

    deleted: list[str] = []
    reasons: set[str] = set()
    for pod, reason in actionable:
        pod_id = _pod_id(pod)
        reasons.add(reason)
        if not terminate_fn(client, pod_id):
            raise ValueError(f"pod deletion could not be confirmed for {pod_id}")
        deleted.append(pod_id)
    return {"schema": "p1b-runpod-watchdog-result/v1", "action": "delete_confirmed",
            "reasons": sorted(reasons), "deleted_pod_ids": sorted(deleted),
            "matching_pods": len(matches), "terminal_pods": terminal_count}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intent", type=Path)
    args = parser.parse_args()
    key = os.environ.get("RUNPOD_API_KEY")
    if not key:
        raise ValueError("RUNPOD_API_KEY is required (never printed or stored)")
    result = run_once(launcher.RunPodREST(key), load_intent(args.intent))
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"watchdog failed: {error}", file=sys.stderr)
        raise SystemExit(2)
