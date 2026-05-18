# P3_v3149_R11 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 105.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=63200, completion=6233, reasoning=5178, total=69433

---

## PAPER-GPT-B1 — BLOCKER

**Section:** §5 Cosmological Applications  
**Issue:** §5 still presents the linear-extrapolated Fisher interval `[3.62, 12.95]` and calls the symmetric `±2.37 / ±4.65` form the “canonical credible interval,” directly contradicting caveat (i) and the abstract’s corrected Fisher-positivity envelope `[2.4, 8.98]`. This is the exact unphysical Fisher-bound regression R10 was supposed to close.  
**Fix:** Replace the §5 linear-CI paragraph with: local-linear central forecast only; positivity-respecting 95% envelope `[2.4, 8.98]`; delete “canonical” language for `[3.62, 12.95]` or label it explicitly invalid outside the local Taylor region.

## PAPER-GPT-B2 — MAJOR

**Section:** Abstract; §5 Gold+Silver paragraph; Conclusions item 5  
**Issue:** The Gold+Silver forecast is still quoted prominently as `σ_GS = 2.28 ± 7.43`, with no inline `[0.94, 8.98]` positivity-remapped envelope in the abstract or conclusions. §5 contains the corrected envelope, but still uses the linear central `2.28` and “74% improvement,” while caveat (j) says the corrected central is `1.95`.  
**Fix:** Make the primary GS quote `σ_GS = 1.95` with Fisher-positive envelope `[0.94, 8.98]`; demote `2.28 ± 7.43` to a clearly invalid local-linear diagnostic or remove it from abstract/conclusions.

## PAPER-GPT-B3 — MAJOR

**Section:** §2.2 In-sample scoring; §6.4 caveat (i); Conclusions item 7; Abstract  
**Issue:** DESI 5-fold stability is internally inconsistent. The abstract says each fold scores the full 47k pool, making 470-object top-1% sets and union 546 feasible; §2.2 and §6.4(i) say each fold scores only its disjoint 9,400 held-out split, where top-1% sets have 94 objects and cannot have 399 objects appearing in all five folds.  
**Fix:** Choose one protocol. If full-pool scoring was used, remove all “held-out 20% only / never saw it” language. If held-out-only was used, recompute the Jaccard/union statistics because the reported numbers are impossible.

## PAPER-GPT-B4 — MAJOR

**Section:** §2.2 threshold policy; Table 1 caption/footnotes; §3.2–§3.3; Conclusions item 8  
**Issue:** The headline catalog count mixes incompatible thresholds. Text says spectroscopic surveys use fixed `S>5`, but the Path-C sum uses SDSS `77,905` at `S≥0.1060` despite only `12` at `S>5`, and LAMOST `113,342` at p99 despite only `2,054` at `S>5` and a failed 5σ gate. The `378,280` headline is therefore not a uniformly defined anomaly catalog.  
**Fix:** Split headline products: strict validated `S>5` catalog-grade count, percentile/continuity exploratory count, and LAMOST exploratory tier. Recompute dedup counts separately for each tier.

## PAPER-GPT-B5 — MAJOR

**Section:** §2.2 OOD validation paragraph  
**Issue:** The DESI OOD MSE arithmetic is inconsistent. It says the `S>5` threshold corresponds to MSE `≈0.143`, while the OOD median MSE is `0.178`; if these are the same units, ≥50% of OOD spectra exceed the threshold, contradicting the claimed preserved `0.87%` anomaly rate and “upper tail” framing.  
**Fix:** Report OOD scores in the same canonical `S` units as Eq. (2), give the exact OOD fraction above `S>5`, and separate raw MSE from standardized/rescaled MSE.

## PAPER-GPT-B6 — MAJOR

**Section:** Abstract; Appendix C “Sensitivity to Bias Enhancement”; §5 legacy fixed-α text  
**Issue:** The abstract advertises a “full sensitivity table” with linear `α` scaling, and Appendix C still states `Δσ/σ ∝ α` over `α∈[0.05,0.50]`. Caveat (i) says the Fisher-positive form is `1/σ^2 = F0 + cα^2`; the table is therefore stale outside the local linear neighborhood and conflicts with the corrected Fisher treatment.  
**Fix:** Replace Appendix C with the positivity-respecting mapping or label the current table “legacy local-linear diagnostic, invalid for interval propagation”; remove “full sensitivity table” language from the abstract unless updated.
