#!/usr/bin/env python3
"""Bind HubStack deterministic pre-review checks to the six-paper portfolio."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from paper_registry import CANONICAL_IDS, load_registry, registry_path, repo_root
from verify_analysis_artifact_manifest import verify_manifest

SCHEMA = "bigbounce.pre-review-portfolio-receipt/v1"
ENGINE = Path.home() / ".claude/scistack/hubstack/learning-loop/paper-pre-review-check/scripts/pre_review_check.py"
DEFAULT_RULES = "project-context/pre-review-rules.json"
EXPECTED_ENGINE_COMMIT = "79a436e"
P1B_ANALYSIS_MANIFEST = "reproducibility/p1b_analysis_artifact_manifest_v1B.0.108.json"


class PortfolioError(ValueError):
    pass


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_record(root: Path, relative: str) -> dict[str, Any]:
    candidate = Path(relative)
    if not relative or candidate.is_absolute() or ".." in candidate.parts:
        raise PortfolioError(f"unsafe portfolio path: {relative!r}")
    path = (root / candidate).resolve(strict=True)
    if not path.is_file() or not path.is_relative_to(root):
        raise PortfolioError(f"portfolio path escapes root or is not a file: {relative!r}")
    raw = path.read_bytes()
    return {"path": relative, "bytes": len(raw), "sha256": sha256(raw)}


def load_engine():
    if not ENGINE.is_file():
        raise PortfolioError(f"canonical HubStack engine missing: {ENGINE}")
    spec = importlib.util.spec_from_file_location("hubstack_pre_review_check", ENGINE)
    if spec is None or spec.loader is None:
        raise PortfolioError(f"cannot load canonical HubStack engine: {ENGINE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git_head(root: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()


def ensure_clean_inputs(
    root: Path,
    registry: dict[str, dict[str, Any]],
    extra_paths: tuple[str, ...] = (),
) -> None:
    paths = [
        entry[field]
        for paper_id in CANONICAL_IDS
        for entry in (registry[paper_id],)
        for field in ("tex_path", "pdf_path")
    ]
    paths.extend(extra_paths)
    status = subprocess.check_output(
        ["git", "status", "--porcelain", "--", *paths], cwd=root, text=True,
    ).strip()
    if status:
        raise PortfolioError(f"canonical paper inputs are dirty:\n{status}")


def engine_commit() -> str:
    stack_root = ENGINE.parents[3]
    relative = ENGINE.relative_to(stack_root).as_posix()
    commit = subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", relative],
        cwd=stack_root, text=True,
    ).strip()
    if not commit.startswith(EXPECTED_ENGINE_COMMIT):
        raise PortfolioError(
            f"canonical HubStack engine provenance changed: expected {EXPECTED_ENGINE_COMMIT}, got {commit}"
        )
    return commit


def paper_version(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for pattern in (r"\\newcommand\{\\paperVersion\}\{([^}]+)\}", r"\\date\{[^}]*\}\s*%\s*(v[\w.\-]+)", r"^%\s*(v[\w.\-]+)\s*\("):
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            return match.group(1)
    raise PortfolioError(f"cannot determine paper version: {path}")


def pdf_pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    match = re.search(r"^Pages:\s+(\d+)$", output, re.MULTILINE)
    if not match or int(match.group(1)) < 1:
        raise PortfolioError(f"cannot determine PDF pages: {path}")
    return int(match.group(1))


def evaluate(root: Path, rules_path: Path) -> dict[str, Any]:
    root = root.resolve(strict=True)
    registry = load_registry(root)
    try:
        rule_catalog = json.loads(rules_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PortfolioError(f"cannot read portfolio validator catalog: {exc}") from exc
    validator_ids = rule_catalog.get("portfolio_validators", [])
    if not isinstance(validator_ids, list) or not all(isinstance(item, str) for item in validator_ids):
        raise PortfolioError("portfolio_validators must be a string list")
    validator_inputs = tuple(
        P1B_ANALYSIS_MANIFEST for item in validator_ids if item == "p1b-analysis-manifest"
    )
    ensure_clean_inputs(root, registry, validator_inputs)
    registry_raw = registry_path(root).read_bytes()
    engine = load_engine()
    generic = engine.evaluate(root, rules_path)
    if generic.get("verdict") != "PASS":
        raise PortfolioError("generic pre-review verdict is not PASS")
    portfolio_validators = []
    for validator_id in validator_ids:
        if validator_id == "p1b-analysis-manifest":
            portfolio_validators.append({
                "id": validator_id,
                **verify_manifest(root, root / P1B_ANALYSIS_MANIFEST),
            })
        else:
            raise PortfolioError(f"unknown portfolio validator: {validator_id}")
    papers = []
    for paper_id in CANONICAL_IDS:
        entry = registry[paper_id]
        source = file_record(root, entry["tex_path"])
        pdf = file_record(root, entry["pdf_path"])
        papers.append({
            "paper_id": paper_id,
            "verdict": "PASS",
            "version": paper_version(root / entry["tex_path"]),
            "pages": pdf_pages(root / entry["pdf_path"]),
            "source": source,
            "pdf": pdf,
        })
    engine_raw = ENGINE.read_bytes()
    core = {
        "schema": SCHEMA,
        "repository_head": git_head(root),
        "registry": {"path": registry_path(root).relative_to(root).as_posix(), "bytes": len(registry_raw), "sha256": sha256(registry_raw)},
        "generic_engine": {
            "path": str(ENGINE), "git_commit": engine_commit(),
            "bytes": len(engine_raw), "sha256": sha256(engine_raw),
        },
        "generic_rule_receipt": generic,
        "generic_rule_receipt_sha256": sha256(canonical_bytes(generic)),
        "portfolio_validators": portfolio_validators,
        "papers": papers,
        "paper_count": len(papers),
        "verdict": "PASS",
    }
    core["core_sha256"] = sha256(canonical_bytes(core))
    return core


def write_receipt(root: Path, rules: Path, output: Path) -> dict[str, Any]:
    receipt = evaluate(root, rules)
    receipt["generated_at"] = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    receipt["receipt_sha256"] = sha256(canonical_bytes(receipt))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipt


def verify_receipt(root: Path, rules: Path, receipt_path: Path) -> dict[str, Any]:
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PortfolioError(f"invalid portfolio receipt: {exc}") from exc
    if receipt.get("schema") != SCHEMA or receipt.get("verdict") != "PASS":
        raise PortfolioError("portfolio receipt is not a PASS receipt")
    claimed = receipt.get("receipt_sha256")
    unhashed = {k: v for k, v in receipt.items() if k != "receipt_sha256"}
    if claimed != sha256(canonical_bytes(unhashed)):
        raise PortfolioError("portfolio receipt content hash mismatch")
    recorded_core = {k: v for k, v in receipt.items() if k not in {"generated_at", "receipt_sha256", "core_sha256"}}
    expected_core_hash = sha256(canonical_bytes(recorded_core))
    if receipt.get("core_sha256") != expected_core_hash:
        raise PortfolioError("portfolio receipt core hash mismatch")
    current = evaluate(root, rules)
    if current != {**recorded_core, "core_sha256": expected_core_hash}:
        raise PortfolioError("portfolio receipt is stale: HEAD, registry, rules, source, or PDF changed")
    return receipt


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="command", required=True)
    for name in ("run", "verify"):
        command = commands.add_parser(name)
        command.add_argument("--project-root", type=Path, default=repo_root())
        command.add_argument("--rules", type=Path)
        command.add_argument("--receipt", required=True, type=Path)
    return result


def main() -> int:
    try:
        args = parser().parse_args()
        root = args.project_root.resolve(strict=True)
        rules = args.rules or root / DEFAULT_RULES
        receipt = write_receipt(root, rules, args.receipt) if args.command == "run" else verify_receipt(root, rules, args.receipt)
        print(json.dumps({"receipt": str(args.receipt), "verdict": receipt["verdict"], "core_sha256": receipt["core_sha256"]}, sort_keys=True))
        return 0
    except (PortfolioError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
