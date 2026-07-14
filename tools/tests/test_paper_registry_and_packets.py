#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from paper_registry import CANONICAL_IDS, load_registry, repo_root  # noqa: E402
from review_packet import build_packet, packet_key, publish_packet, sha256_file  # noqa: E402


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

    def tearDown(self):
        self.tmp.cleanup()

    def packet(self, expected=None):
        return build_packet(
            self.root, "PTEST", self.entry, b"prompt", b"context",
            "model-x", "high", expected, self.root / "cache",
        )

    def test_exact_key_reuse(self):
        packet = self.packet(sha256_file(self.root / "paper/test.pdf"))
        path, reused = publish_packet(packet, self.root / "packets", b"prompt", b"context")
        self.assertFalse(reused)
        same, reused = publish_packet(packet, self.root / "packets", b"prompt", b"context")
        self.assertEqual(path, same)
        self.assertTrue(reused)
        self.assertEqual(json.loads(path.read_text()), packet)
        self.assertEqual(path.with_suffix(".prompt").read_bytes(), b"prompt")
        self.assertEqual(path.with_suffix(".context").read_bytes(), b"context")

    def test_labeled_key_has_no_concatenation_ambiguity(self):
        left = packet_key("ab", "c", "d", "e", "f")
        right = packet_key("a", "bc", "d", "e", "f")
        self.assertNotEqual(left, right)

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
