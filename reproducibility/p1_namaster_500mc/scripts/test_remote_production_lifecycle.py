#!/usr/bin/env python3

import hashlib
import base64
import json
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_remote_bootstrap as bootstrap
import remote_production_runner as runner


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RemoteLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.repo, check=True)
        (self.repo / "bound.txt").write_text("bound\n")
        subprocess.run(["git", "add", "bound.txt"], cwd=self.repo, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.repo, check=True)
        self.commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.repo, text=True).strip()
        self.state = Path(self.tmp.name) / "state"
        jobs = []
        for i in range(9):
            kind = "canonical" if i == 0 else "robustness"
            out = f"out/job{i}.txt"
            jobs.append({"name": f"job{i}", "kind": kind,
                         "command": f"mkdir -p out; printf job{i} > {out}", "outputs": [out]})
        self.manifest = {
            "contract_id": "test", "git_commit": self.commit,
            "input_sha256": {"bound.txt": digest(self.repo / "bound.txt")},
            "container": {"install": ["true"]}, "execution_jobs": jobs,
            "merge_job": {"name": "strict-merge", "kind": "merge",
                          "command": "test -f out/job8.txt; printf merged > out/merged.txt",
                          "outputs": ["out/merged.txt"]},
        }

    def tearDown(self):
        self.tmp.cleanup()

    def test_wrong_commit_and_hash_fail_closed(self):
        bad = dict(self.manifest, git_commit="0" * 40)
        with self.assertRaisesRegex(ValueError, "HEAD"):
            runner.run(self.repo, bad, self.state)
        bad = dict(self.manifest, input_sha256={"bound.txt": "0" * 64})
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            runner.run(self.repo, bad, self.state)

    def test_failure_never_promotes_completion(self):
        self.manifest["execution_jobs"][3]["command"] = "exit 7"
        with self.assertRaisesRegex(RuntimeError, "job failed"):
            runner.run(self.repo, self.manifest, self.state)
        self.assertFalse((self.state / "production.complete.json").exists())
        self.assertTrue((self.state / "job3.failed.json").exists())

    def test_resume_skips_only_verified_completion(self):
        runner.run(self.repo, self.manifest, self.state)
        receipt = self.state / "job0.receipt.json"
        before = receipt.read_bytes()
        runner.run(self.repo, self.manifest, self.state)
        self.assertEqual(before, receipt.read_bytes())
        (self.repo / "out/job1.txt").write_text("tampered")
        runner.run(self.repo, self.manifest, self.state)
        self.assertEqual((self.repo / "out/job1.txt").read_text(), "job1")

    def test_missing_shard_and_merge_failure_do_not_promote(self):
        self.manifest["execution_jobs"][8]["command"] = "true"
        with self.assertRaisesRegex(RuntimeError, "missing outputs"):
            runner.run(self.repo, self.manifest, self.state)
        self.assertFalse((self.state / "production.complete.json").exists())
        failed_status = json.loads((self.state / "job8.status.json").read_text())
        self.assertEqual(failed_status["state"], "failed")
        self.assertIn("missing outputs", failed_status["reason"])
        self.assertIn("log_sha256", failed_status)
        self.assertFalse((self.state / "job8.receipt.json").exists())
        self.manifest["execution_jobs"][8]["command"] = "mkdir -p out; printf job8 > out/job8.txt"
        self.manifest["merge_job"]["command"] = "exit 9"
        with self.assertRaisesRegex(RuntimeError, "strict-merge"):
            runner.run(self.repo, self.manifest, self.state)
        self.assertFalse((self.state / "production.complete.json").exists())

    def test_full_success_and_bootstrap_generation(self):
        final = runner.run(self.repo, self.manifest, self.state)
        self.assertEqual(final["state"], "complete")
        self.assertEqual(final["job_count"], 9)
        argv = bootstrap.generate(self.manifest, Path("/tmp/manifest.json"),
                                  Path("/tmp/clean-work"), Path("/tmp/state"))
        self.assertEqual(argv[:2], ["bash", "-lc"])
        self.assertIn("git checkout --detach", argv[2])
        self.assertIn(self.commit, argv[2])
        self.assertIn("sha256sum -c -", argv[2])
        self.assertIn("remote_production_runner.py", argv[2])
        self.assertNotIn("/tmp/manifest.json", argv[2])
        canonical = bootstrap.canonical_manifest_bytes(self.manifest)
        encoded = base64.b64encode(canonical).decode("ascii")
        self.assertIn(encoded, argv[2])
        self.assertIn(hashlib.sha256(canonical).hexdigest(), argv[2])
        self.assertEqual(base64.b64decode(encoded), canonical)
        self.assertIn("bound-production-manifest.json", argv[2])

    def test_generated_bootstrap_executes_fresh_local_clone(self):
        source = Path(self.tmp.name) / "bootstrap-source"
        runner_path = source / "reproducibility/p1_namaster_500mc/scripts/remote_production_runner.py"
        runner_path.parent.mkdir(parents=True)
        (source / "bound.txt").write_text("bootstrap-bound\n")
        runner_path.write_text(
            "#!/usr/bin/env python3\n"
            "import argparse, pathlib\n"
            "p=argparse.ArgumentParser(); p.add_argument('--manifest'); "
            "p.add_argument('--repo'); p.add_argument('--state-dir'); a=p.parse_args()\n"
            "pathlib.Path(a.state_dir).mkdir(parents=True, exist_ok=True)\n"
            "pathlib.Path(a.state_dir, 'fake-runner.success').write_text('ok\\n')\n"
        )
        subprocess.run(["git", "init", "-q"], cwd=source, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=source, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=source, check=True)
        subprocess.run(["git", "add", "."], cwd=source, check=True)
        subprocess.run(["git", "commit", "-qm", "bootstrap fixture"], cwd=source, check=True)
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
        manifest = {
            "git_commit": commit,
            "input_sha256": {
                "bound.txt": digest(source / "bound.txt"),
                "reproducibility/p1_namaster_500mc/scripts/remote_production_runner.py": digest(runner_path),
            },
            "container": {"install": ["true"]},
        }
        workspace = Path(self.tmp.name) / "fresh-workspace"
        state = Path(self.tmp.name) / "remote-state"
        with mock.patch.object(bootstrap, "REPO_URL", str(source)):
            argv = bootstrap.generate(manifest, Path("/definitely/local/manifest.json"), workspace, state)
        result = subprocess.run(argv, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        cloned = workspace / "bigbounce"
        cloned_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=cloned, text=True).strip()
        self.assertEqual(cloned_head, commit)
        branch = subprocess.run(["git", "symbolic-ref", "-q", "HEAD"], cwd=cloned, check=False)
        self.assertNotEqual(branch.returncode, 0)
        embedded = state / "bound-production-manifest.json"
        self.assertEqual(embedded.read_bytes(), bootstrap.canonical_manifest_bytes(manifest))
        self.assertEqual(digest(embedded), hashlib.sha256(bootstrap.canonical_manifest_bytes(manifest)).hexdigest())
        self.assertEqual((state / "fake-runner.success").read_text(), "ok\n")


if __name__ == "__main__":
    unittest.main()
