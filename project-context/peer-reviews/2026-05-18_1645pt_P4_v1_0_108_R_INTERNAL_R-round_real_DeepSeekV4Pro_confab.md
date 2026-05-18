# P4_v1_0_108_R_INTERNAL R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1645pt
**Wall time**: 186.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=83695, completion=15363, reasoning=13994, total=99058

---

# Adversarial Peer Review — P4 v1.0.108 Multi-Null Battery & Provenance Audit

## PAPER-DEE-B1 (BLOCKER) — Injection-recovery subsample size is inconsistent across abstract, body, and artifact; Fisher-floor comparison is contradictory

**Location:** Abstract (lines ~50–80, and the later “P4-EXT ChatGPT-B3” clarification paragraph), §IX.J (Sensitivity Floor), and the artifact `injection_recovery_extended.json`.

**Issue:**  
The abstract first states: “the empirical 50%-recovery-at-3σ threshold of |A_dipole|≈0.75% on the N=471,049 HC-spiral subsample … tracks the HC-subsample shot-noise budget … ratio ≈1.0”. Later, the abstract’s own clarification says the released JSON was run on the broader p_eq>0.6 HC-spiral subsample (N=2,107,494), not the P>0.9 subsample, and that the empirical 0.75% exceeds the p_eq>0.6 Fisher floor by a factor of ~2. The paper body (§IX.J) still describes the injection sweep as using the 471k subsample. The artifact’s manifest confirms the p_eq>0.6 sample. This means:

- The central sensitivity number (0.75%) is attributed to the wrong sample in the main narrative.
- The “ratio ≈1.0, no systematic-inclusive degradation” claim is based on the wrong N and is directly contradicted by the later clarification.
- The body and abstract are not self-consistent; a reader cannot tell which sample was actually used without decoding the meta-commentary.

**Fix:**  
Correct the abstract and §IX.J to state that the injection-recovery sweep was performed on the p_eq>0.6 HC-spiral subsample (N=2,107,494). Remove the initial claim that it used the 471k sample. Recompute the like-for-like Fisher comparison using N=2,107,494 (Fisher floor ≈0.36%) and report the empirical/Fisher ratio as ~2, consistent with systematic-inclusive degradation. Update the conclusions accordingly.

---

## PAPER-DEE-M1 (MAJOR) — Conclusions do not reflect the multi-null battery’s bootstrap-null result; framing is slightly misaligned with the abstract

**Location:** §VII (Conclusions) vs. Abstract and §IV.D multi-null paragraph.

**Issue:**  
The abstract now declares “bootstrap-null collapse to -0.22σ is the canonical honest result” and the multi-null battery concludes that the canonical-mask residual is null under the bootstrap null. However, the Conclusions section still anchors entirely on the subsample-mask -0.12σ and the canonical-mask direct-MC +1.85σ, without mentioning the bootstrap null or the multi-null battery. While not contradictory, this omission weakens the paper’s internal consistency: the abstract’s strong “canonical honest result” language is not echoed in the formal conclusions, leaving the reader uncertain which null is the definitive one.

**Fix:**  
Add a sentence to the Conclusions summarizing the multi-null battery outcome: the canonical-mask residual is consistent with null under a spatial-correlation-preserving bootstrap null (σ = -0.22), and the binomial-shuffle excess is attributed to per-pixel correlated systematics. This aligns the conclusions with the abstract’s updated framing.

---

## PAPER-DEE-M2 (MAJOR) — Bootstrap null procedure is underspecified; reproducibility of the -0.22σ figure is not fully assured from the paper text alone

**Location:** §IV.D multi-null battery paragraph (“bootstrap pixel resample … gives σ=-0.22”).

**Issue:**  
The paper states: “bootstrap pixel resample (preserves spatial correlations of the data: each pixel's CW/CCW chirality contribution is sampled with replacement) gives σ=-0.22”. It does not specify:

- The number of bootstrap resamples.
- Whether the resampling is performed on the pixel-level CW/CCW counts or on the asymmetry map directly.
- How the dipole significance σ is computed from the bootstrap distribution (e.g., z-score of the observed dipole relative to the bootstrap mean and standard deviation).

The companion artifact `p4_multinull_battery.json` presumably contains these details, but the paper must provide enough information for a reader to understand the procedure without inspecting the JSON. The -0.22σ is a load-bearing number in the abstract; its derivation must be transparent.

**Fix:**  
Add a brief description: e.g., “We draw 10,000 bootstrap samples by resampling HEALPix pixels with replacement, recompute the dipole amplitude for each sample, and quote the z-score of the observed amplitude relative to the bootstrap distribution.” Cite the artifact for the exact parameter values.

---

## PAPER-DEE-m1 (minor) — Abstract contains meta-commentary (“P4-EXT ChatGPT-B3 …”) that is inappropriate for a journal abstract

**Location:** Abstract, final paragraph before the “Scope of the null claim” note.

**Issue:**  
The abstract includes a long, self-referential clarification about an external review finding, complete with artifact paths and internal version tags. This is not standard for a published abstract and distracts from the scientific message. The information is important for provenance but belongs in a footnote, an appendix, or the data-availability section.

**Fix:**  
Move the injection-subsample-predicate clarification to a footnote on the first mention of the 0.75% threshold, or to §IX.J. Keep the abstract focused on the scientific result.

---

## PAPER-DEE-m2 (minor) — The “canonical honest result” phrasing is informal and could be misinterpreted

**Location:** Abstract (“bootstrap-null collapse to -0.22σ is the canonical honest result”).

**Issue:**  
The phrase “canonical honest result” is colloquial and may confuse readers who expect a formal statement of the primary result. The paper’s primary result remains the subsample-mask -0.12σ; the bootstrap null is a diagnostic that supports the null interpretation of the canonical-mask excess. The wording could be read as elevating the bootstrap null above the primary estimator.

**Fix:**  
Rephrase to: “Under a spatial-correlation-preserving bootstrap null, the canonical-mask residual collapses to -0.22σ, confirming it is not a detection. The load-bearing null remains the subsample-mask post-MASTER -0.12σ.”

---

## PAPER-DEE-n1 (nit) — Abstract’s pre-MASTER/post-MASTER chain description is verbose but not incorrect

**Location:** Abstract, lines describing the mode-coupling-removal chain.

**Issue:**  
The abstract states: “the pre-MASTER value and the post-MASTER headline differ in mask, in input-map definition, in monopole-subtraction treatment, and in MASTER mode-coupling inversion, so the full mode-coupling-removal chain is (map choice + monopole-subtraction + mask choice + MASTER), not pure MASTER on identical inputs.” This is accurate but could be condensed. It does not affect scientific correctness.

**Fix:**  
No action required, but consider shortening for readability.
