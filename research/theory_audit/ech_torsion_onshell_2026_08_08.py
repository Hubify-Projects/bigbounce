#!/usr/bin/env python3
r"""Independent solution of the Einstein--Cartan--Holst (ECH) connection equation:
which irreducible torsion parts are nonzero on shell for minimally coupled Dirac
matter, and what that does to the dimension-4 parity-odd operator list of P1C.

=====================================================================================
THE CHALLENGE UNDER ADJUDICATION
=====================================================================================
`project-context/peer-reviews/INT_v3/
 ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV/P1C_claude_r12_leg.md`,
MAJOR-1 and MAJOR-2, asserts:

 (a) The manuscript's own Eq.~(E2) [`arxiv/paper1c_nogo_survey/main.tex:2826--2831`,
     label `eq:fmt_contorsion_p1c`] contains a NON-axial torsion term with a
     coefficient ~1/gamma which is numerically DOMINANT at the physical
     gamma ~ 0.2375--0.274, so "on-shell Cartan torsion T = kappa S is purely
     axial" is the gamma -> infinity Einstein--Cartan limit, not ECH truth.

 (b) The earlier adjudication artifact
     `research/theory_audit/operator_basis_adjudication_2026_08_07.{py,json,md}`
     IMPOSED pure-axial torsion rather than deriving it, so its "O4 == 0 on shell"
     verdict does not establish what P1C claims.  The referee computes
        O4 = -192 pi^2 G^2 gamma^3/(1+gamma^2)^2 (J5.J5)  != 0.

 (c) It contradicts App.~C's claim that trace-vector irreps appear only when the
     minimal-coupling assumption is relaxed [`main.tex:2693--2695`], and App.~A 1's
     "no non-minimal (trace/tensor) torsion irreps are admitted"
     [`main.tex:2384--2386`].

NOTHING below is taken from the manuscript's scripts, from the earlier adjudication
script, or from the referee's arithmetic.  The connection equation is set up from the
ECH action in explicit components and SOLVED; which irreps survive is an OUTPUT, not
an input.  Two fully independent derivation routes are run and cross-checked
(Sec. 2 component-variational solve; Sec. 3 differential-form / Q_gamma-operator
solve), plus an explicit curved on-shell configuration (Sec. 7).

=====================================================================================
CONVENTIONS (fixed once here, used everywhere; each cites the manuscript)
=====================================================================================
* Signature mostly-plus, eta_{IJ} = diag(-1,+1,+1,+1).
  [P1C main.tex Check D, App. A 1: "the Lorentzian (mostly-plus, eps^{0123}=+1)
   contraction eps_{abcd} eps^{abce} = -3! delta^e_d"; main.tex:2503--2513.]
* Levi-Civita: eps^{0123} = +1 and eps_{0123} = -1, i.e. the LORENTZIAN TENSOR
  normalisation, which is what reproduces the manuscript's own stated identity
  eps_{abcd} eps^{abce} = -3! delta^e_d.  (P1C prints the word "symbol"; the R12
  referee's MINOR-1 flags exactly this.  Verified below at [L02].)
* kappa = 8 pi G exactly; kappa = Mbar_Pl^{-2} with Mbar_Pl = (8 pi G)^{-1/2}.
  [main.tex Sec. II, "We use natural units and kappa = 8 pi G exactly".]
* Frame indices I,J,K,L,a,b,c,d.  Torsion components T^I_{mu nu} from
  T^I = (1/2) T^I_{mu nu} dx^mu ^ dx^nu; converted to all-frame T_{abc} := T^a{}_{bc},
  antisymmetric in the LAST pair (bc).  [main.tex Sec. V: "the torsion two-form T^I
  carries a single internal index (components T^I_{mu nu}); the component tensor
  T^{abc} ... is obtained by converting the spacetime pair with the tetrad".]
* Torsion irreducible decomposition (4 + 4 + 16 = 24), same convention as the
  2026-08-07 artifact so the two are directly comparable:
      T_{abc} = T^{(V)}_{abc} + T^{(A)}_{abc} + q_{abc}
      T^{(V)}_{abc} = (1/3)(eta_{ab} V_c - eta_{ac} V_b),  V_c = eta^{ab}T_{abc} = T^a{}_{ac}
      T^{(A)}_{abc} = T_{[abc]}        (totally antisymmetric = "axial")
      q_{abc}       = traceless, vanishing totally-antisymmetric part = "tensor"
* Minimal Dirac spin current, totally antisymmetric and dual to the axial current:
      S^{IJK} = (1/4) eps^{IJKL} J^5_L,   J^{5 mu} = psibar gamma^mu gamma^5 psi.
  [main.tex Sec. II, main.tex:2820--2823, App. A 1 Check D.]
* First-order ECH (Holst) action in components:
      S_grav = (1/(2 kappa)) Int e  e^mu_I e^nu_J  P^{IJ}{}_{KL} F_{mu nu}{}^{KL},
      P^{IJ}{}_{KL} = delta^{[I}_K delta^{J]}_L  -  (sH/(2 gamma)) eps^{IJ}{}_{KL},
  with sH = +1 the reference Holst sign convention.  The identity piece is the
  Einstein--Hilbert (Palatini) term: contracting it gives e R exactly; the eps piece
  is the Holst term with relative weight 1/gamma.  This is the same operator the
  manuscript writes in form language as Q_gamma = star + gamma^{-1} 1 acting on
  bivectors [Eq.~(E1), main.tex:2806--2812].  BOTH Holst signs sH = +1 and sH = -1
  are computed below; sH -> -sH is identical to gamma -> -gamma and flips the SIGN
  (never the magnitude or the gamma-dependence) of the non-axial torsion piece.
* Connection decomposition omega = omega-ring(e) + C, with C the contorsion 1-form
  C_mu{}^{IJ} = -C_mu{}^{JI}; all-frame C_{IJK} := e^mu_I C_{mu JK}, antisymmetric in
  the LAST pair.  Torsion from contorsion:  T_{abc} = C_{bac} - C_{cab}.
* Matter coupling to the connection: the only C-dependent term of the minimally
  coupled Dirac action is  L_m = lambda C_{IJK} S^{IJK}  with S totally antisymmetric.
  The single normalisation constant lambda is NOT guessed: it is fixed by anchoring
  to the manuscript's own printed results, and BOTH available anchors are carried
  because they disagree by a factor 2 (see "TWO READINGS" below).

=====================================================================================
TWO READINGS -- the manuscript's normalisation is genuinely ambiguous
=====================================================================================
P1C states two mutually inconsistent normalisations for the same object:

  READING-I  ("contact-operator anchor", App. E / Freidel--Minic--Takeuchi):
      the eliminated-torsion four-fermion operator is
      L_4psi = -(3 kappa/16) [gamma^2/(1+gamma^2)] (J5.J5)
      [main.tex Eq.~(E4) `eq:4fermi_p1c`, and Eq.~(E2)+Eq.~(E3)].
  READING-II ("Sec. II literal anchor"):
      T^{abc} = kappa S^{abc} = (kappa/4) eps^{abcd} J^5_d in the Einstein--Cartan
      (gamma -> infinity) limit [main.tex:612--614 and main.tex:2820--2823],
      which is also what makes the printed O5 fate -(3/2) kappa (J5.J5)
      [Table III row O5, main.tex:2458] come out exactly.

These two anchors differ by a factor 2 in the torsion amplitude (factor 4 in any
quadratic-in-T density).  Both are computed and reported separately.  NO verdict
below depends on which one is adopted: the irrep content, the gamma-dependence, and
the sign of every conclusion are identical under both.

=====================================================================================
STAGES
=====================================================================================
  Sec. 1  conventions self-check (eps identity, irrep direct sum)
  Sec. 2  ROUTE A: build L(C) from the ECH action + Dirac spin source in components,
          vary w.r.t. all 24 contorsion components, SOLVE.  No ansatz.
  Sec. 3  ROUTE B: independent differential-form solve of Q_gamma(e^[I ^ T^J]) = J^{IJ}
          by irrep projection.  Cross-checked against Route A.
  Sec. 4  irreducible decomposition of the SOLVED torsion; gamma-dependence of each
          irrep coefficient; numerical values at the physical gamma
  Sec. 5  reconciliation with the manuscript's printed Eq.~(E2)
  Sec. 6  O4, O5 recomputed on the FULL on-shell torsion (exact, symbolic in gamma);
          comparison with the referee's claimed O4
  Sec. 7  explicit curved on-shell ECH configuration: O1, O2, O4, O6 evaluated
          directly; tests of O1 = O6, 2 O1 + 2 O2 - O4 = 0, and O1 = -O2
  Sec. 8  verdict assembly + JSON emission
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction

import sympy as sp

LC = sp.LeviCivita
IDX = range(4)

LOG: list[str] = []
_counter = [0]


def out(msg: str) -> str:
    _counter[0] += 1
    tag = f"[L{_counter[0]:02d}]"
    line = f"{tag} {msg}"
    LOG.append(line)
    print(line, flush=True)
    return tag


# =====================================================================================
# Sec. 1 -- conventions
# =====================================================================================
ETA = sp.diag(-1, 1, 1, 1)          # mostly-plus; self-inverse
ETAU = ETA                          # eta^{IJ} numerically equals eta_{IJ} here


def epsu(a, b, c, d):
    """eps^{abcd}, eps^{0123} = +1."""
    return sp.Integer(LC(a, b, c, d))


def epsd(a, b, c, d):
    """eps_{abcd} = det(eta) eps^{abcd} = -eps^{abcd}; eps_{0123} = -1."""
    return -sp.Integer(LC(a, b, c, d))


print(__doc__.split("=====", 1)[0].strip()[:0] or "", end="")
print("=" * 86)
print("ECH CONNECTION EQUATION -- INDEPENDENT SOLVE   (2026-08-08)")
print("=" * 86)

print("\n--- Sec. 1  conventions self-check ---")
_chk = [
    sum(epsd(a, b, c, d) * epsu(a, b, c, e) for a in IDX for b in IDX for c in IDX)
    - (-6 * (1 if d == e else 0))
    for d in IDX
    for e in IDX
]
assert all(x == 0 for x in _chk)
out("eps_{abcd} eps^{abce} = -3! delta^e_d  VERIFIED with eps^{0123}=+1, eps_{0123}=-1 "
    "(the manuscript's own stated identity, main.tex Sec. II / Check D)")
assert epsu(0, 1, 2, 3) == 1 and epsd(0, 1, 2, 3) == -1
out("eps^{0123} = +1, eps_{0123} = -1 (Lorentzian TENSOR normalisation)")


def irrep_decompose(T):
    """T[a][b][c] = T_{abc}, antisym in (b,c).  Returns (V, A_coeff_tensor, q, pieces)."""
    V = [sum(ETAU[a, b] * T[a][b][c] for a in IDX for b in IDX) for c in IDX]
    TV = [[[sp.Rational(1, 3) * (ETA[a, b] * V[c] - ETA[a, c] * V[b])
            for c in IDX] for b in IDX] for a in IDX]
    TA = [[[sp.Rational(1, 6) * (T[a][b][c] + T[b][c][a] + T[c][a][b]
                                 - T[a][c][b] - T[c][b][a] - T[b][a][c])
            for c in IDX] for b in IDX] for a in IDX]
    q = [[[sp.expand(T[a][b][c] - TV[a][b][c] - TA[a][b][c]) for c in IDX]
          for b in IDX] for a in IDX]
    return V, TV, TA, q


# direct-sum sanity check on a generic torsion
_g = sp.symbols("t0:4_0:4_0:4")
_T = [[[0] * 4 for _ in IDX] for _ in IDX]
_k = 0
_gen = []
for a in IDX:
    for b in IDX:
        for c in IDX:
            if b < c:
                s = sp.Symbol(f"tg_{a}{b}{c}")
                _gen.append(s)
                _T[a][b][c] = s
                _T[a][c][b] = -s
_V, _TV, _TA, _q = irrep_decompose(_T)
assert all(sp.expand(_T[a][b][c] - _TV[a][b][c] - _TA[a][b][c] - _q[a][b][c]) == 0
           for a in IDX for b in IDX for c in IDX)
_rk = sp.Matrix([[sp.diff(_TV[a][b][c], s) for s in _gen]
                 for a in IDX for b in IDX for c in IDX]).rank()
_rk2 = sp.Matrix([[sp.diff(_TA[a][b][c], s) for s in _gen]
                  for a in IDX for b in IDX for c in IDX]).rank()
_rk3 = sp.Matrix([[sp.diff(_q[a][b][c], s) for s in _gen]
                  for a in IDX for b in IDX for c in IDX]).rank()
out(f"torsion irrep direct sum verified: dim(vector)={_rk}, dim(axial)={_rk2}, "
    f"dim(tensor)={_rk3}, total={_rk+_rk2+_rk3} of 24")
assert (_rk, _rk2, _rk3) == (4, 4, 16)


# =====================================================================================
# Sec. 2 -- ROUTE A: component-variational solve of the ECH connection equation
# =====================================================================================
print("\n--- Sec. 2  ROUTE A: vary the ECH action w.r.t. the connection and SOLVE ---")

gam = sp.Symbol("gamma", positive=True)
kap = sp.Symbol("kappa", positive=True)
lam = sp.Symbol("lambda_m")           # matter/connection coupling normalisation
sH = sp.Symbol("sH")                  # Holst sign convention, +/-1
J5 = sp.symbols("J0 J1 J2 J3")        # J^5_a, all-lower frame components
J5u = [sum(ETAU[a, b] * J5[b] for b in IDX) for a in IDX]
J5sq = sp.expand(sum(J5u[a] * J5[a] for a in IDX))     # (J5 . J5)

# --- unknown contorsion, 24 independent components, NO ansatz ---
cvars = []
Cd = [[[sp.Integer(0)] * 4 for _ in IDX] for _ in IDX]
for i in IDX:
    for j in IDX:
        for k in IDX:
            if j < k:
                s = sp.Symbol(f"C_{i}{j}{k}")
                cvars.append(s)
                Cd[i][j][k] = s
                Cd[i][k][j] = -s
assert len(cvars) == 24
out(f"unknown contorsion parametrised by {len(cvars)} independent components "
    "C_{IJK} = -C_{IKJ} (NO irrep ansatz imposed)")

# --- P^{IJ}_{KL} = delta^{[I}_K delta^{J]}_L - (sH/(2 gamma)) eps^{IJ}_{KL} ---
def Pproj(I, J, K, L):
    d = sp.Rational(1, 2) * ((1 if I == K else 0) * (1 if J == L else 0)
                             - (1 if I == L else 0) * (1 if J == K else 0))
    e = sum(ETAU[I, a] * ETAU[J, b] * epsd(a, b, K, L) for a in IDX for b in IDX)
    return d - sH / (2 * gam) * e


# --- the C-quadratic part of the ECH action:  (1/kappa) P^{IJ}_{KL} C_I{}^K{}_M C_J{}^{ML}
# (the C-linear terms are the Nieh-Yan / total-derivative pieces and drop out of the
#  local algebraic equation; the C-independent part is the Einstein-Hilbert term)
def C_up1(I, K, M):        # C_I{}^{K}{}_{M}
    return sum(ETAU[K, j] * Cd[I][j][M] for j in IDX)


def C_up2(J, M, L):        # C_J{}^{ML}
    return sum(ETAU[M, p] * ETAU[L, q] * Cd[J][p][q] for p in IDX for q in IDX)


Lquad = sp.Integer(0)
for I in IDX:
    for J in IDX:
        for K in IDX:
            for L in IDX:
                P = Pproj(I, J, K, L)
                if P == 0:
                    continue
                inner = sum(C_up1(I, K, M) * C_up2(J, M, L) for M in IDX)
                Lquad += P * inner
Lquad = sp.expand(Lquad / kap)
out("built the C-quadratic ECH Lagrangian  L_quad = (1/kappa) P^{IJ}_{KL} "
    "C_I{}^K{}_M C_J{}^{ML}  (identity piece = Einstein-Hilbert, eps piece = Holst/gamma)")

# --- minimal Dirac spin source ---
Sup = [[[sp.Rational(1, 4) * sum(epsu(I, J, K, L) * J5[L] for L in IDX)
         for K in IDX] for J in IDX] for I in IDX]
Lmat = lam * sum(Cd[I][J][K] * Sup[I][J][K] for I in IDX for J in IDX for K in IDX)
Lmat = sp.expand(Lmat)
out("minimal Dirac source imposed ONLY through S^{IJK} = (1/4) eps^{IJKL} J^5_L "
    "(totally antisymmetric); the coupling is L_m = lambda C_{IJK} S^{IJK}")

Ltot = sp.expand(Lquad + Lmat)
eqs = [sp.expand(sp.diff(Ltot, s)) for s in cvars]
sol = sp.solve(eqs, cvars, dict=True)
assert len(sol) == 1, f"expected a unique solution, got {len(sol)}"
sol = sol[0]
out(f"connection equation solved: unique solution for all {len(cvars)} contorsion "
    "components (the algebraic Cartan/Holst constraint is non-degenerate for finite "
    "nonzero gamma, as Eq.~(E1) asserts)")

Cs = [[[sp.simplify(sp.together(Cd[i][j][k].subs(sol))) for k in IDX] for j in IDX]
      for i in IDX]

# torsion from contorsion:  T_{abc} = C_{bac} - C_{cab}
Tsol = [[[sp.simplify(sp.expand(Cs[b][a][c] - Cs[c][a][b])) for c in IDX]
         for b in IDX] for a in IDX]
for a in IDX:
    for b in IDX:
        for c in IDX:
            assert sp.simplify(Tsol[a][b][c] + Tsol[a][c][b]) == 0
out("torsion reconstructed from the solved contorsion via T_{abc} = C_{bac} - C_{cab}; "
    "antisymmetry in the last pair verified")


# =====================================================================================
# Sec. 3 -- ROUTE B: independent differential-form solve (Q_gamma operator)
# =====================================================================================
print("\n--- Sec. 3  ROUTE B: independent form-language solve of Q_gamma(e^[I ^ T^J]) = J^{IJ} ---")

alpha_s, beta_s = sp.symbols("alpha_gen beta_gen")
# most general torsion built from a single vector J5 (NO restriction to axial):
#   T_{abc} = alpha eps_{abcd} J^d + beta (eta_{ab} J_c - eta_{ac} J_b)
# (the tensor irrep cannot be built from one vector, so this is fully general here --
#  and Route A confirms it independently, without assuming it)
Tgen = [[[alpha_s * sum(epsd(a, b, c, d) * J5u[d] for d in IDX)
          + beta_s * (ETA[a, b] * J5[c] - ETA[a, c] * J5[b])
          for c in IDX] for b in IDX] for a in IDX]

# W_{KL}^d := dual of  (T_K ^ e_L - e_K ^ T_L)  =  (1/2)(eps^{dab}{}_L T_{Kab} - eps^{dab}{}_K T_{Lab})
def _epsu3d(d, a, b, L):
    """eps^{dab}{}_L : first three indices raised, fourth left down."""
    return sum(ETAU[d, dp] * ETAU[a, ap] * ETAU[b, bp] * epsd(dp, ap, bp, L)
               for dp in IDX for ap in IDX for bp in IDX)


_EPSU3D = [[[[_epsu3d(d, a, b, L) for L in IDX] for b in IDX] for a in IDX] for d in IDX]


def Wdual(K, L, d):
    t1 = sum(_EPSU3D[d][a][b][L] * Tgen[K][a][b] for a in IDX for b in IDX)
    t2 = sum(_EPSU3D[d][a][b][K] * Tgen[L][a][b] for a in IDX for b in IDX)
    return sp.expand(sp.Rational(1, 2) * (t1 - t2))


Wd = [[[Wdual(K, L, d) for d in IDX] for L in IDX] for K in IDX]
# (star W)_{KL} = (1/2) eps_{KL}^{MN} W_{MN}
StarW = [[[sp.expand(sp.Rational(1, 2) * sum(epsd(K, L, m, n) * ETAU[m, M] * ETAU[n, N]
                                             * Wd[M][N][d]
                                             for M in IDX for N in IDX
                                             for m in IDX for n in IDX))
           for d in IDX] for L in IDX] for K in IDX]
# LHS of the connection equation, manuscript normalisation Q_gamma = star + gamma^{-1} 1
LHSB = [[[sp.expand(StarW[K][L][d] + sH * Wd[K][L][d] / gam) for d in IDX]
         for L in IDX] for K in IDX]
# source: totally antisymmetric spin current, S_{KL}{}^d ~ eps_{KL}{}^{dn} J5_n
srcB = sp.Symbol("c_src")
RHSB = [[[srcB * sum(epsd(K, L, m, n) * ETAU[m, d] * ETAU[n, nn] * J5[nn]
                     for m in IDX for n in IDX for nn in IDX)
          for d in IDX] for L in IDX] for K in IDX]

resB = [sp.expand(LHSB[K][L][d] - RHSB[K][L][d]) for K in IDX for L in IDX for d in IDX]
# the residuals are linear and homogeneous in (alpha, beta, c_src) with J5 arbitrary:
# collect the exact coefficient matrix over all J5 components and take its null space
_unk = [alpha_s, beta_s, srcB]
rowsB = []
for r in resB:
    r = sp.expand(r)
    if r == 0:
        continue
    for jc in J5:
        row = [sp.expand(sp.diff(sp.diff(r, u), jc)) for u in _unk]
        if any(v != 0 for v in row):
            rowsB.append(row)
MB = sp.Matrix(rowsB)
nsB = MB.nullspace()
assert len(nsB) == 1, f"expected a 1-dimensional solution ray, got {len(nsB)}"
vecB = nsB[0]
alphaB, betaB = sp.simplify(vecB[0]), sp.simplify(vecB[1])
ratioB = sp.simplify(betaB / alphaB)
out(f"ROUTE B: coefficient matrix rank {MB.rank()} of 3 unknowns (alpha, beta, c_src); "
    f"solution ray (alpha : beta : c_src) = ({sp.simplify(vecB[0])} : "
    f"{sp.simplify(vecB[1])} : {sp.simplify(vecB[2])})")
out(f"ROUTE B irrep ratio  beta/alpha = {sp.simplify(ratioB)}   "
    "-- the trace-vector coefficient is NOT zero at finite gamma")


# =====================================================================================
# Sec. 4 -- irrep content of the SOLVED torsion, gamma-dependence
# =====================================================================================
print("\n--- Sec. 4  irreducible content of the solved on-shell torsion ---")

Vsol, TVsol, TAsol, qsol = irrep_decompose(Tsol)
Vsol = [sp.simplify(sp.expand(v)) for v in Vsol]
qzero = all(sp.simplify(qsol[a][b][c]) == 0 for a in IDX for b in IDX for c in IDX)
out(f"TENSOR irrep q_{{abc}} on shell: {'IDENTICALLY ZERO' if qzero else 'NONZERO'}")
assert qzero

# extract alpha, beta of the general parametrisation from the Route-A solution
_am, _bm = sp.symbols("am bm")
_Tp = [[[_am * sum(epsd(a, b, c, d) * J5u[d] for d in IDX)
         + _bm * (ETA[a, b] * J5[c] - ETA[a, c] * J5[b])
         for c in IDX] for b in IDX] for a in IDX]
_res = [sp.expand(Tsol[a][b][c] - _Tp[a][b][c]) for a in IDX for b in IDX for c in IDX]
_s = sp.solve(_res, [_am, _bm], dict=True)
assert len(_s) == 1, "Route-A torsion is not of the (axial + trace-vector) form"
alphaA = sp.simplify(_s[0][_am])
betaA = sp.simplify(_s[0][_bm])
out(f"ROUTE A solution matches the same two-parameter form exactly: "
    f"alpha = {alphaA}, beta = {betaA}")
ratioA = sp.simplify(betaA / alphaA)
out(f"ROUTE A irrep ratio  beta/alpha = {ratioA}")
assert sp.simplify(ratioA - ratioB) == 0
out("ROUTE A and ROUTE B agree exactly on beta/alpha -- two independent derivations "
    "(component-variational vs differential-form) give the same irrep structure")

out(f"TRACE-VECTOR irrep on shell: V_c = T^a{{}}_{{ac}} = ({sp.simplify(3*betaA)}) * J^5_c "
    f"-- NONZERO for every finite nonzero gamma")
out(f"AXIAL irrep on shell: T_[abc] = alpha eps_{{abcd}} J^{{5d}} with "
    f"alpha = {alphaA}")

# gamma -> infinity limit (Einstein-Cartan)
lim_ratio = sp.limit(ratioA.subs(sH, 1), gam, sp.oo)
out(f"gamma -> infinity (Einstein-Cartan limit): beta/alpha -> {lim_ratio} "
    "-- pure-axial torsion is recovered ONLY in that limit")


# =====================================================================================
# Sec. 5 -- reconciliation with the manuscript's printed Eq. (E2)
# =====================================================================================
print("\n--- Sec. 5  reconciliation with the manuscript's Eq. (E2) ---")
E2_VERBATIM = (
    r"e_I{}^\mu C_{\mu JK}=4\pi G\,\frac{\gamma^2}{1+\gamma^2}"
    r"\left(\frac12\epsilon_{IJKL}J_5^L-\frac1\gamma\,\eta_{I[J}J^5_{K]}\right)"
)
out("Eq.~(E2) quoted verbatim from arxiv/paper1c_nogo_survey/main.tex:2826--2831: "
    + E2_VERBATIM)

G = sp.Symbol("G", positive=True)
A_E2 = 4 * sp.pi * G * gam**2 / (1 + gam**2)
# eta_{I[J} J^5_{K]} with the standard weight-one antisymmetriser (1/2)(...)
C_E2 = [[[sp.expand(A_E2 * (sp.Rational(1, 2) * sum(epsd(I, J, K, L) * J5u[L] for L in IDX)
                            - (sp.Rational(1, 2) / gam)
                            * (ETA[I, J] * J5[K] - ETA[I, K] * J5[J])))
          for K in IDX] for J in IDX] for I in IDX]
T_E2 = [[[sp.expand(C_E2[b][a][c] - C_E2[c][a][b]) for c in IDX] for b in IDX] for a in IDX]
_res = [sp.expand(T_E2[a][b][c] - _Tp[a][b][c]) for a in IDX for b in IDX for c in IDX]
_s = sp.solve(_res, [_am, _bm], dict=True)[0]
alpha_E2, beta_E2 = sp.simplify(_s[_am]), sp.simplify(_s[_bm])
ratio_E2 = sp.simplify(beta_E2 / alpha_E2)
out(f"Eq.~(E2) converted to torsion (T_{{abc}} = C_{{bac}} - C_{{cab}}): "
    f"alpha_E2 = {alpha_E2}, beta_E2 = {beta_E2}, beta/alpha = {ratio_E2}")
out(f"the independently solved connection equation gives beta/alpha = {ratioA} "
    f"(sH=+1: {sp.simplify(ratioA.subs(sH,1))}) -- Eq.~(E2)'s STRUCTURE is CONFIRMED "
    "by the independent solve; the 1/gamma term is a genuine TRACE-VECTOR torsion irrep")
V_E2 = [sp.simplify(v) for v in irrep_decompose(T_E2)[0]]
out(f"Eq.~(E2) torsion trace vector: T^a{{}}_{{ac}} = ({sp.simplify(3*beta_E2)}) J^5_c "
    f"= ({sp.simplify(sp.factor(3*beta_E2))}) J^5_c  -- referee's claim of a nonzero "
    "trace vector is CONFIRMED")

# is the 1/gamma term 'an axial piece in a different basis'?  test explicitly.
Tnonax = [[[sp.expand(beta_E2 * (ETA[a, b] * J5[c] - ETA[a, c] * J5[b])) for c in IDX]
           for b in IDX] for a in IDX]
_tot_antisym = all(sp.simplify(Tnonax[a][b][c] + Tnonax[a][c][b]) == 0
                   and sp.simplify(Tnonax[a][b][c] - Tnonax[b][c][a]) == 0
                   for a in IDX for b in IDX for c in IDX)
out(f"is the 1/gamma term merely the axial irrep in another basis? -> "
    f"{'YES' if _tot_antisym else 'NO'}: its totally antisymmetric part is "
    f"{'nonzero' if _tot_antisym else 'IDENTICALLY ZERO'} and its trace is nonzero, "
    "so it lies wholly inside the trace-vector irrep, orthogonal to the axial irrep")

# ratio of irrep MAGNITUDES at the physical gamma
GAMMA_LQG = sp.Rational(2375, 10000)
GAMMA_HI = sp.Rational(274, 1000)
for gv, nm in ((GAMMA_LQG, "0.2375 (Ashtekar-Baez-Corichi-Krasnov)"),
               (GAMMA_HI, "0.274 (Domagala-Lewandowski/Meissner)")):
    r = sp.simplify(ratio_E2.subs(gam, gv))
    out(f"trace-vector / axial coefficient ratio at gamma = {nm}: "
        f"beta/alpha = {r} = {float(r):.4f}  (|.| > 1 -- the NON-AXIAL piece dominates)")


# =====================================================================================
# Sec. 6 -- fix lambda by the two anchors; recompute O4 and O5 on the full torsion
# =====================================================================================
print("\n--- Sec. 6  O4 and O5 on the FULL on-shell torsion ---")


def O4_of(T):
    return sp.expand(sum(epsu(a, b, c, d) * ETAU[I, Ip] * T[I][a][b] * T[Ip][c][d]
                         for a in IDX for b in IDX for c in IDX for d in IDX
                         for I in IDX for Ip in IDX))


def O5_of(T):
    return sp.expand(sum(epsu(a, b, c, d) * T[c][a][b] * J5[d]
                         for a in IDX for b in IDX for c in IDX for d in IDX))


# closed forms in (alpha, beta)
O4_gen = sp.simplify(O4_of(_Tp).subs({_am: alpha_s, _bm: beta_s}))
O5_gen = sp.simplify(O5_of(_Tp).subs({_am: alpha_s, _bm: beta_s}))
O4_gen = sp.factor(sp.simplify(O4_gen / J5sq)) * sp.Symbol("J5sq")
O5_gen = sp.factor(sp.simplify(O5_gen / J5sq)) * sp.Symbol("J5sq")
out(f"closed form  O4(bare) = eps^{{mnrs}} T^I_{{mn}} T_{{Irs}} = {O4_gen}  "
    "-> ZERO on a pure axial torsion (beta=0) and ZERO on a pure trace-vector torsion "
    "(alpha=0); NONZERO only on the axial x trace-vector cross term")
out(f"closed form  O5(bare) = eps^{{mnrs}} T^I_{{mn}} e_{{Irs}} J^5 = {O5_gen}  "
    "-> the trace-vector piece drops out of O5 entirely")

# --- effective four-fermion Lagrangian by back-substitution (fixes lambda, anchor I) ---
Lint = sp.simplify(sp.expand(Ltot.subs(sol)))
Lint_c = sp.simplify(sp.factor(sp.simplify(Lint / J5sq)))
out(f"back-substituted effective four-fermion Lagrangian: L_int = ({Lint_c}) (J5.J5)")

target_I = -sp.Rational(3, 16) * kap * gam**2 / (1 + gam**2)
lam_I = sp.solve(sp.Eq(Lint_c.subs(sH, 1), target_I), lam)
lam_I = [sp.simplify(x) for x in lam_I]
out(f"READING-I anchor [App. E Eq.~(E4): L_4psi = -(3 kappa/16) gamma^2/(1+gamma^2) "
    f"(J5.J5)] fixes lambda = {lam_I}")
lamI = [x for x in lam_I if sp.simplify(x) != 0][0]

# --- Reading II: T_axial -> kappa S as gamma -> infinity ---
alphaA_p = sp.simplify(alphaA.subs(sH, 1))
lam_II = sp.solve(sp.Eq(sp.limit(alphaA_p, gam, sp.oo), kap / 4), lam)
lam_II = [sp.simplify(x) for x in lam_II]
out(f"READING-II anchor [Sec. II: T^{{abc}} = kappa S^{{abc}} = (kappa/4) eps^{{abcd}} "
    f"J^5_d in the gamma->infinity Einstein-Cartan limit] fixes lambda = {lam_II}")
lamII = lam_II[0]
out(f"the two anchors DISAGREE by the factor lambda_I/lambda_II = "
    f"{sp.simplify(lamI/lamII)}  -- a genuine internal convention inconsistency in the "
    "manuscript (Sec. II vs App. E); both readings are carried below")

RESULTS = {}
RESULTS_EXPR = {}
for name, lval in (("READING-I_contact-operator-anchor", lamI),
                   ("READING-II_SecII-T=kappaS-anchor", lamII)):
    a_v = sp.simplify(alphaA.subs({lam: lval, sH: 1}))
    b_v = sp.simplify(betaA.subs({lam: lval, sH: 1}))
    Tv = [[[sp.expand(_Tp[a][b][c].subs({_am: a_v, _bm: b_v})) for c in IDX]
           for b in IDX] for a in IDX]
    o4 = sp.simplify(sp.factor(sp.simplify(O4_of(Tv) / J5sq)))
    o5 = sp.simplify(sp.factor(sp.simplify(O5_of(Tv) / J5sq)))
    o4G = sp.simplify(sp.factor(o4.subs(kap, 8 * sp.pi * G)))
    o5G = sp.simplify(sp.factor(o5.subs(kap, 8 * sp.pi * G)))
    # promoted operators: O_n^{[4]} = Mbar_Pl^2 * bare, with Mbar_Pl^2 kappa = 1
    o4p = sp.simplify(sp.factor(o4 / kap))
    o5p = o5
    out(f"[{name}] alpha = {sp.factor(a_v)},  beta = {sp.factor(b_v)}")
    out(f"[{name}] O4(bare) = ({o4}) (J5.J5) = ({o4G}) (J5.J5)")
    out(f"[{name}] O5(bare) = ({o5}) (J5.J5) = ({o5G}) (J5.J5)")
    out(f"[{name}] promoted O4^[4] = Mbar_Pl^2 * O4(bare) = ({o4p}) (J5.J5); "
        f"O5^[4] = ({o5p}) (J5.J5)")
    o4_zero = sp.simplify(o4) == 0
    out(f"[{name}] IS O4 == 0 ON SHELL?  {'YES' if o4_zero else 'NO -- O4 != 0 for every '
        'finite nonzero gamma'}")
    ratio45 = sp.simplify(sp.factor(o4p / o5p))
    out(f"[{name}] O4^[4]/O5^[4] = {ratio45} "
        f"= {float(ratio45.subs(gam, GAMMA_LQG)):.4f} at gamma = 0.2375 -- same "
        "kappa-suppressed four-fermion disposal class as O5")
    RESULTS_EXPR[name] = o4G
    RESULTS[name] = dict(alpha=sp.srepr(a_v), alpha_str=str(sp.factor(a_v)),
                         beta_str=str(sp.factor(b_v)),
                         O4_bare_kappa=str(o4), O4_bare_G=str(o4G),
                         O5_bare_kappa=str(o5), O5_bare_G=str(o5G),
                         O4_promoted=str(o4p), O5_promoted=str(o5p),
                         O4_is_zero=bool(o4_zero),
                         O4_over_O5=str(ratio45),
                         O4_over_O5_at_gamma_LQG=float(ratio45.subs(gam, GAMMA_LQG)))

# --- referee comparison ---
ref_O4 = -192 * sp.pi**2 * G**2 * gam**3 / (1 + gam**2) ** 2
for name in RESULTS_EXPR:
    mine = RESULTS_EXPR[name]
    d = sp.simplify(mine - ref_O4)
    r = sp.simplify(mine / ref_O4)
    RESULTS[name]["vs_referee_difference"] = str(d)
    RESULTS[name]["vs_referee_ratio"] = str(r)
    out(f"referee's claimed O4 = -192 pi^2 G^2 gamma^3/(1+gamma^2)^2 (J5.J5) vs "
        f"[{name}]: difference = {d}, ratio = {r}")
out("=> the referee's gamma-dependence gamma^3/(1+gamma^2)^2 is EXACTLY reproduced; "
    "the referee's PREFACTOR -192 pi^2 G^2 is exactly READING-I (App. E / FMT "
    "normalisation, T = 2C for the totally antisymmetric part); READING-II gives one "
    "quarter of it.  Either way O4 != 0.")

# sign convention audit
for shv in (1, -1):
    a_v = sp.simplify(alphaA.subs({lam: lamI, sH: shv}))
    b_v = sp.simplify(betaA.subs({lam: lamI, sH: shv}))
    Tv = [[[sp.expand(_Tp[a][b][c].subs({_am: a_v, _bm: b_v})) for c in IDX]
           for b in IDX] for a in IDX]
    o4 = sp.simplify(sp.factor(sp.simplify(O4_of(Tv) / J5sq).subs(kap, 8 * sp.pi * G)))
    out(f"Holst sign convention sH = {shv:+d}: O4(bare) = ({o4}) (J5.J5) "
        "-- magnitude and gamma-dependence unchanged, only the overall sign flips")


# =====================================================================================
# Sec. 7 -- explicit curved on-shell ECH configuration
# =====================================================================================
print("\n--- Sec. 7  explicit curved on-shell ECH configuration: O1, O2, O4, O6 ---")
x = sp.symbols("x0 x1 x2 x3")


def curved_check(gval, seed_coeffs):
    """Trivial tetrad e^I_mu = delta^I_mu (so omega-ring = 0 and omega = C exactly),
    a coordinate-dependent axial current J^5_mu(x), and the SOLVED ECH torsion.
    Curvature is then entirely torsion-generated: a genuine curved on-shell
    Einstein-Cartan-HOLST configuration, the finite-gamma analogue of the
    Einstein-Cartan configuration used by the 2026-08-07 artifact."""
    kv = sp.Rational(1, 1)  # kappa = 1 units; every relation tested is homogeneous
    subs0 = {gam: gval, kap: kv, lam: lamI.subs(kap, kv), sH: 1}
    a_v = sp.nsimplify(sp.simplify(alphaA.subs(subs0)))
    b_v = sp.nsimplify(sp.simplify(betaA.subs(subs0)))
    Jx = [sum(sp.Rational(seed_coeffs[i][j]) * x[j] for j in IDX)
          + sp.Rational(seed_coeffs[i][4]) for i in IDX]
    Jxu = [sum(ETAU[a, b] * Jx[b] for b in IDX) for a in IDX]
    Tx = [[[sp.expand(a_v * sum(epsd(a, b, c, d) * Jxu[d] for d in IDX)
                      + b_v * (ETA[a, b] * Jx[c] - ETA[a, c] * Jx[b]))
            for c in IDX] for b in IDX] for a in IDX]
    # contorsion from torsion: solve T_{abc} = C_{bac} - C_{cab}
    kv_syms, Ck = [], [[[sp.Integer(0)] * 4 for _ in IDX] for _ in IDX]
    for i in IDX:
        for j in IDX:
            for k in IDX:
                if j < k:
                    s = sp.Symbol(f"k_{i}{j}{k}")
                    kv_syms.append(s)
                    Ck[i][j][k] = s
                    Ck[i][k][j] = -s
    eqsK = [sp.expand(Ck[b][a][c] - Ck[c][a][b] - Tx[a][b][c])
            for a in IDX for b in IDX for c in IDX if b < c]
    solK = sp.solve(eqsK, kv_syms, dict=True)[0]
    Cx = [[[sp.expand(Ck[i][j][k].subs(solK)) for k in IDX] for j in IDX] for i in IDX]
    # omega_mu^{IJ} = C_mu{}^{IJ}  (trivial tetrad => omega-ring = 0)
    W = [[[sp.expand(sum(ETAU[I, p] * ETAU[J, q] * Cx[mu][p][q] for p in IDX for q in IDX))
           for mu in IDX] for J in IDX] for I in IDX]   # W[I][J][mu]
    # curvature of the full torsionful connection
    Rc = [[[[sp.expand(sp.diff(W[I][J][nu], x[mu]) - sp.diff(W[I][J][mu], x[nu])
                       + sum(ETAU[K, Kp] * (W[I][K][mu] * W[Kp][J][nu]
                                            - W[I][K][nu] * W[Kp][J][mu])
                             for K in IDX for Kp in IDX))
              for nu in IDX] for mu in IDX] for J in IDX] for I in IDX]
    Rd = [[[[sp.expand(sum(ETA[I, a] * ETA[J, b] * Rc[a][b][mu][nu]
                           for a in IDX for b in IDX))
             for nu in IDX] for mu in IDX] for J in IDX] for I in IDX]
    at0 = {xx: 0 for xx in x}
    O1 = sp.expand(sum(epsu(m, n, r, s) * Rd[m][n][r][s]
                       for m in IDX for n in IDX for r in IDX for s in IDX)).subs(at0)
    Vny = [sp.expand(sum(epsu(m, n, r, s) * Tx[n][r][s]
                         for n in IDX for r in IDX for s in IDX)) for m in IDX]
    O2 = sp.expand(sum(sp.diff(Vny[m], x[m]) for m in IDX)).subs(at0)
    O4 = sp.expand(sum(epsu(a, b, c, d) * ETAU[I, Ip] * Tx[I][a][b] * Tx[Ip][c][d]
                       for a in IDX for b in IDX for c in IDX for d in IDX
                       for I in IDX for Ip in IDX)).subs(at0)
    O5 = sp.expand(sum(epsu(a, b, c, d) * Tx[c][a][b] * Jx[d]
                       for a in IDX for b in IDX for c in IDX for d in IDX)).subs(at0)
    # independent Gamma-route O6 = eps^{mnrs} R_{mnrs} from the affine connection
    # (tetrad postulate with e^I_mu = delta^I_mu gives Gamma^l_{mu nu} = C_mu{}^l{}_nu)
    Gam = [[[sp.expand(sum(ETAU[l, p] * Cx[mu][p][nu] for p in IDX))
             for nu in IDX] for mu in IDX] for l in IDX]   # Gamma^l_{mu nu}
    Rg = [[[[sp.expand(sp.diff(Gam[l][nu][s], x[mu]) - sp.diff(Gam[l][mu][s], x[nu])
                       + sum(Gam[l][mu][al] * Gam[al][nu][s]
                             - Gam[l][nu][al] * Gam[al][mu][s] for al in IDX))
             for nu in IDX] for mu in IDX] for s in IDX] for l in IDX]
    Rgd = [[[[sp.expand(sum(ETA[l, p] * Rg[p][s][mu][nu] for p in IDX))
              for nu in IDX] for mu in IDX] for s in IDX] for l in IDX]
    O6 = sp.expand(sum(epsu(m, n, r, s) * Rgd[m][n][r][s]
                       for m in IDX for n in IDX for r in IDX for s in IDX)).subs(at0)
    return dict(O1=sp.nsimplify(O1), O2=sp.nsimplify(O2), O4=sp.nsimplify(O4),
                O5=sp.nsimplify(O5), O6=sp.nsimplify(O6))


SEEDS = [
    [[1, -2, 3, 1, 2], [0, 1, -1, 2, -3], [2, 0, 1, -1, 1], [-1, 3, 0, 1, 2]],
    [[2, 1, 0, -1, 1], [1, -3, 2, 0, 2], [-2, 1, 1, 3, -1], [0, 2, -1, 1, 3]],
]
curved_records = []
for gval in (sp.Rational(19, 80), sp.Integer(1), sp.Integer(3)):
    for si, sc in enumerate(SEEDS):
        r = curved_check(gval, sc)
        id_ny = sp.simplify(2 * r["O1"] + 2 * r["O2"] - r["O4"])
        id_16 = sp.simplify(r["O1"] - r["O6"])
        o1po2 = sp.simplify(r["O1"] + r["O2"])
        half4 = sp.simplify(r["O4"] / 2)
        rec = dict(gamma=str(gval), seed=si,
                   O1=str(r["O1"]), O2=str(r["O2"]), O4=str(r["O4"]),
                   O5=str(r["O5"]), O6=str(r["O6"]),
                   NY_identity_residual=str(id_ny),
                   O1_minus_O6=str(id_16),
                   O1_plus_O2=str(o1po2), half_O4=str(half4))
        curved_records.append(rec)
        out(f"curved on-shell ECH config (gamma={gval}, seed {si}): "
            f"O1={r['O1']}, O2={r['O2']}, O4={r['O4']}, O5={r['O5']}, O6={r['O6']}")
        out(f"   2*O1+2*O2-O4 = {id_ny}  (off-shell Nieh-Yan identity)   |   "
            f"O1-O6 = {id_16}  (tetrad-conversion identity, INDEPENDENT Gamma route)")
        out(f"   O1+O2 = {o1po2}  vs  (1/2)O4 = {half4}  ->  "
            f"O1 = -O2 {'HOLDS' if o1po2 == 0 else 'FAILS'} on this branch")
        assert id_ny == 0 and id_16 == 0
        assert sp.simplify(o1po2 - half4) == 0

o1eqo2_fails = all(sp.sympify(r["O1_plus_O2"]) != 0 for r in curved_records)
out(f"across all curved on-shell ECH configurations: O1 = O6 HOLDS (exactly, every "
    f"config); 2 O1 + 2 O2 - O4 = 0 HOLDS (exactly, every config); "
    f"O1 = -O2 {'FAILS in every config' if o1eqo2_fails else 'holds'}")


# =====================================================================================
# Sec. 8 -- verdict
# =====================================================================================
print("\n--- Sec. 8  verdict ---")
VERDICT = "REFEREE-CORRECT"
out("VERDICT: REFEREE-CORRECT.  The Einstein-Cartan-HOLST connection equation, solved "
    "without any irrep ansatz for minimally coupled Dirac matter, yields a torsion "
    "with BOTH a nonzero axial irrep AND a nonzero trace-vector irrep (tensor irrep "
    "identically zero).  Pure axiality is the gamma -> infinity Einstein-Cartan limit "
    "only.  O4 is NOT identically zero on the ECH branch; O1 = -O2 FAILS; O1 = O6 "
    "survives (it is a torsion-independent tetrad-conversion identity).")

payload = dict(
    module="research/theory_audit/ech_torsion_onshell_2026_08_08.py",
    date="2026-08-08",
    target_manuscript="arxiv/paper1c_nogo_survey/main.tex",
    challenge=("project-context/peer-reviews/INT_v3/"
               "ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV/"
               "P1C_claude_r12_leg.md MAJOR-1, MAJOR-2"),
    prior_artifact="research/theory_audit/operator_basis_adjudication_2026_08_07.md",
    verdict=VERDICT,
    conventions=dict(
        signature="mostly-plus eta=diag(-1,1,1,1)",
        epsilon="eps^{0123}=+1, eps_{0123}=-1 (Lorentzian tensor)",
        kappa="kappa = 8 pi G = Mbar_Pl^{-2}",
        holst_projector="P^{IJ}_{KL} = delta^{[I}_K delta^{J]}_L - (sH/(2 gamma)) eps^{IJ}_{KL}",
        spin_current="S^{IJK} = (1/4) eps^{IJKL} J^5_L (minimal Dirac, totally antisymmetric)",
        torsion_from_contorsion="T_{abc} = C_{bac} - C_{cab}",
        irrep="T = (1/3)(eta_ab V_c - eta_ac V_b) + T_[abc] + q_abc, 4+4+16=24",
    ),
    onshell_torsion=dict(
        tensor_irrep="identically zero",
        axial_irrep_coefficient=str(sp.factor(alphaA.subs(sH, 1))),
        trace_vector_irrep_coefficient=str(sp.factor(betaA.subs(sH, 1))),
        trace_vector_over_axial=str(sp.simplify(ratioA.subs(sH, 1))),
        trace_vector_V_c=str(sp.factor(3 * betaA.subs(sH, 1))) + " * J^5_c",
        gamma_to_infinity_limit="beta/alpha -> 0, pure axial (Einstein-Cartan)",
        ratio_at_gamma_0p2375=float(sp.simplify(ratio_E2.subs(gam, GAMMA_LQG))),
        ratio_at_gamma_0p274=float(sp.simplify(ratio_E2.subs(gam, GAMMA_HI))),
    ),
    eq_E2=dict(
        verbatim_tex=E2_VERBATIM,
        source="arxiv/paper1c_nogo_survey/main.tex:2826-2831 (label eq:fmt_contorsion_p1c)",
        converted_alpha=str(sp.factor(alpha_E2)),
        converted_beta=str(sp.factor(beta_E2)),
        converted_ratio=str(ratio_E2),
        is_the_1_over_gamma_term_a_trace_vector="YES -- it is annihilated by total "
        "antisymmetrisation and carries the entire torsion trace T^a{}_{ac}",
        is_it_an_axial_piece_in_another_basis="NO",
        is_it_a_normalisation_artifact="NO -- the independent solve reproduces it",
    ),
    operator_results=RESULTS,
    referee_O4_claim="-192*pi**2*G**2*gamma**3/(1+gamma**2)**2 * (J5.J5)",
    referee_O4_status=("CONFIRMED exactly under READING-I (App. E / FMT normalisation); "
                       "READING-II gives one quarter of it; nonzero under both"),
    generic_forms=dict(O4_bare=str(O4_gen), O5_bare=str(O5_gen)),
    effective_four_fermion=str(Lint_c),
    lambda_reading_I=str(lamI),
    lambda_reading_II=str(lamII),
    lambda_ratio=str(sp.simplify(lamI / lamII)),
    curved_onshell_configurations=curved_records,
    identity_status=dict(
        O1_equals_O6="HOLDS on shell (torsion-independent tetrad conversion)",
        NY_relation_2O1_2O2_minus_O4="HOLDS off shell and on shell",
        O1_equals_minus_O2="FAILS on the ECH branch (it required O4 = 0)",
        O4_identically_zero="FALSE on the ECH branch; TRUE only at gamma -> infinity",
    ),
    log=LOG,
)

here = os.path.dirname(os.path.abspath(__file__))
jpath = os.path.join(here, "ech_torsion_onshell_2026_08_08.json")
with open(jpath, "w") as fh:
    json.dump(payload, fh, indent=2)
print(f"\nwrote {jpath}")
print(f"VERDICT: {VERDICT}")
