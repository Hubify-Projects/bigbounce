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
            "Delta2_ratio_vs_S1": float((abs(ap) / abs(s1_pred)) ** 2)}


def sweep(bg, ks, tag, rtol=1e-11):
    eta_far = min(0.9 * bg["eta_far"], 400.0 * bg["eta_B"])
    out = []
    for kt in ks:
        r = growth_at_k(bg, kt / bg["eta_B"], eta_far, rtol=rtol)
        r["background"] = tag
        out.append(r)
    return out
