# 01 — FRW Consistency of the Sector II Pseudoscalar Mode

**Date:** 2026-03-16
**Status:** FIRST QUICK-KILL TEST
**Question:** Is phi(t) = S_0(t) nonzero on homogeneous isotropic FRW?

---

## 1. Torsion irreducible decomposition on FRW

The torsion tensor T_{lambda mu nu} decomposes into three irreducible pieces
under the Lorentz group:

    T_{lambda mu nu} = (1/3)(T_mu g_{lambda nu} - T_nu g_{lambda mu})
                      + (1/3) epsilon_{lambda mu nu rho} S^rho
                      + q_{lambda mu nu}

where:
- T_mu = T^lambda_{mu lambda} is the trace vector (16 -> 4 components)
- S^rho = (1/6) epsilon^{rho lambda mu nu} T_{lambda mu nu} is the axial vector (4 components)
- q_{lambda mu nu} is the tensor part (16 components), traceless and totally antisymmetric-free

On FRW (homogeneous, isotropic, spatially flat for simplicity):

**Trace vector T_mu:** Homogeneity and isotropy force T_i = 0. The time
component T_0(t) is a scalar under spatial rotations and parity-even.
Result: T_mu = (T_0(t), 0, 0, 0) is ALLOWED.

**Tensor part q_{lambda mu nu}:** The tensor part transforms as a reducible
representation under SO(3). Isotropy kills all components.
Result: q_{lambda mu nu} = 0 on FRW.

**Axial vector S^mu:** Isotropy forces S^i = 0. The time component S^0(t) is
a pseudoscalar under spatial parity (P: S^0 -> -S^0).
This is the critical case.

## 2. Parity analysis of S_0(t)

Under spatial parity P: x^i -> -x^i, the axial vector transforms as

    P: S^0 -> -S^0,   P: S^i -> +S^i

This is because S^mu is a pseudovector (axial vector). Its time component is
a pseudoscalar.

FRW spacetime is parity-invariant: the metric g_{mu nu} and all curvature
tensors are even under P. A nonzero VEV <S^0> != 0 would spontaneously break
parity.

### Does parity invariance of FRW FORBID S_0 != 0?

**No. Parity invariance of the background does not forbid spontaneous breaking.**

The field equations derived from the PGT action are parity-invariant (the
quadratic torsion Lagrangian L = t_1 T^2 + t_2 T^2 + t_3 T^2 is parity-even
because each term is quadratic in torsion). But parity-invariant equations can
have parity-breaking solutions. This is spontaneous symmetry breaking.

However, there is a crucial constraint:

**If S_0 = 0 is a solution and the action is parity-invariant, then S_0 = 0 is
always a consistent solution.** This is because:
- The field equation for S_0 is obtained by varying L with respect to S_0
- Since L is even in S_0 (quadratic), the field equation is odd in S_0
- Therefore dL/dS_0 |_{S_0=0} = 0 identically
- S_0 = 0 is always an extremum

This means S_0 = 0 is a STABLE FIXED POINT of the field equations unless the
effective mass-squared is negative (tachyonic instability).

## 3. Effective potential for S_0

The Sector II quadratic torsion Lagrangian, restricted to the axial part, gives:

    L_axial = (1/2kappa) [(-2t_1 + t_2) S_mu S^mu]    (from decomposition)

Wait — we need to be more careful. The quadratic torsion invariants in terms
of irreducible parts are:

    T^lambda_{mu nu} T_lambda^{mu nu} = (2/3) T_mu T^mu - (2/3) S_mu S^mu + q^2
    T^lambda_{mu nu} T^{mu nu}_{lambda} = (2/3) T_mu T^mu + (2/3) S_mu S^mu + ...
    T^lambda_{mu lambda} T^{mu nu}_{nu} = T_mu T^mu

So the axial-vector contribution to the Lagrangian is:

    L_S = (1/2kappa) [(-2t_1/3 + 2t_2/3) S_mu S^mu]
        = (1/2kappa) [(2/3)(t_2 - t_1)] S_mu S^mu

With the ghost-free condition t_2 = -2t_1:

    L_S = (1/2kappa) [(2/3)(-2t_1 - t_1)] S_mu S^mu
        = (1/2kappa) [(-2t_1)] S_mu S^mu

For S_mu = (S_0(t), 0, 0, 0) on FRW with metric (-,+,+,+):

    S_mu S^mu = g^{00} (S_0)^2 = -(S_0)^2

So:

    L_S = (1/2kappa) [(-2t_1)(-(S_0)^2)] = (1/2kappa)(2t_1)(S_0)^2

This is a MASS TERM, not a kinetic term. On FRW, the homogeneous axial mode
S_0(t) has no spatial gradients, and the time derivatives come from the
kinetic structure of the PGT action (which involves derivatives of torsion
through the curvature-squared terms or through the field equations).

**Critical point:** In the PURELY QUADRATIC torsion sector (no curvature-squared
terms), the torsion field equation is ALGEBRAIC in torsion (second-order in
the metric but algebraic in T). The quadratic terms t_1, t_2, t_3 give a mass
to the torsion, but the KINETIC term for propagating torsion comes from the
curvature-squared sector of PGT.

For Sector II (spin-0^-), the propagating degree of freedom gets its kinetic
term from specific curvature-squared terms in the PGT Lagrangian. Without
those terms, the torsion is non-dynamical (no time derivatives of S_0 in the
equations of motion), and S_0 is algebraically determined.

**On FRW with parity-even matter:** If the matter sector has no axial spin
density (J^5 = 0), then the algebraic equation gives S_0 = 0.

## 4. With propagating kinetic term

If we include the curvature-squared terms that give Sector II its kinetic
energy, then S_0(t) becomes a genuine dynamical field with a Klein-Gordon-like
equation on FRW:

    phi-ddot + 3H phi-dot + m_T^2 phi = source terms

where phi = S_0(t) and m_T = M_Pl / (2 sqrt(|t_3|)).

The source terms on the right-hand side come from:
1. Matter axial spin density J^5 (if present)
2. Non-minimal couplings to curvature (model-dependent)

**For parity-even matter (J^5 = 0) and minimal coupling:**

    phi-ddot + 3H phi-dot + m_T^2 phi = 0

This has the solution phi = 0 as a STABLE fixed point (m_T^2 > 0, no
tachyonic instability). Small perturbations around phi = 0 oscillate and
decay. The solution phi = 0 is an attractor.

## 5. Quick-kill verdict

**S_0 = 0 is NOT forced by FRW symmetry in principle** — parity can be
spontaneously broken. However:

1. S_0 = 0 is always a consistent solution (parity invariance of the action).
2. S_0 = 0 is a STABLE solution (m_T^2 > 0, no tachyonic instability).
3. There is no source term to drive S_0 away from zero in the absence of
   axial spin density.
4. The effective potential V(phi) = (1/2) m_T^2 phi^2 has a unique minimum at
   phi = 0.

**The mode is ALLOWED but NOT POPULATED by the symmetric background.**

This does NOT immediately kill the program, because:
- phi(0) could be nonzero as an initial condition
- The bounce itself might excite phi through parametric effects
- Quantum fluctuations during the bounce could seed phi

But there is no classical mechanism that forces phi to be O(M_Pl) at the
bounce. It is a FREE INITIAL CONDITION.

**RESULT: The quick-kill test is PASSED (barely).** The mode exists on FRW but
S_0 = 0 is a stable attractor. The program continues to File 02 to determine
whether the bounce dynamics can populate this mode.
