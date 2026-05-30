#!/usr/bin/env python3
"""
Direct-vendor adversarial peer review — bypasses OpenRouter entirely.

Per feedback_no_openrouter_excuse 2026-05-29 standing directive: never lean on
the OpenRouter weekly cap as a blocker. All direct vendor keys live in the
sibling repo .env.local at /Users/houstongolden/Desktop/CODE_2025/youmd/.env.local
(also appended to bigbounce/.env.local on 2026-05-29).

4 reviewers, each calling its native vendor's HTTP API directly:

  - GPT5_methodology              → OpenAI            (api.openai.com)
  - Gemini31Pro_cosmology         → Google Gemini     (generativelanguage.googleapis.com)
  - Grok43_brutal                 → xAI               (api.x.ai/v1, OpenAI-compatible)
  - PerplexitySonarPro_citations  → Perplexity        (api.perplexity.ai, OpenAI-compatible)

DeepSeek-V4-Pro is NOT included here because the youmd .env.local has no
DEEPSEEK_API_KEY; it can be added later or the script can fall back to
OpenRouter for DeepSeek only (out of scope for this initial refactor).

Anthropic is INTENTIONALLY excluded per feedback_cross_model_peer_review
(no echo chamber: papers are Claude-assisted, so Claude can't be an
adversarial reviewer of them).

Usage:
    python tools/cross_vendor_review_direct.py <paper_tex_path> <round_label> <paper_tag> [round_context]

    # Example:
    python tools/cross_vendor_review_direct.py \\
        pipelines/p3_anomaly_engine/paper3_draft.tex \\
        2026-05-29_R-direct-v1 \\
        P3 \\
        "First direct-vendor R-round on P3 v3.1.68 — verify all 4 §pathc_caveats closures hold"

Reads keys from bigbounce/.env.local (which now contains the direct keys
copied from youmd/.env.local). Saves per-reviewer findings to
project-context/peer-reviews/<round_label>_<paper>_<reviewer>.md.
"""
from __future__ import annotations

import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _SSL_CTX = ssl.create_default_context()

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_LOCAL = REPO / ".env.local"

# --------- Reviewer configurations ---------
# Each reviewer has:
#   key_var            — env var name for the API key
#   url                — endpoint URL
#   model              — model ID (vendor-native, NOT OpenRouter slugs)
#   fallback           — secondary model if primary 404s
#   call_style         — "openai_chat" (most), "gemini_native" (Google)
#   reasoning_effort   — for OpenAI o-series, Grok reasoning; None for others

REVIEWERS = {
    "GPT5_methodology": {
        "key_var": "OPENAI_API_KEY",
        "url": "https://api.openai.com/v1/chat/completions",
        "model": "gpt-5",
        "fallback": "gpt-4o",
        "call_style": "openai_chat",
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
    "Gemini25Pro_cosmology": {
        "key_var": "GOOGLE_GEMINI_API_KEY",
        # Gemini's HTTP API uses the model name in the URL path:
        "url_template": "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
        "model": "gemini-2.5-pro",
        "fallback": "gemini-2.0-flash-exp",
        "call_style": "gemini_native",
        "reasoning_effort": None,  # Gemini 2.5 Pro has built-in thinking
        "persona": "Gemini-2.5-Pro cosmology-physics reviewer",
        "focus": (
            "Theoretical physics: gauge-frame vs physical-frame distinctions, GR "
            "projection effects, model-class scope boundaries, EFT counting, "
            "consistency-relation applicability. Flag any 'mechanism-independent' "
            "claim that overstates UV-completion independence. Check parity-violation "
            "/ ALP / Chern-Simons references against standard reviews."
        ),
    },
    "Grok_brutal": {
        "key_var": "XAI_API_KEY",
        "url": "https://api.x.ai/v1/chat/completions",
        "model": "grok-4",
        "fallback": "grok-2-1212",
        "call_style": "openai_chat",
        "reasoning_effort": None,  # Grok 4 reasoning is on by default
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
        "key_var": "PERPLEXITY_API_KEY",
        "url": "https://api.perplexity.ai/chat/completions",
        "model": "sonar-pro",
        "fallback": "sonar",
        "call_style": "openai_chat",
        "reasoning_effort": None,
        "persona": "Perplexity Sonar Pro citation-chain forensic auditor",
        "focus": (
            "Citation forensics — does each cited paper actually say what's claimed? "
            "Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are "
            "authors and journal venues correct? Use web search to verify against "
            "arXiv.org / ADS / publisher sites. Flag any fused metadata "
            "(title from one paper + arXiv ID from another)."
        ),
    },
}


def load_keys() -> dict:
    keys = {}
    if not ENV_LOCAL.exists():
        raise RuntimeError(f"no .env.local at {ENV_LOCAL}")
    for line in ENV_LOCAL.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        keys[k.strip()] = v.strip().strip('"').strip("'")
    return keys


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


def call_openai_chat(url: str, api_key: str, model: str, prompt: str,
                     max_tokens: int = 16000, timeout: int = 480,
                     reasoning_effort: str | None = None) -> dict:
    """OpenAI-compatible /chat/completions call. Works for OpenAI, Grok (xAI), Perplexity."""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }
    if reasoning_effort and "api.openai.com" in url:
        # OpenAI o-series-style: top-level reasoning_effort field.
        payload["reasoning_effort"] = reasoning_effort
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"error": {"status": e.code, "body": body[:4000]}}
    except Exception as e:
        return {"error": {"exception": repr(e)}}


def call_gemini_native(url_template: str, api_key: str, model: str, prompt: str,
                       max_tokens: int = 16000, timeout: int = 480) -> dict:
    """Google Gemini native HTTP API (generativelanguage.googleapis.com)."""
    url = url_template.format(model=model, key=api_key)
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": max_tokens,
        },
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"error": {"status": e.code, "body": body[:4000]}}
    except Exception as e:
        return {"error": {"exception": repr(e)}}


def extract_content(result: dict, call_style: str) -> tuple[str | None, dict]:
    """Returns (content, usage_dict)."""
    if "error" in result:
        return None, {}
    try:
        if call_style == "openai_chat":
            content = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            return content, usage
        elif call_style == "gemini_native":
            cand = result["candidates"][0]
            parts = cand["content"]["parts"]
            content = "\n".join(p.get("text", "") for p in parts)
            usage_meta = result.get("usageMetadata", {})
            usage = {
                "prompt_tokens": usage_meta.get("promptTokenCount"),
                "completion_tokens": usage_meta.get("candidatesTokenCount"),
                "total_tokens": usage_meta.get("totalTokenCount"),
            }
            return content, usage
    except (KeyError, IndexError, TypeError):
        pass
    return None, {}


def call_with_fallback(cfg: dict, prompt: str, key: str) -> tuple[dict, str]:
    style = cfg["call_style"]
    primary = cfg["model"]
    fallback = cfg.get("fallback", primary)

    if style == "openai_chat":
        res = call_openai_chat(cfg["url"], key, primary, prompt,
                               reasoning_effort=cfg.get("reasoning_effort"))
        model_used = primary
        if "error" in res:
            status = res["error"].get("status")
            err_body = (res["error"].get("body") or "").lower()
            is_missing = status == 404 or "model" in err_body or "not found" in err_body
            if is_missing and fallback != primary:
                # Fallback models (e.g. gpt-4o) typically don't accept reasoning_effort —
                # retry without it.
                res = call_openai_chat(cfg["url"], key, fallback, prompt, reasoning_effort=None)
                model_used = fallback
            else:
                # 400 "Unrecognized request argument: reasoning_effort" → retry primary without it
                if status == 400 and "reasoning_effort" in err_body:
                    res = call_openai_chat(cfg["url"], key, primary, prompt, reasoning_effort=None)
                    model_used = primary
        return res, model_used
    elif style == "gemini_native":
        res = call_gemini_native(cfg["url_template"], key, primary, prompt)
        model_used = primary
        if "error" in res:
            status = res["error"].get("status")
            err_body = (res["error"].get("body") or "").lower()
            is_missing = status == 404 or "model" in err_body
            if is_missing and fallback != primary:
                res = call_gemini_native(cfg["url_template"], key, fallback, prompt)
                model_used = fallback
        return res, model_used
    return {"error": {"exception": f"unknown call_style: {style}"}}, primary


def run_reviewer(name: str, cfg: dict, paper_text: str, round_label: str,
                 paper_tag: str, round_context: str, keys: dict, out_dir: Path) -> dict:
    key_var = cfg["key_var"]
    api_key = keys.get(key_var)
    if not api_key:
        out_path = out_dir / f"{round_label}_{paper_tag}_R-round_direct_{name}.md"
        out_path.write_text(f"# {paper_tag} R-round — direct — {cfg['persona']}\n\n**FAILED**: no `{key_var}` in .env.local\n")
        return {"name": name, "model": cfg["model"], "duration_s": 0, "out": str(out_path), "ok": False, "skip_reason": f"no {key_var}"}

    persona = cfg["persona"]
    prompt = build_prompt(paper_text, persona, cfg["focus"], round_context)
    t0 = time.time()
    result, model_used = call_with_fallback(cfg, prompt, api_key)
    dt = time.time() - t0

    out_path = out_dir / f"{round_label}_{paper_tag}_R-round_direct_{name}.md"
    fallback_note = f" (FALLBACK from `{cfg['model']}`)" if model_used != cfg["model"] else ""
    header = (
        f"# {paper_tag} R-round — DIRECT vendor — {persona}\n\n"
        f"**Model**: `{model_used}`{fallback_note} (direct vendor API; NOT via OpenRouter)\n"
        f"**Round**: {round_label}\n"
        f"**Wall time**: {dt:.1f}s\n"
        f"**Persona focus**: {cfg['focus']}\n\n"
        f"---\n\n"
    )

    content, usage = extract_content(result, cfg["call_style"])
    if content is None:
        body = f"## Reviewer call failed or returned unparseable response\n\n```json\n{json.dumps(result, indent=2)[:4000]}\n```\n"
        ok = False
    else:
        usage_line = ", ".join(
            f"{k.replace('_tokens', '')}={v}" for k, v in usage.items() if v is not None
        )
        body = f"**Tokens**: {usage_line}\n\n---\n\n{content}\n"
        ok = True

    out_path.write_text(header + body)
    return {"name": name, "model": model_used, "duration_s": dt, "out": str(out_path), "ok": ok}


def main() -> int:
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <paper_tex_path> <round_label> <paper_tag> [round_context]", file=sys.stderr)
        return 1
    tex_path = Path(sys.argv[1])
    round_label = sys.argv[2]
    paper_tag = sys.argv[3]
    round_context = sys.argv[4] if len(sys.argv) >= 5 else "Cross-vendor adversarial peer-review round (direct-vendor SDKs)."

    keys = load_keys()
    paper_text = tex_path.read_text()
    out_dir = REPO / "project-context" / "peer-reviews"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[direct-xreview] {paper_tag} — {len(paper_text):,} chars — dispatching {len(REVIEWERS)} reviewers in parallel", flush=True)
    available = [name for name, cfg in REVIEWERS.items() if cfg["key_var"] in keys]
    missing = [(name, cfg["key_var"]) for name, cfg in REVIEWERS.items() if cfg["key_var"] not in keys]
    if missing:
        for name, kv in missing:
            print(f"  WARN: skipping {name} — no {kv} in .env.local", flush=True)
    print(f"  reviewers with keys: {len(available)}/{len(REVIEWERS)}", flush=True)

    results = []
    with ThreadPoolExecutor(max_workers=len(REVIEWERS)) as pool:
        futures = {
            pool.submit(run_reviewer, name, cfg, paper_text, round_label, paper_tag, round_context, keys, out_dir): name
            for name, cfg in REVIEWERS.items()
        }
        for fut in as_completed(futures):
            res = fut.result()
            status = "OK " if res["ok"] else "FAIL"
            print(f"[{status}] {res['name']:30s} {res['model']:25s} {res['duration_s']:6.1f}s → {res['out']}", flush=True)
            results.append(res)

    ok_count = sum(1 for r in results if r["ok"])
    print(f"\n[direct-xreview] done: {ok_count}/{len(results)} reviewers landed", flush=True)
    return 0 if ok_count else 2


if __name__ == "__main__":
    sys.exit(main())
