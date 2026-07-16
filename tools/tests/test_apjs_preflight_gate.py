#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))


def load_child():
    spec = importlib.util.spec_from_file_location(
        "int_api_review_p3apjs_under_test", TOOLS / "int_api_review_p3apjs.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


class ApjsPreflightGateTests(unittest.TestCase):
    def test_child_missing_receipt_fails_before_gemini(self):
        module = load_child()
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(
            module, "apjs_call_gemini"
        ) as provider:
            self.assertEqual(module.main(), 2)
        provider.assert_not_called()

    def test_child_rejects_receipt_without_six_papers(self):
        module = load_child()
        incomplete = {"paper_count": 1, "papers": [{}]}
        with mock.patch.dict(
            os.environ, {"BIGBOUNCE_PREFLIGHT_RECEIPT": "/tmp/receipt.json"}, clear=True
        ), mock.patch.object(module, "verify_receipt", return_value=incomplete):
            with self.assertRaisesRegex(module.PortfolioError, "all six"):
                module.require_verified_preflight()

    def test_child_tampered_receipt_fails_before_gemini(self):
        module = load_child()
        with mock.patch.dict(
            os.environ, {"BIGBOUNCE_PREFLIGHT_RECEIPT": "/tmp/tampered.json"}, clear=True
        ), mock.patch.object(
            module, "verify_receipt", side_effect=module.PortfolioError("content hash mismatch")
        ), mock.patch.object(module, "apjs_call_gemini") as provider:
            self.assertEqual(module.main(), 2)
        provider.assert_not_called()

    def test_wrapper_uses_single_canonical_dispatch_implementation(self):
        source = (TOOLS / "int_wave_apjs.sh").read_text(encoding="utf-8")
        self.assertIn('exec "$REPO/tools/int_wave.sh" P3', source)
        self.assertNotIn("for vend in grok gemini", source)
        self.assertNotIn("codex exec", source)

    def test_wrapper_dry_run_launches_no_provider_or_output_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ)
            env.update(
                {
                    "BIGBOUNCE_INT_WAVE_DRY_RUN": "1",
                    "BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED": "0",
                    "BIGBOUNCE_REVIEW_CACHE": str(Path(tmp) / "cache"),
                    "INT_OUTDIR": str(Path(tmp) / "must-not-exist"),
                }
            )
            result = subprocess.run(
                ["bash", str(TOOLS / "int_wave_apjs.sh")], cwd=ROOT, env=env,
                text=True, capture_output=True, timeout=60, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("DRY_RUN paper=P3", result.stdout)
            self.assertFalse(Path(env["INT_OUTDIR"]).exists())

    def test_canonical_dispatch_does_not_reverify_preflight_in_shell(self):
        source = (TOOLS / "int_wave.sh").read_text(encoding="utf-8")
        self.assertNotIn('bigbounce_preflight.py" verify', source)
        self.assertIn("review_packet.py independently verifies the receipt", source)


if __name__ == "__main__":
    unittest.main()
