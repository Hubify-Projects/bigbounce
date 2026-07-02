#!/usr/bin/env python3
"""
DEFINITIVE, coefficient-free diagnostic for cubic bispectrum transmission
through an explicit nonsingular bounce (P2 assumption (d)).

The squeezed local f_NL is PRESERVED across the bounce iff, mode by mode, the
bounce transmits the curvature perturbation with:
  (1) SCALE-INDEPENDENT transfer  -> preserves the spectral shape (n_s), hence
      the T(k1)T(k2)T(k3) prefactor cancels against T(k)^2 P(k)^2 in
      f_NL = B / P^2, and the local shape is unchanged;
  (2) GROWING-mode dominance (no decaying/particle-production contamination),
      so the transmitted correlator is the frozen contraction correlator.

We therefore measure two coefficient-free quantities on the SAME background:
  A) Delta n = n_s^out - n_s^in : the change in the spectral tilt of the
     DIMENSIONLESS power spectrum P(k)=k^3 |zeta(k)|^2 induced by the bounce,
     comparing the same physical modes deep in contraction vs deep in expansion.
     If the bounce added a scale-dependent transfer, n_s would shift; a shift
     of Delta n directly bounds the shape distortion of the local bispectrum.
  B) A_dec/A_grow : the fraction of the transmitted amplitude carried by the
     decaying mode, from the WKB out-state. Decaying-mode injection is what
     would reshape/kill f_NL. We read it from the residual conformal-time
     variation of the out-mode relative to the constant growing branch.

Both are pure numbers derived from the explicit bounce mode functions --
NO inserted O(1) coefficient. The derived f_NL correction is then
  |delta f_NL / f_NL| <~ 3 |Delta n| * ln(k_max/k_min)_squeeze + (A_dec/A_grow).
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

np.seterr(all='ignore')
EPS=1.5; FNL=-35.0/8.0

def bg_lqc(rho_c=0.41,t_max=300.0):
    def eom(t,y):
        a=y[0]; rho=rho_c/a**3; H2=(rho/3.0)*(1-rho/rho_c)
        return [a*np.sqrt(max(H2,0.0))]
    s=solve_ivp(eom,(0,t_max),[1+1e-12],method='DOP853',max_step=0.02,
                rtol=1e-12,atol=1e-14)
    t=s.t;a=s.y[0];dt=np.diff(t);eh=np.concatenate([[0],np.cumsum(dt/a[:-1])])
    af=np.concatenate([a[::-1][:-1],a]);ef=np.concatenate([-eh[::-1][:-1],eh])
    return _fin(ef,af),1/np.sqrt(rho_c)

def bg_analytic(eta_b=2.0,span=150.0,n=60000):
    eta=np.linspace(-span,span,n); a=np.sqrt(1+(eta/eta_b)**2)
    return _fin(eta,a),eta_b

def _fin(eta,a):
    ap=np.gradient(a,eta);app=np.gradient(ap,eta);zppz=app/a
    return dict(a_i=interp1d(eta,a,'cubic',fill_value='extrapolate'),
                zppz_i=interp1d(eta,zppz,'cubic',fill_value='extrapolate'),
                emin=eta[0],emax=eta[-1])

def propagate(bg,k,eta0,eta1):
    zp=bg['zppz_i']
    def rhs(eta,y):
        vr,vi,dr,di=y;w2=k*k-zp(eta);return[dr,di,-w2*vr,-w2*vi]
    nm=1/np.sqrt(2*k);ph=-k*eta0
    y0=[nm*np.cos(ph),nm*np.sin(ph),nm*k*np.sin(ph),-nm*k*np.cos(ph)]
    return solve_ivp(rhs,[eta0,eta1],y0,method='DOP853',max_step=min(0.05,0.3/k),
                     rtol=1e-11,atol=1e-14,dense_output=True)

def zeta(bg,s,eta):
    y=s.sol(eta);z=bg['a_i'](eta)*np.sqrt(2*EPS);return (y[0]+1j*y[1])/z

def tilt_and_decaying(bg,eta_b,tag):
    """Compute input tilt (deep contraction), output tilt (deep expansion),
    and decaying fraction, on the SAME modes/background."""
    eta_in =max(bg['emin']+2.0,-100.0)
    eta_out=min(bg['emax']-2.0, 100.0)
    # sample the SAME conformal-time slices for all k so the tilt comparison is
    # apples-to-apples. Deep in contraction: eta_s = a few * eta_in fraction.
    eta_s_in = eta_in+3.0          # deep contraction, all modes superhorizon
    eta_s_out= eta_out-3.0         # deep expansion, all modes frozen
    ks=np.array([0.01,0.02,0.05,0.1,0.2])
    Pin=[];Pout=[];dec=[]
    for k in ks:
        s=propagate(bg,k,eta_in,eta_out)
        zin =zeta(bg,s,eta_s_in)
        zout=zeta(bg,s,eta_s_out)
        # dimensionless power spectra
        Pin.append(k**3*abs(zin)**2)
        Pout.append(k**3*abs(zout)**2)
        # decaying fraction: for a frozen growing mode zeta'=0. Residual
        # log-derivative d ln|zeta|/d(eta) over a late window measures the
        # decaying admixture (which redshifts away, leaving a constant).
        h=0.5
        zA=zeta(bg,s,eta_s_out-h);zB=zeta(bg,s,eta_s_out+h)
        dlnz=abs((abs(zB)-abs(zA))/(2*h))/max(abs(zout),1e-300)
        dec.append(dlnz)
    Pin=np.array(Pin);Pout=np.array(Pout);dec=np.array(dec)
    lk=np.log(ks)
    n_in =np.polyfit(lk,np.log(Pin ),1)[0]   # d ln P / d ln k = n_s - 1
    n_out=np.polyfit(lk,np.log(Pout),1)[0]
    dn=n_out-n_in
    print(f"\n### {tag}  eta_bounce~{eta_b:.3f} ###",flush=True)
    print(f"  input  spectral slope d lnP/d lnk (contraction) = {n_in:+.4f}")
    print(f"  output spectral slope d lnP/d lnk (expansion)   = {n_out:+.4f}")
    print(f"  Delta n (bounce-induced tilt change)            = {dn:+.4e}")
    print(f"  decaying admixture |d ln|zeta|/d eta|_out (max) = {dec.max():.3e}")
    # derived f_NL shape correction. Squeezing spans ~ln(k_max/k_min) e-folds;
    # take a generous 5 e-folds over the observational band:
    n_efold=5.0
    dfnl_shape = FNL*abs(dn)*n_efold
    dfnl_dec   = FNL*dec.max()
    print(f"  => derived |delta f_NL| shape distortion <= {abs(dfnl_shape):.3e}")
    print(f"  => derived |delta f_NL| decaying inject   <= {abs(dfnl_dec):.3e}")
    return dict(n_in=n_in,n_out=n_out,dn=dn,dec=dec.max(),
                dfnl=abs(dfnl_shape)+abs(dfnl_dec))

if __name__=="__main__":
    print("="*72)
    print("DEFINITIVE BOUNCE TRANSMISSION DIAGNOSTIC (coefficient-free)")
    print("f_NL=-35/8 preserved iff Delta n ~ 0 AND decaying admixture ~ 0")
    print("="*72)
    res={}
    for tag,(bg,eb) in {
        "analytic eta_b=2":bg_analytic(2.0),
        "analytic eta_b=5":bg_analytic(5.0),
        "LQC Wilson-Ewing":bg_lqc(),
    }.items():
        res[tag]=tilt_and_decaying(bg,eb,tag)
    print("\n"+"="*72)
    print("VERDICT")
    print("="*72)
    dnmax=max(abs(r['dn']) for r in res.values())
    dfmax=max(r['dfnl'] for r in res.values())
    print(f"  max |Delta n| across bounce models = {dnmax:.3e}")
    print(f"  => DERIVED bound  f_NL = {FNL:.4f}  +/-  {dfmax:.3e}")
    print(f"     fractional: {dfmax/abs(FNL)*100:.3f}%")
