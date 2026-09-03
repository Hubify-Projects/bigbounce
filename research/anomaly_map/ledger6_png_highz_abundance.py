#!/usr/bin/env python3
"""
NEXT_SCIENCE_LEDGER item #6, first discriminator.

Local primordial non-Gaussianity (PNG) modification of the high-z halo/galaxy
abundance, evaluated at the lab's matter-contraction squeezed value
f_NL = -35/16 (ledger #1, CLOSED 2026-09-02), against the Cai et al. 2009
value -35/8 and the single-field Gaussian baseline f_NL = 0.

Method
------
1. Linear matter power spectrum from the Eisenstein & Hu (1998) no-wiggle
   transfer function (arXiv:astro-ph/9709112, Eqs. 28-31), normalised to sigma_8.
   No external data files: the whole calculation is analytic + quadrature.
2. Poisson kernel  M_R(k) = (2/3) k^2 T(k) W(kR) / (Omega_m H0^2)  connecting
   the primordial potential Phi to the smoothed density contrast delta_R.
3. Smoothed skewness for the local model
       <delta_R^3> = 6 f_NL /(8 pi^3) * int dk1 k1^2 int dk2 k2^2 int dmu
                     M_R(k1) P_Phi(k1) M_R(k2) P_Phi(k2) M_R(k12)
   with k12 = sqrt(k1^2 + k2^2 + 2 k1 k2 mu), from
       B_Phi(k1,k2,k3) = 2 f_NL [P_Phi(k1)P_Phi(k2) + 2 perms].
   S_3 = <delta_R^3> / sigma_R^4.
4. Non-Gaussian mass function: LoVerde, Miller, Shandera & Verde 2008
   (arXiv:0711.4126) Eq. (45), Edgeworth-corrected Press-Schechter:
       dn/dM ∝ exp(-nu^2/2) [ (nu + S_3 sigma/6 (nu^4 - 2 nu^2 - 1)) dlnsigma/dM
                              + (1/6) dS_3/dM sigma (nu^2 - 1) ]
   with nu = delta_c / sigma_M.  The reported discriminator is the ratio
       R(M,z,f_NL) = (dn/dM)_NG / (dn/dM)_G   [LMSV Eq. (46)],
   which is the standard multiplicative PNG correction applied to any Gaussian
   mass function; it is independent of the Gaussian fit used.
5. Redshift scaling: sigma(z) = sigma_0 D(z), S_3(z) = S_3(0)/D(z),
   nu(z) = delta_c / (sigma_0 D(z)),  D from the flat-LCDM growth integral.

Deterministic (no RNG). CPU-only, ~seconds.

Outputs: outputs/ledger6_png_highz_abundance.json
         outputs/ledger6_png_highz_abundance.png
"""

import json
import os
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

# ----------------------------------------------------------------- cosmology
# Planck 2018 TT,TE,EE+lowE+lensing+BAO (Planck 2018 VI, Table 2, last column)
OMEGA_M = 0.3153
OMEGA_B = 0.04930
H = 0.6736
NS = 0.9649
SIGMA8 = 0.8111
THETA27 = 2.7255 / 2.7
DELTA_C = 1.686
RHO_CRIT = 2.77536627e11          # h^2 Msun / Mpc^3
RHO_M = OMEGA_M * RHO_CRIT        # h^2 Msun / Mpc^3  (comoving, units h/Mpc)
H0 = 1.0 / 2997.92458             # H0 in (h/Mpc) units, i.e. c=1 with k in h/Mpc

FNL_VALUES = {
    "gaussian": 0.0,
    "lab_matter_contraction": -35.0 / 16.0,   # ledger #1 (CLOSED 2026-09-02)
    "cai2009": -35.0 / 8.0,                   # Cai et al. 2009 value (x2)
    "positive_control": +35.0 / 16.0,         # sign control only
}


def transfer_eh98_nowiggle(k):
    """Eisenstein & Hu 1998 zero-baryon 'shape' transfer function. k in h/Mpc."""
    om_h2 = OMEGA_M * H * H
    ob_h2 = OMEGA_B * H * H
    fb = OMEGA_B / OMEGA_M
    s = 44.5 * np.log(9.83 / om_h2) / np.sqrt(1.0 + 10.0 * ob_h2 ** 0.75)   # Mpc
    alpha = (1.0 - 0.328 * np.log(431.0 * om_h2) * fb
             + 0.38 * np.log(22.3 * om_h2) * fb * fb)
    # k*s wants k in Mpc^-1
    gamma_eff = OMEGA_M * H * (alpha + (1.0 - alpha) / (1.0 + (0.43 * k * H * s) ** 4))
    q = k * THETA27 ** 2 / gamma_eff
    L0 = np.log(2.0 * np.e + 1.8 * q)
    C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
    return L0 / (L0 + C0 * q * q)


def poisson_kernel(k):
    """M(k) = (2/3) k^2 T(k) / (Omega_m H0^2); delta(k) = M(k) Phi(k), z=0."""
    return (2.0 / 3.0) * k * k * transfer_eh98_nowiggle(k) / (OMEGA_M * H0 * H0)


def window_tophat(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    small = x < 1e-4
    out[small] = 1.0 - x[small] ** 2 / 10.0
    xs = x[~small]
    out[~small] = 3.0 * (np.sin(xs) - xs * np.cos(xs)) / xs ** 3
    return out


# --- primordial potential power spectrum, amplitude fixed by sigma_8 ---------
KPIV = 0.05 / H   # h/Mpc  (0.05 Mpc^-1)


def pphi_shape(k):
    """P_Phi(k) up to the overall amplitude A: A * k^(ns-4) with a pivot."""
    return (k / KPIV) ** (NS - 1.0) / k ** 3


def _sigma2_unnorm(R):
    def integrand(lnk):
        k = np.exp(lnk)
        return (k ** 3 / (2.0 * np.pi ** 2)) * poisson_kernel(k) ** 2 * pphi_shape(k) \
            * window_tophat(np.array([k * R]))[0] ** 2
    val, _ = quad(integrand, np.log(1e-5), np.log(200.0), limit=400)
    return val


A_PHI = SIGMA8 ** 2 / _sigma2_unnorm(8.0)


def pphi(k):
    return A_PHI * pphi_shape(k)


def sigma_of_R(R):
    return np.sqrt(A_PHI * _sigma2_unnorm(R))


def radius_of_mass(M):
    """Lagrangian top-hat radius (Mpc/h) for halo mass M (Msun/h)."""
    return (3.0 * M / (4.0 * np.pi * RHO_M)) ** (1.0 / 3.0)


# ------------------------------------------------------------ skewness S_3
def skewness_delta3(R, nk=140, nmu=48, kmin=1e-4, kmax=60.0):
    """<delta_R^3> per unit f_NL (i.e. the f_NL=1 value). Deterministic quadrature."""
    lnk = np.linspace(np.log(kmin), np.log(kmax), nk)
    k = np.exp(lnk)
    dlnk = lnk[1] - lnk[0]
    w_simpson = np.ones(nk)
    w_simpson[1:-1:2] = 4.0
    w_simpson[2:-1:2] = 2.0
    w_simpson *= dlnk / 3.0

    MR = poisson_kernel(k) * window_tophat(k * R)
    f = MR * pphi(k) * k ** 3          # k^3 from d^3k measure in log-k

    mu, wmu = leggauss(nmu)

    K1 = k[:, None, None]
    K2 = k[None, :, None]
    MU = mu[None, None, :]
    k12 = np.sqrt(np.clip(K1 ** 2 + K2 ** 2 + 2.0 * K1 * K2 * MU, 1e-30, None))
    M12 = poisson_kernel(k12) * window_tophat(k12 * R)

    integ = (f[:, None, None] * f[None, :, None] * M12) * wmu[None, None, :]
    total = np.einsum('i,j,ijm->', w_simpson, w_simpson, integ)
    return 6.0 / (8.0 * np.pi ** 3) * total


# ------------------------------------------------------------------- growth
def growth_D(z):
    """Linear growth factor normalised to D(z=0)=1, flat LCDM."""
    def integrand(a):
        E = np.sqrt(OMEGA_M / a ** 3 + (1.0 - OMEGA_M))
        return 1.0 / (a * E) ** 3
    def D_unnorm(zz):
        a = 1.0 / (1.0 + zz)
        E = np.sqrt(OMEGA_M / a ** 3 + (1.0 - OMEGA_M))
        val, _ = quad(integrand, 1e-8, a, limit=200)
        return 2.5 * OMEGA_M * E * val
    return D_unnorm(z) / D_unnorm(0.0)


# ---------------------------------------------- LMSV 2008 Eq. (45) / (46)
def mass_function_ratio(M_grid, z, fnl, sig0, s3_0, dlnsig_dM, ds3_dM_0):
    """R = (dn/dM)_NG / (dn/dM)_G, LoVerde+2008 Eq. (45)/(46)."""
    D = growth_D(z)
    sig = sig0 * D
    S3 = fnl * s3_0 / D                     # S_3 = <d^3>/sigma^4 scales as 1/D
    dS3_dM = fnl * ds3_dM_0 / D
    nu = DELTA_C / sig
    num = ((nu + S3 * sig / 6.0 * (nu ** 4 - 2.0 * nu ** 2 - 1.0)) * dlnsig_dM
           + (1.0 / 6.0) * dS3_dM * sig * (nu ** 2 - 1.0))
    den = nu * dlnsig_dM
    return num / den


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(here, "outputs")
    os.makedirs(outdir, exist_ok=True)

    # halo-mass grid (Msun/h), spanning the plausible hosts of M* > 1e10 Msun
    logM = np.linspace(10.5, 13.5, 61)
    M = 10.0 ** logM
    R = np.array([radius_of_mass(m) for m in M])
    sig0 = np.array([sigma_of_R(r) for r in R])
    d3_0 = np.array([skewness_delta3(r) for r in R])     # per unit f_NL
    s3_0 = d3_0 / sig0 ** 4                              # S_3 per unit f_NL

    dlnsig_dM = np.gradient(np.log(sig0), M)
    ds3_dM_0 = np.gradient(s3_0, M)

    redshifts = [8.0, 10.0, 11.0, 12.0, 14.0]

    # M* > 1e10 Msun host-halo mass under a baryon-conversion efficiency eps
    f_b = OMEGA_B / OMEGA_M
    eps_cases = {"eps_0.05": 0.05, "eps_0.20": 0.20, "eps_0.50": 0.50, "eps_1.00": 1.00}
    Mstar_thresh = 1.0e10                                # Msun
    Mh_of_eps = {name: (Mstar_thresh / (eps * f_b)) * H   # Msun -> Msun/h
                 for name, eps in eps_cases.items()}

    results = {
        "cosmology": {"Omega_m": OMEGA_M, "Omega_b": OMEGA_B, "h": H,
                      "n_s": NS, "sigma8": SIGMA8, "delta_c": DELTA_C,
                      "source": "Planck 2018 VI Table 2 TT,TE,EE+lowE+lensing+BAO"},
        "method": {
            "transfer": "Eisenstein & Hu 1998 no-wiggle (astro-ph/9709112 Eqs. 28-31)",
            "mass_function": "LoVerde, Miller, Shandera & Verde 2008 (arXiv:0711.4126) Eq. (45)/(46)",
            "bispectrum": "local: B_Phi = 2 f_NL [P(k1)P(k2) + 2 perms]",
            "note": "R is the multiplicative PNG correction; independent of the Gaussian fit used.",
        },
        "fnl_values": FNL_VALUES,
        "sigma8_check": float(sigma_of_R(8.0)),
        "growth": {str(z): float(growth_D(z)) for z in redshifts},
        "S3_per_fnl_at_z0": {f"logMh_{lm:.2f}": float(v) for lm, v in zip(logM, s3_0)},
        "ratios": {},
        "threshold_cases": {},
    }

    for z in redshifts:
        results["ratios"][f"z{z:.1f}"] = {}
        for name, fnl in FNL_VALUES.items():
            Rm = mass_function_ratio(M, z, fnl, sig0, s3_0, dlnsig_dM, ds3_dM_0)
            results["ratios"][f"z{z:.1f}"][name] = {
                "logMh": [float(x) for x in logM],
                "ratio": [float(x) for x in Rm],
            }

    # --- headline numbers at the M* > 1e10 threshold -------------------------
    for epsname, Mh in Mh_of_eps.items():
        lm = np.log10(Mh)
        entry = {"Mh_Msun_over_h": float(Mh), "logMh": float(lm),
                 "eps": eps_cases[epsname], "f_b": float(f_b)}
        for z in redshifts:
            sub = {}
            for name, fnl in FNL_VALUES.items():
                Rm = mass_function_ratio(M, z, fnl, sig0, s3_0, dlnsig_dM, ds3_dM_0)
                sub[name] = float(np.interp(lm, logM, Rm))
            # equivalent shift in log10 Mh that would produce the same abundance
            # change in the Gaussian mass function (local logarithmic slope)
            D = growth_D(z)
            nu = DELTA_C / (np.interp(lm, logM, sig0) * D)
            dlnn_dlnM = np.gradient(
                np.log(np.exp(-0.5 * (DELTA_C / (sig0 * D)) ** 2)
                       * np.abs(dlnsig_dM) * DELTA_C / (sig0 * D)), np.log(M))
            slope = float(np.interp(lm, logM, dlnn_dlnM))
            sub["nu"] = float(nu)
            sub["dln_n_dln_Mh"] = slope
            for name in FNL_VALUES:
                if name == "gaussian":
                    continue
                sub[f"equiv_dlog10Mh_{name}"] = float(
                    np.log(sub[name]) / slope / np.log(10.0)) if slope != 0 else None
            entry[f"z{z:.1f}"] = sub
        results["threshold_cases"][epsname] = entry

    # --- confrontation: how large would |f_NL| have to be? -----------------
    # Solve for the f_NL that makes R(M_h, z) equal a target abundance factor.
    # The Edgeworth expansion is a LINEAR-response result in S_3*sigma; values
    # of |f_NL| that drive R far from 1 are outside its validity and are
    # reported as an ORDER-OF-MAGNITUDE requirement, not a prediction.
    conf = {}
    for epsname, eps in eps_cases.items():
        Mh = Mh_of_eps[epsname]
        lm = np.log10(Mh)
        sub = {}
        for z in [10.0, 11.0, 12.0]:
            r1 = np.interp(lm, logM,
                           mass_function_ratio(M, z, 1.0, sig0, s3_0,
                                               dlnsig_dM, ds3_dM_0))
            slope_per_fnl = r1 - 1.0          # dR/df_NL, linear by construction
            sub[f"z{z:.1f}"] = {
                "dR_dfnl": float(slope_per_fnl),
                "fnl_for_factor_2": float(1.0 / slope_per_fnl),
                "fnl_for_factor_10": float(9.0 / slope_per_fnl),
                "R_at_planck_2sigma_high": float(1.0 + slope_per_fnl * (-0.9 + 2 * 5.1)),
                "R_at_planck_2sigma_low": float(1.0 + slope_per_fnl * (-0.9 - 2 * 5.1)),
            }
        conf[epsname] = sub
    results["confrontation"] = {
        "planck2018_fnl_local": {"value": -0.9, "sigma": 5.1,
                                 "source": "Planck 2018 IX (arXiv:1905.05697), KSW T+E"},
        "note": ("fnl_for_factor_N is the linear-response requirement to change "
                 "the abundance by factor N; |f_NL| that large violates the "
                 "Edgeworth validity condition |S_3 sigma nu^3| << 1 and is a "
                 "scale indicator only."),
        "cases": conf,
    }

    outjson = os.path.join(outdir, "ledger6_png_highz_abundance.json")
    with open(outjson, "w") as fh:
        json.dump(results, fh, indent=2)

    # ------------------------------------------------------------- figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axes[0]
    for z, c in zip([8.0, 10.0, 12.0, 14.0], ["#4477aa", "#228833", "#cc6677", "#aa3377"]):
        Rm = mass_function_ratio(M, z, -35.0 / 16.0, sig0, s3_0, dlnsig_dM, ds3_dM_0)
        ax.plot(logM, 100.0 * (Rm - 1.0), color=c, label=f"z = {z:.0f}")
    ax.axhline(0.0, color="k", lw=0.6)
    ax.set_xlabel(r"$\log_{10}(M_h\,/\,M_\odot h^{-1})$")
    ax.set_ylabel(r"abundance change  $100\,(R-1)$  [%]")
    ax.set_title(r"$f_{\rm NL} = -35/16$ (matter contraction)")
    ax.legend(frameon=False, fontsize=9)

    ax = axes[1]
    z = 11.0
    for name, c, ls in [("lab_matter_contraction", "#228833", "-"),
                        ("cai2009", "#cc6677", "--"),
                        ("positive_control", "#4477aa", ":")]:
        Rm = mass_function_ratio(M, z, FNL_VALUES[name], sig0, s3_0, dlnsig_dM, ds3_dM_0)
        ax.plot(logM, 100.0 * (Rm - 1.0), color=c, ls=ls,
                label=f"{name}  ($f_{{NL}}={FNL_VALUES[name]:+.4f}$)")
    ax.axhline(0.0, color="k", lw=0.6)
    ax.set_xlabel(r"$\log_{10}(M_h\,/\,M_\odot h^{-1})$")
    ax.set_ylabel(r"abundance change  $100\,(R-1)$  [%]")
    ax.set_title("z = 11")
    ax.legend(frameon=False, fontsize=8)

    fig.suptitle("Local-PNG correction to the high-$z$ halo abundance (LoVerde+2008 Eq. 45)",
                 fontsize=11)
    fig.tight_layout()
    figpath = os.path.join(outdir, "ledger6_png_highz_abundance.png")
    fig.savefig(figpath, dpi=150)

    print(f"sigma8 check: {results['sigma8_check']:.4f}")
    for epsname, e in results["threshold_cases"].items():
        print(f"\n{epsname}  Mh = {e['Mh_Msun_over_h']:.3e} Msun/h  (log {e['logMh']:.2f})")
        for z in redshifts:
            s = e[f"z{z:.1f}"]
            print(f"  z={z:>4}: nu={s['nu']:.2f}  "
                  f"R(-35/16)={s['lab_matter_contraction']:.5f}  "
                  f"R(-35/8)={s['cai2009']:.5f}  "
                  f"dlnn/dlnM={s['dln_n_dln_Mh']:.2f}  "
                  f"equiv dlog10Mh={s['equiv_dlog10Mh_lab_matter_contraction']:+.4f}")
    print(f"\nwrote {outjson}\nwrote {figpath}")


if __name__ == "__main__":
    main()
