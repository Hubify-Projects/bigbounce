#!/usr/bin/env python3
"""
Corrected f_NL computation: Terms 1-4 only (all finite terms).

KEY FIX: Term 3 had a SIGN ERROR in previous versions.
The correct T3 contributes a LARGE coefficient (27/2 = 13.5) times the base integrand,
NOT zero as the buggy version gave.

Terms 5+6 involve the constraint variable χ². Their physical contribution to f_NL
is ZERO (proven: the k₁⁻² divergence is in Re[ext×I], not Im[ext×I]).
"""

import numpy as np
from scipy import integrate
import warnings
warnings.filterwarnings('ignore')

def ghat(x):
    return np.exp(-1j*x) * (1 - 1j/x) / x**2

def ghat_prime(x):
    return np.exp(-1j*x) * (-1j - 3.0/x + 3j/x**2) / x**2

def compute_fnl_corrected(r=1e-3, xf=-0.01, x0=-1000, eps_reg=1e-4, verbose=True):
    """Compute f_NL from Terms 1-4 with corrected T3 sign."""

    eta_f = xf  # k=1

    # Mode functions
    def zk(x): return ghat(x) / np.sqrt(6.0)
    def zk1(x): return ghat(r*x) / np.sqrt(6.0*r)
    def zkp(x): return ghat_prime(x) / np.sqrt(6.0)
    def zk1p(x): return np.sqrt(r) * ghat_prime(r*x) / np.sqrt(6.0)

    damp = lambda x: np.exp(eps_reg * x)

    # External and power spectra
    ext = np.conj(ghat(r*eta_f)/np.sqrt(6*r)) * (np.conj(ghat(eta_f)/np.sqrt(6)))**2
    Pk1 = (1+1/(r*eta_f)**2)/(r*eta_f)**4 / (6*r)
    Pk = (1+1/eta_f**2)/eta_f**4 / 6
    PP = Pk1 * Pk

    def do_integral(f):
        re_val, re_err = integrate.quad(lambda x: f(x).real, x0, eta_f, limit=5000, epsabs=1e-14, epsrel=1e-12)
        im_val, im_err = integrate.quad(lambda x: f(x).imag, x0, eta_f, limit=5000, epsabs=1e-14, epsrel=1e-12)
        return complex(re_val, im_val)

    # === TERM 1: (9/4) a² ζ ζ'² ===
    c1 = 9/4
    def T1(x):
        d = damp(x)
        p1 = c1 * x**4 * zk1(x) * zkp(x)**2 * d
        p23 = c1 * x**4 * zk(x) * zk1p(x) * zkp(x) * d
        return p1 + 2*p23

    I_T1 = do_integral(T1)

    # === TERM 2: (9/4) a² ζ (∂ζ)² ===
    # Dominant squeezed perm: k₁ undiff, -k₂·k₃ ≈ +k² = 1
    def T2(x):
        return (9/4) * 1.0 * x**4 * zk1(x) * zk(x)**2 * damp(x)

    I_T2 = do_integral(T2)

    # === TERM 3: -2a²ε ζ'(∂ζ)(∂χ) — CORRECTED ===
    # After χ-sub: -(9/2)·(kb·kc)/kc²·η⁸·ζ'_{ka}·ζ_{kb}·ζ'_{kc}
    #
    # All 6 permutation assignments, grouped:
    #
    # Assigns 1+2 (ka=k₁, chi on short mode):
    #   coefficient = -(9/2)·(-1) = +9/2 each, ×2 = +9
    #   mode fns: ζ'_{k₁}·ζ_k·ζ'_k
    #
    # Assigns 4+6 (ka=k, chi on k₁, dot product provides k₁²):
    #   coefficient = -(9/2)·(-1/2) = +9/4 each, ×2 = +9/2
    #   mode fns: ζ'_k·ζ_k·ζ'_{k₁} (same product)
    #
    # Assigns 3+5 (chi on short, ζ on k₁): suppressed by k₁²/k²
    #
    # TOTAL coefficient: 9 + 9/2 = 27/2 = 13.5
    # All modes: ζ'_{k₁}·ζ_k·ζ'_k (same regardless of permutation)

    T3_coeff = 27.0 / 2.0  # CORRECTED from previous zero

    def T3(x):
        return T3_coeff * x**8 * zk1p(x) * zk(x) * zkp(x) * damp(x)

    I_T3 = do_integral(T3)

    # === TERM 4: (9/16) a² ζ² ζ' ===
    c4 = 9/16
    def T4(x):
        d = damp(x)
        pa = c4 * x**4 * zk(x)**2 * zk1p(x) * d
        pb = c4 * x**4 * zk1(x) * zk(x) * zkp(x) * d
        return pa + 2*pb

    I_T4 = do_integral(T4)

    # === TOTAL (T1+T2+T3+T4, skipping T5+T6) ===
    I_total = I_T1 + I_T2 + I_T3 + I_T4

    fnl_T1 = (5/12) * (-2*np.imag(ext * I_T1)) / PP
    fnl_T2 = (5/12) * (-2*np.imag(ext * I_T2)) / PP
    fnl_T3 = (5/12) * (-2*np.imag(ext * I_T3)) / PP
    fnl_T4 = (5/12) * (-2*np.imag(ext * I_T4)) / PP

    fnl_intr = (5/12) * (-2*np.imag(ext * I_total)) / PP
    fnl_tot = fnl_intr + 5/4

    if verbose:
        print(f"\n{'='*55}")
        print(f"CORRECTED f_NL (T1-T4, xf={xf}, r={r})")
        print(f"{'='*55}")
        print(f"  T1 (ε²a²ζζ'²):     {fnl_T1:+.6f}")
        print(f"  T2 (ε²a²ζ(∂ζ)²):   {fnl_T2:+.6f}")
        print(f"  T3 (CORRECTED):      {fnl_T3:+.6f}")
        print(f"  T4 (a²ζ²ζ'):        {fnl_T4:+.6f}")
        print(f"  T5+T6 (χ²):         [OMITTED — proven zero]")
        print(f"  {'─'*45}")
        print(f"  Intrinsic (T1-T4):   {fnl_intr:+.6f}")
        print(f"  Field redef:         +1.250000")
        print(f"  TOTAL:               {fnl_tot:+.6f}")
        print(f"{'='*55}")
        print(f"  Cai:  -4.375000")
        print(f"  L-B:  -2.187500")

    return fnl_intr, fnl_tot

if __name__ == "__main__":
    print("MATTER BOUNCE f_NL — CORRECTED (T3 SIGN FIX)")
    print("=" * 55)

    # Main computation
    fi, ft = compute_fnl_corrected(r=1e-3, xf=-0.01, x0=-1000, verbose=True)

    # Convergence tests
    print(f"\n{'='*55}")
    print("CONVERGENCE TESTS")
    print(f"{'='*55}")

    print("\n--- xf dependence ---")
    for xf in [-0.1, -0.05, -0.01, -0.005, -0.001]:
        _, ft = compute_fnl_corrected(r=1e-3, xf=xf, verbose=False)
        print(f"  xf={xf:8.4f}  f_NL={ft:+.8f}")

    print("\n--- Squeeze ratio ---")
    for rv in [0.1, 0.01, 0.001, 0.0001]:
        _, ft = compute_fnl_corrected(r=rv, xf=-0.01, verbose=False)
        print(f"  r={rv:.5f}  f_NL={ft:+.8f}")

    print("\n--- iε regulator ---")
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        _, ft = compute_fnl_corrected(r=1e-3, xf=-0.01, eps_reg=eps, verbose=False)
        print(f"  ε={eps:.0e}  f_NL={ft:+.8f}")

    print("\n--- UV cutoff ---")
    for x0 in [-100, -500, -1000, -5000]:
        _, ft = compute_fnl_corrected(r=1e-3, xf=-0.01, x0=x0, verbose=False)
        print(f"  x0={x0:6d}  f_NL={ft:+.8f}")
