# EXT11 Harvest — P2 — ChatGPT

- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5f2-5e8c-83e8-9318-b7aefa847ee0
- PDF md5: ab99c187 (paper2_fnl_forecast_v1.7.64_ab99c187.pdf)
- Harvested: 2026-06-13 17:16 PDT

---

## Headline Verdict: MINOR REVISIONS (very close to ACCEPT)

The revision is very close. No basis for major revisions: the main scientific architecture remains intact, the headline SPHEREx recast is still internally defensible, and most EXT10 concerns have been closed or downgraded to style. However, not quite ACCEPT because the revised abstract introduces one remaining headline-accounting ambiguity, and the new Bayes-factor self-check paragraph contains a small numerical/logical error.

## EXT10 Items Status

### 1. Null-space scatter vs. 2.6σ floor — Still open (abstract-level fix required)

The body now says the right thing: the null-space percentile calculation is a distributional effect, not the central headline denominator. But the abstract now says the 16th-percentile r=0.75 "anchors the conservative 2.6σ floor," while Table IV's all-combined 2.6σ row is computed with central r=0.84, not r=0.75.

**Proposed fix:** In the abstract, replace the parenthetical with:
> "polynomial-null-space scatter ±0.13 in r at fixed sampling measure, reported as a separate distributional robustness check rather than included in the cumulative 2.6σ denominator floor"

Alternatively, if the 16th-percentile r=0.75 is included simultaneously with all-combined b_ϕ+GR, revise the conservative floor to approximately 4.375×0.75/1.41 ≃ 2.3σ.

### 2. Cai/Li factor-of-two item — Closed

The appendix now explicitly separates local-template normalization from the in-in commutator doubling, gives the operator identity, and reports Table V as a stress-test rather than a physical alternative branch.

### 3. Shape-definition/reproducibility item — Closed enough

The revised manuscript now states that the coefficient map and per-configuration overlap values are archived, and identifies the artifact used to reproduce r=0.84±0.02.

### 4. σ(f_NL) ≃ 0.36/0.93 issue — Closed/no issue

The paper consistently uses Heinrich et al. σ(f_NL) = 0.7 as the baseline and then applies template and systematic degradations.

### 5. Prior minor/style items — Closed or non-holding

UV-independence claim restricted to scalar-only Wilson-Ewing class; GR section states ~23% calibration for σ_GR=0.5; SDB subsection explicitly marks joint Fisher as subordinate.

## New Items Introduced by Closures

### New Item 1 — Bayes-factor "self-consistency check" has a wrong explanatory comparison (MINOR, fix required)

In the new closed-form Bayes-factor subsection, the text says that for σ_theory=1.0, narrow competitor [-5,+5], the exact B=4.01, while Eq. (10) gives 5.69, calling this a ~42% error caused by narrow-prior CDF tails.

That explanation mixes two different effects. Eq. (10) is the delta-bounce-prior large-W approximation, whereas B=4.01 is the Gaussian-bounce-prior result. The reduction to 4.01 is dominated by prior convolution of the bounce model, not by narrow-competitor CDF tails.

**Proposed fix:** Replace the narrow-prior bullet with:
> "For the Gaussian-bounce-prior narrow competitor, Eq. (10) is not applicable because it is a delta-prior approximation. The exact prior-convolved calculation gives B=4.01. For the delta-bounce-prior narrow competitor, Eq. (9) gives B ≃ 7.0, as reported in Table II."

Also change "error 0.18% (<0.1% threshold met after rounding)" to "~0.2%."

### New Item 2 — Abstract became slightly more crowded (polish)

The new abstract carries the entire audit trail before the introduction. After fixing the null-space sentence, a compression pass is recommended.

## Bottom Line

MINOR REVISIONS only. The remaining corrections are local edits to the abstract and Bayes-factor explanatory paragraph. Would move to ACCEPT after those two fixes.
