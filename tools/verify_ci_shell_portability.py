#!/usr/bin/env python3
"""Fail closed on POSIX-only GitHub Actions steps that can run on Windows."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

SCHEMA = "bigbounce.ci-shell-portability/v1"
POSIX_RUN_PATTERNS = (
    re.compile(r"\$\{[A-Za-z_][A-Za-z0-9_]*\}"),
    re.compile(r"\\\s*$", re.MULTILINE),
    re.compile(r"(?:^|[;&|]\s*)(?:chmod|printf|test|rm|cp|mv|mkdir)\b", re.MULTILINE),
)


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _step_blocks(text: str) -> list[tuple[int, str]]:
    starts = list(re.finditer(r"(?m)^(\s*)-\s+name:\s*.+$", text))
    blocks: list[tuple[int, str]] = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        blocks.append((text.count("\n", 0, match.start()) + 1, text[match.start():end]))
    return blocks


def verify(root: Path, relative_paths: list[str]) -> dict[str, Any]:
    root = root.resolve(strict=True)
    if not relative_paths or len(relative_paths) != len(set(relative_paths)):
        raise ValueError("ci_shell_portability_paths must be a unique non-empty list")
    records = []
    findings = []
    for relative in sorted(relative_paths):
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise ValueError(f"unsafe workflow path: {relative!r}")
        path = (root / candidate).resolve(strict=True)
        if not path.is_file() or not path.is_relative_to(root):
            raise ValueError(f"workflow path escapes root or is not a file: {relative!r}")
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        records.append({"path": relative, "bytes": len(raw), "sha256": _sha256(raw)})
        if "windows-latest" not in text:
            continue
        for line, block in _step_blocks(text):
            run_match = re.search(r"(?m)^\s+run:\s*(?:\||>)?\s*$", block)
            if not run_match:
                continue
            shell_match = re.search(r"(?m)^\s+shell:\s*([^\s#]+)", block)
            shell = shell_match.group(1).lower() if shell_match else ""
            if shell in {"bash", "bash.exe"}:
                continue
            run_body = block[run_match.end():]
            matched = sorted({
                pattern.pattern for pattern in POSIX_RUN_PATTERNS if pattern.search(run_body)
            })
            if matched:
                name = re.search(r"(?m)^(\s*)-\s+name:\s*(.+)$", block)
                findings.append({
                    "path": relative,
                    "line": line,
                    "step": name.group(2).strip() if name else "unnamed",
                    "shell": shell or "runner-default",
                    "matched_patterns": matched,
                    "message": (
                        "POSIX-only run syntax can execute under the Windows runner's "
                        "default PowerShell; select shell: bash or use portable commands"
                    ),
                })
    result = {
        "schema": SCHEMA,
        "verdict": "PASS" if not findings else "FAIL",
        "workflows": records,
        "workflow_count": len(records),
        "findings": findings,
        "finding_count": len(findings),
    }
    result["receipt_sha256"] = _sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    )
    return result
