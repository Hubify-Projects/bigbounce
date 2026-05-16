#!/usr/bin/env python3
"""Fetch the P4 chirality catalog (8,474,531 rows) from HuggingFace.

Uses huggingface_hub.hf_hub_download with the immutable revision tag pinned
in `config/p5_config.yaml`. Writes a provenance sidecar with SHA-256 +
row count + revision.

Usage:
    python scripts/01_fetch_p4_catalog.py
    python scripts/01_fetch_p4_catalog.py --force   # re-download
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, write_provenance, sha256_of_file, ensure_dir, resolve_p5_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    cfg = load_config(args.config)
    out_path = resolve_p5_path(cfg["paths"]["p4_catalog"])
    ensure_dir(out_path.parent)

    if out_path.exists() and not args.force:
        print(f"[ok] {out_path} already present; --force to re-download.")
        return 0

    try:
        from huggingface_hub import hf_hub_download
    except ImportError:
        print("ERROR: huggingface_hub not installed. `pip install huggingface_hub`.")
        return 2

    repo = cfg["sources"]["p4"]["hf_repo"]
    fname = cfg["sources"]["p4"]["hf_file"]
    revision = cfg["sources"]["p4"]["hf_revision"]
    expected_rows = int(cfg["sources"]["p4"]["expected_rows"])

    token = os.environ.get("HF_TOKEN")
    print(f"[fetch] {repo}/{fname}@{revision} -> {out_path}")
    cached = hf_hub_download(
        repo_id=repo,
        filename=fname,
        revision=revision,
        repo_type="dataset",
        token=token,
    )
    shutil.copy(cached, out_path)

    # Row-count verification
    try:
        import pyarrow.parquet as pq
        n_rows = pq.read_metadata(out_path).num_rows
    except ImportError:
        n_rows = None

    if n_rows is not None and n_rows != expected_rows:
        print(
            f"WARNING: row mismatch — expected {expected_rows:,}, got {n_rows:,}. "
            "The HF revision may have moved. Bump config.version if intentional."
        )

    sha = sha256_of_file(out_path)
    write_provenance(out_path, {
        "source": "huggingface",
        "hf_repo": repo,
        "hf_file": fname,
        "hf_revision": revision,
        "sha256": sha,
        "rows_observed": n_rows,
        "rows_expected": expected_rows,
        "config_version": cfg["version"],
        "config_hash": cfg["_config_hash"],
    })
    print(f"[done] sha256={sha[:16]}... rows={n_rows} expected={expected_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
