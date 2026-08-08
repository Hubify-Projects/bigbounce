# P2 — Cai −35/8 vs Li −35/16 factor-of-2: in-in re-derivation attempt

- date: 2026-07-04
- leg: Claude Code INT (Houston subscription), high-judgment physics re-derivation
- target: the #1 verified-reviewer MAJOR on P2 — resolve (or honestly bound) the
  matter-bounce local f_NL factor-of-2 between Cai 2009 (−35/8) and Li 2017 (−35/16 at c_s=1).
- method: fetched both source PDFs (arXiv:0903.0631, arXiv:1612.02036), extracted text,
  read the actual cubic-action / in-in / shape-function / local-limit equations, and
  attempted an independent symbolic re-derivation of the local limit from the published
  shape polynomials under the standard Komatsu–Spergel local f_NL definition.

---

## 1. What both papers actually write (verified verbatim, not P2's prose)

### f_NL normalization — IDENTICAL

- **Cai Eq (21):** `|B|_NL(k1,k2,k3) = 10 A(k1,k2,k3) / (3 Σ_i k_i³)`, with `ζ = ζ_g + (3/5) f_NL ζ_g²` (Eq 20).
- **Li Eq (4.20):** `f_NL(k1,k2,k3) = 10 A_tot(k1,k2,k3) / (3 Σ_i k_i³)`.

These are byte-identical. The `Σ_i k_i³` in the denominator is the SAME symmetric combination
(3-term sum), NOT a single-permutation `k1³`. So the factor-of-2 is **not** in the
normalization and **not** in a "symmetrized vs single-permutation denominator" choice.

### Bispectrum → shape → permutation structure — IDENTICAL

Both build the bispectrum from the same cubic-action vertices and both carry the SAME
permutation bookkeeping. Verbatim from Li:
- Eq (4.11): `⟨ζζζ⟩_redef = ∫ … × ζ_k1 ζ_k2 ζ_k0 ζ_{k3−k0} + (2 permutations)`
- Eq (4.13): `⟨ζζζ⟩_{ζζ̇²} = −2×2 Im ∫dτ̄ … u*u*u… + (2 permutations)`

Cai carries the same `Σ_{i≠j}` / `Σ_{i≠j≠k}` symmetric sums. The `+ (2 permutations)`
appears in BOTH; neither takes a single ordering. So the factor-of-2 is **not** a
"one paper symmetrizes over the 3 momentum permutations, the other doesn't" effect —
they symmetrize identically.

Note also Li Eq (4.13) shows the standard in-in `−2 Im ∫` (i.e. the full `−2Im` of the
nested commutator, both time-orderings included). This directly REFUTES the "Li dropped
the second time-ordering / used −Im not −2Im" mechanism that P2's abstract/Appendix A
asserted: Li's own displayed in-in integral is `−2×2 Im`, not `−Im`. (The prior INT audit
2026-07-03 flagged this same fabricated mechanism; here it is confirmed from Li Eq 4.13.)

### The shared shape polynomial

**Cai Eq (37)** (extracted cleanly):
```
A_T = (3 / (256 Σ k_i²)) [ 3 Σ k_i⁹ + Σ_{i≠j} k_i⁷k_j² − 9 Σ_{i≠j} k_i⁶k_j³
                           + 5 Σ_{i≠j} k_i⁵k_j⁴ − 66 Σ_{i≠j≠k} k_i⁵k_j²k_k²
                           + 9 Σ_{i≠j≠k} k_i⁴k_j³k_k² ]
```
Everything sits inside the `3/(256 Σ k_i²)` prefactor; the naive `Σ k_i³` "local" piece and
the `Σ k_i²k_j` piece have already cancelled at ε = 3/2 (Cai lines ~236: the `(−ε/2 + ε/8)Σk³`
etc. cancel). **Li Eq (4.19)** is the c_s-general version; at c_s=1 the prior INT audit reports
it reduces to Cai Eq (37) coefficient-for-coefficient (the `(10 − 9c_s²) → 1` term etc.).

---

## 2. Independent re-derivation attempt — and why it does NOT settle it

I attempted to compute f_NL^local directly from Cai Eq (37) under the standard definition
`f_NL = 10 A / (3 Σ k_i³)`, taking the local limit k1 ≪ k2 = k3 = k (sympy, exact fractions).

**Result 1 — the naive local limit of Eq (37) is ZERO, not −35/8:**
```
lim_{k1→0} [ 10 A_T / (3 Σ k_i³) ] |_{k2=k3=k}  =  0
```
This is NOT a bug — Cai SAYS SO in the text (line ~550): *"the leading terms cancel and the
total shape function"* → `A_T|_squeezed = −k³` (Cai Eq 44) only AFTER the leading terms cancel
and one keeps the subleading structure. So the published `f_NL^local = −35/8` (Cai Eq 38–39)
is **not** a clean k1→0 limit of the published polynomial; it is the output of a specific
reduction of the "loosely local" configuration k1 ≪ k2 = k3 in which the cancelling leading
pieces and the `Σ k_i²` denominator must be expanded together to a chosen subleading order.

**Result 2 — I cannot even reproduce Cai's OWN equilateral value from Eq (37):**
Under either sum convention (ordered `Σ_{i≠j}` = 6 terms, or unordered = 3 terms), Eq (37) at
k1=k2=k3=k gives
```
ordered:   f_NL^equil = −195/128
unordered: f_NL^equil = −95/128
```
but Cai's published Eq (40) is `f_NL^equil = −255/64 = −510/128`. **Neither matches.**

The equilateral point is fully symmetric and convention-free, so a mismatch there means the
extracted Eq (37) polynomial does **not**, by itself, regenerate Cai's published amplitudes.
The gap is a factor ≈ 2.6 (−510 vs −195), inconsistent with a simple dropped-2. The most
likely cause is that pdftotext scrambled a coefficient/exponent in the two-column Eq (37)
extraction, OR Cai's reduction Eq (37)→(38)/(40) uses intermediate steps (re-expansion of the
`Σ k_i²` denominator, or an additional contribution) that are not recoverable from the printed
polynomial alone.

**Consequence:** the local f_NL in both papers lives in exactly the step my symbolic check
cannot access — the reduction of a shared polynomial whose leading terms cancel, where the
answer depends on how the `Σ k_i²` denominator and the subleading isoceles-limit expansion are
bookkept. That is precisely the −35/8 vs −35/16 divergence point. I cannot arbitrate it from the
polynomials because (a) I cannot reproduce either paper's published amplitude (even the
convention-free equilateral one) from the extracted Eq (37), and (b) the local piece is a
cancellation-sensitive subleading extraction, not a plain limit.

---

## 3. Where Cai and Li actually diverge (the KEY step)

The divergence is **not** in: (i) the f_NL normalization (Eq 21 = Eq 4.20, identical);
(ii) the bispectrum-to-shape factor of 2 or the `+2 permutations` (identical in both);
(iii) a dropped in-in time-ordering (Li Eq 4.13 shows the full `−2×2 Im`, refuting that story).

The divergence IS in **the local-limit reduction of the shared shape polynomial** — the step
where k1 ≪ k2 = k3 is imposed on a polynomial whose leading squeezed terms cancel, so the
result is a subleading extraction sensitive to how the `Σ k_i²` denominator is expanded and
which subleading order is retained. Cai reads off `f_NL^local = −35/8` (Eq 38–39); Li reads off
`f_NL^local = −165/16 + 65/(8c_s²) → −35/16` at c_s=1 (Eq 5.1). Same polynomial, same
normalization, factor-of-2-different reduction. Cai is a coauthor on BOTH papers, and neither
paper flags a disagreement with the other — so there is no published statement of which
reduction supersedes.

---

## 4. VERDICT

**GENUINELY UNRESOLVABLE by careful analytic work at this level — honest disclosed open problem.**
NOT fabricated either way. Specifically:

- The factor-of-2 is a **real, unresolved reduction/bookkeeping discrepancy in the shared
  local-limit extraction** of two overlapping-authorship papers. It is not a
  normalization/convention artifact (ruled out: identical Eq 21 = Eq 4.20), not a
  single-vs-symmetrized-permutation choice (ruled out: both carry `+2 permutations`), and not a
  demonstrable dropped time-ordering (ruled out: Li Eq 4.13 shows `−2×2 Im`).
- I **could not** determine the correct value from first principles, because the local f_NL is a
  cancellation-sensitive subleading reduction of a polynomial that — as extracted — does not even
  reproduce Cai's own convention-free equilateral value. Settling it requires the papers'
  intermediate reduction steps (or a clean re-typeset Eq 37 / Eq 4.19 with the `Σ k_i²`
  denominator expansion), i.e. information not reliably recoverable from the PDFs here. Doing it
  "by hand" from the published polynomials would require reproducing the full four-vertex in-in
  conformal-time integrals and the isoceles-limit expansion from scratch — genuinely beyond a
  tractable symbolic check, and I will NOT fabricate a reduction to force −35/8 or −35/16.

**This is a valid, valuable outcome** (per the CRITICAL RESEARCH DIRECTIVE's spirit: honest
negative result, not a fake resolution). It also independently CONFIRMS the 2026-07-03 INT
audit's integrity fix: P2 must NOT claim to have resolved this via a symbolic operator identity,
and must NOT assert Li dropped a time-ordering (Li Eq 4.13 refutes that).

### Is P2's −35/8 correct / incorrect / convention-dependent?

**Correct-as-an-ADOPTED-value, origin-of-the-2 unresolved.** −35/8 is a real published value
(Cai Eq 39) in the standard normalization and local limit; adopting it as the central value is
defensible IF and ONLY IF P2 discloses that the Cai/Li factor-of-2 is an unresolved literature
discrepancy and carries −35/16 as a real robustness branch. −35/8 is NOT demonstrably "more
correct" than −35/16 — I could not establish which reduction is right.

### Does P2 need a value change / new significance?

**No forced central-value change.** Keep −35/8 as the adopted Cai value WITH the honest
unresolved-discrepancy disclosure and the −35/16 stress branch already in the paper (halves
every significance: the SPHEREx optimistic ~5.2σ → ~2.6σ, and the post-systematic band
~2.75σ → ~1.3–1.4σ on the −35/16 branch). The paper already computes this ×½ band; the fix is
to keep it as a disclosed robustness band, not to headline −35/8 as resolved.

---

## 5. Proposed P2 .tex edit (DO NOT APPLY — for orchestrator review)

The 2026-07-03 INT audit already made the integrity edits (retracted the fabricated
single-time-ordering mechanism; relabeled −35/16 as a real stress branch). This re-derivation
ADDS one strengthening: cite Li Eq (4.13)'s explicit `−2×2 Im` as the positive refutation of the
dropped-time-ordering story, and state the divergence point precisely.

Suggested replacement for the P2 sentence describing the origin of the factor-of-2
(in Sec II.C / Appendix A, wherever the current disclosure sits):

> The Cai (2009) local value $f_{\rm NL}^{\rm local}=-35/8$ and the Li \emph{et al.}\ (2017)
> value $-165/16+65/(8c_s^2)\to-35/16$ at $c_s=1$ share an identical $f_{\rm NL}$ normalization
> ($10A/3\sum_i k_i^3$; Cai Eq.~21 $=$ Li Eq.~4.20), identical permutation bookkeeping (both carry
> the full $+\,2$ permutations), and — at $c_s=1$ — a coefficient-for-coefficient identical shape
> polynomial. The factor of two is therefore \emph{not} a normalization, permutation, or
> time-ordering artifact: Li's in-in integral (their Eq.~4.13) is written as $-2\times2\,\mathrm{Im}\int$,
> so no time-ordering is dropped. The discrepancy resides entirely in the reduction of this shared
> polynomial to the loosely-local configuration $k_1\ll k_2=k_3$, whose leading squeezed terms
> cancel, leaving a subleading extraction sensitive to the bookkeeping of the $\sum_i k_i^2$
> denominator. We were unable to determine which reduction is correct from the published
> expressions and treat it as an unresolved literature discrepancy: we adopt $-35/8$ as the central
> value and carry $-35/16$ as a real robustness branch that halves every reported significance.

Also: fix P2's miscite ("CaiBrandenberger:2014" → Li, Quintin, Wang, Cai 2017, JCAP 03:031,
arXiv:1612.02036), if not already fixed.

---

## 6. Integrity note

I did NOT invent a resolution. I ruled out three candidate mechanisms with verbatim source
equations, localized the divergence to the shared-polynomial local-limit reduction, attempted an
independent symbolic derivation, and found it could not reproduce even the convention-free
published equilateral value — so I honestly report the factor-of-2 as an unresolved, disclosed
open problem for a human referee, consistent with the standing "never fabricate a derivation"
gate (pattern-036) and the recalibrated convergence directive.
