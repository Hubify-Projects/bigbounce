---
pattern_id: dpattern-abstract-mega-paragraph
status: seeded
first_seen: D1-2026-06-19
papers_observed: []
proposed_by: paper-design-round 2026-06-19
---

# dpattern-abstract-mega-paragraph — Abstract is one unbroken wall of text

## Defect

The abstract is typeset as a single dense paragraph of 200–400 words with no
structural breaks. Journal-style readers scan the abstract for (1) motivation,
(2) method, (3) result, (4) implication. A single block forces linear reading
and buries the headline result. External reviewers consistently flag this as
an editorial hygiene issue.

## How to detect

- Visual: in the rendered PDF the abstract block occupies >3 cm of height with
  no visual break or indentation.
- Source: `grep -A 50 '\\begin{abstract}' paper.tex | grep -c '\\n\\n'` — if
  the result is 0, the abstract is a single paragraph.

## Fix

Break the abstract into 2–4 logical paragraphs separated by blank lines:
- Paragraph 1: motivation + problem statement (2–3 sentences).
- Paragraph 2: method + data (2–3 sentences).
- Paragraph 3: headline result with numbers (1–2 sentences).
- Paragraph 4 (optional): implications + context (1–2 sentences).

In revtex4-2 the `abstract` environment renders paragraph breaks normally; no
special markup needed. Keep total word count ≤ 250 words for PRD-style journals.
