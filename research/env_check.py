#!/usr/bin/env python3
"""
BigBounce Research Environment Checker

Validates that API keys are configured and optionally tests connectivity.
Run: python research/env_check.py [--test]
"""

import os
import sys
from pathlib import Path

# Load .env.local if python-dotenv is available
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent.parent / ".env.local"
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

# Key definitions: (env_var, name, required, category)
KEYS = [
    # LLM / Deep Reasoning
    ("ANTHROPIC_API_KEY",       "Anthropic Claude",     True,  "LLM"),
    ("OPENAI_API_KEY",          "OpenAI GPT",           False, "LLM"),
    ("GOOGLE_AI_API_KEY",       "Google Gemini",        False, "LLM"),
    ("DEEPSEEK_API_KEY",        "DeepSeek R1",          False, "LLM"),
    ("XAI_API_KEY",             "xAI Grok",             False, "LLM"),
    ("OPENROUTER_API_KEY",      "OpenRouter",           False, "LLM"),
    # Science
    ("NASA_ADS_API_KEY",        "NASA ADS",             True,  "Science"),
    ("SEMANTIC_SCHOLAR_API_KEY","Semantic Scholar",      False, "Science"),
    # Data
    ("HUGGINGFACE_TOKEN",       "Hugging Face",         False, "Data"),
    # Web
    ("FIRECRAWL_API_KEY",       "Firecrawl",            False, "Web"),
]


def check_keys():
    """Check which keys are configured."""
    configured = []
    missing_required = []
    missing_optional = []

    for env_var, name, required, category in KEYS:
        val = os.environ.get(env_var, "").strip()
        if val:
            # Mask the key for display
            masked = val[:8] + "..." + val[-4:] if len(val) > 16 else val[:4] + "..."
            configured.append((env_var, name, category, masked))
        elif required:
            missing_required.append((env_var, name, category))
        else:
            missing_optional.append((env_var, name, category))

    return configured, missing_required, missing_optional


def test_anthropic():
    """Quick connectivity test for Anthropic."""
    try:
        import anthropic
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=32,
            messages=[{"role": "user", "content": "Reply with just 'ok'"}],
        )
        return True, resp.content[0].text.strip()
    except Exception as e:
        return False, str(e)[:80]


def test_nasa_ads():
    """Quick connectivity test for NASA ADS."""
    try:
        import urllib.request
        key = os.environ.get("NASA_ADS_API_KEY", "")
        req = urllib.request.Request(
            "https://api.adsabs.harvard.edu/v1/search/query?q=bigbounce&rows=1",
            headers={"Authorization": f"Bearer {key}"},
        )
        resp = urllib.request.urlopen(req, timeout=10)
        return resp.status == 200, f"HTTP {resp.status}"
    except Exception as e:
        return False, str(e)[:80]


def main():
    do_test = "--test" in sys.argv

    print("\n  BigBounce Research Environment Check")
    print("  " + "=" * 40)

    configured, missing_req, missing_opt = check_keys()

    # Configured
    if configured:
        print(f"\n  Configured ({len(configured)}):")
        for env_var, name, category, masked in configured:
            print(f"    [{category:7}] {name:20} {masked}")

    # Missing required
    if missing_req:
        print(f"\n  Missing REQUIRED ({len(missing_req)}):")
        for env_var, name, category in missing_req:
            print(f"    [{category:7}] {name:20} → set {env_var} in .env.local")

    # Missing optional
    if missing_opt:
        print(f"\n  Missing optional ({len(missing_opt)}):")
        for env_var, name, category in missing_opt:
            print(f"    [{category:7}] {name:20}")

    # Connectivity tests
    if do_test and configured:
        print(f"\n  Connectivity Tests:")
        if os.environ.get("ANTHROPIC_API_KEY"):
            ok, msg = test_anthropic()
            status = "PASS" if ok else "FAIL"
            print(f"    Anthropic Claude:  {status} ({msg})")
        if os.environ.get("NASA_ADS_API_KEY"):
            ok, msg = test_nasa_ads()
            status = "PASS" if ok else "FAIL"
            print(f"    NASA ADS:          {status} ({msg})")

    # Summary
    total = len(KEYS)
    n_configured = len(configured)
    print(f"\n  {n_configured}/{total} keys configured", end="")
    if missing_req:
        print(f" ({len(missing_req)} required keys missing!)")
        sys.exit(1)
    else:
        print(" (all required keys present)")
        sys.exit(0)


if __name__ == "__main__":
    main()
