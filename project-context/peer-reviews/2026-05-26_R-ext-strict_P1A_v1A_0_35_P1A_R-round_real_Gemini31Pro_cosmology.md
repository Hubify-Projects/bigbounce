# P1A R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P1A_v1A_0_35
**Wall time**: 44.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=30023, completion=4346, reasoning=3286, total=34369

---

## PAPER-GEM-B1: BLOCKER - AI-Vendor and Audit-Trail Contamination in Manuscript Body
**Location:** Sec. II.C.1, Sec. IV, Sec. IV.A, Sec. IV.D, Sec. IX.L, Sec. XIII, Appendix B
**Issue:** The manuscript body is heavily contaminated with internal version-control tags, prompt-meta language, and AI-vendor review histories (e.g., "per R23 Gemini-3.1-Pro PAPER-GEM-M1 closure", "v1A.0.28 R7 Grok-B1 closure", "A multi-vendor adversarial-review round (GPT-5.5 / Gemini-2.5-Pro / Grok-4-fast / Perplexity Sonar Pro / DeepSeek-V3.2..."). This violates basic journal submission standards and invalidates the manuscript for peer review.
**Fix:** Purge all internal audit-trail prose, AI-vendor references, and version-history closure tags from the main text and appendices prior to submission.

## PAPER-GEM-B2: BLOCKER - Overclaim of "Definitive" Erasure Without Joint Fit
**Location:** Abstract, Sec. I.B, Sec. XIII, Sec. XIV.D
**Issue:** The paper repeatedly claims the matter-bounce $\fnl = -35/8$ signature would be "\emph{definitively} erased" by $N_{\rm tot} \gtrsim 60$. A "definitive" exclusion claim in cosmology requires a joint nuisance-marginalized model fit demonstrating that the posterior volume for the signal vanishes, which is absent here; a kinematic horizon-exit scaling argument only proves suppression, not definitive observational exclusion against all possible tracer combinations.
**Fix:** Downgrade "definitively erased" to "kinematically suppressed below cosmic variance," or provide the explicit joint nuisance-marginalized Fisher/MCMC contours proving definitive exclusion.

## PAPER-GEM-M1: MAJOR - Contradictory "Mechanism-Independent" Claims
**Location:** Abstract, Sec. I, Sec. XIII
**Issue:** The abstract and introduction heavily promote the surviving $\fnl = -35/8$ prediction as "mechanism-independent." However, Sec. XIII explicitly contradicts this, admitting the value holds only for the "scalar-only $w=0$ matter-bounce class" and is "not a fully mechanism-independent prediction across the broader bouncing-cosmology landscape." This overstates the UV-completion independence of the observable.
**Fix:** Remove "mechanism-independent" from the abstract and introduction; replace with "class-specific" or "scalar-matter-bounce-specific" to accurately reflect the theoretical boundaries.

## PAPER-GEM-M2: MAJOR - Missing Data Vector Definitions Table
**Location:** Sec. V, Sec. VII
**Issue:** The manuscript claims a "confirmed null" for the galaxy spin asymmetry and relies on specific observational constraints (Planck/ACT DR6 $\beta$, SPHEREx $\fnl$) to close theoretical routes, but completely lacks a formalized data vector definitions table. Deferring to a companion paper (Paper IV) is insufficient when the structural closure in *this* paper relies on the commensurability of those specific data vectors.
**Fix:** Insert a data vector definitions table explicitly defining the observables, their assumed covariance structures, and the specific datasets/subsamples used to substantiate the null claim.

## PAPER-GEM-m1: minor - Dimensional Inconsistency in Route 2 Dimensionless Ratio
**Location:** Sec. IV.B
**Issue:** The dimensionless ratio derivation calculates $10^{-3} \cdot 10^{-61} / (10^{-2} \cdot 6\times 10^{-3}) \sim 10^{-58}$ to $10^{-60}$. The arithmetic yields exactly $\sim 1.6 \times 10^{-59}$, but the text hand-waves a "factor-of-$\sim$100 ambiguity" attributed loosely to "$\varepsilon$-correction perturbative-order scaling alone" without formal EFT error propagation to justify this two-order-of-magnitude theoretical uncertainty.
**Fix:** State the exact leading-order arithmetic result and formally define the theoretical error budget, rather than asserting an unproven two-order-of-magnitude ambiguity range.

## PAPER-GEM-m2: minor - Stale Release Tags and Version History Mismatch
**Location:** Appendix B
**Issue:** The manuscript contains fragmented and stale versioning references in the text (e.g., "Status update for v1A.0.23", "v1A.0.29 R8+R9") that directly conflict with the `\paperVersion{v1A.0.35}` tag declared in the preamble and abstract.
**Fix:** Remove all internal versioning references from the manuscript body to ensure consistency with the submitted v1A.0.35 release tag.
