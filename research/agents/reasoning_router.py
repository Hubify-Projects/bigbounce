#!/usr/bin/env python3
"""
Multi-Model Reasoning Router

Routes research questions to the best model based on task type.
All models use OpenAI-compatible chat completions format where possible.

Usage:
    from research.agents.reasoning_router import query, MODELS
    result = query("Verify this tensor contraction: ...", task="math_rigor")
    result = query("Summarize the state of cosmic birefringence", task="literature")
    result = query("Write an abstract for...", task="writing")
"""

import os
import json
import requests
from typing import Optional

# Model routing table
MODELS = {
    "math_rigor": {
        "name": "DeepSeek R1",
        "provider": "deepseek",
        "model": "deepseek-reasoner",
        "base_url": "https://api.deepseek.com/v1",
        "env_key": "DEEPSEEK_API_KEY",
        "description": "Highest skepticism for math — catches sign errors in tensor derivations",
    },
    "multimodal": {
        "name": "Gemini Deep Think",
        "provider": "google",
        "model": "gemini-2.5-pro",
        "base_url": "https://generativelanguage.googleapis.com/v1beta",
        "env_key": "GOOGLE_AI_API_KEY",
        "description": "Best at integrating images, plots, and long-form math",
    },
    "writing": {
        "name": "Claude Opus",
        "provider": "anthropic",
        "model": "claude-opus-4-6",
        "base_url": "https://api.anthropic.com/v1",
        "env_key": "ANTHROPIC_API_KEY",
        "description": "Most natural academic voice, best for structuring arguments",
    },
    "reasoning": {
        "name": "GPT",
        "provider": "openai",
        "model": "gpt-4o",
        "base_url": "https://api.openai.com/v1",
        "env_key": "OPENAI_API_KEY",
        "description": "High ELO general reasoning, good default",
    },
    "literature": {
        "name": "Perplexity",
        "provider": "perplexity",
        "model": "sonar-pro",
        "base_url": "https://api.perplexity.ai",
        "env_key": "PERPLEXITY_API_KEY",
        "description": "Web-grounded LLM — live search over recent papers",
    },
    "fast": {
        "name": "Grok",
        "provider": "xai",
        "model": "grok-3",
        "base_url": "https://api.x.ai/v1",
        "env_key": "XAI_API_KEY",
        "description": "Fast reasoning, alternative perspective",
    },
    "multi": {
        "name": "OpenRouter",
        "provider": "openrouter",
        "model": "anthropic/claude-sonnet-4",
        "base_url": "https://openrouter.ai/api/v1",
        "env_key": "OPENROUTER_API_KEY",
        "description": "Multi-model routing, fallback, comparison runs",
    },
}

# Task → model mapping (default routing)
TASK_ROUTES = {
    "math_rigor":    "math_rigor",
    "tensor_check":  "math_rigor",
    "sign_error":    "math_rigor",
    "derivation":    "math_rigor",
    "multimodal":    "multimodal",
    "plot_analysis":  "multimodal",
    "image":         "multimodal",
    "writing":       "writing",
    "abstract":      "writing",
    "paper_edit":    "writing",
    "reasoning":     "reasoning",
    "general":       "reasoning",
    "literature":    "literature",
    "search":        "literature",
    "recent_papers": "literature",
    "fast":          "fast",
    "quick":         "fast",
    "compare":       "multi",
}


def _call_openai_compatible(base_url: str, api_key: str, model: str,
                            messages: list, max_tokens: int = 4096,
                            temperature: float = 0.1) -> dict:
    """Call any OpenAI-compatible chat completions endpoint."""
    resp = requests.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "content": data["choices"][0]["message"]["content"],
        "model": data.get("model", model),
        "usage": data.get("usage", {}),
    }


def _call_anthropic(api_key: str, model: str, messages: list,
                    max_tokens: int = 4096, temperature: float = 0.1) -> dict:
    """Call Anthropic Messages API."""
    # Extract system message if present
    system = None
    chat_msgs = []
    for m in messages:
        if m["role"] == "system":
            system = m["content"]
        else:
            chat_msgs.append(m)

    body = {
        "model": model,
        "messages": chat_msgs,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    if system:
        body["system"] = system

    resp = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        json=body,
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "content": data["content"][0]["text"],
        "model": data.get("model", model),
        "usage": data.get("usage", {}),
    }


def _call_google(api_key: str, model: str, messages: list,
                 max_tokens: int = 4096, temperature: float = 0.1) -> dict:
    """Call Google Gemini API."""
    contents = []
    system_instruction = None
    for m in messages:
        if m["role"] == "system":
            system_instruction = m["content"]
        else:
            role = "user" if m["role"] == "user" else "model"
            contents.append({"role": role, "parts": [{"text": m["content"]}]})

    body = {
        "contents": contents,
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "temperature": temperature,
        },
    }
    if system_instruction:
        body["systemInstruction"] = {"parts": [{"text": system_instruction}]}

    resp = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}",
        headers={"Content-Type": "application/json"},
        json=body,
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return {
        "content": text,
        "model": model,
        "usage": data.get("usageMetadata", {}),
    }


def query(prompt: str, task: str = "general", system: Optional[str] = None,
          model_override: Optional[str] = None, max_tokens: int = 4096,
          temperature: float = 0.1) -> dict:
    """
    Route a research question to the appropriate model.

    Args:
        prompt: The research question or task
        task: Task type (math_rigor, writing, literature, multimodal, etc.)
        system: Optional system prompt
        model_override: Force a specific model key from MODELS
        max_tokens: Max response tokens
        temperature: Sampling temperature

    Returns:
        dict with keys: content, model, usage, provider
    """
    route_key = model_override or TASK_ROUTES.get(task, "reasoning")
    config = MODELS[route_key]

    api_key = os.environ.get(config["env_key"], "")
    if not api_key:
        raise ValueError(f"Missing API key: {config['env_key']} for {config['name']}")

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    provider = config["provider"]

    if provider == "anthropic":
        result = _call_anthropic(api_key, config["model"], messages, max_tokens, temperature)
    elif provider == "google":
        result = _call_google(api_key, config["model"], messages, max_tokens, temperature)
    else:
        # OpenAI-compatible: openai, deepseek, perplexity, xai, openrouter
        result = _call_openai_compatible(
            config["base_url"], api_key, config["model"],
            messages, max_tokens, temperature,
        )

    result["provider"] = config["name"]
    result["task"] = task
    return result


def multi_query(prompt: str, models: list[str] = None,
                system: Optional[str] = None, max_tokens: int = 4096) -> list[dict]:
    """
    Send the same prompt to multiple models for comparison.

    Args:
        prompt: The question
        models: List of model keys (defaults to all available)
        system: Optional system prompt

    Returns:
        List of result dicts, one per model
    """
    if models is None:
        models = [k for k, v in MODELS.items()
                  if os.environ.get(v["env_key"], "")]

    results = []
    for model_key in models:
        try:
            r = query(prompt, model_override=model_key, system=system,
                      max_tokens=max_tokens)
            results.append(r)
        except Exception as e:
            results.append({
                "provider": MODELS[model_key]["name"],
                "error": str(e),
                "content": None,
            })
    return results


def available_models() -> dict:
    """Return dict of models that have API keys configured."""
    return {
        k: v for k, v in MODELS.items()
        if os.environ.get(v["env_key"], "")
    }


if __name__ == "__main__":
    print("\nAvailable models:")
    for key, info in available_models().items():
        print(f"  [{key:12}] {info['name']:20} — {info['description']}")
    print(f"\n{len(available_models())}/{len(MODELS)} models configured")
