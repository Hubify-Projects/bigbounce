# P4_v1_0_113_R_INTERNAL R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1815pt
**Wall time**: 27.2s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=82000, completion=2112, reasoning=1207, total=84112

---

**## PAPER-GRO-B1**  
**BLOCKER** — Abstract, lines 1–80 (and repeated in §VII and Conclusions)  
The three-discriminator logic (ℓ=2>ℓ=1 broadband + p_eq quartile washout + cross-spectrum quadrupole anti-alignment) does not rigorously support the headline (ii) verdict. The cross-spectrum is measured on the canonical mask where the binomial null still yields +3.64σ (and ℓ=2 exceeds ℓ=1), while the p_eq washout is only shown on a different mask; the combination rules out a clean cosmological dipole but leaves an unresolved systematic excess rather than a clean null.  
**Fix:** State explicitly that the three discriminators exclude interpretation (i) on the canonical footprint but the load-bearing result remains the subsample-mask MASTER −0.12σ; move the canonical +1.85σ / +3.64σ numbers into a dedicated “unresolved systematic” subsection instead of folding them into the “rigorous support” claim.

**## PAPER-GRO-B2**  
**MAJOR** — Abstract (entire 1200+ word block) and §I  
Abstract remains a defensive log of every reviewer objection and internal patch (R17 GEM-B1, R18 GEM-B2, v1.0.106 bin-indexing, bootstrap scrubbing, etc.). It buries the actual result (null at ℓ=1 after leakage removal) under 800+ words of pre-emptive qualification.  
**Fix:** Reduce to ≤450 words: open with the quantified leakage channel and the post-MASTER −0.12σ null on the subsample mask, then one paragraph on the 0.75 % HC-subsample empirical threshold and the factor-of-~9 amplitude tension with Shamir; delete all meta-review language.

**## PAPER-GRO-B3**  
**MAJOR** — §IX.J (sensitivity) and abstract headline  
The claimed “50 %-recovery 3σ threshold |A|≈0.75 %” is measured only on the 471 k HC-spiral subsample; the full-catalog Fisher floor of 0.29 % is never demonstrated empirically. Comparing the two numbers produces a misleading “systematic degradation” narrative that the paper itself later retracts in a footnote.  
**Fix:** State plainly: “Empirical 50 %-recovery threshold is 0.75 % on the p_eq>0.9 subsample (N=471 k); no full-catalog injection sweep was performed. The 0.29 % figure is the ideal-statistical Poisson floor only.”

**## PAPER-GRO-B4**  
**MAJOR** — §VII (monopole-mask null) and Table VII  
The σ-reconciliation paragraph claims internal consistency after the v1.0.107 monopole correction, yet the null variance changes by a factor ~2.5 between the uncorrected and corrected pipelines. The text never states that the two scripts compute different observables (raw A_p vs. properly demonopole-subtracted A_p).  
**Fix:** Add one sentence: “The factor-2.5 null-variance ratio is expected: the residual monopole contributes ~2.5× the power that the demonopole-corrected field retains; both calculations are internally consistent under their respective input definitions.”

**## PAPER-GRO-B5**  
**minor** — Abstract and §VI (bootstrap claims)  
Despite the explicit scrubbing note, the text still describes the bootstrap result as “consistent with null” without the required tautological qualifier that the same bootstrap also returns median σ≈−0.49 on a real injected 1.7 % dipole.  
**Fix:** Change every bootstrap “consistent with null” phrase to “consistent with null under the bootstrap sampling-variance diagnostic (which is insensitive to a real dipole of this amplitude).”

**## PAPER-GRO-B6**  
**nit** — Title and abstract framing  
The title and opening paragraphs still imply a broad “no evidence for large-scale parity violation” result. The observable is strictly the parity-even axial-vector ℓ=1 dipole of a projected pseudoscalar field; the parity-odd monopole is reported separately as a 9.5σ systematic.  
**Fix:** Change title/abstract lead to “No Evidence for an Isotropy-Breaking Axial-Vector Chirality Dipole at |A|≳0.75 % …” and keep the parity-even/odd distinction in the first paragraph.
