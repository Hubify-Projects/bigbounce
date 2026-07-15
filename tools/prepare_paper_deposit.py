#!/usr/bin/env python3
"""Prepare a version- and commit-bound paper deposit without publishing it.

The command is dry-run by default.  ``--write`` copies exact, verified inputs
into the gitignored staging tree and emits a machine-readable manifest,
``SHA256SUMS``, and Zenodo upload metadata.  It never calls GitHub, Zenodo,
arXiv, or any other external service.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CONFIG_PATH = Path(__file__).with_name("paper_deposit_config.json")
VERSION_RE = re.compile(
    r"\\(?:newcommand|renewcommand)\s*\{\\paperVersion\}\s*\{([^}]+)\}"
)
PREPRINT_VERSION_RE = re.compile(r"^\s*\\preprint\s*\{(v[^}]+)\}\s*$", re.MULTILINE)
FULL_COMMIT_RE = re.compile(r"[0-9a-f]{40}")
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
ARXIV_RE = re.compile(r"(?:arXiv:)?\d{4}\.\d{4,5}(?:v\d+)?", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(
    r"(?:\b(?:todo|tbd|placeholder|pending)\b|doi\s+xyz|10\.x{3,}|"
    r"arxiv:\s*x+|insert(?:ed)?\s+at\s+submission)",
    re.IGNORECASE,
)


class DepositError(RuntimeError):
    """Raised whenever exact deposit provenance cannot be proven."""


def digest(path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def run(root: Path, *command: str, input_bytes: bytes | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        cwd=root,
        input=input_bytes,
        capture_output=True,
        check=False,
        timeout=180,
    )


def git(root: Path, *args: str) -> str:
    result = run(root, "git", *args)
    if result.returncode:
        detail = result.stderr.decode(errors="replace").strip()
        raise DepositError(f"git {' '.join(args)} failed: {detail or 'unknown error'}")
    return result.stdout.decode().strip()


def load_config(path: Path, paper_id: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        paper = payload["papers"][paper_id]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise DepositError(f"invalid or missing configuration for {paper_id}: {path}") from exc
    required = {"tex", "pdf", "arxiv_tarball", "standalone_proof", "tarball_main_tex", "deposit_root", "metadata"}
    missing = sorted(required - set(paper))
    if missing:
        raise DepositError(f"configuration for {paper_id} lacks: {', '.join(missing)}")
    return paper


def paper_version(tex_path: Path) -> str:
    try:
        text = tex_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise DepositError(f"missing TeX source: {tex_path}") from exc
    match = VERSION_RE.search(text) or PREPRINT_VERSION_RE.search(text)
    if not match or not match.group(1).strip():
        raise DepositError(f"no active \\paperVersion or versioned \\preprint declaration found in {tex_path}")
    return match.group(1).strip()


def pdf_page_count(root: Path, pdf_path: Path) -> int:
    if pdf_path.read_bytes()[:5] != b"%PDF-":
        raise DepositError(f"PDF magic is invalid: {pdf_path}")
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        raise DepositError("pdfinfo is required to validate PDF page count")
    result = run(root, pdfinfo, str(pdf_path))
    if result.returncode:
        detail = result.stderr.decode(errors="replace").strip()
        raise DepositError(f"pdfinfo rejected {pdf_path}: {detail or 'unknown error'}")
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout.decode(errors="replace"), re.MULTILINE)
    if not match or int(match.group(1)) < 1:
        raise DepositError(f"pdfinfo returned no positive page count for {pdf_path}")
    return int(match.group(1))


def require_exact_commit(root: Path, commit: str) -> None:
    if not FULL_COMMIT_RE.fullmatch(commit):
        raise DepositError("--git-commit must be a full lowercase 40-character SHA-1")
    resolved = git(root, "rev-parse", f"{commit}^{{commit}}")
    if resolved != commit:
        raise DepositError(f"requested Git object is not the exact commit {commit}")


def require_clean_commit_inputs(root: Path, commit: str, paths: list[Path]) -> None:
    for path in paths:
        if not path.is_file():
            raise DepositError(f"required input is missing: {path}")
        try:
            relative = path.resolve().relative_to(root.resolve()).as_posix()
        except ValueError as exc:
            raise DepositError(f"input escapes repository: {path}") from exc
        tracked = run(root, "git", "ls-files", "--error-unmatch", "--", relative)
        if tracked.returncode:
            raise DepositError(f"required input is not tracked: {relative}")
        dirty = run(root, "git", "diff", "--quiet", commit, "--", relative)
        if dirty.returncode == 1:
            raise DepositError(f"required input differs from commit {commit}: {relative}")
        if dirty.returncode != 0:
            raise DepositError(f"could not verify clean Git state for {relative}")
        committed = run(root, "git", "show", f"{commit}:{relative}")
        if committed.returncode or hashlib.sha256(committed.stdout).hexdigest() != digest(path, "sha256"):
            raise DepositError(f"working bytes do not equal {commit}:{relative}")


def require_clean_tracked_receipt(root: Path, path: Path) -> None:
    """Require a post-build receipt to be tracked and byte-identical to HEAD."""
    if not path.is_file():
        raise DepositError(f"required input is missing: {path}")
    try:
        relative = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise DepositError(f"input escapes repository: {path}") from exc
    if run(root, "git", "ls-files", "--error-unmatch", "--", relative).returncode:
        raise DepositError(f"required input is not tracked: {relative}")
    if run(root, "git", "diff", "--quiet", "HEAD", "--", relative).returncode:
        raise DepositError(f"tracked proof receipt is dirty: {relative}")
    committed = run(root, "git", "show", f"HEAD:{relative}")
    if committed.returncode or hashlib.sha256(committed.stdout).hexdigest() != digest(path, "sha256"):
        raise DepositError(f"proof receipt bytes do not equal HEAD:{relative}")


def _proof_value(proof: dict[str, Any], key: str) -> Any:
    if key in proof:
        return proof[key]
    compile_info = proof.get("compile")
    return compile_info.get(key) if isinstance(compile_info, dict) else None


def validate_proof(
    proof_path: Path,
    *,
    paper_id: str,
    version: str,
    commit: str,
    tarball_sha256: str,
    expected_pages: int,
) -> dict[str, Any]:
    try:
        proof = json.loads(proof_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise DepositError(f"standalone proof is missing or invalid: {proof_path}") from exc
    checks = {
        "paper_id": paper_id,
        "paper_version": version,
        "git_commit": commit,
        "tarball_sha256": tarball_sha256,
        "page_count": expected_pages,
    }
    for key, expected in checks.items():
        if _proof_value(proof, key) != expected:
            raise DepositError(f"standalone proof {key} does not match exact release")
    if str(_proof_value(proof, "status")).lower() not in {"pass", "passed", "ok"}:
        raise DepositError("standalone proof does not record a passing status")
    for key in ("errors", "undefined_references"):
        if _proof_value(proof, key) != 0:
            raise DepositError(f"standalone proof requires {key}=0")
    if not _proof_value(proof, "engine"):
        raise DepositError("standalone proof does not identify its TeX engine")
    return proof


def safe_extract(tarball: Path, destination: Path) -> None:
    with tarfile.open(tarball, "r:gz") as archive:
        members = archive.getmembers()
        if not members:
            raise DepositError("arXiv tarball is empty")
        for member in members:
            target = (destination / member.name).resolve()
            if destination.resolve() not in target.parents and target != destination.resolve():
                raise DepositError(f"unsafe tar path: {member.name}")
            if member.issym() or member.islnk() or member.isdev():
                raise DepositError(f"unsupported tar member type: {member.name}")
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            if not member.isfile():
                raise DepositError(f"unsupported tar member type: {member.name}")
            target.parent.mkdir(parents=True, exist_ok=True)
            source = archive.extractfile(member)
            if source is None:
                raise DepositError(f"could not read tar member: {member.name}")
            with source, target.open("xb") as output:
                shutil.copyfileobj(source, output)


def verify_tarball(root: Path, tarball: Path, main_tex: str, expected_pages: int) -> dict[str, Any]:
    engine = shutil.which("tectonic") or shutil.which("pdflatex")
    if not engine:
        raise DepositError("no supported TeX engine found; provide a tracked standalone proof")
    with tempfile.TemporaryDirectory(prefix="bigbounce-deposit-") as temp:
        stage = Path(temp)
        safe_extract(tarball, stage)
        candidates = list(stage.rglob(main_tex))
        if len(candidates) != 1:
            raise DepositError(f"tarball must contain exactly one {main_tex}")
        tex = candidates[0]
        command = [engine, "--keep-logs", tex.name] if Path(engine).name == "tectonic" else [engine, "-interaction=nonstopmode", "-halt-on-error", tex.name]
        passes = 1 if Path(engine).name == "tectonic" else 2
        combined = b""
        for _ in range(passes):
            result = run(tex.parent, *command)
            combined += result.stdout + result.stderr
            if result.returncode:
                raise DepositError(f"standalone compile failed with {Path(engine).name}")
        compiled = tex.with_suffix(".pdf")
        pages = pdf_page_count(root, compiled)
        console = combined.decode(errors="replace")
        log_path = tex.with_suffix(".log")
        file_log = log_path.read_text(encoding="utf-8", errors="replace") if log_path.is_file() else ""
        log = console + "\n" + file_log
        undefined = len(
            re.findall(
                r"(?:Reference|Citation).*?undefined|There were undefined (?:references|citations)",
                log,
                re.IGNORECASE | re.DOTALL,
            )
        )
        errors = len(re.findall(r"^!", log, re.MULTILINE))
        overfull_hboxes = len(re.findall(r"Overfull \\hbox", file_log))
        overfull_vboxes = len(re.findall(r"Overfull \\vbox", file_log))
        if pages != expected_pages or errors or undefined:
            raise DepositError(
                f"standalone compile mismatch: pages={pages}, errors={errors}, undefined={undefined}"
            )
        return {
            "status": "pass",
            "engine": Path(engine).name,
            "page_count": pages,
            "compiled_pdf_size_bytes": compiled.stat().st_size,
            "compiled_pdf_sha256": digest(compiled, "sha256"),
            "compiled_pdf_md5": digest(compiled, "md5"),
            "errors": errors,
            "undefined_references": undefined,
            "overfull_hboxes": overfull_hboxes,
            "overfull_vboxes": overfull_vboxes,
            "mode": "isolated-safe-extraction",
        }


def validate_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(metadata, dict):
        raise DepositError("deposit metadata must be an object")
    for key in ("title", "creators", "description", "upload_type", "access_right", "license"):
        if not metadata.get(key):
            raise DepositError(f"deposit metadata lacks {key}")
    encoded = json.dumps(metadata, sort_keys=True)
    if PLACEHOLDER_RE.search(encoded):
        raise DepositError("deposit metadata contains a placeholder identifier or value")
    for item in metadata.get("related_identifiers", []):
        identifier = str(item.get("identifier", "")) if isinstance(item, dict) else ""
        if not (DOI_RE.fullmatch(identifier) or ARXIV_RE.fullmatch(identifier)):
            raise DepositError(f"unverified related identifier format: {identifier or '<empty>'}")
    return metadata


def copy_exclusive(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        with source.open("rb") as incoming, destination.open("xb") as outgoing:
            shutil.copyfileobj(incoming, outgoing)
    except FileExistsError as exc:
        raise DepositError(f"refusing to overwrite staged asset: {destination}") from exc


def configured_provenance(root: Path, config: dict[str, Any]) -> list[Path]:
    """Expand the configured tracked provenance set without following symlinks."""
    selected: set[Path] = set()
    for raw in config.get("extra_assets", []):
        selected.add((root / raw).resolve())
    for pattern in config.get("provenance_globs", []):
        result = run(root, "git", "ls-files", "-z", "--", f":(glob){pattern}")
        if result.returncode:
            raise DepositError(f"could not enumerate tracked provenance: {pattern}")
        matches = [
            (root / item.decode()).resolve()
            for item in result.stdout.split(b"\0")
            if item
        ]
        if not matches:
            raise DepositError(f"provenance glob matched no tracked files: {pattern}")
        selected.update(matches)
    paths = sorted(selected, key=lambda path: path.relative_to(root).as_posix())
    for path in paths:
        if path.is_symlink():
            raise DepositError(f"provenance asset may not be a symlink: {path}")
    return paths


def deterministic_tar_gz(root: Path, paths: list[Path]) -> bytes:
    """Return a reproducible gzip-compressed tar of exact repository-relative files."""
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode="w", format=tarfile.PAX_FORMAT) as archive:
            for path in paths:
                relative = path.relative_to(root).as_posix()
                payload = path.read_bytes()
                info = tarfile.TarInfo(relative)
                info.size = len(payload)
                info.mtime = 0
                info.mode = 0o644
                info.uid = info.gid = 0
                info.uname = info.gname = ""
                archive.addfile(info, io.BytesIO(payload))
    return buffer.getvalue()


def prepare(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.repo).resolve()
    config = load_config(Path(args.config).resolve(), args.paper)
    require_exact_commit(root, args.git_commit)
    tex = root / config["tex"]
    version = paper_version(tex)
    pdf = root / config["pdf"]
    tarball = root / str(config["arxiv_tarball"]).format(version=version)
    proof = Path(args.proof).resolve() if args.proof else root / str(config["standalone_proof"]).format(version=version)
    page_count = pdf_page_count(root, pdf)
    tarball_sha = digest(tarball, "sha256") if tarball.is_file() else ""
    if not tarball_sha:
        raise DepositError(f"versioned arXiv tarball is missing: {tarball}")

    provenance = configured_provenance(root, config)
    tracked_inputs = [tex, pdf, tarball, *provenance]
    if args.verify_tarball:
        proof_receipt = verify_tarball(root, tarball, config["tarball_main_tex"], page_count)
        proof_source: Path | None = None
    else:
        require_clean_commit_inputs(root, args.git_commit, tracked_inputs)
        require_clean_tracked_receipt(root, proof)
        proof_receipt = validate_proof(
            proof,
            paper_id=args.paper,
            version=version,
            commit=args.git_commit,
            tarball_sha256=tarball_sha,
            expected_pages=page_count,
        )
        proof_source = proof
    if args.verify_tarball:
        require_clean_commit_inputs(root, args.git_commit, tracked_inputs)

    if config.get("metadata_complete") is False:
        reason = str(config.get("metadata_blocker", "required deposit metadata is unresolved"))
        raise DepositError(f"deposit metadata intentionally incomplete: {reason}")
    metadata = validate_metadata(dict(config["metadata"]))
    metadata["version"] = version.removeprefix("v")
    output = root / config["deposit_root"] / args.paper / version
    assets = [tex, pdf, tarball] + ([proof_source] if proof_source else [])
    asset_records = [
        {
            "name": item.name,
            "source": item.relative_to(root).as_posix(),
            "size_bytes": item.stat().st_size,
            "sha256": digest(item, "sha256"),
            "md5": digest(item, "md5"),
        }
        for item in assets
        if item is not None
    ]
    provenance_bytes = deterministic_tar_gz(root, provenance) if provenance else b""
    provenance_name = str(config.get("provenance_archive", f"{args.paper}_{version}_provenance.tar.gz"))
    if provenance_bytes:
        asset_records.append(
            {
                "name": provenance_name,
                "source": f"generated from {len(provenance)} tracked provenance files",
                "size_bytes": len(provenance_bytes),
                "sha256": hashlib.sha256(provenance_bytes).hexdigest(),
                "md5": hashlib.md5(provenance_bytes).hexdigest(),
            }
        )
    manifest = {
        "schema": "bigbounce-paper-deposit/v1",
        "paper_id": args.paper,
        "paper_version": version,
        "git_commit": args.git_commit,
        "repository_head": git(root, "rev-parse", "HEAD"),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "dry_run": not args.write,
        "pdf": {
            "page_count": page_count,
            "sha256": digest(pdf, "sha256"),
            "md5": digest(pdf, "md5"),
        },
        "arxiv_tarball_sha256": tarball_sha,
        "standalone_proof": proof_receipt,
        "assets": asset_records,
        "external_state_mutated": False,
    }
    if args.write:
        if output.exists():
            raise DepositError(f"refusing to replace existing deposit staging directory: {output}")
        output.mkdir(parents=True)
        try:
            for item in assets:
                if item is not None:
                    copy_exclusive(item, output / item.name)
            if provenance_bytes:
                (output / provenance_name).write_bytes(provenance_bytes)
            (output / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            (output / ".zenodo.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            sums = "".join(f"{record['sha256']}  {record['name']}\n" for record in sorted(asset_records, key=lambda row: row["name"]))
            (output / "SHA256SUMS").write_text(sums, encoding="utf-8")
        except Exception:
            shutil.rmtree(output, ignore_errors=True)
            raise
    manifest["staging_directory"] = output.relative_to(root).as_posix()
    return manifest


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper", required=True, help="configured paper ID (initially P4)")
    parser.add_argument("--git-commit", required=True, help="exact full commit SHA matching HEAD")
    parser.add_argument("--repo", default=".", help="repository root")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="deposit configuration JSON")
    parser.add_argument("--proof", help="override tracked standalone-proof JSON path")
    parser.add_argument("--verify-tarball", action="store_true", help="compile safely in isolation instead of consuming proof metadata")
    parser.add_argument("--write", action="store_true", help="write gitignored staging output (default: dry-run)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    try:
        manifest = prepare(parse_args(argv))
    except (DepositError, OSError, tarfile.TarError, subprocess.TimeoutExpired) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
