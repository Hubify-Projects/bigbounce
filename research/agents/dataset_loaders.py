#!/usr/bin/env python3
"""
Dataset Loaders — HuggingFace MMU + AstroML

Loads large-scale astronomical datasets for ML and analysis.

Usage:
    from research.agents.dataset_loaders import load_mmu, load_astroml
    plasticc = load_mmu("plasticc", split="train", streaming=True)
    sdss = load_astroml("sdss_spectra")
"""

import os
from typing import Optional


# ── Multimodal Universe (HuggingFace) ────────────────────────────────

# Known MMU dataset IDs on HuggingFace
MMU_DATASETS = {
    "plasticc":         "MultimodalUniverse/plasticc",
    "legacysurvey":     "MultimodalUniverse/legacysurvey",
    "ssl_legacysurvey": "MultimodalUniverse/ssl_legacysurvey",
    "apogee":           "MultimodalUniverse/apogee",
    "sdss_spectra":     "MultimodalUniverse/sdss",
    "des":              "MultimodalUniverse/des",
    "vipers":           "MultimodalUniverse/vipers",
    "manga":            "MultimodalUniverse/manga",
    "swift_uvot":       "MultimodalUniverse/swift_uvot_sne",
    "chandra_agn":      "MultimodalUniverse/chandra_agn",
    "gaia_xp":          "MultimodalUniverse/gaia_xp",
    "jwst_ceers":       "MultimodalUniverse/jwst",
}


def load_mmu(name: str, split: str = "train", streaming: bool = True,
             max_samples: Optional[int] = None):
    """
    Load a Multimodal Universe dataset from HuggingFace.

    Args:
        name: Dataset name (see MMU_DATASETS keys) or full HF ID
        split: Dataset split
        streaming: If True, stream data (no full download). Recommended for large datasets.
        max_samples: If set, take only first N samples

    Returns:
        HuggingFace Dataset or IterableDataset (if streaming)
    """
    try:
        from datasets import load_dataset
    except ImportError:
        raise ImportError("Install HuggingFace datasets: pip install datasets")

    hf_token = os.environ.get("HUGGINGFACE_TOKEN", "")
    dataset_id = MMU_DATASETS.get(name, name)

    ds = load_dataset(dataset_id, split=split, streaming=streaming,
                      token=hf_token if hf_token else None)

    if max_samples and streaming:
        ds = ds.take(max_samples)
    elif max_samples and not streaming:
        ds = ds.select(range(min(max_samples, len(ds))))

    return ds


def list_mmu_datasets() -> dict:
    """List all known MMU datasets with their HuggingFace IDs."""
    return dict(MMU_DATASETS)


def mmu_info(name: str) -> dict:
    """Get metadata about an MMU dataset without downloading it."""
    try:
        from datasets import load_dataset_builder
    except ImportError:
        raise ImportError("Install HuggingFace datasets: pip install datasets")

    hf_token = os.environ.get("HUGGINGFACE_TOKEN", "")
    dataset_id = MMU_DATASETS.get(name, name)

    builder = load_dataset_builder(dataset_id, token=hf_token if hf_token else None)
    info = builder.info
    return {
        "name": dataset_id,
        "description": info.description[:500] if info.description else "N/A",
        "features": str(info.features) if info.features else "N/A",
        "size": info.size_in_bytes,
        "splits": {k: v.num_examples for k, v in info.splits.items()} if info.splits else {},
    }


# ── AstroML Datasets ─────────────────────────────────────────────────

ASTROML_DATASETS = {
    "sdss_spectra":     "fetch_sdss_corrected_spectra",
    "sdss_specgals":    "fetch_sdss_specgals",
    "sdss_photometry":  "fetch_sdss_sspp",
    "sdss_S82":         "fetch_sdss_S82standards",
    "rrlyrae":          "fetch_rrlyrae_combined",
    "moving_objects":   "fetch_moving_objects",
    "linear_sample":    "fetch_LINEAR_sample",
    "great_wall":       "fetch_great_wall",
    "dr7_quasar":       "fetch_dr7_quasar",
}


def load_astroml(name: str, **kwargs):
    """
    Load an AstroML built-in dataset.

    Args:
        name: Dataset name (see ASTROML_DATASETS keys)

    Returns:
        NumPy array (structured or regular). NpzFile objects are unwrapped
        to return the primary data array.
    """
    try:
        import numpy as np
        from astroML import datasets
    except ImportError:
        raise ImportError("Install AstroML: pip install astroML")

    func_name = ASTROML_DATASETS.get(name)
    if not func_name:
        raise ValueError(f"Unknown AstroML dataset: {name}. "
                         f"Available: {list(ASTROML_DATASETS.keys())}")

    func = getattr(datasets, func_name)
    result = func(**kwargs)

    # Some AstroML functions return NpzFile — unwrap to primary array
    if isinstance(result, np.lib.npyio.NpzFile):
        keys = list(result.files)
        if len(keys) == 1:
            return result[keys[0]]
        # Return dict of arrays for multi-key npz
        return {k: result[k] for k in keys}

    return result


def list_astroml_datasets() -> dict:
    """List all available AstroML datasets."""
    return dict(ASTROML_DATASETS)


# ── Polymathic AI Models ─────────────────────────────────────────────

POLYMATHIC_MODELS = {
    "walrus": {
        "hf_id": "polymathic-ai/walrus",
        "params": "1.3B",
        "description": "Physics foundation model — simulation-based inference",
        "gpu_required": True,
    },
    "aion_base": {
        "hf_id": "polymathic-ai/aion-base",
        "params": "0.3B",
        "description": "Astronomical omnimodal network — base model",
        "gpu_required": True,
    },
    "aion_large": {
        "hf_id": "polymathic-ai/aion-large",
        "params": "3.1B",
        "description": "Astronomical omnimodal network — large model",
        "gpu_required": True,
    },
}


def load_polymathic(model_name: str, device: str = "auto"):
    """
    Load a Polymathic AI model from HuggingFace.

    Requires GPU. Returns model object.
    Note: Walrus uses a custom architecture — requires `pip install walrus`
    (from https://github.com/PolymathicAI/walrus) before loading.

    Args:
        model_name: Key from POLYMATHIC_MODELS
        device: "auto", "cuda", "cpu" (cpu is very slow for inference)
    """
    info = POLYMATHIC_MODELS.get(model_name)
    if not info:
        raise ValueError(f"Unknown model: {model_name}. "
                         f"Available: {list(POLYMATHIC_MODELS.keys())}")

    hf_token = os.environ.get("HUGGINGFACE_TOKEN", "")

    # Walrus uses custom architecture — requires cloning the PolymathicAI repo
    # pip install walrus is the WRONG package (Redis wrapper).
    # Correct: pip install git+https://github.com/PolymathicAI/walrus.git
    if model_name == "walrus":
        try:
            # The PolymathicAI walrus package uses a different import
            from polymathic_walrus import Walrus
            model = Walrus.from_pretrained(
                info["hf_id"],
                token=hf_token if hf_token else None,
            )
            return model
        except ImportError:
            pass

        # Fallback: download weights directly from HF and load manually
        try:
            from huggingface_hub import hf_hub_download
            import torch

            # Download config and weights
            config_path = hf_hub_download(info["hf_id"], "config.json",
                                          token=hf_token if hf_token else None)
            weights_path = hf_hub_download(info["hf_id"], "pytorch_model.bin",
                                           token=hf_token if hf_token else None)
            import json
            with open(config_path) as f:
                config = json.load(f)
            weights = torch.load(weights_path, map_location="cuda" if torch.cuda.is_available() else "cpu")
            params = sum(v.numel() for v in weights.values())
            return {"config": config, "weights_path": weights_path, "params": params,
                    "note": "Raw weights loaded. Install PolymathicAI walrus for full model inference."}
        except Exception:
            pass

    try:
        from transformers import AutoModel
    except ImportError:
        raise ImportError("Install transformers: pip install transformers torch")

    model = AutoModel.from_pretrained(
        info["hf_id"],
        token=hf_token if hf_token else None,
        device_map=device,
        trust_remote_code=True,
    )
    return model


def list_polymathic_models() -> dict:
    """List available Polymathic AI models."""
    return {k: f"{v['params']} — {v['description']}" for k, v in POLYMATHIC_MODELS.items()}


if __name__ == "__main__":
    print("BigBounce Dataset Loaders")
    print("=" * 40)

    print("\nMultimodal Universe (HuggingFace):")
    for name, hf_id in MMU_DATASETS.items():
        print(f"  {name:20} → {hf_id}")

    print(f"\nAstroML (local):")
    for name, func in ASTROML_DATASETS.items():
        print(f"  {name:20} → {func}()")

    print(f"\nPolymathic AI (GPU required):")
    for name, info in POLYMATHIC_MODELS.items():
        print(f"  {name:20} → {info['hf_id']} ({info['params']})")
