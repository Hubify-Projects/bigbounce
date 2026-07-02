# P1A operator-basis completion: Jackiw–Pi Chern–Simons & parity-odd four-fermion Holst partner

**Date:** 2026-07-02
**Paper:** `arxiv/paper1a_ech_nogo.tex` (slug paper-1a), ECH spin-torsion dark-energy no-go
**Trigger:** Grok + Gemini external review flagged that the four-route operator
basis is non-exhaustive; specifically the Jackiw–Pi gravitational Chern–Simons
term \(R\wedge\widetilde R\) and the parity-odd four-fermion partner of R1 are
omitted. Task: decide whether either omitted operator opens a dark-energy (DE)
route the paper's four channels missed, or is also closed — i.e. whether P1A can
upgrade from a channel-level survey toward an operator-level theorem.

**Integrity note (pattern-036):** No math is fabricated below. Where a closure
rests on a standard identity I cite the identity and the paper line that already
uses it; where a genuine calculation is required I say so and scope it rather
than assert a closure.

---

## 0. What the paper already concedes (so we grade the right thing)

P1A is unusually self-aware about this exact gap. It is already conceded in:
- Abstract L965–971 ("channel-level assessment, *not* an operator-level
  theorem … we acknowledge missing operators (Jackiw–Pi gravitational
  Chern–Simons \(R\wedge\widetilde R\), parity-odd four-fermion partner)").
- Scope paragraph L1969–2001 (`sec:fourroute`): the four routes are
  "illustrative, explicitly *non-exhaustive*"; the two omitted operators are
  named; a full operator-level no-go "would require enumerating all
  dimension-6 parity-odd four-fermion + gravitational Chern–Simons operators …
  deferred to a follow-up theory paper."
- Closure summary L2480–2488 (`sec:fourroute_summary`): omitted operators
  "explicitly *not* closed at this level."
- The "structural definition" block L1121–1133: explicitly disclaims (a) an
  operator-level no-go and names the two operators.

So the honest baseline is: **the paper does not currently claim these are
closed.** The research question is whether they *can* be closed with a rigorous
argument (upgrading the theorem) or whether one/both genuinely open a route.

Crucially, the paper already contains the two physical mechanisms that do the
work below: (i) the Pontryagin/topological identity for \(R\wedge\widetilde R\)
(L3122–3126, invoked to *distinguish* it from the Holst dual), and (ii) the
torsion-elimination four-fermion structure with the
\(\gamma^2/(\gamma^2{+}1)\) coefficient (Eq. `eq:4fermi`, L1510–1511). The
completion is largely a matter of turning those already-present facts into an
explicit closure argument for the two named operators.

---

## 1. Jackiw–Pi gravitational Chern–Simons \(R\wedge\widetilde R\)

### 1.1 The operator and why it is a candidate DE route
Jackiw–Pi (2003) gravitational Chern–Simons adds
\(S_{\rm CS}=\tfrac{1}{4}\int d^4x\,\vartheta\,{}^*RR\), with
\({}^*RR\equiv \tfrac12\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu}{}^{\alpha\beta}
R_{\rho\sigma\alpha\beta}\propto R\wedge\widetilde R\) the Pontryagin (Chern–
Simons) density and \(\vartheta\) an embedding/coupling field. A *late-time
rolling* \(\vartheta(t)\) is the standard DE-adjacent worry: it can source
parity-violating gravity (GW birefringence) and, if it carries a potential,
behave as quintessence.

### 1.2 Closure argument (CLOSED at channel/amplitude level; upgradeable to
operator-level for constant \(\vartheta\), Tier-II otherwise)

Three independent legs close this operator *as a DE source in minimal ECH*:

**Leg A — topological / total-derivative for constant coupling (rigorous,
Tier-I within scope).** In 4D the Pontryagin density is a total derivative:
\({}^*RR=\partial_\mu K^\mu_{\rm grav}\) (Chern–Simons current). For **constant
\(\vartheta\)** the CS term is a pure boundary term and contributes *nothing* to
the equations of motion or to \(\rho_\Lambda\) — exactly the statement the paper
already makes at L3122–3126 to separate \(R\widetilde R\) from the Holst dual.
This is deductive, not ansatz. So the only way \(R\wedge\widetilde R\) sources
anything dynamical is a **non-constant \(\vartheta\)** with its own kinetic
term / potential.

**Leg B — a dynamical \(\vartheta\) is not in the minimal-ECH field content
(structural, Tier-II).** Minimal ECH has: tetrad, Holst/Barbero–Immirzi term
(a *constant* \(\gamma\), fixed by the LQG area spectrum — Barrier 7, L2946), and
minimally-coupled matter. There is no dynamical pseudoscalar \(\vartheta\)
gravitational-CS coupling in the minimal action. Promoting \(\vartheta\) to a
rolling field is a **non-minimal extension** — precisely the class the paper's
scope excludes and Barrier 11 ("Decoupling Universality," L2983) forbids without
new non-minimal couplings. A \(\vartheta\) with a \(\sim H_0\) mass/potential
tuned to give \(\rho_\Lambda\) is R4 in a gravitational costume: it re-imports
the cosmological-constant fine-tuning (same logic as `sec:r4_birefringence`,
L2443–2458). So *if* one adds it, it is closed by the **same naturalness /
explanatory-deficit objection** that closes R4, not by amplitude.

**Leg C — perturbation transparency covers the induced signal for scalar matter
(rigorous within scope).** For canonical scalar matter, torsion vanishes at all
orders (L3039–3043), the connection is Levi-Civita, and any parity-odd curvature
contraction built from it is governed by the same Bianchi machinery. The CS
term's *observable* channel (GW/CMB birefringence) is exactly the parity channel
the transparency theorem shows is inert in the scalar-matter branch (L3086–3092).
The dynamical-\(\vartheta\), fermion-loop branch is explicitly named as outside
scope (L3030–3031, L3136–3139) — honest, not hidden.

### 1.3 Verdict — Jackiw–Pi
**CLOSED for the minimal sector**, at the same evidentiary tier as R4:
- Constant \(\vartheta\): **Tier-I rigorous** (total derivative; zero EOM
  contribution — a genuine operator-level statement).
- Any DE-relevant *dynamical* \(\vartheta\): outside minimal ECH; if adjoined,
  **Tier-II naturalness closure** identical in structure to R4 (mass/potential
  tuned to \(H_0\) = CC problem relabelled), reinforced by Barriers 7 & 11 and
  by perturbation transparency for the scalar-matter channel.

This is a genuine strengthening: the constant-\(\vartheta\) leg is an
*operator-level* (not merely channel-level) closure and can be stated as a short
theorem-let. It does **not** open a new DE route.

---

## 2. Parity-odd four-fermion Holst partner of R1

### 2.1 The operator
Integrating out torsion in the Holst-extended Einstein–Cartan action yields the
Freidel–Minic–Takeuchi four-fermion structure. The paper already carries the
axial–axial (parity-even) piece,
\(\mathcal{L}_{\rm int}=-\tfrac{3\pi G}{2}\,\tfrac{\gamma^2}{\gamma^2+1}
J^5_\mu J^{5\mu}\) (Eq. `eq:4fermi`, L1510–1511, R1/NJL). The **omitted partner**
is the parity-odd cross term generated at finite \(\gamma\): the vector–axial
current–current interaction \(\propto \tfrac{\gamma}{\gamma^2+1}\,8\pi G\,
J_\mu J^{5\mu}\) (equivalently the \(V\!\cdot\!A\) piece of the
Freidel et al. contact Lagrangian, which the pure-axial R1 term drops). This is
the genuine "Holst partner" the referees named — its coefficient carries the
single power of \(\gamma\) in the numerator (parity-odd), versus \(\gamma^2\)
(parity-even) for R1.

### 2.2 Closure argument (CLOSED at amplitude level; Tier-III)

**Leg A — Planck suppression is identical to R1 (Tier-III, robust).** The
partner is generated by the *same* torsion-elimination step and carries the same
\(\kappa=8\pi G=1/M_{\rm Pl}^2\) prefactor. Its energy density at any
cosmological fermion density is bounded exactly as R1:
\(\rho_{4f}\sim \kappa\,\langle J\rangle\langle J^5\rangle \lesssim
n_\psi^2/M_{\rm Pl}^2\), i.e. the ~70-orders-below-\(\rho_\Lambda\) bound of
`sec:r1_njl` (L2499–2501) applies verbatim. The parity-odd coefficient
\(\gamma/(\gamma^2{+}1)\le \tfrac12\) is O(1) and cannot lift the amplitude.

**Leg B — the mean field vanishes (structural, Tier-II).** A coherent DE
contribution needs a nonzero VEV. \(\langle J^5\rangle\approx 0\) in a
CP-conserving, unpolarized cosmological medium (paper's Barrier 8 / L2502–2504);
\(\langle J\rangle\) (vector current) is the net fermion-number density, tiny
and non-vacuum-like (it redshifts as \(a^{-3}\), \(w=0\), not \(w=-1\)). The
cross term \(\langle J\rangle\langle J^5\rangle\) is therefore doubly
suppressed and carries no coherent \(w=-1\) structure — it cannot mimic
\(\rho_\Lambda\). Incoherent variance \(\langle J J^5\rangle\) is permitted but,
as the paper already argues for R1, does not source coherent DE.

**Leg C — it is genuinely a projection of the R1 operator, not independent
(L1986–1990).** The paper already states R1 and R4 are projections of the *same*
torsion-elimination operator. The parity-odd partner is the third projection of
that identical dimension-6 operator. Closing R1's amplitude budget closes the
partner's, because they share the prefactor and the current bilinears; only the
Lorentz/parity contraction differs, and that changes an O(1) coefficient, not
the \(M_{\rm Pl}^{-2}\) scaling.

### 2.3 Verdict — four-fermion partner
**CLOSED at the amplitude (channel) level, Tier-III**, by the *same* Planck-
suppression + vanishing-mean-field argument that closes R1, because it is
literally the parity-odd projection of the same integrate-out-torsion operator.
It does **not** open a new DE route. One honest caveat keeps it Tier-III not
Tier-I: a fully *operator-level* statement would require writing the complete
basis of dimension-6 torsion-induced four-fermion operators
(\(VV,AA,VA,\) tensor) with the Fierz relations and showing each projection
inherits the bound. That enumeration is short and mechanical (Freidel et al.
give the full contact Lagrangian) but is a real ~1–2 page calculation, not yet
in the paper.

---

## 3. Overall verdict: can P1A upgrade toward operator-level?

**Yes, partially and credibly — this strengthens P1A.** Neither omitted operator
opens a new dark-energy route:

| Operator | Verdict | Basis |
|---|---|---|
| Jackiw–Pi \(R\wedge\widetilde R\) | **CLOSED** | Constant \(\vartheta\): total derivative (Tier-I, operator-level). Dynamical \(\vartheta\): non-minimal ⇒ R4-type naturalness closure (Tier-II) + Barriers 7/11 + transparency. |
| Parity-odd 4-fermion partner | **CLOSED** | Same torsion-elimination operator as R1; identical \(M_{\rm Pl}^{-2}\) Planck suppression + vanishing coherent mean field (Tier-III), O(1) parity coefficient. |

**What the upgrade requires (all in-scope, no new physics):**
1. Add a short subsection to `sec:fourroute` closing the Jackiw–Pi term:
   constant-\(\vartheta\) total-derivative theorem-let (cite Jackiw–Pi 2003;
   reuse the L3122–3126 Pontryagin identity), + the dynamical-\(\vartheta\)
   ⇒ R4-class naturalness closure.
2. Add the parity-odd four-fermion partner explicitly to R1: write the
   \(V\!A\) cross term with coefficient \(\gamma/(\gamma^2{+}1)\,8\pi G\), show
   it inherits R1's Planck suppression and vanishing mean field.
3. **The residual honest gap** — a *complete* dimension-6 parity-odd operator
   basis (all four-fermion Fierz structures + the single gravitational-CS
   invariant) with a projection lemma — is a genuine, bounded, ~1–2 page
   calculation. It is the difference between "operator-level for these two named
   operators" (achievable now) and "operator-level over the entire minimal-ECH
   parity-odd EFT" (the follow-up theory paper the abstract already promises).

**Recommendation:** P1A can legitimately move its language from "these two
operators are *not closed here*" to "these two operators are *also closed*, by
[total-derivative / naturalness] and [Planck-suppression] respectively, leaving
only the full-basis enumeration to the follow-up." That is a real, defensible
strengthening that directly answers the Grok/Gemini flag — while keeping the
one remaining scope statement (complete basis) honest rather than overclaimed.

**Do NOT** claim a full operator-level theorem over the whole parity-odd EFT
from this analysis; that still needs the dedicated enumeration (scoped in step 3).
