# P3 R-round — DIRECT vendor — GPT-5 methodology reviewer

**Model**: `gpt-4o` (FALLBACK from `gpt-5`) (direct vendor API; NOT via OpenRouter)
**Round**: 2026-05-29_R-direct-v1b
**Wall time**: 10.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=74268, completion=651, total=74919, prompt_details={'cached_tokens': 0, 'audio_tokens': 0}, completion_details={'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}

---

```markdown
## PAPER-GPT-B1: Abstract, Line 5

**Issue:** The abstract overstates the novelty fraction by quoting the SIMBAD-unmatched fraction (58.8%) as if it were a discovery rate, while the genuine novelty fraction is only 17.8% based on deeper cross-matching.

**Fix:** Clearly distinguish between the SIMBAD-unmatched fraction and the genuine novelty fraction in the abstract. State that the genuine novelty fraction is 17.8% and emphasize that the SIMBAD-unmatched fraction is a database-coverage measurement, not a discovery rate.

## PAPER-GPT-B2: Section 2.2, Line 315

**Issue:** The description of the 5-fold cross-validation methodology is misleading. It states that the model scores the held-out 20% split, which contradicts the Jaccard arithmetic that requires scoring the full 47,000-spectrum pool.

**Fix:** Correct the text to explicitly state that each fold's model scores the full 47,000-spectrum pool, not just the disjoint 9,400-spectrum held-out split, to align with the Jaccard statistic calculation.

## PAPER-GPT-B3: Section 5, Line 620

**Issue:** The Fisher forecast for $\sigfnl$ uses a linear approximation that fails at the stationary point $\alpha = 0$, leading to an unphysical $+1\sigma$ tail. This misrepresents the credible interval.

**Fix:** Replace the linear approximation with the Fisher-positivity-respecting form $1/\sigfnl^2 = F_0 + c\,\alpha^2$, and update the credible interval to reflect the proper asymptotic form.

## PAPER-GPT-M1: Section 3.3, Line 440

**Issue:** The LAMOST anomaly catalog is heavily contaminated by a training-bias artifact, with 98% of anomalies showing blue-excess signatures. This undermines the validity of the LAMOST results.

**Fix:** Clearly state that the LAMOST results are affected by a training-bias artifact and should be treated as a methodological lesson rather than a validated catalog component. Recommend future work to address this bias.

## PAPER-GPT-M2: Section 4, Line 750

**Issue:** The cross-survey analysis reports a significant $\chi^2$ value for spatial uniformity but does not account for the inhomogeneous survey footprints, which dominate the signal.

**Fix:** Clarify that the significant $\chi^2$ result is driven by survey footprint inhomogeneities, not intrinsic astrophysical clustering, and that a rigorous spatial uniformity test would require modeling each survey's selection function.

## PAPER-GPT-M3: Section 6, Line 1020

**Issue:** The discussion of the $\fnl$ multi-tracer forecast does not adequately address the impact of observational systematics, which could degrade the forecast.

**Fix:** Explicitly state that the $\fnl$ forecast assumes zero observational systematics and that any non-zero systematic budget could degrade the central $\sigfnl$. Recommend a full systematics-marginalization Fisher recompute as future work.
```

