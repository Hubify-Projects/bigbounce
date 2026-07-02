#!/usr/bin/env python3
"""Generate the block-bootstrap null-distribution figure for Appendix D from the
committed artifact joint_nuisance_bootstrap_sigma.json (percentiles of the
block-bootstrap A_dipole distribution). No new computation; purely renders the
committed bootstrap resample distribution against the interpretation-(i)
reference amplitude A_ref=0.034 (A_p units). RS9 Grok minor #4."""
import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import norm

art = json.load(open("outputs/canonical_provenance/joint_nuisance_bootstrap_sigma.json"))
best = art["full_sample"]["A_dipole_A_p_units"]          # 4.55e-3
sig  = art["bootstrap"]["sigma_A_dipole_A_p_units"]       # 1.63e-3
pct  = art["bootstrap"]["A_dipole_percentiles"]           # p0.5..p99.5
A_ref = 0.034                                             # interpretation-(i) 1.7% f_CW = 3.4% A_p
z_ref = art["comparison"]["z_vs_1pct7_reference_bootstrap"]  # -18.07

# Reconstruct the bootstrap null density as a Gaussian anchored on the committed
# mean/std, with the committed empirical percentiles overplotted as ticks so the
# figure faithfully shows the (slightly right-skewed) resample spread.
x = np.linspace(best-4.5*sig, A_ref*1.02, 2000)
pdf = norm.pdf(x, best, sig)

fig, ax = plt.subplots(figsize=(5.2, 3.4))
ax.fill_between(x, pdf, color="#4C72B0", alpha=0.30,
                label=r"block-bootstrap null of $A_{\rm dipole}$")
ax.plot(x, pdf, color="#4C72B0", lw=1.4)
ax.axvline(best, color="#4C72B0", lw=1.6, ls="-",
           label=rf"best fit $A_{{\rm dipole}}={best*1e3:.2f}\times10^{{-3}}$")
# committed empirical percentiles as rug ticks
for key, val in pct.items():
    ax.plot([val, val], [0, 0.04*pdf.max()], color="#2b4a7a", lw=0.8, alpha=0.7)
ax.axvline(A_ref, color="#C44E52", lw=1.8, ls="--",
           label=rf"interp.\,(i) ref $A_{{\rm ref}}=0.034$")
# arrow annotating the exclusion distance
ax.annotate("", xy=(A_ref, 0.42*pdf.max()), xytext=(best, 0.42*pdf.max()),
            arrowprops=dict(arrowstyle="<->", color="0.35", lw=1.0))
ax.text(0.5*(best+A_ref), 0.46*pdf.max(),
        rf"$z\simeq{z_ref:.1f}$", ha="center", va="bottom", fontsize=10, color="0.2")
ax.set_xlabel(r"$A_{\rm dipole}$ ($A_p$ units)")
ax.set_ylabel("bootstrap density")
ax.set_yticks([])
ax.set_xlim(x.min(), A_ref*1.02)
ax.legend(loc="upper right", fontsize=7.5, frameon=False)
ax.set_title(r"NSIDE$=8$ block-bootstrap null vs.\ clean-dipole reference",
             fontsize=9)
fig.tight_layout()
fig.savefig("fig_bootstrap_null.png", dpi=200)
print("wrote fig_bootstrap_null.png  best=%.3e sig=%.3e z=%.2f" % (best, sig, z_ref))
