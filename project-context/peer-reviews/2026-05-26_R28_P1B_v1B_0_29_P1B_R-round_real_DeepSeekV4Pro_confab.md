# P1B R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R28_P1B_v1B_0_29
**Wall time**: 214.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=23277, completion=8896, reasoning=7743, total=32173

---

## PAPER-DEE-B1 (MAJOR) — Abstract L47–50: SNR=20.32 (and body eq.~1 SNR=20.32, SNR=25.71) reported without standard deviation on recovered $\hat\beta$

The abstract headlines `SNR=20.32` and the body gives `pipeline-recovery SNR=20.32` (for $\hat\beta=0.238^\circ$) and `SNR=25.71` (for $\hat\beta=0.302^\circ$), but nowhere is the associated precision $\sigma_{\hat\beta}$ stated. A reader cannot reproduce these SNR values from displayed numbers because SNR $\equiv \hat\beta/\sigma_{\hat\beta}$ (or similar) is undetermined when $\sigma_{\hat\beta}$ is absent.  
**Fix:** Add the per‑injection $\hat\beta \pm \sigma_{\hat\beta}$ or report $\sigma_{\hat\beta}$ explicitly so the claimed SNR is traceable to the pipeline output.

---

## PAPER-DEE-B2 (minor) — §VI L??? (ALP birefringence): the factor “$1.07$” in $\beta\approx(\alpha_{\rm EM}\times 8)/(4\pi)\times 1.07\approx 0.29^\circ$ appears with no derivation

The text says “For $C_{a\gamma}=8$, $\theta_i=1$, $m\approx 2H_0$: $\beta\approx …\times 1.07$”. It is not stated where the $1.07$ comes from (presumably $\Delta\phi/f_a$ for that mass choice, but earlier only a range $[0.2,1.1]$ and a single value $0.65$ for $m=H_0$ are given). The number is unreproducible without definition.  
**Fix:** Define the $1.07$ as the integrated field displacement for $m\approx 2H_0$ or replace it with an explicitly stated $\Delta\phi/f_a$ value.

---

## PAPER-DEE-B3 (minor) — Table \texttt{tab:crosspaper}: P1(b) readiness stuck at 67\% and version v1B.0.13, but the paper is at v1B.0.29

The cross‑paper status table still shows Paper 1(b) at version v1B.0.13 and 67 % readiness. Extensively updated readiness percentages (and the version) are now load‑bearing provenance for the “verification companion” framing, yet they are stale.  
**Fix:** Update the table row to reflect the current version and readiness (e.g., based on the closed audit‑cascade state).

---

## PAPER-DEE-B4 (minor) — §VI L??? (NaMaster bias): the claim that the $0.032^\circ$ bias is “consistent with the apodized‑mask bias expected from a $2^\circ$ apodization scale” lacks a reference or quantitative expectation

The statement appears without a supporting citation, calculation, or calibration curve that maps apodization scale to expected $E\to B$ leakage bias. This makes the “consistency” claim an unreproducible assertion.  
**Fix:** Either provide a reference (e.g., NaMaster validation study, internal calibration run) or remove the qualitative “consistent with” and rephrase as an empirical measurement only.

---

## PAPER-DEE-B5 (nit) — Footnote \texttt{fn:sample\_stratification}: post‑burnin count arithmetic uses hard‑coded 30 % burn‑in but the actual chain‑header burn‑in fraction is not shown

The footnote computes $176{,}240\times0.7 = 123{,}368$ and $132{,}949\times0.7 \approx 93{,}064$ assuming a uniform 30 % burn‑in. The actual burn‑in fraction may differ per chain, and the text asserts a “chain‑end‑truncation of partial samples” that could shift the numbers by a few samples. The footnote does not point to a file where the precise post‑burnin count is recorded.  
**Fix:** Replace the rounded multiplication with a direct readout from the chain manifest or convergence summary JSON (e.g., “post‑burnin samples according to \texttt{convergence\_summary.json}: $123{,}368$ (full‑tension), $93{,}064$ (Planck+BAO+SN)”).

---

## PAPER-DEE-B6 (nit) — §VI L??? (auxiliary $\beta$ combination): the combined value $0.241\pm0.061$ is presented as an inverse‑variance weighted mean, but the explicit weights are not displayed, and the $3.9\sigma$ significance is not broken down

A careful reader can reverse‑engineer the weights from the published $\pm$ numbers, but the text does not show the arithmetic (weights, $\chi^2$ of combination, test for consistency). The paper’s own defense is that this is an auxiliary cross‑check, yet it is still a numerical claim in the body.  
**Fix:** Add a one‑line derivation (or reference to a repository script) that shows the inverse‑variance weights and the $\chi^2$ test, or state that the combination is provided in \texttt{aux\_combination.py} at a specific path.
