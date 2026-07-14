#!/usr/bin/env python3
"""Validated access to the canonical six-paper campaign registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


CANONICAL_IDS = ("P1A", "P1B", "P2", "P3", "P4", "P5")
REQUIRED_FIELDS = (
    "tex_path", "pdf_path", "site_slug", "target_journal",
    "article_type", "review_profile",
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def registry_path(root: Path | None = None) -> Path:
    return (root or repo_root()) / "project-context" / "paper_registry.json"


def load_registry(root: Path | None = None, *, require_paths: bool = True) -> dict[str, dict[str, Any]]:
    root = (root or repo_root()).resolve()
    payload = json.loads(registry_path(root).read_text(encoding="utf-8"))
    papers = payload.get("papers")
    if not isinstance(papers, dict) or tuple(papers) != CANONICAL_IDS:
        raise ValueError(f"registry must own exactly {CANONICAL_IDS}")
    slugs = []
    for paper_id, entry in papers.items():
        missing = [field for field in REQUIRED_FIELDS if not entry.get(field)]
        if missing:
            raise ValueError(f"{paper_id} missing registry fields: {missing}")
        slugs.append(entry["site_slug"])
        if require_paths:
            for field in ("tex_path", "pdf_path"):
                path = root / entry[field]
                if not path.is_file():
                    raise FileNotFoundError(f"{paper_id} {field} not found: {path}")
    if len(slugs) != len(set(slugs)):
        raise ValueError("registry site slugs must be unique")
    if papers["P3"]["tex_path"] != "pipelines/p3_anomaly_engine/paper3_apjs.tex":
        raise ValueError("P3 must map to paper3_apjs.tex")
    if papers["P3"]["pdf_path"] != "pipelines/p3_anomaly_engine/paper3_apjs.pdf":
        raise ValueError("P3 must map to paper3_apjs.pdf")
    return papers


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper", choices=CANONICAL_IDS)
    parser.add_argument("field", choices=REQUIRED_FIELDS)
    parser.add_argument("--absolute", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    value = load_registry(root)[args.paper][args.field]
    if args.absolute and args.field in ("tex_path", "pdf_path"):
        value = str(root / value)
    print(value)


if __name__ == "__main__":
    main()
