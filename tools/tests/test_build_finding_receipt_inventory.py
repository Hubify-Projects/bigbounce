import importlib.util
import pathlib
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).parents[1] / "build_finding_receipt_inventory.py"
SPEC = importlib.util.spec_from_file_location("receipt_inventory", SCRIPT)
inventory = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(inventory)


class ReceiptInventoryTests(unittest.TestCase):
    def write(self, root, relative, body):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body)
        return path

    def test_counts_only_explicit_findings_and_clean_reviews(self):
        tagged = """# INT API Review — P4\nUTC: 2026-07-16T00:00:00Z\nRAW RESPONSE\n1. [MAJOR] one\n[MINOR] two\n"""
        clean = """# INT Codex-subscription Review — P4\nUTC: 2026-07-16T01:00:00Z\nRAW RESPONSE\nISSUES: NONE\n"""
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            root = base / "project-context" / "peer-reviews"
            self.write(root, "INT_v3/ROUND_2026-07-15/API_P4_grok.md", tagged)
            self.write(root, "INT_v3/ROUND_2026-07-15/intwave_P4_codex_0100.md", clean)
            result, report = inventory.build(root, inventory.DEFAULT_CUTOFF)
            self.assertEqual([row["finding_count"] for row in result["receipts"]], [2, 0])
            self.assertEqual(report["completed_fraction"], 1.0)
            self.assertEqual(result["generated_at"], "2026-07-16T01:00:00Z")

    def test_ambiguous_prose_is_an_explicit_parse_gap(self):
        body = """# INT API Review — P5\nRAW RESPONSE\nThe paper needs several changes.\n"""
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            root = base / "project-context" / "peer-reviews"
            self.write(root, "INT_v3/ROUND_2026-07-15/API_P5_gemini.md", body)
            result, report = inventory.build(root, inventory.DEFAULT_CUTOFF)
            self.assertEqual(result["receipts"][0]["status"], "parse_error")
            self.assertIsNone(result["receipts"][0]["finding_count"])
            self.assertIn("no explicit", report["gaps"][0]["reason"])

    def test_cutoff_is_exclusive_and_unrelated_markdown_is_ignored(self):
        body = "# INT API Review — P2\nRAW RESPONSE\n[MINOR] x\n"
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            root = base / "project-context" / "peer-reviews"
            self.write(root, "INT_v3/ROUND_2026-06-10/API_P2_grok.md", body)
            self.write(root, "INT_v3/ROUND_2026-07-15/TRUTH_AUDIT.md", body)
            result, _ = inventory.build(root, inventory.DEFAULT_CUTOFF)
            self.assertEqual(result["receipts"], [])


if __name__ == "__main__":
    unittest.main()
