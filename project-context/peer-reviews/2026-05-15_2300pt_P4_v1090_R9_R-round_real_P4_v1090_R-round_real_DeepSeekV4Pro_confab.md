# P4_v1090 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2300pt_P4_v1090_R9_R-round_real
**Wall time**: 544.1s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=76226, completion=13912, reasoning=12594, total=90138

---

# Adversarial Peer Review — Findings

## Finding PAPER-DEE-B1 (BLOCKER)
**Empirical detection threshold still cited as 0.5% in multiple locations, contradicting the injection‑recovery sweep that establishes 0.75% as the 50%‑recovery‑at‑3σ threshold.**

- **Where:**  
  *Abstract* (end of paragraph): “ … no scale or sky region yields a primordial‑dipole detection above the empirical sensitivity floor |A_dipole| > 0.5% ”.  
  *Section 10.2* (after Table III): “The empirical MC floor of ≥ 0.5% is the **detection threshold** under a strict per‑pixel‑shuffle null”.  
  *Conclusions*, item 1: “we achieve a **conservative empirical 50%‑recovery‑3σ threshold of ∼0.5% at 3σ** ”.

- **What the paper’s own artifact says:**  
  `/pipelines/p2_chirality/outputs/canonical_provenance/injection_recovery_extended.json` (Table IV) shows:  
  – at *A* = 0.5%, *P*(σ>3) = 0.15 (a non‑detection)  
  – at *A* = 0.75%, *P*(σ>3) = 0.55 (the **first** amplitude where the 50%‑recovery condition is met).  
  Therefore the empirical 50%‑recovery‑at‑3σ threshold is **0.75%**, not 0.5%.

- **Verdict:** **REGRESSION** — the closure noted in the round context required migration of all “0.5% floor” references to 0.75%; the above sites were not corrected and now directly contradict the abstract’s own earlier correct statement of the 0.75% threshold.

- **Fix:** Replace every occurrence of “0.5%” as the empirical detection‑threshold / floor / 50%‑recovery point with “0.75%” (the 9‑amplitude sweep’s 50%‑recovery‑at‑3σ amplitude). Also adjust the phrase “empirical sensitivity floor > 0.5%” to “empirical detection threshold of ≈ 0.75%”.

---

## Finding PAPER-DEE-M1 (MAJOR)
**Incorrect physics description: “polar‑vector direction” used for the parity‑even dipole in the symmetry‑classification paragraph.**

- **Line / location:** Section 7.8 (“Symmetry classification of the chirality dipole …”), the sentence  
  “A nonzero chirality dipole therefore strictly tests *isotropy* (the existence of a preferred **polar‑vector direction** on the sky)”.

- **Issue:** The chirality‑asymmetry field *A*(**n̂**) is a pseudoscalar; its spherical‑harmonic coefficients transform as *a*_{ℓ m} → (−1)^{ℓ+1} *a*_{ℓ m} under parity. For the dipole (ℓ = 1) this gives *a*_{1 m} → + *a*_{1 m}, i.e., a parity‑even vector — which is an **axial vector**, not a polar vector. Later in the same paragraph the text correctly states “the dipole vector itself is an axial vector, not a polar vector”. The earlier “polar‑vector direction” therefore contradicts the correct classification and undermines the careful parity‑diagnostic language the paper is trying to establish.

- **Verdict:** **NOVEL** — this site still carries the outdated “polar‑vector” wording that the round‑9 adversarial focus explicitly asked to check. It is a conceptual error, not a typo.

- **Fix:** Change to “the existence of a preferred **axial‑vector direction** on the sky” (or “preferred direction (an axial vector on the sky)”).

---

## Finding PAPER-DEE-Min1 (minor)
**Inconsistent pre‑MASTER C₁ value in the abstract: 1.70 × 10⁻² vs. 1.696 × 10⁻².**

- **Location:** Abstract, second mention of the monopole‑only null: “ … reproduces 99.3% of the observed pre‑MASTER C₁ power (observed C₁ = **1.70** × 10⁻²; null mean 1.68 × 10⁻² ± 0.07 × 10⁻³ )”. The earlier occurrence (and Table IV) gives the observed value as **1.696** × 10⁻².

- **Artifact:** The table and the provenance JSON (`monopole_mask_null_results.json`) contain 1.696 × 10⁻². The value 1.70 is a rounding that is not used elsewhere and creates an unnecessary numerical discrepancy.

- **Verdict:** minor inconsistency.

- **Fix:** Change “1.70 × 10⁻²” to “1.696 × 10⁻²” to match the canonical artifact.

---

## Additional Note
No blocker‑grade issues found for adversarial focus items (a), (d), (e), (f), (g), (h), (i), (j), (k) beyond the already‑noted regression on the 0.5 % threshold. All checked cited artifacts are consistent; the parity‑diagnostic distinction is mathematically clean in the current text; the Shamir language uses “inconsistent in amplitude … under the present pipeline” without claiming formal exclusion; and the Table I/Table III cross‑references are accurate.
