# P4_v1056 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_1700pt
**Wall time**: 79.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=53288, completion=1395, total=54683

---

# Adversarial Peer Review: Chirality Catalog Paper v1.0.56

**Overall Assessment:** No BLOCKER-grade issues found. The paper demonstrates a high degree of numerical provenance and traceability. The abstract and conclusions are supported by explicit references to JSON artifacts, scripts, and datasets. The surviving issues are minor clarifications or documentation items that do not prevent publication readiness.

---

## PAPER-DEE-M1
**Classification:** MAJOR  
**Location:** Abstract, Conclusions, Section 5 (Sensitivity Floor)  
**Issue:** Ambiguous and potentially misleading presentation of the sensitivity floor. The abstract states: "The conservative, systematic-inclusive empirical injection-recovery sensitivity floor is $|A_{\rm dipole}|\!>\!0.5\%$ (at $A\!=\!0.5\%$ the per-pixel-shuffle MC gives $P(\sigma\!>\!2)\!=\!0.18$; explicit 50\%-recovery at $3\sigmaunit$ is not demonstrated... hence the strict inequality)". This conflates a detection threshold (amplitude at which recovery probability >50%) with a sensitivity "floor". The stated $>0.5\%$ is a lower bound on the threshold, not a measured floor. The accompanying "Fisher-floor statistical Poisson asymptote" of $|A_{\rm dipole}|\!\lesssim\!0.29\%$ is presented as a separate, cleaner number, creating confusion about which figure represents the experiment's true sensitivity.  
**Fix:** Clarify the language. State unambiguously: The empirical injection-recovery test shows that for an injected dipole amplitude $A=0.5\%$, the probability of a $>2\sigma$ detection is only 18%. Therefore, the $3\sigma$ detection threshold is **above** $0.5\%$. The $0.29\%$ Fisher floor is the theoretical statistical limit under ideal, zero-systematics conditions. The operational sensitivity is bounded below by $0.5\%$.

---

## PAPER-DEE-M2
**Classification:** MAJOR  
**Location:** Abstract, Section 4.2 (Dipole Analysis), Footnotes  
**Issue:** Proliferation of Monte Carlo (MC) counts and normalization snapshots creates a traceability hazard. The paper uses $N_{MC}=10,000$ for the simple dipole, $500$ for the post-MASTER $\ell=1$ null, and $1,000$ for higher multipoles. While justified in Footnote \ref{fn:mc_count}, the reader must cross-reference to understand why different counts are used. Furthermore, the narrative switches between "canonical $N_{\rm spiral}=3,201,160$" and older snapshot totals ($3,321,795$), requiring careful footnotes (e.g., Table \ref{tab:sky_balance}) to avoid misinterpretation.  
**Fix:** Add a concise summary table in the methods or dipole section listing each key result (simple dipole, post-MASTER $\ell=1$, bandpowers) alongside its $N_{MC}$, $N_{\rm spiral}$ denominator, and primary artifact path. This provides a single point of provenance verification.

---

## PAPER-DEE-m3
**Classification:** minor  
**Location:** Section 3.4 (Bias Hardening Suite), Table \ref{tab:bias_tests}  
**Issue:** The bias test thresholds are acknowledged as "generous relative to the catalog's claimed 0.2\% sensitivity". Test T8 (CW/CCW balance) has a threshold of $50\% \pm 10\%$, which is far above the sub-percent level of interest. Passing these tests does not guarantee the absence of biases at the relevant amplitude for the dipole null.  
**Fix:** In the table caption or accompanying text, explicitly state: "These thresholds are sanity checks for gross systematics ($\sim10\%$ level). They are not sufficient to validate the sub-percent sensitivity of the dipole measurement, which relies on the equivariant TTA procedure."

---

## PAPER-DEE-m4
**Classification:** minor  
**Location:** Section 4.1 (Global CW Fraction), Table \ref{tab:cw_frac}  
**Issue:** The uncertainty $\sigma = \sqrt{p(1-p)/N_{\rm spiral}}$ is quoted as $\pm 0.0003$, but the text correctly notes this assumes independent classifications. The acknowledgment that "spatial correlations... reduce the effective sample size" is buried in the paragraph. The formal $9.5\sigma$ significance of the monopole offset is therefore an upper limit.  
**Fix:** Move the caveat about spatial correlations and effective sample size ($N_{\rm eff}$) closer to the significance statement. Consider rephrasing: "The nominal binomial significance is $9.5\sigma$; the true significance may be lower due to spatial correlations."

---

## PAPER-DEE-m5
**Classification:** minor  
**Location:** Section 5 (Conclusions), Paragraph "Canonical-$N$ MASTER projection at $\ell\!=\!1$ (v1.0.55)"  
**Issue:** The analytic projection of the subsample-mask $\ell=1$ result ($-0.122\sigma$) to the canonical parameters yields $+0.2595\sigma$. The sign reversal and the fact that this is an analytic projection, not a direct recomputation, is subtle. The text states a direct recompute "remains as a lower-priority post-arXiv-submission verification item".  
**Fix:** Add a brief sentence in the abstract or executive conclusions noting that the primary $\ell=1$ null is robust to mask and normalization choices, as evidenced by the analytic projection remaining within $|\sigma| < 1$.

---

## PAPER-DEE-n6
**Classification:** nit  
**Location:** Throughout, especially Abstract and Section 4.2  
**Issue:** Over-use of the $\sigmaunit$ macro and inline TeX formatting ($\sigmaunit$) makes some sentences, particularly in the abstract, difficult to parse visually (e.g., "$-0.122\sigmaunit$", "$6.48\sigmaunit$").  
**Fix:** For improved readability, consider using the standard symbol $\sigma$ in the abstract, as the macro does not provide semantic benefit there. Retain the macro in the body if needed for consistency.

---
**Final Statement:** Zero BLOCKERs identified. The paper is publish-ready from a confabulation-hunting perspective. All load-bearing scalars in the abstract and conclusions are traceable to specific JSON artifacts, scripts, or dataset columns as required. The surviving MAJOR and minor issues pertain to clarity of interpretation and documentation, not to a lack of numerical provenance.
