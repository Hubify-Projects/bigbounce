#!/usr/bin/env python3
"""Download, byte-verify, and semantically validate the exact public P4 Catalog C."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
CONTRACT_PATH = HERE / "SEMANTIC_CONTRACT.json"
HF_RESOLVE = "https://huggingface.co/datasets/{repo}/resolve/{revision}/{path}"
GH_RAW = "https://raw.githubusercontent.com/{repo}/{commit}/{path}"


class ContractError(RuntimeError):
    pass


def safe_relative_path(raw: Any) -> Path:
    if not isinstance(raw, str) or not raw:
        raise ContractError("inventory path must be a non-empty string")
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts or path == Path("."):
        raise ContractError(f"unsafe inventory path: {raw!r}")
    return path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def verify(path: Path, *, size: int, sha256: str) -> None:
    if not path.is_file() or path.is_symlink():
        raise ContractError(f"missing or unsafe file: {path}")
    if path.stat().st_size != size:
        raise ContractError(f"byte-count mismatch: {path.name}")
    if sha256_file(path) != sha256:
        raise ContractError(f"SHA-256 mismatch: {path.name}")


def download(url: str, destination: Path, *, force: bool = False) -> None:
    if destination.exists() and not force:
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.download")
    temporary.unlink(missing_ok=True)
    try:
        with urllib.request.urlopen(url) as response, temporary.open("wb") as output:
            while chunk := response.read(1024 * 1024):
                output.write(chunk)
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def fetch_verified(url: str, destination: Path, record: dict[str, Any], *, force: bool) -> None:
    try:
        if force:
            destination.unlink(missing_ok=True)
        download(url, destination, force=force)
        verify(destination, size=record["bytes"], sha256=record["sha256"])
    except (OSError, KeyError, urllib.error.URLError) as exc:
        raise ContractError(f"download/verification failed for {destination.name}: {type(exc).__name__}") from None


def run(work_dir: Path, receipt_path: Path, *, force: bool = False) -> None:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    dataset = contract["dataset"]
    checkout = work_dir / "pinned-source"
    release = work_dir / "release"

    for key in ("validator_source", "validator_schema_source", "validator_reproducer_source"):
        record = contract[key]
        destination = checkout / record["path"]
        url = GH_RAW.format(
            repo=record["repository"], commit=record["git_commit"], path=record["path"]
        )
        fetch_verified(url, destination, record, force=force)

    provider = dataset["provider_receipt"]
    provider_path = release / "PROVIDER_RECEIPT.json"
    provider_url = HF_RESOLVE.format(
        repo=dataset["repo_id"], revision=dataset["provider_receipt_revision"],
        path=provider["path"],
    )
    fetch_verified(provider_url, provider_path, provider, force=force)
    inventory = json.loads(provider_path.read_text(encoding="utf-8"))
    if inventory.get("data_commit") != dataset["data_revision"]:
        raise ContractError("provider receipt data revision mismatch")
    if inventory.get("path_prefix") != dataset["path_prefix"]:
        raise ContractError("provider receipt path-prefix mismatch")

    for record in inventory["files"]:
        relative_path = safe_relative_path(record.get("path"))
        remote_path = f"{dataset['path_prefix']}/{relative_path.as_posix()}"
        url = HF_RESOLVE.format(
            repo=dataset["repo_id"], revision=dataset["data_revision"], path=remote_path
        )
        fetch_verified(url, release / relative_path, record, force=force)

    validator = checkout / contract["validator_source"]["path"]
    command = [
        sys.executable, str(validator), "--validate-only", "--output-dir", str(release),
        "--validation-receipt", str(receipt_path),
    ]
    completed = subprocess.run(command, cwd=checkout, check=False)
    if completed.returncode != 0:
        raise ContractError(f"pinned semantic validator exited {completed.returncode}")
    print(f"PASS: semantic receipt written to {receipt_path}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, default=Path("p4-semantic-audit"))
    parser.add_argument("--receipt", type=Path, default=Path("p4-semantic-receipt.json"))
    parser.add_argument("--force-download", action="store_true")
    args = parser.parse_args(argv)
    try:
        run(args.work_dir.resolve(), args.receipt.resolve(), force=args.force_download)
    except (ContractError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
