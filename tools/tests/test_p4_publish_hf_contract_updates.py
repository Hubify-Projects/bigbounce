#!/usr/bin/env python3
"""Focused tests for the P4 Hugging Face contract-update publisher."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "publisher", ROOT / "tools/p4_publish_hf_contract_updates.py"
)
assert SPEC and SPEC.loader
publisher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publisher)


class FakeApi:
    def __init__(self, token: str):
        self.token = token
        self.calls = []

    def dataset_info(self, repo_id):
        return SimpleNamespace(sha="dataset-parent")

    def model_info(self, repo_id):
        return SimpleNamespace(sha="model-parent")

    def create_commit(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(oid=f"{kwargs['repo_type']}-immutable-oid")


class PublisherTests(unittest.TestCase):
    def fake_operation(self, remote, local):
        return {"remote": remote, "local": local}

    def fake_download(self, **kwargs):
        target = next(
            local
            for remote, local in publisher.TARGETS[kwargs["repo_type"]]["files"].items()
            if remote == kwargs["filename"]
        )
        return target

    def test_dry_run_uses_no_api_or_token(self):
        def forbidden(*args, **kwargs):
            self.fail(f"provider called during dry-run: {args} {kwargs}")

        receipt = publisher.publish_updates(
            target="both", api_factory=forbidden, download=forbidden
        )
        self.assertFalse(receipt["published"])
        self.assertEqual({r["target"] for r in receipt["repositories"]}, {"dataset", "model"})

    def test_publish_requires_token(self):
        with mock.patch.object(publisher, "token_from_dotenv", return_value=None):
            with self.assertRaisesRegex(publisher.PublishError, "requires HF_TOKEN"):
                publisher.publish_updates(target="dataset", publish=True)

    def test_both_targets_are_atomic_parent_pinned_and_verified(self):
        api = FakeApi("secret-never-render")
        receipt = publisher.publish_updates(
            target="both",
            publish=True,
            token="secret-never-render",
            api_factory=lambda token: api,
            operation_factory=self.fake_operation,
            download=self.fake_download,
        )
        self.assertEqual(len(api.calls), 2)
        self.assertEqual(api.calls[0]["parent_commit"], "dataset-parent")
        self.assertEqual(api.calls[1]["parent_commit"], "model-parent")
        self.assertEqual(len(api.calls[0]["operations"]), 8)
        self.assertEqual(len(api.calls[1]["operations"]), 1)
        self.assertNotIn("secret-never-render", json.dumps(receipt))
        self.assertTrue(all("commit_oid" in item for item in receipt["repositories"]))

    def test_dataset_plan_preserves_morphology_and_adds_semantic_bundle(self):
        files = publisher.TARGETS["dataset"]["files"]
        self.assertTrue(any(path.startswith(publisher.MORPH_PREFIX + "/") for path in files))
        semantic = {path for path in files if path.startswith(publisher.SEMANTIC_PREFIX + "/")}
        self.assertEqual(
            semantic,
            {
                f"{publisher.SEMANTIC_PREFIX}/README.md",
                f"{publisher.SEMANTIC_PREFIX}/SEMANTIC_CONTRACT.json",
                f"{publisher.SEMANTIC_PREFIX}/SEMANTIC_VALIDATION_RECEIPT.json",
                f"{publisher.SEMANTIC_PREFIX}/validate_p4_catalog_c_semantics_v1_0_253.py",
            },
        )

    def test_dataset_only_and_model_only(self):
        for target in ("dataset", "model"):
            api = FakeApi("secret")
            receipt = publisher.publish_updates(
                target=target,
                publish=True,
                token="secret",
                api_factory=lambda token: api,
                operation_factory=self.fake_operation,
                download=self.fake_download,
            )
            self.assertEqual([target], [r["target"] for r in receipt["repositories"]])
            self.assertEqual(1, len(api.calls))

    def test_receipt_written_only_when_requested(self):
        with tempfile.TemporaryDirectory() as td:
            receipt_path = Path(td) / "receipt.json"
            rc = publisher.main(["--target", "model", "--receipt-json", str(receipt_path)])
            self.assertEqual(rc, 0)
            self.assertTrue(receipt_path.is_file())
            self.assertFalse(json.loads(receipt_path.read_text())["published"])
            absent = Path(td) / "absent.json"
            self.assertFalse(absent.exists())


if __name__ == "__main__":
    unittest.main()
