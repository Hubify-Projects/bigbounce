#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"


class ProactiveSweepToolTests(unittest.TestCase):
    def artifact_check(self, relative: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(TOOLS / "artifact_crosscheck.py"), relative],
            cwd=ROOT, text=True, capture_output=True, timeout=30, check=False,
        )

    def test_contextual_artifact_paths_resolve_for_p1b_p2_and_p4(self):
        for relative in (
            "arxiv/paper1b_mcmc_companion.tex",
            "research/focused_paper_source_integration/02_full_draft.tex",
            "pipelines/p2_chirality/chirality_catalog_paper.tex",
        ):
            result = self.artifact_check(relative)
            self.assertEqual(result.returncode, 0, f"{relative}:\n{result.stdout}\n{result.stderr}")

    def test_missing_p5_desivast_join_is_a_real_failure(self):
        result = self.artifact_check(
            "pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex"
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("MISSING  data/desivast_matched_spirals.parquet", result.stdout)

    def test_pattern040_does_not_confuse_explicit_einstein_cartan_limit(self):
        result = subprocess.run(
            [sys.executable, str(TOOLS / "v3_pattern040_cross_section_check.py"),
             "arxiv/paper1a_ech_nogo.tex"],
            cwd=ROOT, text=True, capture_output=True, timeout=30, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_known_pattern_sweep_uses_current_registry(self):
        source = (TOOLS / "check_new_patterns.sh").read_text(encoding="utf-8")
        self.assertIn("project-context/paper_registry.json", source)
        self.assertNotIn("CODE_2025", source)
        self.assertNotIn("paper3_draft.tex", source)


if __name__ == "__main__":
    unittest.main()
