#!/usr/bin/env python3
"""Security-focused tests for the public P4 semantic-contract bootstrap."""

from __future__ import annotations

import importlib.util
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BOOTSTRAP = (
    ROOT
    / "pipelines/p2_chirality/apjs_release_v1.0.253_semantic_contract"
    / "validate_p4_catalog_c_semantics_v1_0_253.py"
)
SPEC = importlib.util.spec_from_file_location("p4_semantic_bootstrap", BOOTSTRAP)
assert SPEC and SPEC.loader
bootstrap = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bootstrap)


class SafeRelativePathTests(unittest.TestCase):
    def test_accepts_nested_release_path(self):
        self.assertEqual(
            bootstrap.safe_relative_path("catalog/chunk-000.parquet"),
            Path("catalog/chunk-000.parquet"),
        )

    def test_rejects_absolute_parent_and_empty_paths(self):
        for raw in ("/tmp/escape", "../escape", "catalog/../../escape", "", None):
            with self.subTest(raw=raw):
                with self.assertRaises(bootstrap.ContractError):
                    bootstrap.safe_relative_path(raw)

    def test_contract_pinned_sources_support_clean_tree_help(self):
        contract = json.loads(bootstrap.CONTRACT_PATH.read_text(encoding="utf-8"))
        keys = ("validator_source", "validator_schema_source", "validator_reproducer_source")
        with tempfile.TemporaryDirectory() as directory:
            checkout = Path(directory) / "pinned-source"
            for key in keys:
                record = contract[key]
                content = subprocess.run(
                    ["git", "show", f"{record['git_commit']}:{record['path']}"],
                    cwd=ROOT, check=True, capture_output=True,
                ).stdout
                self.assertEqual(len(content), record["bytes"])
                self.assertEqual(hashlib.sha256(content).hexdigest(), record["sha256"])
                destination = checkout / record["path"]
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(content)
            validator = checkout / contract["validator_source"]["path"]
            completed = subprocess.run(
                [sys.executable, str(validator), "--help"],
                cwd=checkout, capture_output=True, text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("--validate-only", completed.stdout)


if __name__ == "__main__":
    unittest.main()
