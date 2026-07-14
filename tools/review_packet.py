#!/usr/bin/env python3
"""Build and safely reuse immutable content-addressed review packets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from paper_registry import CANONICAL_IDS, load_registry, repo_root


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def ensure_clean(root: Path, paths: list[str]) -> None:
    status = run_git(root, "status", "--porcelain", "--", *paths)
    if status:
        raise RuntimeError(f"review packet inputs are dirty:\n{status}")


def live_version(tex: Path) -> str:
    text = tex.read_text(encoding="utf-8")
    for pattern in (
        r"\\newcommand\{\\paperVersion\}\{([^}]+)\}",
        r"\\date\{[^}]*\}\s*%\s*(v[\w.\-]+)",
        r"^%\s*(v[\w.\-]+)\s*\(",
    ):
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            return match.group(1)
    raise ValueError(f"cannot determine paper version from {tex}")


def page_count(pdf: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    match = re.search(r"^Pages:\s+(\d+)$", output, re.MULTILINE)
    if not match or int(match.group(1)) < 1:
        raise ValueError(f"cannot determine positive page count for {pdf}")
    return int(match.group(1))


def packet_key(pdf_sha: str, profile: str, prompt_sha: str, model: str, effort: str) -> str:
    return sha256_bytes(f"{pdf_sha}{profile}{prompt_sha}{model}{effort}".encode())


def build_packet(
    root: Path,
    paper_id: str,
    entry: dict[str, Any],
    prompt: bytes,
    allowed_context: bytes,
    model: str,
    effort: str,
    expected_pdf_sha: str | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    tex_rel, pdf_rel = entry["tex_path"], entry["pdf_path"]
    tex, pdf = root / tex_rel, root / pdf_rel
    if not tex.is_file() or not pdf.is_file():
        raise FileNotFoundError(f"missing source/PDF for {paper_id}")
    ensure_clean(root, [tex_rel, pdf_rel])
    pdf_sha = sha256_file(pdf)
    if expected_pdf_sha is not None and pdf_sha != expected_pdf_sha:
        raise ValueError(f"PDF SHA mismatch: expected {expected_pdf_sha}, got {pdf_sha}")
    prompt_sha = sha256_bytes(prompt)
    context_sha = sha256_bytes(allowed_context)
    source_commit = run_git(root, "log", "-1", "--format=%H", "--", tex_rel)
    if not source_commit:
        raise ValueError(f"source path has no commit: {tex_rel}")
    key = packet_key(pdf_sha, entry["review_profile"], prompt_sha, model, effort)
    return {
        "schema_version": 1,
        "packet_key": key,
        "paper_id": paper_id,
        "paper_version": live_version(tex),
        "source_commit": source_commit,
        "source_path": tex_rel,
        "source_sha256": sha256_file(tex),
        "pdf_path": pdf_rel,
        "pdf_sha256": pdf_sha,
        "page_count": page_count(pdf),
        "site_slug": entry["site_slug"],
        "target_journal": entry["target_journal"],
        "article_type": entry["article_type"],
        "review_profile_id": entry["review_profile"],
        "prompt_sha256": prompt_sha,
        "allowed_context_sha256": context_sha,
        "model": model,
        "effort": effort,
    }


def publish_packet(packet: dict[str, Any], output_root: Path) -> tuple[Path, bool]:
    path = output_root / packet["paper_id"] / f"{packet['packet_key']}.json"
    encoded = (json.dumps(packet, indent=2, sort_keys=True) + "\n").encode()
    if path.exists():
        if path.read_bytes() != encoded:
            raise RuntimeError(f"cache-key collision or mutated packet: {path}")
        return path, True
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()
    return path, False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper", choices=CANONICAL_IDS)
    parser.add_argument("--prompt-file", required=True, type=Path)
    parser.add_argument("--context-file", type=Path)
    parser.add_argument("--model", required=True)
    parser.add_argument("--effort", required=True)
    parser.add_argument("--expected-pdf-sha")
    parser.add_argument("--output-root", type=Path)
    args = parser.parse_args()
    root = repo_root()
    registry = load_registry(root)
    context = args.context_file.read_bytes() if args.context_file else b""
    packet = build_packet(
        root, args.paper, registry[args.paper], args.prompt_file.read_bytes(),
        context, args.model, args.effort, args.expected_pdf_sha,
    )
    output = args.output_root or root / "project-context" / "review-packets"
    path, reused = publish_packet(packet, output)
    print(json.dumps({"path": str(path), "reused": reused, "packet": packet}, indent=2))


if __name__ == "__main__":
    main()
