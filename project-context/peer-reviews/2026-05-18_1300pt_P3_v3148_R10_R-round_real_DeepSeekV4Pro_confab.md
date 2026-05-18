# P3_v3148_R10 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1300pt
**Wall time**: 276.1s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=60455, completion=13397, reasoning=11263, total=73852

---

### PAPER-DEE-B1: BLOCKER — Headline catalog size 378,280 is arithmetically inconsistent with reported survey-level detections and pairwise coincidences

**Location:** Abstract, §4.3, §6.4 deferral (a), §7 Conclusions.

**Issue:** The paper states that the sum of per-survey native detections is 388,493 and that there are 637 pairwise multi-survey coincidences. Under the all-pairwise assumption, the unique object count is \(388{,}493 - 637 = 387{,}856\). The headline \(378{,}280\) is \(9{,}576\) objects smaller—a discrepancy the paper itself labels an “invariant arithmetic incompatibility” and “pending recompute” in deferral (a). Yet the abstract and conclusions present \(378{,}280\) as the definitive catalog size without caveat, and all dependent numbers (point-source tier \(378{,}080\), compression \(2.629\%\), \(141\times\) scale increase) inherit this unresolved error.

**Fix:** Either recompute the union-find deduplication to produce a verified unique count and update all downstream figures, or, if the recompute cannot be completed, replace the headline with the arithmetic upper bound \(387{,}856\) and explicitly state that the exact count is under revision. At minimum, the abstract and conclusions must flag the uncertainty.

---

### PAPER-DEE-B2: MAJOR — Unphysical linear Fisher intervals for \(\sigma(f_{\rm NL})\) still quoted in abstract, §5, and conclusions

**Location:** Abstract (\(\sigma(f_{\rm NL})^{\rm GS} = 2.28 \pm 7.43\)), §5 (95% CI \([3.62, 12.95]\) for full sample), §7 Conclusions.

**Issue:** Caveats (i) and (j) demonstrate that the linear propagation \(\sigma(f_{\rm NL}) = 8.98 - 3.66\alpha\) violates Fisher-information positivity when extrapolated to the 95% \(\alpha\) confidence interval, and that the correct Fisher-positivity-respecting form gives asymmetric envelopes: \([2.4, 8.98]\) for the full sample and \([0.94, 8.98]\) for the high-confidence subset. Despite this, the abstract and conclusions still report the invalid symmetric error \(\pm 7.43\) for the high-confidence subset, and §5 presents the linear 95% CI \([3.62, 12.95]\) as the canonical interval. The paper itself acknowledges the linear extrapolation is unphysical for the 95% CI, yet it remains the quoted result.

**Fix:** Replace all linear-extrapolated \(\sigma(f_{\rm NL})\) intervals with the Fisher-positivity-respecting envelopes. If the linear central value is retained for compatibility, clearly label the 95% CI as invalid and provide the corrected asymmetric interval. The abstract must not quote the \(\pm 7.43\) error.

---

### PAPER-DEE-M1: MAJOR — 17.8% genuine novelty fraction lacks a linked reproducibility artifact

**Location:** Abstract, §4.1, §7 Conclusions.

**Issue:** The paper states that cross-matching the top-1,000 DESI anomalies against 20 all-sky catalogs via CDS X-Match yields 17.8% (178/1,000) genuinely novel objects. This is a headline discovery-rate figure, but no specific script, query log, or output file is referenced. Other key numbers in the paper are accompanied by explicit artifact paths (e.g., `alpha_empirical_results.json`), but the 17.8% result has no such provenance. A reader cannot verify or reproduce this number from the information provided.

**Fix:** Include the cross-match output (e.g., a CSV of the 1,000 objects with match flags) in the data release and cite its exact filename in the text. Alternatively, provide the CDS X-Match query parameters and a checksum of the result so that the figure is auditable.

---

### PAPER-DEE-M2: minor — “37.3 million sources” is ambiguous after Path-C reprocessing

**Location:** Abstract, §1, §7.

**Issue:** The abstract states the campaign applied BigAE to “37.3 million sources and CMB map patches.” The initial cross-transfer scan processed 37,292,042 sources (Table 1). However, the Path-C native retrains reprocessed some surveys with different sample sizes (e.g., SDSS native re-score used 1,925,279 spectra, not the full 2.3M; LAMOST used 11,334,161). It is unclear whether the 37.3M figure refers to the original cross-transfer input or the final Path-C processed total. This ambiguity could mislead readers about the actual scale of the final catalog construction.

**Fix:** Clarify whether the 37.3M is the initial scan volume or the Path-C reprocessed volume, and ensure the number matches the sum of spectra/patches actually scored in the final pipeline.

---

### PAPER-DEE-M3: minor — Fisher anchor values (\(\sigma(f_{\rm NL})=8.98, 8.43\)) not tied to specific script outputs

**Location:** §5, Appendix sensitivity table.

**Issue:** The linear scaling \(\sigma(f_{\rm NL}) = 8.98 - 3.66\alpha\) is calibrated using two points: the single-tracer baseline \(\sigma=8.98\) and the multi-tracer result \(\sigma=8.43\) at \(\alpha=0.15\). While the baseline is attributed to the DESI QSO forecast from Heinrich et al., the multi-tracer Fisher run that produces 8.43 is not linked to a specific artifact (e.g., a JSON output from the Fisher pipeline). The sensitivity table in the Appendix lists values but does not provide the raw Fisher matrix outputs. This makes the central forecast less reproducible.

**Fix:** Add a reference to the exact script and output file (e.g., `wave_14_ii_fisher_systematics/result.json` or a dedicated Fisher run artifact) that produces the \(\alpha=0.15\) constraint, so that the anchor point can be independently verified.

---

### PAPER-DEE-N1: nit — Abstract \(\alpha\) confidence interval wording could mislead about \(\sigma(f_{\rm NL})\) interval

**Location:** Abstract.

**Issue:** The abstract says “The 95% confidence interval covers \(\alpha \in [-1.08, +1.46]\) … Inserting the empirical central value into the Fisher pipeline yields \(\sigma(f_{\rm NL}) = 8.27 \pm 2.37\).” A reader might incorrectly assume that the \(\sigma(f_{\rm NL})\) 95% CI is also symmetric and given by \(\pm 1.96\times 2.37\). The paper later clarifies that the proper \(\sigma(f_{\rm NL})\) interval is asymmetric, but the abstract does not.

**Fix:** After stating the \(\alpha\) interval, add a brief note that the corresponding \(\sigma(f_{\rm NL})\) credible interval is asymmetric and given by the Fisher-positivity-respecting form (or cite the corrected envelope).
