#!/usr/bin/env python3
r"""Row 15b -- the ENTROPY (spectator) sector through the three A2 matter-bounce
backgrounds.  Closes ledger row 15's named open item: "the A2 backgrounds have no
entropy sector, so F is not computable here".

What is computed (nothing is tuned):
 [1] a spectator field sigma (massless, then light m eta_B << 1) on each A2
     background: u = a sigma obeys u'' + (k^2 - a''/a + a^2 m^2) u = 0.  Seeded with
     the EXACT pre-bounce matter mode e^{-ik tau}(1 - i/(k tau))/sqrt(2k) (exact for
     all k tau in a matter era, so no sub-Hubble requirement), integrated through the
     bounce, read out at a symmetric late epoch.  ->  lambda_sigma(k).
 [2] the TENSOR mode on the same background, from an INDEPENDENT first-order system
     h' = Pi/a^2, Pi' = -a^2 k^2 h  (Pi = a^2 h'), same IC.  ->  lambda_T(k).
     lambda_sigma / lambda_T - 1 measures the operator identity numerically.
 [3] lambda_zeta^S1 == lambda_sigma by the z = a operator identity (scheme S1,
     geometric/dressed-metric); lambda_zeta^S2 is taken from the committed row 18a
     result on the Quintin background (fluid MS variable).
 [4] the pre-bounce viability condition on X = r_dec M_pl / sigma_* for r_after < 0.036.
 [5] k-dependence of lambda_T across the band -> the shift in the tensor tilt n_T.

Provenance: backgrounds + machinery imported from
  research/cubic_bounce_transmission/a2_transmission_linear.py  (single source of truth)
  research/cubic_bounce_transmission/row18a_s2_tensor/results.json (S2 lambda_zeta)
"""
import importlib.util, json, os, time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CBT = os.path.join(ROOT, "research", "cubic_bounce_transmission")
_s = importlib.util.spec_from_file_location("a2lin", os.path.join(CBT, "a2_transmission_linear.py"))
A = importlib.util.module_from_spec(_s); _s.loader.exec_module(A)

LOG = open(os.path.join(HERE, "row15b_entropy_sector.log"), "w")
def log(m=""):
    print(m); LOG.write(m + "\n"); LOG.flush()

R_BEFORE = 24.0          # row 10: r = 16 eps = 24 in the dust contraction, bounce-invariant in S1
R_TARGET = 0.036         # BICEP/Keck 2021
R_TARGET2 = 0.01


def tau_of(bg, eta):
    """matter-era conformal time, mirrored: |tau| = |eta| - eta_off, sign(tau) = sign(eta)."""
    off = bg["eta_off"]
    return np.where(eta >= 0, eta - off, eta + off)


def matter_vacuum(k, tau):
    """exact matter-era mode u = e^{-ik tau}(1 - i/(k tau))/sqrt(2k) and du/deta."""
    x = k * tau
    u = np.exp(-1j * x) * (1 - 1j / x) / np.sqrt(2 * k)
    du = (np.exp(-1j * x) * (-1j * k) * (1 - 1j / x)
          + np.exp(-1j * x) * (1j / (k * tau**2))) / np.sqrt(2 * k)
    return complex(u), complex(du)


def spectator_lambda(bg, k, eta_star, m=0.0, rtol=1e-12, atol=1e-16):
    """|sigma(+eta_star)/sigma(-eta_star)| for u'' + (k^2 - a''/a + a^2 m^2) u = 0."""
    sw = CubicSpline(bg["eta"], bg["appa"])
    sa = CubicSpline(bg["eta"], bg["a"])
    e0 = -eta_star
    u0, du0 = matter_vacuum(k, float(tau_of(bg, np.array(e0))))
    a0 = float(sa(e0))

    def rhs(e, y):
        w = float(sw(e)) - (m * float(sa(e)))**2
        return [y[1], -(k * k - w) * y[0], y[3], -(k * k - w) * y[2]]

    sol = solve_ivp(rhs, [e0, eta_star], [u0.real, du0.real, u0.imag, du0.imag],
                    rtol=rtol, atol=atol, method="DOP853")
    assert sol.success, sol.message
    uf = sol.y[0, -1] + 1j * sol.y[2, -1]
    s0, sf = u0 / a0, uf / float(sa(eta_star))
    return float(abs(sf / s0)), int(sol.t.size)


def tensor_lambda(bg, k, eta_star, rtol=1e-12, atol=1e-16):
    """|h(+eta_star)/h(-eta_star)| from the INDEPENDENT first-order system
    h' = Pi/a^2, Pi' = -a^2 k^2 h   (Pi = a^2 h'), same pre-bounce vacuum."""
    sa = CubicSpline(bg["eta"], bg["a"])
    e0 = -eta_star
    u0, du0 = matter_vacuum(k, float(tau_of(bg, np.array(e0))))
    a0, ap0 = float(sa(e0)), float(sa.derivative()(e0))
    h0 = u0 / a0
    Pi0 = a0 * du0 - ap0 * u0          # = a^2 (u/a)'

    def rhs(e, y):
        aa = float(sa(e))
        return [y[2] / aa**2, y[3] / aa**2, -aa**2 * k**2 * y[0], -aa**2 * k**2 * y[1]]

    sol = solve_ivp(rhs, [e0, eta_star], [h0.real, h0.imag, Pi0.real, Pi0.imag],
                    rtol=rtol, atol=atol, method="DOP853")
    assert sol.success, sol.message
    hf = sol.y[0, -1] + 1j * sol.y[1, -1]
    return float(abs(hf / h0)), int(sol.t.size)


def X_required(Lam, r_target, r_before=R_BEFORE):
    """r_after = r_before Lam^2 / (1 + Lam^2 (4/3) X^2) < r_target
       => X > sqrt( (3/4) ( r_before/r_target - 1/Lam^2 ) ).   Lam = lam_T/lam_zeta."""
    F2 = r_before / r_target                       # = F_eff^2 (CXB11 Eq. 61 normalisation)
    val = 0.75 * (F2 - 1.0 / Lam**2)
    return float(np.sqrt(val)), float(np.sqrt(F2))


def main():
    t0 = time.time()
    log("=" * 78)
    log("ROW 15b -- entropy (spectator) sector through the three A2 backgrounds")
    log("=" * 78)

    with open(os.path.join(CBT, "row18a_s2_tensor", "results.json")) as f:
        R18 = json.load(f)
    s2 = R18["rows"][0]
    LAM_S2_Q = s2["lam_zeta_S2"]; LAM_T_Q18 = s2["lam_T"]
    LAM_RATIO_S2 = LAM_T_Q18 / LAM_S2_Q
    log(f"[row 18a import] Quintin, k eta_B = {s2['k_etaB']}: lam_T = {LAM_T_Q18:.6f}, "
        f"lam_zeta^S1 = {s2['lam_zeta_S1']:.6f}, lam_zeta^S2 = {LAM_S2_Q:.6f} "
        f"-> Lambda_S2 = lam_T/lam_zeta^S2 = {LAM_RATIO_S2:.5f}")

    bgs = {"quintin": A.bg_quintin(), "LQC": A.bg_lqc(), "poly": A.bg_poly()}
    KETA = [1e-3, 3e-3, 1e-2]
    M_ETA_B = [0.0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2]          # m eta_B ; m^2 << H_B^2 since H_B eta_B = O(1)
    out = {"task": "NEXT_SCIENCE_LEDGER row 15b -- entropy sector in the A2 backgrounds",
           "date": "2026-09-04", "r_before": R_BEFORE,
           "row18a_import": {"lam_T": LAM_T_Q18, "lam_zeta_S1": s2["lam_zeta_S1"],
                             "lam_zeta_S2": LAM_S2_Q, "Lambda_S2": LAM_RATIO_S2,
                             "k_etaB": s2["k_etaB"]},
           "backgrounds": {}}

    for name, bg in bgs.items():
        eta_star = 20.0 * bg["eta_B"]
        assert eta_star < 0.5 * bg["eta_far"], (name, eta_star, bg["eta_far"])
        log(f"\n--- {name}  (label={bg['label']}, eta_B={bg['eta_B']:.6g}, "
            f"eta_off={bg['eta_off']:.6g}, eta_star={eta_star:.6g})")
        log("  k eta_B |   lam_sigma  |    lam_T     | lam_sig/lam_T-1 | dlam/lam (m eta_B = 1e-6, 1e-5, 1e-4, 1e-3, 1e-2)")
        rows = []
        for kt in KETA:
            k = kt / bg["eta_B"]
            lams, ns_ = spectator_lambda(bg, k, eta_star, m=0.0)
            lamT, nt_ = tensor_lambda(bg, k, eta_star)
            lm = {}
            for me in M_ETA_B[1:]:
                lm[f"{me:g}"] = spectator_lambda(bg, k, eta_star, m=me / bg["eta_B"])[0]
            row = dict(k_etaB=kt, k=float(k), lam_sigma=lams, lam_T=lamT,
                       lam_sigma_over_lam_T_minus_1=lams / lamT - 1.0,
                       lam_sigma_massive={kk: float(vv) for kk, vv in lm.items()},
                       dlam_over_lam_massive={kk: float(vv / lams - 1.0) for kk, vv in lm.items()},
                       steps_sigma=ns_, steps_T=nt_)
            rows.append(row)
            log(f"  {kt:7.4g} | {lams:12.7f} | {lamT:12.7f} | {lams/lamT-1:+15.2e} | "
                + "  ".join(f"{lm[key]/lams-1:+9.2e}" for key in ("1e-06", "1e-05", "0.0001", "0.001", "0.01")))
        # k-dependence of lam_T -> tensor-tilt shift  Delta n_T = 2 dln lam_T/dln k
        lt = np.array([r["lam_T"] for r in rows]); kk = np.array(KETA)
        c = float((1.0 - lt[-1] / lt[0]) / kk[-1] ** 2)      # lam_T ~ lam0 (1 - c (k eta_B)^2)
        dln = [float(-2.0 * c * x**2) for x in kk]
        out["backgrounds"][name] = dict(
            label=bg["label"], eta_B=float(bg["eta_B"]), eta_off=float(bg["eta_off"]),
            eta_star=float(eta_star), rows=rows,
            max_abs_lam_sigma_over_lam_T_minus_1=float(max(abs(r["lam_sigma_over_lam_T_minus_1"]) for r in rows)),
            lam_T_curvature_c=c,
            dln_lamT_dln_k=dict(zip([f"{x:g}" for x in kk], dln)),
            delta_n_T=dict(zip([f"{x:g}" for x in kk], [2 * d for d in dln])))
        log(f"  lam_T(k eta_B) = lam_T(0)[1 - c (k eta_B)^2], c = {c:.4g}  ->  "
            f"Delta n_T = 2 dln lam_T/dln k = {2*dln[0]:+.3e} at k eta_B = 1e-3")

    # ---- viability: the pre-bounce condition on X = r_dec Mpl/sigma_*
    log("\n" + "=" * 78)
    log("[viability] r_after = 24 Lambda^2 / (1 + Lambda^2 (4/3) X^2),  X = r_dec Mpl/sigma_*")
    via = {}
    for sch, Lam in (("S1", 1.0), ("S2", LAM_RATIO_S2)):
        e = {}
        for tgt in (R_TARGET, R_TARGET2):
            X, F = X_required(Lam, tgt)
            e[f"r<{tgt}"] = dict(X_min=X, F_eff_min=F,
                                 sigma_star_max_over_Mpl_at_rdec_1=float(1.0 / X))
        e["Lambda"] = float(Lam)
        e["r_after_single_field"] = float(R_BEFORE * Lam**2)
        via[sch] = e
        log(f"  scheme {sch}: Lambda = {Lam:.5f}, single-field r_after = {R_BEFORE*Lam**2:.4g}; "
            f"X_min(r<0.036) = {e['r<0.036']['X_min']:.4f}, X_min(r<0.01) = {e['r<0.01']['X_min']:.4f}, "
            f"F_eff_min = {e['r<0.036']['F_eff_min']:.4f}")
    via["scheme_spread_X_min_r0.036"] = float(abs(via["S2"]["r<0.036"]["X_min"]
                                                  / via["S1"]["r<0.036"]["X_min"] - 1.0))
    log(f"  -> X_min is scheme-independent to {via['scheme_spread_X_min_r0.036']:.2e} "
        f"(the tensor and the spectator share lambda, so Lambda cancels between "
        f"numerator and curvaton term in the large-X limit)")
    out["viability"] = via
    out["runtime_s"] = time.time() - t0
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    log(f"\n[done] {out['runtime_s']:.1f} s -> results.json")
    return out


def make_figure(out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))
    for name, B in out["backgrounds"].items():
        ks = [r["k_etaB"] for r in B["rows"]]
        ax[0].plot(ks, [r["lam_sigma"] for r in B["rows"]], "o-", label=rf"$\lambda_\sigma$ {name}")
        ax[0].plot(ks, [r["lam_T"] for r in B["rows"]], "x--", label=rf"$\lambda_T$ {name}")
        ax[1].semilogy(ks, [abs(r["lam_sigma_over_lam_T_minus_1"]) + 1e-18 for r in B["rows"]],
                       "o-", label=name)
        ax[2].semilogy(ks, [abs(r["dlam_over_lam_massive"]["0.01"]) + 1e-18 for r in B["rows"]],
                       "s-", label=rf"{name}, $m\eta_B=10^{{-2}}$")
    ax[0].set_xscale("log"); ax[0].set_xlabel(r"$k\eta_B$"); ax[0].set_ylabel(r"$\lambda$")
    ax[0].set_title("spectator vs tensor transfer"); ax[0].legend(fontsize=7)
    ax[1].set_xscale("log"); ax[1].set_xlabel(r"$k\eta_B$")
    ax[1].set_ylabel(r"$|\lambda_\sigma/\lambda_T-1|$")
    ax[1].set_title("operator identity (numerical)"); ax[1].legend(fontsize=7)
    ax[2].set_xscale("log"); ax[2].set_xlabel(r"$k\eta_B$")
    ax[2].set_ylabel(r"$|\Delta\lambda_\sigma/\lambda_\sigma|$")
    ax[2].set_title("light-mass correction"); ax[2].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "row15b_entropy_sector.png"), dpi=140)


if __name__ == "__main__":
    make_figure(main())
