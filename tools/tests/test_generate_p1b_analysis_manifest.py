#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "reproducibility" / "generate_p1b_analysis_manifest.py"
SPEC = importlib.util.spec_from_file_location("generate_p1b_manifest", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
manifest = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(manifest)


class GenerateP1BAnalysisManifestTests(unittest.TestCase):
    def test_version_is_derived_from_manuscript(self):
        self.assertEqual(manifest.manuscript_version(), "v1B.0.112")

    def test_transient_checkpoints_are_excluded(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            directory = Path(tmp)
            (directory / "summary.json").write_text("{}\n", encoding="utf-8")
            (directory / ".checkpoint.json").write_text("{}\n", encoding="utf-8")
            with mock.patch.object(manifest, "CURRENT_RESULT_DIRECTORY", directory):
                artifacts = manifest.current_result_artifacts()
        self.assertEqual(len(artifacts), 1)
        self.assertTrue(artifacts[0].endswith("/summary.json"))

    def test_current_contract_includes_new_provenance(self):
        required = {
            "reproducibility/cosmology/frozen/bbn_execution_receipt.json",
            "reproducibility/cosmology/c13_s8_desy3_overlay_postburn.json.receipt.json",
            "reproducibility/p1_namaster_500mc/scripts/multipole_contract.py",
            "reproducibility/p1_namaster_500mc/scripts/physical_spectra.py",
        }
        self.assertTrue(required.issubset(set(manifest.CURRENT_FIXED_ARTIFACTS)))

    def test_commit_blob_record_preserves_lfs_pointer_semantics(self):
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
        relative = (
            "reproducibility/cosmology/frozen/full_tension_20260311_1728/"
            "chains/chain_01/spin_torsion.1.txt"
        )
        record = manifest.artifact_record_at_commit(relative, commit)
        self.assertEqual(record["storage"], "git-lfs-pointer")
        self.assertEqual(record["local_git_blob_bytes"], 133)
        self.assertEqual(len(record["lfs_oid_sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
