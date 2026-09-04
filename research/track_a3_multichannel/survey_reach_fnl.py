"""
Track A3 channel 3 — reach of the matter-bounce f_NL^local = -35/16 = -2.1875
against current and forecast large-scale-structure constraints.

Every sigma below is either QUOTED VERBATIM from a published abstract (label
"cited") or DERIVED here by simple arithmetic from such a number (label
"derived").  Nothing is invented.  Where a survey has no published
sigma(f_NL^local) we say so and do not manufacture one.

Sources (all verified against the arXiv abstracts on 2026-09-02):
 - Heinrich, Dore & Krause 2023, arXiv:2311.13082 (SPHEREx multi-tracer
   redshift-space bispectrum): "Our fiducial result of sigma_fNL = 0.7 from
   bispectrum alone"; "the final SPHEREx capability ... is still on target for
   being sigma_fNL = 0.5 once the power spectrum will be included."
 - Dore et al. 2014, arXiv:1412.4872 — the SPHEREx mission paper (mission and
   survey definition; the abstract does not itself quote a sigma(f_NL)).
 - Ferraro et al. 2019, arXiv:1903.09208 (Astro2020 science white paper,
   MegaMapper-class z>2 spectroscopy): "crossing the crucial theoretical
   threshold of sigma(f_NL^local) of order unity".  NO tighter number is
   quoted in that abstract; we therefore do NOT assert 0.1-0.3 for
   MegaMapper.  Rows below sigma = 1 are labelled ILLUSTRATIVE.
 - Sailer et al. 2021, arXiv:2106.09713 (FishLSS): the Fisher framework in
   which high-z spectroscopic / 21-cm PNG forecasts are computed.
 - Chaussidon et al. 2024, arXiv:2411.17623 (DESI DR1 LRG+QSO):
   f_NL^loc = -3.6 (+9.0/-9.1) at 68% (merger-model QSO bias), and
   f_NL^loc = +3.5 (+10.7/-7.4) at 68% assuming universality for the QSO bias.

Template projection: the matter-bounce bispectrum is not exactly the local
shape.  This lab's P2 forecast adopts a noise-weighted shape overlap
r = 0.84 between the bounce shape and the local template, so an experiment
quoting sigma_local constrains the bounce amplitude at sigma_bounce =
sigma_local / r, i.e. significance = |f_NL^bounce| * r / sigma_local.
Both the bare and the r-projected significance are tabulated.

Output: outputs/survey_reach_fnl.json    Venue: local, no GPU, cost $0.
"""
from __future__ import annotations
import json, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs/survey_reach_fnl.json"

FNL_BOUNCE_LI = -35.0 / 16.0     # -2.1875, this lab's adopted value
FNL_BOUNCE_CAI = -35.0 / 8.0     # -4.375, Cai et al. 2009 printed value
R_OVERLAP = 0.84                 # P2 noise-weighted bounce-vs-local shape overlap

ROWS = [
    dict(survey="SPHEREx (bispectrum only, fiducial)", sigma=0.7,
         status="cited", source="Heinrich, Dore & Krause 2023, arXiv:2311.13082 (abstract)"),
    dict(survey="SPHEREx (target, P + B combined)", sigma=0.5,
         status="cited", source="Heinrich, Dore & Krause 2023, arXiv:2311.13082 (abstract)"),
    dict(survey="MegaMapper-class z>2 spectroscopy", sigma=1.0,
         status="cited", source="Ferraro et al. 2019, arXiv:1903.09208 (abstract: "
                                "'sigma(f_NL^local) of order unity')"),
    dict(survey="Illustrative next-generation floor", sigma=0.3,
         status="ILLUSTRATIVE — not a published forecast", source="none"),
    dict(survey="Illustrative cosmic-variance-limited floor", sigma=0.1,
         status="ILLUSTRATIVE — not a published forecast", source="none"),
]

CURRENT = [
    dict(measurement="DESI DR1 LRG+QSO (merger-model QSO bias)",
         central=-3.6, err_plus=9.0, err_minus=9.1,
         source="Chaussidon et al. 2024, arXiv:2411.17623 (abstract)"),
    dict(measurement="DESI DR1 LRG+QSO (universality QSO bias)",
         central=3.5, err_plus=10.7, err_minus=7.4,
         source="Chaussidon et al. 2024, arXiv:2411.17623 (abstract)"),
]


def main():
    t0 = time.time()
    forecast = []
    for r in ROWS:
        s = r["sigma"]
        forecast.append({**r,
            "significance_bare_-35/16": abs(FNL_BOUNCE_LI) / s,
            "significance_projected_r0.84_-35/16": abs(FNL_BOUNCE_LI) * R_OVERLAP / s,
            "significance_bare_-35/8": abs(FNL_BOUNCE_CAI) / s,
            "significance_projected_r0.84_-35/8": abs(FNL_BOUNCE_CAI) * R_OVERLAP / s,
            "derivation": "significance = |f_NL| (x r) / sigma"})

    current = []
    for c in CURRENT:
        # one-sided error on the side facing the bounce prediction (negative)
        sig_side = c["err_minus"] if FNL_BOUNCE_LI < c["central"] else c["err_plus"]
        current.append({**c,
            "sigma_symmetrised": 0.5 * (c["err_plus"] + c["err_minus"]),
            "tension_with_-35/16_sigma": abs(FNL_BOUNCE_LI - c["central"]) / sig_side,
            "tension_with_-35/8_sigma": abs(FNL_BOUNCE_CAI - c["central"]) / (
                c["err_minus"] if FNL_BOUNCE_CAI < c["central"] else c["err_plus"]),
            "discriminating_power_absfNL_over_sigma_-35/16":
                abs(FNL_BOUNCE_LI) / (0.5 * (c["err_plus"] + c["err_minus"])),
            "derivation": "tension = |f_NL_pred - central| / (1-sigma error on that side)"})

    # --- R3 C1(a): transmitted-amplitude f_NL^after rows ---------------------
    # T (linear handoff fraction) and rho_B read from the committed lane-B
    # numerical results (research/cubic_bounce_transmission/lane_b_numerical/
    # results.json); Delta f_NL^bounce[S1] = -(5/24) rho_B (Eq. bounce_cubic,
    # confirmed there to 3e-4 against the independent finite-k numerical
    # in-in evaluation).
    LANE_B_JSON = (HERE / "../cubic_bounce_transmission/lane_b_numerical/results.json").resolve()
    lane_b = json.loads(LANE_B_JSON.read_text())
    BACKGROUNDS = [
        ("quintin", "Quintin-type"),
        ("lqc", "LQC effective dust"),
        ("poly", "poly (analytic non-LQC)"),
    ]
    SIGMAS = [0.7, 0.5, 1.0]  # SPHEREx bispectrum-only, SPHEREx P+B target, MegaMapper
    after_rows = []
    for key, label in BACKGROUNDS:
        bg = lane_b["backgrounds"][key]
        T = bg["T_fNL_linear"]
        rho_B = bg["rho_B"]
        delta_bounce = -(5.0 / 24.0) * rho_B
        for fnl_label, fnl_pre in (("-35/16", FNL_BOUNCE_LI), ("-35/8", FNL_BOUNCE_CAI)):
            fnl_after = T * fnl_pre + delta_bounce
            row = {
                "background": label,
                "T_fNL": T,
                "rho_B": rho_B,
                "delta_fNL_bounce_S1": delta_bounce,
                "f_NL_pre": fnl_label,
                "f_NL_after": fnl_after,
            }
            for s in SIGMAS:
                row[f"bare_significance_sigma{s}"] = abs(fnl_after) / s
            after_rows.append(row)

    # --- ledger row 9 / D-A3-9: scheme-S2 rows (raw ADM, exact modes) --------
    # f_NL_before/after read verbatim from the committed lane9b2 results.json
    # (research/cubic_bounce_transmission/lane9b2_s2_rawadm/). S2 has been
    # carried through cubic order only on the Quintin-type background; no
    # T_S2/Delta_S2 decomposition robust to the window-evaluation convention
    # exists (LANE9B2 Sec.4, "window scan"), so the -35/8 row is NOT computed
    # by scaling -- it is reported absent rather than invented.
    LANE_9B2_JSON = (HERE / "../cubic_bounce_transmission/lane9b2_s2_rawadm/results.json").resolve()
    lane_9b2 = json.loads(LANE_9B2_JSON.read_text())
    s2_rows = []
    for k_key, k_data in lane_9b2["S2"]["k_scan"].items():
        fnl_after_s2 = k_data["f_NL_after"]
        row = {
            "background": "Quintin-type (only background evaluated in S2)",
            "scheme": "S2 (effective-fluid, raw ADM cubic Lagrangian, exact modes)",
            "k_eta_B": float(k_key),
            "f_NL_before": k_data["f_NL_before"],
            "f_NL_after_-35/16": fnl_after_s2,
            "linear_transmission_abs_lambda_zeta": k_data["linear_transmission_abs"],
            "f_NL_after_-35/8": None,
            "-35/8_status": "NOT COMPUTED: no scheme-independent (window-convention-free) "
                            "T_S2/Delta_S2 decomposition exists to scale from -35/16 without "
                            "re-running the raw-ADM in-in integral with the Cai normalization "
                            "(LANE9B2_S2_RAWADM_2026-09-04.md Sec.4).",
        }
        for s in SIGMAS:
            row[f"bare_significance_sigma{s}_-35/16"] = abs(fnl_after_s2) / s
        s2_rows.append(row)

    out = {
        "task": "Track A3 channel 3 — survey reach for f_NL^local = -35/16",
        "f_NL_matter_bounce_Li_-35/16": FNL_BOUNCE_LI,
        "f_NL_matter_bounce_Cai_-35/8": FNL_BOUNCE_CAI,
        "bounce_to_local_template_overlap_r": R_OVERLAP,
        "r_source": "this lab's P2 forecast (noise-weighted shape overlap); "
                    "research/focused_paper_source_integration/02_full_draft.tex",
        "forecast_reach": forecast,
        "current_constraints": current,
        "transmitted_reach_after_bounce_R3_C1a": {
            "note": "R3 closure C1(a): the kappa*eta_B <~ 1e-2 window is an upper "
                    "bound on k, satisfied most easily at the LSS/CMB pivot, so "
                    "f_NL^after = T*f_NL^pre + Delta_f_NL^bounce[S1] is the "
                    "paper's observable prediction for every channel.",
            "T_and_rho_B_source": str(LANE_B_JSON),
            "rows": after_rows,
        },
        "transmitted_reach_S2_scheme_ledger_row9_D_A3_9": {
            "note": "Science decision D-A3-9 (project-context/PAPER_LINEAGE_2026-08-05.md "
                    "2026-09-04 entry): the S2 'divergence' quoted in earlier versions is a "
                    "total-derivative artefact of the Maldacena/Chen integrated-by-parts form; "
                    "on the raw ADM cubic Lagrangian with exact S2 modes the bounce-window "
                    "integral is finite (lane9b/lane9b2). Reported as a two-scheme band "
                    "alongside S1, not a replacement for it.",
            "source": str(LANE_9B2_JSON),
            "rows": s2_rows,
        },
        "notes": [
            "MegaMapper is a proposed, unapproved facility. Consistent with this "
            "lab's P2 policy we quote it as an outlook at the published "
            "order-unity level only, and do not transfer any systematic budget "
            "or headline a significance for it.",
            "The two illustrative rows (sigma = 0.3, 0.1) are NOT published "
            "forecasts and must never be quoted as such.",
            "DESI DR1 currently has essentially no discriminating power on a "
            "|f_NL| ~ 2 signal: |f_NL|/sigma < 0.3.",
        ],
        "wall_seconds": round(time.time() - t0, 3),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2))
    for f in forecast:
        print(f"{f['survey']:<45s} sigma={f['sigma']:<5} "
              f"bare={f['significance_bare_-35/16']:.2f}s  "
              f"proj={f['significance_projected_r0.84_-35/16']:.2f}s  [{f['status']}]")
    print()
    for c in current:
        print(f"{c['measurement']:<45s} tension(-35/16)={c['tension_with_-35/16_sigma']:.2f}s "
              f"tension(-35/8)={c['tension_with_-35/8_sigma']:.2f}s "
              f"power={c['discriminating_power_absfNL_over_sigma_-35/16']:.2f}")


if __name__ == "__main__":
    main()
