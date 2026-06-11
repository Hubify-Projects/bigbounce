---
pattern_id: 044
status: draft
first_seen: R23conf
papers_observed: [P1B]
finding_count: 2 (two independent wrong pairings in one paper, one round)
proposed_by: r-round-pattern-mine 2026-06-09
---

# Pattern 044 — Wrong-pairing analytic claims (DRAFT)

**Severity**: HIGH (every individual number is real, but the (value, parameter-point) PAIRING is false — undetectable by checking either number alone).
**Shape**: An analytic quantity is quoted at a parameter point where the committed computation gives a DIFFERENT value; the quoted value is real but belongs to a different parameter point. Distinct from pattern-041 (META arithmetic check, where the value itself is wrong) and pattern-007 (reviewer-side arithmetic confab): here both the value and the point exist in the committed grid — they're just paired wrongly, usually because the prose was written from memory of "the table" rather than read off it.

## Recurrence evidence (R23conf)

1. **P1B Δφ/f_a = 1.07 "at m ≈ 2H₀"**: the committed ODE solution (c10b
   artifact) gives Δφ/f_a = 0.42 at m = 2H₀; the value 1.07 occurs at
   m ≈ 4H₀. The quoted value is real — at the wrong mass.
2. **P1B Δφ/f_a = 0.65 "at m = H₀"**: committed ODE gives 0.11 there. The
   pairing fails in the same paper, same section, same round — the whole
   value↔point map was reconstructed from memory.

Both closed in v1B.0.52 by re-pairing against the c10b grid scan.

## Why reviewers miss it

Reviewers (and CCAI passes) check that quoted values appear plausible and that
formulas are dimensionally sane. Verifying a pairing requires EVALUATING the
committed function at the quoted point — repo access + execution, which
PDF-only reviewers never have (pattern-021 blindness). META-arithmetic checks
(pattern-041) catch value-vs-formula breaks but not value-vs-point swaps when
both lie on the genuine solution curve.

## Mechanical detection rule

For each (value, parameter-point) pair in the text (regex anchors:
`at m ≈`, `for [A-Za-zθ_]+ *=`, `evaluated at`, `gives [0-9.]+ at`):

```python
# 1. Locate the committed generating function/ODE (e.g. c10b script).
# 2. Evaluate it at the quoted parameter point.
# 3. Flag if |computed - quoted| / quoted > 5%.
# 4. If mismatch: scan the grid for where the quoted value DOES occur and
#    report the candidate true point (smoking gun for a pairing swap).
```

Step 4 distinguishes this pattern from a plain wrong number: if the quoted
value exists elsewhere on the committed grid, it's a 044 firing, not a 041.

## Prevention hook

- **Belongs in `/paper-pre-review-check`** (quote-formula gate, extending the
  pattern-041 promotion plan): every parameter-point claim must carry (i) the
  generating script reference and (ii) a committed GRID-SCAN artifact covering
  the quoted point, so the pairing is checkable without rerunning the ODE.
- Writing rule: never quote (value, point) pairs from memory — read them out
  of the grid-scan artifact in the same edit that writes the sentence.

## Related

- pattern-041 (META arithmetic check) — value wrong vs pairing wrong.
- pattern-007 (reviewer arithmetic confab) — reviewer-side mirror image.
- pattern-021 (external artifact PDF-blind) — why PDF-only legs can't catch it.

## Promotion criteria

≥2 more confirmed firings on other papers (R24conf+) → promote + fold the
grid-scan evaluation into the pre-bump quote-formula recompute check.
