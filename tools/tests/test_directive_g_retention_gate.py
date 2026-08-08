#!/usr/bin/env python3
"""Regression tests for directive-G's pre-mirror retention hard gate."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DIRECTIVE_G = ROOT / "tools/directive_g.sh"
VERSION = "vT.1"
COMPILED_PDF = b"%PDF-1.4\ncompiled-directive-g-fixture\n%%EOF\n"
SERVED_PDF = b"%PDF-1.4\nprevious-served-fixture\n%%EOF\n"


class DirectiveGRetentionGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="directive_g_retention_")
        self.repo = Path(self.tmp.name)
        self.tools = self.repo / "tools"
        self.paper_dir = self.repo / "paper"
        self.fake_bin = self.repo / "fake-bin"
        self.home = self.repo / "home"
        self.tinytex = self.home / "Library/TinyTeX/bin/universal-darwin"
        for path in (
            self.tools,
            self.paper_dir,
            self.fake_bin,
            self.tinytex,
            self.repo / "site/public/papers",
            self.repo / "public/papers",
        ):
            path.mkdir(parents=True, exist_ok=True)

        shutil.copy2(DIRECTIVE_G, self.tools / "directive_g.sh")
        today = datetime.now().strftime("%B %d, %Y").replace(" 0", " ")
        (self.paper_dir / "paper.tex").write_text(
            "\\newcommand{\\paperVersion}{" + VERSION + "}\n"
            "\\date{" + today + "}\n",
            encoding="utf-8",
        )
        (self.paper_dir / "paper.pdf").write_bytes(SERVED_PDF)
        (self.repo / "site/public/paper.pdf").write_bytes(SERVED_PDF)
        (self.repo / "site/public/papers/paper.pdf").write_bytes(SERVED_PDF)
        (self.repo / "public/papers/paper.pdf").write_bytes(SERVED_PDF)
        self.events = self.repo / "events.log"

        self._write_executable(
            self.tools / "paper_registry.py",
            """
            #!/usr/bin/env python3
            import sys
            values = {
                "tex_path": "paper/paper.tex",
                "site_slug": "paper-1a",
                "review_profile": "CQG-NOTE",
                "served_aliases": "",
            }
            print(values[sys.argv[2]])
            """,
        )
        self._write_executable(
            self.tools / "pdf_version_retention.py",
            """
            #!/usr/bin/env python3
            import argparse
            import json
            import os
            import sys
            from pathlib import Path

            parser = argparse.ArgumentParser()
            parser.add_argument("--paper", action="append", required=True)
            parser.add_argument("--build-command", required=True)
            parser.add_argument("--review-round", required=True)
            args = parser.parse_args()
            root = Path(__file__).resolve().parents[1]
            event_log = Path(os.environ["EVENT_LOG"])
            with event_log.open("a", encoding="utf-8") as handle:
                handle.write("retention:" + json.dumps(vars(args), sort_keys=True) + "\\n")
            if os.environ.get("FAIL_RETENTION") == "1":
                print("injected retention failure", file=sys.stderr)
                raise SystemExit(9)
            if (root / "site/public/paper.pdf").read_bytes() == (root / "paper/paper.pdf").read_bytes():
                print("served mirror changed before retention", file=sys.stderr)
                raise SystemExit(21)
            relative = Path("project-context/pdf-archive/manifests/test/P1A-vT.1.json")
            manifest = root / relative
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text("{}\\n", encoding="utf-8")
            print(json.dumps({
                "papers": [{"paper_id": args.paper[0], "paper_version": "vT.1"}],
                "build_command": args.build_command,
                "review_round": args.review_round,
                "manifest_path": str(relative),
            }))
            """,
        )
        self._write_executable(
            self.tinytex / "pdflatex",
            """
            #!/usr/bin/env bash
            out="."
            for arg in "$@"; do
              case "$arg" in
                -output-directory=*) out="${arg#*=}" ;;
              esac
            done
            tex="${!#}"
            base="${tex%.tex}"
            mkdir -p "$out"
            printf '%%PDF-1.4\\ncompiled-directive-g-fixture\\n%%%%EOF\\n' > "$out/$base.pdf"
            : > "$out/$base.log"
            """,
        )
        self._write_executable(
            self.fake_bin / "md5",
            """
            #!/usr/bin/env python3
            import hashlib
            import sys
            print(hashlib.md5(open(sys.argv[-1], "rb").read()).hexdigest())
            """,
        )
        self._write_executable(
            self.fake_bin / "stat",
            """
            #!/usr/bin/env python3
            import os
            import sys
            print(os.path.getsize(sys.argv[-1]))
            """,
        )
        self._write_executable(
            self.fake_bin / "pdfinfo",
            """
            #!/usr/bin/env python3
            print("Pages:          1")
            """,
        )
        self._write_executable(
            self.fake_bin / "curl",
            """
            #!/usr/bin/env python3
            import json
            import os
            import sys
            from pathlib import Path

            url = next(value for value in sys.argv[1:] if value.startswith("https://"))
            with Path(os.environ["EVENT_LOG"]).open("a", encoding="utf-8") as handle:
                handle.write("curl:" + url + "\\n")
            if "/mutation" in url:
                print(json.dumps({"status": "success", "value": "row-test"}))
            else:
                print(json.dumps({
                    "status": "success",
                    "value": {
                        "version": os.environ["EXPECTED_VERSION"],
                        "pdfMd5": os.environ["EXPECTED_MD5"],
                    },
                }))
            """,
        )

        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(
            ["git", "config", "user.email", "directive-g@example.invalid"],
            cwd=self.repo,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Directive G Test"],
            cwd=self.repo,
            check=True,
        )
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.repo, check=True)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    @staticmethod
    def _write_executable(path: Path, source: str) -> None:
        path.write_text(textwrap.dedent(source).lstrip(), encoding="utf-8")
        path.chmod(0o755)

    def _run(self, *, verify_only: bool = False, fail_retention: bool = False):
        expected = SERVED_PDF if verify_only else COMPILED_PDF
        env = os.environ.copy()
        env.update(
            {
                "HOME": str(self.home),
                "PATH": str(self.fake_bin) + os.pathsep + env["PATH"],
                "EVENT_LOG": str(self.events),
                "EXPECTED_VERSION": VERSION,
                "EXPECTED_MD5": hashlib.md5(expected).hexdigest(),  # noqa: S324
                "FAIL_RETENTION": "1" if fail_retention else "0",
            }
        )
        args = ["bash", str(self.tools / "directive_g.sh")]
        if verify_only:
            args.append("--verify-only")
        args.extend(["P1A", VERSION, "bounded test closure"])
        return subprocess.run(
            args,
            cwd=self.repo,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )

    def _event_lines(self) -> list[str]:
        if not self.events.exists():
            return []
        return self.events.read_text(encoding="utf-8").splitlines()

    def test_normal_mode_retains_before_mirror_and_prints_manifest(self) -> None:
        result = self._run()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        events = self._event_lines()
        self.assertTrue(events[0].startswith("retention:"), events)
        self.assertIn("/mutation", events[1])
        self.assertIn("/query", events[2])
        receipt = json.loads(events[0].removeprefix("retention:"))
        self.assertEqual(receipt["paper"], ["P1A"])
        self.assertEqual(
            receipt["build_command"],
            "tools/directive_g.sh paper=P1A version=vT.1 source=paper/paper.tex pdflatex_passes=2 bibtex=0",
        )
        self.assertEqual(receipt["review_round"], "directive-g/CQG-NOTE/P1A/vT.1")
        self.assertIn(
            "manifest: project-context/pdf-archive/manifests/test/P1A-vT.1.json",
            result.stdout,
        )
        self.assertEqual((self.repo / "site/public/paper.pdf").read_bytes(), COMPILED_PDF)
        self.assertEqual(
            (self.repo / "site/public/papers/paper_vT.1.pdf").read_bytes(),
            COMPILED_PDF,
        )

    def test_retention_failure_aborts_before_mirror_or_convex(self) -> None:
        result = self._run(fail_retention=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("refusing to mirror or mutate Convex", result.stderr)
        self.assertEqual((self.repo / "site/public/paper.pdf").read_bytes(), SERVED_PDF)
        events = self._event_lines()
        self.assertEqual(len(events), 1, events)
        self.assertTrue(events[0].startswith("retention:"), events)

    def test_verify_only_skips_retention_and_convex_mutation(self) -> None:
        result = self._run(verify_only=True, fail_retention=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("verify-only — skipped, no archive writes", result.stdout)
        self.assertEqual((self.paper_dir / "paper.pdf").read_bytes(), COMPILED_PDF)
        self.assertEqual((self.repo / "site/public/paper.pdf").read_bytes(), SERVED_PDF)
        events = self._event_lines()
        self.assertEqual(len(events), 1, events)
        self.assertIn("/query", events[0])
        self.assertNotIn("/mutation", events[0])
        self.assertFalse((self.repo / "project-context/pdf-archive").exists())


if __name__ == "__main__":
    unittest.main()
