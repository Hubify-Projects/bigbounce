#!/usr/bin/env python3
"""Atomic JSON publication and receipt validation for long NaMaster shards."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def receipt_path(path: Path) -> Path:
    return path.with_name(path.name + ".receipt.json")


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    try:
        with temporary.open("xb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if temporary.exists():
            temporary.unlink()


def publish_json(path: Path, payload: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    _atomic_write(path, encoded)
    receipt = {
        "schema_version": 1,
        "result_file": path.name,
        "result_bytes": path.stat().st_size,
        "result_sha256": sha256(path),
        **metadata,
    }
    _atomic_write(
        receipt_path(path),
        (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    )
    return receipt


def validate_json_receipt(
    path: Path,
    *,
    expected_suite: str | None = None,
    expected_configs: list[str] | None = None,
    expected_config_metadata: list[dict[str, Any]] | None = None,
    expected_n_real: int | None = None,
    expected_seed_start: int | None = None,
    expected_seed_end: int | None = None,
    expected_theory_operator: str | None = None,
    expected_code_sha256: str | None = None,
    expected_completed: int | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    receipt_file = receipt_path(path)
    if not path.is_file() or not receipt_file.is_file():
        raise FileNotFoundError(f"missing result/receipt pair for {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    receipt = json.loads(receipt_file.read_text(encoding="utf-8"))
    checks = {
        "result_file": path.name,
        "result_bytes": path.stat().st_size,
        "result_sha256": sha256(path),
    }
    if expected_suite is not None:
        checks["suite"] = expected_suite
    if expected_configs is not None:
        checks["config_names"] = expected_configs
    if expected_config_metadata is not None:
        checks["configs"] = expected_config_metadata
    if expected_n_real is not None:
        checks["n_real"] = expected_n_real
    if expected_seed_start is not None:
        checks["seed_start"] = expected_seed_start
    if expected_seed_end is not None:
        checks["seed_end"] = expected_seed_end
    if expected_theory_operator is not None:
        checks["theory_operator"] = expected_theory_operator
    if expected_code_sha256 is not None:
        checks["code_sha256"] = expected_code_sha256
    if expected_completed is not None:
        checks["completed"] = expected_completed
    mismatches = {
        key: {"expected": value, "actual": receipt.get(key)}
        for key, value in checks.items()
        if receipt.get(key) != value
    }
    if mismatches:
        raise ValueError(f"invalid receipt for {path}: {mismatches}")
    return payload, receipt
