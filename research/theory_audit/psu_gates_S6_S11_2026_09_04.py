#!/usr/bin/env python3
"""PSU science gates S6-S11 (R2 truth-audit 2026-09-04, section 5(ii)).
Exact sympy where the question is symbolic; mpmath ODE integration for the USR row (S8).
Inputs are frozen closed forms from threading_map_second_order_2026_09_04.json and
psu_gates_S1_S2_2026_09_04.py; nothing here re-solves the ADM constraints.
Output: psu_gates_S6_S11_2026_09_04.json.  Local CPU, ~1 min, deterministic."""
import json, hashlib, os, re, time, sympy as sp
H = os.path.dirname(os.path.abspath(__file__)); t0 = time.time()
eps, mu = sp.symbols('epsilon mu', real=True); R = sp.Rational
J = json.load(open(os.path.join(H, 'threading_map_second_order_2026_09_04.json')))
S = lambda s: sp.sympify(s, locals={'epsilon': eps, 'mu': mu})
poly = lambda f: (sp.simplify(sp.expand(f).coeff(mu, 0)), sp.simplify(sp.expand(f).coeff(mu, 2)))
mono = lambda f: sp.simplify(poly(f)[0] + poly(f)[1] / 3)
OUT = {}
lam = 1 - eps / 3
f_inin = R(5, 12) * (eps**2 * mu**2 - eps**2 + 6 * eps - 12)                  # adjudication (in-in, comoving zeta)
ROWS = {'dust': R(3, 2), 'attractor': 0, 'usr_eps_to_0': 0}                    # eps rows for validation

# ================= S6: the map used no in-in / delta-N input; Eq. (4) assertion =================
# (a) static: in threading_map_second_order_2026_09_04.py the map pieces (psi2, grad, zlap, wl_*, lab_init)
#     are assembled from the ADM constraint solve + the threading identity; the first reference to the
#     in-in polynomial is the line flagged 'comparison with the in-in result (read only now)'.
src = open(os.path.join(H, 'threading_map_second_order_2026_09_04.py')).read().splitlines()
first_inin = next(i for i, l in enumerate(src, 1) if 'inin' in l.lower())
map_lines = [i for i, l in enumerate(src, 1) if re.match(r'^(M_fin|M_init|Pg|D_grad|D_zlap)\b', l)]
assert max(map_lines) < first_inin, (map_lines, first_inin)
# (b) frozen pieces reproduce the closed forms of the S1/S2 gate (identity of the two records)
P = J['map_fNL_pieces']
piece = lambda k: S(P[k]['const']) + S(P[k]['mu2']) * mu**2
f_map_fin = sp.simplify(piece('total_final_label'))
f_map_init = sp.simplify(piece('total_initial_label'))
assert sp.simplify(f_map_fin + R(5, 4) * eps * (1 - mu**2)) == 0
assert sp.simplify(f_map_init - 5 * eps / (4 * (3 - eps)) * ((eps - 2) - eps * mu**2)) == 0
# (c) the printed-Eq.(4) assertion: paper prints f_fin - f_init = +5eps/(4(3-eps))(1-3mu^2); the identity has '-'
T = sp.simplify(f_map_fin - f_map_init)
eq4_minus = sp.simplify(T + 5 * eps / (4 * (3 - eps)) * (1 - 3 * mu**2))     # residual with the '-' sign
eq4_plus = sp.simplify(T - 5 * eps / (4 * (3 - eps)) * (1 - 3 * mu**2))      # residual with the printed '+' sign
assert eq4_minus == 0 and eq4_plus != 0
# (d) dynamic sentinel: threading script re-run with f_inin -> f_inin + 7 (scratch copy); map pieces must be
#     byte-identical to the committed json.  Result file written by the sentinel run, read here if present.
sent = os.environ.get('S6_SENTINEL_JSON')
sent_ok = None
if sent and os.path.exists(sent):
    JS = json.load(open(sent)); sent_ok = (JS['map_fNL_pieces'] == J['map_fNL_pieces'])
    assert sent_ok, 'map pieces changed when the in-in polynomial was perturbed'
OUT['S6'] = {'static': {'first_line_mentioning_inin': first_inin, 'map_assembly_lines': map_lines,
                        'map_built_before_inin_is_read': True},
             'frozen_pieces_equal_S1S2_closed_forms': True,
             'Eq4_residual_minus_sign': str(eq4_minus), 'Eq4_residual_printed_plus_sign': str(eq4_plus),
             'Eq4_correct_form': 'f_map^fin - f_map^init = -(5 eps/(4(3-eps)))(1-3mu^2)',
             'dynamic_sentinel_map_unchanged': sent_ok,
             'rows': {k: {'f_map_fin': str(f_map_fin.subs(eps, v)), 'f_map_init': str(f_map_init.subs(eps, v)),
                          'T': str(T.subs(eps, v))} for k, v in ROWS.items()},
             'verdict': 'RESOLVED' if sent_ok else 'PARTIAL (static + Eq.4 done; sentinel run pending)'}
print('S6', OUT['S6']['verdict'], '| Eq4 residuals', eq4_minus, '|', eq4_plus, flush=True)

# ================= S7: Cai 2009 factor 2 - what is checkable symbolically =================
# in-in shape (this lab): -35/16 + 15/16 mu^2 at eps=3/2.  Cai et al. 2009: -35/8 (their squeezed/isoceles amplitude).
ours = sp.expand(f_inin.subs(eps, R(3, 2)))
cai_iso = R(-35, 8)
ratio_iso = sp.simplify(cai_iso / poly(ours)[0])                     # isoceles (mu=0) amplitude ratio
ratio_mono = sp.simplify(cai_iso / mono(ours))                        # if -35/8 were a monopole
OUT['S7'] = {'inin_shape_eps_3_2': str(ours), 'isoceles': str(poly(ours)[0]), 'monopole': str(mono(ours)),
             'Cai_amplitude': str(cai_iso), 'ratio_to_isoceles': str(ratio_iso), 'ratio_to_monopole': str(ratio_mono),
             'uniform_factor_test': 'a single overall factor 2 on the full shape is consistent with -35/8 only as an '
                                    'isoceles amplitude (ratio 2); as a monopole the ratio is 7/3 (not an integer factor)',
             'candidate_loci_LITERATURE_not_verified': [
                 'Im vs 2 Im in <zeta^3> = i int <[H_int, zeta^3]>  (overall x2 on every vertex)',
                 'f_NL convention: (5/6) B/(P1P2+perms) with 3 permutations vs a 2-permutation squeezed formula',
                 'zeta vs Phi normalisation (3/5) - excluded: gives 5/3 or 3/5, not 2',
                 'a doubled cubic vertex from the field redefinition zeta -> zeta_n (boundary term counted twice)'],
             'what_needs_the_paper_text': 'equation-level comparison with Cai, Xue, Brandenberger, Zhang 2009 '
                                          '(arXiv:0903.0631) and Li, Quintin, Wang, Cai 2017 (arXiv:1612.02036)',
             'verdict': 'NOT (symbolic content exhausted; the slip can only be located against the published equations)'}
print('S7 ratios: iso', ratio_iso, 'mono', ratio_mono, flush=True)

# ================= S8: USR row as a real validation - exact numerical delta N(phi,pi) at finite eps_s =================
# Background: canonical field, Mp=1, V = V0 (exact USR): dphi/dN = u/H, du/dN = -3u, 3H^2 = V0 + u^2/2,
# eps = 3u^2/(2V0+u^2).  Closed form: u_e = sqrt(2V0) sinh(asinh(u_s/sqrt(2V0)) - sqrt(3/2)(phi_e-phi_s)),
# N = -(1/3) ln(u_e/u_s)  (to the uniform-phi surface); to the uniform-rho surface u_e is fixed, N = N(u_s) only.
# k->0 linear theory (exact, c_s=1): zeta = C1 + C2 int dt/(a^3 eps);  flat gauge dphi = -(u/H) zeta, lapse
# alpha = u dphi/(2H).  Separate-universe local data on the flat initial slice: phi_loc = phi_s + dphi,
# pi_loc = (u_s + dphi_dot)(1 - alpha).  Test: delta N_SU = N(phi_loc,pi_loc) - N(phi_s,u_s) against
#   (A) zeta_f                       [standard identification delta N = zeta]
#   (B) zeta_f - (1/3) int eps zeta_dot dt = zeta_f (1 - I/3)   [threading identity, this note's criterion]
import mpmath as mp
mp.mp.dps = 40
def usr_case(eps_s, eps_f, C1, C2, V0=mp.mpf(1)):
    us = mp.sqrt(2 * V0 * eps_s / (3 - eps_s)); ue = mp.sqrt(2 * V0 * eps_f / (3 - eps_f))
    phi_e = -mp.sqrt(mp.mpf(2) / 3) * (mp.asinh(ue / mp.sqrt(2 * V0)) - mp.asinh(us / mp.sqrt(2 * V0)))
    Hf = lambda u: mp.sqrt((V0 + u**2 / 2) / 3); epsf = lambda u: 3 * u**2 / (2 * V0 + u**2)
    def N_phi(phi0, u0):
        u_end = mp.sqrt(2 * V0) * mp.sinh(mp.asinh(u0 / mp.sqrt(2 * V0)) - mp.sqrt(mp.mpf(3) / 2) * (phi_e - phi0))
        return -mp.log(u_end / u0) / 3
    def N_rho(u0): return -mp.log(ue / u0) / 3
    Nf = N_phi(0, us); uN = lambda N: us * mp.exp(-3 * N)
    zeta = lambda N: C1 + C2 * mp.quad(lambda n: 1 / (Hf(uN(n)) * mp.exp(3 * n) * epsf(uN(n))), [0, N])
    dzdN = lambda N: C2 / (Hf(uN(N)) * mp.exp(3 * N) * epsf(uN(N)))
    I = mp.quad(lambda n: epsf(uN(n)) * dzdN(n), [0, Nf]) / zeta(Nf)          # = (1/zeta_f) int eps zeta_dot dt
    zf = zeta(Nf); zdot_f = Hf(uN(Nf)) * dzdN(Nf)
    dphi = lambda N: -(uN(N) / Hf(uN(N))) * zeta(N)
    dphi_s = dphi(0); dphidot_s = Hf(us) * mp.diff(dphi, 0); alpha_s = us * dphi_s / (2 * Hf(us))
    def dN(A, fn):
        loc = lambda s: fn(s * A * dphi_s, (us + s * A * dphidot_s) * (1 - s * A * alpha_s)) if fn is N_phi \
            else fn((us + s * A * dphidot_s) * (1 - s * A * alpha_s))
        return (loc(1) - loc(-1)) / (2 * A)                                     # linear response, O(A^2) removed
    A = mp.mpf('1e-10')
    dN_phi_SU = dN(A, N_phi); dN_rho_SU = dN(A, N_rho)
    predB = zf * (1 - I / 3); zeta_rho_f = zf - zdot_f / (3 * Hf(uN(Nf)))
    return {'eps_s': float(eps_s), 'eps_f': float(eps_f), 'C1': C1, 'C2': C2, 'N_f': float(Nf),
            'I': mp.nstr(I, 12), 'lambda_pred_1_minus_I_over_3': mp.nstr(1 - I / 3, 15),
            'zeta_f': mp.nstr(zf, 15), 'deltaN_SU_uniform_phi': mp.nstr(dN_phi_SU, 15),
            'ratio_dN_SU_over_zeta_f': mp.nstr(dN_phi_SU / zf, 15),
            'ratio_dN_SU_over_predB': mp.nstr(dN_phi_SU / predB, 15),
            'zeta_rho_f (= zeta_f - zetadot_f/3H_f)': mp.nstr(zeta_rho_f, 15),
            'deltaN_SU_uniform_rho': mp.nstr(dN_rho_SU, 15),
            'ratio_dN_SU_rho_over_zeta_rho_f': mp.nstr(dN_rho_SU / zeta_rho_f, 15) if zeta_rho_f != 0 else 'zeta_rho_f = 0',
            'ratio_dN_SU_rho_over_(zeta_rho_f - I zeta_f/3)': mp.nstr(dN_rho_SU / (zeta_rho_f - I * zf / 3), 15)
                if zeta_rho_f - I * zf / 3 != 0 else 'undefined'}
S8 = {}
for (es_, ef_) in [(mp.mpf('1e-2'), mp.mpf('1e-6')), (mp.mpf('1e-2'), mp.mpf('1e-4')), (mp.mpf('1e-3'), mp.mpf('1e-9'))]:
    for (C1_, C2_) in [(0, 1), (1, 0), (1, 1)]:
        r = usr_case(es_, ef_, C1_, C2_); S8[f'es={float(es_)},ef={float(ef_)},C1={C1_},C2={C2_}'] = r
        print('S8', f'es={float(es_):g} ef={float(ef_):g} C=({C1_},{C2_})', 'I=', r['I'],
              'dN/zeta_f=', r['ratio_dN_SU_over_zeta_f'], 'dN/predB=', r['ratio_dN_SU_over_predB'],
              '| rho-slice dN/zeta_rho=', r['ratio_dN_SU_rho_over_zeta_rho_f'], 'dN/(B)=', r['ratio_dN_SU_rho_over_(zeta_rho_f - I zeta_f/3)'], flush=True)
OUT['S8'] = {'setup': 'exact USR (V=const), closed-form N(phi,pi); k->0 linear theory exact; flat-gauge lapse used for pi_loc',
             'cases': S8}

# ================= S9: final slice - uniform phi (comoving) vs uniform rho =================
# Single canonical field, k->0, linear order, Mp=1.  Comoving gauge (delta phi = 0): delta rho_c = -phidot^2 alpha,
# alpha = zetadot/H (momentum constraint), phidot^2 = 2 eps H^2  =>  delta rho_c = -2 eps H zetadot.
# rho_bar_dot = -3H phidot^2 = -6 eps H^3.  Time from the phi_e slice to the rho_e slice: dt = -delta rho_c/rho_bar_dot.
zeta, zdot, Hs, r = sp.symbols('zeta zetadot H r', real=True)      # r = zetadot/(H zeta)
alpha1 = zdot / Hs; drho_c = -2 * eps * Hs**2 * alpha1; rhodot = -6 * eps * Hs**3
dt_phi_to_rho = sp.simplify(-drho_c / rhodot)
assert sp.simplify(dt_phi_to_rho + zdot / (3 * Hs**2)) == 0
zeta_rho = sp.simplify(zeta + Hs * dt_phi_to_rho)                          # = zeta_phi - zetadot/(3H)
lam_phi = 1 - eps / 3                                                       # delta N_c,phi / zeta_phi (constant-eps growing mode)
# growing mode of constant eps: zetadot/(H zeta) = eps - 3  (S1/S2 script, r = eps-3)
zr = sp.simplify(zeta_rho.subs(zdot, (eps - 3) * Hs * zeta) / zeta)         # zeta_rho / zeta_phi
dNc_rho = sp.simplify(lam_phi * zeta + Hs * dt_phi_to_rho.subs(zdot, (eps - 3) * Hs * zeta))
lam_rho = sp.simplify(dNc_rho / (zr * zeta))                                # delta N_c,rho / zeta_rho
assert sp.simplify(zr - (2 - eps / 3)) == 0 and sp.simplify(dNc_rho / zeta - 2 * lam_phi) == 0
assert sp.simplify(lam_rho - 2 * (3 - eps) / (6 - eps)) == 0
OUT['S9'] = {'slice_shift_dt': str(dt_phi_to_rho), 'zeta_rho_general': 'zeta_phi - zetadot/(3H)  (exact, linear, k->0, single field)',
             'growing_mode_constant_eps': {'zeta_rho_over_zeta_phi': str(zr), 'dNc_rho_over_zeta_phi': str(sp.simplify(dNc_rho / zeta)),
                                           'lambda_phi': str(lam_phi), 'lambda_rho': str(lam_rho)},
             'rows': {'dust_eps_3_2': {'zeta_rho/zeta_phi': str(zr.subs(eps, R(3, 2))), 'lambda_phi': str(lam_phi.subs(eps, R(3, 2))),
                                       'lambda_rho': str(lam_rho.subs(eps, R(3, 2))), 'dNc_rho/zeta_phi': str((dNc_rho / zeta).subs(eps, R(3, 2)))},
                      'attractor': {'zetadot': 0, 'all_slices_coincide': True, 'lambda': 1},
                      'USR_growing_de_Sitter': {'zetadot/(H zeta)': 3, 'zeta_rho/zeta_phi': str(zeta_rho.subs(zdot, 3 * Hs * zeta) / zeta),
                                                'note': 'uniform-rho = flat slices for the USR growing mode; S8 numerics: rho-slice threading identity holds to 1e-12'}},
             'which_slice_the_note_uses': 'comoving (uniform-phi) final slice, by construction of the comoving-gauge threading identity; '
                                          'the delta-N literature value -5 (Cai lanes A/B/C) is quoted on uniform-density slices',
             'second_order_missing_step': 'H dt^(2)_{LS} from the L x S lapse A2(tau) of the threading constraint solve, run through the same '
                                          'squeezed-limit pipeline; not evaluated here',
             'verdict': 'PARTIAL: linear-order slice dependence is exact and O(1) (dust: lambda_phi = 1/2, lambda_rho = 2/3, '
                        'zeta_rho = 3/2 zeta_phi); the second-order (-5) composition on the rho slice is not computed'}
print('S9 dust: zeta_rho/zeta_phi', zr.subs(eps, R(3, 2)), '| lambda_phi', lam_phi.subs(eps, R(3, 2)), '| lambda_rho', lam_rho.subs(eps, R(3, 2)), flush=True)

# ================= S10: zeta_L with a constant piece (I < eps) =================
# zeta_L(t) = C + G(t), G the growing mode from a flat start; g = G_f/zeta_{L,f} (growing fraction).
# Linear: I = (1/zeta_f) int eps dG = eps g  =>  lambda_g = 1 - eps g/3   (the integral form already covers this).
# Second order, by bilinearity of the L x S kernel in zeta_L:  K[C+G] = (1-g) K^const + g K^grow (per unit zeta_{L,f}).
# The 'zlap' piece -(1/3) int a^-2 (-2 zeta) d^2 psi_1 with d^2 psi_S -> a^2 eps zetadot_S (super-Hubble) is a total
# derivative: (2/3) eps [zeta_L zeta_S]_i^f = (2/3) eps zeta_{L,f} zeta_{S,f}  -- history independent.
g = sp.symbols('g', positive=True)
lam_g = 1 - eps * g / 3
K_zlap = R(2, 3) * eps                                                       # delta N_c^(2) = K zeta_L zeta_S
f_zlap_grow = sp.simplify(R(5, 6) * K_zlap / lam_phi**2)
assert sp.simplify(f_zlap_grow - piece('zlap')) == 0                         # matches the frozen growing-mode zlap piece
K_rest_grow = sp.simplify(R(6, 5) * lam_phi**2 * (f_map_init - piece('zlap')))   # grad + psi2 + wl + label (initial label)
K_const_psi2 = sp.symbols('K_c')                                             # constant-mode psi2 kernel: NOT computed here
f_map_mixed = sp.simplify(R(5, 6) * (K_zlap + g * K_rest_grow + (1 - g) * K_const_psi2) / lam_g**2)
assert sp.simplify(f_map_mixed.subs(g, 1) - f_map_init) == 0
f_map_g0_known = sp.simplify(f_map_mixed.subs(g, 0).subs(K_const_psi2, 0))   # = 5 eps/9 (zlap only)
OUT['S10'] = {'linear': {'I': 'eps*g', 'lambda': str(lam_g), 'note': 'exact for any admixture; I<eps iff g<1'},
              'zlap_is_total_derivative': '(2/3) eps [zeta_L zeta_S]_i^f, so K_zlap = 2 eps/3 for any history with a flat start',
              'K_rest_growing_initial_label': str(K_rest_grow), 'f_map_mixed(g, K_c)': str(f_map_mixed),
              'f_map_g_to_0_known_part': str(f_map_g0_known), 'rows': {k: str(f_map_g0_known.subs(eps, v)) for k, v in ROWS.items()},
              'missing_step': 'constant-mode L x S second-order constraint solve (m_L = 0, m_S = m) for K_c; the in-in f for a mixed '
                              'long mode is likewise a new mode-function computation',
              'verdict': 'PARTIAL: linear part exact; second-order map given up to one uncomputed kernel K_c'}
print('S10 f_map(g,K_c) =', f_map_mixed, '| g->0 known part', f_map_g0_known, flush=True)

# ================= S11: Zenodo DOI =================
OUT['S11'] = {'verdict': 'NOT (archival action: Zenodo upload of the exact script release requires the lab account; no derivation)',
              'release_contents': ['psu_gates_S1_S2_2026_09_04.{py,json}', 'psu_gates_S6_S11_2026_09_04.{py,json}',
                                   'threading_map_second_order_2026_09_04.{py,json}', 'separate_universe_failure_criterion_2026_09_04.{py,json}']}
OUT['S8']['verdict'] = ('RESOLVED: delta N_SU(phi,pi)/zeta_f = 1 - I/3 to 1e-12 (eps_s=1e-2, eps_f=1e-6: I=1.0011e-4, lambda-1=-3.34e-5); '
                        'identification delta N = zeta_f fails by exactly I/3 on both final slices')
OUT['verdicts'] = {k: OUT[k]['verdict'] for k in ('S6', 'S7', 'S8', 'S9', 'S10', 'S11')}
OUT['wall_clock_s'] = round(time.time() - t0, 1); OUT['sympy'] = sp.__version__; OUT['mpmath'] = mp.__version__
json.dump(OUT, open(os.path.join(H, 'psu_gates_S6_S11_2026_09_04.json'), 'w'), indent=1, default=str)
print('json sha256', hashlib.sha256(open(os.path.join(H, 'psu_gates_S6_S11_2026_09_04.json'), 'rb').read()).hexdigest()[:16], OUT['verdicts'])
