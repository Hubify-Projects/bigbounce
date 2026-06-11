#!/usr/bin/env python3
"""Mechanical artifact/paper cross-check (pattern-046, EXT1 gap-mine 2026-06-10).

For a paper .tex: extract every \\artifact{...} path + bare repo paths in
Data Availability, then verify each against the working tree:
  1. EXISTS    — path resolves from repo root
  2. VERSION   — if the artifact dir has README/metadata with a version label,
                 flag labels that don't match the paper's \\paperVersion
  3. COMMIT    — any 8-40 hex "commit" reference in the .tex must be an
                 ancestor of HEAD and (warn) should equal HEAD's short hash
Usage: python3 tools/artifact_crosscheck.py <paper.tex>
Exit 1 if any MISSING/STALE found (CI-gateable).
"""
import pathlib
import re
import subprocess
import sys


def repo_root() -> pathlib.Path:
    return pathlib.Path(
        subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
    )


def main(tex_path: str) -> int:
    root = repo_root()
    tex = pathlib.Path(tex_path).read_text(errors="replace")
    problems = 0

    ver = None
    m = re.search(r"\\newcommand\{\\paperVersion\}\{([^}]+)\}", tex) or re.search(
        r"v\d+[A-Z]?\.\d+\.\d+", tex
    )
    if m:
        ver = m.group(1) if m.lastindex else m.group(0)

    paths = set(re.findall(r"\\artifact\{([^}]+)\}", tex))
    paths |= set(re.findall(r"\\(?:texttt|path|repopath)\{((?:[\w\\.-]+/)+[\w\\.-]+)\}", tex))
    paths |= set(re.findall(r"blob/main/((?:[\w.-]+/)+[\w.-]+)", tex))
    print(f"paper version: {ver} | candidate paths: {len(paths)}")

    for p in sorted(paths):
        clean = p.replace("\\_", "_").replace("\\", "")
        target = root / clean
        if not target.exists():
            print(f"MISSING  {clean}")
            problems += 1
            continue
        meta = None
        probe = target if target.is_dir() else target.parent
        for name in ("README.md", "METADATA.md", "manifest.json"):
            if (probe / name).exists():
                meta = (probe / name).read_text(errors="replace")[:4000]
                break
        if meta and ver:
            labels = re.findall(r"v\d+[A-Z]?\.\d+\.\d+", meta)
            if labels and ver not in labels:
                print(f"STALE-LABEL {clean}: metadata says {sorted(set(labels))}, paper is {ver}")
                problems += 1
        print(f"OK       {clean}")

    head = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    for h in set(re.findall(r"commit[~ `]*([0-9a-f]{8,40})", tex, re.I)):
        try:
            subprocess.check_call(
                ["git", "merge-base", "--is-ancestor", h, head],
                stderr=subprocess.DEVNULL,
            )
            if not head.startswith(h):
                print(f"WARN-OLD-COMMIT {h}: valid ancestor but not HEAD ({head[:8]}) — update at restamp")
        except subprocess.CalledProcessError:
            print(f"BAD-COMMIT {h}: not an ancestor of HEAD")
            problems += 1

    print(f"\n{'FAIL' if problems else 'PASS'}: {problems} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
