#!/usr/bin/env python3
"""Row 16(ii-b) figures. Reads only the committed results JSONs so the plotted
numbers cannot diverge from the reported ones."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent
r1 = json.loads((HERE / "s1_pa_transfer_results.json").read_text())
r4 = json.loads((HERE / "s4_n20k_slope_reanalysis.json").read_text())
rn = json.loads((HERE / "posthoc_nocrop_eps.json").read_text())

ang = r1["angles_deg"]
eps = [r1["S1_paired_parity_transfer"][str(a)]["eps"] for a in ang]
se = [r1["S1_paired_parity_transfer"][str(a)]["eps_boot_se"] for a in ang]
rho = [r1["S1_paired_parity_transfer"][str(a)]["rho"] for a in ang]
L = [r1["S1_paired_parity_transfer"][str(a)]["L"] for a in ang]
R = [r1["S5_rotation_stability"][str(a)]["R_same_class"] for a in ang]
eobs = [r1["POSTHOC_observed_orientation_transfer"][str(a)]["eps_obs"] for a in ang]

fig, ax = plt.subplots(1, 2, figsize=(11.4, 4.3))

a0 = ax[0]
a0.axhline(1.0, color="k", lw=1, ls="--", label=r"$\epsilon=1$ (assumed by the label-level bound)")
a0.errorbar(ang, eps, yerr=se, fmt="o-", color="#1f77b4", capsize=3,
            label=r"$\epsilon(\varphi)$  parity flip registered")
a0.plot(ang, rho, "s--", color="#d62728", label=r"$\rho(\varphi)$  handedness retained (error)")
a0.plot(ang, L, "^--", color="#ff7f0e", label=r"$L(\varphi)$  leaked to NOT_SPIRAL")
a0.plot(ang, R, "d:", color="#7f7f7f", label=r"$R(\varphi)$  rotation-only class stability")
a0.plot(ang, eobs, "v-.", color="#2ca02c", label=r"$\epsilon_{\rm obs}(\varphi)$ vs observed frame (post-hoc)")
nc_ang = rn["angles_deg"]
nc_eps = [rn["all_galaxies"]["per_theta"][str(a)]["eps_corotated"] for a in nc_ang]
a0.plot(nc_ang, nc_eps, "*", ms=13, color="#9467bd", ls="none", zorder=5,
        label=r"$\epsilon(\varphi)$, EXACT released preprocessing, no crop (post-hoc)")
for c in (0, 180):
    a0.axvline(c, color="k", lw=0.6, alpha=0.25)
a0.set_xticks(ang)
a0.set_xlabel(r"restoring rotation $\varphi = 2\,\mathrm{PA}$  [deg]")
a0.set_ylabel("probability")
a0.set_ylim(-0.03, 1.46)
a0.set_title(f"PA-restoring parity transfer, N={r1['n_galaxies']:,}\n"
             r"$\bar\epsilon_{\rm inf}=$" + f"{r1['S1_eps_bar_informative']:.4f}"
             + r"$\pm$" + f"{r1['S1_eps_bar_informative_boot_se']:.4f}"
             + f"  (z={r1['S1_z_vs_unity']:+.1f} vs unity)", fontsize=9)
a0.legend(fontsize=6.4, loc="upper left", ncol=2, framealpha=0.95)
a0.grid(alpha=0.25)

a1 = ax[1]
mu = r4["mc_mean_slope_spiral_classified"]
sd = r4["mc_se_slope_spiral_classified"]
x = np.linspace(mu - 4 * sd, mu + 4 * sd, 400)
a1.plot(x, np.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * np.sqrt(2 * np.pi)),
        color="#1f77b4", label=f"MC null, {r4['mc_replicas']} replicas of the\ncommitted 5f x 10-seed design")
a1.axvline(r4["exact_identity_slope_spiral_classified"], color="k", ls="--", lw=1.2,
           label=r"exact identity $-2A_0=$" + f"{r4['exact_identity_slope_spiral_classified']:+.4f}")
a1.axvline(r4["committed_slope_spiral_classified"], color="#d62728", lw=1.6,
           label=f"committed row 16(ii) slope {r4['committed_slope_spiral_classified']:+.4f}\n"
                 f"(z={r4['z_committed_vs_identity_spiral_classified']:+.2f})")
a1.set_xlabel(r"fitted $dA_{\rm cls}/df$")
a1.set_ylabel("density")
a1.set_title("S4: the N=20,000 injection slope against its own\n"
             f"injection-realisation noise floor (N for 3$\\sigma$ power: "
             f"{r4['n_required_for_3sigma_power_spiral_classified']/1e3:.0f}k)", fontsize=9)
a1.legend(fontsize=6.6)
a1.grid(alpha=0.25)

fig.tight_layout()
fig.savefig(HERE / "fig_row16iib_pa_parity_transfer.png", dpi=160)
print("wrote fig_row16iib_pa_parity_transfer.png")
