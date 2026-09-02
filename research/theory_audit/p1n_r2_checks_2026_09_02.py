#!/usr/bin/env python3
"""P1N v1N.0.2 R2 truth-audit — independent symbolic/numeric checks.

Checks (printed with intermediates):
  C1  Eq. (13) kappa-substitution: is -24 MPl^2 alpha beta = -3 kappa gamma^3/(1+gamma^2)^2 ?
  C2  corrected O4/O5 ratio and the "bare invariant" power of G
  C3  structural contraction O4 = eps T T on the on-shell torsion  -> -24 alpha beta (J5.J5)
  C4  structural contraction O5 = eps T e J5                      -> -6 alpha (J5.J5)
  C5  O1 == O6 for a metric-compatible (so(1,3)) connection: tetrad conversion identity
  C6  parity class of O5 off shell (Gemini P1N-M2 vs Claude MINOR 1)

Run: python3 research/theory_audit/p1n_r2_checks_2026_09_02.py
"""
import itertools, random
import sympy as sp

kappa, gamma, G, MPl = sp.symbols('kappa gamma G M_Pl', positive=True)
J2 = sp.Symbol('J5dotJ5')

print("=" * 72)
print("C1 — Eq. (13) substitution")
print("=" * 72)
alpha = kappa * gamma**2 / (2 * (1 + gamma**2))
beta = kappa * gamma / (4 * (1 + gamma**2))
print("  alpha =", alpha, "   beta =", beta, "   (main.tex:198-199)")
lhs = sp.simplify(-24 * MPl**2 * alpha * beta)
print("  -24 MPl^2 alpha beta =", lhs)
# paper's own convention: kappa = 8 pi G = 8 pi / MPl^2  =>  MPl^2 = 8 pi / kappa
lhs_sub = sp.simplify(lhs.subs(MPl**2, 8 * sp.pi / kappa))
print("  substitute MPl^2 = 8 pi / kappa (main.tex:180):", lhs_sub)
printed = -3 * kappa * gamma**3 / (1 + gamma**2)**2
print("  printed RHS of Eq. (13)                     :", printed)
ratio = sp.simplify(lhs_sub / printed)
print("  correct / printed =", ratio, "=", sp.N(ratio, 17), " (8*pi =", sp.N(8*sp.pi, 17), ")")
assert sp.simplify(ratio - 8 * sp.pi) == 0
print("  => Eq. (13) RHS is too small by exactly 8*pi. Correct: -24*pi*kappa*g^3/(1+g^2)^2")

print()
print("=" * 72)
print("C2 — O4/O5 ratio and the P1C 'bare invariant'")
print("=" * 72)
O5 = -3 * kappa * gamma**2 / (1 + gamma**2)
print("  O5 (paper, verified in C4) =", O5)
r_printed = sp.simplify(printed / O5)
r_correct = sp.simplify(lhs_sub / O5)
g0 = sp.Rational(2375, 10000)
print("  printed  O4/O5 =", r_printed, "=", sp.N(r_printed.subs(gamma, g0), 4), "at gamma=0.2375")
print("  correct  O4/O5 =", r_correct, "=", sp.N(r_correct.subs(gamma, g0), 4), "at gamma=0.2375")
print("  => ordering inverts: O4 is ~5.65x LARGER than O5, not 0.22x smaller.")
bare = sp.simplify(lhs_sub.subs(kappa, 8 * sp.pi * G))
print("  bare invariant (kappa -> 8 pi G):", bare)
print("  P1C v1C.0.16 main.tex:2123 prints -192*pi^2*G^2*g^3/(1+g^2)^2  -> wrong power of G")
print("  dimension check: (J5.J5) has mass dim 6; a dim-4 density needs a coefficient of")
print("  mass dim -2, i.e. exactly ONE power of G. G^2 is dimensionally impossible.")

def eps4():
    e = {}
    for p in itertools.permutations(range(4)):
        sgn = sp.Integer(sp.LeviCivita(*p))
        e[p] = sgn
    return e

EPS = eps4()
eta = sp.diag(-1, 1, 1, 1)          # mostly-plus, as in the Note


def torsion(a_val, b_val, J):
    """T_{abc} = alpha eps_{abcd} J^d + beta (eta_ab J_c - eta_ac J_b), all indices down."""
    T = {}
    Jup = [sum(eta[d, e] * J[e] for e in range(4)) for d in range(4)]  # J^d from J_d
    for a in range(4):
        for b in range(4):
            for c in range(4):
                v = 0
                for d in range(4):
                    if (a, b, c, d) in EPS:
                        v += a_val * EPS[(a, b, c, d)] * Jup[d]
                v += b_val * (eta[a, b] * J[c] - eta[a, c] * J[b])
                T[(a, b, c)] = sp.expand(v)
    return T


A, B = sp.symbols('alpha beta')
J = list(sp.symbols('J0 J1 J2 J3'))
Jsq = sp.expand(sum(eta[m, n] * J[m] * J[n] for m in range(4) for n in range(4)))
T = torsion(A, B, J)
# eps^{abcd} = - eps_{abcd} in mostly-plus with eps_{0123}=+1
EPSup = {k: -v for k, v in EPS.items()}

print()
print("=" * 72)
print("C3/C4 — structural contractions on the on-shell torsion")
print("=" * 72)
# O4 = eps^{mnrs} T^I_{mn} T_{I rs} = eps^{abcd} T^e_{ab} T_{e cd}
O4s = 0
for (a, b, c, d), s in EPSup.items():
    for e in range(4):
        for f in range(4):
            O4s += s * eta[e, f] * T[(e, a, b)] * T[(f, c, d)]
O4s = sp.expand(O4s)
print("  eps.TT =", sp.factor(sp.simplify(O4s)), "  [note J0^2-J1^2-J2^2-J3^2 = -(J5.J5) in mostly-plus]")
print("  i.e. eps.TT = -24*alpha*beta*(J5.J5)  -- matches the paper's structural coefficient")
assert sp.simplify(O4s - (-24 * A * B * Jsq)) == 0
# O5 = eps^{abcd} T^I_{ab} e_{I c} J5_d  -> flat frame: eps^{abcd} T_{c ab} J_d
O5s = 0
for (a, b, c, d), s in EPSup.items():
    O5s += s * T[(c, a, b)] * J[d]
O5s = sp.expand(O5s)
print("  eps.TeJ =", sp.factor(sp.simplify(O5s)), "  i.e. -6*alpha*(J5.J5)")
assert sp.simplify(O5s - (-6 * A * Jsq)) == 0
O5_onshell = sp.simplify((-6 * alpha))
print("  O5 on shell = -6*alpha*(J5.J5) =", O5_onshell, "* (J5.J5)  -> matches printed Eq. (12)")
O4_onshell_struct = sp.simplify(-24 * alpha * beta)
print("  O4 structural = -24*alpha*beta =", O4_onshell_struct,
      "  (NOTE: no MPl^2 -> the MPl^2 in Eq. (13) is the definitional prefactor)")

print()
print("=" * 72)
print("C5 — O1 vs O6 for a metric-compatible connection")
print("=" * 72)
random.seed(11)
# random tetrad and random so(1,3) curvature R_{IJrs} with its pair antisymmetries
e = sp.Matrix(4, 4, lambda i, j: sp.Rational(random.randint(-5, 5), random.randint(1, 4)))
R = {}
for I in range(4):
    for Jn in range(4):
        for r in range(4):
            for s in range(4):
                R[(I, Jn, r, s)] = 0
for I in range(4):
    for Jn in range(I + 1, 4):
        for r in range(4):
            for s in range(r + 1, 4):
                v = sp.Rational(random.randint(-9, 9), random.randint(1, 5))
                R[(I, Jn, r, s)] = v
                R[(Jn, I, r, s)] = -v
                R[(I, Jn, s, r)] = -v
                R[(Jn, I, s, r)] = v
O1 = 0
for (m, n, r, s), sg in EPSup.items():
    for I in range(4):
        for Jn in range(4):
            O1 += sg * e[I, m] * e[Jn, n] * R[(I, Jn, r, s)]
# O6 uses R_{mnrs} := e^I_m e^J_n R_{IJrs}  (the ONLY definition available for a
# metric-compatible so(1,3) connection; the tetrad converts frame->coordinate exactly)
O6 = 0
for (m, n, r, s), sg in EPSup.items():
    Rc = sum(e[I, m] * e[Jn, n] * R[(I, Jn, r, s)] for I in range(4) for Jn in range(4))
    O6 += sg * Rc
print("  O1 =", sp.nsimplify(sp.expand(O1)))
print("  O6 =", sp.nsimplify(sp.expand(O6)))
print("  O1 - O6 =", sp.simplify(O1 - O6))
assert sp.simplify(O1 - O6) == 0
print("  => O1 == O6 IDENTICALLY (tetrad conversion), off shell and on shell, torsion or not.")
print("  P1C v1C.0.16 main.tex:2041-2043 states this in the open ('O1 and O6 are literally")
print("  the same density'); P1C:2690 Table row O6 reads '= O1 exactly (tetrad conversion)'.")
print("  The Note (main.tex:744-753) drops that clause -> disclosure regression, not new physics.")

print()
print("=" * 72)
print("C6 — parity class of O5 off shell")
print("=" * 72)
print("  O5 = eps^{mnrs} T^I_{mn} e_{I r} J5_s.")
print("  Under P: eps (tensor density) -> pseudo (odd); T, e polar (even); J5 axial (odd).")
print("  odd x even x even x odd = EVEN.  So O5 is parity-EVEN off shell as well as on shell.")
print("  => Gemini P1N-M2 is CORRECT; Claude MINOR 1's 'O5 is P-odd off shell' is FALSIFIED.")
print("  The Note's sentence is still defective, but the correct repair is: O5 is admitted by")
print("  the epsilon-CONSTRUCTION rule, not by being P-odd; the list is not strictly P-odd.")
print("  (Same wording is inherited from P1C v1C.0.16 main.tex:2096-2100.)")
print()
print("ALL ASSERTIONS PASSED.")
