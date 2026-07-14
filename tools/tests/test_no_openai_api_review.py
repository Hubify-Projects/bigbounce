#!/usr/bin/env python3
"""Regression gates for the no-OpenAI-API review policy."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))


def load_script(name: str):
    path = TOOLS / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class NoOpenAIAPIReviewTests(unittest.TestCase):
    def test_single_leg_dispatch_fails_closed_before_network(self):
        module = load_script("int_api_review_2026-07-08.py")
        self.assertNotIn("openai", module.VENDORS)
        with mock.patch.object(module.requests, "post") as post:
            with self.assertRaisesRegex(ValueError, "OpenAI API billing is forbidden"):
                module.run_one("P1A", "openai")
        post.assert_not_called()

    def test_current_wave_wrappers_never_dispatch_openai_vendor(self):
        for name in ("int_wave.sh", "int_wave_apjs.sh"):
            source = (TOOLS / name).read_text(encoding="utf-8")
            self.assertNotRegex(source, r'\$PY_REVIEW[^\n]+["\']openai["\']')
            self.assertNotRegex(source, r"for\s+vend\s+in[^\n]*\bopenai\b")

    def test_native_pdf_engine_has_no_openai_reviewer_and_blocks_dispatch(self):
        module = load_script("v3_native_pdf_review.py")
        self.assertFalse(any(cfg["vendor"] == "openai" for cfg in module.REVIEWERS.values()))
        with self.assertRaisesRegex(RuntimeError, "OpenAI API review dispatch is disabled"):
            module._dispatch_one_call("openai", {}, "gpt", "prompt", Path("x.pdf"), "")

    def test_active_dispatch_files_do_not_contain_openai_api_endpoint(self):
        for name in (
            "int_api_review_2026-07-08.py",
            "int_wave.sh",
            "int_wave_apjs.sh",
            "v3_native_pdf_review.py",
        ):
            source = (TOOLS / name).read_text(encoding="utf-8")
            self.assertNotIn("api.openai.com", source)

    def test_canonical_onboarding_does_not_route_openai_review_to_api(self):
        source = (ROOT / "project-context" / "AGENT_ONBOARDING.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("OpenAI native-PDF\n> API", source)
        self.assertIn("OpenAI via Codex CLI/ChatGPT subscription", source)

    def test_bootstrap_does_not_require_openai_api_key(self):
        source = (ROOT / "ops/handoff/bootstrap.sh").read_text(encoding="utf-8")
        required_line = next(
            line for line in source.splitlines() if line.startswith("REQUIRED_KEYS=")
        )
        self.assertNotIn("OPENAI_API_KEY", required_line)


if __name__ == "__main__":
    unittest.main()
