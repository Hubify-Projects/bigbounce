# P4_v1_0_113_R_INTERNAL R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1815pt
**Wall time**: 371.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=86397, completion=12003, reasoning=10942, total=98400

---

# Adversarial Peer Review — Findings (R19 INTERNAL on v1.0.113)

## PAPER-DEE-B1 (BLOCKER)
**Section:** Abstract (sensitivity claim and P4-EXT clarification paragraph)  
**Issue:** The headline empirical **50‑%‑recovery‑at‑3σ threshold of |A_dipole|≈0.75 % is repeatedly attributed to the N=471 049 (P>0.9) HC‑spiral subsample**, but the abstract’s own clarification concedes that the on‑disk injection‑recovery JSON (`injection_recovery_extended.json`) was actually run on the **broader p_eq>0.6 subsample (N=2 107 494)**. The 0.75 % number is therefore not a direct measurement on the claimed sample; the paper treats it as an “order‑of‑magnitude proxy” despite presenting it as the empirical sensitivity for that sample. This breaks the provenance chain of the paper’s primary sensitivity scalar.  
**Fix:** Either re‑run the injection sweep on the exact 471 049 P>0.9 sample and replace the artifact, or rewrite the abstract to report the threshold measured on the actual p_eq>0.6 sample and clearly mark the 471 049 comparison as an extrapolation, not a measurement.

## PAPER-DEE-B2 (MAJOR)
**Section:** Abstract (whole)  
**Issue:** The abstract remains **extremely long and defensive** (still >1200 words, dense with caveats, version‑history notes, and methodological justifications). It reads like a compressed rebuttal rather than a concise summary of the scientific result, and it is almost certain to violate journal word limits and obscure the key findings.  
**Fix:** Cut the abstract to ≤400 words, keeping only the core measurement (no detected dipole, quantified leakage channel, sensitivity floor) and one sentence of caveat; move all systematic‑forensics and reconciliation paragraphs to the main text.

## PAPER-DEE-B3 (minor)
**Section:** Abstract, line “the lowest pseudo‑Cℓ bandpower … reaches +6.48σ”  
**Issue:** The pre‑MASTER **+6.48σ excess** is a load‑bearing number for the leakage narrative, but the abstract gives **no direct pointer to the JSON artifact** that contains it. The paper body links it to `wave11c_nspiral_recompute_2026-05-01/results.json`; adding a footnote or compact artifact reference in the abstract would close the traceability gap for a number that is prominently used to motivate the MASTER correction.  
**Fix:** Insert a brief parenthetical artifact citation after “+6.48σ” (e.g., “(companion artifact …)”).

## PAPER-DEE-B4 (nit)
**Section:** Abstract, sentence beginning “The pre‑MASTER value and the post‑MASTER headline differ…”  
**Issue:** The sentence has a **grammatical error** (“differ” should be “differ” or “the pre‑MASTER signal and the post‑MASTER headline differ”; the current construction is garbled).  
**Fix:** Reword to “The pre‑MASTER and post‑MASTER values differ in mask, input‑map definition, monopole‑subtraction treatment, and MASTER inversion, so the full chain is …”

## PAPER-DEE-B5 (minor)
**Section:** Abstract, “9.5σ from 50/50” and Conclusions  
**Issue:** The **9.5σ monopole significance** is computed under naive binomial errors; the paper itself warns that the effective sample size \(N_{\rm eff}\) is smaller because of spatial correlations, so the true significance is lower. The abstract prints “9.5σ” as a precise number without the N_eff‑corrected value and without flagging it as an upper bound. This can mislead readers who do not parse the later fine print.  
**Fix:** Explicitly state “≥9.5σ under binomial assumptions (N_eff‑corrected significance smaller)” or quote the N_eff‑corrected value if known, so the abstract does not overstate the precision of the monopole detection.

## PAPER-DEE-B6 (minor)
**Section:** §VII (NaMaster appendix), σ‑reconciliation paragraph  
**Issue:** The arithmetic for the v1.0.107 corrected significance gives **specific numeric values (C1 = 1.51×10⁻⁵, null mean = 0.31×10⁻⁵, null std = 0.33×10⁻⁵)** that are not directly tied to a JSON artifact in that paragraph. The artifact `gpt5_b3_monopole_correction_audit.json` is mentioned earlier, but the link to these exact numbers is not repeated.  
**Fix:** Add a short reference to the artifact immediately after the displayed numbers (e.g., “(artifact …)”).
