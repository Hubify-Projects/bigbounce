#!/usr/bin/env python3
"""Fail-closed validation of cross-surface headline-claim dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


SCHEMA = "bigbounce.claim-dependency-graph/v1"
RECEIPT_SCHEMA = "bigbounce.claim-dependency-graph-receipt/v1"


class ClaimGraphError(ValueError):
    pass


def _safe_file(root: Path, relative: str) -> Path:
    candidate = Path(relative)
    if not relative or candidate.is_absolute() or ".." in candidate.parts:
        raise ClaimGraphError(f"unsafe claim-graph path: {relative!r}")
    path = (root / candidate).resolve(strict=True)
    if not path.is_file() or not path.is_relative_to(root):
        raise ClaimGraphError(f"claim-graph path escapes root or is not a file: {relative!r}")
    return path


def _json_pointer(payload: Any, pointer: str) -> Any:
    if not pointer.startswith("/"):
        raise ClaimGraphError(f"JSON pointer must start with '/': {pointer!r}")
    current = payload
    for raw_part in pointer[1:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if isinstance(current, list):
            try:
                current = current[int(part)]
            except (ValueError, IndexError) as exc:
                raise ClaimGraphError(f"JSON pointer does not resolve: {pointer!r}") from exc
        elif isinstance(current, dict) and part in current:
            current = current[part]
        else:
            raise ClaimGraphError(f"JSON pointer does not resolve: {pointer!r}")
    return current


def _file_digest(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {
        "path": path,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def verify(root: Path, graph_path: Path) -> dict[str, Any]:
    root = root.resolve(strict=True)
    graph_path = graph_path.resolve(strict=True)
    if not graph_path.is_relative_to(root):
        raise ClaimGraphError("claim graph must live inside the repository")
    try:
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ClaimGraphError(f"cannot read claim graph: {exc}") from exc
    if graph.get("schema") != SCHEMA:
        raise ClaimGraphError(f"unsupported claim graph schema: {graph.get('schema')!r}")
    claims = graph.get("claims")
    if not isinstance(claims, list) or not claims:
        raise ClaimGraphError("claim graph must contain a non-empty claims list")

    claim_ids: set[str] = set()
    checked_files: dict[str, dict[str, Any]] = {}
    results: list[dict[str, Any]] = []
    for claim in claims:
        if not isinstance(claim, dict):
            raise ClaimGraphError("each claim must be an object")
        claim_id = claim.get("id")
        if not isinstance(claim_id, str) or not claim_id or claim_id in claim_ids:
            raise ClaimGraphError(f"claim IDs must be unique non-empty strings: {claim_id!r}")
        claim_ids.add(claim_id)
        anchors = claim.get("anchors")
        if not isinstance(anchors, list) or len(anchors) < 2:
            raise ClaimGraphError(f"{claim_id} must bind at least two dependency anchors")
        surfaces = set()
        anchor_results = []
        for anchor in anchors:
            if not isinstance(anchor, dict):
                raise ClaimGraphError(f"{claim_id} anchor must be an object")
            relative = anchor.get("path")
            surface = anchor.get("surface")
            kind = anchor.get("kind")
            if not isinstance(relative, str) or not isinstance(surface, str):
                raise ClaimGraphError(f"{claim_id} anchor requires path and surface")
            path = _safe_file(root, relative)
            surfaces.add(surface)
            digest = _file_digest(path)
            checked_files[relative] = {
                "path": relative,
                "bytes": digest["bytes"],
                "sha256": digest["sha256"],
            }
            if kind == "literal":
                expected = anchor.get("expected")
                if not isinstance(expected, str) or not expected:
                    raise ClaimGraphError(f"{claim_id} literal anchor requires expected text")
                text = path.read_text(encoding="utf-8")
                count = text.count(expected)
                minimum = anchor.get("min_occurrences", 1)
                maximum = anchor.get("max_occurrences")
                if not isinstance(minimum, int) or minimum < 1:
                    raise ClaimGraphError(f"{claim_id} min_occurrences must be a positive integer")
                if count < minimum or (
                    maximum is not None and (not isinstance(maximum, int) or count > maximum)
                ):
                    raise ClaimGraphError(
                        f"{claim_id} literal mismatch in {relative}: "
                        f"expected {minimum}..{maximum or 'inf'}, found {count}"
                    )
                detail = {"kind": kind, "occurrences": count, "expected": expected}
            elif kind == "json_pointer":
                pointer = anchor.get("pointer")
                if not isinstance(pointer, str):
                    raise ClaimGraphError(f"{claim_id} JSON anchor requires pointer")
                actual = _json_pointer(json.loads(path.read_text(encoding="utf-8")), pointer)
                expected = anchor.get("expected")
                if actual != expected:
                    raise ClaimGraphError(
                        f"{claim_id} JSON mismatch in {relative}{pointer}: "
                        f"expected {expected!r}, found {actual!r}"
                    )
                detail = {"kind": kind, "pointer": pointer, "value": actual}
            else:
                raise ClaimGraphError(f"{claim_id} uses unknown anchor kind: {kind!r}")
            anchor_results.append({"path": relative, "surface": surface, **detail})
        if len(surfaces) < 2:
            raise ClaimGraphError(f"{claim_id} anchors must span at least two surfaces")
        results.append({
            "id": claim_id,
            "description": claim.get("description", ""),
            "anchor_count": len(anchor_results),
            "surface_count": len(surfaces),
            "anchors": anchor_results,
            "verdict": "PASS",
        })

    graph_raw = graph_path.read_bytes()
    return {
        "schema": RECEIPT_SCHEMA,
        "graph": {
            "path": graph_path.relative_to(root).as_posix(),
            "bytes": len(graph_raw),
            "sha256": hashlib.sha256(graph_raw).hexdigest(),
        },
        "claim_count": len(results),
        "anchor_count": sum(item["anchor_count"] for item in results),
        "checked_files": [checked_files[key] for key in sorted(checked_files)],
        "claims": results,
        "verdict": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--graph",
        default="project-context/claim-dependency-graph.json",
        type=Path,
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    graph = args.graph if args.graph.is_absolute() else root / args.graph
    print(json.dumps(verify(root, graph), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
