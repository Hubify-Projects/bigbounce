# P1B_v1B014_R10 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1300pt
**Wall time**: 117.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=18405, completion=13374, reasoning=12701, total=31779

---

I have reviewed the v1B.0.14 manuscript. The internal consistency of the newly extracted Table 1B posteriors is mathematically sound (error propagation, $\chi^2$ sums, and parameter counting are exact), and the scope-tightening directives from previous rounds have been correctly applied. 

I find **0 BLOCKERS**. The manuscript has reached fully-converged status on the physics-cosmology axis. I have identified 1 MAJOR methodological warning regarding a planned future computation, and 3 minor physical precision issues.

## PAPER-GEM-M1: MAJOR
**Location:** Section 3 (Physics interpretation) & Section 5.2
**Issue:** The text correctly acknowledges there are "zero free-$w_0 w_a$ samples at the LCDM point" because the nested model lies at $>4\sigma$ in the tails, yet simultaneously promises a "deterministic Savage-Dickey ratio on the converged 2D $(w, w_a)$ marginal is queued for v1B.0.13+". Savage-Dickey density estimation via KDE fails catastrophically (yielding arbitrary kernel-dependent noise) when the nested point is unsampled by the Metropolis-Hastings chain.
**Fix:** Remove the promise of an MCMC-based Savage-Dickey recompute. State explicitly that the $>4\sigma$ exclusion of LCDM necessitates dedicated Nested Sampling (e.g., PolyChord) or thermodynamic integration for a robust Bayes factor.

## PAPER-GEM-m1: minor
**Location:** Table 1B caption
**Issue:** The parameter count lists 8 cosmological + 9 CMB nuisance = 17 total parameters. However, the likelihood stack includes DES-Y5 and Pantheon+, which physically require at least one absolute magnitude or calibration nuisance parameter (e.g., $M_B$). 
**Fix:** Add a brief note confirming that SN nuisance parameters are analytically marginalized by the specific Cobaya likelihoods used, preventing the appearance of missing degrees of freedom.

## PAPER-GEM-m2: minor
**Location:** Section 3, Caveat (c)
**Issue:** The text states "$H_0$ is determined predominantly by the BAO+CMB acoustic scale through Pantheon+". This is physically backwards; BAO+CMB determines $H_0$ directly via the sound horizon $r_d$ calibration, which *opposes* the Pantheon+ & SH0ES $M_B$ calibration (which prefers a higher $H_0$).
**Fix:** Change "through Pantheon+" to "via the sound horizon, overpowering the Pantheon+ preference".

## PAPER-GEM-m3: minor
**Location:** Section 7.1
**Issue:** The text claims "Quintom-B is the only class admitted to span the dynamical-equation-of-state window". While canonical single-field models cannot cross the phantom divide $w=-1$ without ghosts, generalized single-field models (e.g., Horndeski theories with kinetic gravity braiding) can cross it stably.
**Fix:** Soften "the only class" to "the canonical scalar-field class" or specify that "standard single-field models cannot span" the window.
