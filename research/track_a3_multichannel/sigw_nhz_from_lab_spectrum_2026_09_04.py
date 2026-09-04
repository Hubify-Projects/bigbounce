"""
A3-3 / audit item DA3M-R4-02 -- scalar-induced gravitational waves (SIGW) in the
NANOGrav band from THE LAB'S OWN curvature power spectrum.

Question (from the R4 truth audit, item DA3M-R4-02): the A3 paper's Channel I
attributes gamma = 3 (Omega_GW ~ f^2) to the matter bounce by borrowing the
low-k slope of Papanikolaou 2025 (arXiv:2504.11641), whose spectrum carries a
small-scale ENHANCEMENT; but the same paper's section V C asserts the model's
spectrum is a featureless near-scale-invariant power law extrapolated over 10-15
decades.  Those are different spectra.  This script settles which slope the
lab's own committed spectrum actually gives.

Method
  (1) f <-> k for a mode re-entering the horizon in radiation domination:
      f = k c / (2 pi a_0), with a_0 = 1 by convention, so
          k [Mpc^-1] = 2 pi f (Mpc_in_km / c_km_per_s).
  (2) P_zeta(k) from the lab's spectrum (inlab_delta2_zeta_2026-09-03):
      Delta^2_zeta = A_s (k/k_*)^{n_s-1}, A_s = 2.1e-9, k_* = 0.05 Mpc^-1,
      branches n_s = 0.9649 (Planck-anchored) and n_s = 1 (pure dust bracket),
      carried through the A2 bounce transfer, which is scale-INDEPENDENT for
      k eta_B << 1 (validity checked below: k eta_B at nHz for each T_B).
  (3) Omega_GW(f) from the radiation-era induced-GW kernel of
      Kohri & Terada 2018 (arXiv:1804.08577, Eqs. (4.7)-(4.9)); the same kernel
      appears in Espinosa, Racco & Riotto 2018 and Domenech's review
      (arXiv:2109.01398).  Oscillation-averaged, sub-horizon (x -> infinity):
          Omega_GW(k) = (1/6) int dv int du
              [ (4 v^2 - (1 + v^2 - u^2)^2) / (4 u v) ]^2
              P_zeta(k u) P_zeta(k v) * xbar2_I2(u,v)
      with
          xbar2_I2 = (1/2) [3(u^2+v^2-3)/(4 u^3 v^3)]^2
                     * { [ -4uv + (u^2+v^2-3) ln|(3-(u+v)^2)/(3-(u-v)^2)| ]^2
                         + pi^2 (u^2+v^2-3)^2 Theta(u+v-sqrt(3)) }
      <- normalisation VALIDATED
      against the published analytic benchmark for an exactly scale-invariant
      P_zeta = A: Omega_GW = 0.8222 A^2 (Espinosa-Racco-Riotto 2018;
      Kohri-Terada 2018).  The script asserts that benchmark; the overall
      constant is therefore fixed by literature, not by this problem.
  (4) Today's amplitude: Omega_GW,0 h^2 = 1.62e-5 * (g_*/106.75) *
      (g_*s/106.75)^{-4/3} * Omega_GW(production).
  (5) Local slope fit across f in [2, 60] nHz -> n_Omega, and
      gamma_pred = 5 - n_Omega  (the paper's convention, pta_gamma_reproduce.py).
  (6) Inverse question: what nHz shape gives gamma = 3, what amplitude it needs,
      and at what bounce scale T_B a k ~ k_B feature would have to sit to put it
      in the PTA band -- compared with section V's T_B >~ 1e8-1e10 GeV.

INTEGRITY: nothing in this script is tuned toward gamma = 3.  The spectrum is
the committed CMB-anchored one; the kernel normalisation is fixed by a published
scale-invariant benchmark computed BEFORE any lab spectrum is inserted.

Venue: local (Apple silicon), CPU only, cost $0.
Outputs: outputs/sigw_nhz_from_lab_spectrum_2026_09_04.{json,png}
"""
from __future__ import annotations
import json, time
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
OUTJ = HERE / "outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json"
OUTP = HERE / "outputs/sigw_nhz_from_lab_spectrum_2026_09_04.png"

# ---------------------------------------------------------------- constants
C_KMS = 299792.458
MPC_KM = 3.0856775814913673e19
K_PER_HZ = 2.0 * np.pi * MPC_KM / C_KMS          # k[Mpc^-1] per f[Hz]
G_STAR_RD = 106.75
OM_R0_H2_FACTOR = 1.62e-5                        # Omega_GW,0 h^2 prefactor
A_S, K_STAR = 2.1e-9, 0.05                       # Planck 2018 anchor
BRANCHES = {"MB_anchored_ns0.9649": 0.9649, "pure_dust_ns1": 1.0}
F_LO_NHZ, F_HI_NHZ = 2.0, 60.0
F_YR = 1.0 / (365.25 * 24 * 3600)                # 3.1688e-8 Hz
NG_A_YR, NG_GAMMA = 2.4e-15, 3.2                 # NANOGrav 15yr HD power law
NG_GAMMA_SIG = 0.6 / 1.645

def delta2_zeta(k, ns):
    return A_S * (np.asarray(k, float) / K_STAR) ** (ns - 1.0)

# ------------------------------------------------- Kohri-Terada RD kernel
def xbar2_I2(u, v):
    """Oscillation-averaged x^2 <I^2> for radiation domination.

    Canonical Kohri-Terada 2018 (arXiv:1804.08577) form, as also written in
    Domenech's review (arXiv:2109.01398, Eq. 2.21) and Espinosa-Racco-Riotto:

        x^2 <I_RD^2> = (1/2) [3(u^2+v^2-3)/(4 u^3 v^3)]^2
                       * { [ -4uv + (u^2+v^2-3) ln|(3-(u+v)^2)/(3-(u-v)^2)| ]^2
                           + pi^2 (u^2+v^2-3)^2 Theta(u+v-sqrt(3)) }

    Validated below against Omega_GW = 0.8222 A^2 for scale-invariant P = A.
    """
    s = u * u + v * v - 3.0
    pref = 3.0 * s / (4.0 * u ** 3 * v ** 3)
    num = np.abs(3.0 - (u + v) ** 2)
    den = np.abs(3.0 - (u - v) ** 2)
    with np.errstate(divide="ignore", invalid="ignore"):
        L = np.log(np.where((num > 0) & (den > 0), num / np.where(den > 0, den, 1.0), 1.0))
    L = np.where(np.isfinite(L), L, 0.0)
    term = (-4.0 * u * v + s * L) ** 2 + np.pi ** 2 * s ** 2 * (u + v > np.sqrt(3.0))
    return 0.5 * pref ** 2 * term

def omega_gw_production(k, pk, nu=1200, nv=1200, vmax=300.0):
    """Omega_GW at production for a callable pk(k), at comoving wavenumber k."""
    # substitution: t = u - |1-v| in [0, 2 min(1,v)] handled by direct grid
    lv = np.linspace(np.log(1e-3), np.log(vmax), nv)
    v = np.exp(lv)
    tot = 0.0
    for i in range(nv):
        vi = v[i]
        ulo, uhi = abs(1.0 - vi), 1.0 + vi
        u = np.linspace(ulo, uhi, nu)
        # avoid the integrable log divergence exactly at u+v=sqrt(3)
        u = np.where(np.abs(u + vi - np.sqrt(3.0)) < 1e-12, u + 1e-12, u)
        f1 = ((4.0 * vi ** 2 - (1.0 + vi ** 2 - u ** 2) ** 2) / (4.0 * u * vi)) ** 2
        integ = f1 * xbar2_I2(u, vi) * pk(k * u) * pk(k * vi)
        integ = np.where(np.isfinite(integ), integ, 0.0)
        tot += np.trapezoid(integ, u) * vi          # * vi for dlnv measure
    dlv = lv[1] - lv[0]
    return (1.0 / 6.0) * tot * dlv

def omega_gw_today_h2(om_prod, g=G_STAR_RD):
    return OM_R0_H2_FACTOR * (g / 106.75) * (g / 106.75) ** (-4.0 / 3.0) * om_prod

def ng_omega_h2(f):
    """NANOGrav 15yr power-law Omega_GW h^2 from h_c = A (f/f_yr)^{(3-g)/2}."""
    hc = NG_A_YR * (f / F_YR) ** ((3.0 - NG_GAMMA) / 2.0)
    H100 = 100.0 / MPC_KM                          # s^-1, for h=1
    return 2.0 * np.pi ** 2 * f ** 2 * hc ** 2 / (3.0 * H100 ** 2)

def main():
    t0 = time.time()
    out = {"task": "A3-3 / DA3M-R4-02: SIGW at nHz from the lab's own Delta^2_zeta",
           "date": "2026-09-04"}

    # ---- (0) kernel normalisation validated on the scale-invariant benchmark
    bench = omega_gw_production(1.0, lambda kk: np.full_like(np.asarray(kk, float), 1.0))
    out["kernel_validation"] = {
        "benchmark": "scale-invariant P_zeta = A -> Omega_GW = 0.8222 A^2 "
                     "(Espinosa-Racco-Riotto 2018; Kohri-Terada 2018 arXiv:1804.08577)",
        "computed_coefficient": float(bench),
        "published_coefficient": 0.8222,
        "rel_error": float(abs(bench - 0.8222) / 0.8222)}
    assert abs(bench - 0.8222) / 0.8222 < 0.02, f"kernel normalisation off: {bench}"

    # ---- (1) f <-> k
    f = np.geomspace(F_LO_NHZ * 1e-9, F_HI_NHZ * 1e-9, 25)
    k = K_PER_HZ * f
    out["f_to_k"] = {
        "relation": "k [Mpc^-1] = 2 pi f (Mpc_km / c_km_s) = 6.4671e14 * f[Hz]",
        "k_per_nHz_Mpc-1": float(K_PER_HZ * 1e-9),
        "k_at_2nHz": float(K_PER_HZ * 2e-9), "k_at_60nHz": float(K_PER_HZ * 60e-9),
        "k_at_f_yr": float(K_PER_HZ * F_YR)}

    # ---- (2) validity: k eta_B at nHz for each committed bounce scale
    Mpl, T0 = 2.435323e18, 2.7255 * 8.617333262e-14
    c_H = np.sqrt(np.pi ** 2 * G_STAR_RD / 90.0) / Mpl
    c_a = T0 * (3.9091 / G_STAR_RD) ** (1.0 / 3.0)
    kB, T_B_LIST = {}, [1e16, 1e14, 1e10, 1e8]
    for T_B in T_B_LIST:
        kB["T_B=1e%d GeV" % round(np.log10(T_B))] = float(c_a * c_H * T_B / 6.39193e-39)
    kmax = float(k.max())
    out["transfer_validity"] = {
        "criterion": "A2 transfer scale-independent only for k eta_B = k/k_B <~ 1e-2",
        "k_B_Mpc-1": kB,
        "k_eta_B_at_60nHz": {kk: kmax / vv for kk, vv in kB.items()},
        "verdict": ("the nHz band sits at k/k_B <= 1e-7 for every bounce scale at or "
                    "above T_B = 1e8 GeV, i.e. DEEP inside the validated "
                    "super-Hubble-at-the-bounce domain; the scale-independent "
                    "transfer is defended here (unlike at k ~ k_B).")}

    # ---- (3) Omega_GW(f) per branch, (5) slope fit
    res, curves = {}, {}
    for name, ns in BRANCHES.items():
        pk = (lambda ns_: (lambda kk: delta2_zeta(kk, ns_)))(ns)
        omp = np.array([omega_gw_production(ki, pk) for ki in k])
        om0 = omega_gw_today_h2(omp)
        cf = np.polyfit(np.log(f), np.log(om0), 1)
        n_omega = float(cf[0])
        gamma_pred = 5.0 - n_omega
        i_yr = int(np.argmin(np.abs(f - F_YR)))
        res[name] = {
            "n_s": ns,
            "Delta2_zeta_at_2nHz": float(delta2_zeta(K_PER_HZ * 2e-9, ns)),
            "Delta2_zeta_at_60nHz": float(delta2_zeta(K_PER_HZ * 60e-9, ns)),
            "Omega_GW_h2_at_2nHz": float(om0[0]),
            "Omega_GW_h2_at_60nHz": float(om0[-1]),
            "Omega_GW_h2_near_f_yr": float(om0[i_yr]),
            "n_Omega_local_slope": n_omega,
            "gamma_pred": float(gamma_pred),
            "gamma_pred_analytic_2(ns-1)+5": float(5.0 - 2.0 * (ns - 1.0)),
            "z_vs_NANOGrav_official_gamma": float((gamma_pred - 3.2) / NG_GAMMA_SIG),
            "log10_amplitude_shortfall_vs_NANOGrav_at_f_yr":
                float(np.log10(ng_omega_h2(f[i_yr]) / om0[i_yr]))}
        curves[name] = om0.tolist()
    out["f_Hz"] = f.tolist(); out["k_Mpc-1"] = k.tolist()
    out["branches"] = res; out["curves_Omega_GW_h2"] = curves
    out["nanograv_reference"] = {
        "A_at_f_yr": NG_A_YR, "gamma": NG_GAMMA, "gamma_sigma_equiv": NG_GAMMA_SIG,
        "Omega_GW_h2_at_f_yr": float(ng_omega_h2(F_YR)),
        "Omega_GW_h2_at_2nHz": float(ng_omega_h2(2e-9)),
        "Omega_GW_h2_at_60nHz": float(ng_omega_h2(60e-9)),
        "source": "Agazie et al. 2023, arXiv:2306.16213 (HD-correlated power law)"}

    # ---- (4)/(6) what WOULD give gamma = 3
    # slope: broad P_R ~ k^n in RD -> Omega_GW ~ f^{2n} (Domenech 2109.01398)
    n_needed = (5.0 - 3.0) / 2.0
    # amplitude needed: Omega_GW,0 h^2 = NG value at f_yr, using Omega = 0.8222 A^2
    om_prod_needed = ng_omega_h2(F_YR) / omega_gw_today_h2(1.0)
    A_needed = float(np.sqrt(om_prod_needed / 0.8222))
    A_lab = float(delta2_zeta(K_PER_HZ * F_YR, 0.9649))
    # a k~k_B feature inside the band requires k_B <= k(60 nHz)
    T_B_needed = 1e16 * kmax / kB["T_B=1e16 GeV"]  # k_B scales linearly with T_B
    H_B_needed = float(np.sqrt(np.pi ** 2 * G_STAR_RD / 90.0) * T_B_needed ** 2 / Mpl)
    out["what_would_give_gamma3"] = {
        "required_spectral_index_of_P_R_at_nHz": n_needed,
        "rule": "broad P_R ~ k^n in RD gives Omega_GW ~ f^{2n} (Domenech arXiv:2109.01398)",
        "lab_spectrum_index_n": {kk: float(vv - 1.0) for kk, vv in BRANCHES.items()},
        "required_Delta2_zeta_at_f_yr_for_NANOGrav_amplitude": A_needed,
        "lab_Delta2_zeta_at_f_yr": A_lab,
        "log10_amplitude_gap": float(np.log10(A_needed / A_lab)),
        "alternative_IR_causal_tail": (
            "Omega_GW ~ f^3 (gamma = 2) is the universal IR causal floor "
            "(Cai, Pi & Sasaki 2020, PRD 102 083528, arXiv:1909.13728); "
            "gamma = 3 is neither that floor nor the flat-spectrum result -- it "
            "requires P_R ~ k^1 sustained ACROSS the band."),
        "k_B_needed_for_a_bounce_feature_in_band_Mpc-1": kmax,
        "T_B_needed_GeV": float(T_B_needed),
        "H_B_needed_GeV": H_B_needed,
        "paper_section_V_condition": "T_B >~ 1e8-1e10 GeV",
        "decades_below_section_V": float(np.log10(1e8 / T_B_needed))}

    verdict_ns = res["MB_anchored_ns0.9649"]
    out["verdict"] = {
        "answer": "A",
        "gamma_pred_MB_anchored": verdict_ns["gamma_pred"],
        "gamma_pred_pure_dust": res["pure_dust_ns1"]["gamma_pred"],
        "statement": (
            "The lab's CMB-anchored spectrum gives gamma_pred ~ %.2f (near-flat "
            "Omega_GW), NOT gamma = 3, and an amplitude ~1e%.0f times below the "
            "NANOGrav signal. The PTA channel is a NULL for this model: it neither "
            "predicts nor is constrained by the signal. gamma = 3 requires "
            "P_R ~ k^1 across the nHz band plus a ~1e%.0f amplitude enhancement -- "
            "i.e. exactly the PBH-forming small-scale enhancement the paper's "
            "section V C denies the model has." % (
                verdict_ns["gamma_pred"],
                verdict_ns["log10_amplitude_shortfall_vs_NANOGrav_at_f_yr"],
                np.log10(A_needed / A_lab)))}
    out["wall_seconds"] = round(time.time() - t0, 2)
    OUTJ.parent.mkdir(exist_ok=True)
    OUTJ.write_text(json.dumps(out, indent=1))

    # ---- figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    fn = f * 1e9
    for name in BRANCHES:
        ax.loglog(fn, curves[name], lw=2, label=f"lab spectrum, {name}")
    ax.loglog(fn, [ng_omega_h2(x) for x in f], "k--", lw=2,
              label=r"NANOGrav 15yr ($A=2.4\times10^{-15}$, $\gamma=3.2$)")
    ref = ng_omega_h2(F_YR)
    ax.loglog(fn, ref * (f / F_YR) ** 2.0, ":", color="crimson", lw=1.6,
              label=r"$\gamma=3$ ($\Omega\propto f^2$) at NANOGrav amplitude")
    ax.set_xlabel("f  [nHz]"); ax.set_ylabel(r"$\Omega_{\rm GW}h^2$"); ax.set_ylim(1e-24, 1e-7)
    ax.set_title("A3-3: induced GWs at nHz from the lab's own $\\Delta^2_\\zeta$")
    ax.legend(fontsize=7.5, loc="center left"); ax.grid(alpha=0.3, which="both")
    fig.tight_layout(); fig.savefig(OUTP, dpi=150)

    print(json.dumps({k2: out[k2] for k2 in
                      ["kernel_validation", "f_to_k", "branches",
                       "what_would_give_gamma3", "verdict"]}, indent=1))

if __name__ == "__main__":
    main()
