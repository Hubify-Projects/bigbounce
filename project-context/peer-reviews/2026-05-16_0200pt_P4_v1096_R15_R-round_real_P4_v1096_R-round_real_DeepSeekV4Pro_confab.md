# P4_v1096 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0200pt_P4_v1096_R15_R-round_real
**Wall time**: 174.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=77547, completion=7885, reasoning=6297, total=85432

---

## PAPER-DEE-1 — BLOCKER: Per-region asymmetry 0.32% not traceable to an on-disk artifact

**Section:** Conclusions (item 2), Table~\ref{tab:sky_balance}  
**Line reference:** LaTeX source near `\caption{CW fraction by sky region ... \label{tab:sky_balance}}`; footnote therein admits per-region values are manuscript-only.  
**Issue:** The headline claim that *“our maximum regional asymmetry is 0.32%”* is a direct, load-bearing contradiction of Shamir’s asymmetry. Table~\ref{tab:sky_balance} reports per-region CW fractions, but the verification artifact `global_cw_fraction.json` contains only the global value; the per-region numerators/denominators exist only in the manuscript. The paper’s own footnote acknowledges the gap (“A dedicated per-region JSON is queued for the next post-submission revision”). This violates the reproducibility requirement that every load-bearing scalar in the conclusions has a JSON/script/dataset that produces it.  
**Fix:** Provide an artifact that tabulates the per-region counts and CW fractions (e.g., a JSON with one entry per row of Table~\ref{tab:sky_balance}) and update the footnote to link that artifact. Until then, the claim is not independently verifiable.

---

## PAPER-DEE-2 — MAJOR: Fisher-floor wording in Conclusions is internally inconsistent

**Section:** Conclusions (item 1, sensitivity summary)  
**Line reference:** LaTeX paragraph after “No dipole detection …” that reads *“the statistical-only Poisson floor on the CW‑fraction half‑modulation $A/2$ is $0.2\%$ (corresponding to a full‑amplitude $A$‑floor of $0.4\%$ conservative, $\sim\!0.29\%$ Fisher exact …)”*.  
**Issue:** The two quantities are arithmetically incompatible. A half‑modulation floor of $0.2\%$ would give a full‑amplitude floor of $0.4\%$, not $0.29\%$. The $0.29\%$ Fisher‑exact value is the correct full‑amplitude $3\sigma$ floor derived from the unrounded half‑modulation $0.144\%$, while the $0.2\%$ half‑modulation is a conservative round‑up. The sentence conflates two different numbers, making the sensitivity statement contradictory.  
**Fix:** Rewrite the sentence to clearly separate the conservative rounded half‑modulation floor ($0.2\%$) from the Fisher‑exact full‑amplitude floor ($0.29\%$), e.g.: “The Poisson floor on the half‑modulation $A/2$ is $0.144\%$ (rounded conservatively to $0.2\%$); the corresponding full‑amplitude $A$ Fisher‑exact $3\sigma$ floor is $\sim\!0.29\%$.”  

---

## PAPER-DEE-3 — MINOR: Arithmetic mismatch in “$2\langle p_{\rm CW}\rangle-1\approx-0.0053$”

**Section:** Abstract (first paragraph)  
**Line reference:** “$2\langle p_{\rm CW}\rangle\!-\!1\!\approx\!-0.0053$ at $\langle p_{\rm CW}\rangle\!=\!0.4974$”  
**Issue:** With $\langle p_{\rm CW}\rangle = 0.4974$, $2\times0.4974-1 = 0.9948-1 = -0.0052$, not $-0.0053$. The off‑by‑one in the last significant digit is likely due to using the higher‑precision value $0.49735$, but the text quotes $0.4974$. The statement is not arithmetically reproducible from the displayed number.  
**Fix:** Either propagate the exact internal value $\langle p_{\rm CW}\rangle = 0.49735$ (and recompute to $-0.00530$) or keep $0.4974$ and adjust the product to $-0.0052$. The discrepancy is tiny but violates the “every displayed value should be derivable” standard.

---

## PAPER-DEE-4 — MINOR: No artifact that directly certifies the “$0.79\%$ raw CW excess” in the abstract

**Section:** Abstract (early mention of classifier bias)  
**Line reference:** “the pipeline exhibits … a classifier CW bias of only $0.79\%$”  
**Issue:** The $0.79\%$ value is taken from Table~\ref{tab:cw_frac} (Catalog A raw excess), which is backed by `global_cw_fraction.json` (global value) plus the spiral counts. However, the abstract mentions the number without a nearby artifact link, and the derivation requires combining the global CW fraction with the spiral‑only denominator $N_{\rm spiral}$. The JSON cited for the global fraction contains the catalog‑level $\CW/(\CW+\CCW)$ but not explicitly the excess as a percentage. While one can recompute it, a dedicated entry would improve provenance.  
**Fix:** Add a small computed field `raw_cw_excess_pct` to `global_cw_fraction.json` or reference the JSON directly in the abstract’s parenthetical text. This is a mild traceability improvement; not a blocker.

---

## PAPER-DEE-5 — NIT: The “$10{,}000$ isotropic‑null bootstrap” for the simple dipole is not linked to a dedicated artifact in the abstract

**Section:** Abstract (“real‑space dipole fit … $\sigma_{\rm dipole}=0.43$ ($p=0.30$, $N_{\rm MC}=10{,}000$)”)  
**Line reference:** Right before the mention of the injection‑recovery threshold.  
**Issue:** The abstract gives the dipole significance and $p$‑value without a parenthetical artifact pointer, whereas later sections reference `dipolar_analysis.log`/`summary.json`. For a “paranoid” review, the headline cosmological result should have an explicit artifact citation visible in the abstract itself.  
**Fix:** Insert “(artifact `dipolar_analysis.log`)” or a similar short reference after the statistic. This does not affect correctness but raises the provenance transparency of the central $p=0.30$ null.

---

## PAPER-DEE-6 — NIT: The “$\sim 21\%$ rotational uncertainty” in the abstract lacks a direct pointer

**Section:** Abstract (end of the TTA paragraph)  
**Line reference:** “per‑galaxy argmax labels carry $\sim\!21\%$ rotational uncertainty”  
**Issue:** The $21\%$ figure is explained in Sec.~\ref{sec:tta} and backed by `d4_tta_holdout_results.json`, but no artifact is mentioned in the abstract. A reader checking the abstract alone cannot trace the number.  
**Fix:** Add “(artifact `d4_tta_holdout_results.json`)” after the value, consistent with the practice used elsewhere in the paper for key numbers.  

---

**Overall verdict:**  
No new BLOCKER beyond the missing per‑region traceability (PAPER-DEE-1). The paper’s main dipole result is fully reproducible from the cited MASTER and injection‑recovery artifacts. The remaining items are wording inconsistencies or provenance‑tightening nits that do not invalidate the central conclusions.
