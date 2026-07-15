#!/usr/bin/env python3
"""Security-focused tests for the public P4 semantic-contract bootstrap."""

from __future__ import annotations

import importlib.util
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


if __name__ == "__main__":
    unittest.main()
