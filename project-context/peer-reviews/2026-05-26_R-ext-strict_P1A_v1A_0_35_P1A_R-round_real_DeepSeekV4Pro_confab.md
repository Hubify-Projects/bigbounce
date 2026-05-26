# P1A R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P1A_v1A_0_35
**Wall time**: 78.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=28899, completion=4064, reasoning=3063, total=32963

---

## PAPER-DEE-B1 (BLOCKER)
**Location:** §4 (four-route no-go), immediately before §4.1; also scattered inline notes throughout (e.g. §12, §13, §14, footnotes).  
**Issue:** The manuscript body contains extensive audit‑trail / AI‑vendor / version‑history prose that must be purged before journal submission. Examples:  
- “A multi‑vendor adversarial‑review round (GPT‑5.5 / Gemini‑2.5‑Pro / Grok‑4‑fast / Perplexity Sonar Pro / DeepSeek‑V3.2, all queried via the OpenRouter unified API on 2026‑05‑14) surfaced three substantive theory‑derivation BLOCKERs…”  
- “v1A.0.28 R7 Grok‑B1 closure: previously this paragraph carried a full internal cross‑vendor review history …”  
- “R23 Gemini‑3.1‑Pro PAPER‑GEM‑M1 reminder …”  
- “v1A.0.34 R23 undef‑ref closure …”  
- The footnote in Table 2 describing an unconverged MCMC chain with live status (“At the time of this writing the chain has accumulated … we deliberately do not commit to a specific calendar date …”).  
**Fix:** Remove all references to specific AI models, API platforms, internal review rounds, version‑history tags, and live‑run status. Retain only the scientific content; the audit trail belongs in a separate reproducibility log, not in the journal manuscript.

## PAPER-DEE-M1 (MAJOR)
**Location:** Abstract, §1 (Table 1), §13, §15.  
**Issue:** Headline scalar numbers—\(H_0 = 67.68 \pm 1.06\) km s⁻¹ Mpc⁻¹, \(\Delta N_{\rm eff} \approx 0\), and the SPHEREx \(3\)–\(5\sigma\) realistic significance—are stated as results but their provenance is entirely deferred to unpublished companion papers (Paper I(b), Paper II). No data, chain files, or Fisher‑matrix inputs are provided in this manuscript, and the companion papers are not yet publicly verifiable. The numbers are therefore untraceable from the present submission.  
**Fix:** Either (a) include the essential data, likelihoods, and Fisher‑forecast details in this paper (or a supplement) so that the numbers can be reproduced, or (b) remove the specific numerical claims and replace them with qualitative statements that do not require the companion papers to be accepted.

## PAPER-DEE-M2 (MAJOR)
**Location:** Abstract, §1, §13, §14.  
**Issue:** The phrase “definitively erased” (and similar “definitive” language) is used to describe the erasure of the matter‑bounce \(f_{\rm NL} = -35/8\) signature by \(N_{\rm tot} \gtrsim 60\) e‑folds. This claim is based on a simple e‑fold scaling argument, not on a joint nuisance‑marginalized model fit that simultaneously varies \(N_{\rm tot}\), the bounce parameters, and the inflationary sector. The word “definitively” overstates the certainty of a purely theoretical, order‑of‑magnitude argument.  
**Fix:** Replace “definitively erased” with “suppressed to unobservable levels under the stated assumptions” or equivalent, and explicitly note that no joint statistical comparison has been performed.

## PAPER-DEE-m1 (minor)
**Location:** §5, §3, and throughout.  
**Issue:** The paper references observational channels (galaxy spin dipole, CMB \(EB\) birefringence) but provides no data‑vector definitions table. Even though the detailed data are in companion papers, a summary table listing the observables, binning, survey, and null‑model used would greatly aid reproducibility and satisfy the journal’s expectation of a self‑contained methods section.  
**Fix:** Add a concise table (e.g., in §5 or an appendix) that defines the data vectors, their sources, and the primary null model for each channel, with references to the companion papers for full details.

## PAPER-DEE-m2 (minor)
**Location:** Title page (`\date{\paperTimestamp{} --- \paperVersion}`).  
**Issue:** The manuscript carries an internal version tag “v1A.0.35” in the date line. While not as severe as the body contamination, this is non‑standard for a journal submission and may confuse the editorial office.  
**Fix:** Replace with a standard submission date (e.g., “May 22, 2026”) and remove the version string.

## PAPER-DEE-n1 (nit)
**Location:** Footnote to Table 2 (the “Free‑\(w_0 w_a\) chain status” footnote).  
**Issue:** The footnote reports live, unconverged MCMC chain statistics (“\(\hat R - 1 \approx 3\times 10^{-2}\) … descending monotonically … we deliberately do not commit to a specific calendar date for convergence”). This is internal progress reporting, not a scientific result, and has no place in a journal article.  
**Fix:** Delete the footnote. If the \(w_0 w_a\) extension is relevant, state that it is under investigation and will be reported elsewhere; do not include real‑time chain diagnostics.
