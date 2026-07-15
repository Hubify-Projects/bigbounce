#!/usr/bin/env python3
"""Generate a fail-closed exact-commit bootstrap command from a bound manifest."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import shlex
from pathlib import Path


REPO_URL = "https://github.com/Hubify-Projects/bigbounce.git"


def canonical_manifest_bytes(manifest: dict) -> bytes:
    return (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")


def generate(manifest: dict, manifest_path: Path, workspace: Path, state_dir: Path) -> list[str]:
    commit = manifest.get("git_commit", "")
    if len(commit) != 40 or not manifest.get("input_sha256"):
        raise ValueError("manifest is not commit/hash bound")
    install = manifest.get("container", {}).get("install") or []
    if not install:
        raise ValueError("manifest has no dependency installation contract")
    repo = workspace / "bigbounce"
    remote_manifest = state_dir / "bound-production-manifest.json"
    encoded_manifest = base64.b64encode(canonical_manifest_bytes(manifest)).decode("ascii")
    manifest_sha256 = hashlib.sha256(canonical_manifest_bytes(manifest)).hexdigest()
    checks = "\n".join(
        f"printf '%s  %s\\n' {shlex.quote(digest)} {shlex.quote(relative)} | sha256sum -c -"
        for relative, digest in sorted(manifest["input_sha256"].items())
    )
    script = f"""set -euo pipefail
test ! -e {shlex.quote(str(workspace))}
mkdir -p {shlex.quote(str(workspace))}
mkdir -p {shlex.quote(str(state_dir))}
printf '%s' {shlex.quote(encoded_manifest)} | base64 --decode > {shlex.quote(str(remote_manifest))}.tmp
printf '%s  %s\n' {shlex.quote(manifest_sha256)} {shlex.quote(str(remote_manifest))}.tmp | sha256sum -c -
mv {shlex.quote(str(remote_manifest))}.tmp {shlex.quote(str(remote_manifest))}
git clone --no-checkout {shlex.quote(REPO_URL)} {shlex.quote(str(repo))}
cd {shlex.quote(str(repo))}
git checkout --detach {shlex.quote(commit)}
test "$(git rev-parse HEAD)" = {shlex.quote(commit)}
{checks}
{chr(10).join(install)}
python3 reproducibility/p1_namaster_500mc/scripts/remote_production_runner.py --manifest {shlex.quote(str(remote_manifest))} --repo {shlex.quote(str(repo))} --state-dir {shlex.quote(str(state_dir))}
"""
    return ["bash", "-lc", script]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--workspace", type=Path, required=True)
    p.add_argument("--state-dir", type=Path, required=True)
    args = p.parse_args()
    argv = generate(json.loads(args.manifest.read_text()), args.manifest, args.workspace, args.state_dir)
    print(json.dumps(argv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
