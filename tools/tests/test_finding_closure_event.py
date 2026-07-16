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

    def test_appends_batch_atomically_and_idempotently(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            first = self.fixture(root)
            second = closure_event.stamp({
                **{
                    key: value
                    for key, value in first.items()
                    if key not in {"closure_event_id", "content_hash"}
                },
                "finding_event_id": "fev1_" + "b" * 24,
                "action": "fixed second",
            })
            ids = {first["finding_event_id"], second["finding_event_id"]}
            ledger = root / "closures.jsonl"
            result = closure_event.append_many(
                ledger, [first, second], repo=root, finding_event_ids=ids
            )
            self.assertEqual([row["status"] for row in result], ["appended", "appended"])
            self.assertEqual(len(ledger.read_text().splitlines()), 2)
            replay = closure_event.append_many(
                ledger, [first, second], repo=root, finding_event_ids=ids
            )
            self.assertEqual(
                [row["status"] for row in replay],
                ["idempotent", "idempotent"],
            )
            self.assertEqual(len(ledger.read_text().splitlines()), 2)

    def test_rejects_entire_batch_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            first = self.fixture(root)
            invalid = closure_event.stamp({
                **{
                    key: value
                    for key, value in first.items()
                    if key not in {"closure_event_id", "content_hash"}
                },
                "finding_event_id": "fev1_" + "b" * 24,
                "evidence": [{"path": "evidence.txt", "sha256": "0" * 64}],
            })
            ledger = root / "closures.jsonl"
            with self.assertRaisesRegex(closure_event.ClosureError, "sha256"):
                closure_event.append_many(
                    ledger,
                    [first, invalid],
                    repo=root,
                    finding_event_ids={
                        first["finding_event_id"],
                        invalid["finding_event_id"],
                    },
                )
            self.assertFalse(ledger.exists())


if __name__ == "__main__":
    unittest.main()
