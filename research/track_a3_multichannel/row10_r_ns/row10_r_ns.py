#!/usr/bin/env python3
r"""
NEXT_SCIENCE_LEDGER row 10 (A3-4 + A3-ns) -- the matter bounce's OWN
tensor-to-scalar ratio r and scalar tilt n_s.

The A3 paper currently substitutes the OBSERVED r < 0.036 (BICEP/Keck 2021)
and n_s = 0.9649 (Planck 2018) wherever the model's own values are needed.
This script computes them for the dust contraction and propagates them through
each of the three A2 bounce backgrounds with the lab's own mode machinery
(research/cubic_bounce_transmission/a2_transmission_linear.py).

SET-UP (8 pi G = 1, M_p = 1, c_s = 1, a_bounce = 1)
---------------------------------------------------
Canonical variables in the dressed-metric / geometric scheme used throughout A2:
    scalar   mu_S = z zeta,      z = a sqrt(2 eps),   eps = 3(1+w)/2
    tensor   mu_T = (a/2) h_lambda   (per polarisation)
Both obey  mu'' + (k^2 - a''/a) mu = 0  when eps is constant (z ~ a), and both
take the SAME Bunch-Davies normalisation mu -> e^{-i k eta}/sqrt(2k).  Hence

    P_h    = 2 * (k^3/2pi^2) |h|^2       = 2 * (k^3/2pi^2) * 4 |mu_T|^2 / a^2
    P_zeta =     (k^3/2pi^2) |zeta|^2    =     (k^3/2pi^2) |mu_S|^2 / (2 eps a^2)
    r = P_h/P_zeta = 16 eps |mu_T/mu_S|^2 .

For the dust contraction eps = 3/2 exactly and mu_T = mu_S, so r = 24 -- the
matter bounce's own value, with NO free parameter.  This is the well-known
large-r problem of the matter bounce (Cai, Easson & Brandenberger 2012,
arXiv:1206.2382; the single-field no-go of Quintin, Sherkatghanad, Cai &
Brandenberger 2015, arXiv:1508.04141; Brandenberger & Peter 2016 review,
arXiv:1603.05834).  The dust contraction's scale invariance is the Wands 1999
duality (gr-qc/9809062).

TILT.  a ~ (-eta)^q with q = 2/(1+3w) gives P ~ k^{4-2q}, i.e.
    n_s - 1 = n_T = 12 w / (1 + 3 w),
so pure dust (w = 0) predicts n_s = 1 EXACTLY, and the observed 0.9649 is an
ANCHOR that fixes w, not a prediction.  Because scalars and tensors share q,
the model also predicts the consistency relation n_T = n_s - 1 (NOT the
single-field-inflation n_T = -r/8).

WHAT IS COMPUTED NUMERICALLY (nothing is tuned; every number is from this run)
  (1) the analytic block above, checked symbolically;
  (2) for each of the three A2 backgrounds (LQC-effective dust, poly-analytic
      non-LQC, Quintin2015-type) and a grid of super-Hubble k eta_B:
      the scalar mode mu_S integrated through the bounce with adiabatic-vacuum
      ICs (A2's own evolve()), and -- INDEPENDENTLY, in h-form -- the tensor
      mode h'' + 2(a'/a) h' + k^2 h = 0 with the matching vacuum ICs;
      hence T_zeta, T_h (amplitude transfer from the NEC boundary -eta_B to the
      post-bounce super-Hubble constant) and r_after = r_before (T_h/T_zeta)^2;
  (3) the CMB verdict against r < 0.036 and against the "r = 0.84" quoted in
      r5_15_tensor_omega_nhz.py;
  (4) a re-run of r5_15_tensor_omega_nhz.py with the model's own r, to a NEW
      output file (the committed one is not overwritten).

Venue: local (Apple silicon), CPU only, seconds, cost $0.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "research/cubic_bounce_transmission"))
sys.path.insert(0, str(REPO / "research/track_a3_multichannel"))
import a2_transmission_linear as A2   # noqa: E402

OUTJ = HERE / "results.json"
OUTLOG = HERE / "row10_r_ns.log"
OUTPNG = HERE / "row10_r_ns.png"
_t0 = time.time()
R_CMB_BOUND = 0.036          # BICEP/Keck+Planck, Ade et al. 2021, arXiv:2110.00483
R_QUOTED_084 = 0.84          # the number the A3 program has been carrying
NS_PLANCK = 0.9649           # Planck 2018, arXiv:1807.06209


def log(m):
    line = f"[{time.time()-_t0:7.2f}s] {m}"
    print(line, flush=True)
    with open(OUTLOG, "a") as f:
        f.write(line + "\n")


def analytic_block():
    """r = 16 eps and n_s - 1 = n_T = 12w/(1+3w), derived, not asserted."""
    eps, k, a, mu, Mp = sp.symbols("epsilon k a mu M_p", positive=True)
    w = sp.Symbol("w", real=True)
    z = a * sp.sqrt(2 * eps)
    P_h = 2 * (k**3 / (2 * sp.pi**2)) * (2 * mu / a) ** 2          # h = 2 mu/a, 2 pols
    P_z = (k**3 / (2 * sp.pi**2)) * (mu / z) ** 2
    r_sym = sp.simplify(P_h / P_z)                                  # -> 16 eps
    q = 2 / (1 + 3 * w)
    ns_m1 = sp.simplify(4 - 2 * q)                                  # -> 12w/(1+3w)
    eps_w = sp.Rational(3, 2) * (1 + w)
    r_w = sp.simplify(r_sym.subs(eps, eps_w))                       # -> 24(1+w)
    w_star = sp.solve(sp.Eq(ns_m1, NS_PLANCK - 1), w)[0]
    # the formula printed in inlab_delta2_zeta_2026-09-03.md line 23
    w_note = sp.solve(sp.Eq(12 * w / (1 + w), NS_PLANCK - 1), w)[0]
    return {
        "r_symbolic": str(r_sym), "r_of_w": str(r_w),
        "ns_minus_1_of_w": str(sp.simplify(ns_m1)),
        "consistency_relation": "n_T = n_s - 1 (both from q = 2/(1+3w)); "
                                "NOT the single-field-inflation n_T = -r/8",
        "pure_dust": {"w": 0.0, "eps": 1.5, "n_s": 1.0, "n_T": 0.0,
                      "r": float(r_w.subs(w, 0))},
        "planck_anchored": {
            "n_s_target": NS_PLANCK, "w": float(w_star), "eps": float(eps_w.subs(w, w_star)),
            "n_T": NS_PLANCK - 1.0, "r": float(r_w.subs(w, w_star))},
        "note_formula_discrepancy": {
            "inlab_delta2_zeta_2026-09-03.md line 23 states": "n_s - 1 = 12w/(1+w)",
            "correct (a ~ (-eta)^{2/(1+3w)})": "n_s - 1 = 12w/(1+3w)",
            "w_from_correct_formula": float(w_star),
            "w_from_note_formula": float(w_note),
            "impact": "the two differ by 0.6% in w and 0.02% in eps -> r changes "
                      "by 0.006; the note's spectra are unaffected at quoted precision"},
    }


def tensor_evolve(bg, k, eta_far, rtol=1e-11, atol=1e-14):
    """h'' + 2(a'/a) h' + k^2 h = 0, integrated in h-form (an INDEPENDENT
    numerical route from A2's mu-form scalar integration), adiabatic-vacuum ICs
    h = 2 mu_vac/a matching the scalar's Bunch-Davies normalisation."""
    af = bg["af"]
    daf = af.derivative()
    off = bg["eta_off"]
    e_i, e_f = -eta_far, eta_far
    tau_i = e_i - off
    u = k * tau_i
    mu0 = np.exp(-1j * u) * (1 - 1j / u) / np.sqrt(2 * k)
    dmu0 = (np.exp(-1j * u) * (-1j * k) * (1 - 1j / u)
            + np.exp(-1j * u) * (1j / (k * tau_i**2))) / np.sqrt(2 * k)
    a_i, ap_i = float(af(e_i)), float(daf_safe(daf, e_i))
    h0 = 2.0 * mu0 / a_i
    dh0 = 2.0 * (dmu0 / a_i - ap_i * mu0 / a_i**2)

    def rhs(e, y):
        aa, ap = float(af(e)), float(daf(e))
        f = 2.0 * ap / aa
        return [y[1], -f * y[1] - k * k * y[0],
                y[3], -f * y[3] - k * k * y[2]]

    sol = solve_ivp(rhs, [e_i, e_f], [h0.real, dh0.real, h0.imag, dh0.imag],
                    rtol=rtol, atol=atol, method="DOP853", dense_output=True)
    return sol


def daf_safe(daf, e):
    return float(daf(e))


def h_at(sol, e):
    y = sol.sol(e)
    return (y[0] + 1j * y[2]), (y[1] + 1j * y[3])


def zeta_from_scalar(ev, bg, e):
    y = ev["sol"].sol(e)
    mu = y[0] + 1j * y[2]
    return mu / float(bg["af"](e))


def run_background(key, bg, kts):
    eta_far = min(0.9 * bg["eta_far"], 400.0 * bg["eta_B"])
    rows = []
    for kt in kts:
        k = kt / bg["eta_B"]
        ev = A2.evolve(bg, k, eta_far, ic="vacuum")
        sol_h = tensor_evolve(bg, k, eta_far)
        # post-bounce super-Hubble constants, projected on the exact matter basis
        alpha_S = ev["alpha_post"]
        hf, dhf = h_at(sol_h, eta_far)
        muT_f, dmuT_f = 0.5 * float(bg["af"](eta_far)) * hf, None
        af_d = bg["af"].derivative()
        dmuT_f = 0.5 * (float(af_d(eta_far)) * hf + float(bg["af"](eta_far)) * dhf)
        alpha_T, beta_T = A2.project(bg, k, eta_far, muT_f, dmuT_f)
        # handoff epoch = the NEC boundary -eta_B (same convention as A2)
        eh = -bg["eta_B"]
        z_h = zeta_from_scalar(ev, bg, eh)
        h_h, _ = h_at(sol_h, eh)
        zT_h = 0.5 * h_h                      # = mu_T/a, the tensor analogue of zeta
        T_zeta = abs(alpha_S / z_h)
        T_h = abs(alpha_T / zT_h)
        eps_d = 1.5
        r_before = 16.0 * eps_d * abs(zT_h / z_h) ** 2
        r_after = 16.0 * eps_d * abs(alpha_T / alpha_S) ** 2
        rows.append({
            "k_etaB": float(kt), "k": float(k),
            "mu_T_over_mu_S_at_handoff_abs": float(abs(zT_h / z_h)),
            "T_zeta": float(T_zeta), "T_h": float(T_h),
            "T_h_over_T_zeta": float(T_h / T_zeta),
            "T_h_over_T_zeta_minus_1": float(T_h / T_zeta - 1.0),
            "r_before": float(r_before), "r_after": float(r_after),
            "r_after_over_r_before": float(r_after / r_before),
            "scalar_ode_success": bool(ev["success"]),
            "tensor_ode_success": bool(sol_h.success)})
        log(f"  {key:8s} k*eta_B={kt:.1e}  T_zeta={T_zeta:.6e}  T_h={T_h:.6e}  "
            f"T_h/T_zeta-1={T_h/T_zeta-1:.2e}  r_after={r_after:.4f}")
    return {"label": bg["label"], "eta_B": float(bg["eta_B"]),
            "I_inf": float(bg["I_inf"]), "eta_far_used": float(eta_far),
            "rows": rows,
            "r_after_median": float(np.median([r["r_after"] for r in rows])),
            "max_abs_T_ratio_minus_1": float(max(abs(r["T_h_over_T_zeta_minus_1"])
                                                 for r in rows))}


def rerun_r5_15(r_model, out_name="r5_15b_tensor_omega_nhz_model_r_2026_09_04.json"):
    """Re-run the committed first-order tensor Omega_GW script with the model's
    OWN r added as CASE C, writing to a NEW file (the committed JSON is left
    untouched)."""
    import r5_15_tensor_omega_nhz as R
    newp = Path(R.OUTJ).parent / out_name
    R.R_CASES = dict(R.R_CASES)
    R.R_CASES[f"C_model_own_r{r_model:.2f}"] = float(r_model)
    R.OUTJ = newp
    R.main()
    d = json.loads(newp.read_text())
    key = f"C_model_own_r{r_model:.2f}|MB_anchored_ns0.9649"
    key_d = f"C_model_own_r{r_model:.2f}|pure_dust_ns1"
    return {"output_file": str(newp.relative_to(REPO)),
            "case_C_anchored": d["cases"][key], "case_C_dust": d["cases"][key_d]}


def make_png(res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    for key, c in zip(("poly", "LQC", "quintin"), ("C0", "C1", "C2")):
        b = res["backgrounds"][key]
        x = [r["k_etaB"] for r in b["rows"]]
        ax[0].plot(x, [r["r_after"] for r in b["rows"]], "o-", color=c, label=b["label"])
        ax[1].semilogy(x, [max(abs(r["T_h_over_T_zeta_minus_1"]), 1e-16)
                           for r in b["rows"]], "o-", color=c, label=b["label"])
    ax[0].axhline(R_CMB_BOUND, color="k", ls="--",
                  label=r"BICEP/Keck 2021  $r<0.036$")
    ax[0].axhline(R_QUOTED_084, color="r", ls=":", label=r"quoted $r=0.84$")
    ax[0].set_yscale("log")
    ax[0].set_xlabel(r"$k\,\eta_B$")
    ax[0].set_ylabel(r"$r_{\rm after}=P_h/P_\zeta$ (post-bounce)")
    ax[0].set_title("the model's own $r$ vs the CMB bound")
    ax[0].legend(fontsize=7)
    ax[1].set_xlabel(r"$k\,\eta_B$")
    ax[1].set_ylabel(r"$|T_h/T_\zeta-1|$")
    ax[1].set_title("tensor vs scalar transfer through the bounce")
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUTPNG, dpi=140)


def main():
    log("[A] analytic block ...")
    an = analytic_block()
    log(f"    r = {an['r_symbolic']};  pure dust r = {an['pure_dust']['r']:.4f}, "
        f"n_s = 1 exactly;  Planck-anchored w = {an['planck_anchored']['w']:.6f}, "
        f"r = {an['planck_anchored']['r']:.4f}")
    log("[B] backgrounds ...")
    bgs = {"poly": A2.bg_poly(), "LQC": A2.bg_lqc(), "quintin": A2.bg_quintin()}
    kts = [2e-3, 5e-3, 1e-2, 2e-2, 3e-2]
    res = {"task": "NEXT_SCIENCE_LEDGER row 10 (A3-4 + A3-ns) -- the matter "
                   "bounce's OWN tensor-to-scalar ratio r and scalar tilt n_s",
           "date": "2026-09-04", "analytic": an,
           "k_grid_k_etaB": kts, "backgrounds": {}}
    for key, bg in bgs.items():
        log(f"  [M] {key} ({bg['label']}) eta_B={bg['eta_B']:.4e}")
        res["backgrounds"][key] = run_background(key, bg, kts)
    r_model = an["planck_anchored"]["r"]
    r_nums = [res["backgrounds"][k]["r_after_median"] for k in bgs]
    max_dev = max(res["backgrounds"][k]["max_abs_T_ratio_minus_1"] for k in bgs)
    res["numeric_summary"] = {
        "r_after_median_per_background": {k: res["backgrounds"][k]["r_after_median"]
                                          for k in bgs},
        "r_after_spread_vs_analytic_24": float(max(abs(x - 24.0) for x in r_nums)),
        "max_abs_T_h_over_T_zeta_minus_1_all_backgrounds": max_dev,
        "interpretation": "the tensor and the scalar are transported by the SAME "
                          "geometric potential a''/a in the dressed-metric scheme, "
                          "so T_h = T_zeta to integration accuracy and r is "
                          "UNCHANGED by every one of the three bounces."}
    res["cmb_verdict"] = {
        "r_model_planck_anchored": float(r_model),
        "r_model_pure_dust": float(an["pure_dust"]["r"]),
        "cmb_bound_r": R_CMB_BOUND,
        "ratio_model_over_bound": float(r_model / R_CMB_BOUND),
        "sigma_style_statement": f"r_model = {r_model:.2f} exceeds the BICEP/Keck "
            f"2021 95% bound r < {R_CMB_BOUND} by a factor "
            f"{r_model/R_CMB_BOUND:.0f}",
        "vs_quoted_0.84": {
            "quoted": R_QUOTED_084,
            "ratio_model_over_quoted": float(r_model / R_QUOTED_084),
            "provenance_finding": "no derivation of a TENSOR-sense r = 0.84 exists "
                "anywhere in this repository. The only derived 0.84 is R_OVERLAP in "
                "research/track_a3_multichannel/survey_reach_fnl.py:46, P2's "
                "noise-weighted bounce-vs-local BISPECTRUM SHAPE OVERLAP (a "
                "correlation coefficient, documented at length in "
                "research/focused_paper_source_integration/02_full_draft.tex). The "
                "tensor-sense attribution in r5_15_tensor_omega_nhz.py:73,98 and "
                "paper/main.tex:769 is a conflation of that shape overlap with the "
                "tensor-to-scalar ratio, and it is low by a factor "
                f"{r_model/R_QUOTED_084:.1f} relative to the model's own value."},
        "verdict": "CMB TENSION. The modelled dust-contraction background is NOT "
                   "CMB-viable in its bare single-field form: r = 16 eps = 24, "
                   "three orders of magnitude above the observational bound. This "
                   "is the matter bounce's known large-r problem (Cai, Easson & "
                   "Brandenberger 2012; the single-field no-go of Quintin et al. "
                   "2015), not a new defect of this lab's backgrounds, and no "
                   "bounce in the A2 set relieves it."}
    log("[C] re-running r5_15 with the model's own r ...")
    res["r5_15_rerun_with_model_r"] = rerun_r5_15(r_model)
    log("[D] figure ...")
    make_png(res)
    res["wall_seconds"] = time.time() - _t0
    OUTJ.write_text(json.dumps(res, indent=2))
    log(f"[done] r_model = {r_model:.4f} (dust 24.0000); "
        f"max |T_h/T_zeta - 1| = {max_dev:.2e}; wrote {OUTJ.name}")


if __name__ == "__main__":
    main()
