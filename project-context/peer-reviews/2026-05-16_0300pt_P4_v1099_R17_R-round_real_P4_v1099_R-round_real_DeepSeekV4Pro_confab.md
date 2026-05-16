# P4_v1099 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0300pt_P4_v1099_R17_R-round_real
**Wall time**: 339.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=78933, completion=8091, reasoning=7546, total=87024

---

## Finding PAPER-DEE-M1
- **Classification**: MAJOR
- **Section**: §III F (Table~\ref{tab:bias_tests}), also referenced in Abstract and Conclusions
- **Issue**: The pass/fail results of the 8-test bias‑hardening suite (flip‑swap correlation 0.833, rotation stability 89.8%, etc.) are presented as a table, but **no JSON/script artifact is cited** that can reproduce these exact numbers. The bias audit is central to the paper’s claim of a quantified systematic check, yet its raw measurements are untraceable from the manuscript.
- **Fix**: Add a canonical‑provenance artifact (e.g.\ `bias_audit_results.json`) containing the per‑test metric, threshold, and pass/fail and cite it in the table caption.

## Finding PAPER-DEE-M2
- **Classification**: minor
- **Section**: Abstract (end of first paragraph: “the lowest pseudo‑$C_\ell$ bandpower … reaches $+6.48\sigmaunit$”) and §IV D
- **Issue**: The headline pre‑MASTER pseudo‑$C_\ell$ significance of $+6.48\sigma$ on the raw asymmetry map is stated without displaying the underlying data value, null mean, and null standard deviation anywhere in the paper. The arithmetic that produces the $z$‑score cannot be reproduced from displayed values. The companion artifact (`wave11c_nspiral_recompute`) is cited only in a footnote, not in the main text.
- **Fix**: Either extend Table~\ref{tab:multipole} to include a row for the pre‑MASTER Catalog‑A result with data, null mean, null $\sigma$, and $z$, or explicitly print those three numbers in the footnote/passage.

## Finding PAPER-DEE-M3
- **Classification**: minor
- **Section**: §III C (training) and Table~\ref{tab:confusion}
- **Issue**: The internal training‑set accuracy (93.7%) and post‑hoc validation accuracy (94.9%), along with the confusion matrix, are **not linked to a specific artifact** (e.g., a training log or evaluation JSON). While these are self‑consistency checks, the absence of a traceable output leaves the classifier’s internal performance unverifiable from the paper.
- **Fix**: Deposit the validation‑set evaluation output as a JSON artifact (or include it in an existing results file) and cite it in the caption of Table~\ref{tab:confusion}.
