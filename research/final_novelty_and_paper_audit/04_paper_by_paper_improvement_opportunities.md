# Paper-by-Paper Improvement Opportunities

**Created:** 2026-03-20
**Purpose:** Identify the highest-value improvement for each paper. Honest about what matters and what is cosmetic.

---

## Paper 1: The Framework & Reckoning

### Current State
- 99% ready per paper.html.
- 37 pages. Existing LaTeX source in arxiv/main.tex. PDF compiles with 0 undefined references.
- Contains: ECH framework, MCMC constraints, 14 barriers, perturbation-transparency theorem, hybrid-DE rejection, birefringence consistency, galaxy spin, falsification criteria.

### Strongest Element
**The perturbation-transparency theorem + 14-barrier map, taken together.** This is the paper's intellectual contribution: a systematic, theorem-level demonstration that minimal ECH is observationally silent at the perturbation level, with a complete catalog of WHY across all mechanism classes.

### Weakest Element
**Risk of "negative result" framing if not positioned carefully.** A paper that says "we tried 34 things and 14 barriers closed them all" can read as failure documentation rather than scientific contribution. The framing needs to flip this: "We proved a theorem (perturbation transparency) and mapped the complete landscape (14 barriers), establishing that bounce predictions are GENERIC and ROBUST -- they do not depend on UV-completion details."

### Highest-Value Improvement
**Add a "What This Means for the Field" section** (or strengthen the existing discussion) explicitly stating:

> "We close the ECH perturbation program and demonstrate that the live bounce signal (f_NL = -35/8) is GENERIC, not framework-specific. This is a positive structural result: it means matter-bounce predictions do not depend on UV-completion details, making them more robust than previously appreciated. The barrier map serves the broader modified gravity community by identifying 14 mechanism classes that are structurally blocked for bounce-to-DE connections."

This reframes negative results as a positive contribution. The key insight is: "perturbation transparency means predictions are mechanism-independent, which is a STRENGTH."

### Other Improvements (Ranked)

| # | Improvement | Impact | Effort | Priority |
|---|-----------|--------|--------|----------|
| 1 | Reframe negative results as positive structural contribution | HIGH | LOW (framing change in intro/discussion) | MUST_DO |
| 2 | Give the perturbation-transparency theorem a formal name and box | MEDIUM | LOW (formatting) | SHOULD_DO |
| 3 | Cut or compress galaxy spin section (9-12 OOM gap, adds length without science) | MEDIUM | LOW (cut pages) | SHOULD_DO |
| 4 | Add explicit comparison to other systematic barrier analyses (if any exist) | MEDIUM | MEDIUM (literature check) | NICE_TO_HAVE |
| 5 | Tighten birefringence consistency section as bridge to Paper 2 | LOW | LOW | NICE_TO_HAVE |

**Overall priority for Paper 1 improvements: NICE_TO_HAVE.** The paper is essentially ready. The framing change (improvement #1) is the single highest-leverage edit.

---

## Paper 2: The Independent Signal (ALP Birefringence)

### Current State
- 100% ready per paper.html.
- ~8 pages. PDF available.
- Contains: ALP model, birefringence prediction, MCMC inference (9,720 samples), Bayes factor, LiteBIRD forecast.

### Strongest Element
**Clean prediction matching 3.9 sigma data.** beta = 0.27 deg predicted; beta_obs = 0.342 +/- 0.094 deg observed. The prediction is simple, the match is within 1 sigma, and LiteBIRD will test it at 9 sigma.

### Weakest Element
**Not unique to ECH; motivation is thin; crowded field.** The same prediction has been made by Fujita et al. (2021), Obata (2022), and others from the same ALP parameter space. The paper cannot claim novelty for the prediction. It must claim novelty for the implementation (MCMC), the combined constraint (Planck + ACT), and the forecast (LiteBIRD).

### Highest-Value Improvement
**Explicitly benchmark against existing ALP birefringence literature.** The paper must contain a table or paragraph that directly compares our analysis to Fujita et al. (2021), Obata (2022), Eskilt et al. (2023), and any other relevant work. The comparison should show:

| Feature | Fujita et al. | Obata | This work |
|---------|--------------|-------|-----------|
| Prediction | beta from ALP with f_a ~ M_Pl | beta from axion monodromy | beta = 0.27 deg from f_a = M_Pl, theta_i = 1 |
| Data used | Planck 2018 (2.4 sigma) | Planck 2018 | Planck + ACT combined (3.9 sigma) |
| Statistical method | Fisher estimate | Analytic | Full MCMC (9,720 samples) |
| Bayes factor | Not computed | Not computed | ln B = 5.17 |
| Forecast | LiteBIRD mentioned | LiteBIRD mentioned | LiteBIRD 9 sigma quantified |
| Miscalibration treatment | Not addressed | Not addressed | [Need to verify] |

If our analysis adds MCMC implementation quality + combined Planck+ACT constraint + quantitative Bayes factor + LiteBIRD forecast sigma, say that explicitly. If the answer is "not much beyond what exists," acknowledge it and position the paper as a focused MCMC confirmation + forecast update.

### Other Improvements (Ranked)

| # | Improvement | Impact | Effort | Priority |
|---|-----------|--------|--------|----------|
| 1 | Benchmark against Fujita/Obata/Eskilt | HIGH | MEDIUM (literature comparison) | MUST_DO |
| 2 | De-emphasize ECH motivation; frame as "Planck-scale ALP phenomenology" | HIGH | LOW (framing change) | MUST_DO |
| 3 | Address miscalibration degeneracy explicitly | MEDIUM | LOW (one paragraph) | SHOULD_DO |
| 4 | State clearly what this paper adds beyond existing literature | HIGH | LOW (one paragraph in introduction) | MUST_DO |
| 5 | Consider larger MCMC sample (9,720 is modest) | LOW | MEDIUM (computation time) | NICE_TO_HAVE |

**Overall priority for Paper 2 improvements: MUST_DO for items 1, 2, 4.** Without the literature benchmark and clear differentiation statement, the paper risks being perceived as duplicating existing work.

---

## Paper 3: The Decisive Test (f_NL Forecast)

### Current State
- 100% ready per paper.html.
- ~12 pages. 5 publication figures. PDF available.
- Contains: f_NL = -35/8 verification, SPHEREx forecast, MegaMapper forecast, Bayesian discrimination, GR projection marginalization.

### Strongest Element
**The complete integrated analysis.** No single component is individually groundbreaking, but the COMBINATION -- benchmark verification + multi-survey forecast + dominant-systematic identification + Bayesian anti-mimicry + prior robustness -- is the value proposition. This is the first paper to present a complete observational program for testing the matter-bounce prediction.

### Weakest Element
**The prediction is from Cai et al. (2009), not original.** Any reviewer familiar with the bounce bispectrum literature will immediately note that f_NL = -35/8 is a known result. The paper must be positioned as providing the observational follow-through, not the theoretical discovery.

### Highest-Value Improvement
**Frame the novelty as "the first complete observational test design for the matter-bounce non-Gaussianity prediction."**

The abstract and introduction should lead with the SCIENCE QUESTION, not the coefficient:

CURRENT (implied): "We verify f_NL = -35/8 and forecast its detection."

BETTER: "Can upcoming galaxy surveys distinguish bounce cosmology from inflation using primordial non-Gaussianity? We present the first comprehensive observational program for testing the matter-bounce prediction f_NL^local = -35/8 (Cai et al. 2009), combining..."

This framing change:
1. Credits Cai et al. up front, preventing "why are they claiming this is new?" pushback.
2. Positions the paper as answering a question ("Can we test this?"), not claiming a result ("We found this").
3. Makes the integrated analysis the contribution, not the coefficient.

### Other Improvements (Ranked)

| # | Improvement | Impact | Effort | Priority |
|---|-----------|--------|--------|----------|
| 1 | Reframe novelty as "first complete test design" | HIGH | LOW (abstract/intro rewrite) | MUST_DO |
| 2 | Credit Cai et al. prominently in abstract | HIGH | LOW (one sentence) | MUST_DO |
| 3 | Emphasize Bayesian anti-mimicry as the most original analytical contribution | MEDIUM | LOW (reorder discussion) | SHOULD_DO |
| 4 | Add a "what if f_NL = 0?" section quantifying the bounce exclusion power | MEDIUM | LOW (already computed: > 4 sigma) | SHOULD_DO |
| 5 | Address the single-point-of-failure honestly in discussion | MEDIUM | LOW (one paragraph) | SHOULD_DO |
| 6 | Discuss what FUTURE data (beyond SPHEREx) could provide a second independent test | LOW | MEDIUM | NICE_TO_HAVE |

**Overall priority for Paper 3 improvements: MUST_DO for items 1, 2.** The framing change is critical for reviewer perception. Everything else is secondary.

---

## Cross-Paper Summary

| Paper | Single Most Important Fix | Priority Level |
|-------|--------------------------|---------------|
| Paper 1 | Reframe 14 barriers as positive structural contribution | NICE_TO_HAVE (paper is 99% ready) |
| Paper 2 | Benchmark against existing ALP literature (Fujita, Obata) | MUST_DO (essential for differentiation) |
| Paper 3 | Frame as "first complete observational test design" + credit Cai et al. | MUST_DO (critical for reviewer reception) |

The highest-impact single edit across all papers: **Paper 3's abstract/intro framing.** This is the flagship paper, it will be read first, and reviewer first impressions matter more than any internal consistency fix.
