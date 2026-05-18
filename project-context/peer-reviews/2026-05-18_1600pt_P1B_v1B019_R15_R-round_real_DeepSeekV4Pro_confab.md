# P1B_v1B019_R15 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1600pt
**Wall time**: 185.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=18120, completion=5799, reasoning=4670, total=23919

---

## PAPER-DEE-B1 — MAJOR — Section 3, M_B–H_0 arithmetic audit paragraph

The verification that the joint posterior ``(\(M_B = -19.263\), \(H_0 = 67.69\))'' lies at a 0.155 mag offset from the Riess anchor relies on two numbers that are not consistently reported or source-traceable in the paper:
- The value \(H_0 = 67.69\) km s⁻¹ Mpc⁻¹ **differs** from the full‑tension posterior mean in Table 1 (\(H_0 = 67.68 \pm 1.06\)).
- The absolute magnitude posterior mean \(M_B = -19.263 \pm 0.049\) mag is **absent from all tables and is not linked to a chain output file** (the text merely mentions ``chain sample‑mean readout'' and an audit file \texttt{shoes\_yaml\_audit.md}, which is not a standard MCMC summary artifact).

A reviewer cannot reproduce the offset \(0.155\) mag or the implied \(3.17\sigma\) significance from numbers displayed anywhere else in the manuscript.  
**Fix:** Use the \(H_0\) value exactly as reported in Table 1 (or explain the 0.01 km s⁻¹ Mpc⁻¹ rounding difference) and add the full‑tension \(M_B\) posterior mean and uncertainty to a table, explicitly referencing the specific GetDist output file (\texttt{...\allowbreak/fulltension\_M\_B\_summary.txt}) that contains these values.

---

## PAPER-DEE-B2 — minor — Section 3 text vs. Table 1 \(H_0\) consistency

The prose states ``The full‑tension chain returns \(H_0 = 67.69 \pm 1.06\) km/s/Mpc'' while Table 1 of the same paper (and the abstract) reports \(H_0 = 67.68 \pm 1.06\). The discrepancy is small but introduces ambiguity about which value was actually used in the \(M_B\)‑offset arithmetic.  
**Fix:** Reconcile the two numbers; if the correct posterior mean from the chain is 67.69, the table should be updated.

---

## PAPER-DEE-B3 — minor — Abstract “309,789” sample provenance

The headline figure “309,789 frozen samples” in the abstract is derived as the sum \(176{,}840 + 132{,}949\) from Table \ref{tab:verification}, but neither the table nor the text cites a static artifact (e.g., \texttt{chain\_sample\_counts.json}) that stores those raw‑chain totals. The repository provides YAML configs and a regeneration script, but the chain outputs themselves are not pre‑computed, so a reviewer cannot verify the exact counts without running the full MCMC.  
**Fix:** Include a lightweight JSON summary file in the reproducibility directory that contains the final accepted‑sample counts for each frozen chain (already computed by the author), making the number instantly auditable.

---

## PAPER-DEE-B4 — nit — Section 6 ALP arithmetic rounding

The birefringence estimate ``\(\beta \approx \frac{\alpha_{\rm EM}\times 8}{4\pi}\times 1.07 \approx 0.29^\circ\)'' evaluates to \(0.285^\circ\) (using \(\alpha_{\rm EM}=1/137\), \( \alpha_{\rm EM}/(4\pi) \approx 5.81\times10^{-4}\), product \(0.00465\) rad → \(0.266^\circ\) with factor 1.0, or \(\approx 0.285^\circ\) with 1.07).  
**Fix:** Either state the value as \(0.285^\circ\) (or \(0.29^\circ\) after explicit rounding statement) to avoid an inconsistency with the more precise arithmetic shown later in the same section.

---

## PAPER-DEE-B5 — nit — \(M_B\) uncertainty unsourced in offset calculation

The paragraph claims the offset is “\(\sim 3.2\sigma\) relative to the chain's \(\sigma_{M_B} = 0.049\) marginal width,” but the uncertainty \(\sigma_{M_B} = 0.049\) mag is not presented in any table or reproducibility file.  
**Fix:** Report the marginal \(M_B\) uncertainty together with the \(M_B\) posterior mean, as noted in PAPER-DEE-B1.

---

## PAPER-DEE-B6 — minor — NaMaster “pipeline-recovery bias” inconsistent presentation

The text first states “The bias is \(0.032^\circ\) (consistent with the apodized‑mask bias …)” and later acknowledges an amplitude‑dependent component (\(0.040^\circ\) for the \(0.342^\circ\) injection). The early phrasing suggests a single stable bias, which is contradicted after the comma.  
**Fix:** Clarify from the start that the bias shows mild amplitude dependence (e.g., “bias = 0.032°–0.040° across injection amplitudes”) to avoid a self‑contradiction.
