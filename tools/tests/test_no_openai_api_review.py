#!/usr/bin/env python3
"""Regression gates for the no-OpenAI-API review policy."""
from __future__ import annotations

import importlib.util
import ast
import hashlib
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

RETIRED_DUPLICATE_REVIEW_LAUNCHERS = (
    "real_cross_vendor_review.py",
    "cross_vendor_review_direct.py",
    "cross_model_review_gemini.py",
    "final_int_api_review_2026-07-05.py",
    "postpolish_int_api_review_2026-07-06.py",
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
            "$ARTICLE_TYPE", "source_tree: clean detached sparse tree",
        ):
            self.assertIn(binding, source)
        self.assertIn('git clone --quiet --shared --no-checkout "$REPO" "$CODEX_TREE"', source)
        self.assertIn('checkout --quiet --detach "$PACKET_HEAD"', source)
        self.assertIn('"$CODEX_BIN" --cd "$CODEX_TREE" --sandbox read-only', source)
        self.assertIn("dispatch=false", source)
        self.assertIn("INT_SUBSCRIPTION_OUTDIR", source)

    def test_int_wave_dry_run_prints_exact_bindings_without_dispatch(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            codex = root / "codex"
            codex.write_text("#!/bin/sh\necho 'Logged in using ChatGPT'\n", encoding="utf-8")
            codex.chmod(0o755)
            registry = json.loads(
                (ROOT / "project-context/paper_registry.json").read_text()
            )["papers"]["P1B"]
            pdf = ROOT / registry["pdf_path"]
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

    def test_int_wave_codex_only_mode_launches_no_api_subprocess(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            marker = root / "api-launched"
            api_stub = root / "api-review"
            api_stub.write_text(
                f"#!/bin/sh\ntouch {marker!s}\nexit 99\n", encoding="utf-8",
            )
            api_stub.chmod(0o755)
            codex = root / "codex"
            codex.write_text(
                """#!/bin/sh
if [ "${1:-}" = login ]; then
  echo 'Logged in using ChatGPT'
  exit 0
fi
out=''
while [ "$#" -gt 0 ]; do
  if [ "$1" = '--output-last-message' ]; then shift; out="$1"; fi
  shift
done
[ -n "$out" ] || exit 3
printf '(1) VERDICT: MINOR REVISIONS\\n(2) ISSUES: none in stub\\n(3) supported\\n' >"$out"
""",
                encoding="utf-8",
            )
            codex.chmod(0o755)
            outdir = root / "subscription"
            env = dict(os.environ)
            env.update({
                # The explicit CLI mode must override even an inherited
                # API-enabled environment during a subscription-only retry.
                "BIGBOUNCE_INT_API_LEGS_ENABLED": "1",
                "BIGBOUNCE_INT_API_REVIEW_BIN": str(api_stub),
                "BIGBOUNCE_CODEX_BIN": str(codex),
                "BIGBOUNCE_REVIEW_CACHE": str(root / "cache"),
                "INT_SUBSCRIPTION_OUTDIR": str(outdir),
                "OPENAI_API_KEY": "forbidden-openai-secret",
                "ANTHROPIC_API_KEY": "forbidden-anthropic-secret",
                "INT_REVIEW_COMMIT": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
                ).strip(),
            })
            run = subprocess.run(
                ["bash", str(TOOLS / "int_wave.sh"), "--codex-only", "P1B"], cwd=ROOT,
                env=env, capture_output=True, text=True, timeout=45, check=False,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertFalse(marker.exists(), "API dispatcher ran in Codex-only mode")
            self.assertIn("Grok (grok-4.3):           NOT_RUN", run.stdout)
            self.assertIn("Gemini (gemini-3.1-pro):   NOT_RUN", run.stdout)
            raws = list(outdir.glob("intwave_P1B_codex_*.md"))
            self.assertEqual(len(raws), 1)
            raw = raws[0].read_text(encoding="utf-8")
            self.assertIn("binding: packet_key=", raw)
            self.assertIn("source_tree: clean detached sparse tree", raw)
            self.assertIn(
                "review_paths=arxiv,packages/namaster-proof,"
                "reproducibility/p1_namaster_500mc,.github/workflows",
                raw,
            )
            receipt = json.loads((outdir / "manifest.jsonl").read_text().strip())
            self.assertEqual(receipt["paper"], "P1B")
            self.assertEqual(receipt["vendor"], "codex-subscription")
            self.assertEqual(receipt["provider"], "chatgpt-subscription-via-codex-cli")
            self.assertEqual(receipt["status"], "ok")
            self.assertEqual(receipt["verdict"], "MINOR REVISIONS")
            self.assertFalse(receipt["openai_api_used"])
            self.assertFalse(receipt["anthropic_used"])
            self.assertRegex(receipt["packet_key"], r"^[0-9a-f]{64}$")
            self.assertRegex(receipt["prompt_sha256"], r"^[0-9a-f]{64}$")
            self.assertEqual(
                receipt["raw_response_sha256"],
                hashlib.sha256(raws[0].read_bytes()).hexdigest(),
            )
            serialized = json.dumps(receipt).lower()
            for forbidden in ("forbidden-openai-secret", "forbidden-anthropic-secret", "session_id", "api_key"):
                self.assertNotIn(forbidden, serialized)

    def test_routine_int_wave_defaults_codex_subscription_off(self):
        source = (TOOLS / "int_wave.sh").read_text(encoding="utf-8")
        self.assertIn(
            'CODEX_ENABLED="${BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED:-0}"',
            source,
        )
        self.assertIn('elif [ "${1:-}" = "--with-codex" ]; then', source)
        self.assertRegex(source, r'--with-codex" \]; then\s+CODEX_ENABLED=1')

    def test_codex_receipt_backfill_records_failure_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            raw = root / "failed.md"
            raw.write_text(
                """# INT Codex-subscription Review — P4 v1.0.244 — gpt-5.6-sol (high)
paper: P4  version: v1.0.244  tex: paper.tex
binding: packet_key=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  prompt_sha256=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
provenance: commit=cccccccccccccccccccccccccccccccccccccccc  source_sha256=dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
pdf: snapshot=/safe/snapshot.pdf  sha256=eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee  pages=26
UTC: 2026-07-15T09:06:44Z
(Codex subscription leg errored; diagnostics: sanitized.log)
""",
                encoding="utf-8",
            )
            manifest = root / "manifest.jsonl"
            for _ in range(2):
                run = subprocess.run(
                    ["bash", str(TOOLS / "int_wave.sh"), "--backfill-codex-receipt", str(raw), str(manifest)],
                    cwd=ROOT, capture_output=True, text=True, timeout=15, check=False,
                )
                self.assertEqual(run.returncode, 0, run.stderr)
            lines = manifest.read_text().splitlines()
            self.assertEqual(len(lines), 1)
            receipt = json.loads(lines[0])
            self.assertEqual(receipt["status"], "failed")
            self.assertIsNone(receipt["verdict"])
            self.assertEqual(receipt["pdf_pages"], 26)
            self.assertFalse(receipt["openai_api_used"])
            self.assertFalse(receipt["anthropic_used"])

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
                 mock.patch.object(module, "verify_receipt", return_value={"verdict": "PASS"}), \
                 mock.patch.object(module, "build_packet", return_value=packet) as build, \
                 mock.patch.object(module, "publish_packet", return_value=(root / "packet.json", False)), \
                 mock.patch.object(module, "resolve_pdf_snapshot", return_value=pdf), \
                 mock.patch.dict(os.environ, {"BIGBOUNCE_PREFLIGHT_RECEIPT": str(root / "preflight.json")}):
                rec = module.run_one("P1A", "grok")
            self.assertEqual(
                build.call_args.kwargs["preflight_receipt"], root / "preflight.json"
            )
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

    def test_direct_provider_retry_archives_existing_raw_before_overwrite(self):
        module = load_script("int_api_review_2026-07-08.py")
        with tempfile.TemporaryDirectory() as td:
            outfile = Path(td) / "API_P4_grok.md"
            original = b"first failed provider body\n"
            outfile.write_bytes(original)
            archived = module.archive_existing_raw(outfile)
            self.assertIsNotNone(archived)
            self.assertEqual(archived.read_bytes(), original)
            self.assertIn("provider-raw-archive", archived.parts)
            self.assertIn(hashlib.sha256(original).hexdigest()[:12], archived.name)

    def test_direct_api_leg_requires_preflight_before_network(self):
        module = load_script("int_api_review_2026-07-08.py")
        module.REGISTRY = {"P1A": {
            "pdf_path": "paper.pdf", "tex_path": "paper.tex",
            "target_journal": "PRD", "article_type": "article", "review_profile": "physics",
        }}
        with mock.patch.dict(os.environ, {}, clear=False), \
             mock.patch.object(module.requests, "post") as post, \
             mock.patch.object(module, "build_packet") as build:
            os.environ.pop("BIGBOUNCE_PREFLIGHT_RECEIPT", None)
            with self.assertRaisesRegex(ValueError, "BIGBOUNCE_PREFLIGHT_RECEIPT is required"):
                module.run_one("P1A", "grok")
        post.assert_not_called()
        build.assert_not_called()

    def test_invalid_preflight_fails_before_network_and_packet(self):
        module = load_script("int_api_review_2026-07-08.py")
        module.REGISTRY = {"P1A": {
            "pdf_path": "paper.pdf", "tex_path": "paper.tex",
            "target_journal": "PRD", "article_type": "article", "review_profile": "physics",
        }}
        with mock.patch.dict(os.environ, {"BIGBOUNCE_PREFLIGHT_RECEIPT": "/tmp/stale.json"}), \
             mock.patch.object(module, "verify_receipt", side_effect=ValueError("stale preflight")), \
             mock.patch.object(module.requests, "post") as post, \
             mock.patch.object(module, "build_packet") as build:
            with self.assertRaisesRegex(ValueError, "stale preflight"):
                module.run_one("P1A", "gemini")
        post.assert_not_called()
        build.assert_not_called()

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

    def test_codex_review_tree_uses_registry_owned_review_paths(self):
        source = (TOOLS / "int_wave.sh").read_text(encoding="utf-8")
        self.assertIn('REVIEW_PATHS_TEXT="$(python3 "$REGISTRY" "$PAPER" review_paths)"', source)
        self.assertIn(
            'git -C "$CODEX_TREE" sparse-checkout set "${REVIEW_PATHS[@]}"',
            source,
        )
        self.assertIn(
            "modality: registry-scoped Codex CLI ChatGPT-subscription referee",
            source,
        )
        self.assertNotIn("you have the full repo", source)
        self.assertNotIn('SOURCE_SCOPE="$(dirname "$TEX_REL")"', source)

    def test_hourly_portfolio_rereview_loop_is_retired(self):
        run = subprocess.run(
            ["bash", str(TOOLS / "v3_review_autoloop.sh")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        self.assertEqual(run.returncode, 2)
        self.assertIn("retired", run.stderr.lower())

    def test_duplicate_direct_review_launchers_are_retired(self):
        for name in RETIRED_DUPLICATE_REVIEW_LAUNCHERS:
            run = subprocess.run(
                [sys.executable, str(TOOLS / name)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=15,
                check=False,
            )
            self.assertEqual(run.returncode, 2, f"{name}: {run.stderr}")
            self.assertIn("retired", run.stderr.lower(), name)

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

    def test_native_pdf_engine_uses_current_gemini_models(self):
        module = load_script("v3_native_pdf_review.py")
        gemini = module.REVIEWERS["Gemini_cosmology"]
        self.assertEqual(gemini["model"], "gemini-3.1-pro-preview")
        self.assertEqual(gemini["fallback"], "gemini-3.5-flash")

    def test_native_pdf_engine_selects_only_requested_reviewers(self):
        module = load_script("v3_native_pdf_review.py")
        selected = module.select_reviewers("Gemini_cosmology, Perplexity_citations")
        self.assertEqual(list(selected), ["Gemini_cosmology", "Perplexity_citations"])
        self.assertEqual(module.VENDOR_KEY_VARS["perplexity"], "PERPLEXITY_API_KEY")

    def test_native_pdf_engine_rejects_invalid_reviewer_allowlists(self):
        module = load_script("v3_native_pdf_review.py")
        for value, expected in (
            ("", "non-empty"),
            ("Gemini_cosmology,", "non-empty"),
            ("Unknown", "unknown reviewer"),
            ("Gemini_cosmology,Gemini_cosmology", "duplicate"),
        ):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, expected):
                    module.select_reviewers(value)

    def test_native_pdf_engine_requires_every_selected_reviewer_to_succeed(self):
        module = load_script("v3_native_pdf_review.py")
        active = module.select_reviewers("Gemini_cosmology,Grok_brutal")
        self.assertTrue(module.all_selected_reviewers_succeeded([{"ok": True}, {"ok": True}], active))
        self.assertFalse(module.all_selected_reviewers_succeeded([{"ok": True}], active))
        self.assertFalse(module.all_selected_reviewers_succeeded([{"ok": True}, {"ok": False}], active))

    def test_native_pdf_engine_requires_preflight_before_loading_provider_keys(self):
        module = load_script("v3_native_pdf_review.py")
        pdf = module.REPO / module.REGISTRY["P1A"]["pdf_path"]
        argv = [str(TOOLS / "v3_native_pdf_review.py"), str(pdf), "test", "P1A"]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.dict(os.environ, {}, clear=False), \
             mock.patch.object(module, "load_keys") as load_keys:
            os.environ.pop("BIGBOUNCE_PREFLIGHT_RECEIPT", None)
            self.assertEqual(module.main(), 2)
        load_keys.assert_not_called()

    def test_native_pdf_engine_rejects_stale_preflight_before_provider_work(self):
        module = load_script("v3_native_pdf_review.py")
        pdf = module.REPO / module.REGISTRY["P1A"]["pdf_path"]
        argv = [str(TOOLS / "v3_native_pdf_review.py"), str(pdf), "test", "P1A"]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.dict(os.environ, {"BIGBOUNCE_PREFLIGHT_RECEIPT": "/tmp/stale.json"}), \
             mock.patch.object(module, "verify_receipt", side_effect=module.PortfolioError("stale")), \
             mock.patch.object(module, "load_keys") as load_keys:
            self.assertEqual(module.main(), 2)
        load_keys.assert_not_called()

    def test_apjs_wrapper_delegates_to_canonical_p3_registry_route(self):
        source = (TOOLS / "int_wave_apjs.sh").read_text(encoding="utf-8")
        self.assertIn('exec "$REPO/tools/int_wave.sh" P3', source)
        registry = json.loads((ROOT / "project-context/paper_registry.json").read_text())["papers"]["P3"]
        self.assertEqual(registry["review_profile"], "APJS-CATALOG")
        self.assertIn("Astrophysical Journal Supplement", registry["target_journal"])

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
