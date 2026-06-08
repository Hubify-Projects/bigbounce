---
pattern_id: 041
status: draft
first_seen: auto-2026-06-08_1424pt (fire 14)
papers_observed: [P1B, P2, P3, P5]
finding_count: 4 (single fire — to be re-checked next round)
proposed_by: r-round-pattern-mine fire-14 closeout
---

# Pattern 041 — Meta-reviewer arithmetic check (META-only)

**First seen**: fire 14 (auto-2026-06-08_1424pt) — surfaced by gpt-5-pro meta-reviewer.
**Severity**: HIGH (frequently ESSENTIAL; arithmetic errors block publication).
**Frequency**: 4 firings across 4 papers in fire 14 (P1B, P2, P3, P5).
**Detection**: META-reviewer performs an arithmetic re-derivation from quoted formulas or quoted parameters and finds that the paper's narrative result does NOT match what its own equations + numbers produce.

## Why this is meta-reviewer specific

The 5 per-vendor reviewers verify CITATIONS and detect overclaim/UNDERCLAIM language. They do not, by default, run independent arithmetic on quoted parameters to recompute the headline number. The gpt-5-pro meta-reviewer reads the WHOLE PDF + 5 reviewer reports and is structured to "find what the others missed" — this often manifests as taking the paper's own formula and plugging in the paper's own numbers, then noting that the quoted result doesn't match.

The pattern is reviewer-class-specific in the same way pattern-040 is: per-vendor reviews are LOCAL; the meta-reviewer is GLOBAL.

## Examples observed in fire 14

1. **P1B-META-E1** — paper writes "βALP = 0.336° ± 0.107° (C_aγ = 8 fixed), Δϕ/f_a ∈ [0.2, 1.1]". Using the paper's own formula β = [α_EM/(4π)] C_aγ (Δϕ/f_a) with the max Δϕ/f_a = 1.1: maximum attainable β is much less than 0.336°. The arithmetic doesn't close.
2. **P2-META-E1** — with the standard normalization L ⊃ −(g_aγ/4)φ F F̃ and g_aγ = (α/2π)(C/f_a), the predicted rotation is β = (α/4π) C (Δφ/f_a). Using the paper's own Δφ/f_a ≈ 0.24 and C ~ O(1) gives β ≈ 0.002° — NOT the quoted 0.27°.
3. **P3-META-E4** — paper writes "γ = 2.567 ± 0.382 (median 2.591, 68% CI [2.304, 2.882])". A ±0.382 Gaussian half-width gives 1σ ≈ 0.382; the quoted CI width is 0.578. Either the ± is not 1σ, or the CI is not 68% — internal inconsistency.
4. **P5-META-E1** — Table II canonical V-Web f_CW values {0.4836, 0.5034, 0.4980, 0.4963} give range 0.0198 = 1.98pp. Elsewhere the paper repeatedly states 1.7pp range for the same canonical config. Arithmetic doesn't match.

## Detection rule (mechanical pre-flight)

A bullet-proof preventive check is computationally cheap:

```python
# For each quoted result in the paper's results sections, identify:
#   - the formula the result was computed from
#   - the input parameters quoted elsewhere
# Re-derive symbolically (or numerically) and check ±5% match
```

This would catch:
- β formula vs quoted β
- σ/CI consistency
- range/min/max consistency across tables

Until that's built, the META-reviewer is the canonical detector.

## Truth-audit pre-classification

When this pattern fires, **the verdict is usually VERIFIED but ~25% are
FALSIFIED by meta-reviewer hallucinating the input parameters**. Suggested workflow:

1. Truth-audit by independent re-derivation (10 minutes per finding).
2. **Grep the .tex for the meta-reviewer's quoted input parameters**. If the
   inputs aren't there or are misread (common: confusing a fit result with an
   input), the finding is FALSIFIED.
3. If verified, the fix is usually "fix the quoted result" or "fix the formula"
   — a real bug.

### First firing audit (fire 14, 4 findings)

3/4 VERIFIED, 1/4 FALSIFIED:

| Finding | Verdict | Failure mode |
|---|---|---|
| P3-META-E4 γ-CI | VERIFIED | Real ±-vs-CI mismatch (49% width gap) |
| P5-META-E1 ranges | VERIFIED | Real cross-section contradiction (1.98pp/0.22pp/0.2pp) |
| P1B-META-E1 β bound | VERIFIED (mild 15%) | "Much less" overstated; gap is real but smaller |
| P2-META-E1 β arithmetic | **FALSIFIED** | Meta hallucinated Δφ/f_a=0.24 (confused with MCMC fit β=0.242°) |

The P2 falsification was caught only by reading the actual `.tex` line 54 which
explicitly computes the arithmetic the meta said was missing. Standing rule:
**always grep the .tex for the meta-reviewer's quoted input parameters before
accepting a pattern-041 finding**.

## Reviewer-time cost

Each fix is typically 30 min text + verification rerun. But the cost of NOT catching them is high: every quoted-result-vs-formula inconsistency that survives to publication becomes a citizen-of-the-web errata target.

## Related

- `pattern-040-cross-section-internal-contradiction-DRAFT` — same class (META-only) but contradiction-shaped rather than arithmetic-shaped.
- `pattern-008-closure-introduced-regression` — when the closure FIX of a pattern-041 finding itself introduces new arithmetic errors.
- `pattern-036-closure-fabricates-math-justification` — what NOT to do when closing a 041 (don't fabricate math justifications).

## Promotion-to-prevention plan

- **3+ more firings** across additional papers → promote to `/paper-pre-review-check` as a structured prompt for the meta-reviewer ("re-derive each quoted result from the paper's own formula + parameters").
- **6+ firings + ≥80% verdict consistency** → promote to a dedicated `/quote-formula-recompute-check` skill that runs pre-bump on every paper.
