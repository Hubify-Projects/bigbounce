# P4_v1_0_108_R_INTERNAL R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1645pt
**Wall time**: 52.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=88437, completion=6439, reasoning=5597, total=94876

---

## PAPER-GEM-B1: Abstract and Conclusion contradict §IV.D multi-null battery
**Classification**: BLOCKER
**Location**: Abstract and Section VIII (Conclusions)
**Issue**: §IV.D introduces a +3.64σ canonical-mask residual under the binomial null, which is resolved to -0.22σ under the bootstrap null. However, the Abstract and Section VIII completely omit this new battery, still falsely claiming the peak canonical-mask residual is a "sub-detection-threshold +1.85σ" from the direct-MC. This creates a fatal internal contradiction regarding the paper's peak significance and its resolution.
**Fix**: Update the Abstract and Section VIII to explicitly state the canonical mask yields +3.64σ under a binomial null but collapses to -0.22σ under a bootstrap null, replacing the obsolete claim that +1.85σ is the peak canonical-mask excess.

## PAPER-GEM-M1: Mathematically false claim about bootstrap spatial correlations
**Classification**: MAJOR
**Location**: Section IV.D, bullet point (3)
**Issue**: The text claims the "bootstrap pixel resample (preserves spatial correlations of the data: each pixel's CW/CCW chirality contribution is sampled with replacement)". A standard pixel-level bootstrap with replacement destroys spatial off-diagonal covariance (neighboring pixels are randomized); it collapses the significance to -0.22σ because it preserves the empirical *marginal overdispersion* (variance) of the pixels, not their spatial correlation.
**Fix**: Change "preserves spatial correlations of the data" to "captures empirical per-pixel overdispersion and non-binomial variance driven by local systematics".

## PAPER-GEM-M2: Ambiguity in ℓ=2 > ℓ=1 diagnostic logic
**Classification**: MAJOR
**Location**: Section IV.D, bullet point (2)
**Issue**: The argument that $\sigma_{\ell=2} = +4.73 > \sigma_{\ell=1} = +3.63$ rules out a pure dipole is only rigorously true for MASTER-decoupled $C_\ell$. If these are raw pseudo-$C_\ell$ significances, mask coupling can theoretically alias a pure dipole into an $\ell=2$ pseudo-power larger than $\ell=1$ if the signal dipole perfectly aligns with the mask's dipole moment.
**Fix**: Explicitly specify whether the $\sigma_{\ell=1}$ and $\sigma_{\ell=2}$ values in the multipole spectrum diagnostic are pseudo-$C_\ell$ or MASTER-decoupled $C_\ell$ to make the physical argument rigorous.

## PAPER-GEM-m1: Table VII obsolete relative to §IV.D
**Classification**: minor
**Location**: Section VIII, Table VII
**Issue**: Table VII ("Three $\ell=1$ estimators on record") lists the Canonical-N direct-MC (+1.85σ) but omits the newly added Canonical-mask injection sweep (+3.64σ binomial / -0.22σ bootstrap), which is now the load-bearing canonical-mask evaluation in §IV.D.
**Fix**: Add a fourth row to Table VII for the "Canonical-mask injection sweep (binomial / bootstrap nulls)" with the +3.64σ / -0.22σ results to unify the estimators.

## PAPER-GEM-m2: Leaked internal review tags in manuscript text
**Classification**: minor
**Location**: Abstract, §IV.D, §IV.E
**Issue**: The LaTeX source contains raw internal review tracking tags embedded directly in the text (e.g., "P4-INTERNAL Gemini-B1 closure", "v1.0.107 Grok-B1 BLOCKER closure", "Houston directive: explore all 3 interpretations fully"). 
**Fix**: Strip all internal review tracking tags and meta-commentary from the manuscript text before arXiv submission.
