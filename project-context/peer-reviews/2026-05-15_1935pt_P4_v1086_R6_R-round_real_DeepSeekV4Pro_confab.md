# P4_v1086_R6 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1935pt
**Wall time**: 376.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=72940, completion=12439, reasoning=11613, total=85379

---

## PAPER-NUM-B1 — BLOCKER

**Location:** Abstract, lines describing the leakage channel and the pre-MASTER pseudo-\(C_\ell\) excursion (roughly “inflates the raw pseudo-\(C_\ell\) at \(\ell=1\) to \(+6.48\sigma\)unit on the canonical mask (un-monopole-subtracted CW-fraction map)”).

**Issue:** The abstract attributes the large \(+6.48\sigma\) pre-MASTER signal to monopole–mask leakage on the **un‑monopole‑subtracted CW‑fraction map**. However, the paper’s own monopole‑only generative null (Sec. III.F, Table V) computes the pre‑MASTER pseudo-\(C_\ell\) on exactly that map and finds a mere \(+1.68\sigma\) excess — a hundredfold smaller in σ‑space. The \(+6.48\sigma\) value actually comes from the **asymmetry map** \(A_p = (N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})\) (Sec. III.D), which has zero monopole by construction and whose pre‑MASTER boost is driven by partial‑sky mode coupling, not by monopole leakage. Conflating the two maps misrepresents both the magnitude and the physical origin of the leakage channel that the paper claims to demonstrate.

**Fix:** Rewrite the abstract so that the \(+6.48\sigma\) example is correctly identified as coming from the asymmetry map and is caused by mask‑induced mode coupling, while the monopole‑leakage demonstration is properly supported by the \(+1.68\sigma\) pre‑MASTER value from the CW‑fraction map. Adjust the description of the “full leakage‑removal chain” accordingly.

## PAPER-NUM-M1 — MAJOR

**Location:** Abstract, near “P(σ > 3)=0.50 at A=0.75%”.

**Issue:** The abstract states that the empirical injection‑recovery sweep gives \(P(\sigma>3)=0.50\) at injected full‑amplitude \(A=0.75\%\). The canonical extended‑sweep artifact (Table IX, `injection_recovery_extended.json`) reports \(P(\sigma>3)=0.55\) at \(A=0.75\%\). The quoted value is numerically wrong by \(0.05\); it misstates the probability at which the 50%‑recovery threshold is first crossed.

**Fix:** Replace “P(σ > 3)=0.50” with the correct table value “0.55” and, if needed, re‑state the threshold as “\(A\lesssim 0.75\%\)” or retain \(A\approx 0.75\%\) with the true \(P(\sigma>3)\).

## PAPER-NUM-B2 — BLOCKER

**Location:** Conclusions, “Sensitivity convention and remaining caveats” paragraph (after the canonical‑\(N\) MASTER discussion).

**Issue:** The paragraph asserts that “the present injection table … does not cross \(P(\sigma\!>\!3)\) at any tested amplitude”. This directly contradicts the same paper’s extended injection‑recovery sweep (Table IX), which shows \(P(\sigma>3)=0.55\) at \(A=0.75\%\), \(0.91\) at \(A=1.00\%\), and \(1.00\) at \(A\geq 1.50\%\). The statement is an outdated remnant of an earlier analysis and creates a severe internal inconsistency regarding the experiment’s sensitivity.

**Fix:** Replace the obsolete claim with the actual empirical threshold derived from the extended sweep, e.g., “The empirical 50%‑recovery‑at‑\(3\sigma\) threshold is \(A\approx 0.75\%\) …”.
