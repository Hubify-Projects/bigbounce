#!/usr/bin/env python3
"""Run the hash-bound P1B production manifest locally; never call a provider."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from prepare_runpod_production import build_execution
from retain_remote_production import retain


CONTRACT_RELATIVE = Path("reproducibility/p1_namaster_500mc/runpod_production_contract.json")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    payload = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")
    with tmp.open("wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)
    directory_fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def git_head(repo: Path) -> str:
    p = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, text=True,
                       capture_output=True, check=False)
    if p.returncode:
        raise ValueError(p.stderr.strip() or "cannot read git HEAD")
    return p.stdout.strip()


def validate_binding(repo: Path, manifest: dict) -> None:
    if git_head(repo) != manifest.get("git_commit"):
        raise ValueError("repository HEAD does not match manifest git_commit")
    hashes = manifest.get("input_sha256") or {}
    if not hashes:
        raise ValueError("manifest has no input_sha256 binding")
    for relative, expected in hashes.items():
        path = repo / relative
        if not path.is_file() or sha256(path) != expected:
            raise ValueError(f"manifest input hash mismatch: {relative}")
        committed = subprocess.run(
            ["git", "show", f"HEAD:{relative}"], cwd=repo,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )
        if committed.returncode or hashlib.sha256(committed.stdout).hexdigest() != expected:
            raise ValueError(f"manifest input is not the exact committed blob: {relative}")
    contract = json.loads((repo / CONTRACT_RELATIVE).read_text())
    expected = build_execution(contract)
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise ValueError(f"manifest executable semantics mismatch checked-out contract: {key}")


def verified_receipt(receipt: Path, repo: Path, job: dict, commit: str) -> bool:
    if not receipt.is_file():
        return False
    try:
        data = json.loads(receipt.read_text())
    except (OSError, json.JSONDecodeError):
        return False
    if data.get("state") != "complete" or data.get("job") != job["name"]:
        return False
    if data.get("git_commit") != commit or data.get("command") != job["command"]:
        return False
    expected = {p: sha256(repo / p) for p in job["outputs"] if (repo / p).is_file()}
    return len(expected) == len(job["outputs"]) and data.get("output_sha256") == expected


def execute_job(repo: Path, state_dir: Path, job: dict, commit: str) -> None:
    receipt = state_dir / f"{job['name']}.receipt.json"
    status = state_dir / f"{job['name']}.status.json"
    if verified_receipt(receipt, repo, job, commit):
        return
    receipt.unlink(missing_ok=True)
    # An unverified invocation must prove it created every declared artifact;
    # stale files can never satisfy a no-op or failed command.
    for relative in job["outputs"]:
        (repo / relative).unlink(missing_ok=True)
    log = state_dir / f"{job['name']}.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    atomic_json(status, {
        "job": job["name"], "state": "running", "git_commit": commit,
        "command": job["command"], "started_at": started,
    })
    try:
        with log.open("wb") as stream:
            result = subprocess.run(["bash", "-lc", job["command"]], cwd=repo,
                                    stdout=stream, stderr=subprocess.STDOUT, check=False)
            stream.flush()
            os.fsync(stream.fileno())
        if result.returncode:
            raise RuntimeError(f"command exited {result.returncode}")
        missing = [p for p in job["outputs"] if not (repo / p).is_file()]
        if missing:
            raise RuntimeError(f"missing outputs: {missing}")
        completed = {
            "job": job["name"], "state": "complete", "git_commit": commit,
            "command": job["command"], "started_at": started,
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "log_sha256": sha256(log),
            "output_sha256": {p: sha256(repo / p) for p in job["outputs"]},
        }
        atomic_json(receipt, completed)
        atomic_json(status, completed)
    except Exception as exc:
        receipt.unlink(missing_ok=True)
        failure = {
            "job": job["name"], "state": "failed", "started_at": started,
            "reason": str(exc),
        }
        if log.is_file():
            failure["log_sha256"] = sha256(log)
        atomic_json(status, failure)
        atomic_json(state_dir / f"{job['name']}.failed.json", failure)
        raise RuntimeError(f"job failed: {job['name']}: {exc}") from exc


def run(repo: Path, manifest: dict, state_dir: Path, retention_root: Path | None = None) -> dict:
    validate_binding(repo, manifest)
    # A prior success must never survive as apparent evidence for a new partial
    # or failed invocation. It is re-promoted only after every receipt verifies.
    (state_dir / "production.complete.json").unlink(missing_ok=True)
    jobs = manifest.get("execution_jobs") or []
    if len(jobs) != 9 or [j.get("kind") for j in jobs].count("canonical") != 1 or [j.get("kind") for j in jobs].count("robustness") != 8:
        raise ValueError("manifest must contain one canonical and exactly eight robustness jobs")
    if any(not j.get("command") or not j.get("outputs") for j in jobs):
        raise ValueError("every production job requires a command and outputs")
    commit = manifest["git_commit"]
    for job in jobs:
        execute_job(repo, state_dir, job, commit)
    merge = manifest.get("merge_job") or {}
    if merge.get("kind") != "merge":
        raise ValueError("manifest has no strict merge job")
    if not merge.get("command") or not merge.get("outputs"):
        raise ValueError("strict merge job requires a command and outputs")
    execute_job(repo, state_dir, merge, commit)
    all_jobs = jobs + [merge]
    if not all(verified_receipt(state_dir / f"{j['name']}.receipt.json", repo, j, commit) for j in all_jobs):
        raise RuntimeError("not all job receipts verify")
    final = {
        "state": "complete", "contract_id": manifest["contract_id"],
        "git_commit": commit, "job_count": 9,
        "receipts": {j["name"]: sha256(state_dir / f"{j['name']}.receipt.json") for j in all_jobs},
        "completed_at": datetime.now(timezone.utc).isoformat(),
    }
    atomic_json(state_dir / "production.complete.json", final)
    if retention_root is not None:
        retain(repo, state_dir, retention_root, manifest)
    return final


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--repo", type=Path, default=Path.cwd())
    p.add_argument("--state-dir", type=Path, required=True)
    p.add_argument("--retention-root", type=Path, required=True,
                   help="absolute attached-volume path outside repo/workspace/state")
    args = p.parse_args()
    run(args.repo.resolve(), json.loads(args.manifest.read_text()), args.state_dir.resolve(),
        args.retention_root)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"remote production failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
