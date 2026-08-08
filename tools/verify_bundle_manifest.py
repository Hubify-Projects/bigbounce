#!/usr/bin/env python3
"""Fail-fast verification for Git-tracked SHA-256 evidence bundles."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from pathlib import Path


LINE = re.compile(r"^([0-9a-fA-F]{64})\s+[* ]?(.+)$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git(root: Path, *args: str, check: bool = True):
    return subprocess.run(
        ["git", *args], cwd=root, text=True, capture_output=True, check=check
    )


def parse_manifest(manifest: Path) -> list[tuple[str, str]]:
    entries = []
    seen = set()
    for number, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        match = LINE.match(raw)
        if not match:
            raise ValueError(f"invalid manifest line {number}: {raw!r}")
        digest, relative = match.group(1).lower(), match.group(2)
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"unsafe manifest member at line {number}: {relative}")
        if relative in seen:
            raise ValueError(f"duplicate manifest member: {relative}")
        seen.add(relative)
        entries.append((digest, relative))
    if not entries:
        raise ValueError("manifest has no members")
    return entries


def verify(bundle_root: Path, manifest: Path | None = None) -> dict[str, list[str]]:
    bundle_root = bundle_root.resolve()
    manifest = (manifest or bundle_root / "MANIFEST.sha256").resolve()
    if not manifest.is_file():
        raise FileNotFoundError(f"manifest not found: {manifest}")
    repo = Path(git(bundle_root, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    report = {"missing": [], "hash_mismatch": [], "ignored": [], "untracked": []}
    for expected, relative in parse_manifest(manifest):
        path = (bundle_root / relative).resolve()
        if bundle_root not in path.parents and path != bundle_root:
            raise ValueError(f"manifest member escapes bundle root: {relative}")
        if not path.is_file():
            report["missing"].append(relative)
            continue
        if sha256(path) != expected:
            report["hash_mismatch"].append(relative)
        repo_relative = str(path.relative_to(repo))
        tracked = git(repo, "ls-files", "--error-unmatch", "--", repo_relative, check=False)
        if tracked.returncode != 0:
            ignored = git(repo, "check-ignore", "-q", "--", repo_relative, check=False)
            report["ignored" if ignored.returncode == 0 else "untracked"].append(relative)
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle_root", type=Path)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    report = verify(args.bundle_root, args.manifest)
    failures = False
    for category in ("missing", "hash_mismatch", "ignored", "untracked"):
        values = report[category]
        print(f"{category}: {len(values)}")
        for value in values:
            print(f"  {value}")
        failures |= bool(values)
    if failures:
        raise SystemExit(1)
    print("bundle manifest: PASS")


if __name__ == "__main__":
    main()
