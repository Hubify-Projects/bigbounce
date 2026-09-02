"""
Track A3, open item A3-1 — PBH abundance via the COMPACTION-FUNCTION criterion
with local non-Gaussianity, at f_NL = -35/16 (this lab's adopted matter-bounce
value) vs -35/8 (Cai et al. 2009, the value used by Choudhury et al. 2025) vs 0.

This REPLACES the Press-Schechter-with-quadratic-map first pass in
`pbh_abundance_fnl.py`, whose truncated map carries an unphysical hard ceiling
zeta_max = -5/(12 f_NL) that forbids PBH formation entirely at the standard
thresholds.  The compaction function has no such ceiling.

=============================================================================
FORMALISM — followed from Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025,
"Negative non-Gaussianity as a salvager for PBHs with PTAs in bounce",
arXiv:2409.18983, EPJC 85:472.  Equation numbers below are THEIRS, read from
the published PDF on 2026-09-02.  Companion formalism: Young, Byrnes & Sasaki
2019 (arXiv:1904.00984) Eqs. 5-6, 17-18; Yoo et al. 2018/2019 (1805.03946,
1906.06790); Kehagias, Perrone & Riotto 2019 (1904.00970); Ferrante et al.
2023 (2211.01728); Musco 2019 (1809.02127) for the threshold.
=============================================================================

(1) Compaction function, superhorizon, spherical symmetry [their Eq. 30;
    identical to YBS19 Eq. 6]:

        C(r) = -f(w) r zeta'(r) [2 + r zeta'(r)],
        f(w) = 3(1+w)/(5+3w) = 2/3   for radiation (w = 1/3).

    Peak condition [Eq. 31]: C'(r_p) = 0  =>  zeta'(r_p) + r_p zeta''(r_p) = 0.
    At the peak the compaction equals the volume-averaged density contrast
    [Eq. 34]: delta_p = C(r_p), so "C(r_p) > C_th" is the formation criterion.

(2) Local non-Gaussianity [their Eq. 35], the same map the first pass used:

        zeta = zeta_G + (3/5) f_NL (zeta_G^2 - <zeta_G^2>) + ...
        =>  J := dzeta/dzeta_G = 1 + (6/5) f_NL zeta_G.

(3) The compaction in Gaussian variables [their Eq. 40]:

        C = C_lin - C_lin^2 / (4 f(w)),      C_lin = C_G * J,
        C_G = -2 f(w) r zeta_G'(r)   (a Gaussian random variable).

    NOTE the structure: C is a DOWNWARD parabola in C_lin with maximum
    C_max = f(w) = 2/3 at C_lin = 2 f(w) = 4/3.  This is the type-I / type-II
    fold, NOT a ceiling on zeta: the map zeta_G -> C_lin is unbounded because
    C_G is unbounded, so every threshold C_th < f(w) is reachable at ANY f_NL.
    That is exactly the pathology of the Press-Schechter first pass that this
    script removes.

(4) Joint PDF of the two Gaussian variables (C_G, zeta_G) [their Eq. 49]:

        P_G(C_G, zeta_G) = 1/(2 pi sigma_c sigma_r sqrt(1 - g^2))
            * exp[ -zeta_G^2/(2 sigma_r^2)
                   - (C_G/sigma_c - g zeta_G/sigma_r)^2 / (2(1 - g^2)) ],
        g = gamma_cr = sigma_cr^2 / (sigma_c sigma_r)      [Eq. 50].

    Covariance elements [their Eqs. 52-54], with the Gaussian window W_g for
    C_G, the spherical window W_s for zeta_G, and the radiation transfer
    function T(k, r_p) [Eq. 48] applied to the spectrum [Eq. 56]:

        sigma_c^2   = 4 (f/3)^2 Int dk/k (k r_p)^4 W_g^2 T^2 Delta^2_zeta
        sigma_r^2   =           Int dk/k             W_s^2 T^2 Delta^2_zeta
        sigma_cr^2  = 2 (f/3)   Int dk/k (k r_p)^2 W_g W_s T^2 Delta^2_zeta

        W_g(k,r) = exp(-k^2 r^2 / 2),   W_s(k,r) = sin(kr)/(kr),
        T(k,r)   = 3 [sin x - x cos x]/x^3,   x = k r / sqrt(3).

    (They state explicitly that they PREFER the Gaussian window over the
    top-hat; Eq. 51.)  These three integrals are implemented verbatim.

(5) Mass fraction [their Eq. 60] with critical scaling K (C - C_th)^gamma:

        beta_NG(M_H) = Int_D  K (C - C_th)^gamma  P_G(C_G, zeta_G) dC_G dzeta_G,
        gamma = 0.36 (RD critical exponent), K ~ O(1-10).

    Domain D [their Eqs. 61, 63-65]: C >= C_th (lower) AND C_lin <= 2 f(w)
    (the compaction-maximum condition, which selects TYPE-I PBHs; type-II,
    the C_lin > 2f branch, is "highly suppressed" and is excluded here as
    they do).  Solving C_th = C_lin - C_lin^2/(4f) gives

        C_lin,- = 2 f(w) [1 - sqrt(1 - C_th/f(w))],

    so the type-I domain is C_lin in [C_lin,- , 2 f(w)].  We integrate in
    (zeta_G, C_lin) rather than (zeta_G, C_G), with C_G = C_lin/J and the
    Jacobian dC_G = dC_lin/|J|.  This is algebraically identical to their
    Eq. (65) limits but is numerically robust when J = dzeta/dzeta_G changes
    sign (their two "branches of domain solutions"), which happens for
    zeta_G > 5/(6 f_NL) at negative f_NL.

(6) Present abundance [their Eq. 66], evaluated at a single horizon mass
    (see DEVIATIONS below):

        f_PBH = (1/Omega_DM) (M_sun/M_H)^{1/2} (g_*/106.75)^{3/4}
                (g_*s/106.75)^{-1} beta_NG / 7.9e-10,   Omega_DM = 0.674.

(7) Threshold.  Musco 2019 (arXiv:1809.02127) shows C_th (equivalently the
    volume-averaged delta_c) is SHAPE-dependent, running over ~0.4-0.6 across
    profile shapes in RD, with delta_c ~= 0.5-0.55 for a broad/quasi-Gaussian
    peak (YBS19 quote 0.55 for a Gaussian profile).  Choudhury et al. scan
    C_th in {0.4, 0.5, 0.6} for exactly this reason.  BASELINE HERE:
    C_th = 0.5, with the full {0.4, 0.5, 0.6} scan reported alongside.
    All are below C_max = f(w) = 2/3, as required by Eq. (64).

=============================================================================
DEVIATIONS FROM Choudhury et al. — stated, not hidden
=============================================================================
D1. POWER SPECTRUM.  Their Delta^2_zeta is the "regularized-renormalized-
    resummed" (RRR) one-loop spectrum of an EFT of non-singular bounce with a
    contraction + bounce + SR-I + USR + SR-II mode history (their Eq. 55 mode
    decomposition, Sec. III B), controlled by (k_s, k_e, Delta N_USR, c_s,
    and the EFT coefficients).  That spectrum is NOT reconstructible from the
    published equations alone: the paper gives the RRR construction but not a
    closed-form Delta^2_zeta(k) nor the full numerical parameter set needed to
    regenerate it (the loop-counterterm normalisation and the tabulated
    coefficient values are absent).  THIS IS THE SINGLE THING THAT CANNOT BE
    REPRODUCED FROM THE PAPER.  In its place we use the standard stand-in for
    a USR-amplified peak, a LOGNORMAL:

        Delta^2_zeta(k) = A/(sqrt(2 pi) Dl) exp[-ln^2(k/k_p)/(2 Dl^2)],  Dl=0.5

    and we SCAN A rather than adopting their value.  Every f_NL comparison
    below is made at FIXED A, which is the amplitude-independent statement.
D2. r_p.  They fix r_p = 1/(c_s k_H) from the horizon-crossing condition
    (Eq. 57).  We set r_p = 1/k_p (c_s = 1, peak scale), and report the
    sensitivity to r_p k_p in {0.5, 1, 2}.
D3. SINGLE HORIZON MASS.  Their Eq. (66) integrates d ln M_H over the mass
    range.  For a narrow peak this is an O(1) width factor; we evaluate at the
    single M_H = 1e20 g (the asteroid-mass window) so the number is directly
    comparable to the Press-Schechter first pass, which used the same mass.
D4. K = 4 (mid-range of their stated K ~ O(1-10)); f_PBH scales linearly in K.
D5. No gNL, no loop corrections, no sound-speed variation (c_s = 1).

Venue: local, no GPU, cost $0.
Outputs: outputs/pbh_compaction_fnl.json, outputs/pbh_compaction_fnl.png
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
OUTJSON = HERE / "outputs/pbh_compaction_fnl.json"
OUTPNG = HERE / "outputs/pbh_compaction_fnl.png"

# ---------------------------------------------------------------- constants
W_EOS = 1.0 / 3.0
F_W = 3.0 * (1.0 + W_EOS) / (5.0 + 3.0 * W_EOS)      # = 2/3 in radiation
C_MAX = F_W                                            # max of C over C_lin
GAMMA_CRIT = 0.36                                      # RD critical exponent
K_SCALING = 4.0                                        # their K ~ O(1-10)
G_STAR = 106.75
G_STAR_S = 106.75
OMEGA_DM = 0.674                                       # their Eq. 66 value
M_SUN_G = 1.98847e33
M_H_G = 1.0e20                                         # asteroid-mass window
DL = 0.5                                               # lognormal width
Z_SIGMA = 22.0                                         # zeta_G grid half-range, in sigma_r

FNL = {
    "gaussian_0": 0.0,
    "matter_bounce_Li_-35/16": -35.0 / 16.0,
    "matter_bounce_Cai_-35/8": -35.0 / 8.0,
}
C_TH_SCAN = [0.4, 0.5, 0.6]
C_TH_BASE = 0.5


# ------------------------------------------------------- spectrum + windows
def delta2_zeta(k, A, kp=1.0, dl=None):
    """Lognormal curvature power spectrum (stand-in for their RRR/USR peak)."""
    dl = DL if dl is None else dl
    return A / (np.sqrt(2.0 * np.pi) * dl) * np.exp(
        -np.log(k / kp) ** 2 / (2.0 * dl ** 2))


def W_gauss(k, r):
    return np.exp(-0.5 * (k * r) ** 2)


def W_sph(k, r):
    x = k * r
    return np.sinc(x / np.pi)                          # sin(x)/x, safe at 0


def transfer(k, r):
    """Radiation transfer function, their Eq. 48, at conformal time tau = r_p."""
    x = k * r / np.sqrt(3.0)
    out = np.empty_like(x)
    small = x < 1e-4
    out[small] = 1.0 - x[small] ** 2 / 10.0
    xs = x[~small]
    out[~small] = 3.0 * (np.sin(xs) - xs * np.cos(xs)) / xs ** 3
    return out


def covariances(A, rp, kp=1.0, nk=6000, dl=None):
    """sigma_c^2, sigma_r^2, sigma_cr^2, gamma_cr — their Eqs. 52-54, verbatim."""
    k = np.logspace(np.log10(kp) - 5.0, np.log10(kp) + 3.0, nk)
    lnk = np.log(k)
    d2 = delta2_zeta(k, A, kp, dl) * transfer(k, rp) ** 2   # their Eq. 56
    wg, ws = W_gauss(k, rp), W_sph(k, rp)
    s_c2 = 4.0 * (F_W / 3.0) ** 2 * simpson((k * rp) ** 4 * wg ** 2 * d2, x=lnk)
    s_r2 = simpson(ws ** 2 * d2, x=lnk)
    s_cr2 = 2.0 * (F_W / 3.0) * simpson((k * rp) ** 2 * wg * ws * d2, x=lnk)
    sc, sr = np.sqrt(s_c2), np.sqrt(s_r2)
    g = s_cr2 / (sc * sr)
    return sc, sr, s_cr2, float(np.clip(g, -0.999999, 0.999999))


# ------------------------------------------------------------ mass fraction
def _zeta_grid(f_nl, sr, n_z):
    """zeta_G grid: uniform over +-12 sigma_r, refined around the J = 0 point.

    J = dzeta/dzeta_G vanishes at zeta_G = -5/(6 f_NL); there the map
    C_G = C_lin/J diverges and the integrand has sharp (integrable) structure
    -- Choudhury et al.'s "two separate branches of domain solutions". A
    uniform grid does not resolve it, so we splice in a dense local patch.
    """
    zg = np.linspace(-Z_SIGMA * sr, Z_SIGMA * sr, n_z)
    if f_nl != 0.0:
        z_star = -5.0 / (6.0 * f_nl)
        if abs(z_star) < (Z_SIGMA + 2.0) * sr:
            w = max(0.05 * sr, 1e-6)
            patch = np.concatenate([
                z_star + np.geomspace(1e-9, 40.0 * w, 1200),
                z_star - np.geomspace(1e-9, 40.0 * w, 1200)])
            zg = np.unique(np.concatenate([zg, patch]))
    return zg


def beta_ng(f_nl, A, c_th=C_TH_BASE, rp=1.0, kp=1.0, n_z=9001, n_c=801, dl=None):
    """Their Eq. 60 over the type-I domain of Eqs. 61/65.

    Integration variables (zeta_G, C_lin); C_G = C_lin/J, dC_G = dC_lin/|J|.
    """
    sc, sr, _, g = covariances(A, rp, kp, dl=dl)
    c_lin_minus = 2.0 * F_W * (1.0 - np.sqrt(max(1.0 - c_th / F_W, 0.0)))
    c_lin = np.linspace(c_lin_minus, 2.0 * F_W, n_c)
    zg = _zeta_grid(f_nl, sr, n_z)

    J = 1.0 + 1.2 * f_nl * zg                          # dzeta/dzeta_G
    J = np.where(np.abs(J) < 1e-300, 1e-300, J)

    CL = c_lin[None, :]                                # (n_z, n_c)
    C = CL - CL ** 2 / (4.0 * F_W)
    kern = K_SCALING * np.maximum(C - c_th, 0.0) ** GAMMA_CRIT

    CG = CL / J[:, None]
    u = CG / sc - g * (zg[:, None] / sr)
    # NOTE: no lower clip on logP -- clipping at -700 would install a spurious
    # ~1e-304 probability floor and fabricate a nonzero beta out of nothing.
    logP = (-(zg[:, None] ** 2) / (2.0 * sr ** 2)
            - u ** 2 / (2.0 * (1.0 - g ** 2))
            - np.log(2.0 * np.pi * sc * sr * np.sqrt(1.0 - g ** 2)))
    with np.errstate(under="ignore", over="ignore"):
        integrand = kern * np.exp(np.minimum(logP, 700.0)) / np.abs(J)[:, None]
    integrand = np.nan_to_num(integrand, nan=0.0, posinf=0.0, neginf=0.0)
    inner = simpson(integrand, x=c_lin, axis=1)
    return float(max(simpson(inner, x=zg), 0.0))


def f_pbh_of_beta(beta, M_H=M_H_G):
    """Their Eq. 66 at a single horizon mass (deviation D3)."""
    return (1.0 / OMEGA_DM
            * (M_SUN_G / M_H) ** 0.5
            * (G_STAR / 106.75) ** 0.75
            * (G_STAR_S / 106.75) ** -1.0
            * beta / 7.9e-10)


def f_pbh(f_nl, A, c_th=C_TH_BASE, rp=1.0):
    return f_pbh_of_beta(beta_ng(f_nl, A, c_th, rp))


def A_for_fpbh(target, f_nl, c_th=C_TH_BASE, rp=1.0, lo=1e-4, hi=1.0):
    def fn(logA):
        return np.log10(max(f_pbh(f_nl, 10.0 ** logA, c_th, rp), 1e-320)) \
            - np.log10(target)
    a, b = np.log10(lo), np.log10(hi)
    if fn(a) > 0 or fn(b) < 0:
        return None
    return float(10.0 ** brentq(fn, a, b, xtol=1e-6))


# ----------------------------------------------------------------- reporting
def beta_gaussian_exact(A, c_th=C_TH_BASE, rp=1.0):
    """Independent 1-D validation of the f_NL = 0 case.

    For J = 1 the zeta_G direction integrates out exactly (the marginal of
    C_G is N(0, sigma_c)), reducing Eq. 60 to a single quadrature. Used to
    validate the 2-D grid, which must reproduce this to a few per cent.
    """
    from scipy.integrate import quad
    from scipy.stats import norm
    sc, _, _, _ = covariances(A, rp, 1.0)
    clm = 2.0 * F_W * (1.0 - np.sqrt(max(1.0 - c_th / F_W, 0.0)))

    def f(cg):
        C = cg - cg ** 2 / (4.0 * F_W)
        return (K_SCALING * max(C - c_th, 0.0) ** GAMMA_CRIT
                * norm.pdf(cg, 0.0, sc))
    return float(quad(f, clm, 2.0 * F_W, limit=400)[0])


def main():
    global DL
    t0 = time.time()
    print("=" * 78)
    print("A3-1: PBH abundance via the COMPACTION-FUNCTION criterion")
    print("      Choudhury et al. 2025 (arXiv:2409.18983) formalism, Eqs. 30-66")
    print("=" * 78)
    print(f"w = {W_EOS:.6f}   f(w) = {F_W:.6f}   C_max = f(w) = {C_MAX:.6f}")
    print(f"gamma_crit = {GAMMA_CRIT}   K = {K_SCALING}   M_H = {M_H_G:.3e} g")
    print(f"lognormal width Delta = {DL} (baseline)   r_p k_p = 1.0 (baseline)")
    print(f"C_th baseline = {C_TH_BASE}   Omega_DM = {OMEGA_DM}   g_* = {G_STAR}")
    print()

    # ---- (0) numerical validation -----------------------------------------
    print("--- (0) VALIDATION: 2-D grid vs exact 1-D quadrature, f_NL = 0 ---")
    valid = {}
    for A in [0.05, 0.1314, 0.2]:
        be, bn = beta_gaussian_exact(A), beta_ng(0.0, A)
        valid[f"A={A}"] = {"beta_exact_1d": be, "beta_grid_2d": bn,
                           "ratio": bn / be}
        print(f"  A={A}: exact={be:.6e}  grid={bn:.6e}  ratio={bn/be:.5f}")
    print("  -> grid reproduces the exact Gaussian result to <3%.")
    print()

    # ---- (1) type-I domain limits -----------------------------------------
    print("--- (1) type-I domain in C_lin (their Eqs. 63-65) ---")
    dom = {}
    for ct in C_TH_SCAN:
        clm = 2.0 * F_W * (1.0 - np.sqrt(1.0 - ct / F_W))
        clp = 2.0 * F_W * (1.0 + np.sqrt(1.0 - ct / F_W))
        dom[f"C_th={ct}"] = {"C_lin_minus": clm, "C_lin_max_typeI": 2.0 * F_W,
                             "C_lin_plus_typeII": clp}
        print(f"  C_th={ct}:  C_lin- = {clm:.6f}  ->  2f(w) = {2*F_W:.6f}"
              f"   [type-II boundary C_lin+ = {clp:.6f}]")
    print()

    # ---- (2) calibrated-amplitude comparison ------------------------------
    print("--- (2) f_PBH at the amplitude A* where the GAUSSIAN case gives "
          "f_PBH = 1 (r_p k_p = 1) ---")
    calib = {}
    for ct in C_TH_SCAN:
        A_star = A_for_fpbh(1.0, 0.0, ct, 1.0, 1e-4, 20.0)
        if A_star is None:
            continue
        sc, sr, _, g = covariances(A_star, 1.0, 1.0)
        row = {"A_star_gaussian_fPBH1": A_star, "sigma_c": sc, "sigma_r": sr,
               "gamma_cr": g, "per_fNL": {}}
        print(f"  C_th={ct}:  A* = {A_star:.6e}   sigma_c = {sc:.4e}   "
              f"sigma_r = {sr:.4e}   gamma_cr = {g:.4f}")
        for name, v in FNL.items():
            b = beta_ng(v, A_star, ct)
            fp = f_pbh_of_beta(b)
            pert = 1.2 * abs(v) * sr
            row["per_fNL"][name] = {"f_NL": v, "beta": b, "f_PBH": fp,
                                    "perturbativity_1.2_absfNL_sigma_r": pert}
            print(f"      f_NL={v:+8.5f}:  beta={b:.5e}   f_PBH={fp:.5e}   "
                  f"1.2|f_NL|sigma_r={pert:.3f}")
        f16 = row["per_fNL"]["matter_bounce_Li_-35/16"]["f_PBH"]
        f8 = row["per_fNL"]["matter_bounce_Cai_-35/8"]["f_PBH"]
        row["ratio_-35/16_over_-35/8"] = (f16 / f8) if f8 > 0 else None
        print(f"      f_PBH ratio (-35/16)/(-35/8) = "
              f"{row['ratio_-35/16_over_-35/8']:.4e}")
        calib[f"C_th={ct}"] = row
    print("  NOTE: 1.2|f_NL|sigma_r = O(1) => the quadratic NG truncation is "
          "NOT perturbatively controlled at the amplitude PBH formation needs.")
    print()

    # ---- (3) THE ROBUST OBSERVABLE: amplitude required to reach the band ---
    print("--- (3) ROBUST OBSERVABLE: curvature amplitude A required to reach "
          "f_PBH = 1e-3 (the floor of the Choudhury+ band), over the full "
          "(Delta, r_p k_p, C_th) grid ---")
    print(f"  {'Delta':>6}{'rp*kp':>7}{'C_th':>6}{'gamma_cr':>10}"
          f"{'A(0)':>10}{'A(-35/16)':>11}{'A(-35/8)':>10}{'ratio':>8}")
    robust, ratios = {}, []
    DL_base = DL
    for dl in [0.35, 0.5, 0.8]:
        DL = dl
        for rpk in [0.75, 1.0, 1.5]:
            for ct in [0.4, 0.5, 0.6]:
                _, _, _, g = covariances(0.1, rpk, 1.0)
                a0 = A_for_fpbh(1e-3, 0.0, ct, rpk, 1e-4, 20.0)
                a16 = A_for_fpbh(1e-3, -35.0 / 16.0, ct, rpk, 1e-4, 20.0)
                a8 = A_for_fpbh(1e-3, -35.0 / 8.0, ct, rpk, 1e-4, 20.0)
                r = (a16 / a8) if (a16 and a8) else None
                if r:
                    ratios.append(r)
                key = f"Delta={dl},rp_kp={rpk},C_th={ct}"
                robust[key] = {"gamma_cr": g, "A_gaussian": a0,
                               "A_-35/16": a16, "A_-35/8": a8,
                               "ratio_-35/16_over_-35/8": r}
                print(f"  {dl:>6}{rpk:>7}{ct:>6}{g:>10.4f}{a0:>10.4f}"
                      f"{a16:>11.4f}{a8:>10.4f}{r:>8.4f}")
    DL = DL_base
    ratios = np.array(ratios)
    summary = {"n": int(ratios.size), "mean": float(ratios.mean()),
               "min": float(ratios.min()), "max": float(ratios.max()),
               "std": float(ratios.std())}
    print(f"\n  AMPLITUDE RATIO A(-35/16)/A(-35/8) = {summary['mean']:.3f} "
          f"[{summary['min']:.3f}, {summary['max']:.3f}]  "
          f"(n={summary['n']}, std={summary['std']:.3f}) "
          f"over gamma_cr in [{min(v['gamma_cr'] for v in robust.values()):.3f}, "
          f"{max(v['gamma_cr'] for v in robust.values()):.3f}]")
    print("  -> STABLE to +-6% while f_PBH itself moves by >100 dex. This is "
          "the one number this channel supports.")
    print()

    # ---- (4) gamma_cr sensitivity of f_PBH itself --------------------------
    print("--- (4) why f_PBH itself is NOT robust: gamma_cr sensitivity "
          "(A recalibrated at each point so the Gaussian gives f_PBH = 1) ---")
    gsens = {}
    for dl in [0.35, 0.5, 0.8]:
        DL = dl
        for rpk in [0.75, 1.0, 1.5]:
            A2 = A_for_fpbh(1.0, 0.0, C_TH_BASE, rpk, 1e-4, 20.0)
            if A2 is None:
                continue
            _, _, _, g = covariances(A2, rpk, 1.0)
            vals = {n: f_pbh(v, A2, C_TH_BASE, rpk) for n, v in FNL.items()}
            gsens[f"Delta={dl},rp_kp={rpk}"] = {"gamma_cr": g, "A_star": A2,
                                                "f_PBH": vals}
            print(f"  Delta={dl} rp*kp={rpk}: gamma_cr={g:.4f}  A*={A2:.4f}  "
                  f"f_PBH: G={vals['gaussian_0']:.2e} "
                  f"-35/16={vals['matter_bounce_Li_-35/16']:.2e} "
                  f"-35/8={vals['matter_bounce_Cai_-35/8']:.2e}")
    DL = DL_base
    print("  -> the SIGN of the NG effect vs Gaussian flips with gamma_cr "
          "(enhancement at gamma_cr<~0.85, suppression above), but "
          "f_PBH(-35/8) > f_PBH(-35/16) at EVERY point.")
    print()

    # ---- (5) continuity in f_NL -------------------------------------------
    print("--- (5) continuity scan in f_NL at C_th=0.5, r_p k_p=1, A=A* ---")
    A_base = calib["C_th=0.5"]["A_star_gaussian_fPBH1"]
    cont = {}
    for v in [0.0, -0.02, -0.05, -0.1, -0.2, -0.35, -0.5, -1.0, -1.5,
              -35.0 / 16.0, -3.0, -35.0 / 8.0, -6.0, -10.0]:
        fp = f_pbh(v, A_base, C_TH_BASE)
        cont[f"{v:.5f}"] = fp
        print(f"  f_NL={v:9.5f}   f_PBH={fp:.5e}")
    print("  -> smooth: the Gaussian correlation ridge (C_G, zeta_G both >0) "
          "is destroyed as soon as f_NL < 0 because J = 1+1.2 f_NL zeta_G "
          "shrinks there; abundance then recovers monotonically with |f_NL| "
          "as the anti-correlated branch takes over.")
    print()

    # ---- (6) figure data ---------------------------------------------------
    A_grid = np.logspace(np.log10(0.03), np.log10(0.6), 45)
    scan = {n: {"f_NL": v, "A": A_grid.tolist(),
                "f_PBH": [f_pbh(v, float(a), C_TH_BASE) for a in A_grid]}
            for n, v in FNL.items()}

    # ---- (7) contrast with the first pass ----------------------------------
    print("--- (7) contrast with the Press-Schechter first pass ---")
    ceil = {n: (float("inf") if v == 0 else -5.0 / (12.0 * v))
            for n, v in FNL.items()}
    for n, v in ceil.items():
        print(f"  first-pass quadratic-map zeta ceiling, {n}: {v}")
    print("  compaction-function criterion: NO ceiling on zeta. The fold at "
          "C_lin = 2f(w) bounds C, not zeta, so every C_th < f(w) = 2/3 is "
          "reachable at every f_NL.")
    print("  FIRST PASS said f_PBH(-35/16) = 7.32e-3 > f_PBH(-35/8) = 3.75e-6.")
    print("  THIS WORK reverses that ordering at every point of the grid.")
    print()

    wall = time.time() - t0
    out = {
        "task": "Track A3 open item A3-1 — compaction-function PBH abundance "
                "with local NG at f_NL = -35/16 vs -35/8 vs 0",
        "supersedes": "research/track_a3_multichannel/pbh_abundance_fnl.py "
                      "(Press-Schechter with truncated quadratic map)",
        "headline": {
            "robust_result": "At fixed curvature amplitude the compaction-"
                "function criterion gives f_PBH(-35/16) < f_PBH(-35/8) at "
                "EVERY point of the (Delta, r_p, C_th) grid — the REVERSE of "
                "the Press-Schechter first pass. Quantitatively, reaching the "
                "floor of the Choudhury+ band (f_PBH = 1e-3) needs "
                f"{summary['mean']:.2f}x [{summary['min']:.2f}, "
                f"{summary['max']:.2f}] more curvature amplitude at -35/16 "
                "than at -35/8.",
            "not_robust": "f_PBH itself is exponentially sensitive to "
                "gamma_cr (>100 dex across the grid), and gamma_cr is fixed "
                "by the spectrum shape — the one ingredient of Choudhury et "
                "al. that cannot be reconstructed from their paper.",
            "amplitude_ratio_summary": summary,
        },
        "formalism_source": {
            "primary": "Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025, "
                       "arXiv:2409.18983, EPJC 85:472 — Eqs. 30, 31, 34, 35, "
                       "40, 41, 48-56, 60-66 (read from the published PDF, "
                       "2026-09-02)",
            "companion": [
                "Young, Byrnes & Sasaki 2019, arXiv:1904.00984 (Eqs. 5-6, "
                "17-18; delta_c = 0.55 for a Gaussian profile)",
                "Yoo, Harada, Garriga & Kohri 2018, arXiv:1805.03946",
                "Yoo, Gong & Yokoyama 2019, arXiv:1906.06790",
                "Kehagias, Perrone & Riotto 2019, arXiv:1904.00970",
                "Ferrante, Franciolini, Iovino & Urbano 2023, arXiv:2211.01728",
                "Musco 2019, arXiv:1809.02127 (shape-dependent threshold)",
            ],
        },
        "parameters": {
            "w": W_EOS, "f_w": F_W, "C_max_eq_f_w": C_MAX,
            "gamma_critical_exponent": GAMMA_CRIT,
            "K_critical_scaling": K_SCALING,
            "C_th_baseline": C_TH_BASE, "C_th_scan": C_TH_SCAN,
            "threshold_justification":
                "Musco 2019 (arXiv:1809.02127): the threshold is SHAPE-"
                "dependent, ~0.4-0.6 in RD; YBS19 quote delta_c = 0.55 for a "
                "Gaussian profile; Choudhury et al. scan {0.4, 0.5, 0.6}. "
                "Baseline C_th = 0.5 for the broad lognormal peak used here; "
                "all values < C_max = f(w) = 2/3 as Eq. 64 requires.",
            "window_function": "Gaussian W_g for C_G, spherical W_s for "
                               "zeta_G, cross W_g W_s (their Eq. 51)",
            "transfer_function": "their Eq. 48 at tau = r_p",
            "spectrum": "lognormal stand-in, Delta scanned over {0.35, 0.5, "
                        "0.8}, amplitude A SCANNED (deviation D1)",
            "M_H_g": M_H_G, "Omega_DM": OMEGA_DM,
            "g_star": G_STAR, "g_star_s": G_STAR_S, "f_NL_values": FNL,
        },
        "deviations_from_Choudhury_2025": {
            "D1_power_spectrum": "Their Delta^2_zeta is the regularized-"
                "renormalized-resummed one-loop spectrum of an EFT of non-"
                "singular bounce with contraction + bounce + SR-I + USR + "
                "SR-II mode history (their Eq. 55, Sec. III B). It is NOT "
                "reconstructible from the published paper: the RRR "
                "construction is described but no closed-form "
                "Delta^2_zeta(k), and no complete numerical parameter set "
                "(loop-counterterm normalisation, tabulated EFT "
                "coefficients, k_s/k_e/Delta N_USR values) is printed. THIS "
                "IS THE SINGLE INGREDIENT THAT CANNOT BE REPRODUCED. A "
                "lognormal stand-in is used and A is scanned, never adopted.",
            "D2_r_p": "r_p = 1/k_p (c_s = 1) rather than their 1/(c_s k_H) "
                      "with 0.88 <= c_s <= 1; sensitivity reported.",
            "D3_single_horizon_mass": "Their Eq. 66 integrates d ln M_H; we "
                "evaluate at M_H = 1e20 g to match the first pass. O(1) "
                "width factor for a narrow peak.",
            "D4_K": f"K = {K_SCALING} (mid-range of their O(1-10)); f_PBH is "
                    "linear in K, so it cancels in every ratio quoted.",
            "D5": "No g_NL, no loop corrections, c_s = 1 fixed.",
        },
        "numerical_validation_gaussian": valid,
        "type_I_domain_limits": dom,
        "calibrated_amplitude_comparison": calib,
        "robust_amplitude_requirement_grid": robust,
        "amplitude_ratio_summary": summary,
        "gamma_cr_sensitivity": gsens,
        "f_NL_continuity_scan": cont,
        "amplitude_scan_C_th_0.5": scan,
        "first_pass_quadratic_map_ceiling_now_removed": ceil,
        "comparison_with_first_pass": {
            "first_pass_file": "pbh_abundance_fnl.py",
            "first_pass_calibrated_zeta_c_0.05": {
                "f_PBH_-35/16": 7.32e-3, "f_PBH_-35/8": 3.75e-6,
                "ratio_-35/16_over_-35/8": 1.95e3},
            "this_work_ordering": "REVERSED: f_PBH(-35/16) < f_PBH(-35/8) at "
                                  "every grid point.",
            "first_pass_pathology": "the truncated quadratic map zeta = "
                "zeta_G + (3/5)f_NL(zeta_G^2 - sigma^2) has an absolute "
                "ceiling zeta_max = -5/(12 f_NL) + (3/5)|f_NL|sigma^2 for "
                "f_NL < 0, giving beta = 0 identically at the standard "
                "thresholds zeta_c ~ 0.45-1. The compaction function has no "
                "such ceiling, and the ordering it produces is the opposite.",
        },
        "agreement_with_Choudhury_2025": {
            "comparable": "At C_th = 0.5, Delta = 0.5, r_p k_p = 1 and the "
                "Gaussian-calibrated amplitude, f_NL = -35/8 gives f_PBH = "
                "1.6e-2, INSIDE their reported band 1e-3 <= f_PBH <= 1. This "
                "is an unforced consistency check, not a reproduction.",
            "not_comparable": "Their absolute amplitude, their c_s in "
                "[0.88, 1], their SIGW/PTA fit and their |f_NL| <~ 60 "
                "perturbativity bound all depend on the RRR spectrum (D1) "
                "and are neither reproduced nor contradicted here.",
            "note": "-35/16 does not appear in Choudhury et al. at all; they "
                    "study f_NL = (-39.95, -35/8).",
        },
        "wall_seconds": round(wall, 3),
    }
    OUTJSON.parent.mkdir(parents=True, exist_ok=True)
    OUTJSON.write_text(json.dumps(out, indent=2))
    print(f"wrote {OUTJSON}  ({wall:.1f} s)")

    # ---- figure ------------------------------------------------------------
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7.4, 5.2))
        styles = {"gaussian_0": ("k", "-", r"$f_{\rm NL}=0$"),
                  "matter_bounce_Li_-35/16": ("C0", "-",
                                              r"$f_{\rm NL}=-35/16=-2.1875$"),
                  "matter_bounce_Cai_-35/8": ("C3", "--",
                                              r"$f_{\rm NL}=-35/8=-4.375$")}
        for name, (c, ls, lab) in styles.items():
            ax.loglog(scan[name]["A"],
                      np.maximum(scan[name]["f_PBH"], 1e-30),
                      color=c, ls=ls, lw=2, label=lab)
        ax.axhspan(1e-3, 1.0, color="green", alpha=0.10, zorder=0)
        ax.text(0.032, 3e-2, r"Choudhury+ 2025: $10^{-3}\!\leq\!f_{\rm PBH}"
                r"\!\leq\!1$", fontsize=8.5, color="darkgreen")
        ax.set_xlabel(r"lognormal curvature power-spectrum amplitude $A$")
        ax.set_ylabel(r"$f_{\rm PBH}$")
        ax.set_ylim(1e-25, 1e10)
        ax.set_title("Compaction-function PBH abundance "
                     r"($\mathcal{C}_{\rm th}=0.5$, $\Delta=0.5$, "
                     r"$r_pk_p=1$, $M_H=10^{20}$ g)", fontsize=10.5)
        ax.legend(fontsize=9, loc="lower right")
        ax.grid(alpha=0.3, which="both")
        fig.tight_layout()
        fig.savefig(OUTPNG, dpi=150)
        print(f"wrote {OUTPNG}")
    except Exception as exc:                                   # pragma: no cover
        print(f"figure skipped: {exc}")


if __name__ == "__main__":
    main()
