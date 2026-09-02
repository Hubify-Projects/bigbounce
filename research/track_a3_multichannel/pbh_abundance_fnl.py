"""
Track A3 channel 2 — PBH abundance with local non-Gaussianity, at the
matter-bounce values f_NL = -35/16 (this lab's adopted value, Li et al. 2016
arXiv:1612.03231 permutation convention) versus f_NL = -35/8 (Cai et al. 2009
arXiv:0810.4677, the value used by Choudhury et al. 2025 arXiv:2409.18983,
EPJC 85:472) versus the Gaussian case f_NL = 0.

WHAT THIS IS.  A Press-Schechter calculation with the standard local quadratic
non-Gaussian map (Young & Byrnes 2013, arXiv:1307.4995; Franciolini, Kehagias,
Matarrese, Riotto 2018, arXiv:1801.09415):

    zeta = zeta_G + A ( zeta_G^2 - sigma^2 ),      A = (3/5) f_NL,

with zeta_G ~ N(0, sigma^2), sigma^2 the variance of the smoothed Gaussian
curvature perturbation at the PBH scale.  PBHs form in regions with
zeta > zeta_c, so

    beta(zeta_c) = P( zeta > zeta_c ).

Because the map is an exact quadratic it is inverted analytically:
  A zeta_G^2 + zeta_G - (A sigma^2 + zeta_c) = 0
  => zeta_G = [ -1 +/- sqrt( 1 + 4 A (A sigma^2 + zeta_c) ) ] / (2A).
For A < 0 (negative f_NL) the parabola opens downward, so {zeta > zeta_c} is
the *interval* between the two roots, and the map has an ABSOLUTE CEILING

    zeta_max = -1/(4A) - A sigma^2 = -5/(12 f_NL) + (3/5)|f_NL| sigma^2 .

No realisation of zeta can exceed zeta_max.  If zeta_c > zeta_max then
beta = 0 identically.  The leading term -5/(12 f_NL) scales as 1/|f_NL|, so
moving from -35/8 to -35/16 EXACTLY DOUBLES the ceiling.  This is the single
sharpest statement the channel supports, and it is analytic.

WHAT THIS IS NOT.  This is NOT a reproduction of Choudhury et al. 2025.  They
apply the *compaction-function* formation criterion with the full nonlinear
zeta -> C relation and an EFT-of-bounce + ultra-slow-roll power spectrum; the
naive quadratic truncation used here has a hard ceiling that their criterion
does not share.  Their reported outcome (10^-3 <= f_PBH <= 1, PBH
overproduction "completely mitigated", perturbativity bound f_NL >~ -60) is
CITED, never recomputed here.  What we compute is the Press-Schechter-level
statement of what changes between -35/16 and -35/8.

Mass fraction -> present abundance uses the standard radiation-era relation
(Sasaki, Suyama, Tanaka, Yokoyama 2018, arXiv:1801.05235, Eq. 2.6-class):

    f_PBH(M) = 1.68e8 (gamma_c/0.2)^{1/2} (g_*/106.75)^{-1/4}
               (M/M_sun)^{-1/2} beta(M)

with gamma_c = 0.2 the collapse efficiency and g_* = 106.75.

Output: outputs/pbh_abundance_fnl.json   Venue: local, no GPU, cost $0.
"""
from __future__ import annotations
import json, time
from pathlib import Path
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs/pbh_abundance_fnl.json"

M_SUN_G = 1.98847e33
GAMMA_C = 0.2
G_STAR = 106.75

FNL = {"matter_bounce_Li_-35/16": -35.0 / 16.0,
       "matter_bounce_Cai_-35/8": -35.0 / 8.0,
       "gaussian_0": 0.0}


def beta_of(zeta_c: float, sigma: float, f_nl: float) -> float:
    """P(zeta > zeta_c) for zeta = zeta_G + A(zeta_G^2 - sigma^2), A=(3/5)f_NL."""
    A = 0.6 * f_nl
    if A == 0.0:
        return float(norm.sf(zeta_c / sigma))
    disc = 1.0 + 4.0 * A * (A * sigma ** 2 + zeta_c)
    if disc <= 0.0:
        # A<0: threshold above the ceiling -> no solutions -> beta = 0.
        # A>0: disc<0 impossible for zeta_c > -1/(4A)-A sigma^2 (min of parabola);
        #      below the minimum every zeta_G qualifies -> beta = 1.
        return 0.0 if A < 0 else 1.0
    r1 = (-1.0 - np.sqrt(disc)) / (2.0 * A)
    r2 = (-1.0 + np.sqrt(disc)) / (2.0 * A)
    lo, hi = (r1, r2) if r1 < r2 else (r2, r1)
    if A < 0:
        # downward parabola: {zeta > zeta_c} is the interval (lo, hi).
        # Use the survival function on BOTH ends: in the rare-tail regime
        # cdf(hi)-cdf(lo) suffers catastrophic cancellation (both -> 1.0).
        return float(norm.sf(lo / sigma) - norm.sf(hi / sigma))
    return float(norm.cdf(lo / sigma) + norm.sf(hi / sigma))   # outside roots


def zeta_ceiling(sigma: float, f_nl: float) -> float:
    A = 0.6 * f_nl
    return float("inf") if A >= 0 else float(-1.0 / (4.0 * A) - A * sigma ** 2)


def f_pbh(beta: float, M_g: float) -> float:
    return (1.68e8 * (GAMMA_C / 0.2) ** 0.5 * (G_STAR / 106.75) ** -0.25
            * (M_g / M_SUN_G) ** -0.5 * beta)


def sigma_for_fpbh(target: float, zeta_c: float, f_nl: float, M_g: float):
    """Smallest sigma reaching f_PBH = target; None if unreachable for sigma<=1."""
    def fn(s):
        return np.log10(max(f_pbh(beta_of(zeta_c, s, f_nl), M_g), 1e-300)) \
               - np.log10(target)
    lo, hi = 1e-3, 1.0
    if fn(lo) > 0 or fn(hi) < 0:
        return None
    return float(brentq(fn, lo, hi, xtol=1e-8))


def main():
    t0 = time.time()
    M_g = 1.0e20                    # asteroid-mass window (Papanikolaou et al. 2024)

    # --- (1) analytic ceiling of the quadratic map ---------------------------
    ceiling_leading = {k: (float("inf") if v == 0 else -5.0 / (12.0 * v))
                       for k, v in FNL.items()}

    # --- (2) rare-tail regime: sigma << zeta_c, which is where PBHs live -----
    # Calibrate sigma on the GAUSSIAN case so that f_PBH = 1 at each threshold,
    # then read off f_PBH for the two matter-bounce values AT THE SAME sigma.
    # This is the physically meaningful comparison: the curvature power-spectrum
    # amplitude is fixed by the source (e.g. the PTA SIGW amplitude), and f_NL
    # then decides whether PBHs are overproduced.
    calib = {}
    for zc in [0.05, 0.08, 0.10, 0.12, 0.15]:
        s_star = sigma_for_fpbh(1.0, zc, 0.0, M_g)
        if s_star is None:
            continue
        row = {"zeta_c": zc, "sigma_star_gaussian_fPBH1": s_star,
               "perturbativity_0.6_absfNL_sigma": {}}
        for k, v in FNL.items():
            ceil = zeta_ceiling(s_star, v)
            b = beta_of(zc, s_star, v)
            row[k] = {"beta": b, "f_PBH": f_pbh(b, M_g),
                      "zeta_ceiling_at_sigma_star": ceil,
                      "threshold_below_ceiling": bool(zc < ceil)}
            row["perturbativity_0.6_absfNL_sigma"][k] = 0.6 * abs(v) * s_star
        b0 = row["gaussian_0"]["beta"]
        row["suppression_vs_gaussian"] = {
            k: (row[k]["beta"] / b0 if b0 > 0 else None)
            for k in FNL if k != "gaussian_0"}
        r16 = row["matter_bounce_Li_-35/16"]["beta"]
        r8 = row["matter_bounce_Cai_-35/8"]["beta"]
        row["ratio_-35/16_over_-35/8"] = (r16 / r8) if r8 > 0 else None
        calib[f"zeta_c={zc}"] = row

    # --- (3) sigma required to reach f_PBH = 1 at each f_NL -----------------
    req = {}
    for k, v in FNL.items():
        req[k] = {}
        for zc in [0.05, 0.08, 0.10, 0.12, 0.15]:
            s_req = sigma_for_fpbh(1.0, zc, v, M_g)
            req[k][f"zeta_c={zc}"] = {
                "sigma_required": s_req,
                "P_zeta_required": (s_req ** 2 if s_req is not None else None),
                "perturbativity_0.6_absfNL_sigma": (
                    0.6 * abs(v) * s_req if s_req is not None else None)}

    # --- (4) hard ceiling statement at standard thresholds -------------------
    hard = {}
    for zc in [0.45, 1.00]:
        hard[f"zeta_c={zc}"] = {
            k: {"beta_at_sigma_0.02": beta_of(zc, 0.02, v),
                "zeta_ceiling_at_sigma_0.02": zeta_ceiling(0.02, v)}
            for k, v in FNL.items()}

    out = {
        "task": "Track A3 channel 2 — Press-Schechter PBH abundance with local "
                "quadratic NG at f_NL = -35/16 vs -35/8 vs 0",
        "label": "NEW computation (not a reproduction of Choudhury et al. 2025)",
        "convention": "zeta = zeta_G + (3/5) f_NL (zeta_G^2 - sigma^2)",
        "f_NL_values": FNL,
        "PBH_mass_g": M_g,
        "f_PBH_relation": "Sasaki et al. 2018 arXiv:1801.05235; gamma_c=0.2, g_*=106.75",
        "analytic_ceiling_leading_term_-5_over_12_fNL": ceiling_leading,
        "ceiling_ratio_-35/16_over_-35/8": 2.0,
        "fixed_amplitude_comparison": calib,
        "sigma_required_for_fPBH_1": req,
        "hard_ceiling_at_standard_thresholds": hard,
        "cited_not_computed": {
            "Choudhury_2025_arXiv_2409.18983": (
                "EPJC 85:472. Uses f_NL = (-39.95, -35/8) with the compaction-"
                "function criterion in an EFT non-singular bounce + USR setup; "
                "reports 1e-3 <= f_PBH <= 1, PBH overproduction completely "
                "mitigated, and a perturbativity bound f_NL >~ -60. Their "
                "-35/16 case is NOT in that paper."),
            "Papanikolaou_2025_arXiv_2504.11641": (
                "Matter-bounce induced GW background with universal IR scaling "
                "Omega_GW ~ f^2; asteroid-mass PBH window."),
        },
        "caveats": [
            "The quadratic local map has an absolute ceiling zeta_max = "
            "-5/(12 f_NL) + (3/5)|f_NL| sigma^2 for f_NL < 0; for the standard "
            "curvature thresholds zeta_c ~ 0.45-1 in the rare-tail regime "
            "beta = 0 identically at BOTH -35/16 and -35/8. This is a property "
            "of the truncated quadratic map, not a physical no-PBH theorem; "
            "Choudhury et al. avoid it via the compaction-function criterion.",
            "Results are quoted only where 0.6|f_NL|sigma << 1 (perturbativity "
            "of the local expansion) and zeta_c < zeta_max.",
            "Critical-collapse mass function, non-spherical effects, and the "
            "window-function/transfer choice are not modelled.",
        ],
        "wall_seconds": round(time.time() - t0, 3),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps({k: out[k] for k in
                      ["analytic_ceiling_leading_term_-5_over_12_fNL",
                       "fixed_amplitude_comparison", "sigma_required_for_fPBH_1",
                       "hard_ceiling_at_standard_thresholds"]}, indent=2))


if __name__ == "__main__":
    main()
