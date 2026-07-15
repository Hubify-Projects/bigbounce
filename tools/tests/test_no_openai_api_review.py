#!/usr/bin/env python3
"""Regression gates for the no-OpenAI-API review policy."""
from __future__ import annotations

import importlib.util
import ast
import json
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

RETIRED_OPENAI_API_LAUNCHERS = (
    "cross_model_review_openai.py",
    "cross_model_review_retry.py",
    "cross_model_review_synthesize.py",
    "v3_meta_review.py",
)


def discover_executable_review_surface() -> tuple[Path, ...]:
    """Discover current/future review entry points instead of trusting a fixed list."""
    found: list[Path] = []
    for base in (TOOLS, ROOT / "ops"):
        for path in base.rglob("*"):
            if path.suffix not in {".py", ".sh"} or "tests" in path.parts:
                continue
            source = path.read_text(encoding="utf-8", errors="replace")
            rel = str(path.relative_to(ROOT)).lower()
            if any(token in rel for token in ("review", "wave", "loop", "cron", "watchdog")) or "reviewer" in source.lower():
                found.append(path)
    return tuple(sorted(found))


def load_script(name: str):
    path = TOOLS / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class NoOpenAIAPIReviewTests(unittest.TestCase):
    def test_int_wave_codex_subscription_is_exact_packet_bound(self):
        source = (TOOLS / "int_wave.sh").read_text(encoding="utf-8")
        for binding in (
            "packet_key=$PACKET_KEY", "prompt_sha256=$PROMPT_SHA",
            "commit=$PACKET_HEAD", "source_sha256=$SOURCE_SHA",
            "sha256=$PDF_SHA", "pages=$PDF_PAGES", "$TARGET_JOURNAL",
            "$ARTICLE_TYPE", "source_tree: clean detached worktree",
        ):
            self.assertIn(binding, source)
        self.assertIn('worktree add --quiet --detach "$CODEX_TREE" "$PACKET_HEAD"', source)
        self.assertIn('"$CODEX_BIN" --cd "$CODEX_TREE" --sandbox read-only', source)
        self.assertIn("dispatch=false", source)

    def test_int_wave_dry_run_prints_exact_bindings_without_dispatch(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            codex = root / "codex"
            codex.write_text("#!/bin/sh\necho 'Logged in using ChatGPT'\n", encoding="utf-8")
            codex.chmod(0o755)
            pdf = ROOT / "arxiv/paper1b_mcmc_companion.pdf"
            import hashlib
            expected = hashlib.sha256(pdf.read_bytes()).hexdigest()
            env = dict(os.environ)
            env.update({
                "BIGBOUNCE_INT_WAVE_DRY_RUN": "1",
                "BIGBOUNCE_CODEX_BIN": str(codex),
                "BIGBOUNCE_REVIEW_CACHE": str(root / "cache"),
                "INT_EXPECTED_PDF_SHA256": expected,
                "INT_REVIEW_COMMIT": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
                ).strip(),
            })
            run = subprocess.run(
                ["bash", str(TOOLS / "int_wave.sh"), "P1B"], cwd=ROOT,
                env=env, capture_output=True, text=True, timeout=30, check=False,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIn("dispatch=false", run.stdout)
            self.assertIn(f"pdf_sha256={expected}", run.stdout)
            self.assertRegex(run.stdout, r"packet_key=[0-9a-f]{64}")
            self.assertRegex(run.stdout, r"prompt_sha256=[0-9a-f]{64}")
            self.assertIn("source_tree=detached-clean", run.stdout)
            self.assertNotIn("launched:", run.stdout)

    def test_xai_response_parsing_builds_allowlisted_receipt(self):
        module = load_script("int_api_review_2026-07-08.py")
        upload = mock.Mock(status_code=200, text="")
        upload.json.return_value = {"id": "file-xai-1"}
        response = mock.Mock(status_code=200, text="", headers={"x-request-id": "req-xai-1"})
        response.json.return_value = {
            "id": "resp-xai-1",
            "model": "grok-4.3-20260701",
            "output_text": "(1) VERDICT: ACCEPT",
            "usage": {"input_tokens": 10, "output_tokens": 4, "cost": 0.0012},
        }
        with tempfile.NamedTemporaryFile(suffix=".pdf") as pdf:
            module.ENV["XAI_API_KEY"] = "test-secret-must-not-land"
            with mock.patch.object(module.requests, "post", side_effect=[upload, response]):
                text, meta = module.call_xai(pdf.name)
        self.assertIn("ACCEPT", text)
        self.assertEqual(meta["requested_model"], module.XAI_MODEL)
        self.assertEqual(meta["resolved_model"], "grok-4.3-20260701")
        self.assertEqual(meta["response_id"], "resp-xai-1")
        self.assertEqual(meta["request_id"], "req-xai-1")
        self.assertEqual(meta["provider_reported_cost"], 0.0012)
        self.assertNotIn("test-secret", json.dumps(meta))

    def test_gemini_response_parsing_marks_unreported_cost_unavailable(self):
        module = load_script("int_api_review_2026-07-08.py")
        response = mock.Mock(
            status_code=200,
            text="",
            headers={"x-goog-request-id": "req-google-1"},
        )
        response.json.return_value = {
            "responseId": "resp-google-1",
            "modelVersion": "gemini-3.1-pro-preview-202607",
            "candidates": [{"content": {"parts": [{"text": "(1) VERDICT: ACCEPT"}]}}],
            "usageMetadata": {"promptTokenCount": 9, "candidatesTokenCount": 3},
        }
        with tempfile.NamedTemporaryFile(suffix=".pdf") as pdf:
            pdf.write(b"%PDF mocked")
            pdf.flush()
            module.ENV["GEMINI_API_KEY"] = "test-secret-must-not-land"
            with mock.patch.object(module.requests, "post", return_value=response):
                text, meta = module.call_gemini(pdf.name)
        self.assertIn("ACCEPT", text)
        self.assertEqual(meta["resolved_model"], "gemini-3.1-pro-preview-202607")
        self.assertEqual(meta["response_id"], "resp-google-1")
        self.assertEqual(meta["request_id"], "req-google-1")
        self.assertEqual(meta["provider_reported_cost"], "unavailable")
        self.assertNotIn("test-secret", json.dumps(meta))

    def test_success_manifest_and_review_header_include_sanitized_receipt(self):
        module = load_script("int_api_review_2026-07-08.py")
        entry = {
            "pdf_path": "paper.pdf",
            "tex_path": "paper.tex",
            "target_journal": "PRD",
            "article_type": "research article",
            "review_profile": "physics",
        }
        meta = {
            "provider": "xai",
            "requested_model": module.XAI_MODEL,
            "resolved_model": "grok-resolved",
            "response_id": "resp-1",
            "request_id": "req-1",
            "usage": {"input_tokens": 5},
            "provider_reported_cost": "unavailable",
            "modality": "native-PDF test",
        }
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            pdf = root / "snapshot.pdf"
            pdf.write_bytes(b"%PDF mocked")
            module.OUTDIR = root / "out"
            module.MANIFEST = module.OUTDIR / "manifest.jsonl"
            module.REGISTRY = {"P1A": entry}
            module.VENDORS = {"grok": (module.XAI_MODEL, lambda _: ("(1) VERDICT: ACCEPT", meta))}
            packet = {
                "packet_key": "packet-1",
                "pdf_sha256": "a" * 64,
                "repository_head": "commit-1",
            }
            with mock.patch.object(module, "live_version", return_value="v1"), \
                 mock.patch.object(module, "review_cache_root", return_value=root / "cache"), \
                 mock.patch.object(module, "build_packet", return_value=packet), \
                 mock.patch.object(module, "publish_packet", return_value=(root / "packet.json", False)), \
                 mock.patch.object(module, "resolve_pdf_snapshot", return_value=pdf):
                rec = module.run_one("P1A", "grok")
            manifest = json.loads(module.MANIFEST.read_text().strip())
            receipt = manifest["provider_receipt"]
            self.assertEqual(receipt["requested_model"], module.XAI_MODEL)
            self.assertEqual(receipt["resolved_model"], "grok-resolved")
            self.assertEqual(receipt["request_id"], "req-1")
            self.assertEqual(receipt["attempt"], 1)
            self.assertIsInstance(receipt["latency_seconds"], float)
            self.assertEqual(rec["provider_receipt"], receipt)
            header = (module.OUTDIR / "API_P1A_grok.md").read_text()
            self.assertIn("provider_receipt:", header)
            self.assertNotIn("Authorization", header)
            self.assertNotIn("test-secret", header)

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

    def test_native_pdf_engine_has_no_anthropic_reviewer_and_blocks_dispatch(self):
        module = load_script("v3_native_pdf_review.py")
        self.assertFalse(
            any(cfg["vendor"] == "anthropic" for cfg in module.REVIEWERS.values())
        )
        with self.assertRaisesRegex(RuntimeError, "Anthropic/Claude review dispatch is disabled"):
            module._dispatch_one_call(
                "anthropic", {}, "claude", "prompt", Path("x.pdf"), ""
            )

    def test_apjs_dry_run_resolves_live_paper_version(self):
        source = (TOOLS / "int_wave_apjs.sh").read_text(encoding="utf-8")
        self.assertIn(r"\\newcommand\{\\paperVersion\}", source)

    def test_apjs_live_api_dispatch_uses_canonical_p3_and_parses_raws(self):
        """Exercise the real wrapper dispatch/parser seam without provider calls."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            outdir = root / "round"
            stub = root / "stub_review.py"
            stub.write_text(
                """import os, pathlib, sys
paper, vendor = sys.argv[1:]
if paper != "P3":
    raise SystemExit(f"expected canonical P3, got {paper}")
outdir = pathlib.Path(os.environ["INT_OUTDIR"])
outdir.mkdir(parents=True, exist_ok=True)
(outdir / f"API_{paper}_{vendor}.md").write_text(
    "PARSED VERDICT: ACCEPT\\n", encoding="utf-8"
)
""",
                encoding="utf-8",
            )
            env = dict(os.environ)
            env.update(
                {
                    "BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED": "0",
                    "BIGBOUNCE_INT_API_LEGS_ENABLED": "1",
                    "BIGBOUNCE_INT_API_REVIEW_BIN": str(stub),
                    "INT_OUTDIR": str(outdir),
                }
            )
            run = subprocess.run(
                ["bash", str(TOOLS / "int_wave_apjs.sh")],
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
                timeout=20,
                check=False,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIn("Grok (grok-4.3):           ACCEPT", run.stdout)
            self.assertIn("Gemini (gemini-3.1-pro):   ACCEPT", run.stdout)
            self.assertTrue((outdir / "API_P3_grok.md").is_file())
            self.assertTrue((outdir / "API_P3_gemini.md").is_file())
            self.assertFalse((outdir / "API_P3APJS_grok.md").exists())

    def test_active_dispatch_files_do_not_contain_openai_api_endpoint(self):
        for path in discover_executable_review_surface():
            source = path.read_text(encoding="utf-8")
            self.assertNotIn("api.openai.com", source, str(path.relative_to(ROOT)))

    def test_review_python_openai_compatible_clients_pin_non_openai_base_url(self):
        """The OpenAI SDK is allowed only as a protocol client for xAI/Perplexity."""
        for path in discover_executable_review_surface():
            if path.suffix != ".py":
                continue
            name = str(path.relative_to(ROOT))
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=name)
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                fn = node.func
                if not isinstance(fn, ast.Name) or fn.id != "OpenAI":
                    continue
                base_urls = [
                    kw.value.value
                    for kw in node.keywords
                    if kw.arg == "base_url" and isinstance(kw.value, ast.Constant)
                ]
                self.assertTrue(base_urls, f"{name}:{node.lineno} has an unpinned OpenAI client")
                self.assertTrue(
                    base_urls[0].startswith(("https://api.x.ai/", "https://api.perplexity.ai")),
                    f"{name}:{node.lineno} points at a forbidden provider",
                )

    def test_api_health_check_never_calls_anthropic_and_uses_current_repo(self):
        module = load_script("v3_api_health_check.py")
        self.assertFalse(hasattr(module, "check_anthropic"))
        self.assertEqual(module.REPO, ROOT)

    def test_mixed_vendor_reviewers_have_no_openai_leg(self):
        direct = load_script("cross_vendor_review_direct.py")
        real = load_script("real_cross_vendor_review.py")
        final = load_script("final_int_api_review_2026-07-05.py")
        postpolish = load_script("postpolish_int_api_review_2026-07-06.py")
        self.assertFalse(any("openai" in name.lower() for name in direct.REVIEWERS))
        self.assertFalse(any(cfg.get("sdk") == "openai" for cfg in real.REVIEWERS.values()))
        self.assertNotIn("openai", final.VENDORS)
        self.assertNotIn("openai", postpolish.VENDORS)

    def test_retired_api_launchers_fail_closed_without_credentials(self):
        env = dict(os.environ)
        env.pop("OPENAI_API_KEY", None)
        env.pop("CODEX_API_KEY", None)
        for name in RETIRED_OPENAI_API_LAUNCHERS:
            run = subprocess.run(
                [sys.executable, str(TOOLS / name)],
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            self.assertEqual(run.returncode, 2, f"{name}: {run.stderr}")
            self.assertIn("subscription", run.stderr.lower(), name)

    def test_canonical_onboarding_does_not_route_openai_review_to_api(self):
        source = (ROOT / "project-context" / "AGENT_ONBOARDING.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("OpenAI native-PDF\n> API", source)
        self.assertRegex(
            source,
            r"OpenAI via (?:authenticated )?Codex\s+CLI/ChatGPT subscription",
        )

    def test_bootstrap_does_not_require_openai_api_key(self):
        source = (ROOT / "ops/handoff/bootstrap.sh").read_text(encoding="utf-8")
        required_line = next(
            line for line in source.splitlines() if line.startswith("REQUIRED_KEYS=")
        )
        self.assertNotIn("OPENAI_API_KEY", required_line)
        self.assertNotIn("anthropic:anthropic", source)


if __name__ == "__main__":
    unittest.main()
