# INT v3 Referee Report — Paper P2

- **Model:** claude-opus-4-8 (subagent, independent referee leg)
- **Date:** 2026-07-17 (PT)
- **Paper:** P2 — "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping" — v1.7.123
- **pdf_sha256:** `3dc6f1c90e71825b828de7020502eb69dc581e9ef129fbf47a7b4d2da1b55cac`
- **Exactness gate:** PASS (computed SHA-256 equals the required binding hash)
- **Venue:** Physical Review D — profile PRD-RESEARCH
- **Pages reviewed:** 1–11 (full manuscript, fresh rigorous referee pass)
- **PARSED VERDICT:** MINOR REVISIONS

---

## Independent verification performed by the referee (not merely read)

Before writing, I re-derived the paper's central benchmark values by hand from the
stated coefficient vector `(c1..c6) = (3, 1, -9, 5, -33, 9)` in Eq. (3)/(4) and the
prefactors of Eqs. (1)-(2), evaluating `B_NL = (10/3) A_T / Σ k_i^3` with
`A_T = 3/(256 k1^2 k2^2 k3^2) K_9`:

- **Squeezed** (k1→0, k2=k3=k): K_9 → -112·k1^2 + O(k1^5); A_T → -21/16;
  B_NL → **-35/16**. ✓ (constant part of K_9 cancels, so no spurious 1/k1^2 divergence — checked)
- **Equilateral** (k1=k2=k3): K_9 = -153; A_T = -459/256; B_NL = **-255/128**. ✓
- **Folded** (k1=2k, k2=k3=k): K_9 = -1152; A_T = -27/8; B_NL = **-9/8**. ✓

All three benchmarks in Table I reproduce **exactly**. I also confirmed:
- Table V per-vertex squeezed column sums to -35/16 and equilateral column to -255/128 (exact).
- ε-order decomposition Eq. (B5): -5/2 + 5/16 + 0 = -35/16 (exact).
- Prefactor consistency Eq.(3)↔Eq.(B4): 3·K_9 = 256 Π k^2 A, including the (5,2,2)
  orbit multiplicity (-33 over 6 ordered triples ↔ -198 over 3 distinct monomials). ✓
- Li et al. cross-check: f_NL = -165/16 + 65/(8 c_s^2) at c_s=1 → -165/16 + 130/16 = -35/16. ✓
- Torsion prefactor arithmetic Eq.(5): (35/16)(3/16)γ²/(1+γ²) = 0.410·[γ²/(1+γ²)] gives
  0.022 (γ=0.2375) → 0.205 (γ=1). ✓ Dimensionally, κ n_ψ²/ρ = M^{-2}·M^6/M^4 = M^0 (dimensionless). ✓
- The four-fermion coefficient (3κ/16)[γ²/(1+γ²)] = (3πG/2)[γ²/(1+γ²)] matches the
  **standard Einstein–Cartan–Holst result** (Perez–Rovelli PRD 73, 044013; Freidel–Minic–Takeuchi PRD 72, 104002).
- Observational arithmetic: r·|f_NL|/0.7 = 0.84·2.1875/0.7 = 2.625 ≈ 2.63σ; naive 2.1875/0.7 = 3.13σ. ✓
  Table III ladder (3.47/3.14/2.32/0.42σ) rounds to abstract's 3.5/3.1/2.3/0.4σ. ✓

**The primary contribution — the exact matter-contraction amplitude f_NL^local = -35/16 —
is correct and independently confirmed.**

---

## (1) VERDICT

**MINOR REVISIONS.**

The central derivation is correct and I verified it independently. Every problematic
claim in the manuscript is already hedged in-text. The required changes are
predominantly citation, rewording, softening of over-precise numbers, and one
clarification/demotion of the torsion-bound derivation status — not new computation and
not overturning any result. Two items (Issues 1–2, both on Eq. 5) are the gating ones;
if the authors cannot upgrade Eq. 5's transfer to a derivation or explicitly demote it to
a parametric estimate, and cannot cite the standard EC–Holst literature for its
coefficient, those escalate to major.

---

## (2) ISSUES

**[MAJOR] 1 — Eq. (5), the torsion bound: the energy-density→amplitude transfer is a
heuristic scaling, not a derived propagation.** The bound is obtained by taking the
fractional torsion energy density ρ_tor/ρ = (3/16)[γ²/(1+γ²)] κ⟨J_5²⟩/ρ and simply
multiplying by 35/16 to get |δf_NL^tor|. This assumes δf_NL/f_NL ~ ρ_tor/ρ, i.e. that a
subdominant energy component shifts the bispectrum amplitude at the fractional level of
its energy density. That is a plausible order-of-magnitude estimate, but it is not a
propagation of the four-fermion operator through the cubic in-in bispectrum, and Eq. (5)
is presented as a "bound" — a word that implies more rigor than a dimensional argument
supplies. Either derive the transfer (even schematically, through the same in-in
machinery used for the -35/16 result) or explicitly demote Eq. (5) to a parametric
estimate/naturalness argument. Additionally, the operator is J_5^μ J_{5μ} =
(J_5^0)^2 - |J_5|^2, a sign-indefinite Lorentz contraction (torsion four-fermion terms
are famously attractive-or-repulsive); replacing it by ⟨J_5²⟩ ≲ n_ψ² collapses that
tensor structure without stating why the contraction is bounded by the number-density
squared.

**[MAJOR] 2 — Eq. (5) coefficient provenance: a load-bearing quantity is cited only to an
unpublished in-preparation companion.** The four-fermion coefficient (3κ/16)[γ²/(1+γ²)],
the finite-Holst factor, and the "dimensional benchmark" are taken "verbatim from the
convention-audited companion paper [13]" (H. Golden, in preparation, hUBIFY-2026-001A). A
referee cannot verify a result whose key coefficient lives in an unpublished paper. As it
happens the coefficient IS the standard Einstein–Cartan–Holst axial-axial four-fermion
result (Perez–Rovelli 2006; Freidel–Minic–Takeuchi 2005), so the fix is straightforward:
cite that published literature so Eq. (5) is self-contained and independently checkable,
rather than gating verifiability on Ref. [13].

**[MINOR] 3 — Abstract vs body tension on "correcting" -35/8.** The abstract states the
result "corrects the unreproduced printed -35/8 literature value," but Appendix B honestly
concedes "We do not claim a complete term-by-term reconstruction of how the published
-35/8 arose," and instead shows the printed polynomial squeezed-reduces to a *third*
number, -305/64. Three inconsistent values (-35/16, -305/64, -35/8) with no closed
error-mechanism. The -35/16 result is well-supported on its own merits (own re-summation +
Cai's ε-grouped intermediates + Li's independent c_s formula at c_s=1), so the paper does
not need the "corrects the literature" framing to stand. Align the abstract's "corrects"
with the body's more careful "identifies one discrepancy; do not reconstruct the printed
value," to avoid over-claiming an overturn of a published number without the mechanism.

**[MINOR] 4 — False precision in the shape overlaps.** r = 0.83542294 and
r_cos = 0.98167825 are quoted to eight significant figures (Sec IV B) for grid-dependent
numerical overlaps that the paper itself brackets with a ±0.02 weighting-scheme envelope
(Eq. 10) and evaluates on a finite triangle grid. Report 3 sig figs (0.835, 0.982); the
8-figure precision is not supported by the calculation.

**[MINOR] 5 — Observational σ-ladder rests on a surrogate the paper says cannot substitute
for the real covariance.** The 2.3–3.5σ values (Table III, Sec VII) come from an "in-house
leading-order Gaussian" multi-tracer covariance that the manuscript repeatedly states
"does not replace the unpublished external per-triangle covariance." Consequently none of
these are usable significance estimates — the section is a methodological illustration
producing no quotable result. This is honestly disclosed (commendably), but the abstract
still parades many conditional σ numbers (3.5σ, 3.1σ, 2.3σ, 0.4σ, 2.63σ, 2.61σ, 3.13σ)
despite explicitly labeling them "not an observational headline." Trim the abstract's σ
enumeration and foreground the b_φ-free 0.4σ floor as the headline caveat so readers
cannot over-read the higher figures.

**[MINOR] 6 — Eq. (5) wording "saturates at the prefactor throughout that domain" is
loose.** The bound is monotonic in x_ψ ≡ κ n_{ψ,c}²/ρ_c and reaches the prefactor
(0.022–0.21) only at the x_ψ→1 edge; for the physically relevant sub-Planckian regime
x_ψ ≪ 1 it is far below. "Saturates throughout" reads as if the maximum is attained
everywhere. Reword to "the bound over the valid domain x_ψ<1 is maximized at the x_ψ→1
edge." Also justify that the spin-coherent ⟨J_5²⟩ ≲ n_ψ² proxy (maximal alignment) is the
correct conservative upper bound and note that thermal/incoherent spins would reduce it.

**[MINOR] 7 — Numerical-grid specification.** The "23,098-triangle ratio grid" recurs but
its k-range, binning scheme, and convergence of r itself are not stated in-text. The
orientation-grid test (marginalized uncertainties change by ≤1.4×10^{-6}) is mentioned,
but the density-convergence of the recovery ratio r and cosine r_cos is not shown. Add a
one-line convergence note and the grid's k-range so the overlaps are reproducible.

**[MINOR] 8 — Confirm no downstream claim depends on Ref. [13] beyond the disclosed
coefficient.** With [13] in preparation and the MegaMapper/future-facility outlook (Sec V)
speculative, verify (and state) that nothing in the abstract, conclusion, evidence claims,
or readiness assessment rests on either — the paper mostly quarantines these already; make
it airtight.

---

## (3) Is the central claim supported?

Yes — I independently re-derived the exact matter-contraction amplitude
f_NL^local = -35/16 (with equilateral -255/128 and folded -9/8) directly from the stated
coefficient vector and confirmed all three reproduce exactly, cross-checked by Li et al.'s
general-c_s formula at c_s=1; the observational mapping is explicitly and consistently
labeled conditional/illustrative and does not overclaim a detection, and the remaining
issues (Eq. 5 rigor/citation and abstract framing) are addressable in place without
disturbing the verified core result.
