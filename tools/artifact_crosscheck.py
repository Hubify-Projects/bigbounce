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
from __future__ import annotations

import pathlib
import re
import subprocess
import sys


def repo_root(root_override: pathlib.Path | None = None) -> pathlib.Path:
    if root_override is not None:
        return root_override.resolve(strict=True)
    return pathlib.Path(
        subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
    )


def main(tex_path: str, root_override: pathlib.Path | None = None) -> int:
    root = repo_root(root_override)
    tex_file = pathlib.Path(tex_path).resolve()
    tex = tex_file.read_text(errors="replace")
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
        if re.match(r"^10\.\d{4,9}/", clean):
            # DOI (e.g. 10.5281/zenodo.XXXX) — external identifier, not a repo path
            continue
        if clean == "Hubify-Projects/bigbounce" or clean.startswith("github.com/"):
            # GitHub org/repo display label, not a repo-local path
            continue
        if clean.startswith("bamfai/") or re.fullmatch(
            r"[0-9a-f]{7,12}/MANIFEST\.json", clean, re.I
        ):
            # Hugging Face display label / abbreviated immutable remote path.
            continue
        if clean.endswith(".py/json"):
            base = clean[: -len(".py/json")]
            stems = (base + ".py", base + ".json")
            matches = [
                candidate
                for stem in stems
                for candidate in root.rglob(pathlib.Path(stem).name)
                if candidate.is_file() and candidate.as_posix().endswith(stem)
            ]
            if len(matches) == 2:
                print(
                    f"RESOLVED {clean} -> "
                    + ", ".join(str(path.relative_to(root)) for path in matches)
                )
                continue
        ancestor_candidates = []
        parent = tex_file.parent
        while parent.is_relative_to(root):
            ancestor_candidates.append(parent / clean)
            if parent == root:
                break
            parent = parent.parent
        direct_candidates = tuple(ancestor_candidates)
        target = next((candidate for candidate in direct_candidates if candidate.exists()), None)
        if target is None:
            # LaTeX often displays a path relative to a base directory named in
            # the immediately preceding prose. Resolve a unique repository
            # suffix mechanically; multiple matches are retained as an
            # explicit relative-path shorthand rather than mislabeled missing.
            suffix_matches = sorted(
                candidate for candidate in root.rglob(pathlib.Path(clean).name)
                if candidate.is_file() and candidate.as_posix().endswith(clean)
            )
            if len(suffix_matches) == 1:
                target = suffix_matches[0]
                print(f"RESOLVED {clean} -> {target.relative_to(root)}")
            elif len(suffix_matches) > 1:
                print(
                    f"WARN-RELATIVE {clean}: resolves under {len(suffix_matches)} "
                    "declared/possible base directories"
                )
                continue
        if target is None:
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
                explicit_versions = re.findall(r"v\d+[A-Z]?\.\d+\.\d+", clean)
                if any(label in clean for label in labels) or explicit_versions:
                    print(
                        f"HISTORICAL-LABEL {clean}: explicitly versioned artifact "
                        f"contains {sorted(set(labels))}; paper is {ver}"
                    )
                else:
                    print(f"STALE-LABEL {clean}: metadata says {sorted(set(labels))}, paper is {ver}")
                    problems += 1
        print(f"OK       {clean}")

    head = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    for h in set(re.findall(r"commit[~ `]*(?:\\[a-z]+\{)?([0-9a-f]{8,40})\b", tex, re.I)):
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
