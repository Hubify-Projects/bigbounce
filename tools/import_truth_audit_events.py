#!/usr/bin/env python3
"""Validate and append declarative truth-audited finding-event batches."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import sys
from typing import Any


DEFAULT_ENGINE = pathlib.Path(
    "~/.claude/scistack/hubstack/learning-loop/"
    "r-round-finding-archive/scripts/finding_event.py"
).expanduser()


class BatchError(ValueError):
    pass


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_engine(path: pathlib.Path):
    spec = importlib.util.spec_from_file_location("hubstack_finding_event", path)
    if spec is None or spec.loader is None:
        raise BatchError(f"cannot load finding-event engine: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_json(path: pathlib.Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require_exact_keys(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        raise BatchError(f"{label}: fields differ; expected {sorted(keys)}")
    return value


def verified_file(repo: pathlib.Path, row: dict[str, Any], label: str) -> pathlib.Path:
    require_exact_keys(row, {"path", "sha256"}, label)
    relative = pathlib.PurePosixPath(row["path"])
    if relative.is_absolute() or ".." in relative.parts:
        raise BatchError(f"{label}.path: unsafe relative path")
    path = repo / relative
    if not path.is_file():
        raise BatchError(f"{label}.path: missing {relative}")
    actual = sha256(path)
    if actual != row["sha256"]:
        raise BatchError(f"{label}.sha256: expected {row['sha256']}, got {actual}")
    return path


def build_events(
    batch: dict[str, Any],
    inventory: dict[str, Any],
    repo: pathlib.Path,
    engine,
) -> list[dict[str, Any]]:
    require_exact_keys(
        batch,
        {
            "schema_version", "paper", "source", "pdf", "truth_audit",
            "catalog", "receipts",
        },
        "batch",
    )
    if batch["schema_version"] != "truth-audit-event-batch/v1":
        raise BatchError("batch.schema_version: expected truth-audit-event-batch/v1")
    paper = require_exact_keys(batch["paper"], {"id", "version"}, "paper")
    source = require_exact_keys(
        batch["source"], {"round_id", "round_type"}, "source"
    )
    pdf = require_exact_keys(batch["pdf"], {"sha256", "pages"}, "pdf")
    truth = require_exact_keys(
        batch["truth_audit"], {"path", "sha256", "audited_at"}, "truth_audit"
    )
    catalog = require_exact_keys(
        batch["catalog"], {"version", "updated_at"}, "catalog"
    )
    verified_file(
        repo, {"path": truth["path"], "sha256": truth["sha256"]}, "truth_audit"
    )
    engine.validate_inventory(inventory)
    inventory_by_path = {row["path"]: row for row in inventory["receipts"]}
    if not isinstance(batch["receipts"], list) or not batch["receipts"]:
        raise BatchError("receipts: expected non-empty array")

    events: list[dict[str, Any]] = []
    seen_finding_ids: set[tuple[str, str]] = set()
    for index, receipt in enumerate(batch["receipts"]):
        label = f"receipts[{index}]"
        require_exact_keys(
            receipt,
            {"path", "sha256", "occurred_at", "reviewer", "findings"},
            label,
        )
        verified_file(
            repo,
            {"path": receipt["path"], "sha256": receipt["sha256"]},
            label,
        )
        inventory_row = inventory_by_path.get(receipt["path"])
        if inventory_row is None:
            raise BatchError(f"{label}.path: absent from canonical inventory")
        if inventory_row["status"] != "ok":
            raise BatchError(f"{label}.path: inventory status is not ok")
        if inventory_row["sha256"] != receipt["sha256"]:
            raise BatchError(f"{label}.sha256: differs from canonical inventory")
        findings = receipt["findings"]
        if not isinstance(findings, list):
            raise BatchError(f"{label}.findings: expected array")
        if inventory_row["finding_count"] != len(findings):
            raise BatchError(
                f"{label}.findings: expected {inventory_row['finding_count']}, "
                f"got {len(findings)}"
            )
        reviewer = require_exact_keys(
            receipt["reviewer"], {"provider", "model", "reviewer_id"}, f"{label}.reviewer"
        )
        for finding_index, finding in enumerate(findings):
            finding_label = f"{label}.findings[{finding_index}]"
            require_exact_keys(
                finding,
                {
                    "finding_id", "severity", "summary", "truth_verdict",
                    "truth_evidence", "classification", "pattern_ids",
                    "preflight_checked", "preflight_intercepted", "closure",
                },
                finding_label,
            )
            key = (receipt["path"], finding["finding_id"])
            if key in seen_finding_ids:
                raise BatchError(f"{finding_label}.finding_id: duplicate in receipt")
            seen_finding_ids.add(key)
            closure = require_exact_keys(
                finding["closure"],
                {
                    "status", "action", "closed_in_version", "evidence",
                    "regression_of_event_id",
                },
                f"{finding_label}.closure",
            )
            event = {
                "schema_version": "finding-event/v1",
                "occurred_at": receipt["occurred_at"],
                "paper": paper,
                "source": {
                    **source,
                    "artifact_path": truth["path"],
                },
                "pdf": pdf,
                "reviewer": reviewer,
                "raw_receipt": {
                    "path": receipt["path"],
                    "sha256": receipt["sha256"],
                },
                "finding": {
                    "finding_id": finding["finding_id"],
                    "severity": finding["severity"],
                    "summary": finding["summary"],
                },
                "truth_audit": {
                    "verdict": finding["truth_verdict"],
                    "received_at": receipt["occurred_at"],
                    "audited_at": truth["audited_at"],
                    "evidence": finding["truth_evidence"],
                },
                "pattern": {
                    "classification": finding["classification"],
                    "pattern_ids": finding["pattern_ids"],
                    "catalog_version": catalog["version"],
                    "catalog_updated_at": catalog["updated_at"],
                    "preflight_checked": finding["preflight_checked"],
                    "preflight_intercepted": finding["preflight_intercepted"],
                },
                "closure": closure,
            }
            stamped = engine.stamp_identity(event)
            engine.validate_event(stamped)
            events.append(stamped)
    return events


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=pathlib.Path)
    parser.add_argument("--inventory", type=pathlib.Path, required=True)
    parser.add_argument("--ledger", type=pathlib.Path, required=True)
    parser.add_argument("--engine", type=pathlib.Path, default=DEFAULT_ENGINE)
    parser.add_argument("--append", action="store_true")
    args = parser.parse_args()
    try:
        repo = pathlib.Path.cwd().resolve()
        engine = load_engine(args.engine)
        batch = read_json(args.batch)
        inventory = read_json(args.inventory)
        events = build_events(batch, inventory, repo, engine)
        statuses = []
        if args.append:
            for event in events:
                statuses.append(engine.append_event(args.ledger, event))
            engine.read_ledger(args.ledger)
        print(json.dumps({
            "valid": True,
            "mode": "append" if args.append else "dry-run",
            "events": len(events),
            "appended": statuses.count("appended"),
            "idempotent": statuses.count("idempotent"),
            "event_ids": [event["event_id"] for event in events],
        }, indent=2, sort_keys=True))
        return 0
    except (OSError, json.JSONDecodeError, BatchError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
