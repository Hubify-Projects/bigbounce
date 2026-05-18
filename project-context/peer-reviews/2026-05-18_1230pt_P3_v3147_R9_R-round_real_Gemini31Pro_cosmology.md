# P3_v3147_R9 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1230pt
**Wall time**: 99.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=63880, completion=12959, reasoning=11855, total=76839

---

## PAPER-GEM-B1: Hallucinated Asymmetric Remap Arithmetic in Caveat (j)
**Classification:** BLOCKER
**Location:** \S 6.4, Caveat (j)
**Issue:** The asymmetric remap arithmetic for the Gold+Silver Fisher forecast is mathematically impossible under the stated $F_0 + c\alpha^2$ form. The $1\sigma$ interval for $\alpha_{GS} = 1.83 \pm 2.03$ is $[-0.20, 3.86]$. Because this interval crosses $\alpha=0$, the upper bound of $\sigma(f_{NL})$ must be the single-tracer floor $\sigma(0) = 8.98$. The lower bound at $\alpha=3.86$ is $(0.0124 + 0.0747 \times 3.86^2)^{-1/2} \approx 0.94$. The quoted envelope $[2.04, 3.40]$ and central value $2.43$ (true central is $\sigma(1.83) = 1.95$) are completely hallucinated.
**Fix:** Correct the central value to $1.95$ and the asymmetric $1\sigma$ envelope to $[0.94, 8.98]$. 

## PAPER-GEM-B2: OOD MSE Normalization Contradiction
**Classification:** BLOCKER
**Location:** \S 2.2, "In-sample scoring and held-out validation"
**Issue:** The text claims "the 0.87% DESI anomaly rate is preserved on this independent OOD sample", but explicitly states the $S>5$ threshold corresponds to an absolute MSE of $0.143$ while the OOD sample has a median MSE of $0.178$. If the threshold is below the median, more than 50% of the OOD sample is flagged as anomalous, making the 0.87% preservation claim mathematically impossible.
**Fix:** Retract the claim that the 0.87% rate is preserved at the absolute $0.143$ MSE threshold, or explicitly state that a new percentile-based threshold was computed for the OOD sample to maintain the rate.

## PAPER-GEM-M1: Main Text Quotes Unphysical Fisher Bounds
**Classification:** MAJOR
**Location:** Abstract and \S 5
**Issue:** The Abstract and \S 5 quote a $+1\sigma$ tail of $10.64$ and a 95% CI of $[3.62, 12.95]$ derived from linear extrapolation. However, \S 6.4 Caveat (i) correctly proves that these values violate Fisher positivity (since adding tracers can never degrade the constraint past the 8.98 single-tracer floor) and establishes the true 95% envelope as $[2.4, 8.98]$. The paper structurally contradicts itself by knowingly quoting unphysical values in the headline results.
**Fix:** Replace the linear-extrapolated bounds ($10.64$ and $[3.62, 12.95]$) in the Abstract and \S 5 with the positivity-respecting bounds ($[2.41, 8.98]$) established in Caveat (i).

## PAPER-GEM-M2: 5-fold CV Narrative Contradiction
**Classification:** MAJOR
**Location:** \S 6.4 (i) vs Abstract
**Issue:** The Abstract correctly resolves the R7 5-fold Jaccard contradiction by stating the *full* 47,000-spectrum pool was scored by each fold to allow unioning. However, \S 6.4 (i) still contains the stale, mathematically impossible text claiming it scored only the 9,400 held-out spectra ("never saw it during training") while simultaneously claiming 399 objects appear in all 5 folds (which is impossible for disjoint sets).
**Fix:** Update the text in \S 6.4 (i) to match the Abstract, explicitly stating that the full 47,000-spectrum pool was scored by each fold's checkpoint.

## PAPER-GEM-m1: Incorrect "Taylor Expansion" Terminology
**Classification:** minor
**Location:** \S 6.4, Caveat (i)
**Issue:** The text claims the linear scaling $\sigma(\alpha) = 8.98 - 3.66\alpha$ is "valid as a Taylor expansion in the neighborhood of $\alpha \approx 0$". If the true Fisher information scales as $\alpha^2$, the derivative at $\alpha=0$ is strictly zero, meaning the Taylor expansion has no linear term. The $8.98 - 3.66\alpha$ form is a secant interpolation between $\alpha=0$ and $\alpha=0.15$, not a Taylor expansion.
**Fix:** Change "valid as a Taylor expansion" to "valid as a secant interpolation".
