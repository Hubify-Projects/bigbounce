# 06: Synthesis Paper Triage

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Proposed Paper

"Observational Evidence For and Against Bouncing Cosmology: A Systematic Comparison with ΛCDM + Inflation"

Or some variant: a comprehensive paper that catalogs every observational test where bouncing cosmology does better, comparably, or worse than the standard model.

---

## Assessment: Is this paper genuinely novel?

**Partially.**

There ARE existing reviews of bouncing cosmology:
- Brandenberger & Peter (2017), "Bouncing Cosmologies: Progress and Problems" — comprehensive theory review
- Battefeld & Peter (2015), "A Critical Assessment of Some Bouncing Cosmologies"
- Novello & Bergliaffa (2008), "Bouncing Cosmologies"
- Cai (2014), "Exploring Bouncing Cosmologies with Cosmological Surveys"

**What exists:** Theory reviews that discuss various bounce models, their perturbation spectra, and theoretical challenges. These are primarily THEORETICAL reviews.

**What does NOT exist (as of early 2026):**
- A systematic OBSERVATIONAL comparison that takes specific anomalies/tensions in the current data and asks "does the bounce do better than ΛCDM + inflation?"
- A paper that includes the 2020+ birefringence data, the 2023 NANOGrav confirmation, and the latest CMB anomaly analyses
- A paper that honestly tabulates wins AND losses for bouncing cosmology against the standard model

The Agullo et al. (2021) paper comes closest for the CMB anomaly sector, but it is LQC-specific and does not cover PTA, PBH, birefringence, or tensions.

**Verdict on novelty:** A NARROW, DATA-FOCUSED synthesis could be novel. A BROAD theoretical review would not be.

---

## Is it too broad / too review-like?

**Risk: HIGH.**

A paper that tries to address:
- CMB anomalies (low-ℓ, parity, hemispherical)
- PTA/NANOGrav
- PBH dark matter
- S₈ tension
- Hubble tension
- Birefringence
- f_NL predictions
- Tensor spectrum
- BKL problem
- Baryogenesis

...across:
- Matter bounce
- LQC bounce
- Ekpyrotic bounce
- Cyclic models
- Slow contraction + bounce

...is a REVIEW, not a research paper. Reviews are useful but:
1. They require invited status or established authority in the field
2. They don't generate new results
3. They are slower to publish and have less impact than focused research papers
4. We are not established authorities in bounce cosmology (yet)

---

## What would make it publishable rather than just opinionated?

**Three things that would elevate it:**

### 1. A quantitative scorecard with Bayesian comparison

Not just "bounce can explain X" — actually compute the Bayesian evidence for bounce vs inflation for each observable. Even rough estimates (order-of-magnitude Bayes factors) would be more useful than qualitative claims.

**Problem:** This requires actual computation for each observable, not just literature citations. A proper Bayesian comparison for n_s, f_NL, r, PTA, β, S₈ would be a substantial project.

### 2. A joint-constraint analysis

Show the combined parameter space: what values of bounce model parameters (contraction EOS, bounce energy, tensor amplitude) are simultaneously compatible with ALL current data?

**Problem:** This requires choosing a specific bounce model and running MCMC or at least Fisher forecasts.

### 3. A future-observable prediction map

For each bounce model class, tabulate the predictions for experiments coming online in the next 10 years (LiteBIRD, CMB-S4, ET, LISA, SPHEREx). Show which experiments will distinguish bounce from inflation.

**Problem:** This is straightforward but requires careful treatment of degeneracies.

---

## What is the narrowest defensible scope?

**Option A (NARROW — recommended if pursued):**

"Can the matter bounce survive current observational constraints? A joint analysis including n_s, f_NL, r, the NANOGrav GW background, and cosmic birefringence"

This is:
- Focused on ONE bounce model class (matter bounce)
- Quantitative (joint constraint analysis)
- Falsifiable (if no parameter space survives, the model is dead)
- Timely (uses the latest NANOGrav, birefringence, and CMB data)
- Manageable (~15-20 pages)

**Option B (MODERATE):**

"Observational status of bouncing cosmology in 2026: what the data actually says"

This is:
- Broader but still data-focused
- Covers the main observable channels with honest assessment
- Does not require MCMC (qualitative + back-of-envelope quantitative)
- Risk: becomes a review

**Option C (BROAD — not recommended):**

"Complete comparison of bouncing vs inflationary cosmology"

This is the full review. Not recommended for us.

---

## Verdict

**POSSIBLE_BUT_NEEDS_NARROWING**

A synthesis/comparison paper is worth considering ONLY in the narrow form (Option A). Specifically:

**A joint-constraint analysis of the matter bounce model against all 2026 data.**

This would be novel because:
1. Nobody has done the joint constraint with post-2023 data (NANOGrav, birefringence)
2. It confronts the Quintin no-go quantitatively
3. It gives a clear verdict: matter bounce survives or dies
4. It makes specific predictions for upcoming experiments

**What would kill this idea:**
- If the Quintin no-go + n_s = 1 already trivially kills the single-field matter bounce without detailed analysis (i.e., there's nothing to compute — the model is already dead)
- If such an analysis has been published in 2025-2026 that we haven't found
- If the parameter space is so obviously empty that the paper reduces to "the matter bounce is excluded" in one page

**Pre-check needed:** Before committing to this paper, verify that the matter bounce parameter space is NOT trivially empty. The n_s = 1 problem alone is 8.3σ exclusion for dust contraction. Unless a curvaton or modified EOS is included, the base model is already dead. So the paper would need to include at least one tilt mechanism — making it "matter bounce + curvaton" at minimum.
