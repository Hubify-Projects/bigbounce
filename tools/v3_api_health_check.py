#!/usr/bin/env python3
"""BigBounce direct-API health preflight.

Required direct APIs are Google/Gemini and xAI/Grok. Perplexity is optional.
OpenAI-family review runs through Codex/ChatGPT subscription, and Anthropic/
Claude is disabled for the active campaign; neither route is pinged here.

Catches the failure mode documented in AUTOLOOP_IMPROVEMENTS.md fire-18 entry:
gpt-5-pro/gpt-5/o3 all hit 429 insufficient_quota; the autoloop ran
anyway with degraded coverage (3/5 reviewers for P1A) instead of warning.

Runs a minimal-cost ping per provider (1-5 tokens).

Usage:
    python tools/v3_api_health_check.py

Exit code = number of unhealthy REQUIRED providers (0 = launchable).
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
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
        ("Google (gemini-2.5-pro)", check_gemini, keys.get("GOOGLE_GEMINI_API_KEY", "") or keys.get("GEMINI_API_KEY", ""), True),
        ("xAI (grok-4)", check_grok, keys.get("XAI_API_KEY", "") or keys.get("GROK_API_KEY", ""), True),
        ("Perplexity (sonar-pro)", check_perplexity, keys.get("PERPLEXITY_API_KEY", ""), False),
    ]
    unhealthy = 0
    print("# BigBounce direct-API health check")
    print("")
    for name, fn, key, required in checks:
        status, detail = fn(key)
        flag = "OK" if status == "HEALTHY" else ("FAIL" if required else "SKIP")
        tier = "required" if required else "optional"
        print(f"  [{flag:>4}] {name} ({tier}): {status}")
        if status != "HEALTHY":
            print(f"          {detail[:160]}")
        if required and status != "HEALTHY":
            unhealthy += 1
    print("")
    print(f"# Required summary: {2 - unhealthy} / 2 providers healthy")
    if unhealthy > 0:
        print("# Recommendation: restore required Gemini/Grok access before next API wave")
    sys.exit(unhealthy)


if __name__ == "__main__":
    main()
