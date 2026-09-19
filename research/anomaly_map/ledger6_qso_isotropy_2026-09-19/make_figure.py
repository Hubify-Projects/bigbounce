#!/usr/bin/env python3
"""Ledger #6 second discriminator, step 3: the figure.
(a) QSO overdensity map in Galactic coordinates with the Planck modulation axis;
(b) binned clustering variance vs cos(angle to the Planck axis), with the fit and
    the CMB A = 0.07 expectation overlaid;
(c) |A| over the 1,536 admissible axes, with the Planck axis marked.
"""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import healpy as hp
from analyze_isotropy import load_sample, lb_to_vec, PLANCK_LB, A_CMB, OUT

R = json.load(open(f"{OUT}/ledger6_qso_isotropy.json"))
S = load_sample(64)
phat = lb_to_vec(*PLANCK_LB)
x = phat @ S["vec"]
e = S["delta"] ** 2 - S["shot"]
a = np.asarray(R["S2_modulation"]["a_cap"])[S["cap"]]
W = 1.0 / (2.0 * (a + S["shot"]) ** 2)

fig = plt.figure(figsize=(11.0, 7.6))

# (a) map
m = np.full(hp.nside2npix(64), hp.UNSEEN)
m[S["idx"]] = np.clip(S["delta"], -0.6, 0.6)
plt.axes([0.02, 0.50, 0.96, 0.46])
hp.mollview(m, coord=["C", "G"], title="", cbar=True, min=-0.6, max=0.6,
            unit=r"$\delta_{\rm QSO}$ (0.84 deg$^2$ pixels)", hold=True,
            cmap="RdBu_r", badcolor="0.93", bgcolor="white")
hp.graticule(dpar=30, dmer=60, color="0.75", verbose=False)
for lab, (l, b), c in ((r"Planck $\hat p$", PLANCK_LB, "k"),
                       (r"$-\hat p$", (PLANCK_LB[0] - 180, -PLANCK_LB[1]), "0.4")):
    hp.projscatter([l], [b], lonlat=True, coord="G", marker="*", s=220, color=c, zorder=5)
    hp.projtext(l + 6, b + 8, lab, lonlat=True, coord="G", color=c, fontsize=9)
plt.title("DESI DR1 QSO overdensity, $0.8<z<2.1$ (Galactic)   "
          r"$N=856{,}831$, $8947\ \mathrm{deg}^2$", fontsize=11)

# (b) variance vs cos angle
ax = fig.add_axes([0.085, 0.075, 0.40, 0.37])
nb = 10
edges = np.quantile(x, np.linspace(0, 1, nb + 1))
xc, yc, ye = [], [], []
for i in range(nb):
    s = (x >= edges[i]) & (x < edges[i + 1] if i < nb - 1 else x <= edges[i + 1])
    xc.append(np.average(x[s], weights=W[s]))
    yc.append(np.sum(W[s] * e[s]) / np.sum(W[s]) / np.average(a[s], weights=W[s]))
    ye.append(1.0 / np.sqrt(np.sum(W[s])) / np.average(a[s], weights=W[s]))
ax.errorbar(xc, yc, yerr=ye, fmt="o", color="#1b3a6b", ms=5, lw=1.2, label="DESI DR1 QSO")
xx = np.linspace(min(x), max(x), 50)
A = R["S2_modulation"]["A"]; Ae = R["S2_modulation"]["A_err"]
ax.plot(xx, 1 + 2 * A * xx, color="#1b3a6b", lw=1.6,
        label=fr"fit $A={A:+.3f}\pm{Ae:.3f}$")
ax.fill_between(xx, 1 + 2 * (A - Ae) * xx, 1 + 2 * (A + Ae) * xx, color="#1b3a6b", alpha=0.15)
ax.plot(xx, 1 + 2 * A_CMB * xx, color="#c1272d", ls="--", lw=1.6,
        label=fr"CMB modulation $A={A_CMB}$")
ax.axhline(1.0, color="0.6", lw=0.8, ls=":")
ax.set_xlabel(r"$\hat n \cdot \hat p$  (Planck asymmetry axis)")
ax.set_ylabel(r"clustering variance / $\sigma^2_{\rm cap}$")
ax.legend(fontsize=8.5, frameon=False, loc="upper left")
ax.set_title("(b) degree-scale clustering amplitude vs direction", fontsize=10)

# (c) axis scan
ax2 = fig.add_axes([0.575, 0.075, 0.40, 0.37])
scan = np.abs(np.load(f"{OUT}/axis_scan_A.npy"))
ax2.hist(scan, bins=40, color="0.75", edgecolor="0.5", lw=0.4)
ap = abs(R["N2_axis_scan"]["A_profile_planck"])
ax2.axvline(ap, color="#1b3a6b", lw=2,
            label=fr"Planck axis $|A|={ap:.3f}$ ($p_{{\rm LEE}}={R['N2_axis_scan']['p_LEE']:.2f}$)")
ax2.axvline(A_CMB, color="#c1272d", ls="--", lw=1.8, label=fr"CMB $|A|={A_CMB}$")
ax2.set_xlabel(r"$|A|$ over 1,536 admissible axes")
ax2.set_ylabel("number of axes")
ax2.legend(fontsize=8.5, frameon=False)
ax2.set_title("(c) look-elsewhere null: the CMB axis is unremarkable", fontsize=10)

fig.savefig(f"{OUT}/ledger6_qso_isotropy.png", dpi=155, bbox_inches="tight",
            facecolor="white")
print("wrote", f"{OUT}/ledger6_qso_isotropy.png")
