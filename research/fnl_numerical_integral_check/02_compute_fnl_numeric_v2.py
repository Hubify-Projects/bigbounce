#!/usr/bin/env python3
"""
Numerical f_NL for matter bounce — FULL Maldacena cubic action (all 6 terms).

v1 only included Term 1 (eps^2 a^2 zeta zeta'^2) and got f_NL ~ 1.56.
v2 includes ALL terms from the Maldacena cubic action at epsilon = 3/2.

The 6 terms in the cubic action (from file 02, specialized to eps=3/2):
  T1: (9/4) a^2 zeta zeta'^2
  T2: (9/4) a^2 zeta (del zeta)^2   -> in squeezed limit: -(9/4) k^2 a^2 zeta_{k1} zeta_k zeta_k
  T3: -3 a^2 zeta' (del_i zeta)(del_i chi)  -> involves constraint chi
  T4: (9/16) a^2 zeta^2 zeta'
  T5: (3/4) del^2 zeta (del chi)^2  -> involves chi^2
  T6: (9/32) del^2 zeta chi^2       -> involves chi^2

Constraint: nabla^2 chi = (3/2) a^2 zeta'
  => chi_k = -(3/2) a^2 zeta'_k / k^2 = -(3/2) eta^4 zeta'_k / k^2  (with a0=1)

Field redefinition: f_NL^FR = 5*eps/6 = 5/4 = 1.25

We work in units k=1, a0=1, M_Pl=1. f_NL is dimensionless and independent of these.
"""

import numpy as np
from scipy import integrate
import warnings
warnings.filterwarnings('ignore')


# ============================================================
# MODE FUNCTIONS (same as v1, well-tested)
# ============================================================
# ghat(x) = e^{-ix}(1 - i/x)/x^2       [dimensionless zeta mode fn]
# ghat'(x) = e^{-ix}(-i - 3/x + 3i/x^2)/x^2  [d/dx of ghat]

def ghat(x):
    return np.exp(-1j * x) * (1.0 - 1j / x) / x**2

def ghat_prime(x):
    return np.exp(-1j * x) * (-1j - 3.0 / x + 3j / x**2) / x**2

def ghat_abs2(x):
    return (1.0 + 1.0 / x**2) / x**4


# ============================================================
# SQUEEZED-LIMIT BISPECTRUM: ALL 6 TERMS
# ============================================================
#
# In the squeezed limit k1 -> 0, k2 = k3 = k, with k = 1:
# - Long mode (k1=r): superhorizon throughout, ghat(r*eta) ~ -i/(r*eta)^3
# - Short modes (k=1): exact mode functions
#
# For each Maldacena term, we need the Fourier-space vertex in the squeezed limit,
# then integrate over conformal time.
#
# The bispectrum from the in-in formula is:
#   B = sum_terms [ -2 * coeff * Im( ext * integral ) ]
# where ext = zeta*_{k1}(eta_f) zeta*_k(eta_f) zeta*_k(eta_f)
# and integral = int d(eta') [vertex integrand with mode functions]
#
# Then f_NL = (5/12) * B / (P(k1) * P(k))
#
# From file 03, the master formula gives:
#   f_NL^intr = (5/8) * [g*_{k1} g*_k g*_k * sum_I + c.c.] / [|g_{k1}|^2 |g_k|^2]
# where the (5/8) = (5/12)*(9/2)*(1/3) comes from Term 1 only.
#
# For the general case with all terms, I need to track each term's coefficient
# separately. Let me use the DIRECT ratio approach from v1, extended to all terms.
#
# In units k=1, a0=1, M_Pl=1:
#   zeta_k(eta) = ghat(k*eta) / sqrt(6*k)
#   zeta'_k(eta) = sqrt(k) * ghat'(k*eta) / sqrt(6)
#   P(k) = |ghat(k*eta_f)|^2 / (6*k)
#   a^2(eta) = eta^4
#
# The constraint variable chi:
#   chi_k = -(3/2) * eta^4 * zeta'_k / k^2
#         = -(3/2) * eta^4 * sqrt(k) * ghat'(k*eta) / (sqrt(6) * k^2)
#         = -(3/(2*k^{3/2}*sqrt(6))) * eta^4 * ghat'(k*eta)
#
# For k=1: chi_k(eta) = -(3/(2*sqrt(6))) * eta^4 * ghat'(eta)
#          = -sqrt(3/8) * eta^4 * ghat'(eta)
# For k1=r: chi_{k1}(eta) = -(3/(2*r^{3/2}*sqrt(6))) * eta^4 * ghat'(r*eta)

def compute_fnl_all_terms(squeeze_ratio=1e-3, xf=-0.01, x_early=-1000.0,
                          eps_reg=1e-4, verbose=True):
    """
    Compute f_NL including ALL 6 Maldacena cubic action terms.
    """
    r = squeeze_ratio
    eta_f = xf  # since k=1

    # Power spectra
    P_k1 = ghat_abs2(r * eta_f) / (6.0 * r)
    P_k = ghat_abs2(eta_f) / 6.0
    PP = P_k1 * P_k

    # ============================================================
    # For each term, compute B_term = -2 * coeff * Im[ext * I_term]
    # where ext = zeta*_{k1} * zeta*_k * zeta*_k at eta_f
    # and I_term = int d(eta') [vertex integrand]
    #
    # Then f_NL = (5/12) * sum(B_term) / PP
    #
    # However, the permutation structure differs for each term.
    # For the squeezed limit, I focus on the DOMINANT permutation
    # for each term (long mode undifferentiated where applicable).
    # ============================================================

    # External modes
    z1f = ghat(r * eta_f) / np.sqrt(6.0 * r)      # zeta_{k1}(eta_f)
    zkf = ghat(eta_f) / np.sqrt(6.0)                # zeta_k(eta_f)
    ext = np.conj(z1f) * np.conj(zkf)**2

    # Helper: integrate complex integrand from x_early to eta_f
    def do_integral(integrand_func):
        def re_part(eta):
            return integrand_func(eta).real
        def im_part(eta):
            return integrand_func(eta).imag
        r_val, r_err = integrate.quad(re_part, x_early, eta_f,
                                       limit=5000, epsabs=1e-14, epsrel=1e-12)
        i_val, i_err = integrate.quad(im_part, x_early, eta_f,
                                       limit=5000, epsabs=1e-14, epsrel=1e-12)
        return complex(r_val, i_val), max(abs(r_err), abs(i_err))

    damping = lambda eta: np.exp(eps_reg * eta)

    # Mode functions at internal time eta (short mode k=1, long mode k1=r)
    def z1(eta): return ghat(r * eta) / np.sqrt(6.0 * r)      # zeta_{k1}
    def zk(eta): return ghat(eta) / np.sqrt(6.0)                # zeta_k
    def z1p(eta): return np.sqrt(r) * ghat_prime(r * eta) / np.sqrt(6.0)  # zeta'_{k1}
    def zkp(eta): return ghat_prime(eta) / np.sqrt(6.0)         # zeta'_k

    # Constraint: chi_k = -(3/2) * eta^4 * zeta'_k / k^2
    def chi1(eta): return -1.5 * eta**4 * z1p(eta) / r**2       # chi_{k1}
    def chik(eta): return -1.5 * eta**4 * zkp(eta)               # chi_k (k=1)

    # ============================================================
    # TERM 1: (9/4) * a^2 * zeta * zeta'^2
    # Vertex in Fourier space: (9/4) * eta^4 * zeta_{ka} * zeta'_{kb} * zeta'_{kc}
    # Permutations: 3 (which leg is undifferentiated)
    # Dominant in squeezed: ka = k1 (long mode undiff)
    # ============================================================
    coeff_T1 = 9.0 / 4.0

    def T1_perm1(eta):  # k1 undiff, k,k diff
        return coeff_T1 * eta**4 * z1(eta) * zkp(eta)**2 * damping(eta)

    def T1_perm23(eta):  # k undiff, k1 and k diff (x2)
        return coeff_T1 * eta**4 * zk(eta) * z1p(eta) * zkp(eta) * damping(eta)

    I_T1_p1, e1 = do_integral(T1_perm1)
    I_T1_p23, e23 = do_integral(T1_perm23)
    I_T1 = I_T1_p1 + 2.0 * I_T1_p23

    # ============================================================
    # TERM 2: (9/4) * a^2 * zeta * (del zeta)^2
    # In Fourier space with k2·k3: for squeezed k1->0, k2=k3=k:
    #   k2·k3 = (k1^2 - k2^2 - k3^2)/2 = (r^2 - 2)/2 ~ -1
    # So vertex -> (9/4) * (-1) * eta^4 * zeta_{ka} * zeta_{kb} * zeta_{kc}
    # (NO derivatives on any zeta — all are position-space gradients becoming k·k)
    #
    # Permutations for this vertex: 3 (which leg is the "zeta" vs (del zeta)^2)
    # Perm 1: zeta_{k1} * (k2·k3) * zeta_k * zeta_k
    #   k2·k3 = -(k^2 + k^2 - k1^2)/2... wait, let me be more careful.
    #
    # The vertex is zeta(x) (nabla zeta(x))^2 = zeta(x) sum_i (d_i zeta)^2
    # In Fourier space:
    #   -> sum over k_a, k_b, k_c with delta(ka+kb+kc)
    #      zeta_{ka} * (-kb · kc) * zeta_{kb} * zeta_{kc}
    #      (the two nabla's act on the two zeta's in (nabla zeta)^2)
    #
    # But the vertex zeta*(nabla zeta)^2 is NOT symmetric in all 3 legs.
    # The "zeta" leg carries no momentum dot product; the other two do.
    #
    # Perm structure: choose which of k1,k2,k3 is the "plain" zeta.
    # Then the other two legs have dot product (-kb · kc).
    #
    # Perm 1 (k1 is plain zeta): factor = -k2·k3 = -(k1^2-k2^2-k3^2)/2 = (2k^2-r^2)/2 ~ k^2 = 1
    # Perm 2 (k2 is plain zeta): factor = -k1·k3
    #   k1·k3 = (k2^2-k1^2-k3^2)/2 = (k^2-r^2-k^2)/2 = -r^2/2
    #   So factor = r^2/2 ~ 0 (suppressed)
    # Perm 3 (k3 is plain zeta): same as Perm 2 by symmetry = r^2/2 ~ 0
    #
    # So only Perm 1 survives in the squeezed limit.
    # ============================================================
    coeff_T2 = 9.0 / 4.0
    k_dot = 1.0  # -k2·k3 ~ k^2 = 1 in squeezed limit with k=1

    def T2_perm1(eta):  # k1 is plain zeta, (del zeta_k)^2
        return coeff_T2 * k_dot * eta**4 * z1(eta) * zk(eta) * zk(eta) * damping(eta)

    I_T2, e_T2 = do_integral(T2_perm1)

    # ============================================================
    # TERM 3: -3 * a^2 * zeta' * (del_i zeta)(del_i chi)
    # In Fourier space:
    #   -> -3 * a^2 * zeta'_{ka} * (-kb · kc) * zeta_{kb} * chi_{kc}
    #   (or with kb <-> kc assignment)
    #
    # This vertex has 3 distinct types of legs: zeta', nabla zeta, nabla chi.
    # In Fourier space, it becomes:
    #   -3 * eta^4 * zeta'_{ka} * (kb · kc) * zeta_{kb} * chi_{kc}
    # Wait: (del_i zeta)(del_i chi) -> (-i k_b,i)(-i k_c,i) zeta_{kb} chi_{kc} = -(kb · kc) zeta_{kb} chi_{kc}
    # Hmm, actually the spatial derivatives just give momenta:
    # del_i zeta -> i*k_{b,i} * zeta_{kb} in Fourier space
    # del_i chi -> i*k_{c,i} * chi_{kc}
    # Product: -kb·kc * zeta_{kb} * chi_{kc}
    # The vertex is -3*a^2*zeta'_{ka}*(-kb·kc)*zeta_{kb}*chi_{kc}
    #            = 3*a^2*zeta'_{ka}*(kb·kc)*zeta_{kb}*chi_{kc}
    #
    # Assignment permutations: which of k1,k2,k3 is zeta', which is nabla zeta, which is nabla chi.
    # There are 3! = 6 permutations, but the vertex has (del zeta)(del chi) which is NOT
    # symmetric in zeta vs chi, so there are 3 * 2 = 6 distinct assignments.
    #
    # In the squeezed limit, dominant contributions come from assignments where the long mode
    # (k1) avoids being differentiated (if possible). But zeta' always gets a derivative...
    #
    # Let me enumerate the permutations that survive:
    # (a) ka=k1 (zeta'), kb=k2=k (nabla zeta), kc=k3=k (nabla chi):
    #     -> 3 * eta^4 * z1p(eta) * (k2·k3) * zk(eta) * chik(eta)
    #     k2·k3 ~ -k^2 = -1
    # (b) ka=k1, kb=k3, kc=k2: same by k2<->k3 symmetry
    # (c) ka=k2=k, kb=k1, kc=k3=k:
    #     -> 3 * eta^4 * zkp(eta) * (k1·k3) * z1(eta) * chik(eta)
    #     k1·k3 ~ -r^2/2 -> 0 (suppressed)
    # (d) ka=k2, kb=k3, kc=k1:
    #     -> 3 * eta^4 * zkp(eta) * (k3·k1) * zk(eta) * chi1(eta)
    #     k3·k1 ~ -r^2/2 -> 0 (suppressed)
    # (e) ka=k3=k, kb=k1, kc=k2=k:
    #     -> same as (c) by symmetry, suppressed
    # (f) ka=k3, kb=k2, kc=k1:
    #     -> same as (d) by symmetry, suppressed
    #
    # So only permutations (a) and (b) survive, giving factor of 2.
    # k2·k3 = (k1^2 - k2^2 - k3^2)/2 = (r^2 - 2)/2 ~ -1
    # ============================================================
    coeff_T3 = 3.0  # note: the -3 is in the Lagrangian, but we wrote it as -3*a^2*...
    # The vertex contribution to B is -2 * (-coeff_T3) * Im[...] = +2*3*Im[...]
    # Actually let me be careful about signs.
    # The Lagrangian has -3*a^2*zeta'*(del zeta)(del chi).
    # H_int = -L_3, so H_int has +3*a^2*zeta'*(del zeta)(del chi).
    # In-in formula: B = 2*Im[ext* * int deta' H_int * mode fns]
    # = 2*Im[ext* * int deta' * (+3) * a^2 * zeta'_{ka} * (-kb·kc) * zeta_{kb} * chi_{kc}]
    # = 2*(-3)*Im[ext* * int deta' a^2 zeta'_{k1} * (k2·k3) * zeta_k * chi_k]
    # Hmm, I need to be systematic.
    #
    # Let me just compute the integrand for all terms with the SAME sign convention.
    # B_total = -2 * sum_terms(coeff_term * Im[ext* * I_term])
    # where the coeff_term carries the sign from the Lagrangian.
    # For L_3 = sum [coeff * vertex], H_int = -L_3, and
    # B = 2 Im[ext* * (-1) * int deta' L_3] = -2 Im[ext* * sum coeff * I_term]
    #
    # So I need: B = -2 * Im[ext * sum(coeff_i * I_i)]
    # where coeff_i is the coefficient IN THE LAGRANGIAN (including sign).

    # For Term 3, L_3 has -3*a^2*zeta'*(del zeta)(del chi)
    # In Fourier space for perm (a):
    # L_3^T3 = -3 * eta^4 * z1p(eta) * (-k2·k3) * zk(eta) * chik(eta)
    # = -3 * eta^4 * z1p(eta) * (-(-1)) * zk(eta) * chik(eta)  [k2·k3 ~ -1]
    # = -3 * eta^4 * z1p(eta) * zk(eta) * chik(eta)
    # Wait: (del_i zeta)(del_i chi) in Fourier space = sum_i (ik_{b,i})(ik_{c,i}) zeta_kb chi_kc
    # = -kb·kc * zeta_kb * chi_kc
    # So the vertex is -3*a^2*zeta'_{ka}*(-kb·kc)*zeta_{kb}*chi_{kc}
    # = 3*a^2*(kb·kc)*zeta'_{ka}*zeta_{kb}*chi_{kc}
    # For perm (a), kb·kc = k2·k3 ~ -1
    # -> 3*eta^4*(-1)*z1p*zk*chik = -3*eta^4*z1p*zk*chik

    T3_kdot = -1.0  # k2·k3 in squeezed limit

    def T3_integrand(eta):
        # Contribution from perms (a)+(b): factor of 2
        # L_3^T3 = -3*a^2*zeta'*(del zeta)(del chi)
        # Fourier: 3*a^2*(kb·kc)*zeta'_{ka}*zeta_{kb}*chi_{kc}
        # For (a): ka=k1, kb=k, kc=k: 3*eta^4*(-1)*z1p*zk*chik * 2 (for a+b)
        return 2.0 * 3.0 * T3_kdot * eta**4 * z1p(eta) * zk(eta) * chik(eta) * damping(eta)

    # Hmm wait, I realize the "coeff" approach is getting confused.
    # Let me redefine: I'll compute the TOTAL CONTRIBUTION of each term to B
    # using B_term = -2 * Im[ext* * I_term], where I_term includes the Lagrangian coefficient.
    # Then f_NL = (5/12) * sum(B_term) / PP.

    # ACTUALLY: let me simplify. I'll compute:
    # B = -2 * Im[ext* * sum_terms(I_term)]
    # where I_term = int deta' [Lagrangian coefficient * vertex integrand with mode fns]
    # (including all permutations and Fourier space factors)
    #
    # Then f_NL_intrinsic = (5/12) * B / PP

    # For Term 1: L coefficient = +9/4, vertex = a^2*zeta*zeta'^2
    # I_T1 already computed above (all 3 perms)

    # For Term 2: L coefficient = +9/4, vertex = a^2*zeta*(del zeta)^2
    # In Fourier: +9/4 * a^2 * zeta_{ka} * (-kb·kc) * zeta_{kb} * zeta_{kc}
    # Perm 1 only: ka=k1, -k2·k3 ~ +1
    # I_T2 already computed above

    # For Term 3: L coefficient = -3, vertex = a^2*zeta'*(del_i zeta)(del_i chi)
    # Fourier: -3 * a^2 * zeta'_{ka} * (-kb·kc) * zeta_{kb} * chi_{kc}
    # = +3 * a^2 * (kb·kc) * zeta'_{ka} * zeta_{kb} * chi_{kc}
    # Perms (a)+(b): ka=k1, kb=k2=k, kc=k3=k + swap: 2 * 3*(k2·k3) = 2*3*(-1) = -6

    def T3_int(eta):
        # Perms a+b: 2 * (+3) * (k2·k3=-1) * eta^4 * z1p * zk * chik
        return 2.0 * 3.0 * (-1.0) * eta**4 * z1p(eta) * zk(eta) * chik(eta) * damping(eta)

    I_T3, e_T3 = do_integral(T3_int)

    # ============================================================
    # TERM 4: (9/16) * a^2 * zeta^2 * zeta'
    # (from (a^2*eps/2)*(d/deta(eps/H))*zeta^2*zeta')
    # = (a^2)(3/4)(3/4)*zeta^2*zeta' = (9/16)*a^2*zeta^2*zeta'
    #
    # This vertex has zeta*zeta*zeta'. Choose which leg is zeta'.
    # Permutations:
    #   (a) k1 is zeta': (9/16)*eta^4*z1(eta)*z1_or_zk...*z1p(eta)?
    # Wait: the vertex is zeta^2 * zeta'. In Fourier space:
    #   zeta_{ka} * zeta_{kb} * zeta'_{kc}
    # with the constraint that THIS specific form has zeta*zeta*zeta'.
    # The 3 permutations assign which of k1,k2,k3 carries the derivative.
    #
    # Perm (a): kc=k1 (zeta'_{k1}): (9/16)*eta^4*zk(eta)*zk(eta)*z1p(eta)
    # Perm (b): kc=k2 (zeta'_k): (9/16)*eta^4*z1(eta)*zk(eta)*zkp(eta)
    # Perm (c): kc=k3: same as (b) by k2<->k3 symmetry
    # ============================================================
    coeff_T4 = 9.0 / 16.0

    def T4_int(eta):
        pa = coeff_T4 * eta**4 * zk(eta) * zk(eta) * z1p(eta)
        pb = coeff_T4 * eta**4 * z1(eta) * zk(eta) * zkp(eta)
        return (pa + 2.0 * pb) * damping(eta)

    I_T4, e_T4 = do_integral(T4_int)

    # ============================================================
    # TERM 5: (3/4) * del^2 zeta * (del chi)^2
    # Fourier: (3/4) * (-k_a^2) * zeta_{ka} * (-kb·kc) * chi_{kb} * chi_{kc}
    # Wait: del^2 zeta -> -k^2 zeta in Fourier space
    # (del chi)^2 -> sum_i (del_i chi)^2 -> sum_i (ik_i chi)^2... no.
    # (del chi)^2 = (nabla chi)·(nabla chi) = sum_i (d_i chi)(d_i chi)
    # In Fourier: this is a convolution. For three-point vertex:
    # del^2 zeta(x) * [del chi(x)]^2 =
    #   int dk1 dk2 dk3 delta(k123) (-ka^2) zeta_{ka} * (-kb·kc) chi_{kb} chi_{kc}
    # Wait, that's not right either. Let me think more carefully.
    #
    # f(x) = del^2 zeta(x) = int dk (-k^2) zeta_k e^{ikx}
    # g(x) = (nabla chi(x))^2 = int dk1 dk2 (-k1·k2) chi_{k1} chi_{k2} e^{i(k1+k2)x}
    # Product: f*g = int dk dk1 dk2 (-k^2)(-(k1·k2)) zeta_k chi_{k1} chi_{k2} * delta(k+k1+k2) ...
    #
    # Hmm, the vertex del^2 zeta * (del chi)^2 is tricky because it involves
    # a product of THREE fields: zeta, chi, chi. But chi is determined by the
    # constraint chi_k = -(3/2)a^2 zeta'_k / k^2, so this is really a cubic
    # vertex in zeta (after substituting the constraint).
    #
    # In Fourier space for the three-point function:
    # del^2_x zeta(x) * nabla chi(x) · nabla chi(x)
    # When we extract the coefficient of delta(k1+k2+k3):
    # = (-k_a^2) * (k_b · k_c) * zeta_{ka} * chi_{kb} * chi_{kc}
    # where I need to consider which momentum is the "del^2 zeta" leg.
    #
    # Permutations: choose which of k1,k2,k3 is the del^2 zeta leg.
    # The other two are the (del chi) legs.
    # BUT: (del chi)^2 is symmetric in its two chi legs, so there are
    # 3 distinct permutations (not 6).
    #
    # (a) ka=k1 (del^2 zeta_{k1}): (-r^2)*(k2·k3)*z1_{chi_form}*chik(eta)^2
    #     Wait, no: del^2 zeta_{k1} -> -k1^2 * zeta_{k1} = -r^2 * z1(eta)
    #     (del chi)^2 part -> (k2·k3) * chi_{k2} * chi_{k3} = (-1)*chik(eta)^2
    #     Total: (-r^2)*(-1)*z1*chik^2 = r^2*z1*chik^2 [SUPPRESSED by r^2]
    #
    # (b) ka=k2 (del^2 zeta_k): -k^2 * zeta_k = -1 * zk(eta)
    #     (del chi) legs: k1 and k3
    #     (k1·k3) * chi_{k1} * chi_{k3}
    #     k1·k3 = (k2^2 - k1^2 - k3^2)/2 = (1-r^2-1)/2 = -r^2/2 [SUPPRESSED]
    #
    # (c) ka=k3: same as (b) by symmetry
    #
    # ALL permutations are suppressed by r^2 in the squeezed limit!
    # Term 5 is negligible.
    # ============================================================
    I_T5 = complex(0, 0)

    # ============================================================
    # TERM 6: (9/32) * del^2 zeta * chi^2
    # Fourier: (9/32) * (-ka^2) * zeta_{ka} * chi_{kb} * chi_{kc}
    # Same permutation analysis as Term 5 but without the gradient on chi.
    #
    # (a) ka=k1: (-r^2)*z1*chi_k^2 [SUPPRESSED by r^2]
    # (b) ka=k2: -1*zk*chi_{k1}*chi_k
    #     No momentum suppression! But chi_{k1} = -(3/2)*eta^4*z1p(eta)/r^2
    #     which has a 1/r^2 that could compensate...
    #     chi_{k1}*chi_k = [-(3/2)*eta^4/r^2 * z1p] * [-(3/2)*eta^4 * zkp]
    #                    = (9/4)*eta^8/(r^2) * z1p * zkp
    #     Total: (9/32)*(-1)*zk*(9/4)*eta^8/r^2*z1p*zkp
    #          = -(81/128)*eta^8/r^2*zk*z1p*zkp
    #     This has a 1/r^2 enhancement! But z1p ~ sqrt(r) * ghat'(r*eta)/sqrt(6)
    #     and for r->0: ghat'(r*eta) ~ (-3/(r*eta)^3) -> diverges.
    #     So z1p ~ sqrt(r) * (-3)/(r*eta)^3 / sqrt(6) = -3/(sqrt(6)*r^{5/2}*eta^3)
    #     chi_{k1} = -(3/2)*eta^4*z1p/r^2 = -(3/2)*eta^4*(-3/(sqrt(6)*r^{5/2}*eta^3))/r^2
    #             = (9/(2*sqrt(6)))*eta/(r^{9/2})
    #     Then chi_{k1}*chi_k ~ eta/(r^{9/2}) * eta^4*ghat'/sqrt(6) ~ O(r^{-9/2})
    #
    #     BUT: we also need to account for the power spectrum normalization.
    #     P(k1) ~ 1/(r*eta_f^4*r^2*eta_f^2) = 1/(r^3*eta_f^6) [superhorizon]
    #     So chi_{k1}^2/P(k1) is finite as r->0.
    #
    #     Actually, this gets complicated. Let me just compute it numerically
    #     and check if it's significant.
    # ============================================================

    # Perm (b) for Term 6: ka=k2=k, kb=k1, kc=k3=k
    # (9/32) * (-k^2) * zeta_k * chi_{k1} * chi_k  (and perm c gives factor 2)
    coeff_T6 = 9.0 / 32.0

    def T6_int(eta):
        # Note: NO a^2 factor here — Terms 5,6 don't have explicit a^2
        # Actually wait — from the Maldacena action, Terms 5 and 6 do NOT have
        # an explicit a^2 factor. They have epsilon/2 and epsilon/4 * (...) WITHOUT a^2.
        # But chi contains a^2 = eta^4 via the constraint, so the eta powers are different.
        #
        # Term 6 from Maldacena: (eps/4)*d(eps/H)/deta * del^2 zeta * chi^2
        # = (9/32) * del^2 zeta * chi^2
        # No explicit a^2.
        #
        # Perm b+c (×2): (9/32) * (-1) * zk * chi1 * chik * 2
        c1 = chi1(eta)
        ck = chik(eta)
        return 2.0 * coeff_T6 * (-1.0) * zk(eta) * c1 * ck * damping(eta)

    I_T6, e_T6 = do_integral(T6_int)

    # ============================================================
    # TOTAL BISPECTRUM
    # B = -2 * Im[ext* * (I_T1 + I_T2 + I_T3 + I_T4 + I_T5 + I_T6)]
    # ============================================================
    I_total = I_T1 + I_T2 + I_T3 + I_T4 + I_T5 + I_T6
    B_val = -2.0 * np.imag(ext * I_total)

    # Individual term contributions
    B_T1 = -2.0 * np.imag(ext * I_T1)
    B_T2 = -2.0 * np.imag(ext * I_T2)
    B_T3 = -2.0 * np.imag(ext * I_T3)
    B_T4 = -2.0 * np.imag(ext * I_T4)
    B_T5 = -2.0 * np.imag(ext * I_T5)
    B_T6 = -2.0 * np.imag(ext * I_T6)

    fnl_intrinsic = (5.0 / 12.0) * B_val / PP
    fnl_total = fnl_intrinsic + 5.0 / 4.0

    # Individual f_NL contributions
    fnl_T1 = (5.0 / 12.0) * B_T1 / PP
    fnl_T2 = (5.0 / 12.0) * B_T2 / PP
    fnl_T3 = (5.0 / 12.0) * B_T3 / PP
    fnl_T4 = (5.0 / 12.0) * B_T4 / PP
    fnl_T5 = (5.0 / 12.0) * B_T5 / PP
    fnl_T6 = (5.0 / 12.0) * B_T6 / PP

    if verbose:
        print(f"\n{'='*60}")
        print(f"f_NL DECOMPOSITION BY MALDACENA CUBIC ACTION TERM")
        print(f"{'='*60}")
        print(f"  Term 1 (eps^2 a^2 zeta zeta'^2):   {fnl_T1:+.6f}")
        print(f"  Term 2 (eps^2 a^2 zeta (del z)^2): {fnl_T2:+.6f}")
        print(f"  Term 3 (-2eps a^2 z'(del z)(del chi)): {fnl_T3:+.6f}")
        print(f"  Term 4 (eps/2 d(eps/H)/deta a^2 z^2 z'): {fnl_T4:+.6f}")
        print(f"  Term 5 (eps/2 del^2z (del chi)^2): {fnl_T5:+.6f}")
        print(f"  Term 6 (eps/4 d(eps/H)/deta del^2z chi^2): {fnl_T6:+.6f}")
        print(f"  {'─'*50}")
        print(f"  SUM (intrinsic):                   {fnl_intrinsic:+.6f}")
        print(f"  Field redefinition:                {5.0/4.0:+.6f}")
        print(f"  {'─'*50}")
        print(f"  TOTAL f_NL:                        {fnl_total:+.6f}")
        print(f"{'='*60}")
        print(f"\n  Targets:")
        print(f"    Cai (-35/8):  {-35/8:.6f}")
        print(f"    L-B (-35/16): {-35/16:.6f}")
        print(f"    Our result:   {fnl_total:.6f}")

        diff_cai = abs(fnl_total - (-35/8)) / abs(35/8)
        diff_lb = abs(fnl_total - (-35/16)) / abs(35/16)
        print(f"\n  Relative diff from Cai:  {diff_cai*100:.4f}%")
        print(f"  Relative diff from L-B: {diff_lb*100:.4f}%")

    return fnl_intrinsic, fnl_total


def run_convergence():
    """Test convergence of the full calculation."""
    print(f"\n{'='*60}")
    print(f"CONVERGENCE TESTS (all terms)")
    print(f"{'='*60}")

    print("\n--- eta_f independence ---")
    for xf in [-0.1, -0.05, -0.01, -0.005, -0.001]:
        _, ft = compute_fnl_all_terms(xf=xf, verbose=False)
        print(f"  xf={xf:8.4f}  f_NL={ft:.6f}")

    print("\n--- Squeeze ratio convergence ---")
    for r in [0.1, 0.01, 0.001, 0.0001]:
        _, ft = compute_fnl_all_terms(squeeze_ratio=r, verbose=False)
        print(f"  k1/k={r:.5f}  f_NL={ft:.6f}")

    print("\n--- UV cutoff convergence ---")
    for x0 in [-100, -500, -1000, -5000]:
        _, ft = compute_fnl_all_terms(x_early=x0, verbose=False)
        print(f"  x_early={x0:6d}  f_NL={ft:.6f}")

    print("\n--- iε regulator convergence ---")
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        _, ft = compute_fnl_all_terms(eps_reg=eps, verbose=False)
        print(f"  eps={eps:.0e}  f_NL={ft:.6f}")


if __name__ == "__main__":
    print("=" * 60)
    print("MATTER BOUNCE f_NL: FULL MALDACENA CUBIC ACTION")
    print("(All 6 terms, not just Term 1)")
    print("=" * 60)
    print(f"\nTargets: Cai=-35/8={-35/8}, L-B=-35/16={-35/16}")

    compute_fnl_all_terms(
        squeeze_ratio=1e-3,
        xf=-0.01,
        x_early=-1000.0,
        eps_reg=1e-4,
        verbose=True
    )

    run_convergence()

    print("\nDone.")
