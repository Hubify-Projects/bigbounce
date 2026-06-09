#!/usr/bin/env python3
"""
v3 pattern-040 detector — flag cross-section internal contradictions in a paper.

Catches the pattern documented in pattern-040 first-firing (fires 13+14):
META-reviewer finds claims in Section X that contradict claims in Section Y
of the SAME paper. The 5 per-vendor reviewers miss these because they read
locally. Examples from fire 13/14:
  - P1A Sec.IV.D "fine-tuning 10^-61" vs Sec.XII "without fine-tuning"
  - P2 "spectator field" claim vs Ω_φ ≈ 0.17 formula implication
  - P4 "MASTER-deconvolved pseudo-Cℓ" (pseudo = masked NOT deconvolved)
  - P4 v1.0.160 footnote "decoupling absorbs trial-count for pre-MASTER"
    (decoupling is POST-MASTER operation)
  - P5 inter-class range 1.98pp vs per-cell range 0.22pp (same word "range")

Approach (mechanical heuristic, not a definitive detector):
  1. Sweep .tex for "opposite-polarity" claim pairs using a curated list of
     contradictory phrase pairs (e.g., "without fine-tuning" vs "fine-tuning"
     + a quantitative claim).
  2. For each match, report the two sections + the contradicting claims.
  3. The list grows over time as new pattern-040 instances are found in
     subsequent fires.

This is a PRE-FLIGHT check intended to run before every paper bump, NOT
a replacement for the meta-reviewer. Surfaces candidates for author review
in <10 seconds per paper.

Usage:
    python tools/v3_pattern040_cross_section_check.py <paper.tex>

Example:
    python tools/v3_pattern040_cross_section_check.py arxiv/paper1a_ech_nogo.tex

Exit code = number of flagged candidate-contradictions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Curated contradiction-pair patterns. Each entry is:
# (pattern_a, pattern_b, description, severity)
# Both patterns must appear in the .tex for it to be flagged.
CONTRADICTION_PAIRS = [
    (
        r"without\s+fine[- ]?tuning",
        r"(?:dimensionful\s+)?tuning\s+of\s+order|original\s+CC\s+fine[- ]?tuning|relocated?\s+the\s+fine[- ]?tuning|cosmological[- ]?constant\s+problem\s+through\s+the\s+back\s+door|fine[- ]?tuning\s+hierarchy",
        "Section claims 'without fine-tuning' but another section explicitly admits/quantifies fine-tuning",
        "ESSENTIAL",
    ),
    (
        r"spectator\s+(field|alp|axion)",
        r"\\Omega(?:_\\?[a-z]+)?\s*[≈=∼\\sim~]\s*0\.[12]\d?",
        "'Spectator' claim vs Ω ≈ 0.1-0.2 formula (not actually a spectator)",
        "ESSENTIAL",
    ),
    (
        r"master[- ]?deconvolved\s+pseudo[- ]?c[_{]?\\?ell",
        r"pseudo[- ]?c[_{]?\\?ell\s+(?:refers|denotes|is)",
        "Terminology contradiction: 'MASTER-deconvolved pseudo-Cℓ' (pseudo = masked, not deconvolved)",
        "MAJOR",
    ),
    (
        r"decoupling\s+absorbs\s+(?:the\s+)?trial[- ]?count",
        r"pre[- ]?master|pseudo[- ]?c[_{]?\\?ell",
        "Footnote claims MASTER decoupling affects pre-MASTER statistic (decoupling is POST-MASTER)",
        "ESSENTIAL",
    ),
    (
        r"all\s+materials\s+(?:necessary\s+)?(?:to\s+)?reproduce.{0,80}publicly\s+available",
        r"deferred\s+to\s+(?:companion\s+)?(?:work|paper)s?\s+in\s+preparation",
        "Data-availability claim contradicts 'deferred to companion in prep' elsewhere",
        "MAJOR",
    ),
    (
        r"holst[\s\S]{0,300}pontryagin",
        r"R\s*\\*tilde\s*R|pontryagin\s+density",
        "Holst→Pontryagin equivalence claim (Holst has 1 curvature, Pontryagin has 2)",
        "ESSENTIAL",
    ),
    (
        r"range\s+(?:of\s+)?\s*1\.9\d\s*(?:percentage\s+points|pp)",
        r"range\s+(?:of\s+)?\s*0\.\d\s*(?:percentage\s+points|pp)",
        "Two 'range' numbers for canonical config (e.g., 1.98pp vs 0.2-0.22pp)",
        "MAJOR",
    ),
    (
        r"\\sigma\s*\\?pm\s*\d+\.\d+",
        r"68\\%\s*ci\s*\\?\[",
        "Quotes both ± and CI in same line — check arithmetic consistency (pattern-041)",
        "MINOR",  # informational only; the user should run pattern-041 audit
    ),
    (
        # fire 16 P1A-META-E2: Eq.(4) gamma-dependent vs Eq.(13) gamma-free contact coefficient
        # Generalize: same physical coefficient written with two incompatible parametric dependencies
        r"\\frac\{3\\pi\s*G",  # NJL-style coupling A: e.g., (3π G_N/2)
        r"\\frac\{3\}\{16\}\s*\\kappa",  # NJL-style coupling B: e.g., (3/16) κ
        "Two incompatible four-fermion / contact-coupling parametric forms across equations (e.g., Eq.4 vs Eq.13 — pattern-040 cross-eq variant)",
        "ESSENTIAL",
    ),
    (
        # fire 16 P4-META-E2: "T1 flip-swap correlation = 1.000" tautological
        # Detection: claim of a "measured" metric that the methodology enforces by construction
        r"flip[- ]?swap\s+correlation\s*=\s*1\.000",
        r"enforces?\s+flip[- ]?equivariance|by\s+construction",
        "Tautological 'measured' metric — flip-swap correlation = 1.000 is enforced by construction (fire-16 P4-META-E2 family)",
        "ESSENTIAL",
    ),
    (
        # fire 16 P4-META-E3: NaMaster weight uses N_all but A_p variance uses N_spiral
        # Generalize: weight field W_p with one count basis vs variance with different count basis
        r"W_p\s*=\s*N_?\\?{?\\?all\\?}?\\?\(?p\\?\)?|weight\s*\(mask\)\s*map\s*assigns\s*W_p\s*=\s*N",
        r"variance\s+(?:proportional\s+to\s+|is\s+binomial\s+in\s+)N_?\\?{?\\?spiral\\?}?|binomial\s+variance\s+of\s+N_?\\?{?\\?spiral",
        "Weight-variance count-basis mismatch (W_p uses N_all but A_p variance binomial in N_spiral)",
        "MAJOR",
    ),
]


def find_section_for_line(lines: list[str], line_idx: int) -> str:
    """Walk backwards to find the most recent \\section{...} or label{sec:...}."""
    for j in range(line_idx, -1, -1):
        l = lines[j]
        m = re.search(r"\\(?:section|subsection|subsubsection)\*?\{([^}]+)\}", l)
        if m:
            return m.group(1)[:50]
        m = re.search(r"\\label\{(sec:[^}]+)\}", l)
        if m:
            return m.group(1)[:50]
    return "?"


DISAMBIGUATION_CONTEXT_RE = re.compile(
    r"\b(?:distinct from|distinguished from|not equal to|should not be confused with|"
    r"not the same as|"
    r"NOT [a-zA-Z]+|"  # "NOT to Pontryagin"
    r"misidentified|erroneously identified|"
    r"separate (?:topological )?invariant|"
    r"is not the [a-z]+ density|"
    r"have only one|involves \\?emph\{two\}|two curvatures|"
    r"distinguished from|"
    r"differential-form language|"  # disambiguation in my P1A footnote
    r"in differential-form|"
    r"differential[- ]form decomposition|"
    r"correction preserves|"
    r"the headline conclusion|"
    r"this is the|"  # "This is the Bianchi-vanishing of the Holst..."
    r"vanishes identically|"
    r"this should be carefully|"
    r"\\emph\{not\}|"
    r"is \\emph\{not\}|"
    r"reserves|"
    r"reserved for|"
    r"in the prior version|in earlier versions|"
    r"This Bianchi-vanishing is|"
    r"by the first \(algebraic\) Bianchi|"
    r"version of this manuscript)\b",
    re.IGNORECASE,
)


def is_disambiguation_context(window: str) -> bool:
    """
    Return True if the surrounding window is clearly explaining 'X is NOT Y'
    or 'we should not confuse X with Y' rather than asserting 'X = Y'.
    """
    return bool(DISAMBIGUATION_CONTEXT_RE.search(window))


def search_pattern(tex: str, lines: list[str], pattern: str) -> list[tuple]:
    """
    Return list of (line_no, line_text, section) for matches of pattern.
    Now searches both per-line AND text-wide (for multi-line spans).
    Skip matches whose ±300-char window contains explicit disambiguation
    language ("distinct from", "NOT Pontryagin", "misidentified", etc.) —
    these are CORRECTIONS, not assertions of the contradiction.
    """
    matches = []
    seen_lines = set()
    # Per-line pass
    for i, ln in enumerate(lines):
        m = re.search(pattern, ln, re.IGNORECASE)
        if m:
            # Build a ±300-char window from the source text
            # (use line-level neighborhood for simplicity)
            start_line = max(0, i - 4)
            end_line = min(len(lines), i + 4)
            window = "\n".join(lines[start_line:end_line])
            if is_disambiguation_context(window):
                continue
            section = find_section_for_line(lines, i)
            matches.append((i + 1, ln.strip()[:200], section))
            seen_lines.add(i)
    # Text-wide pass: find matches that span multiple lines, locate their start line
    cum = 0
    line_offsets = []
    for ln in lines:
        line_offsets.append(cum)
        cum += len(ln) + 1
    for m in re.finditer(pattern, tex, re.IGNORECASE):
        start = m.start()
        # Find the line number for the start
        for i, off in enumerate(line_offsets):
            if off > start:
                line_no = max(0, i - 1)
                break
        else:
            line_no = len(lines) - 1
        if line_no in seen_lines:
            continue
        # ±300-char window around the match itself
        w_start = max(0, start - 300)
        w_end = min(len(tex), m.end() + 300)
        window = tex[w_start:w_end]
        if is_disambiguation_context(window):
            continue
        section = find_section_for_line(lines, line_no)
        snippet = tex[start:start + 200].replace("\n", " | ")
        matches.append((line_no + 1, snippet, section))
        seen_lines.add(line_no)
    return matches


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    tex_file = Path(sys.argv[1])
    if not tex_file.exists():
        print(f"TEX file not found: {tex_file}", file=sys.stderr)
        sys.exit(2)

    text = tex_file.read_text()
    lines = text.splitlines()
    print(f"## Pattern-040 cross-section contradiction check: {tex_file.name}\n")
    print(f"Scanning {len(lines)} lines against {len(CONTRADICTION_PAIRS)} contradiction-pair rules.\n")

    flagged = 0
    for pat_a, pat_b, desc, sev in CONTRADICTION_PAIRS:
        ma = search_pattern(text, lines, pat_a)
        mb = search_pattern(text, lines, pat_b)
        if ma and mb:
            # Only flag if the matches are in DIFFERENT sections
            sections_a = {m[2] for m in ma}
            sections_b = {m[2] for m in mb}
            if sections_a != sections_b or len(sections_a | sections_b) > 1:
                flagged += 1
                print(f"### {sev}: {desc}")
                for (ln, txt, sec) in ma[:2]:
                    print(f"  A (L{ln}, {sec}): {txt[:140]}")
                for (ln, txt, sec) in mb[:2]:
                    print(f"  B (L{ln}, {sec}): {txt[:140]}")
                print()

    print(f"--- SUMMARY ---")
    print(f"Flagged contradictions: {flagged}")
    print(f"(this is heuristic — not all flags are real; manual review recommended)")
    sys.exit(flagged)


if __name__ == "__main__":
    main()
