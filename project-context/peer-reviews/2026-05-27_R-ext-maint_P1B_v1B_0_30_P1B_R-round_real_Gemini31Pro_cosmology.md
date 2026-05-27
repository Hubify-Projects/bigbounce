# P1B R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint_P1B_v1B_0_30
**Wall time**: 128.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=25319, completion=14143, reasoning=13455, total=39462

---

## PAPER-GEM-B1: BLOCKER
**Location:** Table 1B caption and Section V
**Issue:** The likelihood stack naively combines DES-Y5 and Pantheon+ SNIa compilations. These datasets share low-z anchor samples (e.g., Foundation, CfA) and calibration systematics; multiplying their likelihoods without a joint cross-covariance matrix double-counts data, artificially shrinking errors and inflating the $w_0, w_a$ tension.
**Fix:** Remove either DES-Y5 or Pantheon+ from the iter2 chain, or implement a rigorously constructed joint cross-covariance matrix.

## PAPER-GEM-B2: BLOCKER
**Location:** Section VI, "ALP field evolution"
**Issue:** The numerical integration of the ALP EOM is mathematically incorrect, overestimating field displacement by a factor of 2-4. Exact matter-domination solutions ($\phi \propto j_0(mt)$) yield $\Delta\phi/f_a \approx 0.15$ for $m=H_0$ and $\approx 0.43$ for $m=1.8H_0$, directly contradicting the claimed $0.65$ and $1.0$. This artificially inflates the predicted birefringence, invalidating the "natural parameter range" claim for $C_{a\gamma}$.
**Fix:** Recompute the ODE integration correctly and update the required $C_{a\gamma}$ ranges to reflect the physically smaller $\Delta\phi/f_a$ values.

## PAPER-GEM-M1: MAJOR
**Location:** Table 1B, fn 2 and Physics Interpretation
**Issue:** Quoting a $+4.3\sigma$ departure based on a 1D marginal extrapolation while explicitly acknowledging the $\Lambda$CDM point is unsampled by the chain is statistically invalid. MCMC posteriors for $w_0, w_a$ are highly non-Gaussian in the tails; Gaussian extrapolation of the core yields meaningless tail probabilities.
**Fix:** Report the 2D Mahalanobis distance accounting for the $w_0-w_a$ covariance, or remove the $\sigma$-tension claim entirely until the nested sampling run completes.

## PAPER-GEM-m1: minor
**Location:** Section III, paragraph 2
**Issue:** Describing the $M_{\rm Pl}^{-2}$-suppressed Hehl-Datta-Mercuri interaction as having a "scattering-amplitude shift" as its "leading Boltzmann effect" is physically misleading. At recombination temperatures, the interaction rate is $\Gamma/H \sim 10^{-80}$.
**Fix:** Explicitly state the interaction is completely decoupled at recombination, rather than implying it has a calculable but non-relativistic Boltzmann effect.

## PAPER-GEM-m2: minor
**Location:** Section VI, Eq 4
**Issue:** Performing a naive inverse-variance combination of Planck and ACT birefringence measurements ignores shared instrumental and galactic foreground systematics. Even as an "auxiliary cross-check," this is statistically unsound when a rigorous joint analysis (Eskilt et al.) already exists.
**Fix:** Delete the auxiliary inverse-variance combination (Eq 4) entirely and rely solely on the cited Eskilt et al. joint posterior.
