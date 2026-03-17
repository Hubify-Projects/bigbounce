# Compute Decision

**Date:** 2026-03-17

---

## Should we run any more MCMC for Branch R now?

**NO.**

---

## Why Not

### 1. The existing runs are sufficient for the paper's needs.

The ALP is no longer the primary anchor — it is a supporting payoff within a broader closure assessment. The existing 3 runs provide:
- Run 1: Posterior on (θ_i, m) with C=8 → θ_i = 1.36 ± 0.44 (the headline number)
- Run 2: Degeneracy mapping with C free → C × θ_i ~ 10.6 (confirms SM value is consistent)
- Run 3: Free-β baseline → demonstrates ALP = free β statistically

These are complete, converged (R̂-1 < 0.01), and answer every question the paper needs.

### 2. Run 4 (Planck+BAO joint) would not change the ALP conclusion.

The spectator ALP decouples from standard cosmological parameters by construction. A joint fit would show zero correlation between θ_i and (H_0, Ω_m, σ_8) — a non-result. The compute cost (~$30, ~25 hours) is not justified for a figure that confirms the null hypothesis.

### 3. Our MCMC cannot compete with Namikawa+ 2025.

They use the full Planck EB power spectrum with multi-frequency likelihood. Our single-Gaussian likelihood (β_obs ± σ) is fundamentally less informative. Running more samples or adding more parameters will not close this gap. The gap is in DATA TREATMENT, not in sampling.

### 4. The marginal return on additional runs is near zero.

| Possible Run | What it adds | Value to paper |
|-------------|-------------|----------------|
| Run 4 (Planck+BAO) | H_0, Ω_m posteriors; confirms decoupling | LOW (already known by construction) |
| Run 5 (ALP-as-DE) | w(z) constraints | LOW (rolling-vs-freezing tension already shown) |
| Run 6 (Updated data) | Updated β_obs (ACT DR6 standalone) | MARGINAL (changes β by ~0.1°) |
| Run 7 (EB spectrum) | Mass exclusions from spectrum shape | HIGH but IMPOSSIBLE (requires Planck pixel-level data we don't have) |

The only run that would add substantial value (Run 7) requires data access we don't have. The runs we CAN do don't change the story.

---

## What to do instead

1. **Spend time on the closure assessment.** This is where the real novelty lies. Every hour polishing the 13-barrier catalog, the branch structure, and the failure-mode taxonomy adds more to the paper than another MCMC run.

2. **Create the 5 priority figures.** The barrier map, rolling efficiency curve, and β vs θ_i prediction plot will do more for the paper's impact than additional chains.

3. **Draft the paper.** The science is done. More compute is a procrastination strategy at this point.

---

## Verdict: NO MORE MCMC.

The existing 3 runs are sufficient. Proceed to writing.
