# P1B_v1B013_R8 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1145pt
**Wall time**: 304.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=16606, completion=9174, reasoning=7541, total=25780

---

# Adversarial Peer Review — Paper 1B v1B.0.13 (Convergent Regression Audit)

No blocker-grade regressions found in the computed arithmetic. However, multiple provenance gaps and one methodologically questionable prior statement survive the v1B.0.13 patch. Six findings follow.

---

## Finding PAPER-DEE-M1
**Classification:** MAJOR  
**Location:** Table~1B caption, “Caveats” paragraph, item (b); also repeated in \ref{sec:fullcomp} discussion of priors.

**Issue:** The text states that the iter2 chain uses *“the Planck~2018 prior on τ (Gaussian centered at the Planck best‑fit value) rather than a free τ from a low‑ℓ likelihood.”* If a Gaussian prior was truly applied, that is a non‑standard choice that biases the τ → H₀ → w₀ correlation and is not the canonical Planck‑like setup. However, the likelihood stack explicitly includes Planck 2018 lowl.EE, which already constrains τ. The statement is either an erroneous description (the lowl.EE data acts as a likelihood, not a prior) or an undocumented method that contradicts the reproducibility promise. Either way, it undermines the rigour of the τ caveat and leaves the τ posterior provenance ambiguous.

**Fix:** (1) Clarify whether an additional Gaussian prior was actually placed on τ in the YAML configuration; if yes, provide the exact prior width and justify its origin. (2) If no such prior was used, strike the sentence and simply note that τ is constrained by the Planck lowl.EE likelihood.

---

## Finding PAPER-DEE-M2
**Classification:** MAJOR  
**Location:** Section 4, paragraph “Independent verification”, near Eq. (1); the split bias values 0.032° vs 0.040°.

**Issue:** The claim of an amplitude‑dependent bias (0.032° for β=0.27°, 0.040° for β=0.342°, described as ~12 % relative change) is presented as *“statistically rigorous”* per the R7 closure, yet no uncertainty is given on the recovered angles from the 500 Monte Carlo realisations. The standard error of the mean recovery is essential to judge whether the 0.008° difference is statistically significant. Without it, the amplitude‑dependence claim is unverifiable and the systematic floor of 0.04° is a raw residual, not a confidence‑validated bound.

**Fix:** Compute (or extract from the pipeline output) the 1σ uncertainty on \hat{β} for each injection and quote it. Then assess whether the bias shift is statistically meaningful. If it is not, retract the “amplitude‑dependent” qualifier and simply state the conservative bias envelope.

---

## Finding PAPER-DEE-m1
**Classification:** minor  
**Location:** Section 5.2 (Converged iter2 posterior interpretation), paragraph starting “*Physics interpretation (Table~1B).*”

**Issue:** The phrase “canonical quintom signature” and the argument that the result requires a second degree of freedom (quintom‑B) are presented without a citation to the relevant quintom dark‑energy literature. While the DESI DR2 paper is cited later, the interpretation paragraph itself does not directly reference any quintom model (e.g., Feng 2005; Guo 2005; DESI quintom‑B discussion). In a technical paper with strict provenance requirements, the absence of a reference for the key interpretive term *“quintom‑B”* weakens the audit trail.

**Fix:** Add a short citation to a standard quintom‑B reference (e.g., the DESI 2025 DR2 paper’s explicit quintom‑B analysis section, or the seminal Feng 2005 paper) in the same sentence where “canonical quintom signature” appears.

---

## Finding PAPER-DEE-m2
**Classification:** minor  
**Location:** Section 7 (Cross‑Paper Verification Status), Table~\ref{tab:crosspaper} caption and the conclusion’s “Forward” paragraph.

**Issue:** The paper bumps deferral targets to *“v1B.0.13+”* in multiple places (e.g., the Savage–Dickey ln B recompute, the coordinated P1(a) update), but the conclusion paragraph still speaks of *“v1B.0.12+ will fold…”*, which is stale version‑numbering. This creates an inconsistency in the planned‑action audit and risks a reader confusing which version carries the empirical update.

**Fix:** Change *“v1B.0.12+”* to *“v1B.0.13+”* in the conclusions “Forward” paragraph to match the current version and the other deferral bumps.

---

## Finding PAPER-DEE-m3
**Classification:** minor  
**Location:** Table 1B, χ² decomposition lines; Abstract and Conclusions when quoting BAO/CMB/SN χ² contributions.

**Issue:** The provenance of the decomposed χ² values (10.6 ± 1.8 for BAO, 10983.9 ± 5.3 for CMB, 3043.0 ± 1.6 for SN) is stated to be in the `posterior_summary.txt` file. However, the paper gives no indication of *how* these numbers were produced from the Cobaya chain — e.g., whether they are posterior means of derived χ² parameters added to the chain via a script, or computed externally in a GetDist custom step. Without a named script or documented derived‑parameter extraction, the numbers are reproducible only if a reader already knows Cobaya’s internal likelihood decomposition. The sum matches the total and is plausible, but the audit trail is incomplete.

**Fix:** In the Table 1B caption or reproducibility section, add a one‑line note: “χ² contributions derived by extracting the per‑likelihood ` chi2` columns from the chain via `GetDist`’s `sample_analyser` (or the specific script `extract_chi2.py`) as reproduced in the cited `posterior_summary.txt`.” That makes the provenance explicit.

---

## Finding PAPER-DEE-m4
**Classification:** nit  
**Location:** Abstract, last paragraph: *“w_0+w_a = -1.48 ± 0.15 phantom-crossing required”*

**Issue:** The value −1.4788 is incorrectly rounded to −1.48 with a larger uncertainty 0.15 (the table gives 0.1485). While the rounding is reasonable, the abstract earlier quotes w₀ and w_a to four decimal places, so the sudden coarse rounding of w₀+w_a to two significant digits is a minor inconsistency. Further, the ±0.15 is given to two significant figures whereas the underlying error is 0.1485, which would round to 0.15 anyway; no arithmetic error, just a stylistic inconsistency.

**Fix:** Either unify the significant‑figure policy (all parameters to two decimal places, or all to three or four) throughout the abstract, or keep it as‑is and note that rounding is intentional.

---

**Overall:** The new iter2 posterior is internally consistent and its numbers trace back to a named on‑disk summary file. The principal load‑bearing gaps are the τ‑prior ambiguity and the unsupported bias split claim. Addressed, these would raise the verification bar to the demanded standard.
