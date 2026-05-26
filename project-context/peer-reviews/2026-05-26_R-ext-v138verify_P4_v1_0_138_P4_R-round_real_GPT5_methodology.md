# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v138verify_P4_v1_0_138
**Wall time**: 141.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=106661, completion=6749, reasoning=5696, total=113410

---

## PAPER-GPT-B1 — BLOCKER

**Section:** §“Monopole+Mask Leakage Generative Null”, paragraphs “Joint nuisance-marginalized model fit” and “Extended joint fit…”  
**Issue:** The claimed 99% formal exclusion at `z=-250` uses a WLS coefficient error (`0.006% f_CW`) while the paper itself shows strong spatial/systematics covariance: non-Gaussian MC tails, `χ²/dof≈4.24`, density/leg/confidence residuals, and leg×confidence coefficients with `|z|=10–26`. This covariance is not propagated, so the 250σ exclusion is a parametric independent-pixel artifact, not a systematic-budget result.  
**Fix:** Replace the formal-exclusion claim with a GLS/Bayesian fit using a systematics-preserving pixel covariance or block/bootstrap/sandwich covariance, then quote the profiled/marginalized likelihood interval. Until then, label the result “WLS-only conditional on the template/noise model.”

## PAPER-GPT-B2 — BLOCKER

**Section:** §Conclusions, “Canonical-$N$ MASTER $\ell=1$ direct compute”; §NaMaster appendix  
**Issue:** The reported arithmetic is internally inconsistent: `C1_decoupled=2.298e-5`, null mean `8.004e-6`, null std `8.097e-6` gives `(2.298e-5−8.004e-6)/8.097e-6 = 1.85`, not `+3.64`. The `+3.64` value corresponds to different “corrected” numbers given elsewhere (`1.51e-5`, `3.12e-6`, `3.31e-6`).  
**Fix:** Use one canonical corrected data vector throughout, delete or explicitly label the legacy pre-correction triplet, and recompute all quoted z-scores and empirical p-values from the displayed numbers.

## PAPER-GPT-M1 — MAJOR

**Section:** §“Extended joint fit with leg × confidence interactions”  
**Issue:** The 24-template design is rank-deficient or near-rank-deficient: the 15 leg×confidence-bin templates sum back to the leg-fraction templates, and leg fractions plus the constant already contain a null direction. Individual interaction amplitudes and `|z|=10–26` are not identifiable unless constraints/orthogonalization are specified.  
**Fix:** Report matrix rank, condition number, and the exact contrast basis. Drop redundant main effects or impose sum-to-zero constraints, then test the interaction block with a joint LR/F/Wald test rather than interpreting raw coefficient z-scores.

## PAPER-GPT-M2 — MAJOR

**Section:** §“Joint nuisance-marginalized model fit”; §Sensitivity amplitude-convention disclosure  
**Issue:** The 1.7% reference amplitude is dimensionally ambiguous. The text says `1.7% in f_CW` corresponds to `A_p=0.034`, but other sections define the full-amplitude convention `p_CW=1/2(1+A cosθ)` and inject amplitudes directly into `A_p`, which differs by a factor of two.  
**Fix:** Define one amplitude convention table: `f_CW` half-modulation, `A_p=2f_CW−1`, and full dipole amplitude. Recompute the 1.7% reference and all z-values under that convention.

## PAPER-GPT-M3 — MAJOR

**Section:** §“Hard-label variance widening from the 21.4% argmax-flip rate”  
**Issue:** The variance derivation is wrong. For symmetric independent flips, `Var(x_obs)=q(1−q)` with `q=p(1−2e)+e`; at `p≈0.5` the observed Bernoulli variance is unchanged, not binomial variance plus `e(1−e)`. If correcting back to the true fraction, the uncertainty inflates by `1/(1−2e)≈1.75`, not `1.21`.  
**Fix:** Re-derive using the misclassification matrix. Either keep observed-label binomial variance unchanged, or propagate deattenuated true-fraction errors with the correct dilution factor and update hard-label diagnostic significances.

## PAPER-GPT-m1 — minor

**Section:** §Hemisphere Asymmetry footnote and Fig. hemisphere caption  
**Issue:** “Zero of 10,000 nulls reach the data” is reported as `p_LEE ≤ 1/(N+1)≈10^-4` and `>3.7σ`. That is not a confidence upper bound; zero exceedances only gives MC resolution, with a 95% upper limit of roughly `3/(N+1)≈3e-4`.  
**Fix:** Report `p < 1e-4` only as resolution/point-estimator language, or quote a binomial confidence upper limit and the corresponding sigma.
