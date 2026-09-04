#!/usr/bin/env python3
"""Ledger row 9 (A3-1e) lane (a) -- does the Quintin+2015 scalar-field-velocity-dip
amplification of zeta exist on the lab's three A2 backgrounds, and what happens to
the curvature spectrum / cubic term in the band k eta_B in [0.1, 10] that the S1
super-Hubble transfer (validity k eta_B <~ 1e-2) does not cover?

Literature anchor: J. Quintin, Z. Sherkatghanad, Y.-F. Cai, R. H. Brandenberger,
"Evolution of cosmological perturbations and the production of non-Gaussianities
through a nonsingular bounce: Indications for a no-go theorem in single field
matter bounce cosmologies", arXiv:1508.04141 (PRD 92, 063532).

  bounce-phase ansatz     H(t) = Upsilon (t - t_B),  a(t) = a_B exp[Upsilon (t-t_B)^2/2],
                          phidot(t) = phidot_B exp[-(t-t_B)^2/T^2]
  Eq. (44)                f_NL ~ (Delta zeta)^2 / (Delta t_B M_p^2)
  Eq. (79)                zetadot_max ~= zetadot(t_B^-) [phidot_B/phidot(t_amp-)]^2
  Eq. (80)                zeta(t_amp+) - zeta(t_amp-) <~ zetadot(t_B^-)
                                  [phidot_B/phidot(t_amp-)]^2 (t_amp+ - t_amp-)
  t_amp+- = t_B +- Delta t_amp  (the window in which the linear-growth
                          approximation of their Regime II holds)
  Eq. (30)                |1 + Delta zeta_k*/zeta_k*(eta_B^-)| >~ 50.1
                          -- the amplification REQUIRED to push r below 0.12,
                          not one they achieve; their conclusion is the opposite,
                          that the growth "is very limited because of the
                          conservation of curvature perturbations on super-Hubble
                          scales".  That asymmetry is their no-go.

Nothing here is tuned to any target.  Every number in the .md comes from results.json.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import a2_transmission_linear as a2  # noqa: E402

LOG = os.path.join(HERE, "lane9a_velocity_dip.log")
JSON_OUT = os.path.join(HERE, "results.json")
PNG = os.path.join(HERE, "lane9a_growth_vs_ketaB.png")
_lines = []


def log(m=""):
    print(m)
    _lines.append(m)


K_TABLE = [0.1, 0.3, 1.0, 3.0, 10.0]
K_PLOT = list(np.geomspace(1e-3, 3e1, 46))


# =====================================================================
# [1] Is a scalar-field velocity -- hence a phidot dip -- definable at all?
# =====================================================================
def hdot_profile(bg):
    """Hdot(eta) = a''/a^3 - 2 H^2 = appa/a^2 - 2 (a'/a^2)^2, from the stored arrays."""
    eta, a, appa = bg["eta"], bg["a"], bg["appa"]
    ap = bg["af"].derivative()(eta)
    H = ap / a**2
    Hdot = appa / a**2 - 2.0 * H**2
    return eta, a, H, Hdot


def velocity_block(bg):
    """Two candidate identifications of Quintin's phidot on a lab background.

    (i) TOTAL-SECTOR:  Friedmann gives rho + p = -2 M_p^2 Hdot for ANY background,
        so a single canonical field would need phidot^2 = -2 M_p^2 Hdot.  This
        vanishes identically at the NEC boundary (Hdot = 0 defines eta_B) and is
        negative (ghost) throughout the NEC-violating window.  It is therefore NOT
        Quintin's phidot -- theirs is the velocity of the REGULAR matter scalar in a
        two-component (matter + ghost-condensate/Lee-Wick) model, which stays finite
        while the total rho+p crosses zero.  Reported here only to show that
        substituting it manufactures a spurious divergence at eta_B.

    (ii) MATTER-SECTOR: the lab's backgrounds do not specify a matter Lagrangian, so
        phidot is an ADDED input.  For the one realisation that IS fixed by the
        geometry -- a single field with a constant kinetic normalisation on
        H = Upsilon (t - t_B), i.e. Hdot = Upsilon = const -- phidot^2 = 2 M_p^2
        |Hdot| is CONSTANT through the whole bounce phase: T -> infinity in their
        ansatz, and their Eq. (79) factor is exactly 1.
    """
    eta, a, H, Hdot = hdot_profile(bg)
    eB = bg["eta_B"]
    ins = np.abs(eta) < eB
    Hd_in = Hdot[ins]
    Hd_B = float(np.interp(0.0, eta, Hdot))
    flat = float(np.max(np.abs(Hd_in - Hd_B)) / abs(Hd_B)) if abs(Hd_B) > 0 else np.nan
    rows = []
    for frac in (0.25, 0.5, 0.75, 0.9, 0.99, 1.0):
        e = frac * eB
        hd = float(np.interp(-e, eta, Hdot))
        rows.append({"eta_amp_minus_over_etaB": frac,
                     "Hdot_at_eta_amp_minus": hd,
                     "total_sector_factor_Hdot_ratio": (abs(Hd_B / hd) if hd != 0 else None)})
    return {"eta_B": float(eB), "Hdot_at_bounce": Hd_B,
            "Hdot_max_frac_variation_inside_NEC_window": flat,
            "total_sector_identification": rows,
            "matter_sector_factor_constant_kinetic": 1.0}


# =====================================================================
# [2] the lab's own growth factor lambda_zeta(k), extended to k eta_B ~ 1
# =====================================================================
def growth_at_k(bg, k, eta_far, rtol=1e-11, atol=1e-14):
    """Evolve the adiabatic-vacuum mode across the bounce and measure:

      alpha_post   exact constant-branch amplitude in the expanding matter era
                   (projection onto the exact S/C matter basis; = zeta(+inf)).
      lam_zeta(k)  = |alpha_post| / |zeta(-eta_B)|  -- the lab's lambda_zeta,
                   generalised to finite k by using the numerically evolved
                   zeta = mu/a at the NEC boundary instead of the k->0 branch value.
      G(k)         = |alpha_post| / |alpha_pre + 2 beta_pre I_inf|  -- the ratio of
                   the true transfer to the S1 super-Hubble prediction
                   (alpha, beta) -> (alpha + 2 beta I_inf, beta).  G = 1 means the
                   S1 formula is exact; G != 1 is precisely the content the
                   k eta_B <~ 1e-2 band never tested.  Delta^2_zeta ratio = G^2.
    """
    ev = a2.evolve(bg, k, eta_far, ic="vacuum", rtol=rtol, atol=atol)
    am, bm, ap = ev["alpha_pre"], ev["beta_pre"], ev["alpha_post"]
    s1_pred = am + 2.0 * bm * bg["I_inf"]
    z_hB = a2.zeta_at(bg, ev, -bg["eta_B"])
    lam_sh = abs((am + 2.0 * bm * bg["I_inf"]) / (am + bm * (bg["I_inf"] + float(bg["Jf"](-bg["eta_B"])))))
    return {"k_etaB": float(k * bg["eta_B"]), "k": float(k),
            "eta_far_over_etaB": float(eta_far / bg["eta_B"]),
            "ok": bool(ev["success"]),
            "abs_alpha_pre": float(abs(am)), "abs_beta_pre": float(abs(bm)),
            "abs_alpha_post": float(abs(ap)),
            "abs_beta_post": float(abs(ev["beta_post"])),
            "abs_zeta_at_minus_etaB": float(abs(z_hB)),
            "lambda_zeta": float(abs(ap) / abs(z_hB)),
            "lambda_zeta_S1_superhubble": float(lam_sh),
            "G_transfer_over_S1": float(abs(ap) / abs(s1_pred)),
            "Delta2_ratio_vs_S1": float((abs(ap) / abs(s1_pred)) ** 2),
            "lambda_zeta_is_a_growth_factor": bool(k * bg["eta_B"] <= 1.0)}


def sweep(bg, ks, tag, rtol=1e-11):
    eta_far = min(0.9 * bg["eta_far"], 400.0 * bg["eta_B"])
    out = []
    for kt in ks:
        r = growth_at_k(bg, kt / bg["eta_B"], eta_far, rtol=rtol)
        r["background"] = tag
        out.append(r)
    return out


# =====================================================================
# [3] Eq. (79) factor and [4] the Eq. (44) propagation
# =====================================================================
def eq79_factor(dt_amp_over_T2):
    """Quintin Eq. (79)/(80) amplification factor under THEIR ansatz
    phidot = phidot_B exp[-(t-t_B)^2/T^2]:

        [phidot_B/phidot(t_amp-)]^2 = exp(+2 Delta t_amp^2 / T^2).

    The factor is controlled ENTIRELY by T, the width of the matter-sector velocity
    profile.  T is a free matter parameter: the geometry H(t) = Upsilon (t - t_B)
    does not fix it.  T -> infinity (constant |phidot|, the unique single-field
    constant-kinetic realisation of Hdot = Upsilon = const) gives exactly 1.
    """
    return float(np.exp(2.0 * dt_amp_over_T2))


def eq44_propagation(lam, dtB, fnl_before=-35.0 / 16.0, T_fNL=None):
    """Quintin Eq. (44) structure f_NL ~ (Delta zeta)^2/(Delta t_B M_p^2), with
    Delta zeta/zeta = lam - 1 the growth actually measured on the background, in
    units M_p = 1 and zeta normalised to its pre-bounce value.  Reported as a
    SCALING (their '~'), never as a calibrated prediction: the lab's own
    normalisation of this term is lane (b)'s in-in Delta f_NL^bounce.
    """
    dz = lam - 1.0
    return {"lambda_zeta": float(lam), "Delta_zeta_over_zeta": float(dz),
            "eq44_scaling_fNL_bounce": float(dz**2 / dtB),
            "eq44_relative_to_lambda5": float((dz**2) / ((5.0 - 1.0) ** 2)),
            "fNL_before_input": fnl_before,
            "T_fNL_multiplicative": T_fNL}



def feature_summary(plot_rows):
    """Numerical floor of the projection (|G-1| at k eta_B <= 1e-2, where S1 is exact
    by construction) and the extremum of G inside the band k eta_B in [0.1, 10]."""
    lo = [r for r in plot_rows if r["k_etaB"] <= 1e-2]
    band = [r for r in plot_rows if 0.1 <= r["k_etaB"] <= 10.0]
    floor = max(abs(r["G_transfer_over_S1"] - 1.0) for r in lo) if lo else None
    hi = max(band, key=lambda r: r["G_transfer_over_S1"])
    lowest = min(band, key=lambda r: r["G_transfer_over_S1"])
    ext = hi if abs(hi["G_transfer_over_S1"] - 1) >= abs(lowest["G_transfer_over_S1"] - 1) else lowest
    return {"numerical_floor_absG_minus_1_at_smallk": floor,
            "band_extremum_k_etaB": ext["k_etaB"],
            "band_extremum_G": ext["G_transfer_over_S1"],
            "band_extremum_Delta2_ratio": ext["Delta2_ratio_vs_S1"],
            "band_max_G": hi["G_transfer_over_S1"], "band_max_k_etaB": hi["k_etaB"],
            "band_min_G": lowest["G_transfer_over_S1"], "band_min_k_etaB": lowest["k_etaB"],
            "significant_vs_floor": (bool(abs(ext["G_transfer_over_S1"] - 1.0) > 5.0 * floor)
                                     if floor else None)}


def make_png(res, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(11.0, 4.2))
    cols = {"quintin": "#d62728", "LQC": "#1f77b4", "poly": "#2ca02c"}
    for tag in ("quintin", "LQC", "poly"):
        rows = sorted(res["sweeps"][tag]["plot"], key=lambda r: r["k_etaB"])
        x = [r["k_etaB"] for r in rows]
        ax[0].plot(x, [r["lambda_zeta"] for r in rows], "-", color=cols[tag], label=tag)
        ax[1].plot(x, [r["G_transfer_over_S1"] for r in rows], "-", color=cols[tag], label=tag)
    for a_ in ax:
        a_.set_xscale("log")
        a_.axvspan(0.1, 10.0, color="0.85", zorder=0)
        a_.axvline(1e-2, ls=":", color="0.4")
        a_.set_xlabel(r"$k\,\eta_B$")
        a_.legend(fontsize=8)
        a_.grid(alpha=0.25)
    ax[0].set_yscale("log")
    ax[0].set_ylabel(r"$\lambda_\zeta(k)=|\zeta(+\infty)/\zeta(-\eta_B)|$")
    ax[0].axvspan(1.0, 4e1, color="#c9a227", alpha=0.18, zorder=0)
    ax[0].text(1.6, 2.0, "phase-sampled\n(not a growth factor)", fontsize=7, color="#7a5c00")
    ax[0].set_title(r"growth factor across the bounce (valid for $k\eta_B\lesssim1$)")
    ax[1].set_ylabel(r"$G(k)=|\alpha_{\rm post}|/|\alpha_{\rm pre}+2\beta_{\rm pre}I_\infty|$")
    ax[1].set_title(r"deviation from the S1 super-Hubble transfer ($\Delta^2$ ratio $=G^2$)")
    fig.suptitle("Ledger 9 lane (a): no velocity-dip amplification on the lab backgrounds; "
                 r"shaded = $k\eta_B\in[0.1,10]$, dotted = S1 validity edge", fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    t0 = time.time()
    log("=" * 78)
    log("LEDGER ROW 9 (A3-1e) LANE (a): Quintin+2015 velocity-dip amplification")
    log("=" * 78)
    bgs = {"quintin": a2.bg_quintin(dtB=1.0), "LQC": a2.bg_lqc(), "poly": a2.bg_poly(eta_b=1.0)}
    res = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "backgrounds": {},
           "velocity": {}, "sweeps": {}, "eq79": {}, "eq44": {}, "convergence": {}}
    for tag, b in bgs.items():
        res["backgrounds"][tag] = {"label": b["label"], "params": b["params"],
                                   "eta_B": b["eta_B"], "I_inf": b["I_inf"], "A": b["A"]}
        log(f"  [bg] {tag:8s} {b['label']:22s} eta_B={b['eta_B']:.6g} I_inf={b['I_inf']:.6g}")

    log("")
    log("[1] scalar-field velocity: is a phidot dip definable?")
    for tag, b in bgs.items():
        v = velocity_block(b)
        res["velocity"][tag] = v
        log(f"    {tag:8s} Hdot(t_B)={v['Hdot_at_bounce']:+.6g}  "
            f"max frac variation of Hdot inside |eta|<eta_B = "
            f"{v['Hdot_max_frac_variation_inside_NEC_window']:.3e}")
        for r in v["total_sector_identification"]:
            f = r["total_sector_factor_Hdot_ratio"]
            log(f"        eta_amp-/eta_B={r['eta_amp_minus_over_etaB']:.2f}  "
                f"Hdot={r['Hdot_at_eta_amp_minus']:+.6g}  "
                f"total-sector [phidot_B/phidot]^2 = "
                f"{('%.4g' % f) if f is not None else 'divergent'}")

    log("")
    log("[2] lambda_zeta(k) and the S1-deviation transfer G(k)")
    for tag, b in bgs.items():
        tab = sweep(b, K_TABLE, tag)
        plot = sweep(b, K_PLOT, tag)
        res["sweeps"][tag] = {"table": tab, "plot": plot,
                              "feature": feature_summary(plot)}
        log(f"    --- {tag} ---")
        log("      k*eta_B    lambda_zeta   lambda_S1     G(k)      Delta^2 ratio")
        for r in tab:
            log(f"      {r['k_etaB']:7.3g}   {r['lambda_zeta']:10.5f}   "
                f"{r['lambda_zeta_S1_superhubble']:9.5f}   {r['G_transfer_over_S1']:8.5f}   "
                f"{r['Delta2_ratio_vs_S1']:8.5f}"
                + ("" if r["lambda_zeta_is_a_growth_factor"] else
                   "   [lambda: phase-sampled, NOT a growth factor]"))
        fs = res["sweeps"][tag]["feature"]
        log(f"      floor |G-1|(k eta_B<=1e-2) = {fs['numerical_floor_absG_minus_1_at_smallk']:.2e}; "
            f"band extremum G={fs['band_extremum_G']:.4f} at k eta_B={fs['band_extremum_k_etaB']:.3g} "
            f"(Delta^2 ratio {fs['band_extremum_Delta2_ratio']:.4f}); "
            f"significant vs floor: {fs['significant_vs_floor']}")

    log("")
    log("[3] Quintin Eq. (79) amplification factor per background")
    for tag, b in bgs.items():
        lam_small = res["sweeps"][tag]["table"][0]["lambda_zeta"]
        realisable = (tag == "quintin")
        e79 = {"single_scalar_realisation_exists": realisable,
               "reason": ("H = Upsilon(t-t_B) is Quintin's own single-field bounce ansatz; "
                          "Hdot = Upsilon is constant across the NEC window, so a single "
                          "field with constant kinetic normalisation has phidot^2 = "
                          "2 M_p^2 Upsilon = const: T -> inf in their profile."
                          if realisable else
                          "effective-fluid background (no matter Lagrangian is specified); "
                          "a matter-sector phidot is not definable without adding one. The "
                          "only geometry-fixed velocity is the total-sector "
                          "phidot^2 = -2 M_p^2 Hdot, which vanishes at eta_B by the "
                          "definition of the NEC boundary and is not Quintin's phidot."),
               "factor_Dt_over_T_0": eq79_factor(0.0),
               "factor_if_T_equals_dt_amp": eq79_factor(1.0),
               "adopted_factor": 1.0,
               "lambda_zeta_measured_smallk": lam_small}
        res["eq79"][tag] = e79
        log(f"    {tag:8s} single-scalar realisation: "
            f"{'YES' if realisable else 'NO (effective fluid)'} ; "
            f"adopted [phidot_B/phidot(t_amp-)]^2 = {e79['adopted_factor']:.1f} "
            f"(T -> inf); their T = Delta t_amp would give "
            f"{e79['factor_if_T_equals_dt_amp']:.3f}")

    log("")
    log("[4] Eq. (44) propagation with the MEASURED growth (no dip)")
    for tag, b in bgs.items():
        dtB = b["params"].get("dtB", 2.0 * b["eta_B"])
        for r in res["sweeps"][tag]["table"]:
            key = f"{tag}@k_etaB={r['k_etaB']:g}"
            res["eq44"][key] = eq44_propagation(r["lambda_zeta"], dtB)
        rq = res["sweeps"][tag]["table"]
        log(f"    {tag:8s} Delta zeta/zeta: "
            + ", ".join(f"{r['k_etaB']:g}->{r['lambda_zeta']-1:+.3f}" for r in rq))

    log("")
    log("[5] convergence (rtol 1e-11 -> 1e-9, eta_far x2) on the quintin background")
    b = bgs["quintin"]
    for kt in (0.1, 1.0, 10.0):
        base = growth_at_k(b, kt / b["eta_B"], min(0.9 * b["eta_far"], 400.0 * b["eta_B"]))
        alt1 = growth_at_k(b, kt / b["eta_B"], min(0.9 * b["eta_far"], 400.0 * b["eta_B"]),
                           rtol=1e-9, atol=1e-12)
        alt2 = growth_at_k(b, kt / b["eta_B"], min(0.9 * b["eta_far"], 800.0 * b["eta_B"]))
        res["convergence"][f"k_etaB={kt:g}"] = {
            "rel_dev_rtol": float(abs(alt1["lambda_zeta"] / base["lambda_zeta"] - 1)),
            "rel_dev_eta_far": float(abs(alt2["lambda_zeta"] / base["lambda_zeta"] - 1)),
            "rel_dev_G_rtol": float(abs(alt1["G_transfer_over_S1"] / base["G_transfer_over_S1"] - 1))}
        c = res["convergence"][f"k_etaB={kt:g}"]
        log(f"    k eta_B={kt:<5g} d(lambda)/lambda: rtol {c['rel_dev_rtol']:.2e}, "
            f"eta_far {c['rel_dev_eta_far']:.2e}; d(G)/G rtol {c['rel_dev_G_rtol']:.2e}")

    make_png(res, PNG)
    res["wall_clock_s"] = round(time.time() - t0, 2)
    res["scheme"] = ("S1 geometric / dressed-metric extension: z = a, eps_eff = 1/2, "
                     "c_s = 1, eta_sr = 0, lambda = 0; adiabatic-vacuum initial data in "
                     "the contracting matter era; exact S/C matter-basis projection at "
                     "both ends (no super-Hubble approximation in the measurement).")
    with open(JSON_OUT, "w") as f:
        json.dump(res, f, indent=2)
    log("")
    log(f"  wrote {JSON_OUT}")
    log(f"  wrote {PNG}")
    log(f"  wall clock {res['wall_clock_s']} s")
    with open(LOG, "w") as f:
        f.write("\n".join(_lines) + "\n")


if __name__ == "__main__":
    main()
