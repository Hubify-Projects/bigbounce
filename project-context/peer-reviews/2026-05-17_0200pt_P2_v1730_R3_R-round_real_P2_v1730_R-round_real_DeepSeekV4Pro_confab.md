# P2_v1730 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P2_v1730_R3_R-round_real
**Wall time**: 324.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=29903, completion=9006, reasoning=7641, total=38909

---

## Findings

### PAPER-DEE-B1 (BLOCKER)
**Location:** §9 (Conclusion), paragraph “Our Bayesian model comparison…”  
**Issue:** The conclusion states the Bayesian analysis was “validated over \(>\!6\!\times\!10^5\) Monte Carlo realizations.” This is a stale, incorrect count. The body of the paper (§6.3 and the abstract) explicitly corrects this to \(3 \times 10^5\) (three independent \(10^5\) ensembles) and notes that “any larger number was an aggregation error.” Retaining the \(>6\times 10^5\) figure in the conclusion directly contradicts the internal correction and amounts to a factual inaccuracy in the paper’s closing summary.  
**Fix:** Replace “\(>\!6\!\times\!10^5\)” with “\(3 \times 10^5\)” (or “three \(10^5\)-realization ensembles”) to match the audited count given elsewhere.

---

### PAPER-DEE-M1 (MAJOR)
**Location:** §8.4 “Joint \((f_{\rm NL},\,n_{f_{\rm NL}})\) Forecast…” and discussion thereof  
**Issue:** Specific numerical results for the joint scale‑dependent‑bias Fisher analysis are quoted as key findings: \(\sigma(n_{f_{\rm NL}}) = 0.086\), marginalized \(\sigma(f_{\rm NL}) = 0.44\), and a derived detection significance of \(\sim 9.9\sigma\). The paper explicitly states that the Six‑bin Fisher‑input release (per‑bin \(k_{\min}(z)\), \(\bar n(z)\), \(b_1\), \(b_\phi\) scheme, etc.) is deferred to a companion artifact and is “not yet on disk in this release.” Consequently, none of these numbers can be reproduced from the manuscript or the linked repository. Presenting them as load‑bearing P2 results without any verifiable provenance violates basic reproducibility standards.  
**Fix:** Either (a) include the complete Fisher matrix, inputs, and a validating script in the current repository, or (b) remove all specific numeric claims (\(\sigma(n_{f_{\rm NL}})\), \(\sigma(f_{\rm NL})\), and the \(9.9\sigma\) significance) and replace them with a qualitative statement that the joint analysis is pending release of the input data.  

---

### PAPER-DEE-M2 (MAJOR)
**Location:** §8.4, sentence “Note specifically: the implied \(\sigma_{\rm unmarg}(f_{\rm NL}) \approx 0.114\) from this joint analysis would be \(6.1\times\) sharper than the bispectrum‑only \(\sigma(f_{\rm NL}) = 0.7\) baseline, which is sharper than any published SPHEREx SDB forecast known to us…”  
**Issue:** The quoted \(\sigma_{\rm unmarg} \approx 0.114\) is an order‑of‑magnitude sharper than the known SPHEREx SDB forecasts (Doré+2014, Heinrich+2023). While the paper acknowledges the discrepancy, it nevertheless promotes the derived \(9.9\sigma\) as a notable self‑consistency check in the same subsection. This creates confusion about the reliability of the joint Fisher matrix, which lacks public inputs and produces a result the authors themselves flag as implausibly tight.  
**Fix:** If the Fisher matrix cannot be released immediately, add an explicit, standalone caveat that this forecast should not be quoted until the inputs are validated and the sharpness is explained (e.g., an error in the \(k_{\min}\) per bin or the multi‑bin stacking). Alternatively, remove the numerical results entirely until a rigorous cross‑check against published forecasts is performed and documented.

---

### PAPER-DEE-m1 (minor)
**Location:** Abstract, §4, and elsewhere (e.g., “Heinrich et al.~2024”)  
**Issue:** The text consistently refers to the Heinrich et al. SPHEREx forecast as “2024,” but the citation key used throughout is `\cite{Heinrich:2023}`. This year mismatch (2024 vs. 2023) will confuse readers and may cause the reference to be missed by bibliographic indexers.  
**Fix:** Align the in‑text year with the citation key. If the paper was published in 2023, change “2024” to “2023” everywhere; if a 2024 update exists, provide the correct bibkey and update the key accordingly.

---

### PAPER-DEE-m2 (minor)
**Location:** §3.2 (Template Projection) and Fig. 2, description of weighting schemes  
**Issue:** The central template‑overlap factor \(r = 0.84 \pm 0.02\) is reported as the result of “10 physically motivated weighting schemes (uniform, CMB Fisher, LSS scale‑dependent‑bias, SPHEREx‑like, MegaMapper‑like, and five region‑masked variants).” None of these weighting schemes are defined in the paper; the reader cannot map the quoted range \([0.829, 0.876]\) to specific physical assumptions without consulting the repository. While the scripts are said to be available, a forecasting paper intended for PRD/MNRAS should describe the weighting schemes sufficiently for a reader to understand the envelope.  
**Fix:** Add a short table or enumerated list in §3.2 that spells out each of the ten weighting schemes, their motivation, and their individual \(r\) values, or at minimum define the four non‑masked schemes mathematically.

---

### PAPER-DEE-n1 (nit)
**Location:** §9 (Conclusion), “SPHEREx (NASA, launched March 2025; primary survey nominally complete after \(\sim 25\) months of operations, with the first PNG‑suitable public data release expected \(\sim 2028\))”  
**Issue:** SPHEREx’s nominal 25‑month survey ends around April 2027; a “PNG‑suitable public data release” in 2028 is plausible but the paper provides no citation for this release timeline. For a forecast that depends heavily on the data‑release schedule, a supporting reference (e.g., a SPHEREx data‑management plan or mission‑level document) would strengthen credibility.  
**Fix:** Add a footnote or parenthetical reference to the SPHEREx data‑release policy document (if available) or note that the timeline is estimated based on publicly stated mission schedules.
