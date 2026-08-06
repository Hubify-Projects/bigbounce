#!/usr/bin/env python3
"""Bind HubStack deterministic pre-review checks to the six-paper portfolio."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import importlib.util
import io
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from paper_registry import CANONICAL_IDS, load_registry, registry_path, repo_root
import artifact_crosscheck
from verify_analysis_artifact_manifest import verify_manifest
from verify_p1b_science_contracts import verify as verify_p1b_science_contracts
from verify_p4_p5_science_contracts import verify as verify_p4_p5_science_contracts
from verify_claim_dependency_graph import verify as verify_claim_dependency_graph
from verify_ci_shell_portability import verify as verify_ci_shell_portability
from verify_companion_status import verify as verify_companion_status
from verify_pdf_mirror_integrity import (
    load_policy as load_served_pdf_policy,
    verify as verify_pdf_mirror_integrity,
)

SCHEMA = "bigbounce.pre-review-portfolio-receipt/v1"
DRAFT_REGISTRY_RELATIVE = "project-context/draft_paper_registry.json"
ENGINE = Path.home() / ".claude/scistack/hubstack/learning-loop/paper-pre-review-check/scripts/pre_review_check.py"
DEFAULT_RULES = "project-context/pre-review-rules.json"
EXPECTED_ENGINE_COMMIT = "79a436e"
ALLOWED_LOCAL_ENGINE_PATHS = (
    "project-context/pre-review-rules.json",
    "tools/bigbounce_preflight.py",
    "tools/artifact_crosscheck.py",
    "tools/verify_analysis_artifact_manifest.py",
    "tools/verify_p1b_science_contracts.py",
    "tools/verify_p4_p5_science_contracts.py",
    "tools/verify_claim_dependency_graph.py",
    "tools/verify_ci_shell_portability.py",
    "project-context/claim-dependency-graph.json",
    "tools/verify_companion_status.py",
    "project-context/companion-status-ledger.json",
    "tools/verify_pdf_mirror_integrity.py",
)


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


def draft_registry_path(root: Path) -> Path:
    return root / DRAFT_REGISTRY_RELATIVE


def load_draft_registry(root: Path) -> dict[str, dict[str, Any]]:
    """Load the auxiliary draft-paper registry (papers not yet in the canonical six).

    Returns {} when the registry file is absent.  Draft entries share the
    canonical field shape; they may never redefine a canonical paper id.
    """
    path = draft_registry_path(root)
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PortfolioError(f"invalid draft paper registry: {exc}") from exc
    if not isinstance(payload, dict):
        raise PortfolioError("draft paper registry must be a paper-id map")
    drafts: dict[str, dict[str, Any]] = {}
    for paper_id in sorted(payload):
        entry = payload[paper_id]
        if paper_id in CANONICAL_IDS:
            raise PortfolioError(
                f"draft paper registry may not redefine canonical paper: {paper_id}"
            )
        if not isinstance(entry, dict):
            raise PortfolioError(f"draft paper entry must be a map: {paper_id}")
        for field in ("tex_path", "pdf_path"):
            if not isinstance(entry.get(field), str) or not entry[field]:
                raise PortfolioError(f"draft paper {paper_id} missing field: {field}")
        drafts[paper_id] = entry
    return drafts


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


def evaluate(root: Path, rules_path: Path, *, include_drafts: bool = True) -> dict[str, Any]:
    root = root.resolve(strict=True)
    registry = load_registry(root)
    try:
        rule_catalog = json.loads(rules_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PortfolioError(f"cannot read portfolio validator catalog: {exc}") from exc
    validator_ids = rule_catalog.get("portfolio_validators", [])
    if not isinstance(validator_ids, list) or not all(isinstance(item, str) for item in validator_ids):
        raise PortfolioError("portfolio_validators must be a string list")
    local_engine_paths = rule_catalog.get("portfolio_engine_paths", [])
    if not isinstance(local_engine_paths, list) or any(
        item not in ALLOWED_LOCAL_ENGINE_PATHS for item in local_engine_paths
    ):
        raise PortfolioError("portfolio_engine_paths contains an unsafe or unknown path")
    science_contract_paths = rule_catalog.get("p4_p5_science_contract_paths", {})
    if not isinstance(science_contract_paths, dict) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in science_contract_paths.items()
    ):
        raise PortfolioError("p4_p5_science_contract_paths must be a string map")
    p1b_contract_paths = rule_catalog.get("p1b_science_contract_paths", {})
    if not isinstance(p1b_contract_paths, dict) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in p1b_contract_paths.items()
    ):
        raise PortfolioError("p1b_science_contract_paths must be a string map")
    p1b_analysis_manifest = p1b_contract_paths.get("analysis_manifest")
    claim_graph_path = rule_catalog.get("claim_dependency_graph")
    companion_ledger_path = rule_catalog.get("companion_status_ledger")
    if "companion-status" in validator_ids and not isinstance(companion_ledger_path, str):
        raise PortfolioError(
            "companion-status requires a companion_status_ledger path"
        )
    ci_shell_paths = rule_catalog.get("ci_shell_portability_paths", [])
    if not isinstance(ci_shell_paths, list) or not all(
        isinstance(item, str) for item in ci_shell_paths
    ):
        raise PortfolioError("ci_shell_portability_paths must be a string list")
    if "claim-dependency-graph" in validator_ids and not isinstance(claim_graph_path, str):
        raise PortfolioError(
            "claim-dependency-graph requires a claim_dependency_graph path"
        )
    if "p1b-analysis-manifest" in validator_ids and not p1b_analysis_manifest:
        raise PortfolioError(
            "p1b-analysis-manifest requires p1b_science_contract_paths.analysis_manifest"
        )
    # The served-PDF policy itself lives in the registry (already hash-bound as
    # `registry`); what still has to be pinned clean is every site data file the
    # policy declares as a PDF-reference surface.
    served_pdf_sources: tuple[str, ...] = ()
    if "pdf-mirror-integrity" in validator_ids:
        try:
            served_pdf_sources = tuple(
                source["path"] for source in load_served_pdf_policy(root)[0]["site_data_sources"]
            )
        except ValueError as exc:
            raise PortfolioError(f"served-PDF policy is invalid: {exc}") from exc
    validator_inputs = tuple(
        p1b_analysis_manifest for item in validator_ids if item == "p1b-analysis-manifest"
    ) + tuple(
        p1b_contract_paths.values()
        if "p1b-science-contracts" in validator_ids else ()
    ) + tuple(
        science_contract_paths.values()
        if "p4-p5-science-contracts" in validator_ids else ()
    ) + tuple(
        (claim_graph_path,)
        if "claim-dependency-graph" in validator_ids else ()
    ) + tuple(
        ci_shell_paths
        if "ci-shell-portability" in validator_ids else ()
    ) + tuple(
        (companion_ledger_path,)
        if "companion-status" in validator_ids else ()
    ) + served_pdf_sources + tuple(local_engine_paths)
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
                **verify_manifest(root, root / p1b_analysis_manifest),
            })
        elif validator_id == "p1b-science-contracts":
            try:
                result = verify_p1b_science_contracts(root, p1b_contract_paths)
            except (OSError, UnicodeDecodeError, ValueError) as exc:
                raise PortfolioError(f"P1B science-contract validation failed: {exc}") from exc
            portfolio_validators.append({"id": validator_id, **result})
        elif validator_id == "artifact-crosscheck-six":
            per_paper = []
            failed = []
            for paper_id in CANONICAL_IDS:
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    rc = artifact_crosscheck.main(
                        str(root / registry[paper_id]["tex_path"]), root,
                    )
                rendered = output.getvalue()
                per_paper.append({
                    "paper_id": paper_id,
                    "verdict": "PASS" if rc == 0 else "FAIL",
                    "output_sha256": sha256(rendered.encode()),
                    "output": rendered,
                })
                if rc:
                    failed.append(paper_id)
            if failed:
                raise PortfolioError(
                    "artifact crosscheck failed for canonical papers: " + ", ".join(failed)
                )
            portfolio_validators.append({
                "id": validator_id,
                "schema": "bigbounce.artifact-crosscheck-six/v1",
                "papers": per_paper,
                "paper_count": len(per_paper),
                "verdict": "PASS",
            })
        elif validator_id == "p4-p5-science-contracts":
            try:
                result = verify_p4_p5_science_contracts(root, science_contract_paths)
            except ValueError as exc:
                raise PortfolioError(f"P4/P5 science-contract validation failed: {exc}") from exc
            portfolio_validators.append({"id": validator_id, **result})
        elif validator_id == "claim-dependency-graph":
            try:
                result = verify_claim_dependency_graph(root, root / claim_graph_path)
            except (OSError, UnicodeDecodeError, ValueError) as exc:
                raise PortfolioError(f"claim-dependency validation failed: {exc}") from exc
            portfolio_validators.append({"id": validator_id, **result})
        elif validator_id == "ci-shell-portability":
            try:
                result = verify_ci_shell_portability(root, ci_shell_paths)
            except (OSError, UnicodeDecodeError, ValueError) as exc:
                raise PortfolioError(f"CI shell-portability validation failed: {exc}") from exc
            if result.get("verdict") != "PASS":
                raise PortfolioError(
                    "CI shell-portability validation failed: "
                    + json.dumps(result.get("findings", []), sort_keys=True)
                )
            portfolio_validators.append({"id": validator_id, **result})
        elif validator_id == "companion-status":
            try:
                result = verify_companion_status(root, companion_ledger_path)
            except (OSError, UnicodeDecodeError, ValueError) as exc:
                raise PortfolioError(f"companion-status validation failed: {exc}") from exc
            if result.get("verdict") != "PASS":
                raise PortfolioError(
                    "companion-status validation failed: "
                    + json.dumps(result.get("findings", []), sort_keys=True)
                )
            portfolio_validators.append({"id": validator_id, **result})
        elif validator_id == "pdf-mirror-integrity":
            try:
                result = verify_pdf_mirror_integrity(root)
            except (OSError, UnicodeDecodeError, ValueError, subprocess.CalledProcessError) as exc:
                raise PortfolioError(f"served-PDF mirror-integrity validation failed: {exc}") from exc
            if result.get("verdict") != "PASS":
                raise PortfolioError(
                    "served-PDF mirror-integrity validation failed: "
                    + json.dumps(result.get("findings", []), sort_keys=True)
                )
            portfolio_validators.append({"id": validator_id, **result})
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
    # `paper_count` is the CANONICAL count only — consumers that assert the
    # six-paper portfolio (e.g. int_api_review_p3apjs) rely on it staying 6.
    canonical_count = len(papers)
    drafts = load_draft_registry(root) if include_drafts else {}
    if drafts:
        draft_paths = [
            entry[field]
            for entry in drafts.values()
            for field in ("tex_path", "pdf_path")
        ]
        status = subprocess.check_output(
            ["git", "status", "--porcelain", "--", *draft_paths], cwd=root, text=True,
        ).strip()
        if status:
            raise PortfolioError(f"draft paper inputs are dirty:\n{status}")
        for paper_id, entry in drafts.items():
            papers.append({
                "paper_id": paper_id,
                "verdict": "PASS",
                "draft": True,
                "version": paper_version(root / entry["tex_path"]),
                "pages": pdf_pages(root / entry["pdf_path"]),
                "source": file_record(root, entry["tex_path"]),
                "pdf": file_record(root, entry["pdf_path"]),
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
        "portfolio_engine": [file_record(root, path) for path in local_engine_paths],
        "generic_rule_receipt": generic,
        "generic_rule_receipt_sha256": sha256(canonical_bytes(generic)),
        "portfolio_validators": portfolio_validators,
        "papers": papers,
        "paper_count": canonical_count,
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
    # Draft-paper records ("draft": true) are additive: their per-paper hash
    # bindings are enforced identically at dispatch time (review_packet
    # build_packet compares the recorded binding against the live files), but
    # they never gate canonical verification — old receipts without draft
    # records must keep verifying, and a stale draft must fail only that
    # draft's dispatch, never the canonical six.
    current = evaluate(root, rules, include_drafts=False)
    current_core = {k: v for k, v in current.items() if k != "core_sha256"}
    recorded_canonical = dict(recorded_core)
    recorded_canonical["papers"] = [
        item
        for item in recorded_core.get("papers", [])
        if not (isinstance(item, dict) and item.get("draft"))
    ]
    if current_core != recorded_canonical:
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
