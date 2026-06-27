---
pattern_id: 63
status: draft
first_seen: R52 (2026-06-26)
papers_observed: [P1A, P1B, P2, P3]
finding_count: 7
proposed_by: r-round-pattern-mine 2026-06-26
parent_patterns: [56]
---

# pattern-063: extraction-artifact-false-positive

**Description**: A reviewer flags "garbled math" or "wrong notation" that is in fact
correct in the rendered PDF and `.tex` source — the error exists only in the reviewer's
text-layer extraction or OCR output. The reviewer (or the model reading a pasted
text-extraction) sees mangled glyphs and reports a defect that does not exist.

This is the REVIEWER-FACING analogue of pattern-056 (pdftotext artifact in the
pre-review-check sweep). Pattern-056 catches extraction errors in the automated sweep;
pattern-063 catches the same class when a vendor reviewer reproduces it in their report.

**Root cause**: Some vendor models extract text from PDFs using OCR or pdftotext rather
than rendering the PDF visually. Math glyphs — subscripts, square roots, special
characters, division bars — are particularly fragile in text-layer extraction. The
reviewer receives mangled text and faithfully reports the error.

**Evidence (R52)**:
- P1B: Gemini M1 "Eq.(1) missing factor ½" → FALSIFIED. The ½ IS present in the source (`\tfrac{1}{2}`). Render/extraction artifact.
- P1B: Gemini M4 "broken fn.a/fn.b cross-refs" → FALSIFIED. Caveats (a)-(e) are inline list labels; footnote refs resolve via `\ref{fn:wcaveat}`. Render artifact.
- P2: OpenAI E6 "Eq.(2) dimensional inversion (B_NL ∝ P/A_T)" → FALSIFIED. Source Eq.(2) has A_T in the **numerator**; reviewer misread rasterized math. Gemini + Grok (full PDF) found no such error — corroborates.
- P2: OpenAI m1 "Eq.(2) 'i k^3_i' ambiguous typesetting" → STALE. Source L623 defines `\sum_i k_i^3` explicitly; rasterization read artifact.
- P3: OpenAI E4 / finding D "Cramér's V display omits the √" → STALE/FALSIFIED. L950 shows `V = \sqrt{χ²/(N(k−1))}` correctly applied; reviewer read OCR-broken √ glyph. Changelog L84: fixed in R39conf.
- EXT21/P1A: Gemini "programme mme" duplicate → STALE. Source L794 reads cleanly; extraction artifact.
- EXT21/P1A: Gemini "Eq. (1is not" missing paren → STALE. Source uses `\eqref{eq:torsion}`; renders correctly.

**Why it matters**: Each extraction-artifact finding costs triage time and can pressure
a hasty auditor to "fix" something that is already correct, potentially INTRODUCING an
error. See pattern-036 (closure fabricates math justification) for the failure mode when
this pressure succeeds.

**Detection rule (mechanical)**:
For any math-related FALSIFIED or STALE finding, verify in this order:
```bash
# 1. Check the .tex source directly — the ground truth:
grep -n "<symbol_or_equation>" <source.tex>

# 2. Render the PDF with pdftoppm and visually inspect the relevant equation:
pdftoppm -r 200 -png <paper.pdf> /tmp/pdf_pages
# Open the relevant page in an image viewer

# 3. Cross-check: do other vendors (who rendered the full PDF) report the same?
# If Gemini + Grok (full-PDF) do NOT flag it while OpenAI (text-extraction) does,
# extraction artifact is likely.
```

**Prevention**:
1. Truth-audit rule: for any math finding, ALWAYS verify against the `.tex` source
   before accepting it as VERIFIED. Never accept a "math is wrong" finding solely from
   the reviewer's quoted text.
2. `/peer-review-truth-audit` auto-FALSIFY rule: if the finding involves a math
   expression that parses correctly in the source `.tex` AND no other vendor with
   full-PDF rendering corroborates, classify as extraction-artifact FALSIFIED.
3. Cross-vendor corroboration requirement: math-content findings that appear in ONE
   vendor's report but not in 2+ other vendors' full-PDF reports are extraction-artifact
   candidates.

**Severity**: high — math findings carry high credibility and can pressure incorrect
"fixes." Auto-FALSIFY rule is the correct countermeasure.

**Cross-reference**: Extends pattern-056 (pdftotext artifact in automated sweep) to the
vendor-reviewer context. The pre-review-check catches extraction errors before dispatch;
this pattern catches them when they survive to vendor reports.
