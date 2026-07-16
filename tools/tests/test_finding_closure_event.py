import importlib.util
import json
import pathlib
import subprocess
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).parents[1] / "finding_closure_event.py"
SPEC = importlib.util.spec_from_file_location("closure_event", SCRIPT)
closure_event = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(closure_event)


class FindingClosureEventTests(unittest.TestCase):
    def fixture(self, root):
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
        evidence = root / "evidence.txt"
        evidence.write_text("closed\n")
        subprocess.run(["git", "add", "evidence.txt"], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "closure"], cwd=root, check=True)
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        event = closure_event.stamp({
            "schema_version": "finding-closure-event/v1",
            "finding_event_id": "fev1_" + "a" * 24,
            "status": "CLOSED",
            "closed_in_version": "v2",
            "closure_commit": commit,
            "occurred_at": "2026-07-16T00:00:00Z",
            "action": "fixed",
            "evidence": [{
                "path": "evidence.txt",
                "sha256": closure_event.hashlib.sha256(b"closed\n").hexdigest(),
            }],
        })
        return event

    def test_validates_and_appends_idempotently(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            event = self.fixture(root)
            ids = {event["finding_event_id"]}
            ledger = root / "closures.jsonl"
            self.assertEqual(closure_event.append(ledger, event, repo=root, finding_event_ids=ids), "appended")
            self.assertEqual(closure_event.append(ledger, event, repo=root, finding_event_ids=ids), "idempotent")

    def test_rejects_changed_evidence_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            event = self.fixture(root)
            event["evidence"][0]["sha256"] = "0" * 64
            event = closure_event.stamp(event)
            with self.assertRaisesRegex(closure_event.ClosureError, "sha256"):
                closure_event.validate(event, repo=root, finding_event_ids={event["finding_event_id"]})

    def test_rejects_unknown_finding(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            event = self.fixture(root)
            with self.assertRaisesRegex(closure_event.ClosureError, "absent"):
                closure_event.validate(event, repo=root, finding_event_ids=set())


if __name__ == "__main__":
    unittest.main()
