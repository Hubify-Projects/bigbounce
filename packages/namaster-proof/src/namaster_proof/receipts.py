"""Atomic per-file JSON writes and fail-closed content receipt validation."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Mapping

PROTECTED_RECEIPT_FIELDS = frozenset(
    {"schema_version", "result_file", "result_bytes", "result_sha256"}
)


def sha256(path: Path) -> str:
    """Return a streaming SHA-256 digest for a file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _read_bytes(path: Path) -> bytes:
    """Read one immutable file-handle snapshot."""
    with path.open("rb") as handle:
        return handle.read()


def receipt_path(path: Path) -> Path:
    """Return the canonical sidecar receipt path for a JSON result."""
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
        if os.name == "posix":
            directory_fd = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    finally:
        temporary.unlink(missing_ok=True)


def publish_json(
    path: Path, payload: Mapping[str, Any], metadata: Mapping[str, Any]
) -> dict[str, Any]:
    """Publish a result and sidecar with atomic replacement of each file.

    The two files are replaced sequentially rather than as one filesystem
    transaction. The receipt detects uncoordinated result mutation; callers
    must assert trusted execution metadata with ``validate_json_receipt``.
    """
    overlap = PROTECTED_RECEIPT_FIELDS.intersection(metadata)
    if overlap:
        raise ValueError(
            "metadata cannot override protected receipt fields: "
            + ", ".join(sorted(overlap))
        )
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    _atomic_write(path, encoded)
    receipt = {
        "schema_version": 1,
        "result_file": path.name,
        "result_bytes": len(encoded),
        "result_sha256": hashlib.sha256(encoded).hexdigest(),
        **metadata,
    }
    _atomic_write(
        receipt_path(path),
        (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    )
    return receipt


def verify_json_receipt(path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Verify one coherent result snapshot against one receipt snapshot."""
    sidecar = receipt_path(path)
    if not path.is_file() or not sidecar.is_file():
        raise FileNotFoundError(f"missing result/receipt pair for {path}")
    result_bytes = _read_bytes(path)
    receipt_bytes = _read_bytes(sidecar)
    payload = json.loads(result_bytes.decode("utf-8"))
    receipt = json.loads(receipt_bytes.decode("utf-8"))
    if not isinstance(payload, dict) or not isinstance(receipt, dict):
        raise ValueError("result and receipt must both be JSON objects")
    expected = {
        "schema_version": 1,
        "result_file": path.name,
        "result_bytes": len(result_bytes),
        "result_sha256": hashlib.sha256(result_bytes).hexdigest(),
    }
    mismatches = {
        key: {"expected": value, "actual": receipt.get(key)}
        for key, value in expected.items()
        if receipt.get(key) != value
    }
    if mismatches:
        raise ValueError(f"invalid receipt for {path}: {mismatches}")
    return payload, receipt


def validate_json_receipt(
    path: Path, *, expected: Mapping[str, Any] | None = None, **legacy_expected: Any
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Verify a result receipt and optional declared metadata.

    ``expected`` is the general interface. Keyword arguments beginning with
    ``expected_`` are accepted for compatibility with the original P1B helper.
    """
    payload, receipt = verify_json_receipt(path)
    checks = dict(expected or {})
    for key, value in legacy_expected.items():
        if not key.startswith("expected_"):
            raise TypeError(f"unsupported validation argument: {key}")
        if value is not None:
            checks[key.removeprefix("expected_")] = value
    mismatches = {
        key: {"expected": value, "actual": receipt.get(key)}
        for key, value in checks.items()
        if receipt.get(key) != value
    }
    if mismatches:
        raise ValueError(f"invalid receipt for {path}: {mismatches}")
    return payload, receipt
