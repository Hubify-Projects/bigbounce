#!/usr/bin/env python3
"""
v3 API health check — pre-flight verification that all 5 reviewer keys +
meta-reviewer key have working credits before launching a fire.

Catches the failure mode documented in AUTOLOOP_IMPROVEMENTS.md fire-18 entry:
gpt-5-pro/gpt-5/o3 all hit 429 insufficient_quota; the autoloop ran
anyway with degraded coverage (3/5 reviewers for P1A) instead of warning.

Runs a minimal-cost ping per provider (1-5 tokens).

Usage:
    python tools/v3_api_health_check.py

Exit code = number of UNHEALTHY providers (0 = all healthy).
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_LOCAL = REPO / ".env.local"


def load_keys() -> dict:
    keys = {}
    if not ENV_LOCAL.exists():
        return keys
    for line in ENV_LOCAL.read_text().splitlines():
        line = line.strip()
        if line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        keys[k.strip()] = v.strip().strip('"').strip("'")
    return keys


def classify_error(msg: str) -> str:
    msg_low = msg.lower()
    if "insufficient_quota" in msg_low:
        return "QUOTA_EXHAUSTED"
    if "credit balance" in msg_low or "low credit" in msg_low:
        return "QUOTA_EXHAUSTED"
    if "quota" in msg_low and ("exceed" in msg_low or "exhaust" in msg_low):
        return "QUOTA_EXHAUSTED"
    if "rate" in msg_low and "limit" in msg_low:
        return "RATE_LIMITED"
    if "401" in msg or "unauthorized" in msg_low or "invalid api key" in msg_low:
        return "KEY_INVALID"
    return "UNREACHABLE"


def check_anthropic(key: str) -> tuple[str, str]:
    if not key:
        return ("KEY_MISSING", "ANTHROPIC_API_KEY not in .env.local")
    try:
        import anthropic
        c = anthropic.Anthropic(api_key=key, timeout=15.0)
        r = c.messages.create(
            model="claude-opus-4-7",
            max_tokens=5,
            messages=[{"role": "user", "content": "ping"}],
        )
        return ("HEALTHY", f"claude-opus-4-7 returned {len(r.content)} content blocks")
    except Exception as e:
        return (classify_error(str(e)), str(e)[:200])


def check_openai(key: str) -> tuple[str, str]:
    if not key:
        return ("KEY_MISSING", "OPENAI_API_KEY not in .env.local")
    try:
        from openai import OpenAI
        c = OpenAI(api_key=key, timeout=15.0)
        r = c.chat.completions.create(
            model="gpt-5",
            max_completion_tokens=5,
            messages=[{"role": "user", "content": "ping"}],
        )
        return ("HEALTHY", f"gpt-5 returned {len(r.choices)} choices")
    except Exception as e:
        return (classify_error(str(e)), str(e)[:200])


def check_gemini(key: str) -> tuple[str, str]:
    if not key:
        return ("KEY_MISSING", "GEMINI_API_KEY not in .env.local")
    try:
        import google.generativeai as genai
        genai.configure(api_key=key)
        m = genai.GenerativeModel("gemini-2.5-pro")
        r = m.generate_content("ping")
        fr = getattr(r.candidates[0], "finish_reason", "?") if r.candidates else "?"
        return ("HEALTHY", f"gemini-2.5-pro returned (finish_reason={fr})")
    except Exception as e:
        return (classify_error(str(e)), str(e)[:200])


def check_grok(key: str) -> tuple[str, str]:
    if not key:
        return ("KEY_MISSING", "XAI_API_KEY / GROK_API_KEY not in .env.local")
    try:
        from openai import OpenAI
        c = OpenAI(api_key=key, base_url="https://api.x.ai/v1", timeout=15.0)
        r = c.chat.completions.create(
            model="grok-4",
            max_tokens=5,
            messages=[{"role": "user", "content": "ping"}],
        )
        return ("HEALTHY", f"grok-4 returned {len(r.choices)} choices")
    except Exception as e:
        return (classify_error(str(e)), str(e)[:200])


def check_perplexity(key: str) -> tuple[str, str]:
    if not key:
        return ("KEY_MISSING", "PERPLEXITY_API_KEY not in .env.local")
    try:
        from openai import OpenAI
        c = OpenAI(api_key=key, base_url="https://api.perplexity.ai", timeout=15.0)
        r = c.chat.completions.create(
            model="sonar-pro",
            max_tokens=16,  # sonar-pro minimum is 16
            messages=[{"role": "user", "content": "ping"}],
        )
        return ("HEALTHY", f"sonar-pro returned {len(r.choices)} choices")
    except Exception as e:
        return (classify_error(str(e)), str(e)[:200])


def main():
    keys = load_keys()
    checks = [
        ("Anthropic (claude-opus-4-7)", check_anthropic, keys.get("ANTHROPIC_API_KEY", "")),
        ("OpenAI (gpt-5)", check_openai, keys.get("OPENAI_API_KEY", "")),
        ("Google (gemini-2.5-pro)", check_gemini, keys.get("GOOGLE_GEMINI_API_KEY", "") or keys.get("GEMINI_API_KEY", "")),
        ("xAI (grok-4)", check_grok, keys.get("XAI_API_KEY", "") or keys.get("GROK_API_KEY", "")),
        ("Perplexity (sonar-pro)", check_perplexity, keys.get("PERPLEXITY_API_KEY", "")),
    ]
    unhealthy = 0
    print("# v3 API health check")
    print("")
    for name, fn, key in checks:
        status, detail = fn(key)
        flag = "OK" if status == "HEALTHY" else "FAIL"
        print(f"  [{flag:>4}] {name}: {status}")
        if status != "HEALTHY":
            print(f"          {detail[:160]}")
            unhealthy += 1
    print("")
    print(f"# Summary: {5 - unhealthy} / 5 providers healthy")
    if unhealthy > 0:
        print("# Recommendation: top up degraded provider budgets before next fire")
    sys.exit(unhealthy)


if __name__ == "__main__":
    main()
