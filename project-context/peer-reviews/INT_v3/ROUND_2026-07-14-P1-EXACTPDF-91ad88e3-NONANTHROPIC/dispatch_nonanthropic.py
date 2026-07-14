#!/usr/bin/env python3
"""Dispatch the frozen P1 split PDFs to only OpenAI, Gemini, and xAI.

This round deliberately excludes Anthropic/Claude and Perplexity.  The Codex
subscription leg is run separately so its CLI transcript can be preserved.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
ROUND_ROOT = Path(__file__).resolve().parent
ROUND_LABEL = "P1EXACT91ad88e3"
COMMIT = "91ad88e36121da128175415f55be44d5e458f9f1"


def load_review_module():
    path = REPO / "tools" / "v3_native_pdf_review.py"
    spec = importlib.util.spec_from_file_location("v3_native_pdf_review", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    review = load_review_module()
    keys = review.load_keys()
    allowed = {
        name: cfg
        for name, cfg in review.REVIEWERS.items()
        if cfg["vendor"] in {"openai", "gemini", "xai"}
    }
    if {cfg["vendor"] for cfg in allowed.values()} != {"openai", "gemini", "xai"}:
        raise RuntimeError("authorized reviewer set is incomplete")
    if any(cfg["vendor"] in {"anthropic", "perplexity"} for cfg in allowed.values()):
        raise RuntimeError("forbidden provider entered authorized reviewer set")

    papers = {
        "P1A": {
            "pdf": ROUND_ROOT / "P1A" / "frozen" / "arxiv" / "paper1a_ech_nogo.pdf",
            "out": ROUND_ROOT / "P1A" / "raw",
            "context": (
                f"Fresh exact-PDF review of commit {COMMIT}, P1A v1A.0.116. "
                "The declared scope is the minimal Einstein-Cartan-Holst action, "
                "its axial contact term, a conditional standard-mean-field NJL check, "
                "and classical canonical-scalar transparency. R2/R3 cosmological "
                "matching and observational claims are explicitly not claimed."
            ),
        },
        "P1B": {
            "pdf": ROUND_ROOT / "P1B" / "frozen" / "arxiv" / "paper1b_mcmc_companion.pdf",
            "out": ROUND_ROOT / "P1B" / "raw",
            "context": (
                f"Fresh exact-PDF review of commit {COMMIT}, P1B v1B.0.105. "
                "The declared scope is a generic stock-CAMB extra-radiation proxy, "
                "foreground-free synthetic NaMaster recovery, and a generic spectator-ALP "
                "consistency/prior-volume study; none is claimed as ECH or bounce evidence."
            ),
        },
    }

    jobs = []
    for paper_tag, paper in papers.items():
        pdf_path = paper["pdf"]
        out_dir = paper["out"]
        out_dir.mkdir(parents=True, exist_ok=True)
        page_count = review.get_page_count(pdf_path)
        paper_text = review.extract_pdf_text(pdf_path)
        for name, cfg in allowed.items():
            prompt = review.REVIEW_PROMPT_TEMPLATE.format(
                persona=cfg["persona"],
                paper_tag=paper_tag,
                round_label=ROUND_LABEL,
                round_context=paper["context"],
                page_count=page_count,
                focus=cfg["focus"],
            )
            (out_dir / f"PROMPT_{name}.txt").write_text(prompt)
            jobs.append((paper_tag, paper, paper_text, name, cfg, prompt))

    results = []
    with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
        futures = {
            pool.submit(
                review.run_reviewer,
                name,
                cfg,
                prompt,
                paper["pdf"],
                paper_text,
                ROUND_LABEL,
                paper_tag,
                keys,
                paper["out"],
                True,
            ): (paper_tag, name)
            for paper_tag, paper, paper_text, name, cfg, prompt in jobs
        }
        for future in as_completed(futures):
            paper_tag, name = futures[future]
            result = future.result()
            result["paper"] = paper_tag
            results.append(result)
            print(
                f"[{paper_tag}/{name}] ok={result['ok']} model={result['model']} "
                f"fallback={result['fallback']} duration={result['duration_s']:.1f}s",
                flush=True,
            )

    summary = {
        "round": ROUND_LABEL,
        "commit": COMMIT,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "provider_policy": {
            "allowed": ["openai", "gemini", "xai"],
            "forbidden": ["anthropic", "perplexity"],
            "codex_subscription": "separate CLI leg",
        },
        "results": sorted(results, key=lambda row: (row["paper"], row["name"])),
    }
    (ROUND_ROOT / "API_DISPATCH_RESULTS.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    ok = sum(bool(row["ok"]) for row in results)
    print(f"complete: {ok}/{len(results)} authorized API legs succeeded", flush=True)
    return 0 if ok == len(results) else 2


if __name__ == "__main__":
    sys.exit(main())
