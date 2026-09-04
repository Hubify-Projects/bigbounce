#!/usr/bin/env python3
"""Lane 9c-2 - EXACT dressed-metric modes on the LQC-dust bounce, three initial
states, and the scheme-S1 bounce-window in-in integral over k*eta_B in [0.1, 10].

Executes the computation named in the lane-9c verdict
(../lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md sec. 5): lane (b)'s
in-in machinery run OUTSIDE its super-Hubble reduction, with the initial state
varied, to test whether the Agullo-Bolliet-Sreenath 2017 (arXiv:1712.08148)
enhancement of f_NL near k*eta_B ~ 1 appears in the lab's model.

Reuses, unmodified and by import:
  ../a2_transmission_linear.py        LQC-dust background, a''/a = x^(1/3)(1/6 + x/3),
                                      matter-basis projection, adiabatic dust vacuum
  ../lane_b_numerical/bounce_cubic_inin.py   the S1 vertex set V1-V7, redefinition
                                      terms R1-R4, the in-in convention, f_NL = (5/6)B/sum(PP)

Only the INITIAL STATE of the mode functions and the k-range are new.  No vertex
coefficient, kernel, or convention is altered.  Nothing is tuned to any target.

States (all normalised to the Wronskian Im(mu* mu') = -1/2):
  S-lab   the lab's adiabatic (exact dust) contraction vacuum imposed at eta -> -eta_far,
          mu = exp(-i k tau)(1 - i/(k tau))/sqrt(2k)      [A2 sec. 4; a2.evolve ic='vacuum']
  S-ABS0  adiabatic-order-zero (Minkowski positive-frequency) vacuum imposed at a FIXED
          pre-bounce time eta_0, mu = exp(-i k eta)/sqrt(2k), mu' = -i k mu
          [ABS sec. IV F: their state at eta_0 = -281.5 T_Pl "is only of adiabatic order zero"]
  S-ad4   4th-order adiabatic (WKB) vacuum imposed at the same eta_0 when k^2 > W(eta_0),
          otherwise at the latest pre-bounce time with k^2 >= 4 W(eta) (recorded per k)
"""
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp, cumulative_trapezoid

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lane_b_numerical"))
import a2_transmission_linear as a2          # noqa: E402
import bounce_cubic_inin as lb               # noqa: E402

LOG = os.path.join(HERE, "lane9c2_lqc_modes.log")
JSON_OUT = os.path.join(HERE, "results.json")
_lines = []


def log(m=""):
    print(m)
    _lines.append(m)


# ---------------------------------------------------------------- configuration
SQUEEZE = 0.02                    # k_long/k_short, squeezed isoceles (same as lane b)
K_SCAN = [0.1, 0.3, 1.0, 3.0, 10.0]          # k*eta_B, the row-9 band
K_GATE = 1e-3                                 # gate point (lane b's headline k)
ETA0_FAC = -3.0                               # headline fixed pre-bounce time, in eta_B
ETA0_SCAN = [-2.0, -3.0, -10.0, -30.0, -100.0]
ETA_STAR_FAC = 10.0                           # headline eta_*/eta_B for the k-scan
ETA_STAR_SCAN = [2.0, 5.0, 10.0, 30.0]
ABS_PLATEAU = 1.0e3                           # ABS sec. IV B / VII |f_NL| plateau
ABS_DECAY = 1.830229                          # exp(-alpha k_t/k_LQC) -> exp(-1.83 k eta_B), lane 9c sec. 2.2
K_LQC_ETAB = 1.060146                         # lane 9c sec. 2.2, LQC dust
