#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from bigbounce_preflight import (  # noqa: E402
    PortfolioError,
    load_engine,
    verify_receipt,
    write_receipt,
)
from paper_registry import CANONICAL_IDS  # noqa: E402


class PortfolioPreflightTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="portfolio_preflight_")
        self.root = Path(self.tmp.name)
        (self.root / "project-context").mkdir()
        fixture_pdf = ROOT / "arxiv/paper1a_ech_nogo.pdf"
        self.registry = {}
        sources = []
        for index, paper_id in enumerate(CANONICAL_IDS):
            directory = self.root / "papers" / paper_id
            directory.mkdir(parents=True)
            tex_rel = f"papers/{paper_id}/paper.tex"
            pdf_rel = f"papers/{paper_id}/paper.pdf"
            (self.root / tex_rel).write_text(
                rf"\newcommand{{\paperVersion}}{{v{index}.1}}" + "\n\\begin{document}\nOK\n\\end{document}\n",
                encoding="utf-8",
            )
            shutil.copy2(fixture_pdf, self.root / pdf_rel)
            sources.append(tex_rel)
            self.registry[paper_id] = {
                "tex_path": tex_rel, "pdf_path": pdf_rel, "site_slug": paper_id.lower(),
                "target_journal": "Journal", "article_type": "Article", "review_profile": "PROFILE",
            }
        self.registry_path = self.root / "project-context/paper_registry.json"
        self.registry_path.write_text(json.dumps({"papers": self.registry}), encoding="utf-8")
        self.rules = self.root / "project-context/pre-review-rules.json"
        self.rules.write_text(json.dumps({
            "schema": "hubstack.paper-pre-review-rules/v1", "sources": sources,
            "rules": [{"id": "begin", "detector": "literal_require", "paths": sources, "pattern": "\\begin{document}"}],
        }), encoding="utf-8")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Preflight Test"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.root, check=True)
        self.receipt = self.root / "receipt.json"

    def tearDown(self):
        self.tmp.cleanup()

    def registry_patch(self):
        return mock.patch("bigbounce_preflight.load_registry", return_value=self.registry)

    def run_and_verify(self):
        with self.registry_patch():
            written = write_receipt(self.root, self.rules, self.receipt)
            verified = verify_receipt(self.root, self.rules, self.receipt)
        self.assertEqual(written["verdict"], "PASS")
        self.assertEqual(len(verified["papers"]), 6)
        self.assertTrue(all(p["pages"] > 0 for p in verified["papers"]))
        return verified

    def assert_stale_after(self, mutation):
        self.run_and_verify()
        mutation()
        # Tracked canonical source/PDF mutations now fail even earlier at the
        # clean-input gate; registry/catalog/HEAD mutations reach the stale
        # receipt comparison.  Both are required fail-closed outcomes.
        with self.registry_patch(), self.assertRaisesRegex(
            PortfolioError, "stale|inputs are dirty"
        ):
            verify_receipt(self.root, self.rules, self.receipt)

    def test_run_and_verify_bind_all_six(self):
        receipt = self.run_and_verify()
        self.assertEqual(tuple(p["paper_id"] for p in receipt["papers"]), CANONICAL_IDS)
        self.assertTrue(all(p["verdict"] == "PASS" for p in receipt["papers"]))
        self.assertEqual(receipt["generic_rule_receipt"]["verdict"], "PASS")
        self.assertEqual(len(receipt["registry"]["sha256"]), 64)

    def test_source_mutation_invalidates(self):
        self.assert_stale_after(lambda: (self.root / self.registry["P1A"]["tex_path"]).write_text(
            "\\newcommand{\\paperVersion}{v0.1}\n\\begin{document}\nchanged\n\\end{document}\n", encoding="utf-8"))

    def test_pdf_mutation_invalidates(self):
        def mutate():
            with (self.root / self.registry["P1B"]["pdf_path"]).open("ab") as handle:
                handle.write(b"\n% mutation\n")
        self.assert_stale_after(mutate)

    def test_registry_mutation_invalidates(self):
        self.assert_stale_after(lambda: self.registry_path.write_text(
            self.registry_path.read_text() + "\n", encoding="utf-8"))

    def test_catalog_mutation_invalidates(self):
        self.assert_stale_after(lambda: self.rules.write_text(
            self.rules.read_text() + "\n", encoding="utf-8"))

    def test_head_mutation_invalidates(self):
        def mutate():
            (self.root / "unrelated.txt").write_text("new commit\n", encoding="utf-8")
            subprocess.run(["git", "add", "unrelated.txt"], cwd=self.root, check=True)
            subprocess.run(["git", "commit", "-qm", "advance head"], cwd=self.root, check=True)
        self.assert_stale_after(mutate)

    def test_generic_failure_writes_no_portfolio_receipt(self):
        payload = json.loads(self.rules.read_text())
        payload["rules"][0]["pattern"] = "definitely absent"
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        with self.registry_patch(), self.assertRaisesRegex(PortfolioError, "not PASS"):
            write_receipt(self.root, self.rules, self.receipt)
        self.assertFalse(self.receipt.exists())

    def test_dirty_canonical_input_fails_closed(self):
        source = self.root / self.registry["P1A"]["tex_path"]
        source.write_text(source.read_text(encoding="utf-8") + "% dirty\n", encoding="utf-8")
        with self.registry_patch(), self.assertRaisesRegex(PortfolioError, "inputs are dirty"):
            write_receipt(self.root, self.rules, self.receipt)
        self.assertFalse(self.receipt.exists())

    def test_repository_catalog_passes_current_canonical_sources(self):
        result = load_engine().evaluate(
            ROOT, ROOT / "project-context/pre-review-rules.json"
        )
        self.assertGreaterEqual(result["rule_count"], 9)
        self.assertEqual(result["verdict"], "PASS", json.dumps(result["findings"], indent=2))


if __name__ == "__main__":
    unittest.main()
