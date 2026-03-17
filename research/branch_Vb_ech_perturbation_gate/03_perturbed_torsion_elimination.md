# 03: Torsion Elimination at the Perturbed Level

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Torsion Equation of Motion

In the ECH first-order formalism, varying the action with respect to the spin connection ω^{ab}_μ gives the torsion equation:

$$
T^a_{\mu\nu} + \delta^a_{[\mu} T^b_{\nu]b} - \frac{1}{\gamma}\,\epsilon^a{}_{bcd}\,e^{b[\mu}\,T^{cd}{}_{\nu]} = \frac{1}{M_{\rm Pl}^2}\,\tau^a{}_{\mu\nu}
$$

where $\tau^a{}_{\mu\nu}$ is the spin current of matter:

$$
\tau^a{}_{\mu\nu} = \frac{\delta S_{\rm matter}}{\delta \omega_{a}{}^{\mu\nu}}
$$

**This is an algebraic equation for torsion in terms of the spin current.** Torsion is not dynamical — it does not propagate. It is determined locally by the matter spin density.

---

## Spin Current by Matter Type

### Scalar field: τ = 0

A scalar field φ with action $S = -\int e\,[\frac{1}{2}g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi + V(\phi)]$ has:

$$
\tau^a{}_{\mu\nu}\big|_{\rm scalar} = 0
$$

Scalars have spin 0. They do not couple to the connection. **Their spin current vanishes identically, at all orders in perturbation theory.**

Consequence: If the only matter is a scalar field, the torsion equation gives $T^a_{\mu\nu} = 0$ exactly — both at background and perturbed levels.

### Dirac fermion: τ ≠ 0

A Dirac fermion with action $S = \int e\,\bar{\psi}(i\gamma^a e^\mu_a D_\mu - m)\psi$ has:

$$
\tau^a{}_{\mu\nu}\big|_{\rm Dirac} = \frac{1}{4}\,\epsilon^a{}_{bcd}\,e^{b\mu}\,e^{c\nu}\,\bar{\psi}\gamma^d\gamma_5\psi + \text{(trace terms)}
$$

The spin current is proportional to the axial fermion bilinear $\bar{\psi}\gamma^a\gamma_5\psi$.

Consequence: Fermions source torsion. Torsion perturbations exist only if the matter includes fermions.

---

## Perturbed Torsion Elimination: Three Cases

### Case 1: Scalar field matter only (standard matter bounce setup)

This is the setup used in Phase 1a and in the standard matter bounce literature.

- Background: T̄ = 0 (no torsion on FRW with scalar matter)
- Perturbations: δT = 0 (no torsion perturbations from scalar matter)
- Connection: ω = Levi-Civita(e) at all orders
- Holst term: identically zero when T = 0 (topological identity)

**Result:** The perturbed ECH action with scalar field matter reduces EXACTLY to the perturbed Einstein-Hilbert action with scalar field matter. The Barbero-Immirzi parameter γ drops out completely. No ECH-specific corrections exist.

**The Mukhanov-Sasaki equation is exactly the classical form: v'' + (k² − z''/z)v = 0.**

But wait — where does the ρ² modification to the Friedmann equation come from? If torsion vanishes for scalar fields, the bounce doesn't happen with scalar matter alone.

**Answer:** The bounce requires fermions. The ρ² term comes from integrating out torsion sourced by the cosmic fermion bath (quarks, leptons, neutrinos). The scalar field generates the perturbation spectrum during contraction, but the bounce is driven by fermionic spin-torsion coupling.

This means the perturbation sector (scalar field) and the bounce sector (fermion torsion) are decoupled at leading order. The scalar perturbation equation is classical, and the bounce merely provides the background a(t) through the fermionic ρ² correction.

### Case 2: Fermion matter only (Fermi-bounce, Alexander et al. 2014)

- Background: T̄ ≠ 0 (fermion spin current sources background torsion)
- Actually, on FRW: $\langle\bar{\psi}\gamma^a\gamma_5\psi\rangle = 0$ by isotropy (no preferred axial direction), so T̄ = 0 even with fermions. The ρ² correction comes from the effective stress-energy of the four-fermion interaction after integrating out torsion at the action level.

At the perturbed level:
- $\delta\tau^a_{\mu\nu} \propto \delta(\bar{\psi}\gamma^a\gamma_5\psi)$ — perturbations of the axial bilinear
- These source $\delta T^a_{\mu\nu}$ algebraically
- Integrating out $\delta T$ gives an effective four-fermion vertex at the perturbed level:

$$
\delta^2 S_{\rm eff} \supset \frac{\kappa_s^2}{M_{\rm Pl}^2}\,(\delta J^a_5)(\delta J_{5a})
$$

where $J^a_5 = \bar{\psi}\gamma^a\gamma_5\psi$ is the axial current and $\kappa_s$ involves the Barbero-Immirzi parameter.

**Result:** Fermion perturbations get a four-fermion contact interaction correction. This modifies the fermion perturbation dynamics but does NOT directly affect scalar metric perturbations (Φ, Ψ) unless the fermion perturbations backreact on the metric at second order.

Alexander et al. (2014) found that after integrating out torsion, the perturbation equations for the Mukhanov-Sasaki variable on the modified background are standard. The four-fermion correction affects the matter sector internally but the gravitational perturbation equation is unchanged.

### Case 3: Mixed scalar + fermion matter (most physical)

The actual cosmological scenario has both:
- Scalar field (or effective dust) generating the perturbation spectrum
- Fermion bath sourcing torsion and providing the bounce

At the perturbed level:
- Scalar perturbations δφ do not source torsion perturbations (τ_scalar = 0)
- Fermion perturbations δψ do source torsion perturbations
- The torsion perturbations δT are determined algebraically by δψ alone
- After integrating out δT:
  - δφ equation: unchanged (no coupling to torsion)
  - δψ equation: gets four-fermion correction
  - Metric perturbations (Φ, Ψ): sourced by both δφ and δψ stress-energy

**Key question:** Does the four-fermion correction to the fermion sector feed back into the scalar perturbation spectrum?

**Answer:** At linear order, NO. The scalar and fermion perturbation sectors decouple (different spin, no direct coupling). The metric perturbation Φ is sourced by the total perturbed stress-energy, but if the scalar field dominates the perturbation spectrum (as in the standard matter bounce), the fermion contribution is subdominant.

At second order, there could be mixed scalar-fermion corrections, but these would be:
- Suppressed by (ρ/ρ_crit) during the contraction phase (when ρ ≪ ρ_crit)
- Only relevant near the bounce (when ρ ~ ρ_crit), but for super-Hubble modes the bounce is transparent

---

## Summary: Does Torsion Elimination Introduce New Operators?

| Correction type | Present? | Magnitude | Affects scalar spectrum? |
|----------------|----------|-----------|------------------------|
| Kinetic term modification | NO | — | — |
| Sound speed modification | NO | — | — |
| Effective potential (z''/z) correction | NO for scalar matter | — | — |
| Four-fermion contact at perturbed level | YES (for fermion perturbations) | O(ρ/ρ_crit) | NO (decoupled at linear order) |
| Mixed scalar-fermion at second order | In principle | O(ρ/ρ_crit)² | Negligible for super-Hubble modes |
| Holst-term correction at perturbed level | NO (Holst = 0 when T = 0) | — | — |

**Bottom line:** After integrating out torsion perturbations, the scalar perturbation action is EXACTLY the classical GR result. The Barbero-Immirzi parameter γ does not appear in the scalar perturbation equations. The Holst term is identically zero at the perturbed level for scalar matter. No new scalar operators are generated.
