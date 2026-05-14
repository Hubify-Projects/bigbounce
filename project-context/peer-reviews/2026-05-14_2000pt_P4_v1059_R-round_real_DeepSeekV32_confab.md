# P4_v1059 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_2000pt
**Wall time**: 129.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=54857, completion=1762, total=56619

---

**Review of "No Evidence for Large-Scale Parity Violation in Galaxy Morphology: A Survey-Scale Chirality Catalog of 8.47 Million Galaxies"**

**Overall Assessment:** The paper presents a substantial null result with a rigorous bias audit. The core methodology (equivariant TTA, MASTER deconvolution) appears sound, and the primary conclusions are well-supported. However, several key numerical results lack explicit, traceable provenance in the provided text, creating ambiguity about their exact derivation and reproducibility. No BLOCKERs were identified that would prevent arXiv submission, but several MAJOR clarifications are required.

---

## **Finding 1: MAJOR - Ambiguous Sensitivity Floor Definition**
**ID:** PAPER-DEE-M1
**Location:** Abstract, Sec. VIII.B (Sensitivity Floor)
**Issue:** The abstract states: "the conservative, systematic-inclusive empirical injection-recovery sensitivity floor is $|A_{\rm dipole}|\!>\!0.5\%$ (at $A\!=\!0.5\%$ the per-pixel-shuffle MC gives $P(\sigma\!>\!2)\!=\!0.18$; explicit 50\%-recovery at $3\sigmaunit$ is not demonstrated...)". This conflates a *detection threshold* (amplitude at which a signal would be recoverable with 50% probability at a given significance) with a *sensitivity floor* (minimum amplitude detectable). The text correctly notes the 50%-recovery at 3σ is not demonstrated within the tested grid, yet the ">0.5%" figure is presented as the "primary sensitivity figure." The relationship between the tested amplitudes (0.05% to 0.5%), the reported $P(\sigma>2)=0.18$ at 0.5%, and the final ">0.5%" claim is not mathematically justified from the provided results.
**Fix:** Clearly define "sensitivity floor" as, e.g., the amplitude $A_{min}$ for which $P(\sigma > 3) \geq 0.5$ (or another standard criterion). State explicitly that 0.5% is an *upper bound* on this floor based on the tested grid, and that the true floor may be higher. Rephrase to avoid the strict inequality ">0.5%", which is not directly supported by the $P(\sigma>2)=0.18$ result.

## **Finding 2: MAJOR - Inconsistent $N_{\rm spiral}$ Usage**
**ID:** PAPER-DEE-M2
**Location:** Abstract, Table 1 footnote, Sec. IV (Catalog Statistics)
**Issue:** The canonical spiral count $N_{\rm spiral}=3,201,160$ is stated as superseding an earlier snapshot count of $3,321,795$. However, Table 1 (sky balance) reports regional counts that sum to the snapshot total, and the abstract's Fisher-floor calculation uses the canonical count. It is unclear if the Fisher calculation, regional balances, and all error bars consistently use the canonical count. The footnote states the per-region $|\Delta|$ values shift by <4% and are "insensitive," but this needs verification for all derived statistics (especially binomial $\sigma$).
**Fix:** In Table 1, replace the "All sky (snapshot)" row with the canonical total and provide a note that regional counts are from the snapshot but the CW fraction 0.4974 is canonical. Explicitly state that *all* statistical calculations (binomial errors, Fisher floor, dipole fits) use the canonical $N_{\rm spiral}=3,201,160$. Provide the recalculated regional $|\Delta|$ values in the supplement if they differ.

## **Finding 3: MAJOR - Missing Provenance for Key Statistical Results**
**ID:** PAPER-DEE-M3
**Location:** Abstract, Sec. V.B (Dipole Analysis)
**Issue:** The abstract reports: "real-space dipole fit yields $\sigma_{\rm dipole}=0.43$ ($p=0.30$ at $N_{\rm MC}=10,000$; canonical results file `outputs/dipole/summary.json`)". The paper later states the MASTER-deconvolved $\ell=1$ coefficient is $-0.122\sigma$ with $p_{MC}\approx0.45$ from 500 MC realizations. The provenance for these numbers (the specific MC realizations, random seeds, and the exact calculation of $p$ and $\sigma$) is not fully described in the text. While files are cited, the in-text description of the methods (e.g., how $\sigma_{\rm dipole}$ is calculated from the MC ensemble) is insufficient for independent evaluation.
**Fix:** In Sec. V.B, explicitly define the test statistic for the dipole fit (e.g., amplitude of best-fit vector) and how its significance ($\sigma$, $p$) is derived from the MC null distribution (e.g., (data statistic - mean(null)) / std(null)). Specify the exact random seed used for the canonical $N_{\rm MC}=10,000$ run. For the MASTER result, clarify if the $-0.122\sigma$ is $(C_1 - \langle C_1^{null} \rangle)/\sigma_{null}$ and how $\sigma_{null}$ is computed (std of 500 MC $C_1$ values).

## **Finding 4: minor - Ambiguous "Projection" for MASTER result**
**ID:** PAPER-DEE-m4
**Location:** Abstract, Sec. V.B, Conclusions
**Issue:** The abstract states: "the analytic projection onto the canonical Catalog~C parameters ($N_{\rm spiral}\!=\!3{,}201{,}160$, $f_{\rm sky}\!=\!0.491$) gives $+0.2595\sigmaunit$". It is unclear what "analytic projection" entails. Is this a rescaling of the subsample-mask result? If so, the scaling factors (e.g., $\propto \sqrt{f_{sky}/N}$) should be explicitly stated in the text or in a footnote.
**Fix:** In the paragraph discussing the MASTER result in Sec. V.B, add a brief equation or description of the projection: e.g., "We rescale the subsample-mask significance by the ratio of shot-noise uncertainties $\sigma_{null} \propto 1/\sqrt{N f_{sky}}$ to estimate the significance under the canonical full-sample parameters, obtaining $+0.26\sigma$."

## **Finding 5: minor - Unclear "9.5σ" Monopole Significance**
**ID:** PAPER-DEE-m5
**Location:** Abstract, Sec. IV (Global CW Fraction)
**Issue:** The global CW fraction is given as $0.4974 \pm 0.000279$, a $9.5\sigma$ deviation from 0.5. The uncertainty is presumably the binomial standard error $\sqrt{p(1-p)/N}$. However, the text also mentions spatial correlations may reduce effective $N$. The $9.5\sigma$ claim should be accompanied by a note that this assumes independent classifications, and that the true significance may be lower if spatial correlations are significant.
**Fix:** In the sentence reporting the $9.5\sigma$ deviation, add a clause: "assuming statistically independent classifications; spatial correlations in survey conditions may reduce the effective sample size, making this a formal upper limit on the significance."

## **Finding 6: nit - Inconsistent MC Counts in Footnotes**
**ID:** PAPER-DEE-n1
**Location:** Footnote 2 (MC counts)
**Issue:** Footnote 2 lists three distinct Monte Carlo counts for different analyses (10k, 500, 1k). While justified, the varying counts are spread across the paper and summarized only in this footnote. This could cause confusion for readers skimming the results sections.
**Fix:** Consider adding a small table in Sec. V.B (or the footnote) summarizing: Analysis | MC Realizations | Purpose. This improves readability.

---
**Summary:** The paper is methodologically sound and the null result is robustly supported. The primary needs are to tighten the definitions of the sensitivity floor (M1), ensure consistency in the spiral count used for all derived statistics (M2), and improve the traceability of key statistical results (M3). With these clarifications, the paper is suitable for arXiv submission.
