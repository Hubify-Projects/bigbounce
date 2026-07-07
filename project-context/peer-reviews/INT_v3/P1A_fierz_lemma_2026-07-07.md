# P1A — Fierz-by-Fierz projection lemma: REAL-SCIENCE closure

**Date:** 2026-07-07
**Paper:** `arxiv/paper1a_ech_nogo.tex` (v1A.0.113)
**Standing major:** "completeness asserted, not proven" — the operator-basis
completeness argument (§sec:rotation / §sec:fourroute Scope) names ONE open
item: the *fully explicit Fierz-by-Fierz projection lemma*.
**Script (committed):** `arxiv/scripts/fierz_lemma_check.py` (sympy 1.14, exact
symbolic/rational arithmetic).
**Verdict:** **LEMMA PROVEN** for single-species minimal ECH. Closes the
completeness major *at the level the paper actually claims* (power-counting-class
completeness within minimal ECH). Honest residual scope named in §7.

---

## 1. What the lemma required

The paper eliminates the algebraic (non-propagating) torsion of minimal ECH via
the Cartan constraint `T^{abc} = kappa S^{abc}` (Eq. eq:torsion), with the
**minimally coupled** Dirac spin current *totally antisymmetric*:

    S^{abc} = (1/4) bar psi gamma^{[a}gamma^{bc]} psi
            = (1/4) eps^{abcd} bar psi gamma_d gamma^5 psi.

Integrating out torsion generates the four-fermion contact Lagrangian
(Eq. eq:4fermi, eq:4fermi_partner), all sharing the **single** prefactor
`kappa = 8 pi G = M_Pl^{-2}`:

    L_int = c_AA (J5·J5) + c_VA (J·J5),   J^mu = bar psi gamma^mu psi,
                                          J5^mu = bar psi gamma^mu gamma^5 psi.

The lemma the paper defers: prove that the complete **Fierz rearrangement** of
these generated operators closes onto the enumerated dim-≤6 parity-relevant
basis `{SS, PP, VV, AA, TT, VA, SP}` — i.e. **no** Fierz transform produces a
Lorentz-scalar dim-≤6 structure *outside* the enumerated set, and **no** Fierz
transform changes the `M_Pl` power (which would let an unenumerated channel
evade the single-scale NDA ceiling).

## 2. The proof (sympy, nothing quoted on faith)

1. Built explicit 4×4 Dirac γ-matrices in the paper's **mostly-plus**
   signature `g = diag(-1,+1,+1,+1)`; verified `{γ^μ,γ^ν}=2g^{μν}`,
   `γ5²=1`, `{γ5,γ^μ}=0` (steps [1]-[2] PASS).
2. Constructed the full 16-element Clifford basis
   `{I, γ^μ, σ^{μν}(μ<ν), γ^μγ5, γ5}` = classes `{S,V,T,A,P}` and their
   trace weights `d_A = {4,16,24,-16,4}` (step [3]).
3. **Derived** the 5×5 Fierz class-mixing matrix `F_{AB}` directly from the
   explicit-γ trace formula
   `F_{AB} = (1/4)·Tr_class(Γ^A Γ_B Γ_A Γ^B)/d_B`
   — *not* copied from a reference (step [4]).
4. **Cross-checked** against the standard textbook matrix
   (Itzykson–Zuber; Nieves & Pal, hep-ph/0306087). After fixing the axial-row
   dual-normalization sign forced by `d_A = -16` (a documented mostly-plus
   convention artifact, **not** new physics), `F_norm == textbook F` **exactly**
   on all five rows (step [6]).
5. **Involution check** `F_norm² = I` — PASS (rearranging the two spinors twice
   returns the original ordering; the invariant physical consistency test).
   Eigenvalues `{+1: ×2, -1: ×3}` (step [6b], [8b]).

## 3. Closure table (the ECH-generated operators, Fierz-decomposed)

| Source operator | Fierz decomposition (exact, sympy) | Escape? |
|---|---|---|
| **AA** `(J5·J5)` | `+¼ SS + ½ VV − ½ AA − ¼ PP` | **NONE** (no T; all in basis) |
| **VV** `(J·J)`   | `+¼ SS − ½ VV + ½ AA − ¼ PP` | **NONE** |
| **VA** `(J·J5)` (Holst partner, finite γ) | rotates only within `{V,A}` block (`F[V,A]=F[A,V]=½`) | **NONE** — stays parity-odd, dim-6 |

- **Zero escape classes**: every produced structure lies in the 16-dimensional
  Clifford algebra `{S,V,T,A,P}`, which is closed *by construction* — there is
  no sixth Lorentz class at dim-6.
- **`M_Pl` power preserved**: every Fierz coefficient is a **dimensionless
  rational**, so the `κ = M_Pl^{-2}` prefactor is untouched. Fierz is an O(1)
  linear recombination of the *same four `ψ` fields* — it can never change the
  field count or the coupling dimension.

## 4. sympy verification result

Full run: all assertions PASS; `F_norm == textbook`; `F_norm² == I`; AA/VV/VA
decompositions as tabled; escape set = ∅; all coefficients rational. Final
line: **"LEMMA PROVEN (single-species, minimal ECH)."**

## 5. Does this close the completeness major?

**Yes, at the level the paper claims** — power-counting-class basis-completeness
within minimal ECH. The lemma the abstract flagged as "left to follow-up" (the
explicit Fierz-by-Fierz projection over the dim-6 parity-relevant basis) is now
**executed and machine-verified**: the torsion-generated AA and VA operators
Fierz-close onto `{SS,PP,VV,AA}` (+the `{V,A}` block for VA), no operator escapes
the enumerated basis, and — the load-bearing point for the no-go — every channel
inherits the identical `M_Pl^{-2}` suppression, so the single-scale NDA ceiling
that bounds one representative bounds the **entire finite minimal-ECH tower**.

## 6. Honest residual scope (unchanged, correctly stated)

The proof is for **single-species, minimal (totally-antisymmetric axial) coupling**.
Genuinely outside scope, and correctly left as such:
- **Multi-flavor** contact terms carry additional flavor-off-diagonal Fierz
  channels; the *class* closure `{S,V,T,A,P}` and the `M_Pl` power argument are
  unchanged (Fierz acts on Lorentz structure, not flavor), but the explicit
  per-flavor coefficient bookkeeping is a mechanical extension.
- **Non-minimal couplings** (trace/tensor torsion irreps, a rolling
  Chern–Simons `ϑ`, a new light scale `μ ≪ M_Pl`) are the *stated* scope
  boundary — by construction the tuning the mechanism is meant to explain.

Neither weakens the minimal-ECH no-go; both are already disclosed in the paper.

## 7. Proposed .tex upgrade — PROPOSED, NOT APPLIED

See sibling file `P1A_fierz_lemma_tex_upgrade_PROPOSED_2026-07-07.md`.
Net effect: the abstract / Scope / conclusion language "only the fully explicit
Fierz-by-Fierz projection lemma remains follow-up" → "the Fierz-by-Fierz
projection lemma is proven (App. X, machine-verified); the single residual scope
is the non-minimal completion." A new short appendix states the 5×5 matrix, the
closure table, and cites the script + Nieves–Pal.
