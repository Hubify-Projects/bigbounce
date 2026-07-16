#!/usr/bin/env python3
"""Append-only closure evidence for immutable finding-event records."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
from typing import Any

SCHEMA = "finding-closure-event/v1"
IDENTITY_FIELDS = {"closure_event_id", "content_hash"}


class ClosureError(ValueError):
    pass


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def stamp(event: dict[str, Any]) -> dict[str, Any]:
    result = {key: value for key, value in event.items() if key not in IDENTITY_FIELDS}
    digest = hashlib.sha256(canonical(result)).hexdigest()
    result["closure_event_id"] = f"fcev1_{digest[:24]}"
    result["content_hash"] = f"sha256:{digest}"
    return result


def git_bytes(repo: pathlib.Path, commit: str, path: str) -> bytes:
    process = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=repo,
        capture_output=True,
    )
    if process.returncode:
        raise ClosureError(f"cannot read {commit}:{path}")
    return process.stdout


def finding_ids(ledger: pathlib.Path) -> set[str]:
    result = set()
    for number, line in enumerate(ledger.read_text().splitlines(), 1):
        try:
            result.add(json.loads(line)["event_id"])
        except (json.JSONDecodeError, KeyError) as exc:
            raise ClosureError(f"{ledger}:{number}: invalid finding event") from exc
    return result


def validate(
    event: dict[str, Any],
    *,
    repo: pathlib.Path,
    finding_event_ids: set[str],
) -> dict[str, Any]:
    required = {
        "schema_version", "closure_event_id", "content_hash", "finding_event_id",
        "status", "closed_in_version", "closure_commit", "occurred_at",
        "action", "evidence",
    }
    if not isinstance(event, dict) or set(event) != required:
        raise ClosureError("closure event fields differ")
    if event["schema_version"] != SCHEMA or event["status"] != "CLOSED":
        raise ClosureError("invalid schema or closure status")
    if event["finding_event_id"] not in finding_event_ids:
        raise ClosureError("finding_event_id is absent from finding ledger")
    for field in ("closed_in_version", "closure_commit", "occurred_at", "action"):
        if not isinstance(event[field], str) or not event[field].strip():
            raise ClosureError(f"{field}: expected non-empty string")
    evidence = event["evidence"]
    if not isinstance(evidence, list) or not evidence:
        raise ClosureError("evidence: expected non-empty array")
    for index, row in enumerate(evidence):
        if not isinstance(row, dict) or set(row) != {"path", "sha256"}:
            raise ClosureError(f"evidence[{index}]: invalid fields")
        actual = hashlib.sha256(
            git_bytes(repo, event["closure_commit"], row["path"])
        ).hexdigest()
        if actual != row["sha256"]:
            raise ClosureError(
                f"evidence[{index}].sha256: expected {row['sha256']}, got {actual}"
            )
    expected = stamp(event)
    if event["closure_event_id"] != expected["closure_event_id"]:
        raise ClosureError("closure_event_id mismatch")
    if event["content_hash"] != expected["content_hash"]:
        raise ClosureError("content_hash mismatch")
    return event


def read_closures(
    ledger: pathlib.Path, *, repo: pathlib.Path, finding_event_ids: set[str]
) -> list[dict[str, Any]]:
    if not ledger.exists():
        return []
    events = []
    for number, line in enumerate(ledger.read_text().splitlines(), 1):
        try:
            events.append(
                validate(
                    json.loads(line),
                    repo=repo,
                    finding_event_ids=finding_event_ids,
                )
            )
        except (json.JSONDecodeError, ClosureError) as exc:
            raise ClosureError(f"{ledger}:{number}: {exc}") from exc
    return events


def append(
    ledger: pathlib.Path,
    event: dict[str, Any],
    *,
    repo: pathlib.Path,
    finding_event_ids: set[str],
) -> str:
    validate(event, repo=repo, finding_event_ids=finding_event_ids)
    existing = read_closures(
        ledger, repo=repo, finding_event_ids=finding_event_ids
    )
    for row in existing:
        if row["closure_event_id"] == event["closure_event_id"]:
            return "idempotent"
        if row["finding_event_id"] == event["finding_event_id"]:
            raise ClosureError("finding already has a different closure event")
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as handle:
        handle.write(canonical(event).decode() + "\n")
    return "appended"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("append", "validate", "project"))
    parser.add_argument("closure_ledger", type=pathlib.Path)
    parser.add_argument("--findings", type=pathlib.Path, required=True)
    parser.add_argument("--event", type=pathlib.Path)
    args = parser.parse_args()
    try:
        repo = pathlib.Path.cwd()
        ids = finding_ids(args.findings)
        if args.command == "append":
            if args.event is None:
                raise ClosureError("--event is required for append")
            raw = json.loads(args.event.read_text())
            event = stamp(raw)
            status = append(
                args.closure_ledger, event, repo=repo, finding_event_ids=ids
            )
            print(json.dumps({"status": status, "closure_event_id": event["closure_event_id"]}))
        else:
            events = read_closures(
                args.closure_ledger, repo=repo, finding_event_ids=ids
            )
            if args.command == "validate":
                print(json.dumps({"valid": True, "closures": len(events)}))
            else:
                print(json.dumps({
                    "schema_version": "finding-closure-projection/v1",
                    "closed_findings": len(events),
                    "closures": {
                        event["finding_event_id"]: {
                            "status": event["status"],
                            "closed_in_version": event["closed_in_version"],
                            "closure_commit": event["closure_commit"],
                            "closure_event_id": event["closure_event_id"],
                        }
                        for event in events
                    },
                }, indent=2, sort_keys=True))
        return 0
    except (OSError, json.JSONDecodeError, ClosureError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
