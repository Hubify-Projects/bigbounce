# P1B_v1B012_R7 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1100pt
**Wall time**: 192.1s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=13319, completion=9913, reasoning=8582, total=23232

---

## PAPER-DEE-B1 (BLOCKER) — NaMaster SNR figures lack provenance

**Location:** Abstract (line “SNR$=20.32$”) and Section 4 (Eq.~\eqref{eq:beta_namaster} and surrounding text).

**Issue:** The pipeline-recovery SNR values (20.32 for $\beta=0.27^\circ$, 25.71 for $\beta=0.342^\circ$) are reported without the standard deviation of the recovered $\hat\beta$ from the 500 Monte Carlo realizations. The SNR cannot be reproduced from the displayed numbers ($\hat\beta$ and bias alone); no definition of SNR is given, and no uncertainty on $\hat\beta$ appears anywhere in the paper. These are headline figures in the abstract and conclusions.

**Fix:** Report the MC standard deviation $\sigma_{\hat\beta}$ for each injection (e.g., $\hat\beta = 0.238^\circ \pm 0.0117^\circ$ for the $\beta=0.27^\circ$ case) and define SNR explicitly as $\hat\beta/\sigma_{\hat\beta}$. Alternatively, state the SNR formula and provide the noise level used.

---

## PAPER-DEE-B2 (BLOCKER) — Incorrect citation year for joint Planck+ACT birefringence

**Location:** Abstract, Section 6, and Conclusions; reference `Eskilt2022b` cited for $\beta = 0.342^\circ\pm 0.094^\circ$ ($3.6\sigma$).

**Issue:** The joint Planck+ACT cosmic birefringence analysis was published in 2023 (Eskilt et al. 2023, A&A), not 2022. The paper uses the key `Eskilt2022b`, which either points to a non-existent entry or the wrong year. The $3.6\sigma$ significance is a load-bearing observational anchor; a wrong citation undermines traceability.

**Fix:** Replace `Eskilt2022b` with the correct 2023 reference (e.g., `Eskilt2023`) and ensure the bibliography entry matches the published paper.

---

## PAPER-DEE-B3 (MAJOR) — Cross-paper status table version mismatch

**Location:** Table~\ref{tab:crosspaper} (Cross-paper status table), row “P1(b)”.

**Issue:** The table lists the version of this companion paper as `v1B.0.11`, but the document’s `\paperVersion` macro and title page declare `v1B.0.12`. This inconsistency breaks the version-tracking chain that the table is meant to document.

**Fix:** Update the table row to `v1B.0.12` (and adjust the readiness/blocker text if needed) so that the cross-paper status reflects the actual submitted version.

---

## PAPER-DEE-B4 (MAJOR) — Provenance of $\beta_{\rm free}$ is insufficient

**Location:** Section 6, paragraph “MCMC parameter estimation”.

**Issue:** The value $\beta_{\rm free} = 0.344^\circ\pm 0.096^\circ$ is attributed to “our internal model-independent MCMC fit … 9,720 accepted samples across the 3 configurations described in Sec.~\ref{sec:birefringence_check}”, but Section 6 does not describe three distinct configurations for a free-$\beta$ fit. The same sample count (9,720) is also given for the ALP MCMC with $C_{a\gamma}=8$ fixed, making it unclear whether $\beta_{\rm free}$ comes from a separate analysis or is a subset of the same chains. The number is used as a consistency cross-check; its reproducibility is not established.

**Fix:** Either (a) explicitly describe the three configurations used for the $\beta_{\rm free}$ fit (likelihoods, priors, how they differ) and confirm that the 9,720 samples are distinct from the ALP-MCMC chains, or (b) provide a script/notebook reference that produces $\beta_{\rm free}$ from the frozen chains.

---

## PAPER-DEE-B5 (minor) — Counterintuitive $H_0$ shift under SH0ES prior

**Location:** Table~\ref{tab:verification} and Section 2.

**Issue:** The full-tension combination (which includes the SH0ES $H_0$ prior) yields $H_0 = 67.68\pm 1.06$, while the Planck+BAO+SN combination (without SH0ES) gives $67.79\pm 1.09$. Adding a prior that favours $H_0 \approx 73$ would be expected to increase the posterior mean, yet the reported value decreases by $0.11$ (a $0.1\sigma$ shift). The paper’s qualitative statement that Planck dominates does not explain the direction of the shift; a simple Gaussian update from the Planck+BAO+SN posterior and the SH0ES prior would give $\sim 70.6$, not $67.68$. This may indicate a non-Gaussian likelihood or a chain issue, but no quantitative check is provided.

**Fix:** Add a brief note quantifying the expected shift under a Gaussian approximation, or confirm that the full-tension chain correctly samples the SH0ES prior and that the posterior is not affected by a chain artifact. (Not a math error per se, but a transparency concern.)

---

## PAPER-DEE-B6 (nit) — Abstract sample-count phrasing could mislead

**Location:** Abstract, first sentence of item (1).

**Issue:** The abstract states “$\mathbf{309{,}789}$ frozen samples across two converged dataset combinations, plus a third Planck-only combination ongoing”. The third combination is not frozen, so the headline number correctly excludes it. However, the phrase “plus a third … ongoing” immediately after the bold number could be misread as the total including the third. The body of the paper clarifies this, but the abstract is the most visible summary.

**Fix:** Rephrase to “$\mathbf{309{,}789}$ frozen samples across two converged dataset combinations (a third, Planck-only combination with $114{,}992$ raw samples is still accumulating and is not included in the frozen headline)”.
