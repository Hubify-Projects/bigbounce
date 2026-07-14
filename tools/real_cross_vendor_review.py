#!/usr/bin/env python3
"""
Real cross-vendor adversarial peer review — PDF-native pipeline.

v2.0 (2026-06-04): rewritten to fix the root cause of internal/external review
gap. Previous version sent raw LaTeX source; this version:
  1. Extracts clean text from the compiled PDF via pdftotext
  2. Sends the PDF natively to Gemini (via Google Generative AI SDK)
  3. Uses direct vendor SDKs (xAI, Perplexity, Gemini) instead of
     routing everything through OpenRouter (eliminates the gpt-4o silent
     fallback problem)
  4. Uses a demanding PRD/MNRAS referee-grade prompt with no findings cap
  5. Keeps OpenRouter as a fallback if a direct SDK call fails

Usage:
    python tools/real_cross_vendor_review.py <pdf_path> <round_label> <paper_tag> [context]

All API keys read from bigbounce/.env.local (fallback: youmd/.env.local).
"""
from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
import time
import ssl
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _SSL_CTX = ssl.create_default_context()

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_PATHS = [
    REPO / ".env.local",
    Path("/Users/houstongolden/Desktop/CODE_2025/youmd/.env.local"),
]
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ---------------------------------------------------------------------------
# Reviewer definitions — using direct SDKs where possible
# ---------------------------------------------------------------------------
REVIEWERS = {
    "Gemini_cosmology": {
        "sdk": "gemini_native_pdf",
        "model": "gemini-2.5-pro",
        "fallback_model": "gemini-2.0-flash",
        "or_model": "google/gemini-2.5-pro",
        "persona": "Physical Review D cosmology-physics referee",
        "focus": (
            "Theoretical physics: gauge-frame vs physical-frame distinctions, GR "
            "projection effects, model-class scope, EFT counting, consistency-relation "
            "applicability. Is the paper appropriately scoped for its dataset? Are "
            "parity-odd vs parity-even observables kept strictly separate? Does the "
            "claimed null result scope match the analysis actually performed? Is the "
            "paper too long for the claimed contribution — does it need restructuring "
            "into a main text + appendix?"
        ),
    },
    "Grok_brutal": {
        "sdk": "xai",
        "model": "grok-4",
        "fallback_model": "grok-3",
        "or_model": "x-ai/grok-4",
        "persona": "Brutal-honesty journal referee (treating this as a real PRD submission)",
        "focus": (
            "Cut through narrative inflation. Is the central claim actually new and "
            "significant? Are 'first', 'novel', 'unprecedented' framings honest given "
            "the literature? Is every headline σ value earned by the methodology or is "
            "it cherry-picked? Does the abstract honestly represent what the body "
            "proves? Flag overclaims, false confidence, weak hedges presented as "
            "strong conclusions. Is the manuscript journal-clean — no internal audit "
            "tags, no review-log prose, no version-history language, no 'queued' "
            "placeholders, no duplicate phrases?"
        ),
    },
    "Perplexity_citations": {
        "sdk": "perplexity",
        "model": "sonar-pro",
        "fallback_model": "sonar",
        "or_model": "perplexity/sonar-pro-search",
        "persona": "Citation forensics auditor with real-time web search access",
        "focus": (
            "Verify every cited paper actually says what is claimed. Are arXiv IDs "
            "correct and resolving to the right paper? Are titles, authors, and venues "
            "accurate? Use web search against arXiv.org and NASA ADS to check. Flag "
            "fused metadata, DOI mismatches, 'in preparation' papers that may now be "
            "public. Check that all quoted statistics from prior work can be "
            "traced to the cited paper's abstract or tables."
        ),
    },
    "DeepSeek_confab": {
        "sdk": "openrouter",
        "model": "deepseek/deepseek-r1-0528",
        "fallback_model": "deepseek/deepseek-r1",
        "or_model": "deepseek/deepseek-r1-0528",
        "persona": "Confabulation-hunter referee (reasoning mode)",
        "focus": (
            "Paranoid about numbers without traceable sources. For every load-bearing "
            "scalar in the abstract and conclusions: is there a JSON/script/dataset "
            "that produces this number? Flag headline figures with no provenance and "
            "arithmetic that cannot be reproduced from displayed values alone. Check "
            "that the decomposition 99.3%/12%/88%/25% adds up consistently and the "
            "narrative doesn't contradict itself between sections."
        ),
    },
}

# ---------------------------------------------------------------------------
# The PRD-grade review prompt — no caps, no softening
# ---------------------------------------------------------------------------
REVIEW_PROMPT_TEMPLATE = """\
[REVIEWER METADATA — NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS]
Paper tag: {paper_tag} | Round: {round_label} | Pages: {page_count}
Changes since last round (for your context only, not in paper): {round_context}
[END REVIEWER METADATA]

You are a {persona} for a cosmology methods paper submitted to Physical Review D.

YOUR ROLE: {focus}

CRITICAL: The [REVIEWER METADATA] header above is NOT part of the paper. Do not flag ROUND, paper_tag, or changes-since-last-round metadata as in-paper artifacts. Only flag text that actually appears in the PAPER TEXT section below.

INSTRUCTIONS:
1. Read the full paper carefully.
2. Write a complete referee report. There is NO cap on the number of findings — list everything you genuinely find.
3. Classify each finding as:
   - ESSENTIAL: paper cannot be accepted without this fix
   - MAJOR: significant revision required
   - MINOR: should be addressed but paper can proceed with editor discretion
   - NIT: very minor, fix if time permits
4. For each finding provide:
   - ID (e.g. {paper_tag}-B1, {paper_tag}-M3, etc.)
   - Section and page number (if visible)
   - Specific problem statement (be concrete, quote the problematic text)
   - Required fix
5. Do NOT soften findings. Do NOT praise things that are merely adequate.
6. If the paper is too long for the claimed contribution, say so and state the recommended maximum page count.
7. If any σ values from different null procedures are presented as if they're on the same scale without qualification, flag this as ESSENTIAL.
8. If any version-history language, internal audit tags, or review-log artifacts appear in the PAPER TEXT body prose, flag each one.
9. If any duplicate phrases appear (e.g. "canonical canonical-mask"), flag them.
10. Check that the abstract accurately summarizes what the paper proves — not what the paper hopes to prove.

End your report with:
## Summary recommendation
One of: REJECT | MAJOR REVISIONS | MINOR REVISIONS | ACCEPT WITH MINOR CORRECTIONS | ACCEPT

Then one paragraph justifying your recommendation.

PAPER TEXT:
{paper_text}
"""

# ---------------------------------------------------------------------------
# Key loading
# ---------------------------------------------------------------------------
def load_keys() -> dict[str, str]:
    keys: dict[str, str] = {}
    for env_path in ENV_PATHS:
        if not env_path.exists():
            continue
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if v and k not in keys:
                    keys[k] = v
    return keys

# ---------------------------------------------------------------------------
# PDF text extraction
# ---------------------------------------------------------------------------
def extract_pdf_text(pdf_path: Path) -> str:
    """Extract clean text from PDF using pdftotext. Falls back to pypdf."""
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=60,
        )
        if result.returncode == 0 and len(result.stdout) > 1000:
            return result.stdout
    except Exception as e:
        print(f"[warn] pdftotext failed: {e}", file=sys.stderr)

    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf_path))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(pages)
    except Exception as e:
        print(f"[warn] pypdf failed: {e}", file=sys.stderr)

    raise RuntimeError(f"Cannot extract text from {pdf_path}")


def get_page_count(pdf_path: Path) -> int:
    try:
        result = subprocess.run(
            ["pdfinfo", str(pdf_path)], capture_output=True, text=True, timeout=10,
        )
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return 0

# ---------------------------------------------------------------------------
# SDK call implementations
# ---------------------------------------------------------------------------
def call_gemini_native_pdf(keys: dict, model: str, prompt: str, pdf_path: Path) -> tuple[str, str]:
    """Gemini with native PDF document understanding — no text extraction needed."""
    import google.generativeai as genai
    genai.configure(api_key=keys["GOOGLE_GEMINI_API_KEY"])

    pdf_bytes = pdf_path.read_bytes()
    pdf_size_mb = len(pdf_bytes) / 1024 / 1024

    if pdf_size_mb > 19:
        # Use Files API for large PDFs
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(pdf_bytes)
            tmp_path = tmp.name
        uploaded = genai.upload_file(tmp_path, mime_type="application/pdf")
        # Wait for processing
        import time as _time
        for _ in range(30):
            if uploaded.state.name == "ACTIVE":
                break
            _time.sleep(2)
            uploaded = genai.get_file(uploaded.name)
        file_ref = uploaded
    else:
        # Inline for smaller PDFs
        file_ref = {"mime_type": "application/pdf", "data": base64.b64encode(pdf_bytes).decode()}

    gmodel = genai.GenerativeModel(model)
    resp = gmodel.generate_content(
        [file_ref, prompt],
        generation_config={"max_output_tokens": 32000, "temperature": 0.3},
    )
    return resp.text, model


def call_xai_sdk(keys: dict, model: str, prompt: str) -> tuple[str, str]:
    """xAI Grok via OpenAI-compatible SDK."""
    from openai import OpenAI
    client = OpenAI(
        api_key=keys["XAI_API_KEY"],
        base_url="https://api.x.ai/v1",
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=32000,
        temperature=0.3,
    )
    return resp.choices[0].message.content or "", resp.model


def call_perplexity_sdk(keys: dict, model: str, prompt: str) -> tuple[str, str]:
    """Perplexity via OpenAI-compatible SDK."""
    from openai import OpenAI
    client = OpenAI(
        api_key=keys["PERPLEXITY_API_KEY"],
        base_url="https://api.perplexity.ai",
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=16000,
        temperature=0.2,
    )
    return resp.choices[0].message.content or "", resp.model


def call_openrouter(api_key: str, model: str, prompt: str, timeout: int = 360) -> tuple[str, str]:
    """OpenRouter fallback."""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 32000,
        "temperature": 0.3,
        "reasoning": {"effort": "high"},
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://bigbounce.hubify.app",
            "X-Title": "BigBounce-cross-vendor-review-v2",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    model_used = result.get("model", model)
    content = result["choices"][0]["message"]["content"]
    return content, model_used


# ---------------------------------------------------------------------------
# Per-reviewer dispatch with fallback chain
# ---------------------------------------------------------------------------
def run_reviewer(
    name: str,
    cfg: dict,
    paper_text: str,
    pdf_path: Path,
    page_count: int,
    round_label: str,
    paper_tag: str,
    round_context: str,
    keys: dict,
    out_dir: Path,
) -> dict:
    prompt = REVIEW_PROMPT_TEMPLATE.format(
        persona=cfg["persona"],
        paper_tag=paper_tag,
        round_label=round_label,
        round_context=round_context,
        page_count=page_count,
        focus=cfg["focus"],
        paper_text=paper_text,
    )

    t0 = time.time()
    content = ""
    model_used = "unknown"
    error_msg = ""
    fallback_used = False

    sdk = cfg["sdk"]
    try:
        if sdk == "gemini_native_pdf":
            try:
                content, model_used = call_gemini_native_pdf(keys, cfg["model"], prompt, pdf_path)
            except Exception as e:
                print(f"[{name}] Gemini native PDF failed ({e}), trying OpenRouter text", file=sys.stderr)
                content, model_used = call_openrouter(keys.get("OPENROUTER_API_KEY", ""), cfg["or_model"], prompt)
                fallback_used = True
        elif sdk == "xai":
            try:
                content, model_used = call_xai_sdk(keys, cfg["model"], prompt)
            except Exception as e:
                print(f"[{name}] xAI SDK failed ({e}), trying OpenRouter", file=sys.stderr)
                content, model_used = call_openrouter(keys.get("OPENROUTER_API_KEY", ""), cfg["or_model"], prompt)
                fallback_used = True
        elif sdk == "perplexity":
            try:
                content, model_used = call_perplexity_sdk(keys, cfg["model"], prompt)
            except Exception as e:
                print(f"[{name}] Perplexity SDK failed ({e}), trying OpenRouter", file=sys.stderr)
                content, model_used = call_openrouter(keys.get("OPENROUTER_API_KEY", ""), cfg["or_model"], prompt)
                fallback_used = True
        elif sdk == "openrouter":
            content, model_used = call_openrouter(keys.get("OPENROUTER_API_KEY", ""), cfg["model"], prompt)
    except Exception as e:
        error_msg = repr(e)
        content = f"## Reviewer call failed\n\n```\n{error_msg}\n```\n"

    dt = time.time() - t0
    fallback_note = f" [FALLBACK from {cfg['model']}]" if fallback_used else ""
    pdf_note = " [NATIVE PDF — Gemini sees rendered document]" if sdk == "gemini_native_pdf" and not fallback_used else " [PDF TEXT via pdftotext]"

    header = (
        f"# {paper_tag} {round_label} — {cfg['persona']}\n\n"
        f"**Model**: `{model_used}`{fallback_note}\n"
        f"**Input format**: {pdf_note}\n"
        f"**Wall time**: {dt:.1f}s\n\n---\n\n"
    )

    out_path = out_dir / f"{round_label}_{paper_tag}_{name}.md"
    out_path.write_text(header + content)

    ok = bool(content and "failed" not in content[:50].lower() and len(content) > 200)
    return {
        "name": name,
        "model": model_used,
        "duration_s": dt,
        "out": str(out_path),
        "ok": ok,
        "fallback": fallback_used,
        "error": error_msg,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    if len(sys.argv) < 4:
        print(
            f"Usage: {sys.argv[0]} <pdf_path> <round_label> <paper_tag> [round_context]\n"
            f"  pdf_path: compiled PDF (not .tex) — e.g. pipelines/p2_chirality/chirality_catalog_paper.pdf\n"
            f"  round_label: e.g. 2026-06-04_1400pt\n"
            f"  paper_tag: P1A | P1B | P2 | P3 | P4 | P5\n",
            file=sys.stderr,
        )
        return 1

    pdf_path = Path(sys.argv[1])
    round_label = sys.argv[2]
    paper_tag = sys.argv[3]
    round_context = sys.argv[4] if len(sys.argv) >= 5 else (
        "Full adversarial peer review — treat this as a real PRD/MNRAS submission."
    )

    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return 1

    keys = load_keys()
    missing = [k for k in ["GOOGLE_GEMINI_API_KEY", "XAI_API_KEY", "PERPLEXITY_API_KEY"] if k not in keys]
    if missing:
        print(f"[warn] Missing direct SDK keys: {missing} — will fall back to OpenRouter for those reviewers", file=sys.stderr)

    print(f"[v2 cross-vendor review] Extracting PDF text from {pdf_path.name}...", flush=True)
    paper_text = extract_pdf_text(pdf_path)
    page_count = get_page_count(pdf_path)
    print(f"[v2 cross-vendor review] Extracted {len(paper_text):,} chars from {page_count} pages", flush=True)
    print(f"[v2 cross-vendor review] Dispatching {len(REVIEWERS)} reviewers in parallel on PDF-extracted text", flush=True)

    out_dir = REPO / "project-context" / "peer-reviews"
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    with ThreadPoolExecutor(max_workers=len(REVIEWERS)) as pool:
        futures = {
            pool.submit(
                run_reviewer,
                name, cfg, paper_text, pdf_path, page_count,
                round_label, paper_tag, round_context, keys, out_dir,
            ): name
            for name, cfg in REVIEWERS.items()
        }
        for fut in as_completed(futures):
            res = fut.result()
            status = "OK  " if res["ok"] else "FAIL"
            fb = " [fallback]" if res["fallback"] else ""
            print(f"[{status}] {res['name']:28s} {res['model']:35s} {res['duration_s']:6.1f}s{fb} → {Path(res['out']).name}", flush=True)
            results.append(res)

    ok_count = sum(1 for r in results if r["ok"])
    print(f"\n[v2 cross-vendor review] Complete: {ok_count}/{len(results)} reviewers OK", flush=True)
    return 0 if ok_count >= 3 else 2


if __name__ == "__main__":
    sys.exit(main())
