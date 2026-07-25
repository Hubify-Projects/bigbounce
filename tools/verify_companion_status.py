#!/usr/bin/env python3
"""Fail closed when a paper misdescribes a companion's public availability.

The six papers cite each other. As each companion is archived with a resolvable
DOI, the OTHER papers' descriptions of it go stale: they keep saying "in
preparation" / "forthcoming" / "arXiv ID will be inserted" about a manuscript
that is now permanently archived and citable. This checker converts that defect
class from a prose review pattern into an executable gate.

Two rule classes, both driven entirely by
``project-context/companion-status-ledger.json`` so that minting a DOI or
retiring a value is a DATA edit, never a code edit:

``companion-status``
    A live reference to a companion that HAS a published DOI must not carry an
    unpublished-status phrase, and a bibliography entry for such a companion
    must actually print the DOI.

``superseded-value``
    A live reference to a companion must not state a value that companion has
    itself superseded (e.g. Paper II's retracted f_NL = -35/8).

Both rules read BIBLIOGRAPHY FIELDS as well as body prose -- ``.bib`` entries,
generated ``.bbl`` files, and inline ``\\bibitem`` blocks -- because that is
exactly where every instance of this defect has actually lived. A ``.tex``-body
sweep is blind to it.

Comment-only content is never inspected: ``%`` comments, ``\\begin{comment}``
blocks, and ``\\iffalse`` blocks are the historical changelog and must not be
touched.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from tools.paper_registry import CANONICAL_IDS, load_registry, repo_root
except ModuleNotFoundError:  # direct execution from tools/
    from paper_registry import CANONICAL_IDS, load_registry, repo_root

SCHEMA = "bigbounce.companion-status/v1"
LEDGER_SCHEMA = "bigbounce.companion-status-ledger/v1"
DEFAULT_LEDGER = "project-context/companion-status-ledger.json"

_COMMENT_OPEN = re.compile(r"^\s*(?:\\begin\{comment\}|\\iffalse\b)")
_COMMENT_CLOSE = re.compile(r"^\s*(?:\\end\{comment\}|\\fi\b)")
_TRAILING_COMMENT = re.compile(r"(?<!\\)%.*$")
_CITE = re.compile(r"\\[a-zA-Z]*cite[a-zA-Z]*\s*(?:\[[^\]]*\])*\s*\{([^}]*)\}")
_BIBITEM = re.compile(r"\\bibitem\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}")
_BIB_INPUT = re.compile(r"\\bibliography\s*\{([^}]*)\}")
_BIB_ENTRY = re.compile(r"^\s*@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)


class CompanionStatusError(ValueError):
    """Raised when the ledger or a paper source cannot be validated."""


# --------------------------------------------------------------------------
# live-source extraction
# --------------------------------------------------------------------------
def live_lines(text: str) -> list[tuple[int, str]]:
    """Return (1-based line number, live text) for every non-comment line.

    Strips ``%`` comments and skips ``\\begin{comment}`` / ``\\iffalse`` blocks
    so the historical changelog can never trip -- or silence -- a rule.
    """
    out: list[tuple[int, str]] = []
    depth = 0
    for number, raw in enumerate(text.splitlines(), 1):
        if _COMMENT_OPEN.match(raw):
            depth += 1
            continue
        if depth:
            if _COMMENT_CLOSE.match(raw):
                depth -= 1
            continue
        live = _TRAILING_COMMENT.sub("", raw)
        if live.strip():
            out.append((number, live))
    return out


def cited_keys(lines: list[tuple[int, str]]) -> set[str]:
    keys: set[str] = set()
    for _, line in lines:
        for group in _CITE.findall(line):
            keys.update(part.strip() for part in group.split(",") if part.strip())
    return keys


def bib_blocks(lines: list[tuple[int, str]]) -> list[dict[str, Any]]:
    """Split inline ``\\bibitem`` blocks out of live LaTeX lines."""
    blocks: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for number, line in lines:
        match = _BIBITEM.search(line)
        if match:
            if current:
                blocks.append(current)
            current = {
                "key": match.group(1).strip(), "line": number,
                "text": [line], "covered": {number},
            }
            continue
        if current is not None:
            if re.search(r"\\end\{thebibliography\}", line):
                blocks.append(current)
                current = None
            else:
                current["text"].append(line)
                current["covered"].add(number)
    if current:
        blocks.append(current)
    for block in blocks:
        block["text"] = " ".join(block["text"])
    return blocks


def bib_file_entries(path: Path) -> dict[str, dict[str, Any]]:
    """Parse a ``.bib`` file into {key: {line, text}} using brace balance."""
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: dict[str, dict[str, Any]] = {}
    for match in _BIB_ENTRY.finditer(text):
        start = match.start()
        depth = 0
        end = len(text)
        for index in range(text.index("{", start), len(text)):
            character = text[index]
            if character == "{":
                depth += 1
            elif character == "}":
                depth -= 1
                if depth == 0:
                    end = index + 1
                    break
        entries[match.group(1)] = {
            "line": text.count("\n", 0, start) + 1,
            "text": " ".join(text[start:end].split()),
        }
    return entries


def bib_sources(root: Path, tex_path: Path, lines: list[tuple[int, str]]) -> list[Path]:
    """Resolve ``\\bibliography{...}`` inputs plus any sibling generated ``.bbl``."""
    found: list[Path] = []
    for _, line in lines:
        for group in _BIB_INPUT.findall(line):
            for name in group.split(","):
                name = name.strip()
                if not name:
                    continue
                candidate = Path(name)
                if candidate.is_absolute() or ".." in candidate.parts:
                    raise CompanionStatusError(f"unsafe \\bibliography target: {name}")
                if candidate.suffix != ".bib":
                    candidate = candidate.with_suffix(".bib")
                for base in (tex_path.parent, root):
                    resolved = base / candidate
                    if resolved.is_file():
                        found.append(resolved)
                        break
    bbl = tex_path.with_suffix(".bbl")
    if bbl.is_file():
        found.append(bbl)
    return list(dict.fromkeys(found))


# --------------------------------------------------------------------------
# ledger
# --------------------------------------------------------------------------
def load_ledger(path: Path) -> dict[str, Any]:
    try:
        ledger = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CompanionStatusError(f"cannot read companion-status ledger: {exc}") from exc
    if ledger.get("schema") != LEDGER_SCHEMA:
        raise CompanionStatusError(f"ledger schema must be {LEDGER_SCHEMA}")
    papers = ledger.get("papers")
    if not isinstance(papers, dict) or tuple(papers) != CANONICAL_IDS:
        raise CompanionStatusError(f"ledger must own exactly {CANONICAL_IDS}")
    for paper_id, entry in papers.items():
        if not isinstance(entry, dict):
            raise CompanionStatusError(f"{paper_id} ledger entry must be an object")
        for field in ("labels", "cite_keys"):
            value = entry.get(field)
            if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
                raise CompanionStatusError(f"{paper_id} ledger {field} must be a non-empty string list")
        doi = entry.get("published_doi")
        if doi is not None and (not isinstance(doi, str) or not doi.startswith("10.")):
            raise CompanionStatusError(f"{paper_id} published_doi must be null or a DOI string")
        if doi is None and not entry.get("no_doi_reason"):
            raise CompanionStatusError(f"{paper_id} has no published_doi and no no_doi_reason")
    phrases = ledger.get("unpublished_status_phrases")
    if not isinstance(phrases, list) or not all(isinstance(item, str) and item for item in phrases):
        raise CompanionStatusError("unpublished_status_phrases must be a non-empty string list")
    for phrase in phrases:
        if re.search(r"peer[- ]review|referee|arxiv preprint", phrase, re.IGNORECASE):
            raise CompanionStatusError(
                "unpublished_status_phrases must never contain a peer-review or "
                f"arXiv-preprint phrase (those caveats are TRUE): {phrase!r}"
            )
    values = ledger.get("superseded_values", [])
    if not isinstance(values, list):
        raise CompanionStatusError("superseded_values must be a list")
    for record in values:
        if not isinstance(record, dict):
            raise CompanionStatusError("each superseded_values record must be an object")
        if record.get("owner") not in CANONICAL_IDS:
            raise CompanionStatusError(f"superseded value {record.get('id')!r} has an unknown owner")
        for field in ("superseded_patterns", "legitimate_attribution_patterns"):
            item = record.get(field, [])
            if not isinstance(item, list) or not all(isinstance(one, str) for one in item):
                raise CompanionStatusError(f"superseded value {field} must be a string list")
        if not record.get("current_value"):
            raise CompanionStatusError("each superseded_values record needs a current_value")
    return ledger


def _any(patterns: list[str], text: str) -> str | None:
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return pattern
    return None


def _mentions(entry: dict[str, Any], text: str) -> bool:
    for key in entry["cite_keys"]:
        if re.search(rf"(?<![A-Za-z0-9_:]){re.escape(key)}(?![A-Za-z0-9_:])", text):
            return True
    for label in entry["labels"]:
        if re.search(re.escape(label).replace(r"\ ", r"[~\s]+"), text, re.IGNORECASE):
            return True
    return False


# --------------------------------------------------------------------------
# rules
# --------------------------------------------------------------------------
def check_paper(
    root: Path, paper_id: str, tex_rel: str, ledger: dict[str, Any]
) -> list[dict[str, Any]]:
    tex_path = root / tex_rel
    lines = live_lines(tex_path.read_text(encoding="utf-8", errors="replace"))
    keys = cited_keys(lines)
    papers = ledger["papers"]
    phrases = ledger["unpublished_status_phrases"]
    findings: list[dict[str, Any]] = []

    # Bibliography surfaces: inline \bibitem blocks + every live-cited entry of
    # every resolved .bib / .bbl. This is the surface prior sweeps were blind to.
    inline = bib_blocks(lines)
    surfaces: list[dict[str, Any]] = [
        {"kind": "bibitem", "source": tex_rel, **block} for block in inline
    ]
    # Lines inside an inline bibliography block are reported once, as a
    # bibliography surface -- never a second time as body prose.
    bibliography_lines = {number for block in inline for number in block["covered"]}
    body = [(number, line) for number, line in lines if number not in bibliography_lines]
    for bib in bib_sources(root, tex_path, lines):
        rel = bib.relative_to(root).as_posix()
        for key, entry in bib_file_entries(bib).items():
            if key in keys:
                surfaces.append({"kind": "bib-entry", "source": rel, "key": key, **entry})

    def record(rule, target, location, line, evidence, detail):
        findings.append({
            "rule": rule, "paper_id": paper_id, "target_paper_id": target,
            "location": location, "line": line, "evidence": evidence, "detail": detail,
        })

    for target_id, target in papers.items():
        if target_id == paper_id:
            continue
        doi = target.get("published_doi")

        for surface in surfaces:
            text = surface["text"]
            if not (surface["key"] in target["cite_keys"] or _mentions(target, text)):
                continue
            where = f"{surface['source']}:{surface['kind']}:{surface['key']}"
            if doi:
                hit = _any(phrases, text)
                if hit:
                    record(
                        "companion-status", target_id, where, surface["line"], hit,
                        f"bibliography entry describes {target_id} as unpublished while "
                        f"{target_id} is publicly archived at {doi}",
                    )
                elif doi not in text:
                    record(
                        "companion-status", target_id, where, surface["line"], doi,
                        f"bibliography entry for {target_id} does not print its published "
                        f"DOI {doi}; cite what actually resolves",
                    )

        for number, line in body:
            if not _mentions(target, line):
                continue
            if doi:
                hit = _any(phrases, line)
                if hit:
                    record(
                        "companion-status", target_id, f"{tex_rel}:body", number, hit,
                        f"live prose describes {target_id} as unpublished while "
                        f"{target_id} is publicly archived at {doi}",
                    )

    for value in ledger.get("superseded_values", []):
        owner = value["owner"]
        # The owning paper is required to discuss its own superseded value in
        # order to disown it -- never flag the owner's own source.
        if owner == paper_id:
            continue
        target = papers[owner]
        for number, line in body:
            hit = _any(value["superseded_patterns"], line)
            if not hit or not _mentions(target, line):
                continue
            if _any(value.get("legitimate_attribution_patterns", []), line):
                continue
            record(
                "superseded-value", owner, f"{tex_rel}:body", number, hit,
                f"states {owner}'s superseded {value['quantity']} ({hit}) as its result; "
                f"{owner}'s current value is {value['current_value']}",
            )
        for surface in surfaces:
            text = surface["text"]
            if not (surface["key"] in target["cite_keys"] or _mentions(target, text)):
                continue
            hit = _any(value["superseded_patterns"], text)
            if not hit or _any(value.get("legitimate_attribution_patterns", []), text):
                continue
            record(
                "superseded-value", owner,
                f"{surface['source']}:{surface['kind']}:{surface['key']}",
                surface["line"], hit,
                f"bibliography entry cites {owner} by its superseded "
                f"{value['quantity']} ({hit}); current value is {value['current_value']}",
            )

    return findings


def verify(root: Path, ledger_rel: str = DEFAULT_LEDGER) -> dict[str, Any]:
    root = Path(root).resolve()
    candidate = Path(ledger_rel)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise CompanionStatusError(f"unsafe ledger path: {ledger_rel}")
    ledger = load_ledger(root / candidate)
    registry = load_registry(root)
    findings: list[dict[str, Any]] = []
    papers = []
    for paper_id in CANONICAL_IDS:
        tex_rel = registry[paper_id]["tex_path"]
        paper_findings = check_paper(root, paper_id, tex_rel, ledger)
        findings.extend(paper_findings)
        papers.append({
            "paper_id": paper_id,
            "tex_path": tex_rel,
            "verdict": "FAIL" if paper_findings else "PASS",
            "finding_count": len(paper_findings),
        })
    return {
        "schema": SCHEMA,
        "ledger": candidate.as_posix(),
        "ledger_verified_on": ledger.get("verified_on"),
        "published_companions": sorted(
            paper_id for paper_id, entry in ledger["papers"].items()
            if entry.get("published_doi")
        ),
        "unpublished_companions": sorted(
            paper_id for paper_id, entry in ledger["papers"].items()
            if not entry.get("published_doi")
        ),
        "papers": papers,
        "findings": findings,
        "finding_count": len(findings),
        "verdict": "FAIL" if findings else "PASS",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=repo_root())
    parser.add_argument("--ledger", default=DEFAULT_LEDGER)
    args = parser.parse_args(argv)
    try:
        result = verify(args.project_root, args.ledger)
    except (CompanionStatusError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["verdict"] != "PASS":
        for finding in result["findings"]:
            print(
                f"FAIL [{finding['rule']}] {finding['paper_id']} -> {finding['target_paper_id']}"
                f" at {finding['location']}:{finding['line']}: {finding['detail']}",
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
