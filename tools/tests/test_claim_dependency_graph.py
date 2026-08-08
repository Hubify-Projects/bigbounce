#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from verify_claim_dependency_graph import ClaimGraphError, verify  # noqa: E402


class ClaimDependencyGraphTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="claim_graph_")
        self.root = Path(self.tmp.name)
        (self.root / "a.txt").write_text("shared=42\n", encoding="utf-8")
        (self.root / "b.json").write_text(
            json.dumps({"result": {"value": 42}}), encoding="utf-8"
        )
        self.graph = self.root / "graph.json"
        self.graph.write_text(json.dumps({
            "schema": "bigbounce.claim-dependency-graph/v1",
            "claims": [{
                "id": "SHARED",
                "anchors": [
                    {
                        "surface": "paper",
                        "path": "a.txt",
                        "kind": "literal",
                        "expected": "shared=42",
                    },
                    {
                        "surface": "artifact",
                        "path": "b.json",
                        "kind": "json_pointer",
                        "pointer": "/result/value",
                        "expected": 42,
                    },
                ],
            }],
        }), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid_graph_emits_bound_receipt(self):
        result = verify(self.root, self.graph)
        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual(result["claim_count"], 1)
        self.assertEqual(result["anchor_count"], 2)
        self.assertEqual(len(result["graph"]["sha256"]), 64)

    def test_literal_drift_fails_closed(self):
        (self.root / "a.txt").write_text("shared=41\n", encoding="utf-8")
        with self.assertRaisesRegex(ClaimGraphError, "literal mismatch"):
            verify(self.root, self.graph)

    def test_json_drift_fails_closed(self):
        (self.root / "b.json").write_text(
            json.dumps({"result": {"value": 41}}), encoding="utf-8"
        )
        with self.assertRaisesRegex(ClaimGraphError, "JSON mismatch"):
            verify(self.root, self.graph)

    def test_single_surface_claim_is_rejected(self):
        payload = json.loads(self.graph.read_text(encoding="utf-8"))
        payload["claims"][0]["anchors"][1]["surface"] = "paper"
        self.graph.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(ClaimGraphError, "at least two surfaces"):
            verify(self.root, self.graph)

    def test_duplicate_claim_id_is_rejected(self):
        payload = json.loads(self.graph.read_text(encoding="utf-8"))
        payload["claims"].append(payload["claims"][0])
        self.graph.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(ClaimGraphError, "unique"):
            verify(self.root, self.graph)

    def test_repository_graph_passes(self):
        result = verify(ROOT, ROOT / "project-context/claim-dependency-graph.json")
        self.assertGreaterEqual(result["claim_count"], 5)
        self.assertGreaterEqual(result["anchor_count"], 10)


if __name__ == "__main__":
    unittest.main()
