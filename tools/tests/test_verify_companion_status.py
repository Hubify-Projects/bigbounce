from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from paper_registry import CANONICAL_IDS  # noqa: E402
from verify_companion_status import (  # noqa: E402
    CompanionStatusError,
    live_lines,
    verify,
)


# P3's registry paths are pinned by paper_registry.load_registry, so the fixture
# has to use the real ones.
TEX_PATHS = {
    "P1A": "arxiv/paper1a.tex",
    "P1B": "arxiv/paper1b.tex",
    "P2": "research/p2/p2.tex",
    "P3": "pipelines/p3_anomaly_engine/paper3_apjs.tex",
    "P4": "pipelines/p4/p4.tex",
    "P5": "pipelines/p5/p5.tex",
}

PUBLISHED = {
    "P1A": "10.5281/zenodo.21481838",
    "P1B": "10.5281/zenodo.21481842",
    "P2": "10.5281/zenodo.21461881",
    "P3": "10.5281/zenodo.21461888",
    "P4": "10.5281/zenodo.21461899",
}

CITE_KEYS = {
    "P1A": "golden_ech_2026",
    "P1B": "golden_namaster_2026",
    "P2": "golden_fnl_2026",
    "P3": "golden_anomaly_2026",
    "P4": "golden_chirality_2026",
    "P5": "golden_desi_chirality_2026",
}

LABELS = {
    "P1A": "Paper I A", "P1B": "Paper I B", "P2": "Paper II",
    "P3": "Paper III", "P4": "Paper IV", "P5": "Paper V",
}

SKELETON = "\\begin{document}\n%s\n\\end{document}\n"


def ledger_payload() -> dict:
    papers = {}
    for paper_id in CANONICAL_IDS:
        entry = {
            "labels": [LABELS[paper_id]],
            "cite_keys": [CITE_KEYS[paper_id]],
            "published_doi": PUBLISHED.get(paper_id),
            "concept_doi": None,
            "arxiv_id": None,
            "peer_reviewed": False,
        }
        if paper_id == "P5":
            entry["no_doi_reason"] = "deposit staged, never published"
        papers[paper_id] = entry
    return {
        "schema": "bigbounce.companion-status-ledger/v1",
        "verified_on": "2026-07-24",
        "papers": papers,
        "unpublished_status_phrases": [
            "in preparation", "forthcoming", "not yet public", "XXXX\\.XXXXX",
        ],
        "superseded_values": [
            {
                "id": "P2-fnl-35-8",
                "owner": "P2",
                "quantity": "local f_NL amplitude",
                "superseded_patterns": ["-35/8"],
                "current_value": "-35/16",
                "legitimate_attribution_patterns": ["Cai", "literature value", "not reproduce"],
            }
        ],
    }


class CompanionStatusTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="companion_status_test_")
        self.root = Path(self.tmp.name)
        registry = {"papers": {}}
        for paper_id in CANONICAL_IDS:
            tex = self.root / TEX_PATHS[paper_id]
            tex.parent.mkdir(parents=True, exist_ok=True)
            tex.write_text(SKELETON % "Nothing to see here.", encoding="utf-8")
            tex.with_suffix(".pdf").write_bytes(b"%PDF-1.4\n")
            registry["papers"][paper_id] = {
                "tex_path": TEX_PATHS[paper_id],
                "pdf_path": TEX_PATHS[paper_id].replace(".tex", ".pdf"),
                "site_slug": f"paper-{paper_id.lower()}",
                "target_journal": "Physical Review D",
                "article_type": "Research Article",
                "review_profile": "PRD-RESEARCH",
                "served_aliases": [f"{paper_id.lower()}.pdf"],
                "review_paths": [str(Path(TEX_PATHS[paper_id]).parent)],
            }
        (self.root / "project-context").mkdir(parents=True, exist_ok=True)
        (self.root / "project-context" / "paper_registry.json").write_text(
            json.dumps(registry), encoding="utf-8"
        )
        self.write_ledger(ledger_payload())

    def tearDown(self):
        self.tmp.cleanup()

    def write_ledger(self, payload):
        (self.root / "project-context" / "companion-status-ledger.json").write_text(
            json.dumps(payload), encoding="utf-8"
        )

    def set_body(self, paper_id, body):
        (self.root / TEX_PATHS[paper_id]).write_text(SKELETON % body, encoding="utf-8")

    def run_check(self):
        return verify(self.root, "project-context/companion-status-ledger.json")

    def findings(self, rule=None):
        result = self.run_check()
        return [f for f in result["findings"] if rule is None or f["rule"] == rule]

    # -- clean baseline --------------------------------------------------
    def test_clean_portfolio_passes(self):
        self.assertEqual(self.run_check()["verdict"], "PASS")

    # -- rule 1: companion status ---------------------------------------
    def test_stale_bibitem_for_published_companion_fails(self):
        self.set_body("P5", (
            "We use the companion catalog~\\cite{golden_chirality_2026}.\n"
            "\\begin{thebibliography}{9}\n"
            "\\bibitem{golden_chirality_2026}\n"
            "H.~Golden, \\emph{Chirality catalog}, Paper IV, in preparation.\n"
            "\\end{thebibliography}\n"
        ))
        findings = self.findings("companion-status")
        self.assertEqual(len(findings), 1, findings)
        self.assertEqual(findings[0]["target_paper_id"], "P4")
        self.assertEqual(findings[0]["evidence"], "in preparation")
        self.assertEqual(self.run_check()["verdict"], "FAIL")

    def test_arxiv_id_placeholder_in_bib_entry_fails(self):
        self.set_body("P2", (
            "See~\\cite{golden_ech_2026}.\n"
            "\\begin{thebibliography}{9}\n"
            "\\bibitem{golden_ech_2026} H.~Golden, note: posted on arXiv "
            "[arXiv:XXXX.XXXXX --- ID inserted at submission].\n"
            "\\end{thebibliography}\n"
        ))
        findings = self.findings("companion-status")
        self.assertEqual([f["target_paper_id"] for f in findings], ["P1A"])

    def test_bib_entry_missing_published_doi_fails(self):
        self.set_body("P5", (
            "See~\\cite{golden_chirality_2026}.\n"
            "\\begin{thebibliography}{9}\n"
            "\\bibitem{golden_chirality_2026} H.~Golden, \\emph{Chirality catalog}, Zenodo (2026).\n"
            "\\end{thebibliography}\n"
        ))
        findings = self.findings("companion-status")
        self.assertEqual(len(findings), 1, findings)
        self.assertIn("does not print its published DOI", findings[0]["detail"])

    def test_bib_entry_citing_the_doi_passes(self):
        self.set_body("P5", (
            "See~\\cite{golden_chirality_2026}.\n"
            "\\begin{thebibliography}{9}\n"
            "\\bibitem{golden_chirality_2026} H.~Golden, \\emph{Chirality catalog}, "
            "Paper IV, Zenodo (2026), version DOI 10.5281/zenodo.21461899; "
            "public permanent archive, not an arXiv preprint and not peer reviewed.\n"
            "\\end{thebibliography}\n"
        ))
        self.assertEqual(self.run_check()["verdict"], "PASS")

    def test_stale_claim_in_external_bib_file_fails(self):
        (self.root / "research/p2/refs.bib").write_text(
            "@article{golden_ech_2026,\n"
            '  author = "Golden, Houston",\n'
            '  title = "{ECH}",\n'
            '  journal = "(in preparation)",\n'
            "  year = 2026\n}\n",
            encoding="utf-8",
        )
        self.set_body("P2", "As audited in~\\cite{golden_ech_2026}.\n\\bibliography{refs}\n")
        findings = self.findings("companion-status")
        self.assertEqual(len(findings), 1, findings)
        self.assertEqual(findings[0]["target_paper_id"], "P1A")
        self.assertTrue(findings[0]["location"].endswith("bib-entry:golden_ech_2026"))

    def test_uncited_stale_bib_file_entry_does_not_fire(self):
        # An entry nothing cites never reaches a referee; the .tex-visible rules
        # own what actually renders.
        (self.root / "research/p2/refs.bib").write_text(
            "@article{golden_ech_2026,\n journal = \"(in preparation)\",\n year = 2026\n}\n",
            encoding="utf-8",
        )
        self.set_body("P2", "No citations here.\n\\bibliography{refs}\n")
        self.assertEqual(self.run_check()["verdict"], "PASS")

    def test_stale_body_prose_about_published_companion_fails(self):
        self.set_body("P5", "The Paper IV catalog is a companion manuscript in preparation.\n")
        findings = self.findings("companion-status")
        self.assertEqual(len(findings), 1, findings)
        self.assertEqual(findings[0]["location"], f"{TEX_PATHS['P5']}:body")

    # -- rule 1: must-NOT-fire cases ------------------------------------
    def test_unpublished_claim_about_p5_passes(self):
        # P5 genuinely has no DOI. Saying so is TRUE and must never be "fixed".
        self.set_body("P4", (
            "The Paper V analysis~\\cite{golden_desi_chirality_2026} is in preparation "
            "and has no public archive or persistent identifier.\n"
        ))
        self.assertEqual(self.run_check()["verdict"], "PASS")

    def test_peer_review_and_arxiv_caveats_pass(self):
        self.set_body("P5", (
            "Paper IV~\\cite{golden_chirality_2026} is publicly archived but has not yet "
            "been refereed; it is not peer reviewed and carries no arXiv identifier.\n"
            "\\begin{thebibliography}{9}\n"
            "\\bibitem{golden_chirality_2026} Zenodo (2026), DOI 10.5281/zenodo.21461899; "
            "not an arXiv preprint and not peer reviewed.\n"
            "\\end{thebibliography}\n"
        ))
        self.assertEqual(self.run_check()["verdict"], "PASS")

    def test_stale_claim_inside_comments_is_ignored(self):
        self.set_body("P5", (
            "% Paper IV was a companion manuscript in preparation before 2026-07-20.\n"
            "\\begin{comment}\n"
            "Paper IV~\\cite{golden_chirality_2026} is forthcoming.\n"
            "\\end{comment}\n"
            "\\iffalse\n"
            "Paper IV is in preparation.\n"
            "\\fi\n"
            "Paper IV is publicly archived.\n"
        ))
        self.assertEqual(self.run_check()["verdict"], "PASS")

    # -- rule 2: superseded value ---------------------------------------
    def test_superseded_value_cited_as_companion_result_fails(self):
        self.set_body("P5", (
            "The companion forecast~\\cite{golden_fnl_2026} predicts $f_{NL} = -35/8$.\n"
        ))
        findings = self.findings("superseded-value")
        self.assertEqual(len(findings), 1, findings)
        self.assertEqual(findings[0]["target_paper_id"], "P2")
        self.assertIn("-35/16", findings[0]["detail"])

    def test_superseded_value_in_bibitem_title_fails(self):
        self.set_body("P5", (
            "See~\\cite{golden_fnl_2026}.\n"
            "\\begin{thebibliography}{9}\n"
            "\\bibitem{golden_fnl_2026} H.~Golden, \\emph{$f_{NL} = -35/8$ Forecast}, "
            "Zenodo (2026), DOI 10.5281/zenodo.21461881.\n"
            "\\end{thebibliography}\n"
        ))
        findings = self.findings("superseded-value")
        self.assertEqual(len(findings), 1, findings)
        self.assertIn("bibliography entry cites P2", findings[0]["detail"])

    def test_legitimate_historical_discussion_of_superseded_value_passes(self):
        # The must-not-fire case: comparative discussion attributing -35/8 to the
        # third-party source that printed it is CORRECT and must be preserved.
        self.set_body("P5", (
            "Paper II~\\cite{golden_fnl_2026} corrects the unreproduced printed "
            "$-35/8$ literature value of Cai et al.\n"
        ))
        self.assertEqual(self.run_check()["verdict"], "PASS")

    def test_owner_paper_may_discuss_its_own_superseded_value(self):
        # P2 is REQUIRED to discuss -35/8 in order to disown it.
        self.set_body("P2", "We do not reproduce the separately printed $-35/8$; Paper II gives $-35/16$.\n")
        self.assertEqual(self.run_check()["verdict"], "PASS")

    def test_superseded_value_without_companion_reference_does_not_fire(self):
        self.set_body("P4", "An unrelated ratio of $-35/8$ appears in a different context.\n")
        self.assertEqual(self.run_check()["verdict"], "PASS")

    # -- ledger integrity ------------------------------------------------
    def test_minting_p5_doi_arms_the_check_with_no_code_change(self):
        self.set_body("P4", "The Paper V analysis is in preparation.\n")
        self.assertEqual(self.run_check()["verdict"], "PASS")
        payload = ledger_payload()
        payload["papers"]["P5"]["published_doi"] = "10.5281/zenodo.99999999"
        self.write_ledger(payload)
        findings = self.findings("companion-status")
        self.assertEqual([f["target_paper_id"] for f in findings], ["P5"])

    def test_ledger_rejects_a_peer_review_status_phrase(self):
        payload = ledger_payload()
        payload["unpublished_status_phrases"].append("not peer reviewed")
        self.write_ledger(payload)
        with self.assertRaises(CompanionStatusError):
            self.run_check()

    def test_ledger_requires_a_reason_for_a_missing_doi(self):
        payload = ledger_payload()
        del payload["papers"]["P5"]["no_doi_reason"]
        self.write_ledger(payload)
        with self.assertRaises(CompanionStatusError):
            self.run_check()

    def test_live_lines_strips_comments_and_blocks(self):
        text = (
            "live one\n"
            "% dead\n"
            "tail \\% escaped percent stays % but this goes\n"
            "\\begin{comment}\ndead\n\\end{comment}\n"
            "live two\n"
        )
        rendered = [line.strip() for _, line in live_lines(text)]
        self.assertEqual(rendered[0], "live one")
        self.assertEqual(rendered[1], "tail \\% escaped percent stays")
        self.assertEqual(rendered[2], "live two")


class RealPortfolioTests(unittest.TestCase):
    """The committed portfolio must satisfy the gate it now ships with."""

    def test_repository_passes(self):
        result = verify(ROOT)
        self.assertEqual(result["verdict"], "PASS", result["findings"])
        self.assertEqual(result["unpublished_companions"], ["P5"])


if __name__ == "__main__":
    unittest.main()
