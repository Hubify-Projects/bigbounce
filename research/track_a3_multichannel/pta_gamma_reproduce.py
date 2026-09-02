"""
Track A3 channel 1 — REPRODUCTION of the NANOGrav 15-yr HD-correlated
free-spectrum gamma posterior and its Savage-Dickey Bayes factors, from the
COMMITTED chain pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/
chain_real_freespec.npy (320,000 samples, 2 columns [gamma, log10A]).

This does NOT re-fit.  It re-derives every published summary number from the
committed chain and diffs against the two committed JSON records
(results.json and savage_dickey_2026-05-29.json), so that every PTA number
quoted in the A3 brief is labelled "reproduced", not "cited".

Method (identical to pipelines/p3_pta_mcmc/savage_dickey_2026-05-29.py):
  Savage-Dickey ratio for the nested point hypothesis gamma = gamma_*:
      B_{gamma_*/free} = p(gamma_* | d) / pi(gamma_*)
  with the sampling prior gamma ~ U[0,7]  =>  pi(gamma_*) = 1/7,
  and p(gamma_*|d) a 1-D Gaussian KDE (Scott bandwidth) on the gamma marginal.

Spectral-index conventions (h_c = characteristic strain):
      h_c(f) ~ f^{(3-gamma)/2}
      Omega_GW(f) = (2 pi^2 / 3 H_0^2) f^2 h_c(f)^2  ~  f^{5-gamma}
  so   gamma = 3    <->  Omega_GW ~ f^2   (causality-limited IR slope of a
                                           scalar-induced GW background; the
                                           matter-bounce SIGW prediction,
                                           Papanikolaou 2025 arXiv:2504.11641)
       gamma = 13/3 <->  Omega_GW ~ f^{2/3} (GW-driven SMBHB inspirals)
       gamma = 5    <->  Omega_GW ~ f^0    (scale-invariant primordial tensors,
                                            n_T = 0)
Note the matter-bounce gamma = 3 is NOT n_T = 0; it is the f^2 IR scaling of
the *induced* (second-order scalar-sourced) background.

Output: outputs/pta_gamma_reproduction.json
Venue: local (Apple silicon), no GPU, cost $0.
"""
from __future__ import annotations
import json, time, os
from pathlib import Path
import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CHAINDIR = REPO / "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01"
CHAIN = CHAINDIR / "chain_real_freespec.npy"
REF_RESULTS = CHAINDIR / "results.json"
REF_SD = CHAINDIR / "savage_dickey_2026-05-29.json"
OUT = HERE / "outputs/pta_gamma_reproduction.json"

GAMMA_MB = 3.0            # matter bounce, SIGW f^2 IR scaling
GAMMA_SMBHB = 13.0 / 3.0  # 4.3333, GW-driven SMBHB inspiral
GAMMA_INFL = 5.0          # scale-invariant primordial tensors, n_T = 0
G_LO, G_HI = 0.0, 7.0     # sampling prior on gamma


def main():
    t0 = time.time()
    chain = np.load(CHAIN)
    g, la = chain[:, 0], chain[:, 1]
    n = len(g)

    g_mu, g_sd, g_med = float(g.mean()), float(g.std()), float(np.median(g))
    q16, q84 = [float(x) for x in np.quantile(g, [0.16, 0.84])]

    kde = stats.gaussian_kde(g, bw_method="scott")
    prior = 1.0 / (G_HI - G_LO)
    post = {k: float(kde(v)[0]) for k, v in
            [("mb", GAMMA_MB), ("smbhb", GAMMA_SMBHB), ("infl", GAMMA_INFL)]}
    B = {k: v / prior for k, v in post.items()}

    z = {k: float((v - g_mu) / g_sd) for k, v in
         [("mb", GAMMA_MB), ("smbhb", GAMMA_SMBHB), ("infl", GAMMA_INFL)]}

    ref_r = json.loads(REF_RESULTS.read_text())
    ref_s = json.loads(REF_SD.read_text())
    ref_sd1 = ref_s["savage_dickey_1d_gamma_only_uniform_prior"]

    diffs = {
        "gamma_mean": abs(g_mu - ref_r["gamma"]["mean"]),
        "gamma_std": abs(g_sd - ref_r["gamma"]["std"]),
        "B_mb": abs(B["mb"] - ref_sd1["B_matter_bounce_vs_free"]),
        "B_smbhb": abs(B["smbhb"] - ref_sd1["B_smbhb_vs_free"]),
        "B_mb_over_smbhb": abs(B["mb"] / B["smbhb"]
                               - ref_sd1["B_matter_bounce_vs_smbhb"]),
        "z_smbhb": abs(z["smbhb"]
                       - ref_s["z_distances_gamma_marginal_gaussian"]["smbhb_13_3"]),
    }
    reproduced = all(
        d <= tol for d, tol in [
            (diffs["gamma_mean"], 1e-12), (diffs["gamma_std"], 1e-12),
            (diffs["B_mb"], 1e-9), (diffs["B_smbhb"], 1e-12),
            (diffs["B_mb_over_smbhb"], 1e-6), (diffs["z_smbhb"], 1e-9)])

    out = {
        "task": "Track A3 channel 1 — reproduce committed NANOGrav 15-yr "
                "free-spectrum gamma posterior + Savage-Dickey BFs",
        "chain": str(CHAIN.relative_to(REPO)),
        "chain_sha256_note": "see manifest",
        "n_samples": int(n),
        "gamma_marginal": {"mean": g_mu, "std": g_sd, "median": g_med,
                           "q16": q16, "q84": q84},
        "log10A_marginal": {"mean": float(la.mean()), "std": float(la.std())},
        "sampling_priors": {"gamma": "U[0,7]", "log10A": "U[-18,-11]"},
        "savage_dickey_1d": {
            "prior_density": prior,
            "posterior_at_gamma": post,
            "B_vs_free": B,
            "B_mb_over_smbhb": float(B["mb"] / B["smbhb"]),
            "log10_B_mb_over_smbhb": float(np.log10(B["mb"] / B["smbhb"])),
        },
        "z_distance_sigma": z,
        "omega_gw_slope_5_minus_gamma": {
            "matter_bounce_gamma3": 5.0 - GAMMA_MB,
            "smbhb_gamma13_3": 5.0 - GAMMA_SMBHB,
            "scale_invariant_tensors_gamma5": 5.0 - GAMMA_INFL,
        },
        "diff_vs_committed": diffs,
        "REPRODUCED": bool(reproduced),
        "wall_seconds": round(time.time() - t0, 2),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
