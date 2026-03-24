import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d
import json, time

print('='*70)
print('TIER 1A: COMBINED-INTEGRAND f_NL')
print('='*70)

def solve_mode(eps, k, tau0=-300, tauf=-0.01, n_pts=50000):
    p = 2.0 / (2*eps - 1)
    def rhs(tau, y):
        zr, zi, dzr, dzi = y
        zoz = -p / tau
        return [dzr, dzi, 2*zoz*dzr - k**2*zr, 2*zoz*dzi - k**2*zi]
    z0 = (-tau0)**p
    amp = 1.0 / (z0 * np.sqrt(2*k))
    phase = k * tau0
    y0 = [amp*np.cos(phase), amp*np.sin(phase),
          -amp*k*np.sin(phase), amp*k*np.cos(phase)]
    taus = np.linspace(tau0, tauf, n_pts)
    sol = solve_ivp(rhs, [tau0, tauf], y0, t_eval=taus,
                    method='DOP853', rtol=1e-13, atol=1e-16)
    if not sol.success: return None
    return sol.t, sol.y[0]+1j*sol.y[1], sol.y[2]+1j*sol.y[3]

def compute_fnl(eps, k_long=0.001, k_short=1.0, tau0=-300, tauf=-0.01):
    p = 2.0 / (2*eps - 1)
    sol_k = solve_mode(eps, k_short, tau0, tauf)
    sol_k1 = solve_mode(eps, k_long, tau0, tauf)
    if sol_k is None or sol_k1 is None: return None
    tau, zk, dzk = sol_k
    _, zk1, dzk1 = sol_k1
    
    zk_r = interp1d(tau, np.real(zk), kind='cubic')
    zk_i = interp1d(tau, np.imag(zk), kind='cubic')
    dzk_r = interp1d(tau, np.real(dzk), kind='cubic')
    dzk_i = interp1d(tau, np.imag(dzk), kind='cubic')
    zk1_r = interp1d(tau, np.real(zk1), kind='cubic')
    zk1_i = interp1d(tau, np.imag(zk1), kind='cubic')
    dzk1_r = interp1d(tau, np.real(dzk1), kind='cubic')
    dzk1_i = interp1d(tau, np.imag(dzk1), kind='cubic')
    
    def zc(t): return complex(zk_r(t), zk_i(t))
    def dzc(t): return complex(dzk_r(t), dzk_i(t))
    def z1c(t): return complex(zk1_r(t), zk1_i(t))
    def dz1c(t): return complex(dzk1_r(t), dzk1_i(t))
    
    c1 = eps**2 * (1 - eps/2)
    c2 = eps**2
    c3 = -2 * eps**2
    c4 = eps**3 / 2
    
    def combined(t):
        a3 = (-t)**(3*p)
        z = zc(t); dz = dzc(t); z1 = z1c(t); dz1 = dz1c(t)
        chi_k = -dz / k_short**2
        v1 = c1 * a3 * (z1 * dz * dz + 2 * z * dz1 * dz)
        v2 = c2 * a3 * z1 * (-k_short**2 / 2) * z * z
        v3 = c3 * a3 * (dz * (-k_short * k_long) * z1 * chi_k + dz1 * (-k_short**2) * z * chi_k)
        v4 = c4 * a3 * z1 * k_short**2 * chi_k * chi_k
        return v1 + v2 + v3 + v4
    
    def int_re(t): return np.real(combined(t))
    def int_im(t): return np.imag(combined(t))
    
    try:
        I_re, _ = quad(int_re, tau0*0.99, tauf*1.01, limit=500, epsabs=1e-25, epsrel=1e-10)
        I_im, _ = quad(int_im, tau0*0.99, tauf*1.01, limit=500, epsabs=1e-25, epsrel=1e-10)
    except Exception as e:
        print('  Integration failed:', e)
        return None
    
    I_total = complex(I_re, I_im)
    z_k_f = zc(tauf); z_k1_f = z1c(tauf)
    ext = np.conj(z_k1_f) * np.conj(z_k_f)**2
    B_int = -2 * np.imag(ext * I_total)
    PP = np.abs(z_k1_f)**2 * np.abs(z_k_f)**2
    fnl_int = (5.0/12.0) * B_int / PP if PP > 0 else 0
    fnl_redef = 5 * eps / 6
    return dict(epsilon=float(eps), fnl_redef=float(fnl_redef),
        fnl_int=float(fnl_int), fnl_total=float(fnl_redef + fnl_int))

print('\neps=3/2 (exact dust):')
r = compute_fnl(1.5)
if r:
    print('  f_NL_redef = %+.6f (expect +1.2500)' % r['fnl_redef'])
    print('  f_NL_int   = %+.6f' % r['fnl_int'])
    print('  f_NL_total = %+.6f' % r['fnl_total'])
    print('  Target: -35/8 = -4.375 or -35/16 = -2.1875')
    if abs(r['fnl_total'] + 4.375) < 0.5: print('  >>> MATCHES -35/8')
    elif abs(r['fnl_total'] + 2.1875) < 0.5: print('  >>> MATCHES -35/16')
    else: print('  >>> DOES NOT MATCH (vertex implementation needs work)')

print('\neps scan:')
results = []
for eps in [1.48, 1.49, 1.495, 1.4955, 1.50, 1.505, 1.51, 1.52]:
    r = compute_fnl(eps)
    if r:
        results.append(r)
        print('  eps=%.4f: total=%+12.4f (redef=%+.4f int=%+.4e)' % (
            eps, r['fnl_total'], r['fnl_redef'], r['fnl_int']))

with open('/root/bigbounce/tier1a_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print('\nSaved: tier1a_results.json')
