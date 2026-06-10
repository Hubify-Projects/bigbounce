"""
c10a — Spectator-safe C_agamma slice of the c5 continuous-prior chain.

Closes P1B R23conf META-M7: quantify the C_agamma band required in the
explicitly spectator-safe subset theta_i <= 0.1 of the committed c5 chain
(chains/c5_continuous/c5.[1-4].txt; flat priors C_agamma in [4,60],
theta_i in [0.01, pi], log10(m_a/eV) in [-35,-30]; Gaussian summary
likelihood beta_obs = 0.342 +/- 0.094 deg).

Method: weighted (Cobaya MC weight column) posterior-mass fraction at
theta_i <= 0.1, plus weighted 16/50/84 percentiles of C_agamma inside the
slice. No burn-in removal: the on-disk chains already exclude burn-in
(sampler burn_in: 0.3 per c5.updated.yaml; 8,955 samples total, matching
the paper's quoted accepted-sample count).

Output: c10a_spectator_slice.json in this directory.
"""

import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CHAIN_DIR = os.path.join(HERE, "chains", "c5_continuous")
THETA_CUT = 0.1

# Column order from chain headers / c5.updated.yaml:
# weight minuslogpost theta_i log10_m_eV C_agamma beta_deg eta Omega_a w_a_0 ...
COL_WEIGHT, COL_THETA, COL_CAG, COL_BETA, COL_OMEGA_A = 0, 2, 4, 5, 7


def weighted_percentile(values, weights, q):
    """Weighted percentile (q in [0,100]) via cumulative-weight interpolation."""
    order = np.argsort(values)
    v, w = values[order], weights[order]
    cw = np.cumsum(w) - 0.5 * w
    cw /= np.sum(w)
    return float(np.interp(q / 100.0, cw, v))


def main():
    chunks = []
    files = sorted(
        f for f in os.listdir(CHAIN_DIR)
        if f.startswith("c5.") and f.endswith(".txt")
    )
    for f in files:
        chunks.append(np.loadtxt(os.path.join(CHAIN_DIR, f)))
    data = np.vstack(chunks)

    w = data[:, COL_WEIGHT]
    theta = data[:, COL_THETA]
    cag = data[:, COL_CAG]

    mask = theta <= THETA_CUT
    n_raw = int(mask.sum())
    mass_frac = float(w[mask].sum() / w.sum())

    out = {
        "input_chains": files,
        "n_samples_total": int(len(data)),
        "theta_i_cut": THETA_CUT,
        "n_raw_samples_in_slice": n_raw,
        "posterior_mass_fraction_in_slice": mass_frac,
    }
    if n_raw > 0:
        out["C_agamma_slice_percentiles"] = {
            "p16": weighted_percentile(cag[mask], w[mask], 16),
            "p50": weighted_percentile(cag[mask], w[mask], 50),
            "p84": weighted_percentile(cag[mask], w[mask], 84),
        }
        out["C_agamma_slice_min_max"] = [float(cag[mask].min()),
                                         float(cag[mask].max())]
        out["beta_deg_slice_percentiles"] = {
            "p16": weighted_percentile(data[:, COL_BETA][mask], w[mask], 16),
            "p50": weighted_percentile(data[:, COL_BETA][mask], w[mask], 50),
            "p84": weighted_percentile(data[:, COL_BETA][mask], w[mask], 84),
        }

    out_path = os.path.join(HERE, "c10a_spectator_slice.json")
    with open(out_path, "w") as fh:
        json.dump(out, fh, indent=2)
    print(json.dumps(out, indent=2))
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
