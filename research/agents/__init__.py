"""BigBounce Research Agents — Multi-model scientific research tools."""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    _env = Path(__file__).resolve().parent.parent.parent / ".env.local"
    if _env.exists():
        load_dotenv(_env)
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RESEARCH_DIR = PROJECT_ROOT / "research"

# RunPod workspace detection — /workspace/outputs takes priority
_env_output = os.environ.get("RESEARCH_OUTPUT_DIR", "")
if Path("/workspace").exists():
    OUTPUT_DIR = Path("/workspace/outputs")
elif _env_output:
    OUTPUT_DIR = Path(_env_output)
else:
    OUTPUT_DIR = RESEARCH_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
