#!/usr/bin/env python3
"""Independent exact-arithmetic audit of P1A v1A.0.118 Appendix A/B.

This deliberately does not import arxiv/scripts/fierz_lemma_check.py.  It
checks the row/column selection in the printed matrix, repeats the scalar
projection with explicit Dirac matrices, and propagates the corrected
coefficient through the six-row magnitude scan.
"""

from sympy import I, Matrix, Rational, diag, eye, pi, simplify, zeros


def block(a: Matrix, b: Matrix, c: Matrix, d: Matrix) -> Matrix:
    return Matrix.vstack(Matrix.hstack(a, b), Matrix.hstack(c, d))


# The matrix printed in Eq. (A1), ordered (S,V,T,A,P).  Its prose and the
# cited convention identify rows as source classes and columns as produced
# classes.
F_PRINTED = Rational(1, 4) * Matrix(
    [
        [1, 1, 1, 1, 1],
        [4, -2, 0, 2, -4],
        [6, 0, -2, 0, 6],
        [4, 2, 0, -2, -4],
        [1, -1, 1, -1, 1],
    ]
)

assert F_PRINTED * F_PRINTED == eye(5)
axial_source_row = list(F_PRINTED.row(3))
axial_source_column = list(F_PRINTED.col(3))
eq_a2_coefficients = [
    Rational(1, 4),
    Rational(1, 2),
    0,
    -Rational(1, 2),
    -Rational(1, 4),
]
assert eq_a2_coefficients == axial_source_column
assert axial_source_row == [1, Rational(1, 2), 0, -Rational(1, 2), -1]


# Independent trace check in the normalized basis used by Nieves & Pal,
# arXiv:hep-ph/0306087, Eqs. (1.2), (1.9), and (2.11)--(2.14).
# Their metric is (+---), Gamma_A^mu = i gamma^mu gamma5, and n_A=-i.
z2 = zeros(2)
i2 = eye(2)
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = diag(1, -1)
gamma = [block(i2, z2, z2, -i2)] + [block(z2, s, -s, z2) for s in (s1, s2, s3)]
metric = diag(1, -1, -1, -1)
gamma_lower = [
    sum((metric[mu, nu] * gamma[nu] for nu in range(4)), zeros(4))
    for mu in range(4)
]
gamma5 = simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])

for mu in range(4):
    for nu in range(4):
        assert simplify(
            gamma[mu] * gamma[nu]
            + gamma[nu] * gamma[mu]
            - 2 * metric[mu, nu] * eye(4)
        ) == zeros(4)

# Gamma_A^mu Gamma_{A,mu} = f_AS * 1.  The explicit trace gives f_AS=4.
gamma_a = [I * gamma[mu] * gamma5 for mu in range(4)]
gamma_a_lower = [I * gamma_lower[mu] * gamma5 for mu in range(4)]
trace_product = simplify(sum((gamma_a[mu] * gamma_a_lower[mu] for mu in range(4)), zeros(4)))
assert trace_product == 4 * eye(4)
f_as = simplify(trace_product.trace() / 4)
c_as = simplify(f_as / 4)  # Eq. (2.12): C_AS=f_AS/4
n_a_squared = -1
numeric_spinor_f_as = simplify(n_a_squared * c_as)
grassmann_exchange_f_as = -numeric_spinor_f_as
assert (f_as, c_as, numeric_spinor_f_as, grassmann_exchange_f_as) == (4, 1, -1, 1)


# Propagation under the paper's declared anticommuting direct-channel
# convention.  The original contact coefficient is -3*kappa/16.
g_scalar_over_kappa = -Rational(3, 16) * grassmann_exchange_f_as
g_axial_magnitude_over_kappa = Rational(3, 32)
assert g_scalar_over_kappa == -Rational(3, 16)

print("Eq. (A1) axial source row   :", axial_source_row)
print("Eq. (A1) axial source column:", axial_source_column)
print("Eq. (A2) uses column        :", eq_a2_coefficients)
print("explicit trace f_AS         :", f_as)
print("normalized C_AS             :", c_as)
print("numerical-spinor F_AS       :", numeric_spinor_f_as)
print("Grassmann exchange F_AS     :", grassmann_exchange_f_as)
print("correct G_scalar/kappa      :", g_scalar_over_kappa)
print("axial |G_A|/kappa           :", g_axial_magnitude_over_kappa)
print("corrected six-row scan:")

gamma_bi = Rational(274, 1000)
for degeneracy in (1, 3, 9):
    for cutoff_squared in (1, 1 / gamma_bi):
        scalar_ratio = simplify(
            Rational(3, 4) * degeneracy * cutoff_squared / pi
        )
        axial_ratio = simplify(
            Rational(3, 8) * degeneracy * cutoff_squared / pi
        )
        assert simplify(axial_ratio / scalar_ratio) == Rational(1, 2)
        cutoff_label = "1" if cutoff_squared == 1 else "1/sqrt(0.274)"
        print(
            f"  NfNc={degeneracy} cutoff={cutoff_label:15s} "
            f"R_S={float(scalar_ratio):.8f} R_A={float(axial_ratio):.8f}"
        )
