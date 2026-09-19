#!/usr/bin/env python3
"""
poplawski_reproduction_2026_09_18.py  (W5, 2025 legacy-archaeology campaign)

Independent numerical reproduction of N. Poplawski, "Universe in a black hole
in Einstein-Cartan gravity", ApJ 832:96 (2016), arXiv:1410.3881 (v2 text
fetched 2026-09-18), using only the equations printed in that paper:

  Friedmann constraint with the spin-fluid term        (his eq. 10 / 17)
      (da/dt)^2 / c^2 + k = (kappa/3) (eps - alpha n_f^2) a^2,
      alpha = kappa (hbar c)^2 / 32,  kappa = 8 pi G / c^4,
      eps = h_* T^4,  n_f = h_nf T^3.
  Particle-production ("creation") equation            (his eq. 41 / 42)
      (1/a^3) d(a^3 n_1)/dt = c K,   n_1 = h_n1 T^3
      =>  (da/dt)/a + (dT/dt)/T = c K / (3 h_n1 T^3).
  Production ansatz                                     (his eq. 45)
      K = beta (kappa eps_tilde)^2,  eps_tilde = eps - alpha n_f^2.

Everything is reduced to a two-variable dimensionless system in
(theta = T/T_max, N = ln a) with time in units of tau (his eq. 25) and length
in units of c tau.  Derivation and dimensional checks are in the memo
(research/archaeology_2025/memos/PARENT_CHILD_BOOKKEEPING_MEMO.md, sec. 4).

Parent-mass entry (ASSUMPTION, stated in memo sec. 4.4): the closed universe
begins to contract from rest (da/dt = 0) at a_i = r_s = 2GM/c^2, i.e. the
paper's own prescription below its eq. (16) ("a typical stellar black hole has
the Schwarzschild radius a_i = 10^4 m").  The memo shows this is equivalent to
requiring the Misner-Sharp mass of the equatorial 2-sphere of the child to
equal the parent mass M.

Outputs research/archaeology_2025/outputs/poplawski_reproduction_2026_09_18.json.
No fitting, no randomness.  Every number is either a CODATA constant, a
constant quoted from the paper (flagged), or an ODE integral of the equations
above.
"""

import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

OUT_DIR = Path(__file__).resolve().parent
OUT_JSON = OUT_DIR / "poplawski_reproduction_2026_09_18.json"

# ----------------------------------------------------------------------------
# Physical constants (CODATA 2018)
# ----------------------------------------------------------------------------
G = 6.67430e-11          # m^3 kg^-1 s^-2
c = 299792458.0          # m s^-1
hbar = 1.054571817e-34   # J s
kB = 1.380649e-23        # J K^-1
M_SUN = 1.98892e30       # kg
ZETA3 = 1.2020569031595942
kappa = 8 * math.pi * G / c**4            # m J^-1
hbarc = hbar * c                          # J m
T_P = math.sqrt(hbar * c**5 / G) / kB     # Planck temperature, K
t_P = math.sqrt(hbar * G / c**5)          # Planck time, s
l_P = math.sqrt(hbar * G / c**3)          # Planck length, m
eps_P = c**7 / (hbar * G**2)              # Planck energy density, J m^-3
rho_P = eps_P / c**2                      # Planck mass density, kg m^-3

# ----------------------------------------------------------------------------
# Paper inputs (quoted verbatim from 1410.3881; flagged as PAPER_*)
# ----------------------------------------------------------------------------
PAPER_gb = 28          # relativistic boson spin states, standard model (his ref [18])
PAPER_gf = 90          # relativistic fermion spin states
PAPER_gb1 = 9          # massive spin-1 bosons (W+, W-, Z): 3 x 3 spin states
PAPER_Teq = 8820.0     # K, matter-radiation equality temperature (his eq. 37 text)
PAPER_Lambda_over_kappa = 5.24e-10   # Pa (his eq. 37 text)
PAPER_stellar_ai = 1.0e4             # m (his eq. 29 text)

# Paper's stated numbers (his eqs. 28, 29, 50, 37) used ONLY for comparison
PAPER_Tmax = 1.15e32        # K
PAPER_tau = 4.75e-45        # s
PAPER_Hmax = 8.1e43         # s^-1
PAPER_Ti_stellar = 1.38e12  # K
PAPER_amin_stellar = 1.19e-16  # m
PAPER_beta_cr_inv = 929.0    # beta_cr ~ 1/929
PAPER_required_ratio = 1e10  # a_tilde_i / a_i > 1e10 (eq. 37)
# Desai & Poplawski 2016 (PLB 755, 183; arXiv:1510.08834) calibration run:
DP_beta = 1.0 / 929.25
DP_beta_cr_inv = 929.0915
DP_a0 = 1.0e-27            # m at the bounce
DP_T0_over_Tmax = 0.99
DP_efolds = 60.0           # "about 60 e-folds"
DP_t_end_accel = 1.33e-42  # s, acceleration -> deceleration
DP_table_I = {0.996: 1, 0.984: 2, 0.965: 3, 0.914: 5, 0.757: 10}  # beta/beta_cr -> bounces

# ----------------------------------------------------------------------------
# Thermodynamic coefficients (his section 4)
# ----------------------------------------------------------------------------
g_star = PAPER_gb + 7.0 / 8.0 * PAPER_gf              # 106.75
g_n = PAPER_gb + 3.0 / 4.0 * PAPER_gf                 # 95.5   (all particles)
g_nf = 3.0 / 4.0 * PAPER_gf                           # 67.5   (fermions)
h_star = (math.pi**2 / 30.0) * g_star * kB**4 / hbarc**3        # J m^-3 K^-4
h_n = (ZETA3 / math.pi**2) * g_n * kB**3 / hbarc**3             # m^-3 K^-3
h_nf = (ZETA3 / math.pi**2) * g_nf * kB**3 / hbarc**3           # m^-3 K^-3
h_n1 = (ZETA3 / math.pi**2) * PAPER_gb1 * kB**3 / hbarc**3      # m^-3 K^-3
alpha = kappa * hbarc**2 / 32.0                                  # J m^3

# Bounce temperature: eps = alpha n_f^2  ->  h_* T^4 = alpha h_nf^2 T^6
T_max = math.sqrt(h_star / (alpha * h_nf**2))
# Same thing in his closed form (eq. 20) as a cross-check
T_max_eq20 = math.sqrt(2 * math.pi**5 / 15.0) * math.sqrt(g_star) / (ZETA3 * g_nf) * T_P
# Characteristic torsion time (eq. 25): tau = (alpha h_nf^2 / c) (3/(kappa h_*^3))^(1/2)
tau = (alpha * h_nf**2 / c) * math.sqrt(3.0 / (kappa * h_star**3))
tau_eq25 = (45.0 / 4.0) * math.sqrt(5.0 / math.pi**13) * ZETA3**2 * g_nf**2 / g_star**1.5 * t_P
H_max = math.sqrt(4.0 / 27.0) / tau
ell = c * tau                                                    # length unit, m
# Bounce (thermal) density
eps_max = h_star * T_max**4
rho_max = eps_max / c**2
# beta_cr (eq. 49): sqrt(6)/32 * h_n1 h_nf^3 (hbar c)^3 / h_*^3
beta_cr = math.sqrt(6.0) / 32.0 * h_n1 * h_nf**3 * hbarc**3 / h_star**3
# Independent re-derivation of beta_cr from the stall condition x_max = 1, where
#   x(theta) = gamma theta^3 (1-theta^2)^(3/2), gamma = 3 beta/(c^3 tau^3 h_n1 T_max^3),
#   max_theta theta^3 (1-theta^2)^(3/2) = 1/8  ->  gamma_cr = 8.
beta_cr_rederived = 8.0 * c**3 * tau**3 * h_n1 * T_max**3 / 3.0
# Escape threshold (eq. 33 + 34, derived in memo sec. 4.6):
#   D > 2/(3 sqrt(Lambda)),  D = (1/3) kappa h_* T_eq (a T)^3
Lambda = PAPER_Lambda_over_kappa * kappa                            # m^-2
aT_escape = (2.0 / (kappa * h_star * PAPER_Teq * math.sqrt(Lambda)))**(1.0 / 3.0)   # m K
M_univ_escape = math.pi * c**2 / (2.0 * G * math.sqrt(Lambda))      # kg, memo sec. 4.6


def sanity():
    assert abs(T_max / T_max_eq20 - 1) < 1e-12
    assert abs(tau / tau_eq25 - 1) < 1e-12
    assert abs(beta_cr / beta_cr_rederived - 1) < 1e-10


sanity()

# ----------------------------------------------------------------------------
# Dimensionless dynamics.  theta = T/T_max, N = ln(a/ell), time in tau, b = beta/beta_cr.
#   F(theta)  = theta^4 (1 - theta^2)                 (kappa eps_tilde a^2 /3 -> F a^2)
#   h         = (da/dt)/a * tau = +- sqrt(F - e^{-2N})  (k = +1 closed)
#   G(theta)  = 8 b theta^5 (1-theta^2)^2            (production rate Gamma * tau)
#   dln(theta)/dN = -1 + G/h
# Invariants tracked: aT (particle number N_part ∝ (aT)^3, entropy S ∝ (aT)^3).
# ----------------------------------------------------------------------------
THETA_START = 1.0e-3   # production x = 8 b theta^3 (1-theta^2)^1.5 ~ 8e-9 here: negligible
DELTA = 1.0e-7         # stop/start at theta = 1 - DELTA (bounce); production ~ DELTA^1.5 there


def F(theta):
    return theta**4 * (1.0 - theta**2)


def Gprod(theta, b):
    return 8.0 * b * theta**5 * (1.0 - theta**2)**2


def hub(theta, N):
    val = F(theta) - math.exp(-2.0 * N)
    return math.sqrt(val) if val > 0 else 0.0


def rhs_expand(N, y, b):
    u, t = y
    theta = math.exp(u)
    h = hub(theta, N)
    if h == 0.0:
        return [-1.0, 0.0]
    return [-1.0 + Gprod(theta, b) / h, 1.0 / h]


def rhs_contract(s, y, b, N0):
    # s = N0 - N increases as a shrinks
    u, t = y
    theta = math.exp(u)
    h = hub(theta, N0 - s)
    if h == 0.0:
        return [1.0, 0.0]
    return [1.0 + Gprod(theta, b) / h, 1.0 / h]


def run_cycle(aT_in_ell, b):
    """One contraction -> bounce -> expansion cycle.

    aT_in_ell : a*theta at entry (theta << 1), in units of ell = c tau.
    Returns dict with per-cycle invariants and the expansion history.
    """
    # --- contraction from theta = THETA_START ---
    N0 = math.log(aT_in_ell / THETA_START)
    ev_bounce = lambda s, y, b, N0: y[0] - math.log(1.0 - DELTA)
    ev_bounce.terminal = True
    ev_bounce.direction = 1
    solc = solve_ivp(rhs_contract, [0.0, 400.0], [math.log(THETA_START), 0.0],
                     args=(b, N0), events=ev_bounce, rtol=1e-11, atol=1e-14,
                     method="DOP853", dense_output=True)
    if solc.t_events[0].size == 0:
        raise RuntimeError("contraction did not reach the bounce")
    s_b = solc.t_events[0][0]
    N_b = N0 - s_b
    theta_b = 1.0 - DELTA
    aT_bounce = math.exp(N_b) * theta_b
    t_contract = solc.y_events[0][0][1]
    Ne_contract = math.log(aT_bounce / aT_in_ell)

    # --- expansion from the bounce ---
    ev_end = lambda N, y, b: y[0] - math.log(THETA_START)
    ev_end.terminal = True
    ev_end.direction = -1
    sole = solve_ivp(rhs_expand, [N_b, N_b + 400.0], [math.log(theta_b), 0.0],
                     args=(b,), events=ev_end, rtol=1e-11, atol=1e-14,
                     method="DOP853", dense_output=True, max_step=0.05)
    if sole.t_events[0].size == 0:
        raise RuntimeError("expansion did not reach THETA_START")
    N_end = sole.t_events[0][0]
    aT_out = math.exp(N_end) * THETA_START
    Ne_expand = math.log(aT_out / aT_bounce)

    # --- acceleration bookkeeping on a fine grid (k negligible in this era) ---
    Ngrid = np.linspace(N_b, N_end, 20001)
    U = sole.sol(Ngrid)
    th = np.exp(U[0])
    tt = U[1]
    hh = np.array([hub(x, n) for x, n in zip(th, Ngrid)])
    dudN = np.array([rhs_expand(n, [u, 0.0], b)[0] for n, u in zip(Ngrid, U[0])])
    # dln h/dN = (1/2) dlnF/du * du/dN  (+ k-correction, negligible here)
    dlnF_du = 4.0 - 2.0 * th**2 / (1.0 - th**2)
    dlnh_dN = 0.5 * dlnF_du * dudN
    accel = 1.0 + dlnh_dN          # (a''/a) / H^2
    x = np.array([Gprod(v, b) for v in th]) / np.where(hh > 0, hh, np.inf)
    # end of acceleration = last N where accel crosses from + to -
    sign = np.sign(accel)
    crossings = np.where((sign[:-1] > 0) & (sign[1:] <= 0))[0]
    if crossings.size:
        i_end = crossings[-1]
        N_end_accel = Ngrid[i_end]
        t_end_accel = tt[i_end] * tau
        efolds_bounce_to_end_accel = N_end_accel - N_b
    else:
        N_end_accel = float("nan")
        t_end_accel = float("nan")
        efolds_bounce_to_end_accel = float("nan")
    # plateau: where |dln theta/dN| < 0.05 (T nearly constant while a grows)
    plateau = np.abs(dudN) < 0.05
    efolds_plateau = float(np.trapezoid(plateau.astype(float), Ngrid))
    # H during the plateau (if any)
    H_plateau = float(np.mean(hh[plateau]) / tau) if plateau.any() else float("nan")
    return dict(
        aT_in_ell=aT_in_ell, aT_bounce_ell=aT_bounce, aT_out_ell=aT_out,
        a_bounce_m=math.exp(N_b) * ell,
        Ne_contract=Ne_contract, Ne_expand=Ne_expand,
        Ne_total=Ne_contract + Ne_expand,
        amplification_particle_number=math.exp(3.0 * (Ne_contract + Ne_expand)),
        x_max=float(np.max(x)),
        efolds_bounce_to_end_accel=efolds_bounce_to_end_accel,
        t_end_accel_s=t_end_accel,
        efolds_T_plateau=efolds_plateau,
        H_plateau_s=H_plateau,
        t_contract_s=t_contract * tau,
        t_expand_to_theta_start_s=float(tt[-1]) * tau,
        # naive thermal energy E_th = h_* T^4 * 2 pi^2 a^3 ∝ (a theta)^3 theta
        E_thermal_end_over_bounce=(aT_out / aT_bounce)**3 * THETA_START / theta_b,
        E_thermal_at_theta_0p1_over_bounce=(aT_out / aT_bounce)**3 * 0.1 / theta_b,
    )


def Ne_of_b(b, aT_in_ell):
    return run_cycle(aT_in_ell, b)["Ne_total"]


def bounces_to_escape(aT0_ell, b, max_cycles=300):
    aT = aT0_ell
    target = aT_escape / T_max / ell
    n = 0
    while aT < target and n < max_cycles:
        aT = run_cycle(aT, b)["aT_out_ell"]
        n += 1
    return n if aT >= target else None


# ----------------------------------------------------------------------------
# Part 1: closed-form section-5 numbers (no production)
# ----------------------------------------------------------------------------
def section5_numbers(a_i):
    T_i = (3.0 / (kappa * h_star * a_i**2))**0.25       # eq. 16
    a_min = a_i * T_i / T_max                           # eq. 21
    E_i = h_star * T_i**4 * 2 * math.pi**2 * a_i**3    # naive thermal energy at formation
    N_i = h_n * T_i**3 * 2 * math.pi**2 * a_i**3       # total particle number at formation
    S_i = (2 * math.pi**2 / 45.0) * g_star * (kB * a_i * T_i / hbarc)**3 * 2 * math.pi**2  # in k_B
    return dict(a_i_m=a_i, T_i_K=T_i, a_min_m=a_min, aT_mK=a_i * T_i,
                E_thermal_formation_J=E_i, N_particles_formation=N_i,
                S_child_formation_kB=S_i,
                E_thermal_bounce_over_formation=T_max / T_i)


results = dict(
    provenance=dict(
        script=str(Path(__file__).name),
        paper="Poplawski, ApJ 832:96 (2016), arXiv:1410.3881v2 (fetched 2026-09-18)",
        companions=["arXiv:1007.0587 (PLB 694,181)", "arXiv:1105.6127 (GRG 44,1007)",
                    "arXiv:1510.08834 (Desai & Poplawski, PLB 755,183)",
                    "arXiv:1305.6977 (CQG 31,065005)"],
        assumptions=[
            "Standard-model content at the bounce: g_b=28, g_f=90, g_b1=9 (paper's choice).",
            "Parent mass enters ONLY through a_i = 2GM/c^2 with da/dt=0 at a_i (paper, below eq. 16).",
            "Production acts through eq. 42 with K = beta (kappa eps_tilde)^2 (eq. 45) in both contraction and expansion.",
            "All produced particles thermalize instantly at the common T (implicit in n_1 = h_n1 T^3).",
            "Friedmann constraint (eq. 17) retained with thermal eps(T); eq. 11 abandoned (paper's own choice).",
            "Contraction started at theta = T/T_max = 1e-3 where production is O(1e-8); k=+1 kept in h.",
        ],
    ),
    constants=dict(
        G=G, c=c, hbar=hbar, kB=kB, M_sun_kg=M_SUN, T_Planck_K=T_P, t_Planck_s=t_P,
        rho_Planck_kg_m3=rho_P,
    ),
    derived=dict(
        g_star=g_star, g_n=g_n, g_nf=g_nf,
        h_star_J_m3_K4=h_star, h_nf_m3_K3=h_nf, h_n1_m3_K3=h_n1, alpha_J_m3=alpha,
        T_max_K=T_max, T_max_over_T_Planck=T_max / T_P,
        tau_s=tau, tau_over_t_Planck=tau / t_P, ell_m=ell,
        H_max_s=H_max,
        eps_max_J_m3=eps_max, rho_max_kg_m3=rho_max, rho_max_over_rho_Planck=rho_max / rho_P,
        beta_cr=beta_cr, one_over_beta_cr=1.0 / beta_cr,
        beta_cr_rederived_from_stall=beta_cr_rederived,
        Lambda_m2=Lambda, aT_escape_mK=aT_escape,
        M_univ_escape_kg=M_univ_escape, M_univ_escape_Msun=M_univ_escape / M_SUN,
    ),
    paper_comparison={},
    stellar_check={},
    desai_poplawski_calibration={},
    efolds_vs_b={},
    table_I_reproduction={},
    parent_masses={},
)

# ---- paper numbers (eq. 28, 29, 50) ----
s5 = section5_numbers(PAPER_stellar_ai)
results["paper_comparison"] = dict(
    T_max=dict(paper=PAPER_Tmax, ours=T_max, ratio=T_max / PAPER_Tmax),
    tau=dict(paper=PAPER_tau, ours=tau, ratio=tau / PAPER_tau),
    H_max=dict(paper=PAPER_Hmax, ours=H_max, ratio=H_max / PAPER_Hmax),
    T_i_stellar=dict(paper=PAPER_Ti_stellar, ours=s5["T_i_K"], ratio=s5["T_i_K"] / PAPER_Ti_stellar),
    a_min_stellar=dict(paper=PAPER_amin_stellar, ours=s5["a_min_m"], ratio=s5["a_min_m"] / PAPER_amin_stellar),
    one_over_beta_cr=dict(paper=PAPER_beta_cr_inv, ours=1.0 / beta_cr, ratio=(1.0 / beta_cr) / PAPER_beta_cr_inv),
    one_over_beta_cr_DP=dict(paper=DP_beta_cr_inv, ours=1.0 / beta_cr, ratio=(1.0 / beta_cr) / DP_beta_cr_inv),
    required_ratio_eq37=dict(paper=PAPER_required_ratio,
                             ours=aT_escape / s5["aT_mK"],
                             required_efolds_one_bounce=math.log(aT_escape / s5["aT_mK"])),
    rho_bounce_over_Planck_GRG2012_eq14=dict(paper=15.4, ours=rho_max / rho_P),
)
results["stellar_check"] = s5

# ---- Desai & Poplawski calibration: b = beta_cr/929.25 (via their beta_cr), a0=1e-27 m ----
b_DP = DP_beta / beta_cr
b_DP_their = DP_beta_cr_inv / 929.25
# expansion-only run from their initial condition (T0 = 0.99 Tmax, a0 = 1e-27 m)
N_b = math.log(DP_a0 / ell)
ev_end = lambda N, y, b: y[0] - math.log(THETA_START)
ev_end.terminal = True
ev_end.direction = -1
sol_DP = solve_ivp(rhs_expand, [N_b, N_b + 400.0], [math.log(DP_T0_over_Tmax), 0.0],
                   args=(b_DP,), events=ev_end, rtol=1e-11, atol=1e-14, method="DOP853",
                   dense_output=True, max_step=0.05)
Ng = np.linspace(N_b, sol_DP.t_events[0][0], 20001)
U = sol_DP.sol(Ng)
th = np.exp(U[0])
dudN = np.array([rhs_expand(n, [u, 0.0], b_DP)[0] for n, u in zip(Ng, U[0])])
accel = 1.0 + 0.5 * (4.0 - 2.0 * th**2 / (1.0 - th**2)) * dudN
sign = np.sign(accel)
cr = np.where((sign[:-1] > 0) & (sign[1:] <= 0))[0]
i_end = cr[-1]
results["desai_poplawski_calibration"] = dict(
    beta=DP_beta, beta_over_beta_cr_ours=b_DP, beta_over_beta_cr_theirs=b_DP_their,
    a0_m=DP_a0, T0_over_Tmax=DP_T0_over_Tmax,
    efolds_bounce_to_end_of_acceleration=float(Ng[i_end] - N_b),
    t_end_of_acceleration_s=float(U[1][i_end] * tau),
    Ne_production_expansion_only=float(math.log(math.exp(Ng[-1]) * THETA_START / (DP_a0 / ell * DP_T0_over_Tmax))),
    paper_efolds=DP_efolds, paper_t_end_accel_s=DP_t_end_accel,
)

# ---- N_e(b) scan (single cycle, stellar a_i) ----
aT0 = s5["aT_mK"] / T_max / ell
scan = {}
for b in [0.0, 0.5, 0.757, 0.9, 0.914, 0.965, 0.984, 0.99, 0.996, 0.999, 0.9998, 0.99995, 1.0, 1.05]:
    try:
        r = run_cycle(aT0, b)
        scan[str(b)] = {k: (float(v) if isinstance(v, (int, float, np.floating)) else v) for k, v in r.items()}
    except RuntimeError as e:
        scan[str(b)] = dict(error=str(e))
results["efolds_vs_b"] = scan
# fit exponent of N_e vs (1-b) on the near-critical points
bs = [0.9, 0.965, 0.99, 0.996, 0.999, 0.9998, 0.99995]
lnx = np.log([1 - b for b in bs])
lny = np.log([scan[str(b)]["Ne_total"] for b in bs])
slope, intercept = np.polyfit(lnx, lny, 1)
results["efolds_vs_b_powerlaw"] = dict(exponent_of_one_minus_b=float(slope),
                                       prefactor=float(math.exp(intercept)),
                                       note="N_e ≈ prefactor * (1-b)^exponent; paper text says t_infl ∝ (beta_cr-beta)^-1")

# ---- Table I reproduction (bounces before escape) for stellar a_i ----
tab = {}
for bb, n_paper in DP_table_I.items():
    n_ours = bounces_to_escape(aT0, bb)
    tab[str(bb)] = dict(paper=n_paper, ours_stellar_ai_1e4m=n_ours)
results["table_I_reproduction"] = tab

# ---- Parent-mass sweep ----
for Msun in [10.0, 1.0e3, 1.0e6, 1.0e10]:
    M = Msun * M_SUN
    a_i = 2 * G * M / c**2
    s = section5_numbers(a_i)
    aT0m = s["aT_mK"] / T_max / ell
    # Misner-Sharp mass at the equator of the child at formation (memo sec. 3.1)
    m_MS_equator = c**2 * a_i / (2 * G)
    S_BH = 4 * math.pi * G * M**2 / (hbar * c)   # in k_B
    req_Ne = math.log(aT_escape / s["aT_mK"])   # e-folds needed for one-bounce escape
    # b that delivers req_Ne in one cycle
    f = lambda b: Ne_of_b(b, aT0m) - req_Ne
    try:
        b_req = brentq(f, 0.05, 1 - 1e-7, xtol=1e-9)
    except ValueError:
        b_req = float("nan")
    per_b = {}
    for b in [0.9, 0.99, 0.996, b_req]:
        if math.isnan(b):
            continue
        r = run_cycle(aT0m, b)
        A = r["amplification_particle_number"]
        per_b[f"{b:.6f}"] = dict(
            Ne_total=r["Ne_total"], Ne_contract=r["Ne_contract"], Ne_expand=r["Ne_expand"],
            amplification_particle_number=A,
            efolds_bounce_to_end_accel=r["efolds_bounce_to_end_accel"],
            t_end_accel_s=r["t_end_accel_s"], H_plateau_s=r["H_plateau_s"],
            E_thermal_at_theta_0p1_over_bounce=r["E_thermal_at_theta_0p1_over_bounce"],
            E_thermal_at_theta_0p1_over_formation=r["E_thermal_at_theta_0p1_over_bounce"] * s["E_thermal_bounce_over_formation"],
            N_particles_after=s["N_particles_formation"] * A,
            S_child_after_kB=s["S_child_formation_kB"] * A,
            S_child_after_over_S_BH=s["S_child_formation_kB"] * A / S_BH,
            bounces_to_escape=bounces_to_escape(aT0m, b),
            reproduces_paper_exponential_phase=bool(r["efolds_T_plateau"] > 1.0),
        )
    results["parent_masses"][f"{Msun:.0e}"] = dict(
        M_kg=M, a_i_m=a_i, T_i_K=s["T_i_K"],
        bounce_density_kg_m3=rho_max, bounce_density_over_Planck=rho_max / rho_P,
        bounce_scale_factor_m=s["a_min_m"], bounce_scale_factor_over_ell=s["a_min_m"] / ell,
        misner_sharp_mass_equator_over_M=m_MS_equator / M,
        misner_sharp_mass_full_3sphere=0.0,
        E_thermal_formation_over_Mc2=s["E_thermal_formation_J"] / (M * c**2),
        E_thermal_bounce_over_formation=s["E_thermal_bounce_over_formation"],
        E_effective_at_bounce=0.0,
        N_particles_formation=s["N_particles_formation"],
        S_BH_parent_kB=S_BH, S_child_formation_kB=s["S_child_formation_kB"],
        S_child_formation_over_S_BH=s["S_child_formation_kB"] / S_BH,
        required_Ne_for_one_bounce_escape=req_Ne,
        required_particle_amplification=math.exp(3 * req_Ne),
        b_required_for_one_bounce_escape=b_req,
        runs=per_b,
    )


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    return o


OUT_JSON.write_text(json.dumps(_clean(results), indent=2))
print(f"wrote {OUT_JSON}")
print(json.dumps(_clean(results["paper_comparison"]), indent=1))
print(json.dumps(_clean(results["desai_poplawski_calibration"]), indent=1))
print(json.dumps(_clean(results["efolds_vs_b_powerlaw"]), indent=1))
print(json.dumps(_clean(results["table_I_reproduction"]), indent=1))
