# INT full-source verification — P1U (paper1_unified.tex) v1U.0.4

**Reviewer:** Claude Code INT (Houston subscription, full-source truth-audit, scripts RUN)
**Date:** 2026-07-09
**Scope:** the NEW load-bearing content only (dim-4 completion appendix, term-by-term
transparency derivation, ΔNeff proxy-validity bullet, retitled abstract/title).
**Stance:** skeptical referee; NEVER rubber-stamp. Every claim checked against source +
committed script output.

---

## Item 1 — Dim-4 completion appendix (`app:dim4_completion`, Table VII / `tab:dim4_parityodd`, O1–O6)

**File:** `arxiv/paper1_unified.tex` L4515–4607 (appendix); Table L4533–4554.
**Script:** `arxiv/scripts/dim4_parityodd_enumeration.py` — **RAN, exit 0.**

Script output (verbatim):
- **[CHECK A]** `eps^{μνρσ} R_{μνρσ}` under algebraic Bianchi → contracted result `0`,
  **VANISHES identically: True**. (Independent method: builds a generic symbolic
  Riemann tensor with pair antisymmetries + pair-swap, imposes the first Bianchi
  identity `R_{μ[νρσ]}=0` as linear constraints via `sp.solve`, then contracts with the
  4D Levi-Civita symbol. Result is identically zero as a polynomial in the free
  components — this is a genuine algebraic proof, not an assertion.) **VERIFIED.**
- **[CHECK D]** `eps_{abcd} eps^{abce} = 3! δ^e_d` → computed diag `[6,6,6,6]`,
  off-diagonal all zero, **equals 6·I: True** ⇒ `S_abc S^abc = 6 (J5·J5)`. **VERIFIED.**

**Enumeration completeness logic (independent audit):** The appendix enumerates every
local, Lorentz- + diffeo-invariant, parity-odd density of mass-dimension exactly +4 that
the *minimal* ECH field content admits (tetrad, Holst, algebraic torsion via Cartan
`T=κS`, minimally-coupled canonical matter), with building-block dimensions stated
([e]=0, [ω]=+1, [R]=+2, [κS]=+1). The six-operator basis O1–O6 is the correct minimal
set at dim-4:
- **O1 (Holst dual `ε e e R`), O6 (`ε^{μνρσ}R_{μνρσ}`)** — single-curvature parity-odd
  ⇒ vanish by Check A on the torsion-free branch. **Disposition correct** (both are the
  same Bianchi vanishing; torsionful piece of R is O(κS) and correctly routed to O4/O5).
- **O2 (Nieh–Yan `d(e_I∧T^I)`), O3 (Pontryagin `R∧R`)** — exact total derivatives
  ⇒ 0 EOM, 0 vacuum energy. NY identity `d(e_I∧T^I)=T_I∧T^I − e_I∧e_J∧R^{IJ}` cited to
  NiehYan1982 (bib entry present); Pontryagin exact by Chern–Weil. **Disposition correct.**
- **O4 (`ε_{IJKL}T^{IJ}T^{KL}`), O5 (`ε T e J5`)** — collapse under Cartan `T=κS` +
  Check D to `κ²(J5·J5)` and `κ(J5·J5)` resp., members of the Fierz-closed basis
  (`app:fierz`), bounded at M_Pl^{-2} with natural coefficient ~M_Pl^4 by single-scale
  NDA. **Disposition correct** — Check D supplies the `S_abcS^abc=6(J5·J5)` collapse,
  the Fierz lemma (L4610–4675) supplies basis-closure with F²=1 involution.

**Completeness is honestly scoped:** the appendix + Fierz-lemma scope paragraph (L4662–
4675) explicitly excludes derivative four-fermion terms, higher curvature-torsion
contractions, multi-species chiral structures, dynamical Immirzi, and non-minimal
(trace/tensor) torsion irreps. This is the correct minimal-ECH scope boundary and is NOT
overclaimed as a full-EFT no-go. **No fabrication:** the script verifies only the two
tensor identities; the physics conclusion (topological / Fierz-reducible / Bianchi-
vanishing ⇒ no meV^4 without a new light scale) follows from those + the structural
facts, and is stated as a scoped result, not a universal theorem.

**VERDICT: VERIFIED. No MAJOR, no MINOR.**

---

## Item 2 — Term-by-term transparency derivation (`sec:transp_expansion`, L3696–3782)

Each step audited against source:
1. **Perturbed tetrad** `e^I_μ = ē^I_μ + δe^I_μ`, δe first-order in h — standard. ✓
2. **Composite connection** `ω^{IJ}_μ = ω̊^{IJ}_μ[e]` at every order (Eq. `pert_conn`
   L3714–3719). The load-bearing move: because `T=0` is enforced *algebraically* by
   `S=0` (canonical scalar matter, no spin current) — NOT dynamically/linearized — the
   full connection equals the torsion-free composite `ω̊[e]` at every order, a functional
   of the tetrad alone, with NO independent δT to track. **This is correct and is the
   key insight**; it is what makes the all-orders claim exact rather than truncated.
3. **Holst contribution order-by-order** (L3725–3756): at each order the curvature is
   the Riemann tensor of a torsion-free connection ⇒ obeys the algebraic Bianchi
   `R_{μ[νρσ]}=0` as a tensor identity in the perturbed configuration ⇒
   `ε^{μνρσ}R_{μνρσ}|_{n-th} = 0 ∀n` (Eq. `allorder_vanish`). This is exactly Check A of
   Item 1, correctly cross-referenced to the script. **Logic sound.**
4. **Scalar sector** (L3758–3766): δe diagonal in {Φ,Ψ}, δω̊ carries only gradients;
   every R_H^{(1,2)} term is a perturbed-Riemann component killed by the ε-contraction ⇒
   ζ 2-/3-pt = standard GR, γ_BI absent. ✓
5. **Tensor sector** (L3768–3777): TT perturbation δe^i_j=½h^i_j, δω̊~∂h enters only via
   perturbed Riemann ⇒ annihilated order-by-order; both circular polarizations obey the
   SAME EOM `h'' + 2H h' + k²h = 0`, no ±k parity-splitting term ⇒ v_R=v_L, no tensor
   birefringence. ✓

Each step follows from the previous; the derivation is genuine (perturbed tetrad →
composite connection → Holst dual vanishing per order via Bianchi), not outline-level.

**VERDICT: VERIFIED. No MAJOR, no MINOR.**

---

## Item 3 — ΔNeff proxy-validity bullet (L4121–4136) + App-E derivation (L4905–4932)

Claim: `ΔNeff^(ECH) ~ (T/M_Pl)² ~ 10⁻⁴³` at BBN; stock-CAMB envelope exceeds it by
`>40 orders of magnitude`.

**Arithmetic re-derived independently** (reduced M_Pl = 2.44×10¹⁸ GeV):
- BBN, T=1 MeV: `(T/M_Pl)² = 1.68×10⁻⁴³` — matches boxed `1.7×10⁻⁴³` (Eq. `neff_bound`). ✓
- Recomb, T=0.26 eV: `1.14×10⁻⁵⁶` — matches boxed `1.1×10⁻⁵⁶`. ✓
- Envelope margin vs CMB-S4 σ(Neff)~0.03: `0.03/1.68e-43 = 1.8×10⁴¹` ⇒ **41.25 orders**. ✓
- vs Planck bound ~0.17: `1.0×10⁴²` ⇒ **42 orders**. ✓

The physics chain is sound: torsion 4-fermion coupling ∝ κ²=M_Pl^{-2} ⇒ ρ_tor~G_N T⁶,
ρ_tor/ρ_rad ~ G_N T² = (T/M_Pl)² (Eq. `torsion_ratio`), redshifts a⁻⁶ (stiff), so ΔNeff
in the radiation era is (T/M_Pl)². The ">40 orders" envelope claim is **arithmetically
correct and conservative** (true margin 41–42 orders). The bullet correctly frames the
stock-CAMB run as a conservative observational envelope whose validity is *derived* from
the first-principles Planck suppression, not assumed.

**VERDICT: VERIFIED. No MAJOR, no MINOR.**

---

## Item 4 — Retitled abstract/title consistency

**Title** (L1131–1134): "Channel-Level Constraints on Four Enumerated Minimal
Einstein–Cartan–Holst Dark-Energy Routes Under Stated Assumptions (Amplitude Closure for
R1–R3, Naturalness Closure for R4), **and Perturbation Transparency for Scalar Matter**".

**Abstract** (L1180–1190) explicitly carries: the genuine dim-4 parity-odd completion
enumerated in `app:dim4_completion` with symbolic verification (topological /
Fierz-reducible / Bianchi-vanishing ⇒ single-scale closure survives at dim-4 without the
heuristic on-shell dressing); and the perturbation-transparency result for scalar matter
(`sec:transparency`). Title clause "Perturbation Transparency for Scalar Matter" matches
the abstract's scalar-only transparency scope and the Sec-`transparency` restriction
(L1321: "restricted to canonical scalar matter"). **Consistent.**

**VERDICT: VERIFIED. No MAJOR, no MINOR.**

---

## P1U OVERALL VERDICT: **VERIFIED / ACCEPT-track.**
Both committed symbolic identities pass (Check A εR=0, Check D εε=6δ). Enumeration
completeness logic + all six O1–O6 dispositions are correct and honestly scoped. The
term-by-term transparency derivation is a genuine step-by-step proof, not an outline. The
ΔNeff arithmetic is correct (41–42 orders; ">40" conservative). Title/abstract consistent.
**No fabrication detected. No MAJOR, no MINOR.**
