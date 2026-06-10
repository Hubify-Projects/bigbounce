#!/usr/bin/env python3
"""R23conf closure P4-m5: regenerate fig_multipoles.png from the canonical
200-MC multi-null battery (outputs/canonical_provenance/p4_multinull_battery.json)
so the burned-in per-ell sigma annotations match the canonical values quoted in
the caption and Appendix D (sigma_l = +3.63, +4.73, -0.96, +0.13, -0.63),
replacing the superseded 1000-shuffle figure-generation values (which showed
an ell=5 bar at 2.5 sigma not reproduced by the canonical battery).

Backup of the old figure: fig_multipoles.png.pre_c11_r23conf.bak
"""
import json
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SRC = "outputs/canonical_provenance/p4_multinull_battery.json"
OUT = "fig_multipoles.png"

shutil.copy(OUT, OUT + ".pre_c11_r23conf.bak")

d = json.load(open(SRC))["results"]["multipole_spectrum"]
ells = [1, 2, 3, 4, 5]
data = np.array([d[f"l_{l}"]["data"] for l in ells]) * 1e6
nmean = np.array([d[f"l_{l}"]["null_mean"] for l in ells]) * 1e6
nstd = np.array([d[f"l_{l}"]["null_std"] for l in ells]) * 1e6
sigma = np.array([d[f"l_{l}"]["sigma"] for l in ells])

x = np.arange(len(ells), dtype=float)
w = 0.38

fig, ax = plt.subplots(figsize=(9.6, 6.0), dpi=200)
ax.bar(x - w / 2, nmean, w, yerr=nstd, capsize=5, color="0.8",
       edgecolor="0.4", label="Null expectation (200-MC battery)",
       error_kw={"elinewidth": 1.6})
colors = ["#1f5fa8" if s >= 3 else "#7fb3d8" for s in sigma]
ax.bar(x + w / 2, data, w, color=colors, edgecolor="0.25", label="Measured")
for xi, (di, si) in enumerate(zip(data, sigma)):
    ax.annotate(f"{si:+.2f}$\\sigma$",
                (x[xi] + w / 2, max(di, nmean[xi] + nstd[xi]) + 0.45),
                ha="center", fontsize=13,
                color="#1f5fa8" if si >= 3 else "0.35")
ax.set_xticks(x)
ax.set_xticklabels([f"$\\ell={l}$" for l in ells], fontsize=15)
ax.set_xlabel("Multipole $\\ell$", fontsize=16)
ax.set_ylabel("$C_\\ell$ ($\\times 10^{-6}$)", fontsize=16)
ax.set_title("Angular Power Spectrum of Chirality Asymmetry\n"
             "(canonical mask, 200-MC per-pixel label-shuffle battery)",
             fontsize=16)
ax.legend(fontsize=13, frameon=False)
ax.tick_params(labelsize=13)
ax.set_ylim(bottom=0)
fig.tight_layout()
fig.savefig(OUT)
print("sigma annotations:", [f"{s:+.2f}" for s in sigma])
print(f"saved {OUT}")
