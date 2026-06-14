---
pattern_id: 054
status: active
first_seen: R39conf-batch-truth-audit (2026-06-13)
papers_observed: [P4, P3, P1A, P5]
finding_count: 8  # ≥2 reviewers × ≥2 papers in R39conf; preceded by single-paper instance in R10v3p1 (pattern-038 precursor)
proposed_by: r-round-pattern-mine 2026-06-13
---

# pattern-054: sigma-mixing undeclared

**Description**: σ values from DIFFERENT null procedures are juxtaposed in abstract, figure captions, or body prose without any qualification, causing readers to assume they are on a common scale and directly comparable. This is an instance of undeclared estimator incommensurability — distinct from pattern-029 (estimator multiplicity with no pre-registered primary), which focuses on which estimator is the headline. Pattern-054 focuses on the reader-deception risk when multiple σ values appear near each other with no disambiguation.

**Evidence (R39conf)**:
- P4 abstract: "+3.64σ" (label-shuffle null) and "+7.93σ" (density-stratified null) appear adjacent to "+0.41σ" and "z=0.70" (both analytic Bonferroni null) within one paragraph. Four different null procedures, zero qualifiers. Multiple reviewers flagged as a MAJOR reader-deception risk.
- P3 §IV: max-stat σ and per-pixel-shuffle σ appear in the same table row label without null-procedure annotation.
- P1A §VI: analytic σ (from Fisher matrix) compared to bootstrap σ in the same summary sentence.
- P5 §II: cross-matching σ significance (MASTER null) adjacent to CW-fraction σ (binomial null).

**Resolution**: Insert per-juxtaposition caveat at each site where ≥2 σ values from distinct null procedures appear within ~3 sentences:

> *σ values in this paragraph arise from distinct null procedures; diagnostic-only, not directly comparable.*

Or inline per-value: "+3.64σ (label-shuffle null)" / "+7.93σ (density-stratified null)". Use the `\sigmadisclaimer{}` macro if defined; otherwise inline parenthetical is required.

**Detection rule (mechanical)**:
```bash
# Step 1: find paragraphs with ≥2 σ values
pdftotext -layout <pdf_path> - | grep -oE '[+−-]?[0-9]+\.[0-9]+σ' | wc -l

# Step 2: within-source grep for adjacent σ values (≥2 within 300 chars)
python3 -c "
import re, sys
text = open(sys.argv[1]).read()
hits = [(m.start(), m.group()) for m in re.finditer(r'[+\-−]?[0-9]+\.[0-9]+\\\\?σ', text)]
for i in range(len(hits)-1):
    if hits[i+1][0] - hits[i][0] < 300:
        print(f'Adjacent σ pair at chars {hits[i][0]}-{hits[i+1][0]}: {hits[i][1]} / {hits[i+1][1]}')
" <tex>
```
False positives: pairs that are ALREADY accompanied by null-procedure qualifier in the same sentence (e.g., "(label-shuffle null)" appears within 50 chars of the σ value). These are allowed.

**Severity**: high (abstract-level juxtaposition); medium (body prose)

**Cross-reference**: pattern-038 (σ values mixed across nulls without per-juxtaposition qualifier) — pattern-038 was first observed in R10v3p1 as a single-paper finding. Pattern-054 is the R39conf cross-paper confirmation (≥2 reviewers × ≥2 papers in the same batch), meeting the bar for catalog promotion. The SKILL.md entry for pattern-038 covers the detection; this pattern-054 extends and names the cross-paper recurrence explicitly.
