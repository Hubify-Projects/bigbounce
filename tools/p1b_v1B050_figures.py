#!/usr/bin/env python3
"""
P1B v1B.0.50 figure regeneration (R22prov closure wave A).

Figure A — fig_namaster_recovery.png
  Replaces the stale fig_namaster_beta_vs_nside.png (which plotted an old
  exploratory run inconsistent with every §IV number: 512-point at ~0.15°,
  "Planck SMICA" title, "Planck+ACT (Eskilt)" legend).
  Every plotted number traces to on-disk artifacts:
    reproducibility/p1_namaster_500mc/results/summary.json
    reproducibility/p1_namaster_500mc/results/c1_fsky_sweep.json

Figure B — fig_dneff_viability_two_frozen.pdf (+png)
  Regenerated from the frozen Table I values of paper1b_mcmc_companion.tex
  (artifact-verified in v1B.0.25 against on-disk JSON/chains).
  Changes vs the stale research/final_paper_prep/generate_two_frozen_figures.py
  version: legend count 175,545 -> 176,240 (frozen chain total, v1B.0.23
  closure); uncited overlays removed (WP4 reheating/decay bands, "BBN 2sigma
  upper (0.41)", "ACT DR6 central (0.40)" — the last is not a published value);
  stale hardcoded values replaced by Table I values.
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
FIG_DIR = os.path.join(ROOT, "arxiv", "figures")
RES = os.path.join(ROOT, "reproducibility", "p1_namaster_500mc", "results")

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.linewidth": 0.8,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "legend.frameon": True,
    "legend.framealpha": 0.9,
    "legend.edgecolor": "0.8",
    "figure.dpi": 150,
})

# ---------------------------------------------------------------- Figure A
with open(os.path.join(RES, "summary.json")) as f:
    S = json.load(f)
with open(os.path.join(RES, "c1_fsky_sweep.json")) as f:
    SW = json.load(f)

r = S["results"]
inj = [r["beta_null"]["input_beta_deg"], r["beta_paper1"]["input_beta_deg"],
       r["beta_observed"]["input_beta_deg"]]
rec = [r["beta_null"]["recovered_beta_deg"], r["beta_paper1"]["recovered_beta_deg"],
       r["beta_observed"]["recovered_beta_deg"]]

fsky = [S["f_sky"]] + [x["fsky_actual_apodized"] for x in SW["results"]]
beta_f = [r["beta_paper1"]["recovered_beta_deg"]] + \
         [x["beta_recovered_deg"] for x in SW["results"]]
sig_f = [None] + [x["sigma_beta_per_realization_deg"] for x in SW["results"]]
nreal = SW["results"][0]["n_real"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
fig.subplots_adjust(left=0.09, right=0.97, bottom=0.16, top=0.92, wspace=0.30)

# (a) recovered vs injected at canonical fsky=0.32 mask
ax1.plot([-0.02, 0.40], [-0.02, 0.40], color="0.6", lw=0.9, ls="--",
         label=r"$\hat\beta=\beta_{\rm inj}$ (unbiased)")
ax1.plot(inj, rec, "o", color="#2166ac", ms=7, zorder=5,
         label=r"500-MC mean $\hat\beta$")
for x, y in zip(inj, rec):
    ax1.annotate(f"{y - x:+.3f}" + r"$^\circ$", (x, y), textcoords="offset points",
                 xytext=(6, -11), fontsize=8, color="0.25")
ax1.set_xlabel(r"injected $\beta_{\rm inj}$ [deg]")
ax1.set_ylabel(r"recovered $\hat\beta$ [deg]")
ax1.set_xlim(-0.02, 0.40)
ax1.set_ylim(-0.02, 0.40)
ax1.legend(fontsize=8, loc="lower right")
ax1.text(0.05, 0.88, "(a)", transform=ax1.transAxes, fontsize=12,
         fontweight="bold")
ax1.set_title(r"synthetic $\Lambda$CDM skies, $f_{\rm sky}=0.32$", fontsize=9)

# (b) recovered beta vs fsky at beta_inj = 0.27 deg
ax2.axhline(0.27, color="0.35", lw=0.9, ls="--",
            label=r"injected $\beta=0.27^\circ$")
for i, (x, y, s) in enumerate(zip(fsky, beta_f, sig_f)):
    if s is not None:
        ax2.errorbar([x], [y], yerr=[s], fmt="s", color="#b2182b", ms=6,
                     capsize=4, elinewidth=1.0, alpha=0.45, zorder=4,
                     label=r"per-realization $\pm\sigma_\beta$" if i == 1 else None)
        ax2.errorbar([x], [y], yerr=[s / np.sqrt(nreal)], fmt="s",
                     color="#b2182b", ms=6, capsize=2.5, elinewidth=1.6, zorder=5,
                     label=r"500-MC mean $\pm\sigma_\beta/\sqrt{N}$" if i == 1 else None)
    else:
        ax2.plot([x], [y], "o", color="#2166ac", ms=7, zorder=5,
                 label=r"canonical run (mean $\hat\beta$ only)")
ax2.set_xlabel(r"$f_{\rm sky}$")
ax2.set_ylabel(r"recovered $\hat\beta$ [deg]")
ax2.set_xlim(0.25, 0.95)
ax2.set_ylim(0.17, 0.32)
ax2.legend(fontsize=7.5, loc="upper right")
ax2.text(0.05, 0.06, "(b)", transform=ax2.transAxes, fontsize=12,
         fontweight="bold")
ax2.set_title(r"$\beta_{\rm inj}=0.27^\circ$ sky-fraction sweep", fontsize=9)

p = os.path.join(FIG_DIR, "fig_namaster_recovery.png")
fig.savefig(p, dpi=300, bbox_inches="tight")
print("saved", p)
plt.close(fig)

# ---------------------------------------------------------------- Figure B
# Values verbatim from Table I (tab:verification) of paper1b_mcmc_companion.tex
datasets = {
    "full_tension": {
        "label": "Full tension (176 240 samples)",
        "color": "#2166ac", "marker": "o",
        "H0": (67.68, 1.06), "delta_neff": (-0.020, 0.169),
        "sigma8": (0.803, 0.008), "S8": (0.814, 0.008),
        "omegam": (0.308, 0.005), "tau": (0.054, 0.007), "ns": (0.965, 0.006),
    },
    "planck_bao_sn": {
        "label": "Planck+BAO+SN (132 949 samples)",
        "color": "#b2182b", "marker": "s",
        "H0": (67.79, 1.09), "delta_neff": (0.065, 0.17),
        "sigma8": (0.812, 0.009), "S8": (0.831, 0.018),
        "omegam": (0.312, 0.006), "tau": (0.056, 0.007), "ns": (0.967, 0.006),
    },
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.5))
fig.subplots_adjust(left=0.08, right=0.96, bottom=0.15, top=0.90, wspace=0.35)

x = np.linspace(-0.7, 1.1, 600)
for key, d in datasets.items():
    mu, sig = d["delta_neff"]
    pdf = norm.pdf(x, mu, sig)
    ax1.plot(x, pdf, color=d["color"], lw=1.8, label=d["label"])
    ax1.fill_between(x, pdf, alpha=0.15, color=d["color"])
ax1.axvline(0.0, color="k", ls="-", lw=0.9, label=r"SM ($\Delta N_\mathrm{eff}=0$)")
ax1.set_xlabel(r"$\Delta N_\mathrm{eff}$", fontsize=11)
ax1.set_ylabel("Probability density", fontsize=10)
ax1.set_xlim(-0.65, 1.05)
ax1.set_ylim(bottom=0)
ax1.legend(fontsize=7.5, loc="upper right")
ax1.text(0.03, 0.95, "(a)", transform=ax1.transAxes, fontsize=12,
         fontweight="bold", va="top")

params_order = ["H0", "delta_neff", "sigma8", "S8", "omegam", "tau", "ns"]
param_labels = [r"$H_0$", r"$\Delta N_\mathrm{eff}$", r"$\sigma_8$",
                r"$S_8$", r"$\Omega_m$", r"$\tau$", r"$n_s$"]
y_vals = np.arange(len(params_order))
for key, d in datasets.items():
    offs, errs = [], []
    for pname in params_order:
        mu, sig = d[pname]
        ft_mu, ft_sig = datasets["full_tension"][pname]
        offs.append((mu - ft_mu) / ft_sig)
        errs.append(sig / ft_sig)
    shift = 0.12 if key == "planck_bao_sn" else -0.12
    ax2.errorbar(offs, y_vals + shift, xerr=errs, fmt=d["marker"],
                 color=d["color"], ms=6, capsize=3.5, elinewidth=1.0,
                 label=d["label"], zorder=5)
ax2.axvline(0, color="0.6", ls="-", lw=0.7, zorder=0)
ax2.axvspan(-1, 1, color="0.92", alpha=0.5, zorder=0)
ax2.set_yticks(y_vals)
ax2.set_yticklabels(param_labels, fontsize=9.5)
ax2.set_xlabel(r"$(x - x_\mathrm{full\_tension}) \;/\; \sigma_\mathrm{full\_tension}$",
               fontsize=9.5)
ax2.set_xlim(-3.5, 3.5)
ax2.legend(fontsize=7, loc="lower right")
ax2.text(0.03, 0.95, "(b)", transform=ax2.transAxes, fontsize=12,
         fontweight="bold", va="top")
fig.suptitle("Independent MCMC verification --- 2 frozen dataset combinations",
             fontsize=12, fontweight="bold", color="0.4", y=0.97)
for ext in ("pdf", "png"):
    p = os.path.join(FIG_DIR, f"fig_dneff_viability_two_frozen.{ext}")
    fig.savefig(p, dpi=300, bbox_inches="tight")
    print("saved", p)
plt.close(fig)
