#!/usr/bin/env python3
"""Ledger row 9 (A3-1e) lane (c): translate the Agullo-Bolliet-Sreenath 2017
(arXiv:1712.08148) LQC enhancement scale k_LQC into the lab's k*eta_B, and test
the overlap with the lab's PTA / PBH observational windows under the A3 paper's
section-V bounce-temperature condition.  Local CPU, deterministic, no network.

Literature inputs (quoted, never re-derived):
  ABS 2017 sec. V : k_LQC = a_B sqrt(kappa rho_B) = a_B sqrt(R_B/6);
                    a(t) = a_B (1 + 3 kappa rho_B t^2)^(1/6)   [kinetic-dominated];
                    pole  eta_p = i alpha / k_LQC, alpha = 0.64677;
                    |f_NL| ~ exp(-alpha (k1+k2+k3)/k_LQC) for k_t >~ k_LQC.
Lab inputs (quoted from committed artefacts):
  lane (a) VERTEX_TABLE_2026-09-03.md : LQC dust a^3 = 1 + (3/4) rho_c t^2, kappa=1;
  A3-3 SIGW_NHZ_NOTE_2026-09-04.md    : k_B = 1.71e15 Mpc^-1 at T_B = 1e8 GeV, k_B ~ T_B;
  A3-1b inlab_delta2_zeta_2026-09-03  : Delta^2_zeta ~ 5e-10 - 1.3e-9 over the PBH band.
"""
import json, numpy as np
from scipy.integrate import quad

ALPHA = 0.64677                      # ABS 2017 sec. V
out = {"literature": {"alpha_ABS": ALPHA,
                      "k_LQC_def": "a_B sqrt(kappa rho_B) = a_B sqrt(R_B/6)"}}

# --- (1) k_LQC * eta_B for the two backgrounds ------------------------------
# NEC (Hdot>0) window in LQC is rho > rho_c/2 for both matter contents.
# dust  : a^3 = 1 + u^2 with u = t sqrt(3 rho_c)/2 ; NEC edge a^3 = 2 -> u = 1
# stiff : a^6 = 1 + u^2 with u = t sqrt(3 kappa rho_B); NEC edge a^6 = 2 -> u = 1
I_dust = quad(lambda u: (1 + u**2) ** (-1 / 3), 0, 1)[0]
I_stif = quad(lambda u: (1 + u**2) ** (-1 / 6), 0, 1)[0]
# eta_B = int_0^t_NEC dt/a, with kappa = 1 and a_B = 1 so that k_LQC = sqrt(rho_B)
eta_B_dust = 2.0 / np.sqrt(3.0) * I_dust      # in units 1/sqrt(rho_c)
eta_B_stif = 1.0 / np.sqrt(3.0) * I_stif      # in units 1/sqrt(rho_B)
out["scale_window"] = {
    "eta_B_dust_times_sqrt_rho_c": eta_B_dust,
    "eta_B_stiff_times_sqrt_rho_B": eta_B_stif,
    "k_LQC_eta_B_dust": eta_B_dust,           # k_LQC = sqrt(rho_c) in these units
    "k_LQC_eta_B_stiff": eta_B_stif,
    "pole_over_eta_B_stiff": ALPHA / eta_B_stif,
    "enhancement_edge_k_eta_B_dust": eta_B_dust,        # k = k_LQC
    "fNL_affected_edge_k_eta_B_dust": 10 * eta_B_dust,  # ABS summary point 4: k <~ 10 k_LQC
    "equilateral_decay_exponent_per_k_eta_B": 3 * ALPHA / eta_B_dust,
}

# --- (2) overlap with the lab's observational windows ----------------------
K_B_1e8 = 1.71e15          # Mpc^-1, A3-3 note (k_B linear in T_B)
bands = {"PTA_2nHz": 2 * 6.5e6, "PTA_60nHz": 60 * 6.5e6,
         "PBH_lo": 1e5, "PBH_hi": 5.3e15}
rows = {}
for T_B in (1e8, 1e10):
    kB = K_B_1e8 * T_B / 1e8
    rows["T_B=%.0e GeV" % T_B] = {"k_B_Mpc^-1": kB,
        **{b: k / kB for b, k in bands.items()}}
out["observability"] = {"k_B_Mpc^-1_at_1e8GeV": K_B_1e8,
                        "k_eta_B_of_band": rows,
                        "T_B_for_k_LQC_at_60nHz_GeV": 1e8 * bands["PTA_60nHz"] / K_B_1e8}

# --- (3) does an f_NL ~ 1e3 tail rescue the PBH channel? -------------------
# zeta = zeta_g + (3/5) f_NL zeta_g^2 ; lab Delta^2_zeta = 1e-9 -> sigma_g = 3.16e-5
sigma_g = np.sqrt(1e-9)
for fNL, zc in ((1e3, 0.1), (1e3, 0.7)):
    zg = np.sqrt(zc / (0.6 * fNL))
    out.setdefault("pbh_tail", {})["fNL=%g_zeta_c=%g" % (fNL, zc)] = {
        "sigma_g": sigma_g, "zeta_g_needed": zg, "n_sigma": zg / sigma_g}

print(json.dumps(out, indent=2))
json.dump(out, open("research/cubic_bounce_transmission/lane9c_abs_operator/"
                    "lane9c_scale_window.json", "w"), indent=2)
