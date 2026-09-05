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
