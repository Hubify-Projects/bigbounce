# 02: Best Optional Add-On

## Decision: YES — Mock-Based Estimator Realism Validation

## Why This Is the Only One Worth Doing

The current science case rests on ANALYTIC forecasts (Fisher matrices + closed-form Bayes factors). A skeptical referee will ask: "Does this survive when you generate actual mock power spectra with realistic noise, window effects, and nuisance contamination, and then try to RECOVER the signal?"

The mock-based validation answers that question by:
1. Generating synthetic P(k) observations with the bounce signal injected
2. Adding realistic noise (shot noise + cosmic variance)
3. Applying survey-window / k_min loss
4. Injecting GR systematic contamination and b_φ uncertainty
5. Running the Bayesian model comparison on the MOCK DATA
6. Checking whether the recovered Bayes factors match the analytic predictions

## What Scientific Doubt It Addresses

"Are the analytic Bayes factors an accurate representation of what a real survey analysis would find, or are they optimistic due to simplified assumptions?"

## What Result Would Strengthen the Paper

If the mock-based Bayes factors are CONSISTENT with the analytic ones (within ~factor 2): confirms the current science case is realistic.

## What Result Would Show Current Framework Was Enough

If mock-based results are essentially identical to analytic: the extra computation was informative but didn't change the answer. Still worth including as a robustness appendix.

## Compute Requirements

- 100,000 mock power spectra: trivial (numpy vectorized)
- Bayes factor recovery per mock: trivial (closed-form or simple quadrature)
- Total: laptop-scale, <1 minute
- RunPod CPU: useful ONLY if we want to scale to millions of mocks or vary many more parameters

**RunPod verdict: useful for a LARGER parameter sweep but not essential. The core validation runs on laptop.**
