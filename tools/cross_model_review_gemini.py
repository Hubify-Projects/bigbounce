"""
Cross-model peer review of R42 cosmology papers using Google Gemini.

Reviews 4 papers (P1 spin-torsion, P2 f_NL forecast, P3 anomaly catalog,
P4 chirality catalog) and writes verbatim adversarial findings to
project-context/peer-reviews/r42-cross-model-2026-05-01/.

Mandatory per feedback_cross_model_peer_review.md (no Anthropic echo chamber).

Usage:
    python3 tools/cross_model_review_gemini.py
"""

from __future__ import annotations

import os
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
# De-hubified: read THIS repo's own .env.local first (portable, no external
# dependency); fall back to a hubify .env.local only if it happens to exist.
ENV_FILE = next(
    (p for p in (REPO_ROOT / ".env.local", Path.home() / "Desktop" / "CODE_2025" / "hubify" / ".env.local") if p.exists()),
    REPO_ROOT / ".env.local",
)
OUT_DIR = REPO_ROOT / "project-context" / "peer-reviews" / "r42-cross-model-2026-05-01"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Model fallback chain. The originally requested gemini-2.0-pro-exp / gemini-1.5-pro
# names are 404 on the v1beta API for this key as of 2026-04-30, so we fall through
# the actually-available Pro tier models discovered via list_models().
MODEL_FALLBACK_CHAIN = [
    "gemini-3.1-pro-preview",
    "gemini-3-pro-preview",
    "gemini-pro-latest",
    "gemini-2.5-pro",
    "gemini-2.0-flash",
    "gemini-2.5-flash",
]

PAPERS = [
    {
        "id": "p1",
        "title": "Spin-Torsion Cosmology (Paper 1)",
        "pdf": REPO_ROOT / "arxiv" / "main.pdf",
        "out": OUT_DIR / "gemini_p1_review.md",
        "context": (
            "Paper 1: Spin-torsion (Einstein-Cartan-Holst, ECH) cosmology. "
            "Key claims: 14 structural barriers close ECH-specific dark energy routes; "
            "ALP birefringence prediction beta ~ 0.27 deg vs observed 0.342 +/- 0.094 deg; "
            "Branch V matter bounce f_NL = -35/8 = -4.375; "
            "424,781 frozen MCMC posterior samples across 3 dataset combinations; "
            "Delta N_eff ~ 0; H_0 = 67.68. The paper uses revtex4-2 PRD style."
        ),
    },
    {
        "id": "p2",
        "title": "f_NL Forecast (Paper 2)",
        "pdf": REPO_ROOT / "research" / "focused_paper_source_integration" / "02_full_draft.pdf",
        "out": OUT_DIR / "gemini_p2_review.md",
        "context": (
            "Paper 2: SPHEREx f_NL Fisher forecast for matter-bounce prediction f_NL = -4.375. "
            "Key numbers: sigma(f_NL) = 16.85 baseline -> 12.72 standard multi-tracer -> "
            "11.71 5-tracer (anomaly-optimized). 4.7-12 sigma SPHEREx detection by 2027. "
            "Pipeline 1 Gold+Silver tracers show 1.58x enhanced clustering bias on "
            "5,384 QSO candidates (Landy-Szalay w(theta))."
        ),
    },
    {
        "id": "p3",
        "title": "Multi-Survey Anomaly Catalog (Paper 3)",
        "pdf": REPO_ROOT / "pipelines" / "p3_anomaly_engine" / "paper3_draft.pdf",
        "out": OUT_DIR / "gemini_p3_review.md",
        "context": (
            "Paper 3: 8-survey anomaly sweep, 37,292,042 sources -> 319,443 anomalies. "
            "Surveys: DESI DR1 (22.5M, 195,829 anomalies), SDSS DR18 (2.3M, 77,905), "
            "eROSITA DR1 (930K, 298 BigAE top-cut), LAMOST DR10 (11.4M, 44,075), "
            "Planck CMB / ACT DR6 / NEOWISE / Gaia DR3 (some QC failures noted). "
            "Combined PTA GPU MCMC: gamma = 3.20 +/- 0.42 (P1 bounce gamma=3.0 at 0.48 sigma; "
            "SMBHB excluded at >~ 2 sigma)."
        ),
    },
    {
        "id": "p4",
        "title": "Galaxy Chirality Catalog (Paper 4)",
        "pdf": REPO_ROOT / "pipelines" / "p2_chirality" / "chirality_catalog_paper.pdf",
        "out": OUT_DIR / "gemini_p4_review.md",
        "context": (
            "Paper 4: Equivariant CNN galaxy chirality catalog over 8.47M galaxies. "
            "Outputs: per-galaxy CW/CCW/not-spiral classification + confidence + "
            "sky-region maps + multipole analysis. Companion to spin-torsion papers; "
            "feeds large-scale chirality alignment tests."
        ),
    },
]


REVIEW_PROMPT_TEMPLATE = """You are a senior independent referee reviewing a cosmology / astrophysics paper for the Physical Review D adversarial peer-review queue. The author is bounce-model-agnostic and explicitly wants HARD CRITICISM, not encouragement. Your loyalty is to the literature, not the author.

PAPER: {title}
CONTEXT FROM AUTHOR (use only as ground-truth for what the paper claims to say; verify against the PDF):
{context}

YOUR JOB: Adversarial review. The author is using you specifically because they have been getting Anthropic-Claude reviews and worry about an LLM echo chamber. Push back. Find what Claude would miss.

Required output structure (markdown, no preamble, no marketing language):

## Summary verdict
ONE sentence: ACCEPT / MINOR REVISION / MAJOR REVISION / REJECT, plus a one-line justification.

## BLOCKERS (paper cannot ship as-is)
For each blocker:
- **B-N**: <one-line title>
- Section / equation / figure citation: <exact pointer, e.g. "Sec. III.B, Eq. 14" or "Fig. 7 caption">
- Defect: <what is wrong, in 2-4 sentences>
- What would fix it: <concrete remediation>

## MAJOR concerns (must address before resubmission)
Same format as BLOCKERS, prefix M-N.

## MINOR concerns (should fix, won't block)
Same format, prefix m-N. Brief.

## Statistics / methodology audit
Bullet list. Specifically interrogate:
- Is the chosen statistic (sigma, p-value, AUC, Bayes factor) the right one for the claim?
- Are error bars frequentist, Bayesian, or hybrid? Are they consistent across the paper?
- Are look-elsewhere / multiple-comparison corrections applied where needed?
- Are MCMC convergence diagnostics (R-hat, ESS, autocorrelation) reported and adequate?
- Are systematic uncertainties quantified or just hand-waved?
- Are claimed detection significances reproducible from the reported numbers?

## Cosmology / physics sanity check
Bullet list. Cross-check against known constraints (Planck 2018, ACT DR6, DESI BAO, NANOGrav 15yr,
PTA bounds, BBN, recombination physics, etc.). Flag any claim that conflicts with established
results without explicit reconciliation.

## Reproducibility
- Are data products, code, and chains actually published or just promised?
- Could a competent grad student reproduce the headline numbers from what the paper provides?
- Are software versions, random seeds, and pipeline configs pinned?

## What an Anthropic-Claude review would have missed
2-5 bullets. Be specific. Where does Claude's training distribution / sycophancy bias
likely hide a problem in this paper that you, Gemini, can see?

## Bottom line for the author
3-5 sentences. Direct, no hedging. What is the single highest-leverage fix?

Cite sections, equations, figures, and table numbers EXACTLY as they appear in the PDF.
Do not invent citations. If the PDF is too short or compiles failed, say so explicitly
in the Summary verdict and stop.
"""


def load_api_key() -> str:
    if not ENV_FILE.exists():
        raise SystemExit(f"env file not found: {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("GEMINI_API_KEY="):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            if value:
                return value
    raise SystemExit("GEMINI_API_KEY not found in env file")


def pick_model(api_key: str) -> str:
    """Return the first model in MODEL_FALLBACK_CHAIN that responds successfully."""
    genai.configure(api_key=api_key)
    last_err: Exception | None = None
    for model_name in MODEL_FALLBACK_CHAIN:
        try:
            model = genai.GenerativeModel(model_name)
            # Cheap probe — single short prompt, no PDF.
            resp = model.generate_content("Reply with the single word: ready")
            text = (getattr(resp, "text", "") or "").strip().lower()
            if "ready" in text or text:  # any non-empty response means model is alive
                print(f"[model] using {model_name}", flush=True)
                return model_name
        except Exception as exc:  # noqa: BLE001
            print(f"[model] {model_name} unavailable: {exc}", flush=True)
            last_err = exc
            continue
    raise SystemExit(f"no Gemini model available; last error: {last_err}")


def review_paper(model_name: str, paper: dict, max_attempts: int = 3) -> dict:
    """Upload PDF and run review prompt. Returns dict with text + token usage."""
    pdf_path = paper["pdf"]
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    prompt = REVIEW_PROMPT_TEMPLATE.format(title=paper["title"], context=paper["context"])

    last_err: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"[{paper['id']}] attempt {attempt}: uploading {pdf_path.name} ({pdf_path.stat().st_size/1e6:.1f} MB)", flush=True)
            uploaded = genai.upload_file(path=str(pdf_path), mime_type="application/pdf")
            # Wait for ACTIVE state.
            for _ in range(30):
                f = genai.get_file(uploaded.name)
                if f.state.name == "ACTIVE":
                    uploaded = f
                    break
                if f.state.name == "FAILED":
                    raise RuntimeError(f"upload failed: {f}")
                time.sleep(2)
            else:
                raise RuntimeError("upload did not reach ACTIVE within 60s")

            print(f"[{paper['id']}] uploaded; running review", flush=True)
            model = genai.GenerativeModel(model_name)
            resp = model.generate_content(
                [prompt, uploaded],
                generation_config={"temperature": 0.3, "max_output_tokens": 8192},
            )
            text = getattr(resp, "text", "") or ""
            usage = getattr(resp, "usage_metadata", None)
            tokens = {
                "prompt_tokens": getattr(usage, "prompt_token_count", None) if usage else None,
                "completion_tokens": getattr(usage, "candidates_token_count", None) if usage else None,
                "total_tokens": getattr(usage, "total_token_count", None) if usage else None,
            }
            # Best-effort cleanup of the uploaded file (Gemini auto-expires after 48h, this is just hygiene).
            try:
                genai.delete_file(uploaded.name)
            except Exception:  # noqa: BLE001
                pass

            if not text.strip():
                raise RuntimeError("empty response text")
            return {"text": text, "tokens": tokens}
        except Exception as exc:  # noqa: BLE001
            print(f"[{paper['id']}] attempt {attempt} failed: {exc}", flush=True)
            last_err = exc
            time.sleep(5 * attempt)

    raise RuntimeError(f"all {max_attempts} attempts failed for {paper['id']}: {last_err}")


def write_review(paper: dict, model_name: str, result: dict) -> None:
    tokens = result["tokens"]
    frontmatter = (
        "---\n"
        f"model: {model_name}\n"
        f"paper: {paper['id']}\n"
        f"paper_title: {paper['title']}\n"
        f"pdf_path: {paper['pdf']}\n"
        f"date: 2026-05-01\n"
        f"prompt_tokens: {tokens.get('prompt_tokens')}\n"
        f"completion_tokens: {tokens.get('completion_tokens')}\n"
        f"total_tokens: {tokens.get('total_tokens')}\n"
        "review_type: cross-model adversarial peer review\n"
        "reviewer: Google Gemini (cross-model check vs Anthropic Claude pipeline)\n"
        "---\n\n"
    )
    paper["out"].write_text(frontmatter + result["text"].strip() + "\n")
    print(f"[{paper['id']}] wrote {paper['out']} ({len(result['text'])} chars)", flush=True)


def main() -> int:
    print(
        "ERROR: cross_model_review_gemini.py is retired; use tools/int_wave.sh "
        "with the canonical PDF packet and portfolio preflight",
        file=sys.stderr,
    )
    return 2
    api_key = load_api_key()
    model_name = pick_model(api_key)

    totals = {"prompt": 0, "completion": 0, "total": 0}
    failures: list[str] = []

    for paper in PAPERS:
        try:
            result = review_paper(model_name, paper)
            write_review(paper, model_name, result)
            t = result["tokens"]
            for src_key, dst_key in (
                ("prompt_tokens", "prompt"),
                ("completion_tokens", "completion"),
                ("total_tokens", "total"),
            ):
                v = t.get(src_key) or 0
                totals[dst_key] += v
        except Exception as exc:  # noqa: BLE001
            print(f"[{paper['id']}] FAILED: {exc}", flush=True)
            failures.append(paper["id"])

    print("\n=== summary ===", flush=True)
    print(f"model: {model_name}", flush=True)
    print(f"prompt tokens: {totals['prompt']}", flush=True)
    print(f"completion tokens: {totals['completion']}", flush=True)
    print(f"total tokens: {totals['total']}", flush=True)
    if failures:
        print(f"FAILED: {failures}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
