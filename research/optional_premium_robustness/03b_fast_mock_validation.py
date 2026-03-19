#!/usr/bin/env python3
"""
Fast mock-based estimator realism validation.
100,000 synthetic P(k) observations with realistic nuisance injection.
Lean implementation: ~3ms per mock → ~6 min for 100k.
"""
import numpy as np
from scipy.optimize import minimize_scalar
import time

N_MOCKS = 100000
FNL_TRUE = -35.0/8.0
SEED = 42

# Cosmo
h=0.6736; Om=0.3153; dc=1.686; ns_=0.9649
def Tk(k):
    q=k/(0.073*Om*h)
    return np.log(1+2.34*q)/(2.34*q+1e-30)*(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**(-0.25)
def Dz(z):
    Oz=Om*(1+z)**3/(Om*(1+z)**3+1-Om)
    return (1/(1+z))*(5*Oz/2)/(Oz**(4./7)-(1-Oz)+(1+Oz/2)*(1+(1-Oz)/70))
D0 = Dz(0)
def Pm(k,z): return 2.1e-9*(k*h/0.05)**(ns_-1)*Tk(k)**2*(2*np.pi**2/k**3)*(Dz(z)/D0)**2*h**3
def db1(k,z,b1): return (b1-1)*3*dc*Om*(h/2997.9)**2/(k**2*Tk(k)*Dz(z)/D0+1e-30)

def run_survey(name, z, b1, ng, V_base, kmin_base, kmax, gr_sig, bphi_sig, mt_frac=1.0):
    rng = np.random.default_rng(SEED)
    np.random.seed(SEED+1)

    print(f"\n{'='*65}")
    print(f"MOCK VALIDATION: {name} ({N_MOCKS:,} mocks)")
    print(f"{'='*65}")
    t0 = time.time()

    fnl_rec = np.zeros(N_MOCKS)
    chi2_bounce = np.zeros(N_MOCKS)
    chi2_free = np.zeros(N_MOCKS)
    chi2_null = np.zeros(N_MOCKS)

    for i in range(N_MOCKS):
        # Randomize survey conditions
        kmin = kmin_base * np.clip(rng.lognormal(0, 0.3), 0.3, 5.0)
        kmin = np.clip(kmin, 1e-4, 5e-3)
        gr = rng.normal(0, gr_sig)
        bphi_err = rng.normal(0, bphi_sig)
        mt_ok = rng.random() < mt_frac
        V = V_base if mt_ok else V_base / 9.0

        k = np.geomspace(kmin, kmax, 25)
        pm = Pm(k, z)
        db = db1(k, z, b1)

        # TRUE signal (what nature produces)
        fnl_eff = FNL_TRUE * (1 + bphi_err) + gr  # effective f_NL including systematics
        bt = b1 + db * fnl_eff
        Pg = bt**2 * pm + 1.0/ng

        # Noise
        dk = np.diff(np.log(k), prepend=np.log(k[0])-0.1)
        Nm = np.maximum(V * k**2 * dk * k / (2*np.pi**2), 1)
        sig = Pg * np.sqrt(2.0/Nm)
        Pobs = Pg + np.random.randn(len(k)) * sig

        # FIT: recover f_NL from mock data
        def chi2(fnl):
            bt_ = b1 + db * fnl
            Pg_ = bt_**2 * pm + 1.0/ng
            return np.sum(((Pobs - Pg_)/sig)**2)

        res = minimize_scalar(chi2, bounds=(-15,15), method='bounded')
        fnl_rec[i] = res.x
        chi2_free[i] = res.fun
        chi2_bounce[i] = chi2(FNL_TRUE)
        chi2_null[i] = chi2(0.015)

        if (i+1) % 20000 == 0:
            elapsed = time.time() - t0
            eta = elapsed / (i+1) * N_MOCKS - elapsed
            print(f"  {i+1:>6,}/{N_MOCKS:,}  ETA: {eta:.0f}s")

    elapsed = time.time() - t0
    print(f"  Completed in {elapsed:.1f}s ({elapsed/N_MOCKS*1000:.1f} ms/mock)")

    # Bayes factor: bounce vs free (Laplace approx)
    # BF ≈ prior_range × exp(-Δχ²/2) where prior_range = 30 for [-15,+15]
    dchi2_bf = chi2_bounce - chi2_free
    bf_vs_free = 30 * np.exp(-np.clip(dchi2_bf, -100, 100) / 2)

    dchi2_bs = chi2_bounce - chi2_null
    bf_vs_ssfsr = np.exp(-np.clip(dchi2_bs, -500, 500) / 2)

    # Recovery check
    bias = np.median(fnl_rec) - FNL_TRUE
    scatter = np.std(fnl_rec)
    print(f"\n  f_NL recovery: median={np.median(fnl_rec):.3f}, true={FNL_TRUE:.3f}")
    print(f"  Bias: {bias:.3f}  Scatter: {scatter:.3f}")

    bf = np.clip(bf_vs_free, 1e-10, 1e10)
    print(f"\n  BOUNCE vs TUNED MULTIFIELD (mock-based):")
    print(f"    Median BF:           {np.median(bf):.1f}")
    print(f"    P(BF > 3) [moderate]:{np.mean(bf>3)*100:.1f}%")
    print(f"    P(BF > 10) [strong]: {np.mean(bf>10)*100:.1f}%")
    print(f"    P(BF > 30) [v.str]:  {np.mean(bf>30)*100:.1f}%")
    print(f"    P(BF < 1) [free wins]:{np.mean(bf<1)*100:.1f}%")

    bf2 = np.clip(bf_vs_ssfsr, 1e-30, 1e30)
    print(f"\n  BOUNCE vs STANDARD INFLATION (mock-based):")
    print(f"    Median BF:           {np.median(bf2):.1e}")
    print(f"    P(BF > 100):         {np.mean(bf2>100)*100:.1f}%")
    print(f"    P(BF < 1):           {np.mean(bf2<1)*100:.1f}%")

    return fnl_rec, bf, bf2

print("MOCK-BASED ESTIMATOR REALISM VALIDATION")
print(f"{N_MOCKS:,} synthetic power spectra per survey")

fnl_sp, bf_sp, bf_sp2 = run_survey(
    "SPHEREx-like", z=1.5, b1=1.8, ng=3e-3, V_base=30e9,
    kmin_base=3e-4, kmax=0.1, gr_sig=0.3, bphi_sig=0.15)

fnl_mm, bf_mm, bf_mm2 = run_survey(
    "MegaMapper-like", z=3.0, b1=3.0, ng=5e-4, V_base=100e9,
    kmin_base=2e-4, kmax=0.15, gr_sig=0.7, bphi_sig=0.2, mt_frac=0.7)

# COMBINED
bf_comb = bf_sp * bf_mm
bf_comb2 = bf_sp2 * bf_mm2
bf_comb = np.clip(bf_comb, 1e-10, 1e20)

print(f"\n{'='*65}")
print(f"COMBINED SPHEREx + MegaMapper (MOCK-BASED)")
print(f"{'='*65}")
print(f"  Median combined BF vs tuned: {np.median(bf_comb):.0f}")
print(f"  P(combined BF > 10):   {np.mean(bf_comb>10)*100:.1f}%")
print(f"  P(combined BF > 100):  {np.mean(bf_comb>100)*100:.1f}%")
print(f"  P(combined BF > 1000): {np.mean(bf_comb>1000)*100:.1f}%")
print(f"  P(combined BF < 1):    {np.mean(bf_comb<1)*100:.1f}%")

print(f"\n  Median combined BF vs SSFSR: {np.median(np.clip(bf_comb2,0,1e30)):.1e}")
print(f"  P(combined BF > 100 vs SSFSR): {np.mean(bf_comb2>100)*100:.1f}%")

print("\nDone.")
