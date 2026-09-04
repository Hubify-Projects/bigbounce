"""
A3-1b -- the LAB'S OWN primordial curvature power spectrum Delta^2_zeta(k) at
PBH scales, and what it delivers into the compaction-function PBH channel.

Motivation (NEXT_SCIENCE_LEDGER #3, sub-item A3-1b; PBH_COMPACTION_NOTE_2026-09-02
section 8): the A3 PBH channel currently borrows an external spectrum
(Choudhury et al. 2025, arXiv:2409.18983) whose RRR one-loop Delta^2_zeta is NOT
reconstructible from the published paper (deviation D1 of that note).  Here we
replace it with the spectrum the lab's own matter-bounce model actually predicts,
and ask what that spectrum delivers.

INTEGRITY: the spectrum is fixed by the CMB anchor BEFORE any PBH number is
computed, and is never adjusted afterwards.  `pbh_compaction_fnl.py` is IMPORTED
and its committed functions are used unmodified; only the module-level spectrum
function is swapped (the documented dependency-injection point), and the module
is restored afterwards.  No committed result of that script is changed.

=============================================================================
PART 1 -- THE SPECTRUM
=============================================================================
For a contracting phase with equation of state w, the curvature perturbation
that exits the Hubble radius acquires

    Delta^2_zeta(k) = A_s (k/k_*)^{n_s - 1},     n_s - 1 = 12 w / (1 + 3w)

[LITERATURE: Wands 1999 (gr-qc/9809062) duality; Cai, Easson & Brandenberger 2012
(arXiv:1206.2382) sections 2-4; Quintin, Sherkatghanad, Cai & Brandenberger 2015
(arXiv:1508.04141) section 2 -- exact scale invariance for pure dust (w = 0), a
small tilt from a small deviation of w from zero.]  The lab does NOT predict w
independently, so the tilt is CALIBRATED, not predicted:

  * MB-anchored branch: n_s = 0.9649 (Planck 2018 TT,TE,EE+lowE+lensing),
    i.e. the matter-bounce w is fixed BY the observed tilt, w = (n_s-1)/(13-n_s).
  * pure-dust branch: n_s = 1 exactly (w = 0), reported as the bracket.

Amplitude anchor (both branches): A_s = 2.1e-9 at k_* = 0.05 Mpc^-1 (Planck 2018).
Both branches are single power laws with NO feature: the matter contraction has a
single dynamical scale, and A2 (research/cubic_bounce_transmission/, brief section
4.3) verified numerically that the post-bounce spectrum is flat to 1.2-4.2% across
its k grid, i.e. the bounce transfer is scale-INDEPENDENT for k*eta_B << 1.  The
extrapolation to k ~ 1e5-1e15 Mpc^-1 is therefore an extrapolation of ~7-16
decades under exactly two assumptions:

  E1. w stays at its CMB-calibrated value over those decades (no epoch of
      w-evolution, no USR-like phase, no feature).
  E2. k*eta_B << 1 still holds -- outside that the A2 transfer analysis does not
      apply and the extrapolation is not defended.  k_B = 1/eta_B is computed
      below for the A2 backgrounds and marked on the figure.

=============================================================================
PART 2 -- LITERATURE ENHANCEMENT CANDIDATES (labelled as literature)
=============================================================================
Handled in the accompanying .md; the script records the checked claims as data.

=============================================================================
PART 3 -- DELIVERED vs REQUIRED AMPLITUDE
=============================================================================
The committed compaction machinery is run with the power-law spectrum in place of
the lognormal, at each candidate PBH mass scale, and the amplitude required for
f_PBH in {1e-3, 1e-2, 1} at f_NL = -35/16 and -35/8 is solved for.

=============================================================================
PART 4 -- FIRAS mu-DISTORTION
=============================================================================
mu = 2.2 Int dk/k Delta^2_zeta(k) [exp(-k/5400 Mpc^-1) - exp(-(k/31.6 Mpc^-1)^2)]
[LITERATURE: Chluba, Erickcek & Ben-Dayan 2012, arXiv:1203.2681, their Eq. (16)
window.]  Bound: |mu| < 9e-5 (95% CL, COBE/FIRAS, Fixsen et al. 1996).

Venue: local, no GPU, cost $0.
Outputs: outputs/inlab_delta2_zeta_2026-09-03.{json,png}
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.optimize import brentq

import pbh_compaction_fnl as PC

HERE = Path(__file__).resolve().parent
OUTJSON = HERE / "outputs/inlab_delta2_zeta_2026-09-03.json"
OUTPNG = HERE / "outputs/inlab_delta2_zeta_2026-09-03.png"

# ------------------------------------------------------------- CMB anchor
A_S = 2.1e-9                 # Planck 2018 (TT,TE,EE+lowE+lensing), k_* = 0.05
K_STAR = 0.05                # Mpc^-1
N_S_PLANCK = 0.9649
N_S_SIG = 0.0042

BRANCHES = {
    "MB_anchored_ns0.9649": N_S_PLANCK,
    "pure_dust_ns1": 1.0,
}

# ------------------------------------------------------------- constants
M_SUN_G = 1.98847e33
G_STAR_RD = 106.75
FNL_CASES = {"gaussian_0": 0.0,
             "matter_bounce_Li_-35/16": -35.0 / 16.0,
             "matter_bounce_Cai_-35/8": -35.0 / 8.0}
F_PBH_TARGETS = [1e-3, 1e-2, 1.0]
MU_FIRAS = 9.0e-5


def delta2_zeta_inlab(k_mpc, n_s):
    """The lab's matter-bounce spectrum, in Mpc^-1 units. No feature, no bump."""
    return A_S * (np.asarray(k_mpc, dtype=float) / K_STAR) ** (n_s - 1.0)


# ------------------------------------------------------ k <-> horizon mass
def horizon_mass_of_k(k_mpc, g_star=G_STAR_RD, g_star_s=G_STAR_RD):
    """M_H at horizon crossing k = aH in radiation domination, derived, not quoted.

    M_H = 4 pi M_pl^2 / H  (from M = (4pi/3) rho H^-3, rho = 3 M_pl^2 H^2),
    with H fixed by k = aH and entropy conservation a T g_s^(1/3) = a0 T0 g_s0^(1/3).
    """
    Mpl = 2.435323e18                      # reduced Planck mass, GeV
    T0 = 2.7255 * 8.617333262e-14          # CMB temperature today, GeV
    g_s0 = 3.9091                          # today (photons + 3 nu)
    Mpc_inv_GeV = 6.39193e-39              # 1 Mpc^-1 in GeV (hbar=c=1)
    k = np.asarray(k_mpc, dtype=float) * Mpc_inv_GeV
    # rho = (pi^2/30) g_* T^4 = 3 Mpl^2 H^2  ->  H(T)
    # a/a0 = (T0/T) (g_s0/g_s)^(1/3);  k = a H  ->  solve for T
    # k = a0 (T0/T)(g_s0/g_s)^(1/3) H(T); take a0 = 1 (comoving k in Mpc^-1 today)
    c_H = np.sqrt(np.pi ** 2 * g_star / 90.0) / Mpl        # H = c_H T^2
    c_a = T0 * (g_s0 / g_star_s) ** (1.0 / 3.0)            # a = c_a / T
    T = k / (c_a * c_H)                                    # from k = c_a c_H T
    H = c_H * T ** 2
    M_GeV = 4.0 * np.pi * Mpl ** 2 / H
    GeV_in_g = 1.78266192e-24
    return M_GeV * GeV_in_g


def k_of_horizon_mass(M_g):
    lk = brentq(lambda x: np.log(horizon_mass_of_k(10.0 ** x) / M_g),
                -6.0, 25.0, xtol=1e-12)
    return float(10.0 ** lk)


# --------------------------------------------------- mu-distortion (Chluba+12)
def mu_distortion(spec_fn, k_lo=1.0, k_hi=1e6, n=200000):
    k = np.logspace(np.log10(k_lo), np.log10(k_hi), n)
    W = np.exp(-k / 5400.0) - np.exp(-((k / 31.6) ** 2))
    return float(2.2 * simpson(spec_fn(k) * W, x=np.log(k)))


def mu_window_integral(k_lo=1.0, k_hi=1e6, n=200000):
    k = np.logspace(np.log10(k_lo), np.log10(k_hi), n)
    W = np.exp(-k / 5400.0) - np.exp(-((k / 31.6) ** 2))
    return float(2.2 * simpson(W, x=np.log(k)))


# ------------------------------- required amplitude with the LAB spectrum shape
def _patch_powerlaw(n_s, ir_cut=0.0):
    """Swap the module spectrum for the lab power law, normalised so A = Delta^2 at k_p.

    `ir_cut` is k_min/k_p; 0 means "whatever the committed integrator's grid edge
    is" (that grid runs from 1e-5 k_p to 1e3 k_p, so the effective IR cutoff is
    1e-5 k_p). A near-scale-invariant spectrum makes sigma_r logarithmically
    IR-sensitive, so the cutoff is scanned rather than hidden.
    """
    def d2(k, A, kp=1.0, dl=None):
        kk = np.asarray(k, dtype=float) / kp
        out = A * kk ** (n_s - 1.0)
        if ir_cut > 0:
            out = np.where(kk < ir_cut, 0.0, out)
        return out
    PC.delta2_zeta = d2


def _restore():
    PC.delta2_zeta = _ORIG_SPEC


_ORIG_SPEC = PC.delta2_zeta


def gaussian_beta_exponent(A, c_th=PC.C_TH_BASE, rp=1.0):
    """Decades of suppression in the Gaussian limit: log10 exp(-C_lin,-^2/(2 sigma_c^2)).

    Used only where beta underflows to exactly zero in double precision, so that
    'no PBHs' can be quantified rather than reported as a bare 0.
    """
    sc, sr, _, g = PC.covariances(A, rp, 1.0)
    c_lin_minus = 2.0 * PC.F_W * (1.0 - np.sqrt(max(1.0 - c_th / PC.F_W, 0.0)))
    nsig = c_lin_minus / sc
    return {"sigma_c": float(sc), "sigma_r": float(sr), "gamma_cr": float(g),
            "C_lin_minus": float(c_lin_minus), "n_sigma_to_threshold": float(nsig),
            "log10_beta_gaussian_estimate": float(-nsig ** 2 / (2.0 * np.log(10.0)))}


def main():
    t0 = time.time()
    out = {"generated": "2026-09-03", "script": Path(__file__).name}
    print("=" * 78)
    print("A3-1b: the lab's own Delta^2_zeta(k) at PBH scales")
    print("=" * 78)

    # ---------------- (1) spectrum + validity ------------------------------
    print("\n--- (1) SPECTRUM (CMB-anchored, no feature) ---")
    spec = {"A_s": A_S, "k_star_Mpc-1": K_STAR,
            "n_s_planck2018": N_S_PLANCK, "n_s_sigma": N_S_SIG,
            "branches": {}}
    for name, ns in BRANCHES.items():
        w = (ns - 1.0) / (3.0 * (5.0 - ns))      # n_s-1 = 12w/(1+3w) inverted
        row = {"n_s": ns, "implied_w_matter_bounce": w,
               "delta2_zeta_at_k": {}}
        for kk in [0.05, 1e2, 1e4, 1e5, 1e8, 1e13, 1e15]:
            row["delta2_zeta_at_k"][f"k={kk:.0e}"] = float(delta2_zeta_inlab(kk, ns))
        spec["branches"][name] = row
        print(f"  {name}: w = {w:+.5f}")
        for kk in [1e2, 1e4, 1e13, 1e15]:
            print(f"      Delta^2_zeta({kk:.0e} Mpc^-1) = "
                  f"{delta2_zeta_inlab(kk, ns):.4e}")
    # tilt uncertainty on the extrapolation
    for kk in [1e13, 1e15]:
        hi = A_S * (kk / K_STAR) ** (N_S_PLANCK + N_S_SIG - 1.0)
        lo = A_S * (kk / K_STAR) ** (N_S_PLANCK - N_S_SIG - 1.0)
        spec.setdefault("tilt_1sigma_band", {})[f"k={kk:.0e}"] = {"lo": lo, "hi": hi}
        print(f"  1-sigma tilt band at k={kk:.0e}: [{lo:.3e}, {hi:.3e}]")
    out["spectrum"] = spec

    # A2 validity scale k_B = 1/eta_B (eta_B in the A2 units of the same brief)
    print("\n--- (1b) A2 validity: the extrapolation is defended only for k eta_B << 1 ---")
    a2 = {"note": ("eta_B values from research/cubic_bounce_transmission/ "
                   "A2_TRANSMISSION_BRIEF_2026-09-02.md section 4.1 (a2_transmission_linear.py); "
                   "k_B = 1/eta_B in the same (bounce) units. Converting k_B to Mpc^-1 "
                   "requires the bounce energy scale, which the lab has NOT committed "
                   "(no rho_c/T_B in the repo) -- so k_B is reported in bounce units and "
                   "the Mpc^-1 mapping is given as a function of the bounce temperature."),
          "eta_B_bounce_units": {"LQC_effective_dust": 1.06015,
                                 "analytic_non_LQC_poly": 0.57735,
                                 "Quintin2015_type": 0.44960},
          "k_B_bounce_units": {},
          "k_B_Mpc-1_if_T_B_GeV": {}}
    for nm, eb in a2["eta_B_bounce_units"].items():
        a2["k_B_bounce_units"][nm] = 1.0 / eb
    # k_B in Mpc^-1: the comoving scale crossing the horizon at the bounce
    for T_B in [1e16, 1e14, 1e10]:
        # comoving k that equals aH at temperature T_B (radiation, same relation)
        Mpl = 2.435323e18
        T0 = 2.7255 * 8.617333262e-14
        g_s0, gs = 3.9091, G_STAR_RD
        c_H = np.sqrt(np.pi ** 2 * G_STAR_RD / 90.0) / Mpl
        c_a = T0 * (g_s0 / gs) ** (1.0 / 3.0)
        k_GeV = c_a * c_H * T_B
        kB = k_GeV / 6.39193e-39
        a2["k_B_Mpc-1_if_T_B_GeV"][f"T_B={T_B:.0e}"] = float(kB)
        print(f"  bounce at T_B={T_B:.0e} GeV -> k_B ~ {kB:.3e} Mpc^-1 "
              f"(PBH scales 1e5-1e15 are k eta_B ~ {1e15/kB:.1e} at k=1e15)")
    out["a2_validity"] = a2

    # ---------------- (2) literature enhancement candidates -----------------
    print("\n--- (2) literature enhancement candidates (LITERATURE, not lab results) ---")
    lit = [
        {"ref": "Quintin, Sherkatghanad, Cai & Brandenberger 2015, arXiv:1508.04141",
         "claim": ("growth of the curvature/bispectrum amplitude through a "
                   "non-singular bounce; the bounce's own cubic vertices ENHANCE f_NL"),
         "produces_small_scale_bump_in_Delta2_zeta_in_this_model": False,
         "why": ("the enhancement acts on the BISPECTRUM (cubic) amplitude, not on the "
                 "power spectrum; A2's linear transfer of the same bounce backgrounds "
                 "gives a k-INDEPENDENT factor for k eta_B << 1 (A2 brief section 4.3, "
                 "post-bounce spectrum flat to 1.2-4.2%), so no small-scale bump")},
        {"ref": "Agullo, Bolliet & Sreenath 2017, arXiv:1712.08148",
         "claim": ("LQC bounce strongly enhances primordial non-Gaussianity; the "
                   "power spectrum acquires oscillatory structure and a rise near the "
                   "bounce curvature scale k ~ k_B"),
         "produces_small_scale_bump_in_Delta2_zeta_in_this_model": False,
         "why": ("the structure sits at k ~ k_B, i.e. exactly where the A2 super-Hubble "
                 "transfer analysis stops being valid (k eta_B ~ 1). PBH scales "
                 "1e5-1e15 Mpc^-1 are many orders BELOW k_B for any bounce above the "
                 "BBN scale, so within this lab's stated validity domain the effect "
                 "does not reach PBH scales")},
        {"ref": "Chen, Zhu, Yan, Wang & Cai 2022/2023, arXiv:2207.14532 (JCAP 01 (2023) 015) "
                "-- 'Enhance primordial black hole abundance through the non-linear "
                "processes around bounce point'. THIS is the reference the A3 task "
                "pointer 'Chen-Wang-Xu et al 2023, arXiv:2210.xxxx' was reaching for; "
                "the id is 2207.14532, not a 2210 one. Predecessor: Chen, Yeom & Cai "
                "et al 2016, arXiv:1609.02571, 'Tracing primordial black holes in "
                "nonsingular bouncing cosmology'.",
         "claim": ("non-linear processes in the BOUNCE PHASE itself amplify density "
                   "fluctuations and can enhance the PBH abundance relative to the "
                   "linear expectation"),
         "produces_small_scale_bump_in_Delta2_zeta_in_this_model": False,
         "why": ("the amplification is a bounce-phase effect operating on modes that "
                 "are NOT deep super-Hubble at the bounce, i.e. k eta_B ~ 1. The lab's "
                 "committed transfer result (A2) is derived for k eta_B << 1 and is "
                 "explicitly not defended at k eta_B ~ 1. For any bounce above the BBN "
                 "scale, k_B >= 1e17 Mpc^-1, so PBH scales 1e5-1e15 Mpc^-1 sit at "
                 "k eta_B <= 1e-2 -- far outside the regime where this enhancement "
                 "operates. Importing it would be importing an effect from outside the "
                 "model's validated domain")},
        {"ref": "Papanikolaou, Banerjee, Cai, Capozziello & Saridakis 2024, "
                "arXiv:2404.03779 (JCAP 06 (2024)); see also arXiv:2405.00207, "
                "arXiv:2602.12057",
         "claim": ("PBHs in non-singular matter bouncing cosmology form by DIRECT "
                   "gravitational collapse during the pressureless CONTRACTING phase, "
                   "not from a radiation-era threshold crossing"),
         "produces_small_scale_bump_in_Delta2_zeta_in_this_model": False,
         "why": ("this is a different formation channel altogether and is OUT OF SCOPE "
                 "of the compaction-function criterion used here, which assumes "
                 "radiation-era (w = 1/3) collapse at horizon re-entry. It is recorded "
                 "as an untested alternative channel for the matter bounce, not as an "
                 "enhancement of Delta^2_zeta. Flagged as new open item A3-1e")},
    ]
    for L in lit:
        print(f"  [LIT] {L['ref']}\n        bump in this model? "
              f"{L['produces_small_scale_bump_in_Delta2_zeta_in_this_model']}")
    out["literature_enhancement_candidates"] = lit

    # ---------------- (3) delivered vs required ----------------------------
    print("\n--- (3) DELIVERED vs REQUIRED amplitude (committed compaction machinery) ---")
    mass_scales = {
        "M_H=1e15 g (evaporating)": 1e15,
        "M_H=1e20 g (asteroid window; the A3-1 mass)": 1e20,
        "M_H=1 Msun": M_SUN_G,
        "M_H=30 Msun (LIGO)": 30 * M_SUN_G,
        "M_H=1e4 Msun (early-SMBH seed)": 1e4 * M_SUN_G,
    }
    # sanity: the standard anchor k = 2.9e5 Mpc^-1 <-> tens of solar masses
    anchor_M = horizon_mass_of_k(2.9e5) / M_SUN_G
    print(f"  [check] k = 2.9e5 Mpc^-1 -> M_H = {anchor_M:.2f} Msun "
          f"-> M_PBH = gamma M_H = {0.2*anchor_M:.1f} Msun at gamma=0.2 "
          f"(literature anchor: k=2.9e5 Mpc^-1 <-> ~30 Msun PBH)")
    out["k_mass_anchor_check_Msun_at_k2.9e5"] = float(anchor_M)

    ns_main = N_S_PLANCK
    _patch_powerlaw(ns_main)
    req = {}
    try:
        # `PC.f_pbh` evaluates their Eq. (66) at the module's fixed M_H = 1e20 g.
        # f_PBH scales as (M_sun/M_H)^{1/2}, so the target at another horizon
        # mass is rescaled rather than the committed function being edited.
        def A_required(target, f_nl, M_H_g, c_th=0.5):
            tgt = target * (M_H_g / PC.M_H_G) ** 0.5
            return PC.A_for_fpbh(tgt, f_nl, c_th, 1.0, 1e-4, 50.0)

        per_mass = {}
        for label, Mg in mass_scales.items():
            kp = k_of_horizon_mass(Mg)
            A_del = float(delta2_zeta_inlab(kp, ns_main))
            A_del_dust = float(delta2_zeta_inlab(kp, 1.0))
            g = gaussian_beta_exponent(A_del)
            row = {"M_H_g": Mg, "k_p_Mpc-1": kp,
                   "M_PBH_g_gamma0.2": 0.2 * Mg,
                   "delivered_delta2_zeta_ns0.9649": A_del,
                   "delivered_delta2_zeta_ns1": A_del_dust,
                   "gaussian_limit_at_delivered_amplitude": g,
                   "required_over_delivered": {}}
            for tgt in F_PBH_TARGETS:
                for fname, fv in FNL_CASES.items():
                    Areq = A_required(tgt, fv, Mg)
                    key = f"f_PBH={tgt:g}|{fname}"
                    req[f"{label}|{key}"] = Areq
                    row["required_over_delivered"][key] = {
                        "A_required": Areq,
                        "ratio_required_over_delivered": (Areq / A_del) if Areq else None,
                        "log10_ratio": (float(np.log10(Areq / A_del)) if Areq else None)}
            # the actual machinery at the delivered amplitude (expected: exact 0)
            row["f_PBH_at_delivered_amplitude"] = {
                fname: float(PC.f_pbh(fv, A_del, 0.5, 1.0)) * (PC.M_H_G / Mg) ** 0.5
                for fname, fv in FNL_CASES.items()}
            per_mass[label] = row
            r = row["required_over_delivered"]["f_PBH=0.001|matter_bounce_Li_-35/16"]
            print(f"  {label}:  k_p = {kp:.3e} Mpc^-1   delivered "
                  f"Delta^2 = {A_del:.4e}   required(f_PBH=1e-3, -35/16) = "
                  f"{r['A_required']:.5f}   ratio = {r['ratio_required_over_delivered']:.3e}")
            print(f"      f_PBH delivered = "
                  f"{row['f_PBH_at_delivered_amplitude']['matter_bounce_Li_-35/16']:.3e}"
                  f"   (Gaussian-limit log10 beta ~ "
                  f"{g['log10_beta_gaussian_estimate']:.3e}, "
                  f"{g['n_sigma_to_threshold']:.3e} sigma to threshold)")

        # threshold + IR-cutoff sensitivity of the required amplitude
        print("\n  sensitivity of A_required (f_PBH=1e-3, M_H=1e20 g):")
        sens = {}
        for ct in [0.4, 0.5, 0.6]:
            for fname, fv in FNL_CASES.items():
                sens[f"C_th={ct}|{fname}"] = A_required(1e-3, fv, 1e20, ct)
            print(f"    C_th={ct}: A(0)={sens[f'C_th={ct}|gaussian_0']:.5f}  "
                  f"A(-35/16)={sens[f'C_th={ct}|matter_bounce_Li_-35/16']:.5f}  "
                  f"A(-35/8)={sens[f'C_th={ct}|matter_bounce_Cai_-35/8']:.5f}")
        ir = {}
        for cut in [1e-5, 1e-3, 1e-2, 1e-1]:
            _patch_powerlaw(ns_main, ir_cut=cut)
            _, _, _, gcr = PC.covariances(0.01, 1.0, 1.0)
            ir[f"k_min/k_p={cut:g}"] = {
                "gamma_cr": float(gcr),
                "A_required_-35/16": A_required(1e-3, -35.0 / 16.0, 1e20),
                "A_required_0": A_required(1e-3, 0.0, 1e20)}
            print(f"    IR cutoff k_min/k_p={cut:g}: gamma_cr={gcr:.4f}  "
                  f"A(-35/16)={ir[f'k_min/k_p={cut:g}']['A_required_-35/16']:.5f}")
        _patch_powerlaw(ns_main)
    finally:
        _restore()
    out["required_amplitudes_powerlaw_shape"] = req
    out["threshold_sensitivity"] = sens
    out["ir_cutoff_sensitivity"] = ir
    out["per_mass_scale"] = per_mass
    assert PC.delta2_zeta is _ORIG_SPEC, "committed spectrum not restored"

    # ---------------- (4) FIRAS mu-distortion ------------------------------
    print("\n--- (4) FIRAS mu-distortion (Chluba+2012 window; |mu| < 9e-5) ---")
    Wint = mu_window_integral()
    mu = {"window_integral_2.2_int_dlnk_W": Wint, "mu_FIRAS_95CL": MU_FIRAS,
          "branches": {}, "required_amplitude_check": {}}
    for name, ns in BRANCHES.items():
        m = mu_distortion(lambda k, ns=ns: delta2_zeta_inlab(k, ns))
        mu["branches"][name] = {"mu": m, "mu_over_FIRAS": m / MU_FIRAS,
                                "allowed": bool(abs(m) < MU_FIRAS)}
        print(f"  {name}: mu = {m:.4e}  ({m/MU_FIRAS:.3e} x FIRAS)  "
              f"{'ALLOWED' if abs(m) < MU_FIRAS else 'EXCLUDED'}")
    # max flat amplitude allowed in the mu window
    A_mu_max = MU_FIRAS / Wint
    mu["max_flat_delta2_zeta_allowed_in_mu_window"] = A_mu_max
    print(f"  maximum k-independent Delta^2_zeta over the mu window: {A_mu_max:.4e}")
    # the early-SMBH-seed channel (ledger #6): scan seed masses
    print("  early-SMBH seed channel (ledger #6) -- required amplitude vs FIRAS:")
    seeds = {}
    _patch_powerlaw(ns_main)
    try:
        for M_seed in [1e3, 1e4, 1e5, 1e6]:
            Mg = M_seed * M_SUN_G
            ks = k_of_horizon_mass(Mg)
            Areq = PC.A_for_fpbh(1e-3 * (Mg / PC.M_H_G) ** 0.5, -35.0 / 16.0,
                                 0.5, 1.0, 1e-4, 50.0)
            # (a) broadband: the required amplitude carried as a power law
            mu_pl = mu_distortion(lambda k, A=Areq, kp=ks: A * (k / kp) ** (ns_main - 1.0))
            # (b) narrow: a lognormal peak of width Delta = 0.5 at k_seed
            def _ln(k, A=Areq, kp=ks):
                return A * np.exp(-np.log(k / kp) ** 2 / (2 * 0.5 ** 2))
            mu_ln = mu_distortion(_ln)
            seeds[f"M_seed={M_seed:.0e} Msun"] = {
                "k_seed_Mpc-1": ks, "M_H_g": Mg,
                "A_required_fPBH1e-3_at_-35/16": Areq,
                "delivered_delta2_zeta": float(delta2_zeta_inlab(ks, ns_main)),
                "mu_broadband_powerlaw": mu_pl,
                "mu_broadband_over_FIRAS": mu_pl / MU_FIRAS,
                "mu_narrow_lognormal_dl0.5": mu_ln,
                "mu_narrow_over_FIRAS": mu_ln / MU_FIRAS,
                "FIRAS_verdict": ("EXCLUDED (both realisations)" if abs(mu_ln) > MU_FIRAS
                                  else "broadband EXCLUDED, narrow peak ALLOWED"
                                  if abs(mu_pl) > MU_FIRAS else "ALLOWED")}
            print(f"    {M_seed:.0e} Msun (k={ks:.3e}): A_req={Areq:.5f}  "
                  f"mu_broad={mu_pl:.3e} ({mu_pl/MU_FIRAS:.2e}x)  "
                  f"mu_narrow={mu_ln:.3e} ({mu_ln/MU_FIRAS:.2e}x)  "
                  f"-> {seeds[f'M_seed={M_seed:.0e} Msun']['FIRAS_verdict']}")
    finally:
        _restore()
    mu["required_amplitude_check"] = {
        "note": ("A seed of 1e3-1e6 Msun crosses the horizon at k ~ 1e3-1e5 Mpc^-1, "
                 "on/near the COBE/FIRAS mu window (30-5400 Mpc^-1), so the required "
                 "seed amplitude is directly constrained. Two realisations are "
                 "reported because the verdict differs between them."),
        "seeds": seeds}
    A_req_smbh = seeds["M_seed=1e+04 Msun"]["A_required_fPBH1e-3_at_-35/16"]
    mu_req = seeds["M_seed=1e+04 Msun"]["mu_broadband_powerlaw"]
    out["mu_distortion"] = mu

    # ---------------- verdict ----------------------------------------------
    r16 = per_mass["M_H=1e20 g (asteroid window; the A3-1 mass)"][
        "required_over_delivered"]["f_PBH=0.001|matter_bounce_Li_-35/16"]
    verdict = {
        "does_the_lab_spectrum_make_PBHs": "NO",
        "margin_log10_in_amplitude": r16["log10_ratio"],
        "statement": (
            "The lab's own CMB-anchored matter-bounce spectrum delivers "
            f"Delta^2_zeta ~ 1e-9 at every PBH scale, while the compaction-function "
            f"criterion requires ~0.1-0.5 -- a shortfall of "
            f"{r16['log10_ratio']:.1f} orders of magnitude in amplitude at every mass "
            "scale and at both f_NL values. f_PBH is exactly zero in double precision; "
            "the Gaussian-limit exponent quantifies how far. The PBH channel is "
            "therefore NOT a channel for this model without an added small-scale "
            "amplification mechanism the model does not contain."),
        "early_SMBH_seed_FIRAS": {
            k: v["FIRAS_verdict"] for k, v in seeds.items()},
        "early_SMBH_seed_summary": (
            "The amplitude a 1e3-1e6 Msun PBH seed requires is EXCLUDED by "
            "COBE/FIRAS if it is carried by a broadband (power-law) spectrum "
            f"(mu up to {max(abs(v['mu_broadband_powerlaw']) for v in seeds.values()):.2e} "
            f"vs mu < {MU_FIRAS:.0e}); a narrow (Delta=0.5 lognormal) peak at the seed "
            "scale evades it only for the lightest seed considered (1e3 Msun, k = 1.2e5 "
            "Mpc^-1, above the window); 1e4-1e6 Msun seeds are excluded in both "
            "realisations. Either way the lab's own "
            "spectrum is ~7 dex below the required amplitude, so the lab's model does "
            "not supply the seeds and the discriminator is a null."),
    }
    out["verdict"] = verdict
    print("\n--- VERDICT ---")
    print(f"  PBHs from the lab's own spectrum: {verdict['does_the_lab_spectrum_make_PBHs']} "
          f"(by {r16['log10_ratio']:.1f} dex in amplitude)")
    print(f"  early-SMBH seed amplitude vs FIRAS: {verdict['early_SMBH_seed_summary']}")

    out["wall_clock_s"] = time.time() - t0
    OUTJSON.parent.mkdir(parents=True, exist_ok=True)
    OUTJSON.write_text(json.dumps(out, indent=2))
    print(f"\nwrote {OUTJSON}  ({out['wall_clock_s']:.1f} s)")
    make_figure(out, per_mass, req, mu)
    print(f"wrote {OUTPNG}")


def make_figure(out, per_mass, req, mu):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    k = np.logspace(-3, 16, 4000)
    fig, ax = plt.subplots(figsize=(9.5, 6.0))
    ax.loglog(k, delta2_zeta_inlab(k, N_S_PLANCK), lw=2.2, color="C0",
              label=r"in-lab $\Delta^2_\zeta$, $n_s=0.9649$ (CMB-anchored)")
    ax.loglog(k, delta2_zeta_inlab(k, 1.0), lw=1.4, ls="--", color="C0", alpha=0.7,
              label=r"pure dust, $n_s=1$")
    hi = A_S * (k / K_STAR) ** (N_S_PLANCK + N_S_SIG - 1.0)
    lo = A_S * (k / K_STAR) ** (N_S_PLANCK - N_S_SIG - 1.0)
    ax.fill_between(k, lo, hi, color="C0", alpha=0.18, lw=0,
                    label=r"$\pm1\sigma$ tilt")

    # required-amplitude bands (compaction criterion, power-law shape, C_th=0.5)
    for fname, col, ty in [("matter_bounce_Li_-35/16", "C3", 6.0),
                           ("matter_bounce_Cai_-35/8", "C1", 0.10)]:
        mlab = "M_H=1e20 g (asteroid window; the A3-1 mass)"
        a_lo = req[f"{mlab}|f_PBH=0.001|{fname}"]
        a_hi = req[f"{mlab}|f_PBH=1|{fname}"]
        ax.fill_between([1e4, 1e16], a_lo, a_hi, color=col, alpha=0.30, lw=0)
        lab = fname.split("_")[-1]
        ax.text(3e15, a_hi * ty, rf"required, $f_{{\rm NL}}={lab}$,"
                                 rf" $f_{{\rm PBH}}=10^{{-3}}\!-\!1$",
                color=col, ha="right", fontsize=8.5)

    # FIRAS mu window
    ax.axvspan(31.6, 5400.0, color="0.55", alpha=0.16, lw=0)
    ax.axhline(mu["max_flat_delta2_zeta_allowed_in_mu_window"], color="k",
               ls=":", lw=1.4)
    ax.text(1e2, mu["max_flat_delta2_zeta_allowed_in_mu_window"] * 1.5,
            r"COBE/FIRAS $\mu<9\times10^{-5}$ ceiling", fontsize=8.5)
    ax.text(1.3e2, 2e-14, r"$\mu$ window", fontsize=8.5, color="0.35")

    # mass markers
    for label, row in per_mass.items():
        ax.axvline(row["k_p_Mpc-1"], color="0.3", lw=0.7, alpha=0.5)
        ax.text(row["k_p_Mpc-1"], 3e-16, label.split("(")[0].replace("M_H=", ""),
                rotation=90, fontsize=7.0, va="bottom", ha="right", color="0.3")
    ax.axvline(K_STAR, color="C2", lw=1.2)
    ax.text(K_STAR * 1.4, 1e-4, "CMB pivot", fontsize=8, color="C2", rotation=90)

    ax.set_xlim(1e-3, 1e16)
    ax.set_ylim(1e-16, 1e1)
    ax.set_xlabel(r"$k\ [\mathrm{Mpc}^{-1}]$")
    ax.set_ylabel(r"$\Delta^2_\zeta(k)$")
    ax.set_title("A3-1b: the lab's own matter-bounce curvature spectrum vs. the "
                 "amplitude PBH formation requires", fontsize=10.5)
    ax.legend(loc="lower left", fontsize=8.5, framealpha=0.92)
    ax.grid(alpha=0.22, which="both", lw=0.4)
    fig.tight_layout()
    fig.savefig(OUTPNG, dpi=160)


if __name__ == "__main__":
    main()
