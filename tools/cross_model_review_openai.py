#!/usr/bin/env python3
"""
Cross-model peer review of R42 cosmology papers using OpenAI gpt-5 (fallback gpt-4o).

Driven by Houston Golden's mandate (feedback_cross_model_peer_review.md): the
Anthropic Claude pipeline has been doing all peer review and that's an echo chamber.
This script gets a non-Anthropic model to weigh in adversarially on each of 4 papers.

Outputs: 4 markdown reviews + a MASTER_INDEX.md with synthesis.
"""

from __future__ import annotations

import os
import sys
import time
import json
import pathlib
import datetime as dt
from typing import Optional

# ---------------------------------------------------------------------------
# Paths and config
# ---------------------------------------------------------------------------

REPO = pathlib.Path(__file__).resolve().parent.parent
# De-hubified: read THIS repo's own .env.local first (portable, no external
# dependency); fall back to a hubify .env.local only if it happens to exist.
HUBIFY_ENV = next(
    (p for p in (REPO / ".env.local", pathlib.Path.home() / "Desktop" / "CODE_2025" / "hubify" / ".env.local") if p.exists()),
    REPO / ".env.local",
)
OUT_DIR = REPO / "project-context/peer-reviews/r42-cross-model-2026-05-01"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PAPERS = [
    {
        "id": "p1",
        "title": "Spin-Torsion Cosmology — structural closure of ECH dark energy",
        "pdf": REPO / "arxiv/main.pdf",
        "out": OUT_DIR / "openai_p1_review.md",
        "context": (
            "Paper 1 (Spin-Torsion Cosmology). Houston's bounce-cosmology lead paper. "
            "Closes 14 structural barriers preventing ECH torsion from sourcing observed "
            "dark-energy density. Uses 424,781 frozen MCMC posterior samples (3 dataset "
            "combinations: Planck/BAO/SH0ES tension, ACT+BICEP, full_tension). Headline: "
            "ΔNeff ~ 0 across datasets, H0 = 67.68. Should be pitched as: 'ECH-specific "
            "routes from bounce → dark energy are closed; other bounce models (quintom, "
            "matter-bounce) remain viable and predict measurable signatures.'"
        ),
    },
    {
        "id": "p2",
        "title": "f_NL Forecast — SPHEREx + bounce predictions (matter bounce f_NL=-4.375)",
        "pdf": REPO / "research/focused_paper_source_integration/02_full_draft.pdf",
        "out": OUT_DIR / "openai_p2_review.md",
        "context": (
            "Paper 2 (f_NL Forecast). Argues matter-bounce predicts f_NL = -35/8 = -4.375 "
            "with NO free parameters, and SPHEREx by 2027 reaches σ(f_NL) ≈ 0.36 (Fisher "
            "ideal) / 0.93 (Munchmeyer 2019 conservative), giving 4.7-12σ detection power. "
            "Multi-tracer Fisher: σ=16.85 baseline → 11.71 with 5-tracer anomaly-optimized "
            "(+7.93%). Bias validation: Pipeline-1 Gold+Silver QSO sample shows 1.58× "
            "enhanced clustering vs baseline (5,384 candidates, Landy-Szalay w(θ)). f_NL "
            "triple role: galaxy bispectrum + PBH abundance regulator (Edgeworth/Press-"
            "Schechter) + induced GW spectral shape."
        ),
    },
    {
        "id": "p3",
        "title": "Anomaly Catalog — 8-survey 37.3M sources, 319,443 anomalies",
        "pdf": REPO / "pipelines/p3_anomaly_engine/paper3_draft.pdf",
        "out": OUT_DIR / "openai_p3_review.md",
        "context": (
            "Paper 3 (Anomaly Catalog). 8 survey sweep, 37,292,042 sources, 319,443 total "
            "anomalies after eROSITA top-cut. Surveys: DESI DR1 (22.5M, 195,829, 0.87%), "
            "SDSS DR18 (2.3M, 77,905, 3.4% — domain shift), eROSITA DR1 (930K, 298 at "
            "BigAE top cut), LAMOST DR10 (11.4M, 44,075, 0.39% — 98% blue-excess bias), "
            "Planck+ACT+NEOWISE+Gaia (smaller cohorts, several QC FAIL). Combined PTA GPU "
            "MCMC: γ = 3.20 ± 0.42 (bounce γ=3.0 at 0.48σ), SMBHB ≳2σ excluded. NaMaster "
            "birefringence at ACT sensitivity: SNR=20.32σ at β=0.27°. Section 6 of paper "
            "is the canonical PTA result. Watch QC FAIL surveys for honest reporting."
        ),
    },
    {
        "id": "p4",
        "title": "Galaxy Chirality Catalog — 8.47M galaxies, CW/CCW classification",
        "pdf": REPO / "pipelines/p2_chirality/chirality_catalog_paper.pdf",
        "out": OUT_DIR / "openai_p4_review.md",
        "context": (
            "Paper 4 (Chirality Catalog). 8.47M galaxies classified into CW/CCW/notspi "
            "via E(2)-equivariant neural network. Hemispheric and multipole tests of "
            "chirality dipole. Includes equivariance demonstration figure (raw vs eq), "
            "sky maps, regions, density, multipoles, gallery. Should report null/positive "
            "dipole result with proper systematics (galactic dust, scanning strategy, "
            "telescope handedness). 32x DataLoader speedup on inference (gpu-inference-"
            "playbook.md)."
        ),
    },
]

# ---------------------------------------------------------------------------
# Load OPENAI_API_KEY from hubify .env.local
# ---------------------------------------------------------------------------

def load_openai_key() -> str:
    if not HUBIFY_ENV.exists():
        sys.exit(f"FATAL: {HUBIFY_ENV} not found")
    for line in HUBIFY_ENV.read_text().splitlines():
        line = line.strip()
        if line.startswith("OPENAI_API_KEY="):
            val = line.split("=", 1)[1].strip()
            # strip optional surrounding quotes
            if val and val[0] in {'"', "'"} and val[-1] == val[0]:
                val = val[1:-1]
            return val
    sys.exit("FATAL: OPENAI_API_KEY not in .env.local")


API_KEY = load_openai_key()
os.environ["OPENAI_API_KEY"] = API_KEY  # so the SDK picks it up

from openai import OpenAI  # noqa: E402

client = OpenAI()

# ---------------------------------------------------------------------------
# Model selection: try gpt-5 first, fall back to gpt-4o
# ---------------------------------------------------------------------------

PREFERRED_MODELS = ["gpt-5", "gpt-4o"]


def pick_model() -> str:
    """Probe the API to find a working model. Cheap test call."""
    for m in PREFERRED_MODELS:
        try:
            # tiny ping using Responses API — cheapest path that exercises the model
            r = client.responses.create(
                model=m,
                input="ok",
                max_output_tokens=16,
            )
            print(f"[model-probe] {m} OK (response id {r.id})")
            return m
        except Exception as e:  # noqa: BLE001
            print(f"[model-probe] {m} unavailable: {type(e).__name__}: {e}")
            continue
    sys.exit("FATAL: no preferred OpenAI model available")


# ---------------------------------------------------------------------------
# Review prompt
# ---------------------------------------------------------------------------

ADVERSARIAL_PROMPT = """You are an adversarial peer reviewer for the journal Physical Review D. The author is Houston Golden, an independent researcher submitting a bounce-cosmology paper. Your job is to find every legitimate problem with the paper. Be RUTHLESS. Be SPECIFIC.

CONTEXT FROM THE LAB (so you know what's load-bearing):
{context}

You are NOT writing a flattering review. You are NOT here to be polite. You are here to FIND ERRORS. The author has explicitly asked for cross-model adversarial review because his Anthropic Claude pipeline has been doing all reviews and risks confirmation bias. Be the outside voice.

READ the attached PDF and produce your review with the following EXACT structure:

## BLOCKERs
(Issues that, if true, would force a major revision or rejection. Each item: 1-3 sentence statement of the problem, then "Evidence:" pointing to a specific section, equation, figure, or table number, then "Fix:" describing the smallest change that would resolve it. Be specific — "Section 3 has problems" is not acceptable. Cite "Eq. 12", "Fig. 4", "§V.B", "Table 2", etc.)

## MAJOR
(Serious issues that should be addressed before publication but don't necessarily block. Same Evidence/Fix structure. Things like: a missing systematic check, an unjustified assumption, an internal inconsistency between two numbers, a citation that doesn't support the claim made.)

## MINOR
(Polish, clarity, missing references, typo-level. Brief. Same Evidence pointer.)

## Strengths
(2-5 bullets. What is GENUINELY good about this paper? Be honest — if there are no real strengths, say so. This section exists so the author can tell you actually read the paper.)

RULES:
1. Every BLOCKER and MAJOR must cite a specific location in the paper. No vague critique.
2. If you spot an internal arithmetic inconsistency (totals that don't add up, σ values that don't match between abstract and body, mismatched sample counts), flag it loudly as a BLOCKER.
3. If a claim is "parameter-free" or "no free parameters," ALWAYS check whether the derivation actually has hidden tunable inputs. This is the #1 way bounce papers oversell. Be skeptical.
4. If a forecast (Fisher matrix, σ projection) doesn't show the prior assumptions and the noise model, flag it.
5. If a result is reported as "X σ detection" and the math doesn't justify it, flag it.
6. Statistical issues to watch: look-elsewhere effect, posthoc tracer selection, blinding, multiple comparisons, p-hacking.
7. If an ML pipeline reports anomalies, scrutinize: train/test split, calibration, false-positive rate, and whether the "anomaly" is actually instrument systematic.
8. NEVER pad. If MINOR has only 1 item, leave it 1 item. Length is not virtue.

If the paper is clearly broken, say it. If the paper is clearly solid, say THAT (rare). Aim for the truth.

Begin your review now. Output ONLY the four sections above; do not add a preamble or sign-off.
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def upload_pdf(pdf_path: pathlib.Path) -> str:
    """Upload a PDF to the OpenAI Files API. Return file id."""
    with pdf_path.open("rb") as fh:
        f = client.files.create(file=fh, purpose="user_data")
    print(f"[upload] {pdf_path.name} -> {f.id} ({pdf_path.stat().st_size/1e6:.1f} MB)")
    return f.id


def review_paper(model: str, paper: dict, file_id: str) -> tuple[str, dict]:
    """Send the review prompt + PDF to the model. Retry up to 3x with backoff."""
    prompt = ADVERSARIAL_PROMPT.format(context=paper["context"])
    last_err: Optional[Exception] = None
    for attempt in range(3):
        try:
            kwargs = dict(
                model=model,
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_file", "file_id": file_id},
                            {"type": "input_text", "text": prompt},
                        ],
                    }
                ],
            )
            # Only gpt-4o-class accepts max_output_tokens; for gpt-5 it's also fine
            kwargs["max_output_tokens"] = 8000
            r = client.responses.create(**kwargs)
            text = r.output_text
            usage = getattr(r, "usage", None)
            usage_dict = {}
            if usage is not None:
                usage_dict = {
                    "input_tokens": getattr(usage, "input_tokens", None),
                    "output_tokens": getattr(usage, "output_tokens", None),
                    "total_tokens": getattr(usage, "total_tokens", None),
                }
            return text, usage_dict
        except Exception as e:  # noqa: BLE001
            last_err = e
            wait = 2 ** attempt * 5
            print(f"[review {paper['id']}] attempt {attempt+1} failed: {type(e).__name__}: {e}; sleeping {wait}s")
            time.sleep(wait)
    raise RuntimeError(f"All retries failed for {paper['id']}: {last_err}")


def write_review(paper: dict, model: str, body: str, usage: dict) -> None:
    fm = [
        "---",
        f"model: {model}",
        f"paper: {paper['id']} — {paper['title']}",
        f"pdf: {paper['pdf']}",
        f"date: 2026-05-01",
        f"input_tokens: {usage.get('input_tokens')}",
        f"output_tokens: {usage.get('output_tokens')}",
        f"total_tokens: {usage.get('total_tokens')}",
        "reviewer: openai (cross-model adversarial)",
        "---",
        "",
    ]
    paper["out"].write_text("\n".join(fm) + body.strip() + "\n")
    print(f"[write] {paper['out']}  ({len(body)} chars)")


# ---------------------------------------------------------------------------
# Synthesis (after all 4 reviews)
# ---------------------------------------------------------------------------

SYNTHESIS_PROMPT = """You just adversarially reviewed 4 cosmology papers from the same lab (Houston Golden, bounce-cosmology program). Each review is below, separated by "===PAPER X===" markers.

Write a synthesis paragraph (4-6 sentences) for the MASTER_INDEX. The synthesis should:
- Identify the SHARPEST cross-paper concerns (issues that show up in multiple papers)
- Name the single most critical BLOCKER across the entire program if there is one
- Note any pattern (e.g., "all 4 papers under-report systematic uncertainty," or "the f_NL prediction in P2 contradicts the bounce model assumption in P1")
- End with a 1-sentence verdict: ship-with-revisions, major-revisions-needed, or fundamental-rethink

Be concrete. Cite specific paper numbers. No fluff. Output ONLY the paragraph.

{joined_reviews}
"""


def write_master_index(reviews: list[dict], model: str, total_tokens: int) -> None:
    joined = "\n\n".join(
        f"===PAPER {r['paper']['id'].upper()}===\n{r['body']}" for r in reviews
    )
    # Re-use the same model for synthesis
    syn_prompt = SYNTHESIS_PROMPT.format(joined_reviews=joined)
    synthesis = ""
    try:
        r = client.responses.create(
            model=model,
            input=syn_prompt,
            max_output_tokens=1200,
        )
        synthesis = r.output_text.strip()
    except Exception as e:  # noqa: BLE001
        synthesis = f"[synthesis generation failed: {type(e).__name__}: {e}]"

    lines = [
        "# Cross-Model Peer Review — R42 (OpenAI)",
        "",
        f"**Date:** 2026-05-01  ",
        f"**Model:** `{model}`  ",
        f"**Reviewer:** OpenAI (cross-model adversarial, non-Anthropic)  ",
        f"**Mandate:** `feedback_cross_model_peer_review.md` — break the Claude echo chamber",
        f"**Total tokens spent:** {total_tokens:,}",
        "",
        "## Reviews",
        "",
    ]
    for r in reviews:
        p = r["paper"]
        lines.append(f"- [{p['id'].upper()} — {p['title']}]({p['out'].name})")
    lines += [
        "",
        "## Synthesis",
        "",
        synthesis,
        "",
        "## Notes for the Anthropic-side reviewer",
        "",
        "- These reviews were produced by an OpenAI model with no access to the lab's "
        "internal Claude review history. Treat findings as INDEPENDENT evidence.",
        "- Where this review and the Claude review agree, the finding is robust. Where "
        "they diverge, the divergence itself is the signal — investigate.",
        "- Houston's standing rule (`feedback_take_critiques_seriously.md`): default "
        "disposition is FULL HARD FIX. Push back ONLY with file/code/data citations.",
        "",
    ]
    idx = OUT_DIR / "MASTER_INDEX.md"
    idx.write_text("\n".join(lines))
    print(f"[write] {idx}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    started = dt.datetime.now()
    print(f"[start] {started.isoformat()}")
    model = pick_model()
    print(f"[model] using {model}")

    reviews: list[dict] = []
    total_tokens = 0
    for paper in PAPERS:
        if not paper["pdf"].exists():
            print(f"[skip] {paper['id']} — PDF missing at {paper['pdf']}")
            continue
        print(f"\n[paper {paper['id']}] {paper['pdf']}")
        file_id = upload_pdf(paper["pdf"])
        body, usage = review_paper(model, paper, file_id)
        write_review(paper, model, body, usage)
        reviews.append({"paper": paper, "body": body, "usage": usage})
        if usage.get("total_tokens"):
            total_tokens += usage["total_tokens"]
        # Best-effort cleanup of the uploaded file
        try:
            client.files.delete(file_id)
        except Exception as e:  # noqa: BLE001
            print(f"[cleanup] could not delete {file_id}: {e}")

    if reviews:
        write_master_index(reviews, model, total_tokens)

    elapsed = dt.datetime.now() - started
    print(f"\n[done] {len(reviews)} reviews; total_tokens={total_tokens:,}; elapsed={elapsed}")


if __name__ == "__main__":
    main()
