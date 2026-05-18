# P3_v3149_R11 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 126.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=64626, completion=14236, reasoning=13214, total=78862

---

## PAPER-OOD-B1: OOD Anomaly Rate Contradiction (BLOCKER)
**Location:** Section 2.2, "In-sample scoring and held-out validation"
**Issue:** The text states the $S>5$ anomaly threshold corresponds to $\mathrm{MSE} \approx 0.143$, which is *below* the OOD sample median of $0.178$. If the threshold is below the median, $>50\%$ of the OOD sample must be classified as anomalies. The subsequent claim that "the $0.87\%$ DESI anomaly rate is preserved on this independent OOD sample" is mathematically impossible under these numbers.
**Fix:** Recompute the actual OOD anomaly fraction at $\mathrm{MSE} = 0.143$ and report it, or correct the standardized-to-MSE unit conversion if $0.143$ is a typo.

## PAPER-JAC-B1: Jaccard Cross-Fold Scoring Contradiction (BLOCKER)
**Location:** Section 6.4, Caveat (i)
**Issue:** Section 2.2 was updated to state the 5 folds score the *full 47,000 pool* to resolve the Jaccard intersection math, but Caveat (i) still explicitly claims the models score "the remaining 20% (9,400 held-out spectra)" and repeats the 399/546 intersection numbers. The intersection of 5 disjoint 9,400-spectrum holdouts is exactly zero, making the stated overlap mathematically impossible.
**Fix:** Update Caveat (i) to match Section 2.2's full-pool scoring methodology and remove the claim that "each spectrum is scored by a model that never saw it".

## PAPER-FSH-M1: Abstract Fisher Positivity Contradiction (MAJOR)
**Location:** Abstract
**Issue:** The abstract introduces the Fisher-positivity envelope capping $\sigfnl$ at $8.98$, but in the very next clause justifies the null consistency by claiming "the $+1\sigma$ tail ($\sigfnl = 10.64$) exceeds the $\sigfnl^{\rm std} = 8.98$ DESI QSO baseline." A value of 10.64 violates the physical cap just introduced in the same sentence.
**Fix:** Replace the unphysical 10.64 claim with a statement that the $+1\sigma$ tail of $\alpha$ crosses zero, driving $\sigfnl$ to the 8.98 single-tracer floor.

## PAPER-FSH-M2: Section 5 Fisher Positivity Omission (MAJOR)
**Location:** Section 5
**Issue:** Section 5 explicitly endorses the linear-extrapolated $[3.62, 12.95]$ as the "canonical credible interval" for the full sample, completely ignoring the Fisher-positivity cap of 8.98 introduced in Caveat (i). It also repeats the unphysical "$\sigfnl = 9.71$" claim for the Gold+Silver sample, contradicting Caveat (j).
**Fix:** Propagate the Caveat (i) and (j) Fisher-positivity envelopes ($[2.4, 8.98]$ and $[0.94, 8.98]$) into the Section 5 body text as the canonical intervals, and remove all $\sigfnl > 8.98$ values.

## PAPER-FSH-min1: Fisher Nuisance Parameter Counting (minor)
**Location:** Section 5, Fisher Systematics
**Issue:** The phrasing "a $4n+1$-dimensional nuisance-parameter block per active tracer" is dimensionally confused; it implies $4n+1$ parameters *per tracer* rather than for the whole system.
**Fix:** Change to "a $(4n+1)$-dimensional parameter space (one global $\fnl$ plus 4 nuisance parameters per active tracer)".

## PAPER-QSO-min1: DESI QSO Number Density Baseline (minor)
**Location:** Appendix C, Section C.1
**Issue:** The text cites the standard DESI QSO sample density as $1.5 \times 10^{-4} \, (h/\mathrm{Mpc})^3$. This is the DESI ELG density; the QSO density is $\sim 2-5 \times 10^{-5} \, (h/\mathrm{Mpc})^3$.
**Fix:** Correct the baseline DESI QSO number density to $\sim 3 \times 10^{-5} \, (h/\mathrm{Mpc})^3$ and update the relative sparsity comparison.
