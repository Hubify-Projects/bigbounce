#!/usr/bin/env python3
"""Fail-closed publisher for P4's v1.0.259 strict-primary overlay."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RELEASE = ROOT / "pipelines/p2_chirality/apjs_release_v1.0.259_strict"
REPO_ID = "bamfai/galaxy-chirality-catalog"
PATH_PREFIX = "apjs-release/v1.0.259-strict-primary"
REQUIRED = {
    "MANIFEST.json",
    "PRIMARY_REPRODUCTION.json",
    "README.md",
    "SCHEMA.json",
    "SHA256SUMS",
    "primary_strict_fixed_occupancy_amps_10000.npy",
    "reproduce_p4_primary_null_v1_0_259.py",
}


class PublishError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(release: Path) -> list[dict[str, Any]]:
    names = {path.name for path in release.iterdir() if path.is_file()}
    missing = sorted(REQUIRED - names)
    if missing:
        raise PublishError("missing strict-release products: " + ", ".join(missing))
    if any(path.is_symlink() for path in release.iterdir()):
        raise PublishError("symlinks are forbidden")
    manifest = json.loads((release / "MANIFEST.json").read_text())
    if manifest.get("schema") != "p4-apjs-strict-primary-manifest/v1":
        raise PublishError("strict release manifest schema mismatch")
    if manifest.get("base_catalog", {}).get("sha256") != (
        "139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
    ):
        raise PublishError("base catalog hash mismatch")
    reproduction = json.loads((release / "PRIMARY_REPRODUCTION.json").read_text())
    if reproduction.get("status") != "PASS" or not all(
        reproduction.get("hard_gates", {}).values()
    ):
        raise PublishError("strict primary reproduction does not pass")
    records = []
    for path in sorted(release.iterdir()):
        if path.is_file():
            records.append(
                {
                    "path": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    return records


def publish(release: Path, *, mutate: bool = False, token: str | None = None) -> dict:
    release = release.resolve()
    files = inventory(release)
    receipt = {
        "schema": "p4-hf-strict-primary-provider-receipt/v1",
        "paper": "P4",
        "paper_version": "v1.0.259",
        "repo_id": REPO_ID,
        "repo_type": "dataset",
        "path_prefix": PATH_PREFIX,
        "files": files,
        "published": False,
        "status": "dry-run",
    }
    if not mutate:
        return receipt
    token = token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    if not token:
        raise PublishError("--publish requires HF_TOKEN or HUGGINGFACE_TOKEN")
    try:
        from huggingface_hub import HfApi
    except ImportError as exc:
        raise PublishError("huggingface_hub is unavailable") from exc
    api = HfApi(token=token)
    try:
        commit = api.upload_folder(
            folder_path=str(release),
            path_in_repo=PATH_PREFIX,
            repo_id=REPO_ID,
            repo_type="dataset",
            commit_message="Publish P4 v1.0.259 strict-primary contract",
        )
    except Exception as exc:
        raise PublishError(f"Hugging Face upload failed: {type(exc).__name__}") from None
    revision = getattr(commit, "oid", None) or getattr(commit, "commit_id", None)
    if not revision:
        raise PublishError("Hugging Face upload returned no revision")
    try:
        info = api.dataset_info(REPO_ID, revision=revision, files_metadata=True)
    except Exception as exc:
        raise PublishError(f"remote verification failed: {type(exc).__name__}") from None
    remote = {item.rfilename: getattr(item, "size", None) for item in info.siblings}
    failures = []
    for record in files:
        remote_path = f"{PATH_PREFIX}/{record['path']}"
        if remote.get(remote_path) != record["bytes"]:
            failures.append(remote_path)
    if failures:
        raise PublishError("remote byte verification failed: " + ", ".join(failures))
    return {
        **receipt,
        "published": True,
        "status": "published",
        "data_commit": revision,
        "verification_revision": revision,
        "verification": "remote paths and byte sizes matched",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-dir", type=Path, default=DEFAULT_RELEASE)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--receipt-json", type=Path)
    args = parser.parse_args()
    try:
        receipt = publish(args.release_dir, mutate=args.publish)
    except (OSError, ValueError, PublishError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.receipt_json:
        args.receipt_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
