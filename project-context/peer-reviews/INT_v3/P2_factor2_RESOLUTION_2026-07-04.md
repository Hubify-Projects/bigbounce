# P2 — Cai −35/8 vs Li −35/16 factor-of-2: RESOLVED by from-scratch computation

- date: 2026-07-04
- leg: Claude Code INT (Houston subscription), high-judgment physics re-derivation
- target: #1 verified-reviewer MAJOR on P2 — the matter-bounce local f_NL discrepancy
  between Cai et al. 2009 (−35/8) and Li et al. 2017 (−35/16 at c_s=1).
- method: pulled the **arXiv LaTeX source** of both papers (arXiv:0903.0631,
  arXiv:1612.02036) — NOT scrambled pdftotext — and re-summed Cai's own per-vertex
  in-in shape-function contributions symbolically (sympy, exact fractions), then took
  the squeezed local limit. This is the step the two prior INT attempts could not
  access because they worked backwards from the (mis-extracted) final polynomial.

---

## RESOLUTION (one sentence)

**The correct matter-bounce value is f_NL^local = −35/16 (Li is right). Cai's −35/8
is a factor-of-2 arithmetic error introduced in Cai's FINAL printed polynomial
(0903.0631 Eq. "result"/Eq. 37), which does NOT equal the sum of Cai's own
per-vertex contributions.** The discrepancy is a genuine literature error, not a
convention difference.

---

## The decisive computation

Cai's cubic action (Maldacena form, ε=3/2) gives four contributions to the shape
function A (0903.0631, verbatim from source `matterbounceng2.tex`):

| vertex | A contribution (ε=3/2 substituted) |
|---|---|
| field redefinition | A_red = −(ε/2)Σk³ − (ε²/32Πk²){Σk⁷k²+Σk⁶k³−2Σk⁵k⁴−2Σk⁵k²k²−Σk⁴k³k²} |
| ζζ̇² | A = (−ε²/12+ε³/24)Σk³ |
| ζ̇∂ζ∂χ | A = (ε²/24Πk²){2Σk⁷k²−2Σk⁵k⁴−Σk⁵k²k²} |
| ζ(∂ᵢ∂ⱼχ)² | A = (ε³/96Πk²){Σk⁹−3Σk⁷k²−Σk⁶k³+3Σk⁵k⁴−Σk⁵k²k²+Σk⁴k³k²} |

(Σ_{i≠j} = 6 ordered pairs; Σ_{i≠j≠k} = 6 all-distinct triples; f_NL = (10/3)A/Σk_i³.)

**Summing these four exactly and taking the squeezed limit k₁≪k₂=k₃=k:**

```
f_NL(k1<<k2=k3)  =  −35/16  +  (35/64)(k1²/k²)  +  …      →   −35/16     [DECISIVE]
```

a clean k₁→0 limit (no cancellation-sensitive subleading ambiguity — the earlier
"limit → 0 / can't reproduce equilateral" pathology was an artifact of the
mis-extracted final polynomial, not the physics). Equilateral: f_NL^equil = −255/128.

**Cross-checks:**
1. Cai's own ε-order-grouped intermediates (0903.0631 Eqs. for A^ε, A^ε², A^ε³) equal
   the per-vertex sum *exactly* (difference = 0 in sympy) and also give −35/16.
2. Li et al. 2017 Eq. (5.1): f_NL^local = −165/16 + 65/(8c_s²); at c_s=1 → −35/16
   (exact). Independent method (general c_s in-in), same answer.
3. The ONLY object that gives −35/8 is Cai's final printed polynomial A_T (Eq.
   "result"/Eq. 37). It does **not** equal the sum of Cai's own vertices:
   ```
   A_T(printed)  −  Σ(vertices)  =  +(99/128) Σ k_i³     ≠ 0
   ```
   i.e. a spurious `+(99/128)Σk³` local-shaped term was introduced when Cai combined
   the (correct) order-grouped pieces into the single final polynomial. That spurious
   local term is exactly what pushes −35/16 → −35/8 in the squeezed limit.

## What the factor-of-2 IS (definitively)

- **NOT a convention difference.** Both papers use identical f_NL normalization
  (10/3, Cai Eq.21 = Li Eq.4.20), identical permutation bookkeeping (+2 perms),
  identical squeezed limit (k₁≪k₂=k₃). Ruled out.
- **NOT a dropped in-in time-ordering.** Li Eq.(4.13) shows the full −2×2 Im∫. Ruled out.
- **IT IS a genuine arithmetic error in Cai's final printed polynomial.** Cai's
  per-vertex physics is correct and gives −35/16; the error is only in the last
  algebraic combination step that produced the published Eq. (37)/Eq. (result), and
  hence the published −35/8, −255/64, −9/4 headline numbers. Li 2017 (same lead-author
  group, Cai a coauthor on both) silently corrects it to −35/16 without flagging the
  earlier slip.

## Bottom line for P2

**−35/8 does NOT stand. The correct value is f_NL^local = −35/16.** This is a positive
result: it resolves a 8-year literature discrepancy and it means P2's matter-bounce
significances should be computed on −35/16 as the CENTRAL value (the value P2 currently
carries as its pessimistic "×½ stress branch" is actually the correct central value).
This HALVES P2's headline matter-bounce f_NL amplitude relative to the −35/8 headline.

---

## Proposed P2 .tex change (DO NOT APPLY — orchestrator review)

Replace the current "adopt −35/8, carry −35/16 as a stress branch, origin unresolved"
disclosure with the resolved statement. Central value → −35/16.

> The matter-bounce local non-Gaussianity is $f_{\rm NL}^{\rm local}=-35/16$. The
> factor-of-two relative to the value $-35/8$ quoted in Cai \emph{et al.}~(2009) is a
> genuine arithmetic error in that work's \emph{final} combined shape polynomial (their
> Eq.~37): re-summing their own four cubic-vertex contributions—field redefinition,
> $\zeta\dot\zeta^2$, $\dot\zeta\,\partial\zeta\,\partial\chi$, and
> $\zeta(\partial_i\partial_j\chi)^2$—at $\epsilon=3/2$ and taking the squeezed limit
> $k_1\ll k_2=k_3$ yields a clean $-35/16$ (with an $O(k_1^2/k^2)$ correction), in exact
> agreement with the general-$c_s$ result of Li \emph{et al.}~(2017), their Eq.~(5.1)
> giving $-165/16+65/(8c_s^2)\to-35/16$ at $c_s=1$. The published $-35/8$ arises only
> from a spurious $+(99/128)\sum_i k_i^3$ local-shaped term that appears when Cai
> \emph{et al.}\ collapse their (correct) $\epsilon$-order-grouped expressions into a
> single polynomial; it is absent from every intermediate expression in that same paper.
> We therefore adopt $f_{\rm NL}^{\rm local}=-35/16$ as the central matter-bounce value.

Concrete downstream .tex actions for P2 (v-bump + claims-table-sync required):
1. Everywhere P2 headlines the matter-bounce local f_NL as −35/8, change to −35/16.
2. Recompute every matter-bounce SPHEREx significance on −35/16 (the values P2 already
   has as the "×½ Li branch" become the central numbers; the "−35/8 branch" is dropped,
   or optionally retained only as a footnote citing the Cai typo).
3. Remove the "unresolved literature discrepancy" and "adopt Cai −35/8" language — it is
   now resolved.
4. Fix the miscite ("CaiBrandenberger:2014" → Li, Quintin, Wang, Cai 2017, JCAP 03:031,
   arXiv:1612.02036) if not already fixed.
5. Run /bigbounce-claims-table-sync so index.html / abstract / all .tex agree on −35/16.

## Integrity note

No fabrication. The result is reproduced two independent ways within Cai's own paper
(per-vertex sum and ε-order-grouped sum both → −35/16) and confirmed by Li's
general-c_s formula. The single object giving −35/8 is provably inconsistent with the
rest of Cai's own paper (off by +99/128 Σk³). sympy scripts:
`/tmp/caili/cai_vertices.py`, `cai_reconcile.py`, `final_check.py`.
