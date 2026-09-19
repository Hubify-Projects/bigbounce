#!/usr/bin/env python3
"""
cosmic_fate_turnaround_2026_09_18.py
====================================

Numerics backing `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` (worker W3,
2025 legacy-archaeology campaign).  Every number quoted in that memo is produced
here; nothing in the memo is hand-typed.

Three independent calculations, all from the standard FLRW Friedmann equation
(textbook GR; see memo Sec. 2 for the derivation and the dimensional checks):

  (A) Closed-LambdaCDM recollapse boundary.
      E^2(a) = Om a^-3 + Ok a^-2 + OL ,   Ok = 1 - Om - OL.
      A future turnaround exists iff E^2(a) has a root at a > 1.
      Numeric root scan + bisection on OL gives OL_crit(Om); cross-checked
      against the analytic criterion derived in the memo,
          4 |Ok|^3 = 27 Om^2 OL      (with a_* = sqrt(|Ok|/(3 OL)) > 1).

  (B) Flat universe with matter + a NEGATIVE cosmological constant.
      a_turn/a_0 = (Om/|OL|)^(1/3);  a(t) = a_turn [sin(1.5 sqrt(|OL|) H0 t)]^(2/3).
      Gives present age t_0, time of turnaround t_ta, and time of the crunch.

  (C) Maximum turnaround radius of a bound mass in LambdaCDM,
      r_ta = (3 G M / (Lambda c^2))^(1/3)   [Pavlidou & Tomaras, arXiv:1310.1920].

Cosmology inputs (Planck 2018 VI, arXiv:1807.06209, abstract values verified
2026-09-18): H0 = 67.4 km/s/Mpc, Om = 0.315 -> OL = 1 - Om = 0.685 (flat).
Constants: IAU nominal GM_sun; CODATA c (exact).

Usage:  python3 cosmic_fate_turnaround_2026_09_18.py
Writes: cosmic_fate_turnaround_2026_09_18.json  (same directory)

No third-party dependencies.  Deterministic.
"""

import json
import math
import os
from datetime import datetime, timezone

# ---------------------------------------------------------------- constants --
C_LIGHT = 2.997_924_58e8          # m/s, exact by definition
GM_SUN = 1.327_124_400_18e20      # m^3/s^2, IAU 2015 nominal solar mass parameter
MPC = 3.085_677_581_491_3673e22   # m
KM = 1.0e3
GYR = 3.155_76e16                 # s  (10^9 Julian years of 3.15576e7 s)

# Planck 2018 VI (arXiv:1807.06209) abstract values
H0_KM_S_MPC = 67.4
OMEGA_M_PLANCK = 0.315
OMEGA_L_PLANCK = 1.0 - OMEGA_M_PLANCK   # flat LambdaCDM

H0_SI = H0_KM_S_MPC * KM / MPC          # 1/s
HUBBLE_TIME_GYR = (1.0 / H0_SI) / GYR

# Lambda from the flat-LambdaCDM definition OL = Lambda c^2 / (3 H0^2)
LAMBDA_SI = 3.0 * OMEGA_L_PLANCK * H0_SI ** 2 / C_LIGHT ** 2   # 1/m^2


# ------------------------------------------------------ (A) closed LambdaCDM --
def e2(a, om, ol):
    """E^2(a) = (H/H0)^2 for matter + curvature + constant Lambda."""
    ok = 1.0 - om - ol
    return om / a ** 3 + ok / a ** 2 + ol


def g_cubic(a, om, ol):
    """a^3 E^2(a) = OL a^3 + Ok a + Om ; same sign as E^2 for a > 0."""
    ok = 1.0 - om - ol
    return ol * a ** 3 + ok * a + om


def turnaround_scale_factor(om, ol):
    """Smallest a > 1 with E^2(a) = 0, or None if the model expands forever.

    Works on the cubic g(a) = a^3 E^2(a) = OL a^3 + Ok a + Om, which has the
    same sign as E^2 for a > 0 and is entire.  Note g(1) = Om + Ok + OL = 1 > 0
    identically, so a = 1 is always an allowed expanding epoch.

      OL > 0 : g is convex-up at large a; it can dip below zero only if Ok < 0,
               at the single positive stationary point a_* = sqrt(|Ok|/(3 OL)).
               A future turnaround therefore requires g(a_*) <= 0 AND a_* > 1.
      OL = 0 : g is linear; a root at a > 1 requires Ok < 0 and Om/|Ok| > 1.
      OL < 0 : g -> -infinity, so a root at a > 1 always exists.

    Bisection then returns the smallest root above 1.
    """
    if e2(1.0, om, ol) <= 0.0:
        return 1.0
    ok = 1.0 - om - ol

    if ol > 0.0:
        if ok >= 0.0:
            return None
        a_star = math.sqrt(abs(ok) / (3.0 * ol))
        if a_star <= 1.0:
            return None                      # dip (if any) lies in the past
        if g_cubic(a_star, om, ol) > 0.0:
            return None                      # never reaches zero
        lo, hi = 1.0, a_star
    elif ol == 0.0:
        if ok >= 0.0:
            return None
        root = om / abs(ok)
        return root if root > 1.0 else None
    else:
        hi = 1.0
        while g_cubic(hi, om, ol) > 0.0:
            hi *= 2.0
            if hi > 1.0e12:
                return None
        lo = max(1.0, hi / 2.0)

    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if g_cubic(mid, om, ol) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def brute_turnaround(om, ol, a_max=1.0e4, n=400_000):
    """Independent brute-force check of turnaround_scale_factor (log grid scan)."""
    prev_a, prev_v = 1.0, e2(1.0, om, ol)
    if prev_v <= 0.0:
        return 1.0
    lb = math.log(a_max)
    for i in range(1, n + 1):
        a = math.exp(lb * i / n)
        v = e2(a, om, ol)
        if v <= 0.0:
            lo, hi = prev_a, a
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if e2(mid, om, ol) > 0.0:
                    lo = mid
                else:
                    hi = mid
            return 0.5 * (lo + hi)
        prev_a, prev_v = a, v
    return None


def recollapses(om, ol):
    return turnaround_scale_factor(om, ol) is not None


def omega_lambda_crit(om, lo=-5.0, hi=50.0):
    """Largest OL that still permits a future turnaround, at fixed Om.

    recollapses() is monotone decreasing in OL at fixed Om (more Lambda can
    only help the universe escape), so a plain bisection is valid.
    """
    if not recollapses(om, lo):
        return None
    if recollapses(om, hi):
        return None  # boundary outside bracket
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if recollapses(om, mid):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def analytic_discriminant(om, ol):
    """4|Ok|^3 - 27 Om^2 OL ; zero on the derived boundary (memo Sec. 3b)."""
    ok = 1.0 - om - ol
    return 4.0 * abs(ok) ** 3 - 27.0 * om ** 2 * ol


def omega_m_crit_at_fixed_lambda(ol, lo=0.1, hi=1.0e4):
    """Smallest Om that recollapses at fixed OL (bisection; monotone in Om)."""
    if recollapses(lo, ol):
        return None
    if not recollapses(hi, ol):
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if recollapses(mid, ol):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


# -------------------------------------------- (B) flat, matter + negative Lam --
def negative_lambda_model(abs_ol):
    """Flat FLRW, matter + Lambda < 0.  Flatness forces Om = 1 + |OL|.

    a(t) = a_t [sin(x)]^(2/3),  x = (3/2) sqrt(|OL|) H0 t,  a_t = (Om/|OL|)^(1/3).
    Turnaround at x = pi/2, crunch (a -> 0) at x = pi.  Today: a = 1.
    """
    om = 1.0 + abs_ol
    a_turn = (om / abs_ol) ** (1.0 / 3.0)
    x0 = math.asin(math.sqrt(abs_ol / om))            # a(t_0) = 1
    tau = 1.0 / (1.5 * math.sqrt(abs_ol) * H0_SI)     # x = t/tau
    t0 = x0 * tau
    t_ta = (math.pi / 2.0) * tau
    t_crunch = math.pi * tau
    # independent consistency check: H(t_0)/H0 must be 1
    h_over_h0 = math.sqrt(abs_ol) / math.tan(x0)
    return {
        "abs_Omega_Lambda": abs_ol,
        "Omega_m_required_for_flatness": om,
        "a_turn_over_a0": a_turn,
        "age_today_Gyr": t0 / GYR,
        "time_of_turnaround_Gyr": t_ta / GYR,
        "time_from_now_to_turnaround_Gyr": (t_ta - t0) / GYR,
        "time_of_crunch_Gyr": t_crunch / GYR,
        "time_from_now_to_crunch_Gyr": (t_crunch - t0) / GYR,
        "check_H_over_H0_today": h_over_h0,
    }


# -------------------------------------------------- (C) max turnaround radius --
def r_turnaround_m(m_over_msun, lam=LAMBDA_SI):
    """r_ta = (3 G M / (Lambda c^2))^(1/3), in metres."""
    gm = GM_SUN * m_over_msun                    # m^3/s^2
    return (3.0 * gm / (lam * C_LIGHT ** 2)) ** (1.0 / 3.0)


# ----------------------------------------------------------------------- main --
def main():
    out = {
        "script": os.path.basename(__file__),
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "worker": "W3",
        "memo": "research/archaeology_2025/memos/COSMIC_FATE_MEMO.md",
        "inputs": {
            "H0_km_s_Mpc": H0_KM_S_MPC,
            "Omega_m": OMEGA_M_PLANCK,
            "Omega_Lambda_flat": OMEGA_L_PLANCK,
            "source": "Planck 2018 VI, arXiv:1807.06209 (abstract values verified 2026-09-18)",
            "c_m_s": C_LIGHT,
            "GM_sun_m3_s2": GM_SUN,
            "Mpc_m": MPC,
            "Gyr_s": GYR,
            "Hubble_time_Gyr": HUBBLE_TIME_GYR,
            "Lambda_m^-2": LAMBDA_SI,
            "Lambda_definition": "Lambda = 3 Omega_Lambda H0^2 / c^2",
        },
    }

    # ---- (A0) the actual universe -------------------------------------------
    a_t_real = turnaround_scale_factor(OMEGA_M_PLANCK, OMEGA_L_PLANCK)
    out["A0_observed_flat_LCDM"] = {
        "Omega_m": OMEGA_M_PLANCK,
        "Omega_Lambda": OMEGA_L_PLANCK,
        "Omega_k": 1.0 - OMEGA_M_PLANCK - OMEGA_L_PLANCK,
        "turnaround_scale_factor": a_t_real,
        "recollapses": a_t_real is not None,
        "E2_at_a_1e6": e2(1.0e6, OMEGA_M_PLANCK, OMEGA_L_PLANCK),
        "E2_floor_is_Omega_Lambda": OMEGA_L_PLANCK,
    }

    # ---- (A1) OL_crit(Om): the closed-LambdaCDM recollapse boundary ----------
    rows = []
    for om in [0.10, 0.31, 0.315, 0.50, 0.90, 1.00, 1.05, 1.50, 2.00, 3.00, 5.00, 10.00]:
        olc = omega_lambda_crit(om)
        row = {
            "Omega_m": om,
            "Omega_Lambda_crit": olc,
            "recollapse_requires": (
                "Omega_Lambda < %.6g" % olc if olc is not None else "no boundary in bracket"
            ),
        }
        if olc is not None:
            row["analytic_discriminant_at_boundary"] = analytic_discriminant(om, olc)
            ok = 1.0 - om - olc
            row["Omega_k_at_boundary"] = ok
            row["a_star_at_boundary"] = (
                math.sqrt(abs(ok) / (3.0 * olc)) if olc > 0 else None
            )
        rows.append(row)
    out["A1_closed_LCDM_recollapse_boundary"] = {
        "criterion_derived_in_memo_sec3b": (
            "future turnaround  <=>  Omega_Lambda < 0, "
            "OR (Omega_Lambda > 0 AND |Omega_k| > 3 Omega_Lambda "
            "AND 4|Omega_k|^3 >= 27 Omega_m^2 Omega_Lambda)"
        ),
        "note": (
            "|Omega_k| > 3 Omega_Lambda with Omega_k = 1 - Omega_m - Omega_Lambda < 0 "
            "requires Omega_Lambda < (Omega_m - 1)/2, so for Omega_m < 1 no positive "
            "Lambda permits recollapse at any curvature."
        ),
        "rows": rows,
    }

    # spot checks at Om = 0.31
    om_probe = 0.31
    out["A2_spot_checks_Om_0.31"] = [
        {
            "Omega_Lambda": ol,
            "Omega_k": 1.0 - om_probe - ol,
            "turnaround_a": turnaround_scale_factor(om_probe, ol),
        }
        for ol in [0.69, 0.80, 1.00, 1.50, 2.00, 0.0, -0.01, -0.10, -0.345, -0.69]
    ]

    # how much matter would be needed to recollapse with today's Lambda?
    om_crit = omega_m_crit_at_fixed_lambda(OMEGA_L_PLANCK)
    out["A3_matter_required_to_recollapse_at_observed_Lambda"] = {
        "Omega_Lambda_fixed": OMEGA_L_PLANCK,
        "Omega_m_min_for_recollapse": om_crit,
        "ratio_to_observed_Omega_m": (om_crit / OMEGA_M_PLANCK) if om_crit else None,
        "Omega_k_there": (1.0 - om_crit - OMEGA_L_PLANCK) if om_crit else None,
        "turnaround_a_just_above": (
            turnaround_scale_factor(om_crit * 1.01, OMEGA_L_PLANCK) if om_crit else None
        ),
    }

    # ---- (A4) analytic-vs-brute-force cross-check ---------------------------
    checks = []
    for om, ol in [
        (0.315, 0.685), (0.31, 1.50), (0.31, 2.00), (0.31, -0.10),
        (1.50, 0.02), (2.00, 0.01), (2.00, 0.10), (5.00, 0.50), (1.20, 0.00),
    ]:
        fast = turnaround_scale_factor(om, ol)
        slow = brute_turnaround(om, ol)
        agree = (fast is None and slow is None) or (
            fast is not None and slow is not None and abs(fast - slow) < 1e-6 * max(1.0, fast)
        )
        checks.append(
            {"Omega_m": om, "Omega_Lambda": ol, "analytic": fast, "brute_force": slow, "agree": agree}
        )
    out["A4_analytic_vs_bruteforce"] = checks

    # ---- (B) flat matter + negative Lambda ----------------------------------
    out["B_negative_Lambda_flat"] = {
        "solution": "a(t) = a_turn [sin((3/2) sqrt(|OL|) H0 t)]^(2/3), flatness forces Om = 1 + |OL|",
        "rows": [negative_lambda_model(x) for x in [0.001, 0.01, 0.05, 0.10, 0.345, 0.685]],
        "observational_note": (
            "every row has Omega_m > 1 and a present age below the observed "
            "13.8 Gyr, which is how the pure flat matter + negative-Lambda model "
            "is excluded; the rows are a scaling reference, not a fit."
        ),
    }

    # ---- (C) maximum turnaround radius --------------------------------------
    rta_rows = []
    for m in [1.0e12, 1.0e14, 1.0e15]:
        r = r_turnaround_m(m)
        rta_rows.append(
            {
                "M_over_Msun": m,
                "r_ta_m": r,
                "r_ta_Mpc": r / MPC,
                "M_crit_historical_form_Msun": (
                    LAMBDA_SI * C_LIGHT ** 2 * r ** 3 / (3.0 * GM_SUN)
                ),  # round-trip of M = Lambda c^2 r^3/(3G): must reproduce M
            }
        )
    out["C_max_turnaround_radius"] = {
        "formula": "r_ta = (3 G M / (Lambda c^2))^(1/3)",
        "reference": "Pavlidou & Tomaras, arXiv:1310.1920 (verified 2026-09-18)",
        "Lambda_m^-2": LAMBDA_SI,
        "rows": rta_rows,
    }

    # ---- (D) what the historical "M_crit" criterion actually reduces to ------
    # Applying M_encl > Lambda c^2 r^3/(3G) to a homogeneous sphere,
    # M_encl = (4 pi/3) rho_m r^3, cancels r^3 entirely and leaves
    #   rho_m > Lambda c^2/(4 pi G) = 2 rho_Lambda,  i.e.  Om (1+z)^3 > 2 OL,
    # which is exactly the condition for cosmic DECELERATION (addot < 0),
    # not for recollapse.
    rho_lambda_over_rho_crit0 = OMEGA_L_PLANCK
    one_plus_z_acc = (2.0 * OMEGA_L_PLANCK / OMEGA_M_PLANCK) ** (1.0 / 3.0)
    out["D_historical_Mcrit_reduces_to_deceleration"] = {
        "identity": "M_encl > Lambda c^2 r^3/(3G) with M_encl=(4pi/3) rho_m r^3  <=>  rho_m > 2 rho_Lambda",
        "deceleration_condition": "addot < 0  <=>  Omega_m (1+z)^3 > 2 Omega_Lambda",
        "Omega_m": OMEGA_M_PLANCK,
        "Omega_Lambda": rho_lambda_over_rho_crit0,
        "one_plus_z_acceleration_onset": one_plus_z_acc,
        "z_acceleration_onset": one_plus_z_acc - 1.0,
        "a_acceleration_onset": 1.0 / one_plus_z_acc,
        "note": (
            "the universe satisfied the historical M_crit inequality at every "
            "z above this value and still never recollapsed; the inequality is "
            "a statement about the sign of addot, not about the fate."
        ),
    }

    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "cosmic_fate_turnaround_2026_09_18.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)

    # ------------------------------------------------------------- printout ---
    print("=" * 74)
    print("COSMIC FATE / TURNAROUND NUMERICS  (W3, 2026-09-18)")
    print("=" * 74)
    print(f"H0 = {H0_KM_S_MPC} km/s/Mpc -> 1/H0 = {HUBBLE_TIME_GYR:.4f} Gyr")
    print(f"Omega_m = {OMEGA_M_PLANCK}, Omega_Lambda = {OMEGA_L_PLANCK} (flat)")
    print(f"Lambda  = {LAMBDA_SI:.6e} m^-2")
    print()
    print("(A0) observed flat LCDM: turnaround =", out["A0_observed_flat_LCDM"]["turnaround_scale_factor"])
    print("     E^2 at a = 1e6:", out["A0_observed_flat_LCDM"]["E2_at_a_1e6"])
    print()
    print("(A1) closed-LCDM recollapse boundary  Omega_Lambda_crit(Omega_m):")
    print("      Om      OL_crit      Ok(bdry)    4|Ok|^3-27Om^2*OL")
    for r in rows:
        olc = r["Omega_Lambda_crit"]
        if olc is None:
            print(f"   {r['Omega_m']:6.3f}      (none in bracket)")
        else:
            print(
                f"   {r['Omega_m']:6.3f}  {olc:11.6f}  {r['Omega_k_at_boundary']:10.6f}"
                f"   {r['analytic_discriminant_at_boundary']:.3e}"
            )
    print()
    print("(A2) spot checks at Omega_m = 0.31 (turnaround a, None = expands forever):")
    for r in out["A2_spot_checks_Om_0.31"]:
        print(f"   OL = {r['Omega_Lambda']:7.3f}  Ok = {r['Omega_k']:8.4f}  a_turn = {r['turnaround_a']}")
    print()
    a3 = out["A3_matter_required_to_recollapse_at_observed_Lambda"]
    print("(A3) with Omega_Lambda = 0.685 fixed, recollapse needs Omega_m >= "
          f"{a3['Omega_m_min_for_recollapse']:.4f}  "
          f"({a3['ratio_to_observed_Omega_m']:.2f}x the observed Omega_m)")
    print()
    print("(A4) analytic vs brute-force turnaround (all must agree):")
    for r in out["A4_analytic_vs_bruteforce"]:
        print(
            f"   Om={r['Omega_m']:5.3f} OL={r['Omega_Lambda']:6.3f}  analytic={r['analytic']}"
            f"  brute={r['brute_force']}  agree={r['agree']}"
        )
    print()
    print("(B) flat matter + NEGATIVE Lambda:")
    print("     |OL|    Om     a_turn   age_now   t_turn   now->turn   now->crunch  (Gyr)")
    for r in out["B_negative_Lambda_flat"]["rows"]:
        print(
            f"   {r['abs_Omega_Lambda']:6.3f} {r['Omega_m_required_for_flatness']:6.3f}"
            f" {r['a_turn_over_a0']:8.3f} {r['age_today_Gyr']:9.3f}"
            f" {r['time_of_turnaround_Gyr']:9.3f} {r['time_from_now_to_turnaround_Gyr']:10.3f}"
            f" {r['time_from_now_to_crunch_Gyr']:12.3f}"
            f"   [H/H0 check {r['check_H_over_H0_today']:.6f}]"
        )
    print()
    print("(C) maximum turnaround radius r_ta = (3GM/Lambda c^2)^(1/3):")
    for r in rta_rows:
        print(
            f"   M = {r['M_over_Msun']:.0e} Msun ->  r_ta = {r['r_ta_Mpc']:.4f} Mpc"
            f"   ({r['r_ta_m']:.4e} m)   [round-trip M = {r['M_crit_historical_form_Msun']:.4e} Msun]"
        )
    print()
    print("wrote", path)


if __name__ == "__main__":
    main()
