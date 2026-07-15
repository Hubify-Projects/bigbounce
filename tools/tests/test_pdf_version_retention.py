from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "pdf_version_retention", ROOT / "tools/pdf_version_retention.py"
)
retention = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(retention)


class PdfVersionRetentionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        papers = {}
        for index, paper_id in enumerate(retention.CANONICAL_IDS, start=1):
            paper_dir = self.root / "papers" / paper_id.lower()
            paper_dir.mkdir(parents=True)
            tex = paper_dir / "paper.tex"
            pdf = paper_dir / "paper.pdf"
            tex.write_text(
                rf"\newcommand{{\paperVersion}}{{v{index}.0.{index}}}\n",
                encoding="utf-8",
            )
            pdf.write_bytes(f"%PDF-1.4\n{paper_id}\n%%EOF\n".encode())
            papers[paper_id] = {
                "tex_path": str(tex.relative_to(self.root)),
                "pdf_path": str(pdf.relative_to(self.root)),
            }
        registry = self.root / "project-context/paper_registry.json"
        registry.parent.mkdir(parents=True)
        registry.write_text(json.dumps({"papers": papers}), encoding="utf-8")
        self.when = datetime(2026, 7, 14, 20, 30, tzinfo=timezone.utc)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def take(self, run_id: str, *, dry_run: bool = False, **metadata):
        with mock.patch.object(retention, "pdf_page_count", return_value=1):
            return retention.snapshot(
                self.root,
                Path("archive"),
                retention.CANONICAL_IDS,
                captured_at=self.when,
                run_id=run_id,
                dry_run=dry_run,
                **metadata,
            )

    def test_full_snapshot_creates_six_objects_and_immutable_manifest(self) -> None:
        result = self.take("first")
        self.assertTrue(result["complete_six_paper_snapshot"])
        self.assertEqual(len(result["papers"]), 6)
        manifest = self.root / result["manifest_path"]
        self.assertTrue(manifest.is_file())
        for row in result["papers"]:
            archived = self.root / row["archive_object"]
            reference = self.root / row["archive_reference"]
            self.assertTrue(archived.is_file())
            self.assertTrue(reference.is_file())
            self.assertTrue(reference.samefile(archived))
            self.assertEqual(retention.sha256_bytes(archived.read_bytes()), row["sha256"])
            self.assertEqual(row["page_count"], 1)
            self.assertTrue(row["object_created"])
            self.assertTrue(row["reference_created"])

    def test_repeat_snapshot_deduplicates_without_overwriting(self) -> None:
        first = self.take("first")
        second = self.take("second")
        self.assertEqual(
            [row["sha256"] for row in first["papers"]],
            [row["sha256"] for row in second["papers"]],
        )
        self.assertTrue(all(not row["object_created"] for row in second["papers"]))
        self.assertTrue(all(not row["reference_created"] for row in second["papers"]))
        with self.assertRaises(retention.RetentionError):
            self.take("second")

    def test_corrupt_existing_object_fails_closed(self) -> None:
        first = self.take("first")
        archived = self.root / first["papers"][0]["archive_object"]
        archived.chmod(0o644)
        archived.write_bytes(b"corrupt")
        with self.assertRaises(retention.RetentionError):
            self.take("after-corruption")

    def test_dry_run_writes_nothing(self) -> None:
        result = self.take("dry", dry_run=True)
        self.assertEqual(len(result["papers"]), 6)
        self.assertFalse((self.root / "archive").exists())

    def test_manifest_records_repeatable_build_and_review_metadata(self) -> None:
        result = self.take(
            "metadata",
            build_command="latexmk -pdf paper.tex",
            review_round="ROUND_2026-07-14-P3-r7",
        )
        self.assertEqual(result["build_command"], "latexmk -pdf paper.tex")
        self.assertEqual(result["review_round"], "ROUND_2026-07-14-P3-r7")

    def test_page_count_fails_closed(self) -> None:
        failed = subprocess.CompletedProcess(
            ["pdfinfo", "-"], 1, stdout=b"", stderr=b"broken pdf"
        )
        with mock.patch.object(retention.subprocess, "run", return_value=failed):
            with self.assertRaises(retention.RetentionError):
                retention.pdf_page_count(b"%PDF-1.4\n")

    def test_git_provenance_distinguishes_staged_and_unstaged_changes(self) -> None:
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "Retention Test"], check=True)
        subprocess.run(
            ["git", "-C", str(self.root), "config", "user.email", "retention@example.invalid"],
            check=True,
        )
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-qm", "fixture"], check=True)

        p1a = self.root / "papers/p1a/paper.pdf"
        p1b = self.root / "papers/p1b/paper.pdf"
        p1a.write_bytes(p1a.read_bytes() + b"staged\n")
        subprocess.run(["git", "-C", str(self.root), "add", "papers/p1a/paper.pdf"], check=True)
        p1b.write_bytes(p1b.read_bytes() + b"unstaged\n")

        staged = retention.git_path_provenance(self.root, "papers/p1a/paper.pdf")
        unstaged = retention.git_path_provenance(self.root, "papers/p1b/paper.pdf")
        self.assertTrue(staged["index_dirty"])
        self.assertFalse(staged["worktree_dirty"])
        self.assertTrue(staged["overall_dirty"])
        self.assertFalse(unstaged["index_dirty"])
        self.assertTrue(unstaged["worktree_dirty"])
        self.assertTrue(unstaged["overall_dirty"])

    def test_history_backfill_classifies_manuscripts_and_keeps_unclassified_rows_visible(self) -> None:
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "Retention Test"], check=True)
        subprocess.run(
            ["git", "-C", str(self.root), "config", "user.email", "retention@example.invalid"],
            check=True,
        )
        manuscript = self.root / "public/papers/paper1a_ech_nogo_v1A.0.123.pdf"
        figure = self.root / "arxiv/figures/paper1_corner_full_tension.pdf"
        manuscript.parent.mkdir(parents=True, exist_ok=True)
        figure.parent.mkdir(parents=True, exist_ok=True)
        manuscript.write_bytes(b"%PDF-1.4\nP1A historical manuscript\n%%EOF\n")
        figure.write_bytes(b"%PDF-1.4\nfigure artifact\n%%EOF\n")
        subprocess.run(
            [
                "git",
                "-C",
                str(self.root),
                "add",
                str(manuscript.relative_to(self.root)),
                str(figure.relative_to(self.root)),
            ],
            check=True,
        )
        subprocess.run(
            [
                "git",
                "-C",
                str(self.root),
                "commit",
                "-qm",
                "history fixture",
                "--date",
                "2026-07-14T12:00:00-07:00",
            ],
            env={**os.environ, "GIT_COMMITTER_DATE": "2026-07-14T12:00:00-07:00"},
            check=True,
        )

        with mock.patch.object(retention, "pdf_page_count", return_value=1):
            result = retention.history_inventory(
                self.root,
                Path("archive"),
                captured_at=self.when,
                run_id="history",
                materialize=True,
            )

        self.assertEqual(result["coverage"]["git_pdf_object_path_rows"], 2)
        self.assertEqual(result["coverage"]["classified_rows"], 1)
        self.assertEqual(result["coverage"]["unclassified_rows"], 1)
        self.assertEqual(result["coverage"]["by_paper"]["P1A"], 1)
        classified = [row for row in result["rows"] if row["paper_id"] == "P1A"]
        self.assertEqual(len(classified), 1)
        self.assertEqual(classified[0]["paper_version"], "v1A.0.123")
        self.assertTrue((self.root / classified[0]["archive_object"]).is_file())
        self.assertTrue((self.root / classified[0]["archive_reference"]).is_file())
        unclassified = [row for row in result["rows"] if row["paper_id"] is None]
        self.assertEqual(unclassified[0]["classification_reason"], "excluded.figure-or-render-artifact")


if __name__ == "__main__":
    unittest.main()
