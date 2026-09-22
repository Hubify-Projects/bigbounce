#!/usr/bin/env python3
"""Figures for the row-16 TTA / d(180) / sky-dipole lane.

Reads ONLY the committed result JSONs, so a plotted number cannot diverge from a
reported one.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
T = json.loads((HERE / "t_tta_recovery.json").read_text())
P = json.loads((HERE / "p_d180_catalogue_wide.json").read_text())
S = json.loads((HERE / "s_sky_dipole.json").read_text())

LBL = {"Z2_released": "released\n(flip TTA)", "D4": "D4 TTA\n(4 rot x flip)",
       "D8": "D8 TTA\n(8 rot x flip)"}
COL = {"Z2_released": "#444444", "D4": "#1f77b4", "D8": "#2ca02c"}

fig, ax = plt.subplots(2, 2, figsize=(13.5, 9.5))

# (a) dilution bound by TTA group
a = ax[0, 0]
groups = list(LBL)
x = np.arange(len(groups))
for j, (blk, tag, off, hatch) in enumerate([(T["T2_all_galaxies"], "all spirals", -0.18, None),
                                            (T["T2_primary_hc"], "primary_hc", +0.18, "//")]):
    v = [blk["by_group"][g]["D_upper_bound"] for g in groups]
    e = [blk["by_group"][g]["D_upper_bound_boot_se"] for g in groups]
    a.bar(x + off, v, 0.34, yerr=e, capsize=3, hatch=hatch,
          color=[COL[g] for g in groups], alpha=0.95 if j == 0 else 0.55,
          edgecolor="k", linewidth=0.6, label=f"{tag} (n={blk['n']:,})")
a.axhline(1.0, color="crimson", ls="--", lw=1.2)
a.text(2.45, 1.005, "D = 1 (no dilution)", color="crimson", fontsize=8, ha="right")
for i, g in enumerate(groups):
    f = T["T2_all_galaxies"]["by_group"][g]["recovery_fraction_F"]
    if g != "Z2_released":
        a.text(i - 0.18, T["T2_all_galaxies"]["by_group"][g]["D_upper_bound"] + 0.035,
               f"F={f:.2f}", ha="center", fontsize=9, fontweight="bold")
a.set_xticks(x); a.set_xticklabels([LBL[g] for g in groups], fontsize=9)
a.set_ylabel(r"dilution bound  $D \leq 1-\max_\phi d(\phi)$")
a.set_ylim(0, 1.12); a.legend(fontsize=8, loc="lower right")
a.set_title(f"(a) what rotation equivariance recovers, free\n"
            f"16-angle 22.5$^\\circ$ grid, n={T['n_galaxies_stage3_complete']:,}", fontsize=10)

# (b) d(phi)
b = ax[0, 1]
for g in groups:
    r = T["T2_all_galaxies"]["by_group"][g]
    ph = sorted(float(k) for k in r["d_by_angle"])
    dv = [r["d_by_angle"][f"{p:g}"]["d"] for p in ph]
    b.plot([0] + ph, [0] + dv, "o-", color=COL[g], ms=4, lw=1.4,
           label=f"{LBL[g].replace(chr(10),' ')}  (max$_{{inf}}$={r['max_d_informative']:.3f})")
b.set_xlabel(r"presented rotation $\phi$ [deg]")
b.set_ylabel(r"label self-disagreement  $d(\phi)$")
b.set_xticks(np.arange(0, 361, 45)); b.grid(alpha=0.25)
b.legend(fontsize=8); b.set_ylim(bottom=-0.01)
b.set_title("(b) the TTA zeroes $d$ on its own rotation orbit exactly\n"
            "(theorem, control T0-C) and leaves the off-group residual", fontsize=10)

# (c) d(180) across the independent draws + the labelled estimate
c = ax[1, 0]
names, vals, errs, cols, hatches = [], [], [], [], []
for k in ("scale20k", "scale5k", "pilot500", "UNION"):
    r = P["MEASURED"][k]["all"]
    names.append(f"{k}\nn={r['n']:,}")
    vals.append(r["d_180"]); errs.append(r["d_180_boot_se"])
    cols.append("#1f77b4" if k != "UNION" else "#17557a"); hatches.append(None)
e_all = P["P3_REWEIGHTED_ESTIMATE"]["parent_all_spirals"]
names.append(f"parent ESTIMATE\n(re-weighted)")
vals.append(e_all["d_180_estimate"]); errs.append(e_all["d_180_estimate_boot_se"])
cols.append("#d62728"); hatches.append("xx")
c.bar(range(len(vals)), vals, 0.6, yerr=errs, capsize=3, color=cols, hatch=hatches,
      edgecolor="k", linewidth=0.6)
c.set_xticks(range(len(vals))); c.set_xticklabels(names, fontsize=8)
c.set_ylabel(r"$d(180^\circ)$  (released preprocessing, lossless)")
c.set_title("(c) $d(180^\\circ)$ on every cached draw; the red bar is an\n"
            "EXTRAPOLATION (confidence-stratified), not a measurement", fontsize=10)
c.text(0.02, 0.97, "pre-registered control P2c FAILED:\nthese are properties of the released\nCHECKPOINT on viewer cutouts, not of\nthe released catalogue's own labels",
       transform=c.transAxes, va="top", ha="left", fontsize=7.5, color="#8b0000",
       bbox=dict(boxstyle="round,pad=0.35", fc="#fff3f3", ec="#8b0000", lw=0.7))
c.grid(axis="y", alpha=0.25)

# (d) induced spurious dipole vs the P4' limits
d = ax[1, 1]
fp = S["S2c_induced_label_dipole"]["full_parent"]
st = S["S2c_induced_label_dipole"]["strict_primary"]
labels = ["full parent\nsupport", "strict 887,472\nsupport"]
ind = [fp["A_induced_spurious_dipole"] * 100, st["A_induced_spurious_dipole"] * 100]
inderr = [fp["A_induced_boot_se"] * 100, st["A_induced_boot_se"] * 100]
a95 = [S["S3_verdict"]["A95_obs_full_parent"] * 100, S["S3_verdict"]["A95_obs_strict_887k"] * 100]
xx = np.arange(2)
d.bar(xx - 0.2, a95, 0.38, color="#bbbbbb", edgecolor="k", linewidth=0.6,
      label=r"$A_{95}^{\rm obs}$ (P4$'$ limit)")
d.bar(xx + 0.2, ind, 0.38, yerr=inderr, capsize=3, color="#d62728", edgecolor="k",
      linewidth=0.6, label=r"induced spurious dipole $A_{\rm induced}$")
for i in range(2):
    d.plot([xx[i] + 0.01, xx[i] + 0.39], [0.1 * a95[i]] * 2, color="k", ls=":", lw=1.4)
    d.text(xx[i] + 0.2, ind[i] + inderr[i] + 0.02,
           f"{ind[i]/a95[i]*100:.0f}% of $A_{{95}}$", ha="center", fontsize=9,
           fontweight="bold")
d.plot([], [], color="k", ls=":", lw=1.4, label="10% caveat threshold")
d.set_xticks(xx); d.set_xticklabels(labels, fontsize=9)
d.set_ylabel("dipole amplitude [%]")
d.legend(fontsize=8, loc="upper left")
d.set_title(f"(d) sky-varying dilution $\\times$ observed monopole:\n"
            f"caveat required = {S['S3_verdict']['CAVEAT_REQUIRED']}", fontsize=10)

fig.suptitle("Rows 13/16 follow-ups — rotation-TTA recovery bound, $d(180^\\circ)$ beyond "
             "N=19,800, and the S6 sky-dependence dipole", fontsize=12.5, y=0.985)
fig.tight_layout(rect=[0, 0, 1, 0.965])
fig.savefig(HERE / "fig_row16_tta_d180_dipole.png", dpi=150)
print("wrote fig_row16_tta_d180_dipole.png")
