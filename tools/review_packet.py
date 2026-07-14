#!/usr/bin/env python3
"""Build and safely reuse immutable content-addressed review packets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
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


def review_cache_root() -> Path:
    return Path(
        os.environ.get(
            "BIGBOUNCE_REVIEW_CACHE",
            Path.home() / ".cache/bigbounce/review-packets",
        )
    ).expanduser()


def packet_key(
    pdf_sha: str,
    profile: str,
    prompt_sha: str,
    context_sha: str,
    model: str,
    effort: str,
) -> str:
    fields = {
        "pdf_sha256": pdf_sha, "review_profile_id": profile,
        "prompt_sha256": prompt_sha,
        "allowed_context_sha256": context_sha,
        "model": model, "effort": effort,
    }
    return sha256_bytes(json.dumps(fields, sort_keys=True, separators=(",", ":")).encode())


def freeze_pdf(pdf: Path, cache_root: Path) -> tuple[str, str]:
    content = pdf.read_bytes()
    digest = sha256_bytes(content)
    path = cache_root / "pdf" / f"{digest}.pdf"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if sha256_file(path) != digest:
            raise RuntimeError(f"corrupt cached PDF snapshot: {path}")
    else:
        fd, name = tempfile.mkstemp(prefix=f".{digest}.", dir=path.parent)
        temporary = Path(name)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(content); handle.flush(); os.fsync(handle.fileno())
            os.replace(temporary, path)
        finally:
            if temporary.exists(): temporary.unlink()
    if sha256_file(pdf) != digest:
        raise RuntimeError("canonical PDF changed while snapshotting")
    return digest, path.relative_to(cache_root).as_posix()


def resolve_pdf_snapshot(packet: dict[str, Any], cache_root: Path | None = None) -> Path:
    cache_root = cache_root or review_cache_root()
    relative = Path(packet["pdf_snapshot_path"])
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"unsafe PDF snapshot cache path: {relative}")
    path = cache_root / relative
    if not path.is_file() or sha256_file(path) != packet["pdf_sha256"]:
        raise RuntimeError(f"missing or corrupt cached PDF snapshot: {path}")
    return path


def build_packet(
    root: Path,
    paper_id: str,
    entry: dict[str, Any],
    prompt: bytes,
    allowed_context: bytes,
    model: str,
    effort: str,
    expected_pdf_sha: str | None = None,
    cache_root: Path | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    tex_rel, pdf_rel = entry["tex_path"], entry["pdf_path"]
    tex, pdf = root / tex_rel, root / pdf_rel
    if not tex.is_file() or not pdf.is_file():
        raise FileNotFoundError(f"missing source/PDF for {paper_id}")
    ensure_clean(root, [tex_rel, pdf_rel])
    source_sha = sha256_file(tex)
    cache_root = cache_root or review_cache_root()
    pdf_sha, snapshot = freeze_pdf(pdf, cache_root)
    ensure_clean(root, [tex_rel, pdf_rel])
    if sha256_file(tex) != source_sha:
        raise RuntimeError("canonical source changed while snapshotting")
    if expected_pdf_sha is not None and pdf_sha != expected_pdf_sha:
        raise ValueError(f"PDF SHA mismatch: expected {expected_pdf_sha}, got {pdf_sha}")
    prompt_sha = sha256_bytes(prompt)
    context_sha = sha256_bytes(allowed_context)
    source_last_commit = run_git(root, "log", "-1", "--format=%H", "--", tex_rel)
    if not source_last_commit:
        raise ValueError(f"source path has no commit: {tex_rel}")
    key = packet_key(
        pdf_sha, entry["review_profile"], prompt_sha, context_sha, model, effort,
    )
    snapshot_path = resolve_pdf_snapshot(
        {"pdf_snapshot_path": snapshot, "pdf_sha256": pdf_sha}, cache_root,
    )
    return {
        "schema_version": 2,
        "packet_key": key,
        "paper_id": paper_id,
        "paper_version": live_version(tex),
        "repository_head": run_git(root, "rev-parse", "HEAD"),
        "source_commit": source_last_commit,
        "source_last_commit": source_last_commit,
        "source_path": tex_rel,
        "source_sha256": source_sha,
        "pdf_path": pdf_rel,
        "pdf_sha256": pdf_sha,
        "pdf_snapshot_path": str(snapshot),
        "page_count": page_count(snapshot_path),
        "site_slug": entry["site_slug"],
        "target_journal": entry["target_journal"],
        "article_type": entry["article_type"],
        "review_profile_id": entry["review_profile"],
        "prompt_sha256": prompt_sha,
        "allowed_context_sha256": context_sha,
        "model": model,
        "effort": effort,
    }


def publish_packet(packet: dict[str, Any], output_root: Path, prompt: bytes, context: bytes) -> tuple[Path, bool]:
    parent = output_root / packet["paper_id"]
    packet_dir = parent / packet["packet_key"]
    path = packet_dir / "packet.json"
    encoded = (json.dumps(packet, indent=2, sort_keys=True) + "\n").encode()
    files = {
        "packet.json": encoded,
        "prompt.bin": prompt,
        "allowed-context.bin": context,
    }

    def verify_existing() -> tuple[Path, bool]:
        for name, expected in files.items():
            candidate = packet_dir / name
            if not candidate.is_file() or candidate.read_bytes() != expected:
                raise RuntimeError(f"cache-key collision or incomplete packet: {packet_dir}")
        return path, True

    if packet_dir.exists():
        return verify_existing()
    parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{packet['packet_key']}.", dir=parent))
    try:
        for name, content in files.items():
            with (temporary / name).open("wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
        try:
            os.replace(temporary, packet_dir)
        except OSError:
            if packet_dir.exists():
                return verify_existing()
            raise
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
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
    cache_root = review_cache_root()
    packet = build_packet(
        root, args.paper, registry[args.paper], args.prompt_file.read_bytes(),
        context, args.model, args.effort, args.expected_pdf_sha,
        cache_root,
    )
    output = args.output_root or cache_root / "packets"
    path, reused = publish_packet(packet, output, args.prompt_file.read_bytes(), context)
    print(json.dumps({"path": str(path), "reused": reused, "packet": packet}, indent=2))


if __name__ == "__main__":
    main()
