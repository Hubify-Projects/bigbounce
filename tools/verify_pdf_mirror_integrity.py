#!/usr/bin/env python3
"""Fail closed when a served PDF, or a site reference to one, is not current.

Directive G enforces PDF hygiene in the FORWARD direction only: for each paper,
push the freshly-compiled PDF out to that paper's *known* mirror paths. Nothing
enforced the REVERSE direction -- a ``.pdf`` sitting under a served root that is
not in any paper's registered mirror set is invisible to directive G and can
serve superseded content forever. Four separate agents tripped over instances of
this on 2026-07-24 alone, each by accident.

This checker closes that hole from both ends, driven entirely by the
``served_pdf_policy`` and ``companion_manuscripts`` blocks of
``project-context/paper_registry.json`` so that adopting a new alias, adding a
paper, or dispositioning a retired file is a DATA edit, never a code edit.

Reverse direction -- every git-tracked ``.pdf`` under a served root must be one
of:

``current mirror``
    byte-identical to a registry paper's (or registered companion's) canonical
    PDF, under that paper's canonical basename or a registered served alias.

``immutable archive``
    a version-pinned historical file (``..._v1.7.126.pdf``). Per PUB-005 these
    are append-only evidence and are LEGITIMATE -- retention must never look
    like a defect. The only thing checked about them is that an archive
    claiming a paper's CURRENT version really carries that version's bytes.

``non-manuscript asset``
    a figure/render PDF, matched by policy path pattern.

``retired``
    an explicitly dispositioned entry in ``retired_served_pdfs``. Only
    ``disposition: "retain"`` passes; ``remove`` / ``archive-then-remove`` are
    recorded-but-still-open defects and keep failing until the file is gone, so
    a known orphan cannot quietly become permanent.

Anything else is an unregistered orphan and fails.

Forward direction -- every ``/papers/*.pdf`` reference reachable from the site
data files must resolve to a real file, and (for the ``current`` kinds) to the
paper's CURRENT bytes. A link to a real-but-superseded PDF is exactly as bad as
a dead one: that is the ``papers.ts`` r13/r14 failure. The declared version
string and the ``pdfMeta`` md5 in the same record are checked too, because a
stale version label is the same lie told in prose.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    from tools.paper_registry import CANONICAL_IDS, registry_path, repo_root
except ModuleNotFoundError:  # direct execution from tools/
    from paper_registry import CANONICAL_IDS, registry_path, repo_root

SCHEMA = "bigbounce.pdf-mirror-integrity/v1"
POLICY_SCHEMA = "bigbounce.served-pdf-policy/v1"

CURRENT_REFERENCE_KINDS = ("current-paper-artifacts",)
HISTORICAL_REFERENCE_KINDS = ("historical-archive-links",)
REFERENCE_KINDS = CURRENT_REFERENCE_KINDS + HISTORICAL_REFERENCE_KINDS
DISPOSITIONS = ("retain", "remove", "archive-then-remove")
PASSING_DISPOSITIONS = ("retain",)

_VERSION_PATTERNS = (
    re.compile(r"\\(?:new|renew)command\s*\{\\paperVersion\}\s*\{([^}]+)\}"),
    re.compile(r"\\def\s*\\paperVersion\s*\{([^}]+)\}"),
    re.compile(r"\\preprint\s*\{([^}]+)\}"),
)
_MD5_IN_PROSE = re.compile(r"\bmd5\s+([0-9a-f]{32})\b", re.IGNORECASE)
_SLUG_FIELD = re.compile(r'slug:\s*"([^"]+)"')
_VERSION_FIELD = re.compile(r'^\s*version:\s*"([^"]+)"', re.MULTILINE)
_PDFMETA_FIELD = re.compile(r'^\s*pdfMeta:\s*"((?:[^"\\]|\\.)*)"', re.MULTILINE)


class MirrorIntegrityError(ValueError):
    """Raised when the policy or the served tree cannot be validated."""


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def md5_bytes(payload: bytes) -> str:
    return hashlib.md5(payload).hexdigest()  # noqa: S324 - directive-G receipt parity


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def safe_relative(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise MirrorIntegrityError(f"{label} must be a non-empty string")
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts or str(candidate) != value:
        raise MirrorIntegrityError(f"{label} must be a safe normalized repository path: {value!r}")
    return value


def compile_patterns(values: Any, label: str) -> list[re.Pattern[str]]:
    if not isinstance(values, list) or not all(isinstance(item, str) and item for item in values):
        raise MirrorIntegrityError(f"{label} must be a non-empty string list")
    try:
        return [re.compile(item) for item in values]
    except re.error as exc:
        raise MirrorIntegrityError(f"{label} contains an invalid regex: {exc}") from exc


def paper_version(tex_path: Path) -> str:
    text = tex_path.read_text(encoding="utf-8", errors="replace")
    for pattern in _VERSION_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1).strip()
    raise MirrorIntegrityError(f"cannot determine paper version: {tex_path}")


def tracked_files(root: Path, roots: list[str]) -> list[str]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z", "--", *roots], cwd=root, text=True,
    )
    return sorted(item for item in output.split("\0") if item.endswith(".pdf"))


# --------------------------------------------------------------------------
# policy
# --------------------------------------------------------------------------
def load_policy(root: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Return (policy, registry papers, companion manuscripts) from the registry."""
    try:
        payload = json.loads(registry_path(root).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MirrorIntegrityError(f"cannot read paper registry: {exc}") from exc

    papers = payload.get("papers")
    if not isinstance(papers, dict) or tuple(papers) != CANONICAL_IDS:
        raise MirrorIntegrityError(f"registry must own exactly {CANONICAL_IDS}")

    companions = payload.get("companion_manuscripts", {})
    if not isinstance(companions, dict):
        raise MirrorIntegrityError("companion_manuscripts must be an object")
    for companion_id, entry in companions.items():
        if companion_id in CANONICAL_IDS:
            raise MirrorIntegrityError(f"companion id collides with a paper id: {companion_id}")
        if not isinstance(entry, dict):
            raise MirrorIntegrityError(f"{companion_id} companion entry must be an object")
        for field in ("tex_path", "pdf_path"):
            safe_relative(entry.get(field), f"{companion_id}.{field}")

    policy = payload.get("served_pdf_policy")
    if not isinstance(policy, dict):
        raise MirrorIntegrityError("registry has no served_pdf_policy block")
    if policy.get("schema") != POLICY_SCHEMA:
        raise MirrorIntegrityError(f"served_pdf_policy schema must be {POLICY_SCHEMA}")

    roots = policy.get("served_roots")
    if not isinstance(roots, list) or not roots:
        raise MirrorIntegrityError("served_roots must be a non-empty list")
    for served_root in roots:
        safe_relative(served_root, "served_roots entry")
        if not (root / served_root).is_dir():
            raise MirrorIntegrityError(f"served root does not exist: {served_root}")

    prefix = policy.get("site_href_prefix")
    if not isinstance(prefix, str) or not prefix.startswith("/") or not prefix.endswith("/"):
        raise MirrorIntegrityError("site_href_prefix must be an absolute directory prefix")
    safe_relative(policy.get("site_href_root"), "site_href_root")

    compile_patterns(policy.get("immutable_archive_name_patterns"), "immutable_archive_name_patterns")
    compile_patterns(policy.get("non_manuscript_path_patterns"), "non_manuscript_path_patterns")

    sources = policy.get("site_data_sources")
    if not isinstance(sources, list) or not sources:
        raise MirrorIntegrityError("site_data_sources must be a non-empty list")
    for source in sources:
        if not isinstance(source, dict):
            raise MirrorIntegrityError("each site_data_sources entry must be an object")
        safe_relative(source.get("path"), "site_data_sources[].path")
        if source.get("kind") not in REFERENCE_KINDS:
            raise MirrorIntegrityError(
                f"site_data_sources[].kind must be one of {REFERENCE_KINDS}: {source.get('kind')!r}"
            )

    retired = policy.get("retired_served_pdfs", [])
    if not isinstance(retired, list):
        raise MirrorIntegrityError("retired_served_pdfs must be a list")
    seen: set[str] = set()
    for record in retired:
        if not isinstance(record, dict):
            raise MirrorIntegrityError("each retired_served_pdfs entry must be an object")
        path = safe_relative(record.get("path"), "retired_served_pdfs[].path")
        if path in seen:
            raise MirrorIntegrityError(f"retired_served_pdfs lists {path} twice")
        seen.add(path)
        if not any(path == item or path.startswith(f"{item}/") for item in roots):
            raise MirrorIntegrityError(f"retired_served_pdfs[].path is not under a served root: {path}")
        if record.get("disposition") not in DISPOSITIONS:
            raise MirrorIntegrityError(
                f"{path} disposition must be one of {DISPOSITIONS}: {record.get('disposition')!r}"
            )
        for field in ("identified_paper", "identified_version", "note"):
            if not isinstance(record.get(field), str) or not record[field]:
                raise MirrorIntegrityError(f"{path} retired entry needs a non-empty {field}")
    return policy, papers, companions


# --------------------------------------------------------------------------
# canonical state
# --------------------------------------------------------------------------
def canonical_state(
    root: Path, papers: dict[str, dict[str, Any]], companions: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    """Read every canonical manuscript PDF once: {id: {md5, version, names}}."""
    state: dict[str, dict[str, Any]] = {}
    for entry_id, entry in list(papers.items()) + list(companions.items()):
        pdf_path = root / entry["pdf_path"]
        tex_path = root / entry["tex_path"]
        if not pdf_path.is_file():
            raise MirrorIntegrityError(f"{entry_id} canonical PDF missing: {entry['pdf_path']}")
        if not tex_path.is_file():
            raise MirrorIntegrityError(f"{entry_id} canonical source missing: {entry['tex_path']}")
        names = [Path(entry["pdf_path"]).name]
        for alias in entry.get("served_aliases", []):
            if Path(alias).name != alias or not alias.endswith(".pdf"):
                raise MirrorIntegrityError(f"{entry_id} served alias must be a PDF basename: {alias!r}")
            names.append(alias)
        state[entry_id] = {
            "pdf_path": entry["pdf_path"],
            "tex_path": entry["tex_path"],
            "md5": md5_bytes(pdf_path.read_bytes()),
            "version": paper_version(tex_path),
            "site_slug": entry.get("site_slug"),
            "names": tuple(dict.fromkeys(names)),
        }
    return state


# --------------------------------------------------------------------------
# reverse direction: the served tree
# --------------------------------------------------------------------------
def classify_served_tree(
    root: Path, policy: dict[str, Any], canonical: dict[str, dict[str, Any]]
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    archive_patterns = compile_patterns(
        policy["immutable_archive_name_patterns"], "immutable_archive_name_patterns"
    )
    asset_patterns = compile_patterns(
        policy["non_manuscript_path_patterns"], "non_manuscript_path_patterns"
    )
    retired = {record["path"]: record for record in policy.get("retired_served_pdfs", [])}
    by_md5 = {entry["md5"]: entry_id for entry_id, entry in canonical.items()}
    owner_of_name: dict[str, str] = {}
    for entry_id, entry in canonical.items():
        for name in entry["names"]:
            owner_of_name.setdefault(name, entry_id)

    findings: list[dict[str, Any]] = []
    counts = {
        "current_mirror": 0, "immutable_archive": 0, "non_manuscript_asset": 0,
        "retained_by_policy": 0, "orphan": 0, "total": 0,
    }
    inventory: list[str] = []
    unused_retired = set(retired)

    for relative in tracked_files(root, policy["served_roots"]):
        path = root / relative
        if not path.is_file():
            findings.append({
                "rule": "served-pdf-missing-from-worktree", "path": relative,
                "detail": "path is tracked under a served root but absent from the working tree",
            })
            continue
        counts["total"] += 1
        # Seen on disk: whatever this file turns out to be, a retired entry
        # naming it is describing something real, not a leftover ledger row.
        unused_retired.discard(relative)
        digest = md5_bytes(path.read_bytes())
        inventory.append(f"{relative} {digest}")
        name = Path(relative).name

        if any(pattern.search(relative) for pattern in asset_patterns):
            counts["non_manuscript_asset"] += 1
            continue

        if any(pattern.search(name) for pattern in archive_patterns):
            counts["immutable_archive"] += 1
            # Retention is legitimate and must never be reported as a defect.
            # The one archive rule: a file version-pinned to a paper's CURRENT
            # version has to actually be that version's bytes.
            for entry_id, entry in canonical.items():
                if not name.endswith(f"_{entry['version']}.pdf"):
                    continue
                if digest != entry["md5"]:
                    findings.append({
                        "rule": "archive-version-collision", "path": relative,
                        "paper_id": entry_id, "expected_md5": entry["md5"], "actual_md5": digest,
                        "detail": (
                            f"version-pinned archive claims {entry_id} {entry['version']} but its "
                            f"bytes are not that version's canonical PDF ({entry['pdf_path']})"
                        ),
                    })
            continue

        owner = by_md5.get(digest)
        if owner is not None and name in canonical[owner]["names"]:
            counts["current_mirror"] += 1
            if relative in retired:
                findings.append({
                    "rule": "retired-entry-contradicts-current-mirror", "path": relative,
                    "paper_id": owner,
                    "detail": (
                        "registry retires a path that is currently a byte-identical mirror of "
                        f"{owner}; drop the retired_served_pdfs entry or the alias, not both"
                    ),
                })
            continue

        record = retired.get(relative)
        if record is not None:
            if record["disposition"] in PASSING_DISPOSITIONS:
                counts["retained_by_policy"] += 1
                continue
            counts["orphan"] += 1
            findings.append({
                "rule": "retired-served-pdf-still-present", "path": relative,
                "paper_id": record["identified_paper"], "actual_md5": digest,
                "identified_version": record["identified_version"],
                "disposition": record["disposition"],
                "detail": (
                    f"{relative} is a dispositioned orphan ({record['identified_paper']} "
                    f"{record['identified_version']}) still served; recorded disposition is "
                    f"{record['disposition']} -- {record['note']}"
                ),
            })
            continue

        counts["orphan"] += 1
        registered_owner = owner_of_name.get(name)
        if registered_owner is not None:
            findings.append({
                "rule": "mirror-bytes-stale", "path": relative, "paper_id": registered_owner,
                "expected_md5": canonical[registered_owner]["md5"], "actual_md5": digest,
                "detail": (
                    f"{relative} uses {registered_owner}'s canonical name/alias but its bytes are "
                    f"not {registered_owner}'s current PDF ({canonical[registered_owner]['pdf_path']}); "
                    "directive G never mirrored this path"
                ),
            })
        else:
            findings.append({
                "rule": "unregistered-orphan-pdf", "path": relative, "actual_md5": digest,
                "detail": (
                    f"{relative} is served but matches no paper's current PDF, is not a "
                    "version-pinned archive, and carries no registry disposition"
                ),
            })

    for relative in sorted(unused_retired):
        findings.append({
            "rule": "stale-retired-entry", "path": relative,
            "detail": "registry retires a served path that no longer exists; drop the entry",
        })

    summary = {
        "counts": counts,
        "inventory_sha256": sha256_text("\n".join(inventory) + "\n"),
        "inventory_size": len(inventory),
    }
    return findings, summary


# --------------------------------------------------------------------------
# forward direction: the site data files
# --------------------------------------------------------------------------
def slug_blocks(text: str) -> dict[str, tuple[int, str]]:
    """Split a site data file into per-slug records keyed by ``slug: "..."``.

    Returns ``{slug: (absolute character offset, block text)}`` so every finding
    can report a real line number in the real file.
    """
    marks = [(match.group(1), match.start()) for match in _SLUG_FIELD.finditer(text)]
    blocks: dict[str, tuple[int, str]] = {}
    for index, (slug, start) in enumerate(marks):
        end = marks[index + 1][1] if index + 1 < len(marks) else len(text)
        blocks.setdefault(slug, (start, text[start:end]))
    return blocks


def check_site_sources(
    root: Path, policy: dict[str, Any], canonical: dict[str, dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    prefix = policy["site_href_prefix"]
    href_root = policy["site_href_root"]
    href_pattern = re.compile(rf'"{re.escape(prefix)}([A-Za-z0-9._\-]+\.pdf)"')
    by_slug = {
        entry["site_slug"]: (entry_id, entry)
        for entry_id, entry in canonical.items()
        if entry.get("site_slug")
    }

    findings: list[dict[str, Any]] = []
    sources: list[dict[str, Any]] = []

    for source in policy["site_data_sources"]:
        relative = source["path"]
        kind = source["kind"]
        path = root / relative
        if not path.is_file():
            findings.append({
                "rule": "site-data-source-missing", "location": relative,
                "detail": f"registry declares {relative} as a PDF-reference surface but it does not exist",
            })
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        references = 0

        # (1) existence: every referenced served PDF must resolve, in every kind.
        for match in href_pattern.finditer(text):
            references += 1
            name = match.group(1)
            line = text.count("\n", 0, match.start()) + 1
            if not (root / href_root / prefix.strip("/") / name).is_file():
                findings.append({
                    "rule": "site-reference-missing", "location": relative, "line": line,
                    "reference": f"{prefix}{name}",
                    "detail": f"{relative}:{line} links {prefix}{name}, which does not exist under {href_root}",
                })

        # (2) currency: only "current" surfaces must point at the current bytes.
        if kind in CURRENT_REFERENCE_KINDS:
            for slug, (offset, block) in slug_blocks(text).items():
                owned = by_slug.get(slug)
                if owned is None:
                    continue
                entry_id, entry = owned

                for match in href_pattern.finditer(block):
                    name = match.group(1)
                    served = root / href_root / prefix.strip("/") / name
                    line = text.count("\n", 0, offset + match.start()) + 1
                    if not served.is_file():
                        continue  # already reported as site-reference-missing
                    digest = md5_bytes(served.read_bytes())
                    if digest != entry["md5"]:
                        findings.append({
                            "rule": "site-reference-stale", "location": relative, "line": line,
                            "paper_id": entry_id, "reference": f"{prefix}{name}",
                            "expected_md5": entry["md5"], "actual_md5": digest,
                            "detail": (
                                f"{relative}:{line} serves {entry_id} from {prefix}{name}, which is a "
                                f"superseded build; {entry_id} is currently {entry['version']} "
                                f"({entry['pdf_path']})"
                            ),
                        })

                version_match = _VERSION_FIELD.search(block)
                if version_match and version_match.group(1) != entry["version"]:
                    line = text.count("\n", 0, offset + version_match.start()) + 1
                    findings.append({
                        "rule": "site-version-field-stale", "location": relative, "line": line,
                        "paper_id": entry_id, "declared": version_match.group(1),
                        "expected": entry["version"],
                        "detail": (
                            f"{relative}:{line} declares {entry_id} as {version_match.group(1)} "
                            f"while {entry['tex_path']} is {entry['version']}"
                        ),
                    })

                meta_match = _PDFMETA_FIELD.search(block)
                if meta_match:
                    digests = _MD5_IN_PROSE.findall(meta_match.group(1))
                    if digests and digests[0].lower() != entry["md5"]:
                        line = text.count("\n", 0, offset + meta_match.start()) + 1
                        findings.append({
                            "rule": "site-pdfmeta-md5-stale", "location": relative, "line": line,
                            "paper_id": entry_id, "declared": digests[0].lower(),
                            "expected": entry["md5"],
                            "detail": (
                                f"{relative}:{line} advertises {entry_id} md5 {digests[0].lower()} "
                                f"while the canonical PDF is {entry['md5']}"
                            ),
                        })

        sources.append({"path": relative, "kind": kind, "reference_count": references})
    return findings, sources


# --------------------------------------------------------------------------
# entry points
# --------------------------------------------------------------------------
def verify(root: Path | str) -> dict[str, Any]:
    root = Path(root).resolve()
    policy, papers, companions = load_policy(root)
    canonical = canonical_state(root, papers, companions)
    served_findings, served_summary = classify_served_tree(root, policy, canonical)
    site_findings, sources = check_site_sources(root, policy, canonical)
    findings = served_findings + site_findings
    return {
        "schema": SCHEMA,
        "policy_schema": POLICY_SCHEMA,
        "served_roots": list(policy["served_roots"]),
        "papers": [
            {
                "paper_id": entry_id,
                "version": entry["version"],
                "md5": entry["md5"],
                "pdf_path": entry["pdf_path"],
            }
            for entry_id, entry in sorted(canonical.items())
        ],
        "served_inventory": served_summary,
        "site_data_sources": sources,
        "findings": findings,
        "finding_count": len(findings),
        "verdict": "FAIL" if findings else "PASS",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=repo_root())
    args = parser.parse_args(argv)
    try:
        result = verify(args.project_root)
    except (MirrorIntegrityError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["verdict"] != "PASS":
        for finding in result["findings"]:
            where = finding.get("path") or finding.get("location", "?")
            line = finding.get("line")
            print(
                f"FAIL [{finding['rule']}] {where}{f':{line}' if line else ''}: {finding['detail']}",
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
