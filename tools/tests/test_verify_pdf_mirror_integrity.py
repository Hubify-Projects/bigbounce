#!/usr/bin/env python3
"""Both directions of the served-PDF gate, plus a replay of the real defects.

The regression replay at the bottom is the part that makes the gate credible:
it reconstructs the exact 2026-07-24 findings (the stale P2 mirror at
``public/focused_paper_bounce_fnl_forecast.pdf`` and the P3 r13/r14 ``papers.ts``
reference) from a fixture and proves the checker names them.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from verify_pdf_mirror_integrity import (  # noqa: E402
    MirrorIntegrityError,
    verify,
)


MINIMAL_PDF = b"%PDF-1.4\n1 0 obj<</Type/Catalog>>endobj\ntrailer<</Root 1 0 R>>\n%%EOF\n"

PAPERS_TS_TEMPLATE = """export const papers = [
  {{
    slug: "paper-2",
    version: "{p2_version}",
    pdfMeta: "PDF · 11 pp · {p2_version} · md5 {p2_md5}",
    artifacts: [
      {{ label: "Read PDF", href: "/papers/{p2_href}", kind: "primary" }},
    ],
  }},
  {{
    slug: "paper-3",
    version: "{p3_version}",
    pdfMeta: "PDF · 17 pp · {p3_version} · md5 {p3_md5}",
    artifacts: [
      {{ label: "Read PDF", href: "/papers/{p3_href}", kind: "primary" }},
    ],
  }},
];
"""

CANONICAL_IDS = ("P1A", "P1B", "P2", "P3", "P4", "P5")
PAPER_STEMS = {
    "P1A": "paper1a_ech_nogo",
    "P1B": "paper1b_namaster_proof",
    "P2": "02_full_draft",
    "P3": "paper3_apjs",
    "P4": "chirality_catalog_paper",
    "P5": "p5_desi_chirality",
}
PAPER_VERSIONS = {
    "P1A": "v1A.0.127", "P1B": "v2B.0.16", "P2": "v1.7.130",
    "P3": "v3.2.0-r14", "P4": "v1.0.272", "P5": "v0.1.146-2026-07-24",
}
PAPER_SLUGS = {
    "P1A": "paper-1a", "P1B": "paper-1b", "P2": "paper-2",
    "P3": "paper-3", "P4": "paper-4", "P5": "paper-5",
}


def md5(payload: bytes) -> str:
    return hashlib.md5(payload).hexdigest()  # noqa: S324 - matches the tool under test


def body(paper_id: str, version: str) -> bytes:
    """Deterministic, distinct PDF bytes per (paper, version)."""
    return MINIMAL_PDF + f"% {paper_id} {version}\n".encode()


class Fixture:
    """A throwaway git repo shaped like bigbounce's served surface."""

    def __init__(self, root: Path) -> None:
        self.root = root
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "t@t"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "t"], cwd=root, check=True)
        self.registry: dict[str, object] = {"schema_version": 2, "papers": {}}
        for paper_id in CANONICAL_IDS:
            stem = PAPER_STEMS[paper_id]
            version = PAPER_VERSIONS[paper_id]
            self.write(f"src/{stem}.tex", f"\\newcommand{{\\paperVersion}}{{{version}}}\n".encode())
            self.write(f"src/{stem}.pdf", body(paper_id, version))
            self.registry["papers"][paper_id] = {
                "tex_path": f"src/{stem}.tex",
                "pdf_path": f"src/{stem}.pdf",
                "site_slug": PAPER_SLUGS[paper_id],
                "target_journal": "j", "article_type": "a", "review_profile": "r",
                "served_aliases": [], "review_paths": ["src"],
            }
            # Current mirror + this version's immutable archive, both roots.
            for served_root in ("public/papers", "site/public/papers"):
                self.write(f"{served_root}/{stem}.pdf", body(paper_id, version))
                self.write(f"{served_root}/{stem}_{version}.pdf", body(paper_id, version))
        self.policy = {
            "schema": "bigbounce.served-pdf-policy/v1",
            "served_roots": ["public", "site/public"],
            "site_href_prefix": "/papers/",
            "site_href_root": "site/public",
            "non_manuscript_path_patterns": ["(?:^|/)figures/"],
            "immutable_archive_name_patterns": [
                r"_v[0-9]+[A-Za-z]?\.[0-9]+\.[0-9]+(?:[.\-][0-9A-Za-z][0-9A-Za-z\-]*)*\.pdf$",
                r"_v[0-9]{2,}\.pdf$",
            ],
            "site_data_sources": [
                {"path": "site/src/data/papers.ts", "kind": "current-paper-artifacts"},
            ],
            "retired_served_pdfs": [],
        }
        self.set_papers_ts()

    # -- fixture helpers ---------------------------------------------------
    def write(self, relative: str, payload: bytes) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)

    def set_papers_ts(self, *, p2_version: str | None = None, p3_version: str | None = None) -> None:
        p2 = p2_version or PAPER_VERSIONS["P2"]
        p3 = p3_version or PAPER_VERSIONS["P3"]
        self.write("site/src/data/papers.ts", PAPERS_TS_TEMPLATE.format(
            p2_version=p2, p2_md5=md5(body("P2", p2)), p2_href=f"02_full_draft_{p2}.pdf",
            p3_version=p3, p3_md5=md5(body("P3", p3)), p3_href=f"paper3_apjs_{p3}.pdf",
        ).encode())

    def commit(self) -> None:
        registry = dict(self.registry)
        registry["served_pdf_policy"] = self.policy
        self.write(
            "project-context/paper_registry.json",
            (json.dumps(registry, indent=2) + "\n").encode(),
        )
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.root, check=True)

    def run(self) -> dict:
        self.commit()
        return verify(self.root)


class PdfMirrorIntegrityTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.fixture = Fixture(Path(self._tmp.name).resolve())

    @staticmethod
    def rules(result: dict) -> list[str]:
        return [finding["rule"] for finding in result["findings"]]

    @staticmethod
    def findings(result: dict, rule: str) -> list[dict]:
        return [finding for finding in result["findings"] if finding["rule"] == rule]

    # -- baseline ----------------------------------------------------------
    def test_clean_served_tree_passes(self) -> None:
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "PASS", result["findings"])
        self.assertEqual(result["served_inventory"]["counts"]["orphan"], 0)
        self.assertEqual(result["served_inventory"]["counts"]["current_mirror"], 12)
        self.assertEqual(result["served_inventory"]["counts"]["immutable_archive"], 12)

    # -- reverse direction -------------------------------------------------
    def test_orphan_stale_pdf_under_a_served_root_fails(self) -> None:
        """The 2026-07-24 class: a served PDF in no paper's mirror set."""
        self.fixture.write("public/focused_paper_bounce_fnl_forecast.pdf", body("P2", "v1.7.110"))
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "FAIL")
        orphans = self.findings(result, "unregistered-orphan-pdf")
        self.assertEqual([item["path"] for item in orphans],
                         ["public/focused_paper_bounce_fnl_forecast.pdf"])

    def test_orphan_outside_the_directive_g_mirror_roots_is_still_caught(self) -> None:
        """``public/`` bare is NOT a directive-G mirror root -- that is the hole."""
        self.fixture.write("public/paper3_draft.pdf", body("P3", "v3.1.158"))
        self.fixture.write("site/public/p1a-ech-nogo.pdf", body("P1A", "v1A.0.112"))
        result = self.fixture.run()
        self.assertEqual(
            sorted(item["path"] for item in self.findings(result, "unregistered-orphan-pdf")),
            ["public/paper3_draft.pdf", "site/public/p1a-ech-nogo.pdf"],
        )

    def test_legitimate_immutable_version_pinned_archive_passes(self) -> None:
        """PUB-005 retention must never be reported as a defect."""
        for stale in ("v1.7.110", "v1.7.126", "v1.7.129"):
            self.fixture.write(f"public/papers/02_full_draft_{stale}.pdf", body("P2", stale))
            self.fixture.write(f"site/public/papers/02_full_draft_{stale}.pdf", body("P2", stale))
        self.fixture.write("public/papers/chirality_catalog_paper_v149.pdf", body("P4", "v1.0.149"))
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "PASS", result["findings"])
        self.assertEqual(result["served_inventory"]["counts"]["immutable_archive"], 19)

    def test_archive_pinned_to_the_current_version_must_carry_its_bytes(self) -> None:
        self.fixture.write(
            "site/public/papers/paper3_apjs_v3.2.0-r14.pdf", body("P3", "v3.2.0-r13"),
        )
        result = self.fixture.run()
        collisions = self.findings(result, "archive-version-collision")
        self.assertEqual([item["paper_id"] for item in collisions], ["P3"])

    def test_registered_mirror_with_drifted_bytes_fails(self) -> None:
        self.fixture.write("site/public/papers/02_full_draft.pdf", body("P2", "v1.7.128"))
        result = self.fixture.run()
        stale = self.findings(result, "mirror-bytes-stale")
        self.assertEqual([item["path"] for item in stale], ["site/public/papers/02_full_draft.pdf"])
        self.assertEqual(stale[0]["paper_id"], "P2")

    def test_registered_alias_is_a_current_mirror_not_an_orphan(self) -> None:
        self.fixture.registry["papers"]["P2"]["served_aliases"] = ["fnl-forecast-paper.pdf"]
        self.fixture.write("site/public/papers/fnl-forecast-paper.pdf", body("P2", PAPER_VERSIONS["P2"]))
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "PASS", result["findings"])

    def test_companion_manuscript_mirror_is_not_an_orphan(self) -> None:
        self.fixture.write("src/companion.tex", b"\\newcommand{\\paperVersion}{v1B.0.112}\n")
        self.fixture.write("src/companion.pdf", body("P1B-MCMC", "v1B.0.112"))
        self.fixture.write("site/public/papers/companion.pdf", body("P1B-MCMC", "v1B.0.112"))
        self.fixture.registry["companion_manuscripts"] = {
            "P1B-MCMC": {
                "tex_path": "src/companion.tex", "pdf_path": "src/companion.pdf",
                "served_aliases": [],
            }
        }
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "PASS", result["findings"])

    def test_figure_pdfs_are_not_manuscripts(self) -> None:
        self.fixture.write("site/public/paper/figures/fig_dneff.pdf", b"%PDF-1.4 fig\n")
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "PASS", result["findings"])
        self.assertEqual(result["served_inventory"]["counts"]["non_manuscript_asset"], 1)

    # -- retired-file dispositions ----------------------------------------
    def test_retired_entry_marked_remove_keeps_failing_while_the_file_is_served(self) -> None:
        self.fixture.write("public/paper3_draft.pdf", body("P3", "v3.1.158"))
        self.fixture.policy["retired_served_pdfs"] = [{
            "path": "public/paper3_draft.pdf", "identified_paper": "P3",
            "identified_version": "v3.1.158", "disposition": "remove",
            "note": "superseded; retained under a version-pinned name",
        }]
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(self.rules(result), ["retired-served-pdf-still-present"])
        self.assertNotIn("unregistered-orphan-pdf", self.rules(result))

    def test_retired_entry_marked_retain_passes(self) -> None:
        self.fixture.write("public/downloads/legacy_talk.pdf", b"%PDF-1.4 legacy\n")
        self.fixture.policy["retired_served_pdfs"] = [{
            "path": "public/downloads/legacy_talk.pdf", "identified_paper": "P1-LEGACY",
            "identified_version": "2026-03-09", "disposition": "retain",
            "note": "deliberately published legacy artifact",
        }]
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "PASS", result["findings"])
        self.assertEqual(result["served_inventory"]["counts"]["retained_by_policy"], 1)

    def test_retired_entry_for_a_vanished_file_is_reported_so_the_ledger_stays_true(self) -> None:
        self.fixture.policy["retired_served_pdfs"] = [{
            "path": "public/papers/already_deleted.pdf", "identified_paper": "P3",
            "identified_version": "v3.1.138", "disposition": "remove", "note": "gone",
        }]
        result = self.fixture.run()
        self.assertEqual(self.rules(result), ["stale-retired-entry"])

    def test_untracked_served_pdf_is_out_of_scope(self) -> None:
        """The gate reasons about committed state, not build output or scratch."""
        self.fixture.commit()
        self.fixture.write("public/papers/scratch_build.pdf", body("P2", "v1.7.9"))
        self.assertEqual(verify(self.fixture.root)["verdict"], "PASS")

    # -- forward direction -------------------------------------------------
    def test_stale_papers_ts_reference_fails(self) -> None:
        """A link to a real-but-superseded PDF is as bad as a dead one."""
        self.fixture.write(
            "site/public/papers/paper3_apjs_v3.2.0-r13.pdf", body("P3", "v3.2.0-r13"),
        )
        self.fixture.set_papers_ts(p3_version="v3.2.0-r13")
        result = self.fixture.run()
        self.assertEqual(result["verdict"], "FAIL")
        stale = self.findings(result, "site-reference-stale")
        self.assertEqual([item["paper_id"] for item in stale], ["P3"])
        self.assertEqual(stale[0]["reference"], "/papers/paper3_apjs_v3.2.0-r13.pdf")
        self.assertEqual(
            sorted({item["rule"] for item in result["findings"]}),
            ["site-pdfmeta-md5-stale", "site-reference-stale", "site-version-field-stale"],
        )

    def test_papers_ts_reference_to_a_missing_file_fails(self) -> None:
        self.fixture.set_papers_ts(p2_version="v1.7.999")
        result = self.fixture.run()
        missing = self.findings(result, "site-reference-missing")
        self.assertEqual([item["reference"] for item in missing],
                         ["/papers/02_full_draft_v1.7.999.pdf"])

    def test_stale_version_field_fails_even_when_the_href_is_current(self) -> None:
        text = (self.fixture.root / "site/src/data/papers.ts").read_text()
        self.fixture.write(
            "site/src/data/papers.ts",
            text.replace('version: "v3.2.0-r14"', 'version: "v3.2.0-r11"', 1).encode(),
        )
        result = self.fixture.run()
        self.assertEqual(self.rules(result), ["site-version-field-stale"])

    def test_historical_link_surface_requires_existence_but_not_currency(self) -> None:
        self.fixture.write("site/public/papers/02_full_draft_v1.7.110.pdf", body("P2", "v1.7.110"))
        self.fixture.write("site/src/data/reviewTimeline.ts", (
            'export const t = [{ href: "/papers/02_full_draft_v1.7.110.pdf" },\n'
            '                   { href: "/papers/02_full_draft_v1.7.999.pdf" }];\n'
        ).encode())
        self.fixture.policy["site_data_sources"].append(
            {"path": "site/src/data/reviewTimeline.ts", "kind": "historical-archive-links"}
        )
        result = self.fixture.run()
        self.assertEqual(self.rules(result), ["site-reference-missing"])
        self.assertEqual(result["findings"][0]["reference"], "/papers/02_full_draft_v1.7.999.pdf")

    # -- policy validation -------------------------------------------------
    def test_missing_policy_block_is_an_error_not_a_pass(self) -> None:
        self.fixture.policy = {}
        self.fixture.commit()
        with self.assertRaises(MirrorIntegrityError):
            verify(self.fixture.root)

    def test_unsafe_retired_path_is_rejected(self) -> None:
        self.fixture.policy["retired_served_pdfs"] = [{
            "path": "../../etc/passwd.pdf", "identified_paper": "P3",
            "identified_version": "x", "disposition": "remove", "note": "n",
        }]
        self.fixture.commit()
        with self.assertRaises(MirrorIntegrityError):
            verify(self.fixture.root)

    def test_retired_path_must_live_under_a_served_root(self) -> None:
        self.fixture.policy["retired_served_pdfs"] = [{
            "path": "src/02_full_draft.pdf", "identified_paper": "P2",
            "identified_version": "x", "disposition": "remove", "note": "n",
        }]
        self.fixture.commit()
        with self.assertRaises(MirrorIntegrityError):
            verify(self.fixture.root)

    def test_unknown_disposition_is_rejected(self) -> None:
        self.fixture.policy["retired_served_pdfs"] = [{
            "path": "public/papers/x.pdf", "identified_paper": "P2",
            "identified_version": "x", "disposition": "ignore", "note": "n",
        }]
        self.fixture.commit()
        with self.assertRaises(MirrorIntegrityError):
            verify(self.fixture.root)

    def test_retiring_a_path_that_is_a_live_mirror_is_reported(self) -> None:
        self.fixture.policy["retired_served_pdfs"] = [{
            "path": "site/public/papers/02_full_draft.pdf", "identified_paper": "P2",
            "identified_version": PAPER_VERSIONS["P2"], "disposition": "remove",
            "note": "contradiction",
        }]
        result = self.fixture.run()
        self.assertEqual(self.rules(result), ["retired-entry-contradicts-current-mirror"])

    # -- regression replay of the real 2026-07-24 findings -----------------
    def test_replays_the_real_2026_07_24_defects(self) -> None:
        """Reconstruct the pre-fix state and confirm both real findings appear.

        Historical instance 1: ``public/focused_paper_bounce_fnl_forecast.pdf``
        was a July-10 P2 build sitting outside every registered mirror set.
        Historical instance 2: ``papers.ts`` kept pointing P3's Read/Download at
        ``paper3_apjs_v3.2.0-r13.pdf`` after r14 landed.
        """
        self.fixture.registry["papers"]["P2"]["served_aliases"] = [
            "fnl-forecast-paper.pdf", "focused_paper_bounce_fnl_forecast.pdf",
            "paper2_fnl_forecast.pdf",
        ]
        for alias in self.fixture.registry["papers"]["P2"]["served_aliases"]:
            for served_root in ("public/papers", "site/public/papers"):
                self.fixture.write(f"{served_root}/{alias}", body("P2", PAPER_VERSIONS["P2"]))
        # ...but the alias mirrored into bare ``public/`` was never in a
        # directive-G served root, so it kept its July-10 bytes.
        self.fixture.write("public/focused_paper_bounce_fnl_forecast.pdf", body("P2", "v1.7.110"))
        # A sibling leftover under a name no paper claims at all.
        self.fixture.write("public/paper3_barriers_ech_transparency.pdf", b"%PDF-1.4 legacy\n")
        self.fixture.write(
            "site/public/papers/paper3_apjs_v3.2.0-r13.pdf", body("P3", "v3.2.0-r13"),
        )
        self.fixture.set_papers_ts(p3_version="v3.2.0-r13")

        result = self.fixture.run()
        self.assertEqual(result["verdict"], "FAIL")

        # The alias name IS owned by P2, so the July-10 copy reads as a mirror
        # directive G never reached -- not as an anonymous orphan.
        drifted = self.findings(result, "mirror-bytes-stale")
        self.assertEqual([item["path"] for item in drifted],
                         ["public/focused_paper_bounce_fnl_forecast.pdf"])
        self.assertEqual(drifted[0]["paper_id"], "P2")
        self.assertEqual(drifted[0]["actual_md5"], md5(body("P2", "v1.7.110")))

        orphan = self.findings(result, "unregistered-orphan-pdf")
        self.assertEqual([item["path"] for item in orphan],
                         ["public/paper3_barriers_ech_transparency.pdf"])

        p3 = self.findings(result, "site-reference-stale")
        self.assertTrue(p3)
        self.assertTrue(all(item["paper_id"] == "P3" for item in p3))
        self.assertTrue(all(
            item["reference"] == "/papers/paper3_apjs_v3.2.0-r13.pdf" for item in p3
        ))
        # The registered P2 aliases in real served roots stay clean -- the gate
        # must not turn correct mirroring into noise.
        self.assertFalse([
            item for item in result["findings"]
            if item.get("path", "").endswith(("papers/fnl-forecast-paper.pdf",
                                              "papers/paper2_fnl_forecast.pdf"))
        ])


if __name__ == "__main__":
    unittest.main()
