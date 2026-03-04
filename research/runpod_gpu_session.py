#!/usr/bin/env python3
"""
BigBounce GPU Research Session — RunPod / Local / Colab

Migrated from the Colab notebook (research/notebooks/bigbounce_gpu.ipynb).
Works on RunPod (/workspace), local machines, and Google Colab (fallback).

Usage:
    # On RunPod or local:
    python3 research/runpod_gpu_session.py

    # Or import as module:
    from research.runpod_gpu_session import run_session, detect_environment
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime


# ── Environment detection ────────────────────────────────────────────

def detect_environment() -> dict:
    """Detect whether we're on RunPod, Lambda, Colab, or local."""
    env = {
        "platform": "local",
        "gpu_available": False,
        "gpu_name": None,
        "gpu_vram_gb": None,
        "workspace_dir": None,
        "repo_dir": None,
    }

    # Check RunPod
    if Path("/workspace").exists():
        env["platform"] = "runpod"
        env["workspace_dir"] = "/workspace"
        repo = Path("/workspace/bigbounce")
        if repo.exists():
            env["repo_dir"] = str(repo)

    # Check Lambda
    elif Path("/lambda/nfs").exists():
        env["platform"] = "lambda"
        env["workspace_dir"] = "/lambda/nfs"

    # Check Colab
    elif os.environ.get("COLAB_GPU") or Path("/content").exists():
        env["platform"] = "colab"
        env["workspace_dir"] = "/content"
        repo = Path("/content/bigbounce")
        if repo.exists():
            env["repo_dir"] = str(repo)

    # Local — find repo from this file's location
    else:
        repo = Path(__file__).resolve().parent.parent
        if (repo / "arxiv").exists():
            env["repo_dir"] = str(repo)
        env["workspace_dir"] = str(repo / "research" / "outputs")

    # Check GPU
    try:
        import torch
        if torch.cuda.is_available():
            env["gpu_available"] = True
            env["gpu_name"] = torch.cuda.get_device_name(0)
            props = torch.cuda.get_device_properties(0)
            total_mem = getattr(props, 'total_memory', 0) or getattr(props, 'total_mem', 0)
            env["gpu_vram_gb"] = round(total_mem / 1e9, 1)
    except ImportError:
        pass

    return env


def load_api_keys(env: dict) -> dict:
    """Load API keys from .env.local (RunPod/local) or Colab Secrets."""
    keys = {}

    # Try .env.local first (RunPod + local)
    env_file = None
    if env.get("repo_dir"):
        env_file = Path(env["repo_dir"]) / ".env.local"

    if env_file and env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
            print(f"  Loaded keys from {env_file}")
        except ImportError:
            # Manual parse
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
            print(f"  Loaded keys from {env_file} (manual parse)")

    # Colab Secrets fallback
    elif env.get("platform") == "colab":
        try:
            from google.colab import userdata
            colab_keys = [
                "HUGGINGFACE_TOKEN", "ANTHROPIC_API_KEY",
                "GOOGLE_AI_API_KEY", "DEEPSEEK_API_KEY",
            ]
            for k in colab_keys:
                try:
                    os.environ[k] = userdata.get(k)
                except Exception:
                    pass
            print("  Loaded keys from Colab Secrets")
        except ImportError:
            print("  WARNING: No Colab Secrets available")

    # Collect loaded keys
    key_names = [
        "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "GOOGLE_AI_API_KEY",
        "DEEPSEEK_API_KEY", "XAI_API_KEY", "OPENROUTER_API_KEY",
        "NASA_ADS_API_KEY", "SEMANTIC_SCHOLAR_API_KEY",
        "PERPLEXITY_API_KEY", "WOLFRAM_ALPHA_APP_ID",
        "HUGGINGFACE_TOKEN", "FIRECRAWL_API_KEY",
    ]
    for k in key_names:
        val = os.environ.get(k, "")
        if val:
            keys[k] = val

    return keys


def save_to_workspace(data, filename: str, env: dict = None) -> str:
    """Save data to the workspace output directory."""
    if env is None:
        env = detect_environment()

    if env["platform"] == "runpod":
        out_dir = Path("/workspace/outputs")
    elif env.get("repo_dir"):
        out_dir = Path(env["repo_dir"]) / "research" / "outputs"
    else:
        out_dir = Path("./outputs")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename

    if isinstance(data, (dict, list)):
        out_path.write_text(json.dumps(data, indent=2, default=str))
    elif isinstance(data, str):
        out_path.write_text(data)
    else:
        out_path.write_text(str(data))

    print(f"  Saved: {out_path}")
    return str(out_path)


# ── GPU session cells ────────────────────────────────────────────────

def cell_0_verify_environment(env: dict) -> dict:
    """Verify GPU and environment. (Colab cell 0-1)"""
    print("\n  [0] Environment")
    print(f"      Platform:  {env['platform']}")
    print(f"      GPU:       {env['gpu_name'] or 'None'}")
    print(f"      VRAM:      {env['gpu_vram_gb'] or 0} GB")
    print(f"      Workspace: {env['workspace_dir']}")
    print(f"      Repo:      {env['repo_dir'] or 'not found'}")

    if not env["gpu_available"]:
        print("      WARNING: No GPU detected. GPU-intensive cells will be skipped.")

    return env


def cell_1_load_keys(env: dict) -> dict:
    """Load and verify API keys. (Colab cell 1)"""
    print("\n  [1] API Keys")
    keys = load_api_keys(env)
    print(f"      {len(keys)} keys loaded")
    for k in sorted(keys.keys()):
        v = keys[k]
        masked = v[:6] + "..." + v[-3:] if len(v) > 12 else v[:4] + "..."
        print(f"      {k}: {masked}")
    return keys


def cell_2_clone_repo(env: dict) -> str:
    """Clone BigBounce repo if needed. (Colab cell 2)"""
    print("\n  [2] Repository")

    if env.get("repo_dir") and Path(env["repo_dir"]).exists():
        print(f"      Already available at {env['repo_dir']}")
        # Add to sys.path
        if env["repo_dir"] not in sys.path:
            sys.path.insert(0, env["repo_dir"])
        return env["repo_dir"]

    # Clone on RunPod/Colab
    target = None
    if env["platform"] == "runpod":
        target = "/workspace/bigbounce"
    elif env["platform"] == "colab":
        target = "/content/bigbounce"

    if target:
        if not Path(target).exists():
            print(f"      Cloning to {target}...")
            os.system(
                f"git clone https://github.com/Hubify-Projects/bigbounce.git {target} 2>&1"
            )
        env["repo_dir"] = target
        sys.path.insert(0, target)
        print(f"      Repo at {target}")
        return target

    print("      WARNING: Could not locate or clone repo")
    return None


def cell_3_import_agents(env: dict) -> dict:
    """Import research agents. (Colab cell 3)"""
    print("\n  [3] Research Agents")
    agents = {}

    try:
        from research.agents.dataset_loaders import (
            load_mmu, load_astroml, load_polymathic,
            list_mmu_datasets, list_astroml_datasets, list_polymathic_models,
        )
        agents["dataset_loaders"] = True
        print(f"      dataset_loaders: OK")
        print(f"      MMU datasets: {list(list_mmu_datasets().keys())}")
        print(f"      Polymathic models: {list_polymathic_models()}")
    except Exception as e:
        agents["dataset_loaders"] = False
        print(f"      dataset_loaders: FAILED ({e})")

    try:
        from research.agents.data_access import search_jwst, search_gaia
        agents["data_access"] = True
        print(f"      data_access: OK")
    except Exception as e:
        agents["data_access"] = False
        print(f"      data_access: FAILED ({e})")

    try:
        from research.agents.computation import deepseek_verify
        agents["computation"] = True
        print(f"      computation: OK")
    except Exception as e:
        agents["computation"] = False
        print(f"      computation: FAILED ({e})")

    try:
        from research.agents.reasoning_router import query
        agents["reasoning_router"] = True
        print(f"      reasoning_router: OK")
    except Exception as e:
        agents["reasoning_router"] = False
        print(f"      reasoning_router: FAILED ({e})")

    return agents


def cell_4_load_walrus(env: dict) -> object:
    """Load Polymathic AI Walrus model (1.3B). (Colab cell 5)"""
    print("\n  [4] Polymathic AI — Walrus (1.3B)")

    if not env["gpu_available"]:
        print("      SKIPPED: No GPU available")
        return None

    if (env.get("gpu_vram_gb") or 0) < 4:
        print("      SKIPPED: Need 4+ GB VRAM")
        return None

    try:
        import torch
        from huggingface_hub import hf_hub_download
        hf_token = os.environ.get("HUGGINGFACE_TOKEN", "")
        print("      Downloading Walrus weights from HuggingFace...")

        # Walrus uses custom architecture — download weights directly
        # (pip install walrus is the WRONG package — it's a Redis wrapper)
        try:
            weights_path = hf_hub_download(
                "polymathic-ai/walrus", "pytorch_model.bin",
                token=hf_token if hf_token else None,
            )
            weights = torch.load(weights_path, map_location="cuda")
            params = sum(v.numel() for v in weights.values())
            print(f"      Weights loaded on CUDA")
            print(f"      Parameters: {params:,}")
            print(f"      Keys: {list(weights.keys())[:5]}...")
            del weights
            torch.cuda.empty_cache()
            return {"status": "ok", "params": params, "weights_path": weights_path}
        except Exception as e1:
            print(f"      Direct weight load failed: {e1}")
            # Try safetensors format
            try:
                weights_path = hf_hub_download(
                    "polymathic-ai/walrus", "model.safetensors",
                    token=hf_token if hf_token else None,
                )
                from safetensors.torch import load_file
                weights = load_file(weights_path, device="cuda")
                params = sum(v.numel() for v in weights.values())
                print(f"      Safetensors loaded on CUDA")
                print(f"      Parameters: {params:,}")
                del weights
                torch.cuda.empty_cache()
                return {"status": "ok", "params": params}
            except Exception as e2:
                print(f"      Safetensors also failed: {e2}")
                return None
    except Exception as e:
        print(f"      FAILED: {e}")
        return None


def cell_5_plasticc(env: dict) -> dict:
    """Stream PLAsTiCC light curves. (Colab cell 7)"""
    print("\n  [5] PLAsTiCC Light Curves (streaming)")

    try:
        from research.agents.dataset_loaders import load_mmu
        ds = load_mmu("plasticc", streaming=True, max_samples=100)
        sample = next(iter(ds))
        print(f"      Sample keys: {list(sample.keys())}")
        print(f"      Target: {sample.get('target', 'N/A')}")
        return {"status": "ok", "keys": list(sample.keys())}
    except Exception as e:
        print(f"      FAILED: {e}")
        return {"status": "failed", "error": str(e)}


def cell_6_jwst_ceers(env: dict) -> dict:
    """Stream JWST CEERS galaxy images. (Colab cell 8)"""
    print("\n  [6] JWST CEERS Galaxy Images (streaming)")

    try:
        from research.agents.dataset_loaders import load_mmu
        ds = load_mmu("jwst_ceers", streaming=True, max_samples=10)
        sample = next(iter(ds))
        print(f"      Sample keys: {list(sample.keys())}")
        return {"status": "ok", "keys": list(sample.keys())}
    except Exception as e:
        print(f"      FAILED: {e}")
        return {"status": "failed", "error": str(e)}


def cell_7_sdss_spectra(env: dict) -> dict:
    """Load SDSS spectra via AstroML. (Colab cell 9)"""
    print("\n  [7] SDSS Spectra (AstroML)")

    try:
        from research.agents.dataset_loaders import load_astroml
        spectra = load_astroml("sdss_spectra")
        print(f"      Shape: {spectra.shape}")
        print(f"      Columns: {spectra.dtype.names[:10]}...")
        return {"status": "ok", "shape": spectra.shape}
    except Exception as e:
        print(f"      FAILED: {e}")
        return {"status": "failed", "error": str(e)}


def cell_8_jwst_query(env: dict) -> dict:
    """Query JWST observations. (Colab cell 11)"""
    print("\n  [8] JWST Observations — NGC 1365")

    try:
        from research.agents.data_access import search_jwst
        obs = search_jwst("NGC 1365", radius_arcmin=5)
        print(f"      Found {len(obs)} observations")
        for o in obs[:5]:
            print(f"        {o['obs_id']}: {o['instrument']} {o['filters']} ({o['exposure_time']:.0f}s)")
        return {"status": "ok", "count": len(obs)}
    except Exception as e:
        print(f"      FAILED: {e}")
        return {"status": "failed", "error": str(e)}


def cell_9_gaia(env: dict) -> dict:
    """Query Gaia DR3 near Galactic Center. (Colab cell 12)"""
    print("\n  [9] Gaia DR3 — Galactic Center")

    try:
        from research.agents.data_access import search_gaia
        stars = search_gaia(ra=266.4, dec=-29.0, radius_deg=0.1, max_results=20)
        print(f"      Found {len(stars)} sources")
        for s in stars[:5]:
            print(f"        Gaia {s['source_id']}: G={s['phot_g_mean_mag']:.2f}, parallax={s['parallax']:.3f} mas")
        return {"status": "ok", "count": len(stars)}
    except Exception as e:
        print(f"      FAILED: {e}")
        return {"status": "failed", "error": str(e)}


def cell_10_cmb_parity(env: dict) -> dict:
    """Template: CMB parity analysis data retrieval. (Colab cell 14)"""
    print("\n  [10] CMB Parity Analysis (template)")

    try:
        from research.agents.data_access import search_mast
        planck = search_mast(target="Planck", collection="Planck")
        print(f"      Planck products in MAST: {len(planck)}")
        return {"status": "ok", "count": len(planck)}
    except Exception as e:
        print(f"      FAILED: {e}")
        return {"status": "failed", "error": str(e)}


def cell_11_deepseek_verify(env: dict) -> dict:
    """Cross-check equations with DeepSeek R1. (Colab cell 15)"""
    print("\n  [11] DeepSeek R1 Equation Verification")

    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("      SKIPPED: DEEPSEEK_API_KEY not set")
        return {"status": "skipped"}

    try:
        from research.agents.computation import deepseek_verify
        result = deepseek_verify(
            claim=(
                "The inflationary suppression factor D_inf = e^{-3N}(T_reh/M_GUT)^{3/2} "
                "gives D_inf ~ 10^{-121} for N=92, T_reh=10^{15} GeV, M_GUT=10^{16} GeV"
            ),
            context=(
                "Einstein-Cartan cosmology with Holst term, evaluating parity-odd "
                "operator on-shell during inflation"
            ),
        )
        print(f"      Verdict: {result['verdict']}")
        print(f"      {result['content'][:200]}...")
        return {"status": "ok", "verdict": result["verdict"]}
    except Exception as e:
        print(f"      FAILED: {e}")
        return {"status": "failed", "error": str(e)}


# ── Session runner ───────────────────────────────────────────────────

def run_session(cells: list = None) -> dict:
    """Run a full GPU research session.

    Args:
        cells: List of cell numbers to run (default: all). Example: [0, 1, 4]

    Returns:
        dict with results from each cell
    """
    print("\n  BigBounce GPU Research Session")
    print("  " + "=" * 50)
    print(f"  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    all_cells = [
        (0, cell_0_verify_environment),
        (1, cell_1_load_keys),
        (2, cell_2_clone_repo),
        (3, cell_3_import_agents),
        (4, cell_4_load_walrus),
        (5, cell_5_plasticc),
        (6, cell_6_jwst_ceers),
        (7, cell_7_sdss_spectra),
        (8, cell_8_jwst_query),
        (9, cell_9_gaia),
        (10, cell_10_cmb_parity),
        (11, cell_11_deepseek_verify),
    ]

    env = detect_environment()
    results = {}

    for num, func in all_cells:
        if cells and num not in cells:
            continue

        try:
            if num <= 1:
                result = func(env)
            elif num == 2:
                result = func(env)
            elif num == 3:
                result = func(env)
            else:
                result = func(env)
            results[f"cell_{num}"] = result
        except Exception as e:
            print(f"\n  [ERROR] Cell {num} failed: {e}")
            results[f"cell_{num}"] = {"error": str(e)}

    # Save session report
    report = {
        "timestamp": datetime.now().isoformat(),
        "environment": env,
        "results": {k: str(v)[:200] for k, v in results.items()},
    }
    save_to_workspace(report, f"gpu_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", env)

    print(f"\n  Session complete. {len(results)} cells executed.")
    return results


# ── CLI ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    # Parse cell numbers from args
    cells = None
    if len(sys.argv) > 1:
        try:
            cells = [int(x) for x in sys.argv[1:]]
        except ValueError:
            pass

    run_session(cells=cells)
