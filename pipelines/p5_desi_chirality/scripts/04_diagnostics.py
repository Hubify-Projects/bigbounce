#!/usr/bin/env python3
"""Schema + provenance diagnostics for the matched catalog.

Reads the matched parquet, prints a per-column schema (dtype, nulls, basic
stats), and writes a markdown report under `results/p5_crossmatch_diagnostics.md`
that's safe to drop straight into the paper appendix.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, resolve_p5_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    matched_path = resolve_p5_path(cfg["paths"]["out_matched"])
    summary_path = resolve_p5_path(cfg["paths"]["out_summary"])
    diag_path = resolve_p5_path(cfg["paths"]["out_diagnostics"])

    if not matched_path.exists():
        print(f"ERROR: {matched_path} not present. Run scripts/03_crossmatch.py first.")
        return 2

    df = pd.read_parquet(matched_path)
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}

    lines = ["# P5 Cross-match Diagnostics", ""]
    lines.append(f"_Generated from `{matched_path.name}`._  ")
    lines.append(f"Config version: **{cfg['version']}** (hash `{cfg['_config_hash']}`)  ")
    lines.append("")

    lines.append("## Top-level counts")
    lines.append("")
    if summary:
        lines.append("```json")
        lines.append(json.dumps(summary.get("totals", {}), indent=2))
        lines.append("```")
        lines.append("")
        if "chirality_among_spirals" in summary:
            lines.append("## Chirality among matched spirals")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(summary["chirality_among_spirals"], indent=2))
            lines.append("```")
            lines.append("")

    lines.append("## Schema")
    lines.append("")
    lines.append("| Column | Dtype | Non-null | Example |")
    lines.append("|--------|-------|----------|---------|")
    for col in df.columns:
        ex = ""
        s = df[col].dropna()
        if len(s):
            v = s.iloc[0]
            ex = f"`{str(v)[:30]}`"
        lines.append(f"| `{col}` | {df[col].dtype} | {df[col].notna().sum():,} | {ex} |")
    lines.append("")

    lines.append("## Sensitivity (matches at alternate radii)")
    lines.append("")
    if "sensitivity" in summary:
        lines.append("| Radius (arcsec) | Matches |")
        lines.append("|---:|---:|")
        for k, v in summary["sensitivity"].items():
            lines.append(f"| {k.replace('arcsec_matches','')} | {v:,} |")
        lines.append("")

    lines.append("## Provenance pointer")
    lines.append("")
    lines.append(f"Sidecar: `{matched_path.name}.provenance.json`")

    diag_path.write_text("\n".join(lines))
    print(f"[done] wrote {diag_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
