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
PATH_VERSION_PATTERNS = (
    re.compile(r"(v1A\.0\.\d+)", re.IGNORECASE),
    re.compile(r"(v1B\.0\.\d+)", re.IGNORECASE),
    re.compile(r"(v\d+\.\d+\.\d+(?:-r\d+)?)", re.IGNORECASE),
    re.compile(r"(v\d+\.\d+\.\d+-\d{4}-\d{2}-\d{2})", re.IGNORECASE),
)
HISTORY_PAPER_HINTS = {
    "P1A": (
        "paper1a_ech_nogo",
        "p1a_",
        "/p1a/",
        "p1a-",
    ),
    "P1B": (
        "paper1b_mcmc_companion",
        "p1b_",
        "/p1b/",
        "p1b-",
    ),
    "P2": (
        "02_full_draft",
        "focused_paper_source_integration",
        "focused_paper_bounce_fnl_forecast",
        "fnl-forecast-paper",
        "/p2/",
        "paper2_",
    ),
    "P3": (
        "paper3_apjs",
        "paper3_draft",
        "paper3_anomaly_catalog",
        "anomaly_catalog_paper",
        "anomaly-catalog-paper",
        "/p3/",
        "p3_",
    ),
    "P4": (
        "chirality_catalog_paper",
        "paper4_chirality_catalog",
        "p4_chirality_catalog_paper",
        "/p4/",
        "p4_",
    ),
    "P5": (
        "p5_desi_chirality",
        "p5-chirality",
        "/p5/",
        "p5_",
    ),
}


class RetentionError(RuntimeError):
    """Raised when append-only retention cannot be proved safe."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def md5_bytes(payload: bytes) -> str:
    return hashlib.md5(payload).hexdigest()  # noqa: S324 - compatibility receipt only


def pdf_page_count(payload: bytes) -> int:
    """Read page count from the exact captured bytes, failing closed."""
    try:
        result = subprocess.run(
            ["pdfinfo", "-"],
            input=payload,
            check=False,
            capture_output=True,
            timeout=20,
        )
    except subprocess.TimeoutExpired as exc:
        raise RetentionError("pdfinfo timed out after 20 seconds") from exc
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


def run_git_bytes(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RetentionError(f"git {' '.join(args)} failed: {detail or 'unknown error'}")
    return result.stdout


def git_object_size(root: Path, git_blob: str) -> int | None:
    size = run_git(root, "cat-file", "-s", git_blob)
    if size is None:
        return None
    try:
        return int(size)
    except ValueError:
        return None


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


def infer_path_version(path: str) -> str:
    name = Path(path).name
    for pattern in PATH_VERSION_PATTERNS:
        match = pattern.search(name)
        if match:
            return match.group(1)
    return "unknown"


def classify_history_pdf(path: str) -> tuple[str | None, str]:
    normalized = "/" + path.lower()
    basename = Path(path).name.lower()
    if "/figures/" in normalized or "/render/" in normalized:
        return None, "excluded.figure-or-render-artifact"
    if "/pdf-archive/" in normalized:
        return None, "excluded.archive-self-reference"
    matches: list[str] = []
    for paper_id, hints in HISTORY_PAPER_HINTS.items():
        if any(hint.lower() in normalized or hint.lower() in basename for hint in hints):
            matches.append(paper_id)
    if len(matches) == 1:
        return matches[0], "matched.high-confidence-path"
    if len(matches) > 1:
        return None, f"ambiguous.paper-hints.{','.join(matches)}"
    return None, "unclassified.no-paper-hint"


def git_pdf_object_rows(root: Path) -> list[dict[str, str]]:
    output = run_git(root, "rev-list", "--objects", "--all")
    if output is None:
        raise RetentionError("cannot enumerate git objects")
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for line in output.splitlines():
        if " " not in line:
            continue
        git_blob, path = line.split(" ", 1)
        if not path.lower().endswith(".pdf"):
            continue
        key = (git_blob, path)
        if key in seen:
            continue
        seen.add(key)
        rows.append({"git_blob": git_blob, "path": path})
    rows.sort(key=lambda row: (row["path"], row["git_blob"]))
    return rows


def first_seen_pdf_blob(root: Path, git_blob: str, path: str) -> dict[str, str | None]:
    output = run_git(
        root,
        "log",
        "--all",
        "--reverse",
        f"--find-object={git_blob}",
        "--format=%H%x09%aI",
        "--",
        path,
    )
    if not output:
        output = run_git(root, "log", "--all", "--reverse", "--format=%H%x09%aI", "--", path)
    for line in (output or "").splitlines():
        if "\t" not in line:
            continue
        commit, timestamp = line.split("\t", 1)
        return {"commit": commit, "timestamp": timestamp}
    return {"commit": None, "timestamp": None}


def first_seen_pdf_blob_map(root: Path) -> dict[tuple[str, str], dict[str, str | None]]:
    output = run_git(
        root,
        "log",
        "--all",
        "--reverse",
        "--raw",
        "--no-renames",
        "--no-abbrev",
        "--format=commit%x09%H%x09%aI",
        "--",
        "*.pdf",
    )
    mapping: dict[tuple[str, str], dict[str, str | None]] = {}
    current_commit: str | None = None
    current_timestamp: str | None = None
    for line in (output or "").splitlines():
        if line.startswith("commit\t"):
            _, current_commit, current_timestamp = line.split("\t", 2)
            continue
        if not line.startswith(":") or "\t" not in line:
            continue
        meta, path = line.split("\t", 1)
        if not path.lower().endswith(".pdf"):
            continue
        parts = meta.split()
        if len(parts) < 5:
            continue
        git_blob = parts[3]
        if set(git_blob) == {"0"}:
            continue
        mapping.setdefault((git_blob, path), {"commit": current_commit, "timestamp": current_timestamp})
    return mapping


def history_reference_name(
    paper_id: str,
    version: str,
    first_seen: dict[str, str | None],
    digest: str,
) -> str:
    timestamp = first_seen.get("timestamp")
    if timestamp:
        try:
            local = datetime.fromisoformat(timestamp).astimezone(LOCAL_ZONE)
            local_stamp = local.strftime("%Y-%m-%dT%H%M%S%z-%Z")
        except ValueError:
            local_stamp = "unknown-time"
    else:
        local_stamp = "unknown-time"
    return (
        f"{safe_component(paper_id)}__{safe_component(version)}__"
        f"{safe_component(local_stamp)}__{digest[:12]}.pdf"
    )


def history_inventory(
    root: Path,
    archive: Path,
    *,
    captured_at: datetime,
    run_id: str,
    materialize: bool = False,
    dry_run: bool = False,
    page_count: bool = True,
    row_offset: int = 0,
    row_limit: int | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    archive = archive if archive.is_absolute() else root / archive
    archive = archive.resolve()
    rows = []
    totals: dict[str, Any] = {
        "git_pdf_object_path_rows": 0,
        "classified_rows": 0,
        "unclassified_rows": 0,
        "classified_distinct_git_blobs": 0,
        "classified_distinct_sha256": 0,
        "objects_created": 0,
        "references_created": 0,
        "errors": 0,
        "by_paper": {paper_id: 0 for paper_id in CANONICAL_IDS},
        "unclassified_reasons": {},
    }
    classified_git_blobs: set[str] = set()
    classified_sha256: set[str] = set()
    first_seen_map = first_seen_pdf_blob_map(root) if materialize else {}

    all_pdf_rows = git_pdf_object_rows(root)
    if row_offset < 0:
        raise RetentionError("history row offset must be non-negative")
    if row_limit is not None and row_limit < 1:
        raise RetentionError("history row limit must be positive")
    selected_pdf_rows = all_pdf_rows[row_offset : None if row_limit is None else row_offset + row_limit]

    for row in selected_pdf_rows:
        totals["git_pdf_object_path_rows"] += 1
        path = row["path"]
        git_blob = row["git_blob"]
        paper_id, reason = classify_history_pdf(path)
        size = git_object_size(root, git_blob) if (materialize or page_count) else None
        base: dict[str, Any] = {
            "path": path,
            "git_blob": git_blob,
            "git_blob_size_bytes": size,
            "paper_id": paper_id,
            "classification_reason": reason,
        }
        if paper_id is None:
            totals["unclassified_rows"] += 1
            reasons = totals["unclassified_reasons"]
            reasons[reason] = reasons.get(reason, 0) + 1
            rows.append(base)
            continue

        totals["classified_rows"] += 1
        totals["by_paper"][paper_id] += 1
        classified_git_blobs.add(git_blob)
        version = infer_path_version(path)
        first_seen = first_seen_map.get((git_blob, path), {"commit": None, "timestamp": None})
        if not materialize and not page_count:
            base.update(
                {
                    "paper_version": version,
                    "sha256": None,
                    "md5": None,
                    "page_count": None,
                    "first_seen": first_seen,
                    "archive_object": None,
                    "object_created": False,
                    "archive_reference": None,
                    "reference_created": False,
                }
            )
            rows.append(base)
            continue
        try:
            payload = run_git_bytes(root, "cat-file", "-p", git_blob)
            if not payload.startswith(b"%PDF-"):
                raise RetentionError("git blob does not start with %PDF-")
            digest = sha256_bytes(payload)
            classified_sha256.add(digest)
            pages = pdf_page_count(payload) if page_count else None
            object_path = archive / "objects" / "sha256" / digest[:2] / f"{digest}.pdf"
            reference_path = archive / "refs" / safe_component(paper_id) / history_reference_name(
                paper_id, version, first_seen, digest
            )
            object_created = False
            reference_created = False
            if materialize and not dry_run:
                object_path, object_created = retain_object(archive, digest, payload)
                reference_created = retain_reference(object_path, reference_path, digest)
                if object_created:
                    totals["objects_created"] += 1
                if reference_created:
                    totals["references_created"] += 1
            base.update(
                {
                    "paper_version": version,
                    "sha256": digest,
                    "md5": md5_bytes(payload) if page_count else None,
                    "page_count": pages,
                    "first_seen": first_seen,
                    "archive_object": relative_or_absolute(object_path, root),
                    "object_created": object_created,
                    "archive_reference": relative_or_absolute(reference_path, root),
                    "reference_created": reference_created,
                }
            )
        except (OSError, ValueError, RetentionError) as exc:
            totals["errors"] += 1
            base["error"] = str(exc)
        rows.append(base)

    totals["classified_distinct_git_blobs"] = len(classified_git_blobs)
    totals["classified_distinct_sha256"] = len(classified_sha256)
    stamp = captured_at.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    manifest_path = archive / "manifests" / stamp[:4] / stamp[4:6] / f"{stamp}-{run_id}-history.json"
    manifest = {
        "schema": "bigbounce-pdf-retention-history/v1",
        "run_id": run_id,
        "mode": "history-backfill" if materialize else "history-inventory",
        "captured_at_utc": captured_at.astimezone(timezone.utc).isoformat(),
        "captured_at_local": captured_at.astimezone(LOCAL_ZONE).isoformat(),
        "git_head": run_git(root, "rev-parse", "HEAD"),
        "materialized": materialize and not dry_run,
        "page_counts_recorded": page_count,
        "row_selection": {
            "total_git_pdf_object_path_rows": len(all_pdf_rows),
            "offset": row_offset,
            "limit": row_limit,
            "selected_rows": len(selected_pdf_rows),
        },
        "coverage": totals,
        "classification_policy": {
            "scope": "reachable Git PDF object/path rows; only high-confidence six-paper manuscript paths are materialized",
            "excluded": [
                "figure PDFs",
                "render artifacts",
                "existing pdf-archive self-references",
                "paths without a six-paper manuscript hint",
                "ambiguous paper-hint matches",
            ],
            "unknown_version_policy": "When no version token is present in the historical path, paper_version is recorded as unknown rather than inferred.",
        },
        "rows": rows,
    }
    manifest["manifest_path"] = relative_or_absolute(manifest_path, root)
    if not dry_run:
        encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
        write_exclusive(manifest_path, encoded)
    return manifest


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
    history_mode = parser.add_mutually_exclusive_group()
    history_mode.add_argument(
        "--history-inventory",
        action="store_true",
        help="write a ledger for every reachable Git PDF object/path row without materializing history refs",
    )
    history_mode.add_argument(
        "--history-backfill",
        action="store_true",
        help="materialize high-confidence historical six-paper manuscript PDFs and write a full ledger",
    )
    parser.add_argument(
        "--history-skip-page-count",
        action="store_true",
        help="history mode only: skip pdfinfo page counts for fast inventory/dry-run",
    )
    parser.add_argument("--history-offset", type=int, default=0, help="history mode only: zero-based PDF row offset")
    parser.add_argument("--history-limit", type=int, help="history mode only: maximum PDF rows to process")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    paper_ids = tuple(args.paper) if args.paper else CANONICAL_IDS
    if len(paper_ids) != len(set(paper_ids)):
        parser.error("--paper values must be unique")
    run_id = args.run_id or secrets.token_hex(6)
    try:
        captured_at = parse_timestamp(args.timestamp)
        if args.history_inventory or args.history_backfill:
            if args.paper:
                parser.error("--paper cannot be combined with history modes")
            if args.build_command or args.review_round:
                parser.error("--build-command/--review-round are snapshot metadata, not history metadata")
            result = history_inventory(
                args.root,
                args.archive_root,
                captured_at=captured_at,
                run_id=run_id,
                materialize=args.history_backfill,
                dry_run=args.dry_run,
                page_count=args.history_backfill and not args.history_skip_page_count,
                row_offset=args.history_offset,
                row_limit=args.history_limit,
            )
        else:
            result = snapshot(
                args.root,
                args.archive_root,
                paper_ids,
                captured_at=captured_at,
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
