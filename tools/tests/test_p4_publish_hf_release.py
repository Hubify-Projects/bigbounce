#!/usr/bin/env python3
"""Focused tests for the fail-closed P4 Hugging Face publisher."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import p4_publish_hf_release as publisher  # noqa: E402


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def make_release(root: Path) -> Path:
    release = root / "release"
    release.mkdir()
    payloads = {
        "p4_catalog_primary_safe_v1.0.244.parquet": b"safe-catalog",
        "p4_catalog_raw_flip_quarantine_v1.0.244.parquet": b"quarantine",
        "primary_null_amps_10000.npy": b"null-array",
        "SCHEMA.json": b'{"schema":"test"}\n',
        "CATALOG_SCHEMA.md": b"# schema\n",
        "reproduce_p4_primary_null_v1_0_244.py": b"print('ok')\n",
        "validate_p4_v1_0_244_claims.py": b"print('ok')\n",
        "VALIDATION.json": b'{"status":"PASS"}\n',
        "PRIMARY_REPRODUCTION.json": b'{"status":"PASS"}\n',
        "SHA256SUMS": b"fixture\n",
    }
    for name, data in payloads.items():
        (release / name).write_bytes(data)
    manifest_products = {}
    for index, name in enumerate(
        (
            "p4_catalog_primary_safe_v1.0.244.parquet",
            "p4_catalog_raw_flip_quarantine_v1.0.244.parquet",
            "primary_null_amps_10000.npy",
            "SCHEMA.json",
            "CATALOG_SCHEMA.md",
            "reproduce_p4_primary_null_v1_0_244.py",
            "validate_p4_v1_0_244_claims.py",
        )
    ):
        data = payloads[name]
        manifest_products[f"product_{index}"] = {
            "filename": name,
            "bytes": len(data),
            "sha256": digest(data),
        }
    manifest = {
        "schema": "p4-apjs-release-manifest/v1",
        "paper": "P4",
        "release_gate": "LOCAL_RELEASE_CANDIDATE_ONLY; DOI open",
        "source": {
            "path": "/Users/example/private/p4_chirality.parquet",
            "identity_validation": {
                "receipt_path": "/Users/example/private/receipt.json"
            },
        },
        "products": manifest_products,
    }
    (release / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return release


class FakeApi:
    def __init__(self, token: str, *, corrupt_remote: bool = False):
        self.token = token
        self.corrupt_remote = corrupt_remote
        self.revisions: dict[str, dict[str, int]] = {}
        self.public_manifest = ""
        self.uploaded_receipt = ""

    def upload_folder(self, **kwargs):
        folder = Path(kwargs["folder_path"])
        self.public_manifest = (folder / "MANIFEST.json").read_text(encoding="utf-8")
        prefix = kwargs["path_in_repo"]
        entries = {
            f"{prefix}/{path.relative_to(folder).as_posix()}": path.stat().st_size
            for path in folder.rglob("*")
            if path.is_file()
        }
        if self.corrupt_remote:
            entries[f"{prefix}/p4_catalog_primary_safe_v1.0.244.parquet"] += 1
        self.revisions["data-commit"] = entries
        return SimpleNamespace(oid="data-commit")

    def upload_file(self, **kwargs):
        receipt_path = Path(kwargs["path_or_fileobj"])
        self.uploaded_receipt = receipt_path.read_text(encoding="utf-8")
        data = receipt_path.read_bytes()
        self.revisions["receipt-commit"] = {
            **self.revisions[kwargs["parent_commit"]],
            kwargs["path_in_repo"]: len(data),
        }
        return SimpleNamespace(oid="receipt-commit")

    def dataset_info(self, repo_id, *, revision, files_metadata=True):
        del repo_id, files_metadata
        return SimpleNamespace(
            siblings=[
                SimpleNamespace(rfilename=name, size=size, lfs=None)
                for name, size in self.revisions[revision].items()
            ]
        )


class P4PublisherTests(unittest.TestCase):
    def test_default_dry_run_validates_without_token_or_api(self):
        with tempfile.TemporaryDirectory() as td:
            release = make_release(Path(td))
            original = (release / "MANIFEST.json").read_bytes()

            def forbidden_factory(**kwargs):
                self.fail(f"API factory called in dry-run: {kwargs}")

            receipt = publisher.publish_release(
                release, publish=False, api_factory=forbidden_factory
            )
            self.assertEqual(receipt["status"], "dry-run")
            self.assertFalse(receipt["published"])
            self.assertEqual((release / "MANIFEST.json").read_bytes(), original)
            self.assertNotIn("token", json.dumps(receipt).lower())

    def test_staged_manifest_is_public_safe_and_source_is_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            release = make_release(Path(td))
            original = (release / "MANIFEST.json").read_bytes()
            with publisher.stage_public_release(release) as (staged, _):
                public = (staged / "MANIFEST.json").read_text(encoding="utf-8")
                self.assertNotIn("/Users/", public)
                self.assertNotIn("LOCAL_RELEASE_CANDIDATE_ONLY", public)
                self.assertIn("PUBLIC_HUGGINGFACE_RELEASE", public)
            self.assertEqual((release / "MANIFEST.json").read_bytes(), original)

    def test_manifest_hash_or_byte_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            release = make_release(Path(td))
            target = release / "primary_null_amps_10000.npy"
            target.write_bytes(target.read_bytes() + b"corrupt")
            with self.assertRaisesRegex(publisher.ReleaseError, "byte mismatch"):
                publisher.publish_release(release)

    def test_missing_required_product_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            release = make_release(Path(td))
            (release / "VALIDATION.json").unlink()
            with self.assertRaisesRegex(publisher.ReleaseError, "missing required"):
                publisher.publish_release(release)

    def test_publish_requires_explicit_token(self):
        with tempfile.TemporaryDirectory() as td:
            release = make_release(Path(td))
            with mock.patch.dict(
                "os.environ", {"HF_TOKEN": "", "HUGGINGFACE_TOKEN": ""}
            ):
                with self.assertRaisesRegex(publisher.ReleaseError, "requires HF_TOKEN"):
                    publisher.publish_release(release, publish=True, token=None)

    def test_publish_verifies_exact_data_revision_and_uploads_safe_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            release = make_release(Path(td))
            secret = "super-secret-token-must-never-appear"
            api = FakeApi(secret)
            receipt = publisher.publish_release(
                release,
                publish=True,
                token=secret,
                api_factory=lambda **kwargs: api,
            )
            self.assertEqual(receipt["data_commit"], "data-commit")
            self.assertEqual(receipt["verification_revision"], "data-commit")
            self.assertEqual(receipt["provider_receipt_commit"], "receipt-commit")
            self.assertIn('"data_commit": "data-commit"', api.uploaded_receipt)
            for rendered in (api.public_manifest, api.uploaded_receipt, json.dumps(receipt)):
                self.assertNotIn("/Users/", rendered)
                self.assertNotIn("LOCAL_RELEASE_CANDIDATE_ONLY", rendered)
                self.assertNotIn(secret, rendered)

    def test_remote_size_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            release = make_release(Path(td))
            api = FakeApi("secret", corrupt_remote=True)
            with self.assertRaisesRegex(publisher.ReleaseError, "size mismatch"):
                publisher.publish_release(
                    release,
                    publish=True,
                    token="secret",
                    api_factory=lambda **kwargs: api,
                )


if __name__ == "__main__":
    unittest.main()
