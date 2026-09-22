"""LS12 addendum -- how the perturbative-subset ratio depends on where the
cut is placed. Pre-registration §4 requires the non-perturbative points to be
named rather than summarised; this reports the equally-important fact that the
subset statistic SLIDES with the threshold, since no point of the headline
population reaches eps <= 0.5 and almost all reach eps <= 1.5.
"""
import json
import numpy as np

d = json.load(open("results.json"))
H = [p for p in d["points"] if 0.267 <= p["gamma_cr"] <= 0.630]
r = np.array([p["ratio_-35/16_over_-35/8"] for p in H])
e16 = np.array([p["eps[-35/16]"] for p in H])
e8 = np.array([p["eps[-35/8]"] for p in H])
emax = np.maximum(e16, e8)

out = {"note": "subset of H with max(eps_16, eps_8) <= t, at both legs",
       "pearson_r_ratio_vs_eps_max_over_H": float(np.corrcoef(emax, r)[0, 1]),
       "ols_slope_ratio_per_unit_eps_max": float(np.polyfit(emax, r, 1)[0]),
       "curve": []}
print(f"{'t':>6}{'n':>6}{'mean':>9}{'std':>8}{'min':>8}{'max':>8}")
for t in [0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]:
    m = emax <= t
    row = {"threshold": t, "n": int(m.sum())}
    if m.sum():
        row.update(mean=float(r[m].mean()), std=float(r[m].std()),
                   min=float(r[m].min()), max=float(r[m].max()))
        print(f"{t:>6.1f}{m.sum():>6}{r[m].mean():>9.4f}{r[m].std():>8.4f}"
              f"{r[m].min():>8.4f}{r[m].max():>8.4f}")
    else:
        print(f"{t:>6.1f}{0:>6}{'--':>9}")
    out["curve"].append(row)
print(f"\nratio vs max-eps over H: pearson r = {out['pearson_r_ratio_vs_eps_max_over_H']:+.3f}, "
      f"OLS slope = {out['ols_slope_ratio_per_unit_eps_max']:+.4f} per unit eps")
json.dump(out, open("threshold_sensitivity.json", "w"), indent=1)
