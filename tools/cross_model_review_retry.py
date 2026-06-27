#!/usr/bin/env python3
"""
Retry-only script for the two papers (P1, P4) that came back empty on first run.

Root cause: gpt-5 is a reasoning model. With max_output_tokens=8000, the model
spent the entire budget on hidden reasoning tokens and produced 0 visible text.
This run bumps max_output_tokens to 32000 and lowers reasoning effort to "medium"
so visible output isn't starved.
"""

from __future__ import annotations
import os
import sys
import time
import pathlib
import datetime as dt
from typing import Optional

# Reuse the main script's PAPERS + helpers
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from cross_model_review_openai import (  # noqa: E402
    PAPERS,
    OUT_DIR,
    ADVERSARIAL_PROMPT,
    load_openai_key,
)

API_KEY = load_openai_key()
os.environ["OPENAI_API_KEY"] = API_KEY
from openai import OpenAI  # noqa: E402

client = OpenAI()
MODEL = "gpt-5"


def upload_pdf(pdf_path: pathlib.Path) -> str:
    with pdf_path.open("rb") as fh:
        f = client.files.create(file=fh, purpose="user_data")
    print(f"[upload] {pdf_path.name} -> {f.id} ({pdf_path.stat().st_size/1e6:.1f} MB)")
    return f.id


def review_paper(paper: dict, file_id: str) -> tuple[str, dict]:
    prompt = ADVERSARIAL_PROMPT.format(context=paper["context"])
    last_err: Optional[Exception] = None
    for attempt in range(3):
        try:
            r = client.responses.create(
                model=MODEL,
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_file", "file_id": file_id},
                            {"type": "input_text", "text": prompt},
                        ],
                    }
                ],
                max_output_tokens=32000,
                reasoning={"effort": "medium"},
            )
            text = r.output_text
            usage = getattr(r, "usage", None)
            usage_dict = {}
            if usage is not None:
                usage_dict = {
                    "input_tokens": getattr(usage, "input_tokens", None),
                    "output_tokens": getattr(usage, "output_tokens", None),
                    "total_tokens": getattr(usage, "total_tokens", None),
                }
            if not text.strip():
                # Still empty — try to inspect
                print(f"[warn] empty output_text on attempt {attempt+1}; usage={usage_dict}")
                # Try to surface any structured output
                print(f"[debug] response.output (first 500 chars): {str(r.output)[:500]}")
                raise RuntimeError("empty model response")
            return text, usage_dict
        except Exception as e:  # noqa: BLE001
            last_err = e
            wait = 2 ** attempt * 5
            print(f"[review {paper['id']}] attempt {attempt+1} failed: {type(e).__name__}: {e}; sleeping {wait}s")
            time.sleep(wait)
    raise RuntimeError(f"All retries failed for {paper['id']}: {last_err}")


def write_review(paper: dict, body: str, usage: dict) -> None:
    fm = [
        "---",
        f"model: {MODEL}",
        f"paper: {paper['id']} — {paper['title']}",
        f"pdf: {paper['pdf']}",
        "date: 2026-05-01",
        f"input_tokens: {usage.get('input_tokens')}",
        f"output_tokens: {usage.get('output_tokens')}",
        f"total_tokens: {usage.get('total_tokens')}",
        "reviewer: openai (cross-model adversarial)",
        "retry: true (reasoning=medium, max_output=32000)",
        "---",
        "",
    ]
    paper["out"].write_text("\n".join(fm) + body.strip() + "\n")
    print(f"[write] {paper['out']}  ({len(body)} chars)")


def main() -> None:
    target_ids = {"p1", "p4"}
    started = dt.datetime.now()
    print(f"[start] {started.isoformat()}")
    total_tokens = 0
    for paper in PAPERS:
        if paper["id"] not in target_ids:
            continue
        print(f"\n[paper {paper['id']}] {paper['pdf']}")
        file_id = upload_pdf(paper["pdf"])
        body, usage = review_paper(paper, file_id)
        write_review(paper, body, usage)
        if usage.get("total_tokens"):
            total_tokens += usage["total_tokens"]
        try:
            client.files.delete(file_id)
        except Exception as e:  # noqa: BLE001
            print(f"[cleanup] could not delete {file_id}: {e}")
    elapsed = dt.datetime.now() - started
    print(f"\n[done] retry total_tokens={total_tokens:,}; elapsed={elapsed}")


if __name__ == "__main__":
    main()
