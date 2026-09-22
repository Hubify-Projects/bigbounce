"""LS12 figure: the pointwise diagnostic over the scan, and the ratio's
dependence on it inside the headline window."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

d = json.load(open("results.json"))
pts = d["points"]
g = np.array([p["gamma_cr"] for p in pts])
e8 = np.array([p["eps[-35/8]"] for p in pts])
e16 = np.array([p["eps[-35/16]"] for p in pts])
fam = np.array([p["family"] for p in pts])
inH = (g >= 0.267) & (g <= 0.630)
r = np.array([p["ratio_-35/16_over_-35/8"] for p in pts])
emax = np.maximum(e8, e16)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.9))

ax1.axvspan(0.267, 0.630, color="0.88", zorder=0, label=r"headline window (n=144)")
ax1.axvspan(0.766, 0.968, color="#ffe9c4", zorder=0, label="27-point grid window")
for f, m, c in [("lognormal", "o", "#1f77b4"), ("powerlaw", "s", "#d62728")]:
    s = fam == f
    ax1.scatter(g[s], e8[s], marker=m, s=16, alpha=0.7, c=c, label=f"{f}, $-35/8$ leg")
    ax1.scatter(g[s], e16[s], marker=m, s=10, alpha=0.35, c=c, facecolors="none",
                label=f"{f}, $-35/16$ leg")
ax1.axhline(1.0, color="k", lw=1.2, ls="--", label=r"paper's criterion $\varepsilon=1$")
ax1.set_xlabel(r"$\gamma_{\rm cr}$")
ax1.set_ylabel(r"$\varepsilon = 1.2\,|f_{\rm NL}|\,\sigma_r$")
ax1.set_title(r"pointwise perturbativity over the 255-point scan", fontsize=9)
ax1.legend(fontsize=5.6, loc="upper left", ncol=2)
ax1.grid(alpha=0.25)

sc = ax2.scatter(emax[inH], r[inH], c=np.array([p["C_th"] for p in pts])[inH],
                 cmap="viridis", s=20, alpha=0.85)
xs = np.linspace(emax[inH].min(), emax[inH].max(), 20)
k, b = np.polyfit(emax[inH], r[inH], 1)
ax2.plot(xs, k * xs + b, "k-", lw=1.1,
         label=fr"OLS slope ${k:+.3f}$, $\rho={np.corrcoef(emax[inH], r[inH])[0,1]:+.2f}$")
ax2.axvline(1.0, color="r", lw=1.2, ls="--", label=r"$\varepsilon=1$ cut")
ax2.axhline(1.8374, color="0.4", lw=1.0, ls=":", label="full-window mean 1.837")
ax2.axhline(1.8121, color="g", lw=1.0, ls="-.", label=r"$\varepsilon\leq1$ mean 1.812")
ax2.set_xlabel(r"$\max(\varepsilon_{-35/16},\varepsilon_{-35/8})$ at each point")
ax2.set_ylabel(r"$A(-35/16)/A(-35/8)$")
ax2.set_title("inside the headline window: the ratio tracks the\n"
              "control parameter it is supposed to be robust to", fontsize=9)
ax2.legend(fontsize=6, loc="lower right")
ax2.grid(alpha=0.25)
plt.colorbar(sc, ax=ax2, label=r"$C_{\rm th}$")

fig.tight_layout()
fig.savefig("pbh_perturbativity.png", dpi=140)
print("wrote pbh_perturbativity.png")
