#!/usr/bin/env python3
"""Atomically retain a completed P1B production set on an off-workspace volume."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path


MARKER = "RETENTION_COMPLETE.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def atomic_json(path: Path, value: dict) -> None:
    payload = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with tmp.open("wb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, path)
    fsync_dir(path.parent)


def _assert_separate_absolute(root: Path, repo: Path, state: Path) -> None:
    if not root.is_absolute():
        raise ValueError("retention root must be an explicit absolute path")
    resolved = [root.resolve(), repo.resolve(), state.resolve()]
    for index, left in enumerate(resolved):
        for right in resolved[index + 1:]:
            if left == right or left in right.parents or right in left.parents:
                raise ValueError("retention root, repository, and state directory must be distinct")


def source_files(repo: Path, state: Path, manifest: dict) -> dict[str, Path]:
    complete = state / "production.complete.json"
    bound = state / "bound-production-manifest.json"
    required = {"state/production.complete.json": complete, "state/bound-production-manifest.json": bound}
    for job in (manifest.get("execution_jobs") or []) + [manifest.get("merge_job") or {}]:
        name = job.get("name")
        if not name:
            raise ValueError("manifest contains unnamed job")
        for suffix in ("receipt.json", "status.json", "log"):
            required[f"state/{name}.{suffix}"] = state / f"{name}.{suffix}"
        for relative in job.get("outputs") or []:
            required[f"repo/{relative}"] = repo / relative
    missing = sorted(name for name, path in required.items() if not path.is_file())
    if missing:
        raise ValueError(f"retention inputs missing: {missing}")
    final = json.loads(complete.read_text())
    if final.get("state") != "complete" or final.get("git_commit") != manifest.get("git_commit"):
        raise ValueError("production completion receipt has wrong state or commit")
    if final.get("contract_id") != manifest.get("contract_id"):
        raise ValueError("production completion receipt has wrong contract")
    if json.loads(bound.read_text()) != manifest:
        raise ValueError("bound manifest does not match retention manifest")
    return required


def inventory(paths: dict[str, Path]) -> list[dict]:
    return [{"path": name, "bytes": path.stat().st_size, "sha256": sha256(path)}
            for name, path in sorted(paths.items())]


def validate_retention(directory: Path, *, commit: str | None = None,
                       contract_id: str | None = None) -> dict:
    marker_path = directory / MARKER
    if not marker_path.is_file():
        raise ValueError("retention completion marker is missing")
    marker = json.loads(marker_path.read_text())
    if marker.get("schema") != "p1b-runpod-retention/v1":
        raise ValueError("unknown retention schema")
    if commit and marker.get("git_commit") != commit:
        raise ValueError("retention commit mismatch")
    if contract_id and marker.get("contract_id") != contract_id:
        raise ValueError("retention contract mismatch")
    declared = {item["path"]: item for item in marker.get("inventory", [])}
    actual = {str(path.relative_to(directory)): path for path in directory.rglob("*")
              if path.is_file() and path.name != MARKER}
    if set(declared) != set(actual):
        raise ValueError("retention inventory is incomplete or contains extras")
    for name, path in actual.items():
        item = declared[name]
        if item.get("bytes") != path.stat().st_size or item.get("sha256") != sha256(path):
            raise ValueError(f"retained file hash mismatch: {name}")
    return marker


def retain(repo: Path, state: Path, retention_root: Path, manifest: dict) -> dict:
    _assert_separate_absolute(retention_root, repo, state)
    sources = source_files(repo, state, manifest)
    source_inventory = inventory(sources)
    name = f"{manifest['contract_id']}--{manifest['git_commit']}"
    final_dir = retention_root / name
    staging = retention_root / f".{name}.staging"
    retention_root.mkdir(parents=True, exist_ok=True)
    fsync_dir(retention_root)
    if final_dir.exists():
        marker = validate_retention(final_dir, commit=manifest["git_commit"],
                                    contract_id=manifest["contract_id"])
        if marker.get("inventory") != source_inventory:
            raise ValueError("completed retention set conflicts with current source set")
        return marker
    if staging.exists():
        raise ValueError("partial retention staging directory exists; inspect before retry")
    staging.mkdir()
    fsync_dir(retention_root)
    try:
        for item in source_inventory:
            source = sources[item["path"]]
            target = staging / item["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            with target.open("rb") as stream:
                os.fsync(stream.fileno())
            if target.stat().st_size != item["bytes"] or sha256(target) != item["sha256"]:
                raise ValueError(f"copy verification failed: {item['path']}")
            fsync_dir(target.parent)
        marker = {
            "schema": "p1b-runpod-retention/v1", "state": "complete",
            "contract_id": manifest["contract_id"], "git_commit": manifest["git_commit"],
            "contract_sha256": (manifest.get("input_sha256") or {}).get(
                "reproducibility/p1_namaster_500mc/runpod_production_contract.json"),
            "bound_manifest_sha256": sha256(state / "bound-production-manifest.json"),
            "inventory": source_inventory,
        }
        atomic_json(staging / MARKER, marker)  # Always written after every payload file.
        validate_retention(staging, commit=manifest["git_commit"], contract_id=manifest["contract_id"])
        os.replace(staging, final_dir)
        fsync_dir(retention_root)
        return validate_retention(final_dir, commit=manifest["git_commit"], contract_id=manifest["contract_id"])
    except Exception:
        # Preserve partial staging as forensic evidence; never silently replace it.
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--state-dir", type=Path)
    parser.add_argument("--retention-root", type=Path)
    args = parser.parse_args()
    if args.validate:
        validate_retention(args.validate.resolve())
    else:
        if not all((args.manifest, args.repo, args.state_dir, args.retention_root)):
            parser.error("retention requires --manifest, --repo, --state-dir, and --retention-root")
        manifest = json.loads(args.manifest.read_text())
        retain(args.repo.resolve(), args.state_dir.resolve(), args.retention_root, manifest)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"retention failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
