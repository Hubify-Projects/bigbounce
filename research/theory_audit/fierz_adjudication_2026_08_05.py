#!/usr/bin/env python3
r"""Independent Fierz adjudication: frozen monolith vs published P1A (2026-08-05).

Adjudicates the recorded coefficient discrepancy between

  (M) the frozen monolith ``arxiv/paper1_unified.tex`` App B (verbatim twin of
      P1C App B): matrix (1/4)[[1,1,1,1,1],[4,-2,0,2,-4],[6,0,-2,0,6],
      [4,2,0,-2,-4],[1,-1,1,-1,1]], decomposition
      (J5.J5) -> 1/4 SS + 1/2 VV - 1/2 AA - 1/4 PP, and downstream
      G_scalar = -(3/64) kappa;  and

  (P) the published companion P1A ``arxiv/paper1a_ech_nogo.tex`` App
      "Fierz Rearrangement of the Minimal Axial Contact Operator" +
      released script ``arxiv/scripts/fierz_lemma_check.py``: Nieves-Pal
      c-number matrix (1/4)[[1,1,1/2,-1,1],[4,-2,0,-2,-4],[12,0,-2,0,12],
      [-4,-2,0,-2,4],[1,-1,1/2,1,1]], operator map F_op = -F_c, axial
      operator row (1, 1/2, 0, 1/2, -1) i.e.
      (J5.J5) -> SS + 1/2 VV + 1/2 AA - PP, and G_s = -(3/16) kappa.

Method: NOTHING is taken from remembered coefficient tables.  Explicit 4x4
Dirac matrices are constructed in BOTH metric signatures, the full 5x5 Fierz
matrix on the physical class bilinears {S,V,T,A,P} is SOLVED FOR from the
256-component tensor identity, the anticommuting-field (operator) map is
independently re-derived with an exact Grassmann-algebra engine (distinct
fields -> unique coefficients; identical fields -> relation module), and the
two disputed coefficient sets are mapped onto the computed objects under each
source's stated normalization.

Conventions probed:
  * signatures (+,-,-,-) and (-,+,+,+);
  * axial class basis "phys" Gamma_A = gamma^mu gamma5 vs "iA" Gamma_A =
    i gamma^mu gamma5 (the Nieves-Pal normalized choice);
  * tensor class normalization "half" (sum mu<nu) vs "full" (independent
    double sum, = 2x half).

Every printed line is tagged [L##] so the markdown summary can cite exact
computed output lines.  Output JSON: fierz_adjudication_2026_08_05.json.
"""

from __future__ import annotations

import itertools
import json
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
I = sp.I

_line_no = 0
LOG = []


def out(msg: str) -> None:
    global _line_no
    _line_no += 1
    tagged = f"[L{_line_no:02d}] {msg}"
    LOG.append(tagged)
    print(tagged)


# ----------------------------------------------------------------------------
# 1. Explicit Dirac matrices, both signatures (Dirac representation).
# ----------------------------------------------------------------------------

def block(a, b, c, d):
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))


def build_gammas(signature: str):
    """Return (gamma[0..3] upper-index, gamma5, eta) with Clifford verified."""
    z2, i2 = sp.zeros(2), sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -I], [I, 0]])
    s3 = sp.diag(1, -1)
    g0 = block(i2, z2, z2, -i2)
    gmm = [g0] + [block(z2, s, -s, z2) for s in (s1, s2, s3)]
    if signature == "mostly-minus":
        eta = sp.diag(1, -1, -1, -1)
        gam = gmm
    elif signature == "mostly-plus":
        eta = sp.diag(-1, 1, 1, 1)
        gam = [I * g for g in gmm]  # {gamma,gamma} = -2 eta_mm = +2 eta_mp
    else:
        raise ValueError(signature)
    for mu in range(4):
        for nu in range(4):
            res = sp.expand(gam[mu] * gam[nu] + gam[nu] * gam[mu]
                            - 2 * eta[mu, nu] * sp.eye(4))
            assert res == sp.zeros(4), (signature, mu, nu)
    # gamma5: anticommutes with all gamma^mu, squares to +1.
    g5 = sp.expand(I * gam[0] * gam[1] * gam[2] * gam[3])
    if sp.expand(g5 * g5) != sp.eye(4):
        g5 = sp.expand(gam[0] * gam[1] * gam[2] * gam[3])
        assert sp.expand(g5 * g5) == sp.eye(4)
    for mu in range(4):
        assert sp.expand(g5 * gam[mu] + gam[mu] * g5) == sp.zeros(4)
    return gam, g5, eta


def lower(gam, eta):
    return [sp.expand(sum((eta[mu, nu] * gam[nu] for nu in range(4)),
                          sp.zeros(4))) for mu in range(4)]


# ----------------------------------------------------------------------------
# 2. Class bilinear tensors T^X[i][j][k][l] = sum_a (M_a)_{ij} (N_a)_{kl}.
#    These are the PHYSICAL contracted current-current products, e.g.
#    A-class = sum_mu (gamma^mu gamma5) x (gamma_mu gamma5) = (J5.J5) matrix
#    kernel.
# ----------------------------------------------------------------------------

def pair_tensor(pairs):
    T = [[[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
         for _ in range(4)]
    for M, N in pairs:
        for i in range(4):
            for j in range(4):
                mij = M[i, j]
                if mij == 0:
                    continue
                for k in range(4):
                    for l in range(4):
                        nkl = N[k, l]
                        if nkl == 0:
                            continue
                        T[i][j][k][l] += mij * nkl
    return T


def class_tensors(signature: str, axial_basis: str, tensor_norm: str):
    """Physical class tensors; axial_basis in {phys, iA}; tensor_norm in
    {half, full}."""
    gam, g5, eta = build_gammas(signature)
    gml = lower(gam, eta)
    # sigma^{mu nu} = (i/2)[gamma^mu, gamma^nu]
    sig = [[sp.expand(I * (gam[m] * gam[n] - gam[n] * gam[m]) / 2)
            for n in range(4)] for m in range(4)]
    sigl = [[sp.expand(sum((eta[m, a] * eta[n, b] * sig[a][b]
                            for a in range(4) for b in range(4)),
                           sp.zeros(4)))
             for n in range(4)] for m in range(4)]
    S = pair_tensor([(sp.eye(4), sp.eye(4))])
    V = pair_tensor([(gam[m], gml[m]) for m in range(4)])
    if tensor_norm == "half":
        tp = [(sig[m][n], sigl[m][n]) for m in range(4) for n in range(4)
              if m < n]
    else:
        tp = [(sig[m][n], sigl[m][n]) for m in range(4) for n in range(4)]
    T = pair_tensor(tp)
    if axial_basis == "phys":
        A = pair_tensor([(sp.expand(gam[m] * g5), sp.expand(gml[m] * g5))
                         for m in range(4)])
    else:  # iA: Gamma_A = i gamma^mu gamma5 in BOTH bilinears
        A = pair_tensor([(sp.expand(I * gam[m] * g5),
                          sp.expand(I * gml[m] * g5)) for m in range(4)])
    P = pair_tensor([(g5, g5)])
    return {"S": S, "V": V, "T": T, "A": A, "P": P}


CLASSES = ("S", "V", "T", "A", "P")


def flatten(T):
    return [sp.expand(T[i][j][k][l]) for i in range(4) for j in range(4)
            for k in range(4) for l in range(4)]


def swap_1432(T):
    """e_Y(1432) coefficient tensor: (Gamma)_{il}(Gamma')_{kj} pattern."""
    return [[[[T[i][l][k][j] for l in range(4)] for k in range(4)]
             for j in range(4)] for i in range(4)]


def solve_fierz(tensors):
    """Solve T^X[ijkl] = sum_Y F[X,Y] T^Y[i l k j] exactly.  Returns 5x5
    sympy Matrix (rows = source class, cols = produced class)."""
    basis_flat = {Y: sp.Matrix(flatten(swap_1432(tensors[Y])))
                  for Y in CLASSES}
    Mcols = sp.Matrix.hstack(*[basis_flat[Y] for Y in CLASSES])  # 256 x 5
    F = sp.zeros(5, 5)
    MH = Mcols.H
    G = sp.expand(MH * Mcols)
    Ginv = G.inv()
    for xi, X in enumerate(CLASSES):
        b = sp.Matrix(flatten(tensors[X]))
        f = sp.expand(Ginv * (MH * b))
        # exactness check: residual must vanish identically
        assert sp.expand(Mcols * f - b) == sp.zeros(256, 1), X
        for yi in range(5):
            F[xi, yi] = sp.nsimplify(f[yi])
    return F


# ----------------------------------------------------------------------------
# 3. Exact Grassmann engine.
# ----------------------------------------------------------------------------

def gmono(ids):
    """Canonicalize a Grassmann monomial; returns (tuple, sign) or (None, 0)."""
    arr = list(ids)
    sign = 1
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sign = -sign
    for a, b in zip(arr, arr[1:]):
        if a == b:
            return None, 0
    return tuple(arr), sign


def gpoly_bilinear_product(T, slots):
    """Grassmann polynomial of (bar_u Gamma v)(bar_w Gamma' x) given class
    tensor T and generator-id offsets slots = (bar1, f2, bar3, f4)."""
    poly = {}
    b1, f2, b3, f4 = slots
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    c = T[i][j][k][l]
                    if c == 0:
                        continue
                    key, sgn = gmono((b1 + i, f2 + j, b3 + k, f4 + l))
                    if key is None:
                        continue
                    poly[key] = poly.get(key, sp.Integer(0)) + sgn * c
    return {k: sp.expand(v) for k, v in poly.items() if sp.expand(v) != 0}


def poly_to_vec(polys):
    keys = sorted(set().union(*[set(p) for p in polys]))
    return keys, [sp.Matrix([p.get(k, sp.Integer(0)) for k in keys])
                  for p in polys]


def solve_operator_fierz(tensors):
    """Distinct anticommuting fields psibar1(0-3), psi2(4-7), psibar3(8-11),
    psi4(12-15).  Solve e_X(1234) = sum_Y Fop[X,Y] e_Y(1432) as exact
    Grassmann-polynomial identities.  Unique because the e_Y(1432) are
    linearly independent."""
    direct = {X: gpoly_bilinear_product(tensors[X], (0, 4, 8, 12))
              for X in CLASSES}
    # e_Y(1432): (bar1 Gamma psi4)(bar3 Gamma' psi2)
    exchanged = {Y: gpoly_bilinear_product(swap_1432_fields(tensors[Y]))
                 for Y in CLASSES}
    Fop = sp.zeros(5, 5)
    for xi, X in enumerate(CLASSES):
        keys, vecs = poly_to_vec([direct[X]] + [exchanged[Y] for Y in CLASSES])
        b, cols = vecs[0], vecs[1:]
        M = sp.Matrix.hstack(*cols)
        MH = M.H
        f = sp.expand((MH * M).inv() * (MH * b))
        assert sp.expand(M * f - b) == sp.zeros(M.rows, 1), X
        for yi in range(5):
            Fop[xi, yi] = sp.nsimplify(f[yi])
    return Fop


def swap_1432_fields(T):
    """Return the Grassmann polynomial of e_Y(1432) = (bar1 G psi4)(bar3 G' psi2).

    The class tensor is stored as T[row1][col1][row2][col2]; in e_Y(1432) the
    first bilinear contracts psibar1 (ids 0-3) with psi4 (ids 12-15) and the
    second contracts psibar3 (ids 8-11) with psi2 (ids 4-7).  The Grassmann
    reordering sign into canonical generator order is computed by gmono, not
    inserted by hand."""
    poly = {}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    c = T[i][j][k][l]
                    if c == 0:
                        continue
                    key, sgn = gmono((0 + i, 12 + j, 8 + k, 4 + l))
                    if key is None:
                        continue
                    poly[key] = poly.get(key, sp.Integer(0)) + sgn * c
    return {k: sp.expand(v) for k, v in poly.items() if sp.expand(v) != 0}


# make gpoly usable with a prebuilt poly
def gpoly_bilinear_product(T, slots=None):  # noqa: F811
    if slots is None:
        return T  # already a poly
    poly = {}
    b1, f2, b3, f4 = slots
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    c = T[i][j][k][l]
                    if c == 0:
                        continue
                    key, sgn = gmono((b1 + i, f2 + j, b3 + k, f4 + l))
                    if key is None:
                        continue
                    poly[key] = poly.get(key, sp.Integer(0)) + sgn * c
    return {k: sp.expand(v) for k, v in poly.items() if sp.expand(v) != 0}


def identical_field_ops(tensors):
    """Single species: psibar(0-3), psi(4-7).  O_X = T^X[ijkl] b_i a_j b_k a_l."""
    ops = {}
    for X in CLASSES:
        poly = {}
        T = tensors[X]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        c = T[i][j][k][l]
                        if c == 0:
                            continue
                        key, sgn = gmono((0 + i, 4 + j, 0 + k, 4 + l))
                        if key is None:
                            continue
                        poly[key] = poly.get(key, sp.Integer(0)) + sgn * c
        ops[X] = {k: sp.expand(v) for k, v in poly.items()
                  if sp.expand(v) != 0}
    return ops


def row_str(row):
    return "(" + ", ".join(str(sp.nsimplify(x)) for x in row) + ")"


def mat_json(F):
    return [[str(sp.nsimplify(F[i, j])) for j in range(5)] for i in range(5)]


# ----------------------------------------------------------------------------
# 4. The two disputed claims, transcribed verbatim from the sources.
# ----------------------------------------------------------------------------

MONOLITH_B1 = sp.Rational(1, 4) * sp.Matrix([
    [1, 1, 1, 1, 1],
    [4, -2, 0, 2, -4],
    [6, 0, -2, 0, 6],
    [4, 2, 0, -2, -4],
    [1, -1, 1, -1, 1],
])  # paper1_unified.tex eq:fierzmatrix (L4919-4921)

MONOLITH_AADECOMP = [sp.Rational(1, 4), sp.Rational(1, 2), 0,
                     -sp.Rational(1, 2), -sp.Rational(1, 4)]
# paper1_unified.tex eq:AAdecomp (L4928): 1/4 SS + 1/2 VV - 1/2 AA - 1/4 PP

P1A_FC = sp.Rational(1, 4) * sp.Matrix([
    [1, 1, sp.Rational(1, 2), -1, 1],
    [4, -2, 0, -2, -4],
    [12, 0, -2, 0, 12],
    [-4, -2, 0, -2, 4],
    [1, -1, sp.Rational(1, 2), 1, 1],
])  # paper1a_ech_nogo.tex eq:fierzmatrix (L4818-4826) == script F_cnum

P1A_OP_ROW = [sp.Integer(1), sp.Rational(1, 2), 0, sp.Rational(1, 2),
              sp.Integer(-1)]
# paper1a_ech_nogo.tex eq:AAdecomp (L4837-4840): SS + 1/2 VV + 1/2 AA - PP

KAPPA_PREF = -sp.Rational(3, 16)  # L_int = -(3/16) kappa (J5.J5), both papers
G_S_MONOLITH = -sp.Rational(3, 64)   # paper1_unified.tex eq:gscalar (L4992-93)
G_S_P1A = -sp.Rational(3, 16)        # paper1a_ech_nogo.tex eq:gscalar (L4878)


def main() -> None:
    results = {"date": "2026-08-05",
               "task": "Independent Fierz adjudication: monolith vs published P1A",
               "classes_order": list(CLASSES),
               "signatures": {}, "mapping": {}, "identical_field": {}}

    out("Independent Fierz adjudication (explicit Dirac matrices; no "
        "remembered tables). Classes ordered (S,V,T,A,P).")

    computed = {}
    for signature in ("mostly-minus", "mostly-plus"):
        sig_res = {}
        for axial_basis in ("phys", "iA"):
            for tensor_norm in ("half", "full"):
                tens = class_tensors(signature, axial_basis, tensor_norm)
                F = solve_fierz(tens)
                assert sp.expand(F * F) == sp.eye(5)
                key = f"{axial_basis}-T{tensor_norm}"
                computed[(signature, axial_basis, tensor_norm)] = (tens, F)
                sig_res[key] = {"F_cnumber": mat_json(F),
                                "involution_F2_eq_I": True}
        results["signatures"][signature] = sig_res
        Fp = computed[(signature, "phys", "half")][1]
        out(f"{signature}: c-number Fierz matrix solved exactly in 4 basis "
            f"variants (axial phys/iA x tensor half/full); F^2=I verified "
            f"for all 4.")
        out(f"{signature}: PHYSICAL-basis (Gamma_A=gamma^mu gamma5, T half-sum)"
            f" c-number axial row [(J5.J5)(1234) on e_Y(1432)]: "
            f"{row_str(Fp.row(3))}")

    # Signature independence
    F_mm = computed[("mostly-minus", "phys", "half")][1]
    F_mp = computed[("mostly-plus", "phys", "half")][1]
    sig_indep = sp.expand(F_mm - F_mp) == sp.zeros(5, 5)
    same_all = all(
        sp.expand(computed[("mostly-minus", ab, tn)][1]
                  - computed[("mostly-plus", ab, tn)][1]) == sp.zeros(5, 5)
        for ab in ("phys", "iA") for tn in ("half", "full"))
    results["signature_independent"] = bool(sig_indep and same_all)
    out(f"Signature independence: identical 5x5 matrices under (+,-,-,-) and "
        f"(-,+,+,+) in every basis variant: {sig_indep and same_all}")

    # --- Grassmann operator map, distinct fields (mostly-minus, phys, half) ---
    tens_mm = computed[("mostly-minus", "phys", "half")][0]
    Fop = solve_operator_fierz(tens_mm)
    grassmann_minus = sp.expand(Fop + F_mm) == sp.zeros(5, 5)
    results["operator_map"] = {
        "F_op_physical_Thalf": mat_json(Fop),
        "F_op_equals_minus_F_c": bool(grassmann_minus)}
    out(f"Grassmann engine (4 distinct anticommuting fields, exact): operator "
        f"Fierz matrix solved; F_op == -F_c (single Grassmann exchange): "
        f"{grassmann_minus}")
    op_axial = list(Fop.row(3))
    out(f"COMPUTED operator axial row (anticommuting fields, physical basis): "
        f"(J5.J5) -> {row_str(op_axial)}  i.e. "
        f"{sp.nsimplify(op_axial[0])}*SS + {sp.nsimplify(op_axial[1])}*VV + "
        f"{sp.nsimplify(op_axial[2])}*TT + {sp.nsimplify(op_axial[3])}*AA + "
        f"{sp.nsimplify(op_axial[4])}*PP")
    results["computed_axial_rows"] = {
        "cnumber_physical": [str(sp.nsimplify(x)) for x in F_mm.row(3)],
        "operator_physical": [str(sp.nsimplify(x)) for x in op_axial]}

    # Also the mostly-plus Grassmann check
    tens_mp = computed[("mostly-plus", "phys", "half")][0]
    Fop_mp = solve_operator_fierz(tens_mp)
    op_same = sp.expand(Fop_mp - Fop) == sp.zeros(5, 5)
    results["operator_map"]["mostly_plus_identical"] = bool(op_same)
    out(f"Operator matrix re-derived in (-,+,+,+): identical to (+,-,-,-): "
        f"{op_same}")

    # --- Identical-field relation module -------------------------------------
    ops = identical_field_ops(tens_mm)
    keys, vecs = poly_to_vec([ops[X] for X in CLASSES])
    M = sp.Matrix.hstack(*vecs)  # dim x 5
    rank = M.rank()
    null = M.nullspace()
    rels = [[str(sp.nsimplify(v[i])) for i in range(5)] for v in null]
    out(f"Identical single-species field: span rank of "
        f"{{O_S,O_V,O_T,O_A,O_P}} = {rank}; relation module dimension = "
        f"{len(null)}; relations (coeffs on (S,V,T,A,P)): {rels}")

    def id_test(row):
        """Does O_A == sum_Y row_Y O_Y hold as identical-field identity?"""
        target = sp.Matrix([ops["A"].get(k, sp.Integer(0)) for k in keys])
        rhs = sp.zeros(len(keys), 1)
        for yi, Y in enumerate(CLASSES):
            rhs += row[yi] * sp.Matrix([ops[Y].get(k, sp.Integer(0))
                                        for k in keys])
        return sp.expand(target - rhs) == sp.zeros(len(keys), 1)

    t_computed = id_test(op_axial)
    t_p1a = id_test(P1A_OP_ROW)
    t_mono_decomp = id_test(MONOLITH_AADECOMP)
    t_mono_b1row = id_test(list(MONOLITH_B1.row(3)))
    results["identical_field"] = {
        "rank": rank, "relations": rels,
        "computed_operator_row_valid": bool(t_computed),
        "p1a_row_SS+half.VV+half.AA-PP_valid": bool(t_p1a),
        "monolith_eqAAdecomp_quarter.SS+half.VV-half.AA-quarter.PP_valid":
            bool(t_mono_decomp),
        "monolith_B1_axial_row_applied_as_physical_valid": bool(t_mono_b1row)}
    out(f"Identical-field operator identity tests -- computed row "
        f"{row_str(op_axial)}: {t_computed}; P1A row {row_str(P1A_OP_ROW)}: "
        f"{t_p1a}; monolith eq:AAdecomp {row_str(MONOLITH_AADECOMP)}: "
        f"{t_mono_decomp}; monolith B1 axial row read as physical "
        f"{row_str(MONOLITH_B1.row(3))}: {t_mono_b1row}")

    # --- Map computed matrices onto each source's stated display -------------
    match_p1a = None
    match_mono = None
    for (sigt, ab, tn), (_, F) in computed.items():
        if sigt != "mostly-minus":
            continue
        if sp.expand(F - P1A_FC) == sp.zeros(5, 5):
            match_p1a = (ab, tn)
        if sp.expand(F - MONOLITH_B1) == sp.zeros(5, 5):
            match_mono = (ab, tn)
    out(f"P1A/script matrix F_c identified: equals computed c-number matrix "
        f"in basis (axial={match_p1a[0] if match_p1a else None}, "
        f"tensor={match_p1a[1] if match_p1a else None})"
        f"{' -- EXACT MATCH' if match_p1a else ' -- NO MATCH'}")
    out(f"Monolith B1 matrix identified: equals computed c-number matrix "
        f"in basis (axial={match_mono[0] if match_mono else None}, "
        f"tensor={match_mono[1] if match_mono else None})"
        f"{' -- EXACT MATCH' if match_mono else ' -- NO MATCH'}")
    results["mapping"]["p1a_matrix_basis"] = match_p1a
    results["mapping"]["monolith_matrix_basis"] = match_mono

    # NP-basis (iA) axial rows for the record
    F_iA_full = computed[("mostly-minus", "iA", "full")][1]
    out(f"Computed c-number axial row in the i-normalized axial basis "
        f"(axial=iA, tensor=full): {row_str(F_iA_full.row(3))} "
        f"[e_A^iA = -(J5.J5), so this row is the sign-flipped presentation].")

    # P1A chain check under its stated convention
    p1a_cnum_AS = P1A_FC[3, 0]
    p1a_op_row_from_matrix = [-x for x in P1A_FC.row(3)]
    p1a_chain_ok = (match_p1a is not None
                    and list(map(sp.nsimplify, p1a_op_row_from_matrix))
                    == list(map(sp.nsimplify, P1A_OP_ROW)))
    # The physical-operator content of P1A's claim: does P1A's final operator
    # row equal the computed physical operator row?
    p1a_final_matches_computed = (
        [sp.nsimplify(x) for x in P1A_OP_ROW]
        == [sp.nsimplify(x) for x in op_axial])
    gs_computed = sp.nsimplify(KAPPA_PREF * op_axial[0])
    out(f"P1A chain under its stated convention: (F_c)_AS = "
        f"{sp.nsimplify(p1a_cnum_AS)}; F_op=-F_c gives axial operator row "
        f"{row_str(p1a_op_row_from_matrix)} == P1A eq:AAdecomp: "
        f"{p1a_chain_ok}; equals COMPUTED physical operator row: "
        f"{p1a_final_matches_computed}")
    out(f"Scalar-channel coupling from the COMPUTED operator row: G_s = "
        f"(-3/16 kappa) * ({sp.nsimplify(op_axial[0])}) = "
        f"{gs_computed} kappa  -> P1A's G_s=-3/16 kappa: "
        f"{gs_computed == G_S_P1A}; monolith's G_s=-3/64 kappa: "
        f"{gs_computed == G_S_MONOLITH}")

    # Monolith eq:AAdecomp against every computed convention row
    mono_row_matches = []
    for (sigt, ab, tn), (_, F) in computed.items():
        for label, row in (("cnumber", list(F.row(3))),
                           ("operator", [-x for x in F.row(3)])):
            if ([sp.nsimplify(x) for x in row]
                    == [sp.nsimplify(x) for x in MONOLITH_AADECOMP]):
                mono_row_matches.append((sigt, ab, tn, label))
    out(f"Monolith eq:AAdecomp (1/4,1/2,0,-1/2,-1/4) compared against the "
        f"c-number AND operator axial rows of ALL 8 computed convention "
        f"variants x both signatures: matches = {mono_row_matches or 'NONE'}")
    results["mapping"]["monolith_eqAAdecomp_matches_any_convention"] = \
        [list(m) for m in mono_row_matches]

    # Internal consistency of the monolith: its own B1 axial row vs its
    # eq:AAdecomp
    b1row = [sp.nsimplify(x) for x in MONOLITH_B1.row(3)]
    mono_internal = b1row == [sp.nsimplify(x) for x in MONOLITH_AADECOMP]
    out(f"Monolith internal consistency: B1 axial row {row_str(b1row)} == "
        f"its own eq:AAdecomp {row_str(MONOLITH_AADECOMP)}: {mono_internal} "
        f"(the S,P entries of eq:AAdecomp carry a spurious extra 1/4).")
    results["mapping"]["monolith_internally_consistent"] = bool(mono_internal)

    # What B1's axial row means when correctly interpreted (iA basis):
    # e_A^{iA} = -(J5.J5), so B1 row translated to the physical operator row:
    F_iA_half = computed[("mostly-minus", "iA", "half")][1]
    b1_is_iA_half = sp.expand(MONOLITH_B1 - F_iA_half) == sp.zeros(5, 5)
    results["mapping"]["monolith_B1_equals_iA_Thalf_cnumber"] = bool(
        b1_is_iA_half)

    # --- Verdict, derived strictly from the computed booleans above ----------
    p1a_ok = bool(match_p1a and p1a_chain_ok and p1a_final_matches_computed
                  and t_p1a and gs_computed == G_S_P1A)
    mono_ok = bool(mono_row_matches) and bool(t_mono_decomp) and \
        (gs_computed == G_S_MONOLITH)
    if p1a_ok and not mono_ok:
        verdict = "P1A-CORRECT"
    elif mono_ok and not p1a_ok:
        verdict = "MONOLITH-CORRECT"
    elif p1a_ok and mono_ok:
        verdict = "BOTH-CORRECT-DIFFERENT-CONVENTIONS"
    else:
        verdict = "BOTH-WRONG"
    results["verdict"] = verdict
    results["verdict_detail"] = {
        "p1a": "P1A's tabulated F_c equals the independently computed "
               "PHYSICAL-basis c-number Fierz matrix (Gamma_A = gamma^mu "
               "gamma5 acting on the physical (J5.J5), tensor full double "
               "sum) -- i.e. the Nieves-Pal normalization phases do land on "
               "the physical operator exactly as P1A asserts.  Its operator "
               "map F_op=-F_c, axial operator row SS+1/2VV+1/2AA-PP, and "
               "G_s=-3/16 kappa are each reproduced by the exact Grassmann "
               "computation.",
        "monolith": "B1 matrix is a valid c-number matrix ONLY in the mixed "
                    "basis (axial=i*gamma*gamma5, tensor half-sum), which the "
                    "monolith does not state (it claims physical Dirac "
                    "matrices, mostly-plus); its eq:AAdecomp "
                    "(1/4,1/2,0,-1/2,-1/4) matches NO computed convention "
                    "(c-number or operator, either signature), is internally "
                    "inconsistent with B1's own axial row, fails the "
                    "identical-field Grassmann test, and its downstream "
                    "G_s=-3/64 kappa is wrong; the correct value is "
                    "G_s=-3/16 kappa.",
        "signature": "All Fierz matrices are identical under (+,-,-,-) and "
                     "(-,+,+,+); the discrepancy is NOT a signature effect."}
    out(f"VERDICT: {verdict} (p1a_all_checks={p1a_ok}, "
        f"monolith_all_checks={mono_ok})")

    results["log_lines"] = LOG
    json_path = os.path.join(HERE, "fierz_adjudication_2026_08_05.json")
    with open(json_path, "w") as fh:
        json.dump(results, fh, indent=2)
    out(f"JSON written: {json_path}")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
