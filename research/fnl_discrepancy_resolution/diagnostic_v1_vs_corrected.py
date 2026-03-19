#!/usr/bin/env python3
"""
Minimal diagnostic: compare v1 and corrected T1 computation side by side.
Find the factor-of-3 discrepancy.
"""
import numpy as np
from scipy import integrate

def ghat(x):
    return np.exp(-1j*x) * (1-1j/x) / x**2

def ghat_prime(x):
    return np.exp(-1j*x) * (-1j - 3.0/x + 3j/x**2) / x**2

r = 1e-3
xf = -0.01
x0 = -1000.0
eps_reg = 1e-4
damp = lambda x: np.exp(eps_reg * x)

# ======== MODE FUNCTIONS (identical in both) ========
def zk1(x): return ghat(r*x) / np.sqrt(6.0*r)
def zk(x): return ghat(x) / np.sqrt(6.0)
def zk1p(x): return np.sqrt(r) * ghat_prime(r*x) / np.sqrt(6.0)
def zkp(x): return ghat_prime(x) / np.sqrt(6.0)

# ======== EXTERNAL AND PP (identical) ========
ext = np.conj(zk1(xf)) * np.conj(zk(xf))**2
P1 = np.abs(zk1(xf))**2
Pk = np.abs(zk(xf))**2
PP = P1 * Pk

print(f"ext = {ext:.6e}")
print(f"P1  = {P1:.6e}")
print(f"Pk  = {Pk:.6e}")
print(f"PP  = {PP:.6e}")

# ======== V1 APPROACH ========
# Integrate WITHOUT coefficient, apply eps^2 outside
def v1_perm1(x):
    return x**4 * zk1(x) * zkp(x)**2 * damp(x)
def v1_perm23(x):
    return x**4 * zk(x) * zk1p(x) * zkp(x) * damp(x)

def do_integral(f):
    rr, _ = integrate.quad(lambda x: f(x).real, x0, xf, limit=5000, epsabs=1e-14, epsrel=1e-12)
    ii, _ = integrate.quad(lambda x: f(x).imag, x0, xf, limit=5000, epsabs=1e-14, epsrel=1e-12)
    return complex(rr, ii)

I1_v1 = do_integral(v1_perm1)
I23_v1 = do_integral(v1_perm23)
I_total_v1 = I1_v1 + 2*I23_v1

eps2 = 2.25  # (3/2)^2 = 9/4
B_v1 = -2.0 * eps2 * np.imag(ext * I_total_v1)
fnl_v1 = (5.0/12.0) * B_v1 / PP

print(f"\n=== V1 APPROACH ===")
print(f"I1 = {I1_v1:.6e}")
print(f"I23= {I23_v1:.6e}")
print(f"Itot={I_total_v1:.6e}")
print(f"ext*Itot = {ext*I_total_v1:.6e}")
print(f"Im[ext*Itot] = {np.imag(ext*I_total_v1):.6e}")
print(f"B_v1 = {B_v1:.6e}")
print(f"f_NL_v1 (intrinsic) = {fnl_v1:.8f}")
print(f"f_NL_v1 (total)     = {fnl_v1+1.25:.8f}")

# ======== CORRECTED APPROACH ========
# Integrate WITH coefficient inside
c1 = 9.0/4.0
def corr_T1(x):
    d = damp(x)
    p1 = c1 * x**4 * zk1(x) * zkp(x)**2 * d
    p23 = c1 * x**4 * zk(x) * zk1p(x) * zkp(x) * d
    return p1 + 2*p23

I_T1_corr = do_integral(corr_T1)
B_corr = -2.0 * np.imag(ext * I_T1_corr)
fnl_corr = (5.0/12.0) * B_corr / PP

print(f"\n=== CORRECTED APPROACH ===")
print(f"I_T1 = {I_T1_corr:.6e}")
print(f"ext*I_T1 = {ext*I_T1_corr:.6e}")
print(f"Im[ext*I_T1] = {np.imag(ext*I_T1_corr):.6e}")
print(f"B_corr = {B_corr:.6e}")
print(f"f_NL_corr (intrinsic) = {fnl_corr:.8f}")
print(f"f_NL_corr (total)     = {fnl_corr+1.25:.8f}")

# ======== ALGEBRAIC CHECK ========
print(f"\n=== ALGEBRAIC CHECK ===")
print(f"c1 * I_total_v1 = {c1*I_total_v1:.6e}")
print(f"I_T1_corr       = {I_T1_corr:.6e}")
print(f"Ratio: {I_T1_corr/(c1*I_total_v1):.6f}")
print(f"B_v1 / B_corr = {B_v1/B_corr:.6f}")
print(f"fnl_v1 / fnl_corr = {fnl_v1/fnl_corr:.6f}")
