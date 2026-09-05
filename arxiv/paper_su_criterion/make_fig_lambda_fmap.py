"""
Figure generator for arxiv/paper_su_criterion/main.tex (paper-su, v1S.0.1).
Plots the general-w linear rescaling lambda(w) = (1-w)/2 and the second-order
map monopole f_map^mono(w) = -5(1+w)/4, from
research/theory_audit/separate_universe_failure_criterion_2026_09_04.json
(general_w block). No new derivation -- transcribes the frozen closed forms.
Run: python3 make_fig_lambda_fmap.py  (writes fig_lambda_fmap.png here)
"""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

with open("../../research/theory_audit/separate_universe_failure_criterion_2026_09_04.json") as f:
    data = json.load(f)

# closed forms, transcribed from data["general_w"] (lambda_ = -(w-1)/2, f_map_monopole = -5(w+1)/4)
w = np.linspace(-1, 1, 400)
lam = (1 - w) / 2.0
fmap_mono = -5.0 * (1 + w) / 4.0

fig, ax1 = plt.subplots(figsize=(3.4, 2.6))
ax1.plot(w, lam, color="#1b4f72", lw=2, label=r"$\lambda(w)=(1-w)/2$")
ax1.set_xlabel(r"$w$ (constant equation of state)")
ax1.set_ylabel(r"$\lambda$", color="#1b4f72")
ax1.tick_params(axis="y", labelcolor="#1b4f72")
ax1.axvline(0.0, color="gray", lw=0.6, ls=":")
ax1.axhline(0.0, color="gray", lw=0.6, ls=":")

ax2 = ax1.twinx()
ax2.plot(w, fmap_mono, color="#a93226", lw=2, ls="--",
         label=r"$f_{\rm map}^{\rm mono}(w)=-\frac{5}{4}(1+w)$")
ax2.set_ylabel(r"$f_{\rm map}^{\rm mono}$", color="#a93226")
ax2.tick_params(axis="y", labelcolor="#a93226")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=6.5, loc="lower left", frameon=False)

fig.tight_layout()
fig.savefig("fig_lambda_fmap.png", dpi=300)
print("wrote fig_lambda_fmap.png")
