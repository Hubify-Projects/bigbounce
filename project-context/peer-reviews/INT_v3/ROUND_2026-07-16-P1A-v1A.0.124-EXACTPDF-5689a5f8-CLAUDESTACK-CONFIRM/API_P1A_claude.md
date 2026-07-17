# INT v3 Referee Report — P1A

- **Model:** claude-opus-4-8 (Claude Code subagent; independent referee leg)
- **Date:** 2026-07-16 (PT)
- **Paper:** P1A v1A.0.124 — "Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches"
- **PDF SHA-256:** 5689a5f8b4c6488b9fa1c4d2225d3c0211b830b028b0284299c00f912d0977aa
- **Venue / profile:** Classical and Quantum Gravity — CQG-NOTE
- **Exactness gate:** PASS (on-disk shasum == mandated hash)
- **PARSED VERDICT: MAJOR REVISIONS**

---

## Referee prompt executed

"You are an expert referee for Classical and Quantum Gravity. Review this Note
manuscript under profile CQG-NOTE to the standard of a real submission. Respond
with exactly: (1) VERDICT; (2) ISSUES (numbered, [MAJOR]/[MINOR]); (3) one
sentence on whether the central claim is supported."

Reviewed as a fresh referee with no knowledge of prior rounds. Full 7-page PDF
read; key derivations and numbers independently re-checked.

---

## (1) VERDICT

**MAJOR REVISIONS**

The manuscript is careful, internally consistent, and unusually honest about its
own limits. The arithmetic I could check reproduces exactly (Q_γ inverse Eq (2)
multiplies to unity on the ⋆²=−1 bivector algebra; the κn_ψ² ≃ 1.0×10⁻⁷⁹ eV⁴ and
κn_ψ²/ρ_Λ ≃ 3.6×10⁻⁶⁹ benchmark of Eq (10) reproduce from ħc, M_Pl, ρ_Λ=(2.3 meV)⁴;
Table I R_S = 3/(4π)·N_fN_c = 0.239/0.716/2.15 and R_A = R_S/2 = 0.119/0.358/1.07
reproduce exactly; the γ→∞ coefficient −3κ/16 = −(3/2)πG is consistent). The
physics is standard and correctly attributed. But the paper's *scientific yield*
is marginal for a real submission, and two of its stated sub-results are fragile
in ways that need substantive work before acceptance — hence MAJOR, not MINOR.

---

## (2) ISSUES

**[MAJOR] 1 — Novelty / significance threshold for a CQG Note.**
Every physical ingredient is explicitly standard and cited: the Hehl–Datta axial
contact term [1,2], the Freidel–Minic–Takeuchi γ²/(1+γ²) factor [3], and the
Bianchi-vanishing of the Holst contraction on a torsion-free connection. The
authors state the contribution is a "convention-audited consolidation," a
dimensional benchmark that lies ~68 orders of magnitude below ρ_Λ, and an
explicit claim boundary — with, by their own statement, *no* observable
prediction (no dark energy, no birefringence). A Note must still deliver a new,
usable result. As written it is not clear what the community gains beyond careful
bookkeeping of known conventions; the significance case for publication needs to
be made explicitly (what open confusion in the literature does the audit resolve,
and for whom), or the scope broadened.

**[MAJOR] 2 — The NJL "no-condensate" result is convention-fragile and
self-undercutting.**
Sec. III.B / App. B conclude the real homogeneous scalar gap equation "has no
nonzero solution" from G_scalar = −3κ/16 < 0. Yet the paper simultaneously
(a) admits the mean-field Fierz ambiguity is "not removed" and that the axial
sign is "convention-bound" (reported only through |G_A|), and (b) shows in
Table I that the coefficient is magnitude-*supercritical* (R_S = 2.15 > 1 at
N_fN_c = 9). With the old magnitude-subcriticality claim correctly retracted, the
entire conclusion now rests on a single convention-dependent sign. The Note must
demonstrate that no legitimate Fierz/exchange-basis choice flips G_scalar > 0
(which would admit a condensate in the same mean-field model), or the "no
nonzero solution" statement should be withdrawn rather than stated even
conditionally. As it stands a reader cannot tell whether the sign is a physical
result or an artifact of the declared direct-channel ordering.

**[MAJOR] 3 — Scalar-transparency proof: the boundary/surface-term step is
asserted, not shown.**
Sec. IV.A–B claim the first-order variational surface contribution "vanishes"
under standard falloff, yielding scalar equations and tensor evolution operators
equal to GR "at every perturbative order." First-order (Palatini/Holst) actions
carry boundary structure distinct from the second-order Einstein–Hilbert case;
the vanishing of that surface term and the order-by-order equality of the tensor
evolution operators E_R = E_L (Eq (12)) are load-bearing for the "GR-equivalent
observables" claim and are presently only asserted. An explicit demonstration, or
a specific citation that establishes the boundary result for this action, is
required. (The pointwise Bianchi-vanishing of the Holst dual, Eqs (13), is
correctly argued and distinguished from the Pontryagin/Nieh–Yan densities — that
part is fine.)

**[MINOR] 4 — "Two branches of the same algebraic Cartan equation" framing.**
The fermion (spin-sourced) and scalar (zero-spin) cases are two different matter
contents, not two branches of one equation. The unifying "branches" language in
the title/abstract slightly overstates the structural link; consider softening.

**[MINOR] 5 — Reduction Eqs (3)→(5)/(7) is compressed.**
The step from the sourced connection equation to the contact coefficient is
delegated to FMT [3]. A short explicit intermediate (parallel to App. A for the
Fierz projection) would make the Note self-contained, which is the whole point of
a "convention-audited" consolidation.

**[MINOR] 6 — Table I interpretation risk.**
The retraction of subcriticality is welcome, but the surrounding text still leans
on "coefficient-scale comparison." State plainly that the table does NOT
establish a magnitude bound underlying the conclusion (only the sign is used), so
a reader does not infer a subcriticality result the authors explicitly disavow.

**[MINOR] 7 — Purpose of the dimensional benchmark.**
A number 68 orders below ρ_Λ, disclaimed as "neither a cosmological-density
estimate nor a preferred state," invites the question of what it is for. One
sentence on its intended diagnostic use (e.g., excluding a class of naive
torsion→dark-energy scalings) would justify its prominence.

---

## (3) Central-claim support

The narrow consolidation-plus-benchmark claim is arithmetically correct and
honestly bounded, but the NJL "no-condensate" sub-claim is convention-fragile
(rests on a sign the paper itself calls convention-bound, with the magnitude now
admitted supercritical) and the scalar-transparency proof's boundary-term step is
asserted rather than demonstrated — so the paper's stated results are only
partially supported as written.
