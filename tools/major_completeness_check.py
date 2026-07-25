#!/usr/bin/env python3
"""Disposition-completeness check for peer-review rounds.

Encodes the 2026-07-24 rule: severity is read from PER-ITEM TAGS
(`[BLOCKER]` / `[MAJOR]` / `[MINOR]`) in the raw reviewer text, NEVER from the
leg's summary verdict word. A leg whose header says `PARSED VERDICT: MINOR
REVISIONS` may still contain `[MAJOR]`-tagged items, and every tagged item must
carry a source-cited disposition before any convergence claim is written.

That exact mismatch caused the 2026-07-23 six-paper re-sweep to publish
"0 genuinely-new-real outstanding across all six papers" while 4 of the round's
7 tagged MAJORs had never been dispositioned. Record:
project-context/peer-reviews/INT_v3/TRUTH_AUDIT_RESWEEP_2026-07-23.md

Usage
-----
    # inventory only: what tagged items exist, per leg
    tools/major_completeness_check.py ROUND_DIR [ROUND_DIR ...]

    # completeness gate: are they all traceable in the truth-audit doc?
    tools/major_completeness_check.py ROUND_DIR ... --audit path/to/TRUTH_AUDIT.md

Exit codes
----------
    0  clean (inventory printed; with --audit, every MAJOR/BLOCKER traced)
    2  INCOMPLETE — at least one tagged MAJOR/BLOCKER has no trace in the audit
    1  usage / no legs found

The --audit trace is a deliberately CONSERVATIVE token-overlap heuristic: it
prefers flagging an item that was in fact dispositioned under a heavy paraphrase
over silently passing one that was not. A flagged item is a prompt to go read the
audit, not proof of a gap. Resolve every flag by hand — never by lowering
--threshold to make the run green.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

# Legs tag severity as either `[MAJOR]` (Grok/Gemini API legs) or `(MAJOR)`
# (Claude INT legs, e.g. `### F1 (MINOR) — ...`). Both forms count; bare prose
# mentions ("No BLOCKER or MAJOR findings") deliberately do not.
TAG_RE = re.compile(r"[\[(]\s*(BLOCKER|MAJOR|MINOR)\s*[\])]", re.IGNORECASE)
VERDICT_RE = re.compile(
    r"^\s*(?:PARSED VERDICT|VERDICT|Recommendation)\s*[:\-]\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
# Legs are saved either as API_<P>_<vendor>.md or <VENDOR>_INT_<P>_raw.md.
LEG_GLOBS = ("API_*.md", "*_raw.md", "*_INT_*.md", "*_EXT_*.md")

STOPWORDS = {
    "about", "above", "after", "again", "against", "because", "before", "being",
    "below", "between", "both", "cannot", "could", "does", "doing", "during",
    "each", "every", "from", "further", "have", "having", "here",
    "into", "itself", "more", "most", "must", "other", "over", "same", "should",
    "some", "such", "than", "that", "their", "them", "then", "there", "these",
    "they", "this", "those", "through", "under", "until", "very", "were", "what",
    "when", "where", "which", "while", "with", "would", "your", "paper",
    "manuscript", "section", "table", "authors", "author", "shows", "show",
    "given", "using", "used", "also", "explicit", "explicitly", "result",
    "results", "analysis",
}


def tokens(text: str) -> set[str]:
    """Distinctive lowercase tokens: words >=5 chars plus any numeric literal."""
    words = re.findall(r"[A-Za-z][A-Za-z\-]{4,}", text.lower())
    nums = re.findall(r"\d[\d.,]{2,}", text)
    return {w for w in words if w not in STOPWORDS} | set(nums)


def find_legs(round_dir: pathlib.Path) -> list[pathlib.Path]:
    seen: dict[pathlib.Path, None] = {}
    for pattern in LEG_GLOBS:
        for path in sorted(round_dir.glob(pattern)):
            if path.is_file():
                seen[path] = None
    return list(seen)


def extract_items(text: str) -> list[tuple[str, int, str]]:
    """Return (severity, line-number, item-text) for every tagged item.

    An item runs from its tag to the next tag or blank-line break, so the
    matcher sees the whole substance and not just the first clause.
    """
    lines = text.split("\n")
    starts = [(i, m) for i, line in enumerate(lines) for m in [TAG_RE.search(line)] if m]
    items: list[tuple[str, int, str]] = []
    for idx, (line_no, match) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        body: list[str] = []
        for line in lines[line_no:end]:
            if body and not line.strip():
                break
            body.append(line)
        items.append((match.group(1).upper(), line_no + 1, " ".join(body).strip()))
    return items


def verdict_word(text: str) -> str:
    match = VERDICT_RE.search(text)
    return match.group(1).strip()[:40] if match else "(none)"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("round_dirs", nargs="+", type=pathlib.Path)
    parser.add_argument(
        "--audit",
        type=pathlib.Path,
        help="truth-audit markdown; every MAJOR/BLOCKER must be traceable in it",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.40,
        help="fraction of an item's distinctive tokens that must appear in the audit",
    )
    args = parser.parse_args()

    audit_tokens: set[str] | None = None
    if args.audit:
        if not args.audit.is_file():
            print(f"ERROR: audit file not found: {args.audit}", file=sys.stderr)
            return 1
        audit_tokens = tokens(args.audit.read_text(encoding="utf-8", errors="replace"))

    rows: list[tuple[str, str, str, int, int, int, str]] = []
    untraced: list[tuple[str, str, str, int, str]] = []
    any_leg = False

    for round_dir in args.round_dirs:
        if not round_dir.is_dir():
            print(f"ERROR: not a directory: {round_dir}", file=sys.stderr)
            return 1
        label = round_dir.name
        legs = find_legs(round_dir)
        if not legs:
            print(f"WARNING: no reviewer legs matched in {round_dir}", file=sys.stderr)
        for leg in legs:
            any_leg = True
            text = leg.read_text(encoding="utf-8", errors="replace")
            items = extract_items(text)
            # The header's own "PARSED VERDICT:" line is not a finding.
            items = [it for it in items if it[2]]
            n_block = sum(1 for s, _, _ in items if s == "BLOCKER")
            n_major = sum(1 for s, _, _ in items if s == "MAJOR")
            n_minor = sum(1 for s, _, _ in items if s == "MINOR")
            vw = verdict_word(text)
            rows.append((label, leg.name, vw, n_block, n_major, n_minor, ""))

            if audit_tokens is not None:
                for sev, line_no, body in items:
                    if sev == "MINOR":
                        continue
                    item_tokens = tokens(body)
                    if not item_tokens:
                        continue
                    hit = len(item_tokens & audit_tokens) / len(item_tokens)
                    if hit < args.threshold:
                        untraced.append((label, leg.name, sev, line_no, body[:160]))

    if not any_leg:
        print("ERROR: no reviewer legs found in any round directory", file=sys.stderr)
        return 1

    width = max(len(r[1]) for r in rows)
    print(f"{'leg'.ljust(width)}  BLOCK  MAJOR  MINOR  verdict word")
    print("-" * (width + 40))
    for _, leg, vw, nb, nmaj, nmin, _ in rows:
        flag = "  <-- verdict word understates item tags" if (
            nmaj + nb > 0 and re.search(r"minor|accept", vw, re.IGNORECASE)
        ) else ""
        print(f"{leg.ljust(width)}  {nb:5d}  {nmaj:5d}  {nmin:5d}  {vw}{flag}")

    tot_block = sum(r[3] for r in rows)
    tot_major = sum(r[4] for r in rows)
    print(
        f"\nTOTAL across {len(rows)} legs: {tot_block} BLOCKER, {tot_major} MAJOR "
        f"(severity read from per-item tags, not from verdict words)"
    )

    if audit_tokens is None:
        print(
            "\nInventory only. Re-run with --audit <truth-audit.md> to gate the "
            "convergence claim on every MAJOR/BLOCKER being dispositioned."
        )
        return 0

    if untraced:
        print(f"\nINCOMPLETE — {len(untraced)} tagged item(s) with no trace in {args.audit}:")
        for label, leg, sev, line_no, snippet in untraced:
            print(f"  [{sev}] {label}/{leg}:{line_no}\n      {snippet}")
        print(
            "\nAdjudicate each with a source-cited verdict. Do NOT re-word or narrow "
            "the convergence claim to make this pass."
        )
        return 2

    print(f"\nCOMPLETE — every MAJOR/BLOCKER traceable in {args.audit}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
