from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.p1c_consistency_check import (
    DEFAULT_TEX,
    build_document,
    check_rule_a,
    check_rule_b,
    check_rule_c,
    check_rule_d,
    main,
    run_all_rules,
)


ROOT = Path(__file__).resolve().parents[2]


def _write(tmp: Path, name: str, text: str) -> Path:
    path = tmp / name
    path.write_text(text, encoding="utf-8")
    return path


class RuleAConstraintCountTests(unittest.TestCase):
    def test_passing_fixture_all_counts_agree(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "pass_a.tex",
                r"""
We catalog three distinct
mechanism-class constraints, one per catalog entry.

\caption{\label{tab:barriers} The 3 catalogue entries --- 3 distinct
mechanism-class constraints on routes.}

\medskip\noindent\textbf{B1 --- First (Found.\ A) [R1].} text here.
\medskip\noindent\textbf{B2 --- Second (Found.\ B) [R1].} text here.
\medskip\noindent\textbf{B3 --- Third (Found.\ C) [R2].} text here.
""",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_a(doc)
            self.assertTrue(result.passed, result.evidence)
            self.assertEqual(result.detail["actual_count"], 3)

    def test_failing_fixture_disagreeing_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "fail_a.tex",
                r"""
We catalog three distinct
mechanism-class constraints, one per catalog entry.

\caption{\label{tab:barriers} The 4 catalogue entries --- 4 distinct
mechanism-class constraints on routes.}

\medskip\noindent\textbf{B1 --- First (Found.\ A) [R1].} text here.
\medskip\noindent\textbf{B2 --- Second (Found.\ B) [R1].} text here.
\medskip\noindent\textbf{B3 --- Third (Found.\ C) [R2].} text here.
""",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_a(doc)
            self.assertFalse(result.passed)
            self.assertEqual(result.detail["actual_count"], 3)
            values = {v for _, v, _ in result.detail["sites"]}
            self.assertEqual(values, {3, 4})

    def test_comment_only_count_does_not_cause_false_failure(self) -> None:
        # A stale changelog comment claiming an old count must not be seen at
        # all -- comments are stripped before Rule A ever runs.
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "pass_a_comment.tex",
                r"""
% Old changelog note: this used to catalog thirteen distinct
% mechanism-class constraints before the B14 split.
We catalog three distinct
mechanism-class constraints, one per catalog entry.

\medskip\noindent\textbf{B1 --- First (Found.\ A) [R1].} text here.
\medskip\noindent\textbf{B2 --- Second (Found.\ B) [R1].} text here.
\medskip\noindent\textbf{B3 --- Third (Found.\ C) [R2].} text here.
""",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_a(doc)
            self.assertTrue(result.passed, result.evidence)


class RuleBTierICountTests(unittest.TestCase):
    TABLE_HEADER = r"""
\begin{table*}[tb]
\caption{\label{tab:evidentiary_status} Evidentiary status test table.}
\begin{ruledtabular}
\begin{tabular}{lll}
"""
    TABLE_FOOTER = r"""
\end{tabular}
\end{ruledtabular}
\end{table*}
"""

    def test_passing_fixture_table_and_prose_agree(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            body = (
                self.TABLE_HEADER
                + r"Leg1 & rules out X & \textbf{(I) Rigorous within stated scope} \\"
                + r"Leg2 & rules out Y & \textbf{(II) Structural argument} \\"
                + self.TABLE_FOOTER
                + "\n\nOnly the perturbation-transparency result is a Tier-I "
                "rigorous theorem; this is the catalog's sole Tier-I leg.\n"
            )
            path = _write(Path(tmp), "pass_b.tex", body)
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_b(doc)
            self.assertTrue(result.passed, result.evidence)
            self.assertEqual(result.detail["table_count"], 1)

    def test_failing_fixture_two_markers_one_prose_claim(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            body = (
                self.TABLE_HEADER
                + r"Leg1 & rules out X & \textbf{(I) Rigorous within stated scope} \\"
                + r"Leg2 & rules out Y & \textbf{(I)} for a second leg \\"
                + self.TABLE_FOOTER
                + "\n\nThis is the catalog's sole Tier-I closure leg.\n"
            )
            path = _write(Path(tmp), "fail_b.tex", body)
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_b(doc)
            self.assertFalse(result.passed)
            self.assertEqual(result.detail["table_count"], 2)
            self.assertEqual(len(result.detail["mismatches"]), 1)

    def test_tier_ii_markers_do_not_count_as_tier_i(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            body = (
                self.TABLE_HEADER
                + r"Leg1 & rules out X & \textbf{(II)+(III)} structural \\"
                + self.TABLE_FOOTER
            )
            path = _write(Path(tmp), "tier_ii.tex", body)
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_b(doc)
            self.assertEqual(result.detail["table_count"], 0)


class RuleCAssertDisclaimTests(unittest.TestCase):
    def test_passing_fixture_disclaim_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "pass_c.tex",
                "We therefore do not claim the NDA bound covers it, and the "
                "route splits into two cases.\n",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_c(doc)
            self.assertTrue(result.passed, result.evidence)

    def test_failing_fixture_assert_and_disclaim_both_present(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "fail_c.tex",
                "The Riccati flow has no fixed point, and the operator is "
                "bounded by the single-scale\nNDA no-go regardless of "
                "normalization.\n\n"
                "Elsewhere: we therefore do not claim the NDA bound covers "
                "it.\n",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_c(doc)
            self.assertFalse(result.passed)
            self.assertTrue(result.detail["pairs"]["nda_covers_eq1"]["failed"])

    def test_line_wrapped_assert_phrase_still_detected(self) -> None:
        # The real-world defect: the assert phrase wraps across a line break
        # exactly between "single-scale" and "NDA".
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "wrap_c.tex",
                "and the operator is bounded by the single-scale\n"
                "NDA no-go regardless of that normalization.\n"
                "We therefore do not claim the NDA bound covers it.\n",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_c(doc)
            self.assertFalse(result.passed)


class RuleDUniversalClosureTests(unittest.TestCase):
    def test_passing_fixture_no_universal_claim(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "pass_d.tex",
                r"""
We catalog constraints, each bearing on one or more of the four routes.

\medskip\noindent\textbf{B1 --- First (Found.\ A) [R1].} closes route one.
\medskip\noindent\textbf{B9 --- Ninth (Branch J) [R2].} is not an
independent bound on the one-loop amplitude, so B9 is never used as a
stand-alone closure.
""",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_d(doc)
            self.assertTrue(result.passed, result.evidence)

    def test_failing_fixture_universal_claim_vs_self_declared_non_closure(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "fail_d.tex",
                r"""
We catalog N constraints, each closing one or more of the four routes.

\medskip\noindent\textbf{B1 --- First (Found.\ A) [R1].} closes route one.
\medskip\noindent\textbf{B9 --- Ninth (Branch J) [R2].} is not an
independent bound on the one-loop amplitude, so B9 is never used as a
stand-alone closure.
\medskip\noindent\textbf{B14 --- Fourteenth (Branch H).} B14 is not, and is
not used as, a closure of the fermionic or one-loop content of any route.
""",
            )
            doc = build_document(path.read_text(encoding="utf-8"))
            result = check_rule_d(doc)
            self.assertFalse(result.passed)
            self.assertEqual(result.detail["offending_entries"], [9, 14])


class RealManuscriptSmokeTest(unittest.TestCase):
    def test_real_manuscript_is_checkable_without_raising(self) -> None:
        # P1C's main.tex may be under concurrent edit; this only asserts the
        # linter can parse and run all four rules without raising -- it does
        # NOT assert the manuscript currently passes.
        tex_path = ROOT / "arxiv" / "paper1c_nogo_survey" / "main.tex"
        self.assertTrue(tex_path.is_file(), tex_path)
        doc = build_document(tex_path.read_text(encoding="utf-8"))
        results = run_all_rules(doc)
        self.assertEqual(len(results), 4)
        for result in results:
            self.assertIn(result.rule, {"A", "B", "C", "D"})
            self.assertIsInstance(result.passed, bool)

    def test_default_tex_path_points_at_p1c_main(self) -> None:
        self.assertEqual(
            DEFAULT_TEX,
            ROOT / "arxiv" / "paper1c_nogo_survey" / "main.tex",
        )


class CliExitCodeTests(unittest.TestCase):
    def test_main_returns_zero_on_clean_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "clean.tex",
                r"""
We catalog three distinct
mechanism-class constraints, one per catalog entry, each bearing on one or
more of the four routes.

\begin{table*}[tb]
\caption{\label{tab:evidentiary_status} Evidentiary status.}
\begin{ruledtabular}
\begin{tabular}{lll}
Leg1 & rules out X & \textbf{(I) Rigorous within stated scope} \\
Leg2 & rules out Y & \textbf{(II) Structural argument} \\
\end{tabular}
\end{ruledtabular}
\end{table*}

Only the perturbation-transparency result is a Tier-I rigorous theorem;
this is the catalog's sole Tier-I leg.

\medskip\noindent\textbf{B1 --- First (Found.\ A) [R1].} closes route one.
\medskip\noindent\textbf{B2 --- Second (Found.\ B) [R1].} closes route two.
\medskip\noindent\textbf{B3 --- Third (Found.\ C) [R2].} closes route three.
""",
            )
            self.assertEqual(main(["--tex", str(path)]), 0)

    def test_main_returns_one_on_broken_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = _write(
                Path(tmp),
                "broken.tex",
                r"""
We catalog N constraints, each closing one or more of the four routes.

\medskip\noindent\textbf{B9 --- Ninth (Branch J) [R2].} is not an
independent bound on the one-loop amplitude, so B9 is never used as a
stand-alone closure.
""",
            )
            self.assertEqual(main(["--tex", str(path)]), 1)

    def test_main_missing_file_returns_one(self) -> None:
        self.assertEqual(main(["--tex", "/nonexistent/path/does-not-exist.tex"]), 1)


if __name__ == "__main__":
    unittest.main()
