# P1A INT (Claude Code full-source leg) — v1A.0.107 — ROUND 2026-07-05

**Reviewer:** Claude Code INT leg (Houston subscription, NOT Anthropic API).
**Paper:** `arxiv/paper1a_ech_nogo.tex` v1A.0.107 (July 5 2026).
**Scope:** full-source PRD-referee review; verify the 3 upgrades this session
(R3 Immirzi running derived; ρ_Λ crux reframed as single-scale NDA no-go;
operator-basis completeness) against `.tex` + `references.bib` + numeric recompute.

## VERDICT: MINOR

The central claim — **ECH torsion cannot source dark energy** — is **SUPPORTED**.
The single-scale NDA dimensional no-go is dimensionally correct, non-circular as
argued, and the R3 running upgrade is a genuine (numerically reproduced) result,
not an ansatz. One real internal inconsistency (abstract vs body on operator
closure) and a completeness-overclaim tension must be reconciled; both are
presentational, not amplitude-level defects.

---

## Verification of the three session upgrades

### (1) R3 Immirzi running — ansatz → DERIVED ✔ CORRECT
- Benedetti–Speziale β-function transcribed at L2519-2524 (their Eq. 7):
  `μ ∂γ²/∂μ = -(γ²-1)(μ²κ²/(8π)²)(23γ²+5)`, κ²=16πG.
- I re-integrated it numerically (scipy `solve_ivp`, rtol 1e-10) from
  μ_UV=1e16 GeV → μ_IR=1 GeV with γ≈0.24, κ²=16π/M_Pl² (M_Pl=1.22e19 GeV):
  **|Δγ/γ| = 1.383e-6**, matching the paper's `1.4×10⁻⁶` (L2538) to 2 sig figs. ✔
- The stated physics — power-suppressed flow ∝ (μ_UV/M_Pl)², UV-endpoint
  dominated, perturbatively controlled sub-Planck, γ²=1 fixed point outside
  perturbative control (L2529-2547) — is correct and matches the integrand
  behavior I observed. ✔
- Propagated suppression: (Δγ/γ)(H0/M_Pl). I get log10(H0/M_Pl)=-60.9;
  ×0.3 → 3.5e-62 (paper's "3×10⁻⁶²", L2590 ✔); ×1.4e-6 → 1.65e-67 (log -66.8),
  which is the "67 orders below" upper end of the claimed **"41–67 orders below
  observed ρ_Λ"** (L2554). The 41–67 band brackets my computed values under the
  stated ansatz choices. ✔ Numerically consistent; margin ≳60 orders as claimed.
- Honest hedging intact: the larger chiral-count Δγ/γ~0.3 (L2559, 2573) is kept
  as a *deliberately pessimistic upper bound*, correctly labeled "not a precisely
  derived value" (L2575). Closure is insensitive to the coefficient (≳60 order
  margin). No overclaim.

### (2) ρ_Λ crux reframed as single-scale NDA no-go ✔ DIMENSIONALLY CORRECT
- App. Dimensions (L3990-4113): [α/M]=-1, [ε e e F]=+2 ⟹ [L_odd]=+1. **Correct**
  in the stated conventions: vierbein e^I_μ dimensionless, curvature 2-form
  F_{IJρσ} dimension +2 (L1618 Eq. Seff_comp). Three-unit deficit to +4. ✔
- NDA: relevant operator d=1 ⟹ Wilson coefficient Λ^{4-d}=Λ³. Minimal ECH's
  only scale is Λ~M_Pl ⟹ coefficient forced to M_Pl³ ⟹ ρ~M_Pl³⟨T⟩ or
  ρ~M_Pl⁴, never (meV)⁴. **Dimensional bookkeeping is internally consistent.**
- Two admissible completions (Case I coefficient-dressing, Case II on-shell
  curvature) both land at M_Pl⁴ up to O(1)–O(10⁻²) — correct; neither reaches
  (meV)⁴. ✔
- **Non-circularity argument is sound** (L4041-4046): no positive ρ_Λ is
  derived, so there is no "assume the conclusion → derive the conclusion" loop;
  the +1→+4 gap *is* the mechanism. This is a legitimate naturalness/
  amplitude-ceiling no-go, not a fitted amplitude. ✔
- Caveats explicit + not overclaimed (L4048-4061): single-scale EFT assumption,
  no intermediate μ≪M_Pl, no exact cancellation named as the residual
  assumption; a non-minimal light scale/symmetry "is itself the tuning" —
  honest and correct. The deferred "matching calculation" (L4057-4061) is
  retained. ✔

### (3) Operator-basis completeness (F1 + F2 → dim≤6 finite basis) — SOUND but OVERCLAIMED in one paragraph
- F1 (L2108): Cartan constraint T=κS algebraic/non-propagating ⟹ only
  spin-current contact + metric/topological sector. Correct — matches Eq.
  torsion (L1537) and the totally-antisymmetric spin current derived in the
  footnote (L1548). ✔
- F2 (L2110-2114): minimal fermion coupling ⟹ S^{abc}∝ε^{abcd}J⁵_d totally
  antisymmetric ⟹ trace-vector + tensor torsion irreps only under non-minimal
  couplings (out of scope). **Verified against the Step-1 footnote** (L1548-1555):
  the spin current IS totally antisymmetric (all trace parts vanish), so F2 is a
  correct consequence of minimal coupling, not an assumption smuggled in. ✔
- The monotone/class-blind NDA argument (L2124-2133): the dim-+1 operator is the
  least-suppressed representative; every higher-dim operator carries strictly
  more M_Pl suppression ⟹ bounding the ceiling bounds the tower. **Logically
  valid GIVEN the finite basis** — no channel I can identify escapes: the
  four-fermion class (all Fierz VV/AA/VA/TT share κ=M_Pl⁻², Fierz recombination
  is O(1) — correct, Fierz identities are O(1) linear recombinations that cannot
  change a mass-power) and the parity-odd curvature/topological class (Holst,
  Nieh–Yan, Jackiw–Pi CS — each total-derivative for constant coupling, R4-class
  dynamical, closed explicitly at L2299 and L2261). No omitted channel found
  within minimal ECH.

---

## Numbered issues

**[MINOR-1] Abstract vs body inconsistency on operator closure (REAL — EXT would
likely miss without a source diff).** The abstract "Scope and limitations"
(L1143-1150) still states the Jackiw–Pi CS term and the parity-odd four-fermion
partner "are **excluded from the enumeration** and their explicit closure is
**left to a follow-up** operator-basis analysis." But the v107 body now closes
BOTH explicitly: parity-odd 4-fermion partner in Sec. R1-partner (L2261) and
Jackiw–Pi CS in Sec. 2299-2333. The abstract was not updated to track the
upgrade. Fix: update abstract L1143-1150 to "closed explicitly in §IV.C–IV.D;
a complete Fierz-basis projection lemma is left to follow-up."

**[MINOR-2] Completeness overclaim vs residual-scope disclaimer (internal
tension).** The new completeness paragraph (L2102-2133) asserts the enumeration
"is complete for the minimal ECH field content" and the four routes are
"exhaustive within minimal ECH" (basis-complete no-go). Yet the Residual-scope
paragraph 260 lines later (L2335-2344) still says "we therefore do NOT claim
operator-level closure over the whole minimal-ECH parity-odd effective theory,
only for these two named operators," and defers "a complete dim-6 parity-odd
basis + projection lemma" to follow-up. These two statements are in direct
tension. The completeness paragraph's claim is defensible IF read as "complete
up to O(1) Fierz recombinations that provably cannot change the M_Pl power,"
but as written it reads stronger than the residual-scope disclaimer permits.
Fix: harmonize — either (a) soften L2129 "exhaustive within minimal ECH" to
"exhaustive at the level of M_Pl-power-counting classes within minimal ECH
(the residual open item is the explicit Fierz projection lemma, §IV.D)," or
(b) state in the residual-scope paragraph that the projection lemma is now
argued at the power-counting level and only its fully-explicit Fierz-by-Fierz
form is deferred. Right now a referee can quote one paragraph against the other.

**[MINOR-3] "Class-blind monotone" rests on an unstated genericity assumption.**
The monotonicity argument (L2126-2128) — "every higher-dimension operator
carries strictly greater M_Pl suppression" — is true for the *natural* NDA
coefficient but silently assumes no higher-dim operator has an *anomalously
enhanced* coefficient (e.g. from a large multiplicity or a would-be-forbidden
term lifted by a small parameter). Within strict single-scale NDA this is fine
(that is the whole assumption), but the paper should state once that
monotonicity is an NDA-coefficient statement, inheriting the same single-scale
caveat already flagged in App. Dimensions (L4048). One clause suffices; it
closes the only formal gap I can find in the completeness logic.

**[MINOR-4] N_tot ansatz-dependence disclosure is good but the two values
(92 vs 94) invite a "which is headline?" question.** L2081-2106 and L4088-4106
honestly disclose the ~2% offset (N_tot=92±2) between the on-shell-ansatz
bookkeeping and the M_Pl⁴→ρ_obs hierarchy. This is correctly hedged and NOT a
defect — flagging only so a truth-audit confirms the paper does not headline
the more-favorable of the two (it does not; it states 92±2 as
order-of-magnitude). Consistent with directive F (no value-headlining). ✔ No
action required beyond confirming abstract/exec-summary quote 92±2, not a bare
92.

---

## No dimensional errors, no omitted operator, no circular reasoning found

- Dimensional bookkeeping [L_odd]=+1, Λ³ forcing, single-scale → M_Pl⁴:
  **correct**.
- RG integration Δγ/γ≈1.4e-6: **numerically reproduced** (1.383e-6).
- Completeness: **no channel missed** within minimal ECH; F1+F2 correctly fix
  the finite basis; the two named residual operators (JP-CS, PO 4-fermion
  partner) are genuinely closed in-body.
- Non-circularity: **sound** — no positive amplitude derived.
- Caveats (single-scale EFT, non-minimal escape, UV matching scale):
  **intact and not overclaimed**.

The three upgrades are correctly and honestly implemented. The only real items
are the abstract/body de-sync (MINOR-1) and the completeness-vs-residual-scope
wording tension (MINOR-2); both are one-edit reconciliations, neither touches
the amplitude-level no-go. Recommend **MINOR revisions**, then converged.
