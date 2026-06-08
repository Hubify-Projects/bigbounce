#!/usr/bin/env python3
"""
v3 pattern-041 auto-truth-audit — pre-flight check for META arithmetic findings.

Catches the failure mode documented in pattern-041 first-firing (fire 14, 75%
verification rate): meta-reviewer hallucinates input parameters by confusing
fit results with priors (e.g., fire 14 P2-META-E1 used Δφ/f_a=0.24, but the
paper uses Δφ/f_a∈[0.2,1.1] with fiducial 1.07 — the 0.24 came from confusing
it with the MCMC fit β=0.242°).

Approach:
  1. Extract every ESS-tagged finding from the meta review file.
  2. For each finding, pull out numeric input parameters the meta cites
     (formula inputs like "Δφ/f_a ≈ 0.24", "C ~ O(1)", "C_aγ = 8", etc.).
  3. Grep the paper's .tex for each input parameter (allowing typical
     decimal formats).
  4. Report:
       VERIFIED-likely: all cited inputs found in .tex with similar values.
       FALSIFIED-likely: any cited input NOT in .tex (possible hallucination).
       UNCERTAIN: complex finding, can't auto-classify.

Output: a per-finding verdict table for the Houston decision package.

Usage:
    python tools/v3_pattern041_audit.py <meta_review_file> <paper_tex>

Example:
    python tools/v3_pattern041_audit.py \\
        project-context/peer-reviews/auto-2026-06-08_1424pt_P2_META_REVIEW.md \\
        research/focused_paper_source_integration/paper2_alp_birefringence.tex

Exit code = number of findings classified FALSIFIED-likely (saves Houston
time by pre-flagging hallucinations).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SEV_BLOCK_RE = re.compile(
    r"^[\s-]*Severity:\s*ESSENTIAL\s*$", re.MULTILINE
)

# Patterns for "input parameter" claims:
#   "Δφ/fa ≈ 0.24"
#   "Δφ/f_a ≈ 0.24"
#   "C_aγ = 8"
#   "Caγ = 8"
#   "θ_i = 1"
#   "m/H0 ∈ [0.5, 3]"
#   "X = Y" where Y is a number
PARAM_RE = re.compile(
    r"""
    (?:
        # variable names: greek + indices
        [Α-ω_a-zA-Z]+
        (?: [_/\\\\][Α-ω_a-zA-Z0-9]+ )*
        (?: \^ \d+ )?
    )
    \s* (?: \\approx | ≈ | = | \\equiv )
    \s* (?: -)? \s* (\d+\.\d+|\d+)
    """,
    re.VERBOSE,
)

# Capture float-or-int from claims like "≈ 0.24" or "= 8"
NUM_NEAR_RE = re.compile(r"(?:[≈=≈≡])\s*(?:-)?\s*(\d+\.?\d*)")


def extract_ess_blocks(text: str) -> list[dict]:
    """Yield each ESS finding's text block + ID + problem text."""
    lines = text.splitlines()
    sev_idx = [
        (i, m.group(0)) for i, ln in enumerate(lines)
        if (m := re.match(r"^[\s-]*Severity:\s*(ESSENTIAL|MAJOR|MINOR|NIT|FATAL|BLOCKER)\s*$", ln))
    ]
    blocks = []
    for k, (idx, _) in enumerate(sev_idx):
        sev_line = lines[idx]
        if "ESSENTIAL" not in sev_line:
            continue
        end = sev_idx[k + 1][0] if k + 1 < len(sev_idx) else len(lines)
        block_lines = lines[idx:end]
        # Find ID just above the Severity line
        id_str = ""
        for j in range(max(0, idx - 3), idx):
            l = lines[j].strip().lstrip("-").strip()
            mm = re.search(r"\b[PR]\d?[A-Z]?-?META-?[EBMNm]\d+\b", l)
            if mm:
                id_str = mm.group(0)
                break
        text_block = "\n".join(block_lines)
        blocks.append({"id": id_str, "text": text_block})
    return blocks


def extract_input_params(block_text: str) -> list[tuple]:
    """
    Pull (param_name, value) tuples from claims like:
       "Δφ/f_a ≈ 0.24" -> ("Δφ/f_a", 0.24)
       "C_aγ = 8" -> ("C_aγ", 8.0)
       "Δφ/f_a ∈ [0.2, 1.1]" -> ("Δφ/f_a", 0.2), ("Δφ/f_a", 1.1)
    """
    params = []
    # Search for "≈ X" or "= X" preceded by something that looks like a variable
    for m in re.finditer(
        r"([A-ZΑ-ω][\w_Α-ω/\\^]*(?:[_/\\][\w_Α-ω]+)*)\s*[≈=∈≡]\s*(?:\[)?\s*(-?\d+\.?\d*)",
        block_text,
    ):
        var, val = m.group(1), m.group(2)
        try:
            params.append((var.strip(), float(val)))
        except ValueError:
            pass
    return params


def grep_tex_for_value(tex_text: str, value: float, tolerance: float = 0.02) -> list[str]:
    """
    Return list of .tex lines that contain a number within `tolerance` of `value`.
    """
    matches = []
    for ln in tex_text.splitlines():
        for m in re.finditer(r"-?\d+\.?\d+", ln):
            try:
                n = float(m.group(0))
                if abs(n - value) <= tolerance * max(abs(value), 1.0):
                    matches.append(ln.strip()[:160])
                    break
            except ValueError:
                continue
    return matches


def grep_tex_for_param_name(tex_text: str, var: str) -> bool:
    """Return True if variable name (or close variant) appears in .tex."""
    base = re.sub(r"[_/\\^]", " ", var).lower()
    words = [w for w in base.split() if len(w) > 1]
    if not words:
        return False
    tex_lower = tex_text.lower()
    return all(w in tex_lower for w in words)


def grep_tex_for_value_near_variable(tex_text: str, value: float, var: str,
                                      tolerance: float = 0.02,
                                      proximity_chars: int = 200) -> list[str]:
    """
    Stricter check: find every occurrence of `value` in the .tex AND verify
    that the variable name `var` appears within `proximity_chars` characters
    of the match.

    This fixes the false-positive case where the value coincidentally matches
    a different quantity in the .tex (e.g., meta cited "Δφ/f_a=0.24" and the
    .tex has β=0.242° — same digits, different quantity).
    """
    # Translate variable to a regex that matches typical LaTeX forms
    # e.g., "Δφ/f_a" -> r"(?:\\Delta)?\\?phi.{0,5}/.{0,5}f.?_?a"
    var_base = re.sub(r"[_/\\^]", "", var).lower()
    # Generate variant regexes for the variable
    candidates = []
    if "deltaphi" in var_base or "phi" in var_base.replace("delta", ""):
        candidates.append(r"\\Delta\s*\\phi")
        candidates.append(r"\\Delta\\phi")
        candidates.append(r"\\phi")
    if "fa" in var_base or "f_a" in var or "f/a" in var:
        candidates.append(r"f_?a")
        candidates.append(r"f_\{a\}")
    if "agamma" in var_base or "c_a" in var.lower() or "caγ" in var.lower():
        candidates.append(r"C_?\{?a\\?gamma\}?")
        candidates.append(r"C_?\{?a\\?γ\}?")
    if "thetai" in var_base or "theta_i" in var.lower():
        candidates.append(r"\\theta_?i")
    if "mh0" in var_base or "m/h" in var.lower():
        candidates.append(r"m\s*/\s*H_0")
    if not candidates:
        candidates.append(re.escape(var))
    # Look for value occurrences in the .tex, and require variable nearby
    matches = []
    tex_low = tex_text  # keep case for LaTeX
    for m in re.finditer(r"-?\d+\.?\d+", tex_text):
        try:
            n = float(m.group(0))
            if abs(n - value) <= tolerance * max(abs(value), 1.0):
                # Check window for variable name
                start = max(0, m.start() - proximity_chars)
                end = min(len(tex_text), m.end() + proximity_chars)
                window = tex_text[start:end]
                if any(re.search(c, window, re.IGNORECASE) for c in candidates):
                    matches.append(window[max(0, m.start()-start-20):m.end()-start+30].replace("\n"," "))
        except ValueError:
            continue
    return matches


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    meta_file = Path(sys.argv[1])
    tex_file = Path(sys.argv[2])
    if not meta_file.exists():
        print(f"META file not found: {meta_file}", file=sys.stderr)
        sys.exit(2)
    if not tex_file.exists():
        print(f"TEX file not found: {tex_file}", file=sys.stderr)
        sys.exit(2)

    meta_text = meta_file.read_text()
    tex_text = tex_file.read_text()

    blocks = extract_ess_blocks(meta_text)
    print(f"## Pattern-041 audit: {meta_file.name} vs {tex_file.name}\n")
    print(f"Found {len(blocks)} ESSENTIAL findings.\n")

    falsified_likely = 0
    for b in blocks:
        params = extract_input_params(b["text"])
        if not params:
            verdict = "UNCERTAIN (no extractable numeric inputs)"
        else:
            missing = []
            stricter_missing = []
            for var, val in params:
                # Loose check: value anywhere in .tex
                tex_hits = grep_tex_for_value(tex_text, val)
                # Strict check: value within proximity of variable name
                strict_hits = grep_tex_for_value_near_variable(tex_text, val, var)
                name_in_tex = grep_tex_for_param_name(tex_text, var)
                if not tex_hits and not name_in_tex:
                    missing.append(f"{var}={val}")
                if not strict_hits:
                    stricter_missing.append(f"{var}={val}")
            if not missing and not stricter_missing:
                verdict = "VERIFIED-likely (inputs match .tex with variable name in proximity)"
            elif len(missing) == len(params):
                verdict = f"FALSIFIED-likely (none of {len(params)} cited inputs found in .tex)"
                falsified_likely += 1
            elif len(stricter_missing) >= len(params) - 1:
                verdict = f"SUSPICIOUS (loose value matches but no variable proximity for {len(stricter_missing)}/{len(params)} inputs — possible hallucination)"
                falsified_likely += 1
            elif missing:
                verdict = f"PARTIAL (missing: {', '.join(missing[:3])})"
            else:
                verdict = "PROXIMITY-PARTIAL (some values lack variable proximity in .tex)"

        print(f"### {b['id'] or '?'} — {verdict}")
        if params:
            print(f"  Cited inputs ({len(params)}): {[(v, val) for v, val in params[:6]]}")
        # Quote a snippet
        snippet = " ".join(b["text"].splitlines()[1:6])[:200]
        print(f"  Snippet: {snippet}...\n")

    print(f"\n--- SUMMARY ---")
    print(f"Total ESS findings: {len(blocks)}")
    print(f"FALSIFIED-likely (need manual verification): {falsified_likely}")
    sys.exit(falsified_likely)


if __name__ == "__main__":
    main()
