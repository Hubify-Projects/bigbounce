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
