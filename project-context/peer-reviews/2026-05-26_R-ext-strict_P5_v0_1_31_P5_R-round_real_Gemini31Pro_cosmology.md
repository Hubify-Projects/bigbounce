# P5 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P5_v0_1_31
**Wall time**: 35.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=27218, completion=3246, reasoning=2487, total=30464

---

## PAPER-GEM-B1: AI-Vendor Audit Trail Contamination in Abstract
**Class:** BLOCKER
**Section:** Abstract
**Issue:** The abstract contains leaked internal AI-vendor review prose: "...supporting rather than load-bearing per R-ext-GRO-M2: the primary robustness evidence is...". This is unacceptable for journal submission.
**Fix:** Purge the "per R-ext-GRO-M2" tag and any associated version-history conversational text from the abstract.

## PAPER-GEM-B2: AI-Vendor Audit Trail Contamination in Conclusions
**Class:** BLOCKER
**Section:** XII. Conclusions
**Issue:** The main text contains explicit version-history and AI-vendor tagging: "...must satisfy (R-ext-GRO-min1 reframing from prior "clean environment-dependent constraint"); it does not constrain...". 
**Fix:** Delete the parenthetical audit-trail note entirely to restore publication-grade academic prose.

## PAPER-GEM-M1: Insufficient Monte Carlo Size for Headline p-values
**Class:** MAJOR
**Section:** VI.B (Redshift dependence) and VI.E (Sky-position regional coherence)
**Issue:** The empirical max-stat MC nulls are computed using only 1,000 label-shuffle permutations (yielding $p=0.372$ and $p=0.135$). A sample size of $N_{\rm MC} < 10^4$ is insufficient for headline cosmological p-values and leaves the tail distributions undersampled.
**Fix:** Re-run all empirical label-shuffle and position-shuffle nulls with $N_{\rm MC} \ge 10,000$ and update the reported p-values and look-elsewhere thresholds.

## PAPER-GEM-M2: Missing Data Vector Definitions Table
**Class:** MAJOR
**Section:** V. Statistical methods
**Issue:** The paper lacks a formal data vector definitions table and covariance specification. It is impossible to determine if the covariance matrix for the multi-bin scans (e.g., HEALPix pixels, density quintiles) is assumed diagonal or how off-diagonal spatial/environmental correlations are handled in the joint fits.
**Fix:** Insert a table explicitly defining the primary data vector(s) and mathematically specify the covariance matrix treatment used for the multi-bin hypothesis tests.

## PAPER-GEM-M3: Omission of GR Projection and 3D-to-2D Kinematic Effects
**Class:** MAJOR
**Section:** XI. Limitations
**Issue:** The paper correlates a 3D environment (V-Web) with a 2D projected quantity (chirality) but completely ignores the geometric projection of 3D angular momentum onto the observer's past lightcone, as well as GR projection effects (e.g., weak lensing rotation) for the high-redshift ($z \le 4$) sample. 
**Fix:** Add a theoretical physics limitation explicitly addressing the 3D-to-2D geometric projection of the spin vector and bound the expected magnitude of weak lensing/GR projection effects on the observed CW fraction.

## PAPER-GEM-min1: Null Model Commensurability Undefined
**Class:** minor
**Section:** V. Statistical methods
**Issue:** The text introduces both label-shuffle and position-shuffle permutations but fails to formally designate their roles in the analysis hierarchy, leading to ad-hoc usage.
**Fix:** Explicitly declare one permutation scheme as the primary cosmological null and the other as the systematics-preserving diagnostic null.
