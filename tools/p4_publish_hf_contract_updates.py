#!/usr/bin/env python3
"""Fail-closed publisher for P4 Hugging Face cards and morphology contract.

Dry-run is the default. ``--publish`` is required for any provider mutation.
Each repository update is one atomic commit pinned to its observed parent head,
then every uploaded file is downloaded from the returned immutable commit and
verified byte-for-byte by size and SHA-256.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
DATASET_REPO = "bamfai/galaxy-chirality-catalog"
MODEL_REPO = "bamfai/galaxy-chirality-v2"
MORPH_PREFIX = "apjs-release/v1.0.251-morphology-sidecar"
SEMANTIC_PREFIX = "apjs-release/v1.0.253-semantic-contract"
SEMANTIC_DIR = ROOT / "pipelines/p2_chirality/apjs_release_v1.0.253_semantic_contract"

TARGETS: dict[str, dict[str, Any]] = {
    "dataset": {
        "repo_id": DATASET_REPO,
        "repo_type": "dataset",
        "files": {
            "README.md": ROOT / "pipelines/p2_chirality/HF_DATASET_README.md",
            f"{MORPH_PREFIX}/MANIFEST.json": ROOT / "pipelines/p2_chirality/apjs_release_v1.0.251_morphology_sidecar/MANIFEST.json",
            f"{MORPH_PREFIX}/SCHEMA.json": ROOT / "pipelines/p2_chirality/apjs_release_v1.0.251_morphology_sidecar/SCHEMA.json",
            f"{MORPH_PREFIX}/validate_p4_morphology_join_v1_0_251.py": ROOT / "pipelines/p2_chirality/apjs_release_v1.0.251_morphology_sidecar/validate_p4_morphology_join_v1_0_251.py",
            f"{SEMANTIC_PREFIX}/README.md": SEMANTIC_DIR / "README.md",
            f"{SEMANTIC_PREFIX}/SEMANTIC_CONTRACT.json": SEMANTIC_DIR / "SEMANTIC_CONTRACT.json",
            f"{SEMANTIC_PREFIX}/SEMANTIC_VALIDATION_RECEIPT.json": SEMANTIC_DIR / "SEMANTIC_VALIDATION_RECEIPT.json",
            f"{SEMANTIC_PREFIX}/validate_p4_catalog_c_semantics_v1_0_253.py": SEMANTIC_DIR / "validate_p4_catalog_c_semantics_v1_0_253.py",
        },
    },
    "model": {
        "repo_id": MODEL_REPO,
        "repo_type": "model",
        "files": {"README.md": ROOT / "pipelines/p2_chirality/HF_MODEL_README.md"},
    },
}


class PublishError(RuntimeError):
    """Sanitized publication failure safe to print to a terminal."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(files: dict[str, Path]) -> list[dict[str, Any]]:
    result = []
    for remote_path, local_path in files.items():
        if not local_path.is_file() or local_path.is_symlink():
            raise PublishError(f"missing or unsafe local file: {local_path.name}")
        result.append(
            {
                "path": remote_path,
                "bytes": local_path.stat().st_size,
                "sha256": sha256_file(local_path),
            }
        )
    return result


def token_from_dotenv(path: Path) -> str | None:
    try:
        from dotenv import dotenv_values
    except ImportError as exc:
        raise PublishError("python-dotenv is required for --publish") from exc
    values = dotenv_values(path)
    return values.get("HF_TOKEN") or values.get("HUGGINGFACE_TOKEN")


def default_api_factory(token: str) -> Any:
    try:
        from huggingface_hub import HfApi
    except ImportError as exc:
        raise PublishError("huggingface_hub is required for --publish") from exc
    return HfApi(token=token)


def default_operation_factory(path_in_repo: str, path_or_fileobj: str) -> Any:
    from huggingface_hub import CommitOperationAdd

    return CommitOperationAdd(
        path_in_repo=path_in_repo, path_or_fileobj=path_or_fileobj
    )


def default_download(
    *, repo_id: str, repo_type: str, filename: str, revision: str, token: str
) -> Path:
    from huggingface_hub import hf_hub_download

    return Path(
        hf_hub_download(
            repo_id=repo_id,
            repo_type=repo_type,
            filename=filename,
            revision=revision,
            token=token,
            force_download=True,
        )
    )


def selected_targets(target: str) -> Iterable[str]:
    return TARGETS if target == "both" else (target,)


def publish_updates(
    *,
    target: str = "both",
    publish: bool = False,
    dotenv_path: Path | None = None,
    token: str | None = None,
    api_factory: Callable[[str], Any] = default_api_factory,
    operation_factory: Callable[[str, str], Any] = default_operation_factory,
    download: Callable[..., Path] = default_download,
) -> dict[str, Any]:
    if target not in {"dataset", "model", "both"}:
        raise PublishError(f"unsupported target: {target}")
    plans = []
    for name in selected_targets(target):
        spec = TARGETS[name]
        plans.append(
            {
                "target": name,
                "repo_id": spec["repo_id"],
                "repo_type": spec["repo_type"],
                "files": inventory(spec["files"]),
            }
        )
    if not publish:
        return {"schema": "p4-hf-contract-update-receipt/v1", "status": "dry-run", "published": False, "repositories": plans}

    token = token or token_from_dotenv(dotenv_path or ROOT / ".env.local")
    if not token:
        raise PublishError("--publish requires HF_TOKEN or HUGGINGFACE_TOKEN in dotenv")
    api = api_factory(token)
    completed = []
    for plan in plans:
        name = plan["target"]
        spec = TARGETS[name]
        try:
            info = (
                api.dataset_info(plan["repo_id"])
                if plan["repo_type"] == "dataset"
                else api.model_info(plan["repo_id"])
            )
            parent = info.sha
            operations = [
                operation_factory(remote, str(local))
                for remote, local in spec["files"].items()
            ]
            commit = api.create_commit(
                repo_id=plan["repo_id"],
                repo_type=plan["repo_type"],
                operations=operations,
                parent_commit=parent,
                commit_message=f"Publish P4 v1.0.253 {name} contract updates",
            )
            oid = getattr(commit, "oid", None) or getattr(commit, "commit_id", None)
            if not isinstance(oid, str) or not oid:
                raise PublishError(f"{name} commit returned no immutable oid")
            for record in plan["files"]:
                remote = Path(
                    download(
                        repo_id=plan["repo_id"],
                        repo_type=plan["repo_type"],
                        filename=record["path"],
                        revision=oid,
                        token=token,
                    )
                )
                if remote.stat().st_size != record["bytes"]:
                    raise PublishError(f"{name} remote byte verification failed: {record['path']}")
                if sha256_file(remote) != record["sha256"]:
                    raise PublishError(f"{name} remote SHA-256 verification failed: {record['path']}")
        except PublishError:
            raise
        except Exception as exc:
            raise PublishError(f"{name} publication failed: {type(exc).__name__}") from None
        completed.append({**plan, "parent_commit": parent, "commit_oid": oid, "verification": "immutable downloads matched bytes and SHA-256"})
    return {
        "schema": "p4-hf-contract-update-receipt/v1",
        "status": "published",
        "published": True,
        "published_at_utc": datetime.now(timezone.utc).isoformat(),
        "repositories": completed,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("dataset", "model", "both"), default="both")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--dotenv", type=Path, default=ROOT / ".env.local")
    parser.add_argument("--receipt-json", type=Path)
    args = parser.parse_args(argv)
    try:
        receipt = publish_updates(target=args.target, publish=args.publish, dotenv_path=args.dotenv)
    except PublishError as exc:
        print(f"FAIL: {exc}")
        return 1
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.receipt_json:
        args.receipt_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
