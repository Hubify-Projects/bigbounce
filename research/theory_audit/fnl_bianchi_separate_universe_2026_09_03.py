#!/usr/bin/env python3
"""A3-2: Bianchi-I (anisotropic) separate-universe cross-check of the
matter-contraction squeezed f_NL, INCLUDING the long mode's shear.

Ledger #1 left exactly one computation open (adjudication 2026-09-02,
"What remains open"): a second-order anisotropic separate-universe
computation of the comoving zeta response to a long mode carrying shear
sigma^i_j = (khat_i khat_j - delta_ij/3) eps zetadot, to see whether it
reproduces the in-in monopole -15/8 and mu^2 coefficient +15/16.

Everything below is derived, not quoted, except the literature comparison
values which are only used AFTER the computation.  Exact sympy throughout.
"""
import json, sympy as sp

out = {}

eps, ns, mu, N, phi, u_i, W = sp.symbols('epsilon n_s mu N phi u_i W', positive=True)
eps = sp.Symbol('epsilon', positive=True)
ns  = sp.Symbol('n_s')
mu  = sp.Symbol('mu')

# ---------------------------------------------------------------- 1. background
# constant eps: a ~ |t|^{1/eps}, H = 1/(eps t) (t<0 contraction).
t = sp.Symbol('t', negative=True)
a_of_t = (-t)**(sp.Rational(1,1)/eps)
H = sp.simplify(sp.diff(a_of_t, t)/a_of_t)
assert sp.simplify(H - 1/(eps*t)) == 0
eps_check = sp.simplify(-sp.diff(H, t)/H**2)
assert sp.simplify(eps_check - eps) == 0
out['background'] = {'H': str(H), 'eps_from_H': str(sp.simplify(eps_check))}

# long-wavelength D (growing) mode: zeta_D ~ int dt / (a^3 eps)
zetaD = (-t)**(1 - 3/eps)                       # D-mode: zeta ~ int dt/(a^3 eps)
# verify it solves the exact super-horizon equation d/dt(a^3 eps zetadot) = 0
assert sp.simplify(sp.diff(a_of_t**3*eps*sp.diff(zetaD, t), t)) == 0
r_zdot = sp.powsimp(sp.simplify(sp.diff(zetaD, t)/zetaD/H), force=True)   # zetadot/(H zeta)
out['growing_mode'] = {'zeta_D(t)': str(zetaD),
                       'zetadot_over_H_zeta': str(sp.simplify(r_zdot)),
                       'at_eps_3_2': str(sp.simplify(r_zdot.subs(eps, sp.Rational(3,2))))}
assert sp.simplify(r_zdot - (eps - 3)) == 0                 # zetadot = (eps-3) H zeta
assert sp.simplify(r_zdot.subs(eps, sp.Rational(3,2)) + sp.Rational(3,2)) == 0

# ------------------------------------------- 2. shear of the long mode (order in k_L)
# Comoving gauge (Maldacena): N_i = d_i psi, psi = -zeta/H + a^2 eps grad^{-2} zetadot.
# h_ij = a^2 e^{2 zeta} delta_ij ; K_ij = (1/2N)(hdot_ij - D_i N_j - D_j N_i)
#   => K^i_j = (H + zetadot) delta^i_j - d_i d_j psi / (a^2 e^{2 zeta}).
# In Fourier d_i d_j -> -k_i k_j, and grad^{-2} -> s_conv / k^2 with s_conv = -1
# for the standard convention (grad^2 -> -k^2).  We keep s_conv symbolic because
# the 2026-09-02 adjudication quotes the opposite sign convention; it multiplies
# the whole shear and therefore only flips the sign of the quadrupole.
kL, zdot = sp.symbols('k_L zetadot')
s_conv = sp.Symbol('s_conv')                                  # +-1
psi_k = -sp.Symbol('zeta')/sp.Symbol('H') + sp.Symbol('a')**2*eps*s_conv*zdot/kL**2
# the k_L -> 0 dominant piece of  +k_i k_j psi / a^2 :
shear_kernel = sp.simplify(sp.expand(kL**2*(s_conv*eps*zdot/kL**2)))   # coeff of khat_i khat_j
out['shear'] = {
    'K^i_j anisotropic part': '(k_i k_j psi)/a^2 |_traceless = s_conv*eps*zetadot*(khat_i khat_j - delta/3)',
    'order_in_kL': 'k_L^0  (the 1/k_L^2 of grad^{-2} exactly cancels the k_i k_j)',
    'coefficient': str(shear_kernel),
    'trace_part_deltaK': str(shear_kernel),
}
# => sigma^z_z = (2/3) s_conv eps zetadot ; the OTHER (non-shift) piece of psi,
# -zeta/H, contributes k_i k_j (-zeta/H)/a^2 = O(k_L^2) and is dropped here.
sigma_zz = sp.Rational(2,3)*s_conv*eps*zdot
out['shear']['sigma_zz'] = str(sigma_zz)

# ------------------------------- 3. accumulated anisotropy of the local scale factors
# h_ij = a^2 e^{2 lambda_i} => K^i_j = (H + lambdadot_i) delta^i_j (no sum),
# so beta_i (traceless part of lambda_i) obeys betadot_i = sigma^i_i.
# On the pure growing mode int zetadot dt = zeta, hence
beta_z_over_zeta = sp.Rational(2,3)*s_conv*eps
out['anisotropy'] = {'beta_z / zeta_L': str(beta_z_over_zeta),
                     'at_eps_3_2': str(beta_z_over_zeta.subs(eps, sp.Rational(3,2)))}

# ------------------------------------------------- 4. isotropic piece: comoving delta-N
# Exponential potential, lambda^2 = 2 eps, x = phidot/(sqrt6 M H), M=1.
lam = sp.sqrt(2*eps)
x = sp.Symbol('x')
F = (1 - x**2)*(sp.sqrt(6)*lam/2 - 3*x)          # dx/dN, derived in the 09-02 lane
xs = lam/sp.sqrt(6)                               # fixed point ; eps = 3 xs^2
assert sp.simplify(F.subs(x, xs)) == 0
assert sp.simplify(3*xs**2 - eps) == 0
uu = sp.Symbol('u')
# dphi/dN = sqrt6 x  =>  du/dphi = F/(sqrt6 x)
dudphi = sp.series(sp.simplify(F.subs(x, xs+uu)/(sp.sqrt(6)*(xs+uu))), uu, 0, 3).removeO()
c1 = sp.simplify(sp.expand(dudphi).coeff(uu, 1))
c2 = sp.simplify(sp.expand(dudphi).coeff(uu, 2))
A2 = sp.simplify(c2/c1)
Wsym = sp.Symbol('W', positive=True)
# u(phi) = u_i W + A2 u_i^2 (W^2 - W),  W = e^{c1 phi}   (ODE residual checked)
ui = sp.Symbol('u_i')
ph = sp.Symbol('phi')
u_sol = ui*sp.exp(c1*ph) + A2*ui**2*(sp.exp(2*c1*ph) - sp.exp(c1*ph))
res = sp.simplify(sp.expand(sp.diff(u_sol, ph) - (c1*u_sol + c2*u_sol**2)))
res2 = sp.simplify(sp.expand(sp.series(res, ui, 0, 3).removeO()).coeff(ui, 2))
assert sp.simplify(res2) == 0, res2
# delta-N to a uniform-phi (comoving) final slice, flat initial slice, growing mode only
integrand = sp.series(1/(sp.sqrt(6)*(xs+uu)), uu, 0, 3).removeO()
P1 = sp.expand(integrand).coeff(uu, 1)
P2c = sp.expand(integrand).coeff(uu, 2)
# growing-mode-dominated limit: W = exp(c1*phi) -> infinity, keep the highest power.
# int_0^Phi e^{c1 phi} dphi = (W-1)/c1 ;  int_0^Phi e^{2 c1 phi} dphi = (W^2-1)/(2 c1)
# delta-N = P1*u + P2c*u^2 integrated; u = u_i e^{c1 phi} + A2 u_i^2 (e^{2c1phi}-e^{c1phi})
z1L = sp.simplify(P1/c1)                                     # coeff of u_i W
z2L = sp.simplify((P1*A2 + P2c)/(2*c1))                      # coeff of u_i^2 W^2
f_iso = sp.radsimp(sp.simplify(sp.Rational(5,3)*z2L/z1L**2))
out['delta_N_comoving'] = {'c1': str(sp.simplify(c1)), 'c2': str(sp.simplify(c2)),
                           'A2': str(A2), 'P1': str(sp.simplify(P1)), 'P2': str(sp.simplify(P2c)),
                           'zeta1_leading_coeff': str(z1L), 'zeta2_leading_coeff': str(z2L),
                           'f_NL_comoving_general_eps': str(f_iso)}
assert sp.simplify(f_iso + 5) == 0, f_iso   # independent rederivation of f_c = -5

# ---------------------------------------------- 5. projection onto global comoving k
# xi_global(x) = xi_local(xtilde), xtilde_i = e^{lambda_i} x_i, lambda_i = zeta_L + beta_i
# => P_global(k) = e^{-sum lambda} P_local(ktilde), ktilde_i = e^{-lambda_i} k_i.
# P_local(k) = A k^{n_s-4}.
zL = sp.Symbol('zeta_L')
bz = beta_z_over_zeta*zL
lam_z, lam_x = zL + bz, zL - bz/2
sum_lam = lam_z + 2*lam_x
sum_khat2_lam = lam_z*mu**2 + lam_x*(1-mu**2)
dlnP = sp.simplify(-sum_lam + (ns-4)*(-sum_khat2_lam))
dlnP = sp.expand(sp.simplify(dlnP))
iso_part = sp.simplify(dlnP.subs(s_conv, 0))
shear_part = sp.simplify(dlnP - iso_part)
out['projection'] = {'dlnP_over_zetaL': str(sp.simplify(dlnP/zL)),
                     'isotropic_part': str(sp.simplify(iso_part/zL)),
                     'shear_part': str(sp.simplify(shear_part/zL))}
assert sp.simplify(iso_part/zL - (1-ns)) == 0        # consistency relation recovered

# validation: attractor (zetadot = 0 -> beta = 0) must give (5/12)(1-n_s), no quadrupole
f_attr = sp.simplify(sp.Rational(5,12)*iso_part/zL)
assert sp.simplify(f_attr - sp.Rational(5,12)*(1-ns)) == 0
# validation: USR has eps -> 0, so the shear (prop to eps) vanishes -> pure monopole
shear_usr = sp.simplify((shear_part/zL).subs(eps, 0))
assert shear_usr == 0
out['validation'] = {'attractor_gives_consistency_relation': 'PASS  f=(5/12)(1-n_s)',
                     'USR_shear_vanishes_as_eps_to_0': 'PASS (pure monopole, consistent with Namjoo+ 5/2)',
                     'shear_is_O(kL^0)': 'PASS (see out["shear"])'}

# ------------------------------------------------------------------ 6. assembly
# scale-invariant matter contraction: n_s = 1 exactly
f_shear = sp.simplify(sp.Rational(5,12)*(shear_part/zL).subs(ns, 1))
f_tot = sp.simplify(f_iso + f_shear)
sub32 = {eps: sp.Rational(3,2), s_conv: 1}
f_tot_32 = sp.simplify(sp.expand(f_tot.subs(sub32)))
f_tot_32_neg = sp.simplify(sp.expand(f_tot.subs({eps: sp.Rational(3,2), s_conv: -1})))
mono = sp.simplify(sp.integrate(f_tot_32, (mu, -1, 1))/2)
quad_mu2 = sp.simplify(sp.expand(f_tot_32).coeff(mu, 2))
# Legendre P2 decomposition
f2_P2 = sp.simplify(sp.integrate(f_tot_32*(3*mu**2-1)/2, (mu, -1, 1))*sp.Rational(5,2)/2)
out['result'] = {
    'f_shear(mu)_general': str(f_shear),
    'f_total(mu)_general_eps': str(f_tot),
    'f_total(mu)_eps_3_2_sconv_+1': str(f_tot_32),
    'f_total(mu)_eps_3_2_sconv_-1': str(f_tot_32_neg),
    'monopole': str(mono),
    'mu2_coefficient': str(quad_mu2),
    'P2_coefficient': str(f2_P2),
    'isoceles_mu_0': str(sp.simplify(f_tot_32.subs(mu, 0))),
}

# ------------------------------------------------------- 7. comparison (AFTER the fact)
inin = -sp.Rational(35,16) + sp.Rational(15,16)*mu**2
out['comparison'] = {
    'in_in_f(mu)': str(inin),
    'in_in_monopole': str(sp.simplify(sp.integrate(inin, (mu,-1,1))/2)),
    'in_in_mu2_coefficient': str(sp.Rational(15,16)),
    'this_work_minus_in_in': str(sp.simplify(sp.expand(f_tot_32 - inin))),
    'ratio_mu2_coefficients': str(sp.simplify(quad_mu2/sp.Rational(15,16))),
    'monopole_gap': str(sp.simplify(mono - sp.Rational(-15,8))),
    'shear_monopole_contribution': str(sp.simplify(sp.integrate(f_shear.subs(sub32), (mu,-1,1))/2)),
}
out['verdict'] = (
    'DISAGREES, and FALSIFIES the reconciliation mechanism. The long mode\'s shear IS '
    'O(k_L^0) - beta_z = (2 eps/3) zeta_L, i.e. exactly zeta_L at eps=3/2 - so the '
    'adjudication is right that it is not an O(k^2) effect. But it is TRACELESS: its '
    'squeezed response is proportional to (3 mu^2 - 1) and contributes exactly ZERO '
    'monopole, so it cannot carry the -25/8 monopole residual between the comoving '
    'delta-N (-5) and the in-in monopole (-15/8). This route gives '
    'f(mu) = -45/8 + (15/8) mu^2 (s_conv=+1): monopole -5 (unchanged from delta-N) vs '
    'in-in -15/8; mu^2 coefficient 15/8, exactly 2x the in-in 15/16 (sign matches only '
    'for s_conv=+1, the sign convention of the 09-02 adjudication); isoceles -45/8 vs '
    '-35/16. The in-in -35/16 is NOT overturned - this route is a gradient-expansion '
    'response, not a complete computation of the bispectrum - but it does not confirm it, '
    'and the shear-carries-the-residual explanation does not survive.')

print(json.dumps(out, indent=2))
with open('research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.json','w') as fh:
    json.dump(out, fh, indent=2)
