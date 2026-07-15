#!/usr/bin/env python3
"""Build a deterministic, commit-bound arXiv source bundle.

The command is dry-run by default.  A bundle is written only with ``--write``
and only to the explicit ``--output`` path.  It performs no network calls.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import sys
import tarfile
from pathlib import Path, PurePosixPath
from typing import Any

from tools.prepare_paper_deposit import (
    CONFIG_PATH,
    DepositError,
    digest,
    load_config,
    paper_version,
    require_clean_commit_inputs,
    require_exact_commit,
)


def _inside(root: Path, raw: str | Path, label: str) -> Path:
    path = (root / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise DepositError(f"{label} escapes repository: {raw}") from exc
    return path


def _archive_name(raw: object) -> str:
    if not isinstance(raw, str) or not raw:
        raise DepositError("bundle asset lacks a non-empty archive_name")
    name = PurePosixPath(raw)
    if name.is_absolute() or ".." in name.parts or "." in name.parts or raw.endswith("/"):
        raise DepositError(f"unsafe bundle archive name: {raw}")
    return name.as_posix()


def _safe_member_name(name: str) -> None:
    path = PurePosixPath(name)
    if not name or path.is_absolute() or ".." in path.parts:
        raise DepositError(f"unsafe tar member: {name}")


def _tar_member(tarball: Path, member_name: str, expected_sha256: object) -> bytes:
    _safe_member_name(member_name)
    if not isinstance(expected_sha256, str) or len(expected_sha256) != 64:
        raise DepositError(f"tar member {member_name} requires an expected sha256")
    try:
        int(expected_sha256, 16)
    except ValueError as exc:
        raise DepositError(f"tar member {member_name} has an invalid expected sha256") from exc
    with tarfile.open(tarball, "r:*") as archive:
        matches = []
        for member in archive.getmembers():
            _safe_member_name(member.name)
            if member.issym() or member.islnk() or member.isdev():
                raise DepositError(f"unsupported tar member type: {member.name}")
            if member.name == member_name:
                matches.append(member)
        if len(matches) != 1 or not matches[0].isfile():
            raise DepositError(f"source tar must contain exactly one regular member: {member_name}")
        source = archive.extractfile(matches[0])
        if source is None:
            raise DepositError(f"could not read tar member: {member_name}")
        payload = source.read()
    actual = hashlib.sha256(payload).hexdigest()
    if actual != expected_sha256.lower():
        raise DepositError(
            f"tar member hash mismatch for {member_name}: expected {expected_sha256}, got {actual}"
        )
    return payload


def _bundle_bytes(files: list[tuple[str, bytes]]) -> bytes:
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode="w", format=tarfile.PAX_FORMAT) as archive:
            for name, payload in sorted(files):
                info = tarfile.TarInfo(name)
                info.size = len(payload)
                info.mtime = 0
                info.uid = info.gid = 0
                info.uname = info.gname = ""
                info.mode = 0o644
                archive.addfile(info, io.BytesIO(payload))
    return buffer.getvalue()


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.repo).resolve()
    if not (root / ".git").exists():
        raise DepositError(f"repository root is not a Git worktree: {root}")
    config_path = _inside(root, args.config, "config")
    output = _inside(root, args.output, "output")
    if output.exists():
        raise DepositError(f"refusing to overwrite bundle output: {output}")

    require_exact_commit(root, args.git_commit)
    config = load_config(config_path, args.paper)
    tex = _inside(root, config["tex"], "paper TeX")
    # Establish the configuration and version source as exact commit bytes
    # before interpreting either one.
    require_clean_commit_inputs(root, args.git_commit, [config_path, tex])
    version = paper_version(tex)
    assets = config.get("bundle_assets", [])
    tar_members = config.get("bundle_tar_members", [])
    if not isinstance(assets, list) or not isinstance(tar_members, list) or not (assets or tar_members):
        raise DepositError(
            f"configuration for {args.paper} lacks bundle_assets or bundle_tar_members"
        )

    tracked: list[Path] = [config_path, tex]
    parsed: list[tuple[str, Path, dict[str, Any]]] = []
    names: set[str] = set()
    for index, raw in enumerate(assets):
        if not isinstance(raw, dict):
            raise DepositError(f"bundle asset {index} must be an object")
        name = _archive_name(raw.get("archive_name"))
        if name in names:
            raise DepositError(f"duplicate bundle archive name: {name}")
        names.add(name)
        if "source" not in raw:
            raise DepositError(f"bundle asset {name} lacks source")
        source = _inside(root, str(raw["source"]).format(version=version), f"bundle asset {name}")
        tracked.append(source)
        parsed.append((name, source, raw))
    for index, raw in enumerate(tar_members):
        if not isinstance(raw, dict):
            raise DepositError(f"bundle tar member {index} must be an object")
        name = _archive_name(raw.get("archive_name"))
        if name in names:
            raise DepositError(f"duplicate bundle archive name: {name}")
        names.add(name)
        if "source_tarball" not in raw or "member" not in raw:
            raise DepositError(f"bundle tar member {name} lacks source_tarball or member")
        source = _inside(
            root,
            str(raw["source_tarball"]).format(version=version),
            f"bundle tar member {name}",
        )
        tracked.append(source)
        parsed.append((name, source, raw))

    require_clean_commit_inputs(root, args.git_commit, list(dict.fromkeys(tracked)))
    files: list[tuple[str, bytes]] = []
    records: list[dict[str, Any]] = []
    for name, source, raw in parsed:
        if "source_tarball" in raw:
            payload = _tar_member(source, str(raw["member"]), raw.get("expected_sha256"))
            origin = f"{source.relative_to(root).as_posix()}::{raw['member']}"
        else:
            payload = source.read_bytes()
            origin = source.relative_to(root).as_posix()
            expected = raw.get("sha256")
            if expected is not None and hashlib.sha256(payload).hexdigest() != str(expected).lower():
                raise DepositError(f"source hash mismatch for {origin}")
        files.append((name, payload))
        records.append({
            "archive_name": name,
            "source": origin,
            "size_bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        })

    payload = _bundle_bytes(files)
    receipt = {
        "schema": "bigbounce-exact-arxiv-bundle/v1",
        "paper_id": args.paper,
        "paper_version": version,
        "git_commit": args.git_commit,
        "dry_run": not args.write,
        "output": output.relative_to(root).as_posix(),
        "bundle_size_bytes": len(payload),
        "bundle_sha256": hashlib.sha256(payload).hexdigest(),
        "bundle_md5": hashlib.md5(payload).hexdigest(),
        "assets": sorted(records, key=lambda row: row["archive_name"]),
        "external_state_mutated": False,
    }
    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        try:
            with output.open("xb") as handle:
                handle.write(payload)
        except FileExistsError as exc:
            raise DepositError(f"refusing to overwrite bundle output: {output}") from exc
        if digest(output, "sha256") != receipt["bundle_sha256"]:
            output.unlink(missing_ok=True)
            raise DepositError("written bundle failed post-write hash verification")
    return receipt


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper", required=True)
    parser.add_argument("--git-commit", required=True, help="full exact Git commit")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--config", default=str(CONFIG_PATH))
    parser.add_argument("--output", required=True, help="explicit repository-confined output path")
    parser.add_argument("--write", action="store_true", help="write output; default is dry-run")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    try:
        receipt = build(parse_args(argv))
    except (DepositError, OSError, tarfile.TarError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
