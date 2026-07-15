#!/usr/bin/env python3
"""Verify a git-bound analysis-artifact manifest without fetching secrets/data."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


class ManifestError(ValueError):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def safe_manifest(root: Path, path: Path) -> Path:
    root = root.resolve(strict=True)
    resolved = path.resolve(strict=True)
    if not resolved.is_file() or not resolved.is_relative_to(root):
        raise ManifestError(f"manifest is outside repository root: {path}")
    return resolved


def git_blobs(root: Path, commit: str, paths: list[str]) -> dict[str, bytes]:
    process = subprocess.Popen(
        ["git", "cat-file", "--batch"], cwd=root,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    assert process.stdin is not None and process.stdout is not None
    records: dict[str, bytes] = {}
    try:
        for path in paths:
            process.stdin.write(f"{commit}:{path}\n".encode())
            process.stdin.flush()
            header = process.stdout.readline().decode("utf-8", "replace").strip()
            if header.endswith(" missing"):
                raise ManifestError(f"artifact missing at base commit: {path}")
            fields = header.split()
            if len(fields) != 3 or fields[1] != "blob" or not fields[2].isdigit():
                raise ManifestError(f"unexpected git object for {path}: {header}")
            size = int(fields[2])
            data = process.stdout.read(size)
            separator = process.stdout.read(1)
            if len(data) != size or separator != b"\n":
                raise ManifestError(f"truncated git blob for {path}")
            records[path] = data
    finally:
        process.stdin.close()
        stderr = process.stderr.read().decode("utf-8", "replace") if process.stderr else ""
        process.stdout.close()
        if process.stderr:
            process.stderr.close()
        rc = process.wait()
        if rc and not sys.exc_info()[0]:
            raise ManifestError(f"git cat-file failed: {stderr.strip()}")
    return records


def verify_manifest(root: Path, manifest_path: Path) -> dict[str, Any]:
    root = root.resolve(strict=True)
    manifest_path = safe_manifest(root, manifest_path)
    raw = manifest_path.read_bytes()
    try:
        manifest = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ManifestError(f"invalid manifest JSON: {exc}") from exc
    commit = manifest.get("base_repository_commit")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ManifestError("base_repository_commit must be a full lowercase Git SHA")
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=root,
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise ManifestError("artifacts must be a non-empty list")
    paths = [item.get("path") for item in artifacts if isinstance(item, dict)]
    if len(paths) != len(artifacts) or any(not isinstance(path, str) or not path for path in paths):
        raise ManifestError("every artifact requires a path")
    if len(paths) != len(set(paths)):
        raise ManifestError("artifact paths must be unique")
    blobs = git_blobs(root, commit, paths)
    storage_counts: collections.Counter[str] = collections.Counter()
    for item in artifacts:
        path = item["path"]
        data = blobs[path]
        storage = item.get("storage")
        storage_counts[storage] += 1
        if item.get("local_git_blob_bytes") != len(data):
            raise ManifestError(
                f"blob byte mismatch at {commit[:12]} for {path}: "
                f"recorded {item.get('local_git_blob_bytes')}, actual {len(data)}"
            )
        if item.get("local_git_blob_sha256") != sha256(data):
            raise ManifestError(f"blob SHA-256 mismatch at {commit[:12]} for {path}")
        if storage == "git-blob":
            if item.get("scientific_payload_bytes") != len(data) or item.get(
                "scientific_payload_sha256"
            ) != sha256(data):
                raise ManifestError(f"scientific payload fields mismatch Git blob for {path}")
        elif storage == "git-lfs-pointer":
            pointer = data.decode("ascii", "strict")
            oid = re.search(r"^oid sha256:([0-9a-f]{64})$", pointer, re.MULTILINE)
            size = re.search(r"^size ([0-9]+)$", pointer, re.MULTILINE)
            if not oid or not size:
                raise ManifestError(f"malformed Git LFS pointer for {path}")
            if oid.group(1) != item.get("lfs_oid_sha256") or int(size.group(1)) != item.get(
                "lfs_declared_bytes"
            ):
                raise ManifestError(f"Git LFS OID/size mismatch for {path}")
        else:
            raise ManifestError(f"unsupported storage type {storage!r} for {path}")
    result = {
        "schema": "bigbounce.analysis-artifact-manifest-verification/v1",
        "manifest_path": manifest_path.relative_to(root).as_posix(),
        "manifest_bytes": len(raw),
        "manifest_sha256": sha256(raw),
        "base_repository_commit": commit,
        "paper_version": manifest.get("paper_version"),
        "artifact_count": len(artifacts),
        "storage_counts": dict(sorted(storage_counts.items())),
        "verdict": "PASS",
    }
    result["core_sha256"] = sha256(canonical_bytes(result))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(json.dumps(verify_manifest(args.project_root, args.manifest), indent=2, sort_keys=True))
        return 0
    except (ManifestError, OSError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
