#!/usr/bin/env python3
"""
Computation & Verification Agent

Verifies equations and computations using Wolfram Alpha and DeepSeek R1.

Usage:
    from research.agents.computation import wolfram, verify_equation, cross_check
    result = wolfram("integrate x^2 sin(x) dx")
    check = verify_equation("e^{-3*92} * (10^15/10^16)^{3/2}", "~10^{-121}")
    report = cross_check("Verify the dimensional analysis: [alpha/M] = -1, [F] = +2")
"""

import os
import json
import urllib.request
import urllib.parse
from typing import Optional

from . import OUTPUT_DIR


# ── Wolfram Alpha ─────────────────────────────────────────────────────

WOLFRAM_BASE = "https://api.wolframalpha.com"

def wolfram(query: str, format: str = "full") -> dict:
    """
    Query Wolfram Alpha.

    Args:
        query: Natural language or mathematical query
        format: "full" (structured pods), "short" (one-line), "llm" (agent-friendly)

    Returns:
        Dict with answer and pods (for full format)
    """
    app_id = os.environ.get("WOLFRAM_ALPHA_APP_ID", "")
    if not app_id:
        raise ValueError("WOLFRAM_ALPHA_APP_ID not set")

    if format == "short":
        params = urllib.parse.urlencode({"appid": app_id, "i": query})
        req = urllib.request.Request(f"{WOLFRAM_BASE}/v1/result?{params}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {"answer": resp.read().decode(), "format": "short"}

    elif format == "llm":
        params = urllib.parse.urlencode({"appid": app_id, "input": query})
        req = urllib.request.Request(f"{WOLFRAM_BASE}/v1/llm-api?{params}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {"answer": resp.read().decode(), "format": "llm"}

    else:  # full
        params = urllib.parse.urlencode({
            "appid": app_id, "input": query, "output": "json",
            "format": "plaintext",
        })
        req = urllib.request.Request(f"{WOLFRAM_BASE}/v2/query?{params}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())

        pods = data.get("queryresult", {}).get("pods", [])
        result = {"format": "full", "success": data["queryresult"].get("success", False), "pods": []}
        for pod in pods:
            subpods = pod.get("subpods", [])
            texts = [s.get("plaintext", "") for s in subpods if s.get("plaintext")]
            if texts:
                result["pods"].append({
                    "title": pod.get("title", ""),
                    "text": "\n".join(texts),
                })
        return result


def wolfram_verify(expression: str, expected: str) -> dict:
    """
    Verify a mathematical expression against an expected value.

    Args:
        expression: Mathematical expression to evaluate
        expected: Expected result (approximate match)

    Returns:
        Dict with computed value, expected value, and match status
    """
    result = wolfram(expression, format="short")
    computed = result.get("answer", "")
    return {
        "expression": expression,
        "computed": computed,
        "expected": expected,
        "match": expected.lower().replace(" ", "") in computed.lower().replace(" ", ""),
    }


# ── DeepSeek R1 Verification ─────────────────────────────────────────

def deepseek_verify(claim: str, context: Optional[str] = None,
                    max_tokens: int = 4096) -> dict:
    """
    Use DeepSeek R1 to verify a mathematical claim with high rigor.

    Args:
        claim: The mathematical statement or derivation to verify
        context: Optional context (e.g., "In Einstein-Cartan theory with Holst term...")

    Returns:
        Dict with verdict, reasoning, and any errors found
    """
    import requests

    key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not key:
        raise ValueError("DEEPSEEK_API_KEY not set")

    system = """You are a mathematical physics referee with the highest standards of rigor.
Your job is to verify mathematical claims, checking for:
1. Dimensional consistency (every term must have matching dimensions)
2. Sign errors (especially in Levi-Civita contractions and metric signatures)
3. Index symmetry violations
4. Unjustified approximations
5. Logical gaps in derivation chains

For each claim, provide:
- VERDICT: CORRECT / ERROR FOUND / UNCLEAR
- REASONING: Step-by-step verification
- ERRORS: List of specific errors found (if any)
- SEVERITY: CRITICAL / MINOR / COSMETIC (for each error)"""

    prompt = claim
    if context:
        prompt = f"Context: {context}\n\nClaim to verify:\n{claim}"

    resp = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "deepseek-reasoner",
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": max_tokens,
            "temperature": 0.0,
        },
        timeout=180,
    )
    resp.raise_for_status()
    data = resp.json()
    content = data["choices"][0]["message"].get("content", "")

    # DeepSeek R1 may return empty content when reasoning uses all tokens
    if not content:
        reasoning = data["choices"][0]["message"].get("reasoning_content", "")
        return {
            "verdict": "INCOMPLETE",
            "content": f"Reasoning chain exhausted tokens. Partial reasoning:\n{reasoning[:2000]}",
            "model": "deepseek-reasoner",
        }

    return {
        "verdict": "CORRECT" if "CORRECT" in content.upper()[:200] else
                   "ERROR FOUND" if "ERROR" in content.upper()[:200] else "REVIEW",
        "content": content,
        "model": "deepseek-reasoner",
    }


# ── Combined Verification ────────────────────────────────────────────

def verify_equation(equation: str, expected: str,
                    context: Optional[str] = None) -> dict:
    """
    Verify an equation using both Wolfram Alpha and DeepSeek R1.

    Returns combined report.
    """
    report = {"equation": equation, "expected": expected}

    # Wolfram (numerical check)
    try:
        w = wolfram_verify(equation, expected)
        report["wolfram"] = w
    except Exception as e:
        report["wolfram"] = {"error": str(e)}

    # DeepSeek (logical check)
    try:
        d = deepseek_verify(
            f"Evaluate: {equation}\nExpected result: {expected}",
            context=context,
        )
        report["deepseek"] = d
    except Exception as e:
        report["deepseek"] = {"error": str(e)}

    return report


def cross_check(claim: str, models: list[str] = None) -> dict:
    """
    Cross-check a claim across multiple reasoning models.
    Uses the reasoning_router for multi-model queries.
    """
    from .reasoning_router import multi_query

    system = """You are verifying a mathematical physics claim.
Be skeptical. Check dimensions, signs, and logical steps.
Reply with: VERDICT (CORRECT/ERROR/UNCLEAR), then your reasoning."""

    if models is None:
        models = ["math_rigor", "reasoning", "writing"]

    results = multi_query(claim, models=models, system=system, max_tokens=2048)
    verdicts = []
    for r in results:
        content = r.get("content", "")
        if content:
            if "CORRECT" in content[:200].upper():
                verdicts.append("CORRECT")
            elif "ERROR" in content[:200].upper():
                verdicts.append("ERROR")
            else:
                verdicts.append("UNCLEAR")

    return {
        "claim": claim,
        "responses": results,
        "verdicts": verdicts,
        "consensus": max(set(verdicts), key=verdicts.count) if verdicts else "NO_RESPONSE",
    }


if __name__ == "__main__":
    print("Testing Wolfram Alpha...\n")
    try:
        r = wolfram("mass of the Sun in GeV", format="short")
        print(f"  Solar mass: {r['answer']}")
    except Exception as e:
        print(f"  Wolfram error: {e}")

    print("\nTesting Wolfram LLM API...\n")
    try:
        r = wolfram("Planck mass in grams", format="llm")
        print(f"  {r['answer'][:200]}")
    except Exception as e:
        print(f"  Wolfram LLM error: {e}")
