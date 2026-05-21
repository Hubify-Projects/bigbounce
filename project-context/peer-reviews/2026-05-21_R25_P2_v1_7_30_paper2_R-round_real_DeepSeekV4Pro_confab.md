# paper2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P2_v1_7_30
**Wall time**: 271.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=29361, completion=7872, reasoning=6815, total=37233

---

# Adversarial Peer Review — Provenance of Load-Bearing Scalars

## PAPER-DEE-B1 (BLOCKER)  
**Section:** §8.2 (“Current Data and Consistency Relation”) and §2.1 / abstract references to the $\kappa_1$ bounds.  
**Issue:** The $\mathcal{O}(\epsilon)$ correction to $\fnl=-35/8$ hinges on the coefficient $\kappa_1$, stated to lie between $5.6$ (lower) and $80$ (upper).  
These two numbers determine the $1$–$8\%$ uncertainty envelope and the range $\fnl\in[-4.35,-4.02]$, both repeatedly quoted as central forecasts. No derivation, script, or external reference is given for $5.6$ and $80$; they appear unsupported assertions.  
**Fix:** Either provide a closed-form expression or a script that computes $\kappa_1$ from the mode-function integrals and the cubic-action prefactors, or replace the numeric bounds with an explicit derivation tied to an identifiable file on disk.

## PAPER-DEE-B2 (BLOCKER)  
**Section:** §8.4 (“Joint $(\fnl,\, n_{\fnl})$ Forecast …”)  
**Issue:** The discussion states an idealized Fisher significance of ${\sim}9.9\sigma$, derived from $\sigma_{\rm marg}(\fnl)=0.44$ and $\sigma(n_{\fnl})=0.086$, and explicitly notes that the full six-bin Fisher-input release is *deferred to a companion artifact*. These numbers are therefore not reproducible from the current repository or any dataset referenced in the paper, violating the paper’s own code‑availability claim for a load‑bearing quantitative result.  
**Fix:** Remove the $9.9\sigma$, $0.44$, and $0.086$ figures from the manuscript until the companion Fisher inputs are publicly available and linked; or include the Fisher matrix as a supplementary file and regenerate the numbers from an in‑repo script.

## PAPER-DEE-M1 (MAJOR)  
**Section:** Abstract and §7 (“Systematics and Robustness”) — the headline $3$–$5\sigma$ post‑systematic significance.  
**Issue:** The detection significance $3$–$5\sigma$ is presented as a final envelope combining template mismatch, $\epsilon$-correction, GR marginalisation, $b_\phi$ uncertainty, photo‑$z$ degradation, and other effects. No single script or dataset performs this joint combination; the paper hand‑assembles the range from separate sensitivity plots without a traceable aggregation point. A reader cannot reproduce the $3$–$5\sigma$ number from any single file on disk.  
**Fix:** Provide a monolithic systematics‑budget script (e.g., `systematics_budget.py`) that reads all degradation factors and outputs the final significance, and reference its filename and output clearly.

## PAPER-DEE-m1 (minor)  
**Section:** §3.2 (“Template Projection and Amplitude Recovery”) — the canonical noise‑weighted overlap $r=0.84\pm0.02$.  
**Issue:** The text explains the 10 weighting schemes and states the result, but does not link to a specific JSON/script that produces this number (unlike the `phase3_fisher_overlap.json` mentioned for a related quantity). A reviewer would have to guess which file in the repository holds the computation.  
**Fix:** Add a sentence naming the script (e.g., `template_overlap_scan.py`) and the output file (e.g., `noise_weighted_overlap.json`) that directly yields $0.84\pm0.02$.

## PAPER-DEE-m2 (minor)  
**Section:** §2.1 — the $\fnl$ correction range $[-4.35,-4.02]$ and the associated $1$–$8\%$ uncertainty.  
**Issue:** These numbers are arithmetically derived from the $\kappa_1$ bounds flagged in B1. Even if the $\kappa_1$ bounds were supported, the derived range is not output by a named script; the text offers only the final values.  
**Fix:** Provide a short script (or a single Pandas/JSON table) that takes the $\kappa_1$ sweep, $n_s=0.9649$, and the formula, and outputs the $\fnl$ range. Reference it explicitly.

## PAPER-DEE-n1 (nit)  
**Section:** §3.2 — the injection‑recovery result $r_{\rm meas}=0.90\pm0.01$.  
**Issue:** The script `03b_fast_mock_validation.py` is mentioned in the abstract, but the paper does not state the exact output filename or location where this number is stored, making a quick provenance check needlessly indirect.  
**Fix:** Append “(see `results/injection_recovery_r.json`)” or similar to the sentence so that the value can be traced to a single file.
