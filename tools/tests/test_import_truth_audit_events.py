import importlib.util
import json
import pathlib
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).parents[1] / "import_truth_audit_events.py"
SPEC = importlib.util.spec_from_file_location("batch_import", SCRIPT)
batch_import = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(batch_import)

ENGINE_PATH = pathlib.Path(
    "/Users/houstongolden/.claude/scistack/hubstack/learning-loop/"
    "r-round-finding-archive/scripts/finding_event.py"
)


class TruthAuditBatchImportTests(unittest.TestCase):
    def setUp(self):
        self.engine = batch_import.load_engine(ENGINE_PATH)

    def fixture(self, root):
        audit = root / "audit.md"
        receipt = root / "receipt.md"
        audit.write_text("truth audit\n")
        receipt.write_text("raw receipt\n")
        receipt_path = receipt.relative_to(root).as_posix()
        inventory = {
            "schema_version": "finding-receipt-inventory/v1",
            "generated_at": "2026-07-16T00:00:00Z",
            "receipts": [{
                "receipt_id": "receipt_test",
                "path": receipt_path,
                "sha256": batch_import.sha256(receipt),
                "status": "ok",
                "finding_count": 1,
            }],
        }
        batch = {
            "schema_version": "truth-audit-event-batch/v1",
            "paper": {"id": "P4", "version": "v1"},
            "source": {"round_id": "round", "round_type": "internal"},
            "pdf": {"sha256": "a" * 64, "pages": 1},
            "truth_audit": {
                "path": audit.relative_to(root).as_posix(),
                "sha256": batch_import.sha256(audit),
                "audited_at": "2026-07-16T01:00:00Z",
            },
            "catalog": {"version": "v", "updated_at": "2026-07-01T00:00:00Z"},
            "receipts": [{
                "path": receipt_path,
                "sha256": batch_import.sha256(receipt),
                "occurred_at": "2026-07-16T00:00:00Z",
                "reviewer": {
                    "provider": "provider", "model": "model", "reviewer_id": "id"
                },
                "findings": [{
                    "finding_id": "F1", "severity": "MINOR", "summary": "summary",
                    "truth_verdict": "VERIFIED", "truth_evidence": "evidence",
                    "classification": "NEW_REAL", "pattern_ids": [],
                    "preflight_checked": False, "preflight_intercepted": False,
                    "closure": {
                        "status": "OPEN", "action": "fix", "closed_in_version": None,
                        "evidence": "audit", "regression_of_event_id": None,
                    },
                }],
            }],
        }
        return batch, inventory, audit, receipt

    def test_builds_valid_canonical_event(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            batch, inventory, _, _ = self.fixture(root)
            events = batch_import.build_events(batch, inventory, root, self.engine)
            self.assertEqual(len(events), 1)
            self.engine.validate_event(events[0])

    def test_rejects_receipt_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            batch, inventory, _, receipt = self.fixture(root)
            receipt.write_text("mutated\n")
            with self.assertRaisesRegex(batch_import.BatchError, "sha256"):
                batch_import.build_events(batch, inventory, root, self.engine)

    def test_rejects_truth_audit_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            batch, inventory, audit, _ = self.fixture(root)
            audit.write_text("mutated audit\n")
            with self.assertRaisesRegex(batch_import.BatchError, "sha256"):
                batch_import.build_events(batch, inventory, root, self.engine)

    def test_rejects_finding_count_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            batch, inventory, _, _ = self.fixture(root)
            inventory["receipts"][0]["finding_count"] = 2
            with self.assertRaisesRegex(batch_import.BatchError, "expected 2"):
                batch_import.build_events(batch, inventory, root, self.engine)

    def test_append_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            batch, inventory, _, _ = self.fixture(root)
            event = batch_import.build_events(batch, inventory, root, self.engine)[0]
            ledger = root / "ledger.jsonl"
            self.assertEqual(self.engine.append_event(ledger, event), "appended")
            self.assertEqual(self.engine.append_event(ledger, event), "idempotent")


if __name__ == "__main__":
    unittest.main()
