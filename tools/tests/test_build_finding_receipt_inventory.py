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

    def test_external_verbatim_boundary_and_bold_tags_are_explicit(self):
        body = """# EXT Review — P4 × Gemini
## Raw verbatim response
**VERDICT:** MAJOR REVISIONS
**ISSUES:**
1. **[MAJOR] First issue.**
2. **[MINOR] Second issue.**
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("ok", 2, "explicit severity-tagged findings"),
        )

    def test_explicit_none_may_be_followed_by_support_sentence(self):
        body = """# INT API Review — P2
RAW RESPONSE (verbatim):
(1) VERDICT: ACCEPT
(2) ISSUES: None. All targeted findings are closed.
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("ok", 0, "explicit clean-review statement"),
        )

    def test_bold_prose_severity_word_without_tag_is_not_counted(self):
        body = """# INT API Review — P3
RAW RESPONSE
**VERDICT:** MAJOR REVISIONS
The major concern is described without a severity tag.
"""
        status, count, _ = inventory.parse_receipt(body)
        self.assertEqual(status, "parse_error")
        self.assertIsNone(count)

    def test_explicit_errored_leg_inside_raw_is_failed_not_clean(self):
        body = """# INT Codex-subscription Review — P5
RAW RESPONSE (verbatim):
(Codex subscription leg errored; diagnostics retained elsewhere)
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("failed", None, "explicit provider failure in raw response"),
        )

    def test_markdown_bullet_before_tag_is_counted(self):
        body = """# INT API Review — P3
RAW RESPONSE
* **[MINOR]** One explicit issue.
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("ok", 1, "explicit severity-tagged findings"),
        )

    def test_bold_numbered_severity_tag_is_counted(self):
        body = """# INT API Review — P3
RAW RESPONSE
**1. [MINOR] First explicit issue.**
**2. [MINOR] Second explicit issue.**
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("ok", 2, "explicit severity-tagged findings"),
        )

    def test_single_explicit_severity_summary_count_is_counted(self):
        body = """# INT API Review — P3
RAW RESPONSE
Verdict: MINOR REVISIONS — 4 minor items, all presentation/hygiene.
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("ok", 4, "explicit severity-summary finding count"),
        )

    def test_matching_parsed_and_raw_accept_is_clean(self):
        body = """# INT API Review — P2
PARSED VERDICT: ACCEPT
RAW RESPONSE
**VERDICT: ACCEPT**
Prior issues are closed and require no fix.
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("ok", 0, "matching parsed and raw ACCEPT verdicts"),
        )

    def test_severity_sections_count_numbered_items_and_ignore_none(self):
        body = """# INT API Review — P5
RAW RESPONSE
MAJOR ISSUES:
None
MINOR ISSUES:
1. First issue.
2. Second issue.
REPRODUCIBILITY AND STATISTICAL CHECKS:
1. This numbered verification is not an issue.
"""
        self.assertEqual(
            inventory.parse_receipt(body),
            ("ok", 2, "explicit severity-section numbered findings"),
        )

    def test_explicit_none_variants_are_clean(self):
        for raw in ("ISSUES: (none)", "**ISSUES:**\nNone.", "2. `ISSUES: None`"):
            with self.subTest(raw=raw):
                status, count, _ = inventory.parse_receipt(
                    "# INT API Review — P2\nRAW RESPONSE\n" + raw + "\n"
                )
                self.assertEqual((status, count), ("ok", 0))

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
