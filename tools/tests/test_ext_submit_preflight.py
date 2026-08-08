#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/ext_submit.sh"


class ExtSubmitPreflightTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ext_submit_preflight_")
        self.base = Path(self.tmp.name)
        self.pdf = self.base / "paper.pdf"
        self.pdf.write_bytes(b"%PDF-1.4\n%%EOF\n")
        self.calls = self.base / "calls.log"
        self.browser = self.base / "browser"
        self.browser.write_text(
            "#!/usr/bin/env bash\n"
            f"echo browser:$* >> {self.calls!s}\n"
            "if [ \"${1:-}\" = status ]; then echo 'Mode: launched'; fi\n",
            encoding="utf-8",
        )
        self.browser.chmod(0o755)
        self.round_dir = self.base / "round"

    def tearDown(self):
        self.tmp.cleanup()

    def environment(self, preflight: Path) -> dict[str, str]:
        return {
            **os.environ,
            "BIGBOUNCE_REPO": str(ROOT),
            "BIGBOUNCE_BROWSER_BIN": str(self.browser),
            "BIGBOUNCE_EXT_ROUND_DIR_BASE": str(self.round_dir),
            "BIGBOUNCE_PREFLIGHT_BIN": str(preflight),
        }

    def run_submit(self, preflight: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", str(SCRIPT), "P4", "grok", "TEST-WAVE", str(self.pdf)],
            cwd=ROOT,
            env=self.environment(preflight),
            text=True,
            capture_output=True,
        )

    def test_preflight_failure_denies_browser_launch(self):
        preflight = self.base / "preflight_fail.py"
        preflight.write_text(
            "import pathlib,sys\n"
            f"pathlib.Path({str(self.calls)!r}).open('a').write('preflight:' + sys.argv[1] + '\\n')\n"
            "raise SystemExit(2)\n",
            encoding="utf-8",
        )
        result = self.run_submit(preflight)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("browser launch denied", result.stderr)
        self.assertEqual(self.calls.read_text().splitlines(), ["preflight:run"])

    def test_run_and_verify_precede_first_browser_call(self):
        preflight = self.base / "preflight_pass.py"
        preflight.write_text(
            "import json,pathlib,sys\n"
            f"log=pathlib.Path({str(self.calls)!r})\n"
            "log.open('a').write('preflight:' + sys.argv[1] + '\\n')\n"
            "receipt=pathlib.Path(sys.argv[sys.argv.index('--receipt')+1])\n"
            "if sys.argv[1]=='run':\n"
            " receipt.parent.mkdir(parents=True,exist_ok=True)\n"
            " receipt.write_text(json.dumps({'verdict':'PASS','core_sha256':'a'*64,'receipt_sha256':'b'*64}))\n",
            encoding="utf-8",
        )
        result = self.run_submit(preflight)
        self.assertNotEqual(result.returncode, 0)  # headed assertion intentionally stops the fixture
        self.assertEqual(
            self.calls.read_text().splitlines(),
            ["preflight:run", "preflight:verify", "browser:status"],
        )
        receipt = self.round_dir / "preflight/P4_grok_TEST-WAVE.json"
        self.assertEqual(json.loads(receipt.read_text())["verdict"], "PASS")

    def test_malformed_pass_receipt_denies_browser_launch(self):
        preflight = self.base / "preflight_malformed.py"
        preflight.write_text(
            "import json,pathlib,sys\n"
            f"log=pathlib.Path({str(self.calls)!r})\n"
            "log.open('a').write('preflight:' + sys.argv[1] + '\\n')\n"
            "receipt=pathlib.Path(sys.argv[sys.argv.index('--receipt')+1])\n"
            "if sys.argv[1]=='run':\n"
            " receipt.parent.mkdir(parents=True,exist_ok=True)\n"
            " receipt.write_text(json.dumps({'verdict':'PASS','core_sha256':'short','receipt_sha256':'b'*64}))\n",
            encoding="utf-8",
        )
        result = self.run_submit(preflight)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("browser:status", self.calls.read_text())

    def test_manifest_rows_bind_preflight_provenance(self):
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn('"preflight": {"path": preflight_path', source)
        self.assertIn('"core_sha256": preflight_core', source)
        self.assertIn('"receipt_sha256": preflight_receipt', source)


if __name__ == "__main__":
    unittest.main()
