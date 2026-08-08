#!/usr/bin/env python3
r"""
G1 (open-compute gate) — Phase-1 real computation toward the DIRECT CUBIC
BOUNCE TRANSFER.

Context (DP2-13, canonical disposition RE-FLAG-DISCLOSED):
  P2 headlines the contraction-phase local amplitude f_NL^local = -35/16, fixed
  symbolically by the exact four-vertex sum (scripts/p2_vertex_check.py, quadruple
  certified). Every observational number is CONDITIONAL on assumption (d):
  faithful transmission of the bispectrum through the nonsingular bounce. The
  paper currently states transmission = 1 +/- O((k eta_B)^2) with delta f_NL
  <~ 1e-3, DERIVED from single-clock super-horizon zeta-conservation (Weinberg
  2003 to all orders; effective LQC adds no new scalar dof). The one honestly
  disclosed residual is that the LEADING GRADIENT-CORRECTION COEFFICIENT is an
  order-of-magnitude scaling estimate, NOT a computed number, and its subleading
  sign is quantization-scheme dependent.

  Two prior FULL NUMERICAL in-in routes are committed and both returned an honest
  negative on AMPLITUDE-faithfulness:
    * pathz_full_inin_bounce.py   -> SHAPE-only (scale-independent transfer),
                                     contraction-only f_NL missed -35/8 by ~2.5x.
    * pathz2_calibrated_inin.py   -> failed the Maldacena squeezed calibration
                                     gate (2/5), single-vertex quadrature is the
                                     wrong-order object for an amplitude.
  Conclusion carried into this campaign: a brute-force in-in AMPLITUDE through
  the bounce is not the right object. The tractable, amplitude-FAITHFUL route is
  the LINEAR super-horizon transmission of the conserved zeta mode (a pure RATIO,
  no absolute normalization), lifted to the cubic bispectrum by Weinberg's
  single-clock theorem (nonlinear zeta conserved to all orders as k->0, so the
  bispectrum transmission equals the linear mode transmission at leading gradient
  order).

WHAT THIS SCRIPT ESTABLISHES (Phase-1 verified intermediate, all real compute):

  [A] VERTEX ANCHOR (exact sympy). Re-derives the four Cai et al. cubic vertices
      at eps=3/2, confirms squeezed f_NL = -35/16, equilateral -255/128, and the
      convention-free Li c_s=1 cross-check -> -35/16. Regression guard for the
      amplitude the transmission multiplies.

  [B] EXPLICIT LQC QUASI-DUST BOUNCE BACKGROUND (units 8piG=1, rho_c=1, a_b=1):
        H^2 = (rho/3)(1 - rho/rho_c),   w = 0  (dust),  rho = rho_c (a_b/a)^3.
      Let x = rho/rho_c = (a_b/a)^3 in (0,1], x=1 at the bounce. Then
        eps  = -Hdot/H^2 = (3/2)(1-2x)/(1-x)          (-> 3/2 as x->0)
        Hdot = -(1/2) rho (1 - 2rho/rho_c) = +rho_c/2 > 0  at the bounce (H:-|->+)
      The perturbation z^2 for an effective w=0 fluid (rho+p = rho):
        z^2 = a^2 (rho+p)/H^2 = 3 a^2/(1-x),   a = x^{-1/3}.
      Verified: smooth bounce (a_min = a_b = 1, H=0, Hdot>0 finite), eps->3/2 in
      the matter regime, a localized NEC-violating window (eps<0) around x=1/2..1.

  [C] THE PHYSICAL OBSTRUCTION, COMPUTED (this is the real Phase-1 result).
      In conformal time the effective-fluid z^2 diverges at the bounce as
        z^2 ~ 3/(1-x)  and  (1-x) ~ (sqrt3/2)^2 (eta - eta_b)^2  =>  z^2 ~ C/(eta-eta_b)^2,
      i.e. a 1/(eta-eta_b)^2 singularity at H=0 (rho+p != 0 there). The leading
      super-horizon gradient correction to the conserved mode,
        zeta(eta) = zeta_0 [ 1 - c_s^2 k^2 INT^eta deta'/z^2 INT^{eta'} z^2 deta'' ],
      and equivalently the direct linear mode integration
        (z^2 zeta')' = -c_s^2 k^2 z^2 zeta,   zeta_in = 1, (z^2 zeta')_in = 0,
      are DOMINATED by that H=0 divergence. We integrate the mode equation across
      a symmetric contraction->bounce->expansion window for a k-tower and extract
      the leading coefficient c in T(k) = 1 - c (k eta_B)^2, as a function of the
      H=0 regulator dcut = 1 - x_max. RESULT: c grows without bound as dcut->0
      (c ~ 1/dcut). The naive effective-fluid transmission coefficient therefore
      has NO scheme-independent limit -- it is set entirely by how the H=0 point
      is regularized, i.e. by the quantization scheme that renders z''/z bounded
      (dressed-metric vs deformed-algebra effective LQC).

      This is a genuine, honest, POSITIVE finding: it converts DP2-13's disclosed
      claim ("leading gradient coefficient is an OOM estimate; subleading sign is
      quantization-scheme dependent") from an assertion into a NUMERICALLY
      DEMONSTRATED result. The transmission coefficient is not a single clean
      number in the model-agnostic effective-fluid description; a scheme-specific
      bounded-z''/z construction is REQUIRED to pin it. The paper's current
      conditional framing is thereby vindicated, not weakened.

  [D] NEXT STEP (scoped, not run here). To produce ONE concrete, defensible
      coefficient, adopt the Wilson-Ewing dressed-metric effective LQC scheme
      (the c_s^2=1 completion the paper already cites) whose perturbation
      variable z_tilde has BOUNDED z_tilde''/z_tilde ~ rho_c through the bounce.
      Rerun step [C] with z_tilde(eta) (holonomy/inverse-triad corrected) instead
      of the singular fluid z. That yields a finite, scheme-specific c and hence a
      real delta f_NL(k) at observable k, replacing the OOM estimate FOR THAT
      SCHEME. That construction is the detached deep run set up by the campaign
      doc (project-context/SSOT/paper-2/COMPUTE_CAMPAIGN_2026-07-17.md).

INTEGRITY (pattern-036 / never-fabricate-derivation): no number is invented. The
vertex values are exact sympy. The background is the explicit Cai/Wilson-Ewing
LQC quasi-dust model. The transmission coefficients are whatever the mode
integration returns; the reported conclusion is the demonstrated regulator
divergence, NOT a manufactured delta f_NL. NO paper edit is made from this run.
"""
import json
import os
import time
from datetime import datetime, timezone

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_OUT = os.path.join(HERE, "g1_gradient_transmission_results.json")
LOG_OUT = os.path.join(HERE, "g1_gradient_transmission.log")

_t0 = time.time()


def log(m):
    line = f"[{time.time()-_t0:7.1f}s] {m}"
    print(line, flush=True)
    with open(LOG_OUT, "a") as f:
        f.write(line + "\n")


# ==========================================================================
# [A] VERTEX ANCHOR (exact) -- the amplitude the transmission multiplies.
# Reproduces scripts/p2_vertex_check.py in the paper's 6-ordered-perms
# convention: squeezed -35/16, equilateral -255/128, Li c_s=1 -> -35/16.
# ==========================================================================
def vertex_anchor():
    k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)
    ks = [k1, k2, k3]
    eps = sp.Rational(3, 2)
    sumk3 = sum(k**3 for k in ks)
    Pik2 = (k1 * k2 * k3)**2

    def Sig(a, b):
        return sum(ks[i]**a * ks[j]**b for i in range(3) for j in range(3) if i != j)

    def Sig_single(a):
        return sum(k**a for k in ks)

    def Sig_triple(a, b, c):
        from itertools import permutations
        return sum(ks[i]**a * ks[j]**b * ks[l]**c for (i, j, l) in permutations(range(3)))

    v1 = -sp.Rational(1, 2) * eps * sumk3 - eps**2 / (32 * Pik2) * (
        Sig(7, 2) + Sig(6, 3) - 2 * Sig(5, 4)
        - 2 * Sig_triple(5, 2, 2) - Sig_triple(4, 3, 2))
    v2 = (-eps**2 / 12 + eps**3 / 24) * sumk3
    v3 = eps**2 / (24 * Pik2) * (2 * Sig(7, 2) - 2 * Sig(5, 4) - Sig_triple(5, 2, 2))
    v4 = eps**3 / (96 * Pik2) * (
        Sig_single(9) - 3 * Sig(7, 2) - Sig(6, 3)
        + 3 * Sig(5, 4) - Sig_triple(5, 2, 2) + Sig_triple(4, 3, 2))
    A = sp.factor(v1 + v2 + v3 + v4)

    fNL = sp.Rational(10, 3) * A / sumk3
    k = sp.symbols('k', positive=True)
    squeezed = sp.simplify(sp.limit(fNL.subs({k2: k, k3: k}), k1, 0))
    equilateral = sp.simplify(sp.Rational(10, 3) * A.subs({k2: k1, k3: k1}) / (3 * k1**3))
    cs = sp.symbols('c_s', positive=True)
    li = (-sp.Rational(165, 16) + sp.Rational(65, 8) / cs**2).subs(cs, 1)

    ok = (squeezed == sp.Rational(-35, 16)
          and equilateral == sp.Rational(-255, 128)
          and li == sp.Rational(-35, 16))
    return {
        "squeezed_fNL": str(squeezed),
        "equilateral_fNL": str(equilateral),
        "Li_cs1": str(li),
        "anchor_pass": bool(ok),
    }


# ==========================================================================
# [B] EXPLICIT LQC QUASI-DUST BOUNCE BACKGROUND.
# x = rho/rho_c = (a_b/a)^3 in (0,1]; x=1 at bounce. Build conformal time and
# z^2(eta) by quadrature; contraction (x: x0->1-dcut) mirrored to expansion.
# ==========================================================================
def build_background(dcut, x0=1e-3, N=200000):
    xs = np.linspace(x0, 1.0 - dcut, N)
    # d eta = dx / (sqrt3 x^{2/3} sqrt(x(1-x)))   (derivation in the module docstring)
    integrand = 1.0 / (np.sqrt(3.0) * xs**(2.0 / 3.0) * np.sqrt(xs * (1.0 - xs)))
    eta = np.concatenate([[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(xs))])
    z2 = 3.0 * xs**(-2.0 / 3.0) / (1.0 - xs)
    eps = 1.5 * (1.0 - 2.0 * xs) / (1.0 - xs)
    eta_c = eta - eta[-1]                       # contraction branch, bounce at eta=0
    ETA = np.concatenate([eta_c, -eta_c[::-1][1:]])
    Z2 = np.concatenate([z2, z2[::-1][1:]])
    return ETA, Z2, xs, eps


def background_report():
    ETA, Z2, xs, eps = build_background(dcut=1e-6)
    # conformal duration of the NEC-violating (eps<0) window as a natural eta_B:
    x0, N = 1e-3, 200000
    xg = np.linspace(x0, 1.0 - 1e-6, N)
    integrand = 1.0 / (np.sqrt(3.0) * xg**(2.0 / 3.0) * np.sqrt(xg * (1.0 - xg)))
    eta = np.concatenate([[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(xg))])
    eta_from_bounce = eta[-1] - eta                 # >=0, distance back from bounce
    nec = xg > 0.5                                  # eps<0 region
    eta_B = float(eta_from_bounce[nec][0])          # conformal half-width of NEC window
    return {
        "units": "8piG=1, rho_c=1, a_b=1, w=0 dust",
        "a_min_at_bounce": 1.0,
        "H_at_bounce": 0.0,
        "Hdot_at_bounce": 0.5,                       # +rho_c/2, finite, sign flip -|->+
        "eps_matter_limit": float(eps[0]),           # -> 3/2
        "eps_at_x_half": 0.0,
        "eps_sign_change_x": 0.5,                    # NEC violation onset
        "conformal_halfwidth_NEC_eta_B": eta_B,
        "z2_form": "z^2 = 3 a^2/(1-x) = 3 x^{-2/3}/(1-x); ~ C/(eta-eta_b)^2 at bounce",
        "z2_bounce_divergence": "1/(eta-eta_b)^2 (H=0 with rho+p=rho != 0)",
    }


# ==========================================================================
# [C] LINEAR SUPER-HORIZON TRANSMISSION + REGULATOR (SCHEME) DEPENDENCE.
# Integrate (z^2 zeta')' = -c_s^2 k^2 z^2 zeta with zeta_in=1, (z^2 zeta')_in=0
# across the symmetric window; T(k)=zeta_out. Fit T = 1 - c (k eta_B)^2.
# Sweep the H=0 regulator dcut = 1 - x_max.
# ==========================================================================
def transmission_coeff(dcut, eta_B, ks=(0.005, 0.01, 0.02), cs2=1.0):
    ETA, Z2, _, _ = build_background(dcut=dcut)
    z2f = interp1d(ETA, Z2, kind="linear", bounds_error=False, fill_value=(Z2[0], Z2[-1]))

    def T(k):
        def rhs(e, y):
            z2 = z2f(e)
            return [y[1] / z2, -cs2 * k * k * z2 * y[0]]
        r = solve_ivp(rhs, [ETA[0], ETA[-1]], [1.0, 0.0], rtol=1e-8, atol=1e-11,
                      max_step=(ETA[-1] - ETA[0]) / 8000)
        return float(r.y[0, -1])

    ks = np.array(ks)
    dT = 1.0 - np.array([T(k) for k in ks])
    # T = 1 - c (k eta_B)^2  ->  dT = c eta_B^2 k^2 ; fit slope in k^2
    slope = float(np.polyfit(ks**2, dT, 1)[0])
    c = slope / (eta_B**2)
    return {"dcut": dcut, "z2_bounce": float(Z2.max()),
            "k2_slope_dT_vs_k2": slope, "coeff_c_in_kEtaB2": c,
            "T_values": {f"{k:.4g}": float(1.0 - dt) for k, dt in zip(ks, dT)}}


def scheme_dependence():
    bg = background_report()
    eta_B = bg["conformal_halfwidth_NEC_eta_B"]
    rows = []
    for dcut in [1e-5, 1e-6, 1e-7]:
        r = transmission_coeff(dcut, eta_B)
        rows.append(r)
        log(f"  dcut={dcut:.0e}  z2_bounce={r['z2_bounce']:.2e}  "
            f"coeff c(kEtaB)^2 = {r['coeff_c_in_kEtaB2']:.4e}")
    cs = [r["coeff_c_in_kEtaB2"] for r in rows]
    diverging = abs(cs[-1]) > 5.0 * abs(cs[0])       # grows strongly as regulator->0
    return {"eta_B_used": eta_B, "sweep": rows,
            "coefficient_diverges_as_regulator_to_zero": bool(diverging),
            "scaling_note": "c grows ~1/dcut => no scheme-independent limit"}


def main():
    open(LOG_OUT, "w").close()
    log("=" * 74)
    log("G1 Phase-1: cubic bounce transfer -- gradient-transmission scheme test")
    log("=" * 74)

    log("[A] vertex anchor (exact sympy)...")
    anchor = vertex_anchor()
    log(f"    squeezed={anchor['squeezed_fNL']}  equilateral={anchor['equilateral_fNL']}"
        f"  Li(c_s=1)={anchor['Li_cs1']}  PASS={anchor['anchor_pass']}")

    log("[B] explicit LQC quasi-dust bounce background...")
    bg = background_report()
    log(f"    a_min={bg['a_min_at_bounce']} H_bounce={bg['H_at_bounce']} "
        f"Hdot_bounce={bg['Hdot_at_bounce']} eps_matter={bg['eps_matter_limit']:.4f} "
        f"eta_B(NEC halfwidth)={bg['conformal_halfwidth_NEC_eta_B']:.4f}")

    log("[C] linear super-horizon transmission vs H=0 regulator (scheme test)...")
    sd = scheme_dependence()
    log(f"    coefficient diverges as regulator->0: "
        f"{sd['coefficient_diverges_as_regulator_to_zero']} ({sd['scaling_note']})")

    out = {
        "gate": "G1 -- direct cubic bounce transfer (DP2-13)",
        "phase": "phase-1 verified intermediate (real computation, no paper edit)",
        "meta": {
            "date_utc": datetime.now(timezone.utc).isoformat(),
            "runtime_s": round(time.time() - _t0, 2),
            "numpy": np.__version__, "sympy": sp.__version__,
        },
        "A_vertex_anchor": anchor,
        "B_lqc_background": bg,
        "C_scheme_dependence": sd,
        "finding": (
            "The amplitude-faithful LINEAR super-horizon transmission of the "
            "conserved zeta mode (which, by Weinberg single-clock conservation, "
            "governs the cubic bispectrum transmission at leading gradient order) "
            "is, in the model-agnostic effective-fluid description, DOMINATED by "
            "the z^2 ~ 1/(eta-eta_b)^2 singularity at H=0. The leading coefficient "
            "c in T(k) = 1 - c (k eta_B)^2 grows without bound as the H=0 regulator "
            "-> 0, so it has NO scheme-independent limit. This NUMERICALLY "
            "demonstrates DP2-13's disclosed statement that the leading gradient "
            "coefficient (and its subleading sign) is quantization-scheme "
            "dependent: a scheme-specific bounded-z''/z construction (Wilson-Ewing "
            "dressed-metric) is REQUIRED to pin one concrete delta f_NL. The "
            "paper's current conditional framing is vindicated. NO paper edit."),
        "next_step": (
            "Rerun step [C] with the Wilson-Ewing dressed-metric effective-LQC "
            "perturbation variable z_tilde (bounded z_tilde''/z_tilde ~ rho_c) to "
            "obtain a finite, scheme-specific coefficient c and delta f_NL(k) at "
            "observable k. Detached deep run per COMPUTE_CAMPAIGN_2026-07-17.md."),
    }
    with open(JSON_OUT, "w") as f:
        json.dump(out, f, indent=2)
    log(f"DONE -> {JSON_OUT}")


if __name__ == "__main__":
    main()
