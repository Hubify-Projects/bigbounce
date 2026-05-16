# P4_v1092 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0000pt_P4_v1092_R11_R-round_real
**Wall time**: 167.6s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=81396, completion=11296, reasoning=9586, total=92692

---

Here is the adversarial peer review of v1.0.92, focusing on theoretical physics, cosmology, and the R10 closure criteria. 

## PAPER-GEM-B1: Botched sentence splice conflates $\ell=1$ mode with $\ell_{\rm eff}=4$ bandpower
**Type:** BLOCKER
**Location:** Sec IV.C (Dipole), L866-871
**Issue:** A severe editing artifact has spliced the description of the $\ell_{\rm eff}=4$ bandpower into the numerical reporting of the $\ell=1$ single-mode result. The text reads: *"After deconvolution, the lowest bandpower (centered at $\ell_{\rm eff}=4$... [long parenthetical]) is $C_1^{\rm meas} = 1.494 \times 10^{-6}$"*. This equates the lowest bandpower to the $C_1$ mode, which is mathematically false (Table III shows $\ell_{\rm eff}=4$ is $3.210 \times 10^{-6}$) and destroys the readability of the paper's most critical headline result.
**Fix:** Separate the sentences. State the $\ell=1$ result cleanly, then describe the $\ell_{\rm eff}=4$ bandpower separately.

| Cite | Paper-says verbatim | Artifact-says verbatim | Verdict | Concrete Fix Proposal |
| :--- | :--- | :--- | :--- | :--- |
| L866 | "After deconvolution, the lowest bandpower (centered at $\ell_{\rm eff}=4$... [parenthetical]) is $C_1^{\rm meas} = 1.494 \times 10^{-6}$" | N/A | BLOCKER | "After deconvolution, the single-mode $\ell=1$ value is $C_1^{\rm meas} = 1.494 \times 10^{-6}$... The lowest bandpower (centered at $\ell_{\rm eff}=4$) is reported separately as a mode-coupling diagnostic." |

## PAPER-GEM-M1: Contradiction in Table III vs Text regarding $\ell \geq 2$ MC nulls
**Type:** MAJOR
**Location:** Table III caption vs Sec IV.C (L880-882)
**Issue:** The Table III caption states that Rows 2-5 (the $\ell \geq 2$ bandpowers) are derived from the *"canonical-N MASTER recompute... 500 MC realizations"*. However, the text in Sec IV.C explicitly claims: *"The $\ell \geq 2$ rows of Table III use the cheaper 1,000-MC raw pseudo-$C_\ell$ null because no mode-coupling inversion is required there"*. These cannot both be true. Either the bandpowers in Table III are MASTER-decoupled (500 MC) or they are raw pseudo-$C_\ell$ (1000 MC).
**Fix:** Reconcile the text and the caption to reflect the actual estimator and MC count used in `wave_14_pp_namaster_verification.json`.

| Cite | Paper-says verbatim | Artifact-says verbatim | Verdict | Concrete Fix Proposal |
| :--- | :--- | :--- | :--- | :--- |
| Table III / L880 | Caption: "Rows 2-5... MASTER recompute... 500 MC realizations" vs Text: "The $\ell \geq 2$ rows of Table III use the cheaper 1,000-MC raw pseudo-$C_\ell$ null" | N/A | MAJOR | Align Sec IV.C text with Table III caption to accurately reflect whether Rows 2-5 are MASTER-decoupled or raw pseudo-$C_\ell$. |

## PAPER-GEM-M2: "Machine precision" overclaim survives in real-space TTA description
**Type:** MAJOR
**Location:** Sec VI.A (L1365-1367)
**Issue:** The text claims: *"Equivariant averaging eliminates the real-space systematic by construction: the CW and CCW channels are exactly symmetrized, so any residual bias cancels to machine precision."* This is an overclaim that contradicts the paper's own findings of a $9.5\sigma$ residual monopole and a $21\%$ argmax flip rate. While the *soft probabilities* of a single flip-pair sum to exactly 1.0 by definition, the *residual bias* in the catalog does not cancel to machine precision.
**Fix:** Soften the claim to accurately reflect what is mathematically guaranteed.

| Cite | Paper-says verbatim | Artifact-says verbatim | Verdict | Concrete Fix Proposal |
| :--- | :--- | :--- | :--- | :--- |
| L1365 | "...so any residual bias cancels to machine precision." | N/A | MAJOR | "...so the horizontal-flip component of the orientation bias cancels exactly in the soft probabilities." |

## PAPER-GEM-m1: Missing null mean column in Table III
**Type:** minor
**Location:** Table III, footnote d
**Issue:** The footnote states: *"The null means are not displayed in this column-compact rendering... A dedicated null-mean column is queued for the next post-submission revision."* In an adversarial peer review, deferring critical baseline data (the null means) to a "post-submission revision" while explicitly acknowledging their absence is unacceptable, as it forces the reviewer/reader to reverse-engineer the $z$-scores.
**Fix:** Add the `<C_null>` column to Table III now.

| Cite | Paper-says verbatim | Artifact-says verbatim | Verdict | Concrete Fix Proposal |
| :--- | :--- | :--- | :--- | :--- |
| Table III | "A dedicated null-mean column is queued for the next post-submission revision." | N/A | minor | Insert the `<C_null>` column into Table III and remove the deferral footnote. |

## PAPER-GEM-m2: Grammatical error in Abstract LEE framing
**Type:** minor
**Location:** Abstract, L188-190
**Issue:** A sentence-editing collision resulted in broken grammar: *"puts the local effective significance drops to <1σ"*.
**Fix:** Fix the grammar.

| Cite | Paper-says verbatim | Artifact-says verbatim | Verdict | Concrete Fix Proposal |
| :--- | :--- | :--- | :--- | :--- |
| L188 | "...puts the local effective significance drops to <1σ..." | N/A | minor | "...reduces the local effective significance to <1σ..." |

## PAPER-GEM-n1: "Parity-violating dipole" terminology vs Sec VI.G physics
**Type:** nit
**Location:** Abstract (L129) vs Sec VI.G (L1845)
**Issue:** Sec VI.G contains a brilliant and theoretically rigorous deduction: the chirality dipole ($\ell=1$) is an axial vector and therefore *parity-even*. A non-zero dipole tests isotropy, not parity violation. The author notes they retain the phrase "parity-violating dipole" for continuity with Shamir's literature. However, using this phrase in the abstract without qualification risks confusing theoretical physicists who know a dipole of a pseudoscalar field doesn't violate parity.
**Fix:** Add a brief parenthetical in the abstract to signal theoretical rigor upfront.

| Cite | Paper-says verbatim | Artifact-says verbatim | Verdict | Concrete Fix Proposal |
| :--- | :--- | :--- | :--- | :--- |
| L129 | "...non-detection of a parity-violating dipole under the present..." | N/A | nit | "...non-detection of a parity-violating dipole (strictly, an isotropy-breaking axial vector) under the present..." |
