#!/usr/bin/env python3
"""R10 (A3M v3M.0.26): put every (r, f_NL) window number on a STATED criterion.

The R10 confirmation board found that the Lambda-scan "best case (DBI) r_min = 12.6"
was computed under |f_NL^after| <= 5.1 (Planck 1-sigma) on the Quintin-type
background alone, while the adjacent Table VII numbers use the asymmetric Planck
95% upper edge (9.3) and 68% upper edge (4.2) with ranges over three backgrounds.
The two criteria happened to collide near 12.6, concealing the mismatch.

This script recomputes the Lambda lines on the SAME criteria and the SAME three
backgrounds as Table VII, from the paper's own equations:

  f_NL^pre(c_s, Lambda) = -245/16 + 105/(8 c_s^2) - 30 Lambda           [Eq. (15)]
  Delta f_NL^bounce(c_s) = -(5/24) rho_B (6 c_s^2 - 5)/c_s^4            [Eq. (17)]
  f_NL^after = T_fNL f_NL^pre + Delta f_NL^bounce,  rho_B = 1 - 2 T_fNL
  r = 24 c_s                                                            [Eq. (14)]

T_fNL per background is Table III: Quintin-type 0.165, LQC 0.250, poly 0.196.
No new physics: only the criterion and the background set are made explicit.
"""
import json, pathlib
import numpy as np

T_FNL = {"quintin": 0.165, "lqc": 0.250, "poly": 0.196}
R_CMB = 0.036                      # BICEP/Keck 2021 bound on r
CRITERIA = {"planck_95_upper": 9.3, "planck_68_upper": 4.2, "planck_1sigma": 5.1}
LINES = {
    "DBI": ("Lambda = (1-c_s^2)/(2 c_s^2)", lambda cs: (1 - cs ** 2) / (2 * cs ** 2)),
    "P_propto_X_n": ("Lambda = (1-c_s^2)/(6 c_s^2)  [Li+2016 Eq. (A.20)]",
                     lambda cs: (1 - cs ** 2) / (6 * cs ** 2)),
    "Lambda_0": ("Lambda = 0", lambda cs: 0.0 * cs),
}


def f_pre(cs, L):
    return -245.0 / 16.0 + 105.0 / (8.0 * cs ** 2) - 30.0 * L


def f_after(cs, L, T):
    rho_B = 1.0 - 2.0 * T
    return T * f_pre(cs, L) - (5.0 / 24.0) * rho_B * (6.0 * cs ** 2 - 5.0) / cs ** 4


cs = np.geomspace(1e-4, 1.0, 400001)
out = {"task": "A3M R10: (r, f_NL) window minima with an explicit criterion",
       "equations": {"f_pre": "-245/16 + 105/(8 cs^2) - 30 Lambda",
                     "d_f_bounce": "-(5/24) rho_B (6 cs^2 - 5)/cs^4",
                     "r_of_cs": "24 cs"},
       "T_fNL_per_background_TableIII": T_FNL,
       "criteria": CRITERIA, "results": {}}

for cname, cval in CRITERIA.items():
    out["results"][cname] = {}
    for lname, (ldesc, lfun) in LINES.items():
        per_bg = {}
        for bg, T in T_FNL.items():
            ok = np.abs(f_after(cs, lfun(cs), T)) <= cval
            if ok.any():
                cmin = float(cs[ok].min())
                per_bg[bg] = {"c_s_min": cmin, "r_min": 24.0 * cmin,
                              "r_min_over_BK18": 24.0 * cmin / R_CMB}
            else:
                per_bg[bg] = None
        viable = {k: v for k, v in per_bg.items() if v}
        best = min(viable, key=lambda k: viable[k]["r_min"]) if viable else None
        out["results"][cname][lname] = {
            "line": ldesc, "per_background": per_bg,
            "best_background": best,
            "r_min_overall": viable[best]["r_min"] if best else None,
        }

best95 = out["results"]["planck_95_upper"]
lo = min((v for v in best95.values() if v["r_min_overall"]), key=lambda v: v["r_min_overall"])
out["headline"] = {
    "criterion": "Planck 95% upper edge |f_NL^after| <= 9.3, three backgrounds",
    "best_line": lo["line"], "best_background": lo["best_background"],
    "r_min": lo["r_min_overall"], "r_min_over_BK18": lo["r_min_overall"] / R_CMB,
}
p = pathlib.Path(__file__).resolve().parent / "results.json"
p.write_text(json.dumps(out, indent=2) + "\n")
for cname in CRITERIA:
    for lname, rec in out["results"][cname].items():
        r = rec["r_min_overall"]
        print(f"{cname:16s} {lname:13s} best={rec['best_background']:8s} "
              f"r_min={r:.3f} ({r/R_CMB:.0f}x BK18)")
print("\nheadline:", json.dumps(out["headline"]))
print("wrote", p)
