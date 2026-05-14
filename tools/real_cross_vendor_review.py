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
#
# "model" is the preferred (latest, highest-tier) model ID; "fallback" is
# used if OpenRouter returns 404 / model_not_found for the preferred one.
# "reasoning_effort" enables higher-budget thinking on supported models
# (OpenAI o-series-style, Gemini thinking, Grok reasoning, DeepSeek R1).
# Perplexity Sonar's web-search-augmented role doesn't benefit from
# explicit reasoning effort.
REVIEWERS = {
    "GPT5_methodology": {
        "model": "openai/gpt-5.5",
        "fallback": "openai/gpt-5.5",
        "reasoning_effort": "high",
        "persona": "GPT-5 methodology reviewer",
        "focus": (
            "Methodology rigor: derivations, dimensional analysis, statistical-method "
            "scrutiny, internal arithmetic consistency. Flag overclaim of statistical "
            "significance. Check that error bars propagate correctly through the "
            "systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing "
            "for proper marginalization vs parameter-shift."
        ),
    },
    "Gemini31Pro_cosmology": {
        "model": "google/gemini-3.1-pro-preview",
        "fallback": "google/gemini-2.5-pro",
        "reasoning_effort": "high",
        "persona": "Gemini-3.1-Pro cosmology-physics reviewer",
        "focus": (
            "Theoretical physics: gauge-frame vs physical-frame distinctions, GR "
            "projection effects, model-class scope boundaries, EFT counting, "
            "consistency-relation applicability. Flag any 'mechanism-independent' "
            "claim that overstates UV-completion independence. Check parity-violation "
            "/ ALP / Chern-Simons references against standard reviews."
        ),
    },
    "Grok43_brutal": {
        "model": "x-ai/grok-4.3",
        "fallback": "x-ai/grok-4",
        "reasoning_effort": "high",
        "persona": "Grok-4.3 brutal-honesty reviewer",
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
        "fallback": "perplexity/sonar-pro-search",
        # No reasoning_effort: Sonar's web-search augmentation does the work.
        "persona": "Perplexity Sonar Pro citation-chain forensic auditor",
        "focus": (
            "Citation forensics — does each cited paper actually say what's claimed? "
            "Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are "
            "authors and journal venues correct? Use web search to verify against "
            "arXiv.org / ADS / publisher sites. Flag any fused metadata "
            "(title from one paper + arXiv ID from another)."
        ),
    },
    "DeepSeekV4Pro_confab": {
        "model": "deepseek/deepseek-v4-pro",
        "fallback": "deepseek/deepseek-r1",
        "reasoning_effort": "high",
        "persona": "DeepSeek-V4-Pro confabulation-hunter (reasoning mode)",
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


def call_openrouter(api_key: str, model: str, prompt: str, max_tokens: int = 16000, timeout: int = 360, reasoning_effort: str | None = None) -> dict:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }
    if reasoning_effort:
        # OpenRouter normalizes the reasoning-effort field across vendors:
        # OpenAI o-series, Gemini thinking-mode, Grok reasoning, DeepSeek R1.
        # See https://openrouter.ai/docs/use-cases/reasoning-tokens
        payload["reasoning"] = {"effort": reasoning_effort}
    body = json.dumps(payload).encode("utf-8")
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


def call_with_fallback(api_key: str, primary: str, fallback: str, prompt: str, reasoning_effort: str | None = None) -> tuple[dict, str]:
    """Try primary model; on 404/model_not_found, fall back. Returns (result, model_used)."""
    res = call_openrouter(api_key, primary, prompt, reasoning_effort=reasoning_effort)
    if "error" in res:
        err_body = (res["error"].get("body") or "").lower()
        status = res["error"].get("status")
        is_model_missing = status == 404 or "model" in err_body and ("not found" in err_body or "no allowed providers" in err_body or "no endpoints" in err_body)
        if is_model_missing and fallback and fallback != primary:
            res2 = call_openrouter(api_key, fallback, prompt, reasoning_effort=reasoning_effort)
            return res2, fallback
    return res, primary


def run_reviewer(name: str, cfg: dict, paper_text: str, round_label: str, paper_tag: str, round_context: str, api_key: str, out_dir: Path) -> dict:
    persona = cfg["persona"]
    prompt = build_prompt(paper_text, persona, cfg["focus"], round_context)
    t0 = time.time()
    result, model_used = call_with_fallback(
        api_key,
        primary=cfg["model"],
        fallback=cfg.get("fallback", cfg["model"]),
        prompt=prompt,
        reasoning_effort=cfg.get("reasoning_effort"),
    )
    dt = time.time() - t0

    out_path = out_dir / f"{round_label}_{paper_tag}_R-round_real_{name}.md"
    fallback_note = ""
    if model_used != cfg["model"]:
        fallback_note = f" (FALLBACK from `{cfg['model']}` — primary unavailable)"
    reasoning_note = ""
    if cfg.get("reasoning_effort"):
        reasoning_note = f"\n**Reasoning effort**: `{cfg['reasoning_effort']}`"
    header = (
        f"# {paper_tag} R-round — REAL cross-vendor — {persona}\n\n"
        f"**Model**: `{model_used}`{fallback_note} (via OpenRouter){reasoning_note}\n"
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
            reasoning_tokens = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0) if isinstance(usage.get("completion_tokens_details"), dict) else 0
            reasoning_line = f", reasoning={reasoning_tokens}" if reasoning_tokens else ""
            body = (
                f"**Tokens**: prompt={usage.get('prompt_tokens', '?')}, "
                f"completion={usage.get('completion_tokens', '?')}{reasoning_line}, "
                f"total={usage.get('total_tokens', '?')}\n\n---\n\n{content}\n"
            )
        except Exception as e:
            body = f"## Parse failure\n\n```json\n{json.dumps(result, indent=2)[:4000]}\n```\n\n`{repr(e)}`\n"

    out_path.write_text(header + body)
    return {"name": name, "model": model_used, "duration_s": dt, "out": str(out_path), "ok": "error" not in result}


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
