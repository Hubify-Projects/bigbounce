# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P3_v3_1_62
**Wall time**: 86.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=68083, completion=4741, reasoning=3624, total=72824

---

## PAPER-GPT-B1 — BLOCKER — §2.2 “In-sample scoring and held-out validation”

**Issue:** The text says each fold scores only its held-out 9,400 spectra, but then reports top-1% sets of 470 objects, 546-object union, and 399 objects appearing in all five folds. Those numbers are mathematically impossible under held-out-only scoring; they only work if every fold scores the full 47,000-spectrum pool.  
**Fix:** Rewrite §2.2 to match §6.4(i): each fold trains on 80% and scores the full 47,000 pool for the Jaccard statistic. If held-out-only validation is desired, recompute all union/Jaccard counts using 94-object fold sets.

## PAPER-GPT-B2 — BLOCKER — §5, abstract, conclusions, Appendix C

**Issue:** The $f_{\rm NL}$ forecast still mixes incompatible uncertainty models: the positivity-respecting mapping gives $\sigma(f_{\rm NL})=8.14$ with envelope $[3.92,8.98]$, but §5 later calls the linear $8.27\pm2.37$ / 95% $[3.62,12.95]$ interval “canonical,” and the conclusions again headline unphysical linear values including $\sigma_{\rm GS}=2.28\pm7.43$. This is internally contradictory and overstates statistical precision; the quoted error bars propagate only $\alpha$ jackknife noise, not the systematic Fisher nuisance budget.  
**Fix:** Choose one canonical mapping. Use the $\alpha^2$ Fisher-positive transformation everywhere, demote linear values to a clearly labeled diagnostic, and do not call any interval a realistic forecast until the stated systematics and GR-projection terms are marginalized or deterministically included.

## PAPER-GPT-M1 — MAJOR — Table I, §3.5 Planck CMB, §7 conclusions

**Issue:** The Planck Path-C native result is described as scoring $2\times10^5$ patches and selecting the top 200, i.e. top 0.1%, but Table I still lists Planck as 20,000 total patches, 200 anomalies, 1.00%. This also makes the paper-wide processed total $37{,}272{,}042$ inconsistent with the native Planck analysis; it should increase by 180,000 if the 200k native set is the science product.  
**Fix:** Decide whether the retained Planck catalog is based on 20k or 200k patches. Update $N_{\rm total}$, anomaly rate, headline processed total, and all “top-1%” language accordingly.

## PAPER-GPT-M2 — MAJOR — Table I caption/footnotes, §3.2 SDSS

**Issue:** The SDSS native “top-$77{,}905$” slice is repeatedly called top-1%, but $77{,}905/1{,}925{,}279=4.05\%$ and $77{,}905/2{,}304{,}830=3.38\%$. The actual top-1% native SDSS count is stated elsewhere as 19,253 at $S\ge0.2051$.  
**Fix:** Split SDSS into three explicit thresholds: native $S>5$ = 12, native top-1% = 19,253, and continuity-count slice = 77,905. Do not label the continuity slice as top-1%, and recompute any rates/dedup products that depend on which SDSS threshold is canonical.

## PAPER-GPT-M3 — MAJOR — Table I footnote $\spadesuit$, abstract, §4.2

**Issue:** The catalog-grade/exploratory split is arithmetically over-specified: the footnote gives catalog-grade $264{,}938$ plus LAMOST $113{,}342$ exactly equaling $378{,}280$, implying zero LAMOST overlap and zero LAMOST intra-survey duplicate loss, while the abstract says the exact split depends on cross-survey dedup geometry and is only $\sim113{,}000/\sim265{,}000$.  
**Fix:** Use the union-find cluster manifest to report exact unique counts by tier under a defined attribution rule, or keep the split approximate everywhere. Do not make the raw LAMOST detection count equal to its unique post-dedup contribution unless verified.

## PAPER-GPT-M4 — MAJOR — §5.2 NANOGrav, Appendix PTA MCMC

**Issue:** The PTA “likelihood” multiplies per-bin free-spectrum KDE posterior densities as independent likelihood factors, while admitting missing inter-bin covariance and prior/Jacobian effects. The proposed “Savage-Dickey on the existing chain” is not a valid Bayes factor for non-nested fixed-spectral-index model comparison with different amplitude priors, and “SMBHB strongly disfavored” remains too strong for a marginal $\gamma$ parameter-shift.  
**Fix:** Present only the marginal posterior shift in $\gamma$ as a descriptive diagnostic. For model comparison, compute evidences from the joint likelihood with covariance and model-specific priors, or remove Bayes-factor/Savage-Dickey language entirely.
