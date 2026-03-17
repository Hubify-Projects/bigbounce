# Anomaly and Photon Coupling Analysis

**Date:** 2026-03-16

---

## Question: Does exact elimination generate any direct phi-photon coupling?

### Tree Level

The Maxwell action is:

```
S_Maxwell = -(1/4) integral d^4x sqrt(-g) F_{mu nu} F^{mu nu}
```

where F_{mu nu} = partial_mu A_nu - partial_nu A_mu.

The photon field A_mu is a U(1) gauge field. It couples to the metric (through
sqrt(-g) and index raising) but NOT to the spin connection or torsion. This is
because:

1. A_mu carries no Lorentz index -- it is a Lorentz scalar 1-form.
2. The U(1) covariant derivative D_mu = partial_mu + ie A_mu does not involve
   the spin connection.
3. The field strength F_{mu nu} is defined using the partial derivative, not
   the covariant derivative (they are equal for a scalar-valued 1-form even
   with torsion, because torsion only affects the antisymmetric part of the
   connection, and F is already antisymmetrized).

Therefore: **torsion elimination produces NO direct modification of the
Maxwell sector.** This is exact -- not an approximation, and independent of
the order in phi/f_phi.

In particular:
- No phi F F term (parity-even photon coupling)
- No phi F Ftilde term (parity-odd photon coupling)
- No (partial phi)^2 F^2 term
- No phi^n F^2 or phi^n F Ftilde terms

at tree level from torsion elimination.

### Could the Holst term couple to photons directly?

The Holst term is:

```
(1/2 kappa gamma) e^I wedge e^J wedge F_{IJ}
```

where F_{IJ} is the Lorentz curvature, NOT the electromagnetic field strength.
The notation is unfortunately similar, but these are entirely different objects.
The Lorentz curvature F^{IJ} = dw^{IJ} + w^I_K wedge w^{KJ} involves the
spin connection, while the electromagnetic F = dA involves the U(1) potential.

There is NO coupling between the Holst term and the electromagnetic field at
any level.

### Could the d_mu phi - dependent torsion modify the photon propagation?

The torsion with dynamical gamma contains a piece proportional to d_mu phi.
Could this modified torsion affect photon propagation through some indirect
channel?

NO. The photon does not see torsion at all (see above). The torsion-modified
geometry affects the METRIC connection (Christoffel symbols), but only through
the metric itself, which is determined by the Einstein equation. The metric
equation of motion receives torsion corrections (the "torsion stress-energy"),
but these are:
- Quadratic in torsion ~ O(kappa * J^5) ~ O(1/M_Pl^2)
- Modifications to the BACKGROUND geometry, not to the photon coupling
- Present in any theory with fermions and torsion, not ECH-specific

The photon dispersion relation is unmodified by torsion at tree level.

---

## One-Loop: The ABJ Anomaly

The ONLY phi-photon coupling arises at one loop through the ABJ triangle:

```
psi loop: phi -- psi -- gamma -- psi -- gamma
          (derivative coupling vertex) --- (two QED vertices)
```

The effective vertex is:

```
L_{phi gamma gamma} = [alpha / (4 pi)] * [c_psi / f_phi] * phi * F_{mu nu} Ftilde^{mu nu}
```

where c_psi is the derivative coupling coefficient from the torsion-eliminated
action, and the factor alpha/(4 pi) comes from the fermion loop.

For N_eff charged fermion species:

```
L_{phi gamma gamma} = [alpha N_eff / (4 pi f_eff)] * phi * F Ftilde
```

### Is this ECH-specific?

**NO.** The Adler-Bardeen theorem guarantees that the anomaly coefficient is
exact at one loop. It is:

```
c_anomaly = alpha / (4 pi) * sum_f Q_f^2
```

per fermion species with charge Q_f. This is IDENTICAL for:
- The dynamical Immirzi field with derivative coupling
- A standard ALP with derivative coupling
- A KSVZ-type ALP with Yukawa coupling to heavy quarks
- Any pseudoscalar with the appropriate coupling to charged fermions

The anomaly coefficient knows about the CHARGES of the fermions running in the
loop, not about the UV origin of the pseudoscalar.

### Does the phi-dependent derivative coupling modify the anomaly?

The derivative coupling in the ECH-reduced action is:

```
C_1(gamma_0 + phi/f_phi) * (1/f_phi) * partial_mu phi * J^{5,mu}
```

where C_1 is a function, not a constant. Does the phi-dependence of C_1
modify the anomaly?

At one loop, the anomaly calculation uses the LEADING (constant) part of C_1.
The phi-dependent corrections to C_1 generate HIGHER-LOOP effects (the phi
running in the loop modifies the vertex). These are:

```
delta c_anomaly ~ [alpha / (4 pi)] * [C_1'(gamma_0) / C_1(gamma_0)] * (phi/f_phi) * [alpha/(4 pi)]
```

This is a two-loop effect, suppressed by an additional factor of alpha/(4 pi)
~ 10^{-3}. It generates a phi-dependent correction to the anomaly coupling:

```
L_{phi gamma gamma} = [alpha N_eff / (4 pi f_eff)] * phi * [1 + O(alpha/(4 pi)) * phi/f_phi] * F Ftilde
```

The correction is:
- Two-loop suppressed: ~ alpha/(4 pi) ~ 10^{-3}
- Further suppressed by phi/f_phi (slow-roll: phi/f_phi << 1 at late times)
- Total suppression: ~ 10^{-3} * (phi/f_phi) relative to leading term
- Unmeasurable

### Is there a gravitational anomaly contribution?

The gravitational ABJ anomaly generates:

```
L_{phi R Rtilde} ~ [1/(192 pi^2 f_eff)] * phi * R_{mu nu rho sigma} Rtilde^{mu nu rho sigma}
```

This is a gravitational Chern-Simons coupling. It is:
- Present for any pseudoscalar coupled to fermions (not ECH-specific)
- Relevant for chiral gravitational waves (but requires r > 10^{-3})
- A standard result in anomaly calculations

---

## Summary: Photon Coupling

| Source | Coupling | ECH-specific? | Measurable? |
|--------|----------|---------------|-------------|
| Tree-level torsion elimination | None | N/A | N/A |
| 1-loop ABJ anomaly | alpha N_eff/(4 pi f_eff) phi F Ftilde | NO (universal) | YES (birefringence) |
| 2-loop (phi-dependent C_1) | ~ alpha^2/(16 pi^2) * (phi/f_phi) * phi F Ftilde | Technically ECH-specific | NO (10^{-3} correction) |
| Gravitational anomaly | 1/(192 pi^2 f_eff) phi R Rtilde | NO (universal) | NO (requires r > 10^{-3}) |

**Bottom line:** The only measurable phi-photon coupling is the standard ABJ
anomaly, which is universal and not ECH-specific. Exact torsion elimination
produces zero tree-level photon coupling at any order in phi/f_phi.
