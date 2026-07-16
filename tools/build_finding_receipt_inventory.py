#!/usr/bin/env python3
"""Build a deterministic HubStack receipt inventory from dated review receipts.

This intentionally does not infer findings from prose. A receipt is parseable only
when it contains explicit severity-tagged issues or an explicit clean-review
statement. All other candidates remain visible as parse gaps.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re
from typing import Any

SCHEMA_VERSION = "finding-receipt-inventory/v1"
DEFAULT_CUTOFF = dt.date(2026, 6, 10)
DATE_RE = re.compile(r"2026-(\d{2})-(\d{2})")
SEVERITY_RE = re.compile(
    r"^\s*(?:(?:[-*+])\s+)?"
    r"(?:\*\*)?"
    r"(?:(?:\d+|[A-Za-z][A-Za-z0-9-]*)[.)-]\s*)?"
    r"(?:\*\*)?\[(BLOCKER|MAJOR|MINOR|NIT)\](?:\*\*)?\s+",
    re.MULTILINE,
)
UTC_RE = re.compile(r"^UTC:\s*([^|\n]+)", re.MULTILINE)
HEADER_RE = re.compile(
    r"^# (?:INT API Review|INT Codex-subscription Review|.*(?:Review|REVIEW).*)",
    re.MULTILINE,
)
RAW_RE = re.compile(
    r"(?:RAW RESPONSE(?:\s*\(verbatim\))?|Raw verbatim response)",
    re.IGNORECASE,
)
EXPLICIT_CLEAN_RE = re.compile(
    r"(?:^|\n)\s*(?:(?:\(\d+\)|(?:\d+|[A-Za-z][A-Za-z0-9-]*)[.)-])\s*)?"
    r"(?:[`*]{0,2})(?:ISSUES?|FINDINGS?)\s*:(?:[`*]{0,2})\s*"
    r"(?:[`*]{0,2})(?:NONE|\(NONE\)|NO\s+(?:ISSUES?|FINDINGS?))(?:[`*]{0,2})"
    r"\s*(?:[.!](?:\s|$)|$)"
    r"|(?:^|\n)\s*(?:[`*]{0,2})(?:ISSUES?|FINDINGS?)\s*:(?:[`*]{0,2})\s*$"
    r"\n\s*(?:[`*]{0,2})?NONE(?:[`*]{0,2})?\s*[.!]?(?:\s|$)"
    r"|(?:^|\n)\s*(?:\(\d+\)\s*)?NO\s+NUMBERED\s+ISSUES?[.!]?\s*$"
    r"|(?:^|\n)\s*(?:\(\d+\)\s*)?NO\s+NUMBERED\s+ISSUES?[.!]?(?:\s|$)"
    r"|(?:^|\n)\s*(?:\(\d+\)\s*)?NO\s+ISSUES?\s+IDENTIFIED[.!]?(?:\s|$)"
    r"|(?:^|\n)\s*I\s+EXPLICITLY\s+STATE\s+THAT\s+NO\s+FRESH\s+VERIFIED\s+"
    r"MAJOR\s+OR\s+MINOR\s+BLOCKERS?\s+EXIST[.!]?(?:\s|$)"
    r"|(?:^|\n)\s*NO\s+(?:ACTIONABLE\s+)?(?:ISSUES?|FINDINGS?)\s*[.!]?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
FAILURE_RE = re.compile(
    r"(?:^|\n)\s*(?:ERROR|FAILED|PROVIDER_ERROR)\s*[:=-]"
    r"|\((?:Codex|Claude|Gemini|Grok|ChatGPT)[^)\n]*\bleg\s+errored\b",
    re.IGNORECASE,
)
SEVERITY_SECTION_RE = re.compile(
    r"^\s*(?:\*\*)?(BLOCKER|MAJOR|MINOR|NIT)\s+ISSUES?\s*:(?:\*\*)?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
SECTION_HEADING_RE = re.compile(
    r"^\s*(?:\*\*)?[A-Z][A-Z0-9 /&()_-]{2,}\s*:(?:\*\*)?\s*$",
    re.MULTILINE,
)
NUMBERED_ITEM_RE = re.compile(r"^\s*\d+[.)]\s+\S", re.MULTILINE)
EXPLICIT_SUMMARY_COUNT_RE = re.compile(
    r"\b(\d+)\s+(BLOCKER|MAJOR|MINOR|NIT)\s+(?:ITEMS?|ISSUES?|FINDINGS?)\b",
    re.IGNORECASE,
)
PARSED_ACCEPT_RE = re.compile(r"^PARSED VERDICT:\s*ACCEPT\s*$", re.MULTILINE)
RAW_ACCEPT_RE = re.compile(
    r"(?:^|\n)\s*(?:\(\d+\)\s*)?(?:\*\*)?VERDICT(?:\*\*)?\s*:\s*"
    r"(?:\*\*)?ACCEPT(?:\*\*)?\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def path_date(relative: pathlib.PurePosixPath) -> dt.date | None:
    dates = []
    for match in DATE_RE.finditer(relative.as_posix()):
        try:
            dates.append(dt.date(2026, int(match.group(1)), int(match.group(2))))
        except ValueError:
            continue
    return max(dates) if dates else None


def is_receipt(path: pathlib.Path, text: str) -> bool:
    name = path.name
    named = bool(
        re.match(r"API_[A-Za-z0-9_-]+\.md$", name)
        or re.match(r"intwave_[A-Za-z0-9_-]+\.md$", name)
        or re.match(r"P(?:1A|1B|1U|[2-5])_(?:grok|gemini|chatgpt)\.md$", name, re.I)
    )
    return named and bool(HEADER_RE.search(text))


def parse_receipt(text: str) -> tuple[str, int | None, str]:
    raw_match = RAW_RE.search(text)
    if FAILURE_RE.search(text) and not raw_match:
        return "failed", None, "explicit provider failure without a raw response"
    if not raw_match:
        return "parse_error", None, "missing explicit RAW RESPONSE boundary"
    raw = text[raw_match.end() :]
    if FAILURE_RE.search(raw):
        return "failed", None, "explicit provider failure in raw response"
    findings = SEVERITY_RE.findall(raw)
    if findings:
        return "ok", len(findings), "explicit severity-tagged findings"
    sections = list(SEVERITY_SECTION_RE.finditer(raw))
    if sections:
        count = 0
        headings = list(SECTION_HEADING_RE.finditer(raw))
        for match in sections:
            end = next(
                (heading.start() for heading in headings if heading.start() > match.start()),
                len(raw),
            )
            body = raw[match.end() : end]
            if re.match(r"^\s*(?:[`*]{0,2})?NONE(?:[`*]{0,2})?\s*$", body, re.I):
                continue
            count += len(NUMBERED_ITEM_RE.findall(body))
        if count:
            return "ok", count, "explicit severity-section numbered findings"
    summary_counts = EXPLICIT_SUMMARY_COUNT_RE.findall(raw)
    if len(summary_counts) == 1:
        return "ok", int(summary_counts[0][0]), "explicit severity-summary finding count"
    if EXPLICIT_CLEAN_RE.search(raw):
        return "ok", 0, "explicit clean-review statement"
    if PARSED_ACCEPT_RE.search(text) and RAW_ACCEPT_RE.search(raw):
        return "ok", 0, "matching parsed and raw ACCEPT verdicts"
    return "parse_error", None, "no explicit tagged findings or clean-review statement"


def generated_at(rows: list[dict[str, Any]], texts: dict[str, str], cutoff: dt.date) -> str:
    timestamps = []
    for row in rows:
        match = UTC_RE.search(texts[row["path"]])
        if not match:
            continue
        value = match.group(1).strip().replace("Z", "+00:00")
        try:
            timestamps.append(dt.datetime.fromisoformat(value).astimezone(dt.timezone.utc))
        except ValueError:
            continue
    if timestamps:
        return max(timestamps).isoformat(timespec="seconds").replace("+00:00", "Z")
    return dt.datetime.combine(cutoff, dt.time.min, tzinfo=dt.timezone.utc).isoformat().replace("+00:00", "Z")


def build(root: pathlib.Path, cutoff: dt.date) -> tuple[dict[str, Any], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    gaps: list[dict[str, Any]] = []
    texts: dict[str, str] = {}
    for path in sorted(root.rglob("*.md")):
        relative = pathlib.PurePosixPath(path.relative_to(root.parent.parent).as_posix())
        date = path_date(relative)
        if date is None or date <= cutoff:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if not is_receipt(path, text):
            continue
        rel = relative.as_posix()
        texts[rel] = text
        status, count, reason = parse_receipt(text)
        digest = sha256(path)
        row = {
            "receipt_id": f"receipt_{hashlib.sha256(rel.encode()).hexdigest()[:20]}",
            "path": rel,
            "sha256": digest,
            "status": status,
            "finding_count": count,
        }
        rows.append(row)
        if status != "ok":
            gaps.append({"path": rel, "status": status, "reason": reason})
    inventory = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at(rows, texts, cutoff),
        "receipts": rows,
    }
    report = {
        "schema_version": "finding-receipt-inventory-report/v1",
        "cutoff_exclusive": cutoff.isoformat(),
        "candidate_receipts": len(rows),
        "parseable_receipts": sum(row["status"] == "ok" for row in rows),
        "failed_receipts": sum(row["status"] == "failed" for row in rows),
        "parse_gap_receipts": sum(row["status"] == "parse_error" for row in rows),
        "explicit_findings": sum(row["finding_count"] or 0 for row in rows),
        "completed_fraction": (
            round(sum(row["status"] == "ok" for row in rows) / len(rows), 6) if rows else None
        ),
        "gaps": gaps,
    }
    return inventory, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path("project-context/peer-reviews"))
    parser.add_argument("--cutoff", type=dt.date.fromisoformat, default=DEFAULT_CUTOFF)
    parser.add_argument("--inventory", type=pathlib.Path, required=True)
    parser.add_argument("--report", type=pathlib.Path, required=True)
    args = parser.parse_args()
    inventory, report = build(args.root, args.cutoff)
    args.inventory.parent.mkdir(parents=True, exist_ok=True)
    args.inventory.write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
