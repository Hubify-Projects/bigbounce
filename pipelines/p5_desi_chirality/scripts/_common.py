"""Shared utilities for P5 scripts.

Reproducibility-first: every script imports `load_config`, `git_sha`,
`config_hash`, `write_provenance`, and uses them on every output.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

import yaml

P5_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = P5_DIR.parents[1]


def load_config(path: str | Path | None = None) -> dict:
    cfg_path = Path(path) if path else P5_DIR / "config" / "p5_config.yaml"
    with cfg_path.open("r") as f:
        cfg = yaml.safe_load(f)
    cfg["_config_path"] = str(cfg_path.resolve())
    cfg["_config_hash"] = config_hash(cfg_path)
    return cfg


def config_hash(path: str | Path) -> str:
    h = hashlib.sha256()
    h.update(Path(path).read_bytes())
    return h.hexdigest()[:16]


def git_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()[:12]
    except Exception:
        return "unknown"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_provenance(output_path: str | Path, payload: Mapping[str, Any]) -> Path:
    output_path = Path(output_path)
    sidecar = output_path.with_suffix(output_path.suffix + ".provenance.json")
    base = {
        "output": str(output_path.name),
        "written_utc": utc_now(),
        "git_sha": git_sha(),
        "python": sys.version.split()[0],
    }
    base.update(payload)
    sidecar.write_text(json.dumps(base, indent=2, default=str))
    return sidecar


def sha256_of_file(path: str | Path, chunk: int = 8 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            buf = f.read(chunk)
            if not buf:
                break
            h.update(buf)
    return h.hexdigest()


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def resolve_p5_path(rel: str) -> Path:
    """Resolve a path relative to the P5 pipeline directory."""
    return (P5_DIR / rel).resolve()
