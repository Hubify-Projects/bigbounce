#!/usr/bin/env python3
"""Fail-closed publisher for the P4 ApJS Hugging Face release.

Dry-run is the default. Public mutation requires ``--publish`` and an HF token.
The local release candidate is never modified: publication always uses a
temporary staged copy with a sanitized public manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Iterator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RELEASE_DIR = ROOT / "pipelines/p2_chirality/apjs_release_v1.0.244"
REPO_ID = "bamfai/galaxy-chirality-catalog"
REPO_TYPE = "dataset"
PATH_PREFIX = "apjs-release/v1.0.244"
PROVIDER_RECEIPT_NAME = "PROVIDER_RECEIPT.json"
PUBLIC_RELEASE_GATE = (
    "PUBLIC_HUGGINGFACE_RELEASE; immutable archival DOI and human ApJS "
    "editorial review remain open"
)
REQUIRED_PRODUCTS = frozenset(
    {
        "p4_catalog_primary_safe_v1.0.244.parquet",
        "p4_catalog_raw_flip_quarantine_v1.0.244.parquet",
        "primary_null_amps_10000.npy",
        "primary_label_shuffle_amps_10000.npy",
        "pixel_permutation_amps_10000.npy",
        "MANIFEST.json",
        "VALIDATION.json",
        "PRIMARY_REPRODUCTION.json",
    }
)


class ReleaseError(RuntimeError):
    """A sanitized, user-actionable release validation failure."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReleaseError(f"invalid JSON: {path.name}") from exc
    if not isinstance(value, dict):
        raise ReleaseError(f"expected JSON object: {path.name}")
    return value


def release_files(release_dir: Path) -> list[Path]:
    if not release_dir.is_dir():
        raise ReleaseError(f"release directory not found: {release_dir}")
    files: list[Path] = []
    for path in sorted(release_dir.rglob("*")):
        if path.is_symlink():
            raise ReleaseError(f"symlink forbidden in release bundle: {path.name}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ReleaseError(f"non-regular release entry: {path.name}")
        files.append(path)
    names = {path.relative_to(release_dir).as_posix() for path in files}
    missing = sorted(REQUIRED_PRODUCTS - names)
    if missing:
        raise ReleaseError(f"missing required release products: {', '.join(missing)}")
    return files


def validate_source_manifest(release_dir: Path) -> dict[str, Any]:
    files = release_files(release_dir)
    manifest = load_json(release_dir / "MANIFEST.json")
    if manifest.get("schema") != "p4-apjs-release-manifest/v1":
        raise ReleaseError("unsupported MANIFEST schema")
    products = manifest.get("products")
    if not isinstance(products, dict) or not products:
        raise ReleaseError("MANIFEST products must be a non-empty object")
    seen: set[str] = set()
    for key, record in products.items():
        if not isinstance(record, dict):
            raise ReleaseError(f"invalid MANIFEST product record: {key}")
        filename = record.get("filename")
        expected_bytes = record.get("bytes")
        expected_sha = record.get("sha256")
        if not isinstance(filename, str) or PurePosixPath(filename).name != filename:
            raise ReleaseError(f"unsafe MANIFEST filename: {key}")
        if filename in seen:
            raise ReleaseError(f"duplicate MANIFEST filename: {filename}")
        seen.add(filename)
        path = release_dir / filename
        if not path.is_file() or path.is_symlink():
            raise ReleaseError(f"MANIFEST product missing: {filename}")
        if not isinstance(expected_bytes, int) or expected_bytes < 0:
            raise ReleaseError(f"invalid MANIFEST byte count: {filename}")
        if path.stat().st_size != expected_bytes:
            raise ReleaseError(f"MANIFEST byte mismatch: {filename}")
        if not isinstance(expected_sha, str) or len(expected_sha) != 64:
            raise ReleaseError(f"invalid MANIFEST SHA-256: {filename}")
        if sha256_file(path) != expected_sha.lower():
            raise ReleaseError(f"MANIFEST SHA-256 mismatch: {filename}")
    for name in REQUIRED_PRODUCTS:
        path = release_dir / name
        if path.stat().st_size <= 0:
            raise ReleaseError(f"required release product is empty: {name}")
        if path.suffix == ".json":
            load_json(path)
    return {
        "manifest": manifest,
        "source_manifest_sha256": sha256_file(release_dir / "MANIFEST.json"),
        "source_files": files,
    }


def sanitize_manifest_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: sanitize_manifest_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize_manifest_value(item) for item in value]
    if isinstance(value, str):
        if Path(value).is_absolute():
            return Path(value).name
        return value.replace("LOCAL_RELEASE_CANDIDATE_ONLY", "PUBLIC_HUGGINGFACE_RELEASE")
    return value


def assert_public_manifest_safe(manifest: dict[str, Any]) -> None:
    rendered = json.dumps(manifest, sort_keys=True)
    if "LOCAL_RELEASE_CANDIDATE_ONLY" in rendered:
        raise ReleaseError("staged public MANIFEST retains local-only wording")
    if "/Users/" in rendered or "\\Users\\" in rendered:
        raise ReleaseError("staged public MANIFEST retains an absolute user path")
    def walk(value: Any) -> Iterator[str]:
        if isinstance(value, dict):
            for item in value.values():
                yield from walk(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk(item)
        elif isinstance(value, str):
            yield value
    if any(Path(value).is_absolute() for value in walk(manifest)):
        raise ReleaseError("staged public MANIFEST retains an absolute path")


@contextmanager
def stage_public_release(release_dir: Path) -> Iterator[tuple[Path, dict[str, Any]]]:
    validated = validate_source_manifest(release_dir)
    original_manifest_bytes = (release_dir / "MANIFEST.json").read_bytes()
    with tempfile.TemporaryDirectory(prefix="p4-hf-release-") as temp_dir:
        staged = Path(temp_dir) / "release"
        staged.mkdir()
        for source in validated["source_files"]:
            relative = source.relative_to(release_dir)
            target = staged / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if relative.as_posix() == "MANIFEST.json":
                continue
            try:
                os.link(source, target)
            except OSError:
                shutil.copy2(source, target)
        public_manifest = sanitize_manifest_value(validated["manifest"])
        public_manifest["release_gate"] = PUBLIC_RELEASE_GATE
        public_manifest["publication_target"] = {
            "provider": "huggingface",
            "repo_id": REPO_ID,
            "repo_type": REPO_TYPE,
            "path_prefix": PATH_PREFIX,
        }
        assert_public_manifest_safe(public_manifest)
        (staged / "MANIFEST.json").write_text(
            json.dumps(public_manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        if (release_dir / "MANIFEST.json").read_bytes() != original_manifest_bytes:
            raise ReleaseError("local MANIFEST changed during staging")
        yield staged, {
            "source_manifest_sha256": validated["source_manifest_sha256"],
            "public_manifest_sha256": sha256_file(staged / "MANIFEST.json"),
        }


def inventory(folder: Path) -> list[dict[str, Any]]:
    return [
        {
            "path": path.relative_to(folder).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in release_files(folder)
    ]


def remote_size(sibling: Any) -> int | None:
    size = getattr(sibling, "size", None)
    if isinstance(size, int):
        return size
    lfs = getattr(sibling, "lfs", None)
    if isinstance(lfs, dict) and isinstance(lfs.get("size"), int):
        return lfs["size"]
    lfs_size = getattr(lfs, "size", None)
    return lfs_size if isinstance(lfs_size, int) else None


def verify_remote(api: Any, revision: str, files: list[dict[str, Any]]) -> None:
    try:
        info = api.dataset_info(REPO_ID, revision=revision, files_metadata=True)
    except Exception as exc:
        raise ReleaseError(f"remote verification failed: {type(exc).__name__}") from None
    remote = {item.rfilename: remote_size(item) for item in info.siblings}
    failures: list[str] = []
    for item in files:
        name = f"{PATH_PREFIX}/{item['path']}"
        if name not in remote:
            failures.append(f"missing {name}")
        elif remote[name] != item["bytes"]:
            failures.append(f"size mismatch {name}")
    if failures:
        raise ReleaseError("remote verification failed: " + "; ".join(failures))


def token_from_environment() -> str | None:
    return os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")


def default_api_factory(*, token: str) -> Any:
    try:
        from huggingface_hub import HfApi
    except ImportError as exc:
        raise ReleaseError("huggingface_hub is required for --publish") from exc
    return HfApi(token=token)


def publish_release(
    release_dir: Path,
    *,
    publish: bool = False,
    token: str | None = None,
    api_factory: Callable[..., Any] = default_api_factory,
) -> dict[str, Any]:
    with stage_public_release(release_dir.resolve()) as (staged, manifest_meta):
        files = inventory(staged)
        base_receipt: dict[str, Any] = {
            "schema": "p4-hf-provider-receipt/v1",
            "paper": "P4",
            "release": "v1.0.244",
            "repo_id": REPO_ID,
            "repo_type": REPO_TYPE,
            "path_prefix": PATH_PREFIX,
            "source_manifest_sha256": manifest_meta["source_manifest_sha256"],
            "public_manifest_sha256": manifest_meta["public_manifest_sha256"],
            "files": files,
        }
        if not publish:
            return {**base_receipt, "status": "dry-run", "published": False}
        token = token or token_from_environment()
        if not token:
            raise ReleaseError("--publish requires HF_TOKEN or HUGGINGFACE_TOKEN")
        api = api_factory(token=token)
        try:
            commit = api.upload_folder(
                folder_path=str(staged),
                path_in_repo=PATH_PREFIX,
                repo_id=REPO_ID,
                repo_type=REPO_TYPE,
                commit_message="Publish P4 ApJS release v1.0.244",
            )
        except Exception as exc:
            raise ReleaseError(f"Hugging Face upload failed: {type(exc).__name__}") from None
        data_commit = getattr(commit, "oid", None) or getattr(commit, "commit_id", None)
        if not isinstance(data_commit, str) or not data_commit:
            raise ReleaseError("Hugging Face upload returned no commit oid")
        verify_remote(api, data_commit, files)
        provider_receipt = {
            **base_receipt,
            "status": "published",
            "published": True,
            "published_at_utc": datetime.now(timezone.utc).isoformat(),
            "data_commit": data_commit,
            "verification_revision": data_commit,
            "verification": "remote paths and byte sizes matched",
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", encoding="utf-8", delete=False
        ) as handle:
            receipt_path = Path(handle.name)
            handle.write(json.dumps(provider_receipt, indent=2, sort_keys=True) + "\n")
        try:
            receipt_commit_info = api.upload_file(
                path_or_fileobj=str(receipt_path),
                path_in_repo=f"{PATH_PREFIX}/{PROVIDER_RECEIPT_NAME}",
                repo_id=REPO_ID,
                repo_type=REPO_TYPE,
                parent_commit=data_commit,
                commit_message="Add P4 ApJS release provider receipt",
            )
        except Exception as exc:
            raise ReleaseError(f"provider receipt upload failed: {type(exc).__name__}") from None
        finally:
            receipt_path.unlink(missing_ok=True)
        receipt_commit = getattr(receipt_commit_info, "oid", None) or getattr(
            receipt_commit_info, "commit_id", None
        )
        if not isinstance(receipt_commit, str) or not receipt_commit:
            raise ReleaseError("provider receipt upload returned no commit oid")
        receipt_bytes = len(
            (json.dumps(provider_receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")
        )
        verify_remote(
            api,
            receipt_commit,
            [*files, {"path": PROVIDER_RECEIPT_NAME, "bytes": receipt_bytes}],
        )
        return {**provider_receipt, "provider_receipt_commit": receipt_commit}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-dir", type=Path, default=DEFAULT_RELEASE_DIR)
    parser.add_argument("--publish", action="store_true", help="perform public upload")
    parser.add_argument("--receipt-json", type=Path, help="also write sanitized receipt")
    args = parser.parse_args(argv)
    try:
        receipt = publish_release(args.release_dir, publish=args.publish)
    except ReleaseError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.receipt_json:
        args.receipt_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
