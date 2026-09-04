"""
P3-CM-B3: emcee on the REAL NANOGrav 15-yr HD-correlated free-spectrum KDE
likelihood (Zenodo 8060824), replacing the synthetic-from-power-law fit in
nanograv_ptarcade.py.

Likelihood:
  density[0, bin, :] is log p(log10_rho = log10_rho_grid[k] | bin)
  log L(theta=[gamma, log10_A]) = sum_bin interp(grid, density[0,bin,:],
                                                  log10_rho_pred(bin; theta))

Power-law model (Ceffyl/PTArcade convention; T_obs encoded via f_1 = 1/T_obs):
  rho^2_i(gamma, A) = (A^2 / (12 pi^2)) * (f_i)^(-gamma) * f_yr^(gamma - 3) / T_obs
  log10_rho_i = 0.5 * [2*log10_A - log10(12 pi^2)
                       + (gamma - 3) * log10(f_yr) - gamma * log10(f_i)
                       - log10(T_obs)]

MCMC hyperparameters match nanograv_ptarcade.py: 32 walkers x 10,000
production + 2,500 burn-in. Priors:
  gamma ~ U[0, 7]
  log10_A ~ U[-18, -11]

Set BIGBOUNCE_WORKSPACE to run outside the original RunPod pod (default: /workspace).
"""
import json
import os
import time
import numpy as np
import emcee

WORKSPACE = os.environ.get("BIGBOUNCE_WORKSPACE", "/workspace")
ROOT = f"{WORKSPACE}/p3_realfreespec/kde/30f_fs{{hd}}_ceffyl"
OUT_DIR = f"{WORKSPACE}/p3_realfreespec/results"
os.makedirs(OUT_DIR, exist_ok=True)

# ---- Load KDE pack ----
freqs_Hz = np.load(f"{ROOT}/freqs.npy")
log10rho_grid = np.load(f"{ROOT}/log10rhogrid.npy")
log_density = np.load(f"{ROOT}/density.npy")  # shape (1, 30, 10000)
log_density = log_density[0]  # -> (30, 10000)
N_BINS = freqs_Hz.shape[0]
T_obs = 1.0 / freqs_Hz[0]
print(f"[load] N_BINS={N_BINS}  T_obs={T_obs:.3e} s = {T_obs/(365.25*86400):.2f} yr")
print(f"[load] freqs range: {freqs_Hz.min():.3e} - {freqs_Hz.max():.3e} Hz")
print(f"[load] log10rho_grid: {log10rho_grid.min():.2f} - {log10rho_grid.max():.2f}")
print(f"[load] log_density shape: {log_density.shape}, peak per bin (first 5):")
for i in range(5):
    k_peak = int(np.argmax(log_density[i]))
    print(f"        bin {i}: peak at log10_rho={log10rho_grid[k_peak]:+.3f}  "
          f"log_p_peak={log_density[i, k_peak]:.2f}")

YR = 365.25 * 86400.0
F_YR = 1.0 / YR
LOG10_12PI2 = np.log10(12.0 * np.pi ** 2)
LOG10_F_YR = np.log10(F_YR)
LOG10_T_OBS = np.log10(T_obs)
LOG10_FREQS = np.log10(freqs_Hz)

# ---- Pre-extend the grid with -inf padding so out-of-range model points are ----
# disallowed (returns -np.inf). Use np.interp's edge-clamp behavior carefully.
GRID_LO = log10rho_grid.min()
GRID_HI = log10rho_grid.max()


def model_log10rho(theta):
    gamma, log10_A = theta
    return 0.5 * (2.0 * log10_A
                  - LOG10_12PI2
                  + (gamma - 3.0) * LOG10_F_YR
                  - gamma * LOG10_FREQS
                  - LOG10_T_OBS)


def log_prior(theta):
    gamma, log10_A = theta
    if not (0.0 <= gamma <= 7.0):
        return -np.inf
    if not (-18.0 <= log10_A <= -11.0):
        return -np.inf
    return 0.0


def log_likelihood(theta):
    pred = model_log10rho(theta)
    if np.any(pred < GRID_LO + 0.05) or np.any(pred > GRID_HI - 0.05):
        return -np.inf
    total = 0.0
    for i in range(N_BINS):
        # Linear interp on log_density at pred[i]
        total += np.interp(pred[i], log10rho_grid, log_density[i])
    return total


def log_prob(theta):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta)


def main():
    n_walkers = 32
    n_burn = 2500
    n_prod = 10000
    ndim = 2

    rng = np.random.default_rng(42)
    p0_gamma = rng.uniform(2.0, 5.0, n_walkers)
    p0_logA = rng.uniform(-15.5, -13.5, n_walkers)
    p0 = np.column_stack([p0_gamma, p0_logA])

    print(f"\n[mcmc] sanity check at default (gamma=3.2, log10_A=-14.6):")
    print(f"        log10_rho_pred(first 5) = {model_log10rho([3.2, -14.6])[:5]}")
    print(f"        log_likelihood = {log_likelihood([3.2, -14.6]):.3f}")
    print(f"        log10_rho_pred(SMBHB γ=4.33, log10_A=-14.6) "
          f"first 5 = {model_log10rho([13./3., -14.6])[:5]}")
    print(f"        log_likelihood = {log_likelihood([13./3., -14.6]):.3f}")

    sampler = emcee.EnsembleSampler(n_walkers, ndim, log_prob)

    print(f"\n[mcmc] burn-in {n_burn} steps, {n_walkers} walkers...")
    t0 = time.time()
    state = sampler.run_mcmc(p0, n_burn, progress=False)
    print(f"[mcmc] burn-in done in {time.time()-t0:.1f}s. "
          f"acceptance: mean={np.mean(sampler.acceptance_fraction):.3f}")
    sampler.reset()

    print(f"[mcmc] production {n_prod} steps...")
    t0 = time.time()
    sampler.run_mcmc(state, n_prod, progress=False)
    dt = time.time() - t0
    print(f"[mcmc] production done in {dt:.1f}s. "
          f"acceptance: mean={np.mean(sampler.acceptance_fraction):.3f}")

    chain = sampler.get_chain(flat=True)  # (n_walkers*n_prod, 2)
    print(f"[mcmc] chain shape: {chain.shape}")

    try:
        tau = sampler.get_autocorr_time(quiet=True)
        print(f"[mcmc] autocorr time tau (gamma, log10A) = {tau}")
        ess = (n_prod * n_walkers) / np.max(tau)
        print(f"[mcmc] ESS = {ess:.0f}")
    except Exception as e:
        print(f"[mcmc] autocorr failed: {e}")
        tau = None
        ess = None

    g_mean = float(np.mean(chain[:, 0]))
    g_std = float(np.std(chain[:, 0]))
    g_med = float(np.median(chain[:, 0]))
    g_q16, g_q84 = [float(x) for x in np.quantile(chain[:, 0], [0.16, 0.84])]
    A_mean = float(np.mean(chain[:, 1]))
    A_std = float(np.std(chain[:, 1]))
    A_med = float(np.median(chain[:, 1]))

    np.save(f"{OUT_DIR}/chain_real_freespec.npy", chain)

    out = {
        "task": "P3-CM-B3 NANOGrav 15-yr HD-correlated free-spectrum REAL emcee fit",
        "dataset": "Zenodo 10.5281/zenodo.8060824 (KDE Free Spectra v1.0.0) "
                   "-> 30f_fs{hd}_ceffyl",
        "n_bins": int(N_BINS),
        "T_obs_yr": float(T_obs / YR),
        "n_walkers": int(n_walkers),
        "n_burn": int(n_burn),
        "n_prod": int(n_prod),
        "n_samples": int(chain.shape[0]),
        "production_seconds": float(dt),
        "gamma": {
            "mean": g_mean, "std": g_std, "median": g_med,
            "q16": g_q16, "q84": g_q84,
        },
        "log10_A": {
            "mean": A_mean, "std": A_std, "median": A_med,
        },
        "autocorr_tau": tau.tolist() if tau is not None else None,
        "ess": ess,
        "acceptance_fraction_mean": float(
            np.mean(sampler.acceptance_fraction)),
        "compare_synthetic_powerlaw": {
            "synth_gamma_mean": 3.1925,
            "synth_gamma_std": 0.4233,
            "delta_sigma": (g_mean - 3.1925) / max(g_std, 0.4233),
            "agazie_2023_official": {
                "gamma": 3.2, "gamma_err": 0.6,
            },
        },
    }
    with open(f"{OUT_DIR}/results.json", "w") as f:
        json.dump(out, f, indent=2)

    print("\n=== HEADLINE ===")
    print(f"  gamma = {g_mean:.4f} +/- {g_std:.4f}  "
          f"(median {g_med:.4f}, 68% CI [{g_q16:.3f}, {g_q84:.3f}])")
    print(f"  log10_A = {A_mean:.4f} +/- {A_std:.4f}")
    print(f"  delta_sigma vs synth-power-law gamma=3.1925+/-0.4233: "
          f"{out['compare_synthetic_powerlaw']['delta_sigma']:+.3f}")
    print(f"\n[done] artifacts written to {OUT_DIR}/")


if __name__ == "__main__":
    main()
