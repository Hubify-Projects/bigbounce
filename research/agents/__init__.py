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
OUTPUT_DIR = Path(os.environ.get("RESEARCH_OUTPUT_DIR", RESEARCH_DIR / "outputs"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
