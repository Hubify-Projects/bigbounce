from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from verify_bundle_manifest import verify  # noqa: E402


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="bundle_manifest_test_")
        self.root = Path(self.tmp.name)
        self.bundle = self.root / "bundle"
        self.bundle.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Bundle Test"], cwd=self.root, check=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write_manifest(self, files):
        lines = []
        for name, content in files.items():
            path = self.bundle / name
            path.write_bytes(content)
            lines.append(f"{hashlib.sha256(content).hexdigest()}  {name}")
        (self.bundle / "MANIFEST.sha256").write_text("\n".join(lines) + "\n")

    def commit(self):
        subprocess.run(["git", "add", "-f", "bundle"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "bundle"], cwd=self.root, check=True)

    def test_tracked_hashes_pass(self):
        self.write_manifest({"a.txt": b"a", "b.dat": b"b"})
        self.commit()
        self.assertEqual(verify(self.bundle), {"missing": [], "hash_mismatch": [], "ignored": [], "untracked": []})

    def test_ignored_and_untracked_reported_separately(self):
        (self.root / ".gitignore").write_text("*.log\n")
        subprocess.run(["git", "add", ".gitignore"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "ignore"], cwd=self.root, check=True)
        self.write_manifest({"build.log": b"log", "loose.txt": b"loose"})
        report = verify(self.bundle)
        self.assertEqual(report["ignored"], ["build.log"])
        self.assertEqual(report["untracked"], ["loose.txt"])

    def test_missing_and_hash_mismatch_failures(self):
        self.write_manifest({"a.txt": b"a", "gone.txt": b"gone"})
        self.commit()
        (self.bundle / "a.txt").write_bytes(b"changed")
        (self.bundle / "gone.txt").unlink()
        report = verify(self.bundle)
        self.assertEqual(report["hash_mismatch"], ["a.txt"])
        self.assertEqual(report["missing"], ["gone.txt"])


if __name__ == "__main__":
    unittest.main()
