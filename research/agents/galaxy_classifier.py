"""Galaxy morphology classification using vision models.

Two classification approaches for galaxy spin direction:
  A) Zoobot encoder + linear probe (specialized, runs on CPU)
  B) Frontier vision model via API (general, requires API key)

Phase 4 — intended for Colab Pro GPU work. CPU inference viable
with convnext_nano for small batches (~0.5s/image).
"""

import json
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


# =============================================
# Approach A: Zoobot Encoder + Linear Probe
# =============================================

def classify_with_zoobot(
    image_paths: list[str],
    model_name: str = "convnext_nano",
    batch_size: int = 32,
) -> list[dict]:
    """Classify galaxy spiral direction using Zoobot encoder + linear probe.

    Extracts 640-dim embeddings from the Zoobot encoder, then applies a
    linear probe trained to predict CW vs CCW spiral direction.

    Args:
        image_paths: List of paths to galaxy images
        model_name: Zoobot model variant (convnext_nano = 4M params)
        batch_size: Batch size for inference

    Returns:
        List of dicts with keys: path, cw_prob, ccw_prob, predicted_direction
    """
    try:
        import torch
        import torchvision.transforms as T
        from PIL import Image
    except ImportError:
        raise ImportError("Install: pip install torch torchvision Pillow")

    from research.agents.galaxy_zoo import load_zoobot_encoder

    model = load_zoobot_encoder(model_name)
    model.eval()

    transform = T.Compose([
        T.Resize(224),
        T.CenterCrop(224),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    results = []
    for i in range(0, len(image_paths), batch_size):
        batch_paths = image_paths[i:i + batch_size]
        images = []

        for p in batch_paths:
            try:
                img = Image.open(p).convert("RGB")
                images.append(transform(img))
            except Exception as e:
                logger.warning(f"Failed to load {p}: {e}")
                results.append({
                    "path": p, "cw_prob": None, "ccw_prob": None,
                    "predicted_direction": "error", "error": str(e)
                })
                continue

        if not images:
            continue

        batch = torch.stack(images)

        with torch.no_grad():
            embeddings = model(batch)

        # Without a trained linear probe, use embedding statistics
        # as a proxy (in production, train probe on labeled GZ data)
        for j, emb in enumerate(embeddings):
            # Heuristic: signed sum of first half vs second half of embedding
            # This is a placeholder — real probe needs training
            half = emb.shape[0] // 2
            score = (emb[:half].sum() - emb[half:].sum()).item()
            cw_prob = 1.0 / (1.0 + (-score).__abs__())
            ccw_prob = 1.0 - cw_prob

            results.append({
                "path": batch_paths[j],
                "cw_prob": round(cw_prob, 4),
                "ccw_prob": round(ccw_prob, 4),
                "predicted_direction": "CW" if cw_prob > 0.5 else "CCW",
                "embedding_dim": emb.shape[0],
                "model": model_name,
                "note": "Placeholder probe — train on labeled GZ data for production"
            })

        if (i + batch_size) % 100 == 0:
            logger.info(f"Processed {min(i + batch_size, len(image_paths))}/{len(image_paths)} images")

    return results


# =============================================
# Approach B: Frontier Vision Model via API
# =============================================

def classify_with_vision_api(
    image_paths: list[str],
    provider: str = "anthropic",
    model: Optional[str] = None,
    max_concurrent: int = 5,
) -> list[dict]:
    """Classify galaxy spiral direction using a frontier vision model.

    Sends galaxy images to Claude/GPT-4o with a classification prompt.
    Cost: ~$0.01/image but potentially higher accuracy on ambiguous cases.

    Args:
        image_paths: List of paths to galaxy images
        provider: "anthropic" or "openai"
        model: Model ID (default: latest vision model)
        max_concurrent: Max concurrent API calls

    Returns:
        List of dicts with keys: path, cw_prob, ccw_prob, predicted_direction, reasoning
    """
    import base64
    import os

    if provider == "anthropic":
        try:
            import anthropic
        except ImportError:
            raise ImportError("Install: pip install anthropic")

        client = anthropic.Anthropic()
        model = model or "claude-sonnet-4-20250514"

    elif provider == "openai":
        try:
            import openai
        except ImportError:
            raise ImportError("Install: pip install openai")

        client = openai.OpenAI()
        model = model or "gpt-4o"

    else:
        raise ValueError(f"Unknown provider: {provider}. Use 'anthropic' or 'openai'.")

    CLASSIFICATION_PROMPT = """Analyze this galaxy image and classify its spiral arm winding direction.

Respond in JSON format:
{
  "direction": "CW" or "CCW" or "ambiguous" or "not_spiral",
  "confidence": 0.0 to 1.0,
  "morphology": "spiral" or "elliptical" or "irregular" or "edge_on",
  "reasoning": "brief explanation"
}

CW (clockwise/Z-wise): arms wind clockwise when viewed from our perspective.
CCW (counter-clockwise/S-wise): arms wind counter-clockwise.

If the galaxy is not a clear face-on spiral, classify as "not_spiral" or "ambiguous"."""

    results = []
    for path in image_paths:
        try:
            with open(path, "rb") as f:
                img_b64 = base64.b64encode(f.read()).decode()

            media_type = "image/png" if path.endswith(".png") else "image/jpeg"

            if provider == "anthropic":
                response = client.messages.create(
                    model=model,
                    max_tokens=300,
                    messages=[{
                        "role": "user",
                        "content": [
                            {"type": "image", "source": {
                                "type": "base64", "media_type": media_type,
                                "data": img_b64
                            }},
                            {"type": "text", "text": CLASSIFICATION_PROMPT}
                        ]
                    }]
                )
                text = response.content[0].text

            elif provider == "openai":
                response = client.chat.completions.create(
                    model=model,
                    max_tokens=300,
                    messages=[{
                        "role": "user",
                        "content": [
                            {"type": "image_url", "image_url": {
                                "url": f"data:{media_type};base64,{img_b64}"
                            }},
                            {"type": "text", "text": CLASSIFICATION_PROMPT}
                        ]
                    }]
                )
                text = response.choices[0].message.content

            # Parse JSON response
            parsed = json.loads(text.strip().strip("```json").strip("```"))
            direction = parsed.get("direction", "ambiguous")
            confidence = parsed.get("confidence", 0.5)

            results.append({
                "path": path,
                "cw_prob": round(confidence if direction == "CW" else 1 - confidence, 4),
                "ccw_prob": round(confidence if direction == "CCW" else 1 - confidence, 4),
                "predicted_direction": direction,
                "confidence": confidence,
                "morphology": parsed.get("morphology"),
                "reasoning": parsed.get("reasoning"),
                "model": model,
                "provider": provider
            })

        except Exception as e:
            logger.warning(f"API classification failed for {path}: {e}")
            results.append({
                "path": path, "cw_prob": None, "ccw_prob": None,
                "predicted_direction": "error", "error": str(e)
            })

    return results


# =============================================
# Utilities
# =============================================

def compare_methods(
    image_paths: list[str],
    zoobot_model: str = "convnext_nano",
    api_provider: str = "anthropic",
) -> dict:
    """Run both classification methods and compare results.

    Useful for calibrating the Zoobot probe against frontier model judgments.
    """
    logger.info(f"Classifying {len(image_paths)} images with both methods...")

    zoobot_results = classify_with_zoobot(image_paths, model_name=zoobot_model)
    api_results = classify_with_vision_api(image_paths, provider=api_provider)

    agreements = 0
    total = 0
    for z, a in zip(zoobot_results, api_results):
        if z["predicted_direction"] in ("CW", "CCW") and a["predicted_direction"] in ("CW", "CCW"):
            total += 1
            if z["predicted_direction"] == a["predicted_direction"]:
                agreements += 1

    return {
        "n_images": len(image_paths),
        "zoobot_results": zoobot_results,
        "api_results": api_results,
        "agreement_rate": agreements / max(total, 1),
        "n_compared": total,
        "zoobot_model": zoobot_model,
        "api_provider": api_provider
    }
