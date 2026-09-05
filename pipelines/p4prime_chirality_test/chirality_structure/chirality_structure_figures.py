"""Row 16 (iv) summary figure: all four tests, observed vs null."""
import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ez = json.load(open("chirality_structure_env_z.json"))
ax_ = json.load(open("chirality_structure_axes.json"))
an = json.load(open("chirality_structure_anomaly.json"))
f, axs = plt.subplots(2, 2, figsize=(11, 7.5))

a = ez["a_environment_density_quartiles"]
e = np.sqrt(1.0 / np.asarray(a["bin_counts"]))
axs[0, 0].errorbar(a["bin_centers"], np.asarray(a["bin_means"]) * 100, yerr=e * 100, fmt="o-")
axs[0, 0].axhline(0, color="k", lw=0.6)
axs[0, 0].set_xlabel(r"$\log_{10}\Sigma_{20}$ [sr$^{-1}$]"); axs[0, 0].set_ylabel(r"$\langle\delta\rangle$ [%]")
axs[0, 0].set_title("(a) environment density quartiles\n"
                    rf"$\chi^2$ z={a['chi2']['z']:.2f}, slope z={a['slope']['z']:.2f}")

c = ez["c_redshift_bins"]
e = np.sqrt(1.0 / np.asarray(c["bin_counts"]))
axs[0, 1].errorbar(c["bin_centers"], np.asarray(c["bin_means"]) * 100, yerr=e * 100, fmt="s-", color="C1")
axs[0, 1].axhline(0, color="k", lw=0.6)
axs[0, 1].set_xlabel("spec-z"); axs[0, 1].set_ylabel(r"$\langle\delta\rangle$ [%]")
axs[0, 1].set_title("(c) redshift bins\n"
                    rf"$\chi^2$ z={c['chi2']['z']:.2f}, slope z={c['slope']['z']:.2f}")

ed = np.asarray(an["edges_deg"]); mid = np.sqrt(ed[:-1] * ed[1:])
zs = [r["z"] for r in an["w_theta_vs_rotation"]]
zl = [r["z"] for r in an["w_theta_vs_shuffle"]]
axs[1, 0].plot(mid, zs, "o-", label="rotation null")
axs[1, 0].plot(mid, zl, "^--", label="label-shuffle null")
for y in (-3.8, 3.8):
    axs[1, 0].axhline(y, color="r", ls=":", lw=0.8)
axs[1, 0].axhline(0, color="k", lw=0.6); axs[1, 0].set_xscale("log")
axs[1, 0].set_xlabel(r"$\theta$ [deg]"); axs[1, 0].set_ylabel(r"$z$ of $w(\theta)$")
axs[1, 0].legend(fontsize=8); axs[1, 0].set_title("(b) anomaly x parity cross-correlation")

names, zv = [], []
for k in ("cmb_dipole_l264_b48", "cmb_quad_oct_l250_b60"):
    names.append(k.replace("_", "\n")); zv.append(ax_[k]["vs_pixel_permutation_null"]["z"])
names.append("free\nbest-fit"); zv.append(ax_["free_best_fit_dipole"]["vs_pixel_permutation_max_null"]["z"])
axs[1, 1].bar(names, zv, color="C2")
for y in (-3.8, 3.8):
    axs[1, 1].axhline(y, color="r", ls=":", lw=0.8)
axs[1, 1].axhline(0, color="k", lw=0.6); axs[1, 1].set_ylabel("z vs null")
axs[1, 1].set_ylim(-4.5, 4.5); axs[1, 1].set_title("(d) parity dipole along axes")
f.suptitle("Row 16 (iv): chirality x structure - all pre-registered tests (dotted = 3.8 sigma local threshold)")
f.tight_layout()
f.savefig("chirality_structure_summary.png", dpi=140)
print("wrote chirality_structure_summary.png")
