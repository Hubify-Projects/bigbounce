# Pattern 056 — pdftotext italic rendering artifact

**Severity:** medium
**Frequency:** 1 confirmed case (P4 EXT11 → EXT12, Table I `NS` / `MS` confusion)

## Description

`pdftotext` (and some PDF-viewer copy-paste paths) can misrender italic LaTeX text
(`\textit{NS}`) as a visually similar string in the extracted plain text. In the
confirmed case, Table I of P4 had the column header `\textit{NS}` (neutron
stars, correctly rendered in the compiled PDF). When the reviewer used `pdftotext`
or a text-layer extraction, the italic glyph shapes produced the token `MS`
(millisecond pulsars), triggering a MAJOR-tier finding about a supposed terminology
error that does not exist in the compiled PDF.

**Root cause:** `pdftotext` parses the glyph → Unicode mapping from the PDF font
table. Italic glyph tables in some font encodings map `N` and `S` italic variants
to different Unicode codepoints or use OCR-based ligature fallbacks that confuse
certain short tokens.

## Trigger conditions

- Source uses `\textit{}` or `\emph{}` around short tokens (2–4 chars) that
  resemble other short tokens under italic rendering
- Reviewer supplies a finding that references a token not present in the compiled
  PDF visual rendering (check the compiled PDF first, not the text layer)

## Pre-review check action

```bash
# Step 1: check compiled PDF visually (pdftoppm → eyeball)
pdftoppm -r 150 paper.pdf /tmp/paper_pages && open /tmp/paper_pages-1.ppm

# Step 2: grep pdftotext layer for suspects
pdftotext paper.pdf - | grep -E "MS|NS|[A-Z]{2}" | head -20

# Step 3: if pdftotext shows a token that doesn't appear in the visual PDF,
#         auto-classify the reviewer finding as ARTIFACT (not REAL)
```

## Closure rule

Findings that stem from pdftotext rendering artifacts are auto-classified as
**ARTIFACT / FALSIFIED** in the truth-audit table. No paper edit needed.
Add a note in the truth-audit that the finding is pdftotext-layer-only and
does not appear in the compiled PDF.

## Example

- **Paper:** P4 v1.0.188 (EXT11, Table I header)
- **Finding:** "Table I shows 'MS' (millisecond pulsars) in the header — should
  be 'NS' (neutron stars)"
- **Truth-audit verdict:** ARTIFACT — source is `\textit{NS}`, compiled PDF
  renders NS correctly; `pdftotext` misread the italic glyph shape as MS.
- **Pattern activated:** EXT11-closure-wave 2026-06-13 (confirmed in EXT12 batch
  truth audit, pattern coded as "pattern-056: residual token grep")

## Related patterns

- [pattern-057](pattern-057-figure-regen-text-residual.md) — body-text residuals
  after systematic rename (text layer mismatch in the other direction: source
  has old token, reviewer sees it)
- [pattern-059](pattern-059-math-mode-subscript-miss-after-rename.md) — math-mode
  subscript miss (pdftotext and grep can diverge in math mode)
