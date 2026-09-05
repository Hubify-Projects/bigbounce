#!/usr/bin/env python3
"""Row 16 step (ii): figure comparing the N=20000 pixel-level
production-equivariant-TTA injection-recovery curve (spiral-classified
A statistic, 10 seeds/fraction with per-seed std as the noise floor)
against the exact closed-form label-level analytic identity."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
d = json.loads((HERE / "scale20k_injection_results.json").read_text())
per_seed = pd.DataFrame(d["per_seed_results"])

fig, ax = plt.subplots(figsize=(6.2, 4.4))

means = per_seed.groupby("f_injected")["A_recovered_spiral_classified"].mean() * 100
stds = per_seed.groupby("f_injected")["A_recovered_spiral_classified"].std() * 100
fs = means.index.values * 100

ax.errorbar(fs, means.values, yerr=stds.values, fmt="o-", color="#1e3a5f",
            markersize=5, linewidth=1.4, capsize=3,
            label="pixel-level, production equivariant TTA\n(N=20000, mean $\\pm$ std over 10 seeds)")

label_curve = pd.DataFrame(d["label_level_analytic_curve_spiral_classified"])
ax.plot(label_curve["f_injected"] * 100, label_curve["A_label_cls"] * 100,
        "--", color="#dc2626", linewidth=1.4,
        label="label-level analytic identity\n$A(f)=A_0(1-2f)$")

ax.axhline(d["paper_residual_bias_postprocess"] * 100, linestyle=":", color="#16a34a",
           linewidth=1.2, label=f"paper's published residual bias ({d['paper_residual_bias_postprocess']*100:+.2f}%)")

ax.set_xlabel("injected mirror-flip fraction $f$ (%)", fontsize=10)
ax.set_ylabel("recovered asymmetry $A$ = $2f_{\\rm CW}-1$ among\nspiral-classified galaxies (%)", fontsize=10)
ax.set_title("Row 16 step (ii): pixel-level parity injection\nthrough the production equivariant pipeline (N=20000)", fontsize=10.5)
ax.legend(loc="best", fontsize=7.5, frameon=True)
ax.grid(alpha=0.25)
fig.tight_layout()
out = HERE / "fig_scale20k_injection_recovery.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
plt.close(fig)
print(f"wrote {out}")
