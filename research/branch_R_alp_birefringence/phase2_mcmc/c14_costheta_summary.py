"""
c14 — R24conf QUEUE-31 (META-M3) post-processing.

Summarize the cosθ_i-flat-prior rerun of the c5 continuous-prior ALP fit:
C_aγ median / 16-84 range, β marginal, and the θ_i ≤ 0.1 spectator-sliver
posterior mass, compared against the flat-θ_i c5 anchors
(median 20.7, [7.3, 45.6], sliver 0.33%).

Output: chains/c14_costheta/c14_summary.json
"""
import glob
import json
import os

import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
CDIR = os.path.join(BASE, "chains", "c14_costheta")


def wquant(x, w, qs):
    i = np.argsort(x)
    x, w = x[i], w[i]
    c = np.cumsum(w) / w.sum()
    return [float(np.interp(q, c, x)) for q in qs]


rows = []
for cf in sorted(glob.glob(os.path.join(CDIR, "c14.*.txt"))):
    rows.append(np.loadtxt(cf))
a = np.concatenate(rows)
hdr = open(sorted(glob.glob(os.path.join(CDIR, "c14.*.txt")))[0]
           ).readline().replace("#", "").split()
w = a[:, hdr.index("weight")]
theta = a[:, hdr.index("theta_i")]
cag = a[:, hdr.index("C_agamma")]
beta = a[:, hdr.index("beta_deg")]

cag_16, cag_50, cag_84 = wquant(cag, w, [0.16, 0.50, 0.84])
beta_mu = float(np.average(beta, weights=w))
beta_sig = float(np.sqrt(np.average((beta - beta_mu) ** 2, weights=w)))
sliver = float(w[theta <= 0.1].sum() / w.sum())
n_raw = int(len(w))
n_sliver_raw = int((theta <= 0.1).sum())

out = {
    "experiment": ("c14 cosθ_i-flat-prior rerun of the c5 continuous-prior "
                   "ALP fit (R24conf QUEUE-31 / META-M3)"),
    "prior": ("p(theta_i) ∝ sin(theta_i) on (0.01, π) — flat in cosθ_i — via "
              "external log-prior 'lambda theta_i: np.log(np.sin(theta_i))'; "
              "all other priors/likelihood identical to c5.input.yaml"),
    "n_raw_samples": n_raw,
    "C_agamma": {"median": round(cag_50, 1),
                 "p16_p84": [round(cag_16, 1), round(cag_84, 1)]},
    "beta_deg": {"mean": round(beta_mu, 3), "sigma": round(beta_sig, 3)},
    "spectator_sliver_theta_le_0p1": {
        "mass_fraction": round(sliver, 5),
        "mass_percent": round(100 * sliver, 3),
        "n_raw_samples_in_sliver": n_sliver_raw},
    "flat_theta_c5_anchor": {"C_agamma_median": 20.7,
                             "C_agamma_p16_p84": [7.3, 45.6],
                             "sliver_mass_percent": 0.33},
}
with open(os.path.join(CDIR, "c14_summary.json"), "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
