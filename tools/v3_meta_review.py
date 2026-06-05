#!/usr/bin/env python3
"""
v3.2 meta-reviewer — runs AFTER all 5 vendors complete.

Gives GPT-5 (or Claude Opus 4.7 fallback) the original PDF + concatenated text
of all 5 reviewer reports, and asks: "These 5 reviewers each found some issues.
What did they ALL miss? Look at the paper again with fresh eyes — find issues
that none of the 5 reviewers above caught."

This adds a 6th layer of review using meta-analysis: instead of finding the same
issues, the meta-reviewer specifically hunts for blind spots common to all 5.

Usage:
    python tools/v3_meta_review.py <pdf_path> <round_label> <paper_tag>

Example:
    python tools/v3_meta_review.py site/public/p4-chirality.pdf R10v3p1 P4
"""
from __future__ import annotations

import base64
import sys
import time
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
REVIEWS_DIR = REPO / "project-context" / "peer-reviews"

ENV_PATHS = [
    REPO / ".env.local",
    Path("/Users/houstongolden/Desktop/CODE_2025/youmd/.env.local"),
]


def load_keys() -> dict[str, str]:
    keys: dict[str, str] = {}
    for p in ENV_PATHS:
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if v and k not in keys:
                    keys[k] = v
    return keys


META_PROMPT_TEMPLATE = """\
You are the META-REFEREE for a Physical Review D submission. Five expert
referees have already reviewed this paper. Their reports are concatenated below.

YOUR TASK: read the rendered PDF, then read the 5 prior reports. Find issues
that NONE of the 5 reviewers caught. Your value-add comes specifically from
identifying blind spots common to all 5 reviewers.

You should focus on classes of issue that are systematically harder to catch:

1. **Deep arithmetic chains.** When σ comes from a multi-step computation
   (binomial → MASTER deconvolution → Monte Carlo null → ratio), reviewers
   often verify each step but miss errors in the chain composition. Audit the
   full derivation chain end-to-end.

2. **Cross-reference inconsistencies.** Numbers may match within a section
   but contradict the same quantity quoted in a different section. Build a
   table of every quantity mentioned and look for inconsistencies.

3. **Sensitivity vs precision conflation.** Papers often quote a sensitivity
   limit and a measurement precision interchangeably. Are they the same? Should
   they be?

4. **Hidden conditioning.** "The result is X under the null" often hides what
   the null actually assumes. Is the null mathematically well-defined? Does
   it bias the test?

5. **Selection cuts post-hoc.** "We use the subsample mask" — was the
   subsample mask chosen because it produced the headline number? Is there
   a pre-registered choice?

6. **Comparison fairness.** When comparing to Shamir/Iye/Tadaki, is the
   sample selection identical? Footprint matched? Depth matched? Or is the
   comparison apples-to-oranges?

7. **The honest abstract test.** Read the abstract as if you are a
   non-specialist. What does it claim? Does the body actually prove that?
   Or does the body walk back the abstract's strongest claim?

8. **Footnote and appendix sneak-ins.** Material that should be in the body
   often gets buried in footnotes or appendices. Are there caveats, errata,
   or self-corrections hidden where reviewers don't look?

9. **Missing tests.** What test would a hostile reviewer ask for that
   isn't in the paper? List the most damaging tests the authors did NOT run.

10. **Unit consistency at the integrated level.** Every quantity in the
    paper has a unit. The dimensional consistency of integrated results
    (chi-squared, posteriors, evidence ratios) often hides unit drift.

Below: paper PDF (rendered) → 5 prior reviewer reports → your meta-review.

================================================================
PRIOR REVIEW 1: Claude_brutal (PRD brutal-honesty referee, native PDF + thinking)
================================================================
{claude_review}

================================================================
PRIOR REVIEW 2: OpenAI_methodology (PRD methodology referee, native PDF + reasoning)
================================================================
{openai_review}

================================================================
PRIOR REVIEW 3: Gemini_cosmology (PRD cosmology referee, native PDF)
================================================================
{gemini_review}

================================================================
PRIOR REVIEW 4: Grok_brutal (adversarial referee, PDF rasterized as images)
================================================================
{grok_review}

================================================================
PRIOR REVIEW 5: Perplexity_citations (citation forensics, web search)
================================================================
{perplexity_review}

================================================================
META-REVIEW INSTRUCTIONS:
================================================================

Now write the meta-review. Find issues NONE of the 5 above caught.

For each NEW finding:
- ID: {paper_tag}-META-E# / -M# / -m# / -N#
- Severity: ESSENTIAL / MAJOR / MINOR / NIT
- Section + page (you have the PDF)
- Why no other reviewer caught it (1 sentence)
- Specific problem (quote the text)
- Required fix

End with:
## Meta-review recommendation
One of: REJECT | MAJOR REVISIONS | MINOR REVISIONS | ACCEPT WITH MINOR CORRECTIONS | ACCEPT

Then one paragraph: given the union of all 6 reviews (including yours), what
is the actual blocker count, and what is your confidence the paper would survive
external (non-bigbounce) peer review.
"""


def call_meta_reviewer(keys: dict, model: str, prompt: str, pdf_path: Path) -> tuple[str, str]:
    """Run GPT-5 (or Claude fallback) as meta-reviewer with native PDF."""
    from openai import OpenAI
    client = OpenAI(api_key=keys["OPENAI_API_KEY"], timeout=900.0)
    with open(pdf_path, "rb") as f:
        upload = client.files.create(file=f, purpose="user_data")
    try:
        try:
            resp = client.responses.create(
                model=model,
                reasoning={"effort": "high"},
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_file", "file_id": upload.id},
                        {"type": "input_text", "text": prompt},
                    ],
                }],
                max_output_tokens=32000,
            )
        except Exception as e:
            if "reasoning" in str(e).lower() or "unknown parameter" in str(e).lower():
                resp = client.responses.create(
                    model=model,
                    input=[{
                        "role": "user",
                        "content": [
                            {"type": "input_file", "file_id": upload.id},
                            {"type": "input_text", "text": prompt},
                        ],
                    }],
                    max_output_tokens=32000,
                )
            else:
                raise
        text = getattr(resp, "output_text", "") or ""
        if not text:
            for item in (resp.output or []):
                if getattr(item, "type", "") == "message":
                    for c in (item.content or []):
                        if hasattr(c, "text") and c.text:
                            text += c.text
        return text, getattr(resp, "model", model)
    finally:
        try:
            client.files.delete(upload.id)
        except Exception:
            pass


def call_meta_claude(keys: dict, model: str, prompt: str, pdf_path: Path) -> tuple[str, str]:
    """Claude fallback meta-reviewer."""
    import anthropic
    client = anthropic.Anthropic(api_key=keys["ANTHROPIC_API_KEY"], timeout=900.0)
    pdf_b64 = base64.standard_b64encode(pdf_path.read_bytes()).decode("utf-8")
    chunks: list[str] = []
    model_used = model
    with client.messages.stream(
        model=model,
        max_tokens=32000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        temperature=1.0,
        messages=[{
            "role": "user",
            "content": [
                {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_b64}},
                {"type": "text", "text": prompt},
            ],
        }],
    ) as stream:
        for evt in stream.text_stream:
            chunks.append(evt)
        final = stream.get_final_message()
        model_used = getattr(final, "model", model)
    return "".join(chunks), model_used


def load_review(round_label: str, paper_tag: str, reviewer: str) -> str:
    p = REVIEWS_DIR / f"{round_label}_{paper_tag}_{reviewer}.md"
    if not p.exists():
        return f"(reviewer {reviewer} report not found)"
    txt = p.read_text(errors="replace")
    # Strip the leading meta header
    return txt[:25000]  # cap per reviewer to fit context budget


def main() -> int:
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <pdf_path> <round_label> <paper_tag>", file=sys.stderr)
        return 1
    pdf_path = Path(sys.argv[1]).resolve()
    round_label = sys.argv[2]
    paper_tag = sys.argv[3]

    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 1

    keys = load_keys()

    prompt = META_PROMPT_TEMPLATE.format(
        paper_tag=paper_tag,
        claude_review=load_review(round_label, paper_tag, "Claude_brutal"),
        openai_review=load_review(round_label, paper_tag, "OpenAI_methodology"),
        gemini_review=load_review(round_label, paper_tag, "Gemini_cosmology"),
        grok_review=load_review(round_label, paper_tag, "Grok_brutal"),
        perplexity_review=load_review(round_label, paper_tag, "Perplexity_citations"),
    )

    t0 = time.time()
    fallback = False
    try:
        text, model_used = call_meta_reviewer(keys, "gpt-5-pro", prompt, pdf_path)
        if not text or len(text) < 500:
            raise RuntimeError("empty gpt-5-pro response")
    except Exception as e:
        print(f"[meta] gpt-5-pro failed: {e!r} — trying gpt-5", file=sys.stderr)
        try:
            text, model_used = call_meta_reviewer(keys, "gpt-5", prompt, pdf_path)
        except Exception as e2:
            print(f"[meta] gpt-5 also failed: {e2!r} — falling to Claude Opus 4.7", file=sys.stderr)
            fallback = True
            text, model_used = call_meta_claude(keys, "claude-opus-4-7", prompt, pdf_path)
    dt = time.time() - t0

    header = (
        f"# {paper_tag} {round_label} — META-REVIEW (synthesizes all 5 prior reviewers)\n\n"
        f"**Reviewer**: `meta_reviewer`\n"
        f"**Model**: `{model_used}`{' [FALLBACK to Claude]' if fallback else ''}\n"
        f"**Input format**: NATIVE PDF + 5 prior reviewer reports as context\n"
        f"**Wall time**: {dt:.1f}s\n\n---\n\n"
    )
    out = REVIEWS_DIR / f"{round_label}_{paper_tag}_META_REVIEW.md"
    out.write_text(header + text)
    print(f"→ {out} ({dt:.1f}s, {len(text)} chars)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
