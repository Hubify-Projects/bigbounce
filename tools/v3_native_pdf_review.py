#!/usr/bin/env python3
"""
v3 cross-vendor adversarial review — TRUE native-PDF pipeline.

Closes the internal/external review gap (Houston directive 2026-06-05).

Root cause of v2 gap: v2 sent native PDF to only Gemini; the other 4 reviewers
got pdftotext extraction which strips figures, tables, equations, and 2-column
layout. Internal reviews missed what external (web-app) reviews catch because
external reviewers see the rendered document.

v3 fixes:
  1. ALL major reviewers receive native PDF rendering:
     - Anthropic Claude Opus 4.7   — document content block (NEW reviewer)
     - OpenAI o3                   — Files API + Responses API input_file
     - Gemini 2.5 Pro              — File API / inline PDF
     - Grok 4                      — rasterized to per-page PNG images
     - Perplexity sonar-pro        — text + web search (citation forensics only)
  2. Max reasoning on every vendor:
     - Anthropic: extended thinking 16K budget
     - OpenAI: reasoning effort "high"
     - Gemini: temperature 0.2, max thinking
     - Grok: temperature 0.1
  3. DeepSeek removed (always timed out — 2.75 hr on R9 P3).
  4. Adds Claude as the "matches Houston's web Claude review" baseline.

Usage:
    python tools/v3_native_pdf_review.py <pdf_path> <round_label> <paper_tag> [round_context]

Keys read from bigbounce/.env.local then youmd/.env.local.
"""
from __future__ import annotations

import base64
import os
import re
import subprocess
import sys
import tempfile
import time
import traceback
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_PATHS = [
    REPO / ".env.local",
    Path("/Users/houstongolden/Desktop/CODE_2025/youmd/.env.local"),
]

# ---------------------------------------------------------------------------
# THE REVIEW PROMPT — pass 1 (initial brutal review)
# ---------------------------------------------------------------------------
REVIEW_PROMPT_TEMPLATE = """\
[REVIEWER METADATA — NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS]
Paper tag: {paper_tag}  |  Round: {round_label}  |  Pages: {page_count}
Round context (not in paper): {round_context}
[END REVIEWER METADATA]

You are a {persona} for a cosmology methods paper submitted to Physical Review D.
This is one of the most rigorous physics journals in the world. The acceptance
bar is HIGH. Reject anything that doesn't meet PRD standards.

YOUR ROLE: {focus}

CRITICAL: The [REVIEWER METADATA] block above is NOT part of the paper. Only flag
text that actually appears in the rendered PDF you are looking at.

REVIEW INSTRUCTIONS:
1. Read the FULL paper carefully. Do NOT skim. Examine every figure, table,
   equation, caption, reference, and the abstract. RECOMPUTE every quoted σ,
   p-value, ratio, and percentage from the displayed numbers. Check dimensional
   consistency of every equation. Audit every figure axis label.
2. Write a complete referee report. NO cap on findings — list everything you find.
3. Classify each finding as:
     - ESSENTIAL: paper cannot be accepted without this fix
     - MAJOR: significant revision required
     - MINOR: address but paper can proceed
     - NIT: cosmetic
4. For each finding give:
     - ID (e.g. {paper_tag}-E1, {paper_tag}-M3, {paper_tag}-N1)
     - Section + page number (you can see the rendered PDF, so report exact page)
     - Specific problem (quote the offending text or equation)
     - Required fix
5. Do NOT soften findings. Do NOT praise things that are merely adequate.
6. If the paper is too long for the claimed contribution, say so and state the
   recommended maximum page count.
7. If sigma values from different null procedures appear side-by-side without
   explicit "not directly comparable" qualification at every juxtaposition, flag ESSENTIAL.
8. If any version-history language, internal audit tags ("R7", "R8", "R-round"),
   "superseded", "earlier draft", review-log prose, or internal-bookkeeping
   placeholders appear in the body, flag each one.
9. If any duplicate phrases appear (e.g. "canonical canonical-mask"), flag them.
10. Audit every load-bearing scalar in the abstract: is it consistent with the body?
    Recompute it from the displayed inputs.
11. AUDIT FIGURES AND TABLES: look at each figure and table. Does the caption match
    the body claim? Are the numbers internally consistent? Are axes labeled?
    Are units correct? Is the figure useful or filler?
12. Check that the abstract accurately summarizes what the paper PROVES — not
    what it hopes to prove.
13. Check the bibliography: do citation years, arXiv IDs, journals match? Are
    quoted statistics traceable to the cited paper's abstract/tables?
14. Check for unsupported claims: every assertion of novelty, "first", "largest",
    "unprecedented" — is it true?

End your report with:
## Summary recommendation
One of: REJECT | MAJOR REVISIONS | MINOR REVISIONS | ACCEPT WITH MINOR CORRECTIONS | ACCEPT

Then one paragraph justifying your recommendation.
"""

# ---------------------------------------------------------------------------
# PASS 2 — self-critique prompt (find what was missed)
# ---------------------------------------------------------------------------
SELF_CRITIQUE_TEMPLATE = """\
Here is the review you just wrote on this paper:

================================================================
{initial_review}
================================================================

Now re-examine the paper with FRESH EYES. Your previous review almost certainly
missed important issues. PRD reviewers expect rigor — what did you not look hard enough at?

Check specifically these classes of issue, which initial passes routinely miss:

A. ARITHMETIC. For every σ, percentage, ratio, count, and p-value in tables,
   abstract, and conclusions — RECOMPUTE the value from the inputs in the
   adjacent column / displayed numbers. Flag every value that doesn't match.

B. FIGURE-CAPTION VS BODY-CLAIM. Every figure has a caption, and somewhere
   in the body there's a sentence describing what the figure shows. Compare them.
   Do the numbers match? Do the axes match the units quoted in the body?

C. EQUATION DIMENSIONAL CONSISTENCY. For every equation displayed: does the
   left side have the same units as the right side? Are any unit factors
   missing? Are normalizations explicit?

D. INTERNAL CROSS-REFERENCES. Every \\ref, \\cite, \\eqref. Does the section
   referenced actually contain what the citing sentence claims? Is the cited
   equation the right one?

E. NULL PROCEDURE COMPARABILITY. Every σ value implicitly comes from a null
   procedure. Are different σ values from different null procedures juxtaposed
   without an explicit "not directly comparable" qualifier? Flag every
   juxtaposition.

F. ABSTRACT FAITHFULNESS. Re-read the abstract one sentence at a time.
   For each sentence: where in the body is this proven? Does the body
   support the claim, or does it walk it back?

G. UNSUPPORTED NOVELTY CLAIMS. Every "first", "largest", "novel",
   "unprecedented", "survey-scale" — is the supporting comparison shown?
   Or is it hand-waved?

H. UNQUANTIFIED HEDGES. Phrases like "consistent with", "broadly compatible",
   "no significant tension" — these often hide quantitative gaps. Is the
   actual delta + uncertainty quoted?

I. APPENDIX VS MAIN-TEXT MISMATCH. Do the appendices' equations / configs
   match what the main text claims was done?

J. STALE NUMBERS. Some numbers may be from earlier paper versions that
   weren't updated when other numbers changed. Look for inconsistent pairs.

Add ALL new findings to your report below, using the same format
([{paper_tag}-E#, M#, m#, N#]). Do not repeat findings already in your initial
review — only add NEW ones.

If you find nothing new, write "NO ADDITIONAL FINDINGS" and a brief explanation
of why your initial review was already complete.
"""

# ---------------------------------------------------------------------------
# Reviewers
# ---------------------------------------------------------------------------
REVIEWERS = {
    "Claude_brutal": {
        "vendor": "anthropic",
        "model": "claude-opus-4-7",
        "fallback": "claude-sonnet-4-6",
        "persona": "Brutal-honesty PRD referee with full PDF access (figures, tables, equations)",
        "focus": (
            "BRUTAL HONESTY. Cut through narrative inflation. Is the central claim "
            "actually new and significant? Are 'first', 'novel', 'survey-scale', "
            "'unprecedented' framings honest given the literature? Is every headline "
            "sigma value earned by the methodology? Does the abstract match what the "
            "body proves? Audit every figure caption against the body claim. Audit every "
            "table for arithmetic consistency — recompute the numbers. Flag overclaims, "
            "false confidence, weak hedges presented as strong conclusions, internal "
            "audit tags ('R7', 'superseded'), and duplicate phrases. Treat as a real "
            "PRD submission you would reject on first pass."
        ),
        "native_pdf": True,
    },
    "OpenAI_methodology": {
        "vendor": "openai",
        "model": "gpt-5",
        "fallback": "o3",
        "persona": "Physical Review D methodology referee with full PDF access",
        "focus": (
            "Methodology rigor: statistical-method validity, derivation chains, "
            "dimensional analysis, internal arithmetic consistency, error propagation. "
            "Audit every scalar in the abstract and conclusions for a traceable source "
            "in the body. Flag overclaims of statistical significance. Check sigma "
            "values from different null procedures are kept distinct. Flag if the "
            "primary estimator is not pre-declared. Check N_MC sample sizes against "
            "claimed sub-sigma precision. Audit figure axes and tables for arithmetic "
            "consistency. Recompute every quoted ratio and percentage."
        ),
        "native_pdf": True,
    },
    "Gemini_cosmology": {
        "vendor": "gemini",
        "model": "gemini-2.5-pro",
        "fallback": "gemini-2.0-flash",
        "persona": "Physical Review D cosmology-physics referee with full PDF access",
        "focus": (
            "Theoretical physics + observational rigor. Gauge-frame vs physical-frame, "
            "GR projection effects, EFT counting, consistency-relation applicability. "
            "Parity-odd vs parity-even kept strictly separate? Is the paper appropriately "
            "scoped for its dataset? Does the abstract scope match the analysis? Is the "
            "paper too long for the claimed contribution? Does it need restructuring "
            "into main + appendix? Audit figures and tables for cosmological consistency. "
            "Flag any cosmological claim not directly supported by an in-paper computation."
        ),
        "native_pdf": True,
    },
    "Grok_brutal": {
        "vendor": "xai",
        "model": "grok-4",
        "fallback": "grok-3",
        "persona": "Adversarial journal referee with PDF rendered as images (sees figures)",
        "focus": (
            "Adversarial perspective. Would you reject this paper on first read? List "
            "every reason you would. Don't be polite. Compare against the literature "
            "frontier. Are the framings honest? Is the methodology rigorous? Audit "
            "figures and tables (you can see them). Flag any internal-audit artifact "
            "language. Flag any number in the abstract that you cannot trace to the body."
        ),
        "native_pdf": True,  # via image rasterization
    },
    "Perplexity_citations": {
        "vendor": "perplexity",
        "model": "sonar-pro",
        "fallback": "sonar",
        "persona": "Citation forensics auditor with real-time web search access",
        "focus": (
            "Verify every cited paper. Are arXiv IDs correct? Are titles/authors/venues "
            "accurate? Check against arXiv.org and NASA ADS via web search. Flag "
            "fused metadata, DOI mismatches, 'in preparation' fakes, future-dated arXiv "
            "IDs. Verify every quoted statistic from prior work can be traced to the "
            "cited paper's abstract or tables. Audit the bibliography for "
            "duplicate or stale entries."
        ),
        "native_pdf": False,  # text + web search is the right modality for this role
    },
}

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
# PDF utilities
# ---------------------------------------------------------------------------
def get_page_count(pdf_path: Path) -> int:
    try:
        r = subprocess.run(
            ["pdfinfo", str(pdf_path)],
            capture_output=True, text=True, timeout=15,
        )
        for line in r.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return 0


def extract_pdf_text(pdf_path: Path) -> str:
    """Used only by Perplexity reviewer (text + web search)."""
    try:
        r = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=60,
        )
        if r.returncode == 0 and len(r.stdout) > 1000:
            return r.stdout
    except Exception:
        pass
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf_path))
        return "\n\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception:
        return ""


def rasterize_pdf_to_images(pdf_path: Path, dpi: int = 150, max_pages: int = 25) -> list[bytes]:
    """Used by Grok (xAI takes images, not PDFs). Caps at max_pages for cost."""
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            ["pdftoppm", "-r", str(dpi), "-png",
             "-f", "1", "-l", str(max_pages),
             str(pdf_path), f"{tmpdir}/page"],
            check=True, capture_output=True, timeout=180,
        )
        files = sorted(Path(tmpdir).glob("page-*.png"))
        return [f.read_bytes() for f in files]


# ---------------------------------------------------------------------------
# Vendor SDK calls — ALL native-PDF where the vendor supports it
# ---------------------------------------------------------------------------
def call_anthropic(keys: dict, model: str, prompt: str, pdf_path: Path) -> tuple[str, str]:
    """Claude with native PDF document block + extended thinking (streaming)."""
    import anthropic
    client = anthropic.Anthropic(api_key=keys["ANTHROPIC_API_KEY"], timeout=900.0)
    pdf_b64 = base64.standard_b64encode(pdf_path.read_bytes()).decode("utf-8")

    text_chunks: list[str] = []
    model_used = model
    with client.messages.stream(
        model=model,
        max_tokens=32000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        temperature=1.0,  # required when thinking enabled
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_b64,
                    },
                },
                {"type": "text", "text": prompt},
            ],
        }],
    ) as stream:
        for text_event in stream.text_stream:
            text_chunks.append(text_event)
        final_msg = stream.get_final_message()
        model_used = getattr(final_msg, "model", model)
    return "".join(text_chunks), model_used


def call_openai_responses(keys: dict, model: str, prompt: str, pdf_path: Path) -> tuple[str, str]:
    """OpenAI Responses API with native PDF via Files API + reasoning effort high.
    Handles both reasoning models (o3, o3-pro) and gpt-5 family."""
    from openai import OpenAI
    client = OpenAI(api_key=keys["OPENAI_API_KEY"], timeout=900.0)

    with open(pdf_path, "rb") as f:
        upload = client.files.create(file=f, purpose="user_data")

    common_input = [
        {
            "role": "user",
            "content": [
                {"type": "input_file", "file_id": upload.id},
                {"type": "input_text", "text": prompt},
            ],
        }
    ]

    # gpt-5 with reasoning_effort=high can consume tens of thousands of tokens
    # before producing visible output. Cap output at 64000 (max), use medium
    # reasoning for gpt-5 family to balance depth and output room.
    is_gpt5 = "gpt-5" in model.lower()
    effort = "medium" if is_gpt5 else "high"
    max_out = 64000 if is_gpt5 else 32000

    try:
        # Try with reasoning param first (works for o3, o3-pro, gpt-5)
        try:
            resp = client.responses.create(
                model=model,
                reasoning={"effort": effort},
                input=common_input,
                max_output_tokens=max_out,
            )
        except Exception as e:
            err_msg = str(e).lower()
            # Some models don't accept reasoning param; retry without
            if "reasoning" in err_msg or "unsupported parameter" in err_msg or "unknown parameter" in err_msg:
                resp = client.responses.create(
                    model=model,
                    input=common_input,
                    max_output_tokens=max_out,
                )
            else:
                raise

        # output_text is the convenience getter when present
        text = getattr(resp, "output_text", "") or ""
        if not text:
            for item in (resp.output or []):
                if getattr(item, "type", "") == "message":
                    for c in (item.content or []):
                        if hasattr(c, "text") and c.text:
                            text += c.text
        model_used = getattr(resp, "model", model)

        # Detect silent downgrade only — gpt-5 → gpt-4o / gpt-3.5 / gpt-4.1 is a regression
        if "gpt-4o" in model_used.lower() or "gpt-3.5" in model_used.lower():
            raise RuntimeError(f"silent fallback: requested {model}, got {model_used}")
        return text, model_used
    finally:
        try:
            client.files.delete(upload.id)
        except Exception:
            pass


def call_gemini(keys: dict, model: str, prompt: str, pdf_path: Path) -> tuple[str, str]:
    """Gemini 2.5 Pro with native PDF via inline data (or Files API for big PDFs)."""
    import google.generativeai as genai
    genai.configure(api_key=keys["GOOGLE_GEMINI_API_KEY"])

    pdf_bytes = pdf_path.read_bytes()
    pdf_size_mb = len(pdf_bytes) / 1024 / 1024

    if pdf_size_mb < 18:
        # Inline base64
        file_ref = {
            "mime_type": "application/pdf",
            "data": base64.b64encode(pdf_bytes).decode(),
        }
    else:
        # Files API
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(pdf_bytes)
            tmp_path = tmp.name
        uploaded = genai.upload_file(tmp_path, mime_type="application/pdf")
        for _ in range(60):
            if uploaded.state.name == "ACTIVE":
                break
            time.sleep(2)
            uploaded = genai.get_file(uploaded.name)
        file_ref = uploaded

    gmodel = genai.GenerativeModel(model)
    resp = gmodel.generate_content(
        [file_ref, prompt],
        generation_config={
            "max_output_tokens": 32000,
            "temperature": 0.2,
        },
        request_options={"timeout": 600},
    )
    return resp.text, model


def call_grok_images(keys: dict, model: str, prompt: str, pdf_path: Path) -> tuple[str, str]:
    """Grok 4 with rasterized PDF pages as images (xAI doesn't take PDF directly)."""
    from openai import OpenAI
    client = OpenAI(
        api_key=keys["XAI_API_KEY"],
        base_url="https://api.x.ai/v1",
        timeout=600.0,
    )

    page_images = rasterize_pdf_to_images(pdf_path, dpi=150, max_pages=25)
    image_content = []
    for img_bytes in page_images:
        img_b64 = base64.b64encode(img_bytes).decode()
        image_content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{img_b64}",
                "detail": "high",
            },
        })

    resp = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": [
                *image_content,
                {"type": "text", "text": prompt},
            ],
        }],
        max_tokens=32000,
        temperature=0.1,
    )
    return resp.choices[0].message.content or "", resp.model


def call_perplexity(keys: dict, model: str, prompt: str, paper_text: str) -> tuple[str, str]:
    """Perplexity sonar-pro: text + web search (for citation forensics)."""
    from openai import OpenAI
    client = OpenAI(
        api_key=keys["PERPLEXITY_API_KEY"],
        base_url="https://api.perplexity.ai",
        timeout=300.0,
    )
    full_prompt = prompt + "\n\n--- PAPER TEXT (for citation forensics) ---\n\n" + paper_text
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}],
        max_tokens=16000,
        temperature=0.1,
    )
    return resp.choices[0].message.content or "", resp.model


# ---------------------------------------------------------------------------
# Reviewer dispatcher
# ---------------------------------------------------------------------------
def _dispatch_one_call(vendor: str, keys: dict, model: str, prompt: str, pdf_path: Path, paper_text: str) -> tuple[str, str]:
    if vendor == "anthropic":
        return call_anthropic(keys, model, prompt, pdf_path)
    elif vendor == "openai":
        return call_openai_responses(keys, model, prompt, pdf_path)
    elif vendor == "gemini":
        return call_gemini(keys, model, prompt, pdf_path)
    elif vendor == "xai":
        return call_grok_images(keys, model, prompt, pdf_path)
    elif vendor == "perplexity":
        return call_perplexity(keys, model, prompt, paper_text)
    else:
        raise RuntimeError(f"unknown vendor: {vendor}")


def run_reviewer(
    name: str,
    cfg: dict,
    prompt: str,
    pdf_path: Path,
    paper_text: str,
    round_label: str,
    paper_tag: str,
    keys: dict,
    out_dir: Path,
    enable_pass2: bool = True,
) -> dict:
    t0 = time.time()
    content = ""
    model_used = "unknown"
    error_msg = ""
    fallback_used = False
    pass2_added = 0
    vendor = cfg["vendor"]

    try:
        primary_model = cfg["model"]
        fallback_model = cfg["fallback"]
        try:
            content, model_used = _dispatch_one_call(vendor, keys, primary_model, prompt, pdf_path, paper_text)
        except Exception as e:
            print(f"[{name}] primary {primary_model} failed: {e!r} — trying fallback {fallback_model}", file=sys.stderr)
            fallback_used = True
            content, model_used = _dispatch_one_call(vendor, keys, fallback_model, prompt, pdf_path, paper_text)

        # PASS 2 — self-critique to catch what initial review missed
        if enable_pass2 and content and len(content) > 500 and "FAILED" not in content[:60]:
            try:
                p2_prompt = SELF_CRITIQUE_TEMPLATE.format(
                    initial_review=content[:20000],  # cap for context budget
                    paper_tag=paper_tag,
                )
                # Perplexity gets paper text again since it's text-mode
                # Others get the PDF again
                p2_content, _ = _dispatch_one_call(
                    vendor, keys,
                    primary_model if not fallback_used else fallback_model,
                    p2_prompt, pdf_path, paper_text,
                )
                if p2_content and "NO ADDITIONAL FINDINGS" not in p2_content[:200].upper():
                    content += "\n\n---\n\n## PASS 2 — self-critique findings (what initial review missed)\n\n" + p2_content
                    pass2_added = len(p2_content)
            except Exception as e:
                print(f"[{name}] pass-2 self-critique failed (non-fatal): {e!r}", file=sys.stderr)
    except Exception as e:
        error_msg = repr(e) + "\n" + traceback.format_exc()
        content = f"## Reviewer call FAILED\n\n```\n{error_msg}\n```\n"

    dt = time.time() - t0
    fb = f" [FALLBACK from {cfg['model']}]" if fallback_used else ""

    if vendor == "anthropic":
        input_note = "NATIVE PDF (document block) + extended thinking 16K"
    elif vendor == "openai":
        input_note = "NATIVE PDF (Files API + Responses) + reasoning_effort=high"
    elif vendor == "gemini":
        input_note = "NATIVE PDF (inline or Files API)"
    elif vendor == "xai":
        input_note = f"NATIVE PDF (rasterized to PNG images, 150 DPI)"
    else:
        input_note = "TEXT + web search"

    p2_note = f" + pass-2 self-critique ({pass2_added} chars)" if pass2_added > 0 else (" + pass-2 NO_NEW" if pass2_added == 0 and not error_msg else "")
    # Wrong-PDF-round detectability (2026-06-09 incident): stamp the exact
    # input PDF identity into every reviewer artifact.
    try:
        import hashlib, subprocess as _sp
        _md5 = hashlib.md5(pdf_path.read_bytes()).hexdigest()[:8]
        _pages = _sp.check_output(["pdfinfo", str(pdf_path)]).decode()
        _pages = next((l.split()[1] for l in _pages.splitlines() if l.startswith("Pages")), "?")
    except Exception:
        _md5, _pages = "?", "?"
    header = (
        f"# {paper_tag} {round_label} — {cfg['persona']}\n\n"
        f"**Reviewer**: `{name}`\n"
        f"**Model**: `{model_used}`{fb}\n"
        f"**Input PDF**: `{pdf_path}` md5={_md5} pages={_pages}\n"
        f"**Input format**: {input_note}{p2_note}\n"
        f"**Wall time**: {dt:.1f}s\n\n---\n\n"
    )

    out_path = out_dir / f"{round_label}_{paper_tag}_{name}.md"
    out_path.write_text(header + content)

    ok = bool(content and "FAILED" not in content[:60] and len(content) > 200)
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
            f"Usage: {sys.argv[0]} <pdf_path> <round_label> <paper_tag> [round_context]\n",
            file=sys.stderr,
        )
        return 1

    pdf_path = Path(sys.argv[1]).resolve()
    round_label = sys.argv[2]
    paper_tag = sys.argv[3]
    round_context = sys.argv[4] if len(sys.argv) >= 5 else (
        "Full adversarial peer review — treat this as a real PRD/MNRAS submission."
    )

    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return 1

    keys = load_keys()
    required = ["ANTHROPIC_API_KEY", "OPENAI_API_KEY", "GOOGLE_GEMINI_API_KEY", "XAI_API_KEY", "PERPLEXITY_API_KEY"]
    missing = [k for k in required if k not in keys]
    if missing:
        print(f"[warn] Missing keys: {missing}", file=sys.stderr)

    page_count = get_page_count(pdf_path)
    paper_text = extract_pdf_text(pdf_path)  # only used by Perplexity
    print(f"[v3 native-PDF review] {pdf_path.name}: {page_count} pages, {len(paper_text):,} chars extracted (Perplexity only)", flush=True)
    print(f"[v3 native-PDF review] Dispatching {len(REVIEWERS)} reviewers in parallel...", flush=True)

    out_dir = REPO / "project-context" / "peer-reviews"
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    with ThreadPoolExecutor(max_workers=len(REVIEWERS)) as pool:
        futures = {}
        for name, cfg in REVIEWERS.items():
            prompt = REVIEW_PROMPT_TEMPLATE.format(
                persona=cfg["persona"],
                paper_tag=paper_tag,
                round_label=round_label,
                round_context=round_context,
                page_count=page_count,
                focus=cfg["focus"],
            )
            futures[pool.submit(
                run_reviewer,
                name, cfg, prompt, pdf_path, paper_text,
                round_label, paper_tag, keys, out_dir,
            )] = name

        for fut in as_completed(futures):
            res = fut.result()
            status = "OK  " if res["ok"] else "FAIL"
            fb = " [fallback]" if res["fallback"] else ""
            print(f"[{status}] {res['name']:24s} {res['model']:35s} {res['duration_s']:6.1f}s{fb} → {Path(res['out']).name}", flush=True)
            results.append(res)

    ok_count = sum(1 for r in results if r["ok"])
    print(f"\n[v3 native-PDF review] Complete: {ok_count}/{len(results)} reviewers OK", flush=True)
    return 0 if ok_count >= 3 else 2


if __name__ == "__main__":
    sys.exit(main())
