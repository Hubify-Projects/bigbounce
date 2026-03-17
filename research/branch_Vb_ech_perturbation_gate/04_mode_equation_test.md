# 04: Effective Mode Equation Test

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Test

Starting from the perturbed ECH action with scalar field matter (standard matter bounce setup), derive the effective scalar mode equation and compare with the classical Mukhanov-Sasaki/Bardeen form.

---

## Derivation

### Step 1: ECH action with scalar field

$$
S = \frac{M_{\rm Pl}^2}{2}\int e\, e^\mu_a e^\nu_b \left(R^{ab}{}_{\mu\nu} + \frac{1}{2\gamma}\epsilon^{ab}{}_{cd}R^{cd}{}_{\mu\nu}\right) + S_\phi[e, \phi]
$$

### Step 2: Torsion equation of motion

Varying with respect to ω:

$$
T^a_{\mu\nu}\left(1 + \gamma^{-2}\right)^{-1}(\text{projections}) = \frac{1}{M_{\rm Pl}^2}\tau^a{}_{\mu\nu}
$$

For scalar field matter: $\tau^a{}_{\mu\nu} = 0$.

Therefore: $T^a_{\mu\nu} = 0$ identically.

### Step 3: Consequences of T = 0

When torsion vanishes, the spin connection reduces to the Levi-Civita connection of the tetrad:

$$
\omega^{ab}_\mu = \omega^{ab}_\mu[e] \quad (\text{Levi-Civita})
$$

The curvature tensor $R^{ab}{}_{\mu\nu}[\omega]$ becomes the Riemann tensor $R^{ab}{}_{\mu\nu}[e]$.

The Holst term becomes:

$$
\frac{1}{2\gamma}\epsilon^{ab}{}_{cd}\,e^\mu_a e^\nu_b\, R^{cd}{}_{\mu\nu}[e] = \frac{1}{\gamma}\,\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma} = \frac{1}{\gamma}\,R\tilde{R}
$$

But $\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma} \equiv 0$ by the symmetries of the Riemann tensor (first Bianchi identity when torsion = 0). This is the Gauss-Bonnet-type identity: the Holst term is a topological invariant that vanishes identically when torsion is zero.

**Therefore:** With T = 0, the ECH action reduces exactly to:

$$
S = \frac{M_{\rm Pl}^2}{2}\int d^4x\,\sqrt{-g}\, R[g] + S_\phi[g, \phi]
$$

This is the standard Einstein-Hilbert action plus scalar field. **The Barbero-Immirzi parameter γ has dropped out.**

### Step 4: This holds at ALL orders in perturbation theory

The above is not just a background statement. It holds for the full action, including all perturbative orders:

- $T = 0$ is exact (not an approximation) when matter is a scalar field
- The Holst term vanishes identically (not perturbatively) when $T = 0$
- The reduction to Einstein-Hilbert is exact at all perturbative orders

Therefore:
- The second-order action for scalar perturbations is exactly the standard result
- The Mukhanov-Sasaki equation is exactly the classical form
- No ECH correction terms exist at any order

### Step 5: The mode equation

The scalar perturbation mode equation is:

$$
v_k'' + \left(k^2 - \frac{z''}{z}\right)v_k = 0
$$

with $z = a\dot{\phi}/H$ and the standard expression for $z''/z$ in terms of background quantities.

**There are no ECH corrections to this equation when the perturbation sector is a scalar field.**

---

## Comparison with LQC

In LQC, the situation is fundamentally different:

1. LQC modifies the perturbation equation through "dressed metric" corrections. The effective mass term becomes $z''/z \to \tilde{z}''/\tilde{z}$ where $\tilde{z}$ includes quantum-geometry factors from the holonomy quantization.

2. These corrections arise because LQC modifies the Poisson bracket algebra of constraints (the constraint algebra is "deformed"), which feeds into the perturbation dynamics.

3. The LQC corrections are NOT just from the modified background — they are genuine quantum-gravity effects on the perturbation equation itself.

**ECH does not have these corrections.** ECH is a classical theory (first-order formalism, no holonomy quantization). When torsion is integrated out for scalar matter, the perturbation equations are exactly classical GR on the modified background.

| Feature | ECH perturbations | LQC perturbations |
|---------|-------------------|-------------------|
| Background Friedmann eq | H² = (ρ/3M²)(1 − ρ/ρ_c) | H² = (ρ/3M²)(1 − ρ/ρ_c) |
| Perturbation equation | v'' + (k² − z''/z) v = 0 (classical) | v'' + (k² − z̃''/z̃) v = 0 (quantum-corrected) |
| Source of correction | None (torsion = 0 for scalars) | Holonomy quantization of constraint algebra |
| r prediction | ~10⁻⁵⁵ (no correction to suppress) | ~10⁻⁴ (quantum corrections suppress) |
| γ dependence | None in perturbation eq | ρ_c depends on area gap (related to γ in LQG) |

---

## Verdict

$$
\boxed{\textbf{CLASSICAL\_EQUIVALENT}}
$$

The ECH scalar perturbation equation is exactly the classical Mukhanov-Sasaki equation. No corrections from torsion, Holst term, or Barbero-Immirzi parameter. The only ECH effect is through the modified background evolution (a(t), H(t)), which is the same as LQC at the background level.

**ECH perturbation theory for scalar fields is strictly less informative than LQC perturbation theory**, which at least provides quantum-gravity corrections to the mode equation.

---

## Could anything save this?

### Possibility 1: Include fermion perturbations explicitly

If we track fermion perturbation δψ alongside δφ through the bounce, the four-fermion torsion interaction produces corrections to the fermion sector. These could backreact on the metric perturbations at second order. But:
- This is suppressed by (ρ_fermion/ρ_total) × (ρ/ρ_crit)
- Only relevant near the bounce where ρ ~ ρ_crit
- For super-Hubble modes: bounce is transparent regardless

### Possibility 2: Promote Barbero-Immirzi to a dynamical field

If γ becomes a dynamical pseudoscalar (as explored by Taveras & Yunes 2009, Calcagni & Mercuri 2009), it acquires perturbation dynamics. But this goes beyond the ECH framework — it's a different theory.

### Possibility 3: Include the Nieh-Yan term

The Nieh-Yan topological invariant $N = d(e^a \wedge T_a) = T^a \wedge T_a - e^a \wedge e^b \wedge R_{ab}$ couples the Barbero-Immirzi parameter to torsion in a different way. If included with a dynamical coupling, it could generate perturbation corrections. But again, this goes beyond minimal ECH.

**None of these possibilities operate within the minimal ECH framework as defined by the Holst action with non-dynamical torsion.**
