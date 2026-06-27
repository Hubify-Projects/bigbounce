#!/usr/bin/env python3
"""Regenerate MASTER_INDEX.md after all 4 reviews are present."""

from __future__ import annotations
import os
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from cross_model_review_openai import PAPERS, OUT_DIR, SYNTHESIS_PROMPT, load_openai_key  # noqa: E402

API_KEY = load_openai_key()
os.environ["OPENAI_API_KEY"] = API_KEY
from openai import OpenAI  # noqa: E402

client = OpenAI()
MODEL = "gpt-5"


def strip_frontmatter(md: str) -> str:
    """Drop the YAML frontmatter from a saved review file."""
    lines = md.splitlines()
    if lines and lines[0].strip() == "---":
        # find closing fence
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[i + 1 :]).lstrip("\n")
    return md


def main() -> None:
    reviews = []
    for p in PAPERS:
        body = strip_frontmatter(p["out"].read_text())
        if not body.strip():
            print(f"[warn] {p['out']} is empty, skipping in synthesis")
            continue
        reviews.append({"paper": p, "body": body})

    joined = "\n\n".join(
        f"===PAPER {r['paper']['id'].upper()}===\n{r['body']}" for r in reviews
    )
    syn_prompt = SYNTHESIS_PROMPT.format(joined_reviews=joined)

    r = client.responses.create(
        model=MODEL,
        input=syn_prompt,
        max_output_tokens=8000,
        reasoning={"effort": "medium"},
    )
    synthesis = r.output_text.strip()
    if not synthesis:
        synthesis = "[synthesis empty]"

    usage = getattr(r, "usage", None)
    syn_tokens = getattr(usage, "total_tokens", 0) if usage else 0

    # First-run total + retry total + this synthesis call
    total_tokens = 183266 + 99028 + syn_tokens

    lines = [
        "# Cross-Model Peer Review — R42 (OpenAI)",
        "",
        "**Date:** 2026-05-01  ",
        f"**Model:** `{MODEL}`  ",
        "**Reviewer:** OpenAI (cross-model adversarial, non-Anthropic)  ",
        "**Mandate:** `feedback_cross_model_peer_review.md` — break the Claude echo chamber  ",
        f"**Total tokens spent:** {total_tokens:,}  ",
        "**Run notes:** P1+P4 needed a retry with `reasoning=medium` + `max_output=32000` "
        "(gpt-5 is a reasoning model; default budget went entirely to hidden reasoning).",
        "",
        "## Reviews",
        "",
    ]
    for r2 in reviews:
        p = r2["paper"]
        lines.append(f"- **{p['id'].upper()}** — {p['title']}: [`{p['out'].name}`]({p['out'].name})")
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
    print(f"[write] {idx} ({len(synthesis)} chars synthesis, +{syn_tokens} tokens)")


if __name__ == "__main__":
    main()
