#!/usr/bin/env python3
"""Append-only, content-addressed retention for the six canonical paper PDFs.

This tool never removes or overwrites an archive object or manifest.  It reads
each source PDF once, hashes those exact bytes, stores one object per SHA-256,
and writes a unique manifest containing version and Git provenance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


CANONICAL_IDS = ("P1A", "P1B", "P2", "P3", "P4", "P5")
DEFAULT_ARCHIVE = Path("project-context/pdf-archive")
LOCAL_ZONE = ZoneInfo("America/Los_Angeles")
LEGACY_RECOVERY_PATHS = (
    "arxiv/paper3_anomaly_catalog.pdf",
    "arxiv/paper4_chirality_catalog.pdf",
    "public/papers/anomaly_catalog_paper.pdf",
)
VERSION_PATTERNS = (
    re.compile(r"\\(?:newcommand|renewcommand)\s*\{\\paperVersion\}\s*\{([^}]+)\}"),
    re.compile(r"\\def\s*\\paperVersion\s*\{([^}]+)\}"),
    re.compile(r"\\preprint\s*\{([^}]+)\}"),
)


class RetentionError(RuntimeError):
    """Raised when append-only retention cannot be proved safe."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def md5_bytes(payload: bytes) -> str:
    return hashlib.md5(payload).hexdigest()  # noqa: S324 - compatibility receipt only


def pdf_page_count(payload: bytes) -> int:
    """Read page count from the exact captured bytes, failing closed."""
    result = subprocess.run(
        ["pdfinfo", "-"],
        input=payload,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RetentionError(f"pdfinfo failed: {detail or 'unknown error'}")
    text = result.stdout.decode("utf-8", errors="replace")
    match = re.search(r"^Pages:\s+(\d+)\s*$", text, re.MULTILINE)
    if not match or int(match.group(1)) < 1:
        raise RetentionError("pdfinfo returned no positive page count")
    return int(match.group(1))


def run_git(root: Path, *args: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def git_changed(root: Path, *args: str) -> bool | None:
    """Return Git's quiet-diff result without conflating changes with errors."""
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return False
    if result.returncode == 1:
        return True
    return None


def git_path_provenance(root: Path, relative_path: str) -> dict[str, Any]:
    tracked = run_git(root, "ls-files", "--error-unmatch", "--", relative_path) is not None
    index_dirty = None
    worktree_dirty = None
    if tracked:
        index_dirty = git_changed(root, "diff", "--cached", "--quiet", "--", relative_path)
        worktree_dirty = git_changed(root, "diff", "--quiet", "--", relative_path)
    return {
        "tracked": tracked,
        "index_dirty": index_dirty,
        "worktree_dirty": worktree_dirty,
        "overall_dirty": (index_dirty or worktree_dirty) if tracked else None,
        "head_blob": run_git(root, "rev-parse", f"HEAD:{relative_path}") if tracked else None,
    }


def paper_version(tex_path: Path) -> str:
    text = tex_path.read_text(encoding="utf-8", errors="replace")
    for pattern in VERSION_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1).strip()
    raise RetentionError(f"paper version not found in {tex_path}")


def load_registry(root: Path) -> dict[str, dict[str, Any]]:
    path = root / "project-context/paper_registry.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    papers = payload.get("papers")
    if not isinstance(papers, dict) or tuple(papers) != CANONICAL_IDS:
        raise RetentionError(f"registry must own exactly {CANONICAL_IDS}")
    for paper_id, entry in papers.items():
        for field in ("tex_path", "pdf_path"):
            candidate = root / entry.get(field, "")
            if not candidate.is_file():
                raise RetentionError(f"{paper_id} {field} missing: {candidate}")
    return papers


def write_exclusive(path: Path, payload: bytes, *, mode: int = 0o444) -> None:
    """Create ``path`` atomically and fail rather than overwrite it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.parent / f".{path.name}.{os.getpid()}.{secrets.token_hex(4)}.tmp"
    try:
        with temp.open("xb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp, mode)
        try:
            os.link(temp, path)
        except FileExistsError as exc:
            raise RetentionError(f"refusing to overwrite existing path: {path}") from exc
    finally:
        temp.unlink(missing_ok=True)


def retain_object(archive: Path, digest: str, payload: bytes) -> tuple[Path, bool]:
    object_path = archive / "objects" / "sha256" / digest[:2] / f"{digest}.pdf"
    if object_path.exists():
        existing = object_path.read_bytes()
        if sha256_bytes(existing) != digest or existing != payload:
            raise RetentionError(f"archive object collision/corruption: {object_path}")
        return object_path, False
    write_exclusive(object_path, payload)
    if sha256_bytes(object_path.read_bytes()) != digest:
        raise RetentionError(f"post-write hash mismatch: {object_path}")
    return object_path, True


def safe_component(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    if not cleaned:
        raise RetentionError(f"unsafe empty reference component derived from {value!r}")
    return cleaned


def retain_reference(object_path: Path, reference_path: Path, digest: str) -> bool:
    """Create one immutable human-readable hard link to an archive object."""
    reference_path.parent.mkdir(parents=True, exist_ok=True)
    if reference_path.exists():
        if sha256_bytes(reference_path.read_bytes()) != digest:
            raise RetentionError(f"reference collision/corruption: {reference_path}")
        if not reference_path.samefile(object_path):
            raise RetentionError(f"reference is not hard-linked to object: {reference_path}")
        return False
    try:
        os.link(object_path, reference_path)
    except FileExistsError:
        if sha256_bytes(reference_path.read_bytes()) != digest or not reference_path.samefile(object_path):
            raise RetentionError(f"reference race/collision: {reference_path}")
        return False
    return True


def relative_or_absolute(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def legacy_recovery(root: Path) -> list[dict[str, Any]]:
    rows = []
    for relative_path in LEGACY_RECOVERY_PATHS:
        deletion_log = run_git(
            root,
            "log",
            "--all",
            "--diff-filter=D",
            "--format=%H %aI",
            "--",
            relative_path,
        )
        rows.append(
            {
                "path": relative_path,
                "present": (root / relative_path).is_file(),
                **git_path_provenance(root, relative_path),
                "historical_deletion_events": [line for line in (deletion_log or "").splitlines() if line],
            }
        )
    return rows


def snapshot(
    root: Path,
    archive: Path,
    paper_ids: tuple[str, ...],
    *,
    captured_at: datetime,
    run_id: str,
    build_command: str | None = None,
    review_round: str | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    root = root.resolve()
    archive = archive if archive.is_absolute() else root / archive
    archive = archive.resolve()
    papers = load_registry(root)
    head = run_git(root, "rev-parse", "HEAD")
    entries = []
    local = captured_at.astimezone(LOCAL_ZONE)
    local_stamp = local.strftime("%Y-%m-%dT%H%M%S%z-%Z")

    for paper_id in paper_ids:
        entry = papers[paper_id]
        pdf_rel = entry["pdf_path"]
        tex_rel = entry["tex_path"]
        pdf_path = root / pdf_rel
        payload = pdf_path.read_bytes()
        if not payload.startswith(b"%PDF-"):
            raise RetentionError(f"not a PDF: {pdf_path}")
        digest = sha256_bytes(payload)
        version = paper_version(root / tex_rel)
        pages = pdf_page_count(payload)
        object_path = archive / "objects" / "sha256" / digest[:2] / f"{digest}.pdf"
        created = not object_path.exists()
        reference_name = (
            f"{safe_component(paper_id)}__{safe_component(version)}__"
            f"{local_stamp}__{digest[:12]}.pdf"
        )
        reference_path = archive / "refs" / safe_component(paper_id) / reference_name
        reference_created = not reference_path.exists()
        if not dry_run:
            object_path, created = retain_object(archive, digest, payload)
            reference_created = retain_reference(object_path, reference_path, digest)
        source_stat = pdf_path.stat()
        entries.append(
            {
                "paper_id": paper_id,
                "paper_version": version,
                "source_pdf": pdf_rel,
                "source_tex": tex_rel,
                "sha256": digest,
                "md5": md5_bytes(payload),
                "page_count": pages,
                "size_bytes": len(payload),
                "source_mtime_ns": source_stat.st_mtime_ns,
                "archive_object": relative_or_absolute(object_path, root),
                "object_created": created,
                "archive_reference": relative_or_absolute(reference_path, root),
                "reference_created": reference_created,
                "git": git_path_provenance(root, pdf_rel),
            }
        )

    manifest = {
        "schema": "bigbounce-pdf-retention/v3",
        "run_id": run_id,
        "captured_at_utc": captured_at.astimezone(timezone.utc).isoformat(),
        "captured_at_local": local.isoformat(),
        "build_command": build_command,
        "review_round": review_round,
        "git_head": head,
        "complete_six_paper_snapshot": tuple(paper_ids) == CANONICAL_IDS,
        "papers": entries,
        "legacy_recovery": legacy_recovery(root),
    }
    stamp = captured_at.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    manifest_path = archive / "manifests" / stamp[:4] / stamp[4:6] / f"{stamp}-{run_id}.json"
    manifest["manifest_path"] = relative_or_absolute(manifest_path, root)
    if not dry_run:
        encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
        write_exclusive(manifest_path, encoded)
    return manifest


def parse_timestamp(value: str | None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise RetentionError("--timestamp must include a timezone")
    return parsed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--archive-root", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--paper", action="append", choices=CANONICAL_IDS)
    parser.add_argument("--timestamp", help="ISO-8601 timestamp; defaults to now")
    parser.add_argument("--run-id", default=None, help="unique manifest suffix")
    parser.add_argument("--build-command", help="repeatable build command that produced the PDFs")
    parser.add_argument("--review-round", help="review-round identifier associated with this snapshot")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    paper_ids = tuple(args.paper) if args.paper else CANONICAL_IDS
    if len(paper_ids) != len(set(paper_ids)):
        parser.error("--paper values must be unique")
    run_id = args.run_id or secrets.token_hex(6)
    try:
        result = snapshot(
            args.root,
            args.archive_root,
            paper_ids,
            captured_at=parse_timestamp(args.timestamp),
            run_id=run_id,
            build_command=args.build_command,
            review_round=args.review_round,
            dry_run=args.dry_run,
        )
    except (OSError, ValueError, RetentionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
