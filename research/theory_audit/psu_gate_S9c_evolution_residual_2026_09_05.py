#!/usr/bin/env python3
"""paper-su gate S9c (2026-09-05): does the shift-divergence term explain the 5(6-eps)/24 gap
between the delta-N lane's uniform-density value 5(eps-7)/8 (= -55/16 at dust) and the second-order
threading map's rho-slice value 5(2eps-15)/24 (= -5/2)?

Part A (this file, numerics): an independent exact separate-universe integration of a constant-eps
scalar-field contraction (V = V0 exp(-lam*phi), lam = sqrt(2 eps)), growing-mode initial data on a
flat initial slice, e-fold number read on (i) the comoving (phi) slice and (ii) the uniform-density
(rho) slice; f_NL = (5/6) N2/N1^2 of the e-fold variable itself, initial-position label by construction.
Part B (sympy): the same to second order in closed form, general eps.
Run: python3 psu_gate_S9c_evolution_residual_2026_09_05.py  -> json next to it.
"""
import json, hashlib, os, sys, time
import mpmath as mp

mp.mp.dps = 30   # (mpmath only for the tidy rationals; the ODE cross-check is float64)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'psu_gate_S9c_evolution_residual_2026_09_05.json')

# ---- separate universe in N-time, flat scalar-only: x = phidot/(sqrt6 H), y^2 = 1 - x^2 ----
def G(x, lam):
    """dx/dN for the scalar-only flat universe (Copeland-Liddle-Wands, gamma-fluid term absent)."""
    return -3*x + mp.sqrt(6)/2*lam*(1 - x*x) + 3*x**3

def su_efolds(eps, A, dN, slice_kind):
    """E-fold count from the flat initial slice (N=0, ln|H_i| = 0 on the background) to the final slice,
    for a worldline whose initial data sit at amplitude A along the pure growing eigenvector of the
    linearised system: (dx, dlnH) = (1, v) A, v = 6 x*/(3-eps).  dN>0 is the background e-fold span
    (contraction: N runs 0 -> -dN).  slice_kind: 'rho' (uniform |H|) or 'phi' (comoving).
    The slice condition is used as the independent variable, so the crossing is exact (no root find).
    float64 + DOP853 at rtol 1e-13; used only as a finite-W cross-check of the closed form of Part B."""
    from scipy.integrate import solve_ivp
    import math
    eps = float(eps); A = float(A)
    lam = math.sqrt(2*eps); xs = lam/math.sqrt(6); v = 6*xs/(3 - eps)
    x0 = xs + A; s0 = v*A; sf = eps*dN
    if slice_kind == 'rho':                      # dx/ds = G/(-3x^2), dN/ds = -1/(3x^2)
        f = lambda s, u: [G(u[0], lam)/(-3*u[0]**2), -1/(3*u[0]**2)]
        sol = solve_ivp(f, (s0, sf), [x0, 0.0], method='DOP853', rtol=1e-13, atol=1e-16)
    else:                                        # q = -phi increases; dphi/dN = sqrt6 x
        phi = lambda x, s: -(1/lam)*math.log(3*math.exp(2*s)*(1 - x*x))
        f = lambda q, u: [-G(u[0], lam)/(math.sqrt(6)*u[0]), -1/(math.sqrt(6)*u[0])]
        sol = solve_ivp(f, (-phi(x0, s0), -phi(xs, sf)), [x0, 0.0], method='DOP853', rtol=1e-13, atol=1e-16)
    return mp.mpf(sol.y[1][-1])

def fnl_su(eps, dN, slice_kind, h=None):
    """N1, N2 by central differences (Richardson over h, 2h); f = (5/6) N2/N1^2.
    h scales as 1/W so that the final-slice amplitude A*W stays in the perturbative regime."""
    eps = mp.mpf(eps)
    if h is None: h = mp.mpf('1e-3')*mp.e**((eps - 3)*dN)
    def f_of(hh):
        Np, N0, Nm = (su_efolds(eps, a, dN, slice_kind) for a in (hh, 0, -hh))
        return (Np - Nm)/(2*hh), (Np + Nm - 2*N0)/hh**2
    (N1a, N2a), (N1b, N2b) = f_of(h), f_of(2*h)
    N1 = (4*N1a - N1b)/3; N2 = (4*N2a - N2b)/3
    return N1, N2, mp.mpf(5)/6*N2/N1**2

def lane_value(eps):   return mp.mpf(5)*(eps - 7)/8        # delta-N lane, rho slice (second_method)
def s9_value(eps):     return mp.mpf(5)*(2*eps - 15)/24    # threading map, rho slice, initial label
def phi_slice_value(): return mp.mpf(-5)                    # threading map, phi slice, initial label

# ---------------- Part B: closed form to second order (sympy), general constant eps ----------------
import sympy as sp

def su_second_order():
    """x = x* + A x1 + A^2 x2, s = ln|H| = -eps N + A s1 + A^2 s2, initial data exactly linear in A
    along the growing eigenvector (S9b: any A^2 initial term is O(1/W)).  Returns f on both slices
    as functions of eps and W = e^{kappa N_f} (W -> oo is the growing-mode-dominated limit)."""
    eps, N, W = sp.symbols('epsilon N W', positive=True)
    lam = sp.sqrt(2*eps); xs = lam/sp.sqrt(6); kap = eps - 3
    x = sp.Symbol('x')
    Gx = -3*x + sp.sqrt(6)/2*lam*(1 - x**2) + 3*x**3
    G2 = sp.simplify(sp.diff(Gx, x, 2).subs(x, xs))          # = 4 sqrt(3 eps)
    assert sp.simplify(sp.diff(Gx, x).subs(x, xs) - kap) == 0
    # work with W = e^{kappa N} as the variable: d/dN = kappa W d/dW; W(0) = 1, W -> oo growing-mode limit
    D = lambda f: kap*W*sp.diff(f, W)
    x1 = W
    s1 = -6*xs*W/kap                                          # pure eigenmode (s1(0) = v)
    x2 = G2/(2*kap)*(W**2 - W)                                # x2(0) = 0
    src = sp.expand(-3*(2*xs*x2 + x1**2))                     # s2' = -3(2 x* x2 + x1^2)
    c2 = src.coeff(W, 2); c1 = src.coeff(W, 1)
    assert sp.simplify(src - c2*W**2 - c1*W) == 0
    s2 = c2*(W**2 - 1)/(2*kap) + c1*(W - 1)/kap               # s2(0) = 0
    assert sp.simplify(D(x1) - kap*x1) == 0 and sp.simplify(D(s1) + 6*xs*x1) == 0
    assert sp.simplify(D(x2) - kap*x2 - G2/2*x1**2) == 0 and sp.simplify(D(s2) - src) == 0
    def slice_f(F0p, F1, F2):
        """slice function F(N,A) = Fbar(N) + A F1 + A^2 F2 with Fbar' = F0p (const): solve F = Fbar(N_f)."""
        n1 = -F1/F0p                                          # F0p n1 + F1 = 0
        n2 = -(D(F1)*n1 + F2)/F0p                             # F0p n2 + F1' n1 + F2 = 0
        return sp.simplify(sp.Rational(5, 6)*2*n2/n1**2)
    f_rho_W = slice_f(-eps, s1, s2)                           # rho slice: F = s, Fbar' = -eps
    L1 = sp.diff(sp.log(1 - x**2), x).subs(x, xs); L2 = sp.diff(sp.log(1 - x**2), x, 2).subs(x, xs)
    f_phi_W = slice_f(-2*eps, 2*s1 + L1*x1, 2*s2 + L1*x2 + sp.Rational(1, 2)*L2*x1**2)  # phi slice
    return dict(eps=eps, W=W, f_rho=f_rho_W, f_phi=f_phi_W,
                f_rho_inf=sp.simplify(sp.limit(f_rho_W, W, sp.oo)),
                f_phi_inf=sp.simplify(sp.limit(f_phi_W, W, sp.oo)),
                lin_ratio=sp.simplify((s1/(-eps))/((2*s1 + L1*x1)/(-2*eps))))

def s9_lapse_chain():
    """S9's rho-continuation (S9.3)-(S9.4) on the growing mode, monopole, with the second-order L x S lapse
    A2 (coefficient of zeta_L zeta_S) left symbolic: every other input is a linear object
    (dt1 = lam zeta/H, zetadot = -(3-eps) H zeta, alpha1 = zetadot/H, rhobar' = -6 eps H^3, rhobar'' = 18 eps^2 H^4).
    Returns f_extra(A2), S9's A2 monopole from its json, and the A2 the exact separate universe requires."""
    eps = sp.Symbol('epsilon', positive=True); A2 = sp.Symbol('A2')
    lam = 1 - eps/3; lamp = 2*lam
    H = sp.Symbol('H'); zLzS = 1                              # per zeta_L zeta_S
    dt = lam/H                                                # H dt^(1) = lam zeta
    zdot = -(3 - eps)*H; al = zdot/H
    drho1 = -2*eps*H**2*al                                    # -phidot^2 alpha,  phidot^2 = 2 eps H^2
    # d/dt of the linear field delta rho_L(t) = 2 eps (3-eps) H^2 zeta_L(t): both H (Hdot = -eps H^2) and zeta (zetadot) vary
    drho1dot = 2*eps*(3 - eps)*(2*H*(-eps*H**2) + H**2*zdot)
    rhob1 = -6*eps*H**3; rhob2 = 18*eps**2*H**4
    drho2 = -2*eps*H**2*A2 + 3*2*eps*H**2*al*al               # (S9.4): -phidot^2 A2 + 3 phidot^2 alpha_L alpha_S
    dt2 = -(drho2 + 2*drho1dot*dt + rhob2*dt*dt)/rhob1
    M_extra = sp.simplify(H*dt2 - eps*H**2*dt*dt + lam*2*zdot*dt)   # (S9.3) extra kernel per zeta_L zeta_S
    assert not M_extra.has(H)
    f_extra = sp.simplify(sp.Rational(5, 6)*M_extra/lamp**2)  # local kernel -> f monopole, rho normalisation
    A2_s9 = eps*(3 - eps)**2/3                                # json S9.A2_superhubble_growing, k_L^0, mu^2 -> 1/3
    f_extra_s9 = sp.simplify(f_extra.subs(A2, A2_s9))
    # requirement: f_rho_SU - f_phi_SU/2 = f[M_extra - M_phi]_rho with f[M_phi]_rho = -5 eps/24 (S9 table)
    f_phi_map_rho = -5*eps/24
    f_extra_req = sp.simplify((5*(eps - 7)/8 + sp.Rational(5, 2)) + f_phi_map_rho)
    A2_req = sp.solve(sp.Eq(f_extra, f_extra_req), A2)[0]
    return dict(eps=eps, A2=A2, M_extra=M_extra, f_extra=f_extra, f_extra_s9=f_extra_s9, A2_s9=A2_s9,
                f_extra_req=f_extra_req, A2_req=sp.factor(A2_req),
                f_gap_from_A2=sp.simplify(f_extra_s9 - f_extra_req))

def usr_check():
    """USR (V const, lam = 0): x' = -3x + 3x^3, comoving slice phi = phi_f; small-x closed form N = (1/3) ln(x_i/x_f)."""
    xi, c = sp.symbols('x_i c', positive=True)                 # c = (3/sqrt6) Delta phi, x_f = x_i - c
    N = sp.log(xi/(xi - c))/3
    N1, N2 = sp.diff(N, xi), sp.diff(N, xi, 2)
    f = sp.simplify(sp.Rational(5, 6)*N2/N1**2)
    return sp.simplify(sp.limit(f.subs(xi, c + sp.Symbol('xf', positive=True)), sp.Symbol('xf', positive=True), 0))

if __name__ == '__main__':
    t0 = time.time(); r = su_second_order(); eps, W = r['eps'], r['W']; ch = s9_lapse_chain()
    out = {'part_B_closed_form': {'f_phi(W)': str(r['f_phi']), 'f_rho(W)': str(r['f_rho']),
                                  'f_phi_Winf': str(r['f_phi_inf']), 'f_rho_Winf': str(r['f_rho_inf']),
                                  'f_rho_Winf_minus_lane': str(sp.simplify(r['f_rho_inf'] - 5*(eps - 7)/8)),
                                  'f_rho_Winf_minus_S9': str(sp.simplify(r['f_rho_inf'] - sp.Rational(5, 24)*(2*eps - 15))),
                                  'N1_rho_over_N1_phi_Winf': str(sp.limit(r['lin_ratio'], W, sp.oo)),
                                  'f_phi_dust': str(r['f_phi_inf'].subs(eps, sp.Rational(3, 2))),
                                  'f_rho_dust': str(r['f_rho_inf'].subs(eps, sp.Rational(3, 2)))},
           'part_A_numeric_crosscheck': [], 'part_C_lapse_chain': {k: str(v) for k, v in ch.items() if k not in ('eps', 'A2')},
           'usr_comoving_slice_f': str(usr_check())}
    for e_, dN in ((1.5, 3), (1.5, 6), (1.2, 4), (2.2, 6)):
        Wv = sp.exp((e_ - 3)*(-dN)); row = {'eps': e_, 'dN': dN, 'W': float(Wv)}
        for kind in ('phi', 'rho'):
            f = m_f = float(fnl_su(e_, dN, kind)[2]); pred = float(r['f_' + kind].subs({eps: e_, W: Wv}))
            row[kind] = {'numeric': f, 'closed_form': pred, 'absdiff': abs(f - pred)}
            assert abs(f - pred) < 2e-5, (kind, e_, dN, f, pred)
        out['part_A_numeric_crosscheck'].append(row)
    assert sp.simplify(r['f_phi_inf'] + 5) == 0 and sp.simplify(r['f_rho_inf'] - 5*(eps - 7)/8) == 0
    assert sp.simplify(ch['f_extra_s9'] - (5*eps/24 - sp.Rational(5, 8))) == 0      # reproduces S9 extra_only monopole
    assert sp.simplify(ch['f_gap_from_A2'] - 5*(6 - eps)/24) == 0                  # the whole gap sits in A2
    assert sp.simplify(ch['A2_req'] - 2*(3 - eps)**2) == 0 and str(usr_check()) == '5/2'
    out['verdict'] = {'verdict': 'NOT (hypothesis) / LOCATED', 'shift_divergence_is_evolution_term': False,
        'lane_value_confirmed_general_eps': '5*epsilon/8 - 35/8', 'phi_slice_confirmed': '-5 (all eps)',
        'residual_general_eps': '5*(6 - epsilon)/24', 'residual_dust': '15/16',
        'located_in': 'S9 second-order L x S lapse monopole A2: S9 eps(3-eps)^2/3 (dust 9/8) vs required 2(3-eps)^2 = 2 alpha_L alpha_S (dust 9/2)',
        'wall_clock_s': round(time.time() - t0, 1)}
    json.dump(out, open(OUT, 'w'), indent=1); print(json.dumps(out['part_B_closed_form'], indent=1)); print(json.dumps(out['part_C_lapse_chain'], indent=1)); print(out['verdict'])
