# Physical Distinctiveness Assessment

**Date:** 2026-03-16

---

## Question: Is there ANY observationally accessible ECH-specific content?

This file systematically evaluates every candidate for ECH distinctiveness.

---

## Candidate 1: Coefficient relations

### The claim
The ECH derivation predicts specific functions Z_T(gamma_0, phi/f_phi),
C_1(gamma_0, phi/f_phi), C_2(gamma_0, phi/f_phi) for the kinetic function,
derivative coupling, and four-fermion coupling respectively. These are not
arbitrary but are determined by gamma_0. A generic ALP has independent Wilson
coefficients for each operator.

### Assessment
The coefficient relations connect:
- The leading derivative coupling c_{1,0}(gamma_0) to f_phi
- The subleading corrections c_{1,n}(gamma_0) to c_{1,0}
- The four-fermion coupling G_0(gamma_0) to c_{1,0}
- The kinetic renormalization Z_T(gamma_0) to f_phi

These are genuine predictions. However:
- c_{1,0} and f_phi together determine f_eff, which is the only measurable
  quantity. Measuring f_eff does not test the relation because gamma_0 is free.
- The subleading corrections c_{1,n} are suppressed by (phi/f_phi)^n. For
  late-universe dynamics, phi/f_phi << 1 (slow roll). These corrections are
  unmeasurable.
- G_0 involves kappa ~ 1/M_Pl^2. Planck-suppressed. Unmeasurable.
- Z_T renormalizes f_phi -> f_eff. This is absorbed into the single measurable
  parameter f_eff. No independent test.

**Verdict: UNMEASURABLE.** The relations connect unmeasurable coefficients to
each other, or connect to the single measurable parameter f_eff through the
unknown gamma_0.

---

## Candidate 2: Predictions for higher-order ALP self-interactions

### The claim
After canonical normalization (field redefinition phi -> chi to remove the
non-canonical kinetic term), the effective potential and self-couplings of
chi acquire specific gamma_0-dependent corrections.

### Assessment
The field redefinition phi -> chi is:

```
d chi = sqrt(1 + 2 Z_T(gamma_0 + phi/f_phi)) d phi
```

This generates a non-trivial map chi(phi), and the effective potential becomes
V_eff(chi) = V(phi(chi)). The self-couplings are:

```
lambda_3 = V'''_eff(chi_0) / f_eff^3,  etc.
```

These depend on:
- V(phi), which is NOT determined by ECH (external input)
- The field redefinition chi(phi), which depends on gamma_0 and f_phi
- The combination gamma_0 and f_phi, which are both free parameters

Since V(phi) is unknown, the self-couplings lambda_3, lambda_4, ... are
unpredicted. The gamma_0-dependent field redefinition modifies them, but
the modification is degenerate with the unknown V(phi).

**Verdict: UNMEASURABLE.** The self-interaction predictions require knowledge
of V(phi), which ECH does not provide.

---

## Candidate 3: Correlation between f_phi and gamma_0

### The claim
The physical decay constant f_eff depends on both f_phi and gamma_0:

```
f_eff = f_phi / sqrt(1 + 2 Z_T(gamma_0))
```

If gamma_0 were independently measurable, this would be a testable prediction.

### Assessment
gamma_0 is the background Barbero-Immirzi parameter. It enters:
- Loop quantum gravity (LQG) area spectrum: A = 8 pi gamma_0 l_Pl^2 sqrt(j(j+1))
- Black hole entropy: S_BH = (a_H)/(4 gamma_0 l_Pl^2) * (gamma_0 value fixed by
  matching Bekenstein-Hawking entropy)

In LQG, the standard value is gamma_0 ~ 0.274 (Immirzi's value from BH entropy).
However:
- This value is model-dependent (depends on the spin label sum)
- LQG is not experimentally verified
- The LQG value may not apply to the ECH context (different quantization)
- Even if gamma_0 = 0.274, measuring f_eff only tests f_phi = f_eff * sqrt(1 + 2 Z_T(0.274)),
  which is just a rescaling by a known factor

**Verdict: NOT INDEPENDENTLY TESTABLE.** gamma_0 is a free parameter in the
ECH context. Using the LQG value is a theoretical choice, not an observational
constraint.

---

## Candidate 4: The absence of tree-level phi F Ftilde

### The claim
The ECH derivation shows that phi does not couple to photons at tree level.
The coupling is purely through the ABJ anomaly. This is a RESTRICTION on the
ALP parameter space: in generic ALP models, tree-level phi F Ftilde with
arbitrary coefficient is allowed.

### Assessment
This is technically correct. The ECH framework predicts:

```
c_gamma = alpha N_eff / (4 pi)  [anomaly-induced only]
```

while a generic ALP allows:

```
c_gamma = arbitrary
```

The restriction c_gamma = c_anomaly is testable IN PRINCIPLE: if a measurement
determined both f_eff and c_gamma independently, one could check whether
c_gamma = alpha N_eff / (4 pi).

However:
- Birefringence measures (c_gamma / f_eff) * Delta phi. This is ONE number.
- To test the relation, one needs c_gamma and f_eff separately.
- c_gamma alone is not measurable (always appears as c_gamma / f_eff).
- f_eff alone requires a second observable (e.g., phi-mediated force, or
  phi mass from spectral features). These are model-dependent.

The restriction IS distinguishable from the most general ALP in the
(c_gamma, f_eff) parameter plane, but the two are degenerate along the line
c_gamma / f_eff = constant, which is the only observable.

**Verdict: NOT TESTABLE with birefringence alone.** Would require a second
independent measurement of either c_gamma or f_eff, which is not available
for an ultralight ALP with f ~ M_Pl.

---

## Candidate 5: The four-fermion contact interaction

### The claim
The ECH framework uniquely predicts a (J^5)^2 four-fermion interaction with
strength G ~ kappa / (1 - 3/(4 gamma_0^2)). This is not present in a standard
ALP model (which has only the derivative coupling).

### Assessment
The four-fermion coupling is:

```
G_0 = (3 kappa / 32) / (1 - 3/(4 gamma_0^2)) ~ 10^{-38} GeV^{-2} * O(1)
```

This is a Planck-suppressed contact interaction. For comparison:
- The Fermi constant (weak interaction): G_F ~ 10^{-5} GeV^{-2}
- The torsion four-fermion: G_torsion ~ 10^{-38} GeV^{-2}

The torsion four-fermion is 33 orders of magnitude below the weak interaction.
It is unmeasurable by any conceivable experiment.

Furthermore, this operator is not specific to the dynamical Immirzi field --
it is present in ANY Einstein-Cartan theory with fermions (constant gamma
included). The dynamical gamma adds phi-dependent corrections, but these are
corrections to an already unmeasurable quantity.

**Verdict: UNMEASURABLE by ~33 orders of magnitude.**

---

## Candidate 6: The vector torsion sourced by d_mu phi

### The claim
In the constant-gamma case, vector torsion vanishes (for Dirac sources).
With dynamical gamma, d_mu phi sources nonzero vector torsion. This is
qualitatively new.

### Assessment
The vector torsion sourced by d_mu phi is:

```
v_mu ~ (1/(gamma_0^2 f_phi)) partial_mu phi ~ M_Pl^{-1} partial_mu phi / gamma_0^2
```

This is: (slow-roll velocity of phi) / M_Pl, suppressed by 1/gamma_0^2.
For an ultralight field with H_0 ~ 10^{-33} eV:

```
v_mu ~ H_0 phi_0 / (M_Pl gamma_0^2) ~ 10^{-33} eV * M_Pl / (M_Pl * gamma_0^2) ~ 10^{-33} eV / gamma_0^2
```

This is cosmologically tiny. It modifies the torsion background but at a level
suppressed by H_0 / M_Pl ~ 10^{-61}. Unmeasurable.

Additionally, after torsion elimination, the vector torsion contribution is
absorbed into the phi kinetic term (it is one of the sources of Z_T). There is
no independent observable from vector torsion.

**Verdict: UNMEASURABLE. Absorbed into kinetic renormalization after elimination.**

---

## Candidate 7: Non-perturbative effects (instantons)

### The claim
The Immirzi field phi could have a potential generated by gravitational
instantons (analogous to the QCD axion mass from QCD instantons). This
potential would depend on gamma_0 in a specific way.

### Assessment
Gravitational instanton contributions to the Immirzi field potential are:

```
V_inst ~ M_Pl^4 exp(-S_inst) ~ M_Pl^4 exp(-M_Pl^2 / Lambda_grav^2)
```

For Lambda_grav ~ M_Pl: V_inst ~ M_Pl^4 exp(-1) ~ M_Pl^4, which is far too
large (cosmological constant problem).

For any sub-Planckian scale: V_inst is exponentially suppressed, typically
many orders below the required ultralight mass m ~ 10^{-33} eV.

The gravitational instanton calculation in the ECH context has never been
completed, and the result is highly sensitive to the UV completion. This is
not a prediction but an open problem.

**Verdict: NOT A PREDICTION. Requires UV completion that ECH does not provide.**

---

## Summary

| Candidate | ECH-specific content? | Observable? | Testable? |
|-----------|----------------------|-------------|-----------|
| 1. Coefficient relations | Yes (gamma_0 dependent) | No (Planck-suppressed or degenerate) | No |
| 2. Self-interactions | Yes (after field redef) | No (requires unknown V(phi)) | No |
| 3. f_phi - gamma_0 correlation | Yes | Only if gamma_0 known independently | No |
| 4. No tree-level phi F Ftilde | Yes (restriction) | Degenerate with f_eff | No (with birefringence alone) |
| 5. Four-fermion (J^5)^2 | Yes | No (33 orders too weak) | No |
| 6. Vector torsion from d phi | Yes (qualitatively new) | No (absorbed into Z_T) | No |
| 7. Instanton potential | Unknown | Unknown | No (requires UV completion) |

**NONE of the seven candidates for ECH-specific content is observationally
testable.**

---

## The Honest Statement

The dynamical Immirzi field is a well-motivated ultralight pseudoscalar
whose existence is suggested by the geometric structure of gravity in the
first-order formalism. The ECH framework:

1. MOTIVATES the existence of phi (promoting an existing parameter to a field)
2. CONSTRAINS f_phi ~ M_Pl (from the geometric identification)
3. PREDICTS specific Wilson coefficients (as functions of gamma_0)

But all three contributions are at the level of THEORETICAL PRIORS, not
observable predictions. The low-energy phenomenology is identical to a
generic ALP with f_a ~ M_Pl.

A measurement of birefringence beta ~ 0.3 deg would be CONSISTENT with the
dynamical Immirzi field. But it would be equally consistent with any ALP
having f_a ~ M_Pl. There is no observable that can confirm or refute the
ECH origin.
