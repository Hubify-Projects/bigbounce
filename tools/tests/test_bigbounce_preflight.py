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
from review_packet import build_packet  # noqa: E402


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

    def test_unknown_portfolio_validator_fails_closed(self):
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_validators"] = ["not-allowlisted"]
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        with self.registry_patch(), self.assertRaisesRegex(
            PortfolioError, "unknown portfolio validator"
        ):
            write_receipt(self.root, self.rules, self.receipt)

    def test_p4_p5_science_contract_validator_is_wired(self):
        paths = {}
        for key in ("p4_primary", "p4_harmonics", "p5_robustness"):
            relative = f"receipts/{key}.json"
            path = self.root / relative
            path.parent.mkdir(exist_ok=True)
            path.write_text("{}\n", encoding="utf-8")
            paths[key] = relative
        subprocess.run(["git", "add", "receipts"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "add science receipts"], cwd=self.root, check=True)
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_validators"] = ["p4-p5-science-contracts"]
        payload["p4_p5_science_contract_paths"] = paths
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        expected = {
            "schema": "bigbounce.p4-p5-science-contracts/v1",
            "verdict": "PASS",
            "receipts": {},
        }
        with (
            self.registry_patch(),
            mock.patch("bigbounce_preflight.verify_p4_p5_science_contracts", return_value=expected) as verifier,
        ):
            receipt = write_receipt(self.root, self.rules, self.receipt)
        verifier.assert_called_once_with(self.root.resolve(), paths)
        self.assertEqual(receipt["portfolio_validators"][0]["id"], "p4-p5-science-contracts")
        self.assertEqual(receipt["portfolio_validators"][0]["verdict"], "PASS")

    def test_p1b_science_contract_validator_is_wired(self):
        paths = {
            key: f"receipts/{key}.json"
            for key in (
                "manuscript",
                "namaster_summary",
                "namaster_c10_receipt",
                "namaster_declared_receipt",
                "bbn_execution_receipt",
                "s8_overlay_receipt",
                "analysis_manifest",
            )
        }
        for relative in paths.values():
            path = self.root / relative
            path.parent.mkdir(exist_ok=True)
            path.write_text("{}\n", encoding="utf-8")
        subprocess.run(["git", "add", "receipts"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "add p1b receipts"], cwd=self.root, check=True)
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_validators"] = ["p1b-science-contracts"]
        payload["p1b_science_contract_paths"] = paths
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        expected = {
            "schema": "bigbounce.p1b-science-contracts/v1",
            "verdict": "PASS",
            "contracts": {},
        }
        with (
            self.registry_patch(),
            mock.patch("bigbounce_preflight.verify_p1b_science_contracts", return_value=expected) as verifier,
        ):
            receipt = write_receipt(self.root, self.rules, self.receipt)
        verifier.assert_called_once_with(self.root.resolve(), paths)
        self.assertEqual(receipt["portfolio_validators"][0]["id"], "p1b-science-contracts")

    def test_p1b_analysis_manifest_uses_catalog_path(self):
        relative = "receipts/current-p1b-manifest.json"
        path = self.root / relative
        path.parent.mkdir(exist_ok=True)
        path.write_text("{}\n", encoding="utf-8")
        subprocess.run(["git", "add", "receipts"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "add current manifest"], cwd=self.root, check=True)
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_validators"] = ["p1b-analysis-manifest"]
        payload["p1b_science_contract_paths"] = {"analysis_manifest": relative}
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        expected = {"schema": "test-manifest/v1", "verdict": "PASS"}
        with (
            self.registry_patch(),
            mock.patch("bigbounce_preflight.verify_manifest", return_value=expected) as verifier,
        ):
            receipt = write_receipt(self.root, self.rules, self.receipt)
        verifier.assert_called_once_with(
            self.root.resolve(), self.root.resolve() / relative
        )
        self.assertEqual(receipt["portfolio_validators"][0]["verdict"], "PASS")

    def test_p1b_analysis_manifest_requires_catalog_path(self):
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_validators"] = ["p1b-analysis-manifest"]
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        with self.registry_patch(), self.assertRaisesRegex(
            PortfolioError, "requires .*analysis_manifest"
        ):
            write_receipt(self.root, self.rules, self.receipt)

    def test_ci_shell_portability_validator_is_wired(self):
        relative = ".github/workflows/test.yml"
        path = self.root / relative
        path.parent.mkdir(parents=True)
        path.write_text("jobs: {}\n", encoding="utf-8")
        subprocess.run(["git", "add", relative], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "add workflow"], cwd=self.root, check=True)
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_validators"] = ["ci-shell-portability"]
        payload["ci_shell_portability_paths"] = [relative]
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        expected = {
            "schema": "bigbounce.ci-shell-portability/v1",
            "verdict": "PASS",
            "workflows": [],
            "workflow_count": 1,
            "findings": [],
            "finding_count": 0,
            "receipt_sha256": "0" * 64,
        }
        with (
            self.registry_patch(),
            mock.patch(
                "bigbounce_preflight.verify_ci_shell_portability",
                return_value=expected,
            ) as verifier,
        ):
            receipt = write_receipt(self.root, self.rules, self.receipt)
        verifier.assert_called_once_with(self.root.resolve(), [relative])
        self.assertEqual(receipt["portfolio_validators"][0]["id"], "ci-shell-portability")

    def test_ci_shell_portability_failure_fails_closed(self):
        relative = ".github/workflows/test.yml"
        path = self.root / relative
        path.parent.mkdir(parents=True)
        path.write_text("jobs: {}\n", encoding="utf-8")
        subprocess.run(["git", "add", relative], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "add workflow"], cwd=self.root, check=True)
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_validators"] = ["ci-shell-portability"]
        payload["ci_shell_portability_paths"] = [relative]
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        failed = {
            "schema": "bigbounce.ci-shell-portability/v1",
            "verdict": "FAIL",
            "findings": [{"path": relative, "step": "Example"}],
        }
        with (
            self.registry_patch(),
            mock.patch(
                "bigbounce_preflight.verify_ci_shell_portability",
                return_value=failed,
            ),
            self.assertRaisesRegex(PortfolioError, "shell-portability"),
        ):
            write_receipt(self.root, self.rules, self.receipt)

    def test_unsafe_portfolio_engine_path_fails_closed(self):
        payload = json.loads(self.rules.read_text(encoding="utf-8"))
        payload["portfolio_engine_paths"] = ["../../outside.py"]
        self.rules.write_text(json.dumps(payload), encoding="utf-8")
        with self.registry_patch(), self.assertRaisesRegex(
            PortfolioError, "unsafe or unknown path"
        ):
            write_receipt(self.root, self.rules, self.receipt)

    def test_dirty_canonical_input_fails_closed(self):
        source = self.root / self.registry["P1A"]["tex_path"]
        source.write_text(source.read_text(encoding="utf-8") + "% dirty\n", encoding="utf-8")
        with self.registry_patch(), self.assertRaisesRegex(PortfolioError, "inputs are dirty"):
            write_receipt(self.root, self.rules, self.receipt)
        self.assertFalse(self.receipt.exists())

    def add_draft_fixture(self, paper_id: str = "P1C") -> dict[str, str]:
        directory = self.root / "papers" / paper_id
        directory.mkdir(parents=True)
        tex_rel = f"papers/{paper_id}/paper.tex"
        pdf_rel = f"papers/{paper_id}/paper.pdf"
        (self.root / tex_rel).write_text(
            "\\newcommand{\\paperVersion}{v1C.0.1}\n\\begin{document}\nDRAFT\n\\end{document}\n",
            encoding="utf-8",
        )
        shutil.copy2(ROOT / "arxiv/paper1a_ech_nogo.pdf", self.root / pdf_rel)
        entry = {
            "tex_path": tex_rel, "pdf_path": pdf_rel, "site_slug": paper_id.lower(),
            "target_journal": "Journal", "article_type": "Draft", "review_profile": "PROFILE",
        }
        (self.root / "project-context/draft_paper_registry.json").write_text(
            json.dumps({paper_id: entry}), encoding="utf-8",
        )
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "add draft paper"], cwd=self.root, check=True)
        return entry

    def test_draft_records_bind_and_verify(self):
        self.add_draft_fixture()
        with self.registry_patch():
            written = write_receipt(self.root, self.rules, self.receipt)
            verified = verify_receipt(self.root, self.rules, self.receipt)
        self.assertEqual(written["verdict"], "PASS")
        self.assertEqual(written["paper_count"], 6)
        self.assertEqual(len(written["papers"]), 7)
        self.assertEqual(
            tuple(p["paper_id"] for p in written["papers"]), CANONICAL_IDS + ("P1C",)
        )
        draft = written["papers"][-1]
        self.assertTrue(draft["draft"])
        self.assertEqual(draft["version"], "v1C.0.1")
        self.assertEqual(len(draft["pdf"]["sha256"]), 64)
        self.assertTrue(all("draft" not in p for p in written["papers"][:6]))
        self.assertEqual(verified["receipt_sha256"], written["receipt_sha256"])

    def test_old_receipt_without_drafts_still_verifies_canonical(self):
        self.add_draft_fixture()
        # Simulate a receipt produced by the pre-draft-aware code: no draft
        # records, even though the draft registry now exists in the repo.
        with self.registry_patch(), mock.patch(
            "bigbounce_preflight.load_draft_registry", return_value={}
        ):
            written = write_receipt(self.root, self.rules, self.receipt)
        self.assertEqual(len(written["papers"]), 6)
        with self.registry_patch():
            verified = verify_receipt(self.root, self.rules, self.receipt)
        self.assertEqual(verified["verdict"], "PASS")

    def test_tampered_draft_pdf_fails_only_the_draft(self):
        draft_entry = self.add_draft_fixture()
        with self.registry_patch():
            write_receipt(self.root, self.rules, self.receipt)
        with (self.root / draft_entry["pdf_path"]).open("ab") as handle:
            handle.write(b"\n% draft tamper\n")
        cache = self.root / "cache"
        with self.registry_patch():
            # Canonical verification is untouched by the stale draft.
            verify_receipt(self.root, self.rules, self.receipt)
            # Canonical dispatch still passes.
            packet = build_packet(
                self.root, "P1A", self.registry["P1A"], b"prompt", b"", "model",
                "effort", cache_root=cache, preflight_receipt=self.receipt,
            )
            self.assertEqual(packet["paper_id"], "P1A")
            # Draft dispatch fails on the tampered PDF.
            with self.assertRaises((RuntimeError, ValueError)):
                build_packet(
                    self.root, "P1C", draft_entry, b"prompt", b"", "model",
                    "effort", cache_root=cache, preflight_receipt=self.receipt,
                )

    def test_intact_draft_is_dispatchable(self):
        draft_entry = self.add_draft_fixture()
        cache = self.root / "cache"
        with self.registry_patch():
            write_receipt(self.root, self.rules, self.receipt)
            packet = build_packet(
                self.root, "P1C", draft_entry, b"prompt", b"", "model",
                "effort", cache_root=cache, preflight_receipt=self.receipt,
            )
        self.assertEqual(packet["paper_id"], "P1C")
        self.assertEqual(packet["paper_version"], "v1C.0.1")

    def test_dirty_draft_input_fails_run_closed(self):
        draft_entry = self.add_draft_fixture()
        with (self.root / draft_entry["pdf_path"]).open("ab") as handle:
            handle.write(b"\n% dirty draft\n")
        with self.registry_patch(), self.assertRaisesRegex(
            PortfolioError, "draft paper inputs are dirty"
        ):
            write_receipt(self.root, self.rules, self.receipt)
        self.assertFalse(self.receipt.exists())

    def test_draft_registry_may_not_redefine_canonical(self):
        (self.root / "project-context/draft_paper_registry.json").write_text(
            json.dumps({"P1A": self.registry["P1A"]}), encoding="utf-8",
        )
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "bad draft registry"], cwd=self.root, check=True)
        with self.registry_patch(), self.assertRaisesRegex(
            PortfolioError, "may not redefine canonical"
        ):
            write_receipt(self.root, self.rules, self.receipt)

    def test_repository_catalog_passes_current_canonical_sources(self):
        result = load_engine().evaluate(
            ROOT, ROOT / "project-context/pre-review-rules.json"
        )
        self.assertGreaterEqual(result["rule_count"], 9)
        self.assertEqual(result["verdict"], "PASS", json.dumps(result["findings"], indent=2))


if __name__ == "__main__":
    unittest.main()
