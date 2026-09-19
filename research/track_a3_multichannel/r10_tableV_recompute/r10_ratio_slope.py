#!/usr/bin/env python3
"""R10 (A3M v3M.0.26): measure the amplitude-ratio trend the Table V caption quotes.

The caption previously said the ratio "decreases monotonically, with a slope of ~0.13 per
unit gamma_cr across the 255-point scan". Neither number was recorded in any artifact.
This script measures both trends directly from the committed 255-point scan
(row11_pbh_residuals/results/row11_gammacr_extension.json):

  * ordinary-least-squares slope of ratio vs gamma_cr, over all 255 points and over the
    144 points inside the model's own gamma_cr window [0.267, 0.630];
  * the C_th trend at fixed (family, Delta, r_p k_p), as the mean change in ratio per
    +0.1 in C_th;
  * the family composition of the 144-point in-window subset.
"""
import collections, json, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parents[0] / "row11_pbh_residuals" / "results" / "row11_gammacr_extension.json"
pts = json.loads(SRC.read_text())["points"]

g = np.array([p["gamma_cr"] for p in pts])
r = np.array([p["ratio_-35/16_over_-35/8"] for p in pts])
inwin = (g >= 0.267) & (g <= 0.630)

by = collections.defaultdict(dict)
for p in pts:
    by[(p["family"], p.get("Delta"), p["rp_kp"])][p["C_th"]] = p["ratio_-35/16_over_-35/8"]
steps = [(v[b] - v[a]) / ((b - a) / 0.1)
         for v in by.values() for a, b in zip(sorted(v), sorted(v)[1:])]

fam = collections.Counter(p["family"] for p in pts if 0.267 <= p["gamma_cr"] <= 0.630)
fam_stats = {}
for name in fam:
    vals = [p["ratio_-35/16_over_-35/8"] for p in pts
            if p["family"] == name and 0.267 <= p["gamma_cr"] <= 0.630]
    fam_stats[name] = {"n": len(vals), "mean": float(np.mean(vals)), "std": float(np.std(vals))}

out = {"task": "A3M R10: amplitude-ratio trend vs gamma_cr and C_th",
       "source": str(SRC.relative_to(HERE.parents[2])), "n_points": len(pts),
       "ols_slope_vs_gamma_cr_all": float(np.polyfit(g, r, 1)[0]),
       "ols_slope_vs_gamma_cr_inwindow": float(np.polyfit(g[inwin], r[inwin], 1)[0]),
       "n_inwindow": int(inwin.sum()),
       "d_ratio_per_0.1_C_th": {"mean": float(np.mean(steps)), "n_pairs": len(steps),
                                "min": float(np.min(steps)), "max": float(np.max(steps))},
       "inwindow_family_composition": fam_stats}
(HERE / "ratio_slope.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
