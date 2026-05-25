# P2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-24_Rnext_P2_v1_7_37
**Wall time**: 238.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=31796, completion=6206, reasoning=5146, total=38002

---

## PAPER-DEE-B1 (BLOCKER)
**Section:** Abstract + Sec.-\ref{sec:systematics}  
**Line/Context:** “template‑corrected significance ${\sim}\,3{-}5\sigma$ after the combined systematic budget (noise‑weighted shape mismatch, $\epsilon$‑correction, polynomial‑coefficient null‑space amplitude scatter $\pm 0.13$ absolute in $r$ … photometric‑$z$ degradation, PNG bias, $b_\phi$ marginalization, and relativistic projection uncertainties)”  
**Issue:** The final headline sensitivity interval is a hand‑assembled combination of separate degradation estimates; no single script or unified calculation chain applies all factors jointly. The paper does not provide a JSON/script that produces the `3–5σ` number, nor does it specify the exact combination formula (multiplicative? root‑sum‑square? worst‑case envelope?).  
**Fix:** Write a script (e.g., `systematic_budget.py`) that takes the baseline $\sigma(\fnl)=0.7$, draws from the quoted uncertainty distributions for each systematic component, and outputs the full posterior of the detection significance. Quote the central value and a 68% or 90% interval from that distribution, and deposit the script and its output in the repository.

---

## PAPER-DEE-B3 (minor)
**Section:** Abstract + Sec.-\ref{sec:bayesian}  
**Line/Context:** “$\mathrm{BF}\,{\sim}\,10{-}17$” and the four‑corner Bayes‑factor grid (Table~\ref{tab:bayes}), values like `~10`, `~17`, `~4`.  
**Issue:** The numbers are derived from an analytic closed‑form Gaussian‑prior/uniform‑competitor formula; the formula is given, but no script that evaluates it for the specific prior widths and the observed $\fnl=-4.375$, $\sigma=0.7$ is referenced. The recent v1.7.35 scipy recalculation is mentioned only in the changelog, not linked to a rerunnable file.  
**Fix:** Add a short script `compute_bf_table.py` that implements the closed‑form formula for all four prior corners and prints the BF values to two decimal places, exactly as they appear in the table. Mention the script in the Data & Code section so that the rounding is verifiable.

---

## PAPER-DEE-B4 (minor)
**Section:** Abstract + Sec.-\ref{sec:template}  
**Line/Context:** “200 injection‑recovery realizations … $r_{\rm measured} = 0.90 \pm 0.01$”  
**Issue:** The text describes the estimator and noise model but does not state a fixed random seed or provide the exact simulation parameters that guarantee the reader will reproduce $0.90 \pm 0.01$. Without a reproducible run, the quoted mean and uncertainty are trust‑me numbers.  
**Fix:** In the repository script `03b_fast_mock_validation.py`, hardcode a fixed seed and record the output string containing `r_measured` and its uncertainty in a comment or a side‑car JSON, so that rerunning yields the identical interval.

---

## PAPER-DEE-B5 (nit)
**Section:** Abstract  
**Line/Context:** “Heinrich \etal~2024~\cite{Heinrich:2023}”  
**Issue:** The citation label uses `2023` but the text shows `2024`. This is likely a preprint‑year vs. publication‑year mismatch, but it creates uncertainty about which exact version of the Heinrich et al.\ forecast is used.  
**Fix:** Unify the year (use the officially published year, or the arXiv version tag) and adjust the bib key and in‑text callout to match.

---

## PAPER-DEE-B6 (minor)
**Section:** Sec.-\ref{sec:discussion}, Joint $(\fnl,\,n_{\fnl})$ Forecast  
**Line/Context:** “$\sigma(n_{\fnl}) = 0.086$ … $\sigma_{\rm marg}(\fnl) = 0.44$ … $\rho = 0.966$ … ${\sim}9.9\sigma$”  
**Issue:** The numbers originate from a six‑bin Fisher matrix whose explicit inputs ($k_{\min}(z)$, $\bar n(z)$, $b_1$, $b_\phi$ scheme, photometric‑$z$ scatter, survey volume) are “deferred to a companion artifact” and are not present in the paper or the linked repository. Consequently, the $9.9\sigma$ figure cannot be reproduced from the material supplied.  
**Fix:** Either (i) release the full Fisher‑input JSON/table in the repository alongside the paper and cite its location, or (ii) remove the quantitative $9.9\sigma$ and $0.086\sigma$ claims until the companion artifact is public, retaining only the qualitative degeneracy statement.
