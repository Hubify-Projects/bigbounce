#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "ledger_match", ROOT / "tools/ledger_match.py"
)
assert SPEC and SPEC.loader
ledger_match = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ledger_match)


class LedgerMatchTests(unittest.TestCase):
    def test_repository_root_is_discovered_from_script(self):
        self.assertEqual(ledger_match.REPO, ROOT)

    def test_p1_taxonomies_are_not_collapsed(self):
        self.assertEqual(ledger_match.LEDGER_FILE["P1A"], "P1A.md")
        self.assertEqual(ledger_match.LEDGER_FILE["P1B"], "P1B.md")
        self.assertEqual(ledger_match.LEDGER_FILE["P1U"], "P1U.md")

    def test_compact_p1b_table_is_parseable(self):
        entries = ledger_match.parse_ledger(
            ROOT / "project-context/peer-reviews/DISPOSITIONS/P1B.md"
        )
        ids = {entry[0] for entry in entries}
        self.assertIn("DP1B-15", ids)
        self.assertIn("DP1B-16", ids)
        self.assertGreaterEqual(len(entries), 16)


if __name__ == "__main__":
    unittest.main()
