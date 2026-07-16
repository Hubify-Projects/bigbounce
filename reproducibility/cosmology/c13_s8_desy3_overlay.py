"""
c13 — R24conf QUEUE-28 (META-E1): GetDist overlay + quantification of the
frozen Planck+BAO+SN S8 posterior vs the DES-Y3 Gaussian 0.776 +/- 0.017,
with the full-tension S8 posterior on the same panel.

Outputs:
  reproducibility/cosmology/c13_s8_desy3_overlay.json
  reproducibility/cosmology/c13_s8_desy3_overlay.png
"""
import glob
import hashlib
import json
import os

import numpy as np
from getdist import loadMCSamples

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
DESY3_MU, DESY3_SIG = 0.776, 0.017
BURN_IN_FRACTION = 0.30
OUTPUT_STEM = os.environ.get("S8_OUTPUT_STEM", "c13_s8_desy3_overlay_postburn")


def load_dataset(frozen_dir, root="spin_torsion"):
    """Concatenate the 6 frozen single-chain dirs into one getdist sample."""
    chain_files = sorted(glob.glob(
        os.path.join(frozen_dir, "chains", "chain_*", f"{root}.1.txt")))
    samples, weights = [], []
    raw_samples = 0
    names = None
    for cf in chain_files:
        raw = loadMCSamples(cf[:-6], settings={"ignore_rows": 0})
        raw_samples += len(raw.samples)
        s = loadMCSamples(
            cf[:-6], settings={"ignore_rows": BURN_IN_FRACTION}
        )
        if names is None:
            names = [p.name for p in s.getParamNames().names]
        idx = names.index("S8")
        samples.append(s.samples[:, idx])
        weights.append(s.weights)
    s8 = np.concatenate(samples)
    w = np.concatenate(weights)
    return s8, w, len(chain_files), raw_samples


def wstats(x, w):
    mu = np.average(x, weights=w)
    sig = np.sqrt(np.average((x - mu) ** 2, weights=w))
    return float(mu), float(sig)


def kde_density(x, w, grid):
    """Weighted Gaussian KDE on a fixed grid (Silverman bandwidth)."""
    mu, sig = wstats(x, w)
    neff = w.sum() ** 2 / (w ** 2).sum()
    bw = 1.06 * sig * neff ** (-1 / 5)
    d = np.zeros_like(grid)
    # chunk to keep memory sane
    for i in range(0, len(x), 20000):
        xx, ww = x[i:i + 20000], w[i:i + 20000]
        d += (ww[None, :] * np.exp(
            -0.5 * ((grid[:, None] - xx[None, :]) / bw) ** 2)).sum(axis=1)
    d /= (w.sum() * bw * np.sqrt(2 * np.pi))
    return d


def gauss(grid, mu, sig):
    return np.exp(-0.5 * ((grid - mu) / sig) ** 2) / (sig * np.sqrt(2 * np.pi))


pbs_dir = os.path.join(BASE, "frozen", "planck_bao_sn_20260312_1954")
ft_dir = os.path.join(BASE, "frozen", "full_tension_20260311_1728")

s8_pbs, w_pbs, n_pbs, raw_pbs = load_dataset(pbs_dir)
s8_ft, w_ft, n_ft, raw_ft = load_dataset(ft_dir)

mu_pbs, sig_pbs = wstats(s8_pbs, w_pbs)
mu_ft, sig_ft = wstats(s8_ft, w_ft)

# --- two-Gaussian tension: Planck+BAO+SN vs DES-Y3 ---
tension_gauss = abs(mu_pbs - DESY3_MU) / np.hypot(sig_pbs, DESY3_SIG)

# --- posterior-overlap integral: int min(p1, p2) dS8 (KDE posterior vs Gaussian) ---
grid = np.linspace(0.70, 0.92, 4001)
p_pbs = kde_density(s8_pbs, w_pbs, grid)
p_des = gauss(grid, DESY3_MU, DESY3_SIG)
overlap = float(np.trapz(np.minimum(p_pbs, p_des), grid))

# same two metrics for the full-tension posterior vs DES-Y3 (context)
p_ft = kde_density(s8_ft, w_ft, grid)
tension_ft = abs(mu_ft - DESY3_MU) / np.hypot(sig_ft, DESY3_SIG)
overlap_ft = float(np.trapz(np.minimum(p_ft, p_des), grid))

# naive inverse-variance combination of PBS x DES-Y3 (paper Table I caption)
w1, w2 = 1 / sig_pbs ** 2, 1 / DESY3_SIG ** 2
naive_mu = (w1 * mu_pbs + w2 * DESY3_MU) / (w1 + w2)
naive_sig = (w1 + w2) ** -0.5
pull_ft_vs_naive = abs(mu_ft - naive_mu) / np.hypot(sig_ft, naive_sig)

out = {
    "experiment": ("c13 S8 overlay: frozen Planck+BAO+SN posterior vs DES-Y3 "
                   "Gaussian 0.776+/-0.017 (R24conf QUEUE-28 / META-E1)"),
    "chains": {
        "planck_bao_sn": {"dir": "reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954",
                          "n_chains": n_pbs, "raw_samples": raw_pbs,
                          "post_burn_samples": int(len(s8_pbs))},
        "full_tension": {"dir": "reproducibility/cosmology/frozen/full_tension_20260311_1728",
                         "n_chains": n_ft, "raw_samples": raw_ft,
                         "post_burn_samples": int(len(s8_ft))}},
    "status": "PASS",
    "burn_in_fraction": BURN_IN_FRACTION,
    "S8_definition": "sigma8*(Omega_m/0.3)^0.5 (chain derived column 'S8')",
    "planck_bao_sn_S8": {"mean": round(mu_pbs, 4), "sigma": round(sig_pbs, 4)},
    "full_tension_S8": {"mean": round(mu_ft, 4), "sigma": round(sig_ft, 4)},
    "des_y3_gaussian": {"mean": DESY3_MU, "sigma": DESY3_SIG},
    "two_gaussian_tension_pbs_vs_desy3_sigma": round(float(tension_gauss), 2),
    "posterior_overlap_integral_pbs_vs_desy3": round(overlap, 4),
    "two_gaussian_tension_fulltension_vs_desy3_sigma": round(float(tension_ft), 2),
    "posterior_overlap_integral_fulltension_vs_desy3": round(overlap_ft, 4),
    "naive_invvar_combination_pbs_x_desy3": {
        "mean": round(float(naive_mu), 4), "sigma": round(float(naive_sig), 4)},
    "fulltension_pull_vs_naive_combination_sigma": round(float(pull_ft_vs_naive), 2),
    "notes": ("Overlap integral = int min(p_chain_KDE, p_DESY3) dS8 in [0,1]; "
              "1 = identical, 0 = disjoint. Two-Gaussian tension = "
              "|mu1-mu2|/sqrt(s1^2+s2^2)."),
}

json_path = os.path.join(BASE, OUTPUT_STEM + ".json")
png_path = os.path.join(BASE, OUTPUT_STEM + ".png")
with open(json_path, "w") as f:
    json.dump(out, f, indent=1)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(grid, p_pbs, color="C0", lw=2,
        label=f"Planck+BAO+SN ({mu_pbs:.3f}$\\pm${sig_pbs:.3f})")
ax.plot(grid, p_ft, color="C2", lw=2,
        label=f"Full-tension ({mu_ft:.3f}$\\pm${sig_ft:.3f})")
ax.plot(grid, p_des, color="C3", lw=2, ls="--",
        label=f"DES-Y3 Gaussian ({DESY3_MU}$\\pm${DESY3_SIG})")
ax.fill_between(grid, np.minimum(p_pbs, p_des), color="0.7", alpha=0.5,
                label=f"overlap = {overlap:.3f}")
ax.set_xlabel(r"$S_8 \equiv \sigma_8\,(\Omega_m/0.3)^{1/2}$")
ax.set_ylabel("posterior density")
ax.set_xlim(0.72, 0.88)
ax.legend(fontsize=8, frameon=False)
ax.set_title(f"$S_8$: Planck+BAO+SN vs DES-Y3 "
             f"({tension_gauss:.1f}$\\sigma$ two-Gaussian)", fontsize=10)
fig.tight_layout()
fig.savefig(png_path, dpi=160)
with open(json_path, "rb") as handle:
    result_sha256 = hashlib.sha256(handle.read()).hexdigest()
receipt = {
    "schema_version": 1,
    "status": "PASS",
    "result_file": os.path.basename(json_path),
    "result_sha256": result_sha256,
    "burn_in_fraction": BURN_IN_FRACTION,
    "raw_samples": raw_pbs + raw_ft,
    "post_burn_samples": len(s8_pbs) + len(s8_ft),
}
with open(json_path + ".receipt.json", "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
print(json.dumps(out, indent=1))
