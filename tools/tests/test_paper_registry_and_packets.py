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

from paper_registry import CANONICAL_IDS, load_registry, repo_root  # noqa: E402
from bigbounce_preflight import (  # noqa: E402
    PortfolioError,
    canonical_bytes,
    sha256 as preflight_sha256,
)
from review_packet import (  # noqa: E402
    build_packet,
    page_count,
    packet_key,
    publish_packet,
    resolve_pdf_snapshot,
    sha256_bytes,
    sha256_file,
)


class RegistryTests(unittest.TestCase):
    def test_canonical_six(self):
        papers = load_registry(ROOT)
        self.assertEqual(tuple(papers), CANONICAL_IDS)
        self.assertEqual(len({p["site_slug"] for p in papers.values()}), 6)
        self.assertTrue(papers["P3"]["tex_path"].endswith("paper3_apjs.tex"))
        self.assertTrue(papers["P3"]["pdf_path"].endswith("paper3_apjs.pdf"))
        for entry in papers.values():
            self.assertTrue(entry["target_journal"])
            self.assertTrue(entry["article_type"])
            self.assertTrue(entry["review_profile"])

    def test_dynamic_root(self):
        self.assertEqual(repo_root(), ROOT)
        for path in (ROOT / "tools/paper_registry.py", ROOT / "project-context/paper_registry.json"):
            self.assertNotIn("CODE_2025", path.read_text(encoding="utf-8"))


class PacketTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="review_packet_test_")
        self.root = Path(self.tmp.name)
        (self.root / "paper").mkdir()
        (self.root / "paper/test.tex").write_text(
            r"\newcommand{\paperVersion}{vTEST.1}" + "\n", encoding="utf-8"
        )
        shutil.copy2(ROOT / "arxiv/paper1a_ech_nogo.pdf", self.root / "paper/test.pdf")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Packet Test"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "paper"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.root, check=True)
        self.entry = {
            "tex_path": "paper/test.tex", "pdf_path": "paper/test.pdf",
            "site_slug": "paper-test", "target_journal": "Test Journal",
            "article_type": "Research Article", "review_profile": "TEST-PROFILE",
        }
        self.preflight_path = self.root / "preflight.json"
        self.write_preflight()

    def tearDown(self):
        self.tmp.cleanup()

    def write_preflight(self, *, verdict="PASS"):
        source = self.root / "paper/test.tex"
        pdf = self.root / "paper/test.pdf"
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.root, text=True).strip()
        paper = {
            "paper_id": "PTEST", "verdict": "PASS",
            "version": "vTEST.1", "pages": page_count(pdf),
            "source": {"path": "paper/test.tex", "bytes": source.stat().st_size, "sha256": sha256_file(source)},
            "pdf": {"path": "paper/test.pdf", "bytes": pdf.stat().st_size, "sha256": sha256_file(pdf)},
        }
        receipt = {
            "schema": "bigbounce.pre-review-portfolio-receipt/v1",
            "repository_head": head,
            "registry": {}, "generic_engine": {}, "generic_rule_receipt": {"verdict": "PASS"},
            "generic_rule_receipt_sha256": "g" * 64,
            "papers": [paper], "paper_count": 1, "verdict": verdict,
        }
        receipt["core_sha256"] = preflight_sha256(canonical_bytes(receipt))
        receipt["generated_at"] = "2026-01-01T00:00:00Z"
        receipt["receipt_sha256"] = preflight_sha256(canonical_bytes(receipt))
        self.preflight_path.write_text(json.dumps(receipt), encoding="utf-8")

    def packet(self, expected=None):
        patch = mock.patch("review_packet.verify_receipt", return_value=json.loads(self.preflight_path.read_text()))
        with patch:
            return self._packet(expected)

    def _packet(self, expected=None, receipt=None):
        return build_packet(
            self.root, "PTEST", self.entry, b"prompt", b"context",
            "model-x", "high", expected, self.root / "cache",
            preflight_receipt=receipt or self.preflight_path,
        )

    def test_exact_key_reuse(self):
        packet = self.packet(sha256_file(self.root / "paper/test.pdf"))
        path, reused = publish_packet(packet, self.root / "packets", b"prompt", b"context")
        self.assertFalse(reused)
        same, reused = publish_packet(packet, self.root / "packets", b"prompt", b"context")
        self.assertEqual(path, same)
        self.assertTrue(reused)
        self.assertEqual(json.loads(path.read_text()), packet)
        self.assertEqual((path.parent / "prompt.bin").read_bytes(), b"prompt")
        self.assertEqual((path.parent / "allowed-context.bin").read_bytes(), b"context")
        self.assertEqual(
            resolve_pdf_snapshot(packet, self.root / "cache"),
            self.root / "cache" / "pdf" / f"{packet['pdf_sha256']}.pdf",
        )
        self.assertEqual(
            packet["pdf_snapshot_path"], f"pdf/{packet['pdf_sha256']}.pdf",
        )

    def test_labeled_key_has_no_concatenation_ambiguity(self):
        left = packet_key("ab", "c", "d", "ctx", "e", "f", "preflight")
        right = packet_key("a", "bc", "d", "ctx", "e", "f", "preflight")
        self.assertNotEqual(left, right)

    def test_context_hash_changes_packet_key(self):
        common = ("pdf", "profile", "prompt")
        left = packet_key(*common, sha256_bytes(b"left"), "model", "high", "preflight")
        right = packet_key(*common, sha256_bytes(b"right"), "model", "high", "preflight")
        self.assertNotEqual(left, right)

    def test_preflight_hash_changes_packet_key(self):
        common = ("pdf", "profile", "prompt", "context", "model", "high")
        self.assertNotEqual(packet_key(*common, "left"), packet_key(*common, "right"))

    def test_equivalent_regenerated_preflight_reuses_packet(self):
        first_preflight = json.loads(self.preflight_path.read_text())
        second_preflight = dict(first_preflight)
        second_preflight["generated_at"] = "2026-01-02T00:00:00Z"
        second_preflight["receipt_sha256"] = "f" * 64
        with mock.patch("review_packet.verify_receipt", return_value=first_preflight):
            first = self._packet()
        with mock.patch("review_packet.verify_receipt", return_value=second_preflight):
            second = self._packet()
        self.assertEqual(first, second)
        self.assertEqual(first["schema_version"], 4)
        self.assertNotIn("receipt_sha256", first["preflight"])
        _, reused = publish_packet(first, self.root / "packets", b"prompt", b"context")
        _, reused = publish_packet(second, self.root / "packets", b"prompt", b"context")
        self.assertTrue(reused)

    def test_missing_preflight_fails_closed(self):
        with mock.patch.dict("os.environ", {}, clear=True):
            with self.assertRaisesRegex(ValueError, "preflight receipt is required"):
                build_packet(self.root, "PTEST", self.entry, b"p", b"c", "m", "high")

    def test_preflight_can_be_supplied_by_environment(self):
        preflight = json.loads(self.preflight_path.read_text())
        with mock.patch.dict("os.environ", {"BIGBOUNCE_PREFLIGHT_RECEIPT": str(self.preflight_path)}), \
             mock.patch("review_packet.verify_receipt", return_value=preflight):
            packet = build_packet(
                self.root, "PTEST", self.entry, b"prompt", b"context",
                "model-x", "high", cache_root=self.root / "cache",
            )
        self.assertEqual(packet["preflight"]["core_sha256"], preflight["core_sha256"])

    def test_non_pass_preflight_fails_closed(self):
        with mock.patch("review_packet.verify_receipt", side_effect=PortfolioError("not a PASS receipt")):
            with self.assertRaisesRegex(PortfolioError, "not a PASS"):
                self._packet()

    def test_wrong_preflight_paper_binding_fails_closed(self):
        preflight = json.loads(self.preflight_path.read_text())
        preflight["papers"][0]["source"]["sha256"] = "0" * 64
        with mock.patch("review_packet.verify_receipt", return_value=preflight):
            with self.assertRaisesRegex(ValueError, "do not match PASS portfolio"):
                self._packet()

    def test_incomplete_packet_is_not_reused(self):
        packet = self.packet()
        packet_dir = self.root / "packets" / "PTEST" / packet["packet_key"]
        packet_dir.mkdir(parents=True)
        (packet_dir / "packet.json").write_text("{}", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "incomplete packet"):
            publish_packet(packet, self.root / "packets", b"prompt", b"context")

    def test_failed_publish_leaves_no_partial_packet(self):
        packet = self.packet()
        parent = self.root / "packets" / "PTEST"
        with mock.patch("review_packet.os.fsync", side_effect=OSError("injected")):
            with self.assertRaisesRegex(OSError, "injected"):
                publish_packet(packet, self.root / "packets", b"prompt", b"context")
        self.assertFalse((parent / packet["packet_key"]).exists())
        self.assertEqual(list(parent.iterdir()), [])

    def test_source_is_rechecked_after_pdf_snapshot(self):
        from review_packet import freeze_pdf as real_freeze_pdf

        def freeze_then_mutate(pdf, cache_root):
            result = real_freeze_pdf(pdf, cache_root)
            with (self.root / "paper/test.tex").open("a", encoding="utf-8") as handle:
                handle.write("% changed during snapshot\n")
            return result

        with mock.patch("review_packet.freeze_pdf", side_effect=freeze_then_mutate):
            with self.assertRaisesRegex(RuntimeError, "inputs are dirty"):
                self.packet()

    def test_hash_mismatch_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "PDF SHA mismatch"):
            self.packet("0" * 64)

    def test_dirty_input_fails_closed(self):
        with (self.root / "paper/test.tex").open("a", encoding="utf-8") as handle:
            handle.write("% dirty\n")
        with self.assertRaisesRegex(RuntimeError, "inputs are dirty"):
            self.packet()


if __name__ == "__main__":
    unittest.main()
