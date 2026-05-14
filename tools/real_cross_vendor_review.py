#!/usr/bin/env python3
"""
Real cross-vendor adversarial peer review via OpenRouter.

Replaces the prior Claude-multi-persona simulation with actual API calls to
GPT / Gemini / Grok / Perplexity / DeepSeek through OpenRouter's unified
OpenAI-compatible chat-completions endpoint.

Usage:
    python tools/real_cross_vendor_review.py <paper_tex_path> <round_label>

Reads OPENROUTER_API_KEY from .env.local. Saves per-reviewer findings to
project-context/peer-reviews/<round_label>_<reviewer>.md.
"""
from __future__ import annotations

import json
import os
import re
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
ENV_LOCAL = REPO / ".env.local"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# 5 real frontier models from different vendors, mapped to the project's
# 5 reviewer personas. Models chosen for tier + variety.
REVIEWERS = {
    "GPT5_methodology": {
        "model": "openai/gpt-5.5",
        "persona": "GPT-5 methodology reviewer",
        "focus": (
            "Methodology rigor: derivations, dimensional analysis, statistical-method "
            "scrutiny, internal arithmetic consistency. Flag overclaim of statistical "
            "significance. Check that error bars propagate correctly through the "
            "systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing "
            "for proper marginalization vs parameter-shift."
        ),
    },
    "Gemini25Pro_cosmology": {
        "model": "google/gemini-2.5-pro",
        "persona": "Gemini-2.5-Pro cosmology-physics reviewer",
        "focus": (
            "Theoretical physics: gauge-frame vs physical-frame distinctions, GR "
            "projection effects, model-class scope boundaries, EFT counting, "
            "consistency-relation applicability. Flag any 'mechanism-independent' "
            "claim that overstates UV-completion independence. Check parity-violation "
            "/ ALP / Chern-Simons references against standard reviews."
        ),
    },
    "Grok4_brutal": {
        "model": "x-ai/grok-4",
        "persona": "Grok-4 brutal-honesty reviewer",
        "focus": (
            "Cut through narrative inflation. Flag overclaim, false confidence, "
            "headline numbers that aren't load-bearing, anything written to dodge a "
            "reviewer rather than to be true. Is the central claim actually new? "
            "Are 'first', 'novel', 'unprecedented' framings honest given the actual "
            "literature?"
        ),
    },
    "PerplexitySonarPro_citations": {
        "model": "perplexity/sonar-pro-search",
        "persona": "Perplexity Sonar Pro citation-chain forensic auditor",
        "focus": (
            "Citation forensics — does each cited paper actually say what's claimed? "
            "Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are "
            "authors and journal venues correct? Use web search to verify against "
            "arXiv.org / ADS / publisher sites. Flag any fused metadata "
            "(title from one paper + arXiv ID from another)."
        ),
    },
    "DeepSeekV32_confab": {
        "model": "deepseek/deepseek-v3.2",
        "persona": "DeepSeek-V3.2 confabulation-hunter",
        "focus": (
            "Paranoid about numbers without traceable sources. For every load-bearing "
            "scalar in the abstract and conclusions, ask: is there a JSON/script/dataset "
            "on disk that produces this number? Flag headline figures with no provenance "
            "and arithmetic that can't be reproduced from displayed values."
        ),
    },
}


def load_api_key() -> str:
    text = ENV_LOCAL.read_text()
    for line in text.splitlines():
        if line.startswith("OPENROUTER_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("OPENROUTER_API_KEY not found in .env.local")


def build_prompt(paper_text: str, persona: str, focus: str, round_context: str) -> str:
    return f"""You are a {persona} doing an adversarial peer review of a cosmology paper.

ROUND CONTEXT: {round_context}

YOUR FOCUS:
{focus}

YOUR TASK:
1. Read the paper below in full.
2. Return AT MOST 6 findings, each classified BLOCKER / MAJOR / minor / nit.
3. For each finding give: ID (e.g. PAPER-{persona[:3].upper()}-B1), line number or section, concrete issue, 1-2 sentence fix.
4. Be terse. No padding. No diplomatic softening. If you find nothing blocker-grade, say so.
5. Output as a markdown file with H2 sections per finding.

PAPER TEXT (LaTeX source follows):

```latex
{paper_text}
```

Return your full review as markdown."""


def call_openrouter(api_key: str, model: str, prompt: str, max_tokens: int = 8000, timeout: int = 240) -> dict:
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode("utf-8")
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://bigbounce.hubify.app",
            "X-Title": "BigBounce-cross-vendor-review",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"error": {"status": e.code, "body": body}}
    except Exception as e:
        return {"error": {"exception": repr(e)}}


def run_reviewer(name: str, cfg: dict, paper_text: str, round_label: str, paper_tag: str, round_context: str, api_key: str, out_dir: Path) -> dict:
    persona = cfg["persona"]
    prompt = build_prompt(paper_text, persona, cfg["focus"], round_context)
    t0 = time.time()
    result = call_openrouter(api_key, cfg["model"], prompt)
    dt = time.time() - t0

    out_path = out_dir / f"{round_label}_{paper_tag}_R-round_real_{name}.md"
    header = (
        f"# {paper_tag} R-round — REAL cross-vendor — {persona}\n\n"
        f"**Model**: `{cfg['model']}` (via OpenRouter)\n"
        f"**Round**: {round_label}\n"
        f"**Wall time**: {dt:.1f}s\n"
        f"**Persona focus**: {cfg['focus']}\n\n"
        f"---\n\n"
    )

    if "error" in result:
        body = f"## Reviewer call failed\n\n```json\n{json.dumps(result['error'], indent=2)[:4000]}\n```\n"
    else:
        try:
            content = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            body = (
                f"**Tokens**: prompt={usage.get('prompt_tokens', '?')}, "
                f"completion={usage.get('completion_tokens', '?')}, "
                f"total={usage.get('total_tokens', '?')}\n\n---\n\n{content}\n"
            )
        except Exception as e:
            body = f"## Parse failure\n\n```json\n{json.dumps(result, indent=2)[:4000]}\n```\n\n`{repr(e)}`\n"

    out_path.write_text(header + body)
    return {"name": name, "model": cfg["model"], "duration_s": dt, "out": str(out_path), "ok": "error" not in result}


def main() -> int:
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <paper_tex_path> <round_label> <paper_tag> [round_context]", file=sys.stderr)
        return 1
    tex_path = Path(sys.argv[1])
    round_label = sys.argv[2]  # e.g. 2026-05-14_1100pt
    paper_tag = sys.argv[3]    # e.g. P1A
    round_context = sys.argv[4] if len(sys.argv) >= 5 else "Cross-vendor adversarial peer-review round."

    api_key = load_api_key()
    paper_text = tex_path.read_text()
    out_dir = REPO / "project-context" / "peer-reviews"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[real-xreview] {paper_tag} — {len(paper_text)} chars — dispatching {len(REVIEWERS)} reviewers in parallel", flush=True)

    results = []
    with ThreadPoolExecutor(max_workers=len(REVIEWERS)) as pool:
        futures = {
            pool.submit(run_reviewer, name, cfg, paper_text, round_label, paper_tag, round_context, api_key, out_dir): name
            for name, cfg in REVIEWERS.items()
        }
        for fut in as_completed(futures):
            res = fut.result()
            status = "OK " if res["ok"] else "FAIL"
            print(f"[{status}] {res['name']:30s} {res['model']:40s} {res['duration_s']:6.1f}s → {res['out']}", flush=True)
            results.append(res)

    ok_count = sum(1 for r in results if r["ok"])
    print(f"\n[real-xreview] done: {ok_count}/{len(results)} reviewers landed", flush=True)
    return 0 if ok_count else 2


if __name__ == "__main__":
    sys.exit(main())
