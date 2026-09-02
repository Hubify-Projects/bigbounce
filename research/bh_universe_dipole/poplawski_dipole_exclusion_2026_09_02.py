#!/usr/bin/env python3
"""
poplawski_dipole_exclusion_2026_09_02.py

Track C1 / P4' (Next-Science-Ledger item #5): confront the DESI Legacy DR8
chirality catalog's coverage-calibrated observed-label 95% sensitivity upper
limit, A_95^obs, against the amplitude(s) claimed or implied for a preferred
galaxy-spin axis in the literature that motivates Poplawski's rotating
black-hole-universe model (Einstein-Cartan torsion bounce).

This script does NOT re-run the DESI catalog pipeline. A_95^obs and its
defining sample size are read verbatim from the committed, reviewed P4 source
(pipelines/p2_chirality/chirality_catalog_paper.tex, Sec. "Coverage-calibrated
observed-label upper limit", Eq. eq:a95_obs): A_95^obs = 0.98% (full-amplitude,
observed-label), N_support = 887,472 (the strict release-safe HC real-space
support). The illustrative observed-to-physical bridge factor g = 0.398 is
also read verbatim from the same source and is explicitly NOT an established
transfer function (P4's own caveat, reproduced here).

What this script computes, deterministically, from those inputs plus
literature-reported amplitudes (each cited by arXiv id):

  1. A simple approximate 1/sqrt(N) sensitivity-floor scaling law, calibrated
     to the single committed anchor point (A_95^obs, N_support), used ONLY to
     show how much tighter a fixed-shape sensitivity floor would need to be
     to reach each literature sample's size -- NOT a re-derivation of any
     other paper's statistics, and NOT a claim that the floor shape transfers
     across different estimators/samples/pipelines.
  2. Whether each literature-claimed/observed amplitude exceeds A_95^obs
     (i.e., would have been detectable by the P4 estimator/null at >=95%
     coverage had it been present in the P4 sample), both at face value and
     after the illustrative g=0.398 bridge.
  3. A numbered-assumptions exclusion statement (also reproduced in the paper).

No optimization, no fitting, no randomness -- every output number is either a
literal input constant (cited) or a closed-form arithmetic function of inputs.
"""

import json
import math
from pathlib import Path

OUT_PATH = Path(__file__).resolve().parent / "outputs"
OUT_PATH.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_PATH / "poplawski_dipole_exclusion_2026_09_02.json"

# --- Anchor: committed, reviewed P4 result (verbatim, not re-derived here) ---
A95_OBS = 0.0098  # full-amplitude, observed-label; P4 Eq. eq:a95_obs
N_SUPPORT = 887_472  # strict release-safe HC real-space support, P4 Sec. "Data"
A_DIP_OBSERVED = 0.00467  # observed HC real-space dipole amplitude, P4 abstract/body (A_dip=0.467%)
G_BRIDGE_ILLUSTRATIVE = 0.398  # P4's own illustrative observed->physical bridge; NOT established

# Approximate sensitivity-floor scaling constant, calibrated to the single
# committed anchor (A_95^obs, N_support) under a 1/sqrt(N) ansatz. This is a
# bookkeeping device to compare "what sensitivity would a same-shaped floor
# have at a different N", not a claim about any other paper's actual floor.
C_SENSITIVITY = A95_OBS * math.sqrt(N_SUPPORT)


def sensitivity_floor_at_n(n):
    """Illustrative 1/sqrt(N) sensitivity floor, calibrated to the P4 anchor."""
    return C_SENSITIVITY / math.sqrt(n)


# --- Literature amplitudes that motivate the black-hole-universe test ---
# Each entry: the number(s) actually reported in the cited source, the
# sample size the claim was measured on (for the illustrative scaling only),
# and whether it is a "physical" claim (spin-axis handedness fraction) or an
# "observed-label" claim (classifier/algorithm-labelled fraction, same
# category as A_95^obs).
LITERATURE_CLAIMS = [
    {
        "id": "longo2011",
        "citation": "Longo 2011, arXiv:1104.2815 (Phys. Lett. B; SDSS z<0.085, 15158 spirals)",
        "amplitude_frac": 0.07,
        "amplitude_note": "~7% left-handed excess / dipole reported at ~5 sigma",
        "n_claim": 15158,
        "label_type": "physical (visual/algorithmic handedness classification)",
    },
    {
        "id": "shamir2012",
        "citation": "Shamir 2012 (SDSS, ~1.27e5 galaxies)",
        "amplitude_frac_low": 0.05,
        "amplitude_frac_high": 0.20,
        "amplitude_note": "2-4 sigma dipole, per-bin asymmetry ~5-20% (as reported)",
        "n_claim": 127000,
        "label_type": "algorithmic (Ganalyzer)",
    },
    {
        "id": "shamir2020",
        "citation": "Shamir 2020 (SDSS + Pan-STARRS)",
        "amplitude_frac_low": 0.02,
        "amplitude_frac_high": 0.04,
        "amplitude_note": "~2-4% asymmetry reported",
        "n_claim": 200000,
        "label_type": "algorithmic (Ganalyzer)",
    },
    {
        "id": "shamir2022desi",
        "citation": "Shamir 2022, arXiv:2208.13866 (DESI Legacy, ~1.3e6 spirals)",
        "amplitude_frac_low": 0.02,
        "amplitude_frac_high": 0.04,
        "amplitude_note": "~2-4% amplitude reported on a DESI Legacy sample",
        "n_claim": 1300000,
        "label_type": "algorithmic (Ganalyzer)",
    },
    {
        "id": "shamir2025_jwst_jades",
        "citation": "Shamir 2025, MNRAS 538, 76; arXiv:2502.18781 (JWST JADES, 263 galaxies)",
        "amplitude_frac_low": 0.20,
        "amplitude_frac_high": 0.33,
        "amplitude_note": "~2:1 to 1.5:1 CW:CCW imbalance reported (small-N, high-z)",
        "n_claim": 263,
        "label_type": "algorithmic/visual",
    },
]


def evaluate_claim(entry):
    lo = entry.get("amplitude_frac", entry.get("amplitude_frac_low"))
    hi = entry.get("amplitude_frac", entry.get("amplitude_frac_high"))
    n_claim = entry["n_claim"]
    floor_at_n_claim = sensitivity_floor_at_n(n_claim)
    result = {
        "id": entry["id"],
        "citation": entry["citation"],
        "amplitude_note": entry["amplitude_note"],
        "label_type": entry["label_type"],
        "n_claim": n_claim,
        "amplitude_frac_low": lo,
        "amplitude_frac_high": hi,
        "exceeds_A95_obs_face_value": bool(lo > A95_OBS),
        "exceeds_A95_obs_after_g_bridge": bool(lo * G_BRIDGE_ILLUSTRATIVE > A95_OBS),
        "illustrative_sensitivity_floor_at_this_N": floor_at_n_claim,
        "ratio_claim_low_to_A95_obs": lo / A95_OBS,
    }
    return result


def main():
    claim_results = [evaluate_claim(e) for e in LITERATURE_CLAIMS]

    model_section = {
        "model": "Poplawski rotating black-hole-universe (Einstein-Cartan torsion bounce)",
        "mechanism_refs": [
            "Poplawski, arXiv:1007.0587 (torsion avoids the singularity; spin-torsion coupling)",
            "Poplawski, arXiv:1111.4595 (nonsingular, cyclic universes from torsion)",
            "Poplawski, arXiv:1410.3881 = ApJ 832, 96 (2016), 'Universe in a black hole "
            "in Einstein-Cartan gravity' (the bounce mechanism itself)",
            "Poplawski, arXiv:1910.10819, 'Universe in a rotating black hole and preferred axis'",
        ],
        "quantitative_amplitude_predicted": False,
        "finding": (
            "arXiv:1910.10819 states only that 'galaxies tend to align their axes of "
            "rotation with the preferred axis, resulting in clockwise-counterclockwise "
            "asymmetry' -- a qualitative alignment tendency with a stated preferred-axis "
            "direction (inherited from the parent black hole's spin axis), not a derived "
            "dipole amplitude, alignment fraction, or timescale. The mechanism papers "
            "(1007.0587, 1111.4595, 1410.3881) supply the torsion-repulsion bounce itself "
            "but likewise contain no galaxy-spin observable. No Poplawski paper we could "
            "locate gives a closed-form or numerically evaluated amplitude for the "
            "preferred-axis dipole."
        ),
        "assumption_needed_for_quantitative_amplitude": (
            "An alignment efficiency parameter (call it eta, 0<=eta<=1: the fraction of "
            "galaxies whose spin axis relaxes toward the preferred axis within a Hubble "
            "time under the small non-inertial forces from Poplawski 1910.10819) is not "
            "computed in the cited literature. Under the simplest toy closure -- an "
            "observed dipole amplitude equal to eta itself -- the model becomes "
            "quantitatively testable and eta is exactly what A_95^obs bounds (see below)."
        ),
    }

    exclusion_statement = {
        "target": "A_95^obs = 0.98% (full-amplitude, observed-label; P4 Eq. eq:a95_obs, "
        "N_support=887472)",
        "observed_dipole": A_DIP_OBSERVED,
        "statement": (
            "Under the toy closure above (observed dipole amplitude == alignment "
            "efficiency eta), the DESI Legacy DR8 catalog's coverage-calibrated "
            "observed-label sensitivity excludes eta > 0.98% at >=95% coverage on the "
            "primary HC real-space channel -- i.e. any preferred-axis alignment "
            "mechanism that would produce an observed-label dipole above ~1% on this "
            "sample is disfavored, while the model's own literature motivation "
            "(Longo 2011 ~7%; Shamir 2012/2020/2022 ~2-20%; Shamir 2025 JWST/JADES "
            "~20-33%, N=263) sits 2-30x above that floor."
        ),
        "numbered_assumptions": [
            "1. The toy closure 'observed amplitude = alignment efficiency eta' is "
            "adopted for lack of any quantitative prediction in the cited Poplawski "
            "papers; a real closure would require a computed relaxation timescale "
            "and torque strength, which do not exist in the literature we could find.",
            "2. A_95^obs is an OBSERVED-LABEL sensitivity floor (classifier-labelled "
            "chirality, not deprojected physical spin), exactly as defined in P4; it is "
            "NOT a physical parity-amplitude bound. The observed-to-physical bridge "
            "requires the spatially resolved morphology transfer function, which "
            "remains an open gate in P4 (the scalar g=0.398 used below is illustrative "
            "only, not an established calibration).",
            "3. The preferred axis itself is a free direction in the model (inherited "
            "from an unobserved parent black hole's spin); this analysis follows P4/P5 "
            "in testing amplitude only (a full-sky real-space dipole fit and, "
            "separately, a DESIVAST void/non-void environment contrast), not a "
            "axis-matched search against a specific predicted direction.",
            "4. Sample-size sensitivity-floor scaling in this script uses a simple "
            "1/sqrt(N) ansatz calibrated to the single P4 anchor point; it is a "
            "bookkeeping illustration of statistical reach, not a re-derivation of any "
            "other paper's actual estimator or null.",
            "5. Literature amplitude ranges (Longo, Shamir 2012/2020/2022/2025) are "
            "reported as published; no re-analysis of those papers' pipelines is "
            "performed here (cross-references only, as in P4 Sec. comparison-to-Shamir "
            "and P5 Sec. Comparison-to-Shamir-2022).",
        ],
        "illustrative_g_bridge_used": G_BRIDGE_ILLUSTRATIVE,
        "A_95_obs_after_g_bridge_illustrative_only": A95_OBS / G_BRIDGE_ILLUSTRATIVE,
    }

    out = {
        "script": "poplawski_dipole_exclusion_2026_09_02.py",
        "generated_for": "P4' (Track C1, Next-Science-Ledger item #5)",
        "inputs": {
            "A_95_obs": A95_OBS,
            "N_support": N_SUPPORT,
            "A_dip_observed": A_DIP_OBSERVED,
            "g_bridge_illustrative": G_BRIDGE_ILLUSTRATIVE,
            "source": "pipelines/p2_chirality/chirality_catalog_paper.tex "
            "(v1.0.274), Sec. Coverage-calibrated observed-label upper limit, "
            "Eq. eq:a95_obs; abstract (A_dip=0.467%); Sec. parity translation (g=0.398)",
        },
        "sensitivity_floor_calibration_constant_C": C_SENSITIVITY,
        "model": model_section,
        "literature_claims_vs_A95_obs": claim_results,
        "exclusion_statement": exclusion_statement,
    }

    OUT_FILE.write_text(json.dumps(out, indent=2, sort_keys=False) + "\n")
    print(f"wrote {OUT_FILE}")
    print(json.dumps(exclusion_statement["statement"], indent=2))


if __name__ == "__main__":
    main()
