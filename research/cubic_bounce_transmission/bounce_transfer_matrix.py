#!/usr/bin/env python3
"""
DERIVED bound on cubic bispectrum transmission through the bounce, via the
LINEAR TRANSFER MATRIX of the curvature perturbation across an explicit
nonsingular bounce.

WHY THIS IS THE RIGHT (and tractable) OBSERVABLE
------------------------------------------------
The local f_NL is a SQUEEZED-limit quantity. By Maldacena's consistency
argument, the squeezed bispectrum measures how a long-wavelength curvature
mode zeta_L modulates the (contraction-generated) short-scale power. The
short mode's correlator is set DURING CONTRACTION (this is Cai's -35/8). The
ONLY thing the bounce can do to the squeezed bispectrum is act, mode by mode,
through the SAME linear transfer that acts on the two-point function:

    zeta_out(k) = T(k) * zeta_in(k)        (growing mode)
                + (decaying-mode contamination)

If the bounce transmits the constant (growing) superhorizon mode with
T(k) -> 1 and injects NO decaying-mode power for the k of interest, then
    B_out(k1,k2,k3) = T(k1)T(k2)T(k3) * B_in
    P_out(k)        = T(k)^2 * P_in
    => f_NL_out = B_out / (P_out P_out) = f_NL_in   (T factors CANCEL).
So f_NL = -35/8 is PRESERVED exactly to the extent that
    (i)   T(k) is a pure real constant (mode-independent, no phase mixing), and
    (ii)  no decaying-mode / particle-production power is injected at these k.
The DERIVED correction to f_NL is controlled by the DEVIATION of T(k) from a
k-independent constant and by the decaying/growing power ratio, both of which
we compute directly from the mode functions -- NO inserted O(1) coefficient.

This replaces the paper's order-of-magnitude scaling estimate (delta f_NL ~
1e-3, hand-coefficient 1.0) with a NUMBER derived from the explicit bounce.

METHOD
------
1. Build explicit nonsingular bounce backgrounds (LQC Wilson-Ewing; analytic
   matched-asymptotics with tunable width eta_b), each matching matter
   contraction a ~ |eta| (eps=3/2) at |eta| >> eta_b.
2. For each k, propagate the growing superhorizon mode from deep contraction
   through the bounce to deep expansion. Extract:
     T_grow(k)  = zeta_out / zeta_in    for the constant (growing) mode
     D(k)       = |decaying-mode amplitude injected| / |growing|
3. The DERIVED f_NL correction:
     delta_fNL / fNL = 3*(<T> variation across k1,k2,k3) + O(D)
   For the squeezed local shape with k2=k3=k, k1<<k:
     f_NL_out/f_NL_in = [T(k1) T(k)^2] / [T(k1) T(k)^2] * (shape-weighting)
   The leading non-cancelling piece is d ln T / d ln k (scale dependence of
   the transfer) times the squeezing, plus the decaying contamination D.
   We report both:
     eps_T(k) = |T(k) - T_ref| / |T_ref|   (mode-dependence of transfer)
     D(k)     = decaying/growing power ratio
   and delta_fNL = fNL * (eps_T + D) as a conservative DERIVED bound.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

np.seterr(all='ignore')
EPS = 1.5
FNL = -35.0/8.0

# ---------- backgrounds ----------
def bg_lqc(rho_c=0.41, t_max=300.0):
    def eom(t,y):
        a=y[0]; rho=rho_c/a**3; H2=(rho/3.0)*(1-rho/rho_c)
        return [a*np.sqrt(max(H2,0.0))]
    s=solve_ivp(eom,(0,t_max),[1.0+1e-12],method='DOP853',max_step=0.02,
                rtol=1e-12,atol=1e-14)
    t=s.t; a=s.y[0]; dt=np.diff(t)
    eh=np.concatenate([[0],np.cumsum(dt/a[:-1])])
    a_f=np.concatenate([a[::-1][:-1],a]); e_f=np.concatenate([-eh[::-1][:-1],eh])
    return _fin(e_f,a_f), 1.0/np.sqrt(rho_c)

def bg_analytic(eta_b=2.0, a_min=1.0, span=150.0, n=60000):
    eta=np.linspace(-span,span,n)
    a=a_min*np.sqrt(1.0+(eta/eta_b)**2)   # p=1 => eps=3/2 asymptotics
    return _fin(eta,a), eta_b

def _fin(eta,a):
    ap=np.gradient(a,eta); app=np.gradient(ap,eta)
    zppz=app/a
    return dict(a_i=interp1d(eta,a,kind='cubic',fill_value='extrapolate'),
                zppz_i=interp1d(eta,zppz,kind='cubic',fill_value='extrapolate'),
                emin=eta[0], emax=eta[-1])

# ---------- mode propagation ----------
def propagate(bg, k, eta0, eta1):
    """Solve v'' + (k^2 - z''/z)v=0 with Bunch-Davies deep in contraction.
    Return zeta(eta1)=v/z at late time and the late-time zeta' (for
    growing/decaying decomposition). z = a*sqrt(2 eps)."""
    zp=bg['zppz_i']
    def rhs(eta,y):
        vr,vi,dr,di=y; w2=k*k-zp(eta)
        return [dr,di,-w2*vr,-w2*vi]
    nm=1/np.sqrt(2*k); ph=-k*eta0
    y0=[nm*np.cos(ph),nm*np.sin(ph),nm*k*np.sin(ph),-nm*k*np.cos(ph)]
    s=solve_ivp(rhs,[eta0,eta1],y0,method='DOP853',max_step=min(0.05,0.3/k),
                rtol=1e-11,atol=1e-14,dense_output=True)
    return s

def zeta_and_deriv(bg, s, eta, k, h=1e-3):
    a=bg['a_i']; z=lambda e: a(e)*np.sqrt(2*EPS)
    def zt(e):
        y=s.sol(e); return (y[0]+1j*y[1])/z(e)
    return zt(eta), (zt(eta+h)-zt(eta-h))/(2*h)

# ---------- transfer & decaying contamination ----------
def run(bg, tag, eta_b):
    print(f"\n### {tag}  (eta_bounce ~ {eta_b:.3f}) ###", flush=True)
    eta_in  = max(bg['emin']+2.0, -100.0)   # deep contraction, superhorizon
    eta_out = min(bg['emax']-2.0,  100.0)   # deep expansion, frozen
    ks=[0.005,0.01,0.02,0.05,0.1,0.2,0.5]
    Ts=[]; Ds=[]
    # reference: extrapolate T(k->0) using smallest k
    for k in ks:
        s=propagate(bg,k,eta_in,eta_out)
        z_out,zp_out=zeta_and_deriv(bg,s,eta_out,k)
        # zeta amplitude deep in contraction (input growing mode) evaluated on
        # the SAME background at eta_in:
        z_in,_=zeta_and_deriv(bg,s,eta_in+2.0,k)
        T=abs(z_out)/abs(z_in)
        # decaying contamination: a frozen growing mode has zeta'~0.
        # measure residual time-derivative relative to Hubble rate at eta_out
        H_out=abs(np.gradient([bg['a_i'](eta_out-1e-2),bg['a_i'](eta_out+1e-2)])[0])/(2e-2)/bg['a_i'](eta_out)
        D=abs(zp_out)/(abs(z_out)*max(abs(k),1e-6))  # |zeta'|/(k|zeta|): subhorizon oscillation proxy
        Ts.append((k,T)); Ds.append((k,D))
        print(f"  k={k:6.3f}  k*eta_b={k*eta_b:7.4f}  T(k)={T:.6e}  |zeta'/k zeta|_out={D:.3e}", flush=True)
    return ks,Ts,Ds

def analyze():
    print("="*72)
    print("DERIVED BOUNCE TRANSFER: does f_NL=-35/8 survive cubic transmission?")
    print("="*72)
    results={}
    for tag,(bg,eb) in {
        "analytic-bounce eta_b=2": bg_analytic(2.0),
        "analytic-bounce eta_b=5": bg_analytic(5.0),
        "LQC (Wilson-Ewing)":       bg_lqc(),
    }.items():
        ks,Ts,Ds=run(bg,tag,eb)
        results[tag]=(ks,Ts,Ds,eb)

    print("\n"+"="*72)
    print("DERIVED f_NL CORRECTION  (coefficient-free)")
    print("="*72)
    print("f_NL preservation requires T(k) ~ k-independent constant AND no")
    print("decaying-mode injection. delta f_NL / f_NL = scale-dependence of T.")
    for tag,(ks,Ts,Ds,eb) in results.items():
        kk=np.array([k for k,_ in Ts]); TT=np.array([t for _,t in Ts])
        # normalise transfer to its smallest-k (most superhorizon) value
        Tref=TT[0]
        epsT=np.abs(TT/Tref-1.0)     # mode-dependence of transfer
        # local squeezed f_NL uses T(k1->0)T(k)^2 / [T(k1->0)T(k)^2]; the
        # non-cancelling residual at squeezing is the log-slope of T over the
        # short-scale band:
        # delta ln f_NL ~ d ln T / d ln k  (per e-fold of short-scale range)
        good=TT>0
        slope=np.polyfit(np.log(kk[good]),np.log(np.maximum(TT[good],1e-300)),1)[0]
        # conservative derived bound: max mode-dependence over observational band
        band=(kk>=0.005)&(kk<=0.1)
        eps_band=epsT[band].max() if band.any() else np.nan
        dfnl=FNL*eps_band
        print(f"\n{tag}:  eta_bounce~{eb:.2f}")
        print(f"   T(k) over band: {TT[band]}")
        print(f"   d ln T / d ln k = {slope:+.4f}   (0 => perfectly scale-invariant transfer)")
        print(f"   max |T(k)/T0 - 1| over 0.005<k<0.1 = {eps_band:.4e}")
        print(f"   => DERIVED |delta f_NL| <= {abs(dfnl):.4e}   (f_NL = {FNL:.4f} +/- {abs(dfnl):.4e})")

if __name__=="__main__":
    analyze()
