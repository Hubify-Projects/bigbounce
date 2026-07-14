#!/usr/bin/env python3
r"""Exact Fierz convention check for P1A.

The check keeps two maps separate:

1. ``F_cnum`` is the c-number spinor rearrangement of Nieves & Pal,
   arXiv:hep-ph/0306087, Eqs. (2.1), (2.14), and (2.15):

       e_I(1234) = sum_J F_cnum[I,J] e_J(1432).

   Rows are source classes and columns are produced classes.

2. Forming anticommuting field operators requires one Grassmann exchange to
   put the fields into the rearranged bilinears, so ``F_op = -F_cnum``.

For an axial source, the operator row is

    AA -> SS + 1/2 VV + 1/2 AA - PP.

Only the scalar exchange coefficient is used in P1A's declared direct-channel
mean-field check.  The axial entry is reported only by magnitude because its
sign is operator-order-convention dependent and is not used for a condensation
claim.  The calculation does not remove the mean-field Fierz ambiguity or
enumerate derivative, flavor/color-exchange, or gravitational-EFT operators.
"""

from __future__ import annotations

import sympy as sp


CLASSES = ("S", "V", "T", "A", "P")


def block(a: sp.Matrix, b: sp.Matrix, c: sp.Matrix, d: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))


def gamma_trace_scalar_projection() -> dict[str, sp.Expr]:
    """Reproduce the axial-to-scalar coefficient with explicit gamma traces.

    This follows the normalized (+---) basis of Nieves & Pal:
    ``Gamma_A^mu=i gamma^mu gamma5`` and ``n_A=-i``.  Their trace coefficient
    is ``C_AS=f_AS/4``; the ``n_A^2`` conversion gives the c-number Fierz
    coefficient, and one further minus gives the anticommuting operator map.
    """

    I = sp.I
    z2 = sp.zeros(2)
    i2 = sp.eye(2)
    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -I], [I, 0]])
    sigma3 = sp.diag(1, -1)
    gamma = [block(i2, z2, z2, -i2)] + [
        block(z2, sigma, -sigma, z2)
        for sigma in (sigma1, sigma2, sigma3)
    ]
    metric = sp.diag(1, -1, -1, -1)
    gamma_lower = [
        sum((metric[mu, nu] * gamma[nu] for nu in range(4)), sp.zeros(4))
        for mu in range(4)
    ]
    gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])

    for mu in range(4):
        for nu in range(4):
            residual = sp.simplify(
                gamma[mu] * gamma[nu]
                + gamma[nu] * gamma[mu]
                - 2 * metric[mu, nu] * sp.eye(4)
            )
            assert residual == sp.zeros(4)

    gamma_a = [I * gamma[mu] * gamma5 for mu in range(4)]
    gamma_a_lower = [I * gamma_lower[mu] * gamma5 for mu in range(4)]
    axial_contraction = sp.simplify(
        sum(
            (gamma_a[mu] * gamma_a_lower[mu] for mu in range(4)),
            sp.zeros(4),
        )
    )
    assert axial_contraction == 4 * sp.eye(4)

    f_as = sp.simplify(axial_contraction.trace() / 4)
    c_as = sp.simplify(f_as / 4)
    cnum_f_as = sp.simplify((-1) * c_as)  # n_A^2=(-i)^2=-1
    operator_f_as = sp.simplify(-cnum_f_as)  # Grassmann exchange
    assert (f_as, c_as, cnum_f_as, operator_f_as) == (4, 1, -1, 1)
    return {
        "f_AS": f_as,
        "C_AS": c_as,
        "cnumber_F_AS": cnum_f_as,
        "operator_F_AS": operator_f_as,
    }


def main() -> None:
    # Nieves-Pal Eq. (2.14), with rows I=source and columns J=produced.
    F_cnum = sp.Rational(1, 4) * sp.Matrix(
        [
            [1, 1, sp.Rational(1, 2), -1, 1],
            [4, -2, 0, -2, -4],
            [12, 0, -2, 0, 12],
            [-4, -2, 0, -2, 4],
            [1, -1, sp.Rational(1, 2), 1, 1],
        ]
    )
    assert F_cnum * F_cnum == sp.eye(5)

    F_op = -F_cnum
    axial_source = CLASSES.index("A")
    axial_cnum_row = list(F_cnum.row(axial_source))
    axial_operator_row = list(F_op.row(axial_source))
    assert axial_cnum_row == [
        -1,
        -sp.Rational(1, 2),
        0,
        -sp.Rational(1, 2),
        1,
    ]
    assert axial_operator_row == [
        1,
        sp.Rational(1, 2),
        0,
        sp.Rational(1, 2),
        -1,
    ]

    trace = gamma_trace_scalar_projection()
    assert trace["cnumber_F_AS"] == axial_cnum_row[0]
    assert trace["operator_F_AS"] == axial_operator_row[0]

    contact_over_kappa = -sp.Rational(3, 16)
    scalar_over_kappa = sp.simplify(contact_over_kappa * axial_operator_row[0])
    axial_over_kappa = sp.simplify(contact_over_kappa * axial_operator_row[3])
    assert scalar_over_kappa == -sp.Rational(3, 16)
    assert axial_over_kappa == -sp.Rational(3, 32)

    produced = {
        CLASSES[index]
        for index, coefficient in enumerate(axial_operator_row)
        if coefficient != 0
    }
    assert produced == {"S", "V", "A", "P"}

    print("[1] Nieves-Pal c-number Fierz matrix (rows=source, cols=produced):")
    sp.pprint(F_cnum)
    print("    F_cnum^2 = I: PASS")
    print("[2] Anticommuting operator map F_op=-F_cnum: PASS")
    print("[3] Axial c-number row   :", axial_cnum_row)
    print("[4] Axial operator row   :", axial_operator_row)
    print("[5] Explicit trace audit :", trace)
    print("[6] G_scalar/kappa       :", scalar_over_kappa)
    print("[7] |G_A|/kappa benchmark:", abs(axial_over_kappa))
    print("[8] Produced classes     :", sorted(produced))
    print("[9] No single-species eigenspace claim is used.")
    print("FIERZ CONVENTION CHECK: PASS")


if __name__ == "__main__":
    main()
