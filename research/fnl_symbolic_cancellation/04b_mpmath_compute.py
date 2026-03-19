#!/usr/bin/env python3
"""
High-precision f_NL computation using mpmath for all 6 Maldacena terms.
Integrates complex integrands by splitting into real and imaginary parts.
"""
from mpmath import mp, mpf, mpc, quad, exp, sqrt, fabs, re as mpre, im as mpim, j

mp.dps = 40  # 40 decimal digits of precision

def ghat(x):
    return exp(-j*x) * (1 - j/x) / x**2

def ghat_prime(x):
    return exp(-j*x) * (-j - mpf(3)/x + 3*j/x**2) / x**2

def compute_fnl(r_val, xf_val, x0_val, verbose=True):
    r = mpf(r_val)
    xf = mpf(xf_val)
    x0 = mpf(x0_val)
    eps_reg = mpf('1e-4')

    # External and power spectra at xf
    gk_f = ghat(xf)
    gk1_f = ghat(r * xf)
    ext = gk1_f.conjugate() * (gk_f.conjugate())**2

    Pk1 = fabs(gk1_f)**2 / (6*r)
    Pk = fabs(gk_f)**2 / mpf(6)
    PP = Pk1 * Pk

    # Mode functions
    def zk(x): return ghat(x) / sqrt(mpf(6))
    def zk1(x): return ghat(r*x) / sqrt(6*r)
    def zkp(x): return ghat_prime(x) / sqrt(mpf(6))
    def zk1p(x): return sqrt(r) * ghat_prime(r*x) / sqrt(mpf(6))
    def chi_k1(x): return mpf('-1.5') * x**4 * zk1p(x) / r**2
    def chi_k(x): return mpf('-1.5') * x**4 * zkp(x)

    damp = lambda x: exp(eps_reg * x)

    # Integrate by splitting Re and Im (mpmath.quad needs scalar)
    def integrate_complex(f, a, b):
        re_part = quad(lambda x: mpre(f(x)), [a, b], method='tanh-sinh', maxdegree=6)
        im_part = quad(lambda x: mpim(f(x)), [a, b], method='tanh-sinh', maxdegree=6)
        return mpc(re_part, im_part)

    # T1: (9/4) a² ζ ζ'² (all 3 perms)
    c1 = mpf(9)/mpf(4)
    def T1(x):
        d = damp(x)
        p1 = c1 * x**4 * zk1(x) * zkp(x)**2 * d
        p23 = c1 * x**4 * zk(x) * zk1p(x) * zkp(x) * d
        return p1 + 2*p23

    if verbose: print("T1...", end=" ", flush=True)
    I_T1 = integrate_complex(T1, x0, xf)
    if verbose: print("done")

    # T2: (9/4) a² ζ (∂ζ)² — dominant perm only
    c2 = mpf(9)/mpf(4)
    def T2(x):
        return c2 * x**4 * zk1(x) * zk(x)**2 * damp(x)  # -k₂·k₃ ≈ +1

    if verbose: print("T2...", end=" ", flush=True)
    I_T2 = integrate_complex(T2, x0, xf)
    if verbose: print("done")

    # T3: after χ-sub, finite terms only
    def T3(x):
        d = damp(x)
        # Perm with χ_{k₁} (×2): (9/4)η⁸ ζ'_k ζ_k ζ'_{k₁}
        p1 = mpf(9)/mpf(4) * x**8 * zkp(x) * zk(x) * zk1p(x) * d
        # Perm ka=k₁, χ_k: -(9/2)·(-1)·η⁸ ζ'_{k₁} ζ_k ζ'_k = (9/2)·η⁸·...
        # Careful: coefficient is (9/2)·(k₂·k₃/k₃²) with k₂·k₃=-1, k₃²=1 → -(9/2)
        p2 = mpf(-9)/mpf(2) * x**8 * zk1p(x) * zk(x) * zkp(x) * d
        return 2*p1 + p2

    if verbose: print("T3...", end=" ", flush=True)
    I_T3 = integrate_complex(T3, x0, xf)
    if verbose: print("done")

    # T4: (9/16) a² ζ² ζ' (all 3 perms)
    c4 = mpf(9)/mpf(16)
    def T4(x):
        d = damp(x)
        pa = c4 * x**4 * zk(x)**2 * zk1p(x) * d
        pb = c4 * x**4 * zk1(x) * zk(x) * zkp(x) * d
        return pa + 2*pb

    if verbose: print("T4...", end=" ", flush=True)
    I_T4 = integrate_complex(T4, x0, xf)
    if verbose: print("done")

    # T5+T6: using explicit chi
    def T56(x):
        d = damp(x)
        c1_val = chi_k1(x)
        ck_val = chi_k(x)
        # T5 perm (b+c): (3/4)·k²·(k₁·k)/(k₁²k²)·ζ_k·χ_{k₁}·χ_k × 2
        # = (3/4)·(-r²/2)/(r²)·ζ_k·c1·ck × 2 ... wait, let me use explicit chi
        # T5: (3/4)·∂²ζ·(∂χ)²
        # Fourier: (3/4)·k_a²·(k_b·k_c)·ζ_{ka}·χ_{kb}·χ_{kc}
        # Perm b (ka=k, kb=k₁, kc=k): (3/4)·1·(-r²/2)·zk·c1·ck
        t5_bc = 2 * mpf(3)/mpf(4) * (-r**2/2) * zk(x) * c1_val * ck_val * d
        # T6: (9/32)·(-k_a²)·ζ_{ka}·χ_{kb}·χ_{kc}
        # Perm b+c: 2·(9/32)·(-1)·zk·c1·ck
        t6_bc = 2 * mpf(9)/mpf(32) * mpf(-1) * zk(x) * c1_val * ck_val * d
        return t5_bc + t6_bc

    if verbose: print("T5+T6...", end=" ", flush=True)
    I_T56 = integrate_complex(T56, x0, xf)
    if verbose: print("done")

    # Assemble
    I_total = I_T1 + I_T2 + I_T3 + I_T4 + I_T56

    fnl_T1 = mpf(5)/mpf(12) * (-2*mpim(ext*I_T1)) / PP
    fnl_T2 = mpf(5)/mpf(12) * (-2*mpim(ext*I_T2)) / PP
    fnl_T3 = mpf(5)/mpf(12) * (-2*mpim(ext*I_T3)) / PP
    fnl_T4 = mpf(5)/mpf(12) * (-2*mpim(ext*I_T4)) / PP
    fnl_T56 = mpf(5)/mpf(12) * (-2*mpim(ext*I_T56)) / PP

    fnl_intr = mpf(5)/mpf(12) * (-2*mpim(ext*I_total)) / PP
    fnl_tot = fnl_intr + mpf(5)/mpf(4)

    if verbose:
        print(f"\n{'='*55}")
        print(f"f_NL (mpmath {mp.dps}dp, xf={xf_val}, r={r_val})")
        print(f"{'='*55}")
        print(f"  T1:       {float(fnl_T1):+.8f}")
        print(f"  T2:       {float(fnl_T2):+.8f}")
        print(f"  T3:       {float(fnl_T3):+.8f}")
        print(f"  T4:       {float(fnl_T4):+.8f}")
        print(f"  T5+T6:    {float(fnl_T56):+.8f}")
        print(f"  {'─'*45}")
        print(f"  Intrinsic:{float(fnl_intr):+.8f}")
        print(f"  FR:       +1.25000000")
        print(f"  TOTAL:    {float(fnl_tot):+.8f}")
        print(f"{'='*55}")
        print(f"  Cai:  -4.375000")
        print(f"  L-B:  -2.187500")

    return float(fnl_intr), float(fnl_tot)

if __name__ == "__main__":
    print("MATTER BOUNCE f_NL — MPMATH HIGH PRECISION (ALL 6 TERMS)")
    print("=" * 55)

    fi, ft = compute_fnl(r_val=1e-3, xf_val=-0.5, x0_val=-200, verbose=True)

    print(f"\n{'='*55}")
    print("CONVERGENCE TESTS")
    print(f"{'='*55}")

    print("\n--- xf dependence ---")
    for xf in [-2.0, -1.0, -0.5, -0.3]:
        _, ft = compute_fnl(r_val=1e-3, xf_val=xf, x0_val=-200, verbose=False)
        print(f"  xf={xf:6.2f}  f_NL={ft:+.8f}")

    print("\n--- Squeeze ratio ---")
    for rv in [0.01, 0.001, 0.0001]:
        _, ft = compute_fnl(r_val=rv, xf_val=-0.5, x0_val=-200, verbose=False)
        print(f"  r={rv:.5f}  f_NL={ft:+.8f}")
