#!/usr/bin/env python3
r"""Figures for TRACK A2 (NEXT_SCIENCE_LEDGER item #2).

Reads a2_transmission_linear.json (run a2_transmission_linear.py first) and
re-uses its background builders, so every plotted number is the same number the
results JSON reports.  Deterministic; no random state; seconds of runtime.

Panels
  (a) the three explicit nonsingular bounce backgrounds a(eta)/a_b with their
      NEC-violation (Hdot > 0) windows shaded -- the definition of eta_B;
  (b) T_fNL = f_NL^after/f_NL^before vs the handoff epoch eta_h/eta_B, with the
      universal bound T_fNL <= 1/2 and the effective-fluid scheme point;
  (c) validity: the finite-k deviation of the directly-integrated T_fNL from the
      super-Hubble limit, ~ (k eta_B)^2.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import a2_transmission_linear as A2

HERE = os.path.dirname(os.path.abspath(__file__))
J = json.load(open(os.path.join(HERE, "a2_transmission_linear.json")))
OUT = os.path.join(HERE, "a2_transmission_summary.png")

bgs = {"LQC": A2.bg_lqc(), "poly": A2.bg_poly(eta_b=1.0), "quintin": A2.bg_quintin(dtB=1.0)}
NAMES = {"LQC": "LQC effective (dust)",
         "poly": r"analytic non-LQC  $a\propto 1+\eta^2/\eta_b^2$",
         "quintin": "Quintin+2015-type"}
COL = {"LQC": "#1b6ca8", "poly": "#c1440e", "quintin": "#2e7d32"}

fig, ax = plt.subplots(1, 3, figsize=(15.0, 4.4))

# ---- (a) backgrounds -------------------------------------------------
a0 = ax[0]
for key, b in bgs.items():
    eB = b["eta_B"]
    m = np.abs(b["eta"]) <= 6 * eB
    a0.plot(b["eta"][m] / eB, b["a"][m], color=COL[key], lw=1.9, label=NAMES[key])
    a0.axvspan(-1, 1, color="0.85", zorder=0)
a0.set_xlim(-6, 6)
a0.set_ylim(0.8, 30)
a0.set_yscale("log")
a0.set_xlabel(r"$\eta/\eta_B$")
a0.set_ylabel(r"$a(\eta)/a_{\rm b}$")
a0.set_title(r"(a) bounce backgrounds; shaded $=$ NEC window $\dot H>0$")
a0.legend(fontsize=8, loc="upper center")

# ---- (b) T_fNL vs handoff epoch --------------------------------------
a1 = ax[1]
for key, b in bgs.items():
    eB = b["eta_B"]
    eh = np.linspace(1.0, 12.0, 400) * eB
    T = np.array([A2.T_fNL_background(b, e)[1] for e in eh])
    a1.plot(eh / eB, T, color=COL[key], lw=1.9, label=NAMES[key])
    Tb = A2.T_fNL_background(b, eB)[1]
    a1.plot([1.0], [Tb], "o", color=COL[key], ms=6)
    a1.annotate(f"{Tb:.3f}", (1.0, Tb), textcoords="offset points",
                xytext=(7, 3), fontsize=8, color=COL[key])
ft = J["F_fluid_scheme_contrast"]["SECOND_SCHEME_transmission"]
a1.plot([1.0], [ft["T_fNL_fluid"]], "s", color="#6a1b9a", ms=7)
a1.annotate(f"effective-fluid scheme\n(LQC bg): {ft['T_fNL_fluid']:.3f}",
            (1.0, ft["T_fNL_fluid"]), textcoords="offset points", xytext=(10, 6),
            fontsize=8, color="#6a1b9a")
a1.axhline(0.5, color="k", ls="--", lw=1.0)
a1.annotate(r"universal bound $T_{f_{\rm NL}}\leq 1/2$", (6.2, 0.515), fontsize=8)
a1.set_xlabel(r"handoff epoch $\eta_h/\eta_B$")
a1.set_ylabel(r"$T_{f_{\rm NL}}=f_{\rm NL}^{\rm after}/f_{\rm NL}^{\rm before}$")
a1.set_ylim(0, 0.58)
a1.set_xlim(1, 12)
a1.set_title(r"(b) linear-transfer $T_{f_{\rm NL}}=(1-\rho)/2$")
a1.legend(fontsize=8, loc="center right")

# ---- (c) validity: finite-k deviation ---------------------------------
a2 = ax[2]
for key in bgs:
    rows = J["M_mode_evolution_verification"][key]["rows"]
    kk = np.array([r["k_etaB"] for r in rows])
    dv = np.array([r["direct_vs_background_relerr"] for r in rows])
    a2.loglog(kk, dv, "o-", color=COL[key], lw=1.6, ms=5, label=NAMES[key])
kref = np.array([2e-3, 3e-2])
a2.loglog(kref, 2.5 * kref**2, "k--", lw=1.0, label=r"$\propto (k\eta_B)^2$")
a2.set_xlabel(r"$k\,\eta_B$")
a2.set_ylabel(r"$|T^{\rm direct}_{f_{\rm NL}}/T^{\rm super-Hubble}_{f_{\rm NL}}-1|$")
a2.set_title(r"(c) validity of the super-Hubble limit")
a2.set_xticks([2e-3, 5e-3, 1e-2, 3e-2])
a2.set_xticklabels(["0.002", "0.005", "0.01", "0.03"])
a2.minorticks_off()
a2.legend(fontsize=8, loc="upper left")

fig.suptitle("Track A2: transmission of the matter-contraction $f_{\\rm NL}$ through an "
             "explicit nonsingular bounce (linear-transfer term)", fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig(OUT, dpi=150)
print("wrote", OUT)
