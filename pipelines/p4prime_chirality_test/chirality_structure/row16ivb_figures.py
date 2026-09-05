#!/usr/bin/env python3
"""Row 16 (iv-b) summary figure: parity fraction and dipole z per environment bin."""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "row16ivb_bgs_environment.json")))
BINS = ["void_like", "wall_filament", "node_like"]
LAB = ["void-like\n(lowest quintile)", "wall/filament\n(middle)", "node-like\n(top quintile)"]
SUB = [("specz_3d", "DESI spec-z subset, 3D comoving density"),
       ("photoz_projected", "photo-z / no-z subset, projected density")]

fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.2))
x = np.arange(3)
for r, (tag, title) in enumerate(SUB):
    d = R[tag]
    f = [d["f_CW"][b]["value"] for b in BINS]
    e = [d["f_CW"][b]["binomial_sigma"] for b in BINS]
    z = [d["f_CW"][b]["z"] for b in BINS]
    dz = [d["dipole"][b]["z"] for b in BINS]
    ax = axes[r, 0]
    ax.errorbar(x, 100 * (np.array(f) - 0.5), yerr=100 * np.array(e), fmt="o",
                color="C0", capsize=4)
    ax.axhline(0, color="k", lw=0.8)
    ax.axhline(R[tag]["residual_monopole_percent"] / 2, color="C3", ls="--", lw=1,
               label="injection-calibrated residual (-0.26% in $f_{CW}-f_{CCW}$)")
    ax.set_xticks(x); ax.set_xticklabels(LAB, fontsize=8)
    ax.set_ylabel(r"$f_{\rm CW}-0.5$  [%]")
    ax.set_title(f"{title}\nN = {d['N']:,}", fontsize=9)
    ax.legend(fontsize=6.5, loc="best")
    ax = axes[r, 1]
    ax.bar(x - 0.18, z, width=0.34, label=r"$f_{\rm CW}$ z (label-shuffle null)")
    ax.bar(x + 0.18, dz, width=0.34, label="dipole z (label-shuffle null)")
    for y in (3.7, -3.7):
        ax.axhline(y, color="C3", ls=":", lw=1)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xticks(x); ax.set_xticklabels(LAB, fontsize=8)
    ax.set_ylabel("z vs null")
    ax.set_ylim(-4.4, 4.4)
    chi = d["chi2_trend_2dof"]
    ax.set_title(r"$\chi^2$ trend z = %.2f (p = %.3f); dotted = 3$\sigma$ post-LEE"
                 % (chi["z"], chi["p_two_sided"]), fontsize=9)
    ax.legend(fontsize=6.5)
fig.suptitle("Row 16 (iv-b): galaxy chirality vs DESI DR1 BGS_BRIGHT-21.5 environment",
             fontsize=11)
fig.tight_layout(rect=[0, 0, 1, 0.96])
out = os.path.join(HERE, "row16ivb_bgs_environment.png")
fig.savefig(out, dpi=150)
print("wrote", out)
