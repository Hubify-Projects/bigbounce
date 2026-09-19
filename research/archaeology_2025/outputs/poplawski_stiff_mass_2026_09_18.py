#!/usr/bin/env python3
"""
poplawski_stiff_mass_2026_09_18.py  (W5, 2025 legacy-archaeology campaign)

Closed-form check of N. Poplawski, arXiv:1103.4192 (2011, arXiv only),
"On the mass of the Universe born in a black hole": stiff-EOS (p = eps)
spin-fluid collapse inside a black hole of mass M gives a "universe of mass"
    m_max = (128/27)^(1/2) M_*,   M_* = M^2 m_n / m_Pl^2        (his eqs. 9-10)
with a_min = (27/128)^(1/6) 2 G M~ / c^2,  M~ = (m_Pl^2 M^2 / m_n)^(1/3)  (his eqs. 7-8).

What the formula actually is (memo sec. 5.3): the naive energy integral
E = eps * V of stiff matter blue-shifts as a^-3 between a_0 = r_s and the
torsion bounce a_min; the "mass" is E/c^2 with the ASSUMPTION that the
fermion number density tracks eps/(m_n c^2) (n ∝ a^-6, i.e. maximal
conversion of blue-shifted energy into neutrons; his footnote 1).

Independent re-derivation of the prefactor from his eqs. (1),(3),(5),(6):
  bounce: (1/3) kappa eps = (1/3) kappa * kappa s^2 / 4 -> eps = kappa (hbar c n)^2 / 32
  eps = eps_0 (a_0/a)^6, n = n_0 (a_0/a)^6
  => (a_min/a_0)^6 = kappa (hbar c n_0)^2 / (32 eps_0)
  eps_0 = M c^2 / (4 pi r_s^3 / 3),  n_0 = f_q * M / (m_n * 4 pi r_s^3 / 3)
  => (a_min/a_0)^6 = (3 f_q^2 / 128) (hbar c / (G m_n M))^2   [our algebra]
  => m_max / M = (a_0/a_min)^3 = (128 / (3 f_q^2))^(1/2) m_n M / m_Pl^2.
His eq. (6) writes n_0 = 3M/m_n / (4 pi r_g^3/3), i.e. f_q = 3 fermions per
neutron mass (three valence quarks) -- NOT stated in the text.  With f_q = 3
his (27/128) reproduces exactly; with one fermion per neutron (f_q = 1) the
prefactor would be (128/3)^(1/2) instead of (128/27)^(1/2).  Both are recorded.

Also computes, for the same four parents, the 1410.3881-style quantities that
are model independent (a_i, T_i, formation thermal energy (3 pi/2) M c^2).
"""
import json
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent / "poplawski_stiff_mass_2026_09_18.json"

G = 6.67430e-11
c = 299792458.0
hbar = 1.054571817e-34
kB = 1.380649e-23
M_SUN = 1.98892e30
m_n = 1.67492749804e-27          # neutron mass, kg (CODATA 2018)
m_Pl = math.sqrt(hbar * c / G)   # Planck mass, kg
kappa = 8 * math.pi * G / c**4
hbarc = hbar * c

PAPER_prefactor = math.sqrt(128.0 / 27.0)   # his eq. (9)
OUR_prefactor_fq3 = math.sqrt(128.0 / 27.0)  # re-derived with f_q = 3 (his implicit choice)
OUR_prefactor_fq1 = math.sqrt(128.0 / 3.0)   # re-derived with f_q = 1
PAPER_M10_amin = 6e-3        # m, his eq. (11) for M = 10 Msun
PAPER_M10_mmax = 3.1e51      # kg, his eq. (11)
PAPER_Lambda = 5.24e-10 * kappa   # m^-2 (same Lambda/kappa as 1410.3881)


def stiff(M, f_q=3.0):
    r_s = 2 * G * M / c**2
    eps0 = M * c**2 / (4 * math.pi * r_s**3 / 3)
    n0 = f_q * M / (m_n * 4 * math.pi * r_s**3 / 3)
    ratio6 = kappa * (hbarc * n0)**2 / (32 * eps0)      # (a_min/a_0)^6, direct
    a_min_direct = r_s * ratio6**(1.0 / 6.0)
    amp_direct = ratio6**(-0.5)                          # (a_0/a_min)^3
    M_star = M**2 * m_n / m_Pl**2
    return dict(
        M_kg=M, M_Msun=M / M_SUN, r_s_m=r_s,
        M_star_kg=M_star, M_star_over_M=M_star / M,
        a_min_direct_m=a_min_direct,
        a_min_paper_formula_m=(27.0 / 128.0)**(1.0 / 6.0) * 2 * G / c**2 * (m_Pl**2 * M**2 / m_n)**(1.0 / 3.0),
        m_max_direct_kg=amp_direct * M,
        m_max_direct_over_M=amp_direct,
        m_max_paper_kg=PAPER_prefactor * M_star,
        m_max_paper_over_M=PAPER_prefactor * M_star / M,
        prefactor_direct=amp_direct / (M_star / M),
        prefactor_paper=PAPER_prefactor,
        f_q_fermions_per_neutron_mass=f_q,
        m_max_over_M_if_fq1=stiff(M, 1.0)["m_max_direct_over_M"] if f_q != 1.0 else amp_direct,
        # 1410.3881-style formation quantities (model independent)
        E_thermal_formation_over_Mc2=1.5 * math.pi,
        misner_sharp_equator_over_M=1.0,
    )


res = dict(
    provenance="Poplawski arXiv:1103.4192v1 (fetched 2026-09-18); constants CODATA 2018",
    m_Pl_kg=m_Pl, m_n_kg=m_n,
    prefactor_check=dict(paper=PAPER_prefactor, ours_fq3=OUR_prefactor_fq3, ours_fq1=OUR_prefactor_fq1,
                         note="his (27/128) reproduces iff n_0 counts 3 fermions per neutron mass (eq. 6, unstated); with 1 per neutron the prefactor is (128/3)^(1/2)"),
    M_c_escape_kg=(128.0 / (27.0 * PAPER_Lambda))**0.25 * m_Pl * c / math.sqrt(3 * G * m_n),   # his eq. (20)
    parents={},
)
res["M_c_escape_Msun"] = res["M_c_escape_kg"] / M_SUN
for Msun in [10.0, 1e3, 1e6, 1e10]:
    res["parents"][f"{Msun:.0e}"] = stiff(Msun * M_SUN)
# paper's own numeric example (M = 10 Msun)
s10 = stiff(10 * M_SUN)
res["paper_M10_check"] = dict(
    a_min_paper=PAPER_M10_amin, a_min_paper_formula=s10["a_min_paper_formula_m"], a_min_ours=s10["a_min_direct_m"],
    m_max_paper=PAPER_M10_mmax, m_max_paper_formula=s10["m_max_paper_kg"], m_max_ours=s10["m_max_direct_kg"],
)
OUT.write_text(json.dumps(res, indent=2))
print(json.dumps(res, indent=2))
