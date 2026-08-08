from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.verify_ci_shell_portability import verify


class CiShellPortabilityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ci_shell_portability_")
        self.root = Path(self.tmp.name)
        (self.root / ".github/workflows").mkdir(parents=True)
        self.relative = ".github/workflows/test.yml"
        self.path = self.root / self.relative

    def tearDown(self):
        self.tmp.cleanup()

    def test_windows_default_shell_rejects_posix_multiline_step(self):
        self.path.write_text(
            """jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Example
        run: |
          python example.py \\
            --output "${RUNNER_TEMP}/result.json"
""",
            encoding="utf-8",
        )
        result = verify(self.root, [self.relative])
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(result["finding_count"], 1)
        self.assertEqual(result["findings"][0]["step"], "Example")

    def test_explicit_bash_accepts_same_step(self):
        self.path.write_text(
            """jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Example
        shell: bash
        run: |
          python example.py \\
            --output "${RUNNER_TEMP}/result.json"
""",
            encoding="utf-8",
        )
        result = verify(self.root, [self.relative])
        self.assertEqual(result["verdict"], "PASS")

    def test_linux_only_workflow_is_out_of_scope(self):
        self.path.write_text(
            """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Example
        run: |
          printf '%s' "${RUNNER_TEMP}"
""",
            encoding="utf-8",
        )
        self.assertEqual(verify(self.root, [self.relative])["verdict"], "PASS")


if __name__ == "__main__":
    unittest.main()
