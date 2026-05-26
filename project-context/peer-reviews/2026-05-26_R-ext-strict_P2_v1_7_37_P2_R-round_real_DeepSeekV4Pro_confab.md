# P2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P2_v1_7_37
**Wall time**: 103.5s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=32177, completion=4749, reasoning=3713, total=36926

---

## Referee Audit Report  
### Reviewer focus: traceable provenance of load-bearing scalars; audit-trail contamination; reproducibility.

---

## PAPER-DEE-B1 (BLOCKER)  
**Location:** LaTeX preamble, commented block after `\date{May 24, 2026 PDT --- v1.7.37}`.  
**Issue:** The source file contains a large, detailed audit-trail paragraph (AI‑vendor names, cron‑fire ticks, internal round labels “R-next-f brutal-honesty-Grok”, “Gemini”, cross‑model review stages) that must be purged before journal submission.  
**Fix:** Delete the entire commented block and all other similar vendor/version‑history comments from the manuscript source.  

---

## PAPER-DEE-B2 (BLOCKER)  
**Location:** Section 9.4 (“Discussion”) — the joint‑Fisher forecast paragraph introducing `σ(n_fNL) = 0.086`, `ρ = 0.966`, marginalised `σ(fNL) = 0.44`, and implied `~9.9σ` detection significance.  
**Issue:** The paper explicitly states that the six‑bin Fisher inputs (“per‑bin k_min, n_bar, b_1, b_phi scheme, photo‑z scatter, survey volume”) are *not* on disk in this release. The quoted numbers are therefore unreproducible from the supplied artifacts and violate journal‑level provenance requirements for load‑bearing scalars.  
**Fix:** Either (a) release the missing Fisher‑input table and provide the specific script that produces the quoted numbers, or (b) remove all quantitative detection‑significance figures from the discussion and replace with a qualitative statement, leaving only the qualitative degeneracy information.  

---

## PAPER-DEE-B3 (MAJOR)  
**Location:** `\date{May 24, 2026 PDT --- v1.7.37}` vs. the GitHub link `\texttt{v1.7.26-paper2}` in “Data and Code Availability”.  
**Issue:** The manuscript version tag and the archived code release tag are mismatched (v1.7.37 ≠ v1.7.26). This creates ambiguity about which code version actually produced the results, undermining reproducibility.  
**Fix:** Align the tags — either update the GitHub link to a release that matches the paper version, or clarify in the Availability section that the linked tag is the exact version used and explain the version‑number discrepancy.  

---

## PAPER-DEE-B4 (MAJOR)  
**Location:** Section 9.4 — the joint `(fNL, n_fNL)` Fisher forecast.  
**Issue:** The paper reports specific marginalized uncertainties (e.g., `σ(fNL) = 0.44`) but does not provide the data‑vector definitions (per‑bin survey parameters) in a table or appendix, deferring to a “companion artifact”. A reader cannot reproduce or even verify the quoted numbers from the paper alone.  
**Fix:** Add a table (e.g., in an appendix) giving the complete six‑bin Fisher input: `k_min(z)`, `n_bar(z)`, `b_1`, `b_phi` scheme, photometric‑z scatter, and survey volume for each bin. If the table cannot be supplied now, the specific numerical uncertainties must be removed.  

---

## PAPER-DEE-B5 (minor)  
**Location:** Abstract, final third — the sentence beginning “(the abstract previously gave only the central ~2.6σ; …)”.  
**Issue:** This is a stale editorial meta‑comment referring to a previous version of the abstract; it describes the document history rather than the science. Such revision‑tracking prose does not belong in a journal submission.  
**Fix:** Delete the parenthetical aside and any other self‑referential version‑history language (e.g., “the abstract previously gave …”, “the abstract’s headline … is consistent with … here”).  

---

## PAPER-DEE-B6 (minor)  
**Location:** Section 5.2 (“Template Projection …”), Eq. (7) and surrounding text.  
**Issue:** The headline `r = 0.84 ± 0.02` is said to come from 10 physically motivated weighting schemes, but only four distinct numerical values are listed (0.829, 0.830, 0.835, 0.876). The reported ±0.02 error bar cannot be verified from the displayed data alone; the full set of 10 weights or the aggregation script is not cited by filename.  
**Fix:** Provide the complete set of 10 weighting‑scheme values in a footnote or table, or cite the exact JSON/script (e.g., `phase3_fisher_overlap.json`) that produces the ±0.02 spread, so that the stated central value and uncertainty are directly traceable.
