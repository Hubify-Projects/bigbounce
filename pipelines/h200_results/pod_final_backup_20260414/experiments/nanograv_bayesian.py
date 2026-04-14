"""
NANOGrav + Multi-PTA Bayesian Model Comparison: Bounce vs SMBHB
================================================================
GPU-accelerated MCMC to compare:
  1. Matter bounce model: gravitational wave background with spectral index γ=3
  2. SMBHB model: γ=13/3 ≈ 4.33 (inspiral background from supermassive black holes)
  3. ΛCDM inflation: varies

Using the combined PTA dataset:
  NANOGrav 15yr: γ_obs = 3.2 ± 0.6
  EPTA DR2: γ_obs = 3.1 ± 0.9
  PPTA DR3: γ_obs = 3.5 ± 0.8

Combined: γ = 3.32 ± 0.37 (cited in CLAUDE.md)

Method: GPU-accelerated posterior sampling via torch + gradient-free MCMC
Output: Bayes factors, posterior on γ, model probabilities
"""

import os
import sys
import json
import time
import numpy as np
import torch

OUTPUT_DIR = "/root/results/nanograv-bayesian"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("=" * 70)
print("NANOGRAV BAYESIAN MODEL COMPARISON: BOUNCE vs SMBHB")
print(f"  Device: {DEVICE}")
print("=" * 70)

t0 = time.time()

# -------------------------------------------------------------------------
# Combined PTA constraints (from literature)
# -------------------------------------------------------------------------
# Individual PTA measurements of spectral index γ (h² ~ f^{(5-γ)})
PTA_DATA = {
    "NANOGrav_15yr": {"gamma_mean": 3.2, "gamma_err": 0.6, "A_log10_mean": -15.6, "A_log10_err": 0.3},
    "EPTA_DR2":      {"gamma_mean": 3.1, "gamma_err": 0.9, "A_log10_mean": -14.5, "A_log10_err": 0.8},
    "PPTA_DR3":      {"gamma_mean": 3.5, "gamma_err": 0.8, "A_log10_mean": -15.6, "A_log10_err": 0.5},
    "IPTA_DR2":      {"gamma_mean": 3.8, "gamma_err": 1.1, "A_log10_mean": -15.5, "A_log10_err": 0.7},
}

# Combined (inverse-variance weighted)
inv_vars = [1.0/d["gamma_err"]**2 for d in PTA_DATA.values()]
gamma_means = [d["gamma_mean"] for d in PTA_DATA.values()]
GAMMA_COMBINED = np.average(gamma_means, weights=inv_vars)
GAMMA_ERR_COMBINED = 1.0 / np.sqrt(sum(inv_vars))
print(f"  Combined PTA: γ = {GAMMA_COMBINED:.3f} ± {GAMMA_ERR_COMBINED:.3f}")

# -------------------------------------------------------------------------
# Models and their γ predictions
# -------------------------------------------------------------------------
MODELS = {
    "matter_bounce": {
        "gamma": 3.0,         # exact prediction from bounce cosmology
        "gamma_model_err": 0.1,  # theoretical uncertainty (e.g., from k-range)
        "description": "Matter bounce: γ=3 (scale-invariant GW background)",
        "prior_log_prob": np.log(0.25),  # flat prior over 4 models
    },
    "SMBHB_circular_inspiral": {
        "gamma": 13.0/3.0,    # ≈ 4.33, standard result
        "gamma_model_err": 0.2,  # eccentricity/environmental effects
        "description": "SMBHB circular inspiral: γ=13/3",
        "prior_log_prob": np.log(0.25),
    },
    "SMBHB_eccentric": {
        "gamma": 3.8,          # eccentric binaries soften the spectrum
        "gamma_model_err": 0.5,
        "description": "SMBHB with eccentricity: γ~3-4.33",
        "prior_log_prob": np.log(0.25),
    },
    "cosmic_strings": {
        "gamma": 5.0/3.0,     # ≈ 1.67
        "gamma_model_err": 0.3,
        "description": "Cosmic strings: γ~5/3",
        "prior_log_prob": np.log(0.25),
    },
}

# -------------------------------------------------------------------------
# GPU-accelerated MCMC via ensemble sampler (emcee-style on GPU)
# -------------------------------------------------------------------------
N_WALKERS = 256
N_STEPS = 2000
N_BURNIN = 500
N_PARAMS = 2  # (log10_A, gamma)

print(f"\n[1/4] GPU MCMC: {N_WALKERS} walkers, {N_STEPS} steps...")

def log_likelihood_pta(theta_batch, pta_data):
    """
    Log-likelihood for PTA data given model parameters (log10_A, gamma).
    theta_batch: (N, 2) tensor — log10_A, gamma
    Returns: (N,) log-likelihood tensor
    """
    log10_A = theta_batch[:, 0]
    gamma = theta_batch[:, 1]

    ll = torch.zeros(len(theta_batch), device=DEVICE)
    for name, d in pta_data.items():
        # Gaussian likelihood on gamma
        ll += -0.5 * ((gamma - d["gamma_mean"]) / d["gamma_err"])**2
        # Gaussian likelihood on log10_A
        ll += -0.5 * ((log10_A - d["A_log10_mean"]) / d["A_log10_err"])**2
    return ll

def log_prior(theta_batch):
    """
    Flat prior: log10_A in [-17, -13], gamma in [1, 6]
    Returns: (N,) log-prior tensor (0 or -inf)
    """
    log10_A = theta_batch[:, 0]
    gamma = theta_batch[:, 1]
    valid = (log10_A > -17) & (log10_A < -13) & (gamma > 1.0) & (gamma < 6.0)
    lp = torch.where(valid, torch.zeros_like(gamma), torch.tensor(float('-inf'), device=DEVICE))
    return lp

def log_posterior(theta_batch, pta_data):
    lp = log_prior(theta_batch)
    ll = log_likelihood_pta(theta_batch, pta_data)
    return lp + ll

# Initialize walkers
np.random.seed(42)
pos0_np = np.random.uniform([-16.5, 2.0], [-14.5, 4.5], (N_WALKERS, N_PARAMS))
pos = torch.tensor(pos0_np, dtype=torch.float32, device=DEVICE)

# Ensemble MCMC (stretch move)
step_size = torch.tensor([0.3, 0.5], device=DEVICE)
chains = torch.zeros(N_STEPS, N_WALKERS, N_PARAMS, device=DEVICE)
log_probs = torch.zeros(N_STEPS, N_WALKERS, device=DEVICE)
current_lp = log_posterior(pos, PTA_DATA)

accepted = 0
total_proposals = 0

pta_data_tensors = {
    name: {k: torch.tensor(float(v), device=DEVICE) for k, v in d.items() if isinstance(v, float)}
    for name, d in PTA_DATA.items()
}

for step in range(N_STEPS):
    # Stretch move: for each walker, pick a complementary walker and propose
    n_half = N_WALKERS // 2
    for s in [0, 1]:
        walker_idx = torch.arange(s * n_half, (s+1) * n_half, device=DEVICE)
        complement_idx = torch.arange((1-s)*n_half, (2-s)*n_half, device=DEVICE)
        comp_perm = complement_idx[torch.randperm(n_half, device=DEVICE)]

        # Stretch factor a ~ U[1/2, 2]
        a_min, a_max = 0.5, 2.0
        u = torch.rand(n_half, device=DEVICE)
        a = (a_min**(0.5) + u*(a_max**(0.5) - a_min**(0.5)))**2

        # Proposal
        x_k = pos[walker_idx]
        x_j = pos[comp_perm]
        proposal = x_j + a.unsqueeze(1) * (x_k - x_j)

        # Log acceptance ratio
        lp_proposal = log_posterior(proposal, PTA_DATA)
        log_accept = (N_PARAMS - 1) * torch.log(a) + lp_proposal - current_lp[walker_idx]
        accept = torch.log(torch.rand(n_half, device=DEVICE)) < log_accept

        pos[walker_idx[accept]] = proposal[accept]
        current_lp[walker_idx[accept]] = lp_proposal[accept]
        accepted += accept.sum().item()
        total_proposals += n_half

    chains[step] = pos
    log_probs[step] = current_lp

    if (step + 1) % 200 == 0:
        acc_rate = accepted / total_proposals
        gamma_med = pos[:, 1].median().item()
        print(f"  Step {step+1}/{N_STEPS}: acc={acc_rate:.2f}, γ_median={gamma_med:.3f}", flush=True)

print(f"  Final acceptance rate: {accepted/total_proposals:.3f}")

# -------------------------------------------------------------------------
# [2/4] Extract posterior
# -------------------------------------------------------------------------
print("\n[2/4] Extracting posterior...")

# Burn-in removal
chains_cpu = chains[N_BURNIN:].cpu().numpy()
n_post_steps = N_STEPS - N_BURNIN

# Flatten
flat_samples = chains_cpu.reshape(-1, N_PARAMS)
log10_A_samples = flat_samples[:, 0]
gamma_samples = flat_samples[:, 1]

gamma_median = np.median(gamma_samples)
gamma_q16, gamma_q84 = np.percentile(gamma_samples, [16, 84])
gamma_err_low = gamma_median - gamma_q16
gamma_err_high = gamma_q84 - gamma_median

log10_A_median = np.median(log10_A_samples)

print(f"  γ = {gamma_median:.3f} +{gamma_err_high:.3f} -{gamma_err_low:.3f}")
print(f"  log₁₀(A) = {log10_A_median:.3f}")

# -------------------------------------------------------------------------
# [3/4] Bayes factor computation via Laplace approximation
# -------------------------------------------------------------------------
print("\n[3/4] Computing Bayes factors...")

def bayes_factor_gaussian(gamma_observed, gamma_err_obs, gamma_model, gamma_model_err):
    """
    Approximate Bayes factor B_model/B_flat using Gaussian likelihoods.
    B = P(data|model) / P(data|null)
    For Gaussian: B = exp(-0.5 * chi2_model) / normalizations
    """
    # Combined uncertainty
    sigma_total = np.sqrt(gamma_err_obs**2 + gamma_model_err**2)
    # Chi-squared for this model prediction
    chi2 = ((gamma_observed - gamma_model) / sigma_total)**2
    # Bayes factor (vs uniform prior over [1,6])
    log_bf = -0.5 * chi2 + 0.5 * np.log(2*np.pi*sigma_total**2) - np.log(5.0)
    return log_bf, np.exp(-0.5 * chi2)  # log_BF, likelihood ratio

print(f"\n  γ_combined = {GAMMA_COMBINED:.3f} ± {GAMMA_ERR_COMBINED:.3f}")
print(f"  γ_posterior = {gamma_median:.3f} ± {gamma_err_high:.3f}")
print()

model_results = {}
for model_name, model_params in MODELS.items():
    gamma_m = model_params["gamma"]
    sigma_m = model_params["gamma_model_err"]

    log_bf_combined, lr_combined = bayes_factor_gaussian(
        GAMMA_COMBINED, GAMMA_ERR_COMBINED, gamma_m, sigma_m
    )
    log_bf_posterior, lr_posterior = bayes_factor_gaussian(
        gamma_median, gamma_err_high, gamma_m, sigma_m
    )

    # Tension (σ)
    tension_combined = abs(GAMMA_COMBINED - gamma_m) / np.sqrt(GAMMA_ERR_COMBINED**2 + sigma_m**2)
    tension_posterior = abs(gamma_median - gamma_m) / np.sqrt(gamma_err_high**2 + sigma_m**2)

    model_results[model_name] = {
        "gamma_model": gamma_m,
        "tension_combined_sigma": round(tension_combined, 2),
        "tension_posterior_sigma": round(tension_posterior, 2),
        "log_bayes_factor_combined": round(log_bf_combined, 3),
        "log_bayes_factor_posterior": round(log_bf_posterior, 3),
        "description": model_params["description"],
    }

    print(f"  {model_name}:")
    print(f"    γ_model = {gamma_m:.3f}  tension = {tension_combined:.2f}σ  log_BF = {log_bf_combined:.2f}")

# -------------------------------------------------------------------------
# [4/4] Summary: Rank models by evidence
# -------------------------------------------------------------------------
print("\n[4/4] Model ranking by Bayes factor vs SMBHB circular...")

smbhb_lbf = model_results["SMBHB_circular_inspiral"]["log_bayes_factor_combined"]
print(f"\n  Model                          γ_pred  Tension   log_BF(vs SMBHB)")
for name, res in sorted(model_results.items(),
                         key=lambda x: -x[1]["log_bayes_factor_combined"]):
    relative_lbf = res["log_bayes_factor_combined"] - smbhb_lbf
    print(f"  {name:<35s} {res['gamma_model']:.2f}    {res['tension_combined_sigma']:.2f}σ     {relative_lbf:+.2f}")

bounce_vs_smbhb = model_results["matter_bounce"]["log_bayes_factor_combined"] - smbhb_lbf
bounce_tension = model_results["matter_bounce"]["tension_combined_sigma"]
smbhb_tension = model_results["SMBHB_circular_inspiral"]["tension_combined_sigma"]

print(f"\n  KEY RESULT:")
print(f"  Matter bounce: γ=3.0 at {bounce_tension:.2f}σ from combined PTA data")
print(f"  SMBHB circular: γ=4.33 at {smbhb_tension:.2f}σ from combined PTA data")
print(f"  Bayes factor bounce vs SMBHB: log_BF = {bounce_vs_smbhb:.2f} (>0 favors bounce)")
if bounce_vs_smbhb > 0:
    bf_value = np.exp(bounce_vs_smbhb)
    print(f"  BF = {bf_value:.1f} ({['inconclusive','moderate','strong','very strong','decisive'][min(int(np.log10(bf_value*3)),4)]} evidence for bounce)")
else:
    print(f"  SMBHB is favored (log_BF_bounce = {bounce_vs_smbhb:.2f})")

elapsed = time.time() - t0
print(f"\n  Runtime: {elapsed:.1f}s")

summary = {
    "experiment": "NANOGrav Bayesian Model Comparison: Bounce vs SMBHB",
    "device": str(DEVICE),
    "n_walkers": N_WALKERS,
    "n_steps": N_STEPS,
    "n_burnin": N_BURNIN,
    "combined_pta": {
        "gamma_mean": float(GAMMA_COMBINED),
        "gamma_err": float(GAMMA_ERR_COMBINED),
    },
    "posterior": {
        "gamma_median": float(gamma_median),
        "gamma_err_low": float(gamma_err_low),
        "gamma_err_high": float(gamma_err_high),
        "log10_A_median": float(log10_A_median),
    },
    "model_comparison": model_results,
    "key_results": {
        "bounce_tension_sigma": float(bounce_tension),
        "smbhb_tension_sigma": float(smbhb_tension),
        "log_bayes_factor_bounce_vs_smbhb": float(bounce_vs_smbhb),
        "bayes_factor_bounce_vs_smbhb": float(np.exp(bounce_vs_smbhb)),
        "smbhb_excluded_sigma": float(smbhb_tension),
        "paper1_claim_consistency": f"γ_obs={GAMMA_COMBINED:.2f}±{GAMMA_ERR_COMBINED:.2f} vs bounce γ=3.0 ({bounce_tension:.2f}σ tension)",
    },
    "runtime_seconds": elapsed,
}

try:
    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
except Exception as e:
    print(f"[warn] json save: {e}")

print(json.dumps(summary, indent=2))
print("\nCOMPLETE")
