#!/usr/bin/env python3
"""ledger_match.py — DRAFT fingerprint-matcher for the R-round truth-audit ledger pass.

Parses [MAJOR]/[MINOR] findings from a raw reviewer file and fingerprint-matches
each against the "fingerprint:" keyword lines of the paper's canonical disposition
ledger (project-context/peer-reviews/DISPOSITIONS/<P>.md), then emits a draft
markdown table:

    finding # | first 120 chars | best D-id match + score | MATCHED / UNMATCHED

This is a DRAFT for the Opus truth-auditor — NOT a replacement. It exists to kill
the mechanical part of the pattern-066 re-audit churn (matching re-flags against
the existing ledger) so the human/Opus pass only re-derives genuinely-UNMATCHED
findings. The threshold is deliberately conservative: it prefers UNMATCHED over a
false match (a false MATCHED could silently bury a genuinely-new finding).

Exit code: 0 if every finding matched, 2 if any finding is UNMATCHED.

Usage: tools/ledger_match.py <raw-file> <P1U|P1A|P1B|P2|P3|P4|P5>

See canonical spec: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md §3
(Disposition ledgers — MANDATORY FIRST STEP).
"""
import re
import sys
import pathlib

REPO = pathlib.Path("/Users/houstongolden/Desktop/CODE_YOU/bigbounce")
DISP_DIR = REPO / "project-context/peer-reviews/DISPOSITIONS"

# Paper key -> disposition-ledger filename. P1A/P1B/P1U all live in the unified
# P1U ledger on the site side; the ledger dir keys are P1U/P2/P3/P4/P5.
LEDGER_FILE = {
    "P1U": "P1U.md", "P1A": "P1U.md", "P1B": "P1U.md",
    "P2": "P2.md", "P3": "P3.md", "P4": "P4.md", "P5": "P5.md",
}

# Conservative acceptance threshold on the blended score (0..1). Below this a
# finding is reported UNMATCHED even if it has a "best" candidate. Kept low
# enough to catch verbose re-flags whose keyword overlap is diluted by prose,
# but the score is dominated by keyword AGREEMENT (not prose length) so a false
# match still needs several distinctive ledger keywords to co-occur.
MATCH_THRESHOLD = 0.30
# A distinctive-token (number / §ref) hit is worth a strong boost — those are the
# most reliable signal that two findings are the same class (e.g. 268519, 77905,
# val_loss 1.91/0.30). Two or more distinctive hits is near-certain.
DISTINCTIVE_BONUS = 0.22
DISTINCTIVE_BONUS_2PLUS = 0.40

STOPWORDS = set("""
a an the of to in on and or for with without not is are was were be been being
this that these those it its as at by from into than then so such but no nor
paper section claim result results value values figure table set sets same
model models data using used use one two three each other more most only which
what whether does do done can cannot may might must should would could per vs
""".split())

TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.\-/%×σ]*")
# Distinctive tokens: multi-digit numbers, percentages, section refs, sigma etc.
DISTINCTIVE_RE = re.compile(r"(?:\d[\d,\.]{2,}|§\s*[IVXLC0-9.]+|[0-9]+(?:\.[0-9]+)?%|f_?NL|[0-9]+σ)", re.I)


def norm(tok: str) -> str:
    t = tok.lower().strip(".-/").replace(",", "")
    # crude singular fold so prose plurals match curated singular keywords
    # (gates→gate, thresholds→threshold, patches→patche→patch). Only for pure
    # alpha tokens ≥5 chars, to avoid mangling numbers / short codes.
    if t.isalpha() and len(t) >= 5:
        if t.endswith("ies"):
            t = t[:-3] + "y"
        elif t.endswith("ses") or t.endswith("ches") or t.endswith("shes"):
            t = t[:-2]
        elif t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]
    return t


def tokenize(text: str):
    toks = set()
    for m in TOKEN_RE.finditer(text):
        raw = m.group(0)
        t = norm(raw)
        if len(t) >= 2 and t not in STOPWORDS:
            toks.add(t)
        # ALSO split hyphen/slash-joined compounds into their parts so a ledger
        # keyword "three-gate" matches finding prose "three convergent gates"
        # ("three" + "gate") and "read/scored" matches "read" / "scored". This
        # is the dominant re-flag failure mode (curated fp uses compounds; prose
        # spells them out).
        for part in re.split(r"[-/]", raw):
            p = norm(part)
            if len(p) >= 3 and p not in STOPWORDS:
                toks.add(p)
    return toks


def distinctive(text: str):
    out = set()
    # Strip thousands-separators so "268,519" and "268519" collide; keep the
    # decimal-point form intact ("1.91", "0.30", "3.1.152").
    flat = re.sub(r"(?<=\d),(?=\d)", "", text)
    for m in DISTINCTIVE_RE.finditer(flat):
        out.add(norm(m.group(0)))
    # bare distinctive integers (>=3 digits: 200, 12 is too common) + decimals
    for m in re.finditer(r"\b\d{3,}(?:\.\d+)?\b", flat):
        out.add(m.group(0))
    # short but distinctive decimals like 1.91 / 0.30 / 0.92 / 5.67
    for m in re.finditer(r"\b\d\.\d{1,3}\b", flat):
        out.add(m.group(0))
    # section refs like §V, §III
    for m in re.finditer(r"§\s*([IVXLC]+|\d+)", flat):
        out.add("§" + m.group(1).lower())
    return out


def parse_ledger(path: pathlib.Path):
    """Return list of (d_id, fingerprint_tokens, fingerprint_distinctive, raw_fp)."""
    entries = []
    cur_id = None
    for line in path.read_text().splitlines():
        h = re.match(r"^###\s+(D[A-Z0-9]+-\d+)", line)
        if h:
            cur_id = h.group(1)
            continue
        fp = re.search(r"\*\*fingerprint:\*\*\s*(.+)$", line)
        if fp and cur_id:
            raw = fp.group(1).strip()
            kws = [k.strip() for k in raw.split(",") if k.strip()]
            toks = set()
            dist = set()
            for k in kws:
                toks |= tokenize(k)
                dist |= distinctive(k)
            entries.append((cur_id, toks, dist, raw))
            cur_id = None
    return entries


def parse_findings(path: pathlib.Path):
    """Parse [MAJOR]/[MINOR] findings, tolerant of numbered + bold-verdict formats.

    Splits the raw text on [MAJOR]/[MINOR] tags; each finding is the text from one
    tag up to the next tag (or a clear section boundary). Falls back to numbered
    list items if no tags are present.
    """
    text = path.read_text()
    findings = []

    # Primary: split on inline [MAJOR]/[MINOR]/**MAJOR**/**MINOR** tags.
    tag_re = re.compile(r"\[?\*{0,2}(MAJOR|MINOR)\*{0,2}\]?", re.I)
    marks = list(tag_re.finditer(text))
    if marks:
        for i, m in enumerate(marks):
            start = m.start()
            end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
            chunk = text[start:end].strip()
            # strip the leading tag itself from the body for display
            body = tag_re.sub("", chunk, count=1).strip()
            body = re.sub(r"\s+", " ", body)
            if body:
                findings.append((m.group(1).upper(), body))
        return findings

    # Fallback: numbered list items ("1.", "1)", "MAJOR#1", "CG-2", etc.)
    for m in re.finditer(r"^\s*(?:\d+[.)]|[A-Z]{1,4}[-#]\d+)\s+(.+)$", text, re.M):
        body = re.sub(r"\s+", " ", m.group(1).strip())
        if body:
            findings.append(("?", body))
    return findings


def score(finding_body, led_toks, led_dist):
    ftoks = tokenize(finding_body)
    fdist = distinctive(finding_body)
    if not led_toks:
        return 0.0, set(), set()
    overlap = ftoks & led_toks
    # token-overlap component: recall of the ledger fingerprint's keywords
    # (|overlap| / |ledger keywords|). The ledger fp is a terse curated keyword
    # list, so this is the meaningful signal — a re-flag reuses the paper's own
    # distinctive nouns/numbers, which live in the fp.
    tok_score = len(overlap) / max(1, len(led_toks))
    # distinctive-number / §ref agreement is the strongest signal (e.g. 268519,
    # 77905, 195790). Two or more distinctive hits is near-certain same-class.
    dist_hit = fdist & led_dist
    if len(dist_hit) >= 2:
        dist_bonus = DISTINCTIVE_BONUS_2PLUS
    elif dist_hit:
        dist_bonus = DISTINCTIVE_BONUS
    else:
        dist_bonus = 0.0
    return min(1.0, tok_score + dist_bonus), overlap, dist_hit


def main():
    if len(sys.argv) != 3:
        print("usage: ledger_match.py <raw-file> <P1U|P1A|P1B|P2|P3|P4|P5>", file=sys.stderr)
        sys.exit(2)
    raw_path = pathlib.Path(sys.argv[1])
    paper = sys.argv[2].upper()
    if not raw_path.is_file():
        print(f"FAIL: raw file not found: {raw_path}", file=sys.stderr)
        sys.exit(2)
    lf = LEDGER_FILE.get(paper)
    if not lf:
        print(f"FAIL: unknown paper key '{paper}'", file=sys.stderr)
        sys.exit(2)
    ledger_path = DISP_DIR / lf
    if not ledger_path.is_file():
        print(f"FAIL: ledger not found: {ledger_path}", file=sys.stderr)
        sys.exit(2)

    ledger = parse_ledger(ledger_path)
    findings = parse_findings(raw_path)

    print(f"# ledger_match DRAFT — {paper} — {raw_path.name}")
    print()
    print("> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative "
          "threshold (prefers UNMATCHED over a false match). Every UNMATCHED "
          "finding — and every low-score MATCHED — still needs a human/Opus "
          "source-cited disposition per §3.")
    print(f">")
    print(f"> ledger: `{ledger_path.relative_to(REPO)}` ({len(ledger)} D-ids)  |  "
          f"findings parsed: {len(findings)}  |  threshold: {MATCH_THRESHOLD}")
    print()
    print("| # | sev | finding (first 120 chars) | best match | score | status |")
    print("|---|-----|---------------------------|-----------|-------|--------|")

    n_matched = 0
    n_unmatched = 0
    for idx, (sev, body) in enumerate(findings, 1):
        best_id, best_score, best_ov, best_dist = None, 0.0, set(), set()
        for d_id, led_toks, led_dist, _raw in ledger:
            s, ov, dh = score(body, led_toks, led_dist)
            if s > best_score:
                best_id, best_score, best_ov, best_dist = d_id, s, ov, dh
        matched = best_score >= MATCH_THRESHOLD and best_id is not None
        if matched:
            n_matched += 1
            status = "MATCHED"
        else:
            n_unmatched += 1
            status = "**UNMATCHED**"
        snippet = body[:120].replace("|", "\\|").replace("\n", " ")
        best_disp = best_id if best_id else "—"
        print(f"| {idx} | {sev} | {snippet} | {best_disp} | {best_score:.2f} | {status} |")

    total = n_matched + n_unmatched
    rate = (n_matched / total * 100) if total else 0.0
    print()
    print(f"**Match rate: {n_matched}/{total} = {rate:.0f}% MATCHED, "
          f"{n_unmatched} UNMATCHED.**")
    if n_unmatched:
        print(f"\nExit 2 — {n_unmatched} finding(s) need a full §3 truth-audit "
              f"(genuinely-new candidates or too-weak fingerprint overlap).")
        sys.exit(2)
    print("\nExit 0 — every finding fingerprint-matched an existing ledger D-id "
          "(all candidates for the fast re-flag path; still verify closures intact).")
    sys.exit(0)


if __name__ == "__main__":
    main()
