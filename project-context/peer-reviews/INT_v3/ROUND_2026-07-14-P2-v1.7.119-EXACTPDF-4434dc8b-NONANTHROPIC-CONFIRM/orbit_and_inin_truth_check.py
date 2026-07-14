#!/usr/bin/env python3
"""Exact checks for the two high-impact Codex findings in the v1.7.118 audit.

This script is review evidence only.  It reads no project state and writes no
outputs.  The symbolic expressions reproduce the two equal forms of Cai et
al.'s field-redefinition contribution and compare consistent six-Wick and
mixed orbit conventions.
"""

from itertools import permutations

import sympy as sp


k1, k2, k3, epsilon = sp.symbols("k1 k2 k3 epsilon", nonzero=True)
ks = (k1, k2, k3)
pi_k2 = k1**2 * k2**2 * k3**2


def ordered_pair(a: int, b: int) -> sp.Expr:
    return sum(ks[i] ** a * ks[j] ** b for i in range(3) for j in range(3) if i != j)


def six_wick(a: int, b: int, c: int) -> sp.Expr:
    return sum(ks[p[0]] ** a * ks[p[1]] ** b * ks[p[2]] ** c for p in permutations(range(3)))


def distinct_522() -> sp.Expr:
    return sum(ks[i] ** 5 * ks[(i + 1) % 3] ** 2 * ks[(i + 2) % 3] ** 2 for i in range(3))


s3 = sum(k**3 for k in ks)
t522_six = six_wick(5, 2, 2)
t522_distinct = distinct_522()
t432_six = six_wick(4, 3, 2)

# Cai et al. arXiv:0903.0631v2: the first and second displayed forms of the
# field-redefinition contribution (matterbounceng2.tex, source lines 517--526).
def redef_first(t522: sp.Expr) -> sp.Expr:
    brace = (
        ordered_pair(7, 2)
        + ordered_pair(6, 3)
        - 2 * ordered_pair(5, 4)
        - 2 * t522
        - t432_six
    )
    return -epsilon * s3 / 2 - epsilon**2 * brace / (32 * pi_k2)


redef_second = (
    (-epsilon / 2 + epsilon**2 / 8) * s3
    + epsilon**2 * ordered_pair(1, 2) / 32
    - epsilon**2
    * (ordered_pair(7, 2) + ordered_pair(6, 3) - 2 * ordered_pair(5, 4))
    / (32 * pi_k2)
)


print("Wick multiplicity identity T522_six - 2*T522_distinct =")
print(sp.factor(t522_six - 2 * t522_distinct))
print("Cai field-redefinition equality with six-Wick T522 =")
print(sp.factor(redef_first(t522_six) - redef_second))
print("Cai field-redefinition equality with mixed distinct T522/six T432 =")
print(sp.factor(redef_first(t522_distinct) - redef_second))

# The commutator sign follows without a model-specific convention.  For
# z=<Q H_int>, Hermiticity gives <H_int Q>=z*, hence [Q,H_int]=2i Im(z).
print("In-in sign algebra:")
print("<Q H_int> - <H_int Q> = z - z* = 2 i Im(z)")
print("-i <[Q,H_int]> = +2 Im(z)")
print("Therefore a displayed -2 Im(I_v) requires I_v=<Q L_int>=-<Q H_int>,")
print("or another explicit extra-minus definition; v1.7.118 defines neither.")
