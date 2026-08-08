#!/usr/bin/env python3
r"""P1C manuscript self-consistency linter.

WHAT THIS GUARDS
-----------------
`arxiv/paper1c_nogo_survey/main.tex` (the P1C "structural no-go survey"
manuscript) went through an iterative-editing failure mode (R11, INT_v3
round `ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV`,
`P1C_claude_r11_leg.md`): a closure edit fixed a defect at some sites but not
others, leaving the abstract, body prose, Table II (`tab:evidentiary_status`),
and the barrier catalog (`\textbf{B1 --- ...}` ... `\textbf{B14 --- ...}`)
asserting mutually contradictory things about the SAME quantity (how many
barrier entries exist, how many Tier-I legs Table II records, whether the
single-scale NDA bound covers the R2 operator, whether every catalog entry
closes a route). This script is a MECHANICAL, deterministic guard against
that regression class recurring. It does not check physics or prose quality
-- only that the manuscript agrees with itself on four specific axes.

WHEN TO RUN IT
---------------
- Before every P1C version bump (`\paperVersion` bump / `directive_g.sh P1C ...`).
- Before every round-closure commit that edits `main.tex` (R-round closures,
  D-round polish, P-round packaging).
- On demand while investigating a "does the paper agree with itself" question.

This is deliberately NOT a git hook. It is not wired into any pre-commit
hook or CI pipeline; it is invoked by hand or by the operator/skill that owns
a round-closure commit, per `ops/RUNBOOK.md`. Nothing in this repo currently
calls it automatically, and it must not be assumed to run on every commit
unless it is explicitly invoked.

HOW TO RUN IT
-------------
    python3 tools/p1c_consistency_check.py
    python3 tools/p1c_consistency_check.py --tex /path/to/other/main.tex
    python3 tools/p1c_consistency_check.py --json
    python3 tools/p1c_consistency_check.py -v

Default `--tex` path is `arxiv/paper1c_nogo_survey/main.tex` resolved from
the repository root (two parents up from this file).

EXIT-CODE CONTRACT
-------------------
    0  all four rules PASS -- the manuscript is self-consistent on the axes
       this tool checks (this is NOT a claim the manuscript is correct or
       complete -- only that it does not contradict itself).
    1  at least one rule FAILED. The human-readable report (and the `--json`
       payload) names the rule, the conflicting values, and every source
       line involved.

THE FOUR RULES
---------------
    A  constraint-count agreement    -- every stated size of the barrier
       catalog (abstract/intro/Sec. III/Fig. 1/Table I/Sec. VI/Sec. VII/
       appendices) must agree with each other and with the actual count of
       `\textbf{B<n> ---` entries in the barrier section.
    B  Tier-(I) count agreement      -- the number of Tier-(I) grade markers
       counted in Table II (`tab:evidentiary_status`) must agree with every
       prose claim about how many Tier-I legs exist ("sole", "the only",
       "exactly one", "two", ...).
    C  assert-vs-disclaim pairs      -- an explicit RULES list of
       (assert_pattern, disclaim_pattern) tuples; FAILs if both members of a
       pair are present, because the disclaim sentence is the paper's
       considered position and the assert sentence is therefore a defect.
    D  universal closure claim       -- FAILs if the manuscript claims EVERY
       catalog entry closes a route while one or more `\textbf{B<n> ---`
       entries self-declare that they are not used as a closure.

HOW TO ADD A NEW RULE (most common extension: Rule C)
-------------------------------------------------------
Rule C is intentionally the cheapest rule to extend: append one 4-tuple to
the module-level `ASSERT_DISCLAIM_RULES` list --
`(name, assert_pattern, disclaim_pattern, explanation)` -- where both
patterns are regexes matched against the whitespace-normalized (line-wrap-
collapsed) manuscript text. No other code changes are required; the CLI,
the PASS/FAIL report, and the test suite all iterate that list generically.
To add a genuinely new AXIS of consistency (not just a new assert/disclaim
pair), add a new `check_rule_x(...)` function following the existing four,
call it from `run_all_rules`, and give it a `RuleResult` like the others.

Strips LaTeX comments (full-line `%...` and inline ` %...` not preceded by
`\`) before analysis so the ~280-line `.tex` changelog header at the top of
`main.tex` -- which mentions old counts and old Tier claims -- does not
produce false positives.
"""

from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEX = ROOT / "arxiv" / "paper1c_nogo_survey" / "main.tex"

WORD_NUMBERS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}

BARRIER_HEADING_RE = re.compile(r"\\textbf\{B(\d+)\s*---")

# ---------------------------------------------------------------------------
# Rule A -- constraint-count agreement
#
# Each pattern is matched against the whitespace-normalized full-document
# text and must capture exactly one \w+ token that is a digit or a
# recognized word-number naming the asserted size of the barrier catalog.
# ---------------------------------------------------------------------------
COUNT_CLAIM_PATTERNS: list[tuple[str, str]] = [
    (
        r"catalog(?:\s+as)?\s*(?:\\emph\{)?\s*(?:yields\s+)?(\w+)\s+distinct\s+"
        r"mechanism-class\s+constraints",
        "catalog ... distinct mechanism-class constraints",
    ),
    (r"(\w+)-entry catalog", "N-entry catalog"),
    (r"(\w+)\s+catalog entries", "N catalog entries"),
    (
        r"Structure of the\s+(\w+)-entry barrier closure",
        "N-entry barrier closure (Fig. 1 caption)",
    ),
    (
        r"giving\s+(\w+)\s+distinct mechanism-class constraints",
        "giving N distinct mechanism-class constraints",
    ),
    (r"The\s+(\w+)\s+catalogue entries", "The N catalogue entries (Table I caption)"),
    (r"catalogue entries\s*---\s*(\w+)\s*distinct", "catalogue entries --- N distinct"),
    (
        r"not\s+(\w+)\s+independently decisive theorems",
        "not N independently decisive theorems",
    ),
    (
        r"(\w+)\s+mechanism-class\s+structural\s+barriers",
        "N mechanism-class structural barriers",
    ),
]

# ---------------------------------------------------------------------------
# Rule B -- Tier-(I) count agreement
#
# Table marker: a bold "(I)" grade cell (robust to a trailing word like
# "Rigorous", and NOT matching "(II)" or "(III)").
# Prose patterns map to the integer count of Tier-I legs they imply.
# ---------------------------------------------------------------------------
TIER_I_TABLE_MARKER_RE = re.compile(r"\\textbf\{\(I\)")

TIER_I_PROSE_PATTERNS: list[tuple[str, int, str]] = [
    (r"sole Tier-I", 1, "sole Tier-I"),
    (r"the only Tier-I", 1, "the only Tier-I"),
    (r"exactly one Tier-I", 1, "exactly one Tier-I"),
    (
        r"only the perturbation-transparency.{0,400}?Tier-I",
        1,
        "only the perturbation-transparency ... Tier-I",
    ),
    (r"\btwo Tier-I", 2, "two Tier-I"),
]

# ---------------------------------------------------------------------------
# Rule C -- assert-vs-disclaim paired phrases
#
# Extensible: to guard a new round's regression, append one 4-tuple here.
# Both patterns are matched against the whitespace-normalized text.
# ---------------------------------------------------------------------------
ASSERT_DISCLAIM_RULES: list[tuple[str, str, str, str]] = [
    (
        "nda_covers_eq1",
        r"the operator is bounded by the single-scale\s+NDA",
        r"do not claim the NDA bound covers",
        "Eq. (1)/the R2 one-loop operator is described as 'bounded by the "
        "single-scale NDA' while the paper's considered position (Sec. IV A) "
        "explicitly disclaims that the NDA bound covers it.",
    ),
    (
        "nda_operator_label",
        r"the NDA one-loop operator",
        r"do not claim the NDA bound covers",
        "Eq. (1) is labelled 'the NDA one-loop operator' -- i.e. claimed as "
        "the operator the NDA bound covers -- while the paper elsewhere "
        "explicitly disclaims that the NDA bound covers it.",
    ),
    (
        "route2_de_nda",
        r"dark-energy leg (is )?closed by the single-scale NDA",
        r"not closed by the single-scale NDA bound",
        "Route 2's dark-energy leg is asserted to be closed by the "
        "single-scale NDA bound somewhere in the manuscript while another "
        "passage states plainly that it is NOT closed by that bound.",
    ),
]

# ---------------------------------------------------------------------------
# Rule D -- universal per-entry closure claim vs self-declared non-closures
# ---------------------------------------------------------------------------
UNIVERSAL_CLOSURE_PATTERNS: list[str] = [
    r"each closing one or more of the four routes",
    r"each closing a specific route",
    r"every entry closes",
    r"each of the fourteen closes",
]

NON_CLOSURE_PATTERNS: list[str] = [
    r"is not, and is not used as, a closure",
    r"never used as a stand-alone closure",
    r"not a closure",
    r"is not used as a closure",
]


# ---------------------------------------------------------------------------
# Comment stripping + whitespace-normalized text with a line-number map.
# ---------------------------------------------------------------------------
def strip_line_comment(line: str) -> str:
    """Strip a LaTeX comment from one line: from the first UNESCAPED '%' to
    end of line. `\\%` (escaped percent) is not a comment start. Preserves
    the rest of the line verbatim (including leading/trailing whitespace)
    so downstream line numbering is untouched."""
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == "\\" and i + 1 < n:
            out.append(ch)
            out.append(line[i + 1])
            i += 2
            continue
        if ch == "%":
            break
        out.append(ch)
        i += 1
    return "".join(out)


def strip_comments(text: str) -> list[str]:
    """Return the list of comment-stripped lines, 1:1 with the original
    line count (line i+1 of the input == lines_stripped[i])."""
    return [strip_line_comment(line) for line in text.splitlines()]


@dataclass
class Document:
    lines: list[str]          # comment-stripped, original line breaks intact
    raw: str                  # '\n'.join(lines) -- comment-stripped, real newlines
    norm: str                 # whitespace-collapsed single string, one doc
    norm_offsets: list[int]   # norm_offsets[i] = start offset of line i+1 in `norm`

    def raw_line(self, offset: int) -> int:
        return self.raw.count("\n", 0, offset) + 1

    def norm_line(self, offset: int) -> int:
        idx = bisect.bisect_right(self.norm_offsets, offset) - 1
        return max(idx, 0) + 1


def build_document(text: str) -> Document:
    lines = strip_comments(text)
    raw = "\n".join(lines)
    parts: list[str] = []
    offsets: list[int] = []
    pos = 0
    for line in lines:
        collapsed = re.sub(r"\s+", " ", line.strip())
        offsets.append(pos)
        parts.append(collapsed)
        pos += len(collapsed) + 1  # +1 for the join separator
    norm = " ".join(parts)
    return Document(lines=lines, raw=raw, norm=norm, norm_offsets=offsets)


def normalize_number(token: str) -> int | None:
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return WORD_NUMBERS.get(token)


def barrier_headings(doc: Document) -> list[tuple[int, int]]:
    """Return [(line, entry_number), ...] for every `\\textbf{B<n> ---`
    catalog-entry heading, sorted by line number."""
    out = []
    for m in BARRIER_HEADING_RE.finditer(doc.raw):
        out.append((doc.raw_line(m.start()), int(m.group(1))))
    out.sort()
    return out


def nearest_entry(headings: list[tuple[int, int]], line: int) -> int | None:
    """Entry number of the last heading at or before `line`."""
    best = None
    for h_line, num in headings:
        if h_line <= line:
            best = num
        else:
            break
    return best


# ---------------------------------------------------------------------------
# Rule results
# ---------------------------------------------------------------------------
@dataclass
class RuleResult:
    rule: str
    title: str
    passed: bool
    evidence: list[str] = field(default_factory=list)
    detail: dict = field(default_factory=dict)


def check_rule_a(doc: Document) -> RuleResult:
    headings = barrier_headings(doc)
    actual_count = len({num for _, num in headings})

    sites: list[tuple[int, int, str]] = []  # (line, value, label)
    seen: set[tuple[int, int]] = set()
    for pattern, label in COUNT_CLAIM_PATTERNS:
        for m in re.finditer(pattern, doc.norm):
            value = normalize_number(m.group(1))
            if value is None:
                continue
            line = doc.norm_line(m.start())
            key = (line, value)
            if key in seen:
                continue
            seen.add(key)
            sites.append((line, value, label))
    sites.sort()

    values = {v for _, v, _ in sites}
    all_values = values | ({actual_count} if headings else set())
    passed = len(all_values) <= 1

    evidence = [
        f"line {line}: asserts {value} ({label})" for line, value, label in sites
    ]
    evidence.append(
        f"actual `\\textbf{{B<n>}} ---` catalog-entry count: {actual_count} "
        f"(entries found: {sorted({n for _, n in headings})})"
    )
    if not passed:
        evidence.insert(0, f"DISAGREEING VALUES: {sorted(all_values)}")

    return RuleResult(
        rule="A",
        title="constraint-count agreement",
        passed=passed,
        evidence=evidence,
        detail={"sites": sites, "actual_count": actual_count},
    )


def check_rule_b(doc: Document) -> RuleResult:
    table_start = doc.raw.find("\\label{tab:evidentiary_status}")
    if table_start == -1:
        return RuleResult(
            rule="B",
            title="Tier-(I) count agreement",
            passed=False,
            evidence=["`\\label{tab:evidentiary_status}` not found in manuscript -- "
                      "cannot locate Table II."],
        )
    block_start = doc.raw.rfind("\\begin{table*}", 0, table_start)
    block_end = doc.raw.find("\\end{table*}", table_start)
    if block_start == -1 or block_end == -1:
        return RuleResult(
            rule="B",
            title="Tier-(I) count agreement",
            passed=False,
            evidence=["Could not bound the `table*` environment containing "
                      "`tab:evidentiary_status` (missing `\\begin{table*}` / "
                      "`\\end{table*}`)."],
        )
    table_body = doc.raw[block_start:block_end]
    table_line_start = doc.raw_line(block_start)
    table_line_end = doc.raw_line(block_end)

    marker_lines = [
        doc.raw_line(block_start + m.start())
        for m in TIER_I_TABLE_MARKER_RE.finditer(table_body)
    ]
    table_count = len(marker_lines)

    prose_sites: list[tuple[int, int, str]] = []
    seen: set[tuple[int, int]] = set()
    for pattern, implied, label in TIER_I_PROSE_PATTERNS:
        for m in re.finditer(pattern, doc.norm, flags=re.IGNORECASE):
            line = doc.norm_line(m.start())
            # Don't count a prose "Tier-I" reference that is itself inside
            # the table body being counted above.
            if table_line_start <= line <= table_line_end:
                continue
            key = (line, implied)
            if key in seen:
                continue
            seen.add(key)
            prose_sites.append((line, implied, label))
    prose_sites.sort()

    mismatches = [(line, implied, label) for line, implied, label in prose_sites
                  if implied != table_count]
    passed = len(mismatches) == 0

    evidence = [
        f"Table II (`tab:evidentiary_status`, lines {table_line_start}-"
        f"{table_line_end}) contains {table_count} Tier-(I) marker(s) at "
        f"line(s) {marker_lines}."
    ]
    for line, implied, label in prose_sites:
        flag = "" if implied == table_count else "  <-- MISMATCH"
        evidence.append(
            f"line {line}: prose asserts {implied} Tier-I leg(s) ({label}){flag}"
        )

    return RuleResult(
        rule="B",
        title="Tier-(I) count agreement",
        passed=passed,
        evidence=evidence,
        detail={
            "table_count": table_count,
            "marker_lines": marker_lines,
            "prose_sites": prose_sites,
            "mismatches": mismatches,
        },
    )


def check_rule_c(doc: Document) -> RuleResult:
    all_evidence: list[str] = []
    any_failed = False
    per_rule: dict[str, dict] = {}

    for name, assert_pattern, disclaim_pattern, explanation in ASSERT_DISCLAIM_RULES:
        assert_lines = sorted(
            {doc.norm_line(m.start()) for m in re.finditer(assert_pattern, doc.norm)}
        )
        disclaim_lines = sorted(
            {doc.norm_line(m.start()) for m in re.finditer(disclaim_pattern, doc.norm)}
        )
        failed = bool(assert_lines) and bool(disclaim_lines)
        any_failed = any_failed or failed
        per_rule[name] = {
            "assert_lines": assert_lines,
            "disclaim_lines": disclaim_lines,
            "failed": failed,
        }
        if failed:
            all_evidence.append(
                f"[{name}] FAIL -- {explanation}\n"
                f"    assert pattern /{assert_pattern}/ found at line(s) "
                f"{assert_lines}\n"
                f"    disclaim pattern /{disclaim_pattern}/ found at line(s) "
                f"{disclaim_lines}"
            )
        else:
            status = (
                "assert absent" if not assert_lines
                else "disclaim absent" if not disclaim_lines
                else "neither present"
            )
            all_evidence.append(f"[{name}] ok ({status})")

    return RuleResult(
        rule="C",
        title="assert-vs-disclaim paired phrases",
        passed=not any_failed,
        evidence=all_evidence,
        detail={"pairs": per_rule},
    )


def check_rule_d(doc: Document) -> RuleResult:
    headings = barrier_headings(doc)

    universal_sites = []
    for pattern in UNIVERSAL_CLOSURE_PATTERNS:
        for m in re.finditer(pattern, doc.norm, flags=re.IGNORECASE):
            universal_sites.append((doc.norm_line(m.start()), pattern))
    universal_sites.sort()

    non_closure_sites: list[tuple[int, str, int | None]] = []
    for pattern in NON_CLOSURE_PATTERNS:
        for m in re.finditer(pattern, doc.norm, flags=re.IGNORECASE):
            line = doc.norm_line(m.start())
            entry = nearest_entry(headings, line)
            non_closure_sites.append((line, pattern, entry))
    non_closure_sites.sort()

    offending_entries = sorted(
        {entry for _, _, entry in non_closure_sites if entry is not None}
    )
    passed = not (universal_sites and non_closure_sites)

    evidence = []
    if universal_sites:
        for line, pattern in universal_sites:
            evidence.append(f"universal claim at line {line}: /{pattern}/")
    else:
        evidence.append("no universal per-entry closure claim found")

    if non_closure_sites:
        for line, pattern, entry in non_closure_sites:
            tag = f"B{entry}" if entry is not None else "(entry unknown)"
            evidence.append(
                f"self-declared non-closure at line {line} ({tag}): /{pattern}/"
            )
    else:
        evidence.append("no self-declared non-closure entries found")

    if not passed:
        evidence.insert(
            0,
            f"FAIL: universal closure claim present while {offending_entries} "
            f"self-declare as non-closures",
        )

    return RuleResult(
        rule="D",
        title="universal per-entry closure claim vs self-declared non-closures",
        passed=passed,
        evidence=evidence,
        detail={
            "universal_sites": universal_sites,
            "non_closure_sites": non_closure_sites,
            "offending_entries": offending_entries,
        },
    )


def run_all_rules(doc: Document) -> list[RuleResult]:
    return [check_rule_a(doc), check_rule_b(doc), check_rule_c(doc), check_rule_d(doc)]


def render_report(results: list[RuleResult], tex_path: Path, verbose: bool) -> str:
    lines = [f"P1C consistency check -- {tex_path}", "=" * 72]
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"\n[Rule {r.rule}] {r.title}: {status}")
        if r.passed and not verbose:
            lines.append("  (no evidence dump -- pass -v/--verbose for detail)")
            continue
        for line in r.evidence:
            for sub in str(line).splitlines():
                lines.append(f"  {sub}")
    lines.append("\n" + "=" * 72)
    n_pass = sum(1 for r in results if r.passed)
    n_fail = len(results) - n_pass
    overall = "PASS" if n_fail == 0 else "FAIL"
    failed_rules = ", ".join(r.rule for r in results if not r.passed)
    summary = f"SUMMARY: {n_pass}/{len(results)} rules passed -- overall {overall}"
    if n_fail:
        summary += f" (failed: {failed_rules})"
    lines.append(summary)
    return "\n".join(lines)


def render_json(results: list[RuleResult], tex_path: Path) -> str:
    payload = {
        "tex_path": str(tex_path),
        "rules": [
            {
                "rule": r.rule,
                "title": r.title,
                "passed": r.passed,
                "evidence": r.evidence,
            }
            for r in results
        ],
        "passed": all(r.passed for r in results),
    }
    return json.dumps(payload, indent=2)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tex", type=Path, default=DEFAULT_TEX,
                         help="Path to the P1C main.tex (default: repo-root "
                              "arxiv/paper1c_nogo_survey/main.tex)")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    parser.add_argument("-v", "--verbose", action="store_true",
                         help="Show evidence for PASSing rules too")
    args = parser.parse_args(argv)

    tex_path = args.tex
    if not tex_path.is_file():
        print(f"error: tex file not found: {tex_path}", file=sys.stderr)
        return 1

    text = tex_path.read_text(encoding="utf-8")
    doc = build_document(text)
    results = run_all_rules(doc)

    if args.json:
        print(render_json(results, tex_path))
    else:
        print(render_report(results, tex_path, args.verbose))

    return 0 if all(r.passed for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
