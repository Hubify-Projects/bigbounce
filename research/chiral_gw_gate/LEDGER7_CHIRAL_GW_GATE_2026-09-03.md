# Ledger #7 four-question gate — chiral GWs from the torsion bounce

**Date:** 2026-09-03 · **Status:** COMPLETE — **verdict: CLOSE WITH REASON**
**Artifacts:** `chiral_gw_delta_h.py` · `outputs/ledger7_chiral_gw_delta_h.json`
· manifest `reproducibility/manifests/experiments/ledger7-chiral-gw-delta-h.json`

**Question (ledger row 7):** does the lab's minimal Einstein–Cartan–Holst (ECH)
bounce with a Dirac/Weyssenhoff spin fluid predict a net circular polarisation
Δ_h ≡ (P_R − P_L)/(P_R + P_L) of the SGWB? **Gate rule:** O(1) from ingredients
the model already has → open a branch; O(ε) or needs an ad-hoc ingredient →
close with an honest reason.

---

## What prior work already established (NOT redone here)

- **Branch M** (`research/branch_M_pgt_bounce_gw/`, 2026-03-16, `PGT_GW_GENERIC`):
  the *parity-even* tensor spectrum from a torsion/PGT bounce. Amplitude
  Ω_GW h² ≈ 5×10⁻⁶ (m_T/M_Pl)² S(f/f_b), bounce frequency
  f_b ≈ 2.6×10¹⁰ (m_T/M_Pl)^{1/2} Hz, and the universal amplitude–frequency
  trade-off Ω_peak ∼ (f_b/f_Pl)⁴ leaving a **10¹⁷ gap to the best detector**.
  Taken as given: the *carrier* of any chirality is already undetectable.
- **Branch Q** (`research/branch_Q_sourced_parity/`, 2026-03-16,
  `BRANCH_Q_WEAK`): seven parity-violating ECH extensions screened; five killed.
  Survivors are (A) gravitational Chern–Simons — "produces chiral GWs but
  requires r > 10⁻³ and is standard dCS gravity, not ECH-specific" — and
  (C) a dynamical Barbero–Immirzi field, which after torsion elimination is
  "identical to any ALP with f_a ∼ M_Pl" (ABJ coefficient is universal by
  Adler–Bardeen), delivering cosmic birefringence β ≈ 0.13°, not chirality.
  Candidate F (Nieh–Yan) "reduces to C".
- **On-shell ECH torsion** (`research/theory_audit/ech_torsion_onshell_2026_08_08.md`,
  supersedes the pure-axial reading of `operator_basis_adjudication_2026_08_07`):
  the connection equation *solved* over all 24 contorsion components gives
  axial(4) + trace-vector(4) nonzero, tensor(16) ≡ 0, with
  β/α = s_H/(2γ); O4 ≡ ε^{μνρσ}T^I_{μν}T_{Iρσ} = −24αβ (J⁵·J⁵) ≠ 0, equal to
  −3κ²γ³/(1+γ²)² (J⁵·J⁵) in READING-I (reproduced symbolically by this gate's
  script as an independent check, s_H = +1).
- **ECH Note** (`arxiv/paper1bc_ech_note/main.tex`, v1N.0.5): eliminating the
  non-propagating connection generates **exactly one** interaction,
  L_{4ψ} = −(3κ/16)·γ²/(1+γ²)·(J⁵·J⁵), the Hehl–Datta spin–spin contact term;
  γ²/(1+γ²) = 0.0534 at γ = 0.2375 (0.0698 at γ = 0.274). The Note states this
  term is "parity-even … and (on the zero-spin branch) classically transparent
  to every scalar and tensor perturbation."

---

## Q1 — Does minimal ECH contain a parity-odd tensor coupling at O(h²)?

**Answer: NO. Chirality requires an extra ingredient.**

*(i) The generated operator is parity-even.* Torsion in minimal ECH is
non-propagating and algebraic; eliminating it gives Eq. (4fermi),

    L_4ψ = −(3κ/16) [γ²/(1+γ²)] (J⁵·J⁵).

J⁵^μ is an axial vector, so J⁵·J⁵ = J⁵^μ J⁵_μ is a **true scalar** (P-even).
Freidel–Minic–Takeuchi (PRD 72, 104002, hep-th/0507253) and Perez–Rovelli
(PRD 73, 044013) derive precisely this term and precisely this γ²/(1+γ²);
the Holst term with **constant** γ contributes no parity-odd dynamics because
it is, in the Nieh–Yan formulation, a topological density — Mercuri
(PRD 73, 084016, gr-qc/0601013) shows the γ-dependence is removable by a field
redefinition, i.e. the Immirzi parameter is **not observable** unless promoted
to a field (Taveras–Yunes PRD 78, 064070; Calcagni–Mercuri PRD 79, 084004).

*(ii) The one on-shell object that carries an ε tensor is still P-even as a
functional of matter.* The 2026-08-08 result gives a nonzero Nieh–Yan bilinear
O4 = −24αβ (J⁵·J⁵). The Levi-Civita symbol is **fully saturated by the torsion
indices**; what survives is proportional to (J⁵·J⁵) — the same operator as O5,
ratio γ/(1+γ²) = 0.225. Nothing parity-odd is left to couple to h_ij.

*(iii) Structure of the quadratic tensor action.* On FRW the only two-derivative
parity-odd scalar density at O(h²) is the gravitational Chern–Simons structure
ε^{ijk} h_{il} ∂_j h_{kl} (and its derivative descendants). Its coefficient must
be a **background pseudoscalar**. Minimal ECH + a Weyssenhoff fluid supplies
exactly two background scalars: ρ (P-even) and (J⁵·J⁵) (P-even). The only P-odd
candidate is the axial charge density ⟨J⁵^0⟩ (the time component of an axial
vector is P-odd, i.e. a **net fermion helicity**) — but ⟨J⁵^0⟩ enters the ECH
action only inside the *quadratic* contraction (J⁵·J⁵), never linearly, so it
cannot supply a linear parity-odd coefficient. **Coefficient ≡ 0.**

*(iv) What would be needed.* A parity-odd tensor operator requires one of:
a **dynamical** Immirzi pseudoscalar (→ dCS: Taveras–Yunes; Alexander–Yunes
Phys. Rept. 480 (2009) 1); a **Nieh–Yan** coupling to a pseudoscalar
(Bombacigno–Boudet–Olmo–Montani, and Cai–Li–Wang–Zhu on chiral GWs in Nieh–Yan
modified teleparallel gravity, arXiv:2104.08376); or explicit axial-current
alignment / a pseudoscalar condensate. Every one of these is **outside minimal
ECH** and each is exactly Branch Q's screened candidate A / C / F — already
adjudicated `BRANCH_Q_WEAK` and "not ECH-specific". Popławski's spin-fluid
bounce papers (1007.0587, 1111.4595, 1410.3881) contain **no** parity-odd
tensor coupling; they use the same P-even Hehl–Datta term (consistent with
ledger #5, which found only a qualitative preferred-axis tendency, no amplitude).

> **Q1 verdict: minimal ECH has NO parity-odd tensor operator. Chirality is an
> add-on, not a prediction.**

---

## Q2 — Coefficient at the bounce in lab parameters

**Answer: identically zero in minimal ECH.** In the lab's own parameters,

    c_PV(minimal ECH; κ, γ, s², ρ_c) = 0     for all γ, all s², all ρ_c,

because the entire torsion sector collapses into the single P-even coefficient
(3κ/16)·γ²/(1+γ²) = 0.0534·(3κ/16) at γ = 0.2375. It does **not** become nonzero
at large spin density; increasing s² only increases the P-even repulsive
contact density ρ_{4ψ} = −L_{4ψ} that *causes* the bounce.

**Does a nonzero coefficient require ⟨s^μ⟩ ≠ 0?** Yes — any add-on route needs a
P-odd background, i.e. a net axial spin polarisation (net fermion helicity), or
an evolving pseudoscalar σ̇ ≠ 0 that plays the same role. Two honest notes:
(a) this is *not* the quantity P4′ bounds — P4′'s A_95^obs ≲ 0.98% constrains a
present-day **galaxy angular-momentum** dipole (ledger #5), not an early-universe
fermion helicity asymmetry; conflating them would be wrong. (b) The lab has no
committed ⟨J⁵^0⟩/n or ρ_c number for the ECH bounce, so the script scans a
two-point bounce-scale range (10¹⁶ GeV → M_Pl) rather than inventing one; the
Holst sign s_H is likewise unfixed by the lab's artifacts and only flips O4's
sign. Both are recorded in the JSON `convention_flags`.

---

## Q3 — Analytic Δ_h at the bounce scale, kη_B ≪ 1

Write the helicity modes u_± = a h_± with a generic parity-odd coupling
Λ(η) (dCS or Nieh–Yan both reduce to this form at leading order):

    u_λ'' + [ k² − λ k Λ(η)/a − a''/a ] u_λ = 0 ,      λ = ±1 .

**The key structural point is the single power of k.** Parity-odd means an
ε^{ijk}; on FRW, momentum conservation forces ε^{ijk} k_k, i.e. the helicity
label λ **always** enters multiplied by exactly one power of k. Hence at first
order in the coupling, and in the super-Hubble regime where a''/a ∼ η_B^{-2}
dominates over k²,

    Δ_h ≃ 2 · (λ-odd part of δω²) / (dominant term)
        ≃ C · ξ_B · (k η_B) ,    ξ_B ≡ Λ(η_B) η_B / a_B  (dimensionless),

with C = O(1) and, by perturbative unitarity (|δω²| < ω²), ξ_B ≤ 1.
**Δ_h vanishes linearly as kη_B → 0.** This is a theorem-level suppression, not
a model detail: it holds for amplitude birefringence (dCS) and for velocity /
friction birefringence (Nieh–Yan) alike.

Contrast with inflation, where chirality is *not* suppressed: there the mode is
evaluated at horizon crossing, k/a = H, so kη ∼ 1 and Δ_h ∼ σ̇/f. A bounce is
the opposite regime — the observable modes are ~10–30 decades **outside** the
bounce-scale horizon, and each decade costs a decade of Δ_h.

**Evaluation** (`chiral_gw_delta_h.py`; f_B = horizon-scale mode at the bounce
redshifted to today, f_0 ≈ 1.65×10⁻⁷ Hz (T_*/GeV)(g_*/100)^{1/6}):

| bounce scale | f_B today | PTA 10⁻⁸ Hz | LISA 10⁻³ Hz | ET 10² Hz | CMB 3×10⁻¹⁷ Hz |
|---|---|---|---|---|---|
| T_B = 10¹⁶ GeV | 1.67×10⁹ Hz | Δ_h ≤ 6.0×10⁻¹⁸ | 6.0×10⁻¹³ | 6.0×10⁻⁸ | 1.8×10⁻²⁶ |
| T_B = M_Pl      | 2.04×10¹² Hz | 4.9×10⁻²¹ | 4.9×10⁻¹⁶ | 4.9×10⁻¹¹ | 1.5×10⁻²⁹ |

These are **ceilings** (ξ_B = 1, C = 1); in minimal ECH the coefficient is 0, so
the true prediction is Δ_h = 0. Against the ledger's criterion this is
unambiguously **O(ε), not O(1)**.

---

## Q4 — Observability

Every band's chirality channel requires Δ_h = **O(1)**, and each has an
additional structural obstruction:

- **LISA (mHz).** A single planar constellation is **blind to an isotropic
  V-mode**; circular polarisation is accessible only via the kinematic dipole
  (Seto & Taruya, PRL 99, 121101 (2007) and PRD 77, 103001 (2008);
  Domcke, Garcia-Cely, Kahn *et al.* / Domcke *et al.* JCAP 2020,
  arXiv:1910.08052), which costs a further factor v/c ∼ 10⁻³ and needs a strong
  SGWB detection first.
- **PTA (nHz).** Same: the monopole V-mode is unobservable; only the anisotropic
  component of circular polarisation gives a signal (Kato & Soda PRD 93, 062003
  (2016); Belgacem & Kamionkowski PRD 102, 023004 (2020)). NANOGrav has no
  circular-polarisation detection.
- **CMB TB/EB.** Needs O(1) chirality *and* r ≳ 10⁻² (Gluscevic & Kamionkowski
  PRD 81, 123529 (2010); Gerbino *et al.* PRD 93, 103519 (2016); LiteBIRD
  forecasts). The lab has no r ≳ 10⁻² prediction.

**Band mapping is the second, independent kill.** Branch M's own result puts the
torsion-bounce spectral peak at f_b ∼ 10¹⁰ Hz with Ω_peak h² ∼ 3×10⁻³⁰ at best,
a **10¹⁷ amplitude gap** to ET. So even a hypothetical Δ_h = 1 would sit on a
carrier no instrument can detect, in a band no instrument covers. The two kills
are multiplicative: ≥12 orders short on Δ_h *and* ≥17 orders short on Ω_GW.

---

## Verdict

**CLOSE WITH REASON.** Ledger rule: "O(ε) or requires an ad-hoc ingredient →
close." Both triggers fire. (1) Minimal ECH with a Dirac/Weyssenhoff spin fluid
contains **no** parity-odd tensor operator — its single generated interaction is
the P-even Hehl–Datta term, and the on-shell Nieh–Yan bilinear is saturated into
(J⁵·J⁵). Chirality needs a dynamical Immirzi/Nieh–Yan pseudoscalar, which Branch
Q already screened as "not ECH-specific". (2) Even granting that ingredient at
its unitarity ceiling, Δ_h = O(ξ_B · kη_B) ≤ 10⁻¹² (LISA), 10⁻¹⁷ (PTA), 10⁻²⁶
(CMB) — because parity-odd tensor operators are odd in k and the observable
modes are deeply super-Hubble at the bounce. This *reverses* March-2026's
"single best next theory" call, which assumed the bounce is where chirality is
generated without checking the super-Hubble k-odd suppression.

**Salvage kept (directive Q4 — nothing viable gets lost).** Two transferable
results, recorded here rather than discarded:
1. **The k-odd super-Hubble no-go**: *any* parity-odd quadratic tensor operator
   active only in a bounce-localised window gives Δ_h ∝ (kη_B)^{n≥1}, so
   bounce-generated SGWB chirality is generically unobservable regardless of
   coupling strength. This is a two-paragraph addition to the P1C no-go survey's
   barrier catalog, not a branch.
2. The symbolic re-derivation of O4 = −3κ²γ³/(1+γ²)²(J⁵·J⁵) (s_H=+1) here is an
   **independent third confirmation** of the 2026-08-08 adjudication.

---

## Ledger-ready status (3 lines)

```
CLOSED — NEGATIVE (2026-09-03), research/chiral_gw_gate/LEDGER7_CHIRAL_GW_GATE_2026-09-03.md.
Minimal ECH + Weyssenhoff has NO parity-odd O(h^2) operator (the only generated interaction
is the P-even Hehl-Datta term -(3k/16)g^2/(1+g^2)(J5.J5); the on-shell Nieh-Yan bilinear O4
is saturated into (J5.J5)) - chirality needs a dynamical Immirzi/Nieh-Yan pseudoscalar,
already screened BRANCH_Q_WEAK / "not ECH-specific".
Even at the unitarity ceiling xi_B=1, Delta_h = C xi_B (k eta_B) <= 6e-13 (LISA), 6e-18 (PTA),
2e-26 (CMB) vs the O(1) needed in every band (Seto-Taruya 2007/2008; Domcke+2020; Kato-Soda
2016; Gluscevic-Kamionkowski 2010) - O(epsilon), and Branch M's 1e17 amplitude gap kills the
carrier independently. March-2026's "single best next theory" call is REVERSED. Salvage: the
k-odd super-Hubble no-go is a barrier-catalog entry for P1C, not a branch.
```
