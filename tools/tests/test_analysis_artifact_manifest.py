#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from verify_analysis_artifact_manifest import ManifestError, verify_manifest  # noqa: E402


class AnalysisArtifactManifestTests(unittest.TestCase):
    manifest = ROOT / "reproducibility/p1b_analysis_artifact_manifest_v1B.0.111.json"

    def test_canonical_p1b_manifest_matches_every_base_commit_blob(self):
        result = verify_manifest(ROOT, self.manifest)
        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual(result["artifact_count"], 230)
        self.assertEqual(result["storage_counts"], {"git-blob": 206, "git-lfs-pointer": 24})

    def test_one_recorded_byte_mutation_fails_closed(self):
        payload = json.loads(self.manifest.read_text(encoding="utf-8"))
        payload["artifacts"][0]["local_git_blob_bytes"] += 1
        with tempfile.TemporaryDirectory(prefix=".manifest_mutation_", dir=ROOT) as tmp:
            mutated = Path(tmp) / "manifest.json"
            mutated.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ManifestError, "blob byte mismatch"):
                verify_manifest(ROOT, mutated)


if __name__ == "__main__":
    unittest.main()
