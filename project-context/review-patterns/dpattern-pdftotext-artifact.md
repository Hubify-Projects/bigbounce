---
pattern_id: dpattern-pdftotext-artifact
status: seeded
first_seen: D1-2026-06-19
papers_observed: []
proposed_by: paper-design-round 2026-06-19
---

# dpattern-pdftotext-artifact — Vendor "visual" finding is a pdftotext render artifact (auto-FALSIFY)

## Defect

A vendor reviewer fed the PDF via text extraction (`pdftotext`) reports a visual
defect — "broken equation," "truncated label," "missing subscript," "garbled
symbol" — that does not exist in the rendered document. The defect is an artifact
of the text-extraction layer misrendering glyphs, math fonts, or ligatures. The
paper is visually correct; the finding is noise.

**This is the primary risk in D-rounds**: vendor reviewers receiving extracted
text cannot see the actual layout and routinely hallucinate visual problems.

## How to detect

During D-round truth-audit:
1. If a vendor finding describes a visual symptom (broken equation, truncated
   label, garbled glyph), immediately render the affected page: `pdftoppm -r 200 -png paper.pdf page-N`.
2. Read the rendered image. If the layout is correct, the finding is a
   pdftotext artifact.
3. Check whether that vendor received the PDF as a native file or as extracted
   text. If extracted text, auto-classify the entire visual-defect class as
   FALSIFIED for that vendor.

## Fix

The finding is FALSIFIED — no action on the paper. The fix is at the workflow
level: ensure all D-round vendor reviewers receive the **native PDF** (not
extracted text). Use `tools/v3_native_pdf_review.py` which sends native PDF to
all reviewers. Never use pdftotext-based review tools for D-round visual passes
(see `feedback_review_gap_native_pdf` standing directive).

**Auto-FALSIFY rule**: any finding from a vendor that received pdftotext input,
describing a visual/rendering defect, is classified FALSIFIED without requiring
manual inspection. Flag the vendor delivery method for correction.
